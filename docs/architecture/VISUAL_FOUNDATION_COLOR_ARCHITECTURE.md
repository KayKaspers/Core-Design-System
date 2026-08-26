# Visual Foundation Colour Architecture

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for the structure of CDS colour.** It defines the colour
  architecture (**VF-1**) and **selects no colour**.
- **Maturity:** **`Proposed`** — this document promotes nothing.

## Purpose and boundary

This document defines **how colour is structured in CDS**: what a colour primitive
is, what a colour role is, how they relate, what a role must declare, and what may
never be done with colour.

**It chooses no colour.** No palette, no hue, no scale, no value, no colour space
selection, no light or dark instance, no brand colour, and no product colour.

Frame: [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md) ·
[Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md) — Layer 3,
token-flow layers 1 and 2.

**No colour value exists in CDS**, and none is created here.

## The one rule this architecture exists to enforce

> **Colour is a redundant carrier. It is never the only one.**

This is not a courtesy. It is architectural, because CDS scope includes paginated,
printed, greyscale, exported, and assistive-technology-mediated channels in which
colour is **absent or unreliable by construction**. A system whose meaning depends
on colour has no honest representation in half its own registered channels.

Sources: CR-006 (semantic status, never colour-only — the strongest multi-consumer
requirement CDS holds), DEC-S-028, DEC-S-056, DEC-S-111, WCAG **1.4.1 Use of
Color** (a **CDS-alone** obligation), Accessibility Requirements Baseline 3.6 and
7.3.

## Colour flows in one direction

*(Normative — an application of DEC-S-024)*

```text
Colour primitive  →  semantic colour role  →  [context re-binding]  →  [profile override]  →  generated output
   (layer 1)            (layer 2)               (resolution)            (layer 4)            (layer 5)
```

| Position | Owns | Never owns |
| --- | --- | --- |
| **Colour primitive** | A raw colour value with **no consumer meaning** | Any purpose, role, state, or status |
| **Semantic colour role** | **What the colour is for**, its pairing obligations, and its contrast obligation | A raw value of its own; knowledge of any component |
| **Resolution context** | Which primitive a role resolves to in a given context | The role's meaning, existence, or guarantee |
| **Product Profile override** | A value at a **named, approved** extension point | Any role, semantics, or accessibility guarantee |
| **Generated output** | An encoded, provenance-carrying derivative | Any decision at all |

**Prohibited, absolutely:**

```text
component  →  hard-coded colour value        (strips meaning; unthemeable; unprofileable)
component  →  colour primitive               (bypasses the semantic layer — DEC-S-024)
consumer   →  colour primitive               (imports a value, discards its purpose — VF-I-3)
role name  =  a colour's appearance          (forecloses theming — VF-I-2)
```

## Semantic colour role classes

