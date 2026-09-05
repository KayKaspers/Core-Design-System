# ADR-0005 — Visual Identifier Grammar and Identity Spaces

- **Status:** **`PROPOSED / AUTHORIZED FOR INTEGRATION` — NOT YET EFFECTIVE.**
  Prepared under an explicit Human-Maintainer authorization given on 2026-09-05.
  **This document is uncommitted executor output and confers no acceptance and no
  authority.** It becomes `Accepted` **only** upon the Human-Maintainer exact
  integration commit of the exact reviewed Working Tree object, following a Fresh
  Independent Review and Nova integration adjudication — the same acceptance rule
  ADR-0001 … ADR-0004 carry. **A review PASS is not a commit, and a Nova
  recommendation is not an approval.**
- **Date:** 2026-09-05
- **Project:** Core Design System (CDS)
- **Registered by:** CDS Step-9 Decision Integration Pass — **no work package is
  authorized**
- **Related:** [ADR-0001](ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) ·
  [ADR-0002](ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md) ·
  [ADR-0003](ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md) ·
  [ADR-0004](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md) ·
  **DEC-S-132**

## Scope

This ADR records the **architecture rationale** for **DEC-S-132 — Visual Identifier
Grammar and the Two Identity Spaces**, and for that decision only.

**DEC-S-133, DEC-S-134 and DEC-S-135 are deliberately outside this ADR and are not
architecture dependencies of it.** DEC-S-133 applies the existing ST-1 … ST-7
contract and changes nothing about what the machine-readable profile admits or what
a validator enforces; DEC-S-134 is a semantic and accessibility-obligation policy;
DEC-S-135 is a sequencing and authority rule. None of them turns on how an
identifier is shaped, and none of the consequences below is conditioned on them.
Recording that exclusion here is a boundary statement, not a deferral — the same
boundary ADR-0004 holds against DEC-S-129.

**This ADR grants no authority beyond DEC-S-132.** Where this ADR and DEC-S-132
could be read differently, the **Decision wins** and this ADR is corrected.

## Context

[CDS-WP-019](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md) defined the
structure of the Layer-3 visual foundation, and CDS-WP-020 defined the Reference
and Semantic layer contracts and returned **`DECISION_REQUIRED`**. The CDS-WP-020
Decision Integration Pass then answered **OD-1, OD-2 and OD-3** (DEC-S-128,
DEC-S-130, DEC-S-131, with ADR-0004) and deliberately left **OD-4 … OD-7** open.

Identifier **form** was already settled before this ADR and is not revisited here:
a restrictive, machine-validatable naming profile (**DEC-S-081**), technical
identifiers separate from display labels (**DEC-S-110**), a dot-free segment syntax
enforced by the committed token-document schema, a slash-separated `sourceSetId`
syntax enforced by both committed schemas, renames as governed migration events
(**DEC-S-082**), and the naming principles **N-1 … N-8** with their per-layer
applications **RN-1 … RN-9** and **SN-1 … SN-9**.

What was **not** settled was identifier **structure**: the shape of a visual token
path, the relationship between a token path and a source-set identity, and the
concrete root segments. DEC-S-131 clause 4 controlled the root vocabulary through
the registered VF-1 … VF-9 families and **invented, adopted, reserved and
recommended no concrete identifier**, recording that as a residual coupled to OD-4.

