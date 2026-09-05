# Visual Foundation Theme Architecture

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Amended by:** CDS Step-9 Decision Integration Pass, 2026-09-05 — a new *Theme
  sequencing* section, to apply **DEC-S-135**. **That amendment is `PROPOSED /
  AUTHORIZED FOR INTEGRATION` and NOT YET EFFECTIVE**; it becomes effective only at
  the Human-Maintainer exact integration commit of the reviewed object. **It
  decides no theme mechanism, creates no theme and no context, and authorizes no
  work package**, and T-1 … T-10, the candidate contexts, and the Product Profile
  boundary are unchanged.
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for what a CDS theme is and what it may do.** It defines
  **VF-9** as a set of constraints and **creates no theme**.
- **Maturity:** **`Proposed`** — this document promotes nothing.

## Purpose and boundary

This document defines **what a theme is in CDS**, where it sits, what it may
change, and what it may never change.

**It creates no theme.** No light theme, no dark theme, no high-contrast theme, no
print context, and no theme value. It also **does not decide the theme
mechanism** — that remains open and is CDS-WP-022's.

Frame: [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md) ·
[Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md).

Consumer anchor: **CR-025 — Light and dark themes** (*Could*, documented planned
capability, two consumers).

## What a theme is

*(Normative)*

> **A theme is a presentation context that re-binds semantic roles to primitives.
> It is not a layer, not a brand, not a profile, and not a channel.**

| A theme **is** | A theme **is not** |
| --- | --- |
| A named resolution context | A token-flow layer |
| A re-binding of role → primitive | A redefinition of what a role means |
| Composed in a defined, deterministic order | An ad-hoc override set |
| Applicable across products | A product identity |
| A presentation concern | A meaning concern |

## Theme is not a layer

*(Normative — an application of DEC-S-024)*

DEC-S-024 defines **exactly five** token-flow layers. A theme is **not** a sixth.

A theme is a **resolution context**: the Resolver / Composition document declares
how source sets and conditional modifiers combine, **in a defined order**, to
resolve a context. The resolver *"introduces no new value or meaning and does not
invert the downward dependency direction"*.

**Treating a theme as a layer is an architectural defect**, because a layer can
hold a decision and a context cannot. A context selects among approved values; it
never creates one.

## Theme ≠ Brand ≠ Product Profile

*(Normative — three different authorities that are routinely conflated)*

| | Theme | Brand | Product Profile |
| --- | --- | --- | --- |
| **What it is** | A presentation context | An identity | A governed, bounded variation artifact |
| **Architecture layer** | 3 — Foundations | 2 — Brand and Identity | 1 → 2 governance, applied at token-flow layer 4 |
| **Scope** | Applies **across** products | Expresses **who** something is | Applies to **one** product |
| **Who selects it** | Typically the **person viewing**, or their environment | CDS Layer 2 governance | CDS approval, applied by a consumer |
| **What it may change** | Which primitive a role resolves to | Identity expression within governance | Values at **named, approved** extension points |
| **What it may never change** | Role meaning, role existence, accessibility guarantees | Accessibility, shared semantics | Roles, semantics, accessibility, status truth |
| **Exists today** | **No** | **No** | **No — and none can be approved** |

**A theme is not a small Product Profile.** A profile expresses *which product this
is*; a theme expresses *under what conditions this is being viewed*. Collapsing
them produces a system where changing to dark mode is governed like a brand
decision, or where a product's identity silently changes with the ambient light.

## Theme is not a channel

*(Normative — a classification rule, because the two overlap)*

Print, documentation, and presentation are **registered channels** (Layer 6), not
themes. A "print theme" and the PDF channel are not the same construct, even where
they produce similar output.

> **A context that varies *within* a channel is a theme. A context that *is* a
> channel is channel scope.**

| Case | Classification |
| --- | --- |
| Light and dark within the product UI | **Theme** |
| High contrast within the product UI | **Theme** *(mechanism open — see below)* |
| A paginated report | **Channel** — PDF and reports |
| A slide deck | **Channel** — presentations |
| Long-form web documentation | **Channel** — documentation |
| Greyscale output of a paginated report | A **channel** condition, handled by the channel's degradation rules |

Consequence: a channel needs an **accessibility profile** before its artifacts may
reach Candidate or Stable (DEC-S-058); a theme does not create a new channel and
does not escape its channel's profile requirement.

