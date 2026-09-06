# Visual Semantic Token Foundation

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-020 — Reference and Semantic Token Foundation
- **Date:** 2026-08-26
- **Amended by:** CDS-WP-020 (Decision Integration Pass), 2026-08-27 — **SR-3**,
  **AL-3** and the *Deferred decisions* section, to apply **DEC-S-129** and
  **DEC-S-130**. **Those amendments are effective** at the Human-Maintainer
  exact-byte integration commit `42a568d823de3388e45af62967546f13ad67eff6`
  (2026-08-27). **They create no role identifier and select no value**, and SR-1, SR-2,
  SR-4 … SR-12, SN-1 … SN-9, PN-1 … PN-5, TC-1 … TC-7, SS-1 … SS-8, IS-1 … IS-5,
  the alias model's remaining rules, and the focus role set are unchanged.
- **Amended by:** CDS Step-9 Decision Integration Pass, 2026-09-05 — the *Naming and
  identity at the semantic position* section (identifier grammar and fixed family
  roots), a new *Role admission* section, **IS-5**, and the *Deferred decisions*
  section, to apply **DEC-S-132**
  ([ADR-0005](../decisions/ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md)),
  **DEC-S-134** and **DEC-S-135**. **Those amendments are effective** at the
  Human-Maintainer exact integration commit
  `2cb244e889c1a6b5a278afb233995a0379b5d9ef` (2026-09-05). **They create
  no role, no role identifier, no binding and no value**, and SR-1 … SR-12,
  SN-1 … SN-9, PN-1 … PN-5, TC-1 … TC-7, SS-1 … SS-8, IS-1 … IS-4, the alias model,
  the closed role classification, and the focus role set are unchanged.
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for what a CDS visual semantic role is and what it must
  declare** — token-flow layer **2 Semantic** inside the visual foundation. It
  **creates no role identifier and selects no value**.
- **Maturity:** **`Proposed`** — this document promotes nothing and grants no
  maturity to any artifact (DEC-S-036).

## Purpose and boundary

This document defines the **Semantic layer of the CDS visual foundation**: what a
visual semantic role is, which role classes each family holds, what every role
must declare before it may exist, how a role aliases a reference primitive, and
what a role may never do.

**This is where the visual foundation actually lives.** Layer 1 holds values that
nobody may use; layer 2 holds the meaning that makes them usable and reviewable.

Frame: [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md) —
Layer 3, token-flow layer 2. Its companion at token-flow layer 1 is the
[Visual Reference Token Foundation](VISUAL_REFERENCE_TOKEN_FOUNDATION.md).

### What this document is not

It **creates no role identifier**: no colour role name, no text role name, no
spacing role name, no shape role name, no surface role name, no state role name,
and no focus role name. It **selects no value** of any kind, **defines no theme**,
**names no extension point**, **activates no Product Profile**, and **binds no
status axis to any visual role**.

