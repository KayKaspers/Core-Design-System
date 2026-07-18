"""Semantic Status vocabulary validation (CDS-WP-015, DEC-S-116…118).

Objective, machine-checkable V4 rules for documents that carry the CDS
Semantic Status vocabulary (a root group named ``status``): exactly the five
authorized axes with exactly the authorized five values each, ``unknown`` on
every axis, 25 tokens, path/value agreement, no case-only identifier
collisions, no aggregate or appearance-oriented status roles, no
Candidate/approval statements, and source/manifest identity agreement.

These checks run even for ``testOnly``/``nonNormative`` fixtures: the fixture
boundary never disables the objective status rules (resume-run V4 ordering
rule). Non-objective V4 aspects remain Not assessed / Not applicable.
"""

from __future__ import annotations

from tools.cds_validator import diagnostics as diag
from tools.cds_validator.models import CDS_EXTENSION_ROOT

#: The authorized vocabulary (DEC-S-105, DEC-S-106) — 5 axes x 5 values.
AUTHORIZED_AXES: dict[str, tuple[str, ...]] = {
    "condition": ("nominal", "degraded", "disrupted", "unavailable", "unknown"),
    "severity": ("none", "minor", "major", "critical", "unknown"),
    "confidence": ("verified", "supported", "uncertain", "unverified", "unknown"),
    "freshness": ("current", "aging", "stale", "expired", "unknown"),
    "evidence": ("available", "partial", "unavailable", "not-applicable", "unknown"),
}

EXPECTED_TOKEN_COUNT = 25

#: Prohibited status-role segments (resume-run rule). Aggregate-oriented
#: segments and appearance-oriented segments are reported distinctly.
AGGREGATE_SEGMENTS = frozenset({"health", "overall", "score", "aggregate", "success"})
VISUAL_SEGMENTS = frozenset({"color", "icon", "shape", "position", "motion"})

_RESERVED = frozenset({"$value", "$type", "$description", "$deprecated", "$extensions"})


def is_status_vocabulary(content) -> bool:
    """A document is a Semantic Status vocabulary iff it has a root group
    named ``status`` (dict-valued, non-reserved member)."""
    return isinstance(content, dict) and isinstance(content.get("status"), dict)


def _payload(content) -> dict:
    extensions = content.get("$extensions") if isinstance(content, dict) else None
    payload = (extensions or {}).get(CDS_EXTENSION_ROOT)
    return payload if isinstance(payload, dict) else {}


