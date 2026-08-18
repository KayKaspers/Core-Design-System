# First Semantic Status Candidate Plan

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-014 — Semantic Status Foundation Contract and First
  Candidate Plan
- **Date:** 2026-07-17
- **Status:** **A plan, not a promotion.** Pending Human-Maintainer commit.
  **Nothing is Candidate today** (DEC-S-113, DEC-S-114); this document defines
  what the first Candidate would be and what must be true first.
- **Update (CDS-WP-015):** CDS-WP-014 is committed; the machine-readable source
  set, the DE/EN terminology mapping, and the status fixtures exist.
- **Update (CDS-WP-016, 2026-08-17):** the ten-prerequisite list below is
  **incomplete** relative to the normative **Candidate accessibility gate**. The
  current, binding prerequisite view is the additive section
  [Candidate accessibility gate — additive correction](#candidate-accessibility-gate--additive-correction-cds-wp-016-2026-08-17)
  near the end of this document. Everything before it is retained as the
  historical CDS-WP-014 / CDS-WP-015 record. **Candidate remains No.**

## Target artifact

The first planned CDS design Candidate is the **Semantic Status Foundation
Contract** together with its future **machine-readable Semantic Source Set**
(DEC-S-113) — a meaning foundation, deliberately not a visual one: the first
thing CDS commits to at Candidate maturity is *truthful status semantics*, the
area with the strongest multi-consumer evidence (CR-006, CR-007).

## Candidate scope

Included:

- the **five axes** and their **25 axis values**
  ([Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md));
- the **ten invariants**
  ([Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md));
- the **combination and conflict rules** including review-required
  combinations and fail-closed states
  ([Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md));
- the **communication contract** (textual meaning, multi-modal, qualifiers,
  channel preservation —
  [Communication Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md));
- the **token role contract**
  ([Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md));
- **DE/EN semantic parity** of status meaning.

## Exclusions

Not part of the first Candidate: visual values of any kind (colour,
typography, icons, spacing, motion, themes); UI components; CoreOps or any
consumer integration; Product Profiles; mobile/non-web implementations; any
Stable status; any conformance, adoption, or accessibility claim. Scope
expansion into these areas before the contract and evidence are ready is a
registered risk (RISK-089) and a NO-GO trigger, not a stretch goal.

## Candidate Package

*(The reviewable bundle the promotion decision will be made on — 8 elements.)*

| # | Element | State in CDS-WP-014 |
| --- | --- | --- |
| 1 | Normative human-readable Status Contract (the four foundations documents) | Drafted (Experimental) |
| 2 | Machine-readable Semantic Source Set (`.tokens.json`, CDS profile v1, DTCG 2025.10) | **Implemented (CDS-WP-015)** — [`semantic/status`](../../tokens/semantic/status/semantic-status.tokens.json), Experimental |
| 3 | Localization and terminology mapping DE/EN | **Created (CDS-WP-015)** — [25/25 mapping](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md), executor-drafted |
| 4 | Positive and negative validation fixtures for status semantics | **Created (CDS-WP-015)** — 1 positive + 8 negative under `tests/fixtures/semantic-status/` |
| 5 | Validation execution evidence (offline validator, machine-readable results, digests) | **Produced (CDS-WP-015)** — 24/24 harness + source-set run, executor-produced, independently unreviewed |
| 6 | Accessibility and content review evidence (non-visual meaning, DE/EN parity, understandability) | **Drafted (CDS-WP-015)** — executor-produced contract reviews; no user research, AE-0 |
| 7 | Known limitations register for the Candidate | **Recorded (CDS-WP-015)** — inside the [dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md) |
| 8 | Candidate dossier (Elevated change dossier binding 1–7) | **Draft (CDS-WP-015)** — gate incomplete (DEC-S-122) |

## Candidate prerequisites

*(All gates, cumulative — none is met or waived by CDS-WP-014.)*

1. **CDS-WP-014 committed** by the Human Maintainer.
2. **WP-013 validator evidence independently reviewed** — or re-executed and
   then independently reviewed (executor ≠ reviewer, DEC-S-103; currently
   `independentReviewState: pending`).
3. **Evidence Reviewer authorized** (Nova or a separately authorized reviewer,
   DEC-S-045).
4. **Machine-readable Semantic Source Set implemented** under the CDS Token
   Format Profile.
5. **Validator harness passed for that source set** (V1–V4 with committed
   expected outcomes; machine-readable, revision-bound evidence).
6. **No Blocking or High defects** open against the contract or source set
   (accessibility defect model applies).
7. **Accessibility and content review completed** (multi-modal meaning,
   unknown/limitation language, understandability).
8. **DE/EN parity reviewed** (semantic parity, no contradictory translations).
9. **Nova review** with a promotion recommendation.
10. **Human-Maintainer approval** of the maturity transition (Experimental →
    Candidate; DEC-S-036 — Candidate is mandatory before Stable and is itself
    gated).

## Evidence plan

- **Structural evidence:** completeness of axes/values (5/25), ID uniqueness
  and naming-profile conformance, absence of prohibited aggregations,
  source-set and profile validation (schemas + V1–V3), reference and
  provenance integrity (manifest/resolver binding, revision-bound identities).
- **Semantic evidence:** meaning review of all 25 values; combination and
  conflict coverage (all six review-required combinations exercised; all
  eight fail-closed states provoked by negative fixtures); the
  unknown/stale/evidence invariants demonstrated end-to-end; no contradictory
  inferences derivable.
- **Accessibility and content evidence:** non-visual expressibility of every
  value; DE/EN parity; clear unknown- and limitation-communication; label
  flexibility; applicability to future interactive use (keyboard/screenreader
  obligations stated and reviewable).
- **Consumer evidence:** **none exists in CDS-WP-014.** Later at minimum: a
  bounded CoreOps reconciliation against concrete tasks and states (read-only,
  revision-bound, DEC-S-013), without activating the pilot before its entry
  criteria (RISK-018). Consumer evidence informs the Candidate review; it is
  not a pilot start.

## Gate state after CDS-WP-015

Prerequisite 1 (WP-014 committed) is met; 4 and parts of 5 are implemented but
their evidence is executor-produced and **independently unreviewed**;
prerequisites 2–3 and 6–10 remain open. **Candidate Status: Not Candidate.**
Detail: [Candidate Dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md).

## Known blockers

*(**Historical — the CDS-WP-014 snapshot, retained unchanged.** Items 1–3 have
since been overtaken by events and are **not** the current blocker list; see
[Current blockers](#current-blockers-cds-wp-016-2026-08-17) below.)*

1. WP-013 evidence is executor-produced and **independently unreviewed**
   (RISK-078) — prerequisite 2 is open.
2. No machine-readable source set exists (prerequisites 4–5 open).
3. No accessibility/content/parity review evidence exists (prerequisites 6–8
   open; every artifact was AE-0 **when these blockers were recorded**).
4. Licensing/publication state unchanged (`Private Development`) — publication
   is out of scope for the Candidate and remains blocked separately.

## Human-Maintainer decisions required

Commit of CDS-WP-014 · authorization of the independent Evidence Review ·
authorization of CDS-WP-015 · the eventual maturity transition itself. None of
these is made, implied, or scheduled by this plan.

## No-promotion statement

**CDS-WP-014 promotes nothing.** The Semantic Status Foundation remains
**Experimental**; the WP-013 harness result is a bounded, executor-produced
observation and **no Candidate evidence** (DEC-S-104). Unclear readiness at any
future gate resolves as NO-GO, never as "go with notes" (DEC-S-048).

## Next work package

**CDS-WP-015 — Semantic Status Foundation Source Set and Candidate Evidence**
(registered as Next; not executed): the machine-readable Semantic Source Set
(value-neutral roles and identifiers), positive/negative status fixtures,
validator execution with committed expected outcomes, accessibility/content
evidence preparation, and Candidate-dossier preparation — still without visual
values and without a Candidate award. Execution requires an explicit Nova
prompt and Human-Maintainer authorization.

## Candidate accessibility gate — additive correction (CDS-WP-016, 2026-08-17)

*(Additive. Nothing above is deleted or rewritten. The ten prerequisites above
were the plan as CDS-WP-014 wrote them, and they remain the historical record of
what that work package believed sufficient.)*

### What was wrong with the plan

**The ten-prerequisite list is incomplete.** It omits the **Candidate
accessibility gate**, which is normative for accessibility-relevant artifacts and
sits at a **higher authority** than this roadmap document: it lives in the
[Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md#candidate-accessibility-gate)
and is referenced by the
[Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md).

The Semantic Status Foundation **is** accessibility-relevant — it carries the
Unknown invariant, the text-first obligation, and the DE/EN parity requirement —
so the gate always applied. The plan simply did not name it.

The practical consequence was concrete and is recorded as **GAP-H-01**: the
CDS-WP-016 independent evidence review was scoped against *this plan*, returned a
clean **PASS / GO**, and could do so while the nine-requirement accessibility gate
remained wholly unaddressed. **A review is bounded by the checklist it is given.**

**This is not a retroactive edit.** The original plan is not being made to look as
though it always contained the gate. It did not, and the omission is part of the
record.

### The Candidate decision now additionally requires all nine

*(Cumulative **with** prerequisites 1–10 above, not instead of them.)*

| # | Candidate accessibility gate requirement | Artifact | State |
| --- | --- | --- | --- |
| 1 | WCAG applicability mapping | [Candidate WCAG Applicability Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md) | Produced — **independently reviewed (PASS WITH NOTES)** |
| 2 | Responsibility mapping | [Candidate Accessibility Responsibility Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_RESPONSIBILITY_MAPPING.md) | Produced — **independently reviewed (PASS WITH NOTES)** |
| 3 | Known accessibility requirements | [Candidate Evidence Requirements Matrix](../operations/SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md) — 25/25 mapped, 0 unmapped | Produced — **independently reviewed (PASS WITH NOTES)** |
| 4 | **AE-1** | [Clean Re-execution Evidence Record](../operations/SEMANTIC_STATUS_CANDIDATE_AE1_CLEAN_REEXECUTION_EVIDENCE_RECORD.md) · [Admission Record](../governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md) | **ADMITTED** — `AE1-CDS-WP016-SEMSTATUS-002`, source scope only |
| 5 | Relevant AE-2 evidence, **or a reasoned evidence plan** | [Candidate AE-2 Evidence Plan](../governance/SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md) | Produced — **independently reviewed (PASS WITH NOTES)**. AE-2 execution is **not meaningful** against an artifact with no interactive surface, and fabricating it is prohibited. |
| 6 | Known limitations | [Candidate Accessibility Limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md) — 16 entries, 0 Critical | Produced — **independently reviewed (PASS WITH NOTES)** |
| 7 | Support baseline plan | [Candidate Support Baseline Plan](../governance/SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md), on A11Y-BL-001 freshness **`Current`** ([review](../reviews/WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md)) | Produced — **independently reviewed (PASS WITH NOTES)** |
| 8 | Regression plan | [Candidate Accessibility Regression Plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md) — 15 triggers | Produced — **independently reviewed (PASS WITH NOTES)** |
| 9 | **Human-Maintainer approval after Nova review** | — | **OPEN.** Not addressable by an executor and not satisfied by any artifact above. |

**Two distinct review events are cited above and must not be conflated.** The
verdict **PASS WITH NOTES** in requirements 1–3 and 5–8 is the *Fresh Independent
Remediation Implementation Review* of those artifacts. The **PASS** behind
requirement 4 is the separate *Fresh Independent Clean-HEAD Evidence Review* of
Evidence 002. Neither review is an approval, and neither awards Candidate status
([provenance](../reviews/WP016_ACCESSIBILITY_REMEDIATION_REVIEW_PROVENANCE.md)).

### Channel-profile applicability

Per **DEC-S-125**, this Candidate is a **channel-independent Layer-3 semantic
source and contract** and is assessed under its **source-level** accessibility
gate; it is **not** assigned an artificial channel. Every later channel
representation remains subject to its own Channel Accessibility Profile with its
own evidence (DEC-S-058), and **evidence transfers in neither direction**.

## Current blockers (CDS-WP-016, 2026-08-17)

*(This list supersedes the historical CDS-WP-014 "Known blockers" section above
as the **current** view. The historical list is retained, not corrected in
place.)*

| # | Current blocker |
| --- | --- |
| 1 | ~~No fresh independent review of the accessibility-gate remediation exists.~~ **CLOSED** — a fresh independent review returned **PASS WITH NOTES** on the remediation and **PASS** on the clean-HEAD evidence ([provenance](../reviews/WP016_ACCESSIBILITY_REMEDIATION_REVIEW_PROVENANCE.md)). |
| 2 | ~~AE-1 is provisional, not admitted.~~ **CLOSED** — `AE1-CDS-WP016-SEMSTATUS-002` was **admitted at AE-1** by the Human Maintainer on 2026-08-17, for the channel-independent source/contract scope only ([admission record](../governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md)). All other CDS artifacts remain AE-0. |
| 3 | **Nova post-admission Candidate Maturity Re-Review is open** — the earlier Nova Candidate Maturity Review returned **NO-GO** because this gate was unmet, and has not yet been re-run on the remediated and now-admitted package. |
| 4 | **Human-Maintainer Candidate approval is open** (gate requirement 9, DEC-S-036). |
| 5 | **No AE-2, AE-3, or AE-4 exists**, and no execution environment is available for any Required baseline pairing (RISK-051). |
| 6 | Licensing and publication state unchanged (**`Private Development`**) — out of scope for the Candidate and blocked separately. |

**Superseded from the historical list:** blocker 1 (WP-013 evidence
independently unreviewed) was closed by the CDS-WP-016 independent evidence
review (**PASS**); blocker 2 (no machine-readable source set) was closed by
CDS-WP-015; blocker 3 (no accessibility/content/parity review evidence) is
partially closed — contract-level reviews exist and **AE-1 is now admitted for the
source scope**, but **no user research and no AT execution** exist.

### Current status

**Candidate: No. Maturity: Experimental. Approval: Unapproved. Admitted
accessibility evidence level: AE-1 for the channel-independent Semantic Status
source/contract family only (AE-0 for every other CDS artifact). Claims: none.
CDS-WP-017: not activated.**

**AE-3 and AE-4 are not Candidate prerequisites for this source-only Candidate** —
the normative Candidate gate does not require them. They remain future **Stable**,
channel, consumer, and claim requirements. No waiver is created by saying so.

The independent evidence review's **GO stands** in its declared narrow sense and
is **not revoked** — see the
[Candidate Accessibility Gate Addendum](../reviews/WP016_CANDIDATE_ACCESSIBILITY_GATE_ADDENDUM.md).
**GO is not a Candidate award**, and unclear readiness at any gate resolves as
**NO-GO**, never as "go with notes" (DEC-S-048).

## Related documents

- [Candidate Accessibility Gate Addendum](../reviews/WP016_CANDIDATE_ACCESSIBILITY_GATE_ADDENDUM.md)
- [Semantic Status Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
- [Semantic Status Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md)
- [Readiness Review](../reviews/SEMANTIC_STATUS_FOUNDATION_READINESS_REVIEW.md)
- [Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md)
- [Pre-Candidate Operating Plan](PRE_CANDIDATE_OPERATING_PLAN.md)
- [Offline Token Validator Execution Review](../reviews/OFFLINE_TOKEN_VALIDATOR_EXECUTION_REVIEW.md)