It also creates no token source file, no schema, no validator rule, and no
component, and it **resolves no open decision**. The concrete role vocabulary
remains open and is recorded in the
[Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
register.

## Authority basis — this document registers no new decision

*(Normative)*

> **Every binding statement below is an application of a decision already in
> force. This document creates no new normative choice and registers no Decision,
> ADR, or risk.**

| This document's binding statements | Derive from |
| --- | --- |
| A semantic role expresses purpose and aliases a reference value | DEC-S-024, token-flow layer 2 |
| A semantic role is never named after its appearance | DEC-S-024 semantic-first, VF-I-2, N-1 |
| A semantic role never depends on a component, a channel, or a product | DEC-S-021 prohibited dependencies, VF-I-4, N-2, N-3 |
| Every contrast-sensitive role declares its obligation and its pairings | VF-I-8, Colour Architecture CR-2 and CR-3 |
| Colour is never the sole carrier of meaning, in any channel | DEC-S-056, DEC-S-111, CR-006, VF-I-5 |
| Visible focus is a CDS-alone obligation with no permitted mechanism of removal | DEC-S-055, DEC-S-059, CR-021, F-1 … F-8 |
| An interaction state is not a semantic status | VF-I-7, DEC-S-105, DEC-S-111 |
| A visual role never replaces or aggregates a status axis | VF-I-6, DEC-S-107, DEC-S-112 |
| A theme re-binds and never redefines; a profile varies only named extension points | VF-I-9, VF-I-10, DEC-S-025, T-1 … T-10 |
| References and resolution fail closed; the dependency direction is downward only | DEC-S-078, DEC-S-079, DEC-S-091 |
| Adding a semantic role is an **Elevated** change | DEC-S-033, Visual Foundation Governance and Lifecycle |
| Maturity is granted by a gate, never by a document or metadata | DEC-S-035, DEC-S-036, DEC-S-126, VF-I-14 |
| The concrete role vocabulary remains deliberately open | DEC-S-032, DEC-S-003 |
| *(2026-08-27 amendment)* A contrast obligation is evaluated against **WCAG 2.2**, by the method those criteria require, at full precision, with no threshold restated | **DEC-S-129** |
| *(2026-08-27 amendment)* Both ends of an alias carry their own explicit `$type` from the admitted set | **DEC-S-130**, ADR-0004 |

**Those two rows were added by Decisions taken under separate Human-Maintainer
authorization, not by this document.** It still registers no Decision, ADR, or risk
of its own, creates no role identifier, and selects no value.

## What a semantic visual role is

*(Normative)*

> **A semantic visual role is a named purpose that resolves to a value it does not
> own.**

| A semantic role **owns** | A semantic role **never owns** |
| --- | --- |
| **What the decision is for** — its purpose | A raw value of its own |
| Its **class** within its family | Knowledge of any component (VF-I-4) |
| Its **contrast obligation** and the roles it is measured against | Any status axis meaning (VF-I-6) |
| Its **valid pairings** | Any product, consumer, or customer identity (N-2) |
| Its **non-visual carrier** where it participates in meaning | Any channel scope in its identifier (N-3) |
| Its **degradation behaviour** where a channel cannot render it | Any theme or profile term in its identifier (N-6, T-8) |
| Its **resolution target** — the reference primitive it aliases | The right to be removed by a context or a profile |

### A role that is merely a value is not a role

A "role" that can be fully described by naming its value is a primitive wearing a
role's clothes (SP-1, VF-I-2). The test is not stylistic: an appearance-derived
name in a semantic position **forecloses theming, profiles, and channel
transformation simultaneously**, because every downstream context inherits an
assumption the name has already made.

## Role classes by family

*(Normative as a **classification**, not as a vocabulary. **No role identifier is
created.** Every class below is already registered by a CDS-WP-019 family
architecture; this document consolidates them and adds none.)*

| Family | Registered semantic role classes | Registered by |
| --- | --- | --- |
| **VF-1 Colour** | Surface · Content · Boundary · Interaction · Focus · Feedback · Emphasis · Data | [Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md) |
| **VF-2 Typography** | Heading · Body · UI · Editorial and document · Code and monospace · Numeric and data · Supporting; plus font-family role and weight role | [Typography Architecture](VISUAL_FOUNDATION_TYPOGRAPHY_ARCHITECTURE.md) |
| **VF-3 Space and Size** | Spacing role · Size role · Density model | [Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md) |
| **VF-5 Shape** | Radius role · Border role · Separator role | [Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md) |
| **VF-6 Surface and Elevation** | Surface role · Surface hierarchy · Elevation role · Overlay and scrim role | [Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md) |

**VF-4, VF-7, VF-8 and VF-9 contribute no semantic role here.** Layout and grid
are CDS-WP-021's, iconography is CDS-WP-037's, motion is CDS-WP-035's, and a theme
is a resolution context that holds no role of its own (T-1).

### The cross-family role sets

*(Normative — two constructs that no single family owns)*

| Set | Draws on | Why it is cross-family |
| --- | --- | --- |
| **Focus indication** | VF-1 (colour), VF-5 (shape and stroke), VF-3 (space) | Modelling it as a family would let one family's change silently weaken a **CDS-alone** obligation (2.4.7). It is deliberately not a family. |
| **Component-independent state** | VF-1 primarily, with VF-5 and VF-6 | A state that cannot be described without naming a component is Layer 4 and does not belong here (VF-I-4). |

**A cross-family construct matures no faster than its weakest constituent**
(AF-4). The focus role set is not Candidate while any of VF-1, VF-5, or VF-3 is
not.

## Role obligations

*(Normative — **every** visual semantic role, without exception. These consolidate
the family-specific obligations already registered as CR-1 … CR-6, TR-1 … TR-6,
SP-1 … SP-5, and SH-1 … SH-5; they add none.)*

| # | Every visual semantic role must declare | Source |
| --- | --- | --- |
| **SR-1** | Its **family** and its **class** within that family | Family architectures, class tables |
| **SR-2** | Its **purpose** in terms a person can argue about — not its magnitude, not its appearance | VF-I-2, SP-1, SH-1 |
| **SR-3** | Whether it is **contrast-sensitive**, and **against which role or roles** it is measured. Where it is, the evaluation authority is **WCAG 2.2** and the contrast-ratio method those criteria themselves require, compared at **full precision with no rounding before comparison** — CDS restates no threshold and invents none (**DEC-S-129**). | **VF-I-8**, CR-2, TR-2, SH-2, DEC-S-129 |
| **SR-4** | Its **valid pairing set** — a foreground role names the surfaces it is defined against; a surface role names the content roles it must support | CR-3, SU-2 |
| **SR-5** | Whether it **participates in conveying meaning**, and if so **which non-visual carrier accompanies it** | NC-1 … NC-5, SP-2, SH-3, VF-I-5 |
| **SR-6** | Its behaviour under **reduced-colour conditions** — greyscale, forced colours, monochrome print | Colour Architecture, reduced-colour table |
| **SR-7** | Its behaviour under **user text resize, text-spacing overrides, reflow, and magnification**, where the role can affect them | TR-4, SP-3, SP-4, TA-2 … TA-4 |
| **SR-8** | Its **text-length tolerance** — no role assumes a fixed or maximum string length | TR-3, CR-023, baseline 8.3 |
| **SR-9** | Its **channel availability**, and its **degradation behaviour** where a channel cannot render it | TR-6, SH-4, D-1 … D-6, VF-I-11 |
| **SR-10** | Whether it is a **named extension point** for a Product Profile — **no role is one today** | CR-5, TR-5, SP-5, SH-5, DEC-S-025 |
| **SR-11** | Its **resolution target** — the reference primitive it aliases, and in which contexts | DEC-S-024, DEC-S-078 |
| **SR-12** | Its **lifecycle state**, its **compatibility impact**, and on rename or removal a **migration reference** | DEC-S-039, DEC-S-040, DEC-S-082 |

> **A role that does not declare SR-3 cannot be validated, themed, or profiled
> safely, and must not exist.** An unstated contrast obligation is how a theme or
> a profile silently breaks conformance capability without anyone being able to
> detect it (VF-I-8).

### SR-5 is the obligation that is routinely under-declared

Declaring *"this role conveys nothing"* is a real and frequently correct answer,
and it is materially different from leaving SR-5 blank. A blank SR-5 is
indistinguishable from an unexamined role, and it is the state in which
colour-only, shape-only, or position-only meaning enters a system unnoticed.

## The alias model

*(Normative — an application of DEC-S-024, DEC-S-078, DEC-S-079 and DEC-S-091.
**No alias is created.**)*

### Permitted and prohibited edges

```text
reference  ←  semantic          permitted   (a role resolves to a primitive)
semantic   ←  component         permitted   (a component binds a role)
component  ←  product profile   permitted   only at a named, approved extension point
any        ←  generated output  permitted   read-only, provenance-carrying
```

```text
semantic   →  component         prohibited  meaning must not depend on a component
reference  →  semantic          prohibited  a primitive must not know its purpose
component  →  reference         prohibited  the most tempting and most damaging shortcut
consumer   →  reference         prohibited  imports a value, discards its purpose
profile    →  core redefinition prohibited  a profile varies values, never semantics
any cycle  →  any layer         prohibited  at any layer, of any length
```

### Alias rules

| # | Rule |
| --- | --- |
| **AL-1** | **A semantic role resolves to a reference primitive, never to a raw literal.** A role carrying its own literal value has absorbed layer 1 and made the value unthemeable and unprofileable. |
| **AL-2** | **A semantic role never aliases another semantic role.** Role-to-role chains create an implicit hierarchy that no document declares, so that changing one role silently changes another. Where two roles must share a value, both alias the same primitive. |
| **AL-3** | **Type compatibility is enforced.** A reference must resolve to a compatible `$type`; a mismatch fails closed (DEC-S-078). Both ends carry their **own** explicit `$type` from the admitted set — `color`, `dimension`, `number` — and neither may rely on group- or root-level typing (**DEC-S-130**). |
| **AL-4** | **An unresolved alias fails closed.** A dangling reference, a missing source set, a cycle, an undeclared cross-file reference, or a provenance-unknown target is a failure, never a fallback (DEC-S-078, DEC-S-091). |
| **AL-5** | **Cross-file references are valid only through the declared local Manifest and Resolver graph**, offline-resolvable and revision-bound. No network reference of any kind is admissible (DEC-S-091, DEC-S-030). |
| **AL-6** | **Resolution is deterministic.** The same source revisions plus the same resolver plus the same context yield the same resolved result (DEC-S-080, T-6). |
| **AL-7** | **An alias transports a value, never an obligation.** A role's contrast obligation, pairing set, and non-visual carrier are properties of the **role**; they are not inherited from, and never delegated to, the primitive it resolves to. |
| **AL-8** | **A resolved value is not a source.** Any resolved or generated form is a class-3 generated artifact: never normative, never hand-edited, always provenance-carrying (DEC-S-022, DEC-S-031, DEC-S-079, VF-I-12). |

**AL-7 is the rule that keeps the layers honest.** If obligations travelled along
aliases, a theme could satisfy an accessibility obligation by re-binding to a
different primitive, and the role would have stopped being the place where the
obligation is checked.

## Naming and identity at the semantic position

*(Normative — an application of DEC-S-081 and the CDS-WP-019 naming model.
**No role identifier is created, adopted, reserved, recommended, or planned.** The
**family roots** below are fixed by DEC-S-132; **no role name is.**)*

### Grammar and roots

*(Normative — **DEC-S-132**, 2026-09-05. **Effective** at the Human-Maintainer
exact integration commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`.
[ADR-0005](../decisions/ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md)
carries the rationale.)*

A semantic position takes **`<family>.<role>[.<qualifier>]`**. The path is
**family-rooted**; the **token-flow layer is never a segment** of it and remains the
explicit `layer` field; the **qualifier** position is **declared and optional and no
concrete qualifier is created** — the term is `qualifier` rather than `modifier`
because *conditional modifier* is already bound to Resolver / Theme composition
semantics, and **N-6** and **T-8** forbid a theme term inside a shared semantic
identifier.

The fixed technical roots are **`color`** (VF-1), **`typography`** (VF-2),
**`space`** (VF-3), **`shape`** (VF-5) and **`surface`** (VF-6) — one per registered
family. The Semantic Source Set identities are **`semantic/color`**,
**`semantic/typography`**, **`semantic/space`**, **`semantic/shape`** and
**`semantic/surface`**, in the flat **`<layer>/<family>`** form; a `sourceSetId` is
**declared, never derived** (DEC-S-131 clause 3), and **token-path identity and
source-set identity are separate spaces**.

**The `<role>` position is empty.** No role name exists, and none may be invented —
see *Role admission* below. **This creates no Source Set instance, no
`sourceRevision`, no manifest, no resolver, no token, and no file.**

### Role admission

*(Normative — **DEC-S-134**, CDS Step-9 Decision Integration Pass, 2026-09-05.
**Effective** at the Human-Maintainer exact integration commit
`2cb244e889c1a6b5a278afb233995a0379b5d9ef`. **No ADR** —
DEC-S-134 is deliberately not an architecture dependency of ADR-0005.)*

| # | Rule |
| --- | --- |
| **RA-1** | **A visual semantic role enters CDS Core only on demonstrated cross-consumer need.** A need evidenced by one consumer is a consumer-local concern until it is shown to be shared (PN-2, IG-3). |
| **RA-2** | **Requirement classification precedes design.** A candidate role is classified before it is designed, named, or authored. |
| **RA-3** | **Every admitted role satisfies SR-1 … SR-12 from the moment it exists.** A role whose obligations are undeclared is **inadmissible, not provisional** — an accessibility obligation attaches as soon as the role exists. |
| **RA-4** | **The role classification is closed.** The registered classes in *Role classes by family* above stand as they are; **a future vocabulary populates them and adds none**, and DEC-S-134 adds no class. |
| **RA-5** | **The concrete role vocabulary is OPEN**, and **`CDS-WP-020A` may not invent, adopt, reserve, or recommend a CDS Core role identifier.** A vocabulary requires its own separately authorized decision, taken under RA-1 … RA-4. |

**VP-6 remains UNSATISFIED for every family.** A policy is not an authored role with
SR-1 … SR-12 declarations, and no role exists to declare anything.

### Sequencing against the theme mechanism

*(Normative — **DEC-S-135**, 2026-09-05. **Effective** at the Human-Maintainer
exact integration commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`.)*

**No semantic visual role carries a default alias to a reference primitive before
CDS-WP-022 decides the Theme and Context Mechanism**, and **CDS-WP-022 precedes
context-sensitive value selection**. This gates values and bindings, **not
structure**: identifier grammar, scale ownership, role admission, family maturity
governance and **source-set structural identity** are context-independent by
**TC-1**, **TC-2**, **T-8**, **N-6** and **RB-1**, and are not blocked.
**`CDS-WP-022 BEFORE VALUE SELECTION` does not mean `CDS-WP-022 BEFORE EVERY
SOURCE-STRUCTURE OR IDENTITY ACTIVITY`.** **TC-6 continues to bind independently**,
and **SEQUENCED NEXT ≠ AUTHORIZED** — CDS-WP-022 remains `Planned`, not active, and
not authorized.

| # | Rule |
| --- | --- |
| **SN-1** | **A semantic position carries a role name, never an appearance name** (N-1, VF-I-2). This is the inverse of the reference position, where an appearance name is permitted. |
| **SN-2** | **No status axis or status value name is reused as a visual role name** in a way that implies equivalence (N-4, VF-I-6). |
| **SN-3** | **No component name** appears in a shared semantic identifier (N-5). |
| **SN-4** | **No product, brand, customer, or consumer term** appears (N-2). |
| **SN-5** | **No channel term** appears — a channel is a scope, not a meaning (N-3). |
| **SN-6** | **No theme or profile term** appears — both are resolution inputs, never path segments (N-6, T-8). |
| **SN-7** | **A name states a purpose, not a rank**, wherever a rank would be read as an importance the system does not guarantee (N-7). |
| **SN-8** | Segment syntax is the CDS identifier profile; technical identifiers are language-neutral and stable, and display labels are a separate localized concern (DEC-S-081, DEC-S-110). |
| **SN-9** | Every rule above is **machine-checkable** (N-8), and **a rename is a migration event** (DEC-S-082). |

**The concrete path grammar and the role vocabulary are not fixed here.** Both are
open decisions — **OD-4** and **OD-6** — in the
[open-decision register](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md).
Any illustration of role *shape* in a CDS-WP-019 document is an example artifact
and is **never normative** (VF-I-13).

## Channel and product neutrality

*(Normative)*

| # | Rule |
| --- | --- |
| **PN-1** | **A shared semantic role is channel-neutral.** A role that only makes sense in one channel is a channel concern (Layer 6), not a foundation role. |
| **PN-2** | **A shared semantic role is product-neutral.** A consumer-specific need does not become CDS Core because a consumer asked; it is classified first (Requirement classification model, non-goal 11). |
| **PN-3** | **Channel outputs may differ in form and never in meaning.** A distinction a channel cannot render is **declared as a limitation**, never silently dropped (DEC-S-029, VF-I-11). |
| **PN-4** | **No technology is named.** A semantic role names no CSS feature, no layout engine, no framework, and no platform primitive (DEC-S-032, DEC-S-004). |
| **PN-5** | **No consumer holds a role.** Consumer-local token sets are class-7 consumer-local artifacts and enter CDS, if ever, only through reconciliation (DEC-S-026) — never by being read as an override. |

## Theme compatibility

*(Normative — **the theme mechanism is CDS-WP-022's and is not selected here.**
These are the properties the semantic layer must have so that CDS-WP-022 remains
free to choose.)*

| # | Requirement |
| --- | --- |
| **TC-1** | **A role's identity is context-independent.** The same role identifier is used in every context; a context is a resolution input, never a path segment (T-8, N-6). |
| **TC-2** | **A role's meaning is context-independent.** A theme re-binds which primitive a role resolves to; it never changes what the role means, and never removes the role (T-1, T-2, VF-I-9). |
| **TC-3** | **Every declared contrast obligation and pairing must hold in every context.** A context in which they do not hold is not a context change — it is a contract break (T-3, BC-3). |
| **TC-4** | **A context may never remove or weaken the focus indicator** (T-4, F-4). |
| **TC-5** | **Nothing is communicated by which context is active.** No status, state, or severity may be expressed by a context difference (T-5). |
| **TC-6** | **The semantic layer presupposes no context count and no context set.** A role model that only works if exactly two contexts exist has decided CDS-WP-022's question by implication. |
| **TC-7** | **An unresolvable role in a supported context fails closed** and is a declared limitation, never a silent fallback (T-2, VF-I-11). |

> **The semantic layer must be writable without knowing whether CDS ships one
> context, two, or a high-contrast third.** Where that is not achievable for a
> given role, the role is not yet writable — which is a finding for CDS-WP-022,
> not a reason to guess. See **OD-7**.

## The Semantic Status boundary

*(Normative — the sharpest boundary in this document)*

> **COLOUR ≠ STATUS · ICON ≠ STATUS · MOTION ≠ STATUS · ELEVATION ≠ STATUS**

The [Semantic Status Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
remains **authoritative for status meaning**. It is the only **Candidate** artifact
family in CDS (`semantic/status`, source revision
`semantic-status-rev-0002-candidate`, `Candidate` / `Approved`), and CDS-WP-020
changes **nothing** about it — not its source, not its revision, not its maturity,
not its approval, and not its evidence.

| # | Rule |
| --- | --- |
| **SS-1** | **The visual foundation defines no status meaning.** The five axes and their 25 values are the status contract's (DEC-S-105, DEC-S-106). |
| **SS-2** | **A visual role never replaces a status axis.** Visual encoding is an additional, redundant modality bound to an existing meaning (VF-I-6). |
| **SS-3** | **No visual construct may aggregate the axes.** `unknown` must never render as `nominal`, `stale` never as `current`, `unverified` never as `verified` (DEC-S-107, DEC-S-112). |
| **SS-4** | **Text first.** Every status stays communicable non-visually in every channel; removing all visual encoding must remove **no** meaning (DEC-S-110, `CDS-V4-STATUS-DESCRIPTION`). |
| **SS-5** | **A Feedback or Data role is a presentation role, not a status.** It carries no axis meaning, and it must never imply `verified`, `current`, or `nominal` where those axes do not carry it (NC-4). |
| **SS-6** | **An interaction state is not a semantic status.** A non-interactive state, a selection state, a pointer-emphasis state, and a validation outcome are presentation states (VF-I-7). |
| **SS-7** | **The binding is not made here.** How visual roles bind to status axes is **CDS-WP-023's**, gated by **CDS-WP-024** and **CDS-WP-025**. A status that cannot be validated must not be rendered as though it were. |
| **SS-8** | **`AE1-CDS-WP016-SEMSTATUS-004` does not transfer to any visual artifact**, and no visual artifact inherits Candidate maturity from the status family (AF-1, AF-2, EV-5, DEC-S-126). |

## The focus role set

*(Normative — the strictest construct in the visual foundation)*

**Visible focus is a CDS-alone obligation** (WCAG **2.4.7**, CR-021, DEC-S-055) —
one of only **five** criteria CDS owns without the consumer. All eight rules
F-1 … F-8 of the
[Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md)
bind the semantic layer unchanged, and this document adds one consequence:

> **Focus visibility has no permitted mechanism of removal.** Not by a theme
> (T-4), not by a Product Profile (F-5, invariant 10), not by an ordinary
> exception (F-6, DEC-S-059), not by a consumer override (F-7), and not by a
> context reached indirectly (RB-4, T-10). Every other visual decision in CDS has
> a legitimate route to being overridden. This one does not.

**No focus value, geometry, offset, or thickness is defined here**, and none may be
defined before the values it would be built from exist.

## Interaction and validation state roles

*(Normative as constraints; **no state vocabulary is created**)*

The semantic layer may carry roles for states that are genuinely
**component-independent**. It may not carry a state that cannot be described
without naming a component.

| # | Constraint |
| --- | --- |
| **IS-1** | A state role must be **programmatically determinable**, never signalled by appearance alone (4.1.2, baseline 7.6). |
| **IS-2** | A **non-interactive or read-only** state must remain perceivable and **must not be communicated by reduced contrast alone** — that is precisely the encoding that fails for low-vision users, in greyscale, and under forced colours. |
| **IS-3** | A **validation-feedback** role is an outcome, not a status axis value (VF-I-7). A form error is not a status `condition`. |
| **IS-4** | A **destructive or far-reaching** action's risk tier is a Layer-4 contract concern (CR-010). The foundation may supply distinct Interaction roles for tiers; it decides no tier and permits **no colour-only** distinction of danger (baseline 10.5). |
| **IS-5** | **Selected, active, and current** must be conveyed by an accessible state, never by colour or position alone. **Disposition (DEC-S-134, 2026-09-05, effective at commit `2cb244e8…`): none of the three is a CDS Core role today** — no current cross-consumer authority supports admitting them under **RA-1**. **This is not a permanent prohibition**, and it removes no protection: **IS-1** and this rule already bind whatever a consumer builds. **Their distinctness remains open** and is answered with the concrete vocabulary, not before it — deciding the count now would decide the vocabulary by implication. |

## Validation requirements

*(Stated as **requirements on CDS-WP-024**. **No validator is changed here, no
schema is added, and no diagnostic is introduced.**)*

A later validator must be able to detect, at the semantic layer:

| # | Detection |
| --- | --- |
| 1 | A role with **no declared family or class** (SR-1) |
| 2 | A **contrast-sensitive role with no declared pairing set** (SR-3, SR-4) |
| 3 | A role that **participates in meaning with no declared non-visual carrier** (SR-5) |
| 4 | An **appearance-derived role name** in a semantic position (SN-1) |
| 5 | A role name **reusing a status axis or status value** (SN-2) |
| 6 | A **component, product, consumer, channel, theme, or profile term** in a shared semantic identifier (SN-3 … SN-6) |
| 7 | A role **holding a raw literal value** instead of an alias (AL-1) |
| 8 | A **role-to-role alias** (AL-2) |
| 9 | A **type-incompatible, dangling, cyclic, undeclared, or network** reference (AL-3 … AL-5) |
| 10 | A **component binding a reference token directly**, bypassing the semantic layer (DEC-S-024) |
| 11 | A **context that adds or removes a role**, or in which a declared pairing does not hold (TC-2, TC-3) |
| 12 | **Any context or profile that removes or weakens a focus role** (TC-4, F-4, F-5) |
| 13 | A **profile override outside a named extension point** (SR-10, DEC-S-025) |
| 14 | A role **asserting a fixed or maximum text length** (SR-8) |
| 15 | A **resolved output with no declared context or source provenance** (AL-8, DEC-S-031) |

**What a validator cannot do here is the more important half.** Whether a pairing
is *perceivable*, whether a focus indicator is *visible in practice*, whether
reflow and magnification hold, and whether a non-visual carrier actually conveys
the meaning all require **rendering, interaction, and assistive-technology
evidence** — which is CDS-WP-031's and **does not exist**. **An automated check is
never sufficient accessibility evidence** (DEC-S-053), and **absence of a failure
is not evidence of success** (EV-4).

## Change classification

*(Normative — an application of DEC-S-033 and the
[Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md))*

| Change | Track |
| --- | --- |
| Clarifying a role's stated purpose without changing it | **Standard** |
| **Adding a semantic role** | **Elevated** — it extends the shared vocabulary and carries an accessibility obligation from the moment it exists |
| **Changing a role's declared contrast obligation or pairing set** | **Elevated** |
| **Changing what a role means**, renaming it, or removing it | **Elevated** — breaking, and a migration event |
| **Naming an extension point** | **Elevated** |
| **Anything touching the focus role set** | **Elevated** |

> **A change that looks Standard but touches an Elevated trigger is Elevated.**
> The trigger wins over the estimate. In both tracks, authority boundaries,
> traceability, evidence, human approval, and fail-closed behaviour are
> mandatory and may not be reduced.

## Evidence and claim boundary

- Every visual semantic artifact in CDS is **AE-0**. **None exists.** No role has
  been rendered, paired, measured, read aloud, keyboard-operated, or tested in any
  environment.
- **No accessibility claim of any level is valid**, and declaring a contrast
  obligation proves nothing (DEC-S-050). A target is not a claim.
- **Visual foundation families at `Candidate`: 0. At `Stable`: 0.** No visual
  family can reach Candidate today, because **no visual artifact exists to
  evidence** — recorded, not worked around.
- **`AE1-CDS-WP016-SEMSTATUS-004` does not transfer here** (SS-8).
- Publication remains **`Private Development`**; there is no release and no tag.

## Deferred decisions

The concrete role vocabulary, per family · the state-role vocabulary · the density
model and its levels · every value a role would resolve to · **per-family scale
topology parameters** · **VF-1 tonal topology** · composite type admission · **any
migration or deprecation compatibility mechanism outside the normative Semantic
alias graph** · the theme mechanism and the token layering light and dark imply ·
the status-to-visual binding · named extension points · the typeface, its weight
identity, and its licensing, provenance and distribution model.

Each is recorded in the
[Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
register or in the owning work package's architecture document. **Recording one
defers it; it does not decide, schedule, or authorize it.**

**Decided since this document was first written**, by the CDS-WP-020 Decision
Integration Pass (2026-08-27) and **effective** at the Human-Maintainer exact-byte
integration commit `42a568d823de3388e45af62967546f13ad67eff6`: the **colour space
and encoding** (DEC-S-128), the **contrast evaluation authority and precision
rule** (DEC-S-129), the **admitted
`$type` set** (DEC-S-130), and the **visual source-set unit, topology and maturity
granularity** (DEC-S-131). **None of the four creates a role, a role identifier, or
a value**, and **no contrast has been evaluated** — there is nothing to evaluate.

**Decided by the CDS Step-9 Decision Integration Pass (2026-09-05), and effective
at the Human-Maintainer exact integration commit
`2cb244e889c1a6b5a278afb233995a0379b5d9ef`:** the **identifier
grammar, the two identity spaces, and the concrete family and source-set roots**
(**DEC-S-132**, ADR-0005); the **per-scale ownership model and the topology/value
boundary** (**DEC-S-133**); the **role admission rule** (**DEC-S-134**); and the
**theme sequencing rule** (**DEC-S-135**). **None of the four creates a role, a
role identifier, a binding, or a value.** **The concrete role vocabulary stays
open, `CDS-WP-020A` may not invent it, and VP-6 stays UNSATISFIED.**

## Related documents

- [Visual Reference Token Foundation](VISUAL_REFERENCE_TOKEN_FOUNDATION.md)
- [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
- [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
- [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
- [Visual Foundation Typography Architecture](VISUAL_FOUNDATION_TYPOGRAPHY_ARCHITECTURE.md)
- [Visual Foundation Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md)
- [Visual Foundation Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md)
- [Visual Foundation Theme Architecture](VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
- [Visual Foundation Accessibility Mapping](../governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md)
- [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
- [Semantic Status Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
- [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md)
- [Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
- [Machine-Readable Validation Contract](MACHINE_READABLE_VALIDATION_CONTRACT.md)
