# Visual Foundation Accessibility Mapping

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for accessibility applicability across the visual
  foundation.** It is a **policy mapping**, not an evaluation.
- **Maturity:** **`Proposed`** — this document promotes nothing.

## Purpose and boundary

This document maps the **visual foundation families** (VF-1 … VF-9) onto the
existing normative accessibility sources: the
[Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md),
the [Accessibility Requirements Baseline](ACCESSIBILITY_REQUIREMENTS_BASELINE.md),
and the [WCAG 2.2 AA Applicability Matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md).

### What this mapping is not

> **No artifact has been evaluated. No pass or fail exists. No accessibility claim
> of any level is valid.**

A mapping assigns responsibility and future evidence; **it proves nothing**
(DEC-S-050). Missing implementation does not make a criterion inapplicable — it
makes it **not yet assessable**, and every criterion below has an owner regardless.

**This document introduces no accessibility requirement.** Every requirement below
already exists in a committed normative source; this document states **which visual
foundation family carries it**.

## Evidence state — stated first, because it governs everything else

| Item | Value |
| --- | --- |
| Visual foundation artifacts in existence | **0** |
| Visual foundation artifacts evaluated | **0** |
| Evidence level of every visual foundation artifact | **AE-0** |
| Manual, keyboard, screen-reader, or assistive-technology testing performed | **None, anywhere** |
| Baseline environments exercised | **None** — A11Y-BL-001 is a **test contract, not evidence** |
| AE-1 / AE-2 / AE-3 / AE-4 for any visual family | **None** |
| Accessibility claim | **None valid, by anyone, including CDS itself** |
| Conformance | **None** |

The single admitted evidence package in CDS — **`AE1-CDS-WP016-SEMSTATUS-004`** at
**AE-1** — covers the **channel-independent Semantic Status source/contract family
only**. It **does not transfer** to any visual family, any channel, any consumer,
or any other source revision (DEC-S-126).

## The finding that shapes this mapping

*(Derived by re-counting the WCAG 2.2 AA Applicability Matrix, not asserted)*

The matrix classifies **5** of its 56 rows as **`Normative CDS requirement`** — the
criteria CDS owns **without** the consumer. All five map to **architecture Layer 3**:

| SC | Title | Level | Visual foundation family |
| --- | --- | --- | --- |
| **1.3.3** | Sensory Characteristics | A | Cross-family — VF-1, VF-3, VF-5, VF-7, VF-8 |
| **1.4.1** | Use of Color | A | **VF-1 Colour** |
| **1.4.5** | Images of Text | AA | **VF-2 Typography**, VF-7 |
| **2.3.1** | Three Flashes or Below Threshold | A | **VF-8 Motion** |
| **2.4.7** | Focus Visible | AA | **Focus role set** — VF-1, VF-5, VF-3 |

> **Every criterion CDS owns alone is a visual foundation criterion.**

This is not a coincidence and it is not a convenience. A design system can supply a
contract, a role, a state mechanism, and a semantic slot; it cannot supply the
content, the composition, or the process. The five things it *can* own end-to-end
are exactly the non-sensory-meaning, focus-visibility, and flashing obligations —
and all of them live in the foundation.

**Consequence:** these five are the visual foundation's **own** obligations. There
is no consumer to share them with, and no composition argument that shifts them.

## Layer-3 WCAG applicability

*(Extracted from the WCAG matrix — all rows whose registered layer set includes
Layer 3. **14** criteria.)*

| SC | Title | Level | Policy status | Carried by |
| --- | --- | --- | --- | --- |
| 1.1.1 | Non-text Content | A | Shared | VF-7 |
| 1.3.1 | Info and Relationships | A | Shared | VF-2 (hierarchy is not size), VF-3, VF-5 |
| **1.3.3** | Sensory Characteristics | A | **CDS-alone** | Cross-family |
| **1.4.1** | Use of Color | A | **CDS-alone** | VF-1 |
| 1.4.3 | Contrast (Minimum) | AA | Shared | VF-1, VF-2 |
| 1.4.4 | Resize Text | AA | Shared | VF-2, VF-3, VF-4 |
| **1.4.5** | Images of Text | AA | **CDS-alone** | VF-2, VF-7 |
| 1.4.10 | Reflow | AA | Shared | VF-3, VF-4 |
| 1.4.11 | Non-text Contrast | AA | Shared | VF-1, VF-5, VF-6, VF-7 |
| 1.4.12 | Text Spacing | AA | Shared | VF-2, VF-3 |
| **2.3.1** | Three Flashes or Below Threshold | A | **CDS-alone** | VF-8 |
| **2.4.7** | Focus Visible | AA | **CDS-alone** | Focus role set |
| 2.5.8 | Target Size (Minimum) | AA | Shared | VF-3 |
| 4.1.2 | Name, Role, Value | A | Shared | State roles across families |

