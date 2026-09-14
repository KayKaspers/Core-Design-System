# Visual Foundation Theme Architecture

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Amended by:** CDS Step-9 Decision Integration Pass, 2026-09-05 — a new *Theme
  sequencing* section, to apply **DEC-S-135**. **That amendment is effective** at
  the Human-Maintainer exact integration commit
  `2cb244e889c1a6b5a278afb233995a0379b5d9ef` (2026-09-05). **It
  decides no theme mechanism, creates no theme and no context, and authorizes no
  work package**, and T-1 … T-10, the candidate contexts, and the Product Profile
  boundary are unchanged.
- **Amended by:** CDS-WP-022 — Theme and Environmental Presentation Model,
  2026-09-12 — the *Authority basis*, *Theme Resolution Context*,
  *Context admission contract*, *Context identity*,
  *Context selection and resolution entry*, *Environmental presentation inputs*,
  *Fail-closed conditions*, *Composition boundaries*, *Machine-readable boundary*
  and *Neutral / document classification* sections, the reconciled *Candidate
  contexts*, *open mechanism*, *Validation requirements*, *Evidence and claim
  boundary* and *Deferred decisions* sections, and the
  bounded *Open — Human-Maintainer decision required* section — **since replaced by
  *The Human-Maintainer decision package***. **CDS-WP-022 is
  `AUTHORIZED` / `ACTIVE FOR EXECUTION`** by a separate, explicit
  Human-Maintainer act. **This amendment decided no theme mechanism, admitted no
  context, created no theme, no context identifier, no default alias and no
  value, and authorized no work package.** **T-1 … T-10 and TS-1 … TS-6 are
  unchanged**, as are **TC-1 … TC-7**, **DEC-S-135** and **DEC-S-136**. **That
  amendment is effective** at the Human-Maintainer exact-object integration commit
  `23914ecc48c1fb3cba5e3dab97a505589e821b6b` (2026-09-12); **before that commit it
  was uncommitted executor output and changed no authoritative CDS state**.
- **Amended by:** CDS-WP-022 bounded decision rework, 2026-09-12 — applying the
  **Human-Maintainer decisions on `WP022-D1` … `WP022-D5`**: the new *Theme
  resolution mechanism* section (**TM-1 … TM-12**), the reconciled *Context
  selection and resolution entry* (**CS-8** decided, **CS-9 … CS-11** added),
  *Environmental presentation inputs* (**CE-5** decided), *Fail-closed conditions*
  (**CF-9** decided, **CF-11** added) and *Composition boundaries* (**CB-2**,
  **CB-6**), the reconciled *context set*, *high-contrast*, *open mechanism*,
  *Machine-readable boundary*, *Validation requirements*, *Evidence and claim
  boundary* and *Deferred decisions* sections, and the *Human-Maintainer decision
  package* section that replaces the open-decision section. **The decisions are
  recorded as `DEC-S-137` (with
  [ADR-0007](../decisions/ADR-0007-THEME-RESOLUTION-AND-CONTEXT-EVIDENCE-ARCHITECTURE.md),
  covering `DEC-S-137` only) and `DEC-S-138`.** All three are **`Accepted` and
  effective at the Human-Maintainer exact-object integration commit
  `23914ecc48c1fb3cba5e3dab97a505589e821b6b`**, which integrated the reviewed
  CDS-WP-022 object after a Fresh Independent Review, a bounded corrective rework, a
  confirmatory independent review and Nova final integration adjudication —
  **`APPROVED PROPOSITION ≠ EFFECTIVE REPOSITORY DECISION`** held until that
  commit. **The rework decides
  nothing of its own, creates no theme, no context identifier, no default alias and
  no value, and authorizes no work package**; **T-1 … T-10, TS-1 … TS-6,
  TC-1 … TC-7, DEC-S-131, DEC-S-132, DEC-S-135 and DEC-S-136 are unchanged.**
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for what a CDS theme is, what it may do, what makes a
  presentation context supported, how a context is represented and resolved, how a
  context is selected, and where resolution fails closed.** It defines **VF-9** as a
  contract and **creates no theme instance, no machine-readable context identifier,
  and no value**. **The theme mechanism is decided** by **`DEC-S-137`**, and the
  **context set, forced-colours disposition, selection precedence and fail-closed
  policy** by **`DEC-S-138`** — both **effective at the Human-Maintainer exact-object
  integration commit `23914ecc48c1fb3cba5e3dab97a505589e821b6b`**, and **not before**.
- **Maturity:** **`Proposed`** — this document promotes nothing.

## Purpose and boundary

This document defines **what a theme is in CDS**, where it sits, what it may
change, what it may never change, **what makes a presentation context supported,
how a context enters resolution, and where resolution fails closed**.

**It creates no theme.** No light theme, no dark theme, no high-contrast theme, no
print context, no context identifier, no default alias, and no theme value.

**The theme mechanism is decided — by the Human Maintainer, not by this document.**
CDS-WP-022 derived what followed uniquely from effective authority and **escalated
five normative choices it had no authority to invent**. The Human Maintainer decided
all five on 2026-09-12, and they are recorded as **`DEC-S-137`** (with
[ADR-0007](../decisions/ADR-0007-THEME-RESOLUTION-AND-CONTEXT-EVIDENCE-ARCHITECTURE.md))
and **`DEC-S-138`** — see *The Human-Maintainer decision package*. **`DERIVE ≠
DECLARE`**, and an authorized work package is **not** an executor authorized to
invent normative choices.

**Each recorded decision is normative repository authority only from its own
effectivity.** **`DEC-S-137`, `DEC-S-138` and `ADR-0007` are `Accepted` and effective
at the Human-Maintainer exact-object integration commit
`23914ecc48c1fb3cba5e3dab97a505589e821b6b`**, which integrated the reviewed CDS-WP-022
object.
**The effective register held 136 decisions and 6 ADRs until that commit and holds 138
and 7 from it.** Until it, **the supported Theme Resolution Context set was empty**;
from it, **it is `Light` and `Dark`, with no default**.

Frame: [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md) ·
[Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md).

Consumer anchor: **CR-025 — Light and dark themes** (*Could*, documented planned
capability, two consumers). **`COULD` ≠ `MUST`**, and a documented planned
capability is not a commitment.

## Authority basis

*(**Non-normative as a section**; every statement it indexes is normative where it
stands. Recorded so that each binding statement added by CDS-WP-022 can be checked
against the authority it applies, on the CDS-WP-019, CDS-WP-020 and CDS-WP-021
pattern. **No statement below is a new normative choice**, and **no Decision, ADR,
or risk entry is created on theme grounds.**)*

| What CDS-WP-022 records | Authority it applies |
| --- | --- |
| A theme is a named presentation / resolution context and not a sixth token-flow layer | DEC-S-024 · VF-I-1 · TS-5 · CX-8 · *Theme is not a layer* above |
| A theme re-binds and never redefines | DEC-S-135 · **T-1** · VF-I-9 · **TC-2** |
| Role identity and meaning are context-independent; a context is never a path segment | **T-8** · N-6 · SN-6 · **TC-1**, **TC-2** · DEC-S-132 clauses 5, 12 |
| Source Set identity carries no context or theme segment, and the namespace is flat | **DEC-S-131** clauses 1, 5 · **DEC-S-132** clauses 8, 10, 12 |
| Resolution takes a **requested context** as an input and introduces no value or meaning | [Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md) *Resolution order* step 3 · DEC-S-079 · [Machine-Readable Source Model](MACHINE_READABLE_SOURCE_MODEL.md) *Resolver and composition role* |
| Resolution is deterministic **given a context**, offline, and provenance-bound | **T-6**, **T-7**, **T-9** · DEC-S-030 · DEC-S-031 · DEC-S-080 · DEC-S-091 |
| No technology may be named as a selection mechanism | DEC-S-004 · DEC-S-032 · PN-4 · VE-5 · VF-I-13 |
| Accessibility obligations hold in every supported context and focus is never weakened | **T-3**, **T-4** · **TC-3**, **TC-4** · CR-2, CR-3 · VF-I-8 · F-4 · DEC-S-059 |
| Unsupported, unresolvable, obligation-breaking and provenance-less states fail closed with no automatic repair | DEC-S-023 · DEC-S-034 · **T-2** · **TC-7** · VF-I-11 · the *Fail-closed conditions* of the resolution model |
| A theme is not a Product Profile, not a brand, not a channel, and not a status | *Theme ≠ Brand ≠ Product Profile* and *Theme is not a channel* above · DEC-S-025 · DEC-S-029 · **T-5** · **TC-5** · SS-1 … SS-8 |
| A Spatial Context is not a Theme Resolution Context | **DEC-S-136** · **CX-9** · [ADR-0006](../decisions/ADR-0006-ADAPTIVE_SPATIAL_CONTEXT_AND_NAMED_RANGE_ARCHITECTURE.md) |
| A context is admitted only by an explicit Human-Maintainer decision, and admission is **Elevated** | DEC-S-033 · DEC-S-036 · [Governance Operating Model](../governance/GOVERNANCE_OPERATING_MODEL.md) · *The context set* below |
| Every supported context carries its own evidence, and evidence never transfers | DEC-S-052 applied · DEC-S-126 · AF-2 · RV-4 · *Evidence and claim boundary* below |

**Where a question could not be answered this way, it was not answered.** It was
escalated, and the Human Maintainer decided it. The statements those decisions add
rest on a **different** basis — Human-Maintainer authority, not derivation:

| What the decisions add | Authority |
| --- | --- |
| The **Resolver-Modifier Context mechanism** and the **context-evidence input binding** (**TM-1 … TM-12**) | **`DEC-S-137`** (**[ADR-0007](../decisions/ADR-0007-THEME-RESOLUTION-AND-CONTEXT-EVIDENCE-ARCHITECTURE.md)**, covering `DEC-S-137` only) — Human-Maintainer decision of 2026-09-12 resolving **`WP022-D1`** |
| The **initial supported context set** `Light` and `Dark`, **equal peers with no default** | **`DEC-S-138`** part A — resolving **`WP022-D2`** |
| **Forced colours as an environmental accessibility condition and not a Core context** | **`DEC-S-138`** part B — resolving **`WP022-D3`** |
| **Explicit viewer choice over inferred environment preference**, with mandatory platform accessibility conditions outside Theme precedence (**CS-8 … CS-11**) | **`DEC-S-138`** parts C and D — resolving **`WP022-D4`** |
| **No default and no fallback Theme**, fail closed, and `Not Applicable` (**CF-9**, **CF-11**) | **`DEC-S-138`** parts E, F and G — resolving **`WP022-D5`** |

