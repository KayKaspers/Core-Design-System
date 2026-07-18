"""Layered V1–V4 validation engine for the CDS offline token validator.

Implements the Machine-Readable Validation Contract (DEC-S-078, DEC-S-097):

- V1 — syntax and file contract (UTF-8, strict JSON, duplicate keys, file
  identity, pointer/$ref syntax, no network references, no path escape);
- V2 — the bounded DTCG 2025.10 subset required by the CDS profile and the
  committed fixtures (DEC-S-098) — never full DTCG conformance;
- V3 — the CDS profile contract (schemas, extension payload, identity,
  manifest/resolver binding, declared cross-file boundary);
- V4 — the objectively machine-checkable semantic/governance subset; the
  rest stays "Not assessed" with a rationale.

A Fail or Blocked layer stops later layers ("Not assessed"). No aggregate
score exists. Synthetic test-only fixtures yield V4 "Not applicable with
rationale" — they carry no real semantics or governance (DEC-S-087).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from tools.cds_validator import diagnostics as diag
from tools.cds_validator import json_loader
from tools.cds_validator import semantic_status
from tools.cds_validator.graph import ManifestGraph, check_resolver_order
from tools.cds_validator.models import (
    CDS_EXTENSION_ROOT,
    EXTENSION_KINDS,
    LAYER_ORDER,
    Diagnostic,
    DocumentKind,
    Layer,
    ResultState,
    ValidationOutcome,
    aggregate_states,
)
from tools.cds_validator.schema_registry import SchemaRegistry

#: Token $type values defined by the pinned DTCG 2025.10 reports (Format and
#: Color modules) within the bounded validator scope (DEC-S-074, DEC-S-098).
#: Any other $type is treated as an unapproved preview/draft feature.
KNOWN_DTCG_TYPES = frozenset({
    "color", "dimension", "duration", "cubicBezier", "number", "string",
    "boolean", "fontFamily", "fontWeight", "strokeStyle", "border",
    "transition", "shadow", "gradient", "typography",
})

RESERVED_MEMBERS = frozenset({"$value", "$type", "$description", "$deprecated", "$extensions"})
NAME_SEGMENT_RE = re.compile(r"^[a-z][a-z0-9-]*$")
ALIAS_RE = re.compile(r"^\{([^{}]+)\}$")
JSON_POINTER_RE = re.compile(r"^(?:/(?:[^/~]|~0|~1)*)*$")
NETWORK_RE = re.compile(r"^(https?:|file:|//)|\\")
#: Object members whose string values are local-reference paths.
PATH_FIELDS = frozenset({"$ref", "path", "manifestRef"})


@dataclass
class ScopeDocument:
    """One loaded document inside a validation scope."""

    path: Path
    kind: DocumentKind
    v1: ResultState
    content: Any | None = None
    diagnostics: list[Diagnostic] = field(default_factory=list)

    @property
    def payload(self) -> dict | None:
        if not isinstance(self.content, dict):
            return None
        extensions = self.content.get("$extensions")
        if isinstance(extensions, dict):
            payload = extensions.get(CDS_EXTENSION_ROOT)
            if isinstance(payload, dict):
                return payload
        return None

    @property
    def is_fixture(self) -> bool:
        source = self.payload if self.kind is DocumentKind.TOKEN_DOCUMENT else (
            self.content if isinstance(self.content, dict) else None)
        if not isinstance(source, dict):
            return False
        return source.get("testOnly") is True and source.get("nonNormative") is True


@dataclass
class ScopeResult:
    documents: list[ScopeDocument]
    outcome: ValidationOutcome


class ValidationEngine:
    """Validates a scope (one or more documents) through V1–V4."""

    def __init__(self, repository_root: Path | str, registry: SchemaRegistry):
        self.repository_root = Path(repository_root).resolve()
        self.registry = registry

    # ------------------------------------------------------------------ V1

    def run_v1(self, path: Path) -> ScopeDocument:
        source = str(path)
        suffix = _document_suffix(path)
        kind = EXTENSION_KINDS.get(suffix, DocumentKind.UNKNOWN)
        doc = ScopeDocument(path=path, kind=kind, v1=ResultState.PASS)

        if kind is DocumentKind.UNKNOWN:
            doc.diagnostics.append(diag.make(
                "CDS-V1-FILE-EXTENSION",
                f"File extension {suffix or path.suffix!r} is not a CDS document "
                "identity (.tokens.json / .source-set.json / .resolver.json)",
                source))
            doc.v1 = ResultState.FAIL

        try:
            doc.content = json_loader.load_path(path)
        except json_loader.DuplicateKeyError as exc:
            doc.diagnostics.append(diag.make(
                "CDS-V1-DUPLICATE-KEY", str(exc), source, json_pointer=exc.json_pointer))
            doc.v1 = ResultState.FAIL
            return doc
        except json_loader.LoaderError as exc:
            doc.diagnostics.append(diag.make("CDS-V1-JSON-PARSE", str(exc), source))
            doc.v1 = ResultState.FAIL
            return doc

        self._v1_scan(doc.content, doc, "")
        if any(d.layer == "V1" and d.severity == "error" for d in doc.diagnostics):
            doc.v1 = ResultState.FAIL
        return doc

    def _v1_scan(self, node: Any, doc: ScopeDocument, pointer: str) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                child = f"{pointer}/{_escape(key)}"
                if key == "pointer" and isinstance(value, str):
                    if not JSON_POINTER_RE.match(value):
                        doc.diagnostics.append(diag.make(
                            "CDS-V1-POINTER-SYNTAX",
                            f"Invalid RFC 6901 JSON Pointer: {value!r}",
                            str(doc.path), json_pointer=child))
                if key in PATH_FIELDS and isinstance(value, str):
                    self._v1_check_local_path(value, doc, child)
                if key == "resolverDocuments" and isinstance(value, list):
                    for index, item in enumerate(value):
                        if isinstance(item, str):
                            self._v1_check_local_path(item, doc, f"{child}/{index}")
                self._v1_scan(value, doc, child)
        elif isinstance(node, list):
            for index, item in enumerate(node):
                self._v1_scan(item, doc, f"{pointer}/{index}")

    def _v1_check_local_path(self, value: str, doc: ScopeDocument, pointer: str) -> None:
        if NETWORK_RE.search(value):
            doc.diagnostics.append(diag.make(
                "CDS-V1-NETWORK-REFERENCE",
                f"Forbidden network/UNC/backslash reference: {value!r}",
                str(doc.path), json_pointer=pointer))
            return
        try:
            resolved = (doc.path.parent / value).resolve()
        except OSError:
            return
        if not resolved.is_relative_to(self.repository_root):
            doc.diagnostics.append(diag.make(
                "CDS-V1-PATH-ESCAPE",
                f"Local reference escapes the repository root: {value!r}",
                str(doc.path), json_pointer=pointer))

    # ------------------------------------------------------------------ V2

    def run_v2(self, documents: list[ScopeDocument], index: dict[str, dict],
               groups: set[str]) -> dict[int, ResultState]:
        """Scope-level V2. Returns per-document states; appends diagnostics."""
        states: dict[int, ResultState] = {}
        scope_edges: dict[str, str] = {}
        marks: dict[int, int] = {}
        for position, doc in enumerate(documents):
            if doc.kind is DocumentKind.SOURCE_SET_MANIFEST:
                states[position] = ResultState.NOT_APPLICABLE
                continue
            marks[position] = len(doc.diagnostics)
            if doc.kind is DocumentKind.TOKEN_DOCUMENT:
                self._v2_token_document(doc, index, groups, scope_edges)
            elif doc.kind is DocumentKind.RESOLVER_DOCUMENT:
                self._v2_resolver_document(doc)
        # Reference cycles span documents: detect over the scope-wide edge set
        # and report on the document owning the first cycle participant.
        _detect_alias_cycles(scope_edges, index)
        for position, doc in enumerate(documents):
            if position not in marks:
                continue
            failed = any(
                d.layer == "V2" and d.severity == "error"
                for d in doc.diagnostics[marks[position]:])
            states[position] = ResultState.FAIL if failed else ResultState.PASS
        return states

    def _v2_token_document(self, doc: ScopeDocument, index: dict[str, dict],
                           groups: set[str], scope_edges: dict[str, str]) -> None:
        source = str(doc.path)
        if not isinstance(doc.content, dict):
            doc.diagnostics.append(diag.make(
                "CDS-V2-DTCG-STRUCTURE", "Token document root must be a JSON object",
                source))
            return
        for token_path, info in index.items():
            if info["doc"] is not doc:
                continue
            pointer = info["pointer"]
            token_type = info["type"]
            if token_type is None:
                doc.diagnostics.append(diag.make(
                    "CDS-V2-DTCG-STRUCTURE",
                    f"Token {token_path!r} has no own or inherited $type",
                    source, json_pointer=pointer))
            elif token_type not in KNOWN_DTCG_TYPES:
                doc.diagnostics.append(diag.make(
                    "CDS-V2-PREVIEW-FEATURE",
                    f"Token $type {token_type!r} is not defined by the pinned DTCG "
                    "2025.10 reports; treated as an unapproved preview/draft feature "
                    "(DEC-S-074)",
                    source, json_pointer=pointer))
            value = info["value"]
            if isinstance(value, str) and value.startswith("{"):
                match = ALIAS_RE.match(value)
                if not match:
                    doc.diagnostics.append(diag.make(
                        "CDS-V2-DTCG-STRUCTURE",
                        f"Malformed token alias: {value!r}", source, json_pointer=pointer))
                    continue
                alias_path = match.group(1)
                segments = alias_path.split(".")
                if not all(NAME_SEGMENT_RE.match(s) for s in segments):
                    doc.diagnostics.append(diag.make(
                        "CDS-V2-DTCG-STRUCTURE",
                        f"Alias path violates the naming profile: {alias_path!r}",
                        source, json_pointer=pointer))
                    continue
                if alias_path in index:
                    scope_edges[token_path] = alias_path
                    target = index[alias_path]
                    if (token_type and target["type"]
                            and token_type != target["type"]):
                        doc.diagnostics.append(diag.make(
                            "CDS-V2-DTCG-REFERENCE",
                            f"Type mismatch: {token_path!r} ({token_type}) references "
                            f"{alias_path!r} ({target['type']})",
                            source, json_pointer=pointer, category="type-mismatch"))
                elif segments[0] in groups:
                    doc.diagnostics.append(diag.make(
                        "CDS-V2-DTCG-REFERENCE",
                        f"Dangling reference: {{{alias_path}}} has no target token",
                        source, json_pointer=pointer, category="dangling-reference"))
                else:
                    # Root group unknown in this scope: a cross-file candidate.
                    # Deferred to the V3 declared-graph boundary (DEC-S-091).
                    info["deferred"] = alias_path

    def _v2_resolver_document(self, doc: ScopeDocument) -> None:
        source = str(doc.path)
        content = doc.content
        if not isinstance(content, dict) or not isinstance(
                content.get("orderedSourceSets"), list) or not content["orderedSourceSets"]:
            doc.diagnostics.append(diag.make(
                "CDS-V2-DTCG-STRUCTURE",
                "Resolver document must declare a non-empty orderedSourceSets list "
                "(DTCG 2025.10 resolver concept)",
                source))

    # ------------------------------------------------------------------ V3

    def run_v3(self, documents: list[ScopeDocument],
               index: dict[str, dict]) -> dict[int, ResultState]:
        states: dict[int, ResultState] = {}
        scope_manifest = next(
            (d for d in documents if d.kind is DocumentKind.SOURCE_SET_MANIFEST), None)
        for position, doc in enumerate(documents):
            before = len(doc.diagnostics)
            if doc.kind is DocumentKind.TOKEN_DOCUMENT:
                self._v3_token_document(doc, scope_manifest, index)
            elif doc.kind is DocumentKind.SOURCE_SET_MANIFEST:
                self._v3_manifest(doc)
            elif doc.kind is DocumentKind.RESOLVER_DOCUMENT:
                self._v3_resolver(doc)
            failed = any(
                d.layer == "V3" and d.severity == "error"
                for d in doc.diagnostics[before:])
            states[position] = ResultState.FAIL if failed else ResultState.PASS
        return states

    def _v3_schema(self, doc: ScopeDocument, schema_key: str) -> None:
        source = str(doc.path)
        for error in self.registry.iter_errors(schema_key, doc.content):
            pointer = "/" + "/".join(_escape(str(p)) for p in error.absolute_path)
            in_extensions = "$extensions" in [str(p) for p in error.absolute_path]
            code = "CDS-V3-EXTENSION" if in_extensions else "CDS-V3-SCHEMA"
            doc.diagnostics.append(diag.make(
                code, f"Schema violation: {error.message}", source,
                json_pointer=pointer if pointer != "/" else None))

    def _v3_token_document(self, doc: ScopeDocument,
                           scope_manifest: ScopeDocument | None,
                           index: dict[str, dict]) -> None:
        source = str(doc.path)
        self._v3_schema(doc, "token-document")
        payload = doc.payload
        if payload is None:
            doc.diagnostics.append(diag.make(
                "CDS-V3-EXTENSION",
                f"Missing CDS extension payload at $extensions.{CDS_EXTENSION_ROOT} "
                "(required for source-set identity, DEC-S-084)",
                source))
            return
        if "profileVersion" not in payload:
            doc.diagnostics.append(diag.make(
                "CDS-V3-EXTENSION",
                "CDS extension payload lacks the required profileVersion (DEC-S-084)",
                source))

        deferred = [
            (path, info["deferred"], info["pointer"])
            for path, info in index.items()
            if info["doc"] is doc and info.get("deferred")]

        manifest_content, manifest_dir = self._locate_manifest(doc, scope_manifest)
        if manifest_content is None:
            if deferred:
                for _, alias_path, pointer in deferred:
                    doc.diagnostics.append(diag.make(
                        "CDS-V3-UNDECLARED-CROSS-FILE",
                        f"Cross-file reference {{{alias_path}}} cannot be bound: no "
                        "declared Source-Set Manifest is available (references are "
                        "valid only through the declared local graph, DEC-S-091)",
                        source, json_pointer=pointer))
            return

        graph = ManifestGraph.from_manifest(manifest_content)
        set_id = payload.get("sourceSetId")
        entry = graph.entries.get(set_id) if set_id else None
        if entry is None:
            if deferred or set_id:
                doc.diagnostics.append(diag.make(
                    "CDS-V3-UNDECLARED-CROSS-FILE",
                    f"Source set {set_id!r} is not registered in the declared "
                    "manifest graph; undeclared references fail closed (DEC-S-091)",
                    source))
            return
        self._v3_identity(doc, payload, entry)
        if deferred:
            self._v3_resolve_deferred(doc, payload, deferred, graph, manifest_dir)
        if payload.get("layer") == "product-profile":
            self._v3_product_profile_bounds(doc, payload, manifest_content, index)

    def _locate_manifest(self, doc: ScopeDocument,
                         scope_manifest: ScopeDocument | None):
        if scope_manifest is not None and isinstance(scope_manifest.content, dict):
            return scope_manifest.content, scope_manifest.path.parent
        payload = doc.payload or {}
        manifest_ref = payload.get("manifestRef")
        if not isinstance(manifest_ref, str):
            return None, None
        manifest_path = doc.path.parent / manifest_ref
        try:
            return json_loader.load_path(manifest_path), manifest_path.parent
        except json_loader.LoaderError:
            return None, None

    def _v3_identity(self, doc: ScopeDocument, payload: dict, entry: dict) -> None:
        source = str(doc.path)
        checks = (
            ("layer", payload.get("layer"), entry.get("layer")),
            ("sourceRevision", payload.get("sourceRevision"), entry.get("sourceRevision")),
            ("profileVersion", payload.get("profileVersion"),
             entry.get("expectedProfileVersion")),
            ("dtcgReportVersion", payload.get("dtcgReportVersion"),
             entry.get("expectedDtcgVersion")),
        )
        for name, doc_value, manifest_value in checks:
            if doc_value != manifest_value:
                doc.diagnostics.append(diag.make(
                    "CDS-V3-IDENTITY",
                    f"Embedded {name} {doc_value!r} disagrees with the manifest "
                    f"entry {manifest_value!r} (fail closed, DEC-S-085)",
                    source))

    def _v3_resolve_deferred(self, doc: ScopeDocument, payload: dict,
                             deferred: list, graph: ManifestGraph,
                             manifest_dir: Path) -> None:
        source = str(doc.path)
        set_id = payload.get("sourceSetId")
        doc_layer = payload.get("layer")
        closure = graph.transitive_dependencies(set_id)
        dep_index: dict[str, dict] = {}
        dep_groups: set[str] = set()
        for dep_id in closure:
            dep_entry = graph.entries[dep_id]
            dep_path = manifest_dir / dep_entry.get("path", "")
            try:
                dep_content = json_loader.load_path(dep_path)
            except json_loader.LoaderError as exc:
                doc.diagnostics.append(diag.make(
                    "CDS-V3-UNDECLARED-CROSS-FILE",
                    f"Declared dependency {dep_id!r} is not locally resolvable: {exc}",
                    source, related_path=str(dep_path), category="missing-source-set"))
                continue
            dep_doc = ScopeDocument(path=dep_path, kind=DocumentKind.TOKEN_DOCUMENT,
                                    v1=ResultState.PASS, content=dep_content)
            sub_index, sub_groups = _build_token_index([dep_doc])
            for key, info in sub_index.items():
                info["setId"] = dep_id
                info["layer"] = dep_entry.get("layer")
                dep_index.setdefault(key, info)
            dep_groups |= sub_groups

        doc_index, _ = _build_token_index([doc])
        for token_path, alias_path, pointer in deferred:
            target = dep_index.get(alias_path)
            if target is None:
                if alias_path.split(".")[0] in dep_groups:
                    doc.diagnostics.append(diag.make(
                        "CDS-V3-UNDECLARED-CROSS-FILE",
                        f"Dangling cross-file reference: {{{alias_path}}} has no "
                        "target token in the declared dependency closure",
                        source, json_pointer=pointer, category="dangling-reference"))
                else:
                    doc.diagnostics.append(diag.make(
                        "CDS-V3-UNDECLARED-CROSS-FILE",
                        f"Reference {{{alias_path}}} leaves the declared Manifest/"
                        "Resolver graph (undeclared cross-file reference, DEC-S-091)",
                        source, json_pointer=pointer))
                continue
            own = doc_index.get(token_path)
            if own and own["type"] and target["type"] and own["type"] != target["type"]:
                doc.diagnostics.append(diag.make(
                    "CDS-V3-UNDECLARED-CROSS-FILE",
                    f"Cross-file type mismatch: {token_path!r} ({own['type']}) "
                    f"references {alias_path!r} ({target['type']})",
                    source, json_pointer=pointer, category="type-mismatch"))
            target_layer = target.get("layer")
            if (doc_layer in LAYER_ORDER and target_layer in LAYER_ORDER):
                if LAYER_ORDER[target_layer] >= LAYER_ORDER[doc_layer]:
                    doc.diagnostics.append(diag.make(
                        "CDS-V3-MANIFEST",
                        f"Cross-file reference direction violation: {doc_layer} "
                        f"document references {target_layer} layer (DEC-S-079)",
                        source, json_pointer=pointer))
                elif doc_layer == "component" and target_layer == "reference":
                    doc.diagnostics.append(diag.make(
                        "CDS-V3-MANIFEST",
                        "Component document bypasses the semantic layer and "
                        "references the reference layer directly (DEC-S-079)",
                        source, json_pointer=pointer))

    def _v3_product_profile_bounds(self, doc: ScopeDocument, payload: dict,
                                   manifest: dict, index: dict[str, dict]) -> None:
        source = str(doc.path)
        boundary = manifest.get("productProfileBoundary") or {}
        approved = set(boundary.get("approvedExtensionPoints") or [])
        doc_point = payload.get("approvedExtensionPoint")
        for token_path, info in index.items():
            if info["doc"] is not doc:
                continue
            token_point = info.get("extensionPoint") or doc_point
            if token_point not in approved:
                doc.diagnostics.append(diag.make(
                    "CDS-V3-MANIFEST",
                    f"Product-profile override of {token_path!r} uses no approved "
                    f"extension point (got {token_point!r}); illegal override",
                    source, json_pointer=info["pointer"], category="illegal-override"))

    def _v3_manifest(self, doc: ScopeDocument) -> None:
        source = str(doc.path)
        self._v3_schema(doc, "source-set-manifest")
        if not isinstance(doc.content, dict):
            return
        graph = ManifestGraph.from_manifest(doc.content)
        kind_map = {
            "backward-layer": ("CDS-V3-MANIFEST", "backward-layer-dependency"),
            "cycle": ("CDS-V3-MANIFEST", "reference-cycle"),
            "self-dependency": ("CDS-V3-MANIFEST", "reference-cycle"),
            "unregistered-dependency": ("CDS-V3-MANIFEST", "missing-source-set"),
            "graph-mismatch": ("CDS-V3-MANIFEST", "manifest-inconsistency"),
            "duplicate-id": ("CDS-V3-IDENTITY", "conflicting-source-set-identity"),
            "case-collision": ("CDS-V3-IDENTITY", "conflicting-source-set-identity"),
            "invalid-id": ("CDS-V3-IDENTITY", "conflicting-source-set-identity"),
        }
        for finding in graph.findings:
            code, category = kind_map.get(finding.kind, ("CDS-V3-MANIFEST", None))
            doc.diagnostics.append(diag.make(
                code, finding.message, source,
                json_pointer=finding.json_pointer, category=category))

        for set_id, entry in graph.entries.items():
            entry_path = doc.path.parent / entry.get("path", "")
            if not entry_path.is_file():
                doc.diagnostics.append(diag.make(
                    "CDS-V3-MANIFEST",
                    f"Declared source-set path for {set_id!r} does not exist "
                    f"locally: {entry.get('path')!r}",
                    source, related_path=str(entry_path),
                    category="missing-source-set"))
                continue
            try:
                content = json_loader.load_path(entry_path)
            except json_loader.LoaderError as exc:
                doc.diagnostics.append(diag.make(
                    "CDS-V3-MANIFEST",
                    f"Declared source-set document for {set_id!r} fails the "
                    f"controlled load: {exc}",
                    source, related_path=str(entry_path),
                    category="missing-source-set"))
                continue
            embedded = ((content.get("$extensions") or {}).get(CDS_EXTENSION_ROOT)
                        if isinstance(content, dict) else None)
            if isinstance(embedded, dict):
                if embedded.get("sourceSetId") != set_id:
                    doc.diagnostics.append(diag.make(
                        "CDS-V3-IDENTITY",
                        f"Embedded source-set ID {embedded.get('sourceSetId')!r} "
                        f"disagrees with the manifest entry {set_id!r}",
                        source, related_path=str(entry_path)))
                elif embedded.get("layer") != entry.get("layer"):
                    doc.diagnostics.append(diag.make(
                        "CDS-V3-IDENTITY",
                        f"Embedded layer {embedded.get('layer')!r} disagrees with "
                        f"the manifest entry layer {entry.get('layer')!r} for {set_id!r}",
                        source, related_path=str(entry_path)))

        for index, resolver_ref in enumerate(doc.content.get("resolverDocuments") or []):
            resolver_path = doc.path.parent / resolver_ref
            if not resolver_path.is_file():
                doc.diagnostics.append(diag.make(
                    "CDS-V3-MANIFEST",
                    f"Declared resolver document does not exist locally: "
                    f"{resolver_ref!r}",
                    source, json_pointer=f"/resolverDocuments/{index}",
                    category="missing-source-set"))
                continue
            try:
                resolver = json_loader.load_path(resolver_path)
            except json_loader.LoaderError as exc:
                doc.diagnostics.append(diag.make(
                    "CDS-V3-MANIFEST",
                    f"Declared resolver document fails the controlled load: {exc}",
                    source, related_path=str(resolver_path),
                    category="missing-source-set"))
                continue
            for finding in check_resolver_order(resolver, graph):
                doc.diagnostics.append(diag.make(
                    "CDS-V3-MANIFEST", finding.message, source,
                    related_path=str(resolver_path), category="resolver-order"))

    def _v3_resolver(self, doc: ScopeDocument) -> None:
        source = str(doc.path)
        self._v3_schema(doc, "resolver-document")
        if not isinstance(doc.content, dict):
            return
        referenced: list[tuple[dict, Any]] = []
        for index, step in enumerate(doc.content.get("orderedSourceSets") or []):
            pointer = f"/orderedSourceSets/{index}"
            ref = step.get("$ref")
            if not isinstance(ref, str):
                continue
            target_path = doc.path.parent / ref
            if not target_path.is_file():
                doc.diagnostics.append(diag.make(
                    "CDS-V3-UNDECLARED-CROSS-FILE",
                    f"Resolver step $ref target does not exist locally: {ref!r}",
                    source, json_pointer=pointer, category="missing-source-set"))
                continue
            try:
                target = json_loader.load_path(target_path)
            except json_loader.LoaderError as exc:
                doc.diagnostics.append(diag.make(
                    "CDS-V3-UNDECLARED-CROSS-FILE",
                    f"Resolver step target fails the controlled load: {exc}",
                    source, json_pointer=pointer, category="missing-source-set"))
                continue
            referenced.append((step, target))
            step_pointer = step.get("pointer")
            if isinstance(step_pointer, str) and step_pointer:
                if _resolve_json_pointer(target, step_pointer) is _MISSING:
                    doc.diagnostics.append(diag.make(
                        "CDS-V3-UNDECLARED-CROSS-FILE",
                        f"Resolver step pointer {step_pointer!r} does not resolve "
                        f"inside {ref!r}",
                        source, json_pointer=pointer, category="dangling-reference"))
            embedded = ((target.get("$extensions") or {}).get(CDS_EXTENSION_ROOT)
                        if isinstance(target, dict) else None)
            if isinstance(embedded, dict) and embedded.get("sourceSetId") != step.get("sourceSetId"):
                doc.diagnostics.append(diag.make(
                    "CDS-V3-IDENTITY",
                    f"Resolver step sourceSetId {step.get('sourceSetId')!r} disagrees "
                    f"with the embedded identity {embedded.get('sourceSetId')!r}",
                    source, json_pointer=pointer))

        manifest_content, manifest_dir = self._resolver_manifest(doc, referenced)
        if manifest_content is not None:
            graph = ManifestGraph.from_manifest(manifest_content)
            for finding in check_resolver_order(doc.content, graph):
                doc.diagnostics.append(diag.make(
                    "CDS-V3-MANIFEST", finding.message, source,
                    category="resolver-order"))
            declared = manifest_content.get("resolverDocuments") or []
            if doc.path.name not in declared:
                doc.diagnostics.append(diag.make(
                    "CDS-V3-MANIFEST",
                    f"Resolver document {doc.path.name!r} is not declared in the "
                    "manifest's resolverDocuments (implicit discovery is "
                    "prohibited, DEC-S-099)",
                    source, category="manifest-inconsistency"))

    def _resolver_manifest(self, doc: ScopeDocument, referenced: list):
        for _, target in referenced:
            embedded = ((target.get("$extensions") or {}).get(CDS_EXTENSION_ROOT)
                        if isinstance(target, dict) else None)
            manifest_ref = (embedded or {}).get("manifestRef")
            if isinstance(manifest_ref, str):
                manifest_path = doc.path.parent / manifest_ref
                try:
                    return json_loader.load_path(manifest_path), manifest_path.parent
                except json_loader.LoaderError:
                    continue
        return None, None

    # ------------------------------------------------------------------ V4

    def run_v4(self, documents: list[ScopeDocument]) -> dict[int, ResultState]:
        """V4 with the CDS-WP-015 ordering rule for status vocabularies:

        1. Objective semantic-status checks run first for every document
           recognized as a Semantic Status vocabulary — the testOnly/
           nonNormative fixture boundary never disables them (DEC-S-118).
        2. Non-objective generic V4 aspects then stay honestly visible as
           Not assessed / Not applicable with rationale.
        """
        states: dict[int, ResultState] = {}
        scope_manifest = next(
            (d.content for d in documents
             if d.kind is DocumentKind.SOURCE_SET_MANIFEST
             and isinstance(d.content, dict)), None)
        for position, doc in enumerate(documents):
            before = len(doc.diagnostics)
            status_doc = (doc.kind is DocumentKind.TOKEN_DOCUMENT
                          and semantic_status.is_status_vocabulary(doc.content))
            if status_doc:
                semantic_status.check_status_document(doc, scope_manifest)
            if doc.is_fixture and not status_doc:
                states[position] = ResultState.NOT_APPLICABLE
                continue
            if not doc.is_fixture:
                self._v4_objective(doc)
            failed = any(
                d.layer == "V4" and d.severity == "error"
                for d in doc.diagnostics[before:])
            if status_doc:
                states[position] = (
                    ResultState.FAIL if failed else ResultState.PASS)
            else:
                states[position] = (
                    ResultState.FAIL if failed else ResultState.NOT_ASSESSED)
            if not failed:
                doc.diagnostics.append(diag.make(
                    "CDS-V4-NOT-ASSESSED",
                    "Non-objective V4 aspects (status truth beyond the fixed "
                    "vocabulary, semantics, accessibility relevance, "
                    "compatibility) require human/governance review and remain "
                    "Not assessed (DEC-S-097)",
                    str(doc.path)))
        return states

    def _v4_objective(self, doc: ScopeDocument) -> None:
        source = str(doc.path)
        payload = doc.payload if doc.kind is DocumentKind.TOKEN_DOCUMENT else (
            doc.content if isinstance(doc.content, dict) else None)
        if not isinstance(payload, dict):
            return
        if not payload.get("sourceRevision"):
            doc.diagnostics.append(diag.make(
                "CDS-V4-PROVENANCE",
                "Missing sourceRevision: provenance-unknown content fails closed "
                "(DEC-S-080)",
                source))
        for field_name, pattern in (("originatingDecision", r"^DEC-S-[0-9]{3}$"),
                                    ("originatingRequirement", r"^CR-[0-9]{3}$")):
            value = payload.get(field_name)
            if value is not None and not re.match(pattern, str(value)):
                doc.diagnostics.append(diag.make(
                    "CDS-V4-PROVENANCE",
                    f"Invalid {field_name} identifier syntax: {value!r}",
                    source))

    # ------------------------------------------------------------ scope run

    def validate_scope(self, paths: list[Path]) -> ScopeResult:
        outcome = ValidationOutcome()
        documents = [self.run_v1(path) for path in paths]

        def finish() -> ScopeResult:
            outcome.diagnostics = [
                diagnostic for doc in documents for diagnostic in doc.diagnostics]
            return ScopeResult(documents, outcome)

        v1 = aggregate_states([doc.v1 for doc in documents])
        outcome.set_result(Layer.V1, v1)
        if v1 is not ResultState.PASS:
            _mark_not_assessed(outcome, Layer.V2, Layer.V3, Layer.V4,
                               reason="blocked by V1")
            return finish()

        index, groups = _build_token_index(
            [d for d in documents if d.kind is DocumentKind.TOKEN_DOCUMENT])

        v2_states = self.run_v2(documents, index, groups)
        if all(state is ResultState.NOT_APPLICABLE for state in v2_states.values()):
            outcome.set_result(Layer.V2, ResultState.NOT_APPLICABLE,
                               "Source-Set manifests are CDS-owned, non-DTCG documents")
        else:
            outcome.set_result(Layer.V2, aggregate_states(list(v2_states.values())))
        if outcome.v2 is ResultState.FAIL:
            _mark_not_assessed(outcome, Layer.V3, Layer.V4, reason="blocked by V2")
            return finish()

        v3_states = self.run_v3(documents, index)
        outcome.set_result(Layer.V3, aggregate_states(list(v3_states.values())))
        if outcome.v3 is ResultState.FAIL:
            _mark_not_assessed(outcome, Layer.V4, reason="blocked by V3")
            return finish()

        v4_states = self.run_v4(documents)
        if all(state is ResultState.NOT_APPLICABLE for state in v4_states.values()):
            outcome.set_result(
                Layer.V4, ResultState.NOT_APPLICABLE,
                "Synthetic, test-only, non-normative fixtures carry no real "
                "semantics or governance (DEC-S-087)")
        else:
            outcome.set_result(Layer.V4, aggregate_states(list(v4_states.values())))
        return finish()


# ---------------------------------------------------------------- helpers

_MISSING = object()


def _document_suffix(path: Path) -> str:
    name = path.name
    for suffix in EXTENSION_KINDS:
        if name.endswith(suffix):
            return suffix
    return ""


def _escape(key: str) -> str:
    return key.replace("~", "~0").replace("/", "~1")


def _build_token_index(token_docs: list[ScopeDocument]):
    """Index dotted token paths -> info; also collect group paths."""
    index: dict[str, dict] = {}
    groups: set[str] = set()

    def walk(node: dict, doc: ScopeDocument, name_path: list[str],
             pointer: str, inherited_type: str | None) -> None:
        own_type = node.get("$type") if isinstance(node.get("$type"), str) else None
        effective = own_type or inherited_type
        if "$value" in node:
            token_path = ".".join(name_path)
            extensions = node.get("$extensions") or {}
            cds = extensions.get(CDS_EXTENSION_ROOT) if isinstance(extensions, dict) else None
            index[token_path] = {
                "doc": doc,
                "type": effective,
                "value": node.get("$value"),
                "pointer": pointer,
                "extensionPoint": (cds or {}).get("approvedExtensionPoint")
                if isinstance(cds, dict) else None,
            }
            return
        if name_path:
            groups.add(".".join(name_path))
        for key, value in node.items():
            if key in RESERVED_MEMBERS or not isinstance(value, dict):
                continue
            if NAME_SEGMENT_RE.match(key):
                walk(value, doc, name_path + [key],
                     f"{pointer}/{_escape(key)}", effective)

    for doc in token_docs:
        if isinstance(doc.content, dict):
            walk(doc.content, doc, [], "", None)
    return index, groups


def _detect_alias_cycles(edges: dict[str, str], index: dict[str, dict]) -> None:
    """Detect cycles over the scope-wide resolved alias edges.

    A cycle is reported once, on the document that owns the first cycle
    participant, so cross-file cycles surface exactly one primary diagnostic.
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color: dict[str, int] = {}
    reported: set[frozenset] = set()

    def visit(node: str, trail: list[str]) -> None:
        color[node] = GRAY
        target = edges.get(node)
        if target is not None and target in index:
            if color.get(target) == GRAY:
                cycle_nodes = frozenset(trail + [node, target])
                if cycle_nodes not in reported:
                    reported.add(cycle_nodes)
                    cycle = " -> ".join(trail + [node, target])
                    owner = index[target]["doc"]
                    owner.diagnostics.append(diag.make(
                        "CDS-V2-DTCG-REFERENCE",
                        f"Reference cycle: {cycle}",
                        str(owner.path), category="reference-cycle"))
            elif color.get(target, WHITE) == WHITE:
                visit(target, trail + [node])
        color[node] = BLACK

    for node in edges:
        if color.get(node, WHITE) == WHITE:
            visit(node, [])


def _resolve_json_pointer(document: Any, pointer: str):
    if pointer == "":
        return document
    current = document
    for raw in pointer.lstrip("/").split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict):
            if token not in current:
                return _MISSING
            current = current[token]
        elif isinstance(current, list):
            if not token.isdigit() or int(token) >= len(current):
                return _MISSING
            current = current[int(token)]
        else:
            return _MISSING
    return current


def _mark_not_assessed(outcome: ValidationOutcome, *layers: Layer, reason: str) -> None:
    for layer in layers:
        outcome.set_result(layer, ResultState.NOT_ASSESSED, reason)
