# CDS-WP-015 — Semantic Status Foundation Source Set and Candidate Evidence — Notes

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-015 (Completed via the Nova-authorized resume run;
  pending Human-Maintainer commit)
- **Date:** 2026-07-18
- **Executor:** Claude (scoped executor). All evidence herein is
  **executor-produced and independently unreviewed** (DEC-S-121).

## Assignment

Implement the first real, still-Experimental machine-readable Semantic Status
source set with manifest, resolver, DE/EN terminology, status-specific validator
rules, fixtures, additional validation cases, a revision-clean WP-013
re-execution, structural/accessibility/content/localization evidence, and a Draft
Candidate Dossier — explicitly without creating a Candidate.

## The BLOCKED first run and the Nova-authorized schema correction

- **Previous BLOCKED run:** the first CDS-WP-015 run ended correctly as BLOCKED
  with **zero repository changes**. Mechanical conflict: the committed
  validation-case schema restricted `fixturePath` to
  `tests/fixtures/machine-readable/(positive|negative)/…` while the mandate
  placed the new fixtures under `tests/fixtures/semantic-status/…`; the
  unmodifiable CLI blocks schema-invalid case matrices with exit 2 before
  execution, making VAL-CASE-016…024 and 24/24 matches mechanically
  unreachable. The conflict was proven by probe (semantic-status path → 1 schema
  error; machine-readable path → 0 errors).
- **Nova authorization:** Nova reviewed and confirmed the blocker and authorized
  a **minimal additive correction** of `schemas/cds-validation-case.schema.json`
  as the single additional Allowed File (51 total).
- **Old pattern:**
  `^tests/fixtures/machine-readable/(positive|negative)/[a-z0-9-]+\.(tokens|source-set|resolver)\.json$`
- **New additive pattern:**
  `^tests/fixtures/(?:(?:machine-readable)/(?:positive|negative)/[a-z0-9-]+\.(?:tokens|source-set|resolver)\.json|(?:semantic-status)/(?:positive|negative)/[a-z0-9-]+\.tokens\.json)$`
  — semantic-status admits **token documents only**; other roots, subfolders,
  network paths, backslashes, path escapes, and other extensions stay rejected.
- **New diagnostic categories (9, additive):** `semantic-status-axis`,
  `-value`, `-unknown`, `-count`, `-path-value`, `-collision`, `-aggregate`,
  `-visual-leakage`, `-identity`. Existing categories unchanged and not
  reinterpreted.
- **Unchanged schema identity:** `$id`
  `tag:github.com,2026:KayKaspers/Core-Design-System/schema/cds-validation-case/1`,
  `$schema` draft 2020-12, title, case-ID contract, V1…V4 result vocabulary,
  required fields — all verified unchanged by test.
- **VAL-CASE-001…015 unchanged:** the matrix was extended append-only; byte
  identity of the first 15 cases against the committed state is verified in the
  final validation (git diff shows pure insertion after case 15).
- **Regression tests:** 10 targeted tests in `test_semantic_status.py`
  (old paths validate · new token paths validate · foreign roots rejected ·
  semantic-status source-set/resolver paths rejected · backslashes rejected ·
  path escape rejected · all 9 new categories accepted · unknown categories
  rejected · full 24-case matrix validates · `check_schema` passes) — all green.
- **CLI unchanged:** `tools/cds_validator/cli.py` was not touched (verified via
  git status); the **fail-closed schema gate is preserved** — the CLI still
  blocks any schema-invalid matrix with exit 2; the 24-case run passed *through*
  the gate, not around it. **No harness or gate evasion occurred.**
- Governance references kept visible: RISK-064 (schema contract completeness),
  RISK-066 (schema/validator divergence), RISK-070 (fixture coverage),
  RISK-071 (expectation drift). Per the resume prompt, **no new Decision or ADR
  was created for the correction itself**.

## Preflight (resume run)

Repository/branch/origin correct; working tree clean; HEAD `943229d`
(CDS-WP-014) ✓; WP-015 Next, no WP-016 ✓; Decisions 114, Risks 89
(82 Monitored / 7 Mitigating), ADRs 3 ✓; foundation counts 5/25 (+`unknown`
everywhere)/10 ✓; schema `$id` intact ✓; no partial semantic-status or tokens
artifacts ✓; skills 38 dirs / 39 files, manifest 39/39 (verified this session;
tree clean on committed state) ✓. Fail-closed conditions: none triggered.

## Clean-tree re-execution (this run, before any repository change)

On HEAD `943229d`, clean tree, pinned venv (Python 3.12.10, jsonschema 4.26.0,
rfc8785 0.1.4): **71/71 unit tests; 15/15 cases with 15/15 matches; 0
mismatches; 0 internal errors; 14 digests; duplicate-key fixture undigestible;
`repositoryRevision` = WP-014 commit; `worktreeState: clean`;
`independentReviewState: pending`; exit 0.** Outputs written to the session
scratchpad first, then adopted as
`artifacts/validation/wp015-wp013-clean-reexecution-{results,digests}.json`.
Review: [WP-013 Re-Execution Review](../docs/reviews/WP013_VALIDATOR_EVIDENCE_REEXECUTION_REVIEW.md).