The gap was load-bearing rather than cosmetic. **VP-4** of the
[Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
requires that a value have *"somewhere to live that will not be renamed"*, and a
grammar without roots does not provide one — so no authoring work package could be
authorized while it stood open. The Visual Foundation Architecture gave the grammar
only as a **non-normative illustration**, stating that *"no identifier below is
adopted, reserved, recommended, or planned."*

## Decision drivers

- **Authority is granted, never acquired** (DEC-S-033). An identifier structure
  chosen by writing a token file would be a decision taken by implication.
- **Identity is expensive to change.** A `sourceSetId` change **invalidates admitted
  evidence** (DEC-S-131 clause 17), and any rename is a migration event
  (DEC-S-082). Identity therefore carries the longest half-life of any decision in
  the visual foundation and must be shaped once.
- **Do not duplicate machine-checkable state.** Information the committed schemas
  already carry as a validated field must not be re-encoded in an identifier, where
  it becomes a second, drift-prone copy.
- **One word, one meaning.** A term already bound to a construct must not be reused
  for a different construct in the same subject area.
- **Register less where nothing is evidenced.** VF-3, VF-5, VF-6 and VF-7 carry
  **no consumer demand evidence at all** (F-019-06, F-020-06); structure created
  for them is the most likely place for RISK-021 and RISK-026 to materialize.
- **A precedent that already works is evidence.** `semantic/status` is committed,
  Candidate, and carries admitted evidence; its identity shape has survived a
  promotion gate.

## Considered alternatives

### For the token-path root (chosen: family-rooted)

1. **Layer-rooted token paths**, with an explicit `reference` or `semantic` segment
   at the root. The token-flow layer would be visible in every identifier.
   **Rejected:** the layer is already an enumerated, schema-validated field —
   `reference | semantic | component | product-profile` — in **both** the committed
   token-document schema and the committed source-set manifest schema. Encoding it
   again in every identifier duplicates validated state, and a layer change would
   become a mass rename: a DEC-S-082 migration event that, for source sets,
   additionally invalidates admitted evidence under DEC-S-131 clause 17 — all for
   information the manifest already holds and a validator can already read.
2. **Family-rooted paths with no declared qualifier position.** Simplest possible
   grammar. **Rejected:** the first qualifier CDS needs would become a grammar
   change rather than an additive one — the same failure mode **ST-3** identifies
   for a scale that can only be extended by renumbering.
3. **Family-rooted paths with a declared, optional, unpopulated qualifier position
   (chosen).** It satisfies **N-6** literally — *the path encodes family, role, and
   modifier* — matches the committed `status.<axis>.<value>` precedent in shape, and
   makes the first qualifier an additive change. Declaring the position creates no
   qualifier and reserves no term.

### For the relationship between the two identity spaces (chosen: declared, associated)

1. **A mechanically derived `sourceSetId`**, computed from the token path or from
   the file location. Convenient, and it would guarantee agreement by construction.
   **Rejected, and it is the alternative with the sharpest defect:** **DEC-S-131
   clause 3 already states that a source set's identity is declared, not derived
   from a path, a file name, a directory, or a tool's convention**, and **clause 16
   states that a file move alone is not an identity change.** A derived identity
   would make a directory reorganisation an identity event and therefore an
   evidence-invalidating event — the exact coupling clause 16 exists to break.
2. **A single identity space**, with the token path serving as the source-set
   identity. **Rejected:** a source set is a container with its own revision,
   maturity, approval and dependency set; a token path names a value position inside
   one. Collapsing them would make every token path carry maturity semantics, which
   **RV-3** and **VF-I-14** exist to prevent.
3. **Two declared identity spaces, associated but not derivable (chosen).** The
   committed precedent already demonstrates the asymmetry: `sourceSetId`
   `semantic/status` with `layer` `semantic`, against a token document whose root
   group is `status`. The layer appears in the source-set identity and **not** in
   the token path, deliberately.

### For the source-set namespace (chosen: flat `<layer>/<family>`)

1. **A `visual` namespace prefix** — for example a three-segment
   `<layer>/visual/<family>` or `visual/<layer>/<family>` shape — segregating visual
   families from the non-visual `semantic/status`. **Rejected:** the
   `sourceSetId` syntax permits arbitrary depth, but the segment would carry no
   machine-checkable meaning, would have no counterpart in the committed schemas,
   and would make the one existing precedent an exception rather than an instance.
   Grouping is what the `layer` field and the family register already do.
2. **A flat `<layer>/<family>` namespace (chosen).** It is exactly the committed
   precedent, needs no schema change, and keeps every source-set identity two
   segments deep and directly readable against the family register.

### For compound-family root granularity (chosen: one root per family)

1. **Multiple roots per compound family**, splitting *Space and Size* into `space`
   and `size`, and *Surface and Elevation* into `surface`, `elevation`, `overlay`
   and `scrim`, because the display name is compound. **Rejected:** a display name
   is not an identity model. The family register defines **VF-3** and **VF-6** as
   **one family each**, with **one maturity, one evidence set, one gate and one
   compatibility statement** apiece; splitting the root would create identity
   surface that no registered family boundary supports, for two families that carry
   **no consumer demand evidence at all**. The `<primitive-group>` position already
   differentiates the constructs without multiplying roots.
2. **One root per registered family, with internal constructs differentiated by the
   primitive-group position (chosen).** It registers less, keeps root count equal to
   family count, and leaves the differentiation where a later, evidenced decision
   can make it additively.

## Decision

Recorded in full as **DEC-S-132**. In summary: visual token paths are
**family-rooted**; the reference grammar is
`<family>.<primitive-group>.<step>[.<qualifier>]` and the semantic grammar is
`<family>.<role>[.<qualifier>]`, with the qualifier position declared and
unpopulated; **the token-flow layer is never a token-path segment**; **token-path
identity and source-set identity are two separate spaces** and a `sourceSetId` is
**declared, never derived**; the source-set form is **`<layer>/<family>`**, flat;
the technical roots are **`color`, `typography`, `space`, `shape`, `surface`**; and
the ten source-set root identities **`reference/color` … `semantic/surface`** are
fixed as identifier authority **without instantiating anything**.

## Why the layer stays a field and not a segment

The committed schemas already validate `layer` as a closed enumeration, in both the
token document's CDS payload and every source-set manifest entry. A validator can
therefore answer *"which token-flow layer is this?"* today, offline, deterministically,
without parsing an identifier.

Duplicating that answer into every identifier would produce two carriers of one
fact. The repository has an explicit position on two carriers of one fact:
**DEC-S-034** states that a conflict between normative sources **invalidates the
affected artifact state**, and ADR-0004 rejected two canonical colour
representations on the ground that *"synchronization is not a mitigation; it is the
defect."* The same reasoning applies to identity: a path segment and a schema field
that must agree will eventually disagree, and the disagreement would surface as an
identity question — the most expensive kind.

The cost of the duplicate is also asymmetric. Correcting a `layer` field is an edit
to one member. Correcting a layer segment is a rename of every identifier in the
set, and for a source set a rename is an identity event that **invalidates admitted
evidence**. The cheap representation and the correct representation are the same
one.

## Why token-path identity is not source-set identity

They answer different questions and change on different occasions.

A **source-set identity** names an independently evaluable unit — the thing that
carries a revision, a maturity state, an approval state, a dependency set, and, when
one exists, admitted evidence. **Maturity binds to the pair
(`sourceSetId`, `sourceRevision`) and to nothing else** (DEC-S-131 clause 9).

A **token-path identity** names a value position inside such a unit. It carries no
revision, no maturity, and no approval — and **must not**, because **RV-3** holds
that metadata is not authority and **VF-I-14** holds that maturity is granted by a
gate, never by a document, a metadata field, a validator pass, or a renderer.

Deriving one from the other would couple them, and the coupling has a concrete
failure: under a derived identity, moving a file or reorganising a directory would
change a `sourceSetId`, and a `sourceSetId` change **invalidates admitted
evidence** (clause 17). **DEC-S-131 clause 16 already legislates the opposite** — a
file move alone is not an identity change. A derived identity would therefore
contradict a decision already in force, which is why the alternative was rejected
outright rather than weighed.

Association is sufficient for every real need. A manifest entry already binds a
`sourceSetId` to the path of the token document it inventories, so the link between
the two spaces is **declared data**, checkable offline, rather than an inference
from string shape.

## Why `qualifier` rather than `modifier`

CDS already uses **modifier** in a precise, load-bearing sense. The
[Visual Foundation Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md),
the [Machine-Readable Source Model](../architecture/MACHINE_READABLE_SOURCE_MODEL.md),
and the
[Token Reference, Resolution and Validation Model](../architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
all describe how source sets and **conditional modifiers** combine, in a defined
order, to resolve a context — the DTCG Resolver construct that is a leading
candidate for the theme mechanism **CDS-WP-022** will decide.

**N-6** and **T-8** simultaneously forbid a theme term from appearing inside a
shared semantic identifier. Using *modifier* for a path segment would therefore put
one word on both sides of a prohibition: the path slot that may never carry theme
meaning would share its name with the mechanism that carries theme meaning. That is
not a stylistic problem. It is the kind of ambiguity that makes a rule unteachable
and, eventually, unenforced — and **N-8** requires that every naming rule be
expressible as a check.

`qualifier` is a new term rather than an existing repository one; no existing term
filled the slot. **DEC-S-132 therefore renames the N-6 path slot explicitly and
reconciles N-6's wording**, so the principle is preserved and the collision is
removed without leaving two documents describing the same slot differently.

## Why one root per registered family

The family register is the authority DEC-S-131 clause 4 points at, and it registers
**VF-3 Space and Size** and **VF-6 Surface and Elevation** as **single families**.
Each has, by the normative artifact-family model, **its own maturity, its own
evidence, its own gate, and its own compatibility statement** — one of each, not
two or four.

A root per display-name component would have created identity structure that no
registered boundary supports, and it would have done so for families that carry
**no consumer demand evidence at all**. The conservative reading is the one that
registers less, and the `<primitive-group>` position absorbs the distinction at no
identity cost — while leaving a later, evidenced split available as an additive
change rather than foreclosed.

## Consequences

- The **Visual Foundation Architecture** naming model reconciles **N-6** to
  `qualifier` and carries the fixed roots; the **Visual Reference Token
  Foundation** and the **Visual Semantic Token Foundation** carry the two grammars
  and the root authority at their respective positions. All are normative
  human-readable statements; **none is implemented in a schema or a validator by
  this pass.**
- **OD-4 is answered and the OD-3 concrete-root residual is resolved.**
  **OD-5 is partially answered** (DEC-S-133, with per-family topology parameters
  and VF-1 tonal topology open), **OD-6A is policy-answered with the concrete
  vocabulary open** (DEC-S-134), **OD-6B is answered by existing normative
  authority**, and **OD-7 is answered** (DEC-S-135).
- **VP-4 is satisfied for VF-1, VF-2, VF-3, VF-5 and VF-6.** **VP-3, VP-5, VP-6 and
  VP-7 remain unsatisfied**, and VP-2 remains unsatisfied for font-family identity,
  font-weight identity and composites — so **no visual value may be selected** on
  the strength of this decision.
- **No visual value, identifier instance, source set, manifest, resolver, schema,
  validator rule, test or fixture is created.** Visual source sets remain **0**,
  visual Candidate families remain **0**, VF-1 … VF-9 remain **`Proposed`**, and
  every visual artifact remains **AE-0**.
- **CDS-WP-024** inherits three concrete, stated implementation obligations
  (below). None is implemented here.
- **No claim of any kind becomes possible.** An identity decision is not evidence,
  not a conformance statement, and not an accessibility claim.

## Compatibility

| Axis | Impact |
| --- | --- |
| **CDS profile version** | **None.** `profileVersion` stays `"1"`; no schema `const` changes. |
| **Committed schemas** | **None.** `schemas/` is untouched. The chosen grammar and the chosen `sourceSetId` shape already satisfy the committed `nameSegment` and `sourceSetId` patterns unchanged. |
| **Offline validator** | **None.** `tools/` and `tests/` are untouched; the naming obligations below are stated, not implemented. |
| **`semantic/status`** | **None.** Its `sourceSetId`, token path, revision, maturity, approval and evidence are unchanged. It is the precedent this ADR follows, not an artifact this ADR alters. |
| **Existing evidence** | **None, and none transfers.** `AE1-CDS-WP016-SEMSTATUS-004` stays bound to its own source revision and scope. |
| **Existing visual artifacts** | **None exist.** There is nothing to migrate, and no migration reference is owed. |
| **DEC-S-131** | **Unchanged.** Clauses 3, 4, 15, 16 and 17 are applied, not amended; the residual clause 4 recorded is resolved by DEC-S-132, which is the disposition clause 4 anticipated. |
| **Breaking change** | **No.** The grammar constrains a class of artifact that does not yet exist. |

## Future implementation obligations

*(Stated as **requirements on CDS-WP-024**. **Nothing below is implemented here**,
and recording an obligation authorizes no work.)*

| # | Obligation |
| --- | --- |
| 1 | **Root-vocabulary enforcement.** A normative visual token document whose root group is not a fixed family root, and a visual source set whose `sourceSetId` is not one of the ten fixed identities, must be detectable and must fail closed at CDS profile validation. |
| 2 | **Layer-segment prohibition.** A token path carrying a token-flow layer term as a segment must fail closed, distinctly from a path that merely uses an unknown segment. |
| 3 | **Identity-space separation.** A `sourceSetId` must be read from the declared payload and manifest and never inferred from a token path, a file name, or a directory; and a `sourceSetId` change must be detectable as an identity event that invalidates admitted evidence. |

**A pass proves structure, never correctness**, a pass at one layer proves nothing
about the next (VR-1), and **an automated check is never sufficient accessibility
evidence** (DEC-S-053).

## Authority boundary

This ADR **records** architecture rationale. It grants **no** authority beyond
DEC-S-132 — see *Status* above, and note that this ADR is **not yet effective**.

It **does not** change DEC-S-131, redefine the existing identifier profile, create a
source set, create a token identifier beyond the root authority DEC-S-132 explicitly
decides, or define any migration compatibility mechanism — **that mechanism remains
OPEN and undecided.**

It awards **no** maturity, **no** Candidate, **no** Stable, **no** evidence, **no**
admission, **no** claim, **no** conformance, **no** capability registration, **no**
Product Profile, **no** consumer activation, **no** pilot, **no** licence, **no**
release, **no** tag, and **no** publication authority. It activates **no** work
package: **`CDS-WP-020A` and CDS-WP-021 … CDS-WP-053 remain `Planned`, not active,
and not authorized**, and **CDS-WP-022 being the recommended and sequenced Step-10
candidate is not an authorization** — **SEQUENCED NEXT ≠ AUTHORIZED**. **No work
package is currently authorized.**

Publication remains **`Private Development`**. **Stable remains `No` across the
entire repository.**

## Related documents

- [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md)
- [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
- [Visual Foundation Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
- [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md)
- [Machine-Readable Source Model](../architecture/MACHINE_READABLE_SOURCE_MODEL.md)
- [Token Reference, Resolution and Validation Model](../architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
- [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
- [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
- [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
- [Decision Index](DECISION_INDEX.md)
