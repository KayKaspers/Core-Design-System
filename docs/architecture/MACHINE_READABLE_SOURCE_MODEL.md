# Machine-Readable Source Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-011 — Machine-Readable Source and Token Format Decision
- **Date:** 2026-07-16
- **Status:** **Normative and in effect** for the machine-readable source
  architecture; ADR-0001 was committed with CDS-WP-011 (`a81772c`, 2026-07-17). It
  defines structure and authority; it implements nothing and creates no token.
- **Amended by:** CDS-WP-020 (Decision Integration Pass), 2026-08-27 — the
  *The source set is the independently evaluable unit* subsection, under
  **DEC-S-131**
  ([ADR-0004](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md)).
  **That subsection is effective** at the Human-Maintainer exact-byte integration
  commit `42a568d823de3388e45af62967546f13ad67eff6` (2026-08-27); the rest of this
  model is unchanged and remains in effect.

## Purpose and authority

This document defines the **normative machine-readable CDS source** — artifact
**class 2** in the
[Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)
(approved values), distinct from class-1 human-readable meaning and class-3
generated artifacts. It operationalizes the five-layer token flow
([Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md), DEC-S-024) as
concrete source-set classes and their dependency rules.

It is normative for **what a normative source set is, how source sets depend on one
another, and which artifacts are not normative**. Format detail lives in the
[CDS Token Format Profile](CDS_TOKEN_FORMAT_PROFILE.md); references/validation in the
[Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md);
identity in the
[Token Metadata, Provenance and Identity Model](TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md).

## Normative machine-readable source definition

A **normative machine-readable source** is a strict-JSON (`.tokens.json`) document,
conforming to the CDS Token Format Profile over DTCG 2025.10, that holds **approved
values, relationships, and governance metadata** — never meaning, which stays in
class-1 human-readable sources (DEC-S-022). It binds only through change control and
never contradicts a class-1 source; on conflict, **fail closed** (DEC-S-023,
DEC-S-034).

## Source-set classes

*(Normative — eight classes)*

| # | Source-set class | Token-flow layer | Normative? | Role |
| --- | --- | --- | --- | --- |
| 1 | **Reference Source Set** | 1 Reference | **Yes (class 2)** | Raw technical primitives; no consumer meaning |
| 2 | **Semantic Source Set** | 2 Semantic | **Yes (class 2)** | Role and meaning-binding values referencing Reference |
| 3 | **Component Source Set** | 3 Component | **Yes (class 2)** | Binds semantic decisions to component contracts |
| 4 | **Product Profile Source Set** | 4 Product Profile Overrides | **Yes (class 2), bounded** | Approved extension-point overrides only (DEC-S-025) |
| 5 | **Source-Set Manifest** | — | **Yes (class 2)** | Declares the set inventory, identity, layer, and dependencies |
| 6 | **Resolver / Composition Document** | — | **Yes (class 2)** | Composes sets/modifiers into a resolved context (DTCG Resolver) |
| 7 | **Generated Channel Output** | 5 Channel/Platform Outputs | **No (class 3)** | Derived, consumable form; carries provenance; never hand-edited |
| 8 | **Validation and Evidence Artifact** | — | **No (class 6)** | Records validation/evidence; never changes a source automatically |

Classes 1–6 are **class-2 normative**; class 7 is **class-3 generated**; class 8 is
**class-6 evidence**. Only classes that are class-2 bind, and only through change
control.

## Dependency model

*(Normative — strictly downward; DEC-S-024, DEC-S-079)*

```
Reference → Semantic → Component → Product Profile → Generated Channel Output
```

- A **Semantic** token may reference **Reference** tokens.
- A **Component** token may reference **Semantic** tokens.
- A **Product Profile** may override **only explicitly approved extension points**
  (DEC-S-025); it may not redefine shared semantics, weaken accessibility, distort
  status truth, or break contracts.
- **Generated outputs** may be traced back to normative source sets (read-only).
- **Prohibited:** any upward dependency, any component→reference bypass of
  semantics, any cycle at any layer, any output→output chain, any profile→core
  redefinition.
- **Validation/evidence artifacts** never modify a source set automatically — a
  contradiction triggers a controlled decision (Source of Truth, invariant 6).

The Resolver/Composition document composes sets and modifiers **without** inverting
this direction; it selects and layers approved values, it does not create meaning.

## Relationship to human-readable normative sources

Class-1 human-readable sources define **meaning, governance, and usage
constraints**; class-2 machine-readable sources define **approved values and
relationships**. Neither wins automatically; a meaning-vs-values conflict
**invalidates the affected artifact state** and is escalated (DEC-S-034, RISK-020).
A machine-readable source that tries to carry meaning, or a human-readable source
that tries to carry authoritative values, is the defect that creates RISK-020.

