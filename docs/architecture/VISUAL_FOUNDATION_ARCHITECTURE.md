# Visual Foundation Architecture

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Amended by:** CDS Step-9 Decision Integration Pass, 2026-09-05 — the **naming
  model** (**N-6** reconciled to `qualifier`, and the fixed family roots recorded)
  and **deferred decisions 2 and 3**, to apply **DEC-S-132**
  ([ADR-0005](../decisions/ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md))
  and **DEC-S-134**. **Those amendments are effective** at the Human-Maintainer
  exact integration commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`
  (2026-09-05). **They select
  no value, create no token identifier, and create no role identifier**, and
  VF-1 … VF-9, VF-I-1 … VF-I-14, N-1 … N-5 and N-7 … N-8 are unchanged.
- **Amended by:** CDS-WP-021 — Adaptive Layout and Responsive Foundation,
  2026-09-06 — **deferred decision 4 only**, and one *Related documents* row, to
  record the Human-Maintainer decision on **`WP021-D1`** (**`DEC-S-136`**,
  **ADR-0006**) and the deferral of **`WP021-D2`**.
  **That amendment is effective** at the Human-Maintainer exact-object integration
  commit `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9` (2026-09-11) of the exact
  reviewed CDS-WP-021
  Working Tree object. **It selects no value, creates no identifier, and grants
  VF-4 no technical root**, and **VF-1 … VF-9, VF-I-1 … VF-I-14, N-1 … N-8, the
  family register, the maturity of every family, and the deferred decisions
  1 … 3 and 5 … 15 are unchanged.**
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for the structure of the CDS visual foundation** upon
  Human-Maintainer commit. It defines **how** visual foundations are structured,
  governed, represented, extended, validated, and consumed.
- **Maturity of everything it positions:** **`Proposed`** — this document
  **promotes nothing** and grants no maturity to any artifact (DEC-S-036,
  *No retrospective maturity*).

## Purpose and authority

This document is the **entry point for the CDS visual foundation**. It defines the
frame; the specialised documents under
[Related documents](#related-documents) hold the detail and must not be
duplicated here.

It is subordinate to
[Concept and Scope](../governance/CONCEPT_AND_SCOPE.md) and the
[Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md). On conflict with
either, **fail closed and escalate** (DEC-S-023, DEC-S-034).

### What this architecture is

A **structural** architecture for **Layer 3 — Foundations and Tokens**, restricted
to its visual families. It describes what exists, where each thing lives, which
direction dependencies run, and which constraints every later design decision must
satisfy.

### What this architecture is not

It selects **no visual value**. Specifically, it chooses no colour, no palette, no
typeface, no font stack, no size, no spacing value, no radius, no stroke width, no
shadow, no opacity value, no icon, no illustration, no motion duration, no
breakpoint, no theme instance, no brand, and no Product Profile.

It also creates **no token source file**, **no component**, **no channel adapter**,
**no schema**, **no validator rule**, and **no evidence**.

**No visual value exists in CDS.** At the revision this document was written, the
repository contained **no colour value, no typographic value, and no dimensional
value of any kind** — verified by search, not assumed.

## Authority basis — this architecture registers no new decision

*(Normative — the load-bearing statement of this document)*

> **Every binding statement below is an application of a decision already in
> force. This work package creates no new normative choice, and therefore
> registers no new Decision.**

CDS change control requires a Decision Index entry **where a registered decision
changes** (see the change-control clause of the
[Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md)). No registered
decision changes here.

| This document's binding statements | Derive from |
| --- | --- |
| The visual foundation is Layer 3; it may depend on Layers 1–2 only | DEC-S-021 and the allowed-dependency table |
| The visual foundation introduces no new layer | DEC-S-024 — *exactly five* token-flow layers |
| Semantic roles precede values; appearance names are prohibited in semantic positions | DEC-S-024, semantic-first principle |
| A Product Profile varies only approved extension points and never weakens shared semantics or accessibility | DEC-S-025, invariant 10 |
| Channels may transform presentation but never meaning | DEC-S-029, invariant 13 |
| Generated visual output is never normative and always carries provenance | DEC-S-022, DEC-S-031, DEC-S-079 |
| Concrete visual values remain deliberately open | DEC-S-032, DEC-S-003 |
| Colour is never the sole carrier of meaning; visible focus and non-sensory meaning are CDS obligations | DEC-S-049, DEC-S-052, DEC-S-056, CR-006, CR-021 |
| A target is not a claim; an automated check is not evidence | DEC-S-050, DEC-S-053 |
| Non-web channels need a channel profile before Candidate or Stable | DEC-S-058 |
| Naming follows the CDS identifier profile; a rename is a migration event | DEC-S-081, DEC-S-082 |
| Machine-readable expression is strict-JSON DTCG-profile source, validated V1–V4, deterministically serialized | DEC-S-073 … DEC-S-092, ADR-0001, ADR-0002 |
| The five status axes are independent and no visual encoding may replace them | DEC-S-105, DEC-S-111, DEC-S-112 |
| A channel accessibility profile gates channel artifacts, not channel-independent Layer-3 sources | DEC-S-125 |
| Maturity is granted only by a gate, never by a document | DEC-S-035, DEC-S-036, DEC-S-126 |

Where a statement below could only be reached by making a **new** normative
choice, it is **not made**. It is recorded instead under
[Deferred decisions](#deferred-decisions) with the work package that must resolve
it.

## Position in the eight-layer model

*(Normative — no change to DEC-S-021)*

The visual foundation is the visual half of **Layer 3 — Foundations and Tokens**,
whose registered content is *"Colour, typography, space and size, grid and layout,
shape, elevation, motion, iconography, design tokens, theme mechanisms, semantic
status foundations"*.

| Relationship | Rule |
| --- | --- |
| **Layer 1 — Strategy and Governance** | The visual foundation depends on it. Governance, maturity, claims, and accessibility policy are decided there, never here. |
| **Layer 2 — Brand and Identity** | The visual foundation **may** depend on it. Brand marks, logos, product identity, and brand assets are **owned there, not here** — see the [Brand and Product Profile Boundary](../governance/VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md). |
| **Layer 4 — Components** | **Prohibited dependency.** No visual foundation exists because a component wants it (prohibited dependency 2). |
| **Layer 5 — Patterns and Experiences** | **Prohibited dependency.** Viewport strategy and flow-level behaviour live there. |
| **Layer 6 — Channels and Communication** | **Prohibited dependency.** A channel may transform presentation; it may not push a requirement down into the foundation (prohibited dependency 3). |
| **Layer 7 — Distribution and Enablement** | Consumes generated visual output; decides nothing here. |
| **Layer 8 — Evidence and Quality** | Observes; commands nothing (prohibited dependency 6). |

## Position in the five-layer token flow

*(Normative — no change to DEC-S-024)*

The visual foundation does **not** introduce a layer model of its own. It occupies
positions inside the one that already exists:

```text
Reference Tokens
   → Semantic Tokens
      → Component Tokens
         → Product Profile Overrides
            → Channel or Platform Outputs
