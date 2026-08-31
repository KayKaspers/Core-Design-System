# Post-Candidate Development Roadmap

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-017 — Post-WP-016 Roadmap, Authority and Scope
  Reconciliation
- **Date:** 2026-08-25
- **Baseline reconciled against:** commit
  `1fc53ae5afa40807e1950171ab700b0860ee581e` (`main`, clean working tree, clean
  index, 0 tags)
- **Status:** **Roadmap and planning view — NOT normative, NOT an authorization,
  and NOT evidence.** It sequences intended work. It grants no maturity, admits no
  evidence, activates no work package, starts no pilot, and creates no claim.

This document is the **single active forward roadmap** for CDS. Where an older
planning document still projects a forward path, that path is historical; this
document supersedes it **as the forward view only** and rewrites none of it.

## The one rule this document exists to protect

> **A roadmap entry is a plan, not permission.**

| Statement | Never implies |
| --- | --- |
| Listed in this roadmap | Authorized, started, funded, or committed |
| `Planned` | `Active` |
| Defined | Authorized |
| Milestone reached | Maturity granted |
| Candidate | Stable, release, publication, adoption, or conformance |
| Evidence produced | Evidence admitted |
| Evidence admitted | Authority to promote |
| Generated output | Authority |
| Design-tool representation | Authority |
| Consumer need | CDS Core |
| Product Profile | Core override |
| Renderer behaviour | Governance authority |
| AI or executor output | Approval |

**CDS-WP-021 through CDS-WP-053 are `Planned`, `Not active`, and `Not authorized
for execution`. Work on them has not started.** Each becomes executable only on an
explicit Nova prompt **and** Human-Maintainer authorization, one work package at a
time. Nothing in this document activates the next one automatically.

**CDS-WP-018, CDS-WP-019 and CDS-WP-020 are the exceptions, and they prove the
rule:** each left `Planned` only when the Human Maintainer authorized it separately
— CDS-WP-018 on 2026-08-25, CDS-WP-019 and CDS-WP-020 on 2026-08-26 — **not**
because this roadmap listed it next.

## Current state at the reconciled baseline

| Item | Value |
| --- | --- |
| **CDS-WP-016** | **Closed** — closure commit `1fc53ae5afa40807e1950171ab700b0860ee581e` |
| **CDS-WP-017** | **Active** — this reconciliation |
| **CDS-WP-018 … CDS-WP-053** | **Planned · not active · not authorized** |
| Candidate artifact families | **1** — the channel-independent Semantic Status Layer-3 source / contract family |
| Source revision | `semantic-status-rev-0002-candidate` |
| Maturity · approval | `Candidate` · `Approved` |
| Admitted evidence in force | `AE1-CDS-WP016-SEMSTATUS-004` at **AE-1**, source/contract scope only |
| Every other CDS artifact | **AE-0** |
| **Stable** | **No** |
| Claims · conformance | **None** · **None** |
| AE-2 · AE-3 · AE-4 | **None** |
| Channel evidence · consumer evidence | **None** · **None** |
| Visual value · component | **None** · **None** |
| Consumer adoption · pilot | **None** · **Inactive** |
| Publication | **`Private Development`** |
| Releases · tags | **None** · **0** |

Sources: the
[Candidate Promotion Effectivity Record](../governance/SEMANTIC_STATUS_CANDIDATE_PROMOTION_EFFECTIVITY_RECORD.md),
the [Candidate Approval Record](../operations/SEMANTIC_STATUS_CANDIDATE_APPROVAL_RECORD.md),
and the [AE1-004 Admission Record](../governance/SEMANTIC_STATUS_AE1_004_ADMISSION_RECORD.md).

**Work-package rows updated by CDS-WP-018 (2026-08-25).** The table above is bound
to baseline `1fc53ae5afa40807e1950171ab700b0860ee581e` and its maturity, evidence,
claim, and publication rows are **unchanged**. Only the work-package rows have
advanced: **CDS-WP-017 is `Closed`** — closure commit
`df9b8f21ff3bde4607b1c9ff7fdcbe3144366040` — **CDS-WP-018 is `Active`**, and
**CDS-WP-019 … CDS-WP-053** remain **`Planned` · not active · not authorized**. The
controlled carrier for work-package status is
[Work Packages](../../project-system/WORK_PACKAGES.md), never this planning view.

**Work-package rows updated again by CDS-WP-019 (2026-08-26).** The maturity,
evidence, claim, conformance, and publication rows above remain **unchanged** —
Candidate families **1**, Stable **No**, claims **None**, conformance **None**,
AE-2/AE-3/AE-4 **None**, visual value **None**, component **None**, pilot
**Inactive**, publication **`Private Development`**, releases **None**, tags **0**.
Only the work-package rows have advanced: **CDS-WP-018 is `Closed`** — closure
commit `e5d5d492619071655ba956713980d1ee261d9213` — **CDS-WP-019 is `Active`**, and
**CDS-WP-020 … CDS-WP-053** remain **`Planned` · not active · not authorized**.

**Work-package rows updated again by the phase transition (2026-08-26).** The
maturity, evidence, claim, conformance, and publication rows above remain
**unchanged** — Candidate families **1**, Stable **No**, claims **None**,
conformance **None**, AE-2/AE-3/AE-4 **None**, visual value **None**, component
**None**, pilot **Inactive**, publication **`Private Development`**, releases
**None**, tags **0**. Only the work-package rows have advanced: **CDS-WP-019 is
`Closed`** — closure commit `538fbccbf6f554de3b872e9fb75a70d13318feb6` — **no
numbered work package is active**, and **CDS-WP-020 … CDS-WP-053** remain
**`Planned` · not active · not authorized**. The phase relabel by **DEC-S-127**
changed the project-phase label and **nothing else**; it advanced no maturity and
authorized no work package.

**Work-package rows updated again by CDS-WP-020 (2026-08-26).** The maturity,
evidence, claim, conformance, and publication rows above remain **unchanged** —
Candidate families **1**, Stable **No**, claims **None**, conformance **None**,
AE-2/AE-3/AE-4 **None**, **visual value None**, component **None**, pilot
**Inactive**, publication **`Private Development`**, releases **None**, tags **0**.
Only the work-package rows have advanced: **CDS-WP-020 was authorized separately on
2026-08-26 and is `Active` — executed with result `DECISION_REQUIRED`, not
closed** — and **CDS-WP-021 … CDS-WP-053** remain **`Planned` · not active · not
authorized**. CDS-WP-020 delivered a **contract**, not values: it created no visual
value, no identifier, no token source, no schema, and no validator rule, registered
**no** Decision, ADR, or risk, and advanced **no** maturity. **As at that date,
DEC-S-128 and ADR-0004 were recommended and not created**, and the registers stood
at **127** and **98**. *(Dated record. The separately authorized Decision
Integration Pass of 2026-08-27, below, later prepared DEC-S-128 … DEC-S-131 and
ADR-0004.)*

**Work-package rows updated again by the CDS-WP-020 closure and routing pass
(2026-08-27).** The maturity, evidence, claim, conformance, and publication rows
above remain **unchanged** — Candidate families **1**, Stable **No**, claims
**None**, conformance **None**, AE-2/AE-3/AE-4 **None**, **visual value None**,
component **None**, pilot **Inactive**, publication **`Private Development`**,
releases **None**, tags **0**. Only the work-package rows have advanced: the
reviewed CDS-WP-020 object was integrated by the Human-Maintainer commit
`42a568d823de3388e45af62967546f13ad67eff6`, and **CDS-WP-020 is recorded as
`Closed`** — closure is **proposed in the working object of this pass** and becomes
effective only at the Human-Maintainer integration commit of that object.
**`CDS-WP-020A` is newly registered as `Planned` · not active · not authorized**,
and **CDS-WP-021 … CDS-WP-053** remain **`Planned` · not active · not authorized**.
**Registering an identifier activates nothing.** The decision register now holds
**131** entries and the ADR range **4**; the risk register stays at **98**. **The
closure and routing pass reconciled no decision or ADR effectivity qualification;
the separately authorized post-integration effectiveness reconciliation has since
done so — see `F-020C-01`.** **DEC-S-128 … DEC-S-131 are effective and ADR-0004 is
`Accepted`**, at the integration commit named above.

