# Semantic Status Candidate Dossier

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-015 — Semantic Status Foundation Source Set and
  Candidate Evidence
- **Date:** 2026-07-18
- **Status: Draft – Candidate gate incomplete.** This dossier follows the
  [Elevated Change Dossier](ELEVATED_CHANGE_DOSSIER_TEMPLATE.md) discipline
  for the planned first Candidate. **A populated dossier is not an approval**
  (DEC-S-122): the Candidate decision requires independent evidence review,
  Nova review, and Human-Maintainer approval — all open.
  **Candidate Status = Not Candidate.**

## Target artifact

The **Semantic Status Foundation**: the normative contract family (CDS-WP-014)
plus the machine-readable Semantic Source Set **`semantic/status`**
(CDS-WP-015) — the first planned CDS design Candidate (DEC-S-113).

## Scope

Five axes · 25 axis values · ten invariants · combination/conflict rules ·
communication/accessibility contract · token role contract · DE/EN semantic
parity · the `semantic/status` source set with manifest and resolver.

## Exclusions

Visual values of any kind, UI components, CoreOps/consumer integration,
Product Profiles, mobile/non-web implementations, Stable status, and every
conformance/adoption/accessibility claim. Scope expansion is a NO-GO trigger
(RISK-089).

## Normative sources

[Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) ·
[Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) ·
[Composition Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) ·
[Communication Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md) ·
[Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md) ·
[Terminology DE/EN](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md)

## Machine-readable source set, manifest, and resolver

[semantic-status.tokens.json](../../tokens/semantic/status/semantic-status.tokens.json)
(25 tokens, 5 axes, Experimental, Unapproved) ·
[semantic-status.source-set.json](../../tokens/semantic/status/semantic-status.source-set.json) ·
[semantic-status.resolver.json](../../tokens/semantic/status/semantic-status.resolver.json)
— identity `semantic/status`, revision `semantic-status-rev-0001`, local-only,
no Product-Profile extension points.

## Validation evidence

- WP-013 clean re-execution on the committed WP-014 revision: 71/71 tests,
  **15/15 matches, worktree clean**
  ([review](../reviews/WP013_VALIDATOR_EVIDENCE_REEXECUTION_REVIEW.md)).
- Full 24-case harness: **24/24 expected/actual matches** (9 new status
  cases; [results](../../artifacts/validation/wp015-fixture-results.json)).
- Source-set execution: V1–V3 Pass, V4 objective status checks passed, exit 0
  ([review](../reviews/SEMANTIC_STATUS_SOURCE_SET_EXECUTION_REVIEW.md)).
- 103/103 unit tests; RFC 8785 + SHA-256 digests for source set (3) and
  fixtures (23).

## Accessibility and content evidence

[Accessibility and Content Review](../reviews/SEMANTIC_STATUS_ACCESSIBILITY_AND_CONTENT_REVIEW.md)
— executor-produced **contract** review; no user research, no AT execution,
no WCAG claim; every artifact AE-0.

## Localization evidence

[Localization Parity Review](../reviews/SEMANTIC_STATUS_LOCALIZATION_PARITY_REVIEW.md)
— 25/25 DE, 25/25 EN, 0 missing rows; executor-produced; comprehension
unvalidated.

## Known limitations

Bounded DTCG V2 coverage (DEC-S-098) · V4 validates the vocabulary shape, not
meaning quality or channel truthfulness (RISK-093) · fixture coverage may miss
unrepresented invalid states (RISK-094) · single-environment execution
(RISK-075) · executor self-confirmation across implementation, fixtures, and
reviews (RISK-078) · no consumer evidence yet.

## Defects

None known and open against the contract family or the source set at dossier
time. Any Blocking/High defect found in review re-opens this dossier.

## Compatibility

First introduction of the `semantic/status` source set — no consumer depends
on it; no compatibility promise exists (pre-1.0, Experimental). The 25 value
IDs and the `status.<axis>.<value>` paths become compatibility-relevant only
at Candidate; renames are migration events (DEC-S-082, RISK-092).

## Migration

Not applicable (first introduction; nothing migrates). Future path/ID changes
require migration references per DEC-S-082.

## Product-Profile boundary

No approved extension points exist (`approvedExtensionPoints: []`); no
Product Profile may reference or remap the status vocabulary (DEC-S-112,
DEC-S-124).

## Consumer boundary

No consumer integration exists or is authorized; the Experimental source set
must not be consumed, distributed, or represented as approved before the
Candidate gate (RISK-097, DEC-S-124). CoreOps pilot inactive.

## Evidence Reviewer

