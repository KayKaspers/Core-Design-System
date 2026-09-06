# Visual Reference Token Foundation

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-020 — Reference and Semantic Token Foundation
- **Date:** 2026-08-26
- **Amended by:** CDS-WP-020 (Decision Integration Pass), 2026-08-27 — **RP-2**,
  the *Machine-readable disposition*, and the *Deferred decisions* section, to
  apply **DEC-S-128**, **DEC-S-130** and **DEC-S-131**
  ([ADR-0004](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md)).
  **Those amendments are effective** at the Human-Maintainer exact-byte
  integration commit `42a568d823de3388e45af62967546f13ad67eff6` (2026-08-27).
  **They select no value and create no identifier**, and RP-1, RP-3 … RP-10, ST-1 … ST-7,
  RN-1 … RN-9, RV-1 … RV-5 and RB-1 … RB-5 are unchanged.
- **Amended by:** CDS Step-9 Decision Integration Pass, 2026-09-05 — the *Naming at
  the reference position* section (identifier grammar and fixed family roots), the
  *What any future reference scale must satisfy* section (per-scale ownership and
  the topology/value boundary), and the *Deferred decisions* section, to apply
  **DEC-S-132**
  ([ADR-0005](../decisions/ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md))
  and **DEC-S-133**. **Those amendments are effective** at the Human-Maintainer
  exact integration commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`
  (2026-09-05). **They select
  no value and create no token, source set, or file**, and RP-1 … RP-10,
  ST-1 … ST-7, RN-1 … RN-9, RV-1 … RV-5 and RB-1 … RB-5 remain unchanged.
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for what a CDS visual reference token is** — token-flow
  layer **1 Reference** inside the visual foundation. It **selects no value**.
- **Maturity:** **`Proposed`** — this document promotes nothing and grants no
  maturity to any artifact (DEC-S-036, *No retrospective maturity*).

## Purpose and boundary

This document defines the **Reference layer of the CDS visual foundation**: what a
visual reference token is, what each visual family may hold at that layer, what
every reference token must carry, what it may never carry, and what any future
reference scale must satisfy.

Frame: [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md) —
Layer 3, token-flow layer 1. Its companion at token-flow layer 2 is the
[Visual Semantic Token Foundation](VISUAL_SEMANTIC_TOKEN_FOUNDATION.md).

### What this document is not

It **selects no value**: no colour, no colour space, no palette, no hue, no
typeface, no font stack, no weight, no size, no line height, no tracking, no
spacing step, no radius, no stroke width, no shadow, no opacity level, no
elevation step, no icon dimension, no motion value, and no breakpoint.

It also **creates no identifier**, no token source file, no schema, no validator
rule, no component, no brand, no theme, and no Product Profile, and it **resolves
no open decision**. The choices that would be required to author a real reference
value are recorded in the
[Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
register and are **not made here**.

> **No visual value exists in CDS.** The repository was searched at the revision
> this document was written and contains no colour value, no typographic value,
> and no dimensional value of any kind. This is verified, not assumed, and
> CDS-WP-020 creates none.

## Authority basis — this document registers no new decision

*(Normative — the load-bearing statement of this document)*

> **Every binding statement below is an application of a decision already in
> force. This document creates no new normative choice and registers no Decision,
> ADR, or risk.**

| This document's binding statements | Derive from |
| --- | --- |
| A reference token holds a raw value with no consumer meaning | DEC-S-024, token-flow layer 1 |
| Dependency runs strictly downward; a reference token never knows its purpose | DEC-S-024, DEC-S-079 |
| No consumer and no component binds a reference token directly | DEC-S-024, VF-I-3 |
| A reference position may carry an appearance name; a semantic position may not | DEC-S-081, N-1, VF-I-2 |
| Identifier segments follow the CDS identifier profile; a rename is a migration event | DEC-S-081, DEC-S-082, DEC-S-110 |
| Machine-readable expression is strict-JSON DTCG-profile source, validated V1–V4 | DEC-S-073 … DEC-S-082, ADR-0001 |
| Every source set carries an immutable source revision and full identity | DEC-S-080, DEC-S-031, RISK-062 |
| References and resolution fail closed | DEC-S-078, DEC-S-091 |
| Determinism and offline processing are mandatory | DEC-S-030, DEC-S-080 |
| Opacity is an attribute of VF-1 and VF-6, never a family | Shape and Surface Architecture, DEC-S-023 conservative reading |
| Colour is never the sole carrier of meaning | DEC-S-056, DEC-S-111, CR-006 |
| Maturity is granted by a gate, never by a document or metadata | DEC-S-035, DEC-S-036, DEC-S-126, VF-I-14 |
| Concrete visual values remain deliberately open until separately decided | DEC-S-032, DEC-S-003 |

Where a statement below could only be reached by making a **new** normative
choice, it is **not made**. It is recorded instead in the
[open-decision register](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md).

**The 2026-08-27 amendment does not change that.** Three of those recorded choices
have since been made — **by Decisions, under separate Human-Maintainer
authorization, not by this document**:

| Amended statement | Derives from |
| --- | --- |
| A visual colour reference value is authored in one canonical `srgb` representation; perceptual spaces are derivational only | **DEC-S-128**, ADR-0004 |
| A reference token declares its **own** explicit `$type` from the admitted set `color`, `dimension`, `number` | **DEC-S-130**, ADR-0004 |
| The source set is the independently evaluable unit; maturity binds to (`sourceSetId`, `sourceRevision`); aggregation confers nothing | **DEC-S-131**, ADR-0004 |

**This document still registers no Decision, ADR, or risk of its own**, and it
still selects no value and creates no identifier.

## What a reference token is

*(Normative)*

> **A reference token is a value without a purpose.**

That is the whole definition, and it is a restriction rather than a description.
The moment a reference token acquires a purpose — a role, a state, a status, a
component, a product, a channel, or a context — it has stopped being a reference
token and belongs at another layer.

| A reference token **owns** | A reference token **never owns** |
| --- | --- |
| A raw technical value in a declared `$type` | Any purpose, intent, or role |
| Its position in an ordered set, where its family declares one | Any status meaning (VF-I-6) |
| Its own identity, provenance, and lifecycle metadata | Any component knowledge (VF-I-4) |
| A declared family membership | Any product, consumer, or customer identity (N-2) |
| — | Any channel scope (N-3) |
| — | Any theme or context binding (T-8) |
| — | Any accessibility guarantee of its own |

### The last row is the one that is misread

A reference token **cannot** be accessible, because accessibility is a property of
a **pair, a composition, and a context**, none of which exists at layer 1. A
colour primitive has no contrast ratio; a *pair of roles resolved in a context*
does. Recording an accessibility guarantee on a primitive would place the
obligation where nothing can check it and where a theme could silently move it —
which is precisely the failure VF-I-8 exists to prevent.

The accessibility obligations of the visual foundation are declared at the
**semantic** layer. See the
[Visual Semantic Token Foundation](VISUAL_SEMANTIC_TOKEN_FOUNDATION.md).

## Which families hold reference tokens

*(Normative as a **register of positions**, not of content. **No identifier and no
value is created.** The primitive constructs named below are the ones the
CDS-WP-019 family architectures already register; this document adds none.)*

| Family | Registered reference constructs | Registered by |
| --- | --- | --- |
| **VF-1 Colour** | Colour primitive; alpha as an attribute of a colour value | [Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md) |
| **VF-2 Typography** | Typographic primitive; size scale; line-height model; tracking; the fallback chain bound to a family role | [Typography Architecture](VISUAL_FOUNDATION_TYPOGRAPHY_ARCHITECTURE.md) |
| **VF-3 Space and Size** | Spacing primitive; size primitive | [Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md) |
| **VF-5 Shape** | Radius primitive; stroke primitive | [Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md) |
| **VF-6 Surface and Elevation** | Shadow primitive; opacity as an attribute of overlay and scrim | [Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md) |

### Families that hold no reference token here

*(Normative — an exclusion, stated so that absence is not read as oversight)*

| Family | Why it holds none at this revision |
| --- | --- |
| **VF-4 Layout and Grid** | Grid structure, containers, content widths, and the responsive-range vocabulary are **CDS-WP-021's**, and the Layer 3 / Layer 5 split must be confirmed there first. A range is not a spacing primitive. |
| **VF-7 Iconography** | The icon system, its grid, and its licensing and provenance model are **CDS-WP-037's**. Icon extent and stroke are expressible as VF-3 and VF-5 primitives when a role needs them; **no icon-specific primitive family is opened here**. |
| **VF-8 Motion** | **CDS-WP-035 owns the Motion System.** No duration, easing, or threshold is defined, and none is prepared. |
| **VF-9 Theme and Context Mechanism** | A theme is a **resolution context, not a layer** (T-1, T-8). A context holds no primitive of its own; it selects among primitives that already exist. The mechanism is **CDS-WP-022's**. |

**Opacity is registered in no CDS scope statement** and is therefore positioned as
an **attribute** of VF-1 (alpha within a colour value) and VF-6 (overlay and
scrim), never as a family of its own. An opacity change is a colour change or a
surface change and inherits that family's obligations.

## Reference token obligations

*(Normative — every visual reference token, without exception)*

| # | Every visual reference token must | Source |
| --- | --- | --- |
| **RP-1** | Declare exactly one **family** from the register above | Visual Foundation Architecture, family register |
| **RP-2** | Declare an explicit **`$type`** of its own, drawn from the set the CDS profile admits — **`color`, `dimension`, `number`** (DEC-S-130). **Group- or root-level typing is not typing authority**, and a DTCG-known but CDS-unadmitted type fails closed. | CDS Token Format Profile, *The CDS `$type` admission profile* |
| **RP-3** | Hold a **raw value**, never an alias to a semantic, component, or profile token | DEC-S-024, DEC-S-079 |
| **RP-4** | Carry the **source-set identity** of the Reference Source Set it belongs to, including its **immutable source revision** | DEC-S-080, Token Metadata model |
| **RP-5** | Be **resolvable offline**, with no external service, registry, or network reference | DEC-S-030, DEC-S-091, invariant 12 |
| **RP-6** | Be **deterministic**: the same source revision yields the same value and the same digest | DEC-S-080, ADR-0002 |
| **RP-7** | Declare its **position in an ordered set**, where its family declares one, so that ordering is data rather than convention | Spatial and Shape architectures, ordered-scale constructs |
| **RP-8** | Carry **no purpose, role, state, status, component, product, consumer, channel, or context term** in its identifier or metadata | N-2 … N-5, VF-I-3, VF-I-4, VF-I-6 |
| **RP-9** | Carry **no accessibility guarantee of its own** — see *What a reference token is* above | VF-I-8, and the pair rule of the Colour Architecture |
| **RP-10** | Carry its **lifecycle state**, and on rename or removal a **migration reference** | DEC-S-082, DEC-S-040, Token Metadata model |

> **A reference token that satisfies RP-1 … RP-10 is still not usable by anyone.**
> That is intentional. Layer 1 is deliberately unusable on its own; usability
> begins at the semantic layer, which is where meaning, pairing, and obligation
> live.

## What any future reference scale must satisfy

*(Normative as **requirements on a scale**, not as a scale. **No topology, step
count, base unit, progression rule, or value is selected here** — that is
recorded as an open decision.)*

### Scale ownership and the topology/value boundary

*(Normative — **DEC-S-133**, CDS Step-9 Decision Integration Pass, 2026-09-05.
**Effective** at the Human-Maintainer exact integration commit
`2cb244e889c1a6b5a278afb233995a0379b5d9ef`. It applies
ST-1 … ST-7 and changes none of them. **No ADR** — DEC-S-133 is deliberately not an
architecture dependency of ADR-0005.)*

- **ST-1 … ST-7 are the common contract** binding every ordered primitive set.
- **There is no universal cross-family scale base.** A single base shared across
  heterogeneous families is rejected: **ST-5 is per-scale** — *"computable … from
  **its** declared base and rule"* — and a shared base would create the
  cross-family coupling **AF-3** exists to prevent.
- **Each ordered primitive set independently owns** its anchor declaration, its
  ordering, its progression-rule kind, its step-count decision, its extension
  behaviour, and its exclusions and declared deviations. **No family's scale
  derives base, rule, or value authority from another family's.**
- **`SCALE TOPOLOGY ≠ SCALE VALUES`.** A topology states how a scale is structured
  and states no magnitude.
- **VP-3's "base" means the anchor declaration** — the structural anchor position —
  **not a numeric anchor magnitude.** A magnitude is a value, governed by value
  selection.
- **Scope:** VF-2, VF-3, VF-5 and VF-6. **Opacity remains an attribute** of VF-1 and
  VF-6 (DEC-S-128 clause 11); **no standalone opacity family exists.**
  **Excluded:** VF-1 tonal topology, VF-4, VF-7, VF-8 and VF-9.
- **The per-family topology parameters are not decided.** For every family in
  scope, the concrete anchor declaration, progression-rule kind, step count,
  extension behaviour and exclusions **remain open**, and **VF-1 tonal topology is a
  separate open residual**. **VP-3 therefore remains UNSATISFIED for every
  family**, and **no value may be selected.**

Several visual families hold **ordered** primitive sets: a size scale, a spacing
scale, a radius scale, a stroke set, an elevation set, an opacity set. CDS selects
none of them. Any scale later proposed must satisfy the following, and a scale
that cannot is the wrong scale — not a reason to weaken a requirement.

| # | Requirement |
| --- | --- |
| **ST-1** | **The order is declared, not inferred.** A consumer, a tool, or a validator must be able to read the ordering from the source rather than from the values, so that an ordering change is a detectable change. |
| **ST-2** | **The progression rule is stated.** Whether steps are uniform, modular, hybrid, or enumerated must be recorded with the scale, because an unstated rule cannot be reviewed, extended, or migrated. |
| **ST-3** | **Extension is possible without renumbering.** A scale whose only way to add a step is to renumber existing steps makes every addition a breaking change (BC-1) and a migration event. |
| **ST-4** | **A step name states a position, not an importance.** A rank that the system does not actually guarantee must not be encoded in a step name (N-7). |
| **ST-5** | **The scale is computable offline and deterministically** from its declared base and rule, with no external service (DEC-S-030, DEC-S-080). |
| **ST-6** | **Steps are not semantically pre-assigned.** A scale step acquires purpose only by being aliased from a semantic role; a scale that reserves steps for purposes has smuggled the semantic layer into layer 1. |
| **ST-7** | **The scale declares what it does not cover.** A range a family deliberately omits is stated as omitted, so that a later gap is a known gap rather than a discovery (VF-I-11 applied to scales). |

### Why no scale is selected

Selecting a scale topology fixes step count, base unit, and progression rule
simultaneously, and every one of those propagates into every family that derives
from it, into every future role that aliases it, into every channel
transformation, and into the target-size floor (2.5.8). No registered consumer
requirement asks for a spacing scale, a size scale, or a radius scale — **VF-3,
VF-5, VF-6, and VF-7 carry no consumer demand evidence at all** — so there is no
evidenced need that would justify fixing it ahead of the decision.

## Naming at the reference position

*(Normative — an application of DEC-S-081 and the CDS-WP-019 naming model.
**No token identifier is created, adopted, reserved, recommended, or planned.**
The **family roots** below are fixed by DEC-S-132; nothing beneath a root is.)*

### Grammar and roots

*(Normative — **DEC-S-132**, 2026-09-05. **Effective** at the Human-Maintainer
exact integration commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`.
[ADR-0005](../decisions/ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md)
carries the rationale.)*

