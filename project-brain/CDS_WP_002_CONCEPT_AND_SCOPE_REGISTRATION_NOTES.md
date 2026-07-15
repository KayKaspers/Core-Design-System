# CDS-WP-002 — Concept and Scope Registration Notes

Internal work-package evidence for CDS-WP-002 — Concept and Scope Registration.

- **Date:** 2026-07-15
- **Executed by:** Claude (scoped local work)
- **Final status:** Completed

## Assignment

Register the binding project concept, the long-term and current scope, the
non-goals, the target and user groups, the consumer classes, and the ownership
boundaries between CDS and its consumer projects. Add DEC-S-007 … DEC-S-012 and
RISK-006 … RISK-009, create the Foundation Context Pack, and advance the status
to CDS-WP-002 Completed / CDS-WP-003 Next.

No concrete visual or technical design decisions.

## Preflight

| Check | Result |
| --- | --- |
| Repository root | `D:/Projects/Core-Design-System` — matches. |
| Branch | `main` — as required. |
| Working tree | Clean. |
| Last commit | `0369bee chore(ndf): bootstrap verified v1.0.0 skills` |
| Remote (read-only) | `origin` → `https://github.com/KayKaspers/Core-Design-System.git` |
| Merge / rebase / cherry-pick | None active. |
| CDS-WP-001 / CDS-WP-001A | Both Completed, consistently. |
| CDS-WP-002 | Next, consistently. |
| Skill directories / files | 38 / 39 — as expected. |
| Skills version and commit | v1.0.0, `9dcadc12fb960914b9a5baeff2ab1aee75912b57` — confirmed. |
| Skills manifest | Valid JSON; all 39 files hash-match the manifest. |
| Decisions / risks at start | 6 / 5. |

No fail-closed condition was triggered.

Normative documents read in full before any change: README.md, CLAUDE.md,
PROJECT_CHARTER.md, DECISION_INDEX.md, RISK_REGISTER.md, PROJECT_PROFILE.md,
NEXT_PHASE.md, WORK_PACKAGES.md, PROJECT_BRAIN.md.

## Skills used

Only the seven authorized Skills were loaded. No further Skill was read.

| Skill | Purpose in this WP | Section used |
| --- | --- | --- |
| `ndf-work-package-runner` | WP frame: pre-checks, guardrails, closing structure. | Purpose, Allowed/Forbidden actions, Fail-closed, Output contract |
| `ndf-project-brief-runner` | Structure of the concept registration: goal, scope, non-goals, risks, next steps. | Expected outputs, Forbidden actions |
| `ndf-feature-scope-runner` | Scope sharpening: problem/goal/non-goal separation, open questions instead of assumptions. | Expected outputs, Fail-closed |
| `ndf-product-discovery-runner` | Discovery structure: audience, problem, value proposition, non-goals. | Expected outputs, Ethical-use boundaries |
| `ndf-context-pack-maintainer` | Context Pack structure, reference-over-repetition, no invented status. | Expected outputs, Forbidden actions, Output contract |
| `ndf-compact-context-summary-runner` | Report to Nova and Compact Context Summary structure. | Expected outputs, Output contract |
| `ndf-public-neutrality-guard` | Neutrality check of the produced text. | Public-neutrality requirements, Output contract |

No unauthorized Skills were used. No Skill was used to extend scope, Allowed
Files, authority, or decisions.

### Neutrality applicability note

`ndf-public-neutrality-guard` forbids private project names in **public NDF**
artifacts and states that project-specific concretization belongs in the
project's own repository. CDS is that project's own repository, and the
work-package prompt explicitly requires naming CoreOps, SpeakCore, CastCore,
and AirCore. Naming them here is therefore correct and not a neutrality
violation. The guard's other rules were applied: no secrets, no real private
domains, no personal data, no reviewer identities, no search patterns.

## Initial state

The repository held the governance foundation from CDS-WP-001 and the verified
Skills from CDS-WP-001A. Scope existed only as a flat list of categories in the
project charter, with no ownership model, no consumer classification, and no
separation between long-term and current scope. No context pack existed.

