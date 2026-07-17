"""Stable diagnostic codes for the CDS offline token validator.

Codes are a published contract (RISK-077): identifiers and meanings must not
change silently. Each code is bound to a layer, a default severity, a default
diagnostic category, and the Decision/Risk identifiers it operationalizes.
"""

from __future__ import annotations

from dataclasses import dataclass

from tools.cds_validator.models import Diagnostic, Severity


@dataclass(frozen=True)
class DiagnosticSpec:
    code: str
    layer: str
    severity: Severity
    category: str
    decisions: tuple[str, ...]
    risks: tuple[str, ...]


_SPECS: dict[str, DiagnosticSpec] = {
    spec.code: spec
    for spec in (
        # V1 — syntax and file contract
        DiagnosticSpec("CDS-V1-JSON-PARSE", "V1", Severity.ERROR, "invalid-json",
                       ("DEC-S-075",), ("RISK-064",)),
        DiagnosticSpec("CDS-V1-DUPLICATE-KEY", "V1", Severity.ERROR, "duplicate-key",
                       ("DEC-S-088", "DEC-S-095"), ("RISK-068",)),
        DiagnosticSpec("CDS-V1-FILE-EXTENSION", "V1", Severity.ERROR, "invalid-file-identity",
                       ("DEC-S-075",), ("RISK-064",)),
        DiagnosticSpec("CDS-V1-POINTER-SYNTAX", "V1", Severity.ERROR, "invalid-json",
                       ("DEC-S-078",), ("RISK-064",)),
        DiagnosticSpec("CDS-V1-NETWORK-REFERENCE", "V1", Severity.ERROR, "network-reference",
                       ("DEC-S-091", "DEC-S-096"), ("RISK-079",)),
        DiagnosticSpec("CDS-V1-PATH-ESCAPE", "V1", Severity.ERROR, "path-escape",
                       ("DEC-S-091",), ("RISK-079",)),
        # V2 — DTCG 2025.10 contract (bounded coverage, DEC-S-098)
        DiagnosticSpec("CDS-V2-DTCG-STRUCTURE", "V2", Severity.ERROR, "dtcg-profile-violation",
                       ("DEC-S-073",), ("RISK-074",)),
        DiagnosticSpec("CDS-V2-DTCG-REFERENCE", "V2", Severity.ERROR, "dangling-reference",
                       ("DEC-S-078",), ("RISK-059",)),
        DiagnosticSpec("CDS-V2-PREVIEW-FEATURE", "V2", Severity.ERROR, "preview-feature",
                       ("DEC-S-074",), ("RISK-056",)),
        # V3 — CDS profile contract
        DiagnosticSpec("CDS-V3-SCHEMA", "V3", Severity.ERROR, "schema-violation",
                       ("DEC-S-083",), ("RISK-064", "RISK-066")),
        DiagnosticSpec("CDS-V3-EXTENSION", "V3", Severity.ERROR, "invalid-extension",
                       ("DEC-S-084",), ("RISK-064",)),
        DiagnosticSpec("CDS-V3-IDENTITY", "V3", Severity.ERROR, "conflicting-source-set-identity",
                       ("DEC-S-085",), ("RISK-069",)),
        DiagnosticSpec("CDS-V3-MANIFEST", "V3", Severity.ERROR, "backward-layer-dependency",
                       ("DEC-S-079", "DEC-S-085", "DEC-S-099"), ("RISK-060", "RISK-069")),
        DiagnosticSpec("CDS-V3-UNDECLARED-CROSS-FILE", "V3", Severity.ERROR,
                       "undeclared-cross-file-reference",
                       ("DEC-S-091", "DEC-S-099"), ("RISK-059", "RISK-069")),
        # V4 — semantic and governance contract (objective subset)
        DiagnosticSpec("CDS-V4-LAYER-DIRECTION", "V4", Severity.ERROR, "backward-layer-dependency",
                       ("DEC-S-079",), ("RISK-060",)),
        DiagnosticSpec("CDS-V4-REFERENCE-CYCLE", "V4", Severity.ERROR, "reference-cycle",
                       ("DEC-S-078", "DEC-S-091"), ("RISK-059",)),
        DiagnosticSpec("CDS-V4-DANGLING-REFERENCE", "V4", Severity.ERROR, "dangling-reference",
                       ("DEC-S-078", "DEC-S-091"), ("RISK-059",)),
        DiagnosticSpec("CDS-V4-TYPE-MISMATCH", "V4", Severity.ERROR, "type-mismatch",
                       ("DEC-S-078",), ("RISK-059",)),
        DiagnosticSpec("CDS-V4-PROVENANCE", "V4", Severity.ERROR, "missing-metadata",
                       ("DEC-S-080",), ("RISK-080",)),
        DiagnosticSpec("CDS-V4-NOT-ASSESSED", "V4", Severity.INFO, "not-assessed",
                       ("DEC-S-097",), ()),
        # Internal
        DiagnosticSpec("CDS-INTERNAL", "internal", Severity.ERROR, "internal-error",
                       (), ()),
    )
}

ALL_CODES = tuple(sorted(_SPECS))


def make(code: str, message: str, source_path: str, *,
         json_pointer: str | None = None, related_path: str | None = None,
         category: str | None = None) -> Diagnostic:
    """Create a diagnostic from a registered code. Unknown codes fail closed."""
    if code not in _SPECS:
        raise KeyError(f"Unknown diagnostic code: {code}")
    spec = _SPECS[code]
    return Diagnostic(
        code=spec.code,
        layer=spec.layer,
        severity=spec.severity.value,
        category=category or spec.category,
        message=message,
        sourcePath=source_path,
        jsonPointer=json_pointer,
        relatedPath=related_path,
        decisionReferences=list(spec.decisions),
        riskReferences=list(spec.risks),
    )