```

| Token-flow layer | What the visual foundation contributes | Owned by |
| --- | --- | --- |
| **1 Reference** | Visual primitives with **no consumer meaning** — the raw material of a family. | CDS-WP-020 |
| **2 Semantic** | **Visual roles** — what a decision is *for*. This is where the visual foundation actually lives and where a human argument about intent is possible. | CDS-WP-020 |
| **3 Component** | Binding of visual roles to component contracts. **Introduces no visual meaning and no raw value.** | CDS-WP-026 and later |
| **4 Product Profile** | Approved, bounded variation at **named extension points**. **No extension point is named today.** | CDS-WP-032 |
| **5 Channel or Platform Output** | Generated, provenance-carrying, never hand-edited, never normative. | CDS-WP-048 and later |

### Reconciliation of the conceptual A–D reading

A four-part reading of the visual foundation (primitive → semantic → context →
brand) is a useful **description**. It is **not** a CDS layer model, and it must
not be recorded as one. Its parts map as follows:

| Conceptual part | CDS construct | Note |
| --- | --- | --- |
| **A — Primitive visual foundations** | Token-flow layer **1 Reference** (Reference Source Set) | Same thing, existing name |
| **B — Semantic visual foundations** | Token-flow layer **2 Semantic** (Semantic Source Set) | Same thing, existing name |
| **C — Context / theme mapping** | **Not a layer.** A **resolution context**, composed by a Resolver / Composition document | See the [Theme Architecture](VISUAL_FOUNDATION_THEME_ARCHITECTURE.md) |
| **D — Brand / Product Profile mapping** | Token-flow layer **4 Product Profile** (Product Profile Source Set), bounded by Layer 2 brand governance | Two different authorities, not one |
| *(absent from the conceptual reading)* | Token-flow layer **3 Component** | **Must not be dropped.** Omitting it is how a component silently binds a reference token and strips meaning |

**Treating C as a layer is an architectural defect**, because it would make a
presentation context capable of holding a decision. A context selects among
approved values; it never introduces one.

## The visual foundation families

*(Normative — a register of scope, not of content)*

Each family is a **separate artifact family** with its own maturity, evidence, and
gate. **Maturity is never inherited between families.**

| ID | Family | Owns | Registered by | Consumer anchor | Owning work package |
| --- | --- | --- | --- | --- | --- |
| **VF-1** | **Colour** | Colour primitives and semantic colour roles; foreground and background pairing; contrast-capability declarations | DEC-S-021 L3 *"Colour"* · scope domain 3 | CR-006 (non-colour rule), CR-025 | CDS-WP-020 |
| **VF-2** | **Typography** | Family roles, weight roles, size scale, line height, tracking, text roles | DEC-S-021 L3 *"typography"* · scope domain 3 | CR-023 (flexible text, DE/EN) | CDS-WP-020 |
| **VF-3** | **Space and Size** | Spacing scale, sizing scale, density model, target sizing | DEC-S-021 L3 *"space and size"* · scope domain 3 | — **none** | CDS-WP-020 |
| **VF-4** | **Layout and Grid** | Grid structure, containers, content widths, responsive range vocabulary | DEC-S-021 L3 *"grid and layout"* · scope domain 3 | CR-004 **at Layer 5** — see the [Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md) | CDS-WP-021 |
| **VF-5** | **Shape** | Radius scale, stroke and border architecture, separators | DEC-S-021 L3 *"shape"* · scope domain 3 | — **none** | CDS-WP-020 |
| **VF-6** | **Surface and Elevation** | Surface hierarchy, elevation model, shadow primitives, overlays and scrims | DEC-S-021 L3 *"elevation"* · scope domain 3 | — **none** | CDS-WP-020 |
| **VF-7** | **Iconography** | System icon contract, grid and stroke discipline, semantic versus decorative classification | DEC-S-021 L3 *"iconography"* | — **none** | CDS-WP-037 |
| **VF-8** | **Motion** | Duration and easing categories, reduced-motion principle, functional versus decorative motion | DEC-S-021 L3 *"motion"* · scope domain 3 | CR-022 (motion restraint) | **CDS-WP-035** — boundary only here |
| **VF-9** | **Theme and Context Mechanism** | How a presentation context re-binds semantic roles to primitives | DEC-S-021 L3 *"theme mechanisms"* · scope domain 3 | CR-025 (light and dark) | CDS-WP-022 |

### What is deliberately not a family

*(Normative — each of these is positioned, not registered as new scope)*

| Subject | Position | Why |
| --- | --- | --- |
| **Opacity** | An **attribute** of VF-1 (alpha) and VF-6 (overlay, scrim). **Not an independent family.** | Opacity is named in **no** registered scope statement. Positioning it as an attribute of two registered families registers **less**, not more — the conservative reading required by DEC-S-023. |
| **Illustration and imagery** | **Layer 2 — Brand and Identity**, consumed by the visual foundation through a declared interface. **Not a Layer-3 family.** | DEC-S-021 Layer 3 registers *iconography* and does **not** register illustration or imagery; Layer 2 registers *"logos and brand assets"*. See the [Iconography and Imagery Architecture](VISUAL_FOUNDATION_ICONOGRAPHY_AND_IMAGERY_ARCHITECTURE.md). |
| **Focus indication** | A **cross-family semantic role set** drawing on VF-1, VF-5, and VF-3. | Visible focus is a mandatory CDS obligation (2.4.7, CR-021, DEC-S-055) that no single family owns. Modelling it as a family would let one family's change silently weaken it. |
| **Interaction and validation states** | **Semantic roles inside the existing families**, only where they are component-independent. | A state that cannot be expressed without knowing a component is **Layer 4**, not Layer 3 (prohibited dependency 2). |
| **Data-visualization encoding** | **Layer 6**, owned by **CDS-WP-039**. The visual foundation supplies roles; it defines no chart encoding. | Registered as a channel class, not as a foundation family. |
| **Audio, haptics, multimodal feedback, agent interaction** | **Outside registered CDS scope.** Not positioned, not registered, not prepared. | Registered in **none** of the six capability domains and **no** channel model. Extension requires an Elevated scope change with Human-Maintainer approval. |

## Visual foundation invariants

*(Normative — each must hold in every family, mapping, context, profile, and
output)*

| # | Invariant |
| --- | --- |
| **VF-I-1** | **The visual foundation introduces no layer.** Every visual construct occupies a position in the existing eight-layer model and the existing five-layer token flow. |
| **VF-I-2** | **A semantic role is never named after its appearance.** An appearance name in a semantic position forecloses theming, profiles, and channel transformation simultaneously. |
| **VF-I-3** | **No consumer-facing binding to a reference token.** Binding to a primitive imports a value and discards its meaning. |
| **VF-I-4** | **No visual foundation exists because one component needs it.** Semantics precede components. |
| **VF-I-5** | **Colour is never the sole carrier of meaning** — nor is icon, shape, position, size, elevation, or motion. This holds in **every** channel, including print. |
| **VF-I-6** | **A visual role never replaces a semantic status axis.** Visual encoding is redundant to meaning, never a substitute for it. |
| **VF-I-7** | **An interaction state is not a semantic status.** A non-interactive state, a selection state, a pointer-emphasis state, and a validation outcome are presentation states; `condition`, `severity`, `confidence`, `freshness`, and `evidence` are status meaning. Conflating them destroys both. |
| **VF-I-8** | **Every semantic colour role declares whether it is contrast-sensitive, and against what.** A role whose contrast obligation is unstated cannot be validated, themed, or profiled safely. |
| **VF-I-9** | **A presentation context re-binds; it never redefines.** A theme may change which primitive a role resolves to. It may never change what the role means, remove the role, or weaken an accessibility guarantee. |
| **VF-I-10** | **A Product Profile varies values at named extension points only.** Roles, semantics, accessibility guarantees, and status truth are not variable. |
| **VF-I-11** | **Channel outputs may differ in form and never in meaning.** A distinction a channel cannot render must be **declared as a limitation**, never silently dropped. |
| **VF-I-12** | **Generated visual output is never normative**, is never hand-edited, and always identifies its source and transformation revision. |
| **VF-I-13** | **An example is never normative.** An illustrative name or value acquires no authority through repetition, citation, or convenience. |
| **VF-I-14** | **Maturity is granted by a gate, never by a document, a metadata field, a validator pass, or a renderer.** |

## Relationship to the Semantic Status Foundation

*(Normative — the sharpest boundary in this document)*

The [Semantic Status Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
remains **authoritative for status meaning**. It is the only **Candidate** artifact
family in CDS (`semantic/status`, source revision
`semantic-status-rev-0002-candidate`, `Candidate` / `Approved`), and this work
package changes **nothing** about it — not its source, not its revision, not its
maturity, not its evidence.

> **COLOUR ≠ STATUS · ICON ≠ STATUS · MOTION ≠ STATUS · ELEVATION ≠ STATUS**

| Rule | Statement |
| --- | --- |
| **Meaning stays where it is** | The five axes (`condition`, `severity`, `confidence`, `freshness`, `evidence`) and their 25 values are defined by the status contract. The visual foundation defines **no** status meaning. |
| **Visual encoding is redundant** | Any future visual expression of status is an **additional, redundant modality** bound to an existing meaning. Redundancy is additive; contradiction is a defect. |
| **Text first** | Every status remains communicable **non-visually**, as text and accessible semantics, in every channel. Removing all visual encoding must remove **no** meaning. |
| **No aggregation** | No visual construct may collapse the five axes into one opaque signal. `unknown` must never render as `nominal`, `stale` never as `current`, `unverified` never as `verified`. |
| **Naming separation** | A visual role must **not** be named after a status axis or a status value in a way that implies equivalence. A role named for a feedback purpose is a presentation role, not a status. |
| **The binding is not made here** | **How** visual roles bind to status axes is **CDS-WP-023 — Semantic Status Visual Binding Contract**, and it is gated by **CDS-WP-024** (render gate) and **CDS-WP-025** (negative-fixture expansion). A status that cannot be validated must not be rendered as though it were. |

**This work package defines no status-to-visual mapping**, proposes none, and
prepares no binding beyond stating the constraints any future binding must satisfy.

## Interaction and validation states

*(Normative)*

The visual foundation may carry semantic roles for states that are genuinely
**component-independent** — for example an available state, a non-interactive
state, a current-selection state, a pointer-emphasis state, and a
validation-feedback state.

Constraints:

1. A state role that cannot be described without naming a component is **Layer 4**
   and does not belong here (VF-I-4).
2. A state role must be **programmatically determinable**, not signalled only by
   appearance (4.1.2; Accessibility Requirements Baseline 7.6).
3. A **non-interactive or read-only** state must remain perceivable and must not be
   communicated by reduced contrast alone.
4. A **validation-feedback** role is not a status axis value (VF-I-7). A form error
   is a validation outcome; it is not a status `condition`.
5. A **destructive or far-reaching** action's risk tier is a **contract** concern
   (Layer 4, CR-010) that the foundation may supply roles for and must not decide.
6. The **concrete state vocabulary is not fixed here.** It is CDS-WP-020's, under
   the naming model below.

## Naming model

*(Normative — an application of DEC-S-081; **no shipped identifier is created**)*

The CDS identifier profile already governs form: technical identifiers are stable,
language-neutral, dot-free segments matching `^[a-z][a-z0-9-]*$` within a group
hierarchy, separate from human-facing display labels, with case-only collisions
prohibited and renames treated as migration events (DEC-S-081, DEC-S-082,
DEC-S-110).

The visual foundation adds the following **naming principles**:

| # | Principle |
| --- | --- |
| **N-1** | **Semantic positions carry role names; reference positions may carry appearance names.** A primitive may legitimately be named for what it is. A role may not. |
| **N-2** | **No product, brand, customer, or consumer term** appears in a shared foundation identifier. |
| **N-3** | **No channel term** appears in a shared semantic identifier. A channel is a scope, not a meaning. |
| **N-4** | **No status axis or status value name** is reused as a visual role name (VF-I-6, VF-I-7). |
| **N-5** | **No component name** appears in a Reference or Semantic identifier. |
| **N-6** | **The path encodes family, role, and qualifier** — not a value, a theme, or a profile. Theme and profile are **resolution inputs**, never path segments in a shared semantic identifier. *(The slot was originally worded "modifier"; **DEC-S-132** renamed it to **`qualifier`** because *conditional modifier* is already bound to Resolver / Theme composition semantics. **The principle is unchanged** — only the term is.)* |
| **N-7** | **A name states a purpose, not a rank**, wherever a rank would be read as an importance the system does not actually guarantee. |
| **N-8** | **Deterministic and machine-checkable.** Any naming rule that cannot be expressed as a check is guidance, not a rule. |

### Identifier grammar and family roots

*(Normative — **DEC-S-132**, CDS Step-9 Decision Integration Pass, 2026-09-05.
**Effective** at the Human-Maintainer exact integration commit
`2cb244e889c1a6b5a278afb233995a0379b5d9ef`.
[ADR-0005](../decisions/ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md)
carries the rationale. **No token, role, source set, or value is created.**)*

| # | Rule |
| --- | --- |
| **Family-rooted** | A visual token path begins with a **single segment naming a registered visual family**. |
| **Reference grammar** | `<family>.<primitive-group>.<step>[.<qualifier>]` |
| **Semantic grammar** | `<family>.<role>[.<qualifier>]` |
| **Qualifier** | The qualifier position is **declared and optional**, and **no concrete qualifier is created**. Declaring the position is not permission to populate it. |
| **Layer** | The token-flow layer is **never a token-path segment**. It remains the explicit `layer` field the committed schemas already enumerate and validate. |
| **Two identity spaces** | **Token-path identity and Source Set identity are separate.** Neither is computable from the other; a `sourceSetId` is **declared, never derived** (DEC-S-131 clause 3). |
| **Source-set form** | `<layer>/<family>`, flat — **no `visual`, `foundation`, `brand`, `product`, `channel`, `context`, or `theme` namespace segment.** |

**Fixed technical roots — one per registered family in current scope:**

| Family | Technical root | Reference source set | Semantic source set |
| --- | --- | --- | --- |
| **VF-1 Colour** | `color` | `reference/color` | `semantic/color` |
| **VF-2 Typography** | `typography` | `reference/typography` | `semantic/typography` |
| **VF-3 Space and Size** | `space` | `reference/space` | `semantic/space` |
| **VF-5 Shape** | `shape` | `reference/shape` | `semantic/shape` |
| **VF-6 Surface and Elevation** | `surface` | `reference/surface` | `semantic/surface` |

**`color` is the technical identifier; `Colour` remains the display and prose term**
(DEC-S-110). **A compound display name does not produce two roots** — VF-3 and VF-6
each take one, and internal constructs are differentiated by the `<primitive-group>`
position. **These are identifier-authority statements only: no Source Set instance,
no `sourceRevision`, no manifest, no resolver, no token, and no file is created, and
visual source sets remain 0.**

### Non-normative illustration

> **The following illustrates *content* against the normative shapes above.** No
> identifier **content** below is adopted, reserved, recommended, or planned. It is
> an **example artifact** (authority class 8) and is **never normative**
> (architecture invariant 3, VF-I-13). **The concrete vocabulary below the root
> remains open** and requires its own authorization: role vocabulary under
> **DEC-S-134**'s admission rule, and scale steps under **DEC-S-133**'s per-family
> topology, both of which are undecided.

| Shape | Illustrative form | What the shape demonstrates |
| --- | --- | --- |
| Reference position | `<family>.<primitive-group>.<step>` | A primitive may be named for what it is |
| Semantic position | `<family>.<role>.<qualifier>` | A role is named for what it is *for* |
| Prohibited | a rank or appearance term standing in a semantic position | N-1, VF-I-2 |
| Prohibited | a product or consumer term in a shared foundation identifier | N-2 |
| Prohibited | a status value name reused for a visual role | N-4, VF-I-6 |

## Machine-readable representation boundary

*(Normative — an application of ADR-0001 and the CDS profile; **nothing is
implemented**)*

When the visual foundation is later expressed machine-readably, it uses the
**existing** machinery without extension:

| Element | Rule |
| --- | --- |
| **Format** | Strict JSON per RFC 8259, `.tokens.json`, under the CDS Token Format Profile over pinned **DTCG 2025.10** (DEC-S-073, DEC-S-074, DEC-S-075). |
| **Source-set classes** | Reference Source Set and Semantic Source Set first; Component and Product Profile Source Sets later; each with a **Source-Set Manifest** and, where contexts exist, a **Resolver / Composition document**. |
| **Typing** | Every token declares an explicit `$type` drawn from the type set the CDS profile admits, and **must not rely on group- or root-level typing**. **The admitted set is enumerated in the [CDS Token Format Profile](CDS_TOKEN_FORMAT_PROFILE.md), not here** — `color`, `dimension`, `number` (DEC-S-130, CDS-WP-020). The validator's bounded V2 type set is a **DEC-S-098 coverage boundary, not the admission**, and an overstated coverage claim is RISK-074. |
| **References** | Token-to-token references use the DTCG `{group.token}` form; document, property, resolver, and source-set references use `$ref` / RFC 6901 JSON Pointer. Cross-file references must be declared, offline-resolvable, and revision-bound. |
| **CDS metadata** | Only inside DTCG `$extensions` under `io.github.kaykaspers.cds`, carrying `profileVersion`. Foreign extensions are preserved and never automatically normative. |
| **Identity** | Source-set ID, CDS profile version, DTCG report version, immutable source revision, maturity state, approval state, owner role, layer, dependency set — an identity missing any required element fails closed at V3. |
| **Determinism** | RFC 8785 canonicalization plus SHA-256 digests for integrity. **A digest is not a signature** and proves no authorship, approval, or release. |
| **Validation** | V1 syntax · V2 DTCG · V3 CDS profile · V4 semantic and governance. A pass at one layer proves nothing about the next; a `Fail` or `Blocked` stops later layers, which are recorded `Not assessed`. |
| **Authority** | A validator pass is **metadata coherence, never maturity authority** (DEC-S-053 applied to format validation). |

**Requirements this places on later validation work (CDS-WP-024), stated as
requirements and not implemented here:** a semantic role that declares no contrast
obligation, an appearance name in a semantic position, a component binding a
reference token directly, an upward dependency, a profile override outside a named
extension point, and a context that removes a role must each be **detectable**.

> **This work package writes no token source file, adds no schema, changes no
> validator, and produces no digest.** Doing any of that would cross into
> CDS-WP-020 and later, and is **deferred**.

## Motion boundary

*(Normative — boundary only; **CDS-WP-035 owns the Motion System**)*

The visual foundation records that motion is a Layer-3 concern and fixes the
constraints any later motion work must satisfy:

1. **Reduced-motion support is mandatory** (Accessibility Requirements Baseline
   4.1, CR-022).
2. **Motion is never the sole carrier of meaning** (baseline 4.5, VF-I-5).
   Removing motion must remove no meaning.
3. **No CDS artifact may flash above threshold** (2.3.1 — a CDS-alone obligation).
4. **Functional and decorative motion are distinct**, and only functional motion
   may participate in conveying anything.
5. **Moving or auto-updating content must be controllable** (2.2.2), and live
   updates must not interrupt uncontrollably.
6. **Motion is unavailable in paginated and printed channels** and must degrade to
   a form that loses no meaning.

**No duration, easing curve, threshold, or motion value is defined here**, and no
part of the Motion System is begun.

## Accessibility, channels, brand, and governance

These four concerns are load-bearing and are held in dedicated documents rather
than summarised here:

| Concern | Document |
| --- | --- |
| WCAG applicability, requirement coverage, evidence state | [Visual Foundation Accessibility Mapping](../governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md) |
| Per-channel reusability, reduction, transformation, and blocking | [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md) |
| Core identity, product identity, profiles, consumer and customer branding | [Visual Foundation Brand and Product Profile Boundary](../governance/VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md) |
| Ownership, lifecycle, change classification, breaking changes, evidence | [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md) |

**Current accessibility state, stated plainly:** every visual foundation artifact
is **AE-0**. No visual artifact exists, none has been evaluated, and **no
accessibility claim of any level is valid**. The single admitted evidence package
in CDS (`AE1-CDS-WP016-SEMSTATUS-004`, AE-1) covers the channel-independent
Semantic Status source/contract family only and **does not transfer** to anything
here.

## Consumer evidence — stated honestly

*(Recorded so the architecture is not read as demand-driven where it is not)*

Six registered consumer requirements map to Layer 3: **CR-002** (existing
product-local token sets), **CR-006** (semantic status, never colour-only),
**CR-021** (keyboard operability and visible focus), **CR-022** (motion restraint),
**CR-023** (DE/EN and flexible text), **CR-025** (light and dark themes).

**No registered consumer requirement asks for a colour palette, a typographic
scale, a spacing scale, a radius scale, an elevation model, an icon library, or
illustration.** Families VF-3, VF-5, VF-6, and VF-7 therefore carry **no consumer
demand evidence at all** — they are registered because the architecture registers
Layer 3, not because a consumer asked.

This is the same honesty CDS-WP-005 applied to CR-030 (presentations):
**registering structure is not establishing demand.** The underlying evidence is
committed documentation only; no user research, interview, or usability testing has
taken place (RISK-017), and the architecture remains unvalidated by implementation
(RISK-026).

## Deferred decisions

*(Deliberately open — DEC-S-032. Recording an item here **defers** it; it does not
decide, schedule, or authorize it.)*

| # | Open question | Destination |
| --- | --- | --- |
| 1 | Every concrete visual value — colour, palette, typeface, size, spacing, radius, stroke, shadow, opacity, icon, illustration, motion value, breakpoint | CDS-WP-020 and later, each separately authorized |
| 2 | The admitted DTCG `$type` set for visual families — **CLOSED by DEC-S-130** (CDS-WP-020 Decision Integration Pass, 2026-08-27): `color`, `dimension`, `number`. Composite types and font-family / font-weight identity **stay deferred** | **Closed**; residual under **OD-2** |
| 3 | The concrete shared vocabulary of families, roles, and qualifiers — **partly closed 2026-09-05**, effective at commit `2cb244e8…`. **Family roots are fixed by DEC-S-132** and the **qualifier position is declared but unpopulated**. **The concrete role vocabulary stays open:** DEC-S-134 decides an **admission rule only** — a role enters CDS Core only on demonstrated cross-consumer need, satisfying SR-1 … SR-12 from creation, inside the **closed** role classification — and **creates no role identifier**. | The role vocabulary is **still open** as **OD-6A**, for separately authorized successor work; **`CDS-WP-020A` may not invent it** |
| 4 | The responsive-range model, and the Layer 3 / Layer 5 split for viewport strategy — **closed 2026-09-06**, effective at commit `a6bd7bf0…`. **The split is CONFIRMED** by CDS-WP-021 (LO-1 … LO-8), and **CR-004 remains registered at Layer 5** — `F-019-03` is answered. **The model** is recorded — the spatial-context structure (CX-1 … CX-9), the Adaptation Container (AC-1 … AC-6), the range obligations (AR-1 … AR-12), and the grid, container and content-width contracts (GC-1 … GC-9). **The mechanism is DECIDED by the Human Maintainer**: the **Container-Relative Named-Range Foundation** — a declared **Adaptation Container** as primary reference frame, **named discrete available-space ranges** as Core vocabulary, continuous behaviour **permitted downstream but not Core range identity**, fixed-geometry channels governed by **their own geometry**, and **`SPATIAL CONTEXT ≠ THEME RESOLUTION CONTEXT`** — recorded as **`DEC-S-136`** with **[ADR-0006](../decisions/ADR-0006-ADAPTIVE_SPATIAL_CONTEXT_AND_NAMED_RANGE_ARCHITECTURE.md)**, both **effective**. | **Closed.** Residuals: the **concrete range vocabulary** stays open, and **whether VF-4 acquires a technical root and source-set identity is DEFERRED** by the Human Maintainer (`WP021-D2`) — **DEC-S-132 grants VF-4 no root**, and **no Decision and no ADR exists for it** |
| 5 | Whether a theme is a resolver context, a separate source set, or a Product Profile concern — and the token layering light and dark imply (CR-025) | **CDS-WP-022** |
| 6 | Whether high contrast is a CDS context, a platform-honouring behaviour, or both | CDS-WP-022 |
| 7 | How visual roles bind to the five status axes | **CDS-WP-023**, gated by CDS-WP-024 and CDS-WP-025 |
| 8 | Component token granularity | CDS-WP-026 |
| 9 | Which extension points a Product Profile may touch — **the set is empty today** | **CDS-WP-032** |
| 10 | Motion durations, easings, and reduced-motion thresholds | CDS-WP-035 |
| 11 | The icon system, its grid, and its licensing and provenance model | CDS-WP-037, CDS-WP-046 |
| 12 | Data-visualization encoding and its accessible alternative representation | CDS-WP-039 |
| 13 | The transformation tool and the channel adapters | CDS-WP-048 … CDS-WP-050 |
| 14 | Accessibility profiles for PDF, presentations, exported diagrams, and brand materials | Per-channel, before any Candidate in that channel |
| 15 | Font licensing, provenance, self-hosting, and distribution | CDS-WP-020 and CDS-WP-046 — see the [Typography Architecture](VISUAL_FOUNDATION_TYPOGRAPHY_ARCHITECTURE.md) |

## Forward implications

*(A dependency statement. **It authorizes nothing.** Each work package begins only
on an explicit Nova prompt and Human-Maintainer authorization, one at a time.)*

| Work package | What this architecture hands it | What it must not assume |
| --- | --- | --- |
| **CDS-WP-020** — Reference and Semantic Token Foundation | The family register, the naming model, the machine-readable boundary, the invariants | That any value, name, or type set is pre-approved |
| **CDS-WP-021** — Adaptive Layout and Responsive Foundation | VF-4, and the open Layer 3 / Layer 5 split for viewport strategy | That breakpoints are a foundation decision without confirming the split |
| **CDS-WP-022** — Theme and Environmental Presentation Model | VF-9 and the theme constraints | That the theme **mechanism** is decided — it is not |
| **CDS-WP-023** — Semantic Status Visual Binding Contract | VF-I-5 … VF-I-7 and the status boundary | That any binding is pre-approved, or that it may proceed before CDS-WP-024 |
| **CDS-WP-024 / CDS-WP-025** — Validation and render gate | The detection requirements above | That a validator pass is authority |
| **CDS-WP-032** — Product Profile and Brand Extension Governance | The empty extension-point set and its criteria | That any extension point exists |
| **CDS-WP-035 / CDS-WP-037 / CDS-WP-039** — Motion, Icons, Data Visualization | Boundaries only | That any of it is begun here |

## Change control

*(Normative)*

This document is normative for the structure it defines. Changes require an
authorized CDS work package, a corresponding Decision Index entry **where a
registered decision changes**, consistency updates across the dependent visual
foundation documents, Nova review, and Human-Maintainer approval.

A change that touches accessibility obligations, shared semantics, a Product
Profile, a breaking contract change, a claim, licensing, or publication is
**Elevated** (DEC-S-033) — the trigger wins over the estimate.

The visual foundation is not extended implicitly: not by a Skill, not by a
consumer request, not by an implementation convenience, not by a design tool, and
not by a generated artifact.

## Related documents

| Topic | Document |
| --- | --- |
| **Reference layer** (token-flow layer 1) | [Visual Reference Token Foundation](VISUAL_REFERENCE_TOKEN_FOUNDATION.md) — CDS-WP-020 |
| **Semantic layer** (token-flow layer 2) | [Visual Semantic Token Foundation](VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) — CDS-WP-020 |
| **Value-selection discipline** | [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md) — CDS-WP-020 |
| Open decisions gating every value | [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md) — **non-normative** |
| Colour | [Visual Foundation Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md) |
| Typography | [Visual Foundation Typography Architecture](VISUAL_FOUNDATION_TYPOGRAPHY_ARCHITECTURE.md) |
| Spacing, sizing, layout, grid, responsive | [Visual Foundation Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md) |
| **Adaptive layout and responsive foundation** (VF-4) | [Adaptive Layout and Responsive Foundation](ADAPTIVE_LAYOUT_AND_RESPONSIVE_FOUNDATION.md) — CDS-WP-021 |
| Shape, surface, elevation, opacity, focus ring | [Visual Foundation Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md) |
| Icons, illustration, imagery, generated imagery | [Visual Foundation Iconography and Imagery Architecture](VISUAL_FOUNDATION_ICONOGRAPHY_AND_IMAGERY_ARCHITECTURE.md) |
| Themes and presentation contexts | [Visual Foundation Theme Architecture](VISUAL_FOUNDATION_THEME_ARCHITECTURE.md) |
| Accessibility mapping | [Visual Foundation Accessibility Mapping](../governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md) |
| Channel mapping | [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md) |
| Brand and Product Profile boundary | [Visual Foundation Brand and Product Profile Boundary](../governance/VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md) |
| Governance and lifecycle | [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md) |
| Architecture frame | [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) |
| Token flow | [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md) |
| Authority and conflicts | [Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md) |
| Profiles and extensions | [Product Profile and Extension Model](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) |
| Channels and distribution | [Artifact Distribution and Channel Model](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) |
| Machine-readable source | [Machine-Readable Source Model](MACHINE_READABLE_SOURCE_MODEL.md) · [CDS Token Format Profile](CDS_TOKEN_FORMAT_PROFILE.md) · [Validation Contract](MACHINE_READABLE_VALIDATION_CONTRACT.md) |
| Status meaning | [Semantic Status Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) |
| Scope | [Concept and Scope](../governance/CONCEPT_AND_SCOPE.md) |
| Accessibility policy | [Accessibility and Inclusive Design Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) |
| Decisions · Risks | [Decision Index](../decisions/DECISION_INDEX.md) · [Risk Register](../risks/RISK_REGISTER.md) |
