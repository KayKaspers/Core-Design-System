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