A reference position takes **`<family>.<primitive-group>.<step>[.<qualifier>]`**.
The path is **family-rooted**; the **token-flow layer is never a segment** of it and
remains the explicit `layer` field; the **qualifier** position is **declared and
optional and no concrete qualifier is created** — the term is `qualifier` rather
than `modifier` because *conditional modifier* is already bound to Resolver / Theme
composition semantics.

The fixed technical roots are **`color`** (VF-1), **`typography`** (VF-2),
**`space`** (VF-3), **`shape`** (VF-5) and **`surface`** (VF-6) — one root per
registered family, with a compound display name producing **one** root and the
`<primitive-group>` position differentiating internal constructs. The Reference
Source Set identities are **`reference/color`**, **`reference/typography`**,
**`reference/space`**, **`reference/shape`** and **`reference/surface`**, in the
flat **`<layer>/<family>`** form; a `sourceSetId` is **declared, never derived**
from a path (DEC-S-131 clause 3), and **token-path identity and source-set identity
are separate spaces**.

**This creates no Source Set instance, no `sourceRevision`, no manifest, no
resolver, no token, and no file. Visual source sets remain 0.**

| # | Rule |
| --- | --- |
| **RN-1** | **A reference position may carry an appearance name.** A primitive may legitimately be named for what it is; this is the one position in the visual foundation where that is permitted (N-1). |
| **RN-2** | Segment syntax is the CDS identifier profile: dot-free segments matching `^[a-z][a-z0-9-]*$` within a group hierarchy, technical identifiers separate from display labels, case-only collisions prohibited (DEC-S-081, DEC-S-110). |
| **RN-3** | **No product, brand, customer, or consumer term** appears in a shared foundation identifier (N-2). |
| **RN-4** | **No channel term** appears in a shared identifier (N-3). |
| **RN-5** | **No status axis or status value name** is reused (N-4, VF-I-6). |
| **RN-6** | **No component name** appears (N-5). |
| **RN-7** | **No theme or profile term** appears — both are resolution inputs, never path segments (N-6, T-8). |
| **RN-8** | Every rule above is **machine-checkable**; a naming rule that cannot be expressed as a check is guidance, not a rule (N-8). |
| **RN-9** | **A rename is a migration event** with a migration reference, never a silent repurposing (DEC-S-082). |

