# Core Design System

The Core Design System (CDS) is the central design, brand, user-experience,
interface, component, token, document, and multi-channel foundation for the Core
product ecosystem.

CDS is being built as a versioned platform product with a normative Single
Source of Truth. It is deliberately **not**:

- a logo-only project,
- a branding kit,
- an isolated UI component library,
- a design project scoped exclusively to CoreOps.

## Project status

**Foundation / Pre-Design**

The project currently establishes governance, scope, architecture, and
requirements. It does not yet produce visual design.

The concept and scope are registered. See
[Concept and Scope](docs/governance/CONCEPT_AND_SCOPE.md) for the normative
source.

No final decision exists for:

- logo and logo architecture,
- colors,
- typography,
- icons, illustration, and imagery,
- light and dark themes,
- design tool,
- component framework,
- token format and token build system,
- documentation platform,
- package architecture and repository split,
- license, public release, and contribution model,
- long-term compatibility commitments,
- concrete product signatures,
- versioning and maturity model,
- conformance and adoption policy.

These areas remain open until an explicitly authorized work package decides
them.

## Scope

The long-term scope is classified through six capability domains:

1. **Brand and Identity**
2. **Experience and Interaction**
3. **Foundations and Tokens**
4. **Components and Patterns**
5. **Channels and Communication**
6. **Governance and Enablement**

Cross-cutting quality concerns apply across all six, including accessibility,
inclusive design, localization, offline and self-hosted use, maintainability,
and design-code-documentation alignment.

**Registration is not availability.** Long-term scope creates no delivery,
stability, support, release, or compatibility commitment. Cross-cutting
concerns are quality requirements — CDS makes no certification, legal-
compliance, or accessibility-conformance claim.

Active in this phase: concept, scope and non-goals, user groups, consumer
classes, ownership boundaries, governance foundations, and planning for the
remaining Foundation work packages.

## Consumers

CDS distinguishes three consumer relationship classes:

| Class | Meaning |
| --- | --- |
| Core Product Consumer | A Core ecosystem product that may pursue comprehensive or profiled adoption. |
| Associated Project Consumer | An associated project that may use selected foundations without full master-brand membership. |
| Potential External Consumer | A possible future external user. Availability, licensing, and support are undecided. |

Classification grants no brand endorsement, public availability, licensing
rights, or support. It is a relationship model, not a brand architecture.

The per-area responsibility split between CDS and consumer projects is
registered in the [Scope Boundary Matrix](docs/governance/SCOPE_BOUNDARY_MATRIX.md).

## Pilot consumer

CoreOps is the first reference consumer of stable CDS foundations and provides
adoption evidence.

CoreOps is a reference consumer — not the sole design target and not the sole
source of requirements. SpeakCore, CastCore, AirCore, and future Core products
are anticipated consumers.

CoreOps does not alone determine CDS architecture. CoreOps-specific solutions
remain CoreOps-owned unless they are generalized and explicitly accepted
through a CDS work package. The concrete pilot contract is defined in
CDS-WP-004.

## Operating model

This project follows the Nova Development Framework v1.0.0.

| Role | Authority |
| --- | --- |
| Human Maintainer | Final normative approvals; exclusive authority over commit, push, merge, branch operations, tag, release, and publication. |
| Nova | Strategy, architecture, work-package planning, review, project control, approval recommendations. |
| Claude | Scoped local analysis and file work; no Git writes, no publication. |
| Consumer projects | Requirements input and adoption evidence. |

Claude Desktop with a locally connected repository is the execution environment
for Claude work.

### Skills-first operating mode

**Active.** The NDF v1.0.0 Skills Bootstrap is complete: 38 locally verified
docs-only Skills are available under `.claude/skills/`, pinned byte-identical to
the released NDF v1.0.0 tag.

Claude selects only the Skills relevant to a given work package rather than
loading all of them. Skills provide procedural support; they never extend scope
or override the work-package prompt or the Human Maintainer gates.

- [NDF Skills Provenance](docs/governance/NDF_SKILLS_PROVENANCE.md)
- [NDF Skills Inventory](project-system/NDF_SKILLS_INVENTORY.md)

## Work packages

- **Completed:** CDS-WP-001 — Project Governance and NDF Bootstrap
- **Completed:** CDS-WP-001A — NDF Skills Bootstrap
- **Completed:** CDS-WP-002 — Concept and Scope Registration
- **Next:** CDS-WP-003 — Benchmark and Differentiation Research

The full controlled roadmap is in
[project-system/WORK_PACKAGES.md](project-system/WORK_PACKAGES.md).

## Registers

- Decisions: DEC-S-001 … DEC-S-012 (12) — 6 strategic foundation decisions,
  6 strategic scope decisions
- Risks: RISK-001 … RISK-009 (9) — owner model provisional until CDS-WP-006

## Governance documents

- [Concept and Scope](docs/governance/CONCEPT_AND_SCOPE.md) — normative scope source
- [Consumer and Stakeholder Model](docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md)
- [Scope Boundary Matrix](docs/governance/SCOPE_BOUNDARY_MATRIX.md)
- [Project Charter](docs/governance/PROJECT_CHARTER.md)
- [Decision Index](docs/decisions/DECISION_INDEX.md)
- [Risk Register](docs/risks/RISK_REGISTER.md)
- [Project Profile](project-system/PROJECT_PROFILE.md)
- [Foundation Context Pack](project-system/CONTEXT_PACK_FOUNDATION.md)
- [Work Packages](project-system/WORK_PACKAGES.md)
- [Next Phase](project-system/NEXT_PHASE.md)
- [Project Brain](project-brain/PROJECT_BRAIN.md)
- [Claude working instructions](CLAUDE.md)

## Repository status

This repository is initially private.

Licensing, public-release policy, contribution policy, and compatibility
commitments remain intentionally undecided.
