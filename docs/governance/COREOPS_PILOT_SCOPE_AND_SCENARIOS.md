# CoreOps Pilot Scope and Scenarios

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract
- **Date:** 2026-07-15
- **Status:** Normative for the **pilot scope**; not an implementation authorization

## Purpose and boundary

This document defines the bounded CoreOps pilot: which experience slice is in
scope, and what each pilot group must be able to express.

**The pilot is not a CoreOps redesign** (DEC-S-015). It is a representative
slice chosen to test CDS assumptions against real operational complexity.

### What this document deliberately does not do

It **describes requirements and scenarios, never UI solutions**. No layout,
component, visual treatment, colour, typography, icon, or interaction design
appears here, and none may be inferred from it. Scenarios state *what must be
expressible and safe*, not *how it should look* (DEC-S-020).

Requirements referenced as `CR-xxx` are registered in the
[Consumer Requirements Model](CONSUMER_REQUIREMENTS_MODEL.md).

## Roles in scenarios

Neutral, capability-based roles — not CoreOps' own role model, which is
product-owned:

| Role | Meaning |
| --- | --- |
| Operator | Observes state and performs routine operations. |
| Administrator | Configures the system and performs risk-bearing operations. |
| Restricted user | Holds a subset of permissions; some capabilities unavailable. |

## Pilot groups

### Pilot Group A — Application Foundation

**Goal:** establish that a shared application shell can carry a real operational
product without erasing its identity.

**Requirements:** CR-003 application shell and navigation · CR-004 multi-viewport
behavior · CR-018 simple and expert mode · CR-001 product-family recognition.

#### Scenario A-1 — Orientation within the shell

- **Roles:** Operator, Administrator
- **Preconditions:** authenticated; at least one operational area available.
- **Normal flow:** the user enters the application, identifies where they are,
  what the product is, and which areas exist; they move between a global area and
  a local area and remain oriented.
- **Alternative states:** a restricted user sees fewer areas without the
  navigation becoming misleading about what exists.
- **Error and degraded states:** an area is unavailable; the shell must remain
  navigable and say so rather than fail silently (CR-016).
- **Dangerous actions:** none.
- **Accessibility and localization:** navigation reachable and operable by
  keyboard with visible focus (CR-021); titles and labels tolerate DE/EN length
  differences (CR-023).
- **Open questions:** how much product-family expression belongs in the shell
  versus the product (CR-001, CR-002)?

#### Scenario A-2 — Reduced complexity

- **Roles:** Operator (Simple), Administrator (Expert)
- **Preconditions:** both modes available.
- **Normal flow:** in the reduced mode, risk-bearing options are not presented;
  in the expert mode, detail and overrides are.
- **Alternative states:** switching modes must not imply that hidden options do
  not exist.
- **Error and degraded states:** mode preference unavailable — a safe default
  applies, and the active mode stays evident.
- **Dangerous actions:** hidden in Simple; visible and risk-marked in Expert
  (CR-010).
- **Accessibility and localization:** the active mode must be programmatically
  determinable, not colour-signalled only (CR-006).
- **Open questions:** is mode a CDS concern, a product concern, or both?

---

### Pilot Group B — Operations Overview

**Goal:** establish that dense, prioritized operational status can be presented
truthfully.

**Requirements:** CR-005 dense operations overview · CR-006 semantic status
representation · CR-007 unknown is not healthy.

#### Scenario B-1 — Scanning system health

- **Roles:** Operator
- **Preconditions:** several monitored entities with mixed states.
- **Normal flow:** the user scans the overview and identifies within seconds what
  needs attention, in what order, and what is fine.
- **Alternative states:** everything healthy — the overview must not manufacture
  urgency; nothing monitored yet — a real empty state (CR-015).
- **Error and degraded states:** some data is **stale or missing**. It must read
  as unknown, never as healthy (CR-007). Partial data must not imply a complete
  picture.
- **Dangerous actions:** none; the overview is read-only.
- **Accessibility and localization:** status conveyed by text or icon, never
  colour alone (CR-006); severity order must not depend on colour perception.
- **Open questions:** what is the minimum honest representation of "unknown"?
  How is priority expressed without implying false precision?

#### Scenario B-2 — Following a signal

- **Roles:** Operator
- **Preconditions:** at least one non-healthy entity.
- **Normal flow:** the user moves from the summary to the affected entity without
  losing context, and understands why it is flagged.
