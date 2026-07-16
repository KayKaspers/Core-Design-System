# Token and Theme Architecture

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-005 — Design System Architecture
- **Date:** 2026-07-16
- **Status:** **Normative** for the conceptual token flow

## Purpose and boundary

This document defines **how design decisions flow** through CDS — not what they
are.

**No token value, no token name, no naming convention, no format, no build tool,
and no design tool is selected here** (DEC-S-024, DEC-S-032). Every example of a
*category* below is structural, never a proposal.

The reviewed token interoperability draft explicitly identifies itself as a
preview that instructs readers not to implement it or cite it as authoritative.
No format may be selected on its basis today. That is why this document defines a
flow and stops.

Frame: [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) — Layer 3.

## Conceptual token layers

*(Normative, DEC-S-024)*

Exactly five layers, in one direction:

```
Reference Tokens
   → Semantic Tokens
      → Component Tokens
         → Product Profile Overrides
            → Channel or Platform Outputs
```

| # | Layer | Owns | Does not own |
| --- | --- | --- | --- |
| **1** | **Reference Tokens** | Raw technical values. The system's primitives. | Any consumer-facing meaning. |
| **2** | **Semantic Tokens** | Role and meaning — *what a decision is for*. | Raw values of its own; component knowledge. |
| **3** | **Component Tokens** | Binding of semantic decisions to component contracts. | New meaning; new raw values. |
| **4** | **Product Profile Overrides** | Approved product-specific variation at named extension points. | Shared semantics; accessibility guarantees. |
| **5** | **Channel or Platform Outputs** | Transformation into consumable form per channel or platform. | Any decision at all — it is generated. |

### Layer responsibilities

**Reference Tokens** are technical starting values with **no immediate consumer
semantics**. A consumer must never bind to a reference token directly: doing so
imports a value while discarding its meaning, which is exactly the coupling this
architecture prevents.

**Semantic Tokens** express *role and meaning*. This is where the design decision
actually lives, and where a human argument about intent is possible. Semantic
tokens are the layer that makes CDS reviewable.

**Component Tokens** bind semantics to a component contract. They are a *binding*,
not a decision: a component token that introduces meaning absent from the
semantic layer is a defect, not a shortcut.

**Product Profile Overrides** modify **only explicitly approved extension
points** (DEC-S-025). See
[Product Profile and Extension Model](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md).

**Channel or Platform Outputs** transform normative sources into consumable
formats. They are **Generated Artifacts** (authority class 3): never normative,
always provenance-carrying, never hand-edited.

## Semantic-first principle

*(Normative)*

**Semantics take precedence over product-specific or colour-derived raw naming.**

A decision must be expressible as *what it is for*, not *what it looks like* or
*which product asked for it*. Concretely:

- Meaning-carrying layers must not be named after appearance.
- A raw appearance name in a semantic position is an architectural defect,
  because it forecloses theming, profiles, and channel transformation
  simultaneously.
- The status foundations are semantic by construction — see
  [Evidence, Traceability and Status Semantics](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md).

This principle is what makes CR-006 (semantic status representation, never
colour-only) an architectural property rather than a styling guideline.

## Alias and dependency direction

*(Normative)*

Dependency flows **strictly downward through the five layers**.

Permitted:

- Semantic → Reference
- Component → Semantic
- Profile Override → an approved extension point
- Output → any normative layer, read-only

Prohibited:

- **Reference → Semantic** (a primitive must not know its purpose)
- **Semantic → Component** (meaning must not depend on a component; violates the
  layer rule and creates component-specific foundations)
- **Component → Reference directly**, bypassing semantics — this is the most
  tempting shortcut and the most damaging, because it silently strips meaning
- **Output → Output** (transformation chains that obscure provenance)
- **Profile → core redefinition** (DEC-S-025)
- **Any cycle**, at any layer

## Product Profile relationship

A Product Profile enters the flow at **layer 4 only**. It may not reach into
layers 1–3 to redefine them.

Consumers already hold product-local token sets (CR-002, CR-037). Those are
**Consumer-local Artifacts** (authority class 7) — not profile overrides, and not
CDS. They enter CDS, if ever, only through reconciliation (DEC-S-026), never by
being read as an override.

## Channel-output relationship

Outputs (layer 5) are per channel or platform and may legitimately differ in
form. They must not differ in **meaning** (DEC-S-029, invariant 13).

There is no assumption that product UI, PDF, presentation, and diagram render
identically. There is a requirement that they mean the same thing.

## Validation requirements

The following must be **machine-checkable later**. The architecture requires the
capability; it selects no tool.

| Check | Must detect |
| --- | --- |
| Cycles | Any circular reference at any layer |
| Orphans | A token referenced but not defined |
| Unused | A token defined but never referenced |
| Layer violations | A component binding a reference token directly |
| Direction violations | Any upward dependency |
| Illegal overrides | A profile touching an unapproved point |
| Semantic bypass | Consumer-facing use of a reference token |
| Accessibility-affecting override | A profile override that could weaken an accessibility guarantee |
| Provenance | An output without source and transformation revision |

The last two matter most: they are the checks that stop invariant 10 and
DEC-S-031 from degrading into good intentions.

## Prohibited shortcuts

*(Normative)*

1. **Raw values in consumer projects.** Long-term a reconciliation or migration
   topic (DEC-S-026), never a supported pattern.
2. **Reference tokens as a public interface.** Values without meaning.
3. **Component tokens inventing meaning** absent from the semantic layer.
4. **Appearance-derived semantic names.**
5. **Editing an output** instead of its source (authority class 3).
6. **A profile override standing in for a missing semantic token** — that is a
   gap in the core, to be raised.
7. **A design tool as the token source of truth** (DEC-S-004, invariant 4).
8. **Colour as sole meaning carrier** at any layer (CR-006).

## Unresolved format and tooling questions

*(Deliberately open — DEC-S-032)*

1. What machine-readable format expresses the normative source? Undecided; the
   reviewed interoperability draft is explicitly not implementable today.
2. What naming convention encodes layer and role?
3. What tool performs transformation, and how is it made reproducible?
4. How are aliases represented?
5. How is theme selection expressed — and is a theme a profile concern, a
   semantic concern, or both?
6. What granularity do component tokens use?
7. Which validations run in which pipeline, and what blocks?
8. How are consumers' existing raw values mapped without a migration cliff
   (CR-002, RISK-022)?
9. What token layering does light/dark support imply (CR-025)?

Questions 1–3 and 7 are **CDS-WP-006 or later technology decisions**. Questions
4–6, 8, and 9 need design work after the architecture is approved.

**Open risk:** token layers, aliases, component tokens, profiles, and exceptions
can multiply faster than they can be governed (RISK-021). The architecture
constrains direction; it does not by itself constrain volume.

## Related documents

- [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md)
- [Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)
- [Product Profile and Extension Model](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md)
- [Artifact Distribution and Channel Model](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md)
