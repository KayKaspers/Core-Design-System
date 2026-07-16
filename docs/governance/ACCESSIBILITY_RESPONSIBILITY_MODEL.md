# Accessibility Responsibility Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-007
- **Date:** 2026-07-16
- **Status:** **Normative** for accessibility responsibility

## Purpose

Answers one question precisely: **when a consumer's product is inaccessible,
whose problem is it?**

The honest answer is usually *both*, and that is why this model exists. The
[applicability matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md) quantifies it: **49
of 56 Level A/AA criteria require action from both CDS and the consumer.** Only 5
are CDS-alone.

Frame: [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md).

## The core boundary

*(Normative, DEC-S-051, DEC-S-052)*

> **CDS can supply a contract, a role, a state mechanism, and a semantic slot.
> CDS cannot supply the content that fills them, the composition that arranges
> them, or the process they sit inside.**

Those three are where accessibility is usually lost. All three are
consumer-owned.

**Using accessible CDS artifacts does not make a product accessible or
conformant.**

## CDS responsibilities

CDS owns, long-term:

| # | Responsibility |
| --- | --- |
| 1 | The accessibility target and policy |
| 2 | Accessibility requirements of shared foundations |
| 3 | Component and pattern contracts, including accessibility behavior |
| 4 | Status and state semantics, including the Unknown invariant |
| 5 | Permitted Product Profile limits |
| 6 | Accessibility documentation |
| 7 | Reference evidence for CDS artifacts |
| 8 | Known limitations |
| 9 | Channel profile requirements |
| 10 | Regression gates for its own artifacts |

**CDS does not own:** consumer content, composition, domain semantics, runtime,
or a consumer's claim.

## Consumer responsibilities

The Consumer Maintainer owns, in their own product:

| # | Responsibility |
| --- | --- |
| 1 | Accessible composition |
| 2 | Product content |
| 3 | Domain semantics |
| 4 | Complete processes |
| 5 | Consumer-local components and extensions |
| 6 | Runtime behavior |
| 7 | Third-party content |
| 8 | Authentication and session behavior |
| 9 | Local overrides |
| 10 | Product testing in the declared scope |
| 11 | The consumer's accessibility claims |

Item 1 carries the most weight. A keyboard trap can arise **purely from
composition**, from components that are each individually trap-free (2.1.2).

## Shared or contract-controlled

Neither side can settle these alone:

| # | Area |
| --- | --- |
| 1 | Support baseline |
| 2 | Browser, platform, and assistive-technology matrix |
| 3 | Product Profile |
| 4 | Exceptions and known limitations |
| 5 | CoreOps pilot evidence |
| 6 | Complete-process evaluation |
| 7 | Consumer feedback |
| 8 | Regression handling |
| 9 | Scope- and revision-bound claims |

## Roles

Per the [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md), applied to
accessibility.

| Role | Accessibility authority |
| --- | --- |
| **Human Maintainer** | Approves the policy, accessibility claims, accessibility-relevant risk acceptance, Candidate and Stable transitions, and any limitation with normative effect. **Not delegable.** |
| **Nova** | Accessibility governance review, scope and evidence checking, risk control, consistency, approval recommendation. **Declares no conformance and accepts no risk.** |
| **Claude** | Policy documentation, applicability mapping, traceability, register maintenance, quantitative validation. **Confirms no conformance, invents no test, approves no claim, gives no legal interpretation.** |
| **Consumer Maintainer** | Accountable for accessible composition, content, domain behavior, extensions, complete processes, runtime, product testing, and product claims. **Holds no CDS core approval authority.** |
| **Contributor** | May supply proposals, implementations, or evidence. **No acceptance authority; never approves their own contribution.** |
| **Evidence Reviewer** | Checks accessibility evidence against the claimed level. **Never the artifact itself, and never the executor of the work being evidenced.** |

## Responsibility matrix

RACI-style. **A** accountable · **R** responsible · **C** consulted · **I**
informed.

