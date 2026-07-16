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
| **4** | Accessibility verification | **Strong, bounded** | Verified against a stated target — never "accessible" unqualified. |
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
| Accessibility verification | **None** |
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
4. the accessibility target and its evidence method (CR-024),
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

Level 4, and **currently blocked**.

CR-024 records that the accessibility target is undefined: CoreOps names a
baseline with no conformance level, and CastCore documentation contains no
accessibility evidence at all. Until CDS-WP-007 sets a target and an evidence
method:

- **no accessibility claim of any kind may be made**,
- Group E cannot be fully evidenced,
- keyboard and focus verification (CR-021) can still be performed and reported as
  a **specific check**, not as conformance.

Even once a target exists, the claim is bounded: a stated target, plus published
evidence, plus the consumer's own obligation — never "CDS is accessible".

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
