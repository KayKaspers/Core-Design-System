# Next-phase Recommendation

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-008 — Foundation Milestone Review
- **Reviewed revision:** `7b71652`
- **Date:** 2026-07-16
- **Status:** **Review recommendation — not a normative source, not an
  authorisation.** This document **activates no phase**, assigns **no work-package
  ID**, and extends **no roadmap**. It is input for Nova and the Human Maintainer.

## Starting position

The Foundation (CDS-WP-001 … CDS-WP-007) is committed, internally consistent, and
free of Foundation blockers (see
[Foundation Milestone Review](FOUNDATION_MILESTONE_REVIEW.md)). What does **not**
yet exist: any built artifact, any evidence above **AE-0**, an accessibility
support baseline, a licence, and selected technology. Those are the substance of
the **next** phase, not gaps in this one.

The recommended posture is therefore: **close the Foundation with notes, then run
a single, deliberately small design slice** that exercises the architecture and
governance *for real* before any breadth is attempted.

## Recommended next objective

**Prove the Foundation operable on one thin, end-to-end vertical** — a single
semantic status foundation plus one component contract carrying the mandatory
accessibility contract areas (DEC-S-055), taken to **Candidate** under the real
gates. The goal is to **validate the machinery**, not to produce a portfolio.

## Immediate Prerequisites

*Required before the first Candidate or any pilot.* (Cross-referenced to
[Open Gaps](FOUNDATION_OPEN_GAPS_AND_DEPENDENCIES.md).)

1. **A lightweight operating playbook** and Candidate/Elevated dossier templates,
   to make the governance affordable in practice (FM-F-002, FM-F-012; RISK-029,
   RISK-040).
2. **Declare an accessibility support baseline** (browser / platform / assistive-
   technology / language matrix) — the gate for AE-3 and Stable (FM-F-001;
   RISK-044).
3. **Staff the Evidence Reviewer role** (and, for a profile, a Consumer
   Maintainer) — the reviewer may never be the author (FM-F-006; DEC-S-045).
4. **Assign executors and triggers** to the risks that will be active in the next
   phase, turning the register into an instrument (FM-F-003; RISK-040).

## Recommended First Design Slice

The **smallest** scope that genuinely tests architecture *and* governance:

- **One Layer-3 semantic status foundation** — the Unknown/severity/confidence
  axes (DEC-S-028), where the architecture is itself the answer.
- **One Layer-4 component contract** consuming it, carrying keyboard, focus,
  reduced-motion, non-colour, error, and status obligations (DEC-S-055).
- Taken through the **Candidate gate** with AE-1 and an AE-2 plan against the newly
  declared baseline.

This slice touches the token flow, a component contract, the status invariant, the
accessibility gate, the maturity lifecycle, and the human-approval path — i.e. it
**exercises the whole spine** at minimum width.

## Proposed Sequencing

*(Order of work, not a roadmap. No work-package IDs are assigned; Nova authors any
work package.)*

1. Foundation-closure decision (Nova + Human Maintainer) on this review.
2. Operating playbook + templates; support-baseline definition; Evidence-Reviewer
   staffing.
3. Machine-readable-source and token-format decision (FM-F-011).
4. The first design slice to Candidate.
5. Only then: consider CoreOps pilot scope approval and pilot-area naming.
6. Licensing and publication decisions when there is something to publish.

## Deferred Work

- A broader component/pattern portfolio.
- Additional channel profiles (PDF, presentations, diagrams, brand).
- Product Profile reconciliation for secondary consumers.
- Domain Pattern Families (operations patterns) beyond the first slice.
- Differentiation claims pending stronger evidence (FM-F-010).

## Explicitly Not Recommended Yet

- A **full component portfolio**.
- A **full CoreOps redesign**.
- **Public release or any publication-state change**.
- Any **Stable claim** or **accessibility/adoption/conformance claim**.
- **Full Product-Profile migration** of consumers.
- **Broad external contribution** intake.
- Selecting concrete **colours, typography, logos, icons, or themes** as a
  standalone exercise (they belong inside the design slice, governed).

## Required Human-Maintainer decisions

- Accept or amend the recommended milestone outcome (**GO WITH NOTES**).
- Approve the accessibility support-baseline definition when proposed.
- Name the CoreOps pilot area and approve pilot scope **if and when** a Candidate
  exists.
- Decide licensing per artifact class before any publication.
- Authorise the next phase and its first work package (via Nova).

## Required Nova reviews

- Independent milestone review of this package and its recommendation.
- Author the next work-package prompt (no ID is proposed here).
- Control the operating-affordability remediation (FM-F-002, FM-F-003).

## Boundaries

- **No phase is activated** and **no work-package ID is created** by this document.
- **No roadmap is extended.** `WORK_PACKAGES.md` shows CDS-WP-008 completed and
  **no next authorised work package**.
- The next phase begins **only** on an explicit Nova prompt and Human-Maintainer
  authorisation.

## Related documents

- [Foundation Milestone Review](FOUNDATION_MILESTONE_REVIEW.md)
- [Foundation Open Gaps and Dependencies](FOUNDATION_OPEN_GAPS_AND_DEPENDENCIES.md)
- [Foundation Candidate and Pilot Readiness](FOUNDATION_CANDIDATE_AND_PILOT_READINESS.md)
