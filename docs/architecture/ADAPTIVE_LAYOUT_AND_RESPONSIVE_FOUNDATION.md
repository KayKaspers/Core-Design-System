# Adaptive Layout and Responsive Foundation

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-021 — Adaptive Layout and Responsive Foundation
- **Date:** 2026-09-06
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for the Layer-3 adaptive-layout and responsive structure
  of VF-4**, effective at the Human-Maintainer exact-object integration commit
  `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9` (2026-09-11) of the exact reviewed
  Working Tree object, which followed independent review and Nova integration
  adjudication. Before that commit it was uncommitted executor output and changed
  **no** authoritative CDS state. **A review PASS is not a commit, and a Nova
  recommendation is not an approval.** It **selects no value** and **grants VF-4
  no technical root**.
- **Maturity of everything it positions:** **`Proposed`** — this document
  **promotes nothing** (DEC-S-036, *No retrospective maturity*; AF-5, *an
  architecture document is not the artifact*).
- **Execution result:** **`COMPLETE WITH NOTES`.** The structural contract below is
  derived from authority already in force. The one normative choice it could not
  derive — **`WP021-D1`**, the adaptive response mechanism and its reference frame —
  was **escalated by this work package and has since been decided by the Human
  Maintainer**; it is recorded here and registered as **`DEC-S-136`** with
  **[ADR-0006](../decisions/ADR-0006-ADAPTIVE_SPATIAL_CONTEXT_AND_NAMED_RANGE_ARCHITECTURE.md)**,
  both **effective at that same integration commit**. The second
  escalation, **`WP021-D2`** (whether VF-4 acquires a technical root and source-set
  identity), is **DEFERRED by the Human Maintainer** — **not rejected**, and it does
  **not** block this work package. **No `DEC-S-137`, no `ADR-0007`, and no
  `RISK-099` is created.**
- **Execution history.** This work package first returned **`DECISION_REQUIRED`**,
  correctly, because existing authority excluded none of the four admissible
  response mechanisms. **That result was not wrong and is not rewritten** — it is
  what produced the escalation the Human Maintainer then answered. **`WP021-D1` was
  open, and it is now decided.**

## Purpose and boundary

This document defines the **technology-neutral adaptive-layout and responsive
foundation that may safely exist at Layer 3** — the reusable spatial vocabulary and
the structural context model that **VF-4 Layout and Grid** owns — without absorbing
the Layer-5 pattern strategy that would turn the foundation into a composition
library.

It is the destination of two obligations that existing normative sources placed on
**CDS-WP-021 by name**:

1. *"**CDS-WP-021 must confirm this split before it defines any responsive
   foundation**"* — the Layer 3 / Layer 5 boundary of the
   [Visual Foundation Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md),
   recorded as the deferred finding **`F-019-03`**.
2. **RR-5** — *"**The mechanism is open.** Whether ranges are discrete breakpoints,
   continuous functions, container-relative, or a combination is **CDS-WP-021's**."*

Obligation 1 is **discharged**: the split is confirmed below, and it is confirmed
**as a reading of authority already in force**, not as a re-mapping.

Obligation 2 is **discharged by Human-Maintainer decision, not by derivation.**
Existing authority admitted more than one mechanism, so this work package escalated
the choice as **`WP021-D1`** rather than making it. The Human Maintainer decided it
on **2026-09-06**: the **Container-Relative Named-Range Foundation**, recorded below
and prepared as **`DEC-S-136`** with **ADR-0006**. **The architecture is decided; the
vocabulary is not.**

### What this document is not

It selects **no value**. No breakpoint threshold, viewport width, container width,
content width, gutter, margin, padding, spacing magnitude, size magnitude, grid
column count, target dimension, density magnitude, ratio, minimum or maximum width,
device class, or orientation threshold.

It selects **no technology**. It names no CSS feature, no layout engine, no query
mechanism, no framework, and no platform primitive — the same neutrality the
[Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md) already binds.

It creates **no identifier instance**, **no responsive-range name**, **no VF-4
technical root**, **no `sourceSetId`**, **no `sourceRevision`**, **no token source
file**, **no manifest**, **no resolver**, **no schema**, **no validator rule**, **no
test**, **no fixture**, **no component**, **no brand**, and **no Product Profile**.

It produces and admits **no evidence**, changes **no maturity**, accepts or closes
**no risk**, makes **no claim**, and activates **no work package**.

**No visual value exists in CDS**, **no responsive-range identifier exists**, **no
VF-4 technical root exists**, and **no VF-4 source set exists** — verified by search
at this revision, not assumed. CDS-WP-021 creates none of them.

## Authority basis — this document registers no new decision

*(Normative — the load-bearing statement of this document)*

> **Every binding statement below is an application of a decision, contract, or
> architecture already in force, or of the Human-Maintainer decision this work
> package escalated and did not make.** The one normative choice — the response
> mechanism — was **decided by the Human Maintainer** and is recorded as
> **`DEC-S-136`** (**ADR-0006**), **both effective at the integration commit
> `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`**. **This work
> package invented no normative choice of its own, and registers no risk.**

