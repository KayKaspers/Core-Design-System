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

import re

from tools.cds_validator import diagnostics as diag
from tools.cds_validator.models import CDS_EXTENSION_ROOT

#: A Candidate source revision must be an explicit, migration-visible identity
#: (DEC-S-117, DEC-S-122): the base status revision plus a ``-candidate`` marker.
CANDIDATE_REVISION_PATTERN = re.compile(r"^semantic-status-rev-[0-9]{4}-candidate$")

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

    # ---- maturity / approval metadata state machine (CDS-WP-016) ----
    # Experimental/Unapproved (or absent) is the committed default. A *coherent*
    # Candidate+Approved combination becomes validator-conformant only when it
    # also carries a Candidate source revision and is not a testOnly/nonNormative
    # fixture. Stable stays out of contract (a later explicit gate and a separate
    # validator-contract change are required).
    #
    # AUTHORITY BOUNDARY: a validator pass on Candidate+Approved proves ONLY
    # internal metadata coherence (allowed revision form, no fixture marker). It
    # does NOT prove that the governance gate was authorized, nor Human-Maintainer
    # approval, Candidate promotion, Stable, conformance, or publication. Real
    # Candidate authority is established solely by the Candidate Approval Record,
    # the Nova finalization review, and the Human-Maintainer commit (DEC-S-115,
    # DEC-S-122, DEC-S-124). The diagnostic code CDS-V4-STATUS-IDENTITY and its
    # meaning are unchanged; no new diagnostic code is introduced.
    payload = _payload(doc.content)
    maturity = payload.get("maturityState")
    approval = payload.get("approvalState")
    revision = payload.get("sourceRevision")
    is_fixture = (payload.get("testOnly") is True
                  or payload.get("nonNormative") is True)

    if maturity == "Stable":
        emit("CDS-V4-STATUS-IDENTITY",
             "Status source declares maturityState 'Stable': Stable maturity is "
             "out of contract and requires a separate explicit gate and a "
             "validator-contract change (DEC-S-115, DEC-S-124)")
    elif maturity == "Candidate":
        if is_fixture:
            emit("CDS-V4-STATUS-IDENTITY",
                 "Status source declares Candidate maturity on a testOnly/"
                 "nonNormative fixture: Candidate/Approved metadata may not be "
                 "embedded in a fixture (DEC-S-115, DEC-S-124)")
        elif approval != "Approved":
            emit("CDS-V4-STATUS-IDENTITY",
                 f"Status source declares maturityState 'Candidate' with "
                 f"approvalState {approval!r}: a Candidate source must declare "
                 "approvalState 'Approved' and be internally coherent (DEC-S-122)")
        elif not (isinstance(revision, str)
                  and CANDIDATE_REVISION_PATTERN.match(revision)):
            emit("CDS-V4-STATUS-IDENTITY",
                 f"Status source declares Candidate maturity with sourceRevision "
                 f"{revision!r}: a Candidate revision must match "
                 "'semantic-status-rev-NNNN-candidate' (DEC-S-117, DEC-S-122)")
        # else: coherent Candidate metadata — no diagnostic; authority stays
        # external (Approval Record, Nova review, Human-Maintainer commit).
    elif approval == "Approved":
        # 'Approved' outside a coherent Candidate source (e.g. Experimental+
        # Approved, an approval with no Candidate maturity, or on a fixture) is
        # contradictory and fails closed.
        emit("CDS-V4-STATUS-IDENTITY",
             f"Status source declares approvalState 'Approved' with maturityState "
             f"{maturity!r}: 'Approved' is coherent only with a Candidate source "
             "after the governance gate (DEC-S-122)")

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
