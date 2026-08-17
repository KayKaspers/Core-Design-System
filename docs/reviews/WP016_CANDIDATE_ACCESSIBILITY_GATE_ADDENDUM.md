# CDS-WP-016 — Candidate Accessibility Gate Addendum

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Accessibility Gate Remediation
- **Date:** 2026-08-17
- **Addendum to:** [WP-016 Candidate Gate Recommendation](WP016_CANDIDATE_GATE_RECOMMENDATION.md)
- **Status:** **Additive review-history record — NOT normative, NOT evidence,
  NOT a revocation.**

## Why this addendum exists, and why it is a separate file

The [Candidate Gate Recommendation](WP016_CANDIDATE_GATE_RECOMMENDATION.md) is
**historical independent review evidence**. It records what an independent
reviewer actually found, at a specific revision, within a specific declared
scope.

**It has not been edited, and it must not be.** Retrospectively editing a review
to match a later finding would destroy the one property that makes review
evidence worth anything: that it says what was found *at the time*, and can be
checked against that. Evidence history stays truthful even when it turns out to
be incomplete — especially then.

This addendum therefore records what happened **after** that review, alongside
it.

## What the original review established

| # | Finding | Status |
| --- | --- | --- |
| 1 | **Independent Evidence Review: PASS** | **Unchanged and not revoked.** |
| 2 | **Candidate Recommendation: GO**, in the strict review sense | **Unchanged and not revoked.** |
| 3 | Reviewer ≠ executor; a fresh session with no inherited executor context, Human-Maintainer authorized | Unchanged |
| 4 | Independent re-execution reproduced the committed evidence exactly: 103/103 unit tests, 24/24 cases with 24/24 matches, 0 mismatches, 0 execution errors, all 23 fixture and 3 source digests identical | Unchanged |
| 5 | **0 Blocking · 0 High · 0 Medium · 0 Low · 3 Observations** (WP016-OBS-001…003) | Unchanged and preserved |

**The GO was earned and it stands.** Nothing in this addendum contradicts any
finding in it.

## What the GO actually authorized

This is the point the addendum exists to make precise, because "GO" is a word that
travels further than its declared scope.

| GO **did** mean | GO **did not** mean |
| --- | --- |
| The independent review of the **WP-013 validator evidence and the WP-015 semantic-status evidence** was clean. | That the Candidate accessibility gate had been evaluated. |
| The re-execution, digest comparison, traceability, terminology, and accessibility/content **contract** reviews found nothing Blocking or High. | That accessibility evidence existed. Every artifact was, and is, **AE-0**. |
| **Nova may open its Candidate-gate review.** | That Nova's review would conclude anything in particular. |
| The evidence was no longer "executor-produced and independently unreviewed". | **Candidate.** The recommendation itself said GO is not a Candidate award. |

The original review's declared scope was the **technical evidence** — its
re-execution, its integrity, its traceability, and its content. **The full
nine-requirement Candidate accessibility gate was not within that scope, and the
review did not evaluate or close it.** That is not a defect in the review; it is
what the review was asked to do.

## What happened after

| # | Event | Outcome |
| --- | --- | --- |
| 1 | **Nova Candidate Maturity Review** — opened on the strength of the GO | **NO-GO.** Reason: the **Candidate Accessibility Gate is unmet**. The gate is normative for accessibility-relevant artifacts and requires nine things, of which the technical evidence review covers none directly. |
| 2 | **Read-only Candidate Accessibility Gate gap assessment** | Decision: **`CANDIDATE_ACCESSIBILITY_GATE_GAP_CONFIRMED`**. Promotion readiness: **`NOT_READY_FOR_CANDIDATE_PROMOTION`**. Accessibility relevance: **`ACCESSIBILITY_RELEVANT`**. **9 / 9 gate requirements not yet demonstrated as satisfied.** Findings: 7 Blocking (GAP-B-01 … GAP-B-07), 2 High (GAP-H-01, GAP-H-02), 4 Medium (GAP-M-01 … GAP-M-04), 1 Low (GAP-L-01). |
| 3 | **Human-Maintainer authorization** (2026-08-17) | **CDS-WP-016 Candidate Accessibility Gate Remediation authorized** as internal rework of CDS-WP-016 — **not** a new work package. The Nova resolution of GAP-B-07 was accepted; **DEC-S-125** was authorized as a normative clarification; **GAP-H-02** was declared closable-before-promotion. |
| 4 | **Remediation executed** (this work package) | The nine gate requirements now have artifacts; the provisional AE-1 evidence package exists. **The gate is not closed.** |

## The relationship between GO and NO-GO

They do not contradict each other, and neither supersedes the other.

> **The independent review answered "is this evidence sound?" — yes.**
> **The maturity review answered "is this enough for Candidate?" — no.**

