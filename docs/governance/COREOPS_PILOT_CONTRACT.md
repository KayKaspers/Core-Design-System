# CoreOps Pilot Contract

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract
- **Date:** 2026-07-15

## Contract status

**Normative upon Human Maintainer commit following Nova approval.**

This contract is a **proposal** until then. Claude cannot activate it and does
not claim it is active. Entry criteria are unmet at the time of writing, so no
pilot has started.

## Purpose

The pilot tests CDS assumptions against **real operational complexity** rather
than against benchmark documentation or intent.

Specifically, it tests whether:

1. a shared foundation can carry a real operational product without erasing its
   identity (CR-001, CR-003),
2. CDS can express the full operational state set honestly, including unknown
   (CR-015, CR-007),
3. CDS can make a dangerous action safe without absorbing domain semantics
   (CR-010 … CR-014),
4. dense operational data stays legible under a shared foundation (CR-005,
   CR-008),
5. accessibility and DE/EN hold up in a real product (CR-021, CR-023),
6. artifacts work without mandatory external runtime services (CR-031),
7. the ownership boundary in DEC-S-008 survives contact with a real consumer.

**It does not test** whether CDS is differentiated, adopted, or conformant.

## Parties and roles

| Party | Role in the pilot |
| --- | --- |
| **Human Maintainer** | Sole authority to activate this contract, approve scope changes, accept evidence, and decide the exit outcome. Performs all Git writes. |
| **Nova** | Strategy, architecture, planning, review, approval recommendations. Recommends; does not decide. |
| **CDS** | Supplies the versioned foundation under test and owns shared design rules (DEC-S-008). |
| **CoreOps** | Pilot consumer. Supplies real requirements and validation cases; owns its product strategy, business logic, domain data, backend, security architecture, and operations. Does not alone determine CDS architecture (DEC-S-002). |
| **Claude** | Scoped executor. Documentation and analysis within an explicitly authorized work package. No authority, no Git writes, no activation. |

## Entry criteria

The pilot may begin only when **all** hold:

1. CDS-WP-004 is committed by the Human Maintainer.
2. The pilot scope (Groups A–E) is approved.
3. Consumer requirements are registered — CR-001 … CR-040.
4. The CDS-WP-005 design-system architecture is approved.
5. The relevant foundations have reached at least Candidate maturity, per the
   [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md) *(supplied by
   CDS-WP-006)*.
6. The CoreOps pilot area is named unambiguously by the Human Maintainer.
7. No conflict with CoreOps' own governance and work-package queue.
8. The accessibility target and its evidence method are decided (CR-024) —
   otherwise Group E cannot be evidenced.

### Current state — reconciled by CDS-WP-007

**Not met. The pilot remains inactive.**

| # | Criterion | State |
| --- | --- | --- |
| 8 | Accessibility target and evidence method decided | **`Accessibility target defined` — satisfiable upon Human Maintainer commit of CDS-WP-007.** The target (**WCAG 2.2 Level AA**, DEC-S-049, DEC-S-060) and the evidence method (**AE-0 … AE-4**, Evidence and Claims Model) now exist. Claude does not declare this met; **the commit does.** |
| 4 | CDS-WP-005 architecture approved | **Pending** |
| 5 | Foundations at Candidate maturity | **Unmet — structurally.** No artifact is Candidate; the Candidate accessibility gate cannot be passed (AE-0, no support baseline). |

**Accessibility evidence remains not satisfied.** Criterion 8 concerns a
*decision*, not evidence — and Group E still cannot be evidenced. See the
[CoreOps Pilot Accessibility Criterion](COREOPS_PILOT_ACCESSIBILITY_CRITERION.md).

**This contract starts no implementation** (DEC-S-015).

## In-scope pilot groups

| Group | Focus |
| --- | --- |
| **A** | Application Foundation — shell, navigation, orientation, modes |
| **B** | Operations Overview — prioritized status, health summary, honest unknown |
| **C** | Inventory and Dense Data — list/table structure, filter, sort, empty state |
| **D** | State and Safety Patterns — full state set, dangerous action, confirmation |
| **E** | Help, Accessibility, and Localization — setup check, help, keyboard, DE/EN |

Detail: [CoreOps Pilot Scope and Scenarios](COREOPS_PILOT_SCOPE_AND_SCENARIOS.md)
— 9 scenarios across the five groups.

## Out of scope

The complete CoreOps interface · a complete component library · final brand
identity · final colours or typography · topology visualization as a finished
pattern · deployment workflow as a finished pattern · a productive PDF engine · a
complete document or presentation system · marketing material · a mobile
application · a complete CDS conformance assessment.

