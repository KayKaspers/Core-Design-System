# Core Design System — Project Brain

Compact long-term orientation for the Core Design System (CDS). This document
summarizes; it does not duplicate the normative documents it points to.

- **Project:** Core Design System (CDS)
- **Repository:** KayKaspers/Core-Design-System
- **Local path:** `D:\Projects\Core-Design-System`
- **Framework:** Nova Development Framework v1.0.0
- **Phase:** Foundation / Pre-Design

## Strategic purpose

CDS is the central design and brand foundation for the Core ecosystem — a
versioned platform product providing a normative Single Source of Truth.

Its long-term scope reaches well beyond UI components: brand strategy,
corporate identity, corporate design, design principles, UX, UI, components,
design tokens, colors, typography, icons, logos, GitHub presentation, document
design, PDF layouts, presentations, diagram standards, dashboards,
accessibility, motion, marketing materials, and product-family governance.

That scope is long-term. It does not authorize concrete work in any of those
areas today.

## Core principles

- CDS is a versioned platform product, not a logo project, branding kit, or
  isolated component library.
- CDS must be usable by real Core products.
- Normative sources must not depend solely on a proprietary design tool.
- Normative sources and generated artifacts must stay clearly separated.
- Generated output is never an authoritative source.
- Design decisions must be versioned, documented, reviewable, and testable.
- Accessibility is designed in rather than added later.
- Offline and self-hosted usability are core requirements.
- Product individuality must be controlled and governable.
- AI may assist; normative approval remains human.
- Concrete visual and technical decisions come only from explicitly authorized
  work packages.

## Roles

| Role | Authority |
| --- | --- |
| Human Maintainer (Kay) | Final normative approvals; exclusive Git-write, tag, release, publication, and repository-visibility authority. |
| Nova | Strategy, architecture, work-package planning, review, project control, approval recommendations. |
| Claude | Scoped local analysis and file work only; no Git writes, no publication. |
| Consumer projects | Requirements input and adoption evidence. |

## Current state

Governance foundation established. No final design or technology decisions are
approved.

- Decisions: DEC-S-001 … DEC-S-012 (12) — 6 foundation + 6 scope decisions;
  unchanged by CDS-WP-003
- Risks: RISK-001 … RISK-013 (13) — owner model provisional until CDS-WP-006
- Completed work packages: CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003
- Next work package: CDS-WP-004

## Registered scope

Scope is registered normatively in
[Concept and Scope](../docs/governance/CONCEPT_AND_SCOPE.md).

Six capability domains (DEC-S-007): Brand and Identity · Experience and
Interaction · Foundations and Tokens · Components and Patterns · Channels and
Communication · Governance and Enablement.

Cross-cutting concerns: accessibility, inclusive design, localization and
internationalization, offline and self-hosted use, security-aware interaction
design, privacy-aware interaction design, maintainability, provenance and
licensing, quality evidence, design-code-documentation alignment. These are
quality requirements — not certification or conformance claims.

**Registration is not availability.** Long-term scope creates no delivery,
stability, support, release, or compatibility commitment (DEC-S-009).

Currently active: concept, scope, non-goals, user groups, consumer classes,
ownership boundaries, governance foundations, and planning for the remaining
Foundation work packages. Not implemented: brand identity, visual design,
components, tokens, tools, packages, public releases.

## Consumer classes and ownership

Three relationship classes (DEC-S-010): Core Product Consumer · Associated
Project Consumer · Potential External Consumer. Classification grants no brand
endorsement, public availability, licensing rights, or support. It is a
relationship model, not a brand architecture. See
[Consumer and Stakeholder Model](../docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md).

CDS owns normative shared design rules and accepted shared artifacts; consumers
own product strategy, business logic, domain data, backend, security
architecture, operations, and integration of a chosen CDS version (DEC-S-008).
Permanent non-goals: business logic, domain data, backend architecture,
security architecture, deployment and operations. Shared/contract-controlled
areas — new shared components and patterns, profiles, overrides, migrations,
breaking changes, conformance claims — are governed in CDS-WP-006. Per-area
split: [Scope Boundary Matrix](../docs/governance/SCOPE_BOUNDARY_MATRIX.md).

## CoreOps pilot boundary

CoreOps is the first reference consumer and supplies real requirements and
validation cases, but does not alone determine CDS architecture.
CoreOps-specific solutions stay CoreOps-owned unless multi-consumer relevant or
justifiably generalizable, checked against CDS principles, explicitly accepted
via a CDS work package, and documentable, testable, and versionable
(DEC-S-011). Pilot contract: CDS-WP-004.

## NDF Skills

The released NDF v1.0.0 Claude Skills are adopted locally under
`.claude/skills/`, pinned to commit
`9dcadc12fb960914b9a5baeff2ab1aee75912b57`.

- 38 docs-only Skills, all verified byte-identical against the released tag.
- Provenance and a machine-readable hash manifest exist.
- The local copy is a pinned consumption copy, not an independent fork.
- **Skills-first operating mode is active:** select only the Skills relevant to
  the assignment, never load all 38 by default, and never let a Skill extend
  scope or Allowed Files. Prompt and Human Maintainer gates override any Skill.
- Skill updates require a separate authorized Skill-Maintenance work package.

Details: [Provenance](../docs/governance/NDF_SKILLS_PROVENANCE.md) ·
[Inventory](../project-system/NDF_SKILLS_INVENTORY.md) ·
[Manifest](../project-system/NDF_SKILLS_MANIFEST.json)

## Decisions in force