Nothing in the existing documents contradicted the assignment. The charter's
scope list was superseded by the new taxonomy and replaced with a reference.

## Files created and changed

### Created

| Path | Content |
| --- | --- |
| `docs/governance/CONCEPT_AND_SCOPE.md` | Normative scope source: authority, statement classes, problem statement, mission, vision, objectives, six domains, cross-cutting concerns, current and long-term scope, 12 non-goals, ownership boundaries, CoreOps pilot boundary, assumptions, open questions, WP relationships, change control. |
| `docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md` | Direct users, indirect beneficiaries, stakeholder roles, three consumer classes, channel-consumer categories, classification limits, no-endorsement and no-release statements, CoreOps role, validation direction. |
| `docs/governance/SCOPE_BOUNDARY_MATRIX.md` | 21-row responsibility matrix with CDS / consumer / shared columns, Foundation status, and future decision or WP; boundary notes; open boundary questions. |
| `project-system/CONTEXT_PACK_FOUNDATION.md` | Compact continuation summary with an explicit precedence disclaimer and a normative source map. |
| `project-brain/CDS_WP_002_CONCEPT_AND_SCOPE_REGISTRATION_NOTES.md` | This document. |

### Changed

| Path | Change |
| --- | --- |
| `docs/governance/PROJECT_CHARTER.md` | Scope list replaced by the six-domain taxonomy plus a reference to the normative source; consumer classes and pilot boundary added; Foundation status table added; related documents extended. Mission, vision, and phase boundary unchanged. |
| `docs/decisions/DECISION_INDEX.md` | Range extended to DEC-S-001…012; decision-type table added; DEC-S-007…012 appended. DEC-S-001…006 unchanged. |
| `docs/risks/RISK_REGISTER.md` | Range extended to RISK-001…009; provisional-owner note added; RISK-006…009 appended; RISK-002 gained a cross-reference to the pilot boundary with its meaning preserved. |
| `project-system/PROJECT_PROFILE.md` | WP status, registered scope domains, consumer classes, register ranges, pilot-boundary note, deferred areas, document links. |
| `project-system/NEXT_PHASE.md` | Rewritten for CDS-WP-003 including objective, boundaries, the research-source authorization boundary, and prohibitions. |
| `project-system/WORK_PACKAGES.md` | CDS-WP-002 Completed, CDS-WP-003 Next; descriptions updated. No new WPs. |
| `project-brain/PROJECT_BRAIN.md` | Registered scope, consumer classes, ownership, pilot boundary, DEC-S-007…012, RISK-006…009, next step. |
| `README.md` | Scope section, consumers section, pilot boundary, WP status, register ranges, governance links. |
| `CLAUDE.md` | WP pointers; context pack and normative scope references with a precedence statement. Existing Skills-first, fail-closed, and Git rules preserved verbatim. |
| `CHANGELOG.md` | CDS-WP-002 entries under Unreleased. No version or release announced. |

## Scope model

Six capability domains (DEC-S-007): Brand and Identity; Experience and
Interaction; Foundations and Tokens; Components and Patterns; Channels and
Communication; Governance and Enablement. Ten cross-cutting concerns apply
across all six as quality requirements, explicitly not conformance claims.

Statements are classified as normative, current phase scope, long-term
direction, deferred decision, or assumption — so that registered scope cannot
be read as a delivery promise (DEC-S-009).

Twelve non-goals are registered. Five of them — business logic, domain data,
backend architecture, security architecture, deployment and operations — are
recorded in the matrix as permanent out-of-scope rather than deferrals.

## Consumer classification

Three relationship classes (DEC-S-010): Core Product Consumer, Associated
Project Consumer, Potential External Consumer. Eight direct user roles and five
indirect beneficiary groups are registered. Roles are functions, not positions;
no organizational size or design department is assumed.

The classification is explicitly bounded: it grants no endorsement, brand
usage, availability, licensing, support, delivery commitment, decision
influence, or conformance status. It is a relationship model, not a brand
architecture.

## Boundary decisions