**None of these five is a derivation, and none is presented as one.** Each is
**normative repository authority only from the effectivity of its Decision**, and
**not before**.

## What a theme is

*(Normative)*

> **A theme is a presentation context that re-binds semantic roles to primitives.
> It is not a layer, not a brand, not a profile, and not a channel.**

| A theme **is** | A theme **is not** |
| --- | --- |
| A named resolution context | A token-flow layer |
| A re-binding of role → primitive | A redefinition of what a role means |
| Composed in a defined, deterministic order | An ad-hoc override set |
| Applicable across products | A product identity |
| A presentation concern | A meaning concern |

## Theme Resolution Context

*(Normative — the precise term for the construct this document calls a theme)*

> **A Theme Resolution Context is a named presentation condition under which
> approved semantic roles resolve to approved primitives, without any change to
> what a role means or whether it exists.**

**"Theme" and "Theme Resolution Context" name the same construct.** The longer term
is used wherever the shorter one could be confused with a brand, a Product Profile,
a channel, or a **Spatial Context** — and **`SPATIAL CONTEXT ≠ THEME RESOLUTION
CONTEXT`** (**DEC-S-136**, **CX-9**).

**Environmental presentation** is the *category* of presentation condition that
arises from the circumstances under which an artifact is viewed rather than from
the artifact itself. It is a **category name, not a construct**: **no environmental
input kind, mode, or identifier is registered**, and **no input registry is created**
(**CE-1**). What CDS governs is an **abstract precedence between input classes**
(**CE-5**, **CS-8**, **CS-11**) and nothing about how an input is observed
(**CS-3**, **CS-9**).

> **A supported context is one CDS has decided to support. A candidate is one
> somebody has written down.** **`CANDIDATE ≠ SUPPORTED CONTEXT`.** **Supported
> contexts: 0 until `DEC-S-138` is effective; `Light` and `Dark`, with no default,
> from then** — see *The context set*.

## Theme is not a layer

*(Normative — an application of DEC-S-024)*

DEC-S-024 defines **exactly five** token-flow layers. A theme is **not** a sixth.

A theme is a **resolution context**: the Resolver / Composition document declares
how source sets and conditional modifiers combine, **in a defined order**, to
resolve a context. The resolver *"introduces no new value or meaning and does not
invert the downward dependency direction"*.

**Treating a theme as a layer is an architectural defect**, because a layer can
hold a decision and a context cannot. A context selects among approved values; it
never creates one.

## Theme ≠ Brand ≠ Product Profile

*(Normative — three different authorities that are routinely conflated)*

| | Theme | Brand | Product Profile |
| --- | --- | --- | --- |
| **What it is** | A presentation context | An identity | A governed, bounded variation artifact |
| **Architecture layer** | 3 — Foundations | 2 — Brand and Identity | 1 → 2 governance, applied at token-flow layer 4 |
| **Scope** | Applies **across** products | Expresses **who** something is | Applies to **one** product |
| **Who selects it** | Typically the **person viewing**, or their environment | CDS Layer 2 governance | CDS approval, applied by a consumer |
| **What it may change** | Which primitive a role resolves to | Identity expression within governance | Values at **named, approved** extension points |
| **What it may never change** | Role meaning, role existence, accessibility guarantees | Accessibility, shared semantics | Roles, semantics, accessibility, status truth |
| **Exists today** | **No** | **No** | **No — and none can be approved** |

**A theme is not a small Product Profile.** A profile expresses *which product this
is*; a theme expresses *under what conditions this is being viewed*. Collapsing
them produces a system where changing to dark mode is governed like a brand
decision, or where a product's identity silently changes with the ambient light.

## Theme is not a channel

*(Normative — a classification rule, because the two overlap)*

Print, documentation, and presentation are **registered channels** (Layer 6), not
themes. A "print theme" and the PDF channel are not the same construct, even where
they produce similar output.

> **A context that varies *within* a channel is a theme. A context that *is* a
> channel is channel scope.**

| Case | Classification |
| --- | --- |
| Light and dark within the product UI | **Theme** |
| High contrast within the product UI | **Theme** *(mechanism open — see below)* |
| A paginated report | **Channel** — PDF and reports |
| A slide deck | **Channel** — presentations |
| Long-form web documentation | **Channel** — documentation |
| Greyscale output of a paginated report | A **channel** condition, handled by the channel's degradation rules |

Consequence: a channel needs an **accessibility profile** before its artifacts may
reach Candidate or Stable (DEC-S-058); a theme does not create a new channel and
does not escape its channel's profile requirement.

## Theme constraints

*(Normative — binding on any theme mechanism CDS-WP-022 later chooses)*

| # | Constraint |
| --- | --- |
| **T-1** | **A theme re-binds; it never redefines** (VF-I-9). It may change which primitive a role resolves to. It may not change what the role means. |
| **T-2** | **A theme may not add or remove a role.** Every semantic role must resolve in every supported context — or the context **declares the limitation** (VF-I-11). A silently unresolved role is a fail-closed condition, not a fallback. |
| **T-3** | **A theme may not weaken an accessibility guarantee.** Every declared contrast obligation and every declared pairing must hold in **every** context (VF-I-8, CR-2, CR-3). |
| **T-4** | **A theme may never remove or weaken the focus indicator** (F-4). |
| **T-5** | **A theme is never a meaning carrier.** Nothing may be communicated by *which theme is active*, and no status, state, or severity may be expressed by a theme difference (VF-I-5, VF-I-6). |
| **T-6** | **Theme resolution is deterministic**: the same source revisions plus the same resolver plus the same context yield the same resolved result (DEC-S-080). |
| **T-7** | **Theme resolution is offline.** No context may require an external runtime service to resolve (DEC-S-030, invariant 12). |
| **T-8** | **Theme is a resolution input, not a path segment.** A theme name never appears inside a shared semantic identifier (N-6). |
| **T-9** | **A theme carries provenance.** Any generated per-theme output identifies its source revision, transformation revision, and resolved context (DEC-S-031). |
| **T-10** | **A theme is not a place to fix a core gap.** If a role only works in one context, the role is wrong — raise it, do not paper over it with a context (anti-fragmentation rule 3, applied). |

## Theme sequencing

*(Normative — **DEC-S-135**, CDS Step-9 Decision Integration Pass, 2026-09-05.
**Effective** at the Human-Maintainer exact integration commit
`2cb244e889c1a6b5a278afb233995a0379b5d9ef`. It **decides no
theme mechanism** — that remains CDS-WP-022's and is untouched. **No ADR** —
DEC-S-135 is deliberately not an architecture dependency of ADR-0005.)*

| # | Rule |
| --- | --- |
| **TS-1** | **No semantic visual role carries a default alias to a reference primitive before CDS-WP-022 decides the Theme and Context Mechanism.** |
| **TS-2** | **CDS-WP-022 precedes context-sensitive value selection.** |
| **TS-3** | **Context-independent work is not blocked.** Identifier grammar, scale ownership and topology rules, role admission policy, family maturity governance, and **source-set structural identity** are context-independent by **TC-1**, **TC-2**, **T-8**, **N-6** and **RB-1**. |
| **TS-4** | **`CDS-WP-022 BEFORE VALUE SELECTION` does not mean `CDS-WP-022 BEFORE EVERY SOURCE-STRUCTURE OR IDENTITY ACTIVITY`.** Declaring a source set's identity is a structural act; what TS-2 gates is its **content**. |
| **TS-5** | **A theme remains a Resolution Context and is not a sixth token-flow layer** (DEC-S-024), and **A THEME RE-BINDS; IT NEVER REDEFINES** (T-1, VF-I-9). **TC-6 continues to bind independently of this rule.** |
| **TS-6** | **This authorizes no work package.** CDS-WP-022 is the recommended and sequenced Step-10 candidate only — **SEQUENCED NEXT ≠ AUTHORIZED** — and it remains `Planned`, not active, and not authorized, as do `CDS-WP-020A` and CDS-WP-021 … CDS-WP-053. |

**Why the rule exists.** **T-2 is vacuously satisfiable today** — zero contexts are
supported — so it cannot judge whether a single default binding is a legitimate
starting state. A default binding taken now would silently become *the light theme*
and hand CDS-WP-022 a decision it exists to make, satisfying **TC-6** in form while
violating it in substance. The evidence cost is decisive: a value selected before
the context model and re-selected after it produces a new source revision, and **a
new revision inherits no evidence and no admission** (AF-2, RV-4, DEC-S-126,
DEC-S-131 clause 10).

## Theme resolution mechanism

*(Normative — **`DEC-S-137` — Theme Resolution and Context-Evidence Architecture**,
Human-Maintainer decision of 2026-09-12 resolving **`WP022-D1`**.
**[ADR-0007](../decisions/ADR-0007-THEME-RESOLUTION-AND-CONTEXT-EVIDENCE-ARCHITECTURE.md)**
carries the rationale and covers **`DEC-S-137` only**. **`Accepted` and effective at
the Human-Maintainer exact-object integration commit
`23914ecc48c1fb3cba5e3dab97a505589e821b6b`.**
**No source, schema, validator, resolver instance, context identifier, or value is
created.**)*

> **A Theme Resolution Context is a Resolver / Composition input. Theme- and
> context-sensitive binding is represented through the existing Resolver /
> Composition architecture over the existing Source-Set graph — and nothing else in
> the architecture moves to accommodate it.**

