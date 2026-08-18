# Semantic Status Foundation Contract

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-014 — Semantic Status Foundation Contract and First
  Candidate Plan
- **Date:** 2026-07-17
- **Status:** **Normative** for CDS status semantics, **pending Human-Maintainer
  commit**. Maturity: **Experimental** — this contract holds **no Candidate or
  Stable status** (DEC-S-114) and makes no conformance, accessibility, or adoption
  claim.
- **Update (CDS-WP-015):** the machine-readable Semantic Status Source Set
  **`semantic/status`** is implemented (Experimental; 25 non-visual tokens with
  manifest and resolver under `tokens/semantic/status/`; DEC-S-115…117) and
  validated by the executed 24-case harness — **executor-produced evidence,
  independently unreviewed; the Candidate gate remains open** (DEC-S-121,
  DEC-S-122).

## Purpose and authority

This contract is the first concrete CDS design foundation: the
**channel-independent semantic contract for status meaning**. It answers the
taxonomy questions deliberately left open by the architecture
([Evidence, Traceability and Status Semantics](../architecture/EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md),
"Unresolved taxonomy decisions" 1–5) and operationalizes the architectural
invariant (DEC-S-028, architecture invariants 7–9):

> **Unknown, stale, unavailable, incomplete, or unverified information must not
> be represented as healthy, successful, current, or verified.**

It is a **meaning contract, not a visual specification**. It defines what status
values mean, how they combine, and what every representation must preserve. It
selects no colour, icon, typography, spacing, motion value, component, or theme.

Authority: this document is a **normative human-readable source** (artifact
class 1, DEC-S-022). It is subordinate to
[Concept and Scope](../governance/CONCEPT_AND_SCOPE.md) and the
[Design System Architecture](../architecture/DESIGN_SYSTEM_ARCHITECTURE.md); on
conflict, fail closed and escalate (DEC-S-023, DEC-S-034).

## Declared scope

- The **five status axes** and their fixed initial vocabulary
  ([Status Axis Vocabulary](STATUS_AXIS_VOCABULARY.md)) — 5 axes × 5 values = 25
  normative axis values (DEC-S-105, DEC-S-106).
- The **complete status object** and its composition/conflict rules
  ([Composition and Conflict Rules](STATUS_COMPOSITION_AND_CONFLICT_RULES.md)).
- The **communication, accessibility, and localization obligations**
  ([Communication and Accessibility Contract](STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md)).
- The **semantic token role contract** for the future machine-readable source set
  ([Semantic Status Token Contract](SEMANTIC_STATUS_TOKEN_CONTRACT.md)) — roles
  only, no values.
- DE/EN **semantic parity** for status meaning (labels themselves are localized
  later).

## Non-scope

This work package and this contract define **none** of the following: concrete
colours, typography, spacing, sizes, icons, motion values, visual themes, real
token source files, token names as shipped identifiers, components, Product
Profiles, CoreOps or any consumer integration, mobile/non-web implementations,
Candidate or Stable status, and any conformance or adoption claim. Final UI
copy is not fixed here; wording in this contract states *meaning obligations*,
not shipped strings.

## The five-axis model

*(Normative — DEC-S-105. Derived from DEC-S-028 and the five architecture
axes; independently confirmed by consumer evidence CR-006/CR-007.)*

| # | Axis | Technical ID | Answers |
| --- | --- | --- | --- |
| 1 | Operational Condition | `condition` | What state is the subject in? |
| 2 | Severity and Impact | `severity` | How much does it matter in the declared scope? |
| 3 | Knowledge Confidence | `confidence` | How sure are we of what we state? |
| 4 | Freshness | `freshness` | How current is the observation or assessment? |
| 5 | Evidence Availability | `evidence` | Can we show why we believe it? |

**No axis substitutes for another.** Each carries exactly the five values
defined in the [Status Axis Vocabulary](STATUS_AXIS_VOCABULARY.md);
**`unknown` is an explicit value on every axis and never an omitted default**
(DEC-S-106).

## The complete status object

A CDS-conformant status statement is complete only with all of the following
fields (detail and conflict rules in
[Composition and Conflict Rules](STATUS_COMPOSITION_AND_CONFLICT_RULES.md)):

subject identity · declared scope · `condition` · `severity` · `confidence` ·
`freshness` · `evidence` · observed-or-assessed time · source or evidence
identity · known limitations · rationale where required.

A missing mandatory axis is **not** an implicit positive value — it fails
closed.

## The ten invariants

*(Normative — each must hold in every representation, mapping, and output.)*

