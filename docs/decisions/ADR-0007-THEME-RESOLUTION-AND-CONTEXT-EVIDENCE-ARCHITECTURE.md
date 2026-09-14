# ADR-0007 — Theme Resolution and Context-Evidence Architecture

- **Status:** **Accepted upon Human-Maintainer commit following Nova approval** —
  accepted at the exact-object integration commit
  `23914ecc48c1fb3cba5e3dab97a505589e821b6b` (2026-09-12) of the exact reviewed
  Working Tree object of CDS-WP-022, which followed independent review — a Fresh
  Independent Review returning `REWORK REQUIRED` with **0 blocking** findings, a
  bounded corrective rework resolving the material and authorized minor findings, and
  a confirmatory independent review — and Nova final integration adjudication, the
  same acceptance rule ADR-0001 … ADR-0006 carry. Before that commit this ADR was
  **`PROPOSED / HUMAN-MAINTAINER-APPROVED PROPOSITION, PENDING EXACT-OBJECT
  INTEGRATION`**, uncommitted executor output prepared under an explicit
  Human-Maintainer authorization, and conferred **no** acceptance and **no**
  authority; **no earlier wording, review verdict, or adjudication conferred it.**
  **A review PASS is not a commit, and a Nova recommendation is not an approval.**
  **`APPROVED PROPOSITION ≠ EFFECTIVE REPOSITORY DECISION`** held until that commit.
  **Effectivity is not closure: CDS-WP-022 remains `AUTHORIZED` / `ACTIVE FOR
  EXECUTION`, integrated, and not closed.**
- **Date:** 2026-09-12
- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-022 — Theme and Environmental Presentation Model
- **Effectivity commit:** `23914ecc48c1fb3cba5e3dab97a505589e821b6b`
- **Related:** [ADR-0001](ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) ·
  [ADR-0002](ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md) ·
  [ADR-0003](ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md) ·
  [ADR-0004](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md) ·
  [ADR-0005](ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md) ·
  [ADR-0006](ADR-0006-ADAPTIVE_SPATIAL_CONTEXT_AND_NAMED_RANGE_ARCHITECTURE.md) ·
  **DEC-S-137**

## Scope

This ADR records the **architecture rationale** for **DEC-S-137 — Theme Resolution
and Context-Evidence Architecture**, and for that decision only.

**DEC-S-138 is deliberately outside this ADR and is not an architecture dependency
of it.** DEC-S-138 records the **initial Core context set, the forced-colours
disposition, the environmental selection contract, and the default and fail-closed
policy** — a set of policy and vocabulary choices, not a representation
architecture. It is applicable external authority that this ADR neither covers,
modifies, nor supersedes, the same boundary ADR-0006 holds against DEC-S-135 and
ADR-0004 holds against DEC-S-129.

**DEC-S-131, DEC-S-132, DEC-S-135 and DEC-S-136 are preserved unchanged.** This ADR
**applies** them: DEC-S-131 supplies the evaluable unit this architecture refuses to
duplicate, DEC-S-132 supplies the identity spaces it refuses to extend, DEC-S-135
supplies the gate it satisfies without widening, and DEC-S-136 supplies the
spatial/theme separation it preserves. **None of them is amended here**, and none of
them could be amended here: each change would be an **Elevated** governance act
requiring its own Human-Maintainer decision.

**This ADR grants no authority beyond DEC-S-137.** Where this ADR and DEC-S-137
could be read differently, the **Decision wins** and this ADR is corrected.

## Context

CDS-WP-019 fixed **what a theme may and may not do** (T-1 … T-10) and deliberately
left the **mechanism** open. CDS-WP-020 and the Step-9 decisions then fixed the
surrounding machinery: the **Source Set** as the sole independently evaluable unit
(**DEC-S-131**), the **flat `<layer>/<family>` namespace** with ten closed root
identities and **no `context` or `theme` segment at any position**
(**DEC-S-132**), and the rule that **no semantic role carries a default alias before
CDS-WP-022 decides the theme mechanism** (**DEC-S-135**). CDS-WP-021 added
**`SPATIAL CONTEXT ≠ THEME RESOLUTION CONTEXT`** (**DEC-S-136**) and reserved any
composition of the two to CDS-WP-022.