**The concrete path grammar is not fixed here.** Whether a reference path is
family-rooted, layer-rooted, or something else is an open decision, recorded as
**OD-4** in the
[open-decision register](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md).
The CDS-WP-019 illustration of path *shape* remains an example artifact and is
**never normative** (VF-I-13).

## Provenance, identity and lifecycle

*(Normative — an application of the
[Token Metadata, Provenance and Identity Model](TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md))*

A visual Reference Source Set carries the same identity every normative source set
carries: source-set ID, CDS profile version, DTCG report version, immutable source
revision, maturity state, approval state, owner role, layer, and dependency set.
An identity missing any required element **fails closed at V3**.

| # | Rule |
| --- | --- |
| **RV-1** | **`latest` is never an identity.** Evidence, outputs, and claims reference a specific source revision (DEC-S-080). |
| **RV-2** | **A digest is not a signature.** RFC 8785 canonicalization plus SHA-256 is an integrity aid and proves no authorship, approval, or release (DEC-S-090, DEC-S-100, RISK-072). |
| **RV-3** | **Metadata is not authority.** A source set declaring `Candidate` is not Candidate; only a gate grants maturity (VF-I-14, DEC-S-126, VR-4). |
| **RV-4** | **Evidence never transfers** across a source revision, a family, a channel, a context, or a consumer (DEC-S-126, EV-5). |
| **RV-5** | **No secret and no personal data** appears in a token source, its metadata, or its provenance record. |

