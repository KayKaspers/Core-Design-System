# Visual Foundation Spatial Architecture

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for the structure of CDS space, size, layout and grid.**
  It defines **VF-3** and **VF-4** and **selects no value**.
- **Maturity:** **`Proposed`** — this document promotes nothing.

## Purpose and boundary

This document defines **how spatial decisions are structured in CDS**: spacing,
sizing, layout rhythm, grid, containers, content widths, responsive ranges,
density, and target sizing.

**It selects no value.** No spacing step, no size, no grid column count, no gutter,
no container width, no breakpoint, no density level, and no target dimension.

It also selects **no technology**. The spatial architecture is
**technology-neutral**: it names no CSS feature, no layout engine, no framework,
and no platform primitive. A layout system that satisfies the constraints below is
architecturally acceptable; one that does not, is not — regardless of popularity.

Frame: [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md) —
Layer 3, token-flow layers 1 and 2.

## The Layer 3 / Layer 5 boundary

*(Normative — and the most consequential statement in this document)*

Spatial concerns split across two architecture layers, and the split must be
explicit or the foundation will absorb pattern decisions it cannot govern.

| Concern | Layer | Owner |
| --- | --- | --- |
| Spacing scale, sizing scale, density model, target sizing | **3 Foundations** | VF-3 |
| Grid structure, containers, content widths, the **responsive range vocabulary** | **3 Foundations** | VF-4 |
| **Which** layout a screen uses, **when** it changes, and what it becomes | **5 Patterns and Experiences** | Pattern work |
| Channel-imposed layout constraints (page size, slide, export) | **6 Channels** | Channel profiles |

**Recorded discrepancy.** The normative
[Architecture Requirements Traceability](ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md)
maps **CR-004 — Multi-viewport behavior** (*"viewport strategy and breakpoints"*)
to **Layer 5**, while the forward roadmap plans **CDS-WP-021 — Adaptive Layout and
Responsive Foundation** at **Layer 3**.

This document **does not resolve that by editing the traceability matrix** and does
not change CR-004's registered mapping. It states the architectural reading that
reconciles them:

> **Layer 3 owns the spatial vocabulary. Layer 5 owns the strategy that uses it.**
> A range is a foundation value; choosing what happens at that range is a pattern
> decision.

**CDS-WP-021 must confirm this split before it defines any responsive foundation**,
because the alternative reading — that viewport strategy is a foundation concern —
would create exactly the component- and pattern-driven foundation that prohibited
dependency 2 forbids.

## Spacing and sizing

*(Normative as structure; **no value is created**)*

| Construct | Definition | Layer position |
| --- | --- | --- |
| **Spacing primitive** | A raw distance with no purpose | Reference |
| **Spacing role** | A named spatial purpose — separation, grouping, inset, stack rhythm | Semantic |
| **Size primitive** | A raw extent with no purpose | Reference |
| **Size role** | A named extent purpose — control extent, icon extent, container extent | Semantic |
| **Density model** | A declared set of spatial intensities and what each preserves | Semantic |

### Obligations

| # | Every spacing or size role must declare |
| --- | --- |
| **SP-1** | Its **purpose**, not its magnitude. A role named for its number is a primitive wearing a role's clothes (VF-I-2) |
| **SP-2** | Whether it participates in **conveying grouping or relationship** — and if so, its **non-spatial carrier** (1.3.1, 1.3.3) |
| **SP-3** | Its **behaviour under text growth**, so that longer text expands rather than clipping (CR-023, baseline 8.3) |
| **SP-4** | Its **behaviour under reflow and magnification** (1.4.10, 1.4.4) |
| **SP-5** | Whether it is a **named extension point** — **no role is one today** |

### The proximity rule

*(Normative)*

> **No information may be conveyed by visual proximity or position alone**
> (Accessibility Requirements Baseline 3.7, WCAG 1.3.3).

Spacing may express a relationship. It may never be the **only** thing that
expresses it: a relationship communicated by a gap is invisible to assistive
technology, to a linearized reading order, and to any channel that reflows.

## Layout, grid and containers

*(Normative as structure)*

| Construct | Owns | Never owns |
| --- | --- | --- |
| **Grid** | A declared structural rhythm and its subdivisions | Which content occupies it |
| **Container** | A bounded region with declared extent behaviour | Its content's meaning |
| **Content width** | The reading-measure constraint for continuous text | Any specific value |
| **Responsive range** | A named span of available space | What changes within it |

Constraints:

1. **A grid is a rhythm, not a promise of identical rendering.** Product UI, PDF,
   presentation, and diagram do not render identically and are not required to
   (DEC-S-029).
2. **Layout must never lock orientation** (1.3.4).
3. **Reading order must survive layout**, in every channel and after export
   (1.3.2).
4. **Reflow is mandatory** (1.4.10), and **dense operational data is the hard
   case** — it is CDS's most-evidenced consumer need and its least-solved layout
   problem. It is recorded as unresolved, not designed around.
5. **A container must tolerate content it did not expect** — longer labels,
   translated strings, larger user text, and missing values.

## Responsive ranges

*(Normative as constraints; **no range and no threshold is defined here**)*