**Superseded in part (2026-08-31).** The condition stated in the paragraph above —
the Human-Maintainer integration commit of the closure and routing object — has
been met by commit `3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`. **CDS-WP-020
closure is effective at that commit**, and
**no work package is currently authorized**; **`CDS-WP-020A`** and
**CDS-WP-021 … CDS-WP-053** stay **`Planned` · not active · not authorized**. The
maturity, evidence, claim, conformance, and publication rows above remain
**unchanged**.

**CDS-WP-019 created no visual value.** It defined the *architecture* of the visual
foundation — nine families, fourteen invariants, a naming model, and the
accessibility, channel, brand, and governance boundaries — and selected **no
colour, typeface, size, spacing, radius, stroke, shadow, opacity, icon,
illustration, motion value, breakpoint, or theme**. The row *"Visual value ·
component: **None** · **None**"* above is therefore still accurate. All nine visual
foundation families are **`Proposed`**; **none is Candidate**.

**Evidence never transfers across a source revision** (DEC-S-126). Every later
revision needs fresh evidence, a fresh independent review, and a fresh admission.

## Strategic development path

```text
Governance
  → Visual Foundation
    → Semantic Presentation
      → Components
        → Evidence
          → Real Consumers
            → Experience
              → Multimodal
                → Advanced Interaction
                  → Brand & Assets
                    → Distribution
                      → Stable Evaluation
```

The ordering is a **dependency statement**, not a schedule. Nothing later may be
pulled forward past a prerequisite it depends on, and reaching an arc's end
grants no maturity to anything inside it.

## Development arcs and work packages

Each work package is mapped to the layer it primarily serves in the normative
[eight-layer architecture](../architecture/DESIGN_SYSTEM_ARCHITECTURE.md)
(DEC-S-021). The mapping is orientation; the architecture document remains the
normative source.

### Phase R — Reconciliation and Hygiene

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-017 | Post-WP-016 Roadmap, Authority and Scope Reconciliation | 1 | **Closed** |
| CDS-WP-018 | Deferred Governance and Repository Hygiene Reconciliation | 1 | **Closed** |

### Phase V — Visual Foundation

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-019 | Core Visual Foundation Architecture | 3 | **Closed** |
| CDS-WP-020 | Reference and Semantic Token Foundation | 3 | **Closed** *(effective at the Human-Maintainer commit `3f37ecf…`)* |
| CDS-WP-020A | Visual Token Source Authoring and Source Set Realization | 3 | Planned · not active · not authorized |
| CDS-WP-021 | Adaptive Layout and Responsive Foundation | 3 | Planned · not active |
| CDS-WP-022 | Theme and Environmental Presentation Model | 3 | Planned · not active |

**`CDS-WP-020A` is an inserted identifier, not a renumbering.** It follows the
existing **`CDS-WP-001A`** insert precedent already carried in
[Work Packages](../../project-system/WORK_PACKAGES.md): a suffixed identifier placed
between two numbered work packages, occupying no number. **No work package was
renumbered**, and the numeric range CDS-WP-017 … CDS-WP-053 is unchanged.

**Its table position is registration, not sequencing.** Listing CDS-WP-020A before
CDS-WP-021 and CDS-WP-022 does **not** decide that it runs before them. **OD-7 is
open** — it recommends that **CDS-WP-022** be considered before any value-selection
work package — and this registration neither accepts nor rejects that
recommendation. Execution order is a Human-Maintainer decision, and **CDS-WP-020A is
`Planned`, not active, and not authorized.**

**The milestone mapping is not re-derived here.** **M2 — Visual Foundation Ready**
still reads *"reached after CDS-WP-022"*, unchanged. Whether CDS-WP-020A belongs
before or inside that milestone depends on **OD-4 … OD-7**, which are open; deciding
it here would be a sequencing decision this pass holds no authority to make. See
**`F-020C-02`**.

### Phase S — Semantic Presentation

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-023 | Semantic Status Visual Binding Contract | 3 → 4 | Planned · not active |
| CDS-WP-024 | Semantic Validation and Render-Gate Architecture | 8 | Planned · not active |
| CDS-WP-025 | Semantic Validation Negative-Fixture Expansion | 8 | Planned · not active |

### Phase C — Component System

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-026 | Universal Component Contract Model | 4 | Planned · not active |
| CDS-WP-027 | StatusDisclosure Component Contract | 4 | Planned · not active |
| CDS-WP-028 | Core Controls Component Set | 4 | Planned · not active |
| CDS-WP-029 | Core Feedback and Disclosure Component Set | 4 | Planned · not active |

### Phase E — Accessibility and Evidence

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-030 | Component Accessibility Evidence Framework | 8 | Planned · not active |
| CDS-WP-031 | Rendering Matrix and Visual Regression Evidence | 8 | Planned · not active |

### Phase P — Profiles and Consumers

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-032 | Product Profile and Brand Extension Governance | 1 → 2 | Planned · not active |
| CDS-WP-033 | Second Consumer Validation — Real Core Product | 8 → 7 | Planned · not active |
| CDS-WP-034 | Multi-Channel and Localization Preservation | 6 | Planned · not active |

### Phase X — Experience Foundation

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-035 | Motion System | 3 | Planned · not active |
| CDS-WP-036 | Content Design, Voice and Tone | 2 → 5 | Planned · not active |
| CDS-WP-037 | Iconography and Symbol System | 3 → 2 | Planned · not active |
| CDS-WP-038 | Forms and Validation Pattern Family | 5 | Planned · not active |
| CDS-WP-039 | Data Visualization Foundation | 6 → 5 | Planned · not active |

### Phase M — Multimodal Experience

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-040 | Sonic Design / Audio Foundation | 6 | Planned · not active · **scope registration required first** |
| CDS-WP-041 | Multimodal Feedback Contract | 5 → 6 | Planned · not active · **scope registration required first** |
| CDS-WP-042 | Haptic Feedback Extension Model | 6 | Planned · not active · **scope registration required first** |

### Phase A — Advanced Interaction

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-043 | Security and Safety Interaction Patterns | 5 | Planned · not active |
| CDS-WP-044 | AI and Agent Interaction Design | 5 | Planned · not active · **scope registration required first** |

### Phase B — Advanced Brand and Assets

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-045 | Advanced Brand Identity Model | 2 | Planned · not active |
| CDS-WP-046 | Asset Governance and Provenance | 2 → 7 | Planned · not active |
| CDS-WP-047 | Internationalization and Locale Architecture | 5 → 6 | Planned · not active |

### Phase D — Distribution and Adapters

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-048 | Machine-Readable Distribution Contract | 7 | Planned · not active |
| CDS-WP-049 | Design Tool Adapter Architecture | 7 | Planned · not active |
| CDS-WP-050 | Runtime Adapter Reference Architecture | 7 | Planned · not active |

### Phase Q — Mature Quality and Release

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-051 | Cross-Consumer Conformance Evidence Model | 8 | Planned · not active |
| CDS-WP-052 | Candidate-to-Stable Readiness Review | 1 → 8 | Planned · not active |
| CDS-WP-053 | Stable Gate and Distribution Readiness | 1 → 7 | Planned · not active |