## Machine-readable disposition

*(Normative as a **disposition**; **nothing is implemented**)*

**CDS-WP-020 creates no visual token source file, no manifest, no resolver, no
schema, and no validator rule.** The reason is recorded plainly, because a silent
omission would be indistinguishable from an oversight:

| Element | State |
| --- | --- |
| Format authority | **Sufficient.** Strict JSON `.tokens.json` under the CDS Token Format Profile over pinned DTCG 2025.10 (DEC-S-073 … DEC-S-075, ADR-0001). |
| Source-set classes | **Sufficient.** Reference Source Set, Semantic Source Set, Source-Set Manifest, and Resolver are already defined classes (Machine-Readable Source Model). |
| Reference and alias semantics | **Sufficient.** Fail-closed references and the declared local graph are decided (DEC-S-078, DEC-S-091). |
| Serialization and digest | **Sufficient.** RFC 8785 + SHA-256 (ADR-0002, DEC-S-090). |
| Structural schema | **Sufficient without change.** The committed token-document schema constrains structure, the CDS payload, and segment naming; it places no visual-specific constraint and needs none to accept a structurally valid visual document. |
| Colour space and encoding | **DECIDED — DEC-S-128** (OD-1 answered). One canonical space keyed `srgb`, perceptual spaces derivational only. The CDS-specific `hex` disposition stays a recorded residual. |
| Admitted `$type` set | **DECIDED — DEC-S-130** (OD-2 answered). Exactly `color`, `dimension`, `number`, with explicit own typing required and composites unadmitted. The offline validator's bounded V2 type set remains a **validator scope boundary under DEC-S-098**, not a CDS profile admission, and must not be read as one (RISK-074). Font-family and font-weight identity stays a recorded residual. |
| Source-set identity and topology | **DECIDED — DEC-S-131** (OD-3 answered) for the **unit, topology and maturity granularity**: one source set per independently evaluable Family × Token-Flow-Layer unit; maturity binds to (`sourceSetId`, `sourceRevision`); aggregation confers nothing. **The concrete root identifiers are decided by DEC-S-132** (effective at commit `2cb244e8…`), which creates **no instance**. Repository topology remains an explicit DEC-S-032 deferral. |
| Concrete identifiers | **DECIDED — DEC-S-132** (OD-4 answered), **effective at commit `2cb244e8…`**: the grammar, the two identity spaces, and the fixed family and source-set roots. **No identifier instance, Source Set, or `sourceRevision` exists.** |
| Concrete values | **Insufficient.** **VP-3, VP-5, VP-6 and VP-7 are unsatisfied**, VP-2 is unsatisfied for typeface identity, weight identity and composites, and the per-family topology parameters, **VF-1 tonal topology** and the **concrete role vocabulary** stay open. |

