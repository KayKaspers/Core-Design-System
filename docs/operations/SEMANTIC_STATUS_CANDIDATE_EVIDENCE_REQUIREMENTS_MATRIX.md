# Semantic Status Candidate Evidence Requirements Matrix

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Accessibility Gate Remediation
- **Date:** 2026-08-17
- **Status:** **Operational coverage record — NOT normative, NOT evidence by
  existence, NOT an approval.** It maps the 25 per-value **Candidate evidence
  requirements** stated in the normative
  [Status Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) onto the
  evidence that exists today. The Vocabulary remains the normative source; this
  document changes none of it.

## Why this document exists

The read-only Candidate Accessibility Gate gap assessment recorded **GAP-H-02**:
the Vocabulary states a Candidate evidence requirement for **every one of the 25
authorized values**, and those requirements were not fully mapped to evidence.
An unmapped requirement is a silent gap, and a silent gap at a Candidate gate is
exactly what fail-closed governance exists to prevent.

**GAP-H-02 is Candidate-promotion-blocking.** This matrix closes the *mapping*.
It does not close the gate.

## What a row does and does not establish

- A row records **which evidence exists** for a requirement, of **which kind**,
  with **which limitation**.
- A row is **not** a pass, **not** an accessibility statement, **not** a WCAG
  statement, and **not** a Candidate decision.
- `COVERED_WITH_LIMITATION` is **not automatically Candidate-compatible.**
  Whether a stated limitation is acceptable for Candidate is a judgement for the
  fresh independent reviewer, then Nova, then the Human Maintainer — never for
  the executor and never for this table.

## Evidence types

| Type | Meaning |
| --- | --- |
| `MACHINE` | An offline, deterministic, re-executable check produces the evidence. |
| `HUMAN_REVIEW` | The requirement is a meaning or understandability judgement no machine check in this remediation performs. |
| `MIXED` | A machine check covers a structural part; a human judgement covers the rest. |
| `REPRESENTATION_TRIGGERED` | The requirement becomes assessable only once a rendered or interactive representation exists. |

## Coverage states

| State | Meaning |
| --- | --- |
| `COVERED` | Evidence exists for the requirement as stated, within the source-level scope. |
| `COVERED_WITH_LIMITATION` | Evidence exists but does not reach the whole requirement; the limitation is stated in the row and in the [limitations set](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md). |
| `REPRESENTATION_TRIGGERED_WITH_PLAN` | Not assessable at source-only scope; a dated plan and trigger exist. |
| `UNMAPPED` | **Not permitted.** A single `UNMAPPED` row fails this remediation. |

**Current distribution: 22 `COVERED` · 3 `COVERED_WITH_LIMITATION` · 0
`REPRESENTATION_TRIGGERED_WITH_PLAN` · 0 `UNMAPPED`.**

## Evidence sources referenced by the rows

| Key | Path |
| --- | --- |
| `CASES` | [`tests/fixtures/semantic-status-statements/CANDIDATE_EVIDENCE_CASES.json`](../../tests/fixtures/semantic-status-statements/CANDIDATE_EVIDENCE_CASES.json) — test-only, non-normative |
| `RUNNER` | [`tests/validator/semantic_status_candidate_evidence_runner.py`](../../tests/validator/semantic_status_candidate_evidence_runner.py) |
| `SUITE` | [`tests/validator/test_semantic_status_candidate_evidence.py`](../../tests/validator/test_semantic_status_candidate_evidence.py) |
| `RESULTS` | [`artifacts/validation/wp016-candidate-accessibility-remediation-results.json`](../../artifacts/validation/wp016-candidate-accessibility-remediation-results.json) |
| `TOKENS` | [`tokens/semantic/status/semantic-status.tokens.json`](../../tokens/semantic/status/semantic-status.tokens.json) |
| `TERMS` | [`docs/foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md`](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md) |
| `A11Y-REVIEW` | [Semantic Status Accessibility and Content Review](../reviews/SEMANTIC_STATUS_ACCESSIBILITY_AND_CONTENT_REVIEW.md) — executor-produced |
| `PARITY-REVIEW` | [Semantic Status Localization Parity Review](../reviews/SEMANTIC_STATUS_LOCALIZATION_PARITY_REVIEW.md) — executor-produced |
| `IND-REVIEW` | [WP-016 Terminology, Accessibility and Content Review](../reviews/WP016_TERMINOLOGY_ACCESSIBILITY_CONTENT_REVIEW.md) — independent |
| `STATUS-FIX` | `tests/fixtures/semantic-status/` — 1 positive + 9 negative token fixtures |