**Sequence integrity:** CDS-WP-017 … CDS-WP-053 remains a contiguous range of
**37** numeric identifiers with no gap and no duplicate, and **no work package was
renumbered**. **One inserted identifier — `CDS-WP-020A` — now sits inside that
span**, registered by the CDS-WP-020 closure and routing pass on the `CDS-WP-001A`
precedent; a suffix occupies no number, so the numeric range is untouched. Of the
**38** identifiers now recorded, **34** — CDS-WP-020A and CDS-WP-021 … CDS-WP-053 —
are `Planned · not active · not authorized`, and **four** — CDS-WP-017, CDS-WP-018,
CDS-WP-019, and CDS-WP-020 — are closed. The **CDS Phase Transition Governance
Package** occupies **no** identifier in this range.

## Milestones

Milestone names are **roadmap states only**. Reaching one grants **no** maturity,
**no** evidence level, **no** claim, and **no** publication change. Each remains
subject to its own gate.

| Milestone | Name | Reached after | Grants |
| --- | --- | --- | --- |
| **M1** | Reconciled Baseline | CDS-WP-018 | Nothing |
| **M2** | Visual Foundation Ready | CDS-WP-022 | Nothing |
| **M3** | Semantic Presentation Ready | CDS-WP-025 | Nothing |
| **M4** | Core Component Foundation Ready | CDS-WP-029 | Nothing |
| **M5** | Evidence-Ready Component System | CDS-WP-031 | Nothing |
| **M6** | Consumer-Validated Design System | CDS-WP-034 | Nothing |
| **M7** | Experience Foundation Ready | CDS-WP-039 | Nothing |
| **M8** | Multimodal Foundation Ready | CDS-WP-042 | Nothing |
| **M9** | Advanced Interaction Ready | CDS-WP-044 | Nothing |
| **M10** | Advanced Brand Platform | CDS-WP-047 | Nothing |
| **M11** | Distribution Candidate | CDS-WP-050 | Nothing |
| **M12** | Stable Readiness | CDS-WP-051 … CDS-WP-053 | Nothing — see the Stable boundary below |

**M11 is named "Distribution Candidate" and is not a Candidate award.** A
maturity state is granted only through the artifact maturity gate, per artifact
family, on admitted revision-bound evidence.

## Standing gates on the forward path

These are prerequisites recorded by the reconciliation. None of them is satisfied
today, and recording one satisfies nothing.

### Product Profile gate

No Product Profile exists, and none may be created before **CDS-WP-032** is
authorized and executed. A Product Profile **never overrides Core**; it is
bounded, expiring, and never retrospective legitimation (DEC-S-042, DEC-S-043).
The **Consumer Maintainer** role is currently **unstaffed**, and a Product Profile
requires it (FM-F-006). See
[Exception and Product Profile Governance](../governance/EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md)
and the
[Product Profile and Extension Model](../architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md).

### Real-consumer requirement

Committed consumer documentation evidences stated intent or built behaviour — it
is **never** user research and never evidence that an experience works for real
people (RISK-017). A design system validated against one reference consumer is
not validated. **CDS-WP-033** exists to require a **second real Core product**
before consumer-facing maturity claims are considered. Consumer repositories stay
**strictly read-only** in every work package; the CoreOps pilot remains
**inactive** and starts only on separate Human-Maintainer authorization.

### Generated-output authority boundary

Generated artifacts, design-tool representations, reference implementations,
evidence artifacts, consumer-local artifacts, research, and examples are **never
normative** (DEC-S-022). A generated artifact never stands against its source, and
a manual edit to one is invalid and must be reconciled back into the source
(DEC-S-031, DEC-S-079). This boundary is load-bearing for **CDS-WP-024**
(render gate), **CDS-WP-031** (render evidence), **CDS-WP-048** (distribution),
**CDS-WP-049** (design-tool adapters), and **CDS-WP-050** (runtime adapters):
each of those produces or consumes generated output, and **none of them may
acquire authority by doing so**. A renderer is not a governance authority.

### Semantic validation priority

The Semantic Status family is the **only** Candidate family in CDS, and it is a
meaning foundation with **no visual value**. Any visual binding of status
(**CDS-WP-023**) must therefore be gated by validation before it can be rendered:
**CDS-WP-024** defines the render gate and **CDS-WP-025** expands negative-fixture
coverage. Negative fixtures and fail-closed behaviour precede visual expression —
a status that cannot be validated must not be rendered as though it were.
Single-modality encoding of meaning stays prohibited, and text-first meaning
(`CDS-V4-STATUS-DESCRIPTION`) is a source rule, not a rendering preference. The
existing validation contract remains the
[V1–V4 Validation Contract](../architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md);
**an automated check is never sufficient accessibility evidence** (DEC-S-053).

### Authoring and validation separation

**AUTHOR is not VALIDATE. SOURCE CREATION is not CONFORMANCE DETERMINATION.**

Writing a normative machine-readable source and deciding whether a source conforms
are **two responsibilities held by two work packages**. This is a responsibility
boundary, not a runtime-dependency statement: a validator naturally consumes the
sources it checks, and **consuming a source confers no authority over it**.

| Responsibility | Owner | Never acquires |
| --- | --- | --- |
| Authoring visual token sources, source sets, identity, revision, provenance, topology, and — once its gates are satisfied — concrete normative values | **CDS-WP-020A** | Validator implementation, validation authority, conformance determination, evidence admission, maturity promotion, Product Profile activation, pilot activation, release authority, `Stable` declaration, runtime renderer implementation |
| Semantic validation, the render gate, and negative-fixture coverage | **CDS-WP-024** · **CDS-WP-025** | Source authoring, value selection, identifier creation, source-set identity, or any power to originate the normative sources it validates |

**Neither direction of drift is permitted.** A work package that authors sources
does **not** gain validation authority because validators read what it wrote, and a
validation work package does **not** gain authoring authority because it validates
what someone else wrote. **A renderer is not a governance authority** (see the
generated-output authority boundary above), and by the same reasoning **a validator
is not a source**.

**Authoring produces no conformance.** A source that exists has not been validated;
a source that validates has not been evidenced; evidence that exists has not been
admitted; and an admitted evidence record is not a maturity award. Each step is a
separate gate with a separate authority (DEC-S-022, DEC-S-053, DEC-S-126).

**Order.** CDS-WP-024 depends on CDS-WP-020A only in the sense that it validates
what CDS-WP-020A authors. That dependency is **not** permission for either to absorb
the other, and **neither is active or authorized**.

### Multimodal and AI scope-registration gate

**CDS-WP-040, CDS-WP-041, CDS-WP-042, and CDS-WP-044 address subject matter that
is not registered in the normative CDS scope today.** Audio and sonic design,
haptic feedback, multimodal feedback, and AI/agent interaction design appear in
**none** of the six capability domains of
[Concept and Scope](../governance/CONCEPT_AND_SCOPE.md), and audio and haptics
appear in **none** of the nine registered channels of the
[Artifact Distribution and Channel Model](../architecture/ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md)
or the six accessibility
[channel profiles](../governance/ACCESSIBILITY_CHANNEL_PROFILES.md).

Planning them here **does not register them**. Before any of these four work
packages may be authorized, the registered scope must first be extended through
an **Elevated** change to the normative scope sources, with Human-Maintainer
approval.

**CDS-WP-043 is only partly covered, and is not exempt by its title.**
*Security-aware interaction design* and *privacy-aware interaction design* are
registered cross-cutting concerns of
[Concept and Scope](../governance/CONCEPT_AND_SCOPE.md) and need no extension.
**"Safety" is not independently registered**, and it does not inherit coverage
from the security and privacy entries. CDS-WP-043 also stays **interaction design
only**: it may not import *security architecture*, which Concept and Scope assigns
to the **consumer** as a non-goal. If a safety scope is still part of CDS-WP-043
when it is proposed, that scope must be **confirmed before CDS-WP-043 is
authorized**.

