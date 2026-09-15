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

**`CDS-WP-020A` and CDS-WP-023 through CDS-WP-053 are `Planned`, `Not active`, and
`Not authorized for execution`. Work on them has not started.** Each becomes
executable only on an explicit Nova prompt **and** Human-Maintainer authorization,
one work package at a time. Nothing in this document activates the next one
automatically. **`CDS-WP-021` and `CDS-WP-022` are the exceptions** — each authorized
by a separate, explicit Human-Maintainer act, **not** by this document.
**CDS-WP-021 is `Completed` / `Closed`**, closure effective at the Human-Maintainer
integration commit `01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`; **CDS-WP-022 — Theme
and Environmental Presentation Model is `AUTHORIZED` / `ACTIVE FOR EXECUTION`**.
**Closing one authorizes no other** — **`CLOSED ≠ SUCCESSOR AUTHORIZED`** — and the
CDS-WP-022 authorization is a Human-Maintainer decision that this document records
rather than makes.

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

**Work-package rows updated again by CDS-WP-021 (2026-09-06).** The maturity,
evidence, claim, conformance, and publication rows above remain **unchanged** —
Candidate families **1**, Stable **No**, claims **None**, conformance **None**,
AE-2/AE-3/AE-4 **None**, **visual value None**, component **None**, pilot
**Inactive**, publication **`Private Development`**, releases **None**, tags **0**.
Only the work-package rows have advanced: **CDS-WP-021 — Adaptive Layout and
Responsive Foundation was authorized separately and explicitly by the Human
Maintainer and is `AUTHORIZED / ACTIVE FOR EXECUTION`** — **executed with result
`COMPLETE WITH NOTES`, integrated at `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`, not
closed** — and
**`CDS-WP-020A` and CDS-WP-022 … CDS-WP-053** remain **`Planned` · not active · not
authorized**. **The Nova-recommended Step-10 candidate was CDS-WP-022; the Human
Maintainer authorized CDS-WP-021 instead**, which is their prerogative and which
activated no other work package — **a recommendation is not an authorization.**
CDS-WP-021 delivered a **contract**, not values: it created **no** visual value,
identifier, responsive-range name, range count or threshold, VF-4 technical root,
source set, token source, schema, or validator rule, registered **no** risk, and
advanced **no** maturity. **The effective registers are now 138 decisions and
7 ADRs** — `DEC-S-137`, `DEC-S-138` and `ADR-0007` having become effective at
`23914ecc…` — **and the risk register stays at 98.** It first returned `DECISION_REQUIRED`;
the
Human Maintainer then **approved `WP021-D1`** — the **Container-Relative
Named-Range Foundation**, recorded as **`DEC-S-136`** with **`ADR-0006`**, both
**effective at that integration commit** — and **deferred
`WP021-D2`**, leaving the **VF-4 technical root and Source Set identity OPEN** with
**no Decision and no ADR**.

**Superseded in part by the CDS-WP-021 Step-18 closure.** The CDS-WP-021
lifecycle/current-authority state recorded above remains the **2026-09-06** state.
The reviewed Step-18 closure object records **CDS-WP-021** as **`Completed` /
`Closed`**; closure becomes effective only at the Human-Maintainer exact-object
integration commit of that closure object, after the required Fresh Independent
Review and Nova final adjudication. **Until that commit CDS-WP-021 remains not
closed; from that commit no work package is authorized.** **No successor is
activated**: **`CDS-WP-020A` and CDS-WP-022 … CDS-WP-053 remain `Planned`, not
active, and not authorized** unless separately authorized. The maturity, evidence,
claim, conformance, publication and value-state statements above remain
**unchanged**.

**Work-package rows updated again by CDS-WP-022 (2026-09-12).** The maturity,
evidence, claim, conformance, publication and value-state rows above remain
**unchanged** — Candidate families **1**, Stable **No**, claims **None**, conformance
**None**, AE-2/AE-3/AE-4 **None**, channel and consumer evidence **None**, **visual
value None**, component **None**, pilot **Inactive**, publication **`Private
Development`**, releases **None**, tags **0**, **visual source sets 0**. Only the
work-package rows have advanced. **The CDS-WP-021 closure condition stated above has
been met**: the closure object was integrated by the Human-Maintainer commit
`01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`, so **CDS-WP-021 is `Completed` /
`Closed`, closure effective at that commit**, with the execution result unchanged at
**`COMPLETE WITH NOTES`**. The Human Maintainer has since **separately and explicitly
authorized CDS-WP-022 — Theme and Environmental Presentation Model**, which is
**`AUTHORIZED` / `ACTIVE FOR EXECUTION`**, and **`CDS-WP-020A` and
CDS-WP-023 … CDS-WP-053** remain **`Planned` · not active · not authorized**. **This
was the Nova-recommended and `DEC-S-135`-sequenced Step-10 candidate — and the
authorization is still an independent Human-Maintainer act**: **`SEQUENCED NEXT ≠
AUTHORIZED`**, **`CLOSED ≠ SUCCESSOR AUTHORIZED`** and **`DEPENDENCY SATISFIED ≠
AUTHORITY GRANTED`** all continue to hold. **CDS-WP-022 executed with
`DECISION_REQUIRED`**: it derived the context contract that effective authority
uniquely determines — context admission, context identity, selection and resolution
entry, environmental-input boundaries, fail-closed conditions, and the composition
boundaries against channel, Spatial Context, Product Profile, role identity, status,
Source Set and token-flow layer — and **escalated five normative choices** to the
Human Maintainer as the execution-local report keys **`WP022-D1` … `WP022-D5`**: the
theme mechanism, the initial supported context set, the forced-colours disposition,
context selection and environmental precedence, and default / fallback semantics. It
created **no** theme, context, context identifier, default alias, visual value,
identifier, role, source set, token source, schema, validator rule, test, or fixture;
registered **no** risk; advanced **no** maturity; admitted **no** evidence; made
**no** claim; and activated **no** work package.

**The Human Maintainer then decided all five (2026-09-12), and a bounded rework
applied them.** **CDS-WP-022's execution result is `COMPLETE WITH NOTES`**; the
initial **`DECISION_REQUIRED`** is **execution history and is not rewritten**, and the
**lifecycle status and the execution result remain separate axes**. The decisions are
recorded as two Decisions and one ADR, all effective: **`DEC-S-137` — Theme
Resolution and Context-Evidence Architecture** (the **Resolver-Modifier Context** over
the existing Source-Set graph, with **no per-context Source Set**, **no context or
theme segment in any identifier**, the **Source Set remaining the sole independently
evaluable maturity unit**, and context-specific evidence staying bound to
(`sourceSetId`, `sourceRevision`) while recording the **Resolver / Composition
revision** and the **Theme Resolution Context** as exact evidence inputs), with
**`ADR-0007`** covering **`DEC-S-137` only**; and **`DEC-S-138` — Core Theme Context,
Environmental Selection and Fail-Closed Policy** (**`Light` and `Dark`** as equal
peers with **no default**; **forced colours as an environmental accessibility
condition and not a Core context**; **explicit viewer choice over inferred environment
preference**, with mandatory platform accessibility conditions **outside** Theme
precedence and always binding; and **no default or fallback Theme, failing closed** on
missing, unsupported and unresolved-conflict resolution, with **`Not Applicable`**
where Theme resolution genuinely does not apply).

