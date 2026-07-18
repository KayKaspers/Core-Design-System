# WP-016 Candidate Gate Recommendation

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Semantic Status Foundation Independent
  Evidence Review and Candidate Gate
- **Date:** 2026-07-18
- **Status:** **Independent Evidence Reviewer recommendation to Nova.** This is
  a review recommendation, **not** a promotion. The reviewer does **not** award
  Candidate, does not record Nova or Human-Maintainer approval, and does not
  change any decision, risk, ADR, or project-status file. **Candidate: no;
  dossier stays Draft.**

## Result

- **Independent review status: PASS.**
- **Candidate Recommendation: GO** — in the strict sense defined below: the
  independent review is clean and Nova may proceed to its own Candidate-gate
  review. GO here is **not** a Candidate award and asserts no Candidate, Stable,
  approved, promoted, or conformant status.

## Gate rule applied

Per the review contract, GO requires **all** of: 0 Blocking, 0 High, complete
re-execution, consistent digests, complete traceability, semantically
consistent terminology, no open gate ambiguity, and a dossier correctly and
fully marked as Draft. There is **no** GO WITH NOTES and **no** conditional GO.

| Gate criterion | State |
| --- | --- |
| Blocking findings | **0** |
| High findings | **0** |
| Re-execution (103 tests, 24/24 cases, source set) | **complete, passed** |
| Digest consistency (23 fixture + 3 source, vs committed) | **all identical** |
| Traceability (5 axes, 25 values/tokens, identity) | **complete** |
| Terminology parity (25 DE / 25 EN) | **semantically consistent** |
| Open gate ambiguity | **none** |
| Dossier marked Draft | **yes — remains "Draft – Candidate gate incomplete"** |

All GO conditions are met. The residual items are Observations only (below);
none weakens the Candidate scope, all are visible in the dossier as
limitations, and none threatens truth, accessibility, or evidence identity —
so per the gate rule they may remain at GO.

## Findings

Severity scale: Blocking · High · Medium · Low · Observation.

### WP016-OBS-001 — Source-set evidence provenance stamp is pre-commit
- **Severity:** Observation
- **Evidence:** [wp015-semantic-status-source-digests.json](../../artifacts/validation/wp015-semantic-status-source-digests.json)
- **Reference:** DEC-S-013, DEC-S-100
- **Description:** The committed WP-015 source-digest evidence records
  `repositoryRevision: 943229d…` (the WP-014 commit) and
  `worktreeState: modified worktree` — it was produced pre-commit on a dirty
  tree. This is an honestly-recorded, expected metadata difference, not a
  content difference.
- **Reproduction:** The reviewer re-ran at the **clean committed HEAD** and
  obtained **identical content digests** (`8d127cf…`, `879933…`, `61e64f…`).
- **Candidate impact:** none — content digests reproduce exactly; the metadata
  difference is in the "expected differences" class.
- **Correction:** none required. Optionally, Nova may note that a post-commit
  clean-tree re-stamp would tidy provenance; the reviewer's clean-HEAD run
  already supplies that assurance.
- **Recommendation:** accept as Observation.

### WP016-OBS-002 — Source-set V4 label is "Not assessed", not "Pass with limitations"
- **Severity:** Observation
- **Evidence:** [wp016-independent-source-results.json](../../artifacts/validation/wp016-independent-source-results.json)
- **Reference:** DEC-S-097, DEC-S-118
- **Description:** The Candidate Plan characterizes the source-set outcome as
  "Pass with limitations", while the validator reports the V4 **scope
  aggregate** as `Not assessed` (objective status checks executed with 0 error
  diagnostics; informational `CDS-V4-NOT-ASSESSED` residue only). The tool has
  no "Pass with limitations" verdict for a single `validate-file` layer; the
  behaviour is by design and matches the committed evidence and the unit tests.
- **Reproduction:** identical result independently reproduced (V1–V3 Pass, V4
  Not assessed, block none, not Fail, not Blocked).
- **Candidate impact:** none — the substance (no Fail, no Blocked, objective
  status subset passed) is unchanged; only the label wording differs from the
  prose.