def check_status_document(doc, manifest_content=None) -> list:
    """Run all objective semantic-status checks; append and return diagnostics.

    ``doc`` is a ScopeDocument whose content parsed at V1. ``manifest_content``
    is the in-scope Source-Set Manifest content, if any.
    """
    source = str(doc.path)
    found: list = []

    def emit(code, message, pointer=None):
        d = diag.make(code, message, source, json_pointer=pointer)
        found.append(d)
        doc.diagnostics.append(d)

    status = doc.content.get("status")

    # ---- axis-group level: authorized set, prohibited roles, collisions ----
    group_names = [k for k, v in status.items()
                   if k not in _RESERVED and isinstance(v, dict)]
    folded_seen: dict[str, str] = {}
    for name in group_names:
        folded = name.casefold()
        if folded in folded_seen and folded_seen[folded] != name:
            emit("CDS-V4-STATUS-COLLISION",
                 f"Case-only axis identifier collision: {name!r} vs "
                 f"{folded_seen[folded]!r}", f"/status/{name}")
        folded_seen.setdefault(folded, name)
        if name in AUTHORIZED_AXES:
            continue
        if name in AGGREGATE_SEGMENTS:
            emit("CDS-V4-STATUS-AGGREGATE",
                 f"Aggregate status role {name!r} is prohibited: no aggregated "
                 "health statement may exist (DEC-S-108, DEC-S-118)",
                 f"/status/{name}")
        elif name in VISUAL_SEGMENTS:
            emit("CDS-V4-STATUS-VISUAL-LEAKAGE",
                 f"Appearance-oriented status role {name!r} is prohibited: "
                 "status meaning is non-visual (DEC-S-111, DEC-S-118)",
                 f"/status/{name}")
        else:
            emit("CDS-V4-STATUS-AXIS",
                 f"Unauthorized status axis {name!r}: the authorized axis set "
                 "is exactly condition/severity/confidence/freshness/evidence "
                 "(DEC-S-105)", f"/status/{name}")
    for axis in AUTHORIZED_AXES:
        if axis not in group_names:
            emit("CDS-V4-STATUS-AXIS",
                 f"Missing authorized status axis {axis!r}: no axis may be "
                 "silently absent (DEC-S-106)", "/status")

    # ---- value level per authorized axis ----
    token_count = 0
    for axis, values in ((a, v) for a, v in status.items()
                         if a not in _RESERVED and isinstance(v, dict)):
        value_names = [k for k, v in values.items()
                       if k not in _RESERVED and isinstance(v, dict)]
        token_count += sum(1 for k in value_names if "$value" in values[k])
        if axis not in AUTHORIZED_AXES:
            continue
        authorized = AUTHORIZED_AXES[axis]
        folded_vals: dict[str, str] = {}
        for name in value_names:
            pointer = f"/status/{axis}/{name}"
            folded = name.casefold()
            if folded in folded_vals and folded_vals[folded] != name:
                emit("CDS-V4-STATUS-COLLISION",
                     f"Case-only value identifier collision on axis {axis!r}: "
                     f"{name!r} vs {folded_vals[folded]!r}", pointer)
            folded_vals.setdefault(folded, name)
            if name in authorized:
                token = values[name]
                actual = token.get("$value")
                if actual != name:
                    if isinstance(actual, str) and actual.casefold() == name:
                        emit("CDS-V4-STATUS-COLLISION",
                             f"Case-only identifier collision: token "
                             f"status.{axis}.{name} carries value {actual!r} "
                             "differing from its technical identifier only by "
                             "case (DEC-S-117, DEC-S-118)", pointer)
                    else:
                        emit("CDS-V4-STATUS-PATH-VALUE",
                             f"Token path and value disagree: "
                             f"status.{axis}.{name} carries {actual!r} instead "
                             "of its stable technical value identifier "
                             "(DEC-S-117)", pointer)
                continue
            if name in VISUAL_SEGMENTS:
                emit("CDS-V4-STATUS-VISUAL-LEAKAGE",
                     f"Appearance-oriented status value {name!r} on axis "
                     f"{axis!r} is prohibited (DEC-S-111, DEC-S-118)", pointer)
            elif name in AGGREGATE_SEGMENTS:
                emit("CDS-V4-STATUS-AGGREGATE",
                     f"Aggregate status value {name!r} on axis {axis!r} is "
                     "prohibited (DEC-S-108, DEC-S-118)", pointer)
            else:
                emit("CDS-V4-STATUS-VALUE",
                     f"Unauthorized value {name!r} on axis {axis!r}: the "
                     "authorized value set is fixed (DEC-S-106)", pointer)
        for expected in authorized:
            if expected not in value_names:
                code = ("CDS-V4-STATUS-UNKNOWN" if expected == "unknown"
                        else "CDS-V4-STATUS-VALUE")
                emit(code,
                     f"Missing authorized value {expected!r} on axis {axis!r}"
                     + (": `unknown` must exist explicitly on every axis "
                        "(DEC-S-106)" if expected == "unknown" else
                        " (DEC-S-106)"),
                     f"/status/{axis}")

    # ---- token count ----
    if token_count != EXPECTED_TOKEN_COUNT:
        emit("CDS-V4-STATUS-COUNT",
             f"Status token count is {token_count}, expected exactly "
             f"{EXPECTED_TOKEN_COUNT} (5 axes x 5 values, DEC-S-116)",
             "/status")

    # ---- candidate / approval statement boundary ----
    payload = _payload(doc.content)
    maturity = payload.get("maturityState")
    approval = payload.get("approvalState")
    if maturity in ("Candidate", "Stable"):
        emit("CDS-V4-STATUS-IDENTITY",
             f"Status source declares maturityState {maturity!r}: the Semantic "
             "Status vocabulary may not claim Candidate/Stable maturity "
             "(DEC-S-115, DEC-S-124)")
    if approval == "Approved":
        emit("CDS-V4-STATUS-IDENTITY",
             "Status source declares approvalState 'Approved': no approval "
             "statement may be embedded before the Candidate gate (DEC-S-122)")

    # ---- source-set / manifest identity agreement ----
    if isinstance(manifest_content, dict):
        set_id = payload.get("sourceSetId")
        entries = {e.get("sourceSetId"): e
                   for e in manifest_content.get("sourceSets") or []}
        entry = entries.get(set_id)
        if entry is None:
            emit("CDS-V4-STATUS-IDENTITY",
                 f"Status source-set identity {set_id!r} is not registered in "
                 "the in-scope manifest (DEC-S-123)")
        else:
            for field_name, doc_value, man_value in (
                    ("layer", payload.get("layer"), entry.get("layer")),
                    ("sourceRevision", payload.get("sourceRevision"),
                     entry.get("sourceRevision")),
                    ("profileVersion", payload.get("profileVersion"),
                     entry.get("expectedProfileVersion")),
                    ("dtcgReportVersion", payload.get("dtcgReportVersion"),
                     entry.get("expectedDtcgVersion"))):
                if doc_value != man_value:
                    emit("CDS-V4-STATUS-IDENTITY",
                         f"Status identity disagreement on {field_name}: "
                         f"document {doc_value!r} vs manifest {man_value!r} "
                         "(fail closed, DEC-S-123)")
    return found