### Stable boundary

**Stable is not reachable on this roadmap by sequence alone.** A Stable
transition needs its own gate, its own fresh revision-bound evidence, its own
independent review by a reviewer who is not the executor, and its own
Human-Maintainer admission and approval. AE-3 gates Stable for any artifact
carrying an accessibility obligation, and **no baseline environment has ever been
exercised**: A11Y-BL-001 remains a test contract, not evidence. Licence selection,
publication transition, release, and tag are separate Human-Maintainer decisions
that this roadmap neither makes nor prepares.

## Requirement classification model

Every incoming requirement — from a consumer, a review finding, research, or an
external benchmark — must land in **exactly one** of the following. This is an
**intake classification aid**, not an authority grant, and it does not override
the five normative constructs of the
[Product Profile and Extension Model](../architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md)
(Core Foundation · Product Profile · Consumer Extension · Domain Pattern Family ·
Local Exception).

| Classification | Meaning |
| --- | --- |
| **CDS Core Foundation** | Universal foundation owned by CDS; binding for every consumer. |
| **CDS Core Contract** | A universal contract obligation (meaning, behaviour, accessibility, provenance) rather than a value. |
| **Universal Component** | A component genuinely needed across consumers, carrying a component contract. |
| **General Pattern** | A recurring cross-consumer task or interaction pattern. |
| **Domain Pattern Family** | A bounded family for one domain; explicitly not universal core. |
| **Product Profile** | A bounded, expiring product-level profile — **never a Core override**. |
| **Channel Adapter** | A channel-specific transformation; generated, never normative. |
| **Consumer Extension** | Consumer-owned extension built on CDS contracts. |
| **Consumer-local** | Stays in the consumer. **A valid, non-inferior outcome.** |
| **Experimental Evidence** | Recorded as evidence only; AE-0 unless separately admitted; non-normative. |
| **Reject** | Not adopted. Also a valid outcome. |

**A consumer-specific need does not become CDS Core because a consumer asked.**
Classification precedes design; misclassification upward is how a design system
becomes an arbitrary collection of product-specific special solutions (non-goal
11).

## PB001 disposition

**PB001 is not held in this repository.** CDS-WP-017 searched the tracked
repository and found no PB001 artifact, no PB001 evidence, and no PB001 finding
text — only prior work-package notes recording PB001 as external benchmark
material that was deliberately **not integrated, not referenced, and not used as
evidence**.

PB001 remains, unchanged by this roadmap:

| Property | Value |
| --- | --- |
| Kind | **Experimental Evidence** |
| Accessibility evidence level | **AE-0** |
| Normative | **No** |
| Conformance evidence | **None** |
| Product Profile authority | **None** |
| Universal-core authority by itself | **None** |

The table below routes **PB001 finding topics to the work package that would own
them if they are ever brought forward**. Routing a topic to a work package
**imports no evidence, upgrades no evidence, authorizes no work package, and
creates no CDS requirement.** If PB001 material is ever to be used, it must first
be introduced through the requirement classification model above and evidenced on
its own terms.

| PB001 finding | Destination |
| --- | --- |
| Visual Foundation Gap | CDS-WP-019 · CDS-WP-020 |
| Semantic Status Visual Binding | CDS-WP-023 |
| StatusDisclosure | CDS-WP-027 |
| Semantic Validation | CDS-WP-024 · CDS-WP-025 |
| Product Profile / Brand Intake | CDS-WP-032 |
| Channel Preservation | CDS-WP-034 |
| Localization Preservation | CDS-WP-034 · CDS-WP-047 |
| Generated Output Authority | CDS-WP-024 · CDS-WP-031 · CDS-WP-048 |
| Second Consumer | CDS-WP-033 |

**No PB001 evidence is upgraded by this document.**

**Status after CDS-WP-019 (2026-08-26).** The *Visual Foundation Gap* topic routed
above reached its first destination. **CDS-WP-019 imported nothing from PB001**:
PB001 is **not held in this repository**, its finding text remains **outside** it,
and CDS-WP-019 obtained no PB001 material, cited none, and used none as an input.
The visual foundation architecture was derived **entirely** from the committed
normative CDS sources and the registered consumer requirements. **PB001 remains
Experimental Evidence at AE-0, non-normative, with no conformance evidence, no
Product Profile authority, and no universal-core authority** — unchanged — and the
routing to **CDS-WP-020** stands. Should PB001 material ever be used, it must first
be introduced through the requirement classification model above and evidenced on
its own terms.

## Deferred finding disposition

The following review findings are routed to **CDS-WP-018 — Deferred Governance
and Repository Hygiene Reconciliation**. CDS-WP-017 **classifies and routes them
only**; it repairs none of them, and routing is not repair.

As with PB001, CDS-WP-017 searched the tracked repository and found **no
pre-existing occurrence of any of these identifiers**: before this routing was
written, no finding text and no finding record for them was held here. The routing
itself is now the only reason the identifiers appear in the repository at all, and
an identifier in a routing table is **not** the finding.

The finding text is still held **outside this repository**. This table therefore
routes them **by identifier only**, and CDS-WP-018 must obtain each finding's text
from its original source and reconstruct its content before acting on it.
**Routing is not repair**, and a routed identifier is not a local authority for what
the finding says.

| Finding | Disposition |
| --- | --- |
| `R3R-003` | Deferred → **CDS-WP-018** |
| `NF-R3-OBS-001` | Deferred → **CDS-WP-018** |
| `NF-R4-OBS-001` | Deferred → **CDS-WP-018** |
| `NF-R4-OBS-002` | Deferred → **CDS-WP-018** |
| `NF-R5R-OBS-001` | Deferred → **CDS-WP-018** |
| `NF-R5R-OBS-002` | **Informational** — historical evidence limitation; **no repair required**; not routed |
| `NF-R5R-OBS-003` | Deferred → **CDS-WP-018** |

**Status after CDS-WP-018 (2026-08-25).** The routing above is CDS-WP-017's record
and is not rewritten. CDS-WP-018 has since taken up all six routed findings, plus
`F-017-01`, `F-017-02`, `R1-F-01`, `R2-N-01`, and `R2-N-02`, and classified each as
repaired, preserved as historical, or explicitly not repaired with a destination.
What it did and did not do is recorded in
[Work Packages](../../project-system/WORK_PACKAGES.md) and the
[CDS-WP-018 notes](../../project-brain/CDS_WP_018_DEFERRED_GOVERNANCE_HYGIENE_NOTES.md).
`F-017-03` and `R1-F-05` were **not** CDS-WP-018 work and remain routed to their
scope gates; the `F-017-04` phase label remains an open governance item.

### Repository-side findings observed by CDS-WP-017

CDS-WP-017 observed the following while reconciling. Each is recorded and **not
repaired**. They do **not** share one destination: only the first two are
CDS-WP-018 hygiene. **Routing is not repair**, and a governance item is not a
hygiene item.

