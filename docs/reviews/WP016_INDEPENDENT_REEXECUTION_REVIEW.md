# WP-016 Independent Re-Execution Review

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Semantic Status Foundation Independent
  Evidence Review and Candidate Gate
- **Date:** 2026-07-18
- **Evidence class:** **Independent re-execution evidence**, produced by an
  Evidence Reviewer who is **not** the CDS-WP-013 / CDS-WP-015 executor
  (DEC-S-045, DEC-S-103, DEC-S-121). This document reviews committed evidence
  by independent re-execution; it **grants no maturity** — **Candidate: no**
  (DEC-S-115, DEC-S-124).

## Reviewer identity and independence

- **Reviewer:** Claude Opus 4.8 (`claude-opus-4-8`), fresh session, highest
  reasoning effort, **no inherited context** from the WP-013 or WP-015 executor
  sessions.
- **Authorization:** the Human Maintainer authorized this fresh session as a
  separate Evidence Reviewer by initiating the CDS-WP-016 review prompt.
- **Boundary:** the reviewer changed no implementation, schema, fixture,
  validation case, source set, expected outcome, decision, risk, or ADR, and
  performed no Git write action. The review is read-only against the
  implementation and the contract.

## Independent runtime

A fresh virtual environment was created **outside** the repository and
installed **only** from [`requirements-validator.lock`](../../requirements-validator.lock).

| Property | Value |
| --- | --- |
| Python | **3.12.10** (CPython, win32 / Windows 11) |
| Direct dependencies | `jsonschema==4.26.0`, `rfc8785==0.1.4` |
| Transitive dependencies | `attrs==26.1.0`, `jsonschema-specifications==2025.9.1`, `referencing==0.37.0`, `rpds-py==2026.6.3`, `typing_extensions==4.16.0` |
| Pin agreement | **7/7 exact** against the lock file (`pip freeze` compared) |
| Install source | `requirements-validator.lock` exact pins |
| Runtime network | **none after install** — the validator ran fully offline |
| Validator identity | `validatorVersion 0.1.0`, `cdsProfileVersion 1`, `dtcgReportVersion 2025.10` |

The exact pins installed and executed reproducibly; **no** installation into
the repository, **no** global or executor venv, **no** runtime pin change.

## A. Unit tests

`python -m unittest discover -s tests` on the pinned runtime:

- **103 tests collected, 103 passed, 0 failures, 0 errors** — matches the
  committed expectation of 103 exactly.

## B. Full fixture harness

`validate-cases` over
[`VALIDATION_CASES.json`](../../tests/fixtures/machine-readable/VALIDATION_CASES.json):

| Metric | Independent result |
| --- | --- |
| Cases executed | **24** (`VAL-CASE-001…024`, in order) |
| Expected/actual matches | **24 / 24** |
| Mismatches | **0** |
| Execution errors | **0** |
| Exit code | **0** |
| Result-schema validation | **Pass** (0 errors against `cds-validation-result`, reviewer-verified) |

The duplicate-key case (`VAL-CASE-008`) **blocked at V1** and received **no
content digest** (DEC-S-100). The status cases were **actually executed**:
`VAL-CASE-016` passed **V4**, and `VAL-CASE-017…024` each failed at **V4** with
their primary semantic-status diagnostic category — the objective status V4
checks run despite the `testOnly`/`nonNormative` fixture flags (DEC-S-118).

Per-case actuals, blocking layers, and diagnostic categories are recorded in
[wp016-independent-fixture-results.json](../../artifacts/validation/wp016-independent-fixture-results.json).

## C. Source-set validation

`validate-file` on
[semantic-status.tokens.json](../../tokens/semantic/status/semantic-status.tokens.json)
with the [manifest](../../tokens/semantic/status/semantic-status.source-set.json)
and [resolver](../../tokens/semantic/status/semantic-status.resolver.json) in
scope:

