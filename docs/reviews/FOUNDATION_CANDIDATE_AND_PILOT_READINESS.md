# Foundation Candidate and Pilot Readiness

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-008 — Foundation Milestone Review
- **Reviewed revision:** `7b71652`
- **Date:** 2026-07-16
- **Status:** **Review evidence — not a normative source.** **No artifact is
  promoted** by this document.

## Framing

"Readiness" is deliberately split into four independent questions. Conflating them
is how a design system talks itself into a premature Candidate. **Foundation
closure requires none of them to be "yes"** — a foundation can be complete and
correct with zero Candidate artifacts.

## 1. Governance Candidate Readiness

**Can CDS manage Candidate artifacts in a controlled way?** — **Yes (Met).**

The [Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md)
defines a complete Candidate gate (problem/scope, normative documentation,
ownership, source revision, **accessibility mapping and the Candidate accessibility
gate**, risks, evidence plan, consumer-validation plan, provenance, limitations),
a Stable gate, and the human-approval path. The machinery to *govern* a Candidate
exists and is internally consistent.

## 2. Artifact Candidate Readiness

**Does an artifact exist today that satisfies all Candidate gates?** — **No (Not
met).**

**Zero artifacts exist.** No foundation, token, component, or pattern has been
built — by design (DEC-S-003, DEC-S-032: governance and architecture precede
concrete design). This is **explicitly not a Foundation blocker**; it is the first
task of the *next* phase.

## 3. Evidence Readiness

**Can the required evidence be produced now?** — **No (Not met).**

- **No accessibility support baseline is declared** — so AE-3, and therefore
  Stable, cannot be evidenced (RISK-044).
- **No test tooling, browser, or assistive-technology set is selected** —
  deliberately (DEC-S-032, DEC-S-053).
- **No user research exists or is planned** (RISK-017).

Every artifact is **AE-0, Not Assessed**. Evidence readiness is a **Candidate/next-
phase prerequisite**, not a Foundation blocker.

## 4. Consumer Validation Readiness

**Is a bounded consumer-validation path defined?** — **Partially met.**

The [Consumer Validation Plan](../governance/CONSUMER_VALIDATION_PLAN.md) and the
bounded CoreOps pilot (Groups A–E, nine scenarios) define a path, with graded
evidence levels and the honesty rule. The path is **defined but inactive** — no
validation has been performed, and activation depends on the pilot entry criteria
below.

## First possible Candidate categories

*(Assessment only — nothing is authorised or promoted.)*

The artifacts **best positioned** to attempt Candidate first, because the
architecture already carries their structural answer, are:

1. **Semantic status foundations** (Layer 3) — the Unknown/severity/confidence axes
   (DEC-S-028); the architecture is itself the answer, so the design surface is
   smallest.
2. **A single component contract** carrying the mandatory accessibility contract
   areas (DEC-S-055) — e.g. a status-bearing control — as the first end-to-end
   test of the Candidate gate.
3. **Web documentation presentation** (channel profile 2) — one of only two
   channels with a defined target.

These are **candidates for candidacy**, not Candidates. Each still needs a support
baseline, an evidence plan, and Human-Maintainer approval.

## Missing Candidate gates (what any first Candidate still needs)

- a declared **accessibility support baseline**;
- an **evidence plan** and at least AE-1 plus an AE-2 plan;
- selected (but not yet chosen) **tooling** for automated checks (never sufficient
  alone, DEC-S-053);
- a **named Evidence Reviewer** who is not the author (DEC-S-045);
- Human-Maintainer approval after Nova review.

## CoreOps Pilot entry-criteria matrix

Source: [CoreOps Pilot Contract](../governance/COREOPS_PILOT_CONTRACT.md) (eight
entry criteria). Status vocabulary: **Met · Met upon Foundation commit · Partially
met · Not met · Not yet assessable**.

| # | Criterion | Normative source | Status | Evidence | Missing prerequisite | Owner | Blocking effect |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CDS-WP-004 committed | Pilot Contract | **Met** | Commit `3c1acec` in history | — | Human Maintainer | — |
| 2 | Pilot scope (Groups A–E) approved | Pilot Contract | **Not met** | No approval recorded | Human-Maintainer approval of the bounded scope | Human Maintainer | Blocks pilot start |
| 3 | Consumer requirements registered (CR-001…040) | Consumer Requirements Model | **Met** | 40 CRs committed | — | Nova / Human Maintainer | — |
| 4 | CDS-WP-005 architecture approved | Pilot Contract | **Partially met** | Architecture committed (`c40bf4d`); formal milestone approval is the subject of this review | Milestone approval (this review → Nova/Human Maintainer) | Human Maintainer | Blocks pilot start |
| 5 | Foundations at Candidate maturity | Maturity Lifecycle | **Not met** | No artifact is Candidate | A first Candidate artifact + its gates | Human Maintainer | Blocks pilot start |
| 6 | CoreOps pilot area named | Pilot Contract | **Not met** | No area named | Unambiguous Human-Maintainer naming | Human Maintainer | Blocks pilot start |
| 7 | No conflict with CoreOps governance/queue | Pilot Contract | **Not yet assessable** | Consumer repos are read-only and not analysed here | CoreOps-side confirmation | Consumer Maintainer | Blocks pilot start |
| 8 | Accessibility target & evidence method decided | Pilot A11y Criterion (CR-024) | **Met** | CDS-WP-007 committed (`7b71652`); WCAG 2.2 AA + AE-0…AE-4 in force | — | Human Maintainer | — (satisfied) |

### Entry-criteria summary

| Status | Count |
| --- | --- |
| Met | 3 (criteria 1, 3, 8) |
| Partially met | 1 (criterion 4) |
| Not met | 3 (criteria 2, 5, 6) |
| Not yet assessable | 1 (criterion 7) |
| **Total** | **8** |

**Criterion 8 became Met with the CDS-WP-007 commit** — the accessibility target
and evidence method are now decided. This is the one entry criterion CDS-WP-007
was authorised to move, and it moved.

## Explicit statements

*(Normative-status note: these restate committed policy; they create nothing.)*

- **The CoreOps Pilot Contract can be normative**, but **the pilot is not active**:
  four criteria are unmet or unassessable and two structurally cannot be met until
  a first Candidate exists.
- **No pilot validation has been performed.**
- **No CoreOps accessibility or WCAG conformance has been demonstrated, reviewed,
  or approved** — CoreOps is simply **not assessed**.
- **No artifact is promoted** to Candidate or Stable by this review.

## Related documents

- [Foundation Milestone Review](FOUNDATION_MILESTONE_REVIEW.md)
- [CoreOps Pilot Contract](../governance/COREOPS_PILOT_CONTRACT.md)
- [CoreOps Pilot Accessibility Criterion](../governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md)
- [Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md)
- [Open Gaps and Dependencies](FOUNDATION_OPEN_GAPS_AND_DEPENDENCIES.md)
