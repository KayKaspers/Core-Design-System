"""CDS-WP-016 Candidate Accessibility Gate — test-only evidence runner.

TEST AND EVIDENCE TOOLING ONLY. This module is **not** part of the CDS offline
validator CLI, is never imported by ``tools.cds_validator``, defines no public
API, no consumer-facing format, and no runtime contract. It reads explicitly
named input paths, evaluates the already-normative Semantic Status rules over a
test-only statement fixture, and writes one machine-readable evidence result.

What a passing run establishes
------------------------------
Only this: at the named CDS revision, the structural and rule-level properties
listed in the result payload hold for the named inputs. It establishes **no**
accessibility conformance, **no** WCAG statement, **no** assistive-technology
behaviour, **no** comprehension, **no** Candidate status, and **no** admitted
AE-1. Automated evidence is input to a review, never the review.

Boundaries
----------
Offline; no network. Deterministic for identical inputs: no ambient timestamp,
no clock, no environment value, and no random source enters the payload. Strict
UTF-8 in and out. No repository discovery: every input and the output path are
explicit arguments. No source file is mutated and no Git operation is performed.

Dependencies: the Python standard library plus the repository's own canonical
digest implementation (``tools.cds_validator.canonicalization``, RFC 8785 +
SHA-256 per ADR-0002) and its duplicate-key-safe strict-JSON loader, so that
digests produced here are identical in method to every other CDS digest.

Usage (from the repository root, exactly as the validator CLI is invoked)::

    python -B -m tests.validator.semantic_status_candidate_evidence_runner \
        --cases tests/fixtures/semantic-status-statements/CANDIDATE_EVIDENCE_CASES.json \
        --token-source tokens/semantic/status/semantic-status.tokens.json \
        --terminology docs/foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md \
        --cds-revision <sha> --source-revision <rev> \
        --worktree-state "modified worktree" --output <out.json>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from tools.cds_validator import json_loader
from tools.cds_validator.canonicalization import (
    CANONICALIZATION_METHOD,
    DIGEST_ALGORITHM,
    content_digest,
)
from tools.cds_validator.semantic_status import (
    AUTHORIZED_AXES,
    EXPECTED_TOKEN_COUNT,
)

#: Identity of *this evidence result format only*. It is not a CDS schema, is
#: not registered under ``schemas/``, and carries no profile authority.
RESULT_SCHEMA_VERSION = (
    "cds-wp016-candidate-accessibility-evidence-result/1"
)

AXIS_ORDER: tuple[str, ...] = tuple(AUTHORIZED_AXES)

#: The five positive-default values `unknown` may never be mapped onto
#: (Composition Rules, fail-closed condition 3).
POSITIVE_DEFAULTS = frozenset({"nominal", "none", "verified", "current", "available"})

REVIEW_REQUIRED_IDS: tuple[str, ...] = ("RR-1", "RR-2", "RR-3", "RR-4", "RR-5", "RR-6")
FAIL_CLOSED_IDS: tuple[str, ...] = (
    "FC-1", "FC-2", "FC-3", "FC-4", "FC-5", "FC-6", "FC-7", "FC-8",
)

_AXIS_HEADING = re.compile(r"^##\s+Axis\s+`([a-z][a-z0-9-]*)`")
_TERM_ROW = re.compile(r"^\|\s*`([a-z][a-z0-9-]*)`\s*\|(.*)$")


def authorized_value_ids() -> tuple[str, ...]:
    """The 25 qualified technical identifiers, in vocabulary order."""
    return tuple(f"{axis}.{value}"
                 for axis, values in AUTHORIZED_AXES.items()
                 for value in values)


def _text(value) -> str:
    return value.strip() if isinstance(value, str) else ""


def evaluate(statement: dict) -> tuple[list[str], list[str]]:
    """Return ``(fail_closed_ids, review_required_ids)`` for one statement.

    The rules are transcribed from the normative Status Composition and
    Conflict Rules: six review-required combinations and eight fail-closed
    conditions. No seventh combination and no ninth condition is introduced,
    and no review-required state is reinterpreted as fail-closed.
    """
    axes = statement.get("axes") or {}
    representation = statement.get("representation") or {}
    remapping = statement.get("remapping")
    summary = statement.get("summary") or {}
    rationale = _text(statement.get("rationale"))
    observed = _text(statement.get("observedOrAssessedTime"))
    resolvable = statement.get("sourceOrEvidenceResolvable") is True

    fail_closed: list[str] = []
    # FC-1 — a mandatory axis is missing from the status object.
    if any(axis not in axes for axis in AXIS_ORDER):
        fail_closed.append("FC-1")
    # FC-2 — an unknown axis or value identifier is used.
    if any(axis not in AUTHORIZED_AXES or value not in AUTHORIZED_AXES[axis]
           for axis, value in axes.items()):
        fail_closed.append("FC-2")
    # FC-3 — `unknown` applied as a positive default.
    if any(axes.get(axis) == "unknown"
           and representation.get(axis) in POSITIVE_DEFAULTS
           for axis in AXIS_ORDER):
        fail_closed.append("FC-3")
    # FC-4 — stale or expired represented as current.
    if (axes.get("freshness") in ("stale", "expired")
            and representation.get("freshness") == "current"):
        fail_closed.append("FC-4")
    # FC-5 — unverified represented as verified.
    if (axes.get("confidence") == "unverified"
            and representation.get("confidence") == "verified"):
        fail_closed.append("FC-5")
    # FC-6 — not-applicable asserted without a rationale.
    if axes.get("evidence") == "not-applicable" and not rationale:
        fail_closed.append("FC-6")
    # FC-7 — unresolvable source/evidence identity where the values require it.
    if ((axes.get("confidence") == "verified" or axes.get("evidence") == "available")
            and not resolvable):
        fail_closed.append("FC-7")
    # FC-8 — a Product-Profile or consumer remapping loses axis meaning.
    if isinstance(remapping, dict) and remapping.get("preservesAxisMeaning") is False:
        fail_closed.append("FC-8")

    review_required: list[str] = []
    # RR-1 — nominal condition with major or critical severity.
    if axes.get("condition") == "nominal" and axes.get("severity") in ("major", "critical"):
        review_required.append("RR-1")
    # RR-2 — verified confidence with unavailable or unknown evidence.
    if (axes.get("confidence") == "verified"
            and axes.get("evidence") in ("unavailable", "unknown")):
        review_required.append("RR-2")
    # RR-3 — current freshness without a resolvable observed-or-assessed time.
    if axes.get("freshness") == "current" and not observed:
        review_required.append("RR-3")
    # RR-4 — not-applicable evidence without a rationale. The Composition Rules
    # list this state in the review-required table *and* state that it fails
    # closed; FC-6 above records the fail-closed half. Both are reported.
    if axes.get("evidence") == "not-applicable" and not rationale:
        review_required.append("RR-4")
    # RR-5 — unavailable condition with severity none.
    if axes.get("condition") == "unavailable" and axes.get("severity") == "none":
        review_required.append("RR-5")
    # RR-6 — `unknown` on any axis with an unqualified positive summary.
    carried = set(summary.get("qualifiersCarried") or [])
    unknown_axes = [axis for axis in AXIS_ORDER if axes.get(axis) == "unknown"]
    if (unknown_axes and summary.get("positive") is True
            and not all(axis in carried for axis in unknown_axes)):
        review_required.append("RR-6")

    return fail_closed, review_required


def classify(fail_closed: list[str], review_required: list[str]) -> str:
    if fail_closed:
        return "fail-closed"
    if review_required:
        return "review-required"
    return "representable"


def check_source_descriptions(token_source: Path) -> dict:
    """Text-first source rule: every authorized token carries a non-empty
    textual ``$description``. Existence only — never comprehension."""
    content = json_loader.load_path(token_source)
    status = content.get("status") if isinstance(content, dict) else None
    described: list[str] = []
    missing: list[str] = []
    for axis, values in AUTHORIZED_AXES.items():
        group = (status or {}).get(axis) or {}
        for value in values:
            token = group.get(value) or {}
            description = token.get("$description") if isinstance(token, dict) else None
            identifier = f"{axis}.{value}"
            if isinstance(description, str) and description.strip():
                described.append(identifier)
            else:
                missing.append(identifier)
    return {
        "expected": EXPECTED_TOKEN_COUNT,
        "described": len(described),
        "missing": missing,
        "satisfied": len(described) == EXPECTED_TOKEN_COUNT and not missing,
        "boundary": ("Existence of a textual description at the semantic source "
                     "layer only. Proves no comprehension, no accessibility, and "
                     "no conformance."),
    }


def check_de_en_structure(terminology: Path) -> dict:
    """Structural DE/EN coverage of the 25 authorized technical identifiers.

    Machine-checkable structure is not machine-checkable meaning: this verifies
    that a DE and an EN label exist for every authorized identifier exactly
    once. Whether a label preserves the canonical meaning is a human judgement
    and is explicitly not asserted here.
    """
    text = terminology.read_text(encoding="utf-8")
    axis = None
    rows: list[dict] = []
    for line in text.splitlines():
        heading = _AXIS_HEADING.match(line)
        if heading:
            axis = heading.group(1)
            continue
        match = _TERM_ROW.match(line)
        if not match or axis is None:
            continue
        cells = [cell.strip() for cell in match.group(2).split("|")]
        rows.append({
            "id": f"{axis}.{match.group(1)}",
            "axis": axis,
            "value": match.group(1),
            "enLabel": cells[0] if len(cells) > 0 else "",
            "deLabel": cells[1] if len(cells) > 1 else "",
        })

    authorized = authorized_value_ids()
    seen: dict[str, int] = {}
    for row in rows:
        seen[row["id"]] = seen.get(row["id"], 0) + 1
    duplicates = sorted(identifier for identifier, count in seen.items() if count > 1)
    unauthorized = sorted(identifier for identifier in seen if identifier not in authorized)
    missing = [identifier for identifier in authorized if identifier not in seen]
    without_en = sorted(row["id"] for row in rows if not row["enLabel"])
    without_de = sorted(row["id"] for row in rows if not row["deLabel"])
    satisfied = (
        len(rows) == len(authorized)
        and not duplicates and not unauthorized and not missing
        and not without_en and not without_de
    )
    return {
        "expected": len(authorized),
        "rows": len(rows),
        "englishLabels": len(rows) - len(without_en),
        "germanLabels": len(rows) - len(without_de),
        "duplicateIdentifiers": duplicates,
        "unauthorizedIdentifiers": unauthorized,
        "missingIdentifiers": missing,
        "rowsWithoutEnglishLabel": without_en,
        "rowsWithoutGermanLabel": without_de,
        "satisfied": satisfied,
        "boundary": ("Structural 1:1 coverage only. Semantic equivalence, "
                     "comprehension, and cultural suitability of the labels are "
                     "not machine-checked and are not asserted."),
    }


def run(cases_path: Path, token_source: Path, terminology: Path,
        cds_revision: str, source_revision: str,
        worktree_state: str = "unknown") -> dict:
    execution_errors: list[str] = []
    blocked: list[str] = []

    manifest = json_loader.load_path(cases_path)
    cases = manifest.get("cases") or []
    requirements = manifest.get("valueRequirements") or []

    case_by_id = {case.get("caseId"): case for case in cases}
    case_results: list[dict] = []
    failures: list[str] = []
    actual_review_required: set[str] = set()
    actual_fail_closed: set[str] = set()

    for case in cases:
        case_id = case.get("caseId")
        statement = case.get("statement")
        if not isinstance(statement, dict):
            blocked.append(case_id)
            execution_errors.append(f"{case_id}: no statement object")
            continue
        fail_closed, review_required = evaluate(statement)
        actual_fail_closed.update(fail_closed)
        actual_review_required.update(review_required)
        actual_classification = classify(fail_closed, review_required)
        expected_fc = sorted(case.get("expectedFailClosed") or [])
        expected_rr = sorted(case.get("expectedReviewRequired") or [])
        match = (
            actual_classification == case.get("expectedClassification")
            and sorted(fail_closed) == expected_fc
            and sorted(review_required) == expected_rr
        )
        if not match:
            failures.append(case_id)
        case_results.append({
            "caseId": case_id,
            "expectedClassification": case.get("expectedClassification"),
            "actualClassification": actual_classification,
            "expectedReviewRequired": expected_rr,
            "actualReviewRequired": sorted(review_required),
            "expectedFailClosed": expected_fc,
            "actualFailClosed": sorted(fail_closed),
            "expectedMatch": match,
            # Composition Rules fields 1 and 2. Reported as a separate
            # structural property; deliberately NOT folded into the eight
            # enumerated fail-closed conditions.
            "subjectIdentityPresent": bool(_text(statement.get("subjectIdentity"))),
            "declaredScopePresent": bool(_text(statement.get("declaredScope"))),
            "rationaleRequired": bool(review_required),
            "rationalePresent": bool(_text(statement.get("rationale"))),
        })

    # ---- 25/25 value-requirement coverage ----
    authorized = authorized_value_ids()
    by_requirement = {}
    duplicate_requirements: list[str] = []
    for requirement in requirements:
        identifier = requirement.get("id")
        if identifier in by_requirement:
            duplicate_requirements.append(identifier)
        by_requirement[identifier] = requirement
    unauthorized_requirements = sorted(
        identifier for identifier in by_requirement if identifier not in authorized)

    coverage_rows: list[dict] = []
    for identifier in authorized:
        requirement = by_requirement.get(identifier)
        axis, _, value = identifier.partition(".")
        if requirement is None:
            coverage_rows.append({
                "id": identifier, "axis": axis, "value": value,
                "evidenceType": None, "coverageState": "UNMAPPED",
                "caseIds": [], "missingCaseIds": [], "assertingCaseIds": [],
                "satisfied": False,
            })
            continue
        case_ids = list(requirement.get("caseIds") or [])
        missing_case_ids = [c for c in case_ids if c not in case_by_id]
        asserting = [
            c for c in case_ids
            if c in case_by_id
            and ((case_by_id[c].get("statement") or {}).get("axes") or {}).get(axis) == value
        ]
        coverage_rows.append({
            "id": identifier, "axis": axis, "value": value,
            "evidenceType": requirement.get("evidenceType"),
            "coverageState": requirement.get("coverageState"),
            "caseIds": case_ids,
            "missingCaseIds": missing_case_ids,
            "assertingCaseIds": asserting,
            "satisfied": bool(case_ids) and not missing_case_ids and bool(asserting)
            and requirement.get("coverageState") in (
                "COVERED", "COVERED_WITH_LIMITATION",
                "REPRESENTATION_TRIGGERED_WITH_PLAN"),
        })

    covered = [row for row in coverage_rows if row["satisfied"]]
    unmapped = [row["id"] for row in coverage_rows if not row["satisfied"]]

    review_coverage = sorted(actual_review_required)
    fail_closed_coverage = sorted(actual_fail_closed)

    descriptions = check_source_descriptions(token_source)
    de_en = check_de_en_structure(terminology)

    limitation_states = sorted({
        row["coverageState"] for row in coverage_rows
        if row["coverageState"] and row["coverageState"] != "COVERED"
    })

    all_satisfied = (
        not failures and not blocked and not execution_errors
        and not duplicate_requirements and not unauthorized_requirements
        and len(covered) == len(authorized)
        and review_coverage == list(REVIEW_REQUIRED_IDS)
        and fail_closed_coverage == list(FAIL_CLOSED_IDS)
        and descriptions["satisfied"] and de_en["satisfied"]
    )
    if execution_errors or blocked:
        result_status = "Blocked"
    elif not all_satisfied:
        result_status = "Fail"
    elif limitation_states:
        result_status = "Pass with limitations"
    else:
        result_status = "Pass"

    return {
        "schemaVersion": RESULT_SCHEMA_VERSION,
        "testOnly": True,
        "nonNormative": True,
        "authority": (
            "Executor-produced machine evidence. Not a CDS schema, not a "
            "validator contract, not a review, not an approval."),
        "workPackage": "CDS-WP-016",
        "evidenceScope": (
            "Channel-independent Layer-3 Semantic Status source and contract "
            "family. Source-level structural and rule-level checks only."),
        "cdsRevision": cds_revision,
        "sourceRevision": source_revision,
        # A 'modified worktree' execution binds to uncommitted content and must
        # never be presented as the committed revision's result.
        "worktreeState": worktree_state,
        "inputs": {
            "caseManifest": cases_path.as_posix(),
            "tokenSource": token_source.as_posix(),
            "terminology": terminology.as_posix(),
        },
        "caseManifestDigest": content_digest(manifest),
        "canonicalizationMethod": CANONICALIZATION_METHOD,
        "digestAlgorithm": DIGEST_ALGORITHM,
        "caseTotal": len(cases),
        "caseResults": case_results,
        "valueRequirementCoverage": {
            "expected": len(authorized),
            "covered": len(covered),
            "unmapped": unmapped,
            "duplicateRequirementIds": sorted(duplicate_requirements),
            "unauthorizedRequirementIds": unauthorized_requirements,
            "satisfied": len(covered) == len(authorized) and not unmapped,
            "rows": coverage_rows,
        },
        "reviewRequiredCoverage": {
            "expected": list(REVIEW_REQUIRED_IDS),
            "covered": review_coverage,
            "satisfied": review_coverage == list(REVIEW_REQUIRED_IDS),
        },
        "failClosedCoverage": {
            "expected": list(FAIL_CLOSED_IDS),
            "covered": fail_closed_coverage,
            "satisfied": fail_closed_coverage == list(FAIL_CLOSED_IDS),
        },
        "sourceDescriptionCoverage": descriptions,
        "deEnStructuralCoverage": de_en,
        "failures": failures,
        "blocked": blocked,
        "executionErrors": execution_errors,
        "resultStatus": result_status,
        "coverageStatesWithLimitation": limitation_states,
        "scoreProduced": False,
        "boundaries": {
            "maturityState": "Experimental",
            "approvalState": "Unapproved",
            "candidateStatus": "Not Candidate",
            "admittedAccessibilityEvidenceLevel": "AE-0",
            "evidenceLevelProduced": (
                "Provisional AE-1 candidate — pending fresh independent review"),
            "claims": "none",
            "conformanceStatement": "none",
            "humanApproval": "none",
            "note": (
                "A passing run is machine evidence for the named inputs at the "
                "named revision. It is not accessibility, not a WCAG statement, "
                "not admitted AE-1, not a Candidate award, and not human "
                "approval. No numeric or percentage accessibility score exists."),
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="semantic_status_candidate_evidence_runner",
        description=("CDS-WP-016 test-only Candidate accessibility evidence "
                     "runner. Produces machine evidence, never a claim."))
    parser.add_argument("--cases", required=True, type=Path)
    parser.add_argument("--token-source", required=True, type=Path)
    parser.add_argument("--terminology", required=True, type=Path)
    parser.add_argument("--cds-revision", required=True)
    parser.add_argument("--source-revision", required=True)
    parser.add_argument("--worktree-state", required=True,
                        choices=("clean", "modified worktree", "unknown"))
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)

    payload = run(args.cases, args.token_source, args.terminology,
                  args.cds_revision, args.source_revision, args.worktree_state)
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    with open(args.output, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)

    status = payload["resultStatus"]
    if status == "Blocked":
        return 2
    return 0 if status.startswith("Pass") else 1


if __name__ == "__main__":
    sys.exit(main())
