"""Core result and layer models for the CDS offline token validator.

The four validation layers and the six-state result vocabulary are fixed by
the Machine-Readable Validation Contract (DEC-S-078, DEC-S-089, DEC-S-097).
No aggregate or numeric score exists anywhere in these models.
"""

from __future__ import annotations

import enum
from dataclasses import dataclass, field


class Layer(enum.Enum):
    V1 = "V1"
    V2 = "V2"
    V3 = "V3"
    V4 = "V4"


class ResultState(enum.Enum):
    PASS = "Pass"
    PASS_WITH_LIMITATIONS = "Pass with limitations"
    FAIL = "Fail"
    BLOCKED = "Blocked"
    NOT_ASSESSED = "Not assessed"
    NOT_APPLICABLE = "Not applicable with rationale"


class Severity(enum.Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class DocumentKind(enum.Enum):
    TOKEN_DOCUMENT = "token-document"
    SOURCE_SET_MANIFEST = "source-set-manifest"
    RESOLVER_DOCUMENT = "resolver-document"
    UNKNOWN = "unknown"


#: File-extension contract (V1 local file identity).
EXTENSION_KINDS = {
    ".tokens.json": DocumentKind.TOKEN_DOCUMENT,
    ".source-set.json": DocumentKind.SOURCE_SET_MANIFEST,
    ".resolver.json": DocumentKind.RESOLVER_DOCUMENT,
}

CDS_EXTENSION_ROOT = "io.github.kaykaspers.cds"

#: Downward layer order (DEC-S-079): lower index may never depend on higher.
LAYER_ORDER = {"reference": 0, "semantic": 1, "component": 2, "product-profile": 3}


@dataclass
class Diagnostic:
    """A single stable diagnostic (DEC-S-101, RISK-077)."""

    code: str
    layer: str
    severity: str
    category: str
    message: str
    sourcePath: str
    jsonPointer: str | None = None
    relatedPath: str | None = None
    decisionReferences: list[str] = field(default_factory=list)
    riskReferences: list[str] = field(default_factory=list)

    def to_json(self) -> dict:
        payload = {
            "code": self.code,
            "layer": self.layer,
            "severity": self.severity,
            "category": self.category,
            "message": self.message,
            "sourcePath": self.sourcePath,
            "decisionReferences": self.decisionReferences,
            "riskReferences": self.riskReferences,
        }
        if self.jsonPointer is not None:
            payload["jsonPointer"] = self.jsonPointer
        if self.relatedPath is not None:
            payload["relatedPath"] = self.relatedPath
        return payload


@dataclass
class LayerResult:
    layer: Layer
    state: ResultState
    rationale: str | None = None


@dataclass
class ValidationOutcome:
    """Layered outcome for one validation scope (document or case scope)."""

    v1: ResultState = ResultState.NOT_ASSESSED
    v2: ResultState = ResultState.NOT_ASSESSED
    v3: ResultState = ResultState.NOT_ASSESSED
    v4: ResultState = ResultState.NOT_ASSESSED
    rationales: dict[str, str] = field(default_factory=dict)
    diagnostics: list[Diagnostic] = field(default_factory=list)

    def result_for(self, layer: Layer) -> ResultState:
        return {"V1": self.v1, "V2": self.v2, "V3": self.v3, "V4": self.v4}[layer.value]

    def set_result(self, layer: Layer, state: ResultState, rationale: str | None = None) -> None:
        setattr(self, layer.value.lower(), state)
        if rationale:
            self.rationales[layer.value] = rationale

    def blocking_layer(self) -> str:
        for layer in (Layer.V1, Layer.V2, Layer.V3, Layer.V4):
            if self.result_for(layer) in (ResultState.FAIL, ResultState.BLOCKED):
                return layer.value
        return "none"

    def as_dict(self) -> dict[str, str]:
        return {
            "V1": self.v1.value,
            "V2": self.v2.value,
            "V3": self.v3.value,
            "V4": self.v4.value,
        }


def aggregate_states(states: list[ResultState]) -> ResultState:
    """Aggregate one layer across several documents of a case scope.

    Fail dominates, then Blocked, then Not assessed; a mixture of Pass and
    Not-applicable documents is a Pass for the scope; an all-Not-applicable
    layer stays Not applicable. This aggregates one layer's state across
    files only — layers themselves are never merged (DEC-S-097).
    """
    if not states:
        return ResultState.NOT_ASSESSED
    for dominant in (ResultState.FAIL, ResultState.BLOCKED, ResultState.NOT_ASSESSED):
        if dominant in states:
            return dominant
    if ResultState.PASS_WITH_LIMITATIONS in states:
        return ResultState.PASS_WITH_LIMITATIONS
    if all(state is ResultState.NOT_APPLICABLE for state in states):
        return ResultState.NOT_APPLICABLE
    return ResultState.PASS
