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

**CDS-WP-018 through CDS-WP-053 are `Planned`, `Not active`, and `Not authorized
for execution`. Work on them has not started.** Each becomes executable only on an
explicit Nova prompt **and** Human-Maintainer authorization, one work package at a
time. Nothing in this document activates the next one automatically.

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
| CDS-WP-017 | Post-WP-016 Roadmap, Authority and Scope Reconciliation | 1 | **Active** |
| CDS-WP-018 | Deferred Governance and Repository Hygiene Reconciliation | 1 | Planned · not active |

### Phase V — Visual Foundation

| ID | Title | Layer | Status |
| --- | --- | --- | --- |
| CDS-WP-019 | Core Visual Foundation Architecture | 3 | Planned · not active |
| CDS-WP-020 | Reference and Semantic Token Foundation | 3 | Planned · not active |
| CDS-WP-021 | Adaptive Layout and Responsive Foundation | 3 | Planned · not active |
| CDS-WP-022 | Theme and Environmental Presentation Model | 3 | Planned · not active |

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

**Sequence integrity:** CDS-WP-017 … CDS-WP-053 is a contiguous range of **37**
identifiers with no gap and no duplicate. **36** of them are `Planned · not
active`; exactly **one**, CDS-WP-017, is active.

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

## Deferred finding disposition

The following review findings are routed to **CDS-WP-018 — Deferred Governance
and Repository Hygiene Reconciliation**. CDS-WP-017 **classifies and routes them
only**; it repairs none of them, and routing is not repair.

As with PB001, CDS-WP-017 searched the tracked repository and found **no
occurrence of any of these identifiers**. They are held outside this repository,
so this table routes them **by identifier**, and CDS-WP-018 must obtain each
finding's text from its source before acting on it.

| Finding | Disposition |
| --- | --- |
| `R3R-003` | Deferred → **CDS-WP-018** |
| `NF-R3-OBS-001` | Deferred → **CDS-WP-018** |
| `NF-R4-OBS-001` | Deferred → **CDS-WP-018** |
| `NF-R4-OBS-002` | Deferred → **CDS-WP-018** |
| `NF-R5R-OBS-001` | Deferred → **CDS-WP-018** |
| `NF-R5R-OBS-002` | **Informational** — historical evidence limitation; **no repair required**; not routed |
| `NF-R5R-OBS-003` | Deferred → **CDS-WP-018** |

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
| **F-017-04** | The phase label set by **DEC-S-062** ("Pre-Candidate Operating Enablement") predates the completed first Candidate transition. **The label remains authoritative until a Decision supersedes it**, and it names an *operating phase*, **not a maturity state**. The staleness is broader than the label alone: dependent operating-description and current-state text still carries **Pre-Candidate assumptions** the repository has outgrown — for example prose asserting that no token, format, tool, or Candidate is created or selected in this phase, although a Semantic Status token source, ADR-0001, `tools/cds_validator`, and one Candidate family all now exist. **CDS-WP-017 renames nothing and repairs none of that text.** | **Not an executor-owned CDS-WP-018 decision.** → **open governance / phase-transition item**: a relabel requires a **new Decision superseding DEC-S-062**. Dependent documentary and historical hygiene may be reconciled separately, around or after that decision. **None of this blocks CDS-WP-017 integration.** |

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

## Immediate next step

**CDS-WP-018 — Deferred Governance and Repository Hygiene Reconciliation.**

CDS-WP-018 is **inactive** and **remains inactive until separately authorized by
the Human Maintainer**. CDS-WP-017 does not start it, does not scope it in
detail, and does not perform any part of it in advance.

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
- [Decision Index](../decisions/DECISION_INDEX.md) · [Risk Register](../risks/RISK_REGISTER.md)
