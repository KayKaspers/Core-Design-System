# Foundation Context Pack

> **Normative source documents take precedence over this context summary.**
>
> This pack is a compact handover aid for continuation sessions. It summarizes;
> it never defines. Where it disagrees with a normative source, the normative
> source wins and this pack is wrong and must be corrected.

- **Maintained by:** CDS-WP-002
- **Date:** 2026-07-15

## Project identity

- Project: Core Design System (CDS)
- Repository: KayKaspers/Core-Design-System
- Local path: `D:\Projects\Core-Design-System`
- Framework: Nova Development Framework v1.0.0
- Type: versioned platform product and normative design foundation (DEC-S-001)

## Current phase

Foundation / Pre-Design.

Governance, scope, architecture, and requirements are established before
concrete visual or technical design decisions are authorized (DEC-S-003).

## Completed work packages

| WP | Title | Result |
| --- | --- | --- |
| CDS-WP-001 | Project Governance and NDF Bootstrap | Charter, authority model, DEC-S-001…006, RISK-001…005, initial roadmap. |
| CDS-WP-001A | NDF Skills Bootstrap | 38 verified docs-only NDF v1.0.0 Skills; provenance, manifest, inventory; Skills-first mode active. |
| CDS-WP-002 | Concept and Scope Registration | Concept and scope, consumer model, boundary matrix, DEC-S-007…012, RISK-006…009, this pack. |

## Normative source map

Read the source, not this summary, when the detail matters.

| Topic | Normative source |
| --- | --- |
| Concept, scope, non-goals, ownership, pilot boundary | [docs/governance/CONCEPT_AND_SCOPE.md](../docs/governance/CONCEPT_AND_SCOPE.md) |
| Consumer classes, users, stakeholders | [docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md](../docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md) |
| Per-area responsibility split | [docs/governance/SCOPE_BOUNDARY_MATRIX.md](../docs/governance/SCOPE_BOUNDARY_MATRIX.md) |
| Mission, vision, authority model, phase boundary | [docs/governance/PROJECT_CHARTER.md](../docs/governance/PROJECT_CHARTER.md) |
| Decisions | [docs/decisions/DECISION_INDEX.md](../docs/decisions/DECISION_INDEX.md) |
| Risks | [docs/risks/RISK_REGISTER.md](../docs/risks/RISK_REGISTER.md) |
| Working rules, Skills-first mode | [CLAUDE.md](../CLAUDE.md) |
| Roadmap and status | [project-system/WORK_PACKAGES.md](WORK_PACKAGES.md) |
| Skills provenance | [docs/governance/NDF_SKILLS_PROVENANCE.md](../docs/governance/NDF_SKILLS_PROVENANCE.md) |

## Active decisions

- Range: DEC-S-001 … DEC-S-012 · Count: 12 · All Accepted
- DEC-S-001…006: strategic foundation decisions (CDS-WP-001)
- DEC-S-007…012: strategic scope decisions (CDS-WP-002)
- No ADR files exist.

| ID | Summary |
| --- | --- |
| DEC-S-001 | CDS is a versioned platform product and normative design foundation. |
| DEC-S-002 | CoreOps is first reference consumer, not sole target or requirement source. |
| DEC-S-003 | Governance precedes concrete design decisions. |
| DEC-S-004 | Normative sources stay tool-independent. |
| DEC-S-005 | Human Maintainer holds exclusive Git, release, publication, and approval authority. |
| DEC-S-006 | Offline and self-hosted operation must remain possible. |
| DEC-S-007 | Scope classified through six capability domains plus cross-cutting concerns. |
| DEC-S-008 | CDS owns shared design rules; consumers own their products. |
| DEC-S-009 | Long-term scope is not a delivery, support, or compatibility commitment. |
| DEC-S-010 | Three consumer relationship classes; classification grants nothing. |
| DEC-S-011 | Pilot results become normative only when generalized and accepted. |
| DEC-S-012 | Adoption/conformance claims require a version reference and evidence. |

## Active risks

- Range: RISK-001 … RISK-009 · Count: 9 · All Monitored
- Owner model is **provisional** until CDS-WP-006.

| ID | Summary |
| --- | --- |
| RISK-001 | Uncontrolled scope expansion. |
| RISK-002 | CoreOps overfitting. |
| RISK-003 | Premature design decisions. |
| RISK-004 | Tool lock-in and source divergence. |
| RISK-005 | Design, code, and documentation drift. |
| RISK-006 | Ownership boundary ambiguity. |
| RISK-007 | Long-term scope interpreted as current commitment. |
| RISK-008 | Consumer fragmentation. |
| RISK-009 | Misleading adoption or association claims. |

## Approved strategic principles

- CDS is a platform product, not a logo project, branding kit, or isolated
  component library.
- Normative sources must not depend solely on a proprietary design tool;
  generated output is never authoritative.