| Activity | Human Maintainer | Nova | Claude | Consumer Maintainer | Contributor | Evidence Reviewer |
| --- | --- | --- | --- | --- | --- | --- |
| Define the accessibility target | **A** | C | R | I | — | — |
| Approve the policy | **A** | C | — | I | — | — |
| Define component accessibility contracts | **A** | C | R | C | C | — |
| Define status semantics | **A** | C | R | C | — | — |
| Produce CDS artifact evidence (AE-1/AE-2) | **A** | C | — | — | R | C |
| Produce assistive-technology evidence (AE-3) | **A** | C | — | C | R | **R** |
| Review accessibility evidence | **A** | R | — | — | — | **R** |
| Approve Candidate transition | **A** | C | — | I | — | C |
| Approve Stable transition | **A** | C | — | C | — | C |
| Accessible composition in a product | I | C | — | **A/R** | — | — |
| Product content and domain semantics | I | — | — | **A/R** | — | — |
| Complete-process evaluation (AE-4) | C | C | — | **A/R** | — | **R** |
| Make a product accessibility claim | **A** (approves) | C | — | **R** (makes it) | — | C |
| Approve an accessibility limitation | **A** | C | R | C | — | C |
| Accept an accessibility-relevant risk | **A** | C | — | I | — | — |
| Declare conformance | **A** | — | **Never** | R (for own scope) | — | C |

**Claude appears nowhere as accountable or approving.** That is deliberate.

## The component-to-product boundary

*(Normative, DEC-S-052)*

Accessibility evidence for a **component, pattern, test harness, reference
implementation, channel, or limited scope cannot be generalized into a
product-wide conformance claim.**

Concretely — even with perfectly accessible CDS components, a product can fail
because:

- composition creates a keyboard trap none of the parts contained (2.1.2),
- reading order breaks across correctly ordered components (1.3.2),
- content lacks meaningful alternatives, labels, or headings (1.1.1, 2.4.6),
- a complete process is unusable although every screen passes (3.3.4),
- an override suppresses visible focus (2.4.7),
- runtime state contradicts declared semantics (4.1.2),
- third-party content is inaccessible.

**CDS cannot prevent any of these.** The consumer can.

Conversely, a consumer cannot compensate for a component whose contract omits
accessibility. Hence: **shared, both must act, neither alone suffices.**

## The Product Profile boundary

*(Normative, DEC-S-025, DEC-S-059)*

A Product Profile **may never weaken accessibility**. This is an architecture
invariant, not a preference.

Consequently:

- A profile may not remove a visible focus indicator, reduce a required contrast
  role below its target, suppress a semantic state, or make colour the sole
  carrier.
- A profile requires **scope-appropriate accessibility evidence** before approval
  (DEC-S-043) — which **cannot be produced today**, so no profile can be
  approved.
- **An ordinary exception cannot waive accessibility** for Stable or
  CDS-conformant scope.

## Claim responsibility

*(Normative, DEC-S-044 applied)*

| Claim | Who makes it | Who approves | About what |
| --- | --- | --- | --- |
| CDS artifact accessibility evidence | CDS | Human Maintainer | **CDS artifacts only** |
| Product accessibility claim | **Consumer Maintainer** | Human Maintainer | The consumer's declared scope |
| Conformance claim | Consumer, for its scope | Human Maintainer after Nova review | Scope- and revision-bound only |

Rules:

- **A consumer's claim is the consumer's own.** CDS does not make it for them,
  and CDS artifacts do not confer it.
- Claims are scope-, version-, revision-, baseline-, and evidence-bound.
- **No global accessibility claim exists** — for CDS or for any consumer.
- `CDS certified` remains prohibited.
- **No claim is valid today.** Nothing has been tested.

## Escalation

Escalate — do not resolve locally — when:

- accessibility and security appear to conflict (for example authentication,
  3.3.8) — this requires a controlled design and risk decision, never a silent
  trade-off,
- a profile or exception would weaken accessibility,
- evidence is missing, contradictory, or reviewed only by its own executor,
- a criterion's responsibility is genuinely unclear,
- a consumer requests a claim their evidence does not support,
- the support baseline has drifted (RISK-044),
- evidence demand exceeds capacity (RISK-048) — a real constraint, and **never a
  conformance rationale**.

Path: **Claude records and reports → Nova reviews and recommends → Human
Maintainer decides.** While open, the affected state is not Candidate-, Stable-,
or claim-eligible.

## Related documents

- [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [WCAG 2.2 AA Applicability Matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Accessibility Limitations and Exception Policy](ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md)
- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
