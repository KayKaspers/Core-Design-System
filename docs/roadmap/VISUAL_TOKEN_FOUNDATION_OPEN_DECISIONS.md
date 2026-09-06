# Visual Token Foundation — Open Decisions

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-020 — Reference and Semantic Token Foundation
- **Date:** 2026-08-26
- **Updated:** 2026-08-27 — CDS-WP-020 Decision Integration Pass. **OD-1, OD-2 and
  OD-3 are answered by DEC-S-128, DEC-S-130 and DEC-S-131** (with
  [ADR-0004](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md)),
  and a fourth decision — **DEC-S-129**, the contrast evaluation authority — was
  taken alongside them. **All four are effective** at the Human-Maintainer
  exact-byte integration commit `42a568d823de3388e45af62967546f13ad67eff6`.
  **OD-4, OD-5, OD-6 and OD-7 remain open**, and three residual items are recorded
  under the answered entries.
- **Updated:** 2026-09-05 — CDS Step-9 Decision Integration Pass. The Human
  Maintainer decided **OD-4**, **OD-5**, **OD-6A** and **OD-7**, and dispositioned
  **OD-6B** as answered by existing normative authority. **DEC-S-132**
  (with [ADR-0005](../decisions/ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md)),
  **DEC-S-133**, **DEC-S-134** and **DEC-S-135** are **effective** — they became
  effective at the Human-Maintainer exact integration commit
  `2cb244e889c1a6b5a278afb233995a0379b5d9ef` of the
  reviewed object. **OD-4 is answered and the OD-3 concrete-root residual is
  resolved; OD-5 is only partially answered; OD-6A is policy-answered with the
  concrete vocabulary still open; OD-7 is answered.** **Four residuals remain open
  and one is added.** **No value is selected, no Source Set is created, and no work
  package is authorized.**
- **Artifact class:** **8 — Example / planning artifact. NON-NORMATIVE.**
- **Status:** **A decision-preparation register. It decides nothing.** The Decisions
  it prepared for are recorded in the
  [Decision Index](../decisions/DECISION_INDEX.md); **this register is not their
  authority and never becomes one.**

> **This document is not normative, is not a Decision, and is not an
> authorization.** It records the normative choices CDS-WP-020 found it could not
> make, so that they can be decided deliberately rather than by implication.
> Listing an option here does not adopt it; a recommendation is a recommendation
> and nothing more. **The Human Maintainer decides; Nova reviews and recommends;
> Claude records.**

## Why this register exists

CDS-WP-020 was authorized to establish the first concrete Reference and Semantic
token layer of the visual foundation. Executing it revealed that **the value half
of that work is gated on normative choices that no committed CDS source has
made**, and that CDS-WP-020 holds no authority to make them: Claude creates no
Decision, no ADR, and no risk entry without separate authorization.

Rather than making the choices implicitly by writing a token file — which would
**acquire** authority instead of receiving it, contrary to DEC-S-033 — CDS-WP-020
delivered the layer's **contract** and recorded the choices here.

This is the mechanism the Risk Register itself prescribes for **RISK-003**
(premature design decisions): *maintain an explicit list of intentionally open
decisions, and treat any premature decision as a reportable deviation.*

## What is blocked, and what is not

*(Updated 2026-09-05. OD-1, OD-2 and OD-3 are answered and effective; **OD-4 and
OD-7 are answered, OD-5 is partially answered, OD-6A is policy-answered and OD-6B is
answered by existing authority** — all four **effective** at the Human-Maintainer
exact integration commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`. **Every entry in the right-hand column below is still
blocked**, because **VP-3, VP-5, VP-6 and VP-7 remain unsatisfied for every
family** and VP-2 remains unsatisfied for typeface identity, weight identity and
composites. **Only VP-4 has moved**, for VF-1, VF-2, VF-3, VF-5 and VF-6 — and an
identifier grammar with fixed roots creates **no identifier instance**.)*

| Delivered by CDS-WP-020 | Blocked pending the decisions below |
| --- | --- |
| The Reference layer contract (RP-1 … RP-10, ST-1 … ST-7, RN-1 … RN-9, RV-1 … RV-5, RB-1 … RB-5) | Every concrete visual value |
| The Semantic layer contract (SR-1 … SR-12, SN-1 … SN-9, PN-1 … PN-5, TC-1 … TC-7, SS-1 … SS-8, IS-1 … IS-5) | Every concrete identifier |
| The alias model (AL-1 … AL-8) | Every token source file, manifest, and resolver |
| The value-selection discipline (VP, VE, IG, VD, VA, VS) | Any maturity transition for any visual family |
| The machine-readable disposition, stated with reasons | Any accessibility evidence of any level |
| The validation requirements handed to CDS-WP-024 | — |

**Nothing in the existing machinery blocks implementation.** The format profile,
the source-set classes, the reference semantics, the serialization contract, the
committed schemas, and the offline validator are all sufficient. What is missing is
**decisions**, not capability. That distinction is the substance of this register.

## Register state — 2026-09-05

*(Non-normative status view. The **Decisions** are the authority; this table is
not. **DEC-S-132 … DEC-S-135 are effective** at the Human-Maintainer exact
integration commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`. The 2026-08-27 view
this table replaces is preserved as the *Register state — 2026-08-27* record
below.)*

