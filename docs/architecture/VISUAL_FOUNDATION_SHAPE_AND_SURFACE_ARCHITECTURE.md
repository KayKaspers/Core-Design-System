# Visual Foundation Shape and Surface Architecture

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for the structure of CDS shape, surface and elevation.**
  It defines **VF-5** and **VF-6**, positions opacity, and **selects no value**.
- **Maturity:** **`Proposed`** — this document promotes nothing.

## Purpose and boundary

This document defines **how shape and surface are structured in CDS**: radius,
stroke and border, separators, surface hierarchy, elevation and shadow, opacity,
overlays, and the focus ring.

**It selects no value.** No radius, no stroke width, no shadow, no opacity level,
no surface count, and no elevation step.

Frame: [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md) —
Layer 3, token-flow layers 1 and 2.

## Why shape and surface are one document

Radius, stroke, elevation, and opacity are frequently treated as four independent
systems. They are not: they are the four ways a system says **"this is a distinct
surface, and it is here rather than there."** Governing them apart is how a design
system ends up with an elevation model that contradicts its border model and a
focus ring that either can defeat.

The families remain separately identified (**VF-5 Shape**, **VF-6 Surface and
Elevation**) because they have different maturity paths and different channel
behaviour. They are architected together because they share one obligation.

## Opacity is an attribute, not a family

*(Normative — positioning, deliberately conservative)*

**Opacity is registered in no CDS scope statement.** It appears in neither the
Layer 3 enumeration of DEC-S-021 nor capability domain 3 of
[Concept and Scope](../governance/CONCEPT_AND_SCOPE.md).

CDS therefore positions it as an **attribute of two already-registered families**,
rather than registering it as new scope:

| Opacity as | Belongs to | Governed by |
| --- | --- | --- |
| **Alpha within a colour value** | **VF-1 Colour** | The colour role's contrast and pairing obligations |
| **Overlay, scrim, and surface separation** | **VF-6 Surface and Elevation** | The surface obligations below |

Positioning opacity this way registers **less**, not more — the conservative
reading required on unclear authority (DEC-S-023). Registering it as an independent
family would extend scope, and scope is not extended implicitly.

**Consequence, and it is not a formality:** an opacity change is a **colour
change** or a **surface change**, and inherits that family's contrast obligation. A
translucent foreground is a contrast question, not a stylistic one. There is no
opacity token whose accessibility implications nobody owns.

## Shape (VF-5)

*(Normative as structure; **no value is created**)*

| Construct | Definition | Layer position |
| --- | --- | --- |
| **Radius primitive** | A raw corner treatment with no purpose | Reference |
| **Radius role** | A named shape purpose | Semantic |
| **Stroke primitive** | A raw line weight with no purpose | Reference |
| **Border role** | A named boundary purpose — enclosure, control edge, division | Semantic |
| **Separator role** | A named division purpose between regions or items | Semantic |

### Obligations

| # | Every shape role must declare |
| --- | --- |
| **SH-1** | Its **purpose**, not its geometry (VF-I-2) |
| **SH-2** | Whether it conveys a **boundary that matters** — and if so, its **non-text contrast obligation** (1.4.11) |
| **SH-3** | Whether it participates in conveying meaning — and if so, its **non-shape carrier** (1.3.3, VF-I-5) |
| **SH-4** | Its **degradation behaviour** where a channel cannot render it |
| **SH-5** | Whether it is a **named extension point** — **no role is one today** |

### Rules

1. **Shape alone never carries meaning.** A rounded shape does not mean "safe" and
   a square one does not mean "system"; a shape difference that conveys anything
   requires a non-shape carrier.
2. **A boundary that a person must perceive is contrast-sensitive**, and its
   obligation is stated by the role, not inferred by the implementer (1.4.11).
3. **A separator is not a heading.** Visual division does not create programmatic
   structure (1.3.1). Where a division carries meaning, structure must carry it.
4. **Removing all radius must remove no meaning.**

## Surface and elevation (VF-6)

*(Normative as structure)*

| Construct | Definition | Layer position |
| --- | --- | --- |
| **Surface role** | A named ground on which content sits | Semantic, paired with VF-1 |
| **Surface hierarchy** | The declared ordering of surfaces relative to one another | Semantic |
| **Elevation role** | A named position in that hierarchy | Semantic |
| **Shadow primitive** | A raw depth treatment with no purpose | Reference |
| **Overlay and scrim role** | A named obscuring layer above other content | Semantic, with opacity as attribute |

### Rules

| # | Rule |
| --- | --- |
| **SU-1** | **Elevation is an ordering, not a shadow.** Shadow is one possible expression of elevation. A channel that cannot render shadow must still express the ordering, or declare that it cannot (VF-I-11). |
| **SU-2** | **Every surface role declares which content roles it supports**, so that contrast is a property of a declared pair (VF-1, CR-3). |
| **SU-3** | **Elevation never carries meaning alone.** Depth is not status, not severity, and not priority. |
| **SU-4** | **An overlay must not obscure focus** (2.4.11). This is a new WCAG 2.2 criterion for which CDS has **no pattern**, and overlays are its hard case. |
| **SU-5** | **An overlay must not trap keyboard focus** (2.1.2), and the composition that creates a trap may be entirely the consumer's — which is why this is shared, not CDS-alone. |
| **SU-6** | **A scrim is a contrast event.** Content behind or on a scrim inherits a changed contrast condition, and the role declares it. |
| **SU-7** | **Surface hierarchy must survive greyscale and print**, where shadow largely vanishes. |