| Layer | Independent result |
| --- | --- |
| V1 | **Pass** |
| V2 | **Pass** (bounded DTCG scope, DEC-S-098) |
| V3 | **Pass** |
| V4 | **Not assessed** (scope aggregate) — objective semantic-status checks executed with **0 status-error diagnostics**; only the informational `CDS-V4-NOT-ASSESSED` residue remains for the non-objective V4 aspects |

Blocking layer `none`, exit **0** — **not Fail, not Blocked** (the
"Pass with limitations" sense of the Candidate Plan). Recorded in
[wp016-independent-source-results.json](../../artifacts/validation/wp016-independent-source-results.json).

## D. Digests

- **23** parsable harness fixtures received `sha256:` content digests; **1**
  (duplicate-key) is correctly undigestible — matches the committed WP-015
  count exactly.
- **3** source-set content digests (token document, manifest, resolver).
- Canonicalization **RFC 8785 (JCS)**, digest **SHA-256** — an integrity aid,
  not a signature or authenticity statement (DEC-S-100).

## Comparison with committed WP-015 executor evidence

| Dimension | Result |
| --- | --- |
| Unit-test count (103) | identical |
| Case count (24) and order | identical |
| Expected/actual matches (24/24) | identical |
| Per-case actuals, blocking layers, diagnostic categories | **identical for all 24** |
| Fixture content digests (23) | **all identical** |
| Undigestible input (duplicate-key) | identical |
| Source-set results (V1–V3 Pass, V4 Not assessed, block none) | identical |
| Source-set diagnostics (3× `CDS-V4-NOT-ASSESSED`) | identical |
| Source content digests (3) | **all identical** (`8d127cf…`, `879933…`, `61e64f…`) |

**Acceptable (expected) differences:** timestamps, execution identity, and
reviewer runtime identity. The committed WP-015 source-digest evidence records
`repositoryRevision: 943229d…` (the WP-014 commit) and
`worktreeState: modified worktree` (produced pre-commit); the reviewer ran at
the **clean committed HEAD** containing WP-015. **No content digest, case
outcome, diagnostic category, test count, schema/source identity, or
expected/actual match differed.**

## Regression and schema-correction check

- **Schema `$id` unchanged** for both `cds-validation-case` and
  `cds-validation-result` (compared WP-014 commit `943229d` → HEAD).
- The `cds-validation-case` change is **purely additive**: nine
  `semantic-status-*` diagnostic categories appended to the closed enum, and
  the `fixturePath` pattern widened additively — the machine-readable branch is
  preserved unchanged and a semantic-status token-only branch is added; the
  pattern stays anchored and forbids other roots, subfolders, backslashes, and
  path escapes.
- **CLI unchanged** (`git diff 943229d HEAD -- tools/cds_validator/cli.py` is
  empty).
- `VAL-CASE-001…015` are **byte-identical** (no removed or modified lines in
  the cases file); `VAL-CASE-016…024` are present, gap-free, and schema-valid.
- **No gate evasion:** unknown diagnostic categories and unauthorized fixture
  roots remain rejected (unit-tested).

## Findings

No Blocking and no High finding arose from re-execution. Transparency
observations are recorded centrally in the
[Candidate Gate Recommendation](WP016_CANDIDATE_GATE_RECOMMENDATION.md).

## Limitations

Single machine and single OS/Python environment (RISK-075); the harness proves
revision-clean reproducibility on this environment, not cross-environment
reproducibility and not correctness. Bounded DTCG V2 coverage (DEC-S-098) and
objective-only V4 (RISK-093) apply unchanged. A green re-execution confers no
Candidate, Stable, conformance, or claim status (DEC-S-104, DEC-S-124).

## Related documents

- [Source and Contract Traceability Review](WP016_SOURCE_CONTRACT_TRACEABILITY_REVIEW.md)
- [Terminology, Accessibility and Content Review](WP016_TERMINOLOGY_ACCESSIBILITY_CONTENT_REVIEW.md)
- [Candidate Gate Recommendation](WP016_CANDIDATE_GATE_RECOMMENDATION.md)
- [Semantic Status Candidate Dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md)
- [Offline Token Validator Usage](../operations/OFFLINE_TOKEN_VALIDATOR_USAGE.md)
