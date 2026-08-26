# Visual Foundation Channel Mapping

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for how visual foundation families relate to the nine
  registered CDS channels.** It creates **no channel adapter**.
- **Maturity:** **`Proposed`** — this document promotes nothing.

## Purpose and boundary

This document states, per registered channel, **which visual foundation semantics
are directly reusable, mapped, reduced, transformed, or unsupported**.

**It creates no channel adapter**, no template, no export format, no channel
profile, and no channel artifact.

Frame: [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md) ·
[Artifact Distribution and Channel Model](../architecture/ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) —
the nine channel classes are registered there and are **not** extended here.

## The channel rule

*(Normative — DEC-S-029, architecture invariant 13)*

> **Channels share governed semantic foundations and retain their own
> transformation, layout, interaction, and evidence requirements.**
>
> **Presentation is free. Meaning is not.**

**There is no assumption that product UI, PDF, presentation, and diagram render
identically**, and forcing visual identity on them produces bad artifacts in all of
them. What may not differ is what something **means**.

## Classification vocabulary

*(Normative for this document)*

| Value | Meaning |
| --- | --- |
| **Directly reusable** | The semantics apply as-is; the channel imposes no material constraint on this family |
| **Mapped** | The semantics apply through a declared, meaning-preserving correspondence |
| **Reduced** | The channel expresses less than the source; **the reduction must be declared** and must lose no meaning |
| **Transformed** | The channel expresses the same meaning through a **different device** |
| **Unsupported** | The channel cannot carry this family at all; meaning must be carried elsewhere, and the limitation is **declared** |

> **`Reduced` and `Unsupported` are honest outcomes, not failures.** Silently
> dropping a distinction is the failure (VF-I-11).

## The nine channels

*(The channel set is DEC-S-029's. Accessibility profile status is from the
[Accessibility Channel Profiles](ACCESSIBILITY_CHANNEL_PROFILES.md); **only
profiles 1 and 2 have a target today**.)*

| # | Channel | Accessibility profile | Candidate-eligible today |
| --- | --- | --- | --- |
| 1 | **Product UI** | WCAG 2.2 AA | **No** — no evidence |
| 2 | **Repository presentation** | WCAG 2.2 AA where web-rendered | **No** — no evidence |
| 3 | **Documentation** | WCAG 2.2 AA where web-rendered | **No** — no evidence |
| 4 | **PDF and reports** | **Undefined — profile required** | **Blocked** |
| 5 | **Presentations** | **Undefined — profile required** | **Blocked** |
| 6 | **Diagrams** | Mixed — web-embedded inherits, exported does not | Web-embedded: no evidence · exported: **blocked** |
| 7 | **Data visualization** | Mixed, as above | As above |
| 8 | **Release materials** | **Undefined — usage rules required** | **Blocked** |
| 9 | **Selected communication materials** | **Undefined — usage rules required** | **Blocked** |

**Not one channel can produce a Candidate or Stable artifact today.**

## Family-by-channel matrix

*(Normative as a classification. It describes what a channel **can** carry, not
what CDS **will build** — and CDS has decided to build none of it.)*

| Family | 1 Product UI | 2 Repository | 3 Documentation | 4 PDF / reports | 5 Presentations | 6 Diagrams | 7 Data viz | 8 Release | 9 Communication |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **VF-1 Colour** | Directly reusable | **Reduced** — platform-controlled | Directly reusable | **Transformed** — greyscale possible | Transformed — distance viewing | Mapped | Mapped | Mapped | Mapped |
| **VF-2 Typography** | Directly reusable | **Reduced** — platform-controlled | Directly reusable | **Transformed** — paginated, embedding rules | **Transformed** — distance scale | Mapped | Reduced | Mapped | Mapped |
| **VF-3 Space and Size** | Directly reusable | **Reduced** | Directly reusable | **Transformed** — page geometry | **Transformed** — slide geometry | Mapped | Mapped | Mapped | Mapped |
| **VF-4 Layout and Grid** | Directly reusable | **Unsupported** — host controls layout | Mapped | **Transformed** — pagination replaces ranges | **Transformed** — fixed slide | Mapped | Mapped | Mapped | Mapped |
| **VF-5 Shape** | Directly reusable | **Reduced** | Mapped | Mapped | Mapped | Mapped | Mapped | Mapped | Mapped |
| **VF-6 Surface and Elevation** | Directly reusable | **Unsupported** | Reduced | **Reduced** — shadow largely vanishes in print | Reduced | **Reduced** | Reduced | Mapped | Mapped |
| **VF-7 Iconography** | Directly reusable | **Reduced** | Mapped | Mapped — alt text profile-dependent | Mapped — alt text profile-dependent | Mapped | Mapped | Mapped | Mapped |
| **VF-8 Motion** | Directly reusable | **Unsupported** | Reduced | **Unsupported** — paginated, non-interactive | **Unsupported** in exported form | **Unsupported** when exported | **Unsupported** when exported | Unsupported | Unsupported |
| **VF-9 Theme and Context** | Directly reusable | **Unsupported** — viewer-controlled | Mapped | **Transformed** — a channel condition, not a theme | Transformed | Mapped | Mapped | Mapped | Mapped |

### Reading the matrix

Three patterns matter more than the individual cells:

1. **Repository presentation is the least controllable channel.** Its rendering is
   **platform-controlled**; CDS cannot guarantee what a host does with what CDS
   authors. Five families are `Reduced` and four are `Unsupported` there — and
   that is a property of the channel, not a gap in the foundation.
