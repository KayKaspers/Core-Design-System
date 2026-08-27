# Visual Token Value Selection Rules

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-020 — Reference and Semantic Token Foundation
- **Date:** 2026-08-26
- **Amended by:** CDS-WP-020 (Decision Integration Pass), 2026-08-27 — the
  prerequisite-state subsection under VP-1 … VP-7, and the **VE-1** evaluation
  authority, to apply **DEC-S-128**, **DEC-S-129**, **DEC-S-130** and
  **DEC-S-131**. **Those amendments are `PROPOSED / AUTHORIZED FOR INTEGRATION` and
  NOT YET EFFECTIVE** until the Human-Maintainer exact-byte integration commit.
  **No threshold is restated or invented, no value is selected, and VP-1 … VP-7,
  VE-1 … VE-12, IG-1 … IG-10, VD-1 … VD-8, VA-1 … VA-10 and VS-1 … VS-6 are
  otherwise unchanged.**
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for how a visual value may be selected** — the discipline
  every future value must satisfy before it may enter CDS. It **selects no value**.
- **Maturity:** **`Proposed`** — this document promotes nothing and grants no
  maturity to any artifact (DEC-S-036).

## Purpose and boundary

The
[Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md)
defines what a value *is*; the
[Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
defines what a value is *for*. This document defines **how a value may be chosen
at all** — the evaluation a proposal must survive, the record it must leave, the
grounds that are inadmissible, and the lifecycle it enters.

**It selects no value.** No colour, no colour space, no palette, no typeface, no
size, no spacing step, no radius, no stroke width, no shadow, no opacity level, no
elevation step, no motion value, and no breakpoint. It resolves no open decision.

**It introduces no governance rule.** Every rule below applies the
[Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md), the
[Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md), the
[Versioning, Compatibility and Deprecation Policy](VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md),
the
[Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md),
and the CDS-WP-019 visual foundation documents. On conflict, **those sources win**
and this document is corrected.

## The rule this document exists to enforce

> **No visual value enters CDS without a recorded reason that someone else can
> disagree with.**

A value chosen by taste is not reviewable, not defensible under change, and not
distinguishable from a value chosen by accident. Once it is consumed, it acquires
authority it was never granted — and **authority is granted, never acquired**
(DEC-S-033).

This is not a preference for documentation. It is the only mechanism by which
**RISK-003** (premature design decisions) is controlled, and the register's own
mitigation direction for RISK-003 requires exactly this: *maintain an explicit
list of intentionally open decisions, and treat any premature decision as a
reportable deviation.*

## Prerequisites before any value may be selected

*(Normative — a gate, not a checklist)*

**No value in a family may be selected until all of the following hold for that
family.** A value proposed while any of them is open is a premature decision and a
**reportable deviation**.

| # | Prerequisite |
| --- | --- |
| **VP-1** | The family's **reference and semantic constructs are defined** — the two foundation documents above apply to it. |
| **VP-2** | The family's **representation is decided**: its admitted `$type`, and for colour its colour space and encoding. |
| **VP-3** | The family's **scale topology is decided**, where the family holds an ordered set — base, progression rule, step count, and extension behaviour (ST-1 … ST-7). |
| **VP-4** | The family's **identifier grammar is decided**, so that a value has somewhere to live that will not be renamed (DEC-S-082). |
| **VP-5** | The **source-set identity and topology** the value belongs to is decided, with an immutable source revision. |
| **VP-6** | Every role the value will serve **declares its obligations** (SR-1 … SR-12), so the value can be evaluated against something. |
| **VP-7** | The **decision is authorized** — an explicit Nova prompt and Human-Maintainer authorization for the work package that makes it. |

### Prerequisite state after the 2026-08-27 Decision Integration Pass

*(**PROPOSED / AUTHORIZED FOR INTEGRATION — NOT YET EFFECTIVE** until the
Human-Maintainer exact-byte integration commit)*

| Prerequisite | State | Basis |
| --- | --- | --- |
| **VP-2** | **Satisfied** for the families expressible in `color`, `dimension` and `number`, and for colour representation. **Not satisfied** for typeface and weight identity, or for anything needing a composite type. | **DEC-S-128**, **DEC-S-130** |
| **VP-3** | **UNSATISFIED for every family.** No scale topology is decided. | **OD-5**, open |
| **VP-4** | **UNSATISFIED for every family.** No concrete identifier grammar is decided, and **no identifier exists**. | **OD-4**, open |
| **VP-5** | **UNSATISFIED for every family.** The **unit, topology and maturity granularity** are decided, but **no concrete source-set identity and no source revision exists**. | **DEC-S-131** decides the rule; the instance does not exist |

> **Three decisions do not complete the value system.** **VP-3, VP-4 and VP-5 fail
> for every visual family**, so **no visual value may be selected**, and a value
> proposed while any prerequisite is open remains a premature decision and a
> **reportable deviation**. The remaining choices are recorded, with alternatives
> and impact, in the
> [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
> register — **OD-4, OD-5, OD-6 and OD-7 are open**, together with three recorded
> residuals under OD-1, OD-2 and OD-3.

## The evaluation

*(Normative — every proposed value or scale is evaluated against all twelve. A
criterion that does not apply is recorded as **not applicable with a reason**,
never left blank.)*

| # | Criterion | What the record must show |
| --- | --- | --- |
| **VE-1** | **Accessibility** | Which obligations the value bears on, and how it is measured. For a contrast-sensitive role: the **pair**, not the value alone (CR-2, CR-3, VF-I-8). For a dimension: the target-size floor it must not undercut (2.5.8). |
| **VE-2** | **Readability and legibility** | Whether the value serves continuous reading, dense operational scanning, distance viewing, or none of them — these are different systems and one value rarely serves all. |
| **VE-3** | **Consistency** | How the value relates to the rest of its scale and to sibling families, and whether it introduces an exception to a stated progression rule. |
| **VE-4** | **Scalability** | Whether the value survives extension of its scale without renumbering (ST-3), and what happens at the ends of the range. |
| **VE-5** | **Technology neutrality** | That no CSS feature, layout engine, framework, platform primitive, or design tool is presupposed (DEC-S-032, DEC-S-004, PN-4). |
| **VE-6** | **Print and export behaviour** | What the value becomes when paginated, printed, converted to greyscale, or exported — and what is declared lost (D-1 … D-6, VF-I-11). |
| **VE-7** | **Context compatibility** | That the value does not presuppose a context count or a context set, and that its role remains resolvable however CDS-WP-022 decides (TC-1 … TC-7). |
| **VE-8** | **Offline and deterministic computability** | That the value and any derivation of it is computable locally, with no external service or registry (DEC-S-030, DEC-S-080). |
| **VE-9** | **Localization** | That the value tolerates German and English text length, and does not architecturally exclude further languages or bidirectional content (CR-023, baseline 8.3 … 8.6). |
| **VE-10** | **Product neutrality** | That the value expresses no product, consumer, customer, or brand identity, and was not selected because one consumer asked (PN-2, non-goal 11). |
| **VE-11** | **Channel adaptability** | Which of the registered channels can carry it, which transform it, and which cannot — with the limitation declared rather than discovered (DEC-S-029). |
| **VE-12** | **The cost of not choosing** | What happens if the value is **not** selected. A system-stack-only or deliberately-absent outcome is an **admissible result, not a failure** (FP-8, generalized). |

### VE-1 is a pair evaluation, never a value evaluation

**A colour role is never "accessible" on its own.** Contrast is a property of a
pair, in a context, in a channel. A record that states a single value's
"accessibility" has evaluated nothing, and it is the shape in which unfounded
accessibility confidence enters a design system.

The obligation is whatever the cited WCAG criterion itself requires. **CDS
restates no normative criterion text and invents no additional threshold**
(Accessibility Requirements Baseline).

**Evaluation authority** *(**DEC-S-129**, 2026-08-27 — **PROPOSED / AUTHORIZED FOR
INTEGRATION, NOT YET EFFECTIVE**)*: the baseline is **WCAG 2.2** — not `WCAG 2.x`,
not `latest` — and the method is the contrast-ratio method those criteria
themselves require. **Pass and fail are compared at full available precision, with
no rounding before comparison**; presentation rounding is a formatting artifact and
cannot change the outcome. **Additional methods, including APCA, may be calculated
and recorded as informational or experimental analysis only** — calculating one
grants it no normative authority, satisfies no CDS obligation, and supports no
claim. **An automated contrast calculation is not accessibility evidence and grants
no AE level** (DEC-S-053, EV-1).

## Inadmissible grounds

*(Normative — a value selected on any of these grounds is rejected, regardless of
how good the value is)*

| # | Inadmissible ground | Why |
| --- | --- | --- |
| **IG-1** | **Taste alone**, or "it looks right" | Not reviewable, not defensible, and indistinguishable from accident. |
| **IG-2** | **Imitation of another design system** | A benchmark records what others do; it evidences nothing about CDS's registered consumers or channels (RISK-010, research is never normative). |
| **IG-3** | **A consumer asked** | A consumer-specific need does not become CDS Core because a consumer asked. Classification precedes design (Requirement classification model). |
| **IG-4** | **A tool's default** | A design tool is never the source of truth (DEC-S-004, invariant 4), and a default is not a decision. |
| **IG-5** | **A generated artifact contains it** | A generated artifact is never normative and never stands against its source (DEC-S-022, DEC-S-031, VF-I-12). |
| **IG-6** | **An example, illustration, or fixture uses it** | An example is never normative (VF-I-13); fixtures are synthetic, test-only, and never real design values (DEC-S-087). |
| **IG-7** | **A validator accepts it** | A validator pass is metadata coherence, never authority (VR-4, DEC-S-053). |
| **IG-8** | **It was there before the policy** | Nothing acquires standing by having existed first (*No retrospective maturity*, DEC-S-036). |
| **IG-9** | **Schedule pressure, maintenance burden, or embarrassment** | These are not grounds for a normative choice, and they are explicitly not emergency grounds either. |
| **IG-10** | **It makes a failing check pass** | Weakening a test, a fixture, or an obligation to accommodate a value inverts the direction of authority. |

## The value selection record

*(Normative — what must be recorded **with** the value, not merely in a report)*

| # | Every selected value or scale records |
| --- | --- |
| **VD-1** | The **proposition** — the exact value or scale, in its declared representation |
| **VD-2** | The **roles it serves**, and the obligations those roles declared (SR-1 … SR-12) |
| **VD-3** | The **VE-1 … VE-12 evaluation**, with every non-applicable criterion reasoned |
| **VD-4** | The **alternatives considered** and why each was not selected |
| **VD-5** | The **source revision** it enters at, and its maturity and approval state |
| **VD-6** | Its **compatibility impact**, and its **migration reference** if it replaces something |
| **VD-7** | Its **known limitations**, stated honestly, including what has **not** been evaluated |
| **VD-8** | The **authorization** under which it was selected — the work package and the approving decision |

**VD-7 is the entry that decays fastest and matters most.** `Not tested` must
remain available and be used; **`Not yet assessed` must never be read as
compatible** (Visual Foundation Governance and Lifecycle), and rounding it up
because nothing broke is exactly RISK-032.

## Accessibility constraints on selection

*(Normative — an application of the accessibility sources; **no requirement is
introduced and no threshold is restated**)*

The visual foundation carries **14** Layer-3 WCAG 2.2 A/AA criteria, and **all
five criteria CDS owns without the consumer** are among them — 1.3.3, 1.4.1,
1.4.5, 2.3.1, and 2.4.7. Value selection therefore carries obligations that no
consumer can share.

| # | Constraint |
| --- | --- |
| **VA-1** | **A value that participates in meaning requires a non-visual carrier to exist first.** The carrier is primary; the visual value is redundant. Removing all visual encoding must remove **no** meaning (NC-1, NC-2, VF-I-5). |
| **VA-2** | **A contrast obligation is evaluated as a pair in a context and a channel**, and must hold in **every** supported context (TC-3). |
| **VA-3** | **Reduced contrast alone may never encode a non-interactive or read-only state** (IS-2). |
| **VA-4** | **A dimension may never undercut a target-size obligation**, and density operates above that floor, never through it (2.5.8, Spatial Architecture *Density*). |
| **VA-5** | **A typographic value must tolerate user resize, magnification, text-spacing overrides, and reflow** (TA-2 … TA-4). |
| **VA-6** | **A value must survive greyscale, monochrome print, and forced colours**, or its limitation is declared (D-4, baseline 3.5). |
| **VA-7** | **No value may weaken the focus indicator**, in any context, profile, or channel. Focus visibility has **no permitted mechanism of removal** (F-1 … F-8, DEC-S-059). |
| **VA-8** | **Accessibility is not waivable through an ordinary exception** (DEC-S-059). A value that cannot meet an obligation does not get an exception; it does not get selected. |
| **VA-9** | **An automated check is never sufficient** (DEC-S-053), and **absence of a failure is not evidence of success** (EV-4). |
| **VA-10** | **No accessibility claim results from selecting a value.** A target is not a claim (DEC-S-050), and no claim of any level is valid today. |

## Lifecycle and maturity disposition

*(Normative current-state statement — an application of the
[Visual Foundation Governance and Lifecycle](VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md);
**it grants no maturity**)*

| Item | State after CDS-WP-020 |
| --- | --- |
| Visual foundation source sets in existence | **0** |
| Visual foundation families at `Candidate` | **0** |
| Visual foundation families at `Stable` | **0** |
| Maturity of VF-1 … VF-9 | **`Proposed`** — unchanged |
| Maturity of the CDS-WP-020 documents | **`Proposed`** |
| Candidate artifact families in all of CDS | **1** — the channel-independent Semantic Status Layer-3 source/contract family, **not a visual family** |
| Stable artifacts in all of CDS | **0** |
| Compatibility axes for visual families | **`Not yet assessed`** throughout |
| Releases · tags · publication | **None** · **0** · **`Private Development`** |

**CDS-WP-020 promotes nothing.** A visual family reaches `Exploratory` or
`Experimental` only when a draft solution with known limitations exists — which
requires values, which requires the prerequisites above. **No visual family can
reach Candidate today, because no visual artifact exists to evidence**, and none
can reach Stable at all: **AE-2 and AE-3 exist nowhere in CDS**, no baseline
environment has ever been exercised, and no consumer validation exists.

**Maturity is never inherited** (AF-1), **a family may mature at its own pace**
(AF-3), **a cross-family construct matures no faster than its weakest
constituent** (AF-4), and **an architecture document is not the artifact** (AF-5).

## Validation strategy

*(Normative as a **strategy statement**. **CDS-WP-020 changes no validator, adds
no schema, and introduces no diagnostic.**)*

| Layer | What it must cover for visual values |
| --- | --- |
| **V1 — Syntax** | Strict JSON, UTF-8, duplicate-member prohibition, file identity, no network references |
| **V2 — DTCG** | Group and token shape, `$value` / `$type` / `$description` / `$extensions`, reference resolution, type compatibility, resolver semantics, no preview features |
| **V3 — CDS profile** | Naming profile, declared layer, manifest and document identity agreement, dependency graph, Product-Profile bounds, maturity and approval metadata, local cross-file binding |
| **V4 — Semantic and governance** | Downward layer direction, non-visual meaning carriers, declared contrast obligations and pairings, accessibility relevance, Decision and Requirement traceability, provenance completeness, approved overrides only |

The concrete detections are listed in the two foundation documents as
**requirements on CDS-WP-024**. They are not implemented, and implementing them is
not authorized here.

| # | Rule |
| --- | --- |
| **VS-1** | **A pass at one layer proves nothing about the next** (VR-1 of the lifecycle document). |
| **VS-2** | A `Fail` or `Blocked` **stops** later layers, which are recorded **`Not assessed`** — never assumed passed. |
| **VS-3** | **No numeric or aggregate score.** A blocked layer stays individually visible. |
| **VS-4** | **Metadata coherence is not maturity authority.** |
| **VS-5** | **The validation contract wins** over any implementation that diverges from it (DEC-S-102). |
| **VS-6** | **The half a validator cannot reach is the accessibility half.** Perceivability, focus visibility in practice, reflow, magnification, target size, and print degradation require **rendering and interaction evidence** — CDS-WP-031's, and it does not exist (EV-7). |

## Change classification for value work

*(Normative — an application of DEC-S-033)*

| Change | Track |
| --- | --- |
| Correcting a typo or a broken link in a value record | **Standard** |
| **Adding a reference primitive that no role yet binds** | **Standard** |
| **Selecting a colour space, an admitted `$type` set, or a scale topology** | **Elevated** — a CDS Token Format Profile or contract change (DEC-S-082) |
| **Adding or changing a semantic role, its contrast obligation, or its pairing set** | **Elevated** |
| **Changing a value a role already resolves to** | **Elevated** where it bears on an accessibility obligation, a pairing, or a matured family |
| **Selecting a typeface, icon set, or any external asset** | **Elevated** — licensing, provenance, and distribution triggers |
| **Naming an extension point** | **Elevated** |
| **Any change to a family that has reached Candidate or Stable** | **Elevated** |

> **A change that looks Standard but touches an Elevated trigger is Elevated.**
> Ceremony scales; obligations do not. Authority boundaries, traceability,
> evidence, human approval, and fail-closed behaviour hold in both tracks.

## Escalation

Escalate — do not resolve locally — when a value would require a normative choice
no committed source has made; when two normative sources disagree; when a value
cannot satisfy an accessibility obligation; when a role would approve its own
value; when an override would weaken accessibility or status truth; or when
evidence is missing, contradictory, or unreviewable.

Path: **Claude records and reports → Nova reviews and recommends → Human
Maintainer decides.** While an escalation is open, the affected state is **not
releasable and not distributable**.

## Related documents

- [Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md)
- [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
- [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
- [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Accessibility Mapping](VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md)
- [Visual Foundation Governance and Lifecycle](VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
- [Visual Foundation Brand and Product Profile Boundary](VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md)
- [Visual Foundation Channel Mapping](VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
- [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md)
- [Versioning, Compatibility and Deprecation Policy](VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md)
- [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [Accessibility Requirements Baseline](ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [WCAG 2.2 AA Applicability Matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md)
- [Machine-Readable Validation Contract](../architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)