Both are true simultaneously. The evidence that was reviewed was sound; it was
simply not the evidence the accessibility gate asks for. GAP-H-01 records exactly
this: **the WP-016 GO was scoped against incomplete plan prerequisites** — the
[Candidate Plan](../roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md) listed ten
prerequisites and **omitted the normative nine-requirement Candidate accessibility
gate entirely** (GAP-B-01). A reviewer checking against that plan could return a
clean PASS while the higher-authority gate remained wholly unaddressed.

**The lesson is recorded, not the blame:** a review is bounded by the checklist
it is given, so an incomplete checklist produces a clean review of an incomplete
thing. The Candidate Plan has now been corrected additively so that the omission
cannot recur, and the omission itself is preserved in the record rather than
written out of it.

## What the remediation is and is not

**Additive.** It adds the missing gate artifacts. It:

- **revokes nothing** in the original review;
- **re-runs nothing** that the original review already established;
- **changes no** accepted Semantic Status meaning — the five axes, 25 values, ten
  invariants, six review-required combinations, eight fail-closed conditions,
  `status.<axis>.<value>` paths, non-visual source set, DE/EN requirement, and the
  existing source-set, manifest, and resolver identities are untouched;
- **leaves the WP-013/WP-015 24-case harness byte-identical**, as an independent
  regression sentinel (DEC-S-120);
- **preserves all 3 observations** (WP016-OBS-001, -002, -003) unresolved and
  unchanged.

| Gate requirement | Remediation artifact |
| --- | --- |
| 1 WCAG applicability mapping | [Candidate WCAG Applicability Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md) |
| 2 Responsibility mapping | [Candidate Accessibility Responsibility Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_RESPONSIBILITY_MAPPING.md) |
| 3 Known accessibility requirements | [Candidate Evidence Requirements Matrix](../operations/SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md) — 25/25, GAP-H-02 |
| 4 AE-1 | [Provisional AE-1 Evidence Record](../operations/SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md) + results and digest artifacts |
| 5 AE-2 or a reasoned plan | [Candidate AE-2 Evidence Plan](../governance/SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md) |
| 6 Known limitations | [Candidate Accessibility Limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md) — 16 entries |
| 7 Support baseline plan | [Candidate Support Baseline Plan](../governance/SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md) + [freshness review](WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md) |
| 8 Regression plan | [Candidate Accessibility Regression Plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md) |
| 9 Human-Maintainer approval after Nova review | **OPEN — not addressed and not addressable by an executor.** |

## What is still required

**A fresh independent review of this remediation package.** It has not happened,
and this addendum does not substitute for it.

| # | Still open |
| --- | --- |
| 1 | **Fresh independent review** of the remediation, by a reviewer who is neither its executor nor the WP-016 evidence reviewer's prior session. The remediation was written by a single executor who also wrote its fixtures, its expectations, and its tests (SSC-LIM-015). |
| 2 | **Admission of AE-1.** Until that review, the AE-1 package is **provisional**; the admitted accessibility evidence level of every CDS artifact remains **AE-0**. |
| 3 | **Nova Candidate-gate review** of the remediated package. |
| 4 | **Human-Maintainer Candidate approval** — gate requirement 9, not delegable (DEC-S-036). |

## Current state after this addendum

| Property | State |
| --- | --- |
| Original WP-016 Independent Evidence Review | **PASS** — unchanged, not revoked |
| Original Candidate Recommendation | **GO** — unchanged, valid in its declared narrow review sense |
| Nova Candidate Maturity Review | **NO-GO** — Candidate Accessibility Gate unmet |
| Gap assessment | **CONFIRMED** |
| Remediation | **Executed** — CDS-WP-016 internal rework, not a new work package |
| Fresh independent review of the remediation | **Required, not performed** |
| **Candidate** | **No** |
| **Maturity** | **Experimental** |
| **Approval** | **Unapproved** |
| **Admitted accessibility evidence level** | **AE-0** |
| Provisional AE-1 package | **Present, pending fresh independent review** |
| Claims | **None** |
| Pilot | **Inactive** |
| Publication | **Private Development** |
| CDS-WP-017 | **Not activated** |

## Related documents

- [WP-016 Candidate Gate Recommendation](WP016_CANDIDATE_GATE_RECOMMENDATION.md) — **historical, unmodified**
- [WP-016 Independent Re-Execution Review](WP016_INDEPENDENT_REEXECUTION_REVIEW.md)
- [WP-016 Source and Contract Traceability Review](WP016_SOURCE_CONTRACT_TRACEABILITY_REVIEW.md)
- [WP-016 Terminology, Accessibility and Content Review](WP016_TERMINOLOGY_ACCESSIBILITY_CONTENT_REVIEW.md)
- [WP-016 A11Y Baseline Freshness Review](WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md)
- [First Semantic Status Candidate Plan](../roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md)
- [Semantic Status Candidate Dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md)
- [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