2. **The paginated and printed channels lose exactly the families that most tempt
   a design system**: motion entirely, elevation nearly entirely, colour reliably.
   This is why the **non-colour rule is architectural rather than a web courtesy**
   — a status depending on colour, hover, or refresh **fails** in channel 4.
3. **Motion is `Unsupported` in seven of nine channels.** Any meaning carried by
   motion is meaning that most of CDS's registered channels cannot carry.

## Transformation boundaries

*(Normative — DEC-S-029, applied to visual output)*

A transformation from a visual foundation source to a channel output **may**:
select, filter, reformat, restructure for the channel's constraints, and encode for
a platform.

It **may not**:

| # | Prohibition |
| --- | --- |
| **TB-1** | Introduce a visual decision **absent from the source** |
| **TB-2** | **Discard semantics** the source carries |
| **TB-3** | Collapse separate status axes into one opaque value |
| **TB-4** | Make **colour the sole carrier** of meaning |
| **TB-5** | Drop a declared **contrast obligation** or **pairing** |
| **TB-6** | Remove or weaken a **focus indicator** in an interactive output |
| **TB-7** | Produce an output that **cannot identify its source** |

**TB-7 turns a transformation into laundering:** an artifact whose origin nobody
can establish is functionally normative, because nobody can contradict it
(RISK-025). Every generated visual output carries source revision, transformation
revision, and output identity (DEC-S-031).

## The declaration obligation

*(Normative — the rule that makes `Reduced` and `Unsupported` safe)*

Where a channel cannot preserve a distinction the source carries:

1. The limitation is **declared**, in the channel's own record.
2. The **meaning is carried by another modality** in that channel — normally text
   and structure.
3. The output is **not shipped** as though the distinction were present.
4. The declaration is **part of the channel's evidence**, not a footnote to it.

> **A channel that cannot render a distinction may not ship a representation that
> drops it silently.**

## Channel-specific visual constraints

*(Registered as structure. **None is designed here**, and no channel artifact is
created.)*

| Channel | Visual constraints that bind any later work |
| --- | --- |
| **1 Product UI** | Interaction, focus, assistive technology, live state change. The only channel where the full family set applies. Focus obligations are absolute. |
| **2 Repository presentation** | **Rendering is platform-controlled.** CDS covers what it authors; it guarantees nothing about a host's rendering, theme, or typography. |
| **3 Documentation** | Long-form; **DE/EN parity** and staleness control; accessible code and **diagram explanations** required. |
| **4 PDF and reports** | **Paginated, non-interactive, often printed, possibly greyscale.** No hover, no live update, no focus. Status must survive **without colour, interaction, or refresh**. Font embedding and licensing constraints apply. Consumer evidence is **weak** (CR-028). |
| **5 Presentations** | Fixed slide geometry; **distance legibility**; an operations density model is wrong here. **No consumer evidence at all** (CR-030) — registered to close the channel set, not because anyone asked. |
| **6 Diagrams** | **Structural meaning must survive export.** A textual explanation or alternative representation is required. Consumer evidence is **weak** (CR-029). |
| **7 Data visualization** | **The hardest channel.** Dense encoding tempts every prohibited shortcut. `No data` must be distinguishable from zero. **CDS-WP-039** owns it. |
| **8 Release materials** | Outward-facing and **claim-sensitive**: no adoption or conformance claim without evidence. **No claim is valid today.** |
| **9 Selected communication materials** | Brand and verbal identity; **usage rules do not exist**. **Brand approval is never an accessibility claim.** |

## Evidence honesty about channels

*(Recorded so this mapping is not read as demand)*

- **No reviewed design system documented standards for PDF reports, presentations,
  or diagrams**, and CDS's own consumer evidence for those channels is weak to
  absent: **CR-028 and CR-029 are weak; CR-030 has no consumer evidence at all.**
- **Registering a channel class registers structure, not demand.** Nothing here
  asserts that CDS will build a channel, or that a consumer needs one.
- **Evidence never transfers between channels** (DEC-S-052). A future Product-UI
  evidence package evidences **nothing** about a PDF.
- **No channel evidence of any level exists in CDS.**

## Relationship to DEC-S-125

*(Normative — the boundary that keeps this mapping from over-reaching)*

Channel accessibility profiles gate **channel artifacts**. They do **not** gate
**channel-independent Layer-3 semantic sources and contracts**.

| Statement | Consequence |
| --- | --- |
| The visual foundation architecture is **channel-independent** | A missing PDF or presentation profile does **not** block it |
| A visual **channel artifact** is channel-bound | It **is** gated by that channel's profile, and four of nine channels have none |
| Evidence transfers in **neither** direction | A Layer-3 gate grants nothing to a channel; a channel gate grants nothing to Layer 3 |

**This is not a waiver.** No accessibility requirement is relaxed for anything, and
no Candidate is awarded to anything.

## Deferred decisions

Channel adapters · export formats · templates · the PDF, presentation, exported
diagram, and brand-material **accessibility profiles** · document and presentation
standards · the transformation tool · per-channel degradation rules · which
channels CDS actually builds, and in what order.

**Each requires its own explicitly authorized work package.** Channel adapters are
CDS-WP-048 … CDS-WP-050; multi-channel preservation is CDS-WP-034.

## Related documents

- [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Accessibility Mapping](VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md)
- [Visual Foundation Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
- [Artifact Distribution and Channel Model](../architecture/ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md)
- [Accessibility Channel Profiles](ACCESSIBILITY_CHANNEL_PROFILES.md)
- [Evidence, Traceability and Status Semantics](../architecture/EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md)
- [Status Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md)
