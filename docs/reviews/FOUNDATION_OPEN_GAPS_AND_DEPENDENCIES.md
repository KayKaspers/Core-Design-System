# Foundation Open Gaps and Dependencies

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-008 — Foundation Milestone Review
- **Reviewed revision:** `7b71652`
- **Date:** 2026-07-16
- **Status:** **Review evidence — not a normative source.** Findings (**FM-F-###**)
  are review observations, **not** Decisions or Risks. They create no ID in any
  register and change no policy.

## Classification scheme

Each open point is classified as exactly one of:

- **Foundation Blocker** — prevents Foundation closure.
- **Next-phase prerequisite** — required before design/implementation begins.
- **Candidate prerequisite** — required before any first Candidate artifact.
- **CoreOps-pilot prerequisite** — required before the pilot may start.
- **Publication prerequisite** — required before any publication-state change.
- **Long-term governance issue** — ongoing operating concern.
- **Optional improvement** — beneficial, not required.

**FM-F IDs are local to this review.** They are not DEC-S or RISK IDs and must not
be treated as such.

## Findings

| ID | Description | Source | Impact | Owner role | Recommended trigger | Priority | Blocks Foundation closure |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FM-F-001 | **No accessibility support baseline** is declared; AE-3 and Stable are therefore unreachable. | RISK-044; [Evidence & Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) | Candidate/Stable accessibility evidence cannot be produced | Human Maintainer | Before first Candidate with an accessibility obligation | High | **No** |
| FM-F-002 | **Governance affordability**: all approval concentrates on one Human Maintainer; Elevated + accessibility path is High burden (Dry Run C). | RISK-029, RISK-048; [Affordability Review](GOVERNANCE_AFFORDABILITY_AND_OPERATING_READINESS.md) | Risk of bypass/backlog; slow first Candidate | Nova / Human Maintainer | Before first Elevated change | High | **No** |
| FM-F-003 | **Risk register not yet operated as an instrument**: 48 risks, 0 `Mitigating`, 0 named executors. | RISK-040; [Risk Register](../risks/RISK_REGISTER.md) | Risks recorded but not driven; ceremonial governance | Nova (controller) / Human Maintainer (owner) | On next-phase start | High | **No** |
| FM-F-004 | **No licence selected** for any of the ten artifact classes. | DEC-S-047; RISK-038 | No publication-state change possible; no release | Human Maintainer | Before any publication | Medium | **No** |
| FM-F-005 | **No test tooling / browser / assistive-technology** selected for accessibility evidence. | DEC-S-053 | Automated evidence (a support input) cannot yet be gathered | Human Maintainer / Nova | Before first Candidate evidence | Medium | **No** |
| FM-F-006 | **Three of six governance roles unstaffed** (Consumer Maintainer, Contributor, Evidence Reviewer). | [Governance Operating Model](../governance/GOVERNANCE_OPERATING_MODEL.md); DEC-S-045 | Elevated changes needing a distinct Evidence Reviewer cannot proceed | Human Maintainer | Before first Elevated/Stable change | Medium | **No** |
| FM-F-007 | **No first Candidate artifact exists** (by design). | DEC-S-003 | Pilot entry criterion 5 unmet | Human Maintainer | Next phase, first design slice | Medium | **No** |
| FM-F-008 | **CoreOps pilot scope not approved and pilot area not named** (criteria 2, 6). | [Pilot Contract](../governance/COREOPS_PILOT_CONTRACT.md) | Pilot cannot start | Human Maintainer | Before pilot | Medium | **No** |
| FM-F-009 | **No user research exists or is planned**; documentation evidence is not user validation. | RISK-017 | Inclusive-design and requirement claims remain unvalidated by people | Human Maintainer / Nova | Before any "works for users" claim | Medium | **No** |
| FM-F-010 | **HYP-001 … HYP-008 remain research hypotheses** resting largely on absence-of-evidence; none is strongly supported. | [Hypotheses](../research/CDS_DIFFERENTIATION_HYPOTHESES.md) | Differentiation claims not yet substantiable | Nova | Before any differentiation claim | Low | **No** |
| FM-F-011 | **Machine-readable normative source and token format undecided** (deliberately). | DEC-S-032 | Concrete design/build cannot begin until chosen | Human Maintainer | Next phase | Medium | **No** |
| FM-F-012 | **Governance ceremony duplication** (accessibility mapping, provenance, compatibility restated across documents). | [Affordability Review](GOVERNANCE_AFFORDABILITY_AND_OPERATING_READINESS.md) | Avoidable per-artifact effort for a small team | Nova | Next-phase operating setup | Low | **No** |

## Classification summary

| Class | Findings |
| --- | --- |
| Foundation Blocker | **none** |
| Next-phase prerequisite | FM-F-002, FM-F-003, FM-F-005, FM-F-011 |
| Candidate prerequisite | FM-F-001, FM-F-005, FM-F-006, FM-F-007 |
| CoreOps-pilot prerequisite | FM-F-001, FM-F-007, FM-F-008 |
| Publication prerequisite | FM-F-004 |
| Long-term governance issue | FM-F-002, FM-F-003, FM-F-012 |
| Optional improvement | FM-F-012 |
| Cross-cutting note | FM-F-009, FM-F-010 |

*(A finding may serve more than one class; classes are not mutually exclusive.)*

## Blocker assessment

**Zero Foundation blockers.** Every finding is a next-phase, Candidate, pilot, or
publication prerequisite, or a long-term operating concern. None is:

- a contradiction between normative sources,
- a missing or duplicated ID,
- a register/matrix sum that does not balance,
- an unresolved authority or conflict-resolution gap,
- an unsubstantiated adoption/conformance/publication claim,
- a traceability gap that cannot be resolved.

The two findings most likely to be *mistaken* for blockers — FM-F-001 (no support
baseline) and FM-F-007 (no Candidate artifact) — are explicitly **not** Foundation
blockers per the milestone's own closure criteria: missing implementation, missing
Candidate artifacts, and a missing support baseline do not block Foundation
closure; they block *later* phases.

## Related documents

- [Foundation Milestone Review](FOUNDATION_MILESTONE_REVIEW.md)
- [Foundation Completeness Matrix](FOUNDATION_COMPLETENESS_MATRIX.md)
- [Next-phase Recommendation](NEXT_PHASE_RECOMMENDATION.md)