| # | Rule |
| --- | --- |
| **TM-1** | **A Theme Resolution Context is a Resolver / Composition input.** Resolution is performed **for a requested context** (**CS-1**), through the **DTCG Resolver Module 2025.10** construct the machine-readable architecture already assigns to multi-context composition, in a **defined order** over the **declared** source-set graph. |
| **TM-2** | **A Theme is never a token-flow layer.** Exactly five layers exist (DEC-S-024, TS-5, VF-I-1); **no Theme, Environment, Context, or Mode layer is created.** |
| **TM-3** | **A Theme is never a token-path segment** (**CI-2**, T-8, N-6, SN-6, TC-1). A context-qualified role path is not a theme mechanism — it is a **different role**, which **T-2** forbids. |
| **TM-4** | **A Theme is never a Source-Set identity segment** (**CI-3**). The namespace stays flat **`<layer>/<family>`** with **no `context` or `theme` segment at any position** (DEC-S-132 clauses 8 and 12). |
| **TM-5** | **No per-context Source Set is created.** **One** source set per independently evaluable **Family × Token-Flow-Layer** unit remains the topology (DEC-S-131 clause 5), and the ten identities `reference/color` … `semantic/surface` stay **closed** (DEC-S-132 clause 10). |
| **TM-6** | **The Source Set remains the sole independently evaluable maturity unit.** Evaluation, evidence, maturity and approval attach there **and nowhere else** (DEC-S-131 clause 1), and **no maturity propagation exists in either direction** (clause 11). |
| **TM-7** | **Context-specific evidence remains revision-bound to (`sourceSetId`, `sourceRevision`)** and additionally records, as **exact evidence inputs**, the **Resolver / Composition revision** and the **Theme Resolution Context**. |
| **TM-8** | **A Resolver / Composition document is never a maturity carrier.** Recording it as an evidence **input** confers **no** maturity on it — **`AGGREGATED is not MATURE`**, and an artifact that *"introduces no new value or meaning"* (DEC-S-079) has nothing of its own to be mature about. **`EVIDENCE INPUT ≠ MATURITY CARRIER`.** |
| **TM-9** | **Any evidence-relevant change invalidates or supersedes the affected context-specific evidence** — a change to a Source Set revision, to the Resolver / Composition revision, or to the Theme Resolution Context. The affected evidence is not merely stale: **it no longer evidences the thing that now exists.** |
| **TM-10** | **Evidence never transfers automatically** — not between revisions, not between contexts, not between channels, not between artifacts (DEC-S-126, DEC-S-052, AF-2, RV-4). |
| **TM-11** | **Theme Resolution Context and Spatial Context are orthogonal** (**CB-2**, **CX-9**, DEC-S-136). **No Spatial Context is a Theme modifier, a Theme selector, or a Theme-resolution input**, and **no Theme Resolution Context classifies spatial geometry**, changes an Adaptation Container, changes a responsive range, or creates a threshold. |
| **TM-12** | **Joint Theme × Spatial rendering and evidence evaluation is deferred** to separately authorized future scope. It is an **evidence-design** question, unanswerable without rendering evidence that does not exist (CDS-WP-031). **Deferring it is safe because TM-11 fixes the representation.** |

**Why the mechanism is this and not one of the four alternatives.** A **Product
Profile** mechanism was already excluded by the classification above; a
**per-context token path** by TM-3; a **per-context Source Set** by TM-5; and making
the **Resolver a second maturity unit** by TM-6 and TM-8. **The chosen architecture
is the only one of the five that amends nothing** — DEC-S-131, DEC-S-132, DEC-S-135
and DEC-S-136 all stand unchanged. Full reasoning:
[ADR-0007](../decisions/ADR-0007-THEME-RESOLUTION-AND-CONTEXT-EVIDENCE-ARCHITECTURE.md).

**The evidence consequence is stricter, not looser.** **TM-9** makes a resolver
revision or a context change invalidate affected evidence. That is the price of
keeping exactly one evaluable unit, and it is paid deliberately.

**The DEC-S-135 gate.** **`DEC-S-135` is unchanged in byte and in substance**, and
**TS-1 … TS-6 are untouched.** From the effectivity of `DEC-S-137` and `DEC-S-138`
the Theme and Context Mechanism is decided, so **the DEC-S-135 sequencing condition
— *CDS-WP-022 precedes context-sensitive value selection* — is satisfied with
respect to the theme-mechanism question**; until that effectivity it is not.
**`THEME GATE SATISFIED ≠ VALUE SELECTION AUTHORIZED`** and **`THEME GATE SATISFIED
≠ CDS-WP-020A AUTHORIZED`**: **no work package is authorized to select a visual
value**, **VP-3, VP-5, VP-6 and VP-7 stay `UNSATISFIED`**, and **`CDS-WP-020A`
remains `Planned`, not active, and not authorized.** **TS-1 is satisfied by
compliance, not by exemption** — **no semantic role carries a default alias**, and
**`DEC-S-138` part E creates none.**

**`WP021-D2` is untouched and unrelated.** **No relation exists between approving
`WP022-D1` and resolving `WP021-D2`**: VF-4 acquires no technical root and no
source-set identity, `sourceSetId` and `sourceRevision` remain **NONE**, and **no
range name, range count, or threshold is created.**

## Context admission contract

*(Normative — **CDS-WP-022**, 2026-09-12. It states **what a decision to support a
context must be able to affirm**. **It admits no context**, and **zero contexts are
supported.**)*

| # | Rule |
| --- | --- |
| **CA-1** | **A supported Theme Resolution Context is declared, named, and enumerable.** An unnamed or inferred condition is not a context, because provenance must identify the resolved context (**T-9**, DEC-S-031) and nothing unnamed can be identified. |
| **CA-2** | **A context becomes supported only by an explicit Human-Maintainer decision.** Listing a candidate, describing one, or benchmarking one admits nothing. Neither Nova nor Claude may admit a context, and **no document, metadata field, validator pass, or renderer admits one** (VF-I-14 applied). |
| **CA-3** | **A context varies *within* a channel; it never *is* a channel.** The classification rule above is the test. A condition that *is* the channel is channel scope at Layer 6, and a context creates no channel and escapes no channel's accessibility-profile requirement (DEC-S-058). |
| **CA-4** | **A context applies across products.** A presentation condition needed by exactly one product is not a Core context: cross-product scope belongs to a theme and single-product scope to a Product Profile, and **a Product Profile may never define a context.** A single-product need therefore has **no route** to become a Core context. |
| **CA-5** | **A context carries no meaning** (**T-5**, **TC-5**). Nothing may be communicated by *which context is active*, and no `condition`, `severity`, `confidence`, `freshness`, or `evidence` value may be expressed by a context difference (VF-I-5, VF-I-6). |
| **CA-6** | **Every semantic role resolves in every supported context, or the context declares the limitation** (**T-2**, **TC-7**, VF-I-11). A silently unresolved role is a fail-closed condition, never a fallback. |
| **CA-7** | **Every declared contrast obligation and every declared pairing holds in every supported context** (**T-3**, **TC-3**, CR-2, CR-3, VF-I-8). A context in which they do not hold is **not a context change — it is a contract break**. |
| **CA-8** | **Focus visibility survives every context** (**T-4**, **TC-4**, F-4). There is **no permitted mechanism of removal** — not by a context, a profile, an exception (DEC-S-059), or a consumer override. |
| **CA-9** | **A context resolves deterministically, offline, and with provenance** (**T-6**, **T-7**, **T-9**, DEC-S-030, DEC-S-080, DEC-S-091, DEC-S-031). `latest` is not an identity. |
| **CA-10** | **A context is not a place to repair a Core gap** (**T-10**). If a role works in only one context, **the role is wrong** — raise it. |
| **CA-11** | **Each supported context carries its own evidence, and evidence never transfers between contexts.** A future light-context evidence package evidences **nothing** about a dark context, exactly as evidence transfers between neither channels (DEC-S-052) nor source revisions (DEC-S-126, AF-2, RV-4). **Admitting a context creates an evidence obligation, never an accessibility claim.** |
| **CA-12** | **Admitting a context is an Elevated change** (DEC-S-033). It bears on accessibility obligations and on what a consumer may rely on, and **ceremony scales while obligations do not**. |
| **CA-13** | **A context count is never presupposed.** No CDS artifact may be written so that it only works if exactly one, exactly two, or exactly three contexts exist (**TC-6**). A contract that requires a count **has decided the context set by implication**. |

> **CA-1 … CA-13 are satisfiable by zero contexts, and that is the current state.**
> The contract exists so that a future admission can be judged against something,
> exactly as T-1 … T-10 exist so that a future mechanism can be.

## Context identity

*(Normative — **CDS-WP-022**, 2026-09-12. **No context identifier is created,
adopted, reserved, or recommended.**)*

| # | Rule |
| --- | --- |
| **CI-1** | **A context is identified by a declared context identifier**, held in the resolution declaration and nowhere else. Identity is **declared, never derived** from a path, a file name, a directory, or a tool convention — the rule DEC-S-131 clause 3 and DEC-S-132 clause 7 already impose on a `sourceSetId`. |
| **CI-2** | **A context identifier never appears in a token path.** The **same** role identifier is used in every context (**T-8**, N-6, SN-6, **TC-1**). A context-qualified role path is not a theme mechanism — it is a different role, which **T-2** forbids. |
| **CI-3** | **A context identifier never appears in a Source Set identifier.** The source-set namespace is flat **`<layer>/<family>`** and introduces **no `context` or `theme` segment at any position** (**DEC-S-132** clauses 8 and 12). |
| **CI-4** | **A context is not a token-flow layer, and never becomes one by acquiring a segment.** Exactly five layers exist (DEC-S-024); the layer stays the declared `layer` field (**DEC-S-132** clause 5), and **no Theme, Environment, Context, or Mode layer exists** (TS-5, VF-I-1, CX-8). |
| **CI-5** | **A context identifier follows the CDS technical identifier profile** (DEC-S-081) and is **separate from any display label** (DEC-S-110). It carries **no product, brand, customer, or consumer term** (N-2), and it may **not name a channel or a Product Profile** — doing so would assert the conflation this document's classification prohibits. |
| **CI-6** | **A context rename is an identity and migration event** (DEC-S-082, DEC-S-040), and **any evidence bound to the renamed context is invalidated** — the same consequence a `sourceSetId` rename carries (DEC-S-131 clauses 15 and 17). |