*(Normative as a **classification**, not as a vocabulary. **No role name is created
here.** The concrete role set is CDS-WP-020's.)*

Every semantic colour role belongs to exactly one class, and the class determines
its obligations:

| Class | Purpose | Contrast obligation |
| --- | --- | --- |
| **Surface** | The ground a thing sits on | Is a **contrast partner**; carries no text contrast obligation of its own |
| **Content** | Text and other content foreground | **Contrast-sensitive** against a declared surface (1.4.3) |
| **Boundary** | Borders, separators, outlines, dividers | **Contrast-sensitive** where it conveys structure or a control boundary (1.4.11) |
| **Interaction** | Roles carrying an action's affordance and its interaction states | **Contrast-sensitive** for both content and non-text parts (1.4.3, 1.4.11) |
| **Focus** | The visible focus indicator | **Contrast-sensitive**, and a **CDS-alone** obligation (2.4.7) that may never be weakened |
| **Feedback** | Presentation roles for outcomes and conditions communicated to a person | **Contrast-sensitive**, and **never the sole carrier** (1.4.1) |
| **Emphasis** | Selection, current-location, and pointer emphasis | Contrast-sensitive where it conveys state |
| **Data** | Roles intended for data-visualization encoding | **Contrast-sensitive**, and **never the sole encoding channel** |

### Role obligations

*(Normative — every role, without exception)*

| # | Every semantic colour role must declare |
| --- | --- |
| **CR-1** | Its **class** from the table above |
| **CR-2** | Whether it is **contrast-sensitive**, and **against which** role or roles it is measured (**VF-I-8**) |
| **CR-3** | Its **valid pairings** — a foreground role names the surfaces it is defined against; a surface role names the content roles it must support |
| **CR-4** | Whether it participates in conveying meaning, and if so, **which non-colour carrier accompanies it** |
| **CR-5** | Whether it is a **named extension point** available to a Product Profile — **no role is one today** |
| **CR-6** | Its behaviour under a **reduced-colour condition**: greyscale, forced colours, and monochrome print |

> **A role that does not declare CR-2 cannot be validated, themed, or profiled
> safely, and must not exist.** An unstated contrast obligation is how a theme or a
> profile silently breaks conformance capability without anyone being able to
> detect it.

## Foreground and background pairing

*(Normative)*

1. **Contrast is a property of a pair, never of a single colour.** A colour role is
   never "accessible" on its own.
2. Every contrast-sensitive role declares its **pairing set**. A pairing outside
   that set is **undefined**, not merely discouraged, and must fail closed in
   validation.
3. **A context or profile change must preserve every declared pairing.** If it
   cannot, it is not a context change — it is a contract break.
4. **Pairing survives channel transformation.** A pairing that only holds on screen
   is not a pairing; see the
   [Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md).
5. **No contrast threshold is fixed here.** The obligation is whatever the cited
   WCAG criterion itself requires (1.4.3, 1.4.11). CDS restates no normative
   criterion text and invents no additional threshold
   (Accessibility Requirements Baseline, *"No concrete visual value is defined
   here"*).

## Non-colour communication

*(Normative — the rule that binds hardest)*

| # | Rule |
| --- | --- |
| **NC-1** | **Colour never carries meaning alone.** Wherever colour conveys something, a **text, structural, or accessible-semantics** carrier conveys the same thing. |
| **NC-2** | **The non-colour carrier is primary; colour is redundant.** Removing all colour must remove **no** meaning. Removing the text carrier is a defect, not a degradation. |
| **NC-3** | **Icon, shape, position, and motion do not satisfy NC-1 on their own.** Substituting one non-text sensory channel for another is the same failure (1.3.3, DEC-S-111). |
| **NC-4** | **A colour role is not a status.** Feedback and Data roles are presentation roles; they carry no status axis meaning (VF-I-6, VF-I-7). |
| **NC-5** | **This holds in every channel**, including greyscale print, exported diagrams, and presentations viewed at distance. |

## Interaction, feedback and state colour

*(Normative as constraints; **no state vocabulary and no value is fixed here**)*

| Concern | Constraint |
| --- | --- |
| **Destructive and far-reaching actions** | The **risk tier** is a Layer-4 contract concern (CR-010). The foundation may supply distinct Interaction roles for tiers; it decides no tier and permits **no colour-only** distinction of danger. |
| **Warning and caution** | A presentation role only. It is never `severity`, and it must never be the only signal that something needs attention. |
| **Success and completion** | A presentation role only. It must never imply `verified`, `current`, or `nominal` where those axes do not carry it. |
| **Error and validation failure** | A presentation role, accompanied by identification and, where possible, a suggestion (3.3.1, 3.3.3). Colour is not the identification. |
| **Disabled and read-only** | Must remain **perceivable** and must be **programmatically determinable** (4.1.2). **Reduced contrast alone is prohibited** as the carrier — it is precisely the encoding that fails for low-vision users, in greyscale, and in forced-colours conditions. |
| **Selected, active, current** | Must be conveyed by an accessible state, not by colour or position alone. Which of these are distinct roles is CDS-WP-020's. |
| **Focus visible** | A **CDS-alone** obligation (2.4.7). A Focus role may never be removed, suppressed, or weakened by a context, a profile, an exception, or a consumer override (DEC-S-059, invariant 10). |

## Data-visualization colour

*(Normative as a boundary; **CDS-WP-039 owns data-visualization design**)*

The visual foundation may declare a **Data** role class. It defines **no** chart
encoding, no categorical sequence, no scale, and no legend design.

Constraints any later data-visualization work inherits:

1. **Colour is never the only encoding channel.** Shape, pattern, label, direct
   annotation, or an alternative data representation must carry the same
   distinction.
2. **A textual explanation or an alternative data representation is required**
   (Accessibility Channel Profile 5).
3. **`No data` must be distinguishable from zero**, and from a value that exists
   but is unknown. This carries the Unknown invariant into a visual medium.
4. **Confidence and freshness must remain distinguishable** from the value itself.
5. **Dense encoding gets no exemption.** It is where the non-colour rule bites
   hardest and where every prohibited shortcut is most tempting.
6. Exported visualizations lose the web target and **require a channel profile**
   before Candidate or Stable (DEC-S-058).

## Colour under reduced-colour conditions

*(Normative — an obligation on every role, not an optional mode)*

| Condition | Obligation |
| --- | --- |
| **Greyscale and monochrome print** | Every distinction that conveys meaning survives, through a non-colour carrier. |
| **Forced colours and platform high contrast** | The artifact **remains usable** (Accessibility Requirements Baseline 3.5). Whether CDS additionally ships a high-contrast context is **open** and is CDS-WP-022's. |
| **Colour-vision differences** | No meaning depends on distinguishing hues. Pairs that differ only in hue must not be the sole distinction between two meanings. |
| **Reduced or degraded rendering** | A role that cannot be rendered must degrade to a state that loses no meaning, and the limitation must be **declared** (VF-I-11). |

## Colour space and encoding

*(Deliberately open — DEC-S-032)*

The CDS Token Format Profile pins **DTCG 2025.10** and uses the Color Module's
structure **as defined**, selecting **no** colour value. Consequently:

- **Which colour space CDS authors in is not decided here.** It is CDS-WP-020's.
- **No gamut, no encoding, and no conversion rule is selected.**
- Whatever is chosen must satisfy the existing determinism requirement: the same
  source revision plus the same transformation revision yields the same output
  (DEC-S-080), computable **offline** with no external service (DEC-S-030).
- A conversion performed during channel transformation is a **transformation**, and
  it may not introduce a decision absent from the source, nor discard a declared
  pairing or contrast obligation.

## What a Product Profile may do with colour

*(Normative — summary; detail in the
[Brand and Product Profile Boundary](../governance/VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md))*

| A Product Profile **may** | A Product Profile **may never** |
| --- | --- |
| Override a colour **value** at a **named, approved** extension point | Add, remove, rename, merge, or repurpose a colour **role** |
| Select among options the core defines | Change what a role means |
| Express product identity within brand governance | Weaken or remove a declared contrast obligation |
| — | Suppress or weaken the Focus role |
| — | Make colour the sole carrier of anything |
| — | Reach past a named extension point into the core |

**No extension point is named today, so no colour override is possible today.**
Naming extension points is CDS-WP-032's and requires Human-Maintainer approval.

## Validation requirements

*(Stated as requirements on **CDS-WP-024**. **No validator is changed here.**)*

A later validator must be able to detect:

| # | Detection |
| --- | --- |
| 1 | A semantic colour role with **no declared class** |
| 2 | A contrast-sensitive role with **no declared pairing set** (CR-2, CR-3) |
| 3 | A role name that is an **appearance name** (VF-I-2, N-1) |
| 4 | A role name reusing a **status axis or status value** name (N-4) |
| 5 | A **component binding a colour primitive** directly (DEC-S-024) |
| 6 | A **context that removes a role** or breaks a declared pairing (VF-I-9) |
| 7 | A **profile override outside a named extension point** (DEC-S-025) |
| 8 | A role that participates in meaning with **no declared non-colour carrier** (NC-1) |

**An automated check is never sufficient accessibility evidence** (DEC-S-053). Each
detection above is a structural check; none of it demonstrates that anything is
perceivable by a person.

## Evidence and claim boundary

- Every colour artifact in CDS is **AE-0**. None exists, none has been evaluated.
- **No contrast has been measured**, because there is nothing to measure.
- **No accessibility claim of any level is valid**, and defining a contrast
  obligation proves nothing (DEC-S-050).
- WCAG conformance would still not mean *accessible* — the Recommendation states
  that even AAA will not serve every disability.

## Deferred decisions

Palette · hue set · scale structure and step count · every colour value · colour
space and encoding · light and dark instances · high-contrast instance · the
concrete role vocabulary · data-visualization sequences · brand colour · product
colour · named extension points.

**Each requires its own explicitly authorized work package.**

## Related documents

- [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Theme Architecture](VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
- [Visual Foundation Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md)
- [Visual Foundation Accessibility Mapping](../governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md)
- [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md)
- [CDS Token Format Profile](CDS_TOKEN_FORMAT_PROFILE.md)
- [Accessibility Requirements Baseline](../governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [WCAG 2.2 AA Applicability Matrix](../governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md)
- [Semantic Status Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
