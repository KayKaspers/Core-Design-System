# Status Communication and Accessibility Contract

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-014 — Semantic Status Foundation Contract and First
  Candidate Plan
- **Date:** 2026-07-17
- **Status:** **Normative** communication obligations of the
  [Semantic Status Foundation Contract](SEMANTIC_STATUS_FOUNDATION_CONTRACT.md),
  pending Human-Maintainer commit. Experimental; no Candidate status. **This
  contract fixes meaning obligations — no final UI copy, no visual value, and
  no conformance claim.**

## Textual meaning first

*(Normative — DEC-S-111; Accessibility Requirements Baseline 7.1, 7.3, 7.4, 7.6)*

Every one of the 25 axis values has a **textual meaning** (its canonical
meaning in the [Status Axis Vocabulary](STATUS_AXIS_VOCABULARY.md)) that must be
expressible as text and as accessible semantics in every representation:

- **No colour-only encoding.** Colour may accompany, never carry alone
  (invariant 7, CR-006).
- **No icon-only, shape-only, position-only, or motion-only encoding.** The
  same rule applies to every non-textual channel of meaning.
- **Programmatic availability.** Status and its changes must be available to
  assistive technology (WCAG 4.1.2/4.1.3 territory per baseline 7.1/7.6 —
  stated as an obligation on future artifacts, not as a met criterion).
- **Unknown, freshness, and confidence are perceivable** — visually and
  non-visually (baseline 7.4). A status honest only to a sighted user is not
  honest.

## Multi-modal contract

A conforming future representation provides at least: a text form of every
asserted axis value and its material qualifiers; an accessible-semantics form
(name/role/state or channel equivalent); and optional redundant modalities
(colour, icon, position, motion) that never contradict or extend the textual
meaning. Redundancy is additive; contradiction is a defect.

## Screenreader and keyboard boundary

*(An obligation on future interactive artifacts — nothing interactive ships in
CDS-WP-014.)*

- Interactive status representations must be keyboard-reachable and
  keyboard-operable with visible focus (baseline area 2; CR-021).
- Status changes must be perceivable without pointer hover and without
  vision; live updates must not interrupt uncontrollably (baseline 7.7).
- Detail disclosure (drill-down from a summary to all five axes) must be
  operable by keyboard and exposed to assistive technology.
- These are component-contract obligations to be evidenced later (AE-graded).
  **No interactive, keyboard, focus, screen-reader, assistive-technology, or channel
  evidence exists at any level.** The channel-independent Semantic Status
  source/contract family holds admitted source-level **AE-1**, which satisfies **none**
  of these obligations and does not transfer to any component or channel. This
  contract creates the requirement, not the evidence.

## Understandable error and unknown communication

*(Baseline area 5 — plain, non-blaming, actionable)*

- `unknown` is communicated as an honest statement ("not known", "not
  assessed", "no current data" — final wording localized later), never as an
  error of the user, never as silence, never as a positive default.
- Limitations (`partial`, `unavailable`, `stale`, `expired`, `unverified`)
  are stated in plain language with what they mean for the decision at hand.
- Fail-closed states are communicated as system states with a path to
  resolution, not as user faults.

## Reduced-motion boundary

Motion may be used only as a redundant modality for status; every
motion-carrying representation must honor reduced-motion preferences without
losing meaning (baseline area 4, CR-022). Since meaning is textual first,
removing motion never removes meaning. No motion value is defined here.

## DE/EN parity

*(Normative — baseline 8.2; semantic parity now, label wording later)*

- The **normative semantic reference language is English** (technical IDs and
  canonical meanings). German display labels and descriptions are a
  **first-class localization**, not an afterthought: every status meaning must
  be expressible in DE and EN with **identical semantic content**.
- **No semantically contradictory translations:** a DE label may not narrow,
  widen, soften, or upgrade the canonical meaning (e.g. no DE rendering of
  `supported` that reads as *verified*; no rendering of `unknown` that reads
  as neutral-positive). Parity review is part of the Candidate evidence plan.
- Terminology mapping DE/EN is a planned Candidate package element — not
  fixed in CDS-WP-014.

## Flexible labels

Display labels must tolerate localization-driven length variation (baseline
8.3/8.4): no representation may assume a fixed label length, truncate away a
material qualifier, or rely on abbreviations that carry meaning without
understandable context (8.7). Technical IDs remain language-neutral and stable
(DEC-S-110); text direction must not be architecturally excluded (8.6).

## Status-summary qualifiers

*(Normative — DEC-S-108 applied to language)*

- A summary may prioritize (per the
  [disclosure priority](STATUS_COMPOSITION_AND_CONFLICT_RULES.md#disclosure-priority))
  but must carry every **material qualifier**: stale/expired freshness,
  unverified/unknown confidence, partial/unavailable/unknown evidence, and any
  `unknown` axis.
- **Prohibited unqualified claims:** "healthy", "good", "current",
  "verified", "all systems normal" (or equivalents in any language) when the
  corresponding axes do not carry them. "No known impact" is not "no
  impact"; "not verified" must remain available and used.
- Every summary must offer a path to the full five-axis disclosure.

## Channel preservation

Meaning is constant across channels (DEC-S-029, invariant 9): interactive UI,
documents, print/greyscale, and data-dense visualizations must all preserve
the five axes and their qualifiers through text and structure. A channel that
cannot render a distinction must declare the limitation rather than silently
dropping it. Data visualization gets no exemption — dense encoding is where
the non-collapse rules bite hardest.

## No visual values

This contract defines **no** colour, icon, typography, spacing, size, motion
value, or component. Any future visual encoding is a redundant modality bound
to these semantics and enters through a later, explicitly authorized design
work package.

## Related documents

- [Semantic Status Foundation Contract](SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
- [Status Axis Vocabulary](STATUS_AXIS_VOCABULARY.md)
- [Status Composition and Conflict Rules](STATUS_COMPOSITION_AND_CONFLICT_RULES.md)
- [Accessibility Requirements Baseline](../governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [Accessibility and Inclusive Design Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