| # | Invariant |
| --- | --- |
| 1 | The five axes remain independent; none substitutes for or implies another (DEC-S-105). |
| 2 | There is no normative aggregated health score; summaries prioritize disclosure but never replace the axes (DEC-S-108). |
| 3 | `unknown` is never represented as `nominal`, `none`, `verified`, `current`, or `available` (DEC-S-107). |
| 4 | `stale` or `expired` freshness is never communicated as `current`. |
| 5 | `unverified` confidence is never represented as `verified`. |
| 6 | `partial`, `unavailable`, or `unknown` evidence is never hidden from a representation that asserts the status. |
| 7 | Colour, icon, position, shape, or motion is never the sole carrier of status meaning (DEC-S-111, CR-006). |
| 8 | Technical identifiers are stable and language-neutral; localized display labels are separate and preserve the normative meaning (DEC-S-110). |
| 9 | Channel and Product-Profile mappings preserve the semantic distinction and truthfulness of every axis (DEC-S-112, invariant 13, invariant 10). |
| 10 | Consumer Extensions must not weaken the unknown- and truthfulness-rules of any axis (DEC-S-112). |

## Target, evidence, and claim boundary

This contract is a **target and meaning definition — not evidence and not a
claim** (DEC-S-050 applied to status semantics). Nothing here asserts that any
implementation communicates status accessibly or truthfully; that requires
artifact-bound evidence under the
[Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
and the Candidate gates (DEC-S-114). **This contract is not that evidence**, and the
current admitted evidence state is governed externally: the channel-independent
Semantic Status Layer-3 source/contract family holds admitted **AE-1** structural and
automated evidence for its source scope only — see the
[Semantic Status AE-1 Admission Record](../governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md).
That admission creates **no Candidate status and no claim**. No conformance,
accessibility, certification, or adoption claim exists or is implied.

## Channel boundary

Meaning is constant across channels; presentation is not (DEC-S-029). Every
channel — including non-interactive channels such as documents printed in
greyscale — must be able to preserve all five axes and their qualifiers through
**text and accessible semantics**. A channel that cannot preserve a
distinction may not ship a status representation that drops it silently; the
limitation must be declared (invariant 6).

## Product Profile and Consumer Extension boundary

Product Profiles may adjust **approved extension points only** and must never
rename, merge, remap, or reweight status values in ways that change meaning,
weaken accessibility, or distort truth (DEC-S-025, invariant 10, RISK-088).
Consumer Extensions may add product-local *domain* states outside CDS
semantics, but must not repurpose CDS axis values, must not map a CDS
`unknown`/`stale`/`unverified` onto a positive local state, and must keep CDS
technical IDs traceable (DEC-S-112). Where CDS status semantics end and
consumer domain semantics begin remains an explicitly open boundary question
(CR-035) — an open point, not a licence to blur.

## Maturity and approval state

- Maturity: **Experimental** (DEC-S-035). Approval: **Unapproved** — pending
  Nova review and Human-Maintainer commit.
- The planned promotion path is defined in the
  [First Semantic Status Candidate Plan](../roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md);
  **this work package promotes nothing** (DEC-S-113, DEC-S-114).

## Change control

Changes to axes, values, invariants, or combination rules are **Elevated**
(DEC-S-033): they touch shared semantics, accessibility obligations, and future
compatibility. They require impact and migration assessment (a value rename is
a migration event, DEC-S-082), re-verification of dependent vocabulary/
composition/communication documents and any future fixtures and source sets,
Nova review, and Human-Maintainer approval. The vocabulary is **fixed at five
values per axis** for this initial contract; extending it is a governed change,
not an authoring convenience.

## Related documents

- [Status Axis Vocabulary](STATUS_AXIS_VOCABULARY.md)
- [Status Composition and Conflict Rules](STATUS_COMPOSITION_AND_CONFLICT_RULES.md)
- [Status Communication and Accessibility Contract](STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md)
- [Semantic Status Token Contract](SEMANTIC_STATUS_TOKEN_CONTRACT.md)
- [First Semantic Status Candidate Plan](../roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md)
- [Semantic Status Source Set](../../tokens/semantic/status/semantic-status.tokens.json) ·
  [Manifest](../../tokens/semantic/status/semantic-status.source-set.json) ·
  [Resolver](../../tokens/semantic/status/semantic-status.resolver.json)
- [Semantic Status Terminology DE/EN](SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md)
- [Evidence, Traceability and Status Semantics](../architecture/EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md)
- [Accessibility Requirements Baseline](../governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [Token and Theme Architecture](../architecture/TOKEN_AND_THEME_ARCHITECTURE.md)
