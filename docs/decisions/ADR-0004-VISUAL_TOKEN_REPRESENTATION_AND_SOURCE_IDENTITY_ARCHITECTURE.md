# ADR-0004 — Visual Token Representation and Source Identity Architecture

- **Status:** **Accepted upon Human-Maintainer commit following Nova approval** —
  accepted at the exact-byte integration commit
  `42a568d823de3388e45af62967546f13ad67eff6` (2026-08-27), which followed a Fresh
  Independent Review and Nova integration adjudication. Before that commit this ADR
  was uncommitted executor output prepared under an explicit Human-Maintainer
  authorization and conferred **no** acceptance; no earlier wording conferred it.
- **Date:** 2026-08-27
- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-020 — Reference and Semantic Token Foundation
  (Decision Integration Pass)
- **Related:** [ADR-0001](ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) ·
  [ADR-0002](ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md) ·
  [ADR-0003](ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md) ·
  **DEC-S-128**, **DEC-S-130**, **DEC-S-131**

## Scope

This ADR records the **architecture rationale** for the three profile-facing
decisions of the CDS-WP-020 Decision Integration Pass:

| Decision | Question it answers |
| --- | --- |
| **DEC-S-128** | In which representation a normative CDS visual colour value is authored, and what a derivation or a transformation may do to it |
| **DEC-S-130** | Which token `$type` values the CDS profile admits, and how an unadmitted type is treated |
| **DEC-S-131** | What the independently evaluable unit of a visual machine-readable source is, and where maturity binds |

**DEC-S-129 — Visual Contrast Evaluation Authority — is deliberately outside this
ADR and is not an architecture dependency of it.** Contrast evaluation authority is
an accessibility-methodology decision, not a representation or source-identity
decision; none of the three decisions above depends on it, and none of the
consequences below is conditioned on it. Recording that exclusion here is a
boundary statement, not a deferral of DEC-S-129.

**This ADR grants no authority beyond the three Decisions it records.** Where this
ADR and a Decision could be read differently, the **Decision wins** and this ADR is
corrected.

## Context