> **The machinery was always sufficient; the decisions were not.** Three of the
> blocking choices are made and effective — **DEC-S-128, DEC-S-130 and DEC-S-131**,
> with
> [ADR-0004](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md)
> recording the rationale — and the remaining four are decided by the CDS Step-9
> Decision Integration Pass (**DEC-S-132 … DEC-S-135**, with **ADR-0005**), **and
> are effective**. **That still does not permit a source set to
> be written.** **VP-3, VP-5, VP-6 and VP-7 remain unsatisfied for every family**,
> VP-2 remains unsatisfied for typeface identity, weight identity and composites,
> and **only VP-4 moves** — because **deciding an identifier is not creating one**.
> Writing a file anyway would settle the remaining choices by implication —
> acquiring authority instead of receiving it, which DEC-S-033 prohibits.
> **Authority is granted, never acquired.**

## Validation requirements

*(Stated as **requirements on CDS-WP-024**. **No validator is changed here, no
schema is added, and no diagnostic is introduced.**)*

A later validator must be able to detect, at the reference layer:

| # | Detection |
| --- | --- |
| 1 | A reference token with **no declared family** |
| 2 | A reference token with **no explicit `$type`**, or a `$type` outside the admitted set |
| 3 | A reference token whose value is an **alias** rather than a raw value |
| 4 | A reference token carrying a **purpose, role, state, status, component, product, consumer, channel, theme, or profile** term |
| 5 | A **reference token depending on a semantic, component, or profile token** — any upward dependency |
| 6 | A **component or consumer binding a reference token directly** (VF-I-3, DEC-S-024) |
| 7 | An **ordered set whose ordering is not declared** (ST-1) or whose progression rule is unstated (ST-2) |
| 8 | A **case-only identifier collision** or a segment violating the naming profile |
| 9 | A **missing or non-immutable source revision**, or an identity missing a required element |
| 10 | A **network or non-local reference** of any kind |