| # | Constraint |
| --- | --- |
| **RR-1** | A responsive range is a **named span of available space**, not a device, not a screen, and not a product decision. |
| **RR-2** | **A range name is a foundation identifier.** It carries no device, brand, product, or platform term (N-2, N-3). |
| **RR-3** | **Core function may not be removed** because space is constrained. Reducing complexity is permitted; hiding that an option exists, misrepresenting status, or concealing a risk is not (baseline 5.7). |
| **RR-4** | Adaptation must not defeat **user text resize, text spacing, or reflow**. |
| **RR-5** | **The mechanism is open.** Whether ranges are discrete breakpoints, continuous functions, container-relative, or a combination is **CDS-WP-021's**, subject to the Layer 3 / Layer 5 split above. |
| **RR-6** | The model must remain expressible in **non-web channels**, where "viewport" has no meaning and page or slide geometry replaces it. |

## Density

*(Normative as constraints)*

Dense operational displays are the strongest consumer signal CDS holds, and density
is where accessibility obligations bite hardest.

1. **A density level is a declared spatial intensity**, not an ad-hoc compression.
2. **Density never reduces a target below its obligation** (2.5.8) — target sizing
   is a floor, and density operates above it.
3. **Density never removes a status qualifier.** A denser display shows the same
   truth in less space, or it declares that it cannot (VF-I-11).
4. **Density interacts with target size** and with reflow; the interaction is an
   open problem (WCAG matrix, open applicability question 6) and is **not solved
   here**.
5. **No density level, and no number of levels, is defined here.**

## Target sizing

*(Normative as an obligation; **no dimension is defined here**)*

- Target sizing is a **shared** obligation: CDS supplies size and spacing
  foundations; the consumer supplies the final composition (2.5.8).
- **No CDS size value exists**, so the obligation is currently unmeasurable — this
  is recorded, not worked around.
- The obligation is whatever the cited criterion itself requires. **CDS invents no
  additional threshold and restates no normative criterion text.**
- Pointer-alternative obligations (2.5.1, 2.5.2, 2.5.7) are **Layer-4 contract**
  concerns; the foundation supplies extent, not interaction behaviour.

## Document, page and presentation geometry

*(Normative as a boundary)*

| Channel | Spatial reality | Consequence |
| --- | --- | --- |
| **Product UI** | Continuous, resizable, reflowing | The responsive model applies |
| **Documentation** | Long-form, reflowing, DE/EN parity | Reading measure dominates |
| **Repository presentation** | **Platform-controlled rendering** | CDS covers what it authors, not what a host does with it |
| **PDF and reports** | **Paginated, fixed geometry, no reflow, possibly printed** | Ranges do not apply; page geometry replaces them; pagination introduces its own reading-order obligations |
| **Presentations** | Fixed slide geometry, distance viewing | Density models designed for operations are wrong here |
| **Diagrams** | Structural placement carries meaning | Position is meaningful and must therefore have a non-spatial carrier |
| **Data visualization** | Dense, encoding-sensitive | Position is an encoding channel and is never the only one |

**Spatial semantics do not transfer between these.** What transfers is meaning
(DEC-S-029, VF-I-11).

## What a Product Profile may do with spatial values

| A Product Profile **may** | A Product Profile **may never** |
| --- | --- |
| Override a spacing or size **value** at a **named, approved** extension point | Add, remove, rename, or repurpose a spatial **role** |
| Select among density options the core defines | Reduce a target below its obligation |
| — | Break reflow, resize, or text-spacing tolerance |
| — | Introduce a layout that removes core function at any range |
| — | Make position or proximity the sole carrier of meaning |

**No extension point is named today** (CDS-WP-032).

## Validation requirements

*(Requirements on **CDS-WP-024**. **No validator is changed here.**)*

A later validator must be able to detect: a spatial role named for its magnitude; a
role with no declared purpose; a component binding a spatial primitive directly; a
range identifier carrying a device, product, or brand term; a role that conveys
relationship with no declared non-spatial carrier; and a profile override outside a
named extension point.

Reflow, resize, magnification, and target-size behaviour are **not** structurally
checkable and require **rendering evidence** — which does not exist and is
CDS-WP-031's. **An automated check is never sufficient** (DEC-S-053).

## Evidence and claim boundary

Every spatial artifact in CDS is **AE-0**. Nothing has been rendered, reflowed,
magnified, or measured. **No accessibility claim of any level is valid.** VF-3 and
VF-5 in particular carry **no consumer demand evidence at all** — see the
[Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md).

## Deferred decisions

Spacing scale and step count · sizing scale · every value · grid structure ·
gutters · container extents · content widths · the responsive-range model and its
mechanism · the Layer 3 / Layer 5 split confirmation · density levels · target-size
values · document and presentation geometry standards · named extension points.

**Each requires its own explicitly authorized work package.**

## Related documents

- [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Typography Architecture](VISUAL_FOUNDATION_TYPOGRAPHY_ARCHITECTURE.md)
- [Visual Foundation Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md)
- [Visual Foundation Accessibility Mapping](../governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md)
- [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Architecture Requirements Traceability](ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md)
- [Accessibility Requirements Baseline](../governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [WCAG 2.2 AA Applicability Matrix](../governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md)