## Implementation summary

- **Source set** `tokens/semantic/status/`: token document (5 axis groups, 25
  non-visual `string` tokens, values = technical IDs, revision
  `semantic-status-rev-0001`, Experimental/Unapproved, no testOnly flags — it is
  the real source, not a fixture), manifest (`semantic/status/manifest`, empty
  `approvedExtensionPoints`, provenance Bound, digest state Computed with
  method/algorithm; digest values live in evidence), resolver
  (`semantic/status/resolver`, localOnly, one ordered step).
- **Validator extension** `semantic_status.py` + 9 `CDS-V4-STATUS-*` specs in
  `diagnostics.py` + V4 integration in `validation.py` with the mandated
  ordering: status checks run first for `status`-vocabulary documents
  (fixture flags never disable them); generic non-objective V4 aspects stay
  `Not assessed`/`Not applicable with rationale`; non-status fixtures keep the
  WP-013 behavior. Prohibited segments split into aggregate
  (health/overall/score/aggregate/success) and visual
  (color/icon/shape/position/motion) classes.
- **Fixtures:** 1 positive (complete vocabulary) + 8 negative, each with exactly
  one primary failure reason; case-only collision realized at value level
  (`"Nominal"`), because key-level uppercase collisions are already blocked
  structurally by the token-document schema at V3 — key-level detection is
  covered by a direct checker unit test.
- **Cases:** VAL-CASE-016…024 appended (24 total); expected outcomes defined by
  this WP: positive V1–V4 Pass; negatives V1–V3 Pass, V4 Fail, blocking V4,
  primary `semantic-status-*` category; documented secondary
  `semantic-status-count` diagnostics on five negatives.
- **Terminology:** 25/25 DE/EN entries with prohibited shortenings
  (`supported` ≠ „verifiziert/geprüft"; `unknown` never neutral success;
  `not-applicable` keeps its rationale in every locale).
- **Tests:** +32 new (30 in `test_semantic_status.py`, +2 net in the harness
  test) → **103 total, 103 passed**.

## Executed evidence

- **Harness:** 24/24 executed, **24/24 expected/actual matches**, 0 mismatches,
  0 internal errors, exit 0 →
  `artifacts/validation/wp015-fixture-{results,digests}.json`
  (23 digests; duplicate-key undigestible; worktree `modified worktree` —
  honestly bound to the uncommitted WP-015 state).
- **Source set:** `validate-file` with manifest+resolver → V1 Pass · V2 Pass ·
  V3 Pass · V4 `Not assessed` (scope aggregate; the token document's objective
  status-V4 checks executed and passed; manifest/resolver carry only
  non-objective V4 residue), exit 0 — **not Fail, not Blocked** →
  `artifacts/validation/wp015-semantic-status-source-{results,digests}.json`
  (3 `sha256:` digests: token doc, manifest, resolver).
- **Reviews (4, executor-produced):** re-execution, source-set execution,
  accessibility/content (contract review; no user research, no AT execution, no
  WCAG claim; AE-0), localization parity (25/25/0).
- **Dossier:** [Draft – Candidate gate incomplete](../docs/operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md);
  present vs. open gates explicitly tabled; **Candidate Status = Not Candidate**.

## Registers and status files

DEC-S-115…124 added (124 total, contiguous; DEC-S-001…114 unchanged; no new
ADR, count 3). RISK-090…097 added (97 total; 90 Monitored / 7 Mitigating —
distribution derived from the register; no existing status changed; no
acceptance/closure). WP-014 documents reconciled additively (contract,
vocabulary, token contract, candidate plan, readiness review); validator docs
and implementation plan updated; the eight status files updated (WP-015
Completed, WP-016 Next).

## Deviations

1. The first run's BLOCKED outcome and this resume run are documented above —
   the correction was executed exactly as authorized, nothing beyond it.
2. The V4 scope aggregate for the source-set run is `Not assessed` (not `Pass`),
   because manifest/resolver have no objective V4 checks; the prompt's
   requirement ("not Fail or Blocked") is met with exit 0. Documented rather
   than engineered away.
3. The nine skills already fully read in this session were applied from context;
   no skill file outside the twelve authorized was used.

## Open items

Independent review of WP-013 and WP-015 evidence (reviewer ≠ executor) ·
authorized Evidence Reviewer · Nova Candidate-gate review · Human-Maintainer
approval — all open by design (CDS-WP-016).

## Completion status

**PASS** against the original Definition of Done plus the resume-run additions.
No Git write action was performed; publication `Private Development`; no
Candidate, no claim; pilot inactive.