| ID | Observation | Disposition |
| --- | --- | --- |
| **F-017-01** | `project-system/PROJECT_PROFILE.md` — "Intentionally open decision areas" still lists *token format*, *versioning and maturity model*, *conformance and adoption policy*, and *product profile and override governance* as open, although CDS-WP-006 and CDS-WP-011 decided them (DEC-S-035…044, ADR-0001). | Deferred → **CDS-WP-018** |
| **F-017-02** | `README.md` — the equivalent open-decision list carries the same drift for *versioning and maturity model* and *conformance and adoption policy*. | Deferred → **CDS-WP-018** |
| **F-017-03** | Scope registration gap for audio/sonic, haptic, multimodal, and AI/agent subject matter — see the multimodal and AI scope-registration gate above. Not blocking for anything currently authorized. | **Not CDS-WP-018 hygiene.** → a future **Elevated scope / capability-registration gate**, which **blocks later authorization of CDS-WP-040, CDS-WP-041, CDS-WP-042, and CDS-WP-044 until resolved**. |
| **F-017-04** | The phase label set by **DEC-S-062** ("Pre-Candidate Operating Enablement") predates the completed first Candidate transition. **The label remains authoritative until a Decision supersedes it**, and it names an *operating phase*, **not a maturity state**. The staleness is broader than the label alone: dependent operating-description and current-state text still carries **Pre-Candidate assumptions** the repository has outgrown — for example prose asserting that no token, format, tool, or Candidate is created or selected in this phase, although a Semantic Status token source, ADR-0001, `tools/cds_validator`, and one Candidate family all now exist. It also includes **stale forward "next work package" references** frozen at the time each dependent text was written — `CLAUDE.md` naming **CDS-WP-010** as "the next work package", the historical CDS-WP-009 [Pre-Candidate Operating Plan](PRE_CANDIDATE_OPERATING_PLAN.md) naming **CDS-WP-011**, and the [Foundation Closure Record](../governance/FOUNDATION_CLOSURE_RECORD.md) naming **CDS-WP-010** — none of which is the current work package. **CDS-WP-017 renames nothing and repairs none of that text.** | **Not an executor-owned CDS-WP-018 decision.** → **open governance / phase-transition item**: a relabel requires a **new Decision superseding DEC-S-062**. **CDS-WP-018 reconciled the dependent documentary text only** — it corrected the stale `CLAUDE.md` operating description and its `CDS-WP-010` next-work-package reference, and framed the historical carriers as historical; it **did not rename the phase, create a superseding Decision, or touch `DECISION_INDEX.md`**. The label itself remains open. **None of this blocked CDS-WP-017 integration.** |

**Status after the phase transition (2026-08-26).** The routing table above is
CDS-WP-017's record and is **not rewritten**. Since it was written, **DEC-S-127**
has superseded DEC-S-062 for current and future phase state, relabelling the project
phase to **`Post-Candidate Foundation & Design-System Enablement`**. Its effect on
the four findings:

| ID | Status |
| --- | --- |
| `F-017-01`, `F-017-02` | Unchanged — repaired by CDS-WP-018; remain closed. |
| `F-017-03` | **Unchanged and still open.** The phase transition **registers no capability** for audio/sonic, haptic, multimodal, or AI/agent subject matter; the future **Elevated scope / capability-registration gate** still blocks later authorization of CDS-WP-040, CDS-WP-041, CDS-WP-042, and CDS-WP-044. |
| **`F-017-04`** | **Phase-label governance portion: CLOSED BY DEC-S-127.** The relabel is decided rather than drifted, and DEC-S-062 stays `Accepted` and historically valid. The dependent-document hygiene CDS-WP-018 already repaired **remains closed**. The **dated historical references remain historical and are not rewritten** — including the stale forward "next work package" pointers inside the [Pre-Candidate Operating Plan](PRE_CANDIDATE_OPERATING_PLAN.md) and the [Foundation Closure Record](../governance/FOUNDATION_CLOSURE_RECORD.md), which are correct for their dates. **Source history is not rewritten merely to remove an identifier.** |

### Findings from the R1 independent review

The fresh independent review of this reconciliation (**R1**, reviewer ≠ executor)
returned **PASS WITH NOTES** with six findings. Four were corrected in the
CDS-WP-017 artifacts themselves under a bounded, Nova-authorized micro-rework; the
two below need a forward destination and are recorded here. **Recording a finding
repairs nothing and authorizes nothing.**

| ID | Observation | Disposition |
| --- | --- | --- |
| **R1-F-01** | Two Candidate-era records — the [Candidate Promotion Effectivity Record](../governance/SEMANTIC_STATUS_CANDIDATE_PROMOTION_EFFECTIVITY_RECORD.md) and the [Candidate Dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md) — each still carry a row stating `CDS-WP-017: INACTIVE`. Both were true when written and are made stale by CDS-WP-017's own activation. | Deferred → **CDS-WP-018**. **Neither record was modified**: both are dated point-in-time records, and this work package rewrites no such record. Any later repair must be **additive** — a dated supersession note, or removal of work-package-status rows from maturity-boundary tables — never a rewrite of the dated tables. The controlled carrier for work-package status remains [Work Packages](../../project-system/WORK_PACKAGES.md). |
| **R1-F-05** | **CDS-WP-043** is titled "Security and Safety Interaction Patterns", but *safety* is not independently registered scope. | Deferred → a **CDS-WP-043 scope check before authorization**; see the multimodal and AI scope-registration gate above. CDS-WP-043 is **not renamed** here. |

### Findings observed by CDS-WP-019

Recorded while defining the visual foundation architecture. Each is **recorded and
not repaired** — CDS-WP-019 is an architecture work package, not a hygiene pass, and
**routing is not repair**. None of them blocked CDS-WP-019.

