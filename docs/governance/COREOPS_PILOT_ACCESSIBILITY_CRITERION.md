# CoreOps Pilot Accessibility Criterion

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-007
- **Date:** 2026-07-16
- **Status:** **Normative** for the pilot accessibility criterion

## Purpose

Operationalizes **CR-024** — the accessibility target — for the CoreOps pilot.

CR-024 has been the open question since CDS-WP-004, and CDS-WP-006 made it
load-bearing: it blocked the Stable gate, Product Profile approval, the
publication gate, and a pilot entry criterion simultaneously.

Frame: [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) ·
[CoreOps Pilot Contract](COREOPS_PILOT_CONTRACT.md).

## CR-024 resolution

*(Normative, DEC-S-060)*

> **CR-024 is resolved at policy level: WCAG 2.2 Level AA for the declared
> web-based CoreOps pilot scope.**

### What this resolves

| Resolved |
| --- |
| A target level exists |
| Responsibilities are assigned |
| Evidence requirements are defined |
| The policy can serve as a normative basis after Human Maintainer commit |

### What this does not resolve

| **Not** resolved |
| --- |
| **The pilot has not started** |
| **Pilot Group E has not passed — and has not failed; it is not assessed** |
| **No WCAG 2.2 Level AA conformance has been demonstrated, reviewed, or approved for CoreOps** |
| **No CDS artifact has an approved WCAG 2.2 Level AA conformance claim** |
| **The required evidence does not exist** |

**Defining a target proves nothing** (DEC-S-050). This document closes a policy
gap, not an evidence gap.

## Declared pilot scope

The accessibility target applies to the **declared web-based scope** of the
bounded pilot — Groups A–E, nine scenarios, per the
[Pilot Scope and Scenarios](COREOPS_PILOT_SCOPE_AND_SCENARIOS.md).

**Not in scope:** anything outside the bounded slice · non-web channels (each
needs its own profile, DEC-S-058) · the complete CoreOps product · CoreOps
domain content and semantics.

The pilot remains a **bounded representative slice**, not a redesign
(DEC-S-015).

## Target

**WCAG 2.2 Level AA**, per the applicability matrix: **55 applicable Level A and
AA criteria** — 31 A and 24 AA — excluding the obsolete 4.1.1.

Of those, **49 require action from both CDS and CoreOps**. That is the
operative fact for this pilot: **CDS cannot deliver the target alone, and neither
can CoreOps.**

## Responsibilities

| | Owns in the pilot |
| --- | --- |
| **CDS** | Accessibility requirements of shared foundations; component and pattern contracts incl. accessibility behavior; status and state semantics; reference evidence for CDS artifacts; known limitations |
| **CoreOps (Consumer Maintainer)** | **Accessible composition**; product content; domain semantics; complete processes; runtime behavior; consumer-local extensions; **product testing in the declared scope**; the product's claims |
| **Shared** | Support baseline; browser/platform/AT matrix; pilot evidence; complete-process evaluation; consumer feedback; regression handling; claims |

**Using accessible CDS artifacts will not make the CoreOps pilot accessible**
(DEC-S-052).

## Pilot Group E — minimum evidence

*(Normative — required later; **none exists today**)*

| # | Requirement | Level |
| --- | --- | --- |
| 1 | Full keyboard operability (2.1.1) | AE-2, AE-3 |
| 2 | Visible and comprehensible focus (2.4.7, 2.4.3, 2.4.11) | AE-2, AE-3 |
| 3 | **No keyboard trap** (2.1.2) | AE-2, AE-3 |
| 4 | **Status not conveyed by colour alone** (1.4.1) | AE-1, AE-2 |
| 5 | **Programmatically available names, roles, values, states** (4.1.2) | AE-2, AE-3 |
| 6 | **DE/EN text and meaning parity** (3.1.1, 3.1.2) | AE-2 |
| 7 | Flexible text lengths (1.4.12, 1.4.10) | AE-2 |
| 8 | Reduced-motion behavior | AE-2 |
| 9 | Error and help functions (3.3.1, 3.3.3, 3.2.6) | AE-2, AE-3 |
| 10 | **Declared accessibility support baseline** | Prerequisite for AE-3 |
| 11 | **Documented AE-2 and AE-3 evidence** | AE-2, AE-3 |
| 12 | Known limitations | Mandatory |
| 13 | Human Maintainer review | Mandatory |

Requirement 5 carries the pilot's central architectural commitment into
accessibility: the **Unknown invariant must reach assistive technology**
(DEC-S-056). A status honest only to a sighted operator is not honest — and an
operator acting on a green that means *we have no idea* is precisely the failure
Group B and Group D exist to prevent.

## Required future AE levels