| ID | Summary |
| --- | --- |
| DEC-S-001 | CDS is a versioned platform product and normative design foundation. |
| DEC-S-002 | CoreOps is the first reference consumer, not the sole target or requirement source. |
| DEC-S-003 | Governance, scope, architecture, and requirements precede concrete design decisions. |
| DEC-S-004 | Normative sources must remain tool-independent; no proprietary tool as sole source of truth. |
| DEC-S-005 | Human Maintainer holds exclusive authority over Git writes, releases, publication, and approvals. |
| DEC-S-006 | Artifacts and consumer usage must support offline and self-hosted operation. |
| DEC-S-007 | Scope classified through six capability domains plus cross-cutting concerns. |
| DEC-S-008 | CDS owns shared design rules; consumers own their products. |
| DEC-S-009 | Long-term scope is not a delivery, support, or compatibility commitment. |
| DEC-S-010 | Three consumer relationship classes; classification grants nothing. |
| DEC-S-011 | Pilot results become normative only when generalized and accepted. |
| DEC-S-012 | Adoption/conformance claims require a version reference and evidence. |

Details: [Decision Index](../docs/decisions/DECISION_INDEX.md)

## Active risks

| ID | Summary | Status |
| --- | --- | --- |
| RISK-001 | Uncontrolled scope expansion. | Monitored |
| RISK-002 | CoreOps overfitting. | Monitored |
| RISK-003 | Premature design decisions. | Monitored |
| RISK-004 | Tool lock-in and source divergence. | Monitored |
| RISK-005 | Design, code, and documentation drift. | Monitored |
| RISK-006 | Ownership boundary ambiguity. | Monitored |
| RISK-007 | Long-term scope interpreted as current commitment. | Monitored |
| RISK-008 | Consumer fragmentation. | Monitored |
| RISK-009 | Misleading adoption or association claims. | Monitored |
| RISK-010 | Benchmark imitation. | Monitored |
| RISK-011 | Research and source bias. | Monitored |
| RISK-012 | Source volatility. | Monitored |
| RISK-013 | Differentiation overstatement. | Monitored |

Owner model provisional until CDS-WP-006.
Details: [Risk Register](../docs/risks/RISK_REGISTER.md)

## Benchmark research (CDS-WP-003)

**Non-normative evidence**, snapshot dated 2026-07-15. No decision was added or
changed.

Ten systems reviewed against 14 dimensions from official publisher sources only:
Carbon, Fluent 2, Material 3, Primer, Atlassian, Spectrum (with Spectrum 2), SAP
Fiori, SLDS 2, GOV.UK, USWDS.

Key cross-system findings:

- Foundations → components → patterns is settled industry structure, not a
  differentiator.
- Token workflows are often coupled to a proprietary design tool, and this is
  rarely documented as a risk — evidence supporting DEC-S-004 and RISK-004.
- No reviewed system documented PDF, presentation, or diagram standards; they
  are product-interface systems that touch brand at the edges.
- No reviewed system stated an explicit offline or self-hosted guarantee,
  though self-containable distribution is common.
- Every system permits product-level variation; none published the limits of it.
- Strongest observed practices: published per-component maturity states,
  published accessibility conformance evidence, explicitly stating what the
  system does **not** guarantee, and naming who maintains each contributed part.
- Licensing is never one decision: documentation, code, fonts, icons, and brand
  assets routinely sit on different terms.

Hypotheses HYP-001 … HYP-008 are all **Research hypotheses**. None reached
"Strongly supported". HYP-006 (evidence-based adoption) is common industry
practice; HYP-003 (operational patterns) was not verifiable. Claims rest on
absence from public documentation — weaker evidence than presence.

Details: [Benchmark](../docs/research/DESIGN_SYSTEM_BENCHMARK.md) ·
[Hypotheses](../docs/research/CDS_DIFFERENTIATION_HYPOTHESES.md) ·
[Limitations](../docs/research/RESEARCH_LIMITATIONS.md)

## Intentionally open decisions

No final decision exists for: logo, logo architecture, colors, typography,
icons, illustration, imagery, dark theme, light theme, design tool, component
framework, token format, token build system, documentation platform, package
architecture, repository split, license, public release, contribution model,
long-term compatibility commitments, concrete product signatures, versioning
and maturity model, conformance and adoption policy, or product profile and
override governance.

## Next step

CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract: collect
requirements from CoreOps and the further consumer classes, separate shared from
product-specific requirements, define the pilot scope and validation contract,
and test HYP-001 … HYP-008 against real consumer needs rather than against
absence of public documentation. Still no concrete visual design and no
technology selection. Requires an explicit work-package prompt from Nova.

## Related documents

- [Concept and Scope](../docs/governance/CONCEPT_AND_SCOPE.md) — normative scope source
- [Consumer and Stakeholder Model](../docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md)
- [Scope Boundary Matrix](../docs/governance/SCOPE_BOUNDARY_MATRIX.md)
- [Foundation Context Pack](../project-system/CONTEXT_PACK_FOUNDATION.md)
- [Project Charter](../docs/governance/PROJECT_CHARTER.md)
- [Project Profile](../project-system/PROJECT_PROFILE.md)
- [Work Packages](../project-system/WORK_PACKAGES.md)
- [Next Phase](../project-system/NEXT_PHASE.md)
- [CDS-WP-001 Governance Bootstrap Notes](CDS_WP_001_GOVERNANCE_BOOTSTRAP_NOTES.md)
- [CDS-WP-002 Concept and Scope Registration Notes](CDS_WP_002_CONCEPT_AND_SCOPE_REGISTRATION_NOTES.md)
- [CDS-WP-003 Benchmark and Differentiation Research Notes](CDS_WP_003_BENCHMARK_AND_DIFFERENTIATION_RESEARCH_NOTES.md)
