"""Manifest, dependency-graph, and resolver-order validation (DEC-S-099).

Pure graph logic over already-loaded manifest/resolver content: registration,
identity collisions, dependency direction, cycles, and resolver ordering.
Emits (finding-kind, message, pointer) tuples; the validation layer maps them
to stable diagnostics.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from tools.cds_validator.models import LAYER_ORDER

SOURCE_SET_ID_RE = re.compile(r"^[a-z][a-z0-9-]*(?:/[a-z][a-z0-9-]*)*$")


@dataclass
class GraphFinding:
    kind: str  # e.g. "backward-layer", "cycle", "unregistered-dependency"
    message: str
    json_pointer: str | None = None


@dataclass
class ManifestGraph:
    """Declared source-set graph extracted from a Source-Set Manifest."""

    entries: dict[str, dict] = field(default_factory=dict)  # sourceSetId -> entry
    findings: list[GraphFinding] = field(default_factory=list)

    @classmethod
    def from_manifest(cls, manifest: dict) -> "ManifestGraph":
        graph = cls()
        entries = manifest.get("sourceSets") or []
        seen_folded: dict[str, str] = {}
        for index, entry in enumerate(entries):
            set_id = entry.get("sourceSetId", "")
            pointer = f"/sourceSets/{index}"
            if not SOURCE_SET_ID_RE.match(set_id or ""):
                graph.findings.append(GraphFinding(
                    "invalid-id", f"Invalid source-set ID syntax: {set_id!r}", pointer))
                continue
            if set_id in graph.entries:
                graph.findings.append(GraphFinding(
                    "duplicate-id", f"Source-set ID declared twice: {set_id!r}", pointer))
                continue
            folded = set_id.lower()
            if folded in seen_folded and seen_folded[folded] != set_id:
                graph.findings.append(GraphFinding(
                    "case-collision",
                    f"Case-only source-set ID collision: {set_id!r} vs {seen_folded[folded]!r}",
                    pointer))
                continue
            seen_folded[folded] = set_id
            graph.entries[set_id] = entry

        graph._check_dependencies()
        graph._check_dependency_graph_consistency(manifest)
        graph._check_cycles()
        return graph

    def _check_dependencies(self) -> None:
        for set_id, entry in self.entries.items():
            layer = entry.get("layer")
            for dep in entry.get("dependencies") or []:
                if dep == set_id:
                    self.findings.append(GraphFinding(
                        "self-dependency", f"{set_id!r} depends on itself"))
                    continue
                if dep not in self.entries:
                    self.findings.append(GraphFinding(
                        "unregistered-dependency",
                        f"{set_id!r} depends on unregistered source set {dep!r}"))
                    continue
                dep_layer = self.entries[dep].get("layer")
                if layer in LAYER_ORDER and dep_layer in LAYER_ORDER:
                    if LAYER_ORDER[dep_layer] >= LAYER_ORDER[layer]:
                        self.findings.append(GraphFinding(
                            "backward-layer",
                            f"Prohibited dependency direction: {set_id!r} "
                            f"(layer {layer}) depends on {dep!r} (layer {dep_layer}); "
                            "dependencies must point strictly downward (DEC-S-079)"))

    def _check_dependency_graph_consistency(self, manifest: dict) -> None:
        declared = manifest.get("dependencyGraph")
        if not isinstance(declared, dict):
            return
        for set_id, deps in declared.items():
            entry = self.entries.get(set_id)
            if entry is None:
                self.findings.append(GraphFinding(
                    "graph-mismatch",
                    f"dependencyGraph names unregistered source set {set_id!r}",
                    "/dependencyGraph"))
                continue
            if sorted(deps or []) != sorted(entry.get("dependencies") or []):
                self.findings.append(GraphFinding(
                    "graph-mismatch",
                    f"dependencyGraph for {set_id!r} disagrees with the entry's "
                    "dependencies",
                    "/dependencyGraph"))
        for set_id in self.entries:
            if set_id not in declared:
                self.findings.append(GraphFinding(
                    "graph-mismatch",
                    f"dependencyGraph omits registered source set {set_id!r}",
                    "/dependencyGraph"))

    def _check_cycles(self) -> None:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {set_id: WHITE for set_id in self.entries}

        def visit(node: str, trail: list[str]) -> None:
            color[node] = GRAY
            for dep in self.entries[node].get("dependencies") or []:
                if dep not in self.entries:
                    continue
                if color[dep] == GRAY:
                    cycle = " -> ".join(trail + [node, dep])
                    self.findings.append(GraphFinding(
                        "cycle", f"Dependency cycle: {cycle}"))
                elif color[dep] == WHITE:
                    visit(dep, trail + [node])
            color[node] = BLACK

        for set_id in self.entries:
            if color[set_id] == WHITE:
                visit(set_id, [])

    def transitive_dependencies(self, set_id: str) -> list[str]:
        """Downward closure of declared dependencies (excludes set_id)."""
        closure: list[str] = []
        stack = list(self.entries.get(set_id, {}).get("dependencies") or [])
        seen = set()
        while stack:
            dep = stack.pop(0)
            if dep in seen or dep not in self.entries:
                continue
            seen.add(dep)
            closure.append(dep)
            stack.extend(self.entries[dep].get("dependencies") or [])
        return closure


def check_resolver_order(resolver: dict, graph: ManifestGraph) -> list[GraphFinding]:
    """Resolver steps must use registered sets in dependency-respecting order."""
    findings: list[GraphFinding] = []
    steps = resolver.get("orderedSourceSets") or []
    orders = [step.get("order") for step in steps]
    if orders != sorted(orders) or len(set(orders)) != len(orders):
        findings.append(GraphFinding(
            "resolver-order", "orderedSourceSets orders are not strictly increasing"))
    position: dict[str, int] = {}
    for index, step in enumerate(steps):
        set_id = step.get("sourceSetId", "")
        pointer = f"/orderedSourceSets/{index}"
        if set_id not in graph.entries:
            findings.append(GraphFinding(
                "resolver-unregistered",
                f"Resolver step references unregistered source set {set_id!r}",
                pointer))
            continue
        position[set_id] = index
    for set_id, index in position.items():
        for dep in graph.entries[set_id].get("dependencies") or []:
            if dep in position and position[dep] > index:
                findings.append(GraphFinding(
                    "resolver-order",
                    f"Resolver orders {set_id!r} before its dependency {dep!r}"))
    return findings
