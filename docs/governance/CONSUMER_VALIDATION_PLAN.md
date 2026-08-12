# Consumer Validation Plan

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract
- **Date:** 2026-07-15
- **Status:** Normative for **how pilot evidence is judged**

## Purpose

This plan states what counts as evidence, how strong each kind is, and what may
be claimed as a result. It exists so that the pilot cannot quietly upgrade weak
evidence into a strong claim.

**It promises no conformance.** No CDS certification, legal-compliance, or
accessibility-conformance claim is made or enabled by this plan.

## Validation goals

1. Establish whether each pilot requirement holds against real operational
   complexity.
2. Separate what generalizes from what is CoreOps-specific (DEC-S-016).
3. Surface where CDS assumptions break, early and cheaply.
4. Produce evidence a reviewer can check, rather than an assertion they must
   trust.
5. Keep the ownership boundary (DEC-S-008) honest under real pressure.

## Evidence levels

Ordered weakest to strongest. **The current pilot rests entirely at Level 1.**

| Level | Evidence | Strength | Establishes |
| --- | --- | --- | --- |
| **1** | Committed consumer documentation | **Limited** | A need was *stated* or a behavior was *built*. Not that it works. |
| **2** | Human Maintainer validation | **Moderate** | Informed judgement that a requirement is real and correctly classified. |
| **3** | CoreOps implementation evidence | **Moderate to strong** | The pattern survives contact with real complexity. |
| **4** | Accessibility verification — graded **AE-0 … AE-4** *(see [Accessibility evidence](#accessibility-evidence))* | **Strong, bounded** | Verified against a stated target, in a declared scope, against a declared baseline — never "accessible" unqualified. **Currently AE-0.** |
| **5** | Consumer feedback from use | **Strong** | The pattern works for the people doing the work. |
| **—** | User research, usability testing, observational study | **Not planned** | **Not part of this pilot.** Must never be implied. |

### The honesty rule

An outcome may be reported **only at the level its evidence actually reaches**.
Level 1 evidence supports "documented as needed" — it does not support "works",
"validated", "usable", or "accessible" (RISK-017).

## Current evidence state

| Fact | Value |
| --- | --- |
| Evidence sources read | 15 (14 usable) |
| Consumers analyzed | 3 |
| Evidence level reached | **Level 1 only** |
| Human validation performed | **None** |
| Implementation evidence | **None** |
| Accessibility verification | **None — AE-0 for every artifact**; the support baseline A11Y-BL-001 is declared and committed, but nothing has been verified against it |
| User research | **None, and none planned** |

Every requirement is therefore **provisional**. CDS-WP-004 produced a
requirements model and a contract — not validation.

## Human Maintainer validation

Level 2. Required before any requirement is treated as accepted.

The Human Maintainer decides:

1. whether each `Must` requirement is real and correctly prioritized,
2. whether classification is correct — particularly Shared CDS Candidate versus
   Product-local (RISK-016),
3. whether the two single-consumer CoreOps Pilot Requirements (CR-003, CR-014)
   are generalizable (DEC-S-016),
4. the accessibility target and its evidence method (CR-024) — *proposed by
   CDS-WP-007 as **WCAG 2.2 Level AA** with **AE-0 … AE-4**; **the decision takes
   effect on the Human Maintainer's commit**, not before*,
5. whether documentation evidence suffices, or real validation is required first,
6. whether AirCore and further consumers must be reviewed before foundations
   freeze.

Nova recommends. The Human Maintainer decides. Claude does neither.

## Later CoreOps implementation evidence

Level 3. Only after CDS-WP-005 architecture approval and an authorized
implementation work package.

Must be version-bound on both sides (DEC-S-017): a specific CDS version and a
specific CoreOps revision. Must include requirement traceability, design
rationale, state coverage per CR-015 including unknown per CR-007, and
documented deviations.

Visual or render evidence exists only from this level onward. **None exists
today.**

## Accessibility evidence

*(Reconciled by CDS-WP-007)*

Level 4, and **still blocked** — for a different reason.

The target now exists: **WCAG 2.2 Level AA** for the applicable web scope
(CR-024, DEC-S-049, DEC-S-060), with an evidence method (AE-0 … AE-4, per the
[Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)).
What is missing is the **evidence**.

### The accessibility evidence levels

*(Normative source: [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md). This plan does not define them.)*

| Level | Meaning | Current state |
| --- | --- | --- |
| **AE-0** | **No evidence.** Nothing has been examined. | **Every CDS artifact** |
| **AE-1** | Declared intent and mapping — requirements identified, responsibilities assigned. | None |
| **AE-2** | Structured self-assessment against the target, in a declared scope. | None |
| **AE-3** | Verification against a **declared accessibility support baseline** (browser / platform / assistive-technology matrix). | None — the baseline **A11Y-BL-001 is declared**, but no verification has been performed against it |
| **AE-4** | Consumer-level evidence for complete processes in a declared product scope. | None — pilot inactive |

**AE-0 is not a passing state; it is the absence of a question having been
asked.** It is where CDS is today, and this plan may not present it as anything
else.

### What remains blocked

- **No accessibility claim of any level may be made** — for CDS, for CoreOps, or
  for anyone.
- Group E cannot be evidenced. See the
  [CoreOps Pilot Accessibility Criterion](COREOPS_PILOT_ACCESSIBILITY_CRITERION.md).
- Keyboard and focus verification (CR-021) may still be performed and reported as
  a **specific check** — never as conformance.

### Scope and claim boundaries

*(Normative)*

- Evidence is **bound to a revision, a scope, and a channel**, and **never
  transfers** across any of them (DEC-S-052).
- **AE-3 without a declared support baseline is unverifiable** — it does not say
  what it was tested against.
- **Automated checking alone is never sufficient** (DEC-S-053).
- **Non-web channels are never presented as WCAG conformant** (DEC-S-058).
- A claim omitting a known limitation is **invalid** (DEC-S-044).
- **Using accessible CDS artifacts does not make a consumer product accessible**
  (DEC-S-052). Accessible composition is the consumer's.

Even once evidence exists, the claim stays bounded: a stated target, a declared
scope and baseline, published evidence, and the consumer's own obligation —
**never "CDS is accessible"**.

### No validation has been performed

**This plan describes intent, not activity.** No accessibility validation, test,
audit, or user research has been carried out — by CDS or by any consumer — and
none is scheduled (RISK-017). **A target is not conformance** (DEC-S-050).

### Accessibility support baseline and evidence discipline (CDS-WP-010)

*(Additive — no validation is claimed and none has been performed)*

- **Baseline selection:** consumer/pilot accessibility evidence targets
  **A11Y-BL-001** ([Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md)) —
  the Required Tier-1 baseline for the web scope, plus any environments the consumer
  declares (DEC-S-066, DEC-S-069). A consumer may add environments; it may not narrow
  the CDS Required baseline for a shared artifact.
- **Environment identity:** every evidence run binds exact OS, browser/renderer,
  assistive technology, input, language, channel, consumer revision, CDS version, and
  date (DEC-S-068, DEC-S-071); `current`/`latest` is not an identity (RISK-052).
- **Freshness:** evidence carries a freshness state; `Unknown`/`Stale` evidence is
  not current and passes no exit gate (DEC-S-070).
- **Regression:** a previously passed combination that later fails is a regression,
  not a limitation; Blocking/High regressions block the affected scope's Stable,
  claims, and "unchanged-compatible" statement (DEC-S-072, RISK-045, RISK-053).
- **Complete-process evidence:** a consumer accessibility outcome requires **AE-4** —
  the declared scope's complete processes at a consumer revision, with feedback and
  documented limitations (DEC-S-052). Component evidence is not product evidence.
- **Claim boundary:** no accessibility support or conformance claim is valid without
  AE-4, a declared scope, a declared current baseline, evidence identity, known
  limitations, and Human-Maintainer approval (DEC-S-044). **None is valid today.**

## Consumer feedback

Level 5. Recorded as given, not summarized into agreement. Disagreement between
CDS and CoreOps is itself evidence and must survive into the exit review rather
than being reconciled away.

## Deviation model

Every divergence between CDS guidance and what CoreOps actually needs is
classified:

| Deviation | Meaning | Consequence |
| --- | --- | --- |
| **Justified product-local** | CoreOps legitimately differs. | Stays CoreOps-owned; not a CDS defect. |
| **CDS gap** | CDS lacks something genuinely shared. | Candidate for CDS; requires generalizability review. |
| **CDS defect** | CDS guidance is wrong or harmful. | Must be fixed; strongest possible signal. |
| **Scope pressure** | Real need, outside the bounded pilot. | Registered as deferred; **does not extend the pilot** (RISK-015). |
| **Unresolved** | Cannot be classified yet. | Stays visible; never silently closed. |

A deviation is never resolved by widening the pilot.

## Success categories

Per requirement, matching the pilot contract. **No numeric scores, no overall
score, no percentage complete.**

`Validated` · `Validated with limitations` · `Needs redesign` · `Product-local` ·
`Rejected for CDS` · `Not tested`

`Not tested` must be used wherever a requirement was not exercised. An untested
requirement is never reported as validated, and absence of a failure is never
evidence of success.

## Exit review

The exit review answers, per requirement: which category, on what evidence, at
what level, with what limitations.

It must state explicitly:

- which `Must` requirements were **not** addressed and why,
- which outcomes are CoreOps-specific versus generalizable (DEC-S-016),
- which deviations remain unresolved,
- what the pilot **did not** establish,
- architecture feedback for CDS-WP-005 and governance feedback for CDS-WP-006.

The Human Maintainer then decides: extend, revise, or abort.

## No conformance promise

To state it once, unambiguously:

- The pilot does **not** establish CDS adoption (DEC-S-015).
- The pilot does **not** establish CDS conformance (DEC-S-012).
- The pilot does **not** establish accessibility conformance.
- The pilot does **not** establish that CDS is differentiated (DEC-S-019).
- Completing the pilot is **not** certification or endorsement (RISK-018).
- Secondary consumers hold no pilot authority, and their evidence does not imply
  adoption (DEC-S-018).

## Related documents

- [CoreOps Pilot Contract](COREOPS_PILOT_CONTRACT.md)
- [CoreOps Pilot Scope and Scenarios](COREOPS_PILOT_SCOPE_AND_SCENARIOS.md)
- [Consumer Requirements Model](CONSUMER_REQUIREMENTS_MODEL.md)
- [Consumer Evidence Register](../research/CONSUMER_EVIDENCE_REGISTER.md)
