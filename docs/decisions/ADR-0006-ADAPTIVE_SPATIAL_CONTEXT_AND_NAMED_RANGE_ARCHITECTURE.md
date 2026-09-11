# ADR-0006 — Adaptive Spatial Context and Named-Range Architecture

- **Status:** **Accepted upon Human-Maintainer commit following Nova approval** —
  accepted at the exact integration commit
  `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9` (2026-09-11) of the exact reviewed
  Working Tree object, which followed independent review — a Fresh Independent
  Review returning `REWORK REQUIRED` (**F-R21-01** material, **F-R21-02** minor),
  a bounded two-file rework resolving both, and a confirmatory independent review
  returning `PASS` — and Nova integration adjudication — the same acceptance rule
  ADR-0001 … ADR-0005 carry. Before that commit this ADR was
  `PROPOSED / AUTHORIZED FOR INTEGRATION`, uncommitted executor output prepared
  under an explicit Human-Maintainer authorization given on 2026-09-06, and
  conferred **no** acceptance and **no** authority; no earlier wording, review
  verdict, or adjudication conferred it. **A review PASS is not a commit, and a
  Nova recommendation is not an approval.**
- **Date:** 2026-09-06
- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-021 — Adaptive Layout and Responsive Foundation
- **Related:** [ADR-0001](ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) ·
  [ADR-0002](ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md) ·
  [ADR-0003](ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md) ·
  [ADR-0004](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md) ·
  [ADR-0005](ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md) ·
  **DEC-S-136**

## Scope

This ADR records the **architecture rationale** for **DEC-S-136 — Adaptive Spatial
Context and Named-Range Architecture**, and for that decision only.

**DEC-S-132, DEC-S-133 and DEC-S-135 are deliberately outside this ADR and are not
architecture dependencies of it.** DEC-S-132 fixes identifier grammar and root
identity — and **fixes none for VF-4**, which this ADR does not change; DEC-S-133
governs per-scale topology and **explicitly excludes VF-4**; DEC-S-135 is a
sequencing and authority rule about the theme mechanism, which this ADR does not
touch. DEC-S-132 and DEC-S-133 do not supply the rationale for this ADR;
DEC-S-135 remains applicable external authority that this ADR applies without
covering, modifying, or superseding it, including in D-8, the
spatial/theme-separation rationale, and consequence C-5.

**`WP021-D2` is outside this ADR.** Whether **VF-4** acquires a technical token root
and a source-set identity is **deferred by the Human Maintainer** and is decided
neither here nor by DEC-S-136. Recording that exclusion is a boundary statement,
not a deferral this ADR performs — the same boundary ADR-0005 holds against
DEC-S-133 … DEC-S-135 and ADR-0004 holds against DEC-S-129.

**This ADR grants no authority beyond DEC-S-136.** Where this ADR and DEC-S-136
could be read differently, the **Decision wins** and this ADR is corrected.

## Context

[CDS-WP-019](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md) registered **VF-4
Layout and Grid** as a visual foundation family and left its content open.
The [Spatial Architecture](../architecture/VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md)
then fixed six constraints on responsive ranges — **RR-1 … RR-6** — and deliberately
left the **mechanism** open in **RR-5**, assigning it to CDS-WP-021 by name.

CDS-WP-021 executed and returned **`DECISION_REQUIRED`**. It established the
derivable Layer-3 contract — the layer ownership model, the spatial-context model,
the range obligations, the grid, container and content-width contracts, and the
density and adaptation interaction — and reported that **existing authority excluded
none of the four admissible mechanisms**: discrete named ranges, continuous
functions, container-relative adaptation, or a hybrid. Selecting one would have been
a new normative choice the work package held no authority to make.

The Human Maintainer has now made that choice. This ADR records why the chosen
architecture is the right one, and why the alternatives were not selected.

## Decision drivers