CDS-WP-022 then derived everything effective authority uniquely determined — the
context admission contract, context identity, resolution entry, the
environmental-input boundary, the fail-closed conditions, and the composition
boundaries — and returned **`DECISION_REQUIRED`** on five normative choices it had
no authority to invent. **`WP022-D1`** was the first of them.

**The residual question was never "resolver or not".** The machine-readable
architecture already assigns multi-context composition *"(e.g. light/dark themes)"*
to the **DTCG Resolver Module 2025.10**, with the Resolver / Composition document
registered as **source-set class 6** and class-2 normative. Three of the four
readings CDS-WP-019 had listed were already closed or unavailable: a **Product
Profile** mechanism is excluded by the theme classification, a **per-context token
path** by T-8, N-6, SN-6 and TC-1, and a **per-context Source Set** by DEC-S-131
clause 5 together with DEC-S-132 clauses 10 and 12.

**The real question was where a context-conditional binding lives and which unit
carries its evidence.** **DEC-S-131 clause 1** attaches evaluation, evidence,
maturity and approval to a Source Set *"and nowhere else"*. If a context-conditional
binding lives only in a Resolver / Composition document, the artifact that actually
carries the context bindings is **not** the artifact evidence attaches to — and that
is an architectural consequence, not a detail. Each way out changed something
load-bearing: the evaluable unit, the source-set topology, the identity namespace, or
the representation of a binding.

That is the choice the Human Maintainer made, and this ADR records why.

## Decision drivers

| # | Driver |
| --- | --- |
| **1** | **Evidence must stay revision-bound and non-transferring.** DEC-S-126, DEC-S-131 clause 10, AF-2 and RV-4 all require that a new revision inherit nothing. A context mechanism that makes evidence ambiguous about *what was evaluated* breaks the one property CDS has actually earned. |
| **2** | **There must remain exactly one maturity unit.** DEC-S-131 clause 1 and the invariant **`AGGREGATED is not MATURE`** exist because a second maturity carrier is how maturity inflation enters a design system (RISK-031). |
| **3** | **Identity must not acquire a context dimension.** T-8, N-6, SN-6 and TC-1 keep a context out of every shared identifier; DEC-S-132 clause 12 keeps it out of the source-set namespace. A context in an identifier makes a role context-specific, which **T-2** forbids. |
| **4** | **Resolution must stay deterministic and offline.** T-6, T-7, DEC-S-030, DEC-S-080 and DEC-S-091 admit no external service and no ambient input. |
| **5** | **The mechanism must not presuppose a context count.** TC-6 requires the semantic layer to work whether CDS ships one context, two, or a third. |
| **6** | **Theme and Spatial Context must stay separate.** DEC-S-136 and CX-9 fix it; a mechanism that quietly makes a spatial range a resolver dimension would decide by implication what CDS-WP-021 explicitly refused to decide. |
| **7** | **Nothing may be implemented.** No schema, validator, resolver instance, source set, or value may be created by an architecture decision. |

## Considered alternatives

| # | Alternative | Disposition |
| --- | --- | --- |
| **A** | **Make the Resolver / Composition document a second independently evaluable maturity unit**, so context bindings live where evidence attaches. | **Rejected** |
| **B** | **Create one Source Set per Theme Resolution Context**, so each context is independently evaluable. | **Rejected** |
| **C** | **Encode the context as a token-path segment**, so a role resolves per context by path. | **Rejected** |
| **D** | **Encode the context as a Source-Set identity segment**, giving each context its own `sourceSetId` namespace position. | **Rejected** |
| **E** | **Resolver-Modifier Context over the existing Source-Set graph**, with context-specific evidence remaining bound to `(sourceSetId, sourceRevision)` and additionally recording the Resolver / Composition revision and the Theme Resolution Context as **exact evidence inputs**. | **Chosen** |

## Why the Resolver does not become a second maturity unit

Alternative **A** is the tempting one, because it appears to solve the evidence
question directly: put maturity where the bindings are.

It fails on **DEC-S-131 clause 1**. That clause does not merely say a Source Set
carries maturity — it says evaluation, evidence, maturity and approval attach there
**and nowhere else**, and clause 11 adds that **no maturity propagation exists in
either direction**. A second carrier immediately raises the question the clause
exists to foreclose: if a Source Set is `Candidate` and its resolver is not, what is
the composed artifact? Any answer is a propagation rule, and **DEC-S-131 clause 12**
already rejects roll-ups, maxima, minima and inheritance for the manifest — the
exactly analogous case.

