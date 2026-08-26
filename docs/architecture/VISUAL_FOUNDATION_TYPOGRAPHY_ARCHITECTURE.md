# Visual Foundation Typography Architecture

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for the structure of CDS typography.** It defines the
  typography architecture (**VF-2**) and **selects no typeface and no value**.
- **Maturity:** **`Proposed`** — this document promotes nothing.

## Purpose and boundary

This document defines **how typography is structured in CDS**: which typographic
decisions exist, where each lives, what a text role must declare, and which
constraints — accessibility, localization, offline use, licensing — bind every
later typographic decision.

**It selects no typeface**, no font stack, no fallback list, no weight, no size, no
line height, no tracking, and no scale. **No font file is bundled, downloaded,
referenced, or distributed**, and none may be.

Frame: [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md) —
Layer 3, token-flow layers 1 and 2.

## Typography flows in one direction

*(Normative — an application of DEC-S-024)*

```text
typographic primitive  →  text role  →  [context re-binding]  →  [profile override]  →  generated output
     (layer 1)             (layer 2)       (resolution)            (layer 4)            (layer 5)
```

A **typographic primitive** is a raw typographic value with no purpose. A **text
role** is a named typographic purpose. A role that is merely a size is not a role.

## The decision families

*(Normative as a **structure**, not as a vocabulary. **No name and no value is
created here.** The concrete set is CDS-WP-020's.)*

| Family | What it holds | Layer position |
| --- | --- | --- |
| **Font family role** | Which *kind* of typeface a purpose calls for — not which typeface | Semantic |
| **Fallback chain** | The ordered, locally-resolvable alternatives behind a family role | Reference, bound to a family role |
| **Weight role** | The emphasis a purpose requires | Semantic over primitives |
| **Size scale** | The ordered step set available to roles | Reference |
| **Line height model** | Vertical rhythm relative to size | Reference and semantic |
| **Tracking** | Letter-spacing adjustments, where a purpose requires one | Reference |
| **Text role** | The composed purpose: family, weight, size, line height, tracking | **Semantic — this is where typography lives** |

### Text role classes

| Class | Purpose |
| --- | --- |
| **Heading** | Structural hierarchy in content |
| **Body** | Continuous reading text |
| **UI** | Interface labels, controls, and short interactive strings |
| **Editorial and document** | Long-form and paginated reading |
| **Code and monospace** | Literal, character-significant text |
| **Numeric and data** | Aligned, comparable figures in dense displays |
| **Supporting** | Captions, helper text, and metadata |

*"Monospace" above names the **kind of typeface a purpose calls for**, in the sense
of the Font family role. It selects **no typeface, no font stack, and no fallback
list**, and it is not a CSS generic-family declaration.*

**UI typography and editorial typography are not the same system.** A dense
operational interface and a paginated report have different reading distances,
different scanning behaviour, and different failure modes. Forcing one scale on
both produces bad artifacts in both — the same reasoning DEC-S-029 applies to
channels.

### Role obligations

*(Normative — every text role, without exception)*

| # | Every text role must declare |
| --- | --- |
| **TR-1** | Its **class** from the table above |
| **TR-2** | Its **contrast obligation** as a Content role against a declared surface (VF-I-8, 1.4.3) |
| **TR-3** | Its **text-length tolerance** — the role must not assume a fixed or maximum string length (CR-023) |
| **TR-4** | Its behaviour under **user text resize and text-spacing overrides** (1.4.4, 1.4.12) |
| **TR-5** | Whether it is a **named extension point** for a Product Profile — **no role is one today** |
| **TR-6** | Its **channel availability**, where a channel cannot render it |

## Structural hierarchy is not typographic size

*(Normative — the most common typographic accessibility failure)*

| # | Rule |
| --- | --- |
| **TH-1** | **A heading role is a presentation role. It is not a document structure.** Structure is programmatic (1.3.1); appearance is not structure. |
| **TH-2** | **Applying a heading role does not make something a heading**, and applying a body role does not stop something being one. |
| **TH-3** | **Hierarchy must be programmatically determinable** independently of the typographic role applied to it. |
| **TH-4** | A **visual-only** hierarchy is invisible to assistive technology and to every non-visual channel. |

## Accessibility constraints

*(Normative — sourced from the Accessibility Requirements Baseline and the WCAG
matrix; **no value is introduced**)*

| # | Constraint | Source |
| --- | --- | --- |
| **TA-1** | **Text is real text, not an image of text.** Images of text are prohibited in CDS artifacts — a **CDS-alone** obligation | 1.4.5, baseline 3.x |
| **TA-2** | **Text must resize and magnify** without loss of content or function | 1.4.4, baseline 3.3 |
| **TA-3** | **User text-spacing overrides must be tolerated** without content loss | 1.4.12, baseline 3.4 |
| **TA-4** | **Content must reflow**; dense operational data is the hard case and is unresolved until implementation | 1.4.10, baseline 3.2 |
| **TA-5** | **Contrast obligations apply to text** against its declared surface | 1.4.3, baseline 3.1 |
| **TA-6** | **No meaning by typographic appearance alone** — weight, size, italic, and case are never the sole carrier | 1.3.3, 1.4.1, VF-I-5 |
| **TA-7** | **No meaning-bearing abbreviation without understandable context** | baseline 8.7 |
| **TA-8** | **Layout must tolerate variable text length**; no layout-critical text assumption | baseline 8.3, 8.4, CR-023 |
| **TA-9** | **Text direction and bidirectional content must not be architecturally excluded.** This is a **structural constraint, not a commitment to ship right-to-left support** | baseline 8.6 |

**No size, weight, line-height, or contrast value is fixed here.** Where a value is
required, it is required *by the cited criterion*, and it is referenced rather than
restated.

## Localization constraints

*(Normative — CR-023 is a **Must** requirement carried by two consumers)*

1. **German and English are product-facing languages** in the intended scope, with
   **semantic parity**: a translated label may not narrow, widen, soften, or
   upgrade a meaning.
2. **Text length varies between languages.** A role that works only at one
   language's typical length is defective, not merely tight.
3. **Truncation may never remove a material qualifier.** A shortened label that
   drops the part carrying the limitation is a truthfulness defect, not a layout
   compromise.
4. **Technical identifiers stay language-neutral and stable**; display labels are a
   separate, localized concern (DEC-S-110).
5. **Further languages must remain possible** — internationalization capability is
   a normative requirement even where no further language is planned
   (baseline 8.5).
6. **Script coverage is a selection constraint.** Any later typeface decision must
   state which scripts it covers and what happens where it does not.

## Font provenance, licensing and distribution

*(Normative — a constraint on any future selection; **no selection is made**)*

**No font file is bundled, vendored, downloaded, hot-linked, or distributed by
CDS**, and CDS-WP-019 introduces no font dependency of any kind.

A future typeface selection is an **Elevated** change (DEC-S-033: licensing,
provenance, and distribution triggers) and **may not** be made without all of the
following recorded first:

| # | Required before any typeface may be selected |
| --- | --- |
| **FP-1** | **Licence identity** — the exact licence, its version, and its terms for embedding, subsetting, modification, redistribution, and web use |
| **FP-2** | **Provenance** — the authoritative source of the font files and how their integrity is verified |
| **FP-3** | **Offline and self-hosted viability** — the font must be servable locally with **no mandatory external runtime service**, satisfying CR-031, DEC-S-030, and invariant 12 |
| **FP-4** | **Air-gap tolerance** — a consumer with no external network must still consume a pinned CDS revision |
| **FP-5** | **A fallback chain that is itself locally resolvable**, so that a missing font degrades rather than fails |
| **FP-6** | **Script and glyph coverage**, stated, including what is not covered |
| **FP-7** | **Distribution model** — how consumers obtain it, and whether CDS distributes anything at all |
| **FP-8** | **The consequence of not selecting one** — a system-stack-only approach is an admissible outcome, not a failure |

> **A proprietary typeface may not be made normative without FP-1 … FP-8 being
> satisfied and separately approved.** CDS holds **no licence** for any artifact
> class today (DEC-S-047), and publication remains `Private Development`.

**A font hosted by a third-party service is architecturally inadmissible as a
mandatory dependency**, because it converts every consumer into a client of a
service CDS does not control — which invariant 12 forbids outright.

## Responsive typography boundary

*(Normative as a boundary)*

- The **size scale and the roles** are Layer 3 (VF-2).
- **Which role appears at which viewport** is a Layer-5 pattern concern, related to
  CR-004 — see the
  [Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md).
- **A responsive rule must not defeat TA-2, TA-3, or TA-4.** Adaptation that breaks
  user resize or reflow is a defect.
- **No breakpoint, no fluid function, and no clamping rule is defined here.**

## Channel boundary

Typography is one of the families that differs most between channels — see the
[Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md).

| Channel reality | Consequence |
| --- | --- |
| **Repository presentation** | Rendering is **platform-controlled**; CDS cannot guarantee a host's typography and covers only what it authors |
| **PDF and reports** | Paginated, printed, possibly greyscale; no user resize; embedding and licensing constraints apply |
| **Presentations** | Distance viewing; a UI-density scale is wrong here |
| **Diagrams** | Text must survive export and remain selectable or described |
| **Data visualization** | Numeric and dense; label collision is the failure mode |

**Meaning is constant across channels; typographic presentation is not**
(DEC-S-029, VF-I-11).

## What a Product Profile may do with typography

| A Product Profile **may** | A Product Profile **may never** |
| --- | --- |
| Override a typographic **value** at a **named, approved** extension point | Add, remove, rename, or repurpose a **text role** |
| Select among options the core defines | Break text-length tolerance, resize, or reflow behaviour |
| Express product identity within brand governance | Reduce a declared contrast obligation |
| — | Introduce a font dependency that defeats offline or air-gap use |
| — | Make typographic appearance the sole carrier of meaning |

**No extension point is named today**, so no typographic override is possible
today (CDS-WP-032).

## Validation requirements

*(Requirements on **CDS-WP-024**. **No validator is changed here.**)*

A later validator must be able to detect: a text role with no declared class; a
role with no declared contrast obligation; an appearance-derived role name; a
component binding a typographic primitive directly; a context or profile that
removes a role; a role asserting a fixed text length; and a font reference that is
not locally resolvable.

**An automated check is never sufficient accessibility evidence** (DEC-S-053).

## Evidence and claim boundary

Every typographic artifact in CDS is **AE-0**. Nothing has been rendered, resized,
magnified, read aloud, or tested in any environment. **No accessibility claim of
any level is valid.**

## Deferred decisions

Typeface selection · font stack · fallback chain · weight set · size scale and step
count · line-height model · tracking · the concrete role vocabulary · responsive
typography mechanism · right-to-left support scope · licensing, provenance, and
distribution model · named extension points.

**Each requires its own explicitly authorized work package**, and the licensing,
provenance, and distribution items are **Elevated**.

## Related documents

- [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
- [Visual Foundation Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md)
- [Visual Foundation Accessibility Mapping](../governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md)
- [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Accessibility Requirements Baseline](../governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [Artifact Distribution and Channel Model](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md)
- [Licensing and Publication Decision Model](../governance/LICENSING_AND_PUBLICATION_DECISION_MODEL.md)