**Every one of these is `Not yet assessable` in practice**, because no artifact
exists. The matrix records **policy** state; the evidence model records the
**evidence** state, which is AE-0 throughout.

**AAA is out of scope** for this mandatory A/AA mapping (DEC-S-049), and no AAA
criterion is adopted here.

## Requirements-baseline coverage

*(Which of the **69** registered requirements the visual foundation carries. The
remainder belong to Layers 4, 5, 6, or the consumer.)*

### Area 2 — Keyboard and Focus

| # | Requirement | Class | Visual foundation position |
| --- | --- | --- | --- |
| 2.3 | **Visible focus** (2.4.7) | **Normative** | **Owned.** Focus role set; no permitted mechanism of removal |
| 2.4 | Focus must not be obscured or lost (2.4.11) | Implementation-dependent | VF-6 overlays and scrims are the hard case; **CDS has no pattern** |

Requirements 2.1, 2.2, 2.5, 2.6, 2.7 are **component and pattern** obligations
(Layer 4 / 5) and are not visual foundation obligations.

### Area 3 — Visual Access

*(All seven are visual foundation requirements — this is the foundation's own area)*

| # | Requirement | Class | Carried by |
| --- | --- | --- | --- |
| 3.1 | Contrast per 1.4.3 and 1.4.11 | Implementation-dependent | **VF-1**, VF-2, VF-5, VF-6 |
| 3.2 | Reflow (1.4.10) | Implementation-dependent | **VF-3**, **VF-4** |
| 3.3 | Resize and magnification (1.4.4) | Implementation-dependent | **VF-2**, VF-3, VF-4 |
| 3.4 | Text spacing tolerance (1.4.12) | Implementation-dependent | **VF-2**, VF-3 |
| 3.5 | Forced-colors and high contrast remain usable | Implementation-dependent | **VF-9**, VF-1 — mechanism **open** |
| 3.6 | **Meaning without colour** (1.4.1) | **Normative** | **VF-1 — owned** |
| 3.7 | **No information by proximity or position alone** (1.3.3) | **Normative** | **VF-3, VF-4 — owned** |

**Reflow and text spacing are the hardest cases for dense operational data** —
CDS's most-evidenced consumer need and its least-solved layout problem. Recorded as
unresolved, not designed around.

### Area 4 — Motion, Animation and Time

| # | Requirement | Class | Visual foundation position |
| --- | --- | --- | --- |
| 4.1 | Reduced-motion support | **Normative** | **VF-8** boundary constraint |
| 4.2 | No unnecessary or hazardous motion (2.3.1) | **Normative** | **VF-8 — CDS-alone** |
| 4.5 | **Motion never the sole carrier of meaning** | **Normative** | **VF-8 — owned** |

Requirements 4.3 and 4.4 are content and timing obligations at Layers 4 and 5.
**The Motion System itself is CDS-WP-035's**; only the boundary is fixed here.

### Area 7 — Status, Alerts and Dense Operational Data

*(The area with CDS's strongest consumer evidence — and the area where the visual
foundation's role is deliberately **subordinate**)*

| # | Requirement | Class | Visual foundation position |
| --- | --- | --- | --- |
| 7.3 | **Colour never the sole carrier** (1.4.1) | **Normative** | **VF-1 — owned** |
| 7.4 | **Unknown, freshness, and confidence perceivable** | **Normative** | **Not a visual obligation to satisfy — a visual obligation not to defeat.** Meaning is owned by the Semantic Status Foundation |
| 7.6 | Changes not visible-only | **Normative** | Constrains every visual state role |

> **The visual foundation cannot make status honest. It can only fail to make it
> dishonest.** Truthfulness is carried by the status contract and by text; visual
> encoding is redundant to it (VF-I-6).

### Area 8 — Localization and Internationalization

| # | Requirement | Class | Carried by |
| --- | --- | --- | --- |
| 8.3 | **Flexible text lengths** | **Normative** | **VF-2**, VF-3, VF-4 |
| 8.4 | **No layout-critical text assumptions** | **Normative** | **VF-3**, **VF-4** |
| 8.6 | **Text direction and bidirectional content not architecturally excluded** | **Normative** | VF-2, VF-3, VF-4 — a **structural constraint, not a commitment to ship right-to-left support** |

### Area 9 — Documents and Non-web Channels

All eight requirements are **channel-specific** (DEC-S-058) and cannot be assessed
until each channel has a profile. Two bind the visual foundation directly:

| # | Requirement | Visual foundation position |
| --- | --- | --- |
| 9.7 | Meaning without colour | Holds in **every** channel, including print (VF-I-5) |
| 9.8 | Accessible alternative representation for diagrams and visualizations | VF-1 Data roles constrain it; **CDS-WP-039** owns it |

### Areas 1, 5, 6, 10

These are **structure, cognitive, forms, and safety** obligations owned at Layers 4
and 5 or by the consumer. The visual foundation supplies roles they may use — and
supplies **no** substitute for them.

Two constraints reach back into the foundation and are recorded here:

- **Baseline 5.7 — Simple/Expert without hiding function or status.** A responsive
  or density reduction may hide *complexity*; it may never hide that an option
  exists, misrepresent status, or conceal a risk.
- **Baseline 10.5 — Dangerous actions accessibly confirmable and cancellable.** The
  foundation may supply distinct Interaction roles for risk tiers; it decides no
  tier, and **colour-only** danger encoding is prohibited.

## Responsibility split

*(An application of DEC-S-051 and DEC-S-052 — nothing new)*

| CDS owns (visual foundation) | The consumer owns |
| --- | --- |
| Role definitions and their declared obligations | The composition those roles are used in |
| Contrast **capability** of a role pair | Final values in a profile and in the product |
| Non-colour carrier **slots** | The actual content that fills them |
| Focus role existence and non-removability | Not suppressing it through local overrides |
| Reflow, resize, and text-spacing **tolerance** in the foundation | Product layout behaviour |
| Declared channel limitations | Product testing in the declared scope |
| Known limitations, stated honestly | The consumer's own claims |

> **Using accessible CDS artifacts does not make a product accessible or
> conformant** (DEC-S-052). **49 of 56** criteria require action from both sides.
> Composition, content, and context are where accessibility is usually lost, and
> all three are consumer-owned.

## Gate applicability

| Gate | Requirement | Satisfiable for a visual family today? |
| --- | --- | --- |
| **Candidate** | Mapping · responsibility · **AE-1** · AE-2 or plan · limitations · baseline plan · regression plan | **No.** No artifact exists to evidence. This document supplies the *mapping* only — one element of seven. |
| **Stable** | Candidate gate · render evidence · **AE-2 complete + AE-3 against a declared baseline** · consumer evidence · no critical limitations | **No.** AE-2 and AE-3 exist **nowhere in CDS**. |
| **Product Profile** | Scope-appropriate accessibility evidence | **No.** No profile can be approved. |

**Accessibility cannot be waived by an ordinary exception** (DEC-S-059). A visual
family that cannot meet an accessibility obligation does not get an exception; it
does not get promoted.

### The channel-profile boundary

**DEC-S-125** applies directly here: channel accessibility profiles gate **channel
artifacts**, not **channel-independent Layer-3 sources and contracts**.

The visual foundation architecture and its future Layer-3 sources are
channel-independent. A missing PDF or presentation profile therefore does **not**
block a Layer-3 source from reaching its own gate — and, symmetrically, a Layer-3
source reaching a gate grants **nothing** to any channel artifact. **Evidence
transfers in neither direction.**

## What would have to be true before any visual family could be Candidate

*(Recorded as a route to a gate. It is **never a pass through one**.)*

1. The artifact exists, at an **immutable source revision**.
2. Its accessibility requirements are **stated**, per this mapping.
3. Its **responsibility split** is recorded.
4. **AE-1 evidence** is produced against **those exact bytes**.
5. That evidence is **independently reviewed** by a reviewer who is **not** its
   executor.
6. The Human Maintainer **admits** the evidence — a separate decision that
   **precedes** approval (DEC-S-126).
7. **AE-2 evidence or a reasoned AE-2 plan** exists.
8. A **support-baseline plan** exists on a `Current` A11Y-BL-001.
9. A **regression plan** exists.
10. **Limitations are stated honestly**, with no Critical limitation open.
11. Nova reviews; the **Human Maintainer approves**.
12. The **exact-byte Promotion Commit** makes it effective.

**Steps 1 … 12 have been executed exactly once in CDS**, for the Semantic Status
family. **Nothing about that transfers here.**

## Limitations of this mapping

- **Policy mapping only.** No artifact has been evaluated against any criterion.
- Responsibility assignments are **CDS policy judgements**, not standard text.
- A shared criterion cannot be satisfied by CDS alone, however good the contract.
- **No normative criterion text is reproduced**, and no threshold is restated or
  invented.
- **WCAG conformance would still not mean accessible** — the Recommendation itself
  states that even AAA will not serve every disability.
- Source status decays; re-verify before relying on it (RISK-012, RISK-047).
- Four of the nine visual families (**VF-3, VF-5, VF-6, VF-7**) carry **no consumer
  demand evidence at all**, so their accessibility obligations are derived from the
  standard and the policy, not from an evidenced consumer need.

## Related documents

- [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Channel Mapping](VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Visual Foundation Governance and Lifecycle](VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
- [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [Accessibility Requirements Baseline](ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [WCAG 2.2 AA Applicability Matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Accessibility Channel Profiles](ACCESSIBILITY_CHANNEL_PROFILES.md)
- [Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Responsibility Model](ACCESSIBILITY_RESPONSIBILITY_MODEL.md)
- [Accessibility Architecture Alignment](../architecture/ACCESSIBILITY_ARCHITECTURE_ALIGNMENT.md)
