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

- Decisions: DEC-S-001 … DEC-S-032 (32) — 6 foundation + 6 scope + 8 consumer
  and pilot scope + 12 logical architecture decisions
- Risks: RISK-001 … RISK-028 (28) — owner model provisional until CDS-WP-006
- Completed work packages: CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005
- Next work package: CDS-WP-006

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
| DEC-S-013 | Consumer evidence must be bound to a committed revision. |
| DEC-S-014 | Consumer requirements are classified; classification is not approval. |
| DEC-S-015 | The initial CoreOps pilot is a bounded slice, not adoption or conformance. |
| DEC-S-016 | Generalization requires explicit review and acceptance. |
| DEC-S-017 | Pilot outcomes are evaluated through version-bound evidence. |
| DEC-S-018 | Secondary consumers provide evidence, not pilot authority. |
| DEC-S-019 | Consumer need does not establish differentiation. |
| DEC-S-020 | CDS-WP-004 authorizes requirements and a contract only. |
| DEC-S-021 | Eight-layer logical architecture. |
| DEC-S-022 | Authority divided by artifact class. |
| DEC-S-023 | Conflicts fail closed; recency never confers authority. |
| DEC-S-024 | Token flow: Reference → Semantic → Component → Profile → Output. |
| DEC-S-025 | Profiles modify approved extension points only. |
| DEC-S-026 | Existing product designs are reconciled, not overwritten. |
| DEC-S-027 | Operations patterns are a domain family, not the foundation. |
| DEC-S-028 | Status axes separated; unknown is never healthy. |
| DEC-S-029 | Channels share semantics; rendering may differ. |
| DEC-S-030 | Distribution supports offline, pinning, reproducibility. |
| DEC-S-031 | Artifacts stay traceable to source revisions. |
| DEC-S-032 | The architecture is technology-independent. |

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
| RISK-014 | Consumer evidence staleness. | Monitored |
| RISK-015 | Pilot scope inflation. | Monitored |
| RISK-016 | Product-specific requirement contamination. | Monitored |
| RISK-017 | Document evidence mistaken for user validation. | Monitored |
| RISK-018 | Pilot contract mistaken for adoption or conformance. | Monitored |
| RISK-019 | Secondary consumer underrepresentation. | Monitored |
| RISK-020 | Normative-source authority ambiguity. | Monitored |
| RISK-021 | Token and override proliferation. | Monitored |
| RISK-022 | Existing-product reconciliation failure. | Monitored |
| RISK-023 | Domain-pattern leakage into the universal foundation. | Monitored |
| RISK-024 | Channel divergence. | Monitored |
| RISK-025 | Generated-artifact provenance loss. | Monitored |
| RISK-026 | Architecture overdesign. | Monitored |
| RISK-027 | Product-profile fragmentation. | Monitored |
| RISK-028 | Deferred accessibility policy creates architecture debt. | Monitored |

Owner model provisional until CDS-WP-006.
Details: [Risk Register](../docs/risks/RISK_REGISTER.md)

## Logical architecture (CDS-WP-005)

**Normative structure. Selects no technology and no design** (DEC-S-032).

**Eight layers** (DEC-S-021): Strategy and Governance · Brand and Identity ·
Foundations and Tokens · Components · Patterns and Experiences · Channels and
Communication · Distribution and Enablement · Evidence and Quality. Dependencies
run **downward only**.

**Source-of-truth model** (DEC-S-022, DEC-S-023): eight artifact classes. Only
normative human-readable sources (meaning) and normative machine-readable sources
(values) bind. Generated artifacts, design-tool state, reference implementations,
consumer-local artifacts, evidence, and research are **never normative**.
Conflicts **fail closed** — recency confers no authority, which matters because
recency-wins is the silent default of most tooling.

**Token flow** (DEC-S-024): Reference → Semantic → Component → Product Profile
Overrides → Channel/Platform Outputs. Semantic-first; a component binding a
reference token directly is a defect. No format, naming, or tool chosen — the
reviewed interoperability draft is explicitly not implementable.

**Product Profile and Extension Model** (DEC-S-025, DEC-S-026): Core Foundation ·
Product Profile · Consumer Extension · Domain Pattern Family · Local Exception.
Profiles may never redefine shared semantics, weaken accessibility, distort
status truth, or break contracts — a profile needing any of these is a fork.

**Reconciliation:** SpeakCore and CastCore already hold their own design
decisions, so CDS arrives late. Flow: inventory → semantic mapping → conflict
identification → classification → profile candidate, consumer-local retention, or
migration → evidence. Mapping is **semantic, not value-level**. Retention is a
valid final outcome. No overwrite, no retrospective conformance.

**Operations patterns** are a **Domain Pattern Family** above the universal
foundation (DEC-S-027): the consumer need is confirmed, but all three consumers
are infrastructure products, so generalizability is untested (RISK-023).