| ID | Observation | Disposition |
| --- | --- | --- |
| **F-019-01** | `docs/governance/CONCEPT_AND_SCOPE.md` — its *"Open questions and deferred decisions"* list still carries **token format**, **versioning and maturity model**, **conformance and adoption policy**, and **product profile and override governance** as undecided, although CDS-WP-006 and CDS-WP-011 decided them. This is the same drift **F-017-01 / F-017-02** repaired elsewhere; `CONCEPT_AND_SCOPE.md` was **not** in CDS-WP-018's file list. | Deferred → a **bounded, separately authorized governance reconciliation**. It is a **normative scope source**, and its change control requires an authorized work package naming it. **Not repaired by CDS-WP-019.** |
| **F-019-02** | Capability-domain enumeration asymmetry: **DEC-S-021 Layer 3 registers *iconography*** but capability domain 3 of `CONCEPT_AND_SCOPE.md` does not name it, and neither domain names *illustration* or *imagery* although the deferred-decisions list does. CDS-WP-019 positioned icons at **Layer 3** (per DEC-S-021) and illustration and imagery at **Layer 2**, and registered no new scope. | Deferred → the same governance reconciliation as F-019-01, or **CDS-WP-037 / CDS-WP-045** at authorization. **Not repaired by CDS-WP-019.** |
| **F-019-03** | **CR-004** (*viewport strategy and breakpoints*) is mapped to **Layer 5** in the normative [Architecture Requirements Traceability](../architecture/ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md), while this roadmap plans **CDS-WP-021** at **Layer 3**. CDS-WP-019 states the reconciling reading — *Layer 3 owns the spatial vocabulary; Layer 5 owns the strategy that uses it* — and **does not edit the traceability matrix**. | Deferred → **CDS-WP-021 must confirm the split before defining any responsive foundation.** **Not repaired by CDS-WP-019.** |
| **F-019-04** | `docs/architecture/TOKEN_AND_THEME_ARCHITECTURE.md` — its *"Unresolved format and tooling questions"* still present questions **1** (machine-readable format), **2** (naming convention), and **7** (validation layers and blocking) as open, although ADR-0001, DEC-S-081, and the V1–V4 validation contract decided them; its preamble still describes the token interoperability source as a non-implementable preview, which DTCG 2025.10 and ADR-0001 superseded. Question **3** (transformation tool) remains genuinely open. | Deferred → a **bounded, separately authorized reconciliation**, or **CDS-WP-020**. Same class as `NF-R4-OBS-001`. **Not repaired by CDS-WP-019.** |
| **F-019-05** | `docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md` — its *"Deferred technical decisions"* list still carries **token format**, **token naming convention**, **maturity model**, **versioning scheme**, **accessibility conformance level**, and **concrete status taxonomy and naming** as deliberately open, although each has been decided. CDS-WP-019 edited that document **additively only** (one *Related documents* row) and did **not** touch the list. | Deferred → the same reconciliation as F-019-04. **Not repaired by CDS-WP-019.** |
| **F-019-06** | **No registered consumer requirement asks for a colour palette, a typographic scale, a spacing scale, a radius scale, an elevation model, an icon library, or illustration.** Four of the nine visual foundation families — **VF-3, VF-5, VF-6, VF-7** — carry **no consumer demand evidence at all**. | **Recorded as honesty, not as a defect**, in the [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md). It is the same treatment CDS-WP-005 gave CR-030. Mapped to **RISK-026** and **RISK-003**; **no new risk is registered**. |
| **F-019-07** | The visual foundation adds **nine artifact families**, each with its own maturity, evidence, and gate, to a governance model run by **one** Human Maintainer, with the **Consumer Maintainer role unstaffed** (FM-F-006). | **Recorded** in the [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md) as an open capacity question for **CDS-WP-020**. Mapped to **RISK-021**, **RISK-026**, **RISK-029**, **RISK-040**; **no new risk is registered**. |
| **F-019-08** | The phase label set by **DEC-S-062** stays coherent for CDS-WP-019 but will be **materially strained by CDS-WP-020**, the first work package that would create real visual values. | **`PHASE_TRANSITION_RECOMMENDED`** raised as a forward-looking recommendation, tied to the still-open **F-017-04**, to be resolved **before CDS-WP-020 is authorized**. **CDS-WP-019 renames nothing and creates no Decision.** |
| **F-019-09** | **`R1-F-01` recurs by construction.** The [Candidate Dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md) carries `CDS-WP-018 **active**` in its *"Current state (authoritative for this document)"* header — true when CDS-WP-018 wrote it, made stale by CDS-WP-019's activation. This is the **same recurrence R1-F-01 described**, and it will recur at every activation for as long as a maturity-boundary record carries a work-package-status row at all. | **Not repaired by CDS-WP-019**: `docs/operations/**` is outside this work package's file scope. Deferred → a **bounded, separately authorized repair**. Per the R1-F-01 disposition, any repair must be **additive** — a dated supersession note, or **removal of the work-package-status row from the maturity-boundary record** — never a rewrite of a dated table. **Removal is the structural fix**: the controlled carrier for work-package status is [Work Packages](../../project-system/WORK_PACKAGES.md), and the dossier header already says so. **Disclosure:** the dated CDS-WP-017 forward-view note in the [Pre-Candidate Operating Plan](PRE_CANDIDATE_OPERATING_PLAN.md) likewise still reads *"CDS-WP-019 onwards is `Planned` only"*; it is **historical by its own header**, its prohibitions remain in force, and it is **not rewritten**. |

**Status after the phase transition (2026-08-26).** The CDS-WP-019 findings table
above is that work package's record and is **not rewritten**. One finding has since
been dispositioned:

| ID | Status |
| --- | --- |
| **`F-019-08`** — `PHASE_TRANSITION_RECOMMENDED` | **CLOSED / SATISFIED BY DEC-S-127.** The recommendation asked that the phase label be resolved **before CDS-WP-020 is authorized**; DEC-S-127 does exactly that, superseding DEC-S-062 for current and future state and relabelling the phase to **`Post-Candidate Foundation & Design-System Enablement`**. The **phase-label portion of the tied item `F-017-04` closes with it.** |

`F-019-01` … `F-019-07` and `F-019-09` are **unchanged** by the phase transition and
keep their recorded dispositions. A relabel repairs no document and closes no
hygiene item.

### Findings observed by CDS-WP-020

Recorded while defining the reference and semantic visual token contract. Each is
**recorded and not repaired** — CDS-WP-020 is a contract work package, not a hygiene
pass, and **routing is not repair**. None of them blocked CDS-WP-020.

| ID | Observation | Disposition |
| --- | --- | --- |
| **F-020-01** | The **value half** of CDS-WP-020 is gated on **seven** normative choices that no committed CDS source has made. The five earlier work packages that made comparable first-of-their-kind normative choices — **CDS-WP-011 … CDS-WP-015** — each registered a Decision block, and three of them an ADR; CDS-WP-020 holds no authority to register either. | **`DECISION_REQUIRED`.** Recorded as **OD-1 … OD-7** in the **non-normative** [Visual Token Foundation Open Decisions](VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md) register. **Partially answered on 2026-08-27** by the Human-Maintainer-authorized **CDS-WP-020 Decision Integration Pass**: **DEC-S-128, DEC-S-129, DEC-S-130, DEC-S-131** and **ADR-0004** were **prepared and authorized for integration, and at that date NOT YET EFFECTIVE**. They answer **OD-1, OD-2 and OD-3** and add the contrast evaluation authority. **OD-4 … OD-7 stay open, the value half stays gated, and CDS-WP-020 stays `DECISION_REQUIRED` and not closed.** *(Stated as at 2026-08-27, before integration.)* **Superseded in part:** the CDS-WP-020 object was integrated by the Human-Maintainer commit `42a568d823de3388e45af62967546f13ad67eff6` — at which **DEC-S-128 … DEC-S-131 and ADR-0004 became effective** — and CDS-WP-020 is now **`Closed`**, closure effective at the Human-Maintainer commit `3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`. **The `DECISION_REQUIRED` result stands as the executed result of the work package**, **OD-4 … OD-7 stay open**, and the value half stays gated; the value and machine-readable work is routed to **`CDS-WP-020A`** (`FR-N-03`), which is **`Planned`, not active, and not authorized**. |
| **F-020-02** | **AF-1 / AF-3 versus source-set metadata.** A source-set payload carries **one** `maturityState`, but the [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md) requires that maturity is never inherited (AF-1) and that a family may mature at its own pace (AF-3). A shared visual source set cannot express both. **Corrected 2026-08-27 — see the disposition.** | **ANSWERED by DEC-S-131**, with the finding corrected precisely: its **conclusion stands** — a shared visual source set cannot express per-family maturity, so the unit is **one source set per independently evaluable Family × Token-Flow-Layer unit**. Its **artifact-count mechanism was imprecise**: it implied that per-family, per-layer source sets multiply manifests and resolvers at the same rate. They do not — the committed manifest contract carries a **`sourceSets` array**, so **one manifest may aggregate many source sets**, each retaining its own maturity. **A source set is not a manifest**, and **AGGREGATED is not MATURE**. **Residual:** the concrete root identifiers are **not** created, coupled to **OD-4**; **OD-6 stays open and is not pre-answered**. |
| **F-020-03** | **T-2 is vacuously satisfiable today.** *"Every semantic role must resolve in every supported context"* is trivially true when **zero** contexts are supported, so it cannot guide whether a default role binding is legitimate or a pre-emption of **CDS-WP-022**. | Recorded as **OD-7**. The [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) adds **TC-6** so the gap is at least stated. **The theme mechanism remains CDS-WP-022's.** |
| **F-020-04** | The offline validator's bounded token-`$type` set is routinely readable as a **CDS profile admission**. It is a **DEC-S-098 V2 coverage boundary**, and the committed token-document schema constrains `$type` **not at all**. | Stated explicitly in the [Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md) machine-readable disposition and in **OD-2**, citing **RISK-074**. **CLOSED by DEC-S-130** (2026-08-27, effective at commit `42a568d823de3388e45af62967546f13ad67eff6`), which states the admission profile explicitly — `color`, `dimension`, `number` — and restates that **a tool accepting a type is not the profile admitting it**. **The DEC-S-098 coverage boundary is unchanged, and no schema, validator, test, or fixture was changed.** |
| **F-020-05** | **`F-019-04` is incomplete.** `docs/architecture/TOKEN_AND_THEME_ARCHITECTURE.md` question **4** (*"How are aliases represented?"*) is stale in the same way F-019-04 records questions 1, 2, and 7 to be: the [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md) and **DEC-S-078** settled alias representation. F-019-04 does not currently name question 4. | Deferred → the **same destination as `F-019-04`**: a bounded, separately authorized reconciliation. **Not repaired by CDS-WP-020**, which edited no CDS-WP-005 document. |
| **F-020-06** | **`F-019-06` is load-bearing for the role vocabulary.** No registered consumer requirement asks for a palette, a type scale, a spacing scale, a radius scale, an elevation model, an icon library, or illustration, and **VF-3, VF-5, VF-6, VF-7** carry no consumer demand evidence at all. Inventing a full role vocabulary now would be unevidenced structure. | Carried into **OD-6** as the argument for a **minimal vocabulary bound to the six registered Layer-3 consumer anchors**. Mapped to **RISK-021**, **RISK-026**, **RISK-003**; **no new risk is registered**. |
| **F-020-07** | **The pinned validator stack is not installed** in the execution environment (`jsonschema`, `rfc8785`, `pytest` absent; no venv), and installing dependencies is prohibited without explicit approval. **No validator run and no test execution was possible.** | Recorded. **No implementation file was added**, so no regression run was owed, and **nothing was weakened to compensate**. A future implementation work package must have the pinned stack available before it may add a machine-readable source. |
| **F-020-08** | **`F-019-07` is answerable only together with the role vocabulary.** Nine artifact families, one Human Maintainer, Consumer Maintainer unstaffed (FM-F-006) — the capacity question CDS-WP-019 routed here cannot be separated from how many roles and families actually exist. | Answered as a **recommendation inside OD-6** — reduce the number of families matured separately. **The family register was not changed**, and **`F-019-07` stays open** until OD-6 is decided. |