| This document's binding statements | Derive from |
| --- | --- |
| The adaptive foundation is Layer 3 and may depend on Layers 1–2 only | DEC-S-021 and the allowed-dependency table |
| Layer 5 owns viewport strategy and flow-level behaviour; Layer 3 may not depend on it | DEC-S-021; prohibited dependency 2; [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md), *Position in the eight-layer model* |
| A channel may transform presentation but may not push a requirement into the foundation | DEC-S-029; prohibited dependency 3; VF-I-11 |
| It introduces no layer, and a context is not a sixth token-flow layer | DEC-S-024; VF-I-1; TS-5 |
| A range is a named span of available space, carries no device or product term, removes no core function, and defeats no user text setting | **RR-1 … RR-4** of the Spatial Architecture |
| The model must remain expressible in non-web channels, where page or slide geometry replaces the viewport | **RR-6** |
| Grid, container, content width and responsive range each own a structure and never own the content that occupies it | Spatial Architecture, *Layout, grid and containers* |
| Reading order survives layout; orientation is never locked; reflow is mandatory; a container tolerates unexpected content | 1.3.2, 1.3.4, 1.4.10; Spatial Architecture layout constraints 2 – 5 |
| No information may be conveyed by proximity or position alone | Accessibility Requirements Baseline **3.7**, WCAG 1.3.3 — a **CDS-alone** obligation |
| Density is a declared spatial intensity that never reduces a target obligation and never removes a status qualifier | Spatial Architecture, *Density*; 2.5.8; VF-I-11 |
| Accessibility cannot be waived by an ordinary exception | DEC-S-059 |
| A target is not a claim; an automated check is never sufficient evidence | DEC-S-050, DEC-S-053 |
| Every visual artifact is AE-0 and admitted evidence never transfers | DEC-S-126; AF-2; the [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) |
| No semantic role carries a default alias before CDS-WP-022 decides the theme mechanism | **DEC-S-135**, TS-1 … TS-6 |
| Naming follows the CDS identifier profile; a rename is a migration event | DEC-S-081, DEC-S-082, N-1 … N-8 |
| The visual identifier grammar and family roots are fixed for VF-1, VF-2, VF-3, VF-5 and VF-6 — and **for no other family** | **DEC-S-132** clauses 9 – 11, [ADR-0005](../decisions/ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md) |
| An ordered primitive set is bound by ST-1 … ST-7, and **VF-4 is excluded from the per-scale topology decision** | **DEC-S-133** clauses 1 – 4 and 10 |
| A visual semantic role enters Core only on demonstrated cross-consumer need, and no role vocabulary exists | **DEC-S-134** |
| The Source Set is the independently evaluable unit; maturity binds to (`sourceSetId`, `sourceRevision`) | **DEC-S-131**, [ADR-0004](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md) |
| Maturity is granted by a gate, never by a document | DEC-S-035, DEC-S-036, DEC-S-126, VF-I-14, AF-1, AF-5 |
| **The declared Adaptation Container, named discrete available-space ranges, downstream continuous behaviour, fixed-geometry channel authority, and `SPATIAL CONTEXT ≠ THEME RESOLUTION CONTEXT`** | **`DEC-S-136`** (**[ADR-0006](../decisions/ADR-0006-ADAPTIVE_SPATIAL_CONTEXT_AND_NAMED_RANGE_ARCHITECTURE.md)**) — Human-Maintainer decision of 2026-09-06, **effective at the integration commit `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`** |