**Open — not yet authorized.** Must be Nova or a separately authorized
reviewer; never the executor (DEC-S-045, DEC-S-121).

## Nova review

**Open** — Candidate-gate review pending.

## Human-Maintainer approval

**Open** — final maturity authority (DEC-S-036).

## Candidate decision

### Gate state after CDS-WP-015

Present: WP-014 committed · machine-readable source set implemented ·
validator harness executed (24/24) · executor-produced structural evidence ·
executor-produced accessibility/content review · executor-produced DE/EN
parity review.

Open: independent review of the WP-013 and WP-015 evidence · authorized
independent Evidence Reviewer · Nova Candidate-gate review · Human-Maintainer
Candidate approval.

### Decision

**Not Candidate.** The decision field stays empty until every open gate
closes; unclear readiness resolves as NO-GO (DEC-S-048).

## CDS-WP-016 Independent Evidence Review (additive)

*(Added by CDS-WP-016. This section is additive; the dossier status remains
**Draft – Candidate gate incomplete** and **Candidate = No**. The reviewer
awards nothing.)*

### Evidence Reviewer identity

Claude Opus 4.8 (`claude-opus-4-8`), a fresh session with no inherited executor
context, authorized by the Human Maintainer as a **separate** Evidence Reviewer
(reviewer ≠ executor; DEC-S-045, DEC-S-103, DEC-S-121).

### Review scope and revision

Independent review of the committed WP-013 validator evidence and WP-015
semantic-status evidence: clean-tree re-execution, digest comparison,
source/contract traceability, terminology parity, and accessibility/content
contract review. **Review revision:** the committed HEAD containing CDS-WP-015,
reviewed on a **clean** working tree.

### Independent re-execution

Fresh venv outside the repository, exact `requirements-validator.lock` pins
(7/7), Python 3.12.10, offline after install:

- **103/103** unit tests; **24/24** cases with **24/24** expected/actual
  matches; **0** mismatches, **0** execution errors; result-schema validation
  passed.
- Source set: V1–V3 Pass, V4 Not assessed (objective status checks passed, 0
  status errors), block `none` — not Fail, not Blocked.
- **23** fixture content digests + **1** undigestible, and **3** source content
  digests — **all identical** to the committed WP-015 evidence.
- Schema `$id` unchanged; case-schema change additive; CLI unchanged;
  `VAL-CASE-001…015` byte-identical; `VAL-CASE-016…024` schema-valid; no gate
  evasion.

Evidence: [wp016-independent-fixture-results.json](../../artifacts/validation/wp016-independent-fixture-results.json) ·
[wp016-independent-fixture-digests.json](../../artifacts/validation/wp016-independent-fixture-digests.json) ·
[wp016-independent-source-results.json](../../artifacts/validation/wp016-independent-source-results.json) ·
[wp016-independent-source-digests.json](../../artifacts/validation/wp016-independent-source-digests.json).
Reviews: [Re-Execution](../reviews/WP016_INDEPENDENT_REEXECUTION_REVIEW.md) ·
[Traceability](../reviews/WP016_SOURCE_CONTRACT_TRACEABILITY_REVIEW.md) ·
[Terminology/Accessibility/Content](../reviews/WP016_TERMINOLOGY_ACCESSIBILITY_CONTENT_REVIEW.md).

### Findings

**0 Blocking · 0 High · 0 Medium · 0 Low · 3 Observations** — provenance stamp
of the source-set evidence is pre-commit (WP016-OBS-001), source-set V4 label
is "Not assessed" vs the "Pass with limitations" prose (WP016-OBS-002), and the
resolver `outputIdentity` wording is imprecise (WP016-OBS-003). None weakens the
Candidate scope or threatens truth, accessibility, or evidence identity. Detail:
[Candidate Gate Recommendation](../reviews/WP016_CANDIDATE_GATE_RECOMMENDATION.md).

### Independent review outcome and Candidate recommendation

Independent review **PASS**; **Candidate Recommendation: GO** in the strict
review sense — the independent review is clean and Nova may open its
Candidate-gate review. GO is **not** a Candidate award and asserts no
Candidate, Stable, approved, promoted, or conformant status.

### Still-open gates

- **Evidence Reviewer:** authorized and complete for this run (supersedes the
  "Open" note above for the WP-016 review only).
- **Nova review:** **open** — Candidate-gate review and promotion recommendation.
- **Human-Maintainer approval:** **open** — final maturity authority (DEC-S-036).

**Candidate Status = Not Candidate.** The decision field stays empty until the
Nova and Human-Maintainer gates close.
