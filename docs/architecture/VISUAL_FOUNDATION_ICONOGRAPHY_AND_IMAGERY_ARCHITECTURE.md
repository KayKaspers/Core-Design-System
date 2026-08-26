# Visual Foundation Iconography and Imagery Architecture

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for the boundaries of CDS iconography and imagery.** It
  defines **VF-7** and positions illustration and imagery. It **creates no icon and
  no asset**.
- **Maturity:** **`Proposed`** — this document promotes nothing.

## Purpose and boundary

This document defines **where visual assets live, who owns them, and what every
asset owes** — semantically, accessibly, and legally.

**It creates no icon library**, no icon, no illustration, no image, no avatar, no
diagram asset, and no brand mark. It selects no style, no grid, no stroke
discipline, no format, and no source.

**No visual asset of any kind exists in CDS**, and none is created, referenced,
downloaded, or distributed here.

Frame: [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md).

## The asset ownership split

*(Normative — the positioning statement of this document)*

Visual assets do not all belong to the same architecture layer, and treating them
as one family is how a design system quietly takes over brand ownership.

| Asset kind | Architecture layer | Owner | Registered by |
| --- | --- | --- | --- |
| **System icons** | **3 Foundations and Tokens** | CDS, as **VF-7** | DEC-S-021 Layer 3 — *"iconography"* |
| **Brand marks and logos** | **2 Brand and Identity** | CDS Layer 2 — **never VF-7** | DEC-S-021 Layer 2 — *"logos and brand assets"* · scope domain 1 |
| **Product icons and product marks** | **2 Brand and Identity** | CDS Layer 2, within brand governance | Scope domain 1 |
| **Illustration** | **2 Brand and Identity**, consumed through a declared interface | CDS Layer 2 | Not in the Layer 3 enumeration; recorded as a CDS deferred decision area |
| **Photography and imagery** | **2 Brand and Identity**, consumed through a declared interface | CDS Layer 2 | As above |
| **Diagram assets** | **6 Channels and Communication** | Channel work | Registered channel class |
| **Data-visualization output** | **6 Channels and Communication** | **CDS-WP-039** | Registered channel class |
| **Avatars and user-supplied imagery** | **Consumer** | **Consumer**, always | Consumer-owned content |
| **Generated imagery** | **See below** | Case-dependent | — |

### Why illustration and imagery are not a Layer-3 family

The normative Layer 3 enumeration registers *iconography* and does **not** register
illustration or imagery; Layer 2 registers *"logos and brand assets"*. Illustration
and imagery are recorded in
[Concept and Scope](../governance/CONCEPT_AND_SCOPE.md) as **deferred decision
areas within CDS scope** — so they are in scope, but the layer that owns them is
Layer 2, not Layer 3.

Placing them in Layer 3 would let the foundation acquire brand authority by
accident, and Layer 2 may not depend on Layer 3 (allowed-dependency table). The
visual foundation therefore **consumes** them through a declared interface and
**owns** none of them.

**Recorded observation, not repaired here:** capability domain 3 of Concept and
Scope does not name *iconography*, although DEC-S-021 Layer 3 does. The
architectural positioning above follows DEC-S-021; the enumeration asymmetry is
reported as a finding of CDS-WP-019 and is **not** corrected by this work package.

## The semantic / decorative classification

*(Normative — required of **every** asset, in every layer, in every channel)*

| Class | Definition | Obligation |
| --- | --- | --- |
| **Semantic** | The asset conveys information a person needs | Requires a **text alternative** carrying the same information (1.1.1) |
| **Decorative** | The asset conveys nothing not already conveyed | Must be **exposed as decorative**, not described |
| **Functional** | The asset *is* the control, or labels one | Requires an **accessible name matching its visible label** (2.5.3, 4.1.2) |

Rules:

1. **Every asset declares its class.** An undeclared asset is a defect: a consumer
   cannot supply an alternative for something whose class nobody stated.
2. **The class is a property of the use, not of the file.** The same icon is
   semantic in one position and decorative in another; the **contract** carries the
   class, not the asset.
3. **CDS cannot author consumer content.** CDS supplies the **slot and the
   obligation**; the consumer supplies the actual alternative text (1.1.1 is a
   shared criterion).
4. **A decorative asset that is actually carrying meaning is the failure mode**,
   and it is invisible to everyone who can see it.

## The icon boundary (VF-7)

*(Normative as constraints; **CDS-WP-037 owns the Symbol System**)*

CDS-WP-019 defines **no icon**. It fixes the constraints any later icon work
inherits:

| # | Constraint |
| --- | --- |
| **IC-1** | **An icon is never the sole carrier of meaning** (1.3.3, 1.4.1, VF-I-5). An icon-only control requires an accessible name; an icon-only status is prohibited. |
| **IC-2** | **An icon is not a status** (VF-I-6). No icon carries a status axis value, and no icon set may become an alternative status vocabulary. |
| **IC-3** | **Icons that convey boundaries or controls are contrast-sensitive** (1.4.11), and the obligation is declared. |
| **IC-4** | **Monochrome and multicolour behaviour is declared per icon**, together with what happens when colour is unavailable. |
| **IC-5** | **Theme adaptation is a re-binding, never a redefinition** (VF-I-9). An icon may take its colour from a role; it may not change what it means per theme. |
| **IC-6** | **A missing icon degrades to its text alternative**, never to an empty control. |
| **IC-7** | **Icons must survive export and print**, or the limitation is declared. |
| **IC-8** | **Icon meaning is localized like any other meaning** — an icon that reads differently across cultures is a content risk, not a style choice. |
| **IC-9** | **No icon library is selected, imported, vendored, or referenced**, and none may be without FP-style provenance and licensing analysis (below). |