- **Alternative states:** cause unknown — that must be stated, not smoothed over.
- **Error and degraded states:** detail unavailable while the summary is
  available; the mismatch must be explicit.
- **Dangerous actions:** none in this scenario.
- **Accessibility and localization:** plain-language explanation alongside
  technical detail (CR-020).
- **Open questions:** where does CDS guidance end and CoreOps domain semantics
  begin (CR-035)?

---

### Pilot Group C — Inventory and Dense Data

**Goal:** establish that dense inventory data is legible, navigable, and honest.

**Requirements:** CR-008 inventory and dense data · CR-006 semantic status
representation · CR-016 capability and degraded visibility.

#### Scenario C-1 — Working a dense inventory

- **Roles:** Operator, Administrator
- **Preconditions:** an inventory large enough that scanning alone is
  insufficient.
- **Normal flow:** the user filters and sorts to a relevant subset, sees each
  entity's status and available capabilities, and can tell what applies to each.
- **Alternative states:** filter yields nothing — an empty state distinguishable
  from "no data exists" (CR-015); the collection is genuinely empty.
- **Error and degraded states:** partial load; some rows' status unknown; a
  capability unavailable for some entities (CR-016). None may be silently
  hidden.
- **Dangerous actions:** none in this scenario; selection is expressed as a
  contract only, not designed here.
- **Accessibility and localization:** the structure must be traversable by
  keyboard and non-visually (CR-021); columns tolerate DE/EN length variation
  (CR-023).
- **Open questions:** at what density does a shared pattern stop generalizing?
  Is filtering a CDS contract or a product concern?

---

### Pilot Group D — State and Safety Patterns

**Goal:** the core of the pilot — establish that CDS can express the full state
set and make a dangerous action safe without dictating the product's domain.

**Requirements:** CR-015 complete system state set · CR-010 risk-tiered actions ·
CR-011 preview before execute · CR-012 confirmation and cancel path · CR-013 no
misleading success · CR-014 action auditability · CR-016 capability and degraded
visibility · CR-032 offline and degraded states · CR-007 unknown is not healthy ·
CR-020 plain-language errors.

#### Scenario D-1 — Full state coverage

- **Roles:** Operator, Restricted user
- **Preconditions:** an area that can occupy every state.
- **Normal flow:** each state is reachable and distinguishable: loading, empty,
  success, warning, critical, error, offline, degraded, permission denied,
  unavailable capability (CR-015).
- **Alternative states:** states combine — degraded **and** permission denied
  simultaneously. Combination must not produce a misleading or contradictory
  reading.
- **Error and degraded states:** the state itself is unknown. This is the hardest
  case and must be expressible (CR-007).
- **Dangerous actions:** none; this scenario proves representability.
- **Accessibility and localization:** every state must be perceivable
  non-visually and expressible in DE and EN (CR-006, CR-023).
- **Open questions:** which states are CDS-owned and which are domain semantics?
  How are combined states resolved?

#### Scenario D-2 — Performing a dangerous action safely

- **Roles:** Administrator
- **Preconditions:** a risk-bearing operation the user is permitted to perform.
- **Normal flow:** the action is recognizable as dangerous **before** engagement
  (CR-010); an understandable preview or plan states what will change (CR-011);
  the user confirms deliberately or cancels on an unambiguous path (CR-012); the
  outcome is reported truthfully (CR-013) and remains traceable afterwards
  (CR-014).
- **Alternative states:** the user cancels — nothing changes, and that is stated;
  the user lacks permission — the action is visible-but-unavailable rather than
  hidden, unless hiding is itself the product's policy.
- **Error and degraded states:** the action **partially** succeeds; the operation
  is interrupted; the outcome is **unknown**. None may be reported as success
  (CR-013). The system is offline mid-action (CR-032).
- **Dangerous actions:** this is the scenario. Confirmation must be deliberate
  and must not be defeated by habituation.
- **Accessibility and localization:** the danger must not be signalled by colour
  alone (CR-006); confirmation must be keyboard-operable with visible focus
  (CR-021); the consequence must be stated in plain language in both languages
  (CR-020, CR-023).
- **Open questions:** what makes a confirmation deliberate without becoming
  ceremony that trains dismissal? How much of the preview is CDS contract versus
  CoreOps domain content? Does auditability generalize beyond CoreOps (CR-014,
  DEC-S-016)?

---

### Pilot Group E — Help, Accessibility, and Localization