## The focus ring

*(Normative — the strictest construct in this document)*

**Visible focus is a CDS-alone obligation** (WCAG **2.4.7**, CR-021, DEC-S-055,
Accessibility Requirements Baseline 2.3). It is one of only **five** criteria in
the WCAG matrix that CDS owns without the consumer.

The focus indicator is a **cross-family role set** drawing on VF-1 (colour),
VF-5 (shape and stroke), and VF-3 (space). It is deliberately **not** a family of
its own, so that no single family's change can weaken it unnoticed.

| # | Rule |
| --- | --- |
| **F-1** | **A focus indicator exists for every focusable construct.** Its absence is a defect, never a style choice. |
| **F-2** | **It is contrast-sensitive**, and the obligation is declared, not assumed. |
| **F-3** | **It must not be obscured** by an overlay, a sticky region, or a scrolling container (2.4.11). |
| **F-4** | **A theme may not remove or weaken it** (VF-I-9). |
| **F-5** | **A Product Profile may not remove or weaken it** (invariant 10, DEC-S-025). |
| **F-6** | **An ordinary exception may not waive it.** Accessibility is not waivable through the exception mechanism at all (DEC-S-059). |
| **F-7** | **A consumer must not suppress it** through local overrides — an Integration Contract obligation. |
| **F-8** | **It must remain visible under forced colours and platform high contrast** (baseline 3.5). |

> **Focus visibility is the one visual construct in CDS that has no permitted
> mechanism of removal.** Every other visual decision has a legitimate route to
> being overridden, themed, or profiled. This one does not.

## Print, export and degradation

*(Normative)*

Shadow, translucency, and subtle surface differentiation are the visual devices
that survive channel transformation **worst**. Paginated, printed, greyscale, and
exported artifacts lose most of them.

| # | Degradation rule |
| --- | --- |
| **D-1** | **A distinction a channel cannot render must be re-expressed or declared** — never silently dropped (VF-I-11, DEC-S-029). |
| **D-2** | **Elevation degrades to boundary or arrangement**, not to nothing. |
| **D-3** | **Translucency degrades to an opaque equivalent that preserves the declared contrast**, not to whatever the renderer produces. |
| **D-4** | **A greyscale print must preserve every meaningful distinction**, because the non-colour rule already required a non-colour carrier to exist. |
| **D-5** | **The focus ring has no print obligation** — print is not interactive — but an exported *interactive* artifact retains every focus obligation above. |
| **D-6** | Exported diagrams and visualizations lose the web target and **require a channel profile** before Candidate or Stable (DEC-S-058). |

## What a Product Profile may do

| A Product Profile **may** | A Product Profile **may never** |
| --- | --- |
| Override a radius, stroke, shadow, or opacity **value** at a **named, approved** extension point | Add, remove, rename, or repurpose a shape or surface **role** |
| Select among options the core defines | Alter the surface hierarchy's ordering semantics |
| Express product identity within brand governance | Weaken a declared non-text contrast obligation |
| — | **Remove, weaken, or obscure the focus indicator** |
| — | Make shape, depth, or translucency the sole carrier of meaning |

**No extension point is named today** (CDS-WP-032).

## Validation requirements

*(Requirements on **CDS-WP-024**. **No validator is changed here.**)*

A later validator must be able to detect: a shape or surface role named for its
geometry; a boundary role with no declared contrast obligation; a surface role that
declares no supported content roles; an overlay role with no declared contrast
consequence; a focusable construct with no focus role; **any context or profile
that removes or weakens a focus role**; and a component binding a shape or shadow
primitive directly.

Obscured focus, keyboard traps, and print degradation are **not** structurally
checkable and require **rendering and interaction evidence** — which does not exist
and is CDS-WP-031's. **An automated check is never sufficient** (DEC-S-053).

## Evidence and claim boundary

Every shape and surface artifact in CDS is **AE-0**. Nothing has been rendered,
printed, exported, or tested with a keyboard or assistive technology. **No
accessibility claim of any level is valid.** VF-5 and VF-6 carry **no consumer
demand evidence at all**.

## Deferred decisions

Radius scale · stroke weights · separator treatment · surface count and hierarchy
depth · elevation steps · shadow primitives · opacity levels · overlay and scrim
treatment · focus indicator geometry and values · print and export degradation
standards · named extension points.

**Each requires its own explicitly authorized work package.**

## Related documents

- [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
- [Visual Foundation Spatial Architecture](VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md)
- [Visual Foundation Theme Architecture](VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
- [Visual Foundation Accessibility Mapping](../governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md)
- [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Accessibility Requirements Baseline](../governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [Accessibility Limitations and Exception Policy](../governance/ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md)