**A pass proves structure, never correctness.** A pass at one layer proves nothing
about the next (VR-1); a `Fail` or `Blocked` stops later layers, which are recorded
`Not assessed` and never assumed passed (VR-2); and **an automated check is never
sufficient accessibility evidence** (DEC-S-053).

## Theme and Product Profile boundary at the reference layer

*(Normative)*

| # | Rule |
| --- | --- |
| **RB-1** | **A theme never adds, removes, or edits a reference token.** A context re-binds which primitive a role resolves to; it does not touch the primitive set (T-1, T-2, VF-I-9). |
| **RB-2** | **A Product Profile never reaches layer 1.** A profile enters at token-flow layer 4 and overrides values only at **named, approved extension points** (DEC-S-025, DEC-S-043). |
| **RB-3** | **No extension point is named today**, so **no reference value is overridable by anyone** (CDS-WP-032). |
| **RB-4** | **A context must not become a back door.** Overriding through a context what a profile may not override directly is the same violation with an extra step. |
| **RB-5** | **A consumer never binds a reference token.** Doing so imports a value and discards its purpose (VF-I-3), and it is the shortcut that makes theming, profiles, and channel transformation impossible simultaneously. |

## Evidence and claim boundary

- Every visual reference artifact in CDS is **AE-0**. **None exists**, none has
  been rendered, measured, printed, or evaluated.
