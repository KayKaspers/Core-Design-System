# WCAG 2.2 Level A and AA Applicability Matrix

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-007 - Accessibility and Inclusive Design Policy
- **Source date:** 2026-07-16
- **Status:** **Normative** for accessibility applicability and responsibility

## Purpose

Maps every official WCAG 2.2 Level A and Level AA success criterion to CDS
artifact classes, responsibility, architecture layers, required future evidence,
and policy status.

The criteria list, identifiers, titles, and levels were **extracted from the WCAG
2.2 W3C Recommendation itself** and independently re-counted. **No count was
taken from memory.**

Source: `https://www.w3.org/TR/WCAG22/` - W3C Recommendation, 2024-12-12.

## What this matrix is not

**This is a policy mapping, not a conformance evaluation.**

- **No pass/fail statement is made about any artifact.** Nothing has been tested.
- A mapping assigns responsibility and future evidence; it proves nothing.
- Missing implementation does **not** make a criterion `Not applicable`. It makes
  it not yet assessable - and every criterion here has an owner regardless.
- Level AAA criteria are **excluded** from this mandatory matrix (DEC-S-049).

## The obsolete criterion

**4.1.1 Parsing is marked "Obsolete and removed" by the Recommendation itself.**

It carries a Level A tag and is therefore listed here for completeness and
traceability against the source - but it is **excluded from the mandatory
baseline**.

Silently dropping it would make this matrix uncheckable against WCAG 2.2;
silently requiring it would impose an obligation the standard has withdrawn.

## Policy status vocabulary

| Status | Meaning |
| --- | --- |
| **Normative CDS requirement** | CDS owns it in its own artifacts. |
| **Shared CDS and consumer requirement** | CDS provides the contract; the consumer must compose and populate correctly. Both must act. |
| **Consumer-scope requirement** | The consumer owns it. CDS may expose a mechanism but cannot satisfy it. |
| **Channel-profile decision required** | Needs a channel profile before it can be assessed. |
| **Not applicable to a declared artifact type with rationale** | Genuinely does not apply, with a stated reason. |
| **Not yet assessable before implementation** | Applies, but cannot be evaluated until an artifact exists. |

## Reading the matrix

- **Architecture layers** use the CDS eight-layer model (3 Foundations and
  Tokens, 4 Components, 5 Patterns and Experiences, 6 Channels, 8 Evidence).
- **Required evidence** refers to the AE-0 ... AE-4 model.
- **Shared** marks whether both CDS and the consumer must act.
- Titles are the official ones. **No normative criterion text is reproduced.**

## Matrix