Deferred candidates remain registered, not rejected: CR-009 topology, CR-026
repository presentation, CR-027 documentation standards, CR-028 PDF and reports,
CR-029 diagrams, CR-030 presentations, CR-039 recovery mode, CR-040 API parity.

## Evidence requirements

Evidence must be produced for the pilot to be assessable. Required:

1. **Version-bound CDS state** — a specific CDS version, not "current" (DEC-S-012,
   DEC-S-017).
2. **Version- or commit-bound CoreOps state** — a specific revision (DEC-S-013).
3. **Requirement traceability** — each pilot requirement traced to its outcome
   via [Consumer Requirements Traceability](CONSUMER_REQUIREMENTS_TRACEABILITY.md).
4. **Design rationale** — why a solution was chosen, so it can be reviewed rather
   than merely observed.
5. **Accessibility evidence** — against the target **WCAG 2.2 Level AA** for the
   declared web-based pilot scope, per the
   [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md):
   **AE-1 + AE-2 + AE-3** against a declared support baseline for CDS pilot
   artifacts, and **AE-4** for any CoreOps pilot claim.
   **None of this evidence exists** — every artifact is AE-0 — so **no
   accessibility claim may be made** (DEC-S-050).
6. **Keyboard and focus verification** — CR-021.
7. **State and status coverage** — every state in CR-015 demonstrably reachable
   and distinguishable, including unknown (CR-007).
8. **Consumer feedback** — from the CoreOps side, recorded rather than
   summarized away.
9. **Documented deviations** — every divergence classified, not hidden.
10. **Visual or render evidence** — only after later authorized implementation.
    None exists now and none may be implied.
11. **No informal "CDS compliant" statement** — at any point, by anyone
    (DEC-S-012, DEC-S-018, RISK-018).

### What the evidence cannot establish

Documentation and implementation evidence do **not** constitute user research.
Interviews, observational studies, usability testing, and accessibility testing
with real users are **not** part of this pilot and must not be implied by it
(RISK-017). The pilot can show that a pattern is *expressible and internally
consistent*. It cannot show that it *works for real people*.

## Exit criteria

The pilot concludes when **all** hold:

1. All pilot requirements are assessed against the Success Categories.
2. Every `Must` requirement is demonstrably addressed — or its non-fulfilment is
   documented with rationale.
3. All deviations are classified.
4. CoreOps-specific outcomes and generalizable outcomes are **separated**
   (DEC-S-016).
5. Architecture feedback is documented for CDS-WP-005.
6. Governance feedback is documented for CDS-WP-006.
7. No unevidenced conformance claim exists anywhere in the outputs.
8. The Human Maintainer decides: **extend**, **revise**, or **abort**.

## Success categories

Per requirement. **No numeric scores and no overall pilot score.**

| Category | Meaning |
| --- | --- |
| **Validated** | Requirement met, evidenced, and generalizable. |
| **Validated with limitations** | Met, but with documented constraints or scope conditions. |
| **Needs redesign** | The approach failed against real complexity. |
| **Product-local** | Real, but belongs to CoreOps rather than CDS. |
| **Rejected for CDS** | Should not become a CDS standard. |
| **Not tested** | Not exercised — stated honestly, never inferred as a pass. |

`Not tested` exists so that gaps stay visible. An untested requirement is never
reported as validated.

## Change control

Pilot changes require an authorized CDS work package, or an explicit correction
by Nova or the Human Maintainer.

Specifically:

- The scope is **not** extended because implementation reveals adjacent work
  (RISK-015).
- A CoreOps-specific outcome does **not** become a CDS standard by appearing in
  the pilot; it requires a generalizability review and explicit acceptance
  (DEC-S-016, RISK-016).
- Neither the pilot's existence nor its completion constitutes CDS adoption,
  certification, endorsement, or conformance (DEC-S-015, DEC-S-018, RISK-018).
- Claude does not extend scope, activate the contract, or claim acceptance.

## Related documents

- [Consumer Requirements Model](CONSUMER_REQUIREMENTS_MODEL.md) — requirements and classification
- [Consumer Requirements Traceability](CONSUMER_REQUIREMENTS_TRACEABILITY.md) — provenance
- [CoreOps Pilot Scope and Scenarios](COREOPS_PILOT_SCOPE_AND_SCENARIOS.md) — groups and scenarios
- [Consumer Validation Plan](CONSUMER_VALIDATION_PLAN.md) — how evidence is judged
- [Consumer Evidence Register](../research/CONSUMER_EVIDENCE_REGISTER.md) — sources
- [Concept and Scope](CONCEPT_AND_SCOPE.md) — normative scope source