| # | Proposition | State |
| --- | --- | --- |
| **OD-1** | Colour space and encoding | **ANSWERED — DEC-S-128**, effective. Residual **OPEN**: the CDS-specific disposition of the optional DTCG `hex` member. |
| **OD-2** | The admitted DTCG `$type` set | **ANSWERED — DEC-S-130**, effective. Residuals **OPEN**: font-family identity representation, font-weight identity representation, and composite-type admission. |
| **OD-3** | Visual source-set identity, granularity, topology | **ANSWERED — DEC-S-131**, effective, for unit, topology and maturity granularity. **Concrete-root residual: RESOLVED by DEC-S-132**, effective. |
| **OD-4** | The concrete identifier grammar | **ANSWERED — DEC-S-132** (ADR-0005), effective. |
| **OD-5** | Scale topology for the dimensional families | **PARTIALLY ANSWERED — DEC-S-133**, effective: the **scale ownership model** and the **topology/value boundary** only. Residuals **OPEN**: **per-family topology parameters** for every family in scope, and **VF-1 tonal topology**. |
| **OD-6A** | The concrete role vocabulary | **POLICY ANSWERED — DEC-S-134**, effective: an **admission rule** only. **The concrete role vocabulary REMAINS OPEN**, and `CDS-WP-020A` may not invent it. |
| **OD-6B** | How many families CDS matures separately | **ANSWERED BY EXISTING NORMATIVE AUTHORITY. No new Decision.** VF-1 … VF-9 remain separate artifact families under AF-1, AF-3 and AF-4. **BATCHED REVIEW ≠ SHARED MATURITY.** |
| **OD-7** | Sequencing against CDS-WP-022 | **ANSWERED — DEC-S-135**, effective. |

> **Four answers still do not complete the value system.** **VP-3, VP-5, VP-6 and
> VP-7 remain unsatisfied for every visual family**, and VP-2 remains unsatisfied
> for typeface identity, weight identity and composites — so **no visual value may
> be selected**. Visual values remain **0**, visual source sets remain **0**, visual
> Candidate families remain **0**, and VF-1 … VF-9 remain **`Proposed`**.
> **No work package is currently authorized.**

### Residual register — 2026-09-05

| Residual | Origin | State |
| --- | --- | --- |
| The CDS-specific disposition of the optional DTCG `hex` member | OD-1 | **OPEN** |
| Font-family identity representation | OD-2 | **OPEN** — gated by Typography FP-1 … FP-8, **Elevated** |
| Font-weight identity representation | OD-2 | **OPEN** — same gate |
| Composite-type admission | OD-2 | **OPEN** — needs a demonstrated family need |
| Concrete visual source-set root identifiers | OD-3 | **RESOLVED by DEC-S-132**, effective |
| Per-family scale topology parameters — anchor declaration, progression-rule kind, step count, extension behaviour, exclusions | OD-5 | **OPEN for every family in scope** |
| VF-1 Colour tonal topology | OD-5 | **OPEN** — a distinct problem, coupled to CDS-WP-022 and the OD-1 `hex` residual |
| The concrete role vocabulary | OD-6A | **OPEN** — admissible only under DEC-S-134's rule |
| Any migration or deprecation compatibility mechanism outside the normative Semantic alias graph | **NEW, recorded by DEC-S-132** | **OPEN** — AL-2 is unchanged and prohibits a semantic-role alias edge; no committed source specifies any other mechanism |

## Register state — 2026-08-27

*(Preserved point-in-time record. It was true when written and is **not** rewritten
because Step 9 has since been decided.)*

| # | Proposition | State |
| --- | --- | --- |
| **OD-1** | Colour space and encoding | **ANSWERED — DEC-S-128.** Residual: the CDS-specific disposition of the optional DTCG `hex` member. |
| **OD-2** | The admitted DTCG `$type` set | **ANSWERED — DEC-S-130.** Residual: font-family and font-weight identity representation, and composite-type admission. |
| **OD-3** | Visual source-set identity, granularity, topology | **ANSWERED — DEC-S-131** for unit, topology and maturity granularity. Residual: the **concrete root identifiers**, coupled to OD-4. |
| **OD-4** | The concrete identifier grammar | **OPEN** |
| **OD-5** | Scale topology for the dimensional families | **OPEN** |
| **OD-6** | Role vocabulary, and how many families CDS matures separately | **OPEN** |
| **OD-7** | Sequencing against CDS-WP-022 | **OPEN** |

**A decision taken alongside these, belonging to no OD entry:** **DEC-S-129** —
WCAG 2.2 as the contrast evaluation authority, full-precision comparison, and
additional methods informational only. It was **not** recorded as an open decision
here, because it is an accessibility-methodology question rather than a
representation or topology one, and it is deliberately **not** an architecture
dependency of ADR-0004.

> **Three answers do not complete the value system.** **VP-3, VP-4 and VP-5 remain
> unsatisfied for every visual family**, so **no visual value may be selected**.
> Visual source sets remain **0**, visual Candidate families remain **0**, and
> VF-1 … VF-9 remain **`Proposed`**.

## The open decisions

### OD-1 — Colour space and encoding for CDS colour reference tokens

> **ANSWERED by DEC-S-128 (2026-08-27), effective.** The recommendation
> below — option **(a)** combined with **(d)** — was adopted: the pinned DTCG
> 2025.10 colour space keyed **`srgb`** is the single canonical normative authored
> representation, every other representation is a class-3 generated output, and a
> perceptually uniform space such as OKLCH is admitted for **derivation and
> analysis only**. The `colorSpace` key and the component model were verified
> directly against the **Color Module 2025.10 Final Community Group Report**.
>
> **Residual, recorded rather than silently deferred:** the CDS-specific
> disposition of the optional DTCG **`hex`** member. DEC-S-128 creates no hex
> authority and no new hex prohibition, and states only that `hex` may never become
> a second source of truth. Whether CDS requires, permits, or prohibits it in a
> normative visual source is **still open** and needs its own authorization.
>
> The alternatives, recommendation and impact statement below are preserved as the
> **preparation record**. They are not the decision; **DEC-S-128 is.**

**Proposition to decide.** In which colour space CDS authors normative colour
reference tokens, how that value is encoded under the pinned DTCG 2025.10 Color
Module, and what a channel transformation may and may not do to it.