**All three are `Accepted` and effective at the Human-Maintainer exact-object
integration commit `23914ecc48c1fb3cba5e3dab97a505589e821b6b`** of the reviewed
CDS-WP-022 object — which followed a Fresh Independent Review returning `REWORK
REQUIRED` with **0 blocking** findings, a bounded corrective rework, a confirmatory
independent review, and Nova final integration adjudication.
**`APPROVED PROPOSITION ≠ EFFECTIVE REPOSITORY DECISION`** held until that commit;
**a review PASS is not a commit**, and **a Nova recommendation is not an approval**.
**The effective registers
held 136 decisions and 6 ADRs until it and hold 138 and 7 from it; the risk
register stays at 98 throughout** — **no `RISK-099`, no `DEC-S-139`, no `ADR-0008`**.
**Supported Core Theme Resolution Contexts: 0 until that commit, 2 — `Light` and
`Dark` — from it, with no
default.** The rework created **no** visual value, machine-readable context
identifier, role, source set, token source, schema, validator rule, test, or fixture;
admitted **no** evidence; advanced **no** maturity; made **no** claim; and activated
**no** work package. **`DEC-S-135` is untouched in byte and in substance** — from the
effectivity of the two new Decisions its theme-mechanism sequencing condition is
satisfied, and **`THEME GATE SATISFIED ≠ VALUE SELECTION AUTHORIZED`** and **`THEME
GATE SATISFIED ≠ CDS-WP-020A AUTHORIZED`**. **`DEC-S-131`, `DEC-S-132` and
`DEC-S-136` are untouched**, **`WP021-D2` stays deferred**, and **VP-3, VP-5, VP-6 and
VP-7 stay `UNSATISFIED`** with **VP-4 still `UNSATISFIED` for VF-4**. **CDS-WP-022 is
not closed**, **no successor is authorized**, **M2 — Visual Foundation Ready is not
reached**, and **`MILESTONE REACHED ≠ MATURITY AWARDED`** regardless.

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
| CDS-WP-021 | Adaptive Layout and Responsive Foundation | 3 | **Completed / Closed** — executed with `COMPLETE WITH NOTES`; **closure effective at the Human-Maintainer integration commit `01145b8a…`** |
| CDS-WP-022 | Theme and Environmental Presentation Model | 3 | **`AUTHORIZED` / `ACTIVE FOR EXECUTION`** — authorized separately and explicitly by the Human Maintainer; **executed with `COMPLETE WITH NOTES`** after first returning `DECISION_REQUIRED`; **`WP022-D1` … `WP022-D5` decided**, recorded as **`DEC-S-137`**, **`DEC-S-138`** and **`ADR-0007`**, all **`Accepted` and effective at `23914ecc48c1fb3cba5e3dab97a505589e821b6b`**; **integrated, not closed**; **no closure, no successor, no value** |

**`CDS-WP-020A` is an inserted identifier, not a renumbering.** It follows the
existing **`CDS-WP-001A`** insert precedent already carried in
[Work Packages](../../project-system/WORK_PACKAGES.md): a suffixed identifier placed
between two numbered work packages, occupying no number. **No work package was
renumbered**, and the numeric range CDS-WP-017 … CDS-WP-053 is unchanged.

**Its table position is registration, not sequencing.** Listing CDS-WP-020A before
CDS-WP-021 and CDS-WP-022 does **not** decide that it runs before them. **OD-7 is
answered by the effective `DEC-S-135`** — CDS-WP-022 precedes context-sensitive value
selection, and no semantic role carries a default alias before it decides the theme
mechanism — so **CDS-WP-022 is the recommended and sequenced Step-10 candidate.**
**SEQUENCED NEXT ≠ AUTHORIZED.** Execution order remains a Human-Maintainer
decision, and **CDS-WP-020A is `Planned`, not active, and not authorized.**

**And that is exactly how it played out (2026-09-06).** The Human Maintainer
authorized **CDS-WP-021** — **not** the recommended CDS-WP-022 and **not**
CDS-WP-020A — by a separate, explicit act. **The recommendation stands unchanged and
unfulfilled**: `DEC-S-135` still sequences CDS-WP-022 before context-sensitive value
selection, **CDS-WP-022 remains not authorized**, and **CDS-WP-020A remains
`Planned`, not active, and not authorized**. **CDS-WP-021 selects no value**, so it
does not reach the gate `DEC-S-135` guards. **Execution order is a Human-Maintainer
decision, and this document records it rather than making it.**

**And then it was authorized (2026-09-12).** After closing CDS-WP-021, the Human
Maintainer **separately and explicitly authorized CDS-WP-022**, which is now
**`AUTHORIZED` / `ACTIVE FOR EXECUTION`**. **The recommendation and the
authorization remain two different things**: this was an independent
Human-Maintainer act, **not** a consequence of `DEC-S-135`, of the closure, or of
this roadmap — **`SEQUENCED NEXT ≠ AUTHORIZED`** and **`CLOSED ≠ SUCCESSOR
AUTHORIZED`**. **`CDS-WP-020A` remains `Planned`, not active, and not authorized**,
and **authorizing CDS-WP-022 satisfies none of its prerequisites.**

**The milestone mapping is not re-derived here.** **M2 — Visual Foundation Ready**
still reads *"reached after CDS-WP-022"*, unchanged. Whether CDS-WP-020A belongs
before or inside that milestone depends on **OD-4 … OD-7**; deciding it here would
be a sequencing decision this pass holds no authority to make. **The Step-9
decisions do not re-derive it either** — `DEC-S-135` sequences CDS-WP-022 before
context-sensitive value selection and says nothing about M2's composition. See
**`F-020C-02`**, which remains **deferred**.

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
**38** identifiers now recorded, **32** — CDS-WP-020A and CDS-WP-023 … CDS-WP-053 —
are `Planned · not active · not authorized`; **five** — CDS-WP-017, CDS-WP-018,
CDS-WP-019, CDS-WP-020, and CDS-WP-021 — are closed, **CDS-WP-021 upon the
Human-Maintainer exact-object integration commit
`01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`**; and **one — CDS-WP-022 — is
`AUTHORIZED` / `ACTIVE FOR EXECUTION`** by a separate, explicit Human-Maintainer
act. **No other identifier in this range is currently authorized**, and **being
recorded here authorizes nothing.** The **CDS Phase Transition
Governance Package** occupies **no** identifier in this range.

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

**Status after CDS-WP-021 (2026-09-06).** The CDS-WP-019 findings table above is
that work package's record and is **still not rewritten**. One further finding has
been dispositioned:

| ID | Status |
| --- | --- |
| **`F-019-03`** — CR-004 Layer-5 mapping versus CDS-WP-021 at Layer 3 | **ANSWERED BY CDS-WP-021 — PREPARED, NOT EFFECTIVE** until the Human-Maintainer exact integration commit of the CDS-WP-021 object. CDS-WP-021 **confirmed the split** it was required to confirm — **Layer 3 owns the spatial vocabulary and the structural context model · Layer 5 owns the response · Layer 6 owns channel-imposed geometry** (LO-1 … LO-8) — and did so **from authority already in force**: DEC-S-021, the allowed-dependency table, and prohibited dependencies 2 and 3. **`CR-004` remains registered at Layer 5, its row is not edited, and no count changes.** The finding described a **category confusion, not a contradiction**: CDS-WP-021 owns the VF-4 **vocabulary** while CR-004 asks for a **strategy**, and both mappings are correct at once. An **additive clarifying note** was added below the traceability matrix, permitted precisely for this purpose and re-owning nothing. **The confirmation moves no requirement.** |

`F-019-01`, `F-019-02`, `F-019-04` … `F-019-07` and `F-019-09` are **unchanged** by
CDS-WP-021 and keep their recorded dispositions. **CDS-WP-021 is an architecture
work package, not a hygiene pass**, and **routing is not repair**.

### Findings observed by CDS-WP-020

Recorded while defining the reference and semantic visual token contract. Each is
**recorded and not repaired** — CDS-WP-020 is a contract work package, not a hygiene
pass, and **routing is not repair**. None of them blocked CDS-WP-020.