**Recording a finding repairs nothing and authorizes nothing.**

### Findings from the CDS-WP-020 integration review

Raised by Nova against the integrated CDS-WP-020 object and adjudicated with
Human-Maintainer approval. As with the CDS-WP-017 routing above, the tracked
repository held **no pre-existing occurrence of the `FR-N-` identifiers** before
this record was written; the record itself is the only reason the identifier appears
here, and **an identifier in a routing table is not the finding**.

**Only `FR-N-03` was supplied to the closure and routing pass.** Other findings from
that review are separately governed; their text was not provided, and **this pass
neither reconstructs nor disposes of them**.

| ID | Observation | Disposition |
| --- | --- | --- |
| **`FR-N-03`** | The concrete machine-readable **Visual Token Source / Value Authoring** work had **no explicit work-package destination**. Left unrouted, it would have been absorbed into **CDS-WP-024**, giving one work package both source-authoring and conformance-determination authority. | **RESOLVED BY EXPLICIT AUTHORING-WP DESTINATION.** Human-Maintainer-approved Nova adjudication, **Option 2**: authoring and validation stay separate. The destination is **`CDS-WP-020A` — Visual Token Source Authoring and Source Set Realization**, registered in Phase V as **`Planned` · not active · not authorized**, with its scope, exclusions, and order relative to CDS-WP-024 stated in [Work Packages](../../project-system/WORK_PACKAGES.md) and in the authoring-and-validation-separation gate above. **CDS-WP-024 keeps its validation and conformance boundary unchanged.** **Routing is not repair, and registration is not activation.** |

### Findings observed by the CDS-WP-020 closure and routing pass

Observed while reconciling the current-state carriers for closure. **Recorded and
not repaired by that pass** — it was a bounded closure and routing pass, not a
hygiene work package. Neither finding blocked closure. **`F-020C-01` has since
been resolved** by the separately authorized CDS-WP-020 post-integration
effectiveness reconciliation; **`F-020C-02` remains deferred.**

| ID | Observation | Disposition |
| --- | --- | --- |
| **`F-020C-01`** | **STALE CURRENT-STATE — decision and ADR effectivity.** *(Observed by the closure and routing pass; since resolved.)* Live assertions across **21** files still stated that **DEC-S-128 … DEC-S-131** and **ADR-0004** were `PROPOSED / AUTHORIZED FOR INTEGRATION` and **NOT YET EFFECTIVE** *"until the Human-Maintainer exact-byte integration commit"*, and that the effective registers stayed at **DEC-S-127** and **ADR-0003** — **74** by that pass's count. That commit has occurred — `42a568d823de3388e45af62967546f13ad67eff6` — so the stated condition is met and the qualification is stale. Carriers include the **normative** [Decision Index](../decisions/DECISION_INDEX.md) *Register scope* section and the **ADR-0004** status line. | **RESOLVED → the separately authorized CDS-WP-020 post-integration effectiveness reconciliation** (2026-08-31), on the **CDS-WP-016 post-promotion precedent**, where current-state reconciliation after an exact-byte commit was its own authorized pass. **Not repaired by the closure and routing pass:** the volume was a material scope expansion beyond closure and routing, and **marking an ADR `Accepted` is a Human-Maintainer act** the executor may not perform autonomously; **that pass asserted no effectivity state** and changed no effectivity wording anywhere. The reconciliation pass reproduced the finding independently — **78 line-hits / 69 merged statements across 21 files at baseline `42a568d8…`**, and **83 / 74 across 22 files** in the combined working tree — and reconciled the live carriers to the effective state. It **records a completed Human-Maintainer act and performs none**: acceptance follows from the exact-byte integration commit to which the reviewed ADR and Decision text bound it. **The decision and ADR *counts* — 131 and 4 — were already correct** in the register; only the effectivity qualification was stale. |
| **`F-020C-02`** | **Milestone mapping not re-derived.** **M2 — Visual Foundation Ready** is *"reached after CDS-WP-022"*. Registering **CDS-WP-020A** in Phase V leaves it unstated whether M2 should also depend on it. | **Deferred → Nova and Human-Maintainer disposition once OD-4 … OD-7 are decided.** **M2 is unchanged.** Re-deriving it now would be a sequencing decision, and **OD-7 — the sequencing of value-selection work against CDS-WP-022 — is open**. |

### Finding observed after the CDS-WP-020 closure commit

| ID | Observation | Disposition |
| --- | --- | --- |
| **`F-020C-04`** | **POST-CLOSURE CURRENT-STATE EFFECTIVITY DRIFT.** Live current-state carriers still described CDS-WP-020 closure in pre-integration terms — *closure proposed*, *not yet effective*, *becomes effective only at the Human-Maintainer integration commit*, *recorded in the working object* — although the Human-Maintainer closure integration commit `3f37ecfe54dad82f8064aaff521ff9e3aec65fd7` (parent `42a568d823de3388e45af62967546f13ad67eff6`) had occurred and its exact object had passed the **CDS-WP-020 EXACT-OBJECT CLOSURE INTEGRATION GATE R4**. Those formulations were truthful **before** that commit; they are stale only as **live** current state. | **RESOLVED → the separately authorized CDS-WP-020 post-closure current-state reconciliation** (2026-08-31), on the **CDS-WP-016 post-promotion precedent**, where current-state reconciliation after a Human-Maintainer commit was its own authorized pass. The live carriers now record CDS-WP-020 as **`Closed`, effective at that commit**, and **no work package as currently authorized**. It **records a completed Human-Maintainer act and performs none.** **Point-in-time records were preserved**, not rewritten: dated review, execution, decision-time, and event-time changelog statements remain as written. **No successor was activated**; **no Decision, ADR, or risk was added, changed, or removed**; and **`DECISION_REQUIRED` stands as the executed result of CDS-WP-020.** |

