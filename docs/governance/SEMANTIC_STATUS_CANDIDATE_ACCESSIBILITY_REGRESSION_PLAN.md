# Semantic Status Candidate — Accessibility Regression Plan

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Accessibility Gate Remediation
- **Date:** 2026-08-17
- **Scope:** the **Semantic Status Candidate source and contract family**
- **Status:** **A plan — NOT normative, NOT evidence, NOT mitigation.**

## Why this document exists

Requirement 8 of the [Candidate accessibility gate](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md#candidate-accessibility-gate).

Accessibility regresses silently. For a *meaning* foundation the failure mode is
sharper than for a visual one: a single renamed value, a softened German label, or
a removed `$description` does not break a build, does not fail a schema, and does
not look like a defect — it just makes a status statement quietly less true.
Every trigger below is a way that can happen.

> **A regression is a deviation, not a limitation** (RISK-045). It is not
> recorded and lived with; it invalidates evidence until re-verified.
> **Documentation is not mitigation.**

## Evidence effects — defined once

*(Referenced by the trigger table. `Applicable evidence` today means the admitted
AE-1 package `AE1-CDS-WP016-SEMSTATUS-002` — Evidence 002, independently reviewed
**PASS**, integrated, and admitted by the Human Maintainer on 2026-08-17 for the
channel-independent source/contract scope only. Once other levels exist they are
included. **E-REREVIEW is unaffected by that admission:** a completed independent
review of the current package satisfies no future trigger, and every trigger below
requires a fresh one.)*

| Effect | Meaning |
| --- | --- |
| **E-INVALID** | The affected evidence **no longer evidences what it claimed** and is marked as such immediately. Evidence does not carry forward across a change to what it evidenced (DEC-S-052). It is never silently re-used. |
| **E-REVIEW-DUE** | The affected evidence freshness state becomes `Review due`. `Review due` evidence is **not current** and **passes no gate** (DEC-S-070). |
| **E-REEXEC** | The machine evidence run must be **re-executed** at the new revision: the Candidate evidence runner, the semantic-status test suite, and the 24-case harness, with new results and digest artifacts. |
| **E-REREVIEW** | A **fresh independent review** is required by a reviewer who is neither the executor of the change nor the executor of the evidence (DEC-S-045). A re-execution reviewed only by its own executor has not been reviewed. |
| **E-REMAP** | The affected mapping documents must be re-derived: the [WCAG applicability mapping](SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md), the [responsibility mapping](SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_RESPONSIBILITY_MAPPING.md), and the [evidence requirements matrix](../operations/SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md). |
| **E-MIGRATION** | The change is a **migration event** (DEC-S-082): impact and migration assessment, migration references, and compatibility handling are required before it may proceed. |
| **E-GATE** | Candidate status (if ever awarded) is **suspended** until the re-executed evidence has been independently reviewed and re-approved. Stable is unreachable regardless. Any claim covering the affected scope becomes **invalid** and must be withdrawn. |

## Regression triggers

*(15 triggers. Every one is **Elevated** — they touch shared semantics,
accessibility obligations, and future compatibility, per the Foundation
Contract's change control.)*

| # | Trigger | Why it is an accessibility regression risk | Effects |
| --- | --- | --- | --- |
| **T-01** | **Axis count changes** (an axis added or removed) | Invariant 1. A removed axis destroys a distinction no representation can recover; an added axis is a vocabulary a consumer cannot have evidenced. | E-INVALID · E-REVIEW-DUE · E-REEXEC · E-REREVIEW · E-REMAP · E-MIGRATION · E-GATE |
| **T-02** | **Value count or value-set changes** (a value added, removed, or its meaning altered) | The 25 values are the shared vocabulary. A removed value silently reroutes real states onto a neighbouring, less truthful one. | E-INVALID · E-REVIEW-DUE · E-REEXEC · E-REREVIEW · E-REMAP · E-MIGRATION · E-GATE |
| **T-03** | **Technical ID rename** | Technical IDs are the stable, language-neutral anchor every localization and every representation binds to. A rename breaks the anchor without breaking anything visible. | E-INVALID · E-REEXEC · E-REREVIEW · E-MIGRATION · E-GATE |
| **T-04** | **DE terminology change** | A German label that narrows, widens, softens, or upgrades a canonical meaning is an accessibility defect for German-language users — the `supported → verifiziert` upgrade is the archetype (DEC-S-119). | E-INVALID (DE localization evidence) · E-REVIEW-DUE · E-REEXEC (structural) · E-REREVIEW (meaning) · E-GATE |
| **T-05** | **EN terminology change** | Identical risk in the normative semantic reference language, where an erosion propagates into every other locale derived from it. | E-INVALID (EN localization evidence) · E-REVIEW-DUE · E-REEXEC (structural) · E-REREVIEW (meaning) · E-GATE |
| **T-06** | **Review-required combination changes** (a combination added, removed, or redefined) | The six combinations are what force a human to explain an unusual-but-truthful state instead of glossing it. Removing one removes the explanation obligation silently. | E-INVALID · E-REEXEC · E-REREVIEW · E-REMAP · E-GATE |
| **T-07** | **Fail-closed condition changes** (a condition added, removed, or weakened) | The eight conditions are the last line against a dishonest status being asserted at all. Weakening one converts a blocked state into a shipped one. | E-INVALID · E-REEXEC · E-REREVIEW · E-REMAP · E-GATE |
| **T-08** | **Textual communication obligation changes** (disclosure priority, qualifier carrying, prohibited unqualified claims, plain-language rules) | These obligations are the whole text-first accessibility strategy (DEC-S-111). A relaxed obligation lets a summary hide a qualifier lawfully. | E-INVALID · E-REVIEW-DUE · E-REREVIEW · E-REMAP · E-GATE |
| **T-09** | **Introduction or change of a non-textual meaning carrier** (colour, icon, shape, position, motion bound to status) | Invariant 7. The instant meaning can ride on a non-textual carrier, colour-only and icon-only encoding become possible, and WCAG 1.4.1 and 1.3.3 move from "structurally prevented" to "must be tested". | E-INVALID · E-REVIEW-DUE · E-REMAP · **AE-2 and AE-3 become required** · E-GATE |
| **T-10** | **Token path or grouping changes** (`status.<axis>.<value>` restructured) | Paths are the machine-readable traceability between the vocabulary and the source. A regrouping breaks 1:1 traceability and every downstream reference. | E-INVALID · E-REEXEC · E-REREVIEW · E-MIGRATION · E-GATE |
| **T-11** | **Localization coverage changes** (a language added or a row dropped) | A dropped row means a value with no label in a declared language — the user sees a raw identifier or nothing. An added language is coverage that has never been reviewed for meaning parity. | E-INVALID (affected language) · E-REVIEW-DUE · E-REEXEC (structural 25/25) · E-REREVIEW (meaning) · E-GATE |
| **T-12** | **Source-set, manifest, or resolver identity changes** (identity, revision, profile version, DTCG version) | Identity disagreement fails closed (DEC-S-123). Evidence is bound to an identity; changing it un-binds every digest and every result artifact. | E-INVALID · E-REEXEC · E-REREVIEW · E-GATE |
| **T-13** | **First visual binding** (the first representation that renders status) | The 30 representation-triggered WCAG criteria become live and assessable at once, and a Channel Accessibility Profile becomes mandatory (DEC-S-058, DEC-S-125). Source evidence does **not** transfer to it. | E-REMAP · **AE-2 and AE-3 required for the new artifact** · **Channel profile required** · E-GATE (for the new artifact) |
| **T-14** | **A11Y-BL-001 revision or freshness change** | Evidence produced against a baseline that has moved, or whose freshness is `Review due`, `Stale`, or `Unknown`, is not current evidence and satisfies no gate. | E-REVIEW-DUE · E-REREVIEW · targeted revalidation of affected environments · E-GATE |
| **T-15** | **Validator-contract changes affecting this evidence** (diagnostic code, category, layer, severity, or check semantics; schema `$id`; CLI contract) | The machine evidence *is* the validator's output. A changed check meaning changes what a past "Pass" meant, retroactively and invisibly (RISK-077). | E-INVALID · E-REEXEC · E-REREVIEW · E-GATE |

## Traceability to the gap assessment

The read-only gap assessment proposed **13** re-evidence triggers. This plan
implements **15**. Nothing was added beyond the assessed set and **nothing was
lost**: two assessed triggers are split into clearly traceable sub-triggers so
that a change in one language or one rule table cannot be waved through under a
combined heading.

| Assessed trigger | Implemented as | Split? |
| --- | --- | --- |
| Axis count changes | T-01 | — |
| Value count / value-set changes | T-02 | — |
| Technical ID rename | T-03 | — |
| **Terminology change** | **T-04 (DE)** + **T-05 (EN)** | **Yes** — DE and EN carry independent meaning risk and independent evidence; a German-only change must not be assessed under an English-language review, and vice versa. |
| **Combination rule changes** | **T-06 (review-required)** + **T-07 (fail-closed)** | **Yes** — the two tables have different force. Weakening a fail-closed condition ships a state that was previously blocked; changing a review-required combination changes who must explain what. Merging them would let the more severe change hide behind the milder one. |
| Textual communication obligation changes | T-08 | — |
| Introduction / change of non-textual meaning carrier | T-09 | — |
| Token path / grouping changes | T-10 | — |
| Localization coverage changes | T-11 | — |
| Source-set / manifest / resolver identity changes | T-12 | — |
| First visual binding | T-13 | — |
| A11Y-BL-001 revision / freshness change | T-14 | — |
| Validator-contract changes affecting evidence | T-15 | — |
| **Total** | **13 assessed → 15 implemented** | **2 splits, 0 losses** |

## Regression severity handling

*(Per the [Accessibility Defect and Regression Model](ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md).)*

| Severity | Definition for this Candidate | Handling |
| --- | --- | --- |
| **Critical** | A truthfulness invariant is broken: `unknown`, `stale`, `expired`, `unverified`, `partial`, or `unavailable` can be represented as its positive counterpart; or a value loses its textual meaning entirely. | **Blocks Stable. Blocks Candidate.** Evidence for the affected scope is invalid until re-verified; any claim covering it is withdrawn. Escalate immediately: Claude records and reports → Nova reviews → **Human Maintainer decides**. |
| **High** | A distinction is materially degraded but not inverted — e.g. `degraded` and `disrupted` become indistinguishable in a locale, or a review-required combination stops requiring a rationale. | **Blocks Candidate promotion** and any dependent claim until re-executed and independently re-reviewed. |
| **Medium** | A structural or traceability property is broken without a direct meaning loss — e.g. a path/value mismatch, an identity disagreement, a digest divergence. | Evidence goes `Review due`; re-execution and re-review required before the affected evidence supports any gate. |
| **Low** | A documentation or mapping inconsistency with no evidence effect. | Recorded and corrected on the Standard track; no evidence invalidation. |

**A Critical or High accessibility regression also fires baseline-maintenance
trigger 7** and requires an A11Y-BL-001 freshness review
([Maintenance Policy](ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md)).

## Candidate, Stable, and claim effects

| Effect | Rule |
| --- | --- |
| **Candidate** | Any Critical or High regression suspends Candidate status (if ever awarded) until re-executed evidence has been independently reviewed **and** re-approved by the Human Maintainer. A regression is never resolved by re-labelling it a limitation. |
| **Stable** | Unreachable regardless: Stable requires complete AE-2 plus AE-3 against the declared baseline and **no unresolved critical accessibility deviations**. None of that exists. |
| **Claims** | A claim covering an affected scope becomes **invalid** and must be withdrawn. A claim omitting a known regression is invalid by definition (DEC-S-044). **No claim is valid today**, so there is nothing to withdraw yet — that is the current state, not a safeguard. |
| **Exceptions** | An ordinary exception may **never** waive an accessibility requirement, downgrade a critical regression by relabelling it, or substitute AE-1 where AE-2 or AE-3 is required (DEC-S-059). Missing capacity is a planning limit, never a conformance justification. |

## Detection — what is and is not automated

| Trigger | Detected automatically today? |
| --- | --- |
| T-01, T-02, T-03, T-10, T-12 | **Yes** — the validator fails closed on axis/value/path/identity changes, and the digest artifacts expose content drift. |
| T-04, T-05, T-11 | **Structurally yes** (25/25 rows, both labels, no duplicate, no unauthorized), **semantically no** — a label whose *meaning* drifts while the row remains present is not machine-detectable. |
| T-06, T-07 | **Partially** — the evidence runner's 6/6 and 8/8 coverage sentinels fail if a rule is removed from the runner, but a change made to the *normative documents* without touching the runner is caught only by human review. |
| T-08, T-09, T-13 | **No** — these are governance and design events, detected by review, not by a check. |
| T-14 | **No** — detected by the baseline review cadence and by the recorded lifecycle dates. |
| T-15 | **Partially** — existing tests fail on a changed diagnostic contract, but a *meaning* change to a check with unchanged code and category is caught only by review. |

**This table is a limitation record, not a reassurance.** Roughly half the
triggers have no automated detection, which is precisely why the review
obligations above are not optional.

## What this plan does not do

- It **is not mitigation.** Writing a regression plan prevents no regression.
- It **produces no evidence** and **creates no claim**.
- It **promotes nothing**: Candidate remains **No**, maturity **Experimental**,
  approval **Unapproved**. The admitted evidence level is **AE-0** for every CDS
  artifact except this channel-independent source/contract family, which holds
  admitted **AE-1** (`AE1-CDS-WP016-SEMSTATUS-002`, source scope only) — an
  admission this plan neither produced nor extends.

## Related documents

- [Accessibility Defect and Regression Model](ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md) — normative
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) — normative
- [Accessibility Baseline Maintenance Policy](ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md) — normative
- [Semantic Status Candidate Support Baseline Plan](SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md)
- [Semantic Status Candidate AE-2 Evidence Plan](SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md)
- [Semantic Status Candidate Accessibility Limitations](SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md)
