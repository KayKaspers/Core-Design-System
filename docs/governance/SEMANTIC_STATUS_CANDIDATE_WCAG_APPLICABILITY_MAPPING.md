# Semantic Status Candidate — WCAG Applicability Mapping

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Accessibility Gate Remediation
- **Date:** 2026-08-17
- **Scope:** the **Semantic Status Candidate source and contract family** only —
  the four foundations documents, the DE/EN terminology mapping, and the
  `semantic/status` source set with its manifest and resolver.
- **Status:** **Scope-bound applicability mapping — NOT normative, NOT an
  evaluation, NOT evidence.** The normative applicability source remains the
  [WCAG 2.2 AA Applicability Matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md), which
  this document **derives from and does not change**.

## What this document is

Requirement 1 of the [Candidate accessibility gate](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md#candidate-accessibility-gate):
a WCAG applicability mapping **for the artifact actually being proposed**, rather
than for CDS in general.

## What this document is not

> **Target is not evidence. Mapping is not evidence. Not applicable is not
> passed.**

- **No WCAG evaluation.** Nothing has been tested against any success criterion.
- **No WCAG conformance result**, at any level, for any scope.
- **No accessibility claim.** No claim is valid today, for anyone, including CDS.
- **No AE by existence.** Writing a row creates no evidence; the evidence a row
  points to is named explicitly or the row says there is none.
- **No change to the global matrix.** Where this mapping and the global matrix
  disagree, the **global matrix wins** and this document is corrected.

## The artifact being mapped

A **channel-independent Layer-3 semantic source and contract family**. It defines
what status values mean and what every representation must preserve. It ships:

- no rendered output, no interactive surface, no component;
- no colour, typography, spacing, size, icon, shape, or motion value;
- no page, no focus, no keyboard interaction, no live region;
- no media of any kind.

Per **DEC-S-125**, this family is assessed under its **source-level** Candidate
accessibility gate and is **not** assigned an artificial channel. Every later
channel representation is a separate artifact under its own Channel Accessibility
Profile with its own evidence (DEC-S-058), and **evidence transfers in neither
direction** (DEC-S-052).

## Classification vocabulary

*(Exactly one value per criterion.)*

| Classification | Meaning for this artifact family |
| --- | --- |
| `DIRECT_SOURCE_CONTRACT_APPLICABILITY` | The information the criterion protects is carried — or would be destroyed — **in the source or contract itself**. A source-level obligation exists **now**, and AE-1 evidence for that part is required now. The perception/operation part, where one exists, is deferred. |
| `REPRESENTATION_TRIGGERED` | The criterion concerns perceiving, operating, or presenting a rendered artifact. It **applies** to any future representation and is **not assessable** until one exists. Not applicable-by-opt-out. |
| `CONSUMER_OWNED` | The consumer owns the criterion for its product content, composition, page, site, or process. CDS cannot satisfy it however good the contract is. |
| `NOT_APPLICABLE_WITH_RATIONALE` | Genuinely does not apply, with a stated reason that is not "no implementation exists". |

**Missing implementation never makes a criterion `NOT_APPLICABLE`.** It makes it
`REPRESENTATION_TRIGGERED`, and it keeps its owner.

## Fields carried by every row

Every row in this document carries all nine required fields. Four are per-row
columns; five are stated **once per classification group** and hold **per row**
in that group — the same convention the
[terminology mapping](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md) uses
for its per-row review state.

| # | Field | Where it is stated |
| --- | --- | --- |
| 1 | Criterion (SC, title, level) | Per row |
| 2 | Source policy reference (global matrix policy status) | Per row |
| 3 | Candidate artifact relevance | Per row |
| 4 | Rationale | Per row |
| 5 | Owner | Per group |
| 6 | Current evidence applicability | Per group |
| 7 | Evidence required now | Per group |
| 8 | Evidence deferred until representation | Per group |
| 9 | Claim boundary | Per group |

---

## Group A — `DIRECT_SOURCE_CONTRACT_APPLICABILITY` (5 criteria)

**Owner:** CDS, for the source and contract layer only.
**Current evidence applicability:** AE-1 is applicable **now**; AE-2/AE-3/AE-4
are not, because there is nothing to operate and no product scope.
**Evidence required now:** the source-level structural properties named per row,
produced by the CDS-WP-016 evidence run and recorded in the
[AE-1 Evidence Record](../operations/SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md)
— independently reviewed **PASS** as clean-HEAD Evidence 002 and **admitted at
AE-1** (`AE1-CDS-WP016-SEMSTATUS-002`, source scope only). **Admitted structural
evidence is not a criterion pass**; see the claim boundary below.
**Evidence deferred until representation:** all perception, operation, and
assistive-technology exposure aspects; these require AE-2 and AE-3 under the
applicable Channel Accessibility Profile and are planned in the
[AE-2 Evidence Plan](SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md).
**Claim boundary:** none of these rows supports any statement that CDS meets the
criterion. A satisfied source-level obligation is a **precondition** for a
downstream representation to be able to meet it — never the meeting of it.

| SC | Title | Level | Global matrix policy status | Candidate artifact relevance | Rationale |
| --- | --- | --- | --- | --- | --- |
| 1.1.1 | Non-text Content | A | Shared CDS and consumer requirement | **High.** Every one of the 25 values must have a textual meaning that any future non-text carrier can be an equivalent of. Evidence now: 25/25 non-empty `$description` at the source (enforced by `CDS-V4-STATUS-DESCRIPTION`) and 25/25 DE and EN labels. | If a status value had no textual meaning in the source, no downstream representation could supply a correct text alternative for it. The source is where that information is either present or absent, so the obligation is directly assessable here. |
| 1.3.1 | Info and Relationships | A | Shared CDS and consumer requirement | **High.** The five axes are independent and none substitutes for another; the 25 values map 1:1 onto `status.<axis>.<value>`; no aggregate role exists. Evidence now: machine-verified axis/value completeness, path/value agreement, no aggregate and no visual role. | Structure and relationships originate here. A source that merged two axes, or that offered an aggregate health value, would make the criterion structurally unsatisfiable downstream no matter how the representation is built. |
| 1.3.3 | Sensory Characteristics | A | Normative CDS requirement | **High.** The contract forbids meaning carried by shape, position, or other sensory characteristic alone; the source carries no such role. Evidence now: the appearance-oriented-role check (`CDS-V4-STATUS-VISUAL-LEAKAGE`) and the negative visual-role fixture. | The prohibition is a property of the contract and the source vocabulary, not of a rendering. It is stated and machine-checked here. |
| 1.4.1 | Use of Color | A | Normative CDS requirement | **High.** Invariant 7: colour is never the sole carrier of status meaning. The source defines **no colour value and no colour role**. Evidence now: the same visual-leakage check, plus the text-first description rule. | Colour-only encoding is prevented at the source by refusing colour roles and requiring textual meaning. Whether an actual rendering respects that is a representation question. |
| 4.1.3 | Status Messages | AA | Shared CDS and consumer requirement | **High.** This is the criterion the whole Foundation exists to make satisfiable: `unknown` is explicit on every axis and never a positive default; `stale`/`expired` never read as `current`; `unverified` never reads as `verified`; material qualifiers travel with summaries. Evidence now: the 25/25 value-requirement coverage, 6/6 review-required and 8/8 fail-closed coverage. | The source-level half — that the distinctions exist and cannot be silently collapsed — is directly assessable and is what the CDS-WP-016 evidence run exercises. The other half, that a status change actually reaches assistive technology, is inherently representation-triggered and is **not** claimed here. |

---

## Group B — `REPRESENTATION_TRIGGERED` (30 criteria)

**Owner:** CDS for the future artifact's contract; **Consumer** for composition,
content, and runtime once one exists. Shared in the global-matrix sense.
**Current evidence applicability:** **none.** These criteria are **not
assessable** against a source that has no rendered or interactive surface. They
are **not** satisfied, **not** exempt, and **not** waived.
**Evidence required now:** **none.** Recording "not assessable" is the honest
state; producing AE-2 or AE-3 against a non-existent surface would be fabricated
evidence.
**Evidence deferred until representation:** AE-2 for all of them, plus AE-3
against A11Y-BL-001 for the assistive-technology-bearing ones, under the
applicable Channel Accessibility Profile — see the
[AE-2 Evidence Plan](SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md) and the
[Support Baseline Plan](SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md).
**Claim boundary:** no statement of any kind may be made about these criteria for
this artifact. `Not assessable` is reported as **not tested**, and **`not tested`
is never `passed`**.

| SC | Title | Level | Global matrix policy status | Candidate artifact relevance | Rationale |
| --- | --- | --- | --- | --- | --- |
| 1.3.2 | Meaningful Sequence | A | Shared | Indirect — the five-axis disclosure order becomes a reading-order question only when rendered. | No sequence exists in a source set; order is created by a representation. |
| 1.3.4 | Orientation | AA | Shared | Indirect — the contract locks no orientation. | Orientation is a rendering property. |
| 1.4.3 | Contrast (Minimum) | AA | Shared | Indirect — **no CDS colour value exists**; none is created by this Candidate. | Contrast requires colour values and a rendering; the Candidate deliberately has neither. |
| 1.4.4 | Resize Text | AA | Shared | Indirect — labels must tolerate length variation (flexible-label rule). | Resizing is a rendering behaviour. |
| 1.4.5 | Images of Text | AA | Normative CDS requirement | Indirect — the source contains no image. | The obligation binds future rendered documentation and UI, not a JSON source or a contract document. |
| 1.4.10 | Reflow | AA | Shared | Indirect — dense status displays are the known hard case. | Reflow needs a layout. |
| 1.4.11 | Non-text Contrast | AA | Shared | Indirect — no non-text status carrier exists. | No visual carrier is defined by this Candidate. |
| 1.4.12 | Text Spacing | AA | Shared | Indirect — flexible labels are contracted. | Spacing is a rendering behaviour. |
| 1.4.13 | Content on Hover or Focus | AA | Shared | Indirect — the contract already forbids hover as a sole carrier. | Hover and focus exist only in an interactive representation. |
| 2.1.1 | Keyboard | A | Shared | Indirect — the communication contract states the future keyboard obligation for status detail disclosure. | There is nothing to operate. |
| 2.1.2 | No Keyboard Trap | A | Shared | Indirect — same. | There is nothing to trap focus in. |
| 2.1.4 | Character Key Shortcuts | A | Shared | Indirect — CDS defines no shortcut. | No shortcut surface exists. |
| 2.2.2 | Pause, Stop, Hide | A | Shared | Indirect — live status updates must not interrupt uncontrollably. | Requires a live, updating representation. |
| 2.3.1 | Three Flashes or Below Threshold | A | Normative CDS requirement | Indirect — the source defines no motion value. | Flashing is a rendering behaviour; motion is contracted as redundant-only and defined nowhere here. |
| 2.4.3 | Focus Order | A | Shared | Indirect — drill-down from a summary to all five axes will need an order. | Requires focusable elements. |
| 2.4.6 | Headings and Labels | AA | Shared | Indirect — the DE/EN mapping supplies label **material**, not rendered labels. | Supplying wording is not placing a heading or a label in a rendering. |
| 2.4.7 | Focus Visible | AA | Normative CDS requirement | Indirect — a mandatory contract area for future components. | Requires focus. |
| 2.4.11 | Focus Not Obscured (Minimum) | AA | Shared | Indirect — overlays are the known hard case. | Requires focus and layering. |
| 2.5.1 | Pointer Gestures | A | Shared | Indirect. | Requires pointer interaction. |
| 2.5.2 | Pointer Cancellation | A | Shared | Indirect. | Requires pointer interaction. |
| 2.5.3 | Label in Name | A | Shared | Indirect — technical IDs are language-neutral and localized labels are separate, which is what makes accessible-name/visible-label agreement achievable later. | Requires an accessible name and a visible label, neither of which exists yet. |
| 2.5.4 | Motion Actuation | A | Shared | Indirect. | Requires device-motion interaction. |
| 2.5.7 | Dragging Movements | AA | Shared | Indirect. | Requires dragging interaction. |
| 2.5.8 | Target Size (Minimum) | AA | Shared | Indirect — **no CDS size value exists**. | Requires targets and size values; the Candidate creates neither. |
| 3.2.1 | On Focus | A | Shared | Indirect. | Requires focus. |
| 3.2.2 | On Input | A | Shared | Indirect. | Requires input. |
| 3.2.4 | Consistent Identification | AA | Shared | Indirect — stable technical IDs support consistency; composition decides it. | Requires repeated components across a product. |
| 3.3.1 | Error Identification | A | Shared | Indirect — fail-closed states must be communicated as system states, not user faults. | Requires an error presentation. |
| 3.3.2 | Labels or Instructions | A | Shared | Indirect. | Requires form controls. |
| 4.1.2 | Name, Role, Value | A | Shared | Indirect — the source supplies stable identifiers and the states a representation must expose. | Name, role, and value exist only in an accessibility tree produced by a rendering. |

---

## Group C — `CONSUMER_OWNED` (20 criteria)

**Owner:** the **Consumer Maintainer**, for the consumer's product content,
composition, page, site, or process (DEC-S-051, DEC-S-052).
**Current evidence applicability:** **none for CDS**, at any level. **No consumer
of the Semantic Status source exists** and none is authorized.
**Evidence required now:** **none.** CDS may not produce consumer evidence and
does not invent a consumer to produce it against.
**Evidence deferred until representation:** AE-4 in the consumer's declared
product scope, produced and owned by the consumer.
**Claim boundary:** CDS makes **no** statement about these criteria, and **using
CDS artifacts never makes a consumer product accessible** (DEC-S-052). A consumer
claim is the consumer's, bound to its own scope, revision, baseline, and
evidence.

| SC | Title | Level | Global matrix policy status | Candidate artifact relevance | Rationale |
| --- | --- | --- | --- | --- | --- |
| 1.2.1 | Audio-only and Video-only (Prerecorded) | A | Consumer-scope | None — the Candidate ships no media. | Media is consumer-owned; the artifact family contains none and defines no media contract. |
| 1.2.2 | Captions (Prerecorded) | A | Consumer-scope | None. | Consumer media only. |
| 1.2.3 | Audio Description or Media Alternative | A | Consumer-scope | None. | Consumer media only. |
| 1.2.4 | Captions (Live) | AA | Consumer-scope | None. | Consumer media only. |
| 1.2.5 | Audio Description (Prerecorded) | AA | Consumer-scope | None. | Consumer media only. |
| 1.3.5 | Identify Input Purpose | AA | Consumer-scope | None — status values are not form input purposes. | CDS cannot know a field's purpose. |
| 1.4.2 | Audio Control | A | Consumer-scope | None. | No CDS artifact plays audio. |
| 2.2.1 | Timing Adjustable | A | Shared | Low — status freshness is about the observation's age, not a session timer. | Timing behaviour is a product property. |
| 2.4.1 | Bypass Blocks | A | Shared | None at source scope. | A page-composition obligation. |
| 2.4.2 | Page Titled | A | Consumer-scope | None. | CDS cannot author product titles. |
| 2.4.4 | Link Purpose (In Context) | A | Consumer-scope | None. | Link text is consumer content. |
| 2.4.5 | Multiple Ways | AA | Consumer-scope | None. | A site-level obligation. |
| 3.1.1 | Language of Page | A | Consumer-scope | None — the consumer declares the page language. | CDS supplies DE/EN material; declaring a page's language is a product act. |
| 3.1.2 | Language of Parts | AA | Consumer-scope | Low — the 25/25 DE/EN mapping gives a consumer the material to mark parts correctly. | Marking actual language changes happens in consumer content. |
| 3.2.3 | Consistent Navigation | AA | Consumer-scope | None. | A site-level obligation across pages. |
| 3.2.6 | Consistent Help | A | Consumer-scope | None. | A product-level placement obligation. |
| 3.3.3 | Error Suggestion | AA | Shared | None at source scope — CDS cannot know domain semantics. | Suggestions are domain-specific and consumer-owned. |
| 3.3.4 | Error Prevention (Legal, Financial, Data) | AA | Consumer-scope | None — the consumer decides which actions are critical. | A process-level obligation. |
| 3.3.7 | Redundant Entry | A | Shared | None at source scope. | A process-design obligation. |
| 3.3.8 | Accessible Authentication (Minimum) | AA | Shared | None. | Authentication is consumer-owned. |

---

## Group D — `NOT_APPLICABLE_WITH_RATIONALE` (1 row, historical)

**Owner:** none. **Current evidence applicability:** none. **Evidence required
now:** none. **Evidence deferred:** none. **Claim boundary:** a not-applicable
row is **not a passed row** and supports no statement whatsoever.

| SC | Title | Level | Global matrix policy status | Candidate artifact relevance | Rationale |
| --- | --- | --- | --- | --- | --- |
| 4.1.1 | Parsing (Obsolete and removed) | A (historical) | Not applicable to a declared artifact type with rationale | None. | **The WCAG 2.2 Recommendation itself marks this criterion obsolete and removed.** This is the standard's own withdrawal, not a CDS scope judgement and not a convenience exclusion. Retained only so this mapping can be checked against the source without a silent gap; excluded from the 55. |

---

## Counts

| Metric | Count |
| --- | --- |
| Current Level A criteria mapped | **31** |
| Current Level AA criteria mapped | **24** |
| **Current applicable A/AA total** | **55** |
| `DIRECT_SOURCE_CONTRACT_APPLICABILITY` | **5** |
| `REPRESENTATION_TRIGGERED` | **30** |
| `CONSUMER_OWNED` | **20** |
| `NOT_APPLICABLE_WITH_RATIONALE` | **1** (historical row only) |
| Historical removed reference rows | **1** (4.1.1 Parsing) |
| **Total displayed rows** | **56** |
| Criteria for which any evidence exists today | **5** — Group A only, and only its source-level part, only at **admitted AE-1** (`AE1-CDS-WP016-SEMSTATUS-002`, source scope) |
| Criteria for which CDS makes a conformance statement | **0** |

**Independent re-count:** 5 + 30 + 20 = **55** current criteria, plus the single
historical row = **56**, matching the global matrix's 56 displayed rows. Any
mismatch is a defect in this document and fails closed.

## What the distribution says

**Only 5 of 55 criteria have a source-level component that can be evidenced
today, and none of the 5 can be *met* by the source alone.** Thirty are waiting
for a representation that does not exist, and twenty belong to a consumer that
does not exist either.

That is the honest shape of a channel-independent meaning contract at Candidate:
it can make downstream accessibility *possible* and it can make certain failures
*impossible*, and that is all. It cannot make anything accessible, because
accessibility happens where content, composition, and process meet a user — and
none of those is in this Candidate's scope.

This is also why DEC-S-125 does not weaken anything: the 30
representation-triggered criteria keep their full force and simply attach to the
artifact that can actually satisfy them, under its own Channel Accessibility
Profile, with its own evidence.

## Note on the relationship to the global matrix

The global matrix's five "CDS-alone" criteria (1.3.3, 1.4.1, 1.4.5, 2.3.1, 2.4.7)
and this mapping's five `DIRECT` criteria (1.1.1, 1.3.1, 1.3.3, 1.4.1, 4.1.3)
**are deliberately different sets**. The global matrix asks *who owns the
criterion across all of CDS*; this mapping asks *what is assessable against this
non-rendered artifact today*. Criteria such as 1.4.5 and 2.4.7 remain
CDS-owned globally while being representation-triggered for this artifact, and
1.1.1, 1.3.1, and 4.1.3 remain shared globally while having a source-level
component here. Neither reading overrides the other, and the global matrix
remains the normative source.

## Related documents

- [WCAG 2.2 AA Applicability Matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md) — normative source
- [Semantic Status Candidate Accessibility Responsibility Mapping](SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_RESPONSIBILITY_MAPPING.md)
- [Semantic Status Candidate AE-2 Evidence Plan](SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md)
- [Semantic Status Candidate Support Baseline Plan](SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md)
- [Semantic Status Candidate Accessibility Limitations](SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Accessibility Channel Profiles](ACCESSIBILITY_CHANNEL_PROFILES.md)