## Matrix — 25 value rows

*(One row per authorized technical value. `Result` is the machine or review
outcome for the row's evidence, never a gate outcome.)*

| # | Axis | Technical value | Candidate evidence requirement (paraphrased from the Vocabulary) | Evidence type | Evidence case IDs | Evidence sources | Result | Known limitation | Coverage state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `condition` | `condition.nominal` | Positive and negative fixtures plus executed validation, including at least one case where `nominal` coexists with a non-positive value on another axis. | MACHINE | SSC-EV-001, SSC-EV-002 | CASES, RUNNER, RESULTS, STATUS-FIX | Expected/actual match; the unqualified positive summary over an unknown axis is caught as RR-6. | None at source scope. | COVERED |
| 2 | `condition` | `condition.degraded` | Fixture coverage distinguishing `degraded` from `disrupted` and `unavailable`. | MACHINE | SSC-EV-003, SSC-EV-004, SSC-EV-005 | CASES, RUNNER, RESULTS | Three distinct representable/review states with distinct minimum context. | None at source scope. | COVERED |
| 3 | `condition` | `condition.disrupted` | Fixture coverage distinguishing `disrupted` from `degraded` (partial quality loss) and `unavailable` (no service); affected declared functions nameable. | MACHINE | SSC-EV-004, SSC-EV-003, SSC-EV-005 | CASES, RUNNER, RESULTS | Affected function named in the case context. | None at source scope. | COVERED |
| 4 | `condition` | `condition.unavailable` | Fixture coverage including the `unavailable`-with-low-severity review case. | MACHINE | SSC-EV-005 | CASES, RUNNER, RESULTS | RR-5 fires; rationale recorded. | None at source scope. | COVERED |
| 5 | `condition` | `condition.unknown` | Negative fixtures proving an omitted or unknown condition never validates as a positive one. | MACHINE | SSC-EV-006, SSC-EV-007 | CASES, RUNNER, RESULTS, STATUS-FIX | Omission fails closed (FC-1); `unknown → nominal` fails closed (FC-3). | None at source scope. | COVERED |
| 6 | `severity` | `severity.none` | Fixture coverage of `none` combined with non-nominal conditions. | MACHINE | SSC-EV-005 | CASES, RUNNER, RESULTS | `unavailable + none` represented and caught as RR-5. | None at source scope. | COVERED |
| 7 | `severity` | `severity.minor` | Boundary fixtures between `minor` and `major`. | MACHINE | SSC-EV-008, SSC-EV-009 | CASES, RUNNER, RESULTS | Both sides of the declared threshold represented. | The threshold itself belongs to a declared scope, not to CDS; no numeric boundary is fixed. | COVERED |
| 8 | `severity` | `severity.major` | Review-combination fixture `nominal + major`, valid only with an explicit rationale. | MACHINE | SSC-EV-009 | CASES, RUNNER, RESULTS | RR-1 fires; rationale recorded. | None at source scope. | COVERED |
| 9 | `severity` | `severity.critical` | Fixtures for `critical` with each non-unknown condition value, including the review-required pairs. | MACHINE | SSC-EV-010, SSC-EV-011, SSC-EV-012, SSC-EV-013 | CASES, RUNNER, RESULTS | All four non-unknown condition values paired; `nominal + critical` caught as RR-1. | None at source scope. | COVERED |
| 10 | `severity` | `severity.unknown` | Negative fixtures proving `severity: unknown` never validates as `none`. | MACHINE | SSC-EV-014 | CASES, RUNNER, RESULTS | `unknown → none` fails closed (FC-3). | None at source scope. | COVERED |
| 11 | `confidence` | `confidence.verified` | Negative fixtures where `verified` with `evidence: unavailable`/`unknown` fails review; positive fixtures with a resolvable evidence identity. | MACHINE | SSC-EV-015, SSC-EV-016, SSC-EV-017 | CASES, RUNNER, RESULTS | Both review cases fire RR-2; the resolvable-identity case is representable. | None at source scope. | COVERED |
| 12 | `confidence` | `confidence.supported` | DE/EN parity checks that no localized label upgrades `supported` toward verified. | MIXED | SSC-EV-018 | CASES, RUNNER, RESULTS, TERMS, PARITY-REVIEW, IND-REVIEW | Structural DE/EN coverage 25/25 with a distinct DE and EN label per identifier; the case asserts `supported` with no upgrading representation. | **Whether a German label semantically upgrades toward `verifiziert` is a meaning judgement that no machine check performs.** It rests on the executor-produced parity review and the independent terminology/accessibility/content review. See limitation SSC-LIM-011. | COVERED_WITH_LIMITATION |
| 13 | `confidence` | `confidence.uncertain` | Content-review evidence that uncertain language stays understandable (Content and Cognitive Accessibility, area 5). | HUMAN_REVIEW | SSC-EV-032 | CASES, RUNNER, RESULTS, A11Y-REVIEW, IND-REVIEW | The machine case proves representability and that the uncertainty qualifier is carried into the summary. | **Understandability is a human judgement; no user research exists and none is claimed.** See limitations SSC-LIM-001 and SSC-LIM-011. | COVERED_WITH_LIMITATION |
| 14 | `confidence` | `confidence.unverified` | Negative fixtures proving `unverified → verified` renaming or remapping fails closed. | MACHINE | SSC-EV-019, SSC-EV-020 | CASES, RUNNER, RESULTS | Representation route fails closed (FC-5); remapping route fails closed (FC-8). | None at source scope. | COVERED |
| 15 | `confidence` | `confidence.unknown` | Fixtures where `confidence: unknown` blocks unqualified positive summaries. | MACHINE | SSC-EV-002 | CASES, RUNNER, RESULTS | RR-6 fires; the qualifier-carrying variant does not. | None at source scope. | COVERED |
| 16 | `freshness` | `freshness.current` | Negative fixture: `current` without a documented time fails review. | MACHINE | SSC-EV-021 | CASES, RUNNER, RESULTS | RR-3 fires on a missing observed-or-assessed time. | None at source scope. | COVERED |
| 17 | `freshness` | `freshness.aging` | Band-boundary fixtures (current/aging/stale) with declared windows. | MACHINE | SSC-EV-022, SSC-EV-017, SSC-EV-001 | CASES, RUNNER, RESULTS | All three bands represented; the aging case names both declared boundaries. | Band boundaries belong to a declared scope; CDS fixes no interval. | COVERED |
| 18 | `freshness` | `freshness.stale` | Negative fixtures proving stale-as-current representations fail closed. | MACHINE | SSC-EV-023 | CASES, RUNNER, RESULTS, STATUS-FIX | FC-4 fires. | None at source scope. | COVERED |
| 19 | `freshness` | `freshness.expired` | Fixtures distinguishing `stale` from `expired` semantics. | MACHINE | SSC-EV-024, SSC-EV-023 | CASES, RUNNER, RESULTS | The expired case names the hard validity rule and the moment it was passed; the stale case names the advisory threshold. | None at source scope. | COVERED |
| 20 | `freshness` | `freshness.unknown` | Fixtures with missing or uncertain time metadata validating only as `unknown`. | MACHINE | SSC-EV-025, SSC-EV-021 | CASES, RUNNER, RESULTS | Undated statement is representable only as `unknown`; claiming `current` without a time is review-required. | None at source scope. | COVERED |
| 21 | `evidence` | `evidence.available` | Fixtures with resolvable versus unresolvable evidence identities. | MACHINE | SSC-EV-017, SSC-EV-026 | CASES, RUNNER, RESULTS | Resolvable case representable; unresolvable case fails closed (FC-7). | Availability is not correctness; the fixture asserts access, never quality. | COVERED |
| 22 | `evidence` | `evidence.partial` | Fixtures where hiding partiality fails review. | MACHINE | SSC-EV-027 | CASES, RUNNER, RESULTS | Partial evidence hidden behind an unqualified positive summary is caught as RR-6 because an axis carries `unknown`. | **Hiding partiality is invariant 6, which the six normative review-required combinations do not enumerate on its own.** A summary hiding partiality while no axis carries `unknown` is not detected by the current machine rules; it stays a human review obligation. No seventh combination was invented. See limitation SSC-LIM-012. | COVERED_WITH_LIMITATION |
| 23 | `evidence` | `evidence.unavailable` | The `verified + unavailable` review-combination fixture. | MACHINE | SSC-EV-015 | CASES, RUNNER, RESULTS | RR-2 fires with a recorded rationale naming the access restriction as a limitation. | None at source scope. | COVERED |
| 24 | `evidence` | `evidence.not-applicable` | Negative fixture: `not-applicable` without a rationale fails. | MACHINE | SSC-EV-028, SSC-EV-029 | CASES, RUNNER, RESULTS | Without a rationale the state carries RR-4 **and** FC-6 and classifies as fail-closed; with a rationale it is representable. | None at source scope. | COVERED |
| 25 | `evidence` | `evidence.unknown` | Fixtures proving `unknown` evidence blocks evidence-backed phrasing. | MACHINE | SSC-EV-030 | CASES, RUNNER, RESULTS | Evidence-backed phrasing is modelled as representing the axis as `available`; with the asserted value `unknown` that fails closed (FC-3). | None at source scope. | COVERED |

## Counts

| Metric | Value |
| --- | --- |
| Required rows (one per authorized value) | **25** |
| Mapped rows | **25** |
| `COVERED` | **22** |
| `COVERED_WITH_LIMITATION` | **3** (rows 12, 13, 22) |
| `REPRESENTATION_TRIGGERED_WITH_PLAN` | **0** |
| `UNMAPPED` | **0** |
| Evidence type `MACHINE` | **23** |
| Evidence type `MIXED` | **1** (row 12) |
| Evidence type `HUMAN_REVIEW` | **1** (row 13) |
| Evidence type `REPRESENTATION_TRIGGERED` | **0** |

**Independent re-count:** table data rows above: 5 + 5 + 5 + 5 + 5 = **25**;
`unknown` appears exactly once per axis = **5**. Any mismatch between these
counts and the table is a defect in this document and fails closed.

## Machine coverage sentinels

Produced by `RUNNER` and recorded in `RESULTS`:

| Sentinel | Value |
| --- | --- |
| Value-requirement coverage | **25 / 25** |
| Review-required combination coverage | **6 / 6** (RR-1 … RR-6) |
| Fail-closed condition coverage | **8 / 8** (FC-1 … FC-8) |
| Source `$description` coverage | **25 / 25** |
| DE/EN structural coverage | **25 / 25** (25 EN labels, 25 DE labels) |
| Execution errors | **0** |
| Expected/actual mismatches | **0** |

## What this matrix does not do

- It **awards no Candidate status.** Candidate remains **No**; maturity remains
  **Experimental**; approval remains **Unapproved**.
- It **admits no AE-1.** The evidence produced alongside it is a *provisional*
  AE-1 package pending a fresh independent review; the admitted accessibility
  evidence level of every CDS artifact remains **AE-0**.
- It **creates no claim** of any kind.
- It **replaces no normative source.** Where this matrix and the
  [Status Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) disagree,
  the Vocabulary wins and this document is corrected.

## Related documents

- [Status Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md)
- [Status Composition and Conflict Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md)
- [Semantic Status Candidate AE-1 Evidence Record](SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md)
- [Semantic Status Candidate Accessibility Limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md)
- [Semantic Status Candidate Dossier](SEMANTIC_STATUS_CANDIDATE_DOSSIER.md)
- [First Semantic Status Candidate Plan](../roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md)