- **No contrast has been measured**, because there is nothing to measure, and
  because contrast is not a property of a primitive in any case.
- **No accessibility claim of any level is valid**, by anyone, including CDS
  itself (DEC-S-050).
- The single admitted evidence package in CDS — **`AE1-CDS-WP016-SEMSTATUS-004`**
  at **AE-1** — covers the channel-independent Semantic Status source/contract
  family only and **does not transfer here** (DEC-S-126, AF-2, EV-5).
- **Visual foundation families at `Candidate`: 0. At `Stable`: 0.** Publication
  remains **`Private Development`**; there is no release and no tag.

## Deferred decisions

Every concrete reference value · palette and hue set · **per-family scale topology
parameters** — the concrete anchor declaration, progression-rule kind, step count,
extension behaviour and exclusions, for each family in scope · **VF-1 tonal
topology** · the typeface, its weight identity, and its fallback chain · the
identifier vocabulary **beneath a fixed family root** · the CDS-specific `hex`
disposition · composite type admission · **any migration or deprecation
compatibility mechanism outside the normative Semantic alias graph** · icon
dimensions · motion values · named extension points.

Each is recorded, with alternatives and an impact statement, in the
[Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
register. **Recording one defers it; it does not decide, schedule, or authorize
it**, and each requires its own explicitly authorized decision.

**Decided since this document was first written**, by the CDS-WP-020 Decision
Integration Pass (2026-08-27) and **effective** at the Human-Maintainer exact-byte
integration commit `42a568d823de3388e45af62967546f13ad67eff6`: the **colour space
and encoding** (DEC-S-128), the **admitted `$type` set** (DEC-S-130), and the **visual source-set unit, topology
and maturity granularity** (DEC-S-131). **None of the three selects a value or
creates an identifier.**

**Decided by the CDS Step-9 Decision Integration Pass (2026-09-05), and effective
at the Human-Maintainer exact integration commit
`2cb244e889c1a6b5a278afb233995a0379b5d9ef`:** the **identifier
grammar, the two identity spaces, and the concrete family and source-set roots**
(**DEC-S-132**, ADR-0005), and the **per-scale ownership model and the
topology/value boundary** (**DEC-S-133**). **Neither selects a value**, and
DEC-S-132 creates **no Source Set instance and no token** — it fixes identity, not
artifacts. **The per-family topology parameters above stay open, VF-1 tonal
topology stays open, and VP-3 stays UNSATISFIED for every family.**

## Related documents

- [Visual Semantic Token Foundation](VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
- [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
- [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
- [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
- [Visual Foundation Typography Architecture](VISUAL_FOUNDATION_TYPOGRAPHY_ARCHITECTURE.md)
- [Visual Foundation Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md)
- [Visual Foundation Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md)
- [Visual Foundation Theme Architecture](VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
- [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
- [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md)
- [Machine-Readable Source Model](MACHINE_READABLE_SOURCE_MODEL.md) · [CDS Token Format Profile](CDS_TOKEN_FORMAT_PROFILE.md)
- [Token Metadata, Provenance and Identity Model](TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md)
- [Machine-Readable Validation Contract](MACHINE_READABLE_VALIDATION_CONTRACT.md)