| ID | Observation | Disposition |
| --- | --- | --- |
| **F-020-01** | The **value half** of CDS-WP-020 is gated on **seven** normative choices that no committed CDS source has made. The five earlier work packages that made comparable first-of-their-kind normative choices — **CDS-WP-011 … CDS-WP-015** — each registered a Decision block, and three of them an ADR; CDS-WP-020 holds no authority to register either. | **`DECISION_REQUIRED`.** Recorded as **OD-1 … OD-7** in the **non-normative** [Visual Token Foundation Open Decisions](VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md) register. **Partially answered on 2026-08-27** by the Human-Maintainer-authorized **CDS-WP-020 Decision Integration Pass**: **DEC-S-128, DEC-S-129, DEC-S-130, DEC-S-131** and **ADR-0004** were **prepared and authorized for integration, and at that date NOT YET EFFECTIVE**. They answer **OD-1, OD-2 and OD-3** and add the contrast evaluation authority. **OD-4 … OD-7 stay open, the value half stays gated, and CDS-WP-020 stays `DECISION_REQUIRED` and not closed.** *(Stated as at 2026-08-27, before integration.)* **Superseded in part:** the CDS-WP-020 object was integrated by the Human-Maintainer commit `42a568d823de3388e45af62967546f13ad67eff6` — at which **DEC-S-128 … DEC-S-131 and ADR-0004 became effective** — and CDS-WP-020 is now **`Closed`**, closure effective at the Human-Maintainer commit `3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`. **The `DECISION_REQUIRED` result stands as the executed result of the work package**; **OD-4 … OD-7 have since been answered by the CDS Step-9 Decision Integration Pass — OD-4 and OD-7 answered, OD-5 partially answered, OD-6A policy-answered, OD-6B answered by existing authority, effective at the Human-Maintainer commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`, with the concrete role vocabulary, the per-family topology parameters and VF-1 tonal topology still open**; and the value half stays gated; the value and machine-readable work is routed to **`CDS-WP-020A`** (`FR-N-03`), which is **`Planned`, not active, and not authorized**. |
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

### Findings observed by CDS-WP-021

Recorded while defining the adaptive-layout and responsive foundation. Each is
**recorded and not repaired** — CDS-WP-021 is an architecture work package, not a
hygiene pass, and **routing is not repair**. None of them blocked CDS-WP-021.

| ID | Observation | Disposition |
| --- | --- | --- |
| **F-021-01** | **`OD-7` staleness in a controlled carrier.** The *"How to read this table"* section of [Work Packages](../../project-system/WORK_PACKAGES.md) still states that **"OD-7 — whether CDS-WP-022 should be considered before any value-selection work package — stays open"**. **OD-7 is answered** by the effective **`DEC-S-135`** (integration commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`). The statement was true when written and is stale only as **live** current state. It is adjacent to text CDS-WP-021 did edit, and was **left unrepaired deliberately**. | Deferred → a **bounded, separately authorized current-state reconciliation**. **Not repaired by CDS-WP-021**, which holds no authority to repair `OD-7` drift and made no silent repair. The normative carrier for OD-7 remains the [Decision Index](../decisions/DECISION_INDEX.md) and the **non-normative** [Open Decisions](VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md) register, both of which record it as **answered**. |
| **F-021-02** | **VF-4 has no consumer demand evidence for a grid, container, or content-width model, and CDS-WP-021 did not acquire any.** `F-019-06` recorded that **VF-3, VF-5, VF-6 and VF-7** carry none; **VF-4's only registered anchor is CR-004, and CR-004 sits at Layer 5**, which CDS-WP-021 has now confirmed. The Layer-3 half of VF-4 therefore rests on **CR-023** (variable text length) and the accessibility baseline, **not** on a consumer asking for a grid. | **Recorded as honesty, not as a defect**, in the same treatment CDS-WP-005 gave CR-030 and CDS-WP-019 gave `F-019-06`. Mapped to **RISK-003**, **RISK-017** and **RISK-026**; **no new risk is registered**, and the register stays at **98**. |
| **F-021-03** | **A spatial context may be structurally indistinguishable from a theme.** If **`WP021-D1`** makes spatial contexts participate in token resolution, the Theme Architecture rule *"a context that varies within a channel is a theme"* would classify a responsive range as a theme — and a resolver would then compose **more than one context dimension**. **CDS-WP-021 recorded the coupling and decided nothing** (CX-9, theme boundary statement 6). | **Routed → `WP021-D1` and CDS-WP-022.** It is an **input to** CDS-WP-022's mechanism decision and **never a decision for it**. **T-1 … T-10, TC-1 … TC-7 and TS-1 … TS-6 are unchanged**, and **DEC-S-135 is untouched.** |
| **F-021-04** | **The most-evidenced consumer need is still the least-solved problem.** The **density, reflow and target-size** interaction is not structurally checkable and cannot be resolved without **rendering evidence**, which does not exist. CDS-WP-021 fixed the composition rule — **obligations do not weaken under composition** (DA-2, DA-4, DA-5) — and **solved nothing**. | **Routed → CDS-WP-031** (rendering matrix and visual regression evidence), and to the per-channel accessibility profiles for non-web channels. **Recording a constraint is not solving a problem**, and **an automated check is never sufficient** (DEC-S-053). |
| **F-021-05** | **`No work package is currently authorized` survives in two carriers outside the CDS-WP-021 file scope.** The **VP-7** row of the normative [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md) supports its verdict with that clause, and the **non-normative** [Open Decisions](VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md) register repeats it in a dated 2026-09-05 blockquote. Both were true when written. **The VP-7 verdict itself is unaffected and remains correct: VP-7 is UNSATISFIED**, because it requires authorization **of the work package that makes the value selection**, and **CDS-WP-021 selects no value and is not a value-selection work package.** Only the supporting clause is stale. | Deferred → the same **bounded, separately authorized current-state reconciliation** as `F-021-01`. **Not repaired by CDS-WP-021**: neither file is in its scope, **no VP verdict changes**, and **VP-1 … VP-7 are untouched**. **VP-3, VP-5, VP-6 and VP-7 remain unsatisfied for every visual family**, and **no visual value may be selected.** |
| **F-021-06** | **Point-in-time statements inside decision and ADR records name CDS-WP-021 as `Planned` / not authorized.** They appear in the **DEC-S-132 … DEC-S-135** entries and clause texts of the [Decision Index](../decisions/DECISION_INDEX.md), in the boundary sections of **ADR-0004** and **ADR-0005**, and in **TS-6** of the [Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md). Each is a true statement about **what that decision did** — none of them authorized any work package — and each was accurate at its own date. | **NOT A DEFECT and NOT REPAIRED, by the repository's own explicit rule:** the Decision Index states that *"a statement inside an individual decision entry is point-in-time and is not edited when a later event occurs"*, and names its own current-state section as the maintained carrier. **Editing DEC-S-135's text is additionally a stop condition for CDS-WP-021**, which changes it in no way. **`DEC-S-135` is unchanged, CDS-WP-022 remains the recommended and sequenced Step-10 candidate, and it remains not authorized.** |

**Disposition after the bounded decision rework (2026-09-06).** Two of the findings
above have been addressed; the rest are **unchanged**:

| ID | Status |
| --- | --- |
| **`F-021-01`** | **RESOLVED IN BOUNDED REWORK**, for the live stale assertion only. The *"How to read this table"* section of [Work Packages](../../project-system/WORK_PACKAGES.md) now records **`OD-7` as ANSWERED by the effective `DEC-S-135`** — CDS-WP-022 precedes context-sensitive value selection and is the recommended and sequenced Step-10 candidate, and **`CDS-WP-022` remains NOT AUTHORIZED**. **Historical statements that truthfully described OD-7 as open at an earlier date were not rewritten**, and **no unrelated OD state was altered.** |
| **`F-021-05`** | **SPLIT TRUTHFULLY.** The **live VP-7 justification is RESOLVED IN BOUNDED REWORK**: the [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md) carry an **additive current-state note** stating that **CDS-WP-021 is authorized but is not authorized to select visual values**, so **no work package currently authorized to select visual values exists**. **The VP-7 verdict is unchanged — `UNSATISFIED` — and the normative VP-7 prerequisite itself is untouched**, as are the dated 2026-08-27 and 2026-09-05 prerequisite tables. The **dated, non-normative 2026-09-05 occurrence** in the [Open Decisions](VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md) register is **PRESERVED / NO ACTION** — it truthfully recorded the state at that date. **Historical truth is not live current-state drift.** |

**`F-021-02`, `F-021-03`, `F-021-04` and `F-021-06` are unchanged** and keep their
recorded dispositions. **`F-021-03` remains routed to CDS-WP-022** as a composition
concern — and **`DEC-S-136` now states explicitly that `SPATIAL CONTEXT ≠ THEME
RESOLUTION CONTEXT`**, so the coupling is a **declared boundary** rather than an
open ambiguity, while **whether and how the two compose stays CDS-WP-022's**. **No
new finding and no new risk was created.**

### Findings observed by CDS-WP-022

Recorded while deriving the Theme and Environmental Presentation contract. Each is
**recorded and not repaired** — CDS-WP-022 is an architecture and governance work
package, not a hygiene pass, not a schema pass, and not a validation pass, and
**routing is not repair**. **None of them blocked CDS-WP-022**, and **no new risk was
registered: the register stays at 98, with no `RISK-099`.**

| ID | Observation | Disposition |
| --- | --- | --- |
| **F-022-01** | **The committed resolver schema cannot express a context condition.** `schemas/cds-resolver-document.schema.json` admits an optional `modifiers` array whose items carry `order`, `name`, `$ref` and `pointer` only, under `additionalProperties: false` — **there is no condition slot, and none can be added as an extension field**. The offline validator correspondingly records **resolver modifier semantics as *"not validated and not represented as passed"*** — the bounded **DEC-S-098** V2 coverage boundary. | **Recorded, routed → `CDS-WP-020A` and CDS-WP-024**, both **`Planned`, not active, and not authorized**. It is a **declared coverage boundary, not a class-1 / class-2 conflict**: **no resolver instance with modifiers exists**, so there is no affected artifact state and **DEC-S-034 is not triggered**; the resolution model's own *"where applicable"* already anticipates it. **CDS-WP-022 changed no schema, validator, rule, test, or fixture**, and reading the boundary as a profile admission is what **RISK-074** exists to prevent. |
| **F-022-02** | **The evidence-bearing unit and the context-binding carrier may not be the same artifact.** **DEC-S-131 clause 1** attaches evaluation, evidence, maturity and approval to a **Source Set** and *"nowhere else"*, while **clause 5** admits **one** source set per Family × Token-Flow-Layer unit and **DEC-S-132 clauses 10 and 12** close the ten identities and introduce **no `context` or `theme` namespace segment**. A context-conditional binding held only in a Resolver / Composition document therefore sits **outside** the unit evidence attaches to. | **Routed → `WP022-D1`.** It is the **substance** of the open mechanism question, not a defect: **CDS-WP-022 recorded it and decided nothing**, because every remaining alternative changes the evaluable unit, the source-set topology, the namespace, or the representation of a binding — each a normative choice reserved to the Human Maintainer. **DEC-S-131 and DEC-S-132 are untouched.** |
| **F-022-03** | **`F-021-03` consumed as an input, as routed.** CDS-WP-021 routed the spatial-context / theme indistinguishability concern to CDS-WP-022 as *"an input to CDS-WP-022's mechanism decision and never a decision for it"*. | **CONSUMED AS INPUT, NOT DECIDED.** **CB-2** of the [Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md) records that **CDS Core declares no composition** of a Spatial Context with a Theme Resolution Context and that **no spatial context is a resolution input to theme resolution** — the conservative reading CDS-WP-021 preserved, which **forecloses nothing**. Any composition is carried inside **`WP022-D1`**. **`DEC-S-136`, CX-9, AC-1 … AC-6 and RR-1 … RR-6 are unchanged**, and **no range name, count, or threshold was created.** |
| **F-022-04** | **No consumer requirement exists for a high-contrast context or a document context, and CR-025 is `Could`.** The candidate table records **no consumer requirement** for high contrast (it derives only from baseline **3.5**, *Implementation-dependent*) and **none at all** for neutral / document; **CR-025 is `Could`**, a *documented planned capability*, *deferred to foundations work*, status **Open**. So the one candidate pair with consumer evidence has the **weakest** priority class in the model. | **Recorded as honesty, not as a defect**, in the same treatment CDS-WP-005 gave CR-030 and CDS-WP-019 gave `F-019-06`. Mapped to **RISK-003**, **RISK-017** and **RISK-026**; **no new risk is registered.** It is a direct input to **`WP022-D2`** and **`WP022-D3`**, and **`COULD` ≠ `MUST`**. |
| **F-022-05** | **Point-in-time statements naming CDS-WP-022 as `Planned` / not authorized survive in decision and ADR records.** They appear in the **DEC-S-132 … DEC-S-135** entries of the [Decision Index](../decisions/DECISION_INDEX.md), in the boundary sections of **ADR-0004**, **ADR-0005** and **ADR-0006**, in **TS-6** of the [Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md), in the DEC-S-135 application text of the [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md), in the theme-boundary statement of the [Adaptive Layout and Responsive Foundation](../architecture/ADAPTIVE_LAYOUT_AND_RESPONSIVE_FOUNDATION.md), and in the dated CDS-WP-020 and CDS-WP-021 sections of the current-state carriers. **Five of those carriers lie outside the CDS-WP-022 allow-list**, and none was touched. Each is a true statement about **what that decision or work package did** — none of them authorized any work package — and each was accurate at its own date. | **NOT A DEFECT and NOT REPAIRED, by the repository's own explicit rule**, exactly as **`F-021-06`** was treated: the Decision Index states that *"a statement inside an individual decision entry is point-in-time and is not edited when a later event occurs"* and names its own *Register scope* section as the maintained carrier — which **CDS-WP-022 updated additively**. **Editing DEC-S-135 is a stop condition**, and **CDS-WP-022 changed it in no way.** |
| **F-022-06** | **`F-020C-02` was not opportunistically closed.** **M2 — Visual Foundation Ready** still reads *"reached after CDS-WP-022"*, and whether **CDS-WP-020A** belongs before or inside that milestone remains unstated. | **UNCHANGED — still deferred.** **M2 is not reached**: CDS-WP-022 is **not closed**, so the milestone's own precondition is unmet, and re-deriving M2's composition would be a **sequencing decision** CDS-WP-022 holds no authority to make. **`MILESTONE REACHED ≠ MATURITY AWARDED`** regardless, and M2 **grants nothing**. |
| **F-022-07** | **Residual CDS-WP-021 closure-effectivity phrasings.** Statements written **before** the closure commit still describe that closure as *"becoming effective only at the Human-Maintainer exact-object integration commit of this independently reviewed closure object"*. That commit has occurred — `01145b8a0ad2a68c4c2743205f96ec34f3c2ed15` — so those formulations were truthful **before** it and are stale only as **live** current state. **CDS-WP-022 reconciled them only where the live current-authority statement it had to touch would otherwise have been internally incoherent.** | **Deferred → a bounded, separately authorized post-closure current-state reconciliation**, on the **`F-020C-04`** precedent, where exactly this drift was its own authorized pass. **Not repaired wholesale by CDS-WP-022**: the volume is a material scope expansion beyond a theme architecture work package, and **CDS-WP-021's closure and execution result are unaffected** — **`Completed` / `Closed`**, result **`COMPLETE WITH NOTES`**. **Point-in-time and dated records were preserved, not rewritten.** |