It also collides with **DEC-S-079** and the resolver's own registered role: a
resolver *"introduces no new value or meaning"*. An artifact that introduces nothing
has nothing of its own to be mature **about**. Granting it maturity would make a
selection step look like a decision, which is the inversion
**`AGGREGATED is not MATURE`** was written to prevent.

And it would be an **amendment to DEC-S-131**, which is an Elevated change requiring
its own decision. The chosen architecture needs none.

**The evidence question is answered without a second carrier.** Maturity stays bound
to `(sourceSetId, sourceRevision)`; the Resolver / Composition revision and the
Theme Resolution Context are recorded as **exact evidence inputs** of the
context-specific evidence package. This is the same shape the accessibility evidence
model already uses: an evidence record binds exact OS, browser, renderer, assistive
technology, artifact, consumer, CDS, language, channel and date versions **without
any of them becoming a maturity carrier**. A context and a resolver revision are two
more exact inputs of that kind.

The consequence is stated rather than softened: a change to **any** evidence-relevant
Source Set revision, Resolver / Composition revision, or Theme Resolution Context
**invalidates or supersedes** the affected context-specific evidence, and **nothing
transfers automatically**. That is stricter than the alternative, not looser.

## Why there is no Source Set per context

Alternative **B** looks natural and is unavailable.

**DEC-S-131 clause 5** admits **one** source set per independently evaluable
**Family × Token-Flow-Layer** unit, and clause 6 spells the consequence out: a family
occupying layers 1 and 2 may have **two** source sets — one Reference, one Semantic —
and that is the whole permitted multiplicity. A per-context source set would put two
or more source sets on the *same* Family × Layer unit.

**DEC-S-132 clause 10** then closes the door from the identity side: the ten
identities `reference/color` … `semantic/surface` are fixed as identifier authority,
and clause 12 introduces **no `context` or `theme` namespace segment at any
position**. There is no spelling available for an eleventh, context-qualified
identity.

Taking **B** would therefore require amending **two** effective decisions at once.
It also multiplies the identity space by the context count, which is precisely the
volume growth **RISK-021** records: the architecture constrains direction, not
volume, and a per-context identity space is volume that governance would have to
absorb for every family, for every context, forever.

**And it would presuppose a count.** A topology whose shape depends on how many
contexts exist violates **TC-6** in substance — the same form-versus-substance
failure **DEC-S-135** exists to prevent.

## Why the context is not a token-path segment

Alternative **C** is excluded by authority already in force, and CDS-WP-022 added
nothing to that exclusion.

**T-8** states that a theme is a resolution input and that *"a theme name never
appears inside a shared semantic identifier"*; **N-6** and **SN-6** say the same from
the naming side; **TC-1** requires a role's identity to be context-independent.

The decisive argument is not naming hygiene but **T-2**: a theme *"may not add or
remove a role"*. A context-qualified path does not give one role two resolutions — it
gives **two different roles**, one per context, with independent existence. Every
downstream guarantee then weakens at once: a contrast obligation would have to be
declared per path rather than once per role (**CA-7**, TC-3), a consumer would bind
to a context-specific identifier and inherit the coupling the alias model exists to
prevent, and a context could add or remove a role by adding or removing a path.

## Why the context is not a Source-Set identity segment

Alternative **D** is **B**'s identity half taken alone, and it fails for the same
reason plus one more. **DEC-S-132 clause 6** fixes token-path identity and Source-Set
identity as **two separate identity spaces**, neither computable from the other; a
context segment in the second would make source-set identity carry a resolution
input, which is a category error in the same family as treating a theme as a layer.
**DEC-S-131 clause 17** then makes it expensive as well as wrong: a `sourceSetId`
change **invalidates admitted evidence**, so a context taxonomy embedded in identity
would convert every context revision into an identity migration.

## Why the chosen architecture is the conservative one