- **Correction:** none required; a wording clarification in prose (not in the
  tool) could align the two, at Nova's discretion.
- **Recommendation:** accept as Observation.

### WP016-OBS-003 — Resolver `outputIdentity` digest-state wording is imprecise
- **Severity:** Observation
- **Evidence:** [semantic-status.resolver.json](../../tokens/semantic/status/semantic-status.resolver.json)
- **Reference:** DEC-S-031, DEC-S-079
- **Description:** The resolver's `outputIdentity.digestState.status` reads
  "Not computed – validator implementation pending". The offline validator is
  implemented, but there is no resolution/output-generation step (the CLI
  offers no `resolve` command), so the *resolved output* digest genuinely is
  not computed. The substance is correct; only the phrase "validator
  implementation pending" is imprecise (it should read as resolution/output
  generation pending).
- **Reproduction:** `python -m tools.cds_validator --help` lists only
  `version`, `validate-file`, `validate-cases`, `digest`; the resolver still
  validates V1–V3 Pass.
- **Candidate impact:** none — does not affect outcomes, traceability, or the
  gate; the source set validates cleanly.
- **Correction:** none by the reviewer (source is out of review-mutation
  scope). Nova may schedule a cosmetic wording correction as a separate
  Standard change.
- **Recommendation:** accept as Observation.

### Severity counts (independent count)

| Severity | Count |
| --- | --- |
| Blocking | 0 |
| High | 0 |
| Medium | 0 |
| Low | 0 |
| Observation | 3 |

## Candidate prerequisites (Candidate Plan)

After a clean independent review, the following prerequisites may be
**recommended as satisfied** to Nova — and no more:

| # | Prerequisite | Reviewer recommendation |
| --- | --- | --- |
| 2 | WP-013 validator evidence independently reviewed / re-executed | **Satisfiable** — re-executed and reviewed independently |
| 3 | Evidence Reviewer authorized | **Satisfiable** — this fresh, separate session |
| 4 | Machine-readable Semantic Source Set implemented | **Satisfiable** — `semantic/status`, independently traced |
| 5 | Validator harness passed for the source set (V1–V4, committed expected) | **Satisfiable** — 24/24, source set not Fail/Blocked |
| 6 | No Blocking/High defects open | **Satisfiable** — 0 Blocking, 0 High |
| 7 | Accessibility and content review completed | **Satisfiable** — independently reviewed (AE-0, no claim) |
| 8 | DE/EN parity reviewed | **Satisfiable** — 25/25, independently reviewed |

**Remain open and NOT satisfiable by the reviewer:**

- **Prerequisite 1** — Human-Maintainer commit of the contract WP (governance
  record; outside this review).
- **Prerequisite 9 — Nova review** with a promotion recommendation.
- **Prerequisite 10 — Human-Maintainer approval** of the maturity transition.

## Gate state

- **Nova gate:** **open.**
- **Human-Maintainer gate:** **open.**
- **Promotion state:** **Not Candidate.** The reviewer awards nothing; unclear
  readiness at any later gate resolves as NO-GO (DEC-S-048).

## What GO means and does not mean

GO means: from the independent Evidence Reviewer's standpoint, the committed
WP-013 and WP-015 evidence re-executes cleanly, reproduces the committed
digests exactly, is fully traceable, and carries no Blocking/High defect — so
Nova may open its Candidate-gate review. GO does **not** mean Candidate,
approved, promoted, Stable, or conformant, and it starts no pilot and creates
no claim.

## Related documents

- [Independent Re-Execution Review](WP016_INDEPENDENT_REEXECUTION_REVIEW.md)
- [Source and Contract Traceability Review](WP016_SOURCE_CONTRACT_TRACEABILITY_REVIEW.md)
- [Terminology, Accessibility and Content Review](WP016_TERMINOLOGY_ACCESSIBILITY_CONTENT_REVIEW.md)
- [Semantic Status Candidate Dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md)
- [First Semantic Status Candidate Plan](../roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md)