| **F-022-08** | **The *next free identifier* idiom goes stale when the number is allocated.** Statements written before the CDS-WP-022 decision package assert that **`WP021-D2`** has *"no Decision and no ADR"* by naming **`no DEC-S-137, no ADR-0007`** — the then-next free identifiers. Those identifiers are now **allocated to `WP022-D1`**, so the literal claim is stale as live state while its **intent** — that `WP021-D2` has no governance record — stays **true**. Carriers include the normative [Adaptive Layout and Responsive Foundation](../architecture/ADAPTIVE_LAYOUT_AND_RESPONSIVE_FOUNDATION.md) (three occurrences) and the dated CDS-WP-021 changelog entry. | **Split.** **Repaired inside the CDS-WP-022 allow-list**, where the same sentence had to remain coherent beside the new records: the substance is kept and the identifier claim is replaced by *"the prepared `DEC-S-137` and `ADR-0007` record `WP022-D1`, not `WP021-D2`, and are unrelated to it"*. **Deferred → a bounded, separately authorized current-state reconciliation** for the carriers **outside** that allow-list, on the **`F-020C-04`** precedent. **Dated changelog occurrences are HISTORICAL and preserved.** **`WP021-D2` remains DEFERRED** with **no Decision, no ADR, no VF-4 technical root and no VF-4 Source Set identity**, and **no new risk is created.** |

**Disposition after the bounded decision rework (2026-09-12).** The Human Maintainer
decided **`WP022-D1` … `WP022-D5`**, and a bounded rework applied them. Each finding
above is dispositioned; **none is deleted, and no new risk is created — the register
stays at 98, with no `RISK-099`.**

| ID | Status |
| --- | --- |
| **`F-022-01`** | **REMAINS OPEN / ROUTED — unchanged.** **`DEC-S-137` clause 15 keeps it routed and changes no schema.** The committed resolver-document schema still cannot express a context condition, and the validator still records **resolver modifier semantics as not validated and not represented as passed** (DEC-S-098). **`MECHANISM DECIDED ≠ REPRESENTATION AVAILABLE`**: deciding the mechanism does not close the representation gap, and **no context-conditional resolver instance may be authored until it is closed under its own authorization**. Route unchanged → **`CDS-WP-020A`** and **CDS-WP-024**, both `Planned`, not active, not authorized. **Not opportunistically fixed.** |
| **`F-022-02`** | **RESOLVED BY HUMAN-MAINTAINER DECISION.** **`DEC-S-137`** answers the question it stated — *where does a context-conditional binding live, and which unit carries its evidence?* — by choosing the **Resolver-Modifier Context over the existing Source-Set graph** with the context and the Resolver / Composition revision recorded as **exact evidence inputs**, so **evidence stays bound to (`sourceSetId`, `sourceRevision`)** and **the Resolver never becomes a maturity carrier** (clauses 6 to 10; **TM-6 … TM-10**). **`EVIDENCE INPUT ≠ MATURITY CARRIER`.** **DEC-S-131 and DEC-S-132 are unchanged**, and the resolution is **effective only from the integration commit of `DEC-S-137`.** |
| **`F-022-03`** | **HISTORICAL / INPUT CONSUMED — and now closed as to representation.** `F-021-03` was routed to CDS-WP-022 as an input; **`DEC-S-137` clauses 11 and 12** make **Theme Resolution Context and Spatial Context orthogonal**, with **no spatial context a Theme modifier, Theme selector, or Theme-resolution input** and **no Theme classifying spatial geometry** (**TM-11**, **CB-2**). **Joint Theme × Spatial rendering and evidence evaluation remains DEFERRED** to separately authorized scope (**TM-12**) — an evidence-design question, routed alongside **CDS-WP-031**. **DEC-S-136, CX-9, AC-1 … AC-6 and RR-1 … RR-6 unchanged**; **`WP021-D2` unchanged**; **no range name, count, or threshold created.** |
| **`F-022-04`** | **REMAINS OPEN / ROUTED as an evidence-honesty finding — and it was an input to two decisions.** The Human Maintainer admitted **`Light` and `Dark`** (`DEC-S-138` part A) on **`Could`**-priority CR-025 and dispositioned **forced colours as a platform condition** (part B) with **no consumer requirement** behind it. **That is a priority decision, not new evidence:** the consumer-evidence weakness the finding records is **unchanged**, **`COULD` ≠ `MUST`** still holds as a general rule, and **admitting a context creates an evidence obligation, not evidence.** Mapped to **RISK-003**, **RISK-017** and **RISK-026**; **no new risk registered.** |
| **`F-022-05`** | **REMAINS OPEN / ROUTED — NOT A DEFECT and NOT REPAIRED, unchanged.** The point-in-time statements naming CDS-WP-022 as `Planned` / not authorized stay as written, by the repository's own rule. **The bounded rework edited no Decision entry, proposition, status, or effectivity commit**, and **`DEC-S-135` is unchanged in byte and in substance** — editing it is a stop condition. Only the Decision Index's **maintained current carrier** advanced, additively, to record the prepared `DEC-S-137`, `DEC-S-138` and `ADR-0007`. |
| **`F-022-06`** | **REMAINS OPEN / ROUTED — `F-020C-02` still deferred, and deliberately not closed.** **M2 — Visual Foundation Ready** still reads *"reached after CDS-WP-022"*, and **M2 is not reached**: CDS-WP-022 is **not closed**, and re-deriving M2's composition would be a **sequencing decision** this rework holds no authority to make. **`MILESTONE REACHED ≠ MATURITY AWARDED`** regardless, and M2 **grants nothing**. |
| **`F-022-07`** | **REMAINS OPEN / ROUTED — unchanged.** The residual CDS-WP-021 closure-effectivity phrasings written before commit `01145b8a0ad2a68c4c2743205f96ec34f3c2ed15` stay deferred to a **bounded, separately authorized post-closure current-state reconciliation**, on the **`F-020C-04`** precedent. **The bounded decision rework widened nothing here**, and **CDS-WP-021 remains `Completed` / `Closed` with result `COMPLETE WITH NOTES`.** |

**No new finding was created by the bounded decision rework**, and **no F-022 finding
was deleted.** **`F-022-02` is the only one the decisions resolve**; **`F-022-03` is
resolved as to representation with its evaluation half deferred**; **`F-022-08` is
repaired inside the allow-list and deferred outside it**; and the rest are
**unchanged**.

**Disposition after the final pre-closure current-state reconciliation
(2026-09-15).** The findings table and the 2026-09-12 disposition above are **not
rewritten**: each correctly records what was observed or dispositioned at its own
date. In the light of the separately authorized current-state reconciliations
integrated since `23914ecc48c1fb3cba5e3dab97a505589e821b6b` — at
`6f5408b1a6863e52560d8884fb9202f1cdfb85c9`,
`61ee2f3c67d5dd2da4443f782c56d770eaa80074` and
`4714f892a2780afd6425885ccc28a75533fca3df` — and of this final pre-closure
reconciliation, three dispositions advance **additively**:

| ID | Status |
| --- | --- |
| **`F-022-05`** | **NOT A DEFECT for its class — unchanged; ONE carrier reclassified and reconciled.** The 2026-09-12 treatment **remains valid** for individual Decision entries, ADR point-in-time boundaries, the dated `DEC-S-135` application text, and every other explicitly point-in-time carrier the repository's own rule covers. **One carrier was later independently reclassified:** the **unqualified theme-boundary statement** of the normative [Adaptive Layout and Responsive Foundation](../architecture/ADAPTIVE_LAYOUT_AND_RESPONSIVE_FOUNDATION.md), which stated without temporal qualification that CDS-WP-022 **is** `Planned`, not active, and not authorized. It functioned as an **undated maintained architecture boundary**, not as a point-in-time Decision record, and was therefore classified **`LIVE_STALE_PREEXISTING`** and **closure-blocking**. It was **reconciled** by the later residual current-state sequence, **culminating in `4714f892a2780afd6425885ccc28a75533fca3df`**, which dates the state at the CDS-WP-021 milestones and records CDS-WP-022's later authorization as a **lifecycle update, not an architecture change**. **This does not reopen `F-022-05` globally** — **`CARRIER-SPECIFIC RECLASSIFICATION ≠ GLOBAL FINDING REVERSAL`**. Neither that reconciliation nor this disposition edited any Decision entry, proposition, status or effectivity commit, and **`DEC-S-135` is unchanged in byte and in substance.** |
| **`F-022-07`** | **RESOLVED AS LIVE CURRENT-STATE DRIFT.** The remaining live CDS-WP-021 closure-effectivity carriers — in [Work Packages](../../project-system/WORK_PACKAGES.md), `CLAUDE.md` and the [Foundation Context Pack](../../project-system/CONTEXT_PACK_FOUNDATION.md) — still described that closure as becoming effective only at the integration commit of *"this independently reviewed closure object"*; each now records it as **separately authorized and effective at `01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`**. **Historical and dated pre-closure statements are preserved, not deleted** — including the event-time CDS-WP-021 Step-18 changelog entry and the Step-18 supersession note in the current-state section above, whose condition the later 2026-09-12 note already records as met. **CDS-WP-021 remains `Completed` / `Closed`, with result `COMPLETE WITH NOTES`.** |
| **`F-022-08`** | **RESOLVED FOR LIVE CURRENT-STATE CARRIERS.** The live identifier-idiom residuals are reconciled: **`WP021-D2` still has no Decision of its own, no ADR of its own, no VF-4 technical root and no VF-4 Source Set identity**, while **`DEC-S-137` and `ADR-0007` exist, belong to `WP022-D1`, not `WP021-D2`, and are unrelated to it**. **Occurrences that state what CDS-WP-021 itself created, and dated or point-in-time records, remain historical and act-scoped and are not defects** — **`ACT CREATED NOTHING ≠ IDENTIFIER DOES NOT EXIST TODAY`**. **Historical records are preserved.** |

**No new finding identifier was created, no F-022 finding was deleted, and no new
risk was created — the register stays at 98, with no `RISK-099`.** **None of this
closes CDS-WP-022**: it remains **`AUTHORIZED` / `ACTIVE FOR EXECUTION`, integrated,
and not closed**, **closure is a separate Human-Maintainer act that has not
occurred**, and **no successor is authorized**.

## Immediate next step

**Closure of CDS-WP-022 is the next governance requirement — and it is not
authorized.** **`CLOSURE REQUIRED NEXT ≠ CLOSURE AUTHORIZED`**: closure is a
**separate, explicit Human-Maintainer act**, not implied by the integration commit
(**`INTEGRATION ≠ CLOSURE`**), and it has **not** occurred. **CDS-WP-022 remains
`AUTHORIZED` / `ACTIVE FOR EXECUTION`, integrated, and not closed.** **No successor is
authorized**: **`CDS-WP-020A` and CDS-WP-023 … CDS-WP-053 remain `Planned`, not
active, and not authorized** — **`CLOSED ≠ SUCCESSOR AUTHORIZED`** and **`THEME GATE
SATISFIED ≠ CDS-WP-020A AUTHORIZED`**.

**The steps this section previously named have been completed:** the return to Nova
and the Human Maintainer with **`WP022-D1` … `WP022-D5`**, the Human-Maintainer
decision on all five (2026-09-12), the authorized bounded rework that applied them,
the **fresh independent review** (reviewer ≠ executor) returning **`REWORK REQUIRED`
with 0 blocking findings**, the **bounded corrective rework**, the **confirmatory
independent review**, **Nova final integration adjudication**, and the
**Human-Maintainer exact-object integration commit
`23914ecc48c1fb3cba5e3dab97a505589e821b6b`** — **at which `DEC-S-137`, `DEC-S-138` and
`ADR-0007` became effective**, moving the registers from **136/6** to **138/7** with
the risk register unchanged at **98**. **`DECISION_REQUIRED` was the correct first result, not a shortfall** —
a high-quality escalation is preferable to an invented architecture, and **`AUTHORIZED
WORK PACKAGE ≠ EXECUTOR AUTHORIZED TO INVENT NORMATIVE CHOICES`**. The execution
result is now **`COMPLETE WITH NOTES`**, and the initial `DECISION_REQUIRED` **stands
as execution history.**

**The step this section previously named has been completed:** the fresh independent
review of the CDS-WP-021 bounded closure object, Nova final adjudication, and the
Human-Maintainer exact-object integration commit
`01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`, **at which the closure of CDS-WP-021
became effective**. **The Human Maintainer then separately and explicitly authorized
CDS-WP-022** — a distinct act, not implied by that closure: **`CLOSED ≠ SUCCESSOR
AUTHORIZED`**.

**The step this section previously named has been completed:** the fresh independent
review of the reworked CDS-WP-021 working-tree object, Nova final adjudication, and
the Human-Maintainer exact-object integration commit
`a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`, which made the Adaptive Layout and
Responsive Foundation, **`DEC-S-136`** and **`ADR-0006`** effective. **The
Human Maintainer then separately authorized the closure of CDS-WP-021** — a distinct
act, not implied by that integration.

**`REVIEW PASS ≠ INTEGRATION`, and `INTEGRATION ≠ CLOSURE`.** CDS-WP-021 is
**executed with result `COMPLETE WITH NOTES`** — unchanged by closure, and not
rewritten to `COMPLETE` — **integrated**, and **`Completed` / `Closed`**, closure
effective at the Human-Maintainer commit
`01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`. **Neither its execution nor its closure
authorized a successor.** **CDS-WP-022 is authorized by a separate, explicit
Human-Maintainer act** and is **`AUTHORIZED` / `ACTIVE FOR EXECUTION`**;
**`CDS-WP-020A` and CDS-WP-023 … CDS-WP-053 remain `Planned`, not active, and not
authorized.**

**Both escalations have been answered by the Human Maintainer (2026-09-06).**
**`WP021-D1` is APPROVED** — the **Container-Relative Named-Range Foundation**,
which **RR-5** had assigned to CDS-WP-021 and which existing authority could not
settle — and is recorded as **`DEC-S-136`** with **`ADR-0006`**, both **effective at
the Human-Maintainer integration commit
`a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`**. **`WP021-D2` is
DEFERRED, not rejected**: whether **VF-4** acquires a technical root and source-set
identity stays **OPEN**, **DEC-S-132's root vocabulary stays closed at VF-1, VF-2,
VF-3, VF-5 and VF-6**, and **no Decision and no ADR was created for it** — **at that
deferral no `DEC-S-137` and no `ADR-0007` existed**; those identifiers were later
allocated to **`WP022-D1`** and are **unrelated to `WP021-D2`**, and **no `RISK-099`
and no new `OD` identifier exists.** **The
effective registers are now 138 decisions and 7 ADRs**, `DEC-S-137` and `DEC-S-138`
having become effective and `ADR-0007` `Accepted` and effective at
`23914ecc48c1fb3cba5e3dab97a505589e821b6b` —
**`APPROVED PROPOSITION ≠ EFFECTIVE REPOSITORY DECISION`** held until the
integration commit, and **`EFFECTIVE ≠ CLOSED`** holds: `DEC-S-136` and `ADR-0006`
became effective at `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9` before CDS-WP-021
was closed, and that effectivity did not itself close it. **CDS-WP-021 became
`Completed` / `Closed` only at the later Human-Maintainer exact-object integration
commit `01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`** — the CDS-WP-021 effectivity
commit is **not** the CDS-WP-021 closure commit.