| Scope | Required |
| --- | --- |
| CDS pilot components and patterns | **AE-1 + AE-2 + AE-3** against the declared baseline |
| CoreOps pilot slice | **AE-4** — declared scope, complete processes, consumer revision, feedback, limitations |
| Any pilot accessibility claim | **AE-4 + scope + versions + baseline + approval** |

**Automated checking alone is never sufficient** (DEC-S-053).

## Support baseline for the pilot (CDS-WP-010)

*(Additive — the pilot has not started and this changes nothing about that)*

The support baseline is **A11Y-BL-001**
([Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md)), declared and
committed by CDS-WP-010.

- **Applicable tier:** the **Required Tier-1 (Required Core) baseline** applies to
  the declared **web** pilot scope — keyboard-only, Windows 11, Chromium and Firefox
  with NVDA (two pairings), forced-colors, reduced motion, zoom/reflow/text-spacing,
  accessible dynamic status, DE/EN (DEC-S-066, DEC-S-067).
- **Consumer additions remain required:** CoreOps (Consumer Maintainer) must declare
  any additional Tier-2/Tier-3 environments its product scope needs and produce the
  consumer (AE-4) evidence; CDS Tier-1 does not cover the consumer's environments
  (DEC-S-051, DEC-S-069).
- **`Accessibility support baseline` is policy-side present** — CDS-WP-010 is
  committed — satisfying Pilot Group E requirement 10 at the *policy* level only.
  Policy-side presence satisfies **no** evidence requirement.
- **Evidence remains fully outstanding:** the baseline is a test contract, not
  evidence (DEC-S-065). No AE-1/AE-2/AE-3/AE-4 exists; every artifact is AE-0.
- **The pilot stays inactive** and cannot start (entry criteria unmet; DEC-S-015).

## Entry criterion status

*(Normative)*

The pilot contract's entry criterion **"the accessibility target and its evidence
method are decided"** may be treated as:

> ### `Accessibility target defined` — **satisfiable upon Human Maintainer commit of CDS-WP-007**

Claude does not declare it met. The Human Maintainer's commit does.

### Still unmet

| Entry criterion | Status |
| --- | --- |
| CDS-WP-004 committed | Met |
| Pilot scope approved | Pending |
| Consumer requirements registered | Met |
| **CDS-WP-005 architecture approved** | **Pending** |
| **Foundations at Candidate maturity** | **Unmet — no artifact is Candidate** |
| CoreOps pilot area named | Pending |
| No CoreOps governance conflict | Pending |
| **Accessibility target decided** | **Satisfiable on commit** |

**The pilot cannot start.** Two criteria remain structurally unmet: no artifact
can reach Candidate (**no evidence exists** — every artifact is AE-0; the support
baseline itself is declared), and the architecture awaits approval.

## Available evidence

**None.**

| Evidence | State |
| --- | --- |
| CDS artifact accessibility evidence | **AE-0** |
| Support baseline | **Declared and committed — A11Y-BL-001; a test contract, never evidence** |
| CoreOps pilot evidence | **None — pilot inactive** |
| User research | **None, and none planned** (RISK-017) |
| Automated checks | **None run** |

## Missing evidence

The declared support baseline is in place (A11Y-BL-001); everything below remains
outstanding. Before Pilot Group E can be evidenced: CDS components and patterns at
Candidate with AE-1/AE-2 · AE-3 against the baseline · CoreOps pilot
implementation · AE-4 for the declared scope · consumer feedback · documented
limitations · Human Maintainer review.

That is the full distance between a defined target and a pilot that can be
assessed.

## Explicit statements

*(Normative)*

> **The CoreOps pilot has not started.** Entry criteria remain unmet. This
> document starts nothing (DEC-S-015).

> **No WCAG 2.2 Level AA conformance has been demonstrated, reviewed, or approved
> for CoreOps.** No evaluation has occurred, so neither a pass nor a failure can be
> stated. No claim is made, permitted, or implied.

> **No current CDS artifact has an approved WCAG 2.2 Level AA conformance claim.**
> No CDS artifact has been evaluated — every artifact is **AE-0, Not Assessed**,
> which is neither passed nor failed.

> **No accessibility claim of any level is valid today** — for CDS, for CoreOps,
> or for anyone.

> **A target is not conformance** (DEC-S-050).

## Related documents

- [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [WCAG 2.2 AA Applicability Matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md)
- [CoreOps Pilot Contract](COREOPS_PILOT_CONTRACT.md)
- [CoreOps Pilot Scope and Scenarios](COREOPS_PILOT_SCOPE_AND_SCENARIOS.md)
- [Consumer Validation Plan](CONSUMER_VALIDATION_PLAN.md)