| # | Driver | Source |
| --- | --- | --- |
| **D-1** | A range is a **named span of available space** — not a device, not a screen, not a product decision | **RR-1** |
| **D-2** | A range name is a **foundation identifier** carrying no device, brand, product or platform term | **RR-2**, N-2, N-3 |
| **D-3** | **Core function may not be removed** because space is constrained | **RR-3**, baseline 5.7 |
| **D-4** | Adaptation must not defeat **user text resize, text spacing, or reflow** | **RR-4** |
| **D-5** | The model must remain expressible in **non-web channels**, where *viewport* has no meaning and page or slide geometry replaces it | **RR-6** |
| **D-6** | Layer 3 may not depend on **Layer 5** or accept a requirement pushed down from **Layer 6** | DEC-S-021, prohibited dependencies 2 and 3 |
| **D-7** | **Dense operational data** is the strongest registered consumer signal and the least-solved layout problem | Spatial Architecture, *Density*; `F-021-04` |
| **D-8** | A theme **re-binds and never redefines**, and the theme mechanism is **CDS-WP-022's**, undecided | T-1, VF-I-9, DEC-S-135 |
| **D-9** | Whatever is chosen must select **no value** and create **no identifier** | DEC-S-032, VP-1 … VP-7 |

## Considered alternatives

### For the primary spatial reference frame (chosen: declared Adaptation Container)