[CDS-WP-019](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md) defined the
structure of the Layer-3 visual foundation and selected no value. CDS-WP-020
defined the contract for token-flow layers **1 Reference** and **2 Semantic** — the
[Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md),
the [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md),
and the [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
— and returned **`DECISION_REQUIRED`**: the value half of the work package was
gated on seven normative choices that no committed CDS source had made, recorded
**non-normatively** as **OD-1 … OD-7** in the
[Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
register.

The finding that made this ADR necessary was stated plainly there: **the machinery
is sufficient; the decisions are not.** The CDS Token Format Profile, the
source-set classes, the fail-closed reference semantics, the committed JSON Schema
2020-12 contracts, the offline validator, and the RFC 8785 + SHA-256 serialization
contract all accept a visual source set unchanged. What blocked one was that
authoring it would have settled OD-1 … OD-5 **by implication** — acquiring
authority by writing a file, which DEC-S-033 prohibits outright.

Three of those seven choices are profile-facing in the same sense that ADR-0001
(source format), ADR-0002 (serialization) and ADR-0003 (validator stack) were: each
changes what the machine-readable profile admits and what a validator must
enforce. They are recorded here.

## Decision drivers

- **Authority is granted, never acquired** (DEC-S-033). A representation chosen by
  writing a file is not a decision.
- **Accessibility obligations must be evaluable from the normative source**, with
  no conversion step inside the normative path (VF-I-8, CR-2, CR-3).
- **Offline and deterministic processing** with no external service or registry
  (DEC-S-030, DEC-S-080).
- **The registered channel model is not screen-only.** Paginated, printed,
  greyscale, projected and exported channels are registered, and four of nine
  channels have **no accessibility profile at all** (RISK-046).
- **Admitted must not exceed validated.** The gap between what a profile admits and
  what CDS has modelled and can check is exactly **RISK-074**.
- **Maturity is never inherited** (AF-1) and **a family may mature at its own pace**
  (AF-3). A representation that cannot express both is the wrong representation.
- **Fewer moving parts in the normative path.** Every conversion, derivation, or
  aggregation step is a place where an obligation can be silently lost.

## Considered alternatives

### For the authored colour representation (DEC-S-128)

1. **A perceptually uniform space as the normative authored space.** Tonal scales
   become principled and lightness reasoning is direct. **Rejected:** contrast
   evaluation and most channel output would require conversion, gamut mapping would
   have to be specified for out-of-gamut results, and the conversion would enter the
   normative determinism surface (DEC-S-080). A conversion inside the normative path
   is a place an accessibility obligation can be lost without anyone detecting it.
2. **A wide-gamut display space as the normative authored space.** Wider on-screen
   range. **Rejected:** the weakest print, greyscale and export story of the
   alternatives, against a registered channel model that includes paginated,
   printed, projected and exported channels; gamut mapping would become mandatory
   rather than exceptional.
3. **Two canonical representations, kept in sync.** **Rejected outright:** two
   normative representations of one value is two sources of truth, and DEC-S-034
   already states that a conflict between normative sources invalidates the affected
   artifact state. Synchronization is not a mitigation; it is the defect.
4. **DTCG `srgb` as the single canonical normative representation, with perceptual
   spaces admitted as derivation and analysis only (chosen).** The contrast
   obligation of a role pairing is computable from the source with no conversion in
   the normative path; every registered channel can consume it without gamut mapping
   in the source; perceptual evenness stays achievable by **computing** steps
   perceptually and recording the canonical result.

### For the admitted type set (DEC-S-130)

1. **Admit everything the pinned report defines.** Maximum expressiveness
   immediately. **Rejected:** CDS would admit composite types it has neither
   modelled nor validated — precisely the shape RISK-074 describes.
2. **Admit per family on demand, with no standing set.** Maximum precision.
   **Rejected:** maximum governance load against a single-maintainer bottleneck
   (RISK-029, RISK-040), and no stable statement a consumer or a validator could
   read.
3. **A minimal scalar set now, extended additively on demonstrated need (chosen).**
   Every admitted type is one CDS has modelled, can name obligations for, and can
   check. A later family needing another type triggers an **additive, governed,
   detectable** profile change.

### For the source-set unit (DEC-S-131)

1. **Two sets — one Reference, one Semantic, spanning all visual families.** Fewest
   artifacts. **Rejected:** it contradicts AF-1 and AF-3 — five families would share
   one maturity, so the slowest would hold the rest back or, worse, be carried by
   them.
2. **Per family for Semantic; one shared Reference set.** Maturity independence
   where obligations live. **Rejected as the general rule:** the shared Reference
   set's maturity becomes an undeclared floor under every family.
3. **One source set per independently evaluable Family × Token-Flow-Layer unit
   (chosen).** It preserves AF-1 and AF-3 by construction, and — once the manifest
   and the source set are correctly distinguished — its cost is far smaller than the
   artifact-count reasoning that first recorded it assumed. See *Why source sets,
   not manifests, carry maturity* below.

## Decision

**1 — Colour representation.** Exactly **one** canonical normative CDS visual
colour representation: the DTCG 2025.10 Color Module colour space keyed **`srgb`**,
with components expressed in that report's numeric representation and range.
**OKLCH is admitted as a preferred derivation and design-analysis space only** — it
is not a normative source space, not a second canonical representation, not
authority for a value, and not an evidence carrier. The result of a perceptual
derivation is recorded as the canonical value, with the derivation recorded as
provenance where required. Delivery quantization belongs to the channel and
generated-output boundary and never rewrites a canonical source value. A normative
source value outside the admitted canonical model **fails closed**. Full text:
**DEC-S-128**.

**2 — Admitted token types.** The CDS profile carries an **explicit admission
profile**. The initial admitted visual token type set is **`color`**,
**`dimension`** and **`number`** — verified directly against the pinned final DTCG
2025.10 reports. **DTCG-defined is not CDS-admitted.** No composite type is
admitted, every normative CDS visual token carries its **own explicit `$type`**,
and `$type` carries **value-type semantics only** — it implies no maturity,
evidence, approval, lifecycle, authority, publication, or conformance. Full text:
**DEC-S-130**.

**3 — Source-set identity and maturity granularity.** The **Source Set** is the
canonical independently evaluable unit. Each carries its own `sourceSetId`,
`sourceRevision`, `layer`, dependencies where applicable, `maturityState` and
`approvalState`. The topology is **one source set per independently evaluable
Family × Token-Flow-Layer unit**. **One manifest may aggregate several source
sets**, and a manifest's own maturity and approval describe **only the manifest
artifact itself** — never a roll-up, maximum, minimum, or inheritance.
**AGGREGATED is not MATURE.** Full text: **DEC-S-131**.

**None of the three creates a value, an identifier, a source set, a manifest, a
resolver, a schema, a validator rule, a test, or a fixture.**

## Why `srgb` is canonical

WCAG's contrast obligation is defined over relative luminance computed from sRGB
components. Authoring the normative source in that representation makes a role
pairing's declared contrast obligation computable **directly from the source**,
offline and deterministically, with **no conversion step inside the normative
path**.

That is not a convenience argument. Every conversion in the normative path is a
place where an accessibility obligation can change without any artifact recording
that it did — and the visual foundation carries **all five WCAG 2.2 criteria CDS
owns without the consumer** (1.3.3, 1.4.1, 1.4.5, 2.3.1, 2.4.7). An obligation that
can only be checked after a transformation is an obligation that a transformation
can quietly break.

The second reason is channel honesty. The registered channel model includes
paginated, printed, greyscale, projected and exported channels, and **four of nine
channels have no accessibility profile at all**. A representation whose story is
strongest on screen and weakest in print would be strongest exactly where CDS has
the least registered obligation and weakest where it has the most.

## Why OKLCH is derivational

The argument for a perceptually uniform space is real: an even tonal scale is
easier to reason about and easier to defend than one built in a gamma-encoded
space. **That argument is about how a value is arrived at, not about what the
normative value is**, and DEC-S-128 grants exactly that and no more.

Making OKLCH normative — or canonical alongside `srgb` — would buy scale evenness
at three costs the architecture does not accept:

- **Two sources of truth.** DEC-S-034 does not resolve a conflict between normative
  sources by recency or convenience; it **invalidates the affected artifact state**.
  A second canonical representation manufactures that conflict as a standing
  condition.
- **A conversion inside the normative path**, with gamut mapping for out-of-gamut
  results, both of which would join the determinism surface (DEC-S-080) and both of
  which sit between the source and the obligation.
- **An evidence carrier that is not evidence.** A derivation is a calculation. It
  demonstrates nothing about perceivability, and treating it as though it did is the
  shape in which unfounded accessibility confidence enters a design system
  (DEC-S-053, EV-4).

The derivation is therefore preserved as **provenance** — recorded, reviewable, and
non-authoritative — which is the same disposition every other class-3 derived form
already has (DEC-S-031, DEC-S-079).

## Why the admitted type set is closed and minimal

A composite type bundles several decisions into one token: a shadow bundles colour
with offsets and blur; a typography token bundles family, weight, size and line
height. **That bundling is exactly where the semantic layer loses the ability to
declare a per-part obligation** under SR-3 (contrast sensitivity), SR-4 (pairings)
and SR-5 (non-visual carrier). Admitting composites before the roles that would use
them exist would decide the granularity question by implication — the same failure
mode this whole pass exists to avoid.

Minimal is also the only setting in which **admitted does not exceed validated**.
Two repository facts make that concrete, and both are easy to misread:

- The **committed token-document schema constrains `$type` not at all.** A visual
  token document carrying any string would pass it.
- The **offline validator's bounded token-`$type` set is a DEC-S-098 V2 coverage
  boundary, not a CDS profile admission.** Reading it as one is **RISK-074**, and it
  is the specific misreading this decision closes. **A tool accepting a type is not
  the profile admitting it.**

The admission profile therefore has to be stated explicitly, in a normative
human-readable source, because neither the schema nor the validator states it and
neither can be read as though it did.

## Why `profileVersion` stays `"1"`

The CDS profile version is `"1"`, and it is pinned as a JSON Schema `const` in
every committed CDS schema and in every committed source artifact. **DEC-S-130 does
not change it, and this pass changes no schema, no validator, no test and no
fixture.**

The reasoning is that this pass adds an **explicit statement of what was already
required but never enumerated**. The CDS Token Format Profile already required an
explicit `$type` on every token, drawn from the DTCG-defined types applicable to
CDS scope; it enumerated no set. Naming the set is **additive and restrictive at
once** — it admits fewer types than the unenumerated wording could be read to
permit, and it constrains no existing artifact, because **no visual token exists**
and the one existing normative token source (`semantic/status`) is non-visual and
untouched.

A `profileVersion` bump is a compatibility and migration event under DEC-S-082. It
belongs to the work package that **implements** the enforcement — CDS-WP-024 — if
that implementation turns out to require one, and to a decision taken then rather
than pre-empted now. Bumping it here would announce a compatibility break that this
pass does not make.

## Why source sets, not manifests, carry maturity

**AF-1** forbids inherited maturity; **AF-3** grants each family its own pace. A
source-set payload carries **one** `maturityState` and **one** `approvalState`, so
a single shared visual source set spanning five families cannot express five
independent maturities. That much of the original CDS-WP-020 finding **`F-020-02`**
is correct and stands.

What the finding stated imprecisely was the **artifact-count mechanism**. It
implied that per-family, per-layer source sets would multiply manifests and
resolvers at the same rate. The committed manifest schema shows otherwise: a
Source-Set Manifest carries a **`sourceSets` array**, and every entry independently
carries `sourceSetId`, `path`, `layer`, `dependencies`, `sourceRevision`,
`maturityState` and `approvalState`. **One manifest may therefore aggregate many
source sets, each with its own maturity, without collapsing any of them.**

The correction matters because it changes what the governance cost actually is. The
cost of preserving AF-1 and AF-3 is **not** a manifest per family; it is a source
set per independently evaluable unit, which the existing declared-inventory model
already supports. A topology that cannot express AF-1 and AF-3 is the wrong
topology, and the reason to avoid one is not that it is expensive — it is that it
is wrong.

## Why aggregation confers no maturity

A manifest declares an inventory. Declaring one is a **structural** act, and
DEC-S-131 states the consequence as an invariant: **AGGREGATED is not MATURE.**

A manifest's own `maturityState` and `approvalState` describe the **manifest
artifact**, and nothing else. They are not a roll-up, not a maximum, not a minimum,
and not inherited in either direction — neither from entries to manifest nor from
manifest to entries. Maturity does not propagate between source sets, between
layers, between families, to or from generated artifacts, out of metadata, or out
of a validator result.

This is the same rule CDS already holds in three other places, and it is stated
again because aggregation is where it is most likely to be lost quietly:

- **Metadata is not authority.** A source set declaring `Candidate` is not Candidate
  (VR-4, RV-3, DEC-S-126).
- **A validator pass is metadata coherence, never maturity authority** (VR-4,
  DEC-S-053).
- **Only a gate grants maturity**, and the exact-byte Promotion Commit is the point
  at which a transition actually occurs (DEC-S-126).

Maturity binds to the pair **(`sourceSetId`, `sourceRevision`)**. A new revision
inherits **no** admitted evidence; a `sourceSetId` change invalidates admitted
evidence and is a migration and identity event; a file move alone is neither.

## Consequences

- The **CDS Token Format Profile** now states a canonical colour representation and
  an explicit admitted `$type` set. Both are normative human-readable statements;
  neither is implemented in a schema or a validator by this pass.
- **OD-1, OD-2 and OD-3** of the open-decision register are answered. **OD-4
  (identifier grammar), OD-5 (scale topology), OD-6 (role vocabulary and family
  granularity) and OD-7 (sequencing against CDS-WP-022) remain open**, and three
  residual items are recorded there rather than deferred silently: the CDS-specific
  disposition of the optional DTCG `hex` member, the representation of font-family
  and font-weight identity, and the concrete visual source-set root identifiers.
- **VP-2** of the value-selection prerequisites is satisfied for the families
  expressible in `color`, `dimension` and `number`. **VP-3, VP-4 and VP-5 remain
  unsatisfied for every family**, so **no visual value may be selected** on the
  strength of these decisions.
- **No visual value, identifier, source set, manifest, resolver, schema, validator
  rule, test or fixture is created.** Visual source sets remain **0**, visual
  Candidate families remain **0**, VF-1 … VF-9 remain **`Proposed`**, and every
  visual artifact remains **AE-0**.
- **CDS-WP-024** inherits four concrete, stated implementation obligations (below).
  None is implemented here.
- **No claim of any kind becomes possible.** A representation decision is not
  evidence, not a conformance statement, and not an accessibility claim.

## Compatibility

| Axis | Impact |
| --- | --- |
| **CDS profile version** | **None.** `profileVersion` stays `"1"`; no schema `const` changes. |
| **Committed schemas** | **None.** `schemas/` is untouched; a visual token document already passes the structural contract unchanged. |
| **Offline validator** | **None.** `tools/` and `tests/` are untouched; the DEC-S-098 V2 coverage boundary is unchanged and is explicitly **not** the admission profile. |
| **`semantic/status`** | **None.** No source byte, revision, maturity, approval, or evidence changes. It is a non-visual family and holds no `color`, `dimension`, or `number` token. |
| **Existing evidence** | **None, and none transfers.** `AE1-CDS-WP016-SEMSTATUS-004` stays bound to its own source revision and scope. |
| **Existing visual artifacts** | **None exist.** There is nothing to migrate, and no migration reference is owed. |
| **Breaking change** | **No.** The admitted set constrains a class of artifact that does not yet exist. |

## Future implementation obligations

*(Stated as **requirements on CDS-WP-024**. **Nothing below is implemented here**,
and recording an obligation authorizes no work.)*

| # | Obligation |
| --- | --- |
| 1 | **Explicit-own-`$type` enforcement.** A normative CDS visual token that relies on inherited or group-level typing rather than declaring its own `$type` must be detectable and must fail closed at CDS profile validation. |
| 2 | **Admitted-set validation.** A token whose `$type` is DTCG-known but **CDS-unadmitted** must fail closed at CDS profile validation, distinctly from a type the pinned report does not define at all, which fails closed at the applicable lower layer. |
| 3 | **Canonical colour-representation enforcement.** A normative colour source value outside the admitted canonical model must fail closed, and a delivery-quantized or converted form must never be readable as a normative source value. |
| 4 | **Source-set identity and maturity checks.** Per-source-set identity, revision binding, and the prohibition on treating a manifest's maturity as a roll-up must be checkable, and a `sourceSetId` change must be detectable as an identity event. |

**A pass proves structure, never correctness**, a pass at one layer proves nothing
about the next (VR-1), and **an automated check is never sufficient accessibility
evidence** (DEC-S-053).

## Authority boundary

This ADR **records** architecture rationale. It grants **no** authority beyond
DEC-S-128, DEC-S-130 and DEC-S-131 — see *Status* above.

It awards **no** maturity, **no** Candidate, **no** Stable, **no** evidence, **no**
admission, **no** claim, **no** conformance, **no** capability registration, **no**
Product Profile, **no** consumer activation, **no** pilot, **no** licence, **no**
release, **no** tag, and **no** publication authority. It activates **no** work
package: **CDS-WP-021 … CDS-WP-053 remain `Planned`, not active, and not
authorized**, and **this ADR did not close CDS-WP-020** — closure is a separate
Human-Maintainer act, effective at the Human-Maintainer commit
`3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`.

Publication remains **`Private Development`**. **Stable remains `No` across the
entire repository.**

## Related documents

- [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md)
- [Machine-Readable Source Model](../architecture/MACHINE_READABLE_SOURCE_MODEL.md)
- [Machine-Readable Validation Contract](../architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)
- [Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md)
- [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
- [Visual Foundation Colour Architecture](../architecture/VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
- [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
- [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
- [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
- [Decision Index](DECISION_INDEX.md)