| # | Preserved property | How |
| --- | --- | --- |
| **1** | **DEC-S-131 unchanged** | One evaluable unit; no second maturity carrier; no new topology; clauses 1, 5, 10, 11, 12 and 17 all apply as written. |
| **2** | **DEC-S-132 unchanged** | No `context`/`theme` segment in any identifier; the flat namespace and the ten root identities stand; the two identity spaces stay separate. |
| **3** | **`AGGREGATED is not MATURE`** | A resolver still aggregates and still confers nothing. |
| **4** | **Revision-bound, non-transferring evidence** | Maturity binds to `(sourceSetId, sourceRevision)`; context and resolver revision are recorded **inputs**; any change invalidates or supersedes the affected evidence. |
| **5** | **Offline, deterministic resolution** | The mechanism is the resolver CDS already declared normative for multi-context composition — local, declared, revision-bound, with no network reference (DEC-S-078, DEC-S-091, T-6, T-7). |
| **6** | **`THEME ≠ SPATIAL CONTEXT`** | The two stay orthogonal; **no spatial context becomes a theme modifier, a theme selector, or a theme-resolution input**, and no theme classifies spatial geometry. DEC-S-136, CX-9, AC-1 … AC-6 and RR-1 … RR-6 are untouched. |
| **7** | **No context count presupposed** | The mechanism is indifferent to how many contexts exist; TC-6 and CA-13 hold. |
| **8** | **Five token-flow layers** | A Theme Resolution Context is a **resolver input**, never a sixth layer (DEC-S-024, TS-5, VF-I-1). |

**The chosen architecture is the only one of the five that amends nothing.** That is
the argument for it. It uses the construct the machine-readable architecture had
already assigned to this exact purpose, and it answers the evidence question by
making the context and the resolver revision **inputs to an evidence record** rather
than **carriers of maturity** — a distinction CDS already relies on everywhere else.

## Why joint Theme × Spatial evaluation is deferred rather than solved

Keeping the two dimensions orthogonal settles **representation**. It does not settle
**evaluation**: whether a future rendering or accessibility evidence package must
exercise the cross-product of Theme Resolution Contexts and spatial ranges is a
question about **evidence design**, and it cannot be answered without the rendering
evidence that does not exist (**CDS-WP-031**, `F-021-04`).

Deciding it here would either under-specify an evidence obligation or invent one.
**It is therefore deferred to separately authorized future scope**, recorded as a
deferral rather than left unstated — and the orthogonality that makes the deferral
safe is fixed by DEC-S-137 clauses 11 and 12.

## Why nothing is implemented

**`DEFINING A RESOLUTION CONTRACT ≠ AUTHORING A RESOLVER INSTANCE`.**

The committed CDS Resolver Document schema admits an optional `modifiers` array whose
items carry `order`, `name`, `$ref` and `pointer` under `additionalProperties: false`
— **there is no condition slot**, and the offline validator records **resolver
modifier semantics as not validated and not represented as passed**, the bounded
**DEC-S-098** V2 coverage boundary. That is a **declared coverage boundary, not a
class-1 / class-2 conflict**: no resolver instance with modifiers exists, so no
artifact state is affected and **DEC-S-034 is not triggered**.

The gap is recorded as **`F-022-01`** and **remains routed to `CDS-WP-020A` and
CDS-WP-024**, both `Planned`, not active, and not authorized. **This ADR and
DEC-S-137 change no schema, no validator, no test, and no fixture**, and reading the
coverage boundary as a profile admission is what **RISK-074** exists to prevent.
**AUTHOR is not VALIDATE**, and defining a contract is neither.

## Consequences

| # | Consequence |
| --- | --- |
| **C-1** | The [Visual Foundation Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md) records the mechanism and the context-evidence binding as **TM-1 … TM-12**; **T-1 … T-10, TS-1 … TS-6, TC-1 … TC-7, CA, CI, CS, CE, CF and CB are applied, not replaced.** |
| **C-2** | The [Token and Theme Architecture](../architecture/TOKEN_AND_THEME_ARCHITECTURE.md) question 5 and question 9 residuals are reconciled; **the five-layer flow is unchanged.** |
| **C-3** | **No schema, validator, test, or fixture changes**, and the CDS-WP-024 detection requirements stay requirements. |
| **C-4** | **`F-022-02` is resolved by Human-Maintainer decision**; **`F-022-01` remains routed.** |
| **C-5** | **DEC-S-135 is untouched.** From the effectivity of DEC-S-137 and DEC-S-138 its theme-mechanism sequencing condition is satisfied — and **`THEME GATE SATISFIED ≠ VALUE SELECTION AUTHORIZED`** and **`THEME GATE SATISFIED ≠ CDS-WP-020A AUTHORIZED`**. |
| **C-6** | **`WP021-D2` is unchanged and unrelated.** VF-4 acquires no technical root and no source-set identity, and **no relation exists between approving `WP022-D1` and resolving `WP021-D2`.** |