| Option | Assessment |
| --- | --- |
| **A device-class taxonomy** — phone, tablet, desktop, monitor | **Rejected.** It violates **D-1** and **D-2** directly: a device class is not a span of available space, and its names are exactly the terms **RR-2** and **N-2**/**N-3** exclude from a shared foundation identifier. It also fails **D-5** — a device class is meaningless for a printed page — and it silently imports Layer-5 and Layer-6 assumptions into Layer 3, contrary to **D-6**. |
| **A viewport-rooted Core identity model** | **Not selected.** It is the conventional choice and it is not forbidden as a *rendering* concern, but as **Core Layer-3 identity** it fails **D-5**: *viewport* has no referent in a paginated or slide channel, and **RR-6** requires the model to survive there. It also hard-codes a single, global frame, which cannot describe a region whose available space differs from the window's — the exact case **D-7** makes load-bearing. |
| **A declared Adaptation Container** | **Chosen.** It is a technology-neutral spatial reference boundary whose available space may be classified. It satisfies **D-1** by construction, keeps identifiers free of device terms (**D-2**), and generalizes across channels (**D-5**) because *what bounds the space* is declared rather than assumed. It is strictly more expressive than the viewport model without excluding it: **a root or application context may itself be the declared Adaptation Container.** |

### For the Core range model (chosen: named discrete available-space ranges)

| Option | Assessment |
| --- | --- |
| **Continuous functions as Core range identity** | **Not selected as Core identity.** A continuous relation has no named span to classify against, so **RR-1**'s *"named span"* has nothing to bind to, and **RR-2**'s identifier discipline has nothing to constrain. It would leave the foundation with no reviewable, migratable, machine-checkable vocabulary — the property **ST-1**'s principle exists to secure. **This is not a statement that continuous behaviour is impossible or unwanted** — see *Why continuous behaviour survives* below. |
| **Named discrete available-space ranges** | **Chosen.** A named span is exactly what **RR-1** describes, it is declarable rather than inferred, a change to the set is a **detectable** change, and it gives **RR-2**, **N-2** … **N-6** something concrete to police. It is also the only option that keeps the Layer-3 / Layer-5 line legible: a range names *where you are*, never *what happens*. |
| **A hybrid in which the Core model is itself dual** | **Not selected.** A Core vocabulary that is simultaneously discrete and continuous would have two identity models and therefore none. The hybrid CDS actually wants is obtained more cleanly by **layering**: discrete identity at Layer 3, continuous behaviour downstream. |

### For fixed-geometry channels (chosen: channel geometry is authoritative)

| Option | Assessment |
| --- | --- |
| **Universalize responsive ranges into every channel** | **Rejected.** It contradicts the Spatial Architecture channel table (*"ranges do not apply; page geometry replaces them"*) and the Channel Mapping, which classifies **VF-4** as `Transformed` for PDF and presentations. It would also be a Layer-6 constraint pushed into Layer 3, contrary to **D-6**. |
| **Channel geometry is authoritative for the channel** | **Chosen.** The broader spatial-context model still describes those channels — their reference frame is simply page or slide geometry rather than a variable span. **RR-6 is satisfied because the frame generalizes, not because the range construct does.** |

### For the relationship to themes (chosen: separate authority dimensions)

| Option | Assessment |
| --- | --- |
| **Treat a spatial context as a theme resolution context** | **Rejected as an implicit consequence.** The Theme Architecture classifies *"a context that varies within a channel"* as a theme, which would sweep a responsive range into the theme mechanism **by implication** — deciding, in passing, a question **DEC-S-135** reserves to **CDS-WP-022**. That is precisely the *"satisfied in form and violated in substance"* failure DEC-S-135 exists to prevent. |
| **Keep them separate unless CDS-WP-022 defines a mapping** | **Chosen.** The two are separate authority dimensions. **CDS-WP-022 retains full authority** to define a mapping or composition later, and this ADR neither prejudges nor forecloses it. |

## Decision

Recorded in full in **DEC-S-136**. In summary: the primary adaptive reference frame
for responsive Layer-3 classification is a **declared Adaptation Container**; the
Core Layer-3 response vocabulary is **named discrete available-space ranges**;
**continuous behaviour remains permitted downstream** where separately authorized
but is not Core range identity; **fixed-geometry channels use their own geometry**;
and a **Spatial Context is not a Theme Resolution Context** unless CDS-WP-022 later
defines the mapping.

**`RANGE ≠ BEHAVIOUR`** · **`CONTEXT ≠ PATTERN`** · **`FOUNDATION ≠ COMPOSITION`**
· **`CORE RANGE IDENTITY ≠ DOWNSTREAM RESPONSE BEHAVIOUR`** ·
**`SPATIAL CONTEXT ≠ THEME RESOLUTION CONTEXT`**

## Why a container rather than a viewport

The viewport model is not wrong; it is **too narrow to be the Core frame**, in three
independent ways.

It has **no referent in half of CDS's registered channels**. A printed report and a
slide deck have geometry, not a viewport, and **RR-6** requires the model to remain
expressible there. A frame that must be redefined per channel is not a foundation.

It is **global where the hard problem is local**. Dense operational data — CDS's
most-evidenced consumer need (**D-7**) — is composed into regions whose available
space frequently differs from the window's. A frame that can only describe the
window forces every such region to be handled as a Layer-5 exception, which is how a
foundation quietly stops carrying its own obligations.

It **invites the identifiers RR-2 forbids**. Once the frame is *the viewport*, range
names drift toward the devices that produce viewport sizes, and the drift is hard to
police because the names feel accurate. A declared container removes the temptation
at the source rather than policing it afterwards.

**None of this demotes the root or application context.** It may be the declared
Adaptation Container, and saying so creates no viewport identity: what is declared
is *a boundary whose available space is classified*, not *a device that produced
it*. **`viewport`, `desktop`, `tablet`, `mobile`, `phone` and `monitor` are not Core
responsive identifiers**, and this decision creates none of them.

## Why named discrete ranges are Core while behaviour stays Layer 5

A foundation supplies the terms in which a response can be described; it never
supplies the response. A **named span** is a term. A **transition** is a response.

Discrete named ranges give the foundation four properties a continuous relation
cannot: the set is **declared rather than inferred**, so a change to it is
detectable; each name is a **foundation identifier** that **RR-2** and **N-2** …
**N-6** can police; the vocabulary is **reviewable by a person** rather than only
computable; and it is **migratable**, because a rename is an identity event with a
migration reference rather than a silent redefinition.

The Layer-5 line stays legible for the same reason. *"Available-space range"* is
vocabulary. *"Switch navigation to a collapsed menu at that range"* is strategy.
**Layer 3 may describe *that* a response exists without deciding *which*** — the
rule the CDS-WP-021 contract already carries as **LO-8**.

## Why continuous behaviour survives

**Choosing a discrete Core identity model does not prohibit continuous behaviour,
and this ADR does not prohibit it.**

Continuous transformation and interpolation remain **permitted downstream where
separately authorized** — at Layer 5 as pattern behaviour, or in a channel or
runtime adapter. What the decision settles is only **which vocabulary carries Core
Layer-3 identity**.

Two clarifications are deliberate, because both are easy to over-read.

**The closed `$type` profile is not the reason.** The CDS admission profile is
`color`, `dimension` and `number` with no composite type (**DEC-S-130**), and a
continuous relation is not expressible in it today. **That is a fact about the
current profile, not a proof that continuous behaviour is architecturally
impossible.** The profile is itself governed and can be extended through an
authorized Elevated change. **This decision requires no new `$type` and alters
DEC-S-130 in no way.**

**The reason is architectural.** Core identity needs a name to bind obligations to.
A relation has no name to police, no step to declare, and nothing for a rename to
migrate. Discrete identity and continuous behaviour are therefore **complementary
layers, not competing options** — which is why the hybrid CDS wants is obtained by
layering rather than by making the Core model dual.

## Why fixed-geometry channels keep their own geometry

**RR-6** and the Spatial Architecture channel table pull in different directions
only if one insists that the *range construct* is universal. **RR-6** says the model
must remain expressible where *viewport* has no meaning and *"page or slide geometry
replaces it"*; the channel table says *"ranges do not apply; page geometry replaces
them"*.

**Both are true together exactly when the reference frame generalizes and the range
construct does not.** Continuity of available space is the property that decides
applicability: where space varies continuously a range is meaningful, and where
geometry is fixed the geometry occupies that position instead.

Forcing ranges into paginated channels would additionally invert **D-6**: it would
let a Layer-6 constraint dictate a Layer-3 construct. Where a channel cannot carry
the construct, that is a **declared limitation, never a silent drop** (VF-I-11).

## Why spatial context and theme stay separate

The Theme Architecture's classification rule — *a context that varies within a
channel is a theme* — would, read mechanically, make a responsive range a theme.
That reading must be rejected **because of what it would decide silently**.

**DEC-S-135** reserves the Theme and Context Mechanism to **CDS-WP-022**, and
**TC-6** requires that the semantic layer presuppose no context count and no context
set. If a spatial context were a theme by implication, CDS would have decided that
the resolver composes at least two context dimensions — a mechanism decision — while
formally leaving the mechanism open. That is the **form-versus-substance** failure
DEC-S-135 was written to prevent.

Keeping them separate costs nothing and forecloses nothing. **CDS-WP-022 retains
full authority** to define a mapping or a composition between the two, and if it
does, that will be its decision, taken with its evidence obligations. Until then the
conservative reading holds: **`SPATIAL CONTEXT ≠ THEME RESOLUTION CONTEXT`**, and
**`A THEME RE-BINDS; IT NEVER REDEFINES`** is untouched.

## Why no concrete range name or value is selected

The architecture and the vocabulary are two decisions, and only the first has been
taken.

**No range name, no number of ranges, no threshold, no boundary value, and no
magnitude of any kind is selected here**, and none may be inferred from this ADR.
The value prerequisites remain unsatisfied — **VP-3, VP-5, VP-6 and VP-7 fail for
every visual family**, and **VP-4 fails for VF-4** because `WP021-D2` is deferred and
no VF-4 technical root exists.

**An illustrative name would be worse than none.** VF-I-13 already records that an
example acquires no authority through repetition — but a plausible range name in an
ADR is exactly the kind of example that becomes a de facto identifier by citation.
This ADR therefore contains none, and the same restraint DEC-S-134 applied to the
role vocabulary applies here.

## Consequences

| # | Consequence |
| --- | --- |
| **C-1** | **VF-4 has a decided Core response architecture and still has no content.** The frame and the vocabulary *kind* are fixed; the vocabulary itself is not. |
| **C-2** | **A future range name is constrained before it exists.** It must be a span, not a behaviour; a foundation identifier, not a device term; declared, not inferred. |
| **C-3** | **The Layer 3 / Layer 5 line is now enforceable rather than merely stated.** A construct naming what happens is detectably out of Layer 3. |
| **C-4** | **Fixed-geometry channels are permanently exempt from forced range semantics**, and any inability to carry a distinction is a **declared limitation**. |
| **C-5** | **CDS-WP-022 inherits a smaller, cleaner question.** It decides the theme mechanism, and separately whether a spatial context composes with it. **Neither is decided here.** |
| **C-6** | **Continuous behaviour remains available downstream** and requires its own authorization; it acquires nothing from this decision. |
| **C-7** | **No validator changes.** The detection requirements CDS-WP-021 recorded for **CDS-WP-024** stand as requirements and are **not implemented**. |
| **C-8** | **No maturity, no evidence, no claim.** VF-4 stays **`Proposed`** and **AE-0**; the admitted `AE1-CDS-WP016-SEMSTATUS-004` transfers to nothing here. |

## Compatibility

This ADR is **additive** and breaks nothing. **RR-1 … RR-6 are unchanged** — the
decision **disposes of RR-5's open mechanism question and rewrites no constraint**.
**SP-1 … SP-5, ST-1 … ST-7, T-1 … T-10, TC-1 … TC-7, TS-1 … TS-6, VF-I-1 … VF-I-14,
N-1 … N-8, AF-1 … AF-5 and VP-1 … VP-7 are unchanged.** **DEC-S-128 … DEC-S-135 are
unchanged**, and **DEC-S-130 and DEC-S-135 in particular are untouched**.

No artifact exists that could break, because **no VF-4 source, identifier, or value
exists**.

## Future implementation obligations

*(Stated as obligations on later, separately authorized work. **None is
implemented, and naming a destination authorizes nothing.**)*

1. **`WP021-D2`** — whether VF-4 acquires a technical root and a source-set identity
   — remains **deferred** and is a **Human-Maintainer decision**.
2. A concrete range vocabulary requires its own authorization and must satisfy the
   value-selection discipline; **`CDS-WP-020A` may not invent one.**
3. **CDS-WP-022** decides the theme mechanism and, separately, any spatial-context
   composition.
4. **CDS-WP-024** must be able to detect a range identifier carrying a device,
   product or channel term, a construct stating a behaviour rather than a span, and
   an undeclared reference frame.
5. **CDS-WP-031** owns the rendering evidence for reflow, resize, text spacing,
   magnification, target-size outcome, and the density interaction.

## Authority boundary

This ADR records rationale. It **decides nothing that DEC-S-136 does not decide**,
and DEC-S-136 wins on any divergence.

It creates **no** value, **no** range name, **no** identifier instance, **no** VF-4
technical root, **no** `sourceSetId`, **no** `sourceRevision`, **no** Source Set,
**no** token source file, manifest, resolver, schema, validator rule, test, fixture,
component, brand, theme, pattern, or Product Profile. It admits **no** evidence,
changes **no** maturity, accepts or closes **no** risk, makes **no** claim, and
**activates no work package** — **`CDS-WP-020A`, CDS-WP-022, CDS-WP-023 and
CDS-WP-024 remain `Planned`, not active, and not authorized.**

**It is `Accepted` and effective**, at the Human-Maintainer exact integration commit
`a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9` (2026-09-11). Before that commit it was
`PROPOSED / AUTHORIZED FOR INTEGRATION` and conferred no acceptance and no
authority. **Acceptance changed nothing this ADR excludes:** it still creates no
value, no range name, no identifier, no VF-4 technical root, and no Source Set, and
it still activates no work package.

## Related documents

- [DEC-S-136 — Decision Index](DECISION_INDEX.md)
- [Adaptive Layout and Responsive Foundation](../architecture/ADAPTIVE_LAYOUT_AND_RESPONSIVE_FOUNDATION.md) — CDS-WP-021
- [Visual Foundation Spatial Architecture](../architecture/VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md) — RR-1 … RR-6
- [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md) — T-1 … T-10, TS-1 … TS-6
- [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md) — VP-1 … VP-7
- [Design System Architecture](../architecture/DESIGN_SYSTEM_ARCHITECTURE.md) — DEC-S-021 layers
- [Work Packages](../../project-system/WORK_PACKAGES.md)