## Theme constraints

*(Normative — binding on any theme mechanism CDS-WP-022 later chooses)*

| # | Constraint |
| --- | --- |
| **T-1** | **A theme re-binds; it never redefines** (VF-I-9). It may change which primitive a role resolves to. It may not change what the role means. |
| **T-2** | **A theme may not add or remove a role.** Every semantic role must resolve in every supported context — or the context **declares the limitation** (VF-I-11). A silently unresolved role is a fail-closed condition, not a fallback. |
| **T-3** | **A theme may not weaken an accessibility guarantee.** Every declared contrast obligation and every declared pairing must hold in **every** context (VF-I-8, CR-2, CR-3). |
| **T-4** | **A theme may never remove or weaken the focus indicator** (F-4). |
| **T-5** | **A theme is never a meaning carrier.** Nothing may be communicated by *which theme is active*, and no status, state, or severity may be expressed by a theme difference (VF-I-5, VF-I-6). |
| **T-6** | **Theme resolution is deterministic**: the same source revisions plus the same resolver plus the same context yield the same resolved result (DEC-S-080). |
| **T-7** | **Theme resolution is offline.** No context may require an external runtime service to resolve (DEC-S-030, invariant 12). |
| **T-8** | **Theme is a resolution input, not a path segment.** A theme name never appears inside a shared semantic identifier (N-6). |
| **T-9** | **A theme carries provenance.** Any generated per-theme output identifies its source revision, transformation revision, and resolved context (DEC-S-031). |
| **T-10** | **A theme is not a place to fix a core gap.** If a role only works in one context, the role is wrong — raise it, do not paper over it with a context (anti-fragmentation rule 3, applied). |

## Theme sequencing

*(Normative — **DEC-S-135**, CDS Step-9 Decision Integration Pass, 2026-09-05.
**`PROPOSED / AUTHORIZED FOR INTEGRATION` and NOT YET EFFECTIVE.** It **decides no
theme mechanism** — that remains CDS-WP-022's and is untouched. **No ADR** —
DEC-S-135 is deliberately not an architecture dependency of ADR-0005.)*

| # | Rule |
| --- | --- |
| **TS-1** | **No semantic visual role carries a default alias to a reference primitive before CDS-WP-022 decides the Theme and Context Mechanism.** |
| **TS-2** | **CDS-WP-022 precedes context-sensitive value selection.** |
| **TS-3** | **Context-independent work is not blocked.** Identifier grammar, scale ownership and topology rules, role admission policy, family maturity governance, and **source-set structural identity** are context-independent by **TC-1**, **TC-2**, **T-8**, **N-6** and **RB-1**. |
| **TS-4** | **`CDS-WP-022 BEFORE VALUE SELECTION` does not mean `CDS-WP-022 BEFORE EVERY SOURCE-STRUCTURE OR IDENTITY ACTIVITY`.** Declaring a source set's identity is a structural act; what TS-2 gates is its **content**. |
| **TS-5** | **A theme remains a Resolution Context and is not a sixth token-flow layer** (DEC-S-024), and **A THEME RE-BINDS; IT NEVER REDEFINES** (T-1, VF-I-9). **TC-6 continues to bind independently of this rule.** |
| **TS-6** | **This authorizes no work package.** CDS-WP-022 is the recommended and sequenced Step-10 candidate only — **SEQUENCED NEXT ≠ AUTHORIZED** — and it remains `Planned`, not active, and not authorized, as do `CDS-WP-020A` and CDS-WP-021 … CDS-WP-053. |

**Why the rule exists.** **T-2 is vacuously satisfiable today** — zero contexts are
supported — so it cannot judge whether a single default binding is a legitimate
starting state. A default binding taken now would silently become *the light theme*
and hand CDS-WP-022 a decision it exists to make, satisfying **TC-6** in form while
violating it in substance. The evidence cost is decisive: a value selected before
the context model and re-selected after it produces a new source revision, and **a
new revision inherits no evidence and no admission** (AF-2, RV-4, DEC-S-126,
DEC-S-131 clause 10).

## Candidate contexts

*(Registered as **candidates for evaluation**, not as themes. **None exists, none
is selected, and listing one commits CDS to nothing.**)*