## Immediate next step

**A Human-Maintainer decision on OD-4, OD-5, OD-6 and the OD-7 sequencing, and a
separate explicit Human-Maintainer authorization of a next work package. Neither
has occurred, and no work package is currently authorized.**

The steps this section previously named — *independent review of the CDS-WP-020
closure and routing object, Nova adjudication, and the Human-Maintainer exact-byte
integration commit that makes CDS-WP-020 closure effective* — **have been
completed.** The reviewed CDS-WP-020 object was integrated by the Human-Maintainer
commit `42a568d823de3388e45af62967546f13ad67eff6`, and the closure and routing object by the
Human-Maintainer commit `3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`.

**CDS-WP-020 closure is effective at that commit.** **No later work package was
activated by it** — **`CDS-WP-020A`** and **CDS-WP-021 … CDS-WP-053** all remain
`Planned`, not active, and not authorized, and each begins only on an explicit Nova
prompt **and** separate Human-Maintainer authorization. **Closure answers no open
decision, satisfies no value prerequisite, and selects no value.**

**The effectivity qualification of DEC-S-128 … DEC-S-131 and ADR-0004 was not
reconciled by the closure and routing pass**; it is routed as **`F-020C-01`** above
and has since been **resolved**.

### CDS-WP-020 Decision Integration Pass — 2026-08-27

**Authorized separately by the Human Maintainer on 2026-08-27**, following the Nova
adjudication of OD-1 … OD-7. It **prepared, and did not commit**:

| Instrument | Substance |
| --- | --- |
| **DEC-S-128** | One canonical normative visual colour representation — the pinned DTCG 2025.10 colour space keyed `srgb`; OKLCH derivational only; delivery quantization at the channel boundary; out-of-model source values fail closed |
| **DEC-S-129** | **WCAG 2.2** as the contrast evaluation authority — not `WCAG 2.x`, not `latest`; full-precision comparison with no rounding before comparison; APCA and other methods **informational only**; an automated calculation is **not** evidence and grants **no** AE level |
| **DEC-S-130** | An explicit, minimal, closed `$type` admission profile — `color`, `dimension`, `number`; explicit own typing; no composites; `$type` carries value-type semantics only; **`profileVersion` stays `"1"`** |
| **DEC-S-131** | The **Source Set** as the independently evaluable unit; one set per Family × Token-Flow-Layer; maturity binds to (`sourceSetId`, `sourceRevision`); **AGGREGATED is not MATURE** |
| **ADR-0004** | Architecture rationale for DEC-S-128, DEC-S-130 and DEC-S-131. **DEC-S-129 is deliberately not an architecture dependency of it.** |

**All five are effective.** Effectivity occurred **only** at the Human-Maintainer
exact-byte integration commit `42a568d823de3388e45af62967546f13ad67eff6`, which
followed a Fresh Independent Review and Nova integration adjudication. **A review
PASS is not a commit, and a Nova recommendation is not an approval.** The effective
registers are therefore **DEC-S-131** and **ADR-0004**.

**What the pass did not do:** it created **no** visual value, **no** identifier,
**no** token source file, manifest, resolver, schema, validator rule, test, or
fixture; it admitted **no** evidence; it changed **no** maturity; it accepted,
closed, or re-scored **no** risk — **`RISK-099` was assessed and is not required**,
because the normative OKLCH-to-sRGB accessibility-path conversion architecture that
would have created the exposure was **rejected**; it registered **no** capability;
it made **no** claim; it touched **no** Semantic Status byte; and it activated
**no** work package. **The pass itself did not close CDS-WP-020**; closure was
recorded separately by the CDS-WP-020 closure and routing pass and became effective
at its Human-Maintainer integration commit `3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`.

### Standing position

**CDS-WP-020 was authorized separately by the Human Maintainer on 2026-08-26** —
its authorization came from that decision alone, **not** from its position in this
roadmap — and it was **executed with result `DECISION_REQUIRED`**. Its reviewed
object was then **integrated** by the Human-Maintainer commit
`42a568d823de3388e45af62967546f13ad67eff6`, and the CDS-WP-020 closure and routing
pass recorded it as **`Closed`**. **That closure is effective** at the
Human-Maintainer integration commit of that object,
`3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`. **Closure grants no maturity, no evidence,
no claim, and no publication effect**, and **no work package is currently
authorized.**

**CDS-WP-019 is closed**, integrated by the Human-Maintainer commit
`538fbccbf6f554de3b872e9fb75a70d13318feb6`, and **the phase-transition item is
resolved**: **DEC-S-127 (2026-08-26) supersedes DEC-S-062 for current and future
phase state**, closing `F-019-08` and the phase-label portion of `F-017-04`. **The
transition authorized nothing** — the CDS-WP-020 authorization was an independent
Human-Maintainer decision taken afterwards.

**CDS-WP-020 did not create the visual values the phase-transition item
anticipated.** Its contract half is delivered; its value half was **gated** on seven
normative choices no committed CDS source had made, recorded as **OD-1 … OD-7** in
the **non-normative**
[Visual Token Foundation Open Decisions](VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
register. **Three of the seven are now answered** — OD-1, OD-2 and OD-3, by the
Decision Integration Pass above — and **the value half stays gated all the same**:
**OD-4, OD-5, OD-6 and OD-7 are open**, and **VP-3, VP-4 and VP-5 remain
unsatisfied for every visual family**. **Visual values: 0. Visual source sets: 0.
Visual Candidate families: 0. VF-1 … VF-9: `Proposed`.**

**OD-7 carries a sequencing recommendation this roadmap must not act on by
itself:** that **CDS-WP-022 — Theme and Environmental Presentation Model** be
considered before any value-selection work package, because colour values and the
light/dark token layering are the same decision seen from two sides. **A roadmap
entry is a plan, not permission** — reordering the sequence is a Human-Maintainer
decision, and **CDS-WP-021 … CDS-WP-053 all remain `Planned`, not active, and not
authorized.**

## Related documents

- [Work Packages](../../project-system/WORK_PACKAGES.md) — the controlled work-package roadmap
- [Next Phase](../../project-system/NEXT_PHASE.md)
- [Pre-Candidate Operating Plan](PRE_CANDIDATE_OPERATING_PLAN.md) — historical (CDS-WP-009)
- [First Semantic Status Candidate Plan](FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md) — historical, plan complete
- [Machine-Readable Source Implementation Plan](MACHINE_READABLE_SOURCE_IMPLEMENTATION_PLAN.md)
- [Design System Architecture](../architecture/DESIGN_SYSTEM_ARCHITECTURE.md)
- [Governance Operating Model](../governance/GOVERNANCE_OPERATING_MODEL.md)
- [Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md)
- [Concept and Scope](../governance/CONCEPT_AND_SCOPE.md)
- [Accessibility and Inclusive Design Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [Candidate Promotion Effectivity Record](../governance/SEMANTIC_STATUS_CANDIDATE_PROMOTION_EFFECTIVITY_RECORD.md)
- [Visual Token Foundation Open Decisions](VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md) — **non-normative**; OD-1 … OD-7 (CDS-WP-020); OD-1 … OD-3 answered, OD-4 … OD-7 open
- [Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md) · [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) · [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
- [ADR-0004 — Visual Token Representation and Source Identity Architecture](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md) — **`Accepted`, effective at commit `42a568d8…`**
- [Decision Index](../decisions/DECISION_INDEX.md) · [Risk Register](../risks/RISK_REGISTER.md)