| SC | Title | Level | Applicable CDS artifact classes | CDS responsibility | Consumer responsibility | Shared | Layers | Required future evidence | Policy status | Limitations / notes | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1.1 | Non-text Content | A | Components, patterns, docs, examples | Contract requires text alternative slots and roles | Supplies actual alternative text for product content | Yes | 3,4,6 | AE-1, AE-2 | Shared CDS and consumer requirement | CDS cannot author consumer content. | [src](https://www.w3.org/TR/WCAG22/#x1-1-1-non-text-content) |
| 1.2.1 | Audio-only and Video-only (Prerecorded) | A | Product content | None — CDS ships no media | Owns all media and alternatives | No | 6 | AE-4 | Consumer-scope requirement | No CDS artifact class currently carries prerecorded media. | [src](https://www.w3.org/TR/WCAG22/#x1-2-1-audio-only-and-video-only-prerecorded) |
| 1.2.2 | Captions (Prerecorded) | A | Product content | None | Owns captions for its media | No | 6 | AE-4 | Consumer-scope requirement | Consumer media only. | [src](https://www.w3.org/TR/WCAG22/#x1-2-2-captions-prerecorded) |
| 1.2.3 | Audio Description or Media Alternative (Prerecorded) | A | Product content | None | Owns audio description or media alternative | No | 6 | AE-4 | Consumer-scope requirement | Consumer media only. | [src](https://www.w3.org/TR/WCAG22/#x1-2-3-audio-description-or-media-alternative-prerecorded) |
| 1.2.4 | Captions (Live) | AA | Product content | None | Owns live captions | No | 6 | AE-4 | Consumer-scope requirement | Consumer media only. | [src](https://www.w3.org/TR/WCAG22/#x1-2-4-captions-live) |
| 1.2.5 | Audio Description (Prerecorded) | AA | Product content | None | Owns audio description | No | 6 | AE-4 | Consumer-scope requirement | Consumer media only. | [src](https://www.w3.org/TR/WCAG22/#x1-2-5-audio-description-prerecorded) |
| 1.3.1 | Info and Relationships | A | Components, patterns, docs, channels | Contracts define programmatic structure and relationships | Correct composition and content structure | Yes | 3,4,5,6 | AE-1, AE-2, AE-3 | Shared CDS and consumer requirement | Core structural criterion; composition is consumer-owned. | [src](https://www.w3.org/TR/WCAG22/#x1-3-1-info-and-relationships) |
| 1.3.2 | Meaningful Sequence | A | Components, patterns, docs | Contracts define meaningful order | Preserves order in composition | Yes | 4,5,6 | AE-2, AE-3 | Shared CDS and consumer requirement | Reading order survives only if composed correctly. | [src](https://www.w3.org/TR/WCAG22/#x1-3-2-meaningful-sequence) |
| 1.3.3 | Sensory Characteristics | A | Components, patterns, docs, channels | Forbids sensory-only instructions in contracts and guidance | Applies to product content | Yes | 3,4,5,6 | AE-2 | Normative CDS requirement | Directly reinforces multi-modal meaning. | [src](https://www.w3.org/TR/WCAG22/#x1-3-3-sensory-characteristics) |
| 1.3.4 | Orientation | AA | Components, patterns, product UI | Contracts must not lock orientation | Product-level orientation behavior | Yes | 4,5 | AE-2 | Shared CDS and consumer requirement | Implementation-dependent. | [src](https://www.w3.org/TR/WCAG22/#x1-3-4-orientation) |
| 1.3.5 | Identify Input Purpose | AA | Product forms | Contract exposes autocomplete affordance | Declares actual input purpose | Yes | 4 | AE-2 | Consumer-scope requirement | CDS cannot know a field's purpose. | [src](https://www.w3.org/TR/WCAG22/#x1-3-5-identify-input-purpose) |
| 1.4.1 | Use of Color | A | Foundations, components, patterns, channels | Colour never the sole carrier — architecture invariant | Applies in product content | Yes | 3,4,5,6,8 | AE-1, AE-2 | Normative CDS requirement | Binds to the status-axes invariant (DEC-S-028). | [src](https://www.w3.org/TR/WCAG22/#x1-4-1-use-of-color) |
| 1.4.2 | Audio Control | A | Product content | None | Owns auto-playing audio | No | 5 | AE-4 | Consumer-scope requirement | No CDS artifact plays audio. | [src](https://www.w3.org/TR/WCAG22/#x1-4-2-audio-control) |
| 1.4.3 | Contrast (Minimum) | AA | Foundations, components, channels | Semantic colour roles must permit conforming contrast | Final values in profile and product | Yes | 3,4,6 | AE-1, AE-2 | Shared CDS and consumer requirement | No CDS colour value exists; value selection deferred. | [src](https://www.w3.org/TR/WCAG22/#x1-4-3-contrast-minimum) |
| 1.4.4 | Resize Text | AA | Foundations, components, product UI | Contracts must tolerate text resize | Product layout behavior | Yes | 3,4,5 | AE-2 | Shared CDS and consumer requirement | Implementation-dependent. | [src](https://www.w3.org/TR/WCAG22/#x1-4-4-resize-text) |
| 1.4.5 | Images of Text | AA | Foundations, components, docs, channels | Avoid images of text in CDS artifacts | Applies in product content | Yes | 3,4,6 | AE-1, AE-2 | Normative CDS requirement | Relates to flexible text (CR-023). | [src](https://www.w3.org/TR/WCAG22/#x1-4-5-images-of-text) |
| 1.4.10 | Reflow | AA | Components, patterns, product UI, docs | Contracts must support reflow | Composition and product layout | Yes | 3,4,5 | AE-2 | Shared CDS and consumer requirement | Dense operational data is the hard case. | [src](https://www.w3.org/TR/WCAG22/#x1-4-10-reflow) |
| 1.4.11 | Non-text Contrast | AA | Foundations, components | Semantic roles must permit conforming non-text contrast | Final values and product usage | Yes | 3,4 | AE-1, AE-2 | Shared CDS and consumer requirement | No CDS value exists yet. | [src](https://www.w3.org/TR/WCAG22/#x1-4-11-non-text-contrast) |
| 1.4.12 | Text Spacing | AA | Foundations, components, product UI | Contracts tolerate text spacing overrides | Product behavior | Yes | 3,4 | AE-2 | Shared CDS and consumer requirement | Relates to flexible text lengths. | [src](https://www.w3.org/TR/WCAG22/#x1-4-12-text-spacing) |
| 1.4.13 | Content on Hover or Focus | AA | Components, patterns | Hover/focus content contracts | Product usage | Yes | 4,5 | AE-2, AE-3 | Shared CDS and consumer requirement | Hover must never be the sole carrier. | [src](https://www.w3.org/TR/WCAG22/#x1-4-13-content-on-hover-or-focus) |
| 2.1.1 | Keyboard | A | Components, patterns, product UI, docs | Keyboard operability is a contract obligation | Composition and product-level operability | Yes | 4,5 | AE-2, AE-3 | Shared CDS and consumer requirement | CR-021. Mandatory contract area (DEC-S-055). | [src](https://www.w3.org/TR/WCAG22/#x2-1-1-keyboard) |
| 2.1.2 | No Keyboard Trap | A | Components, patterns | Contracts must not trap focus | Composition must not create traps | Yes | 4,5 | AE-2, AE-3 | Shared CDS and consumer requirement | CR-021. A trap can arise purely from composition. | [src](https://www.w3.org/TR/WCAG22/#x2-1-2-no-keyboard-trap) |
| 2.1.4 | Character Key Shortcuts | A | Components, patterns | Character-key shortcut contracts | Product-level shortcuts | Yes | 4,5 | AE-2 | Shared CDS and consumer requirement | CDS defines none today. | [src](https://www.w3.org/TR/WCAG22/#x2-1-4-character-key-shortcuts) |
| 2.2.1 | Timing Adjustable | A | Patterns, product UI | Timing contracts for session and process patterns | Product timing behavior | Yes | 5 | AE-2 | Shared CDS and consumer requirement | Relates to session and security behavior. | [src](https://www.w3.org/TR/WCAG22/#x2-2-1-timing-adjustable) |
| 2.2.2 | Pause, Stop, Hide | A | Components, patterns | Control contracts for moving or auto-updating content | Product content behavior | Yes | 4,5 | AE-2 | Shared CDS and consumer requirement | Live operational updates are the hard case. | [src](https://www.w3.org/TR/WCAG22/#x2-2-2-pause-stop-hide) |
| 2.3.1 | Three Flashes or Below Threshold | A | Foundations, components, patterns | No CDS artifact may flash above threshold | Product content | Yes | 3,4,5 | AE-1, AE-2 | Normative CDS requirement | Relates to motion restraint (CR-022). | [src](https://www.w3.org/TR/WCAG22/#x2-3-1-three-flashes-or-below-threshold) |
| 2.4.1 | Bypass Blocks | A | Patterns, product UI, docs | Shell and navigation pattern contracts provide bypass | Product-level page composition | Yes | 5,6 | AE-2, AE-3 | Shared CDS and consumer requirement | Pilot Group A relevance. | [src](https://www.w3.org/TR/WCAG22/#x2-4-1-bypass-blocks) |
| 2.4.2 | Page Titled | A | Product UI, docs | Shell contract exposes a title mechanism | Supplies actual titles | Yes | 5,6 | AE-2 | Consumer-scope requirement | CDS cannot author product titles. | [src](https://www.w3.org/TR/WCAG22/#x2-4-2-page-titled) |
| 2.4.3 | Focus Order | A | Components, patterns | Focus order contracts | Composition determines final order | Yes | 4,5 | AE-2, AE-3 | Shared CDS and consumer requirement | CR-021. | [src](https://www.w3.org/TR/WCAG22/#x2-4-3-focus-order) |
| 2.4.4 | Link Purpose (In Context) | A | Docs, product content | Link contracts and content guidance | Supplies actual link text and context | Yes | 4,6 | AE-2 | Consumer-scope requirement | Content is consumer-owned. | [src](https://www.w3.org/TR/WCAG22/#x2-4-4-link-purpose-in-context) |
| 2.4.5 | Multiple Ways | AA | Product UI, docs | Navigation pattern options | Product-level navigation provision | Yes | 5,6 | AE-2 | Consumer-scope requirement | A site-level obligation. | [src](https://www.w3.org/TR/WCAG22/#x2-4-5-multiple-ways) |
| 2.4.6 | Headings and Labels | AA | Components, patterns, docs | Heading and label contracts | Supplies actual headings and labels | Yes | 4,5,6 | AE-2 | Shared CDS and consumer requirement | Content wording is consumer-owned. | [src](https://www.w3.org/TR/WCAG22/#x2-4-6-headings-and-labels) |
| 2.4.7 | Focus Visible | AA | Foundations, components, patterns | Visible focus is a mandatory contract area | Must not suppress it via overrides | Yes | 3,4,5 | AE-1, AE-2, AE-3 | Normative CDS requirement | CR-021. Profiles may not weaken (DEC-S-059). | [src](https://www.w3.org/TR/WCAG22/#x2-4-7-focus-visible) |
| 2.4.11 | Focus Not Obscured (Minimum) | AA | Components, patterns | Focus must not be obscured by CDS constructs | Composition must not obscure focus | Yes | 4,5 | AE-2, AE-3 | Shared CDS and consumer requirement | New in WCAG 2.2. Overlays are the hard case. | [src](https://www.w3.org/TR/WCAG22/#x2-4-11-focus-not-obscured-minimum) |
| 2.5.1 | Pointer Gestures | A | Components, patterns | Single-pointer alternatives in contracts | Product gestures | Yes | 4,5 | AE-2 | Shared CDS and consumer requirement | Implementation-dependent. | [src](https://www.w3.org/TR/WCAG22/#x2-5-1-pointer-gestures) |
| 2.5.2 | Pointer Cancellation | A | Components, patterns | Pointer cancellation contracts | Product behavior | Yes | 4,5 | AE-2 | Shared CDS and consumer requirement | Reinforces safe dangerous-action patterns. | [src](https://www.w3.org/TR/WCAG22/#x2-5-2-pointer-cancellation) |
| 2.5.3 | Label in Name | A | Components | Accessible-name contracts match visible label | Supplies matching content | Yes | 4 | AE-2, AE-3 | Shared CDS and consumer requirement | Content-dependent. | [src](https://www.w3.org/TR/WCAG22/#x2-5-3-label-in-name) |
| 2.5.4 | Motion Actuation | A | Components, patterns | No motion-actuation-only operation | Product behavior | Yes | 4,5 | AE-2 | Shared CDS and consumer requirement | Relates to multi-modal meaning. | [src](https://www.w3.org/TR/WCAG22/#x2-5-4-motion-actuation) |
| 2.5.7 | Dragging Movements | AA | Components, patterns | Dragging alternatives in contracts | Product behavior | Yes | 4,5 | AE-2 | Shared CDS and consumer requirement | New in WCAG 2.2. | [src](https://www.w3.org/TR/WCAG22/#x2-5-7-dragging-movements) |
| 2.5.8 | Target Size (Minimum) | AA | Foundations, components | Target size contracts and spacing foundations | Final composition and values | Yes | 3,4 | AE-1, AE-2 | Shared CDS and consumer requirement | New in WCAG 2.2. No CDS size value exists. | [src](https://www.w3.org/TR/WCAG22/#x2-5-8-target-size-minimum) |
| 3.1.1 | Language of Page | A | Product UI, docs | Shell contract exposes a language mechanism | Declares actual page language | Yes | 5,6 | AE-1, AE-2 | Consumer-scope requirement | CR-023. Consumer declares. | [src](https://www.w3.org/TR/WCAG22/#x3-1-1-language-of-page) |
| 3.1.2 | Language of Parts | AA | Docs, product content | Contracts permit per-part language marking | Marks actual language changes | Yes | 4,6 | AE-1, AE-2 | Consumer-scope requirement | CR-023. DE/EN parity relevance. | [src](https://www.w3.org/TR/WCAG22/#x3-1-2-language-of-parts) |
| 3.2.1 | On Focus | A | Components, patterns | No context change on focus, by contract | Product behavior | Yes | 4,5 | AE-2, AE-3 | Shared CDS and consumer requirement | Implementation-dependent. | [src](https://www.w3.org/TR/WCAG22/#x3-2-1-on-focus) |
| 3.2.2 | On Input | A | Components, patterns | No context change on input, by contract | Product behavior | Yes | 4,5 | AE-2, AE-3 | Shared CDS and consumer requirement | Implementation-dependent. | [src](https://www.w3.org/TR/WCAG22/#x3-2-2-on-input) |
| 3.2.3 | Consistent Navigation | AA | Product UI, docs | Navigation pattern consistency | Consistent product-level placement | Yes | 5,6 | AE-4 | Consumer-scope requirement | A site-level obligation across pages. | [src](https://www.w3.org/TR/WCAG22/#x3-2-3-consistent-navigation) |
| 3.2.4 | Consistent Identification | AA | Components, patterns | Consistent component identification | Consistent product usage | Yes | 4,5 | AE-4 | Shared CDS and consumer requirement | CDS consistency helps; composition decides. | [src](https://www.w3.org/TR/WCAG22/#x3-2-4-consistent-identification) |
| 3.2.6 | Consistent Help | A | Product UI, docs | Help pattern contract | Provides consistent help placement | Yes | 5,6 | AE-4 | Consumer-scope requirement | New in WCAG 2.2. CR-019 relevance. | [src](https://www.w3.org/TR/WCAG22/#x3-2-6-consistent-help) |
| 3.3.1 | Error Identification | A | Components, patterns | Error identification contracts | Supplies actual error content | Yes | 4,5 | AE-2, AE-3 | Shared CDS and consumer requirement | CR-020 plain-language errors. | [src](https://www.w3.org/TR/WCAG22/#x3-3-1-error-identification) |
| 3.3.2 | Labels or Instructions | A | Components, patterns | Label and instruction contracts | Supplies actual labels and instructions | Yes | 4,5 | AE-2 | Shared CDS and consumer requirement | Content is consumer-owned. | [src](https://www.w3.org/TR/WCAG22/#x3-3-2-labels-or-instructions) |
| 3.3.3 | Error Suggestion | AA | Components, patterns | Error suggestion contracts | Supplies domain-correct suggestions | Yes | 4,5 | AE-2 | Shared CDS and consumer requirement | CDS cannot know domain semantics. | [src](https://www.w3.org/TR/WCAG22/#x3-3-3-error-suggestion) |
| 3.3.4 | Error Prevention (Legal, Financial, Data) | AA | Patterns, product UI | Safe-action pattern contracts (preview, confirm, cancel) | Determines which actions are legal, financial, or data-critical | Yes | 5 | AE-2, AE-4 | Consumer-scope requirement | CR-011, CR-012. Strong overlap with pilot Group D. | [src](https://www.w3.org/TR/WCAG22/#x3-3-4-error-prevention-legal-financial-data) |
| 3.3.7 | Redundant Entry | A | Patterns, product UI | Process pattern contracts avoid redundant entry | Product process design | Yes | 5 | AE-2 | Shared CDS and consumer requirement | New in WCAG 2.2. | [src](https://www.w3.org/TR/WCAG22/#x3-3-7-redundant-entry) |
| 3.3.8 | Accessible Authentication (Minimum) | AA | Patterns, product UI | Authentication pattern contracts | Owns authentication implementation | Yes | 5 | AE-2, AE-4 | Shared CDS and consumer requirement | New in WCAG 2.2. Security must not silently override accessibility. | [src](https://www.w3.org/TR/WCAG22/#x3-3-8-accessible-authentication-minimum) |
| 4.1.1 | Parsing (Obsolete and removed) | A (historical) | None | None | None | No | - | None | Not applicable to a declared artifact type with rationale | **Obsolete and removed reference row — not a current WCAG 2.2 conformance criterion.** Removed by the Recommendation itself (not a CDS scope judgement); excluded from the 55 applicable and retained only for traceability against the source. | [src](https://www.w3.org/TR/WCAG22/#x4-1-1-parsing-obsolete-and-removed) |
| 4.1.2 | Name, Role, Value | A | Components, patterns | Name, role, value, state contracts — mandatory area | Correct composition and content | Yes | 3,4,5 | AE-2, AE-3 | Shared CDS and consumer requirement | Central to honest states reaching assistive technology. | [src](https://www.w3.org/TR/WCAG22/#x4-1-2-name-role-value) |
| 4.1.3 | Status Messages | AA | Components, patterns | Status message contracts | Product status content | Yes | 4,5,8 | AE-2, AE-3 | Shared CDS and consumer requirement | Directly carries the Unknown invariant (DEC-S-056). | [src](https://www.w3.org/TR/WCAG22/#x4-1-3-status-messages) |

## Counts

All counts derived from the matrix above and independently re-counted against the
WCAG 2.2 Recommendation.

### By level

| Metric | Count |
| --- | --- |
| **Current Level A criteria** | **31** |
| **Current Level AA criteria** | **24** |
| **Current applicable A/AA total** | **55** |
| **Historical removed reference rows** | **1** (4.1.1 Parsing) |
| **Total displayed rows** | **56** |

**WCAG 2.2 does not currently have 32 Level-A criteria.** It has **31 current
Level-A criteria**. The 32nd displayed row is **4.1.1 Parsing**, which the WCAG 2.2
Recommendation itself marks **obsolete and removed** — it is retained here only as
a **historical removed reference row**, clearly flagged, so the matrix can be
checked against the source without a silent gap. It is **not** a current
conformance criterion and is **not** counted toward the 55.

For context, the Recommendation lists **87** success criteria across all levels
(**86** currently applicable): **31 current** Level A (plus the 1 removed), 24 AA,
and 31 AAA. **AAA is out of scope** for this mandatory A/AA matrix and appears in
no row.

### By policy status

| Status | Count |
| --- | --- |
| Shared CDS and consumer requirement | 35 |
| Consumer-scope requirement | 15 |
| Normative CDS requirement | 5 |
| Not applicable to a declared artifact type with rationale | 1 |
| Channel-profile decision required | 0 |
| Not yet assessable before implementation | 0 |
| **Total** | **56** |

### By responsibility

| Responsibility | Count |
| --- | --- |
| Requires both CDS and consumer action | 49 |
| Consumer or CDS acts alone (or not applicable) | 7 |
| **Total** | **56** |

### What the distribution says

**35 of 56 criteria are shared, and 49 require action from both sides.** Only 5
are CDS-alone.

That is the central finding of this matrix, and it is not a gap - it is the
shape of the problem. A design system can supply a contract, a role, a state
mechanism, and a semantic slot. It cannot supply the content that fills them, the
composition that arranges them, or the process they sit inside. Those are where
accessibility is usually lost, and all three are consumer-owned.

This is why DEC-S-052 exists: **accessible components do not compose into an
accessible product by themselves.** The matrix quantifies that claim rather than
asserting it.

The 15 consumer-scope criteria are mostly content and media (1.2.x), page-level
declarations (2.4.2, 3.1.1), and site-wide obligations (2.4.5, 3.2.3) - none of
which CDS can satisfy on a consumer's behalf.

The 5 CDS-alone criteria cluster around **non-sensory meaning** (1.3.3, 1.4.1,
1.4.5), **visible focus** (2.4.7), and **flashing** (2.3.1) - exactly the areas
where the architecture already holds invariants.

### Not-applicable entries

| SC | Rationale |
| --- | --- |
| 4.1.1 Parsing | **Obsolete and removed by the WCAG 2.2 Recommendation itself.** Not a CDS scope judgement. |

**Exactly one** not-applicable entry, and it is the standard's own withdrawal -
not a CDS opt-out. No criterion was declared inapplicable because CDS finds it
inconvenient or because no implementation exists.

### Not-yet-assessable entries

**Zero.** Every applicable criterion has a defined owner and required evidence
today, even though no artifact exists to evaluate.

This is deliberate: `Not yet assessable` would describe the *evidence* state, and
this matrix records *policy* state. The absence of implementation is captured by
the evidence model (all artifacts are AE-0), not by weakening the mapping.

## Open applicability questions

1. **Non-web channels.** This matrix covers the web target. PDF, presentation,
   diagram, and brand channels need channel profiles before any criterion applies
   to them (DEC-S-058).
2. **Dense operational data** (1.4.10 Reflow, 1.4.12 Text Spacing) is the hardest
   case for CDS's most-evidenced consumer need. Unresolved until implementation.
3. **Live operational updates** (2.2.2, 4.1.3) must not interrupt users
   uncontrollably while still conveying honest status changes.
4. **Overlays and focus** (2.4.11) - a new WCAG 2.2 criterion with no CDS
   pattern yet.
5. **Authentication** (3.3.8) - security and accessibility must not be traded off
   silently; a conflict needs a controlled decision.
6. **Target size** (2.5.8) interacts with density; no CDS value exists.
7. **Which AAA criteria**, if any, are adopted selectively as quality goals.

## Limitations

- **Policy mapping only.** No artifact has been evaluated; no pass/fail exists.
- Responsibility assignments are CDS policy judgements, not standard text.
- A shared criterion cannot be satisfied by CDS alone, however good the contract.
- Evidence levels are future requirements; **all CDS artifacts are currently
  AE-0**.
- WCAG conformance would still not mean accessible - the Recommendation states
  that even AAA will not serve every disability.
- Source status decays; re-verify before relying on it (RISK-012 source
  volatility; standards-status note under RISK-047).

## Related documents

- [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [Accessibility Responsibility Model](ACCESSIBILITY_RESPONSIBILITY_MODEL.md)
- [Accessibility Requirements Baseline](ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Accessibility Standard Status and Limitations](../research/ACCESSIBILITY_STANDARD_STATUS_AND_LIMITATIONS.md)
- [Accessibility Source Register](../research/ACCESSIBILITY_SOURCE_REGISTER.md)