**No concrete context identifier exists.** **`Light` and `Dark` are the two supported
Core Theme Resolution Contexts under `DEC-S-138` part A — from that decision's
effectivity and not before — and they are human-readable architectural names, not
machine-readable identifiers**; **naming a context in prose creates none**
(VF-I-13, `DEC-S-138` part A clause 4). `high-contrast`,
`forced-colors`, `neutral` and `document` are **words this document uses to describe
dispositioned candidates** — not identifiers, not reservations, and not
recommendations. **Authoring a machine-readable context identifier is `CDS-WP-020A`'s,
under its own separate authorization**, and any **further** naming constraint on one
is decided there under **CI-1 … CI-6** and the CDS identifier profile.

## Context selection and resolution entry

*(Normative — **CDS-WP-022**, 2026-09-12)*

| # | Rule |
| --- | --- |
| **CS-1** | **Resolution takes a requested context as an input.** The resolution order applies the Resolver / Composition document's modifiers *"in their defined order **for the requested context**"* — so a context is **supplied to** resolution and is **never a property of a token**. |
| **CS-2** | **CDS resolves for a context; it does not perform the act of selecting one.** Selection is exercised by the **person viewing, their environment, or the consumer** (*Who selects it*, above). **CDS holds no runtime**, and **no CDS artifact class is a runtime** — the eight source-set classes are sources, manifests, resolvers, generated outputs and evidence records, and none of them observes a viewer. |
| **CS-3** | **No CDS normative source names the mechanism by which a selection is observed.** No CSS feature or media feature, DOM construct, browser or operating-system API, JavaScript, framework, or design tool is named or presupposed (DEC-S-004, DEC-S-032, PN-4, VE-5). A technology-specific illustration is an **example** and never normative (VF-I-13). |
| **CS-4** | **Resolution is deterministic given a context** (**T-6**, DEC-S-080): the same source revisions plus the same resolver plus the same context yield the same resolved result. **`DETERMINISTIC RESOLUTION ≠ DETERMINISTIC SELECTION`** — **T-6 conditions determinism on a context already given**, and therefore states **nothing** about how a context is chosen. |
| **CS-5** | **Resolution is offline** (**T-7**, DEC-S-030, DEC-S-091). No context may require an external service, registry, or network reference **to resolve**. A selection signal observable only online may exist outside CDS; it may never be a condition of resolvability. |
| **CS-6** | **Resolution introduces no value and no meaning.** A context **selects and layers approved values** and honours the downward dependency direction (DEC-S-079, **T-1**). A resolved value that no source set holds is a defect, not a context. |
| **CS-7** | **Every resolved output identifies the context it was resolved for** (**T-9**, DEC-S-031, DEC-S-080, TB-7), together with its source and transformation revisions. An output that cannot identify its context is **fail-closed**, because an artifact whose origin cannot be established becomes functionally normative (RISK-025). |
| **CS-8** | **CDS constrains selection precedence without owning the runtime.** *(**`DEC-S-138`** part C, resolving **`WP022-D4`**; normative from that decision's effectivity.)* **Within Theme selection, an explicit viewer choice takes precedence over an inferred environment preference**, and **an inferred environment preference may select a supported Core Theme only when no explicit viewer choice exists.** **`THEME SELECTION ≠ THEME RESOLUTION`**: the consumer or runtime **selects**, the CDS resolver **resolves**. |
| **CS-9** | **The consumer or runtime owns the sensing, persistence and transport of selection inputs.** CDS defines the **obligation**, never the **mechanism** — **no technology-specific selector or runtime is defined or implemented** (**CS-3**). |
| **CS-10** | **No CDS normative token artifact stores viewer state or environment state.** A source, manifest, resolver or generated output is a value, relationship and metadata document; adding viewer or device information to one would make it a personal-data artifact CDS neither governs nor is scoped to hold (**CE-4**). |
| **CS-11** | **Mandatory platform accessibility conditions are outside Theme precedence and remain binding regardless of the selected Theme.** They are **not** modelled as a higher or lower Theme priority, because **they are not Themes** — see *The forced-colours disposition*. |

> **The boundary is narrow and deliberate.** CDS owns **what a context is**, **what
> resolving for one must guarantee**, and **which selection input outranks which**.
> It does not own **the moment of choosing**, and it cannot: owning that would
> require naming technology (**CS-3**) or holding runtime state (**CS-2**, **CS-10**),
> and **both are prohibited**.

> **Determinism did not compel CS-8.** **T-6 conditions determinism on a context
> already given** (**CS-4**), so the precedence rule is a **deliberate policy
> addition by Human-Maintainer authority**, not a derived consequence — recorded as
> such rather than dressed up as an inference.

## Environmental presentation inputs

*(Normative as a boundary. **No input kind is registered, and none is created.**)*

An **environmental presentation input** is any circumstance of viewing that could in
principle cause a context to be requested — a person's expressed preference, a
platform or operating-system condition, an ambient condition, an
assistive-technology setting, or a consumer's or channel's own constraint.

| # | Rule |
| --- | --- |
| **CE-1** | **This document registers no environmental input kind**, and naming a category in the paragraph above registers nothing (VF-I-13). |
| **CE-2** | **An environmental input is never a meaning carrier** (**T-5**, **CA-5**). Nothing about a person or their environment may be communicated by which context resolves. |
| **CE-3** | **An environmental input is never a token-path segment, a Source Set segment, or a layer** (**CI-2** … **CI-4**). |
| **CE-4** | **No CDS artifact records, stores, transmits, or profiles an environmental input.** CDS sources, manifests, resolvers and generated outputs are value, relationship and metadata documents; adding viewer or device information to one would make it a personal-data artifact CDS neither governs nor is scoped to hold. |
| **CE-5** | **CDS declares an abstract precedence, not an input registry.** *(**`DEC-S-138`** parts B, C and D.)* Two classes are distinguished and neither is enumerated: an **explicit viewer choice** and an **inferred environment preference**, ordered by **CS-8**; and a **mandatory platform accessibility condition**, which is **outside Theme precedence and always binding** (**CS-11**). **Forced colours and platform high contrast belong to the third class and are not a Theme Resolution Context.** |

> **An environment is not a context.** An environmental condition may *cause* a
> context to be requested; it is never itself the context, and CDS resolves only
> what is requested (**CS-1**).

## Fail-closed conditions

*(Normative — **CDS-WP-022**, 2026-09-12, applying DEC-S-023, DEC-S-034 and the
resolution model's own fail-closed list. **No automatic repair exists.**)*

| # | Condition | Outcome |
| --- | --- | --- |
| **CF-1** | A **requested context that is not a supported context** | **Fail closed.** No substitution, no nearest match, no silent fallback — substituting another context would be an **automatic repair**, and no automatic repair exists (DEC-S-023). |
| **CF-2** | A **role that cannot resolve** in a requested supported context | **Fail closed**, and the limitation is **declared** (**T-2**, **TC-7**, VF-I-11). |
| **CF-3** | A resolution that would **break a declared contrast obligation or pairing** | **Fail closed** (**T-3**, **TC-3**). It is a contract break, not a context. |
| **CF-4** | A resolution that **removes or weakens a focus role** | **Fail closed** (**T-4**, **TC-4**, F-4, DEC-S-059). |
| **CF-5** | A context whose resolution is **non-deterministic or externally dependent** | **Fail closed** (**T-6**, **T-7**). |
| **CF-6** | A resolved output with **no declared context provenance** | **Fail closed** (**T-9**, TB-7, DEC-S-031). |
| **CF-7** | A **profile override reaching a value through a context** it may not override directly | **Fail closed** (DEC-S-025, and the Product Profile prohibition below). |
| **CF-8** | A context identifier appearing **in a token path or a Source Set identifier** | **Fail closed** (**CI-2**, **CI-3**, **T-8**, N-6, DEC-S-132 clause 12). |
| **CF-9** | **A Theme-applicable resolution with no explicitly selected supported context** | **Fail closed.** *(**`DEC-S-138`** parts E and F, resolving **`WP022-D5`**.)* **A Theme-applicable resolution requires an explicitly selected supported Theme Resolution Context**; **CDS defines no default Theme, no resolver-level default Theme, and no semantic default reference alias.** **Absence of a supported context is not a licence to guess one.** |
| **CF-10** | A **conflict between a class-1 meaning source and a class-2 value source** about a context | **Fail closed and escalate** (DEC-S-034). The affected artifact state is invalidated, **blocking precedes diagnosis**, and **recency never resolves it** (DEC-S-023). |
| **CF-11** | An **unresolved conflict between equal-authority selection inputs** | **Fail closed.** *(**`DEC-S-138`** part F.)* Where **CS-8**'s precedence cannot resolve the conflict, resolution **stops**; it does not pick one. |

> **`FAIL CLOSED ≠ DEGRADED OUTPUT`.** A fail-closed state **blocks transformation
> and distribution** until it is corrected at the source. It does not ship a partial
> result, a nearest-match context, or a best-effort resolution.

**There is no silent substitution** — not to `Light`, not to `Dark`, and not to any
other context (**`DEC-S-138`** part F). **No automatic repair exists** (DEC-S-023).

### Not Applicable

*(Normative — **`DEC-S-138`** part G, from that decision's effectivity)*

A flow or channel **where Theme resolution is genuinely not applicable** records
**`Not Applicable`**.

| # | Rule |
| --- | --- |
| 1 | **`Not Applicable` is a declared inapplicability**, recorded in the artifact's own record, and part of that artifact's evidence rather than a footnote to it. |
| 2 | **`Not Applicable` is not a hidden Theme, not a fallback Theme, and not a default Theme.** |
| 3 | **Declaring it is never a way to avoid a fail-closed condition that does apply.** Where Theme resolution **is** applicable and no supported context is selected, **CF-9** governs — not this. |
| 4 | It is the same honesty rule the channel model already uses: **`Reduced` and `Unsupported` are honest outcomes; silently dropping a distinction is the failure** (VF-I-11). |

## Composition boundaries

*(Normative — **CDS-WP-022**, 2026-09-12. Each rule applies an authority already in
force; **none re-owns anything, and none activates anything.**)*

| # | Boundary |
| --- | --- |
| **CB-1** | **Theme × Channel.** The within-channel rule stands unchanged (**CA-3**). Channel outputs may differ in **form** and never in **meaning** (DEC-S-029, PN-3), and the [Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md) VF-9 row is unchanged: in **PDF and reports** a greyscale or monochrome condition is **a channel condition, not a theme**, and in **repository presentation** VF-9 is **`Unsupported`** because rendering is viewer- and platform-controlled. **No channel adapter, profile, or degradation rule is created.** |
| **CB-2** | **Theme × Spatial Context — orthogonal, and decided so.** **`SPATIAL CONTEXT ≠ THEME RESOLUTION CONTEXT`** (**DEC-S-136**, **CX-9**, and **`DEC-S-137`** clauses 11 and 12, **TM-11**). A spatial context **describes the space an artifact is composed into** (CX-1) and **never re-binds a role**; a Theme Resolution Context **re-binds a role** (**T-1**) and **never classifies space**. **No spatial context is a Theme modifier, a Theme selector, or a Theme-resolution input**, and **no Theme classifies spatial geometry**, changes an Adaptation Container, changes a responsive range, or creates a threshold. **Joint Theme × Spatial rendering and evidence evaluation is deferred to separately authorized future scope** (**TM-12**). **DEC-S-136, AC-1 … AC-6 and RR-1 … RR-6 are unchanged**, **`WP021-D2` is unchanged**, and **no range name, range count, or threshold is created.** |
| **CB-3** | **Theme × Product Profile.** Unchanged, and restated because it is the boundary most often crossed by accident: a profile may override a value **within** a context at a **named, approved** extension point and may **select among** Core-supported contexts; it may **never** define, remove, or redefine a context, weaken an obligation, or reach through a context to a value it may not override directly. **No extension point is named** (CDS-WP-032), **no Product Profile exists, and none can be approved.** A profile selecting among contexts is **not** a context decision and **activates no profile**. |
| **CB-4** | **Theme × Semantic role identity.** **TC-1 … TC-7 hold unchanged.** Identity and meaning are context-independent, an obligation is declared once and holds in every context, and **the semantic layer presupposes no context count and no context set** (**TC-6**, **CA-13**). **No role, role name, role count, or role vocabulary is created** — **`THEME MECHANISM ≠ ROLE VOCABULARY`**, and **VP-6 remains `UNSATISFIED`**. |
| **CB-5** | **Theme × Semantic Status.** **COLOUR ≠ STATUS · ICON ≠ STATUS · MOTION ≠ STATUS · ELEVATION ≠ STATUS**, and a **context difference is never a status difference** (**T-5**, **TC-5**, SS-1 … SS-8). The status-to-visual binding is **CDS-WP-023's**, gated by CDS-WP-024 and CDS-WP-025. **`AE1-CDS-WP016-SEMSTATUS-004` does not transfer** to any theme or visual artifact, and the status family's source, revision, maturity, approval and evidence are **untouched**. |
| **CB-6** | **Theme × Source Set — answered.** Maturity and evidence attach to a **Source Set** and nowhere else (**DEC-S-131** clause 1), **one per Family × Token-Flow-Layer unit** (clause 5), with the ten identities `reference/color` … `semantic/surface` fixed as **identifier authority** and a **flat namespace carrying no `context` or `theme` segment** (**DEC-S-132** clauses 8, 10, 12). **Where a context-conditional binding lives and which unit carries its evidence is decided by `DEC-S-137`**: the binding is expressed through the **Resolver / Composition** architecture, and the context and resolver revision are recorded as **exact evidence inputs** of evidence that stays bound to (`sourceSetId`, `sourceRevision`) — **TM-1, TM-5 … TM-10**. **No eleventh source-set identity, no context namespace segment, and no context path segment is created**, and **DEC-S-131 and DEC-S-132 are unchanged.** |
| **CB-7** | **Theme × Token-flow layers.** Exactly **five** layers (DEC-S-024): Reference → Semantic → Component → Product Profile Overrides → Channel or Platform Outputs. A context is a **resolution context**, not a sixth layer, and **the Component layer is never dropped** from the flow. |

## The context set

*(Normative — **`DEC-S-138`** part A, Human-Maintainer decision of 2026-09-12
resolving **`WP022-D2`**. **`Accepted` and effective at the Human-Maintainer
exact-object integration commit `23914ecc48c1fb3cba5e3dab97a505589e821b6b`.** The table was previously a register of **candidates for
evaluation**; it now records the decided disposition of each. **No value, token
binding, Source Set, resolver instance, evidence, maturity, claim, or conformance is
created.**)*

| Context | Consumer evidence | Disposition |
| --- | --- | --- |
| **Light** | CR-025 (*Could*, two consumers, documented planned capability) | **Supported Core Theme Resolution Context** — from the effectivity of `DEC-S-138`, and not before. **Equal peer with `Dark`; not the default.** |
| **Dark** | CR-025, as above | **Supported Core Theme Resolution Context** — from the effectivity of `DEC-S-138`, and not before. **Equal peer with `Light`; not the default.** |
| **High contrast / forced colours** | **No consumer requirement.** Derived from Accessibility Requirements Baseline **3.5** — *"forced-colors and high-contrast conditions remain usable"* (Implementation-dependent) | **Not a Core Theme Resolution Context.** It is an **environmental accessibility condition** that supported consumers and outputs must honour, **binding independently of the selected Theme** — see below. |
| **Neutral / document** | No consumer requirement | **Not a Core Theme Resolution Context — answered by existing authority, no new Decision required.** Its named manifestations are **channel scope**; see below. |

**Print and presentation are deliberately absent from this table** — they are
channels, per the classification rule above.

| # | Rule |
| --- | --- |
| 1 | **`Light` and `Dark` are the initial supported Core Theme Resolution Contexts**, and **the set is exactly those two** until a further Human-Maintainer decision changes it under **CA-1 … CA-13**. **Supported contexts: 2 from the effectivity of `DEC-S-138`, and 0 before it.** |
| 2 | **They are equal peers.** Neither has higher Core authority than the other, and **neither is the default** — **no default exists** (**CF-9**, `DEC-S-138` part E). |
| 3 | **`Light` and `Dark` here are human-readable architectural names, not machine-readable identifiers.** **No machine-readable context identifier instance is authored**, and **naming a context in prose creates none** (VF-I-13, **CI-5**). Authoring one is **`CDS-WP-020A`**'s, under its own separate authorization. |
| 4 | **Admission creates no value.** No colour, typography, spacing, shape, surface, or theme value; **no token binding**; **no Source Set**; **no resolver instance**; **no evidence**; **no maturity**; **no claim**; **no conformance**. **A supported context is a declared presentation condition, not a rendered one.** |
| 5 | **Each supported context carries its own evidence** (**CA-11**, **TM-7**, **TM-10**), and **a future `Light` evidence package evidences nothing about `Dark`.** **Admitting a context creates an evidence obligation, not evidence** — **every theme artifact is AE-0.** |
| 6 | **`COULD` ≠ `MUST`, and this was a priority decision.** CR-025 is **`Could`** priority, a *documented planned capability*, status **Open**. Effective authority compelled neither admitting nor refusing the pair; the Human Maintainer chose to admit both. |
| 7 | **The count is decided, never presupposed.** **TC-6** and **CA-13** continue to bind: **no artifact may be written so that it only works if exactly two contexts exist**, and a third or a removal remains a normal decision under **CA-2**. |

### The forced-colours disposition

*(Normative — **`DEC-S-138`** part B, Human-Maintainer decision of 2026-09-12
resolving **`WP022-D3`**, from that decision's effectivity. **No evidence, no
conformance, and no claim.**)*

Baseline 3.5 requires that artifacts **remain usable** under forced colours and
platform high contrast. That obligation holds **whether or not CDS ships a
high-contrast theme** — and CDS-WP-019 recorded three admissible readings: ship a
CDS context, ship none and honour the platform's, or both with a declared precedence.

**The Human Maintainer chose the second: a platform condition, and no CDS Core
High-Contrast Theme Resolution Context at this stage.**

| # | Rule |
| --- | --- |
| 1 | **CDS introduces no separate Core High-Contrast Theme Resolution Context at this stage.** |
| 2 | **Forced colours and platform high contrast are an environmental accessibility condition**, not a Theme Resolution Context. |
| 3 | **Supported consumers and outputs must honour that condition**, and the obligation **remains binding independently of which Theme Resolution Context is selected** (**CS-11**). |
| 4 | **Forced colours is not** a Theme Resolution Context, a token-flow layer, a semantic role, a Product Profile, or a meaning carrier. **It is never modelled as a higher or lower Theme priority, because it is not a Theme** — **CS-11**, not **CS-8**. |
| 5 | **This is an architecture obligation only.** It is **not** evidence, **not** evidence admission, **not** WCAG conformance, **not** an accessibility claim, and **not** an AE-level award. **A target is not a claim** (DEC-S-050) and **an automated check is never evidence** (DEC-S-053). |
| 6 | **What makes forced colours survivable is the non-colour rule, not a theme.** **Colour is never the sole carrier of meaning** in any channel (VF-I-5, CR-006, 1.4.1, baseline 3.6), and position or proximity alone carries nothing (1.3.3, baseline 3.7). Those bind today. |
| 7 | **A future dedicated CDS High-Contrast Theme requires separate Human-Maintainer authorization and its own governance.** It is **deferred, not permanently rejected**, and **CA-1 … CA-13 would apply to it unchanged** — including **CA-7**, **CA-8** and **CA-11**. |

> **`ACCESSIBILITY OBLIGATION ⇏ CDS SHIPS A HIGH-CONTRAST THEME`.** Baseline 3.5
> bound under **all three** readings, so it could not select among them. Choosing was
> a Human-Maintainer act, and reading the obligation as the choice would have been
> deciding **`WP022-D3`** by implication.

> **The precedence question does not arise.** It would have arisen only under reading
> **3** — shipping a CDS context **and** honouring a platform condition. Under the
> chosen reading, forced colours sits **outside** Theme precedence entirely
> (**CS-11**, `DEC-S-138` part D).

### Neutral / document — derived classification

*(Normative — **CDS-WP-022**, 2026-09-12. **Answered by existing normative
authority; no new Decision is required**, the disposition **OD-6B** also received.)*

Applying the within-channel rule (**CA-3**) to what the candidate table actually
names: **long-form web documentation is channel 3, a paginated report is channel 4,
and a slide deck is channel 5.** Each of them **is** the channel; none of them
*varies within* one. Nothing in CDS names a **within-channel** document-like
presentation condition, and the candidate table records **no consumer requirement**
for one.

| # | Rule |
| --- | --- |
| 1 | **A "neutral / document" Core Theme Resolution Context is not admissible today, and none is created.** The constructs the candidate named are **channel scope** (Layer 6), governed by the [Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md) and the per-channel accessibility profiles — **four of nine of which do not exist** (DEC-S-058). |
| 2 | **This is not a permanent prohibition.** A future *within-channel* document-like presentation condition may be proposed under **CA-1 … CA-13** like any other candidate, and would need the cross-product need **CA-4** requires and the explicit decision **CA-2** requires. |
| 3 | **No context is created for symmetry.** A table with three admitted rows and one empty one is not a reason to admit a fourth — **`SYMMETRY IS NOT EVIDENCE`**. |
| 4 | **No channel classification changes.** The nine registered channels are DEC-S-029's, the Channel Mapping is unchanged, and **no channel adapter, profile, template, or export format is created.** |

## The mechanism question, and how it closed

*(**Answered.** CDS-WP-019 recorded the question; CDS-WP-022 narrowed it and
escalated the residual; the **Human Maintainer decided it** on 2026-09-12 as
**`DEC-S-137`**. Retained as the record of how the answer was reached.)*

The [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md) recorded, and
CDS-WP-019 left open:

> *"How is theme selection expressed — and is a theme a profile concern, a semantic
> concern, or both?"* and *"What token layering does light/dark support imply
> (CR-025)?"*

CDS-WP-019 listed the admissible mechanisms as a resolver-modifier context, a
separate context source set, a combination, or something else satisfying
**T-1 … T-10**. Effective authority had since narrowed that list; the Human
Maintainer closed what remained.

| Reading | Disposition |
| --- | --- |
| **A theme is a Product Profile concern** | **Excluded** — a theme applies **across** products and a profile to **one**, and **a Product Profile may never define a context** (*Theme ≠ Brand ≠ Product Profile*, **CB-3**, DEC-S-025). **Excluded before CDS-WP-022**, which added no authority to it. |
| **A theme is a per-context token path** | **Excluded** — a context never appears in a token path (**T-8**, N-6, SN-6, **TC-1**, **CI-2**, **TM-3**); a context-qualified role path is a **different role**, which **T-2** forbids. |
| **A theme is a per-context Source Set** | **Excluded** — it would need a second source set for the **same** Family × Token-Flow-Layer unit (**DEC-S-131 clause 5**) and a **`context` or `theme` namespace segment** (**DEC-S-132 clause 12**), against ten closed identities (**clause 10**). **`DEC-S-137` clause 5 and TM-5 confirm the exclusion without amending either decision.** |
| **The Resolver becomes a second maturity unit** | **Excluded by `DEC-S-137`** clauses 6 and 8 (**TM-6**, **TM-8**). **DEC-S-131 clause 1** attaches evidence to a Source Set *"and nowhere else"*, and clauses 11 and 12 already reject propagation and roll-ups. |
| **A theme is a resolver-modifier context** | **CHOSEN — `DEC-S-137`.** Multi-context composition *"(e.g. light/dark themes)"* was already assigned to the **DTCG Resolver Module 2025.10**, with the Resolver / Composition document registered as **source-set class 6** and class-2 normative. |

**The residual was never *"resolver or not"*.** It was the question **CB-6** stated:

> **Where does a context-conditional binding live, and which unit carries its
> evidence?**

**`DEC-S-137` answers it without amending anything.** The binding is expressed through
the Resolver / Composition architecture; the **Theme Resolution Context** and the
**Resolver / Composition revision** are recorded as **exact evidence inputs** of
evidence that stays bound to (`sourceSetId`, `sourceRevision`); and **the Resolver
never becomes a maturity carrier** — **`EVIDENCE INPUT ≠ MATURITY CARRIER`**. See
**TM-1 … TM-12** and
[ADR-0007](../decisions/ADR-0007-THEME-RESOLUTION-AND-CONTEXT-EVIDENCE-ARCHITECTURE.md).

> **If a proposed mechanism cannot satisfy T-1 … T-10, the mechanism is wrong — not
> the constraints.** The chosen mechanism satisfies them, and **T-1 … T-10 are
> unchanged.**

## Machine-readable boundary

*(Normative as a boundary. **No source, schema, validator, test, or fixture is
created or changed.**)*

**What is already in force**, and which CDS-WP-022 neither changes nor re-decides:

- Multi-context composition *"(e.g. light/dark themes)"* uses the **DTCG Resolver
  Module 2025.10** — reusable **sets** combined by **conditional modifiers** in a
  **defined order**
  ([Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)).
- The **Resolver / Composition Document** is **source-set class 6** and **class-2
  normative**; it *"introduces no new value or meaning"* and honours the downward
  dependency direction
  ([Machine-Readable Source Model](MACHINE_READABLE_SOURCE_MODEL.md), DEC-S-079).
- **Resolution order:** manifest → strictly downward Reference → Semantic →
  Component → Product Profile → modifiers **for the requested context** → resolved
  set for generation.
- A **cross-file reference** is permitted only when **declared** by the manifest or
  resolver graph, pointing to a **known Source-Set identity**, **offline
  resolvable**, and **revision- and provenance-bound**; anything **ad-hoc or
  undeclared fails closed** (DEC-S-078, DEC-S-091).
- **Validation layers V1 … V4** and the fail-closed list stand unchanged, as does
  **`Not assessed`** for any layer that has not run.

**The mechanism is now decided against exactly that machinery.** **`DEC-S-137`**
selects the **Resolver-Modifier Context** over the existing Source-Set graph
(**TM-1**), which is the construct the bullets above already registered as normative
for multi-context composition. **No new machine-readable construct is introduced**,
and **no source, manifest, resolver instance, schema, validator rule, test, or
fixture is created or changed.**

**One coverage gap is recorded here rather than repaired**, because repairing it is
outside CDS-WP-022:

| # | Recorded gap |
| --- | --- |
| 1 | **The committed CDS Resolver Document schema cannot express a context condition.** Its optional `modifiers` array admits items carrying `order`, `name`, `$ref` and `pointer` only, with `additionalProperties: false` — **there is no condition slot, and none can be added as an extension field.** |
| 2 | **The offline validator does not validate resolver modifier semantics**, and **records them as not validated and not represented as passed** — the bounded **DEC-S-098** V2 coverage boundary, exactly as **RISK-074** warns must not be read as a profile admission. |
| 3 | **This is a declared coverage boundary, not a class-1 / class-2 conflict.** **No resolver instance with modifiers exists**, so there is no affected artifact state and **DEC-S-034 is not triggered**. The resolution model's own wording — Resolver Module *"where applicable"* — already anticipates it. |
| 4 | **Consequence:** a concrete context-conditional resolver instance requires a **schema and validator extension**. That is **not CDS-WP-022's**: it belongs to the separately authorized source-authoring and validation work packages (**`CDS-WP-020A`**, **CDS-WP-024**), both **`Planned`, not active, and not authorized**. **AUTHOR is not VALIDATE**, and defining a contract is neither. |
| 5 | **`DEC-S-137` clause 15 keeps `F-022-01` routed and unresolved**, and **changes no schema.** Deciding the mechanism does not close the representation gap — **`MECHANISM DECIDED ≠ REPRESENTATION AVAILABLE`** — and no context-conditional resolver instance may be authored until the gap is closed under its own authorization. |

> **`DEFINING A RESOLUTION CONTRACT ≠ AUTHORING A RESOLVER INSTANCE`.** No
> `.tokens.json`, Source Set, Source-Set Manifest, Resolver document, context
> source, semantic role, reference primitive, alias, value binding, `sourceSetId`,
> or `sourceRevision` is created. **Visual Source Sets: 0. Visual values: 0.**

## The Human-Maintainer decision package

*(**All five escalations are answered.** CDS-WP-022 escalated rather than invented;
the Human Maintainer decided on 2026-09-12 and authorized a bounded rework to prepare
the records. **`DERIVE ≠ DECLARE`**, and an authorized work package is **not** an
executor authorized to invent normative choices — which is why these are recorded as
**decisions**, not as derivations.)*

| Key | Question | Decision | Recorded as |
| --- | --- | --- | --- |
| **`WP022-D1`** | The Theme and Context Mechanism — where a context-conditional binding lives, which unit carries its evidence, and whether a Spatial Context composes with a Theme Resolution Context | **APPROVED — Resolver-Modifier Context over the existing Source-Set graph**, with context-specific evidence bound to (`sourceSetId`, `sourceRevision`) and the **Resolver / Composition revision** and **Theme Resolution Context** recorded as exact evidence inputs; **no per-context Source Set**; **no second maturity unit**; **Theme and Spatial Context orthogonal**, with joint evaluation deferred | **`DEC-S-137`** · **[ADR-0007](../decisions/ADR-0007-THEME-RESOLUTION-AND-CONTEXT-EVIDENCE-ARCHITECTURE.md)** (covering `DEC-S-137` **only**) · **TM-1 … TM-12** |
| **`WP022-D2`** | The initial supported Core Theme Resolution Context set | **APPROVED — `Light` and `Dark`**, **equal peers**, **neither the default**; **no machine-readable identifier authored** | **`DEC-S-138`** part A · *The context set* |
| **`WP022-D3`** | The forced-colours / high-contrast disposition | **APPROVED — platform condition; no CDS Core High-Contrast Theme Resolution Context at this stage**; the obligation binds independently of Theme selection; a future dedicated theme needs separate authorization | **`DEC-S-138`** part B · *The forced-colours disposition* |
| **`WP022-D4`** | Context selection and environmental precedence | **APPROVED — abstract Core selection contract with bounded precedence: explicit viewer choice > inferred environment preference**; mandatory platform accessibility conditions **outside** Theme precedence and always binding; consumer or runtime owns sensing, persistence and transport; **no technology named**; unresolved equal-authority conflict **fails closed** | **`DEC-S-138`** parts C and D · **CS-8 … CS-11**, **CE-5**, **CF-11** |
| **`WP022-D5`** | Default, fallback and missing-context semantics | **APPROVED — no Core default Theme, no resolver-level default Theme, no semantic default reference alias; fail closed** on missing, unsupported and unresolved-conflict; **no silent substitution**; **`Not Applicable`** where Theme resolution genuinely does not apply | **`DEC-S-138`** parts E, F and G · **CF-9**, **CF-11**, *Not Applicable* |

**Effectivity.** **`DEC-S-137`, `DEC-S-138` and `ADR-0007` are `Accepted` and
effective at the Human-Maintainer exact-object integration commit
`23914ecc48c1fb3cba5e3dab97a505589e821b6b`** of the exact reviewed Working Tree
object of CDS-WP-022, which followed a **Fresh Independent Review** (reviewer ≠
executor), a **bounded corrective rework**, a **confirmatory independent review** and
**Nova final integration adjudication**. **The effective register held
136 decisions and 6 ADRs until that commit and holds 138 and 7 from it.** **`APPROVED
PROPOSITION ≠ EFFECTIVE REPOSITORY DECISION`** held until it, **a review PASS is not a
commit**, and **a Nova recommendation is not an approval**. **The `WP022-D*` keys are
execution-local report keys, not Decisions, ADRs, risks, requirements, or stable
governance identifiers**, and **no `DEC-S-139`, no `ADR-0008` and no `RISK-099`
exists or is prepared** — the risk register stays at **98**.

**What remains open, and is not a decision this package withheld:**

| Item | State |
| --- | --- |
| A resolver representation able to express a **context condition** | **`F-022-01`**, **routed** to **`CDS-WP-020A`** and **CDS-WP-024** — **`MECHANISM DECIDED ≠ REPRESENTATION AVAILABLE`** |
| **Machine-readable context identifiers** for `Light` and `Dark` | **Not authored.** **`CDS-WP-020A`**'s, under its own separate authorization |
| **Joint Theme × Spatial rendering and evidence evaluation** | **Deferred** to separately authorized future scope (**TM-12**) |
| The **evidence-record shape** carrying a context and a resolver revision as exact inputs | Deferred to the accessibility evidence model, under separate authorization |
| **Every visual value**, the concrete role vocabulary, and per-family topology | **Not CDS-WP-022's.** **VP-3, VP-5, VP-6 and VP-7 stay `UNSATISFIED`** |
| **Named extension points** | **CDS-WP-032's.** The set is **empty**, and **no Product Profile can be approved** |

**What is unchanged by all five decisions:**

- **T-1 … T-10**, **TS-1 … TS-6**, **TC-1 … TC-7**, **CA-1 … CA-13**,
  **CI-1 … CI-6**, **CS-1 … CS-7**, **CE-1 … CE-4**, **CF-1 … CF-8**, **CF-10** and
  **CB-1 … CB-7**.
- **DEC-S-024** (five layers), **DEC-S-131**, **DEC-S-132**, **DEC-S-135** and
  **DEC-S-136** — **unchanged in byte and in substance.**
- **`WP021-D2` deferred**, with **no VF-4 technical root and no VF-4 Source Set
  identity**.
- **VF-1 … VF-9 `Proposed`**, **visual values 0**, **visual Source Sets 0**, **every
  visual artifact AE-0**, **claims None**, **conformance None**, **Stable No**,
  publication **`Private Development`**, and the Semantic Status Candidate family
  **untouched**.
- **CDS-WP-022 `AUTHORIZED` / `ACTIVE FOR EXECUTION` and not closed**;
  **`CDS-WP-020A` and CDS-WP-023 … CDS-WP-053 `Planned`, not active, not
  authorized.**

## What a Product Profile may do with themes

| A Product Profile **may** | A Product Profile **may never** |
| --- | --- |
| Override a value **within** a context at a **named, approved** extension point | Define a new context |
| Select among contexts the core supports | Remove a context a consumer depends on |
| — | Change what a role means in any context |
| — | Weaken a contrast obligation or the focus indicator in any context |
| — | Use a context to reach a value it may not override directly |

The last prohibition matters: **a context must not become a back door around the
extension-point boundary.** Overriding through a theme what a profile may not
override directly is the same violation with an extra step.

**No extension point is named today** (CDS-WP-032).

## Validation requirements

*(Requirements on **CDS-WP-024**. **No validator, schema, rule, test, or fixture is
created or changed here**, and none of the checks below can be run today.)*

A later validator must be able to detect: a context that adds or removes a role; a
context in which a declared pairing or contrast obligation does not hold; a context
that removes or weakens a focus role; a theme name appearing in a shared semantic
identifier; a non-deterministic or externally-dependent resolution; a resolved
output with no declared context provenance; and a profile override reaching a value
through a context that it may not override directly.

CDS-WP-022 adds the following detectable conditions, each derived from a rule above
and **each stated as a requirement on CDS-WP-024, never as an implemented check**:

| # | Must detect | Derived from |
| --- | --- | --- |
| 1 | A **requested context absent from the declared supported set** | **CF-1**, **CA-1** |
| 2 | A **context identifier in a token path** | **CF-8**, **CI-2** |
| 3 | A **context identifier in a Source Set identifier**, or a `context` / `theme` namespace segment at any position | **CF-8**, **CI-3**, DEC-S-132 clause 12 |
| 4 | A **second source set declared for the same Family × Token-Flow-Layer unit** | **CB-6**, DEC-S-131 clause 5 |
| 5 | A **resolved output with no declared context provenance**, or one that cannot identify its source and transformation revision | **CF-6**, **CS-7**, TB-7 |
| 6 | A **resolver step that requires a non-local or online reference** to resolve a context | **CF-5**, **CS-5**, DEC-S-091 |
| 7 | A **context-conditional construct in a document position the CDS profile does not admit** | **CB-6**, the machine-readable boundary above |
| 8 | A **resolution that substitutes a different context** for an unsupported request | **CF-1**, DEC-S-023 |
| 9 | A **Theme-applicable resolution with no explicitly selected supported context**, and any **default or fallback Theme** | **CF-9**, `DEC-S-138` part E |
| 10 | A **semantic role carrying a default reference alias** | **CF-9**, `DEC-S-138` part E, TS-1 |
| 11 | An **unresolved conflict between equal-authority selection inputs** that did not fail closed | **CF-11**, `DEC-S-138` part F |
| 12 | A **context-specific evidence record that does not carry its Resolver / Composition revision and its Theme Resolution Context** as exact inputs | **TM-7**, `DEC-S-137` clause 7 |
| 13 | A **Resolver / Composition document asserting a maturity or approval state of its own** | **TM-8**, `DEC-S-137` clause 8, DEC-S-131 clause 1 |
| 14 | A **spatial context appearing as a Theme modifier, Theme selector, or Theme-resolution input** | **TM-11**, `DEC-S-137` clauses 11 and 12 |
| 15 | A **`Not Applicable` declaration standing in for a fail-closed condition that does apply** | *Not Applicable* rule 3, `DEC-S-138` part G |

**None of these checks exists.** The committed resolver schema cannot express a
context condition, the validator records **resolver modifier semantics as not
validated**, and **no context instance, resolver instance with modifiers, or visual
source set exists to check.** **`DEC-S-137` and `DEC-S-138` add requirements, not
implementations**, and **an unrun validation layer is `Not assessed`, never assumed
passed.**

**An automated check is never sufficient accessibility evidence** (DEC-S-053).
Whether a context is *usable* requires rendering and assistive-technology evidence
that does not exist — **`AUTOMATED CHECK ≠ ACCESSIBILITY EVIDENCE`** and
**`STRUCTURAL CONTRACT ≠ RENDERING EVIDENCE`**.

## Evidence and claim boundary

**No theme has been rendered, resolved, or evaluated, and every theme-related
artifact is `AE-0`.** Evidence never transfers between contexts any more than
between channels: a future `Light` evidence package evidences **nothing** about
`Dark` (**TM-10**, **CA-11**).

**Neither the initial execution nor the bounded decision rework changes that.**
Together they produced and admitted **no** evidence, ran **no** test, selected **no**
tool, exercised **no** baseline environment, and awarded **no** AE level.
**Admitting a context creates an evidence obligation, not evidence** — so
`DEC-S-138` part A **adds two evidence obligations and zero evidence.**

| Statement | State |
| --- | --- |
| Supported Theme Resolution Contexts | **0** until `DEC-S-138` is effective; **2** — `Light` and `Dark` — from then, **with no default** |
| Rendered, resolved or evaluated contexts | **0**, in either state |
| Theme or context artifacts at AE-1 or above | **0** — every one is **AE-0** |
| Accessibility claim of any level | **None is valid**, by anyone, including CDS itself (DEC-S-050, DEC-S-052) |
| `AE1-CDS-WP016-SEMSTATUS-004` | **Does not transfer** to any theme or visual artifact (**CB-5**, AF-1, AF-2, EV-5, DEC-S-126) |
| Conformance determination | **None** — it is CDS-WP-024's, and no claim type is valid today (DEC-S-044) |
| Forced-colours usability | **An architecture obligation, never evidence** (`DEC-S-138` part B) — **no test has been run in any baseline environment** |
| Visual Candidate families · Stable · release · tag · publication | **0 · No · none · none · `Private Development`** (DEC-S-048) |

**Admitting a context creates an evidence obligation, not evidence** (**CA-11**,
**CA-12**), and **a target is not a claim** (DEC-S-050). **`AUTOMATED CHECK ≠
ACCESSIBILITY EVIDENCE`** (DEC-S-053), and **`ARCHITECTURE OBLIGATION ≠
CONFORMANCE`**.

## Deferred decisions

*(Reconciled by the CDS-WP-022 bounded decision rework, 2026-09-12. **All five
escalated items are decided by Human-Maintainer authority**; what remains deferred is
listed as deferred.)*

| Deferred item | Disposition |
| --- | --- |
| The **theme mechanism**, and the token layering light and dark imply | **DECIDED** — **`DEC-S-137`**, **ADR-0007**, **TM-1 … TM-12**; effective from its own integration commit and not before |
| The **context set** | **DECIDED** — **`DEC-S-138`** part A: **`Light` and `Dark`**, equal peers, **no default** |
| Whether **high contrast** is a CDS context, a platform behaviour, or both | **DECIDED** — **`DEC-S-138`** part B: a **platform / environmental accessibility condition**, **not** a Core context. **A future dedicated theme needs separate authorization** |
| **Context precedence**, and **how a viewer's preference is expressed** | **DECIDED** — **`DEC-S-138`** parts C and D: **explicit viewer choice > inferred environment preference**; mandatory platform accessibility conditions **outside** Theme precedence. **The expression mechanism stays the consumer's or runtime's and is named by no CDS source** |
| **Default, fallback and missing-context semantics** | **DECIDED** — **`DEC-S-138`** parts E, F and G: **no default, fail closed, `Not Applicable` where genuinely inapplicable** |
| Whether a **Spatial Context** composes with a Theme Resolution Context | **DECIDED as orthogonality** — **`DEC-S-137`** clauses 11 and 12, **TM-11**, **CB-2**. **Joint Theme × Spatial rendering and evidence evaluation stays DEFERRED** to separately authorized scope (**TM-12**). **DEC-S-136 is unchanged.** |
| Whether **neutral / document** is a theme or a channel concern | **Answered by existing authority — channel scope; no new Decision required** (*Neutral / document* above) |
| The **machine-readable representation** of a context condition | **STILL DEFERRED** — **`F-022-01`**, routed to **`CDS-WP-020A`** and **CDS-WP-024**. **`MECHANISM DECIDED ≠ REPRESENTATION AVAILABLE`** |
| **Machine-readable context identifiers** for the two supported contexts | **STILL DEFERRED** — **`CDS-WP-020A`**'s, under its own authorization. **None is authored here**, and a prose name is not an identifier |
| The **evidence-record shape** carrying a context and a resolver revision as exact inputs | **STILL DEFERRED** — to the accessibility evidence model, under separate authorization |
| **Every context value** | **STILL DEFERRED, and not CDS-WP-022's.** Value selection needs **VP-1 … VP-7**, and **VP-3, VP-5, VP-6 and VP-7 are `UNSATISFIED`** — see the [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md) |
| **Named extension points** | **CDS-WP-032's**, unchanged. The set is **empty**, and **no Product Profile can be approved** |
| **Concrete visual roles, primitives, scales and topologies** | **Not CDS-WP-022's** — **`THEME MECHANISM ≠ ROLE VOCABULARY`** (**CB-4**) |

**An authorized work package is not authorization to decide everything inside its
subject.** The five items above were **escalated, not decided by the executor**, and
the Human Maintainer decided them — which is the distinction the escalation existed to
preserve.

## What CDS-WP-022 does not do

*(Normative as a boundary, recorded so the contract is not read as more than it is.
Reconciled by the bounded decision rework: the five decided questions are no longer
listed here as *not done*, and everything that genuinely remains not done still is.)*

1. **It creates no theme instance.** `Light` and `Dark` are **declared presentation
   conditions**, decided by **`DEC-S-138`** part A and **supported only from that
   decision's effectivity**. **Nothing has been rendered, resolved, or evaluated in
   either**, and **a supported context is not a rendered one.**
2. **It creates no machine-readable context identifier.** **`Light` and `Dark` are
   human-readable architectural names, not identifiers** (**CI-5**, `DEC-S-138` part
   A clause 4), and **naming a context in prose creates none** (VF-I-13). Authoring
   one is **`CDS-WP-020A`**'s.
3. **It creates no value, no role, and no alias** — no colour, typography, spacing,
   shape, surface, or breakpoint value; no semantic role; no reference primitive; no
   token identifier; and **no default alias**: **`DEC-S-138`** part E creates none,
   and **TS-1 is satisfied by compliance, not by exemption.**
4. **It creates no machine-readable artifact** — no `.tokens.json`, Source Set,
   manifest, resolver document, `sourceSetId`, `sourceRevision`, schema, validator
   rule, test, fixture, or generated output. **`DEFINING A RESOLUTION CONTRACT ≠
   AUTHORING A RESOLVER INSTANCE`**, and **`MECHANISM DECIDED ≠ REPRESENTATION
   AVAILABLE`** — **`F-022-01` stays routed.**
5. **It creates no second maturity unit.** The **Source Set** remains the sole
   independently evaluable one (**TM-6**), a Resolver / Composition document is an
   **evidence input and never a maturity carrier** (**TM-8**), and **DEC-S-131 and
   DEC-S-132 are unchanged in byte and in substance.**
6. **It admits no evidence and awards no AE level.** Admitting two contexts **adds
   two evidence obligations and zero evidence** (**CA-11**, **TM-7**); **every theme
   artifact stays AE-0**; **`AE1-CDS-WP016-SEMSTATUS-004` transfers nowhere**; and
   the forced-colours rule is an **architecture obligation, never conformance**
   (`DEC-S-138` part B).
7. **It makes no claim and determines no conformance.** **VF-1 … VF-9 stay
   `Proposed`**, visual Candidate families stay **0**, **Stable stays `No`**,
   publication stays **`Private Development`**, and the Semantic Status Candidate
   family is **untouched**.
8. **It adds no risk entry** — the register stays at **98**, with **no `RISK-099`**
   — and **no `DEC-S-139` and no `ADR-0008`** exists or is prepared. **Claude does
   not mark an ADR `Accepted`; that is a Human-Maintainer act**, which is why
   **ADR-0007 became `Accepted` only through the Human-Maintainer exact-object
   integration commit `23914ecc48c1fb3cba5e3dab97a505589e821b6b`**, at which it is
   effective — **not through this document.**
9. **It satisfies no value prerequisite.** **VP-3, VP-5, VP-6 and VP-7 stay
   `UNSATISFIED`**, **VP-4 stays `UNSATISFIED` for VF-4**, and **`WP021-D2` stays
   `DEFERRED`** with **no VF-4 technical root, no VF-4 Source Set identity, and no
   range name, count, or threshold**. **No relation exists between approving
   `WP022-D1` and resolving `WP021-D2`.**
10. **It authorizes no successor and satisfies no `CDS-WP-020A` prerequisite beyond
    one.** From the effectivity of `DEC-S-137` and `DEC-S-138` the **DEC-S-135
    theme-mechanism sequencing condition is satisfied** — and **`THEME GATE SATISFIED
    ≠ VALUE SELECTION AUTHORIZED`**, **`THEME GATE SATISFIED ≠ CDS-WP-020A
    AUTHORIZED`**, **`ONE PREREQUISITE SATISFIED ≠ ALL PREREQUISITES SATISFIED`**, and
    **`ALL PREREQUISITES SATISFIED ≠ WORK PACKAGE AUTHORIZED`**. **`CDS-WP-020A` and
    CDS-WP-023 … CDS-WP-053 remain `Planned`, not active, and not authorized.**
11. **It closes nothing.** **CDS-WP-022 remains `AUTHORIZED` / `ACTIVE FOR
    EXECUTION`**; **closure is a separate Human-Maintainer act and has not occurred**;
    and **`EXECUTION ≠ CLOSURE`**, **`REVIEW PASS ≠ INTEGRATION`** and **`INTEGRATION
    ≠ CLOSURE`** all hold.
12. **It reaches no milestone by itself.** **`MILESTONE REACHED ≠ MATURITY AWARDED`**,
    and **M2 — Visual Foundation Ready** is a roadmap state granting **nothing**.

## Related documents

- [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
- [Visual Foundation Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md)
- [Visual Foundation Brand and Product Profile Boundary](../governance/VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md)
- [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md)
- [Machine-Readable Source Model](MACHINE_READABLE_SOURCE_MODEL.md)
- [Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
- [Accessibility Requirements Baseline](../governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [Visual Semantic Token Foundation](VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) — SR-1 … SR-12, **TC-1 … TC-7**, the alias model
- [Visual Reference Token Foundation](VISUAL_REFERENCE_TOKEN_FOUNDATION.md) — RP-1 … RP-10
- [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md) — VP-1 … VP-7, VE-1 … VE-12
- [Adaptive Layout and Responsive Foundation](ADAPTIVE_LAYOUT_AND_RESPONSIVE_FOUNDATION.md) — CX-1 … CX-9, AC-1 … AC-6
- [ADR-0006 — Adaptive Spatial Context and Named-Range Architecture](../decisions/ADR-0006-ADAPTIVE_SPATIAL_CONTEXT_AND_NAMED_RANGE_ARCHITECTURE.md) — **DEC-S-136**
- [ADR-0007 — Theme Resolution and Context-Evidence Architecture](../decisions/ADR-0007-THEME-RESOLUTION-AND-CONTEXT-EVIDENCE-ARCHITECTURE.md) — **DEC-S-137 only**; **`Accepted` and effective at `23914ecc…`**
- [Decision Index](../decisions/DECISION_INDEX.md) — **DEC-S-024**, **DEC-S-131**, **DEC-S-132**, **DEC-S-135**, **DEC-S-136**, **DEC-S-137** and **DEC-S-138**