## Provenance, licensing and rights

*(Normative — an **Elevated** gate on any future asset)*

**CDS holds no licence for any artifact class** (DEC-S-047), publication is
`Private Development`, and **no external asset is downloaded, vendored, or
distributed** by CDS-WP-019.

Before **any** visual asset may enter CDS:

| # | Required |
| --- | --- |
| **AP-1** | **Licence identity** — exact licence, version, and its terms for modification, redistribution, embedding, and commercial use |
| **AP-2** | **Provenance** — the authoritative source and how integrity is verified |
| **AP-3** | **Attribution obligations**, if any, and how they are discharged in every channel that carries the asset |
| **AP-4** | **Offline viability** — servable locally, with **no mandatory external runtime service** (CR-031, DEC-S-030, invariant 12) |
| **AP-5** | **Rights clearance for depicted people, places, and marks**, where imagery or photography is involved |
| **AP-6** | **Format and degradation behaviour**, including what happens where the format is unsupported |
| **AP-7** | **The consequence of not adopting it** — declining an asset set is an admissible outcome |

An **unfixable provenance or rights violation** is one of the four grounds for
**emergency removal** under the versioning policy. That is the concrete
consequence of getting AP-1 … AP-5 wrong, and it is why they are a gate rather than
a checklist.

## Generated imagery

*(Normative)*

"Generated imagery" spans two very different things, and conflating them is an
authority error:

| Kind | Class | Rule |
| --- | --- | --- |
| **Deterministically generated from a normative CDS source** — a rendered diagram, an exported chart, a produced asset variant | **3 Generated artifact** | **Never normative.** Never hand-edited. Always carries source and transformation revision. A manual edit is reconciled back into the source, never kept (DEC-S-031, DEC-S-079, VF-I-12). |
| **Produced by a generative model or an external tool** | **Not admissible as a CDS asset** without AP-1 … AP-7 being satisfied, including provenance and rights | Provenance is precisely what such an asset usually cannot supply. Absence of provenance is a **blocking** property, not a formality (RISK-025). |

**An asset whose origin cannot be established is functionally normative, because
nobody can contradict it.** That is the failure this section exists to prevent.

## Channel behaviour

| Channel | Asset reality |
| --- | --- |
| **Product UI** | Full obligations, including accessible name and focus behaviour where functional |
| **Documentation** | Alternative text and accessible diagram explanations are required |
| **Repository presentation** | **Platform-controlled rendering**; CDS covers what it authors |
| **PDF and reports** | Alternative text is channel-profile-dependent; **no profile exists** |
| **Presentations** | Alternative text and reading order are channel-profile-dependent; **no profile exists** |
| **Diagrams** | **A textual explanation or alternative data representation is required**; structural meaning must survive export |
| **Data visualization** | The hardest channel; **CDS-WP-039** owns it |
| **Brand and communication materials** | **No usage rules exist**; **blocked** for Candidate and Stable |

**Brand approval is never an accessibility claim.** The two are unrelated
authorities, and a brand sign-off says nothing about whether an asset is
perceivable.

## What a Product Profile may do

| A Product Profile **may** | A Product Profile **may never** |
| --- | --- |
| Select among icon or asset options the core defines, at a **named, approved** extension point | Replace a semantic asset with one that means something else |
| Express product identity within **Layer 2 brand governance** | Remove or weaken a text alternative obligation |
| — | Introduce an asset without AP-1 … AP-7 |
| — | Make an icon the sole carrier of meaning |
| — | Introduce an asset dependency that defeats offline or air-gap use |

**No extension point is named today** (CDS-WP-032).

## Validation requirements

*(Requirements on **CDS-WP-024**. **No validator is changed here.**)*

A later validator must be able to detect: an asset reference with no declared
class; a functional asset with no accessible-name obligation; an asset reference
that is not locally resolvable; a missing licence or provenance declaration; and an
icon identifier reusing a status axis or status value name.

Whether an alternative text is *adequate* is **not** structurally checkable and is
partly consumer-owned. **An automated check is never sufficient** (DEC-S-053).

## Evidence and claim boundary

Every asset-related artifact in CDS is **AE-0**. No asset exists; nothing has been
rendered or read by assistive technology. **No accessibility claim of any level is
valid.** VF-7 carries **no consumer demand evidence at all**.

## Deferred decisions

Icon system, style, grid, stroke discipline, and format · the icon set itself ·
illustration style and system · photography direction · brand marks and logos ·
product marks · avatar treatment · diagram asset standards · asset formats ·
licensing, provenance, and attribution model · asset distribution · named extension
points.

**Each requires its own explicitly authorized work package**, and the licensing,
provenance, and rights items are **Elevated**.

## Related documents

- [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
- [Visual Foundation Brand and Product Profile Boundary](../governance/VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md)
- [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Visual Foundation Accessibility Mapping](../governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md)
- [Accessibility Channel Profiles](../governance/ACCESSIBILITY_CHANNEL_PROFILES.md)
- [Licensing and Publication Decision Model](../governance/LICENSING_AND_PUBLICATION_DECISION_MODEL.md)
- [Versioning, Compatibility and Deprecation Policy](../governance/VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md)
- [Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)