## Relationship to generated artifacts

Generated Channel Outputs are **class-3 generated artifacts** (DEC-S-022): never
independently normative, never hand-edited (a manual edit is reconciled back into
the source), always carrying source and transformation revision (DEC-S-031). A
generated output never stands against its source.

## Source-Set Manifest requirements

Every normative source set is declared in a **Source-Set Manifest** carrying, at
minimum: source-set ID, layer, CDS profile version, DTCG report version, source
revision, dependency set, maturity state, approval state, owner role, and (where
applicable) product profile and channel scope. Detail:
[Token Metadata, Provenance and Identity Model](TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md).

### The source set is the independently evaluable unit

*(Normative — **DEC-S-131**,
[ADR-0004](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md),
CDS-WP-020 Decision Integration Pass, 2026-08-27. **Effective** at the
Human-Maintainer exact-byte integration commit
`42a568d823de3388e45af62967546f13ad67eff6`. **No source set, manifest, resolver, or
identifier is created.**)*

| # | Rule |
| --- | --- |
| 1 | **The Source Set is the canonical independently evaluable unit.** Evaluation, evidence, maturity, and approval attach there and nowhere else. |
| 2 | **Each source set independently carries** its `sourceSetId`, `sourceRevision`, `layer`, dependency set where applicable, `maturityState`, and `approvalState`. Identity is declared, never derived from a path, file name, directory, or tool convention. |
| 3 | **One manifest may aggregate multiple source sets.** **A source set is not a manifest**, and one source set must never be equated with one manifest. |
| 4 | **Maturity binds to the pair (`sourceSetId`, `sourceRevision`)**, and to nothing else. A new revision inherits **no** evidence and **no** admission (DEC-S-126). |
| 5 | **No maturity propagation exists in either direction** — between source sets, between token-flow layers, between families, from a manifest to its entries, from entries to their manifest, to or from generated artifacts, out of metadata, or out of a validator result. |
| 6 | **Manifest-level maturity and approval describe only the manifest artifact itself.** They are **not** a roll-up, **not** a maximum, **not** a minimum, and **not** inherited. |
| 7 | **A source-set rename is a migration and identity event** (DEC-S-082, DEC-S-040). **A file move alone is not a `sourceSetId` change** — location is not identity. **A `sourceSetId` change invalidates admitted evidence.** |

> **AGGREGATED is not MATURE.** Declaring an inventory is a structural act. It
> confers nothing on what is inventoried, and nothing on the inventory — the same
> rule that makes a `Candidate` declaration in metadata not Candidate (VR-4), a
> validator pass not maturity authority (DEC-S-053), and a digest not a signature
> (DEC-S-090).

## Resolver and composition role

The Resolver/Composition document (DTCG Resolver Module 2025.10) declares how sets
and conditional modifiers combine, in a **defined order**, to resolve a context
(e.g. theme). It is normative for **which approved values apply in which context**;
it introduces no new value or meaning and honors the downward dependency direction.

## Product Profile boundary

A Product Profile Source Set enters at **layer 4 only** and may override **only
named, approved extension points** (DEC-S-025, DEC-S-043). Consumer-local token sets
(CR-002, CR-037) are **class-7 consumer-local artifacts**, not profile overrides, and
enter CDS only through reconciliation (DEC-S-026) — never by being read as an
override.

## Channel Output boundary

Channel/Platform outputs are generated per channel and may differ in **form** but
never in **meaning** (DEC-S-029). They are not normative and are never authored
directly.

## Offline and deterministic requirements

Normative sources and their transformation must be **locally processable and
validatable** with no mandatory external runtime or registry (DEC-S-006, DEC-S-030),
and **deterministic**: same source revision + same transformation revision = same
logical output (DEC-S-031, DEC-S-080). `latest` is not an identity.

## Change control

This model is normative and versioned. Changes to source-set classes, the dependency
model, or the manifest requirements are **Elevated** and require Nova review and
Human-Maintainer approval (DEC-S-082). On conflict with the
[Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md) or the
[Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md), those prior
normative sources win and this model is corrected.

## Implementation deferrals

Not decided here (deferred to CDS-WP-012 or later): the concrete file/repository
topology, the profile JSON Schema, the manifest schema, the transformation tool,
the deterministic-serialization mechanism, and any real token value or name.

## Related documents

- [CDS Token Format Profile](CDS_TOKEN_FORMAT_PROFILE.md)
- [Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
- [Token Metadata, Provenance and Identity Model](TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md)
- [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md) ·
  [Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)
- [ADR-0001](../decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) ·
  [ADR-0004](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md)