- Accessibility is designed in, not added later — but nothing is certified.
- Offline and self-hosted usability are core requirements.
- Product individuality must be controlled and governable.
- AI may assist; normative approval remains human.
- Concrete visual and technical decisions require explicit authorization.

## Registered scope domains

Six capability domains (DEC-S-007): **Brand and Identity** · **Experience and
Interaction** · **Foundations and Tokens** · **Components and Patterns** ·
**Channels and Communication** · **Governance and Enablement**.

Cross-cutting concerns: accessibility, inclusive design, localization and
internationalization, offline and self-hosted use, security-aware interaction
design, privacy-aware interaction design, maintainability, provenance and
licensing, quality evidence, design-code-documentation alignment.

**Registration is not availability.** Long-term scope creates no delivery,
stability, support, release, or compatibility commitment (DEC-S-009).
Cross-cutting concerns are quality requirements, not certification or
compliance claims.

Currently active: concept, scope and non-goals, user groups, consumer classes,
ownership boundaries, governance foundations, and planning for benchmark,
requirements, architecture, accessibility, release/contribution/maturity.

Not implemented in this phase: brand identity, visual designs, components,
tokens, tools, frameworks, packages, public releases.

## Consumer classes

Three classes (DEC-S-010): **Core Product Consumer** (e.g. CoreOps, SpeakCore,
CastCore, AirCore) · **Associated Project Consumer** · **Potential External
Consumer**.

Classification grants no brand endorsement, public availability, licensing
rights, or support. Public availability, licensing, and support are undecided.
This is a relationship model, not a brand architecture.

## Ownership boundary

CDS owns normative shared design rules and accepted shared artifacts.
Consumers own product strategy, business logic, domain data, backend, security
architecture, operations, and integration of a chosen CDS version (DEC-S-008).

Permanent non-goals: business logic, domain data, backend architecture,
security architecture, deployment and operations.

Shared/contract-controlled: new shared components and patterns, product profile
overrides, extensions, migrations, breaking changes, pilot requirements,
conformance claims. Governance deferred to CDS-WP-006.

## CoreOps pilot boundary

CoreOps is the first reference consumer, supplying real requirements and
validation cases. It does not alone determine CDS architecture.
CoreOps-specific solutions stay CoreOps-owned unless they are multi-consumer
relevant or justifiably generalizable, checked against CDS principles,
explicitly accepted via a CDS work package, and documentable, testable, and
versionable (DEC-S-011). Pilot contract deferred to CDS-WP-004.

## Explicit prohibitions

Claude must not: commit, push, pull, fetch, clone, merge, rebase, cherry-pick,
create or switch branches, tag, release, publish, or rewrite history.

Claude must not decide or implement: logos, colors, typography, icons,
illustration, imagery, themes, visual language, design tooling, component
frameworks, token formats or build systems, documentation platforms, package
architecture, repository split, license, public release, contribution model,
compatibility commitments, or product signatures.

Claude must not: install dependencies, create executable product code,
download external assets, modify Skill files, or change files outside the
active work package's Allowed Files.

No claim of certification, legal compliance, accessibility conformance, public
availability, or support may be made.

## Deferred decisions

Logo and logo architecture · colors · typography · icons · illustration ·
imagery · themes · design tool · component framework · token format · token
build system · documentation platform · package architecture · repository
split · license · public release · contribution model · compatibility
commitments · product signatures · versioning and maturity model · conformance
and adoption policy · product profile and override governance.

## Repository constraints

- Branch `main`; remote `origin` configured.
- Human Maintainer performs all Git writes; Claude's changes stay uncommitted.
- `.claude/skills/` holds 38 verified Skills / 39 files, pinned to NDF v1.0.0
  commit `9dcadc12fb960914b9a5baeff2ab1aee75912b57`. Never modify during
  product work.
- `.claude/rules/`, `docs/architecture/`, `docs/research/`, `docs/roadmap/` are
  empty placeholders.

## Skills-first instructions

1. Read `CLAUDE.md` and the project-control files first.
2. Select only the Skills relevant to the concrete assignment; never load all
   38 by default; read only the necessary sections.
3. Skills are procedural support, never authorization. A Skill never extends
   scope, Allowed Files, authority, decisions, or Git rights.
4. The work-package prompt and Human Maintainer gates override any Skill.
5. On conflict between prompt, project control, and Skill: fail closed and
   report to Nova.
6. Never modify a Skill file outside an authorized Skill-Maintenance work
   package.
7. Name the Skills actually used in the report to Nova.

## Current and next work package

- **Completed:** CDS-WP-002 — Concept and Scope Registration
- **Next:** CDS-WP-003 — Benchmark and Differentiation Research

CDS-WP-003 analyzes established design systems and derives the CDS
differentiation position. It stays analysis- and documentation-oriented. No
visual elements or foreign design content are copied. Concrete research sources
and any web research require explicit authorization in the CDS-WP-003 prompt —
they are not authorized by this pack. No final tool, branding, or technology
decision.

Being listed as Next identifies sequence, not authorization. Every work package
needs an explicit prompt from Nova.