**Consumer contracts:** Source · Transformation · Distribution · Integration ·
Adoption Evidence.

**Status invariant** (DEC-S-028): five separated axes — operational condition,
severity, knowledge confidence, freshness, evidence availability. **Unknown is
not Healthy. Stale is not Current. Unverified is not Verified.** Placed in the
architecture rather than in convention, because a convention can be forgotten
under deadline.

**Requirement coverage:** CR-001…040 fully mapped — 8 addressed, 24 partially
addressed, 4 deferred to later policy, 2 consumer-owned, 2 out of scope. Only 8
of 40 fully addressed is the **expected** result: an architecture resolving most
requirements would be doing unauthorized design work.

Details: [Architecture](../docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md) ·
[Authority](../docs/architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md) ·
[Coverage](../docs/architecture/ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md)

## Consumer requirements and the CoreOps pilot (CDS-WP-004)

Three consumers analyzed **read-only** at committed revisions: CoreOps (primary
pilot, `399de21c`), SpeakCore (`a5e69771`), CastCore (`6c7614e3`). 15 sources
read, 14 usable. **Documentation only — no user research took place** (RISK-017).

**Requirements CR-001 … CR-040 (40):** Shared CDS Candidate 25 · CoreOps Pilot
Requirement 2 · Product-local 2 · Deferred 9 · Out of CDS Scope 2. Pilot-relevant
28. Classification is **not** approval (DEC-S-014).

Central shared requirements:

- **Status semantics** — graded status documented by all three consumers;
  semantic, never colour-only, always with text or icon (CR-006). Two consumers
  independently require that **unknown must never read as healthy** (CR-007).
  This is the clearest multi-consumer signal found.
- **Safety before execution** — risk-tiered actions, preview or plan before
  execute, deliberate confirmation with a cancel path, no misleading success
  (CR-010 … CR-013).
- **Complete state set** including offline, degraded, permission denied, and
  unavailable capability (CR-015, CR-016, CR-032).
- **Offline and self-hosted** without mandatory external runtime services
  (CR-031) — a confirmed, accepted consumer requirement.
- **DE/EN** with flexible text length (CR-023), enforced in CI by one consumer.
- **Simple and Expert mode** plus guided setup with an environment check
  (CR-017, CR-018) — documented by all three.

Product-specific boundaries: SpeakCore and CastCore **already hold their own
style direction, palette, and tokens** (CR-002, CR-037). CDS arrives after those
decisions — this is reconciliation, not a blank slate. Business logic, domain
data, backend, security architecture, and operations stay consumer-owned
(CR-035, CR-036; permanent non-goals).

**CoreOps pilot** — a bounded slice, **not** a redesign (DEC-S-015). Groups
A Application Foundation · B Operations Overview · C Inventory and Dense Data ·
D State and Safety Patterns · E Help, Accessibility, Localization. 9 scenarios.
The contract is normative only upon Human Maintainer commit following Nova
approval; **entry criteria are unmet and no pilot has started**.

**Hypothesis consumer layer:** HYP-002 offline, HYP-003 operations patterns, and
HYP-005 governed family flexibility are *Confirmed consumer need*; HYP-007
requires *Human validation* (accessibility is weak in both layers); the rest are
partially supported. CDS-WP-003 research assessments are **unchanged**. A
confirmed need is never a differentiation claim (DEC-S-019).

Details: [Requirements](../docs/governance/CONSUMER_REQUIREMENTS_MODEL.md) ·
[Pilot Contract](../docs/governance/COREOPS_PILOT_CONTRACT.md) ·
[Consumer Hypothesis Validation](../docs/research/CONSUMER_HYPOTHESIS_VALIDATION.md)

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

CDS-WP-006 — Governance, Versioning, and Contribution Model: supplies the policy
the architecture deliberately deferred — governance roles, **risk ownership**
(provisional across all 28 risks), maturity states, versioning, compatibility,
deprecation, contribution, exception governance, Product Profile governance,
conformance and adoption claims, and the licensing and publication decision
model. Still no visual design and no technology selection.

**Open for Nova:** the accessibility target (CR-024) remains undefined and now
blocks a CoreOps pilot entry criterion and Pilot Group E evidence (RISK-028).
Advancing CDS-WP-007 is worth considering; Claude does not reorder the roadmap. Requires an explicit work-package prompt from Nova.

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
- [CDS-WP-004 Consumer Requirements and CoreOps Pilot Notes](CDS_WP_004_CONSUMER_REQUIREMENTS_AND_COREOPS_PILOT_NOTES.md)
- [CDS-WP-005 Design System Architecture Notes](CDS_WP_005_DESIGN_SYSTEM_ARCHITECTURE_NOTES.md)