| Context | Consumer evidence | Status |
| --- | --- | --- |
| **Light** | CR-025 (*Could*, two consumers, documented planned capability) | Candidate for evaluation by CDS-WP-022 |
| **Dark** | CR-025, as above | Candidate for evaluation by CDS-WP-022 |
| **High contrast / forced colours** | **No consumer requirement.** Derived from Accessibility Requirements Baseline **3.5** — *"forced-colors and high-contrast conditions remain usable"* (Implementation-dependent) | **Open**: whether CDS ships a context, honours the platform's, or both — CDS-WP-022 |
| **Neutral / document** | No consumer requirement | Open; may prove to be a **channel** concern rather than a theme |

**Print and presentation are deliberately absent from this table** — they are
channels, per the classification rule above.

### The high-contrast question

Baseline 3.5 requires that artifacts **remain usable** under forced colours and
platform high contrast. That obligation holds **whether or not CDS ships a
high-contrast theme**.

Three readings are architecturally admissible, and **CDS-WP-019 selects none**:

1. CDS ships a high-contrast context of its own.
2. CDS ships none and guarantees that its artifacts honour the platform's.
3. Both, with a declared precedence between them.

Each has real consequences for the role model, the evidence burden, and the support
baseline. Choosing among them is a design decision with an evidence obligation, and
it is **CDS-WP-022's** — recorded here as open rather than assumed.

## The open mechanism question

*(Deliberately open — this is the question CDS-WP-019 explicitly does not answer)*

The [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md) records, and
CDS-WP-019 leaves open:

> *"How is theme selection expressed — and is a theme a profile concern, a semantic
> concern, or both?"* and *"What token layering does light/dark support imply
> (CR-025)?"*

Admissible mechanisms include a resolver-modifier context, a separate context
source set, a combination, or something else that satisfies **T-1 … T-10**.

**CDS-WP-019 selects none of them**, because selecting one would be a new normative
choice, and this work package makes none. It fixes the constraints instead, so that
whichever mechanism CDS-WP-022 proposes can be judged against something.

> **If a proposed mechanism cannot satisfy T-1 … T-10, the mechanism is wrong — not
> the constraints.**

## What a Product Profile may do with themes

| A Product Profile **may** | A Product Profile **may never** |
| --- | --- |
| Override a value **within** a context at a **named, approved** extension point | Define a new context |
| Select among contexts the core supports | Remove a context a consumer depends on |
| — | Change what a role means in any context |
| — | Weaken a contrast obligation or the focus indicator in any context |
| — | Use a context to reach a value it may not override directly |

The last prohibition matters: **a context must not become a back door around the
extension-point boundary.** Overriding through a theme what a profile may not
override directly is the same violation with an extra step.

**No extension point is named today** (CDS-WP-032).

## Validation requirements

*(Requirements on **CDS-WP-024**. **No validator is changed here.**)*

A later validator must be able to detect: a context that adds or removes a role; a
context in which a declared pairing or contrast obligation does not hold; a context
that removes or weakens a focus role; a theme name appearing in a shared semantic
identifier; a non-deterministic or externally-dependent resolution; a resolved
output with no declared context provenance; and a profile override reaching a value
through a context that it may not override directly.

**An automated check is never sufficient accessibility evidence** (DEC-S-053).
Whether a context is *usable* requires rendering and assistive-technology evidence
that does not exist.

## Evidence and claim boundary

**No theme exists in CDS.** No context has been rendered, resolved, or evaluated,
and every theme-related artifact is **AE-0**. Evidence never transfers between
contexts any more than between channels: a future light-context evidence package
evidences **nothing** about a dark context.

## Deferred decisions

The theme mechanism · the token layering light and dark imply · whether high
contrast is a CDS context, a platform behaviour, or both · the context set · every
context value · context precedence and composition order · how a viewer's
preference is expressed · named extension points.

**Each requires its own explicitly authorized work package**, and CDS-WP-022 is
`Planned`, not active, and not authorized.

## Related documents

- [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
- [Visual Foundation Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md)
- [Visual Foundation Brand and Product Profile Boundary](../governance/VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md)
- [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md)
- [Machine-Readable Source Model](MACHINE_READABLE_SOURCE_MODEL.md)
- [Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
- [Accessibility Requirements Baseline](../governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