**The step this section previously named — a fresh independent review of the CDS
Step-9 Decision Integration object, Nova adjudication, the Human-Maintainer exact
integration commit making `DEC-S-132 … DEC-S-135` and `ADR-0005` effective, and a
separate explicit authorization of a next work package — has been completed.** The
Step-9 object was integrated at `2cb244e889c1a6b5a278afb233995a0379b5d9ef`, and the
Human Maintainer then authorized **CDS-WP-021**.

**The Human-Maintainer decision on OD-4, OD-5, OD-6 and the OD-7 sequencing has been
taken** (2026-09-05): **OD-4 and OD-7 answered, OD-5 partially answered, OD-6A
policy-answered, OD-6B answered by existing normative authority.** The records are
**effective** at the Human-Maintainer exact integration commit
`2cb244e889c1a6b5a278afb233995a0379b5d9ef`. **The recommended Step-10 candidate is
`CDS-WP-022`**, which remains **`Planned`, not active, and not authorized** —
**SEQUENCED NEXT ≠ AUTHORIZED**. *(Point-in-time, 2026-09-05. **`CDS-WP-022` has
since been authorized** by a separate, explicit Human-Maintainer act of 2026-09-12
— **not** by this recommendation, which authorized nothing then and authorizes
nothing now.)*

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

### CDS Step-9 Decision Integration Pass — 2026-09-05

**Authorized separately by the Human Maintainer on 2026-09-05**, after Nova
adjudicated the CDS Step-9 R1/R2 decision package. It **prepared, and did not
commit**:

| Instrument | Records | Left open |
| --- | --- | --- |
| **`DEC-S-132`** (with **`ADR-0005`**) | **Family-rooted** token paths — `<family>.<primitive-group>.<step>[.<qualifier>]` and `<family>.<role>[.<qualifier>]`; the slot is **`qualifier`, not `modifier`**, and **no concrete qualifier is created**; **the token-flow layer is never a path segment**; **token-path identity and Source Set identity are two separate spaces** with `sourceSetId` **declared, never derived**; the flat **`<layer>/<family>`** form; the roots **`color`, `typography`, `space`, `shape`, `surface`** — **one per family**, so VF-3 and VF-6 take one each; and the ten identities `reference/color` … `semantic/surface` as **identifier authority only**. **OD-4 answered; the OD-3 concrete-root residual resolved.** | **Any migration or deprecation compatibility mechanism outside the normative Semantic alias graph** — a **new** residual. **AL-2 is unchanged.** |
| **`DEC-S-133`** | **No universal cross-family scale base** — ST-5 is per-scale. **Each ordered primitive set independently owns** its anchor declaration, ordering, progression-rule kind, step count, extension behaviour and exclusions, under the **unchanged** ST-1 … ST-7 contract. **`SCALE TOPOLOGY ≠ SCALE VALUES`**, and **VP-3's "base" is the anchor declaration, not a numeric magnitude**. Scope: VF-2, VF-3, VF-5, VF-6; **opacity stays an attribute** of VF-1 and VF-6. **OD-5 only PARTIALLY answered.** | **Per-family topology parameters** for every family in scope, and **VF-1 tonal topology**, split out as a distinct problem. **VP-3 stays UNSATISFIED for every family and fails closed.** |
| **`DEC-S-134`** | **Model B** — a **cross-consumer admission rule** only, inside the **closed** role classification, with SR-1 … SR-12 required from creation. **`CDS-WP-020A` may not invent, adopt, reserve, or recommend a Core role identifier.** **`selected`, `active` and `current` are not Core roles today** (answering **IS-5**) — **not a permanent prohibition**. **OD-6A POLICY ANSWERED.** | **The concrete role vocabulary.** **VP-6 stays UNSATISFIED** — a policy is not an authored role. |
| **`DEC-S-135`** | **No semantic visual role carries a default alias before CDS-WP-022 decides the theme mechanism**, and **CDS-WP-022 precedes context-sensitive value selection**. It gates **values and bindings, not structure**: identifier grammar, scale ownership, role admission, family maturity governance and source-set structural identity are context-independent by TC-1, TC-2, T-8, N-6 and RB-1. **OD-7 answered.** | — |
| **`OD-6B`** | **Answered by existing normative authority — no new Decision, and none is required.** VF-1 … VF-9 remain **separate artifact families**, each with its own maturity, evidence, gate and compatibility statement, under **AF-1**, **AF-3** and **AF-4**. Administrative batching may occur: **BATCHED REVIEW ≠ SHARED MATURITY**, **BATCHED GATE PREPARATION ≠ MATURITY INHERITANCE**. **No maturity group, cluster maturity, roll-up, inherited maturity, or aggregate gate exists or may be created.** `F-019-07` and `F-020-08` close with this disposition. | — |

**Effectivity.** All five instruments are **effective.** They became effective
**only** at the Human-Maintainer exact integration commit
`2cb244e889c1a6b5a278afb233995a0379b5d9ef` of the exact reviewed Working Tree
object, following a Fresh Independent Review and Nova integration adjudication.
**The effective registers were therefore `DEC-S-135` and `ADR-0005` — 135 decisions
and 5 ADRs at that commit; they have since advanced to 138 decisions and 7 ADRs —
`DEC-S-136` and `ADR-0006` effective at
`a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`, and `DEC-S-137`, `DEC-S-138` and
`ADR-0007` effective at `23914ecc48c1fb3cba5e3dab97a505589e821b6b`.** **A review PASS is not a commit, and
a Nova
recommendation is not an approval.**

**What the pass did not do:** it created **no** visual value, **no** identifier
instance, **no** Source Set, **no** role, **no** token source file, manifest,
resolver, schema, validator rule, test, or fixture; it admitted **no** evidence; it
changed **no** maturity; it accepted, closed, or re-scored **no** risk — the
register stays at **98** with **no `RISK-099`**; it registered **no** capability; it
made **no** claim; it touched **no** Semantic Status byte; and it **activated no
work package**. **`CDS-WP-022` is the recommended and sequenced Step-10 candidate
and is NOT authorized**, and **`F-020C-02` remains deferred** — the Step-9 decisions
do not re-derive the **M2** milestone mapping.

### Standing position

**CDS-WP-020 was authorized separately by the Human Maintainer on 2026-08-26** —
its authorization came from that decision alone, **not** from its position in this
roadmap — and it was **executed with result `DECISION_REQUIRED`**. Its reviewed
object was then **integrated** by the Human-Maintainer commit
`42a568d823de3388e45af62967546f13ad67eff6`, and the CDS-WP-020 closure and routing
pass recorded it as **`Closed`**. **That closure is effective** at the
Human-Maintainer integration commit of that object,
`3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`. **Closure grants no maturity, no evidence,
no claim, and no publication effect**, and **CDS-WP-020 activated no successor.**