**Goal:** establish that the slice remains usable, explicable, and honest across
languages and interaction modes.

**Requirements:** CR-017 setup and preflight check · CR-019 contextual help ·
CR-021 keyboard operability and focus · CR-022 motion restraint · CR-023 DE/EN
and flexible text · CR-020 plain-language errors · CR-006 semantic status
representation.

#### Scenario E-1 — Guided setup with an environment check

- **Roles:** Administrator
- **Preconditions:** an unconfigured or partially configured environment.
- **Normal flow:** the user is guided through setup; an environment check runs
  and reports a graded result they can act on (CR-017).
- **Alternative states:** the check passes with warnings — actionable, not
  alarming; the check cannot run at all — reported as unknown, never as pass
  (CR-007).
- **Error and degraded states:** a prerequisite is missing; the check is
  incomplete; setup is resumed after interruption.
- **Dangerous actions:** none; setup must not perform risk-bearing changes
  without the Group D pattern.
- **Accessibility and localization:** the flow is keyboard-completable (CR-021);
  the language choice precedes content the user must read (CR-023); the graded
  result is not colour-only (CR-006).
- **Open questions:** is a setup wizard a CDS pattern or a product pattern?
  Evidence exists in all three consumers, but each built its own.

#### Scenario E-2 — Understanding without leaving the task

- **Roles:** Operator, Restricted user
- **Preconditions:** a screen with non-obvious consequences.
- **Normal flow:** contextual help is available at the point of use, and an error
  is explained in plain language alongside technical detail (CR-019, CR-020).
- **Alternative states:** help unavailable offline — this must degrade honestly
  (CR-031, CR-032).
- **Error and degraded states:** an error with no plain-language explanation
  available; the technical detail must still be reachable.
- **Dangerous actions:** none.
- **Accessibility and localization:** help must be reachable by keyboard
  (CR-021); motion restrained and reduced-motion preferences honoured (CR-022);
  DE/EN parity without layout breakage (CR-023).
- **Open questions:** what accessibility level is actually committed? **Undefined
  today** (CR-024) — CoreOps names a baseline without a level, and CastCore
  documentation contains no accessibility evidence at all. This is the largest
  open question in the pilot.

---

## Scenario coverage

| Pilot group | Scenarios |
| --- | --- |
| A — Application Foundation | 2 |
| B — Operations Overview | 2 |
| C — Inventory and Dense Data | 1 |
| D — State and Safety Patterns | 2 |
| E — Help, Accessibility, and Localization | 2 |
| **Total** | **9** |

Every pilot group has at least one scenario. Counts derived from the sections
above and independently re-counted.

## Out of scope

Explicitly **not** part of the first pilot:

- the complete CoreOps interface,
- a complete component library,
- final brand identity,
- final colours or typography,
- network topology visualization as a finished pattern,
- deployment workflow as a finished pattern,
- a productive PDF engine,
- a complete document or presentation system,
- marketing material,
- a mobile application,
- a complete CDS conformance assessment.

Topology (CR-009), deployments, PDF and reports (CR-028), diagrams (CR-029), and
further multi-channel artifacts (CR-026, CR-027, CR-030) remain **registered
later validation candidates**. They are deferred, not rejected.

## Open design and architecture questions

Carried into CDS-WP-005. None is answered here.

1. Where does a shared pattern end and CoreOps domain semantics begin? (CR-035)
2. How much product individuality may the shell express, given that SpeakCore
   and CastCore already hold product-local design decisions? (CR-001, CR-002,
   CR-037)
3. Which states are CDS-owned, and how are combined states resolved? (CR-015)
4. How is "unknown" represented honestly and consistently? (CR-007)
5. What makes a confirmation deliberate rather than habitual? (CR-012)
6. Is the setup wizard a CDS pattern, given all three consumers built their own?
   (CR-017)
7. Does auditability generalize beyond CoreOps? (CR-014, DEC-S-016)
8. What accessibility level is committed, and how is it evidenced? (CR-024)

## Related documents

- [CoreOps Pilot Contract](COREOPS_PILOT_CONTRACT.md)
- [Consumer Requirements Model](CONSUMER_REQUIREMENTS_MODEL.md)
- [Consumer Requirements Traceability](CONSUMER_REQUIREMENTS_TRACEABILITY.md)
- [Consumer Validation Plan](CONSUMER_VALIDATION_PLAN.md)