CDS owns normative shared design rules and accepted shared artifacts; consumers
own product strategy, business logic, domain data, backend, security
architecture, operations, and integration of a chosen CDS version (DEC-S-008).
Shared and contract-controlled areas require explicit coordination, with the
governance deferred to CDS-WP-006.

The CoreOps pilot boundary sets four cumulative conditions before a
CoreOps solution becomes normative: multi-consumer relevance or documented
generalizability, a check against CDS principles, explicit acceptance through a
CDS work package, and the ability to document, test, and version it
(DEC-S-011).

## Decision extension

DEC-S-007 … DEC-S-012 added, all Accepted, dated 2026-07-15, marked as
strategic scope decisions. DEC-S-001 … DEC-S-006 unchanged. No ADR created.
Range now DEC-S-001 … DEC-S-012, count 12.

## Risk extension

RISK-006 … RISK-009 added, all Monitored, qualitative likelihood and severity
only, owner roles marked provisional until CDS-WP-006. Existing risks not
redefined; RISK-002 gained only a cross-reference. Range now
RISK-001 … RISK-009, count 9.

Each new risk is tied to the decision that mitigates it: RISK-006 → DEC-S-008,
RISK-007 → DEC-S-009, RISK-008 → DEC-S-010 and DEC-S-011, RISK-009 →
DEC-S-012.

## Context Pack creation

The Foundation Context Pack opens with an explicit precedence disclaimer —
normative sources take precedence, and where the pack disagrees it is wrong and
must be corrected. It carries a normative source map pointing to the real
documents rather than reproducing them, and summarizes identity, phase,
completed WPs, decisions, risks, principles, scope, consumer classes, pilot
boundary, prohibitions, deferred decisions, repository constraints,
Skills-first instructions, and the next WP.

## Validations performed

| # | Check | Result |
| --- | --- | --- |
| 1 | Only Allowed Files changed or created | Pass |
| 2 | Git status reviewed | Pass |
| 3 | Full diff reviewed | Pass |
| 4 | `git diff --check` | Pass |
| 5 | Relative internal file references | Pass — no broken link |
| 6 | Six scope domains present | Pass |
| 7 | Cross-cutting concerns present | Pass — all 10 |
| 8 | Three consumer classes present | Pass |
| 9 | Binding non-goals | Pass — all 12 |
| 10 | CDS versus consumer ownership boundary | Pass |
| 11 | CoreOps pilot boundary | Pass |
| 12 | No concrete visual decisions | Pass |
| 13 | No tool, framework, or token-format decisions | Pass |
| 14 | No public release, licensing, or support commitments | Pass |
| 15 | Decision range and count DEC-S-001…012, exactly 12 | Pass |
| 16 | Risk range and count RISK-001…009, exactly 9 | Pass |
| 17 | No ADR created | Pass |
| 18 | Work-package status consistency | Pass |
| 19 | Skill files unchanged | Pass — 39/39 hash-match |
| 20 | Skills manifest and provenance unchanged | Pass |
| 21 | Context Pack references normative sources and is not one | Pass |
| 22 | Only authorized Skills used | Pass — the 7 named |
| 23 | No Git write action | Confirmed |

## Deviations

None. The work package was executed within the defined scope and Allowed Files.

## Open notes

- The neutrality-guard applicability boundary is documented above: naming Core
  product names is correct in this repository and required by the prompt.
- Five non-goals are recorded in the matrix as **permanent** out-of-scope. This
  is a sharper statement than "not now" and is deliberate; reversing one needs
  a governance decision.
- The matrix carries five open boundary questions routed to CDS-WP-004 and
  CDS-WP-005 — most notably where a shared pattern ends and product-specific
  UX begins, and who owns a component only one consumer currently needs.
- Six assumptions are registered explicitly and remain unvalidated until
  CDS-WP-003 and CDS-WP-004.
- Licensing and publication carry no assigned work package. If Nova wants them
  resolved inside the Foundation phase, a work package must be planned; the
  roadmap must not be extended by Claude.
- All changes are uncommitted. Commit authority rests with the Human
  Maintainer.

## Completion status

CDS-WP-002 is Completed against its Definition of Done and reported for Human
Maintainer review.