**CDS-WP-021 — Adaptive Layout and Responsive Foundation is `Completed`**, by the
same rule: its authorization came from a separate, explicit
Human-Maintainer decision alone, **not** from its position in this roadmap and
**not** from the `DEC-S-135` sequencing recommendation, which named **CDS-WP-022**.
It is **executed with result
`COMPLETE WITH NOTES`** and **integrated** at
`a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`; its **closure was separately authorized
by the Human Maintainer and is effective at the Human-Maintainer exact-object
integration commit `01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`**, so **CDS-WP-021 is
`Completed` / `Closed`** with the execution result unchanged at **`COMPLETE WITH
NOTES`**.
It **confirms** the Layer 3 / Layer 5 / Layer 6 ownership split —
**answering `F-019-03` while leaving CR-004 registered at Layer 5** — and creates
**no** visual value, identifier, VF-4 root, or source set. **`WP021-D1` is APPROVED
and recorded as `DEC-S-136` with `ADR-0006`, both effective at that integration
commit**, and
**`WP021-D2` is DEFERRED** — **closure does not resolve it**, and **`DEFERRED OPEN
QUESTION ≠ INCOMPLETE WORK PACKAGE`**. **It authorized no
successor and closing it authorized none.**

**CDS-WP-022 — Theme and Environmental Presentation Model is `AUTHORIZED` / `ACTIVE
FOR EXECUTION`**, by the same rule as every work package before it: its
authorization came from a **separate, explicit Human-Maintainer decision alone** —
**not** from its position in this roadmap, **not** from the `DEC-S-135` sequencing
recommendation that named it, and **not** from the CDS-WP-021 closure. It is
**executed with result `COMPLETE WITH NOTES`**, after first returning
**`DECISION_REQUIRED`** — that first result is **execution history and is not
rewritten**. It derived the Theme Resolution Context contract that effective authority
uniquely determined and **escalated five normative choices** —
**`WP022-D1` … `WP022-D5`** — which the **Human Maintainer decided on 2026-09-12**;
a bounded rework then applied them. The decisions are recorded as
**`DEC-S-137`** (with **`ADR-0007`**, covering `DEC-S-137` **only**) and
**`DEC-S-138`**, all **`Accepted` and effective at the Human-Maintainer exact-object
integration commit `23914ecc48c1fb3cba5e3dab97a505589e821b6b`** of the
reviewed object — **136 decisions and 6 ADRs until it, 138 and 7 from it**, with the
risk register at **98** throughout. Across both passes CDS-WP-022 **created no theme
instance, no machine-readable context identifier, no default alias, no visual value,
no identifier, no role, no Source Set, no schema, no validator rule, no test and no
fixture; registered no risk; advanced no maturity; admitted no evidence; made no
claim; and activated no work package.** **Supported Theme Resolution Contexts: 0
before that commit and 2 — `Light` and `Dark`, with no default — from it.** Its object
is **integrated** at that commit, and its closure would be a **separate
Human-Maintainer act that has not occurred**: **`INTEGRATION ≠ CLOSURE`**. **`CDS-WP-020A` and CDS-WP-023 … CDS-WP-053 remain `Planned`,
not active, and not authorized** — **`THEME GATE SATISFIED ≠ CDS-WP-020A
AUTHORIZED`**.

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
register. **Three of the seven are answered and effective** — OD-1, OD-2 and OD-3,
by the Decision Integration Pass above — and **the remaining four were decided on
2026-09-05** by the **CDS Step-9 Decision Integration Pass**: **OD-4 answered and
OD-7 answered** (`DEC-S-132` with `ADR-0005`, and `DEC-S-135`), **OD-5 only
partially answered** (`DEC-S-133` — the scale ownership model and the
topology/value boundary, **not** the per-family topology parameters, and **VF-1
tonal topology is split out and stays open**), **OD-6A policy-answered** (`DEC-S-134`
— an admission rule, **not** a vocabulary), and **OD-6B answered by existing
normative authority with no new Decision.** **All four Decisions and ADR-0005 are
effective** at the Human-Maintainer exact integration commit
`2cb244e889c1a6b5a278afb233995a0379b5d9ef`.

**The value half stays gated all the same**: **VP-3, VP-5, VP-6 and VP-7 remain
unsatisfied for every visual family**, VP-2 remains unsatisfied for typeface
identity, weight identity and composites, and **only VP-4 moves** — for VF-1, VF-2,
VF-3, VF-5 and VF-6 — because **deciding an identifier is not creating one**.
**Visual values: 0. Visual source sets: 0. Visual Candidate families: 0.
VF-1 … VF-9: `Proposed`.**

**`DEC-S-135` settles the sequencing this roadmap could not act on by itself:**
**CDS-WP-022 — Theme and Environmental Presentation Model precedes
context-sensitive value selection**, because colour values and the light/dark token
layering are the same decision seen from two sides — while identifier, topology,
role-admission, maturity-governance and source-set structural identity work is
**context-independent and not blocked**. **A roadmap entry is a plan, not
permission**, **SEQUENCED NEXT ≠ AUTHORIZED**, and **`CDS-WP-020A` and
CDS-WP-023 … CDS-WP-053 all remain `Planned`, not active, and not authorized**.
**CDS-WP-021 selected no value**, so the `DEC-S-135` gate was untouched by it.
**`CLOSED ≠ SUCCESSOR AUTHORIZED`** and **`DEPENDENCY SATISFIED ≠ AUTHORITY
GRANTED`**: CDS-WP-022 listed CDS-WP-021 as its dependency, and that dependency
being satisfied **authorized nothing** — the Human Maintainer authorized CDS-WP-022
by a separate, explicit act.

**And the gate `DEC-S-135` guards changes state only at a commit.** **CDS-WP-022 is
authorized and executed, and the Human Maintainer has decided the theme mechanism** —
recorded as **`DEC-S-137`** and **`DEC-S-138`**, both **effective at
`23914ecc48c1fb3cba5e3dab97a505589e821b6b`**. **Until that integration commit the gate
was uncleared; from it, the `DEC-S-135` theme-mechanism sequencing condition is
satisfied.** Either way **`TS-1` continues to bind: no
semantic visual role carries a default alias** — **`DEC-S-138` part E creates none**,
so TS-1 is **satisfied by compliance, not by exemption** — and
**context-sensitive value selection remains unauthorized**. **`AUTHORIZED WORK
PACKAGE ≠ GATE SATISFIED`**, **`THEME GATE SATISFIED ≠ VALUE SELECTION
AUTHORIZED`**, **`THEME GATE SATISFIED ≠ WP-020A AUTHORIZED`**, **`ONE PREREQUISITE
SATISFIED ≠ ALL PREREQUISITES SATISFIED`**, and **`ALL PREREQUISITES SATISFIED ≠ WORK
PACKAGE AUTHORIZED`**. **VP-3, VP-5, VP-6 and VP-7 stay `UNSATISFIED`**, **VP-4 stays
`UNSATISFIED` for VF-4**, **visual values stay 0**, and **visual source sets stay
0.**

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
- [Visual Token Foundation Open Decisions](VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md) — **non-normative**; OD-1 … OD-7 (CDS-WP-020); OD-1 … OD-3 answered and effective; OD-4 and OD-7 answered, OD-5 partially answered, OD-6A policy-answered and OD-6B answered by existing authority — **effective**
- [Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md) · [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) · [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
- [ADR-0004 — Visual Token Representation and Source Identity Architecture](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md) — **`Accepted`, effective at commit `42a568d8…`**
- [Adaptive Layout and Responsive Foundation](../architecture/ADAPTIVE_LAYOUT_AND_RESPONSIVE_FOUNDATION.md) — CDS-WP-021; **normative**, effective at the Human-Maintainer integration commit `a6bd7bf0…`
- [Visual Foundation Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md) — CDS-WP-019 and CDS-WP-022; VF-9, **TM-1 … TM-12**
- [ADR-0007 — Theme Resolution and Context-Evidence Architecture](../decisions/ADR-0007-THEME-RESOLUTION-AND-CONTEXT-EVIDENCE-ARCHITECTURE.md) — **DEC-S-137 only**; **`Accepted` and effective at `23914ecc…`**
- [Decision Index](../decisions/DECISION_INDEX.md) · [Risk Register](../risks/RISK_REGISTER.md)