Where a statement could only be reached by making a **new** normative choice, it is
**not made** by this work package. The one such choice was escalated and has been
**decided by the Human Maintainer**; the one that remains is recorded under
[The Human-Maintainer decisions](#the-human-maintainer-decisions) with the authority
that must resolve it.

## The Layer 3 / Layer 5 / Layer 6 ownership model

*(Normative — and the obligation `F-019-03` placed on this work package)*

### The confirmation

> **Layer 3 owns the spatial vocabulary and the structural context model.**
> **Layer 5 owns the product or pattern response selected for a context.**
> **Layer 6 owns channel-imposed geometry and degradation constraints.**

**This confirms a reading; it re-owns nothing.** The
[Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md) stated it and
declined to resolve it by editing the traceability matrix. CDS-WP-021 confirms it
from the same authority the matrix itself rests on, and **CR-004 — Multi-viewport
behavior remains registered at Layer 5, unchanged**, in the
[Architecture Requirements Traceability](ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md).

**Why the two statements never conflicted.** The roadmap places CDS-WP-021 at
Layer 3 because CDS-WP-021 owns the **VF-4 vocabulary**. The traceability matrix
places CR-004 at Layer 5 because CR-004 asks for a **strategy** — *"interfaces must
remain usable across viewport situations, including core functions on small
screens"*. A vocabulary and the strategy that consumes it are different artifacts at
different layers, and both mappings are correct at the same time. **The apparent
discrepancy was a category confusion, not a contradiction**, and resolving it
required no change to either record.

### Ownership rules

| # | Rule |
| --- | --- |
| **LO-1** | **Layer 3 owns the reusable spatial vocabulary and the structural context model.** **VF-3** owns spacing-scale structure, sizing-scale structure, the density model structure, and the target-sizing foundation obligation. **VF-4** owns grid structure, containers, the content-width foundation, and the responsive-range vocabulary. |
| **LO-2** | **Layer 5 owns the response.** *Which* layout a screen uses, *when* a pattern changes, and *what* it becomes are pattern decisions, and CDS-WP-021 makes none of them. |
| **LO-3** | **Layer 6 owns channel-imposed geometry and degradation.** Page size, pagination, slide geometry, export constraints, and host-controlled rendering are channel constraints, not foundation constructs. |
| **LO-4** | **`RANGE ≠ BEHAVIOUR` · `CONTEXT ≠ PATTERN` · `FOUNDATION ≠ COMPOSITION`.** A foundation supplies the terms in which a response can be described. It never supplies the response. |
| **LO-5** | **The dependency direction is fixed and one-way.** Layer 3 may depend on Layers 1–2 only. **A Layer-5 pattern need never justifies a Layer-3 construct** (prohibited dependency 2, applied to layout exactly as VF-I-4 applies it to components), and **a Layer-6 channel may never push a requirement down into the foundation** (prohibited dependency 3). |
| **LO-6** | **CR-004 remains registered at Layer 5.** Confirming the split moves no requirement, re-owns no requirement, and edits no traceability row. |
| **LO-7** | **A construct that cannot be described without naming a screen, a flow, a product, a component, or a channel is not Layer 3.** This is the operative test, and it is the same test VF-I-4 and N-2 … N-5 already apply. |
| **LO-8** | **Layer 3 may describe *that* a response exists without deciding *which*.** Declaring that a composition adapts across a context is vocabulary; declaring what it adapts into is pattern. |

### The boundary, worked

*(Normative as a classification. The right-hand column names constructs CDS does
**not** have and is **not** building; they illustrate the boundary and adopt
nothing.)*

| Layer-3 concept — **admissible** | Not Layer 3 — **why** |
| --- | --- |
| An **available-space range** as a named span | *"Switch navigation to a collapsed menu at range X"* — a pattern response (**Layer 5**) |
| A **container context** as a bounded region with declared extent behaviour | *"The dashboard becomes two columns at threshold Y"* — a screen composition (**Layer 5**) |
| A rule requiring structure to **survive text growth, reflow and magnification** | A consumer-specific screen composition that satisfies that rule (**Layer 5**, or the consumer) |
| A **content-width** construct as a reading-measure constraint | The measure chosen for one product's documentation site (**Layer 5** or a **Product Profile**) |
| A declaration that a channel's **geometry is fixed and ranges do not apply** | The page master, margin set, or slide template that channel uses (**Layer 6**) |
| A declaration that a role must have a **non-spatial carrier** | The specific carrier a component renders (**Layer 4**) |

## The spatial context model

*(Normative as a structure. **No context instance, no reference frame selection,
and no value is created.**)*

The first mission question of CDS-WP-021 is *what information constitutes a
responsive or adaptive spatial context*. The answer must satisfy two normative
sources that pull in different directions and are both binding: **RR-6** requires
the model to remain expressible in non-web channels *"where 'viewport' has no
meaning and page or slide geometry replaces it"*, while the Spatial Architecture
channel table records that in paginated channels *"**ranges do not apply**; page
geometry replaces them"*.

**Both hold only if the frame generalizes and the range construct does not.** That
reconciliation is compelled by the two sources jointly; it is recorded here, not
chosen.

| # | Rule |
| --- | --- |
| **CX-1** | **A spatial context is the declared description of the space an artifact is composed into.** It is **data about the composition environment**, never a decision about what to compose (LO-4). |
| **CX-2** | **Its reference frame is channel-determined and must be declared.** A model that names only one frame cannot satisfy **RR-6**, because *viewport* is meaningless in a paginated or slide channel. |
| **CX-3** | **Continuity decides whether a range applies.** Where available space is **continuously variable**, a responsive range is applicable. Where geometry is **fixed**, it is not, and the channel geometry occupies that position instead — exactly as the Spatial Architecture and the [Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md) already record for channels 4 and 5. |
| **CX-4** | **A spatial context carries no meaning.** Nothing may be communicated by *which context is active*, and no status, severity, confidence, freshness, or evidence value may be expressed by a spatial difference (VF-I-5, VF-I-6, and T-5 applied to space rather than presentation). |
| **CX-5** | **A spatial context never removes core function.** Reducing complexity is permitted; hiding that an option exists, misrepresenting status, or concealing a risk is not (**RR-3**, baseline 5.7). |
| **CX-6** | **Text metrics are context *inputs*, never foundation *outputs*.** User text resize, text-spacing overrides, translated string length, and magnification change the space a composition needs. The foundation must tolerate them; it may never fix them (**RR-4**, SP-3, SP-4, SR-7, SR-8, baseline 8.3, 8.4). |
| **CX-7** | **A spatial context is resolvable offline and deterministically.** No context may require an external service, registry, or network reference (DEC-S-030, DEC-S-080, DEC-S-091). |
| **CX-8** | **A spatial context is not a theme, not a channel, not a Product Profile, and not a status** — and it is **not a sixth token-flow layer** (DEC-S-024, VF-I-1, TS-5). |
| **CX-9** | **A Spatial Context is not automatically a Theme Resolution Context** (**DEC-S-136**). **`SPATIAL CONTEXT ≠ THEME RESOLUTION CONTEXT`.** They are **separate authority dimensions**, and **CDS-WP-021 does not decide whether or how they compose** — that mapping belongs to **CDS-WP-022**, if and when it is separately authorized. This is a **boundary statement, not a theme decision**, and it neither prejudges nor forecloses what CDS-WP-022 may decide. |

> **CX-9 is the boundary that keeps CDS-WP-022's decision its own.** Read
> mechanically, the Theme Architecture's *"a context that varies within a channel is
> a theme"* would sweep a responsive range into the theme mechanism **by
> implication** — deciding, in passing, that a resolver composes at least two
> context dimensions. That is the **form-versus-substance** failure **DEC-S-135**
> exists to prevent, and **TC-6** requires the semantic layer to presuppose no
> context set. Keeping the two separate costs nothing and forecloses nothing.

## The Adaptation Container

*(Normative — **DEC-S-136**, Human-Maintainer decision of 2026-09-06, **effective at
the integration commit `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`**.
**[ADR-0006](../decisions/ADR-0006-ADAPTIVE_SPATIAL_CONTEXT_AND_NAMED_RANGE_ARCHITECTURE.md)**
carries the rationale. **No container instance, no identifier, and no value is
created.**)*

The primary adaptive reference frame for responsive Layer-3 classification is a
**declared Adaptation Container**.

| # | Rule |
| --- | --- |
| **AC-1** | **An Adaptation Container is a technology-neutral spatial reference boundary** whose available space may be classified by the responsive foundation. |
| **AC-2** | **It is declared, never inferred.** A frame that must be guessed is not a foundation construct. |
| **AC-3** | **It is not** a CSS container query, a DOM construct, a framework component, a device class, a viewport identity, a product, a screen type, or a Layer-5 pattern. |
| **AC-4** | **A root or application context may serve as the declared Adaptation Container.** Doing so creates **no viewport or device identity**: what is declared is a **boundary whose available space is classified**, not the device that produced it. |
| **AC-5** | **`viewport`, `desktop`, `tablet`, `mobile`, `phone` and `monitor` are not CDS Core responsive identifiers**, and none is created here (**RR-2**, N-2, N-3). |
| **AC-6** | **The container frame is the Core frame because the viewport frame is too narrow to be one** — it has no referent in paginated and slide channels (**RR-6**), it is global where dense operational data is local, and it invites exactly the device-derived names RR-2 forbids. **The container model excludes the viewport model from Core identity; it does not exclude a root context from being a container.** |

## The responsive range model

*(Normative as constraints. **RR-1 … RR-6 are the standing contract; this section
applies them and changes none.** The **Core range model** below is **DEC-S-136**'s,
**effective at the integration commit `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`**.
**No range, no range name, and no threshold is
defined.**)*

| # | Rule |
| --- | --- |
| **AR-1** | **RR-1 … RR-6 bind unchanged.** Nothing below weakens, replaces, or reinterprets them. |
| **AR-2** | **A responsive range is one member of the spatial-context model, not the whole of it.** It applies where space is continuously variable (**CX-3**). |
| **AR-3** | **A range names a span; it never names a behaviour** (**RR-1**, LO-4). A construct that states what happens has left Layer 3. |
| **AR-4** | **A range name is a foundation identifier** (**RR-2**) and carries **no device, screen, brand, product, consumer, platform, component, channel, status, theme, or profile term** (N-2 … N-6, RN-3 … RN-7). **No range name is created, adopted, reserved, or recommended here.** |
| **AR-5** | **A range is declared, never inferred.** A consumer, a tool, or a validator must be able to read the range set from the source rather than from values, so that a change to it is a **detectable** change (the ST-1 principle, applied as a declaration obligation and not as a scale). |
| **AR-6** | **A concrete range set, once authored, is an ordered set and ST-1 … ST-7 bind it** — and **DEC-S-133 clause 10 explicitly excluded VF-4** from the per-scale topology decision, so **no VF-4 topology has been decided and none may be assumed.** Deciding that the Core vocabulary is *named and discrete* is **not** deciding its anchor, progression rule, step count, extension behaviour, or exclusions. |
| **AR-7** | **A range boundary is not a promise of identical rendering.** Product UI, PDF, presentation and diagram do not render identically and are not required to (DEC-S-029, VF-I-11). |
| **AR-8** | **Where ranges do not apply, that is a declared limitation, never a silent drop** (VF-I-11, and the `Reduced` / `Unsupported` / `Transformed` declaration obligation of the Channel Mapping). |
| **AR-9** | **The Core range model is named discrete available-space ranges** (**DEC-S-136**), classified against a **declared Adaptation Container** (AC-1). A Responsive Range remains **a named span of available space** — **RR-1 is applied, not changed**. |
| **AR-10** | **Continuous transformation and interpolation are permitted downstream where separately authorized** — at Layer 5 as pattern behaviour, or in a channel or runtime adapter. **They are not the Core Responsive Range identity model**, and CDS-WP-021 neither selects nor implements them. |
| **AR-11** | **`CORE RANGE IDENTITY ≠ DOWNSTREAM RESPONSE BEHAVIOUR`.** Discrete identity and continuous behaviour are **complementary layers, not competing options**. |
| **AR-12** | **Continuous behaviour is not prohibited, and its mathematical representation is not defined here.** **No new `$type` is required, and DEC-S-130 is altered in no way.** **The closed `color` / `dimension` / `number` admission profile is not the reason for AR-9** — that is a fact about the current, governed, extendable profile, not a proof that continuous behaviour is architecturally impossible. The reason is that **Core identity needs a name to bind obligations to**, which a relation does not supply. |

> **Why named discrete ranges are Core while behaviour stays Layer 5.** A named span
> is **declared rather than inferred**, so a change to the set is **detectable**;
> each name is a **foundation identifier** that RR-2 and N-2 … N-6 can police; the
> vocabulary is **reviewable by a person**; and a rename is an **identity event with
> a migration reference** rather than a silent redefinition. A continuous relation
> supplies none of these. **`RANGE ≠ BEHAVIOUR`**: a range names *where you are*,
> never *what happens*.

## Grid, container and content width

*(Normative as structural contracts. **No taxonomy, no configuration, and no value
is selected.**)*

The Spatial Architecture already fixes what each construct owns and never owns. This
section adds the **relationships** between them and the obligations that hold
regardless of the mechanism.

| # | Rule |
| --- | --- |
| **GC-1** | **A grid is a declared structural rhythm and its subdivisions.** It never owns which content occupies it. |
| **GC-2** | **A grid is a rhythm, not a promise of identical rendering** (DEC-S-029). |
| **GC-3** | **A container is a bounded region with declared extent behaviour.** It never owns the meaning of its content. |
| **GC-4** | **A container must tolerate content it did not expect** — longer labels, translated strings, larger user text, and missing values. A container that assumes a maximum string length is defective, not configured (baseline 8.3, 8.4, CR-023). |
| **GC-5** | **A content width is the reading-measure constraint for continuous text.** It owns **no** value. |
| **GC-6** | **The three are separate constructs with a declared relationship, not a hierarchy.** A grid does not imply a container, a container does not imply a content width, and a content width is not a container extent. Collapsing them is how a foundation acquires the assumptions of a layout engine. |
| **GC-7** | **Reading order survives layout**, in every channel and after export (1.3.2), and **layout never locks orientation** (1.3.4). |
| **GC-8** | **No grid taxonomy, container taxonomy, or named configuration is selected here.** **`WP021-D1` fixed the reference frame and the range kind; it did not fix a grid taxonomy.** Whether the grid model is column-based, area-based, flow-based, or taxonomy-free remains a **separate vocabulary question** for separately authorized work, and it must be answered **relative to a declared Adaptation Container** (AC-1) rather than to a device or viewport. |
| **GC-9** | **No value.** No column count, gutter, container extent, content width, margin, padding, minimum or maximum width, or threshold. |

### Disposition of the three constructs

| Construct | Disposition under CDS-WP-021 |
| --- | --- |
| **Grid structure** | **`IN_SCOPE_AND_DERIVABLE`** as a structural contract (GC-1, GC-2, GC-6 … GC-9). Its **concrete taxonomy** is **`DEFERRED_BY_EXISTING_AUTHORITY`** — **`WP021-D1` is decided and did not decide it**; it is a separate vocabulary question for separately authorized work (GC-8). Its **values** are **`DEFERRED_BY_EXISTING_AUTHORITY`** — value selection is governed by VP-1 … VP-7 and routed to a separately authorized authoring work package. |
| **Container model** | **`IN_SCOPE_AND_DERIVABLE`** as a structural contract (GC-3, GC-4, GC-6 … GC-9). **Container extents** are **`DEFERRED_BY_EXISTING_AUTHORITY`** — they are values. |
| **Content-width model** | **`IN_SCOPE_AND_DERIVABLE`** as a structural contract (GC-5 … GC-9). **Content-width magnitudes** are **`DEFERRED_BY_EXISTING_AUTHORITY`** — they are values. |

## Density and adaptation

*(Normative as an interaction contract. **Density itself is VF-3, and no density
level and no number of levels is defined.**)*

| # | Rule |
| --- | --- |
| **DA-1** | **Density belongs to VF-3 and adaptation to VF-4; neither absorbs the other.** A density change is not an adaptation, and an adaptation is not a density change. They are separate artifact families and **maturity is never inherited between them** (AF-1, AF-3). |
| **DA-2** | **Density and adaptation compose, and obligations do not weaken under composition.** An obligation that holds for each separately holds for both together. This is the rule the composition exists to make explicit, because a weakening is easiest to lose where two mechanisms meet. |
| **DA-3** | **`DENSITY ≠ COMPRESSION AT ANY COST`.** A density level is a **declared spatial intensity**, not an ad-hoc compression. |
| **DA-4** | **Neither density nor adaptation reduces a target below its obligation** (2.5.8). Target sizing is a floor; density operates above it, and so does adaptation. **Accessibility cannot be waived by an ordinary exception** (DEC-S-059), and constrained space is not an exception. |
| **DA-5** | **Neither removes information, a status qualifier, or a non-spatial carrier.** A denser or more constrained display shows the same truth in less space, **or it declares that it cannot** (VF-I-11, VF-I-6, baseline 5.7, 7.4). |
| **DA-6** | **The density, reflow and target-size interaction remains an OPEN PROBLEM and is not solved here.** It is **not structurally checkable** and requires **rendering evidence**, which does not exist (**CDS-WP-031**). Recording the constraint is not solving the problem. |

> **Dense operational data is the most-evidenced consumer need in CDS and its
> least-solved layout problem.** It is recorded as unresolved, not designed around —
> the same position the Spatial Architecture took, restated here because adaptation
> is where the difficulty concentrates.

## Accessibility constraints

*(Normative as structure. **No threshold is restated or invented, no conformance is
claimed, and no evidence is produced.**)*

> **`TARGET ≠ CLAIM` · `STRUCTURAL CONTRACT ≠ RENDERING EVIDENCE`**

The obligation in each row is **whatever the cited source itself requires**. CDS
restates no external criterion text and invents no additional threshold.

| Obligation | Source | Position under this foundation | Checkable how |
| --- | --- | --- | --- |
| **Orientation is never locked** | 1.3.4 | Binding on every grid, container and range (GC-7) | **Structural** — a declared orientation dependency is detectable |
| **Reading order survives layout and export** | 1.3.2, baseline 1.3 | Binding in every channel (GC-7) | **Rendering** — per channel |
| **Reflow** | 1.4.10, baseline 3.2 | VF-3 and VF-4 shared; CX-6, GC-4 | **Rendering** — CDS-WP-031 |
| **Text resize** | 1.4.4, baseline 3.3 | Adaptation must not defeat it (**RR-4**, CX-6) | **Rendering** — CDS-WP-031 |
| **Text spacing tolerance** | 1.4.12, baseline 3.4 | Adaptation must not defeat it (**RR-4**, CX-6) | **Rendering** — CDS-WP-031 |
| **Target sizing** | 2.5.8, baseline area 3 | A floor that neither density nor adaptation lowers (**DA-4**) | **Rendering** — and currently **unmeasurable**, because no CDS size value exists |
| **No meaning by proximity or position alone** | 1.3.3, baseline **3.7** — **CDS-alone** | Owned by VF-3 and VF-4; a relationship expressed by a gap needs a declared non-spatial carrier | **Structural** — an undeclared carrier is detectable |
| **Localization and text expansion** | baseline 8.3, 8.4, CR-023 | No container, grid, or range assumes a fixed or maximum string length (**GC-4**, CX-6) | **Structural** in the declaration; **rendering** in the outcome |
| **Magnification** | 1.4.4, baseline 3.3 | A context input, never a foundation output (**CX-6**) | **Rendering** — CDS-WP-031 |
| **No function removal under constrained space** | **RR-3**, baseline 5.7 | Binding on every context and every range (**CX-5**) | **Structural** in the declaration; **rendering** and **consumer** in the outcome |
| **Bidirectional text not architecturally excluded** | baseline 8.6 | A **structural constraint**, not a commitment to ship right-to-left support | **Structural** |

**What this section does not do.** It claims **no** WCAG conformance at any level,
produces **no** evidence by declaration, and asserts **no** rendered behaviour.
**Every rendering-dependent row above is routed to CDS-WP-031** and, for non-web
channels, to the per-channel accessibility profile each channel needs before any
Candidate or Stable artifact in it (DEC-S-058). **An automated check is never
sufficient** (DEC-S-053).

**Evidence state:** every VF-3 and VF-4 artifact is **AE-0**. Nothing has been
rendered, reflowed, magnified, or measured, and **no accessibility claim of any
level is valid**.

## Channel preservation

*(Normative as a boundary. It applies the existing channel classification and
changes none of it.)*

> **Do not force *viewport* onto a channel that has none.** The reference frame is
> channel-determined (**CX-2**); the range construct is not universal (**CX-3**).

**`DEC-S-136` settles this for fixed geometry.** For **PDF, reports, print,
presentations and other fixed-geometry contexts, the channel's geometry is
authoritative for that channel**, and **responsive-range semantics are not forced
into them**. The broader spatial context model still describes those channels —
their reference frame is simply page or slide geometry rather than a variable span.
**RR-6 is satisfied because the reference frame generalizes, not because the range
construct does.** Forcing ranges into paginated channels would additionally invert
**LO-5**, letting a Layer-6 constraint dictate a Layer-3 construct.

| Channel | Spatial reality | Does a responsive range apply? | What holds regardless |
| --- | --- | --- | --- |
| **Product UI** | Continuous, resizable, reflowing | **Yes** — the range construct is applicable here | Reflow, resize, text spacing, target floor, no function removal |
| **Documentation** | Long-form, reflowing, DE/EN parity | **Yes** — reading measure dominates | Text expansion tolerance, reading order, reading measure |
| **Repository presentation** | **Host-controlled rendering** | **Not guaranteed** — VF-4 is `Unsupported` here; the host controls layout | CDS covers what it authors, not what a host does with it |
| **PDF and reports** | Paginated, **fixed geometry**, no reflow, possibly printed | **No** — page geometry replaces ranges (**CX-3**, **AR-8**) | Reading order across pagination; meaning without colour; declared limitation |
| **Presentations** | **Fixed slide geometry**, distance viewing | **No** — slide geometry replaces ranges | A density model built for operations is wrong here; declared limitation |
| **Diagrams** | Structural placement carries meaning | **Not as a UI range** | **Position is meaningful and therefore requires a non-spatial carrier** (1.3.3) |
| **Data visualization** | Dense, encoding-sensitive | **Not as a UI range** | Position is an encoding channel and **never the only one**; the accessible alternative representation belongs to **CDS-WP-039** |

**Spatial semantics do not transfer between these; meaning does** (DEC-S-029,
VF-I-11). A distinction a channel cannot render is **declared as a limitation**,
never silently dropped — and a channel may never push its geometry back into the
foundation (**LO-5**).

## Product Profile boundary

*(Normative — no extension point is created, and none exists)*

| A Product Profile **may** | A Product Profile **may never** |
| --- | --- |
| Override a spatial or layout **value** at a **named, approved** extension point | Add, remove, rename, or repurpose a spatial or layout **construct** |
| Select among options the Core defines | Redefine what a range, container, grid, or content width **means** |
| — | Reduce a target below its obligation, or break reflow, resize, or text-spacing tolerance |
| — | Introduce a layout that removes core function at any context (**CX-5**, **RR-3**) |
| — | Make position or proximity the sole carrier of meaning (**1.3.3**) |
| — | Override **Layer-5** authority, or acquire pattern authority through a spatial override |

**No extension point is named today** — the set is **empty**, **SR-10 is
unchanged** (*no role is a named extension point*), and only **CDS-WP-032** may name
one. **No Product Profile exists, none is active, and none may be approved**: the
Consumer Maintainer role is **unstaffed** (FM-F-006). **This document creates no
extension point and activates no Profile.**

## Theme boundary

*(Normative as a boundary. **CDS-WP-021 decides no part of the Theme and Context
Mechanism.**)*

> **`A THEME RE-BINDS; IT NEVER REDEFINES`** (T-1, VF-I-9)
> **`THEME = RESOLUTION CONTEXT`** — not a sixth token-flow layer (DEC-S-024, TS-5)

| # | Statement |
| --- | --- |
| 1 | **This document defines no theme ID, no theme context vocabulary, no environmental presentation mode, no semantic-to-reference theme binding, no default theme alias, and no light, dark, or high-contrast mechanics.** All of it belongs to **CDS-WP-022**, which at the CDS-WP-021 execution and effectivity milestones was **`Planned`, not active, and not authorized** — and **CDS-WP-021 did not authorize it**. **CDS-WP-022 was later authorized by a separate, explicit Human-Maintainer act**, is **integrated** at `23914ecc48c1fb3cba5e3dab97a505589e821b6b`, and is currently **`AUTHORIZED` / `ACTIVE FOR EXECUTION`** and **not closed**. **`LATER AUTHORIZATION ≠ CDS-WP-021 AUTHORIZATION`**, and recording that later state is a lifecycle update, not an architecture change. |
| 2 | **TS-1 holds unchanged:** no semantic visual role carries a default alias to a reference primitive before CDS-WP-022 decides the mechanism. **This document creates no alias, no role, and no binding.** |
| 3 | **TS-2 holds unchanged:** CDS-WP-022 precedes **context-sensitive value selection**. **This document selects no value of any kind**, so it does not reach that gate. |
| 4 | **TS-3 and TS-4 apply:** the structural work above — the layer split, the shape of the context model, the range obligations, and the grid, container and content-width contracts — is **context-independent** by **TC-1**, **TC-2**, **T-8**, **N-6** and **RB-1**, and is therefore not blocked. **`CDS-WP-022 BEFORE VALUE SELECTION` does not mean `CDS-WP-022 BEFORE EVERY STRUCTURAL ACTIVITY`.** |
| 5 | **What CDS-WP-022 may consume from this document:** that a spatial context has a **declared, channel-determined reference frame** (CX-2, AC-1); that **continuity decides applicability** (CX-3); that a spatial context **carries no meaning** (CX-4); and that **a spatial context is not a theme resolution context** (CX-9). |
| 6 | **`SPATIAL CONTEXT ≠ THEME RESOLUTION CONTEXT`** (**DEC-S-136**). The two are **separate authority dimensions**. **CDS-WP-021 does not decide whether or how they compose**, and **CDS-WP-022 retains full authority** to define a mapping or composition later. **This is a boundary, not a theme decision**, and it neither prejudges nor forecloses that mapping. |
| 7 | **Rejecting the implicit reading is the point.** Treating a spatial context as a theme by implication would decide — silently, and in passing — that a resolver composes at least two context dimensions, which is a **mechanism decision reserved to CDS-WP-022** (DEC-S-135, TC-6). The conservative reading holds until CDS-WP-022 says otherwise. |

## Validation requirements

*(Requirements **on CDS-WP-024**. **No validator, schema, test, fixture, validation
case, render gate, or conformance logic is created or changed here.**)*

> **`AUTHOR ≠ VALIDATE` · `STRUCTURE CHECK ≠ RENDERING EVIDENCE` ·
> `VALIDATION ≠ CONFORMANCE` · `EVIDENCE ≠ AUTHORITY`**

### Structurally checkable — a later validator must be able to detect

1. A range identifier carrying a **device, screen, product, brand, consumer,
   platform, component, channel, status, theme, or profile term** (**AR-4**).
2. A range or context construct that **states a behaviour** rather than a span
   (**AR-3**, **LO-4**).
3. A spatial context whose **reference frame is undeclared** (**CX-2**).
4. A grid, container, content-width, or range construct that **conveys a
   relationship with no declared non-spatial carrier** (**1.3.3**, baseline 3.7).
5. A container or layout construct declaring a **fixed or maximum string length
   assumption** (**GC-4**, baseline 8.4).
6. A construct that **locks orientation** (**GC-7**).
7. A profile override **outside a named extension point** — the set being **empty**,
   every such override currently fails.
8. A layout construct whose identifier or declaration **can only be described by
   naming a screen, flow, product, component, or channel** (**LO-7**).
9. An **ordered** VF-4 set that does not satisfy **ST-1 … ST-7**, **if** one is ever
   created — noting that **no VF-4 topology is decided** (**AR-6**).
10. A VF-4 construct asserting a **technical root or `sourceSetId`** that no
    Decision has granted (**`WP021-D2`**).

### Not structurally checkable — rendering evidence required

Reflow, text resize, text-spacing tolerance, magnification, target-size outcome,
reading order after pagination or export, and the **density, reflow and target-size
interaction** (**DA-6**). These are routed to **CDS-WP-031** and to the per-channel
accessibility profiles. **An automated check is never sufficient** (DEC-S-053), and
**a validator pass is metadata coherence, never maturity authority**.

## Evidence boundary

Every VF-3 and VF-4 artifact is **AE-0**. No adaptive or responsive artifact exists,
none has been rendered, and **no accessibility claim of any level is valid**. The
single admitted evidence package in CDS — **`AE1-CDS-WP016-SEMSTATUS-004`**, AE-1,
bound to source revision `semantic-status-rev-0002-candidate` — covers the
**channel-independent Semantic Status source and contract family only** and **does
not transfer** to anything in this document. **Evidence never transfers across a
source revision, a family, a channel, a context, or a consumer** (AF-2, DEC-S-126).

**Visual values: 0 · visual Source Sets: 0 · visual Candidate families: 0 ·
Stable: 0 · claims: none · conformance: none · publication: `Private
Development`.** **VF-1 … VF-9 remain `Proposed`.**

## The Human-Maintainer decisions

*(**`WP021-D1`** and **`WP021-D2`** were **escalation keys for the CDS-WP-021
execution report, not governance identifiers.** **`WP021-D1` is now decided** and is
carried by **`DEC-S-136`** and **ADR-0006**, both **effective at the integration
commit `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`**.
**`WP021-D2` is deferred** and has **no Decision and no ADR**. **No `DEC-S-137`, no
`ADR-0007`, no `RISK-099`, and no new `OD` identifier is created.**)*

### `WP021-D1` — DECIDED: the Container-Relative Named-Range Foundation

**RR-5 assigned the mechanism to CDS-WP-021 and left it open.** Discrete ranges,
continuous functions, container-relative adaptation, and hybrid models were **each
admissible** under RR-1 … RR-6, and no committed CDS source excluded any of them.
Selecting one was a new normative choice, so this work package **escalated it rather
than making it** and returned `DECISION_REQUIRED`.

**The Human Maintainer decided it on 2026-09-06.** The approved model is the
**Container-Relative Named-Range Foundation**: a **declared Adaptation Container**
as the primary reference frame (**AC-1 … AC-6**), **named discrete available-space
ranges** as the Core Layer-3 response vocabulary (**AR-9**), **continuous behaviour
permitted downstream** but never Core range identity (**AR-10 … AR-12**),
**fixed-geometry channels governed by their own geometry**, and **`SPATIAL CONTEXT ≠
THEME RESOLUTION CONTEXT`** (**CX-9**).

It is recorded as **`DEC-S-136`**, with
**[ADR-0006](../decisions/ADR-0006-ADAPTIVE_SPATIAL_CONTEXT_AND_NAMED_RANGE_ARCHITECTURE.md)**
carrying the rationale. Both were **`PROPOSED / AUTHORIZED FOR INTEGRATION`** before
the exact-object integration, and
**`APPROVED PROPOSITION ≠ EFFECTIVE REPOSITORY DECISION`** held until then. Both
became effective only at the Human-Maintainer exact-object integration commit
`a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`: **`DEC-S-136` is effective there**, and
**ADR-0006 is `Accepted` and effective at the same commit**.

**The architecture is decided; the vocabulary is not.** No range name, no number of
ranges, no threshold, and no boundary value is selected, and none may be inferred.

### `WP021-D2` — DEFERRED: whether VF-4 acquires a technical root and source-set identity

**DEC-S-132 clause 9 fixes technical roots for `color`, `typography`, `space`,
`shape` and `surface` — for the five registered visual families *in current scope*,
and for no other.** **VF-4 is not among them**, and the ten fixed source-set
identities of clause 10 include none for VF-4. The
[Visual Reference Token Foundation](VISUAL_REFERENCE_TOKEN_FOUNDATION.md) records
that **VF-4 holds no reference token**, and the
[Visual Semantic Token Foundation](VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) records that
**VF-4 contributes no semantic role.**

**CDS-WP-021 therefore may not create a VF-4 root, a range identifier, a
`sourceSetId`, or a `sourceRevision`, and it creates none.** Whether VF-4 should
acquire them at all — and whether the responsive-range vocabulary is
machine-readable token source or a structural construct expressed some other way —
is a normative choice that **the closed scope of DEC-S-132 did not make.** **Silence
is recorded as silence, and extending DEC-S-132 by implication is prohibited.**

**The Human Maintainer has DEFERRED `WP021-D2`** (2026-09-06). **Deferral is not
rejection**, and it approves **no** concrete VF-4 identity.

| Item | State |
| --- | --- |
| VF-4 technical root | **OPEN — none selected** |
| VF-4 Source Set identity | **OPEN — none selected** |
| VF-4 `sourceSetId` · `sourceRevision` | **NONE** |
| Concrete VF-4 range identifiers | **0** |
| Decision for `WP021-D2` | **NONE** — and none is created |
| ADR for `WP021-D2` | **NONE** — and none is created |

**Why the deferral costs nothing here.** The WP-021 structural contract completes
**without** an identity-bearing machine-readable VF-4 Source Set: every rule above
is a structural obligation, not a token. **Identity should not be decided before
there is both authority and a need for an actual identity-bearing source.**

**VF-4 already exists as an artifact family**, registered by CDS-WP-019 with its own
maturity, evidence and gate. **It simply has no authorized technical token root and
no source-set identity.** A future root decision would **extend machine-readable
identity coverage to an existing family** — **it would not create a sixth family**,
and nothing here should be read as implying one.

## Deferred decisions

*(Deliberately open — DEC-S-032. Recording an item here **defers** it; it does not
decide, schedule, or authorize it.)*

| # | Open question | Destination |
| --- | --- | --- |
| 1 | **The concrete range vocabulary** — range names, the number of ranges, boundaries, and the VF-4 scale topology. **`WP021-D1` decided the *kind* of vocabulary, not the vocabulary**, and **DEC-S-133 excluded VF-4** from the per-scale topology decision | A separately authorized work package, under the value-selection discipline; **`CDS-WP-020A` may not invent one** |
| 2 | **Whether VF-4 acquires a technical root and source-set identity** — **`WP021-D2`, DEFERRED by the Human Maintainer** (2026-09-06); **the DEC-S-132 scope stays closed at five families** | A separate, future Human-Maintainer decision. **No Decision and no ADR exists for it** |
| 3 | The **grid, container and content-width taxonomy** and any named configuration — **not gated by `WP021-D1`, which is decided**; a separate vocabulary question (GC-8) | A separately authorized work package |
| 4 | Every **concrete value** — threshold, width, gutter, margin, column count, extent, measure, target dimension | A separately authorized value-authoring work package, under **VP-1 … VP-7**; **VP-3, VP-5, VP-6 and VP-7 are UNSATISFIED** |
| 5 | **Density levels and their number** | **VF-3**; values route to a separately authorized authoring work package |
| 6 | The **density, reflow and target-size interaction** | **CDS-WP-031** — it requires rendering evidence (**DA-6**) |
| 7 | The **Theme and Context Mechanism**, and **whether and how a Spatial Context composes with a Theme Resolution Context**. **`DEC-S-136` fixes only that they are separate** (CX-9) | **CDS-WP-022**, which **retains full authority** over that mapping |
| 8 | The **pattern strategy** — which layout a screen uses and what it becomes | **Layer 5**, pattern work; **CR-004 stays there** |
| 9 | **Named extension points** for a Product Profile — the set is **empty** | **CDS-WP-032** |
| 10 | **Document, page and presentation geometry standards** | Per-channel, with the accessibility profile each channel needs first (DEC-S-058) |
| 11 | **Validation implementation** for every requirement above | **CDS-WP-024**, with negative-fixture expansion in **CDS-WP-025** |
| 12 | **Rendering evidence** for every rendering-dependent obligation | **CDS-WP-031** |

## Explicit non-goals

1. **No value of any kind** — the full prohibition is stated under *What this
   document is not*.
2. **No range vocabulary.** The **response mechanism is decided** by `DEC-S-136`;
   **the vocabulary is not**, and no range name or count may be inferred.
3. **No identifier** — no range name, no VF-4 root, no `sourceSetId`, no
   `sourceRevision`. **`WP021-D2` is deferred**, and **VF-4 has no authorized
   technical token root or source-set identity.**
4. **No token source file, manifest, resolver, schema, validator rule, test, or
   fixture.**
5. **No theme mechanism, theme instance, context vocabulary, or default alias.**
6. **No pattern, screen composition, navigation model, or layout template.**
7. **No component, brand, or Product Profile**, and **no extension point**.
8. **No technology, framework, layout engine, query mechanism, or platform
   primitive.**
9. **No evidence, no maturity change, no risk accepted or closed, no claim, no
   conformance, no release, no tag, and no publication.**
10. **No risk entry** — the risk register stays at **98**, with **no `RISK-099`**.
    **At the CDS-WP-021 effectivity and closure milestones the effective Decision
    and ADR registers were 136 and 6**; **`DEC-S-136` and `ADR-0006` are
    effective** at the integration commit
    `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`, and **no `DEC-S-137` and no
    `ADR-0007` existed then — CDS-WP-021 created neither.** **The effectivity of
    `DEC-S-136` and `ADR-0006` created no value and no identifier.** **`DEC-S-137`
    and `DEC-S-138` later became effective, and `ADR-0007` `Accepted` and
    effective, at the Human-Maintainer exact-object integration commit
    `23914ecc48c1fb3cba5e3dab97a505589e821b6b`** of the reviewed CDS-WP-022 object,
    and are unrelated to `WP021-D2`; **the current effective Decision and ADR
    registers are 138 and 7.**
11. **No work package is activated** — **CDS-WP-021 itself activated no later work
    package**, and at its effectivity and closure milestones **`CDS-WP-020A`**,
    **CDS-WP-022**, **CDS-WP-023** and **CDS-WP-024** all remained `Planned`, not
    active, and not authorized. **CDS-WP-022 was later authorized by a separate,
    explicit Human-Maintainer act**, not by CDS-WP-021, and is **`AUTHORIZED` /
    `ACTIVE FOR EXECUTION`**, **integrated** at
    `23914ecc48c1fb3cba5e3dab97a505589e821b6b`, and **not closed** —
    **`CLOSED ≠ SUCCESSOR AUTHORIZED`**. **`CDS-WP-020A`**, **CDS-WP-023** and
    **CDS-WP-024** remain `Planned`, not active, and not authorized.

## Change control

*(Normative)*

This document is normative for the structure it defines **once it is effective**.
Changes require an authorized CDS work package, a Decision Index entry **where a
registered decision changes**, consistency updates across the dependent visual
foundation documents, Nova review, and Human-Maintainer approval.

A change that touches accessibility obligations, shared semantics, a Product
Profile, a breaking contract change, a claim, licensing, or publication is
**Elevated** (DEC-S-033) — **the trigger wins over the estimate.**

The adaptive foundation is not extended implicitly: not by a Skill, not by a
consumer request, not by an implementation convenience, not by a design tool, and
not by a generated artifact.

## Related documents

| Topic | Document |
| --- | --- |
| Visual foundation frame | [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md) |
| Spacing, sizing, layout, grid, responsive constraints | [Visual Foundation Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md) |
| Reference layer (token-flow layer 1) | [Visual Reference Token Foundation](VISUAL_REFERENCE_TOKEN_FOUNDATION.md) |
| Semantic layer (token-flow layer 2) | [Visual Semantic Token Foundation](VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) |
| Value-selection discipline | [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md) |
| Themes and presentation contexts | [Visual Foundation Theme Architecture](VISUAL_FOUNDATION_THEME_ARCHITECTURE.md) |
| Accessibility mapping | [Visual Foundation Accessibility Mapping](../governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md) |
| Channel mapping | [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md) |
| Governance and lifecycle | [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md) |
| Brand and Product Profile boundary | [Visual Foundation Brand and Product Profile Boundary](../governance/VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md) |
| Architecture frame and layers | [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) |
| Requirement traceability — **CR-004 stays at Layer 5** | [Architecture Requirements Traceability](ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md) |
| Accessibility requirements | [Accessibility Requirements Baseline](../governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md) · [WCAG 2.2 AA Applicability Matrix](../governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md) |
| Accessibility policy and evidence | [Accessibility and Inclusive Design Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) · [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) |
| **Adaptive spatial context and named ranges** (DEC-S-136) | [ADR-0006](../decisions/ADR-0006-ADAPTIVE_SPATIAL_CONTEXT_AND_NAMED_RANGE_ARCHITECTURE.md) — **`Accepted` and effective at `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`** |
| Identifier grammar and identity spaces | [ADR-0005](../decisions/ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md) |
| Representation and source identity | [ADR-0004](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md) |
| Channels and distribution | [Artifact Distribution and Channel Model](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) |
| Profiles and extensions | [Product Profile and Extension Model](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) |
| Authority and conflicts | [Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md) |
| Decisions · Risks | [Decision Index](../decisions/DECISION_INDEX.md) · [Risk Register](../risks/RISK_REGISTER.md) |
| Work package status | [Work Packages](../../project-system/WORK_PACKAGES.md) |