## Compatibility

This ADR introduces **no** breaking change, because there is nothing to break: no
theme, no context, no resolver instance, no visual source set, no visual value, and
no consumer artifact exists. **Visual source sets: 0. Visual values: 0.**
**VF-1 … VF-9 stay `Proposed`.** A future context-conditional resolver instance will
be a **new** artifact under this architecture, evaluated on its own revision-bound
evidence.

## Future implementation obligations

*(Requirements on later, separately authorized work packages. **None is implemented
here**, and recording one authorizes nothing.)*

| # | Obligation | Owner |
| --- | --- | --- |
| **1** | A resolver-document representation able to express a **context condition** — the **`F-022-01`** gap | **`CDS-WP-020A`** (authoring) and **CDS-WP-024** (validation) |
| **2** | Machine-readable **context identifiers**, authored under the CDS identifier profile; **none exists and none is authored here** | **`CDS-WP-020A`**, once separately authorized |
| **3** | Validation that a resolved output records its **Theme Resolution Context** and its resolver revision, and that an unsupported or missing context **fails closed** | **CDS-WP-024** |
| **4** | The **evidence-record shape** that carries a Theme Resolution Context and a Resolver / Composition revision as exact inputs | the accessibility evidence model, under separate authorization |
| **5** | Whether **joint Theme × Spatial rendering and evidence evaluation** is required | **separately authorized future scope**, informed by **CDS-WP-031** |

## Authority boundary

This ADR records a **rationale**, not an authorization, and **DEC-S-137 is the
authority**. It creates **no** theme, context, context identifier, default alias,
visual value, token identifier, semantic role, reference primitive, alias, Source
Set, `sourceSetId`, `sourceRevision`, manifest, resolver instance, schema, validator
rule, test, fixture, generated output, Product Profile, or extension point. It awards
**no** maturity, Candidate, Stable, evidence, admission, claim, conformance, pilot,
licence, release, tag, or publication authority, and **it activates no work
package** — **`CDS-WP-020A`, CDS-WP-023, CDS-WP-024 and every later identifier remain
`Planned`, not active, and not authorized.** It adds **no** risk entry: the register
stays at **98**, with **no `RISK-099`**. **VP-3, VP-5, VP-6 and VP-7 stay
`UNSATISFIED`**, and **VP-4 stays `UNSATISFIED` for VF-4**.

**Claude does not mark an ADR `Accepted`; that is a Human-Maintainer act.**

## Related documents

- [Visual Foundation Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
  — **VF-9**; T-1 … T-10, TS-1 … TS-6, **TM-1 … TM-12**, CA, CI, CS, CE, CF, CB
- [Token and Theme Architecture](../architecture/TOKEN_AND_THEME_ARCHITECTURE.md) —
  the five-layer flow, unchanged
- [Machine-Readable Source Model](../architecture/MACHINE_READABLE_SOURCE_MODEL.md) —
  source-set classes, the resolver role, **DEC-S-131**
- [Token Reference, Resolution and Validation Model](../architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
  — the DTCG resolver relationship, resolution order, fail-closed conditions
- [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
  — SR-1 … SR-12, **TC-1 … TC-7**, the alias model
- [Adaptive Layout and Responsive Foundation](../architecture/ADAPTIVE_LAYOUT_AND_RESPONSIVE_FOUNDATION.md)
  — CX-1 … CX-9, AC-1 … AC-6; **DEC-S-136**
- [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
  — AE-0 … AE-4, revision-bound evidence
- [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
  — VP-1 … VP-7
- [Decision Index](DECISION_INDEX.md) — **DEC-S-137**, and DEC-S-024, DEC-S-131,
  DEC-S-132, DEC-S-135, DEC-S-136, DEC-S-138
- [ADR-0006](ADR-0006-ADAPTIVE_SPATIAL_CONTEXT_AND_NAMED_RANGE_ARCHITECTURE.md) ·
  [ADR-0005](ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md) ·
  [ADR-0004](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md)