**Why existing authority is insufficient.** The
[Visual Foundation Colour Architecture](../architecture/VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
states it directly: *"Which colour space CDS authors in is not decided here. It is
CDS-WP-020's,"* and lists *colour space and encoding* under **Deferred decisions**,
each item requiring *"its own explicitly authorized work package."* The
[CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md) admits the
Color Module's `colorSpace` + `components` structure **as defined** and selects no
value. **No DEC-S entry and no ADR selects a colour space.**

**Alternatives.**

| # | Option | Consequence |
| --- | --- | --- |
| **a** | **A standard gamma-encoded RGB space as the authored space**, with deterministic offline conversion for any channel needing another | WCAG contrast is defined over that space's relative luminance, so a role pairing's contrast obligation is computable **directly from the source** with no conversion. Every registered CDS channel — product UI, documentation, repository, PDF, presentation, diagrams — can consume it. Cost: scale steps are not perceptually uniform, so a tonal scale needs care. |
| **b** | **A perceptually uniform space as the authored space** | Tonal scales become principled and even, and lightness reasoning is direct. Cost: contrast evaluation and most channel output require conversion, gamut mapping must be specified for out-of-gamut results, and the conversion becomes part of the normative determinism surface (DEC-S-080). |
| **c** | **A wide-gamut display space as the authored space** | Wider on-screen range. Cost: the weakest print, greyscale, and export story of the three, against a registered channel model that includes **paginated, printed, projected, and exported** channels — *PDF and reports*, *Presentations*, and *Diagrams* — and in which **four of nine channels have no accessibility profile at all** (RISK-046). Gamut mapping becomes mandatory rather than exceptional. |
| **d** | **Author in one space and derive the others as generated output** | Compatible with any of (a) … (c); it is an orthogonal statement about outputs, not a substitute for choosing the authored space. |

**Recommendation.** **(a) combined with (d)** — a standard gamma-encoded RGB space
as the single **normative authored** space, with every other representation
produced as a **class-3 generated output** carrying provenance. Reasons: the
contrast obligation of every colour role becomes computable offline from the
source with no conversion step in the normative path; the registered print,
export, and greyscale channels are served without gamut mapping in the source; and
DEC-S-030 and DEC-S-080 are satisfied with the fewest moving parts. Perceptual
evenness remains achievable by **computing** steps in a perceptual space and
recording the result — a derivation method, not a normative space.

**Confirm before deciding.** The exact `colorSpace` identifiers admissible must be
read from the **pinned DTCG 2025.10 Color Module** at decision time, not assumed.
Preview, draft, and future reports are **not** part of this profile (DEC-S-074,
RISK-056).

**Affected if decided.**
[CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md) ·
[Visual Foundation Colour Architecture](../architecture/VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md) ·
[Machine-Readable Validation Contract](../architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md) ·
`schemas/` · `tools/cds_validator/` · `tests/` · the Decision Index.

**Track.** **Elevated** — a CDS Token Format Profile change (DEC-S-082) bearing on
accessibility obligations.

---

### OD-2 — The admitted DTCG `$type` set for the visual families

> **ANSWERED by DEC-S-130 (2026-08-27), effective.** The recommendation
> below — option **(b)** — was adopted: the admitted set is exactly **`color`**,
> **`dimension`** and **`number`**, each verified directly against the **Format
> Module 2025.10 Final Community Group Report**; **no composite type is admitted**;
> every normative CDS visual token carries its **own** explicit `$type`; and
> `$type` carries value-type semantics only. **`profileVersion` stays `"1"`**, and
> no schema, validator, test, or fixture was changed.
>
> **Residuals, recorded rather than silently deferred:** the representation of
> **font-family and font-weight identity** — still gated by the Typography
> Architecture's FP-1 … FP-8 as an **Elevated** change — and **composite-type
> admission**, which requires a demonstrated family need and its own authorization.
>
> The alternatives, recommendation and impact statement below are preserved as the
> **preparation record**. They are not the decision; **DEC-S-130 is.**

**Proposition to decide.** Which token `$type` values the CDS profile **admits**
at the Reference and Semantic layers of the visual families, and whether composite
types are admitted at all.

**Why existing authority is insufficient.** The
[Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
records *"the admitted DTCG `$type` set for visual families"* as **deferred
decision 2, destination CDS-WP-020**, and states that *"that admitted type set is
not enumerated here."* The CDS Token Format Profile requires an explicit `$type`
*"from the DTCG-defined types applicable to CDS scope"* and **enumerates no set**.

**A repository fact that must not be misread:** the committed offline validator
carries a bounded set of token `$type` values for its **V2** layer, explicitly
scoped by **DEC-S-098** (*initial DTCG coverage is explicitly bounded*). That is a
**validator coverage boundary**, not a CDS profile admission, and reading it as
one is precisely **RISK-074** (*partial DTCG coverage overstated*). The committed
token-document schema places **no** `$type` constraint at all.

**Alternatives.**

| # | Option | Consequence |
| --- | --- | --- |
| **a** | **Admit the full set the pinned report defines** | Maximum expressiveness immediately. Cost: CDS would admit composite types it has neither modelled nor validated, and the gap between *admitted* and *validated* is exactly the shape RISK-074 describes. |
| **b** | **Admit a minimal scalar set now; admit composites only when a family demonstrably needs one** | Each admitted type is one CDS has modelled, named obligations for, and can validate. Cost: a later family needing a composite requires an additive profile change — which is governed, non-breaking, and detectable. |
| **c** | **Admit per family on demand, with no standing set** | Maximum precision, maximum governance load against a single-maintainer bottleneck (RISK-029, RISK-040). |

**Recommendation.** **(b)**. A composite type bundles several decisions into one
token — a shadow bundles colour with offsets and blur; a typography token bundles
family, weight, size, and line height — and that bundling is precisely where the
semantic layer loses the ability to declare a **per-part** obligation under SR-3,
SR-4, and SR-5. Admitting composites before the roles that would use them exist
would decide the granularity question by implication.

**Affected if decided.** The CDS Token Format Profile · the Validation Contract ·
`schemas/cds-token-document.schema.json` · `tools/cds_validator/validation.py` ·
`tests/` · the Decision Index.

**Track.** **Elevated** — a profile and validation-contract change (DEC-S-082).

---

### OD-3 — Visual source-set identity, granularity, and file topology

> **ANSWERED by DEC-S-131 (2026-08-27), effective**, for the **unit, the
> topology and the maturity granularity.** The recommendation below — option
> **(b)** — was adopted in substance: **one source set per independently evaluable
> Family × Token-Flow-Layer unit**, each carrying its own `sourceSetId`,
> `sourceRevision`, `layer`, dependencies, `maturityState` and `approvalState`, with
> maturity binding to the pair (`sourceSetId`, `sourceRevision`).
>
> **The cost argument below was corrected, and the correction matters.** Option (b)
> was recorded as *"ten sets, plus manifests and a resolver"*, which implied that
> per-family, per-layer source sets multiply manifests at the same rate. They do
> not: the committed Source-Set Manifest contract carries a **`sourceSets` array**,
> and **one manifest may aggregate many source sets**, each retaining its own
> maturity. **A source set is not a manifest**, and **AGGREGATED is not MATURE** —
> a manifest's own maturity describes only the manifest artifact. This is the
> precise correction of CDS-WP-020 finding **`F-020-02`**: its **conclusion
> stands**, its **artifact-count mechanism was imprecise**.
>
> **Residual, recorded rather than silently deferred:** the **concrete root
> identifiers** of the visual source sets. DEC-S-131 controls the root vocabulary
> through the registered VF-1 … VF-9 families but **invents, adopts, reserves and
> recommends no concrete identifier**. That residual is coupled to **OD-4**, and
> **repository topology remains an explicit DEC-S-032 deferral**.
>
> **That residual is RESOLVED by DEC-S-132 (2026-09-05)**, **effective at the
> Human-Maintainer commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`**: the ten source-set identities
> `reference/color` … `semantic/surface` are fixed in the flat `<layer>/<family>`
> form, and the technical roots are `color`, `typography`, `space`, `shape` and
> `surface`. **Identity is fixed; no Source Set instance, no `sourceRevision`, no
> manifest and no resolver is created, and repository topology remains a DEC-S-032
> deferral.**
>
> The alternatives, recommendation and impact statement below are preserved as the
> **preparation record**. They are not the decision; **DEC-S-131 is.**

**Proposition to decide.** How many normative source sets the visual foundation
has, what their stable identities are, where they live, and how each maps to the
per-family maturity model.

**Why existing authority is insufficient.** The
[Machine-Readable Source Model](../architecture/MACHINE_READABLE_SOURCE_MODEL.md)
defines the **classes** (Reference Source Set, Semantic Source Set, Manifest,
Resolver) but establishes no visual instance. The one existing precedent —
`semantic/status` — required an explicit Decision to establish its identity and
location (**DEC-S-115**). **Repository topology is an explicit DEC-S-032
deferral.**

**The tension that must be resolved, not papered over.** A source-set payload
carries **one** `maturityState` and **one** `approvalState`. The
[Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
requires that **maturity is never inherited** (AF-1) and that **a family may
mature at its own pace** (AF-3). A single shared semantic source set spanning
VF-1, VF-2, VF-3, VF-5, and VF-6 cannot express five independent maturities;
per-family sets can, at a real governance cost.

**Alternatives.**

| # | Option | Consequence |
| --- | --- | --- |
| **a** | **Two sets** — one Reference, one Semantic, spanning all visual families | Fewest artifacts, simplest graph. Cost: **contradicts AF-1 and AF-3** — every family would share one maturity, so the slowest family would hold the rest back or, worse, be carried by them. |
| **b** | **Per family, per token-flow layer** — a Reference and a Semantic set for each of VF-1, VF-2, VF-3, VF-5, VF-6 (ten source sets). *(Corrected 2026-08-27: the original wording, "ten sets, plus manifests and a resolver", implied a manifest per set. **One manifest may aggregate many source sets**, so the artifact count does not multiply that way.)* | Preserves AF-1 and AF-3 exactly; each family's evidence and gate are cleanly bound. Cost: a governance load on a model run by **one** Human Maintainer, with the Consumer Maintainer role **unstaffed** (FM-F-006, RISK-029, RISK-040) — **smaller than first assessed**, for the reason in the correction. |
| **c** | **Per family for Semantic; one shared Reference set** | Maturity independence where obligations live; one primitive pool. Cost: the shared Reference set's maturity becomes a floor under every family (AF-4 generalized), which must be stated rather than discovered. |

**Recommendation.** **(b)**, and it should be decided together with **OD-6**. AF-1
and AF-3 are normative and were written knowing the cost; a topology that cannot
express them is the wrong topology. If the governance load proves unsustainable,
the correct response is to **reduce the number of families being matured** (OD-6),
not to collapse independent maturities into a shared artifact — the lifecycle
document says so itself: *"Fewer families that actually reach a gate beat nine
that do not."*

**Affected if decided.** `tokens/` topology · the Machine-Readable Source Model ·
the Visual Foundation Governance and Lifecycle document · the Decision Index.

**Track.** **Elevated** — it fixes source-set identity and the maturity surface.

---

### OD-4 — The concrete identifier grammar for reference and semantic positions

> **ANSWERED by DEC-S-132 (2026-09-05), effective at the Human-Maintainer commit
> `2cb244e889c1a6b5a278afb233995a0379b5d9ef`.** The recommendation below — option **(c)** — was adopted in
> substance: **family-rooted paths with a declared, optional qualifier position**,
> the reference grammar `<family>.<primitive-group>.<step>[.<qualifier>]` and the
> semantic grammar `<family>.<role>[.<qualifier>]`. Three things were decided that
> this entry did not anticipate: **the slot is named `qualifier`, not `modifier`**,
> because *conditional modifier* is already bound to Resolver / Theme composition
> semantics; **token-path identity and source-set identity are two separate spaces**
> and a `sourceSetId` is **declared, never derived**; and **the concrete roots were
> fixed** — `color`, `typography`, `space`, `shape`, `surface`, with the ten
> source-set identities `reference/color` … `semantic/surface` in the flat
> `<layer>/<family>` form. **The OD-3 concrete-root residual is resolved by it.**
>
> **A new residual, recorded rather than silently deferred:** any **migration or
> deprecation compatibility mechanism outside the normative Semantic alias graph**.
> AL-2 is unchanged and prohibits a semantic-role alias edge; no committed source
> specifies any other mechanism, and DEC-S-132 specifies none.
>
> **VP-4 is satisfied for VF-1, VF-2, VF-3, VF-5 and VF-6** —
> and nothing more. **No identifier instance, no Source Set, and no
> `sourceRevision` exists; VP-5 stays unsatisfied; visual source sets stay 0.**
>
> The alternatives, recommendation and impact statement below are preserved as the
> **preparation record**. They are not the decision; **DEC-S-132 is**, with
> [ADR-0005](../decisions/ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md)
> as its architecture record.

**Proposition to decide.** The concrete path grammar for visual reference and
semantic identifiers, and the fixed set of root segments it admits.

**Why existing authority is insufficient.** The Visual Foundation Architecture
gives the grammar only as a **non-normative illustration**, stating that *"no
identifier below is adopted, reserved, recommended, or planned"* and that *"the
concrete vocabulary is CDS-WP-020's and requires its own authorization."*
DEC-S-081 fixes **segment syntax**, not path structure. The one precedent —
`status.<axis>.<value>` — required an explicit Decision (**DEC-S-117**).

**Alternatives.**

| # | Option | Consequence |
| --- | --- | --- |
| **a** | **Family-rooted paths**, with the token-flow layer carried only by source-set metadata | Matches the `status.<axis>.<value>` precedent; the layer is already machine-checkable from the manifest, so the path carries no duplicate information. |
| **b** | **Layer-rooted paths**, with an explicit layer segment | The layer is visible in every identifier. Cost: it duplicates manifest metadata in every name, and a layer change would become a mass rename — a migration event (DEC-S-082) for information the manifest already holds. |
| **c** | **Family-rooted, with a reserved modifier position** | As (a), with a declared slot for modifiers so that adding one is not a grammar change. |

**Recommendation.** **(c)** — family-rooted with a declared modifier position.
N-6 requires that *"the path encodes family, role, and modifier — not a value, a
theme, or a profile"*, which (c) satisfies literally, and the `semantic/status`
precedent shows a family-rooted path working under exactly this profile. A
reserved modifier position avoids turning the first modifier CDS needs into a
breaking grammar change.

**Affected if decided.** Both CDS-WP-020 foundation documents · the CDS Token
Format Profile · every future token source · the Decision Index.

**Track.** **Elevated** — a naming-profile statement; a later rename is a
migration event.

---

### OD-5 — Scale topology for the dimensional families

> **PARTIALLY ANSWERED by DEC-S-133 (2026-09-05), effective at the Human-Maintainer
> commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`.** The recommendation below — option **(c)**,
> *one declared base unit with per-family step sets derived from it* — was **not
> adopted, and was rejected on the normative text.** **ST-5 is per-scale**:
> *"computable offline and deterministically from **its** declared base and
> rule"*, and the section carrying ST-1 … ST-7 is introduced as *"Normative as
> requirements on a scale, not as a scale."* A universal cross-family base would
> have created the coupling **AF-3** exists to prevent.
>
> **What was decided:** **independent per-family ordered scales under the common
> ST-1 … ST-7 contract**, with **no universal cross-family base** and no family's
> scale deriving base, rule, or value authority from another's; the invariant
> **`SCALE TOPOLOGY ≠ SCALE VALUES`**; and the reading that **VP-3's "base" means
> the anchor declaration, not a numeric anchor magnitude.**
>
> **What was NOT decided, and stays open:** **the per-family topology parameters** —
> for every family in scope, the concrete anchor declaration, progression-rule kind,
> step count, extension behaviour and exclusions. **VP-3 therefore remains
> UNSATISFIED for every family and fails closed.** Deciding *who owns a scale* is
> not deciding *what the scale is*.
>
> **VF-1 Colour tonal topology was split out and remains OPEN as a distinct
> residual.** It is not among the ordered primitive sets the Visual Reference Token
> Foundation enumerates; it would be ordered by a perceptual property while OKLCH is
> derivation-only (DEC-S-128); and it is coupled to CDS-WP-022 and to the OD-1 `hex`
> residual. **VF-4, VF-7, VF-8 and VF-9 are excluded** to their owning work
> packages, and **opacity remains an attribute of VF-1 and VF-6** (DEC-S-128 clause
> 11), never a family.
>
> The alternatives, recommendation and impact statement below are preserved as the
> **preparation record**, including the recommendation that was rejected. They are
> not the decision; **DEC-S-133 is.**

**Proposition to decide.** For each family holding an ordered primitive set —
VF-2 size and line height, VF-3 spacing and size, VF-5 radius and stroke, VF-6
elevation and opacity — the base unit, the progression rule, the step count, the
step-naming convention, and the extension behaviour.

**Why existing authority is insufficient.** Each family architecture lists *scale
structure and step count* under **Deferred decisions**, each requiring its own
explicitly authorized work package. No committed source constrains topology beyond
the requirement that an ordered set exists. **ST-1 … ST-7** of the
[Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md)
state what a scale must **satisfy**; they select none.

**Alternatives.**

| # | Option | Consequence |
| --- | --- | --- |
| **a** | **One shared scale across families** | Maximum visual coherence. Cost: a change for one family silently changes every other, and radius, stroke, and opacity have no honest reason to share a spacing rhythm. |
| **b** | **Independent per-family scales** | Each family is free. Cost: no relationship between families is expressible, and coherence becomes convention rather than structure. |
| **c** | **One declared base unit; per-family step sets derived from it by a declared rule** | Relationships are data rather than coincidence, derivation is deterministic and offline (ST-5), and a family may deviate by declaring that it does. |

**Recommendation.** **(c)**. It is the only option under which ST-1, ST-2, and
ST-5 are satisfiable by construction rather than by discipline, and it keeps a
family change from propagating silently. Note that (c) fixes **topology only** —
the step **values** remain gated on OD-1 for colour-adjacent families and on the
authorization that selects values at all.

**Affected if decided.** The Spatial, Shape and Surface, and Typography
architectures · the Visual Reference Token Foundation · the Decision Index.

**Track.** **Elevated** — it bears on the target-size floor (2.5.8) and on
text-resize and reflow behaviour.

---

### OD-6 — The concrete role vocabulary, and how many families CDS matures separately

> **SPLIT AND DISPOSITIONED (2026-09-05).** The two coupled questions were separated
> because they are not one indivisible normative choice: they have different
> authority families, different amendment triggers, and different risks.
>
> **OD-6A — the concrete role vocabulary: POLICY ANSWERED by DEC-S-134**,
> **effective at the Human-Maintainer commit
> `2cb244e889c1a6b5a278afb233995a0379b5d9ef`**. Option **(b)**
> below was adopted **as an admission rule only** — a role enters CDS Core only on
> demonstrated **cross-consumer** need, classified before design, satisfying
> **SR-1 … SR-12 from creation**, inside the **closed** role classification.
> **The concrete role vocabulary REMAINS OPEN**, no role identifier is created, and
> **`CDS-WP-020A` may not invent, adopt, reserve, or recommend one.** **VP-6 stays
> UNSATISFIED** — a policy is not an authored role. **`selected`, `active` and
> `current` are not CDS Core roles today** (answering **IS-5**); that is **not a
> permanent prohibition**, IS-1 and IS-5 already bind whatever a consumer builds,
> and their distinctness is answered with the vocabulary rather than before it.
>
> **OD-6B — how many families CDS matures separately: ANSWERED BY EXISTING
> NORMATIVE AUTHORITY. No new Decision, and none should be created.** The
> [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
> already states normatively that **each of VF-1 … VF-9 is a separate artifact
> family with its own maturity, evidence, gate, and compatibility statement**, under
> **AF-1**, **AF-3** and **AF-4**. **The recommendation below — reducing the family
> count by treating VF-3, VF-5 and VF-6 as one maturity group — was rejected**,
> because it would have required amending that rule rather than answering an open
> question, and would have created the inheritance AF-1 forbids. What was genuinely
> open was **how many families CDS chooses to pursue to a gate, and how the review
> effort is organised** — a scheduling matter settled at authorization time.
> **Administrative batching may occur, and BATCHED REVIEW ≠ SHARED MATURITY;
> BATCHED GATE PREPARATION ≠ MATURITY INHERITANCE.** No maturity group, cluster
> maturity, roll-up maturity, inherited maturity, or aggregate gate exists or may be
> created. `F-019-07` and `F-020-08` close with this disposition.
>
> The alternatives, recommendation and impact statement below are preserved as the
> **preparation record**, including the family-count recommendation that was
> rejected. They are not the decision; **DEC-S-134 and the existing artifact-family
> authority are.**

**Proposition to decide.** Two coupled questions: the concrete semantic role
vocabulary per family, and **whether all nine visual families are worth maturing
separately** at all.

**Why existing authority is insufficient.** The Visual Foundation Architecture
records *"the concrete shared vocabulary of families, roles, and modifiers"* as
**deferred decision 3, destination CDS-WP-020**. The Visual Foundation Governance
and Lifecycle document leaves the second question explicitly open: *"Whether all
nine are worth maturing separately is a real question for CDS-WP-020, and this
document does not pre-answer it."* **Adding a semantic role is an Elevated
change**, and the `semantic/status` precedent registered both its token count
(DEC-S-116) and its path grammar (DEC-S-117) as Decisions.

**What makes this hard, stated honestly.** **No registered consumer requirement
asks for a colour palette, a type scale, a spacing scale, a radius scale, an
elevation model, an icon library, or illustration.** VF-3, VF-5, VF-6, and VF-7
carry **no consumer demand evidence at all**. A role vocabulary invented without
demand is the most likely place for **RISK-021** (token proliferation) and
**RISK-026** (architecture overdesign) to materialize, and every role added
carries an accessibility obligation **from the moment it exists**.

**Alternatives.**

| # | Option | Consequence |
| --- | --- | --- |
| **a** | **A complete role vocabulary for all five families at once** | One decision, one review. Cost: the largest possible Elevated change, mostly unevidenced, reviewed by one maintainer. |
| **b** | **A minimal vocabulary bound to the six registered Layer-3 consumer anchors** — CR-002, CR-006, CR-021, CR-022, CR-023, CR-025 — extended only on evidenced need | Every role traces to a registered requirement; the unevidenced families stay deliberately small. Cost: the system looks incomplete next to benchmarks, which is a cost worth paying (IG-2). |
| **c** | **Focus role set first, alone** | It is the one construct CDS owns end-to-end (2.4.7), and it is cross-family, so it exercises AF-4 immediately. Cost: it is also the construct that matures **no faster than its weakest constituent**, so it cannot reach a gate before VF-1, VF-5, and VF-3 do. |

**Recommendation.** **(b)**, with the family count reduced accordingly: mature
**VF-1 and VF-2** as separate families, and treat **VF-3, VF-5, and VF-6** as one
maturity group until an evidenced need separates them. This is the reading the
lifecycle document's own capacity section points at — *"prefer removing structure
that earns nothing over defending it"* — and it keeps AF-1 and AF-3 meaningful for
the families that actually carry consumer anchors. It also directly reduces the
OD-3 topology cost.

**Affected if decided.** The Visual Semantic Token Foundation · the Visual
Foundation Architecture family register · the Visual Foundation Governance and
Lifecycle document · the Decision Index.

**Track.** **Elevated** — shared semantics and accessibility obligations.

---

### OD-7 — Sequencing against CDS-WP-022: may a role carry a binding before contexts exist?

> **ANSWERED by DEC-S-135 (2026-09-05), effective at the Human-Maintainer commit
> `2cb244e889c1a6b5a278afb233995a0379b5d9ef`.** The recommendation below was adopted: **(d)** as the
> sequencing answer with **(b)** as the substantive rule. **No semantic visual role
> carries a default alias to a reference primitive before CDS-WP-022 decides the
> Theme and Context Mechanism**, and **CDS-WP-022 precedes context-sensitive value
> selection**. **(c)** was rejected: its re-evaluation obligation would need a named
> enforcing owner, and the Consumer Maintainer role is **unstaffed (FM-F-006)**, so
> it degrades to **(a)**.
>
> **One clarification this entry did not contain was added:** the rule gates
> **values and bindings, not structure**. Identifier grammar, scale ownership,
> role admission, family maturity governance and **source-set structural identity**
> are context-independent by **TC-1**, **TC-2**, **T-8**, **N-6** and **RB-1**, and
> are **not** blocked. **`CDS-WP-022 BEFORE VALUE SELECTION` does not mean
> `CDS-WP-022 BEFORE EVERY SOURCE-STRUCTURE OR IDENTITY ACTIVITY`.**
>
> **CDS-WP-022 becomes the recommended and sequenced Step-10 candidate only.**
> **SEQUENCED NEXT ≠ AUTHORIZED** — it remains `Planned`, not active, and not
> authorized, as do `CDS-WP-020A` and CDS-WP-021 … CDS-WP-053, and **no work package
> is currently authorized.**
>
> The alternatives, recommendation and impact statement below are preserved as the
> **preparation record**. They are not the decision; **DEC-S-135 is.**

**Proposition to decide.** Whether a semantic visual role may carry a **default**
alias to a reference primitive before **CDS-WP-022** decides the theme mechanism
and the token layering that light and dark imply — and, consequently, whether any
context-sensitive value may be selected in CDS-WP-020's successor work at all.

**Why existing authority is insufficient.** The
[Visual Foundation Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
leaves the mechanism open and assigns it to **CDS-WP-022**, together with *"the
token layering light and dark imply (CR-025)."* **T-2** requires that *"every
semantic role must resolve in every supported context"* — and **zero contexts are
supported today**, which makes the requirement vacuously satisfiable and therefore
untrustworthy as a guide. Whether a single default binding is a legitimate
starting state or a pre-emption of CDS-WP-022 is **not answered by any committed
source**.

**Alternatives.**

| # | Option | Consequence |
| --- | --- | --- |
| **a** | **Roles carry a single default binding now; contexts re-bind later** | Values can be selected as soon as OD-1 … OD-5 are decided. Cost: the default silently becomes "the light theme", and CDS-WP-022 inherits a decision it was supposed to make. TC-6 is violated in substance while satisfied in form. |
| **b** | **Roles carry no binding until CDS-WP-022 decides the mechanism** | CDS-WP-022 stays genuinely free. Cost: the semantic layer stays unresolvable, so no end-to-end value flow exists until CDS-WP-022 closes. |
| **c** | **Roles carry a binding declared as context-neutral, with a recorded, blocking obligation to re-evaluate every binding when CDS-WP-022 lands** | Values become selectable while the re-evaluation is a **registered obligation** rather than a hope. Cost: the obligation must actually block, or it is (a) with extra words. |
| **d** | **Reorder the roadmap: authorize CDS-WP-022 before value selection** | Removes the coupling entirely. Cost: a roadmap sequence change, which is a Human-Maintainer decision. |

**Recommendation.** **(d)**, with **(b)** as the position until it is decided.
The coupling is genuine and not a scheduling artifact: colour values and the light
and dark layering are the same decision seen from two sides, and option (a) is the
route by which a design system acquires an unstated default theme. **(c)** is only
admissible if the re-evaluation obligation is registered as a blocking gate with a
named owner — otherwise it is (a).

**Affected if decided.** The forward roadmap sequence · the Visual Semantic Token
Foundation (TC-6) · the Visual Foundation Theme Architecture · CDS-WP-021 and
CDS-WP-022 scope.

**Track.** **Elevated** — it determines whether an accessibility obligation can be
evaluated in every supported context.

## Items that are *not* open decisions

*(Recorded so that nothing is silently deferred)*

| Item | Disposition |
| --- | --- |
| **Typeface selection, font stack, and fallback chain** | **Already governed and already deferred.** The Typography Architecture requires **FP-1 … FP-8** — licence identity, provenance, offline and self-hosted viability, air-gap tolerance, a locally resolvable fallback chain, script coverage, distribution model, and the consequence of not selecting one — before any typeface may be made normative, as an **Elevated** change. **No new decision is needed to keep it deferred**, and *"a system-stack-only approach is an admissible outcome, not a failure."* CDS-WP-020 defines the typographic token **structure** and leaves the family unresolved, exactly as instructed. |
| **The theme mechanism** | **CDS-WP-022's**, unchanged. |
| **The responsive-range model and the Layer 3 / Layer 5 split** | **CDS-WP-021's**, unchanged. CR-004's registered Layer-5 mapping is **not altered**. |
| **The status-to-visual binding** | **CDS-WP-023's**, gated by CDS-WP-024 and CDS-WP-025, unchanged. |
| **Named extension points** | **CDS-WP-032's.** The set is **empty**, and no Product Profile can be approved. |
| **Motion values** | **CDS-WP-035's.** Deferred by default, unchanged. |
| **The icon system** | **CDS-WP-037's**, unchanged. |
| **Data-visualization encoding** | **CDS-WP-039's**, unchanged. |
| **The transformation tool** | Still genuinely open — Token and Theme Architecture question 3, unchanged by CDS-WP-020. |

## Recommended instruments

*(A recommendation to Nova and the Human Maintainer. **CDS-WP-020 creates none of
these**, and this section authorizes nothing.)*

| Instrument | Recommendation | Disposition — 2026-08-27 |
| --- | --- | --- |
| **A Decision block** covering OD-1 … OD-7 | **Recommended.** Each of the five work packages that made comparable first-of-their-kind normative choices registered one: **CDS-WP-011** (DEC-S-073 … DEC-S-082), **CDS-WP-012** (DEC-S-083 … DEC-S-092), **CDS-WP-013** (DEC-S-093 … DEC-S-104), **CDS-WP-014** (DEC-S-105 … DEC-S-114), and **CDS-WP-015** (DEC-S-115 … DEC-S-124) — see the *Decision types* table of the Decision Index. **CDS-WP-019 registered none, correctly, because it made no new normative choice.** Numbering would begin at **DEC-S-128**; the register held **127**. | **PREPARED, under explicit Human-Maintainer authorization** — but **four** entries, not seven: **DEC-S-128** (colour representation), **DEC-S-129** (contrast evaluation authority — an item this register had **not** raised), **DEC-S-130** (`$type` admission) and **DEC-S-131** (source-set unit and maturity granularity). **OD-4 … OD-7 were deliberately not decided.** The prepared register held **131** against an effective **127**; that commit — `42a568d823de3388e45af62967546f13ad67eff6` — has since occurred, and the **effective** register holds **131**. |
| **One ADR** covering the profile-facing choices — OD-1, OD-2, and OD-3 | **Recommended**, numbered **ADR-0004**. These are the same class as ADR-0001 (source format), ADR-0002 (serialization), and ADR-0003 (validator stack): each changes what the machine-readable profile admits and what the validator enforces. | **PREPARED** as [ADR-0004](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md), covering **DEC-S-128, DEC-S-130 and DEC-S-131**. **DEC-S-129 is deliberately not an architecture dependency of it.** The prepared ADR range was **ADR-0001 … ADR-0004** against an effective **ADR-0001 … ADR-0003**; since the integration commit `42a568d823de3388e45af62967546f13ad67eff6` the **effective** range is **ADR-0001 … ADR-0004**. |
| **A new risk entry** | **Not recommended.** The risk surface of CDS-WP-020 as executed is already carried by **RISK-003**, **RISK-021**, **RISK-026**, **RISK-029**, **RISK-031**, **RISK-040**, **RISK-061**, **RISK-074**, **RISK-087**, and **RISK-091**. Registering a duplicate would add ceremony that produces no decision — which RISK-040 exists to prevent. | **NOT CREATED**, and the recommendation is upheld. **`RISK-099` was explicitly assessed and is not required**: the normative OKLCH-to-sRGB accessibility-path conversion architecture that would have created a new exposure was **rejected** by DEC-S-128, so the exposure does not arise. The register stays at **98**, and **no risk was accepted, closed, or re-scored**. |

**No instrument above was created by Claude on its own authority.** Each was
prepared only under an explicit, separate Human-Maintainer authorization, and **a
Decision Index entry is a Human-Maintainer instrument**: the four Decisions and
ADR-0004 became effective only at the Human-Maintainer exact-byte integration
commit `42a568d823de3388e45af62967546f13ad67eff6`, which followed a Fresh
Independent Review and Nova integration adjudication. **A review PASS is not a
commit, and a Nova recommendation is not an approval.**

### Instruments prepared by the CDS Step-9 Decision Integration Pass — 2026-09-05

*(Prepared under an explicit Human-Maintainer authorization given on 2026-09-05.
**All are effective**, at the Human-Maintainer exact integration commit
`2cb244e889c1a6b5a278afb233995a0379b5d9ef` of the reviewed object.)*

| Instrument | Covers | Disposition |
| --- | --- | --- |
| **DEC-S-132** — Visual Identifier Grammar and the Two Identity Spaces | **OD-4**, and the **OD-3 concrete-root residual** | **PREPARED.** Architecture record: **ADR-0005**. |
| **DEC-S-133** — Per-Scale Topology Under the Common Scale Contract | **OD-5**, partially | **PREPARED.** **No ADR** — it applies ST-1 … ST-7 and changes nothing the profile admits or the validator enforces. |
| **DEC-S-134** — Visual Role Admission Rule | **OD-6A**, policy only | **PREPARED.** **No ADR** — a semantic and accessibility-obligation decision, on the DEC-S-129 precedent. |
| **DEC-S-135** — Theme Sequencing Before Context-Sensitive Value Selection | **OD-7** | **PREPARED.** **No ADR** — a sequencing and authority decision. |
| **ADR-0005** — Visual Identifier Grammar and Identity Spaces | **DEC-S-132 only** | **PREPARED.** **DEC-S-133, DEC-S-134 and DEC-S-135 are deliberately not architecture dependencies of it.** |
| **A new Decision for OD-6B** | — | **NOT CREATED, and not required.** OD-6B is answered by the existing artifact-family model and AF-1, AF-3 and AF-4. Creating one would be ceremony that produces no decision (**RISK-040**) and a governance abstraction created to reduce maintainer load. |
| **A new risk entry** | — | **NOT CREATED, and not required.** The surface is carried by **RISK-003**, **RISK-010**, **RISK-021**, **RISK-026**, **RISK-028**, **RISK-029**, **RISK-031**, **RISK-040**, **RISK-061** and **RISK-087**. **No `RISK-099`**; the register stays at **98**, with no risk accepted, closed, or re-scored. **RISK-092** is scoped to *status* token paths and its mechanism generalizes but its text does not — if explicit coverage is wanted, the instrument is **widening RISK-092**, a Human-Maintainer act, never a near-duplicate. |

**The effective register holds 135 decisions and 5 ADRs**, at the integration
commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`. **No `DEC-S-136`,
no `ADR-0006`, and no `RISK-099`.**

## Related documents

- [Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md)
- [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
- [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
- [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Colour Architecture](../architecture/VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
- [Visual Foundation Typography Architecture](../architecture/VISUAL_FOUNDATION_TYPOGRAPHY_ARCHITECTURE.md)
- [Visual Foundation Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
- [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
- [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md)
- [Machine-Readable Source Model](../architecture/MACHINE_READABLE_SOURCE_MODEL.md)
- [Post-Candidate Development Roadmap](POST_CANDIDATE_DEVELOPMENT_ROADMAP.md)
- [Decision Index](../decisions/DECISION_INDEX.md) · [Risk Register](../risks/RISK_REGISTER.md)
