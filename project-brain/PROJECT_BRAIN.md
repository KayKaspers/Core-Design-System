# Core Design System — Project Brain

Compact long-term orientation for the Core Design System (CDS). This document
summarizes; it does not duplicate the normative documents it points to.

- **Project:** Core Design System (CDS)
- **Repository:** KayKaspers/Core-Design-System
- **Local path:** `D:\Projects\Core-Design-System`
- **Framework:** Nova Development Framework v1.0.0
- **Phase:** Post-Candidate Foundation & Design-System Enablement — **Foundation /
  Pre-Design: Closed with Notes** (**DEC-S-127**, 2026-08-26, effective at its
  Human-Maintainer integration commit). It supersedes `Pre-Candidate Operating
  Enablement` (**DEC-S-062**) **for current and future state only**; DEC-S-062 stays
  `Accepted` and correct for the period it governed. **Phase is not maturity** — the
  transition grants nothing.

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

- Decisions: DEC-S-001 … DEC-S-138 (138) — 6 foundation + 6 scope + 8 consumer
  and pilot scope + 12 logical architecture + 16 governance + 12 accessibility +
  4 operating enablement and pre-candidate + 8 accessibility support baseline and
  evidence + 10 machine-readable source and token format + 10 machine-readable
  bootstrap and validation + 12 offline validator implementation + 10 semantic
  status foundation + 10 semantic status source and evidence + 1 accessibility /
  maturity / channel boundary + 1 candidate finalization / maturity / evidence
  transition + 1 phase transition + 4 visual token representation, evaluation
  authority and source identity + 4 visual identifier, scale ownership, role
  admission and theme sequencing + 1 adaptive spatial context and responsive
  architecture + 2 theme resolution, context-evidence and environmental selection
  decisions ·
  **ADRs: 7 (ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0005, ADR-0006, ADR-0007)**
  - **Effectivity: DEC-S-128 … DEC-S-131 and ADR-0004 are effective**, at the
    Human-Maintainer exact-byte integration commit
    `42a568d823de3388e45af62967546f13ad67eff6` of the CDS-WP-020 Decision
    Integration Pass; **DEC-S-132 … DEC-S-135 and ADR-0005 are effective**, at the
    Human-Maintainer exact integration commit
    `2cb244e889c1a6b5a278afb233995a0379b5d9ef` of the CDS Step-9 Decision
    Integration Pass; **DEC-S-136 and ADR-0006 are effective**, at the
    Human-Maintainer exact-object integration commit
    `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9` of the CDS-WP-021 object;
    **DEC-S-137, DEC-S-138 and ADR-0007 are effective**, at the Human-Maintainer
    exact-object integration commit `23914ecc48c1fb3cba5e3dab97a505589e821b6b` of the
    CDS-WP-022 object. The
    **effective** register is **DEC-S-001 … DEC-S-138 (138)**
    with **7 ADRs**.
- Risks: RISK-001 … RISK-098 (98) — **89 Monitored; RISK-031, RISK-040, RISK-044,
  RISK-066, RISK-067, RISK-068, RISK-069, RISK-071, RISK-098 Mitigating**; **owner
  model finalized**; no risk accepted or closed
- Completed work packages: CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005, CDS-WP-006, CDS-WP-007, CDS-WP-008, CDS-WP-009, CDS-WP-010,
  CDS-WP-011, CDS-WP-012, CDS-WP-013, CDS-WP-014, CDS-WP-015, **CDS-WP-016**,
  **CDS-WP-017**, **CDS-WP-018**, **CDS-WP-019**
- Closed work package: **CDS-WP-019 — Core Visual Foundation Architecture** —
  **architecture only**: it defines how the visual foundation is structured,
  governed, represented, extended, validated, and consumed. It created **no visual
  value**, no token source file, no component, no brand, and no Product Profile;
  produced and admitted no evidence; changed no maturity; added no ADR, Decision, or
  risk; renamed no phase; registered no capability; and activated no later work
  package. Closure became effective with the Human-Maintainer commit
  `538fbccbf6f554de3b872e9fb75a70d13318feb6`.
- **Current work package: `CDS-WP-022` — Theme and Environmental Presentation
  Model.** **`AUTHORIZED` / `ACTIVE FOR EXECUTION`** by a separate, explicit
  Human-Maintainer act taken after the CDS-WP-021 closure — **`CLOSED ≠ SUCCESSOR
  AUTHORIZED`**, **`DEPENDENCY SATISFIED ≠ AUTHORITY GRANTED`**, and **`SEQUENCED
  NEXT ≠ AUTHORIZED`**: the `DEC-S-135` recommendation that named it authorized
  nothing. **Contract only**, and **executed with result `COMPLETE WITH NOTES`** after
  first returning `DECISION_REQUIRED`: it
  defines what a **Theme Resolution Context** is (**CA-1 … CA-13**), the **theme
  resolution mechanism** (**TM-1 … TM-12**), how a context is
  identified without becoming a path segment (**CI-1 … CI-6**), how a **requested**
  context enters resolution (**CS-1 … CS-11**), what CDS may and may not do with an
  environmental input (**CE-1 … CE-5**), where resolution **fails closed**
  (**CF-1 … CF-11**), and how a context composes against channel, **Spatial
  Context**, Product Profile, role identity, status, Source Set and token-flow layer
  (**CB-1 … CB-7**) — and it **escalates five normative choices** as the
  execution-local report keys **`WP022-D1`** the theme mechanism, **`WP022-D2`** the
  initial supported context set, **`WP022-D3`** the forced-colours disposition,
  **`WP022-D4`** context selection and environmental precedence, and **`WP022-D5`**
  default / fallback / missing-context semantics. **`DERIVE ≠ DECLARE`**, and **an
  authorized work package is not an executor authorized to invent normative choices.**
  **The Human Maintainer decided all five on 2026-09-12**, and a bounded
  rework applied them: the **execution result is now `COMPLETE WITH NOTES`**, and the
  initial `DECISION_REQUIRED` **stands as execution history**. **`WP022-D1`** is the
  **Resolver-Modifier Context** over the existing Source-Set graph, with the
  **Resolver / Composition revision** and the **Theme Resolution Context** recorded as
  **exact evidence inputs** of evidence that stays bound to (`sourceSetId`,
  `sourceRevision`), **no per-context Source Set**, **no second maturity unit**, and
  **Theme and Spatial Context orthogonal** — recorded as **`DEC-S-137`** with
  **`ADR-0007`** (covering `DEC-S-137` **only**). **`WP022-D2` … `WP022-D5`** are
  **`Light` and `Dark`** as equal peers with **no default**, **forced colours as an
  environmental accessibility condition and not a Core context**, **explicit viewer
  choice over inferred environment preference** with mandatory platform accessibility
  conditions **outside** Theme precedence, and **no default or fallback Theme with
  fail-closed resolution** and **`Not Applicable`** where Theme resolution genuinely
  does not apply — recorded as **`DEC-S-138`**, which has **no ADR**. **All three are
  `Accepted` and effective at the Human-Maintainer exact-object integration commit
  `23914ecc48c1fb3cba5e3dab97a505589e821b6b`**, which integrated the reviewed
  CDS-WP-022 object — **`APPROVED PROPOSITION ≠ EFFECTIVE REPOSITORY DECISION`** held
  until it; **136 decisions and 6 ADRs until that commit, 138 and 7 from it**, with the
  risk register at **98**
  throughout — **no `RISK-099`, no `DEC-S-139`, no `ADR-0008`**. **Supported Core Theme
  Resolution Contexts: 0 before that commit, 2 — `Light` and `Dark` — from it, with no
  default**, and
  **`Light` and `Dark` are human-readable architectural names, not machine-readable
  identifiers.** **`DEC-S-131`, `DEC-S-132`, `DEC-S-135` and `DEC-S-136` are unchanged
  in byte and in substance**; from the effectivity of the two new Decisions the
  **DEC-S-135 theme-mechanism sequencing condition is satisfied**, and **`THEME GATE
  SATISFIED ≠ VALUE SELECTION AUTHORIZED`** and **`THEME GATE SATISFIED ≠
  CDS-WP-020A AUTHORIZED`**. **CDS-WP-022 is not closed**, and **closure is a separate
  Human-Maintainer act.**
  The next one begins only on an explicit Nova prompt **and** a separate
  Human-Maintainer authorization.
- Preceding work package: **CDS-WP-021 — Adaptive Layout and Responsive
  Foundation** — **`Completed` / `Closed`**. Authorized for execution by a separate,
  explicit Human-Maintainer
  decision; **executed with result `COMPLETE WITH NOTES`**, unchanged by closure and
  never rewritten to `COMPLETE`; **integrated** by the
  Human-Maintainer exact-object commit
  `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9` (2026-09-11); and **closed by a
  further, separate Human-Maintainer authorization, effective at the Human-Maintainer
  exact-object integration commit `01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`** —
  **`CLOSURE OBJECT PREPARED ≠ CLOSURE EFFECTIVE`** held until that commit.
  **Contract only:** it confirms the
  **Layer 3 / Layer 5 / Layer 6** ownership split — **`F-019-03` answered, CR-004
  unchanged at Layer 5** — and records the spatial-context model (CX-1 … CX-9), the
  **Adaptation Container** (AC-1 … AC-6), the
  responsive-range obligations (AR-1 … AR-12), the grid, container and content-width
  contracts (GC-1 … GC-9), and the density and adaptation interaction (DA-1 … DA-6).
  It creates **no** visual value, **no** identifier, **no** responsive-range name,
  **no** range count or threshold, **no** VF-4 technical root, and **no** source
  set; admits **no** evidence; changes **no** maturity; and adds **no** risk — the
  risk register stays at **98**.
  **`WP021-D1` is APPROVED by the Human Maintainer** (2026-09-06) — the
  **Container-Relative Named-Range Foundation**: a declared **Adaptation Container**
  as primary reference frame, **named discrete available-space ranges** as Core
  Layer-3 vocabulary, continuous behaviour **permitted downstream but not Core range
  identity**, fixed-geometry channels governed by **their own geometry**, and
  **`SPATIAL CONTEXT ≠ THEME RESOLUTION CONTEXT`** — recorded as **`DEC-S-136`**
  with **`ADR-0006`**, both **effective at that integration commit**, so the
  **effective registers are now 138 and 7**, `DEC-S-137`, `DEC-S-138` and `ADR-0007`
  having become effective at `23914ecc…`. **`EFFECTIVE ≠ CLOSED`**, and effectivity
  selected no value and created no identifier.
  **`WP021-D2` is DEFERRED** — **VF-4 technical root OPEN, VF-4 Source Set identity
  OPEN**, and **no Decision and no ADR exists for it** — **`DEC-S-137`
  and `ADR-0007` record `WP022-D1`, not `WP021-D2`, and are unrelated to it**.
  **Closure does not resolve it** — **`DEFERRED OPEN QUESTION ≠
  INCOMPLETE WORK PACKAGE`** — and closure satisfies no value prerequisite, admits
  no evidence, changes no maturity, and adds no Decision, ADR, or risk.
  **CDS-WP-022 was later authorized by a separate, explicit Human-Maintainer act**,
  not by this closure, and is **integrated** at `23914ecc…`, **`AUTHORIZED` /
  `ACTIVE FOR EXECUTION`**, and **not closed**; **`CDS-WP-020A` and CDS-WP-023 …
  CDS-WP-053 remain `Planned`, not active, and not authorized**, and **`DEC-S-135`
  is unchanged.**
- Previous work package: **CDS-WP-020 — Reference and Semantic Token
  Foundation** was authorized separately by the Human Maintainer on 2026-08-26,
  **executed with result `DECISION_REQUIRED`**, and **integrated** by the
  Human-Maintainer commit `42a568d823de3388e45af62967546f13ad67eff6`. It is recorded
  as **`Completed`**; **closure was recorded in the working object of the
  CDS-WP-020 closure and routing pass and became effective at that object's
  Human-Maintainer integration commit `3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`.**
  **Contract only:** it defines what a visual reference primitive and a visual
  semantic role are, what each must declare, how a role aliases a primitive, and
  the discipline any future value must satisfy.
  It selects **no value**, creates **no identifier**, and creates no token source
  file, schema, validator rule, or test; produced and admitted no evidence; changed
  no maturity; added no risk; renamed no phase; registered no
  capability; and activated no later work package. Its value and machine-readable
  half is **gated** on **OD-1 … OD-7** — of which **OD-1, OD-2 and OD-3 were
  answered** by the separately authorized **Decision Integration Pass** of
  2026-08-27 (**DEC-S-128 … DEC-S-131 + ADR-0004, effective at `42a568d8…`**),
  while **OD-4 and OD-7 were answered, OD-5 partially answered, OD-6A
  policy-answered and OD-6B answered by existing authority** by the **CDS Step-9
  Decision Integration Pass** of 2026-09-05 (**DEC-S-132 … DEC-S-135 + ADR-0005,
  effective at `2cb244e8…`**), and **VP-3, VP-5, VP-6 and VP-7 stay
  unsatisfied**.
  **`DECISION_REQUIRED` stands as the executed result**: closure answers no open
  decision and selects no value. The **CDS Phase Transition Governance
  Package** (**DEC-S-127**) ran between CDS-WP-019 closure and this authorization;
  it is **not** a numbered work package and activated nothing.
- **`FR-N-03`: RESOLVED BY EXPLICIT AUTHORING-WP DESTINATION.** Nova adjudicated it
  with Human-Maintainer approval — **Option 2**: **AUTHOR is not VALIDATE**, and the
  concrete machine-readable Visual Token Source and Value Authoring work must not be
  absorbed into **CDS-WP-024**. Its destination is **`CDS-WP-020A` — Visual Token
  Source Authoring and Source Set Realization**, an **inserted** identifier on the
  `CDS-WP-001A` precedent that renumbered nothing. **`CDS-WP-020A` is `Planned`, not
  active, and not authorized**; **CDS-WP-024 keeps its validation, render-gate, and
  conformance boundary unchanged.** **Routing is not repair; registration is not
  activation; a dependency is not authority.**
- Closed work package: **CDS-WP-016 — Semantic Status Foundation Independent Evidence
  Review and Candidate Gate.** Its review work was
  **executed** — **Independent Review PASS**, **Candidate Recommendation GO**;
  **GO is not a Candidate award**. The **Nova Candidate Maturity Review** then
  returned **NO-GO** (Candidate Accessibility Gate unmet), the read-only gap
  assessment **confirmed** it, and the Human-Maintainer-authorized **Candidate
  Accessibility Gate Remediation** — internal rework of CDS-WP-016, **not** a new
  work package — is **executed**, **independently reviewed**, and admitted
  (`AE1-CDS-WP016-SEMSTATUS-002`, 2026-08-17, bound to `semantic-status-rev-0001`).
  A further internal rework — the **Candidate Finalization Governance Rework**
  (2026-08-18, DEC-S-126) — defined the promotion sequence. **That sequence has since
  completed.** Foundation **Closed with Notes**; machine-readable machinery
  implemented and executed (ADR-0001…0003); Semantic Status Foundation **Contract
  defined (CDS-WP-014)** and **machine-readable implemented (CDS-WP-015:
  `semantic/status`, 25 non-visual tokens, 24/24 harness matches, 25/25 DE/EN —
  executor-produced, since independently reviewed; not Candidate at that
  milestone)**

### Current Semantic Status lifecycle state

| Item | Value |
| --- | --- |
| **Promotion Commit** | **`22fa0710e2b75df22e7b420c2f9d86bbe67b2777`** (parent `8d1374fa4c61cc1eed214823681ee1209a2d91f7`), 2026-08-19 |
| **Source revision** | **`semantic-status-rev-0002-candidate`** |
| **Maturity** | **`Candidate`** |
| **Approval** | **`Approved`** |
| **`AE1-CDS-WP016-SEMSTATUS-004`** | **ADMITTED / AE-1** — the package in force, channel-independent source/contract scope only |
| `AE1-CDS-WP016-SEMSTATUS-002` | Historical `semantic-status-rev-0001` admission only |
| `AE1-CDS-WP016-SEMSTATUS-003` | **NOT ADMITTED** · `SUPERSEDED_FOR_ADMISSION_BY_EVIDENCE_INPUT_CHANGE` |
| Promotion gate | **PASS** — committed blob identity 15/15 exact; regression 47/47 · 64/64 · 184/184 · 24/24/0/0; remote fast-forward PASS |
| Stable · claims · conformance | **No** · **None** · **None** |
| AE-2 / AE-3 / AE-4 · channel · consumer evidence | **None** everywhere |
| **CDS-WP-016** | **Closed** — post-promotion closure reconciliation integrated by the Human-Maintainer commit `1fc53ae5afa40807e1950171ab700b0860ee581e` |
| **CDS-WP-017** | **Closed** — Post-WP-016 Roadmap, Authority and Scope Reconciliation, integrated by the Human-Maintainer commit `df9b8f21ff3bde4607b1c9ff7fdcbe3144366040` (governance/roadmap only; no design, evidence, maturity, claim, or publication effect) |
| **CDS-WP-018** | **Closed** — Deferred Governance and Repository Hygiene Reconciliation, integrated by the Human-Maintainer commit `e5d5d492619071655ba956713980d1ee261d9213` (documentary current-state, mirror, and hygiene reconciliation only; no phase rename, no capability registration) |
| **CDS-WP-019** | **Closed** — Core Visual Foundation Architecture (**architecture only; no visual value**; no token source, component, brand, profile, evidence, maturity change, Decision, ADR, risk, phase rename, or capability registration), integrated by the Human-Maintainer commit `538fbccbf6f554de3b872e9fb75a70d13318feb6` |
| **CDS-WP-020** | **Closed** — executed with result `DECISION_REQUIRED`; Reference and Semantic Token Foundation (**contract only; no visual value, no identifier**; no token source, schema, validator rule, test, component, brand, profile, evidence, maturity change, risk, phase rename, or capability registration), integrated by the Human-Maintainer commit `42a568d823de3388e45af62967546f13ad67eff6`. **Closure was recorded in the closure and routing object and became effective at the Human-Maintainer commit `3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`.** **`AE1-CDS-WP016-SEMSTATUS-004` was not transferred to it.** |
| **`CDS-WP-020A`** | **PLANNED / NOT ACTIVE / NOT AUTHORIZED** — Visual Token Source Authoring and Source Set Realization; the `FR-N-03` authoring destination; **inserted** identifier, nothing renumbered; owns authoring, never validation or conformance |
| **CDS-WP-021** | **Completed / Closed** — Adaptive Layout and Responsive Foundation; **executed with result `COMPLETE WITH NOTES`**, **integrated** at `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`, and **closed effective at the Human-Maintainer exact-object integration commit `01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`**. **Contract only; no visual value, no identifier, no range name or count, no VF-4 technical root, no source set**; no token source, schema, validator rule, test, component, brand, profile, evidence, maturity change, risk, phase rename, or capability registration. **Layer 3 / Layer 5 / Layer 6 split CONFIRMED — `F-019-03` answered, CR-004 unchanged at Layer 5.** **`WP021-D1` APPROVED** — the Container-Relative Named-Range Foundation — recorded as **`DEC-S-136`** with **`ADR-0006`**, both **effective at that commit**. **`WP021-D2` DEFERRED** — VF-4 root and Source Set identity **OPEN**, with **no Decision and no ADR**; **closure resolves it in no way and authorizes no successor** |
| **CDS-WP-022** | **`AUTHORIZED` / `ACTIVE FOR EXECUTION`** — Theme and Environmental Presentation Model; authorized by a **separate, explicit Human-Maintainer act** after the CDS-WP-021 closure, and **executed with result `COMPLETE WITH NOTES`** after first returning `DECISION_REQUIRED`. **Contract only; no theme instance, no machine-readable context identifier, no default alias, no visual value, no identifier, no role, no source set**; no schema, validator rule, test, fixture, component, brand, profile, evidence, maturity change, risk, phase rename, or capability registration. Derives **CA-1 … CA-13**, **CI-1 … CI-6**, **CS-1 … CS-11**, **CE-1 … CE-5**, **CF-1 … CF-11**, **CB-1 … CB-7**, and records the Human-Maintainer-decided mechanism as **TM-1 … TM-12**. **`WP022-D1` … `WP022-D5` decided 2026-09-12**, recorded as **`DEC-S-137`** (with **`ADR-0007`**, covering `DEC-S-137` only) and **`DEC-S-138`** — all **`Accepted` and effective at the Human-Maintainer exact-object integration commit `23914ecc48c1fb3cba5e3dab97a505589e821b6b`**: **136/6 until it, 138/7 from it, risks 98 throughout**. **Supported Core Theme Resolution Contexts: 0 before that commit, 2 — `Light` and `Dark`, no default — from it.** **`DEC-S-131`, `DEC-S-132`, `DEC-S-135` and `DEC-S-136` untouched**; **TS-1 still binds**; **closure is a separate Human-Maintainer act and has not occurred** |
| **CDS-WP-023 … CDS-WP-053** | **PLANNED / NOT ACTIVE / NOT AUTHORIZED** — work not started |

**F-001 lifecycle-metadata resolution (Human Maintainer, 2026-08-19).** The five
`AE1-CDS-WP016-SEMSTATUS-004`-bound normative Foundation documents remain
**exact-byte unchanged**. Their semantic content stays **normative**; their embedded
pre-promotion lifecycle labels (`Experimental`, `Unapproved`, "no Candidate status")
are treated as **historical for the current lifecycle state only**, superseded by the
completed Promotion Commit. This creates **no** general source-precedence rule, does
**not** say recency wins, waives **no** evidence requirement, transfers **no**
evidence, and weakens **no** future re-evidence requirement. The completed lifecycle
event is recorded in the
[Candidate Promotion Effectivity Record](../docs/governance/SEMANTIC_STATUS_CANDIDATE_PROMOTION_EFFECTIVITY_RECORD.md)
— a governance lifecycle effectivity record, **not evidence** and **not a Promotion
Commit**.

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
| DEC-S-033 | Governance separates authority by function; activity grants nothing. |
| DEC-S-034 | Neither normative source wins automatically. |
| DEC-S-035 | Seven maturity states, separate from version and publication. |
| DEC-S-036 | Candidate and Stable need evidence and approval. |
| DEC-S-037 | MAJOR.MINOR.PATCH; honest pre-1.0 policy. |
| DEC-S-038 | Releases need an immutable identity; `latest` is not one. |
| DEC-S-039 | Compatibility declared per axis. |
| DEC-S-040 | Stable requires deprecation before removal. |
| DEC-S-041 | Controlled contribution; use never equals acceptance. |
| DEC-S-042 | Exceptions are explicit, bounded, expiring. |
| DEC-S-043 | Product Profiles are separately governed. |
| DEC-S-044 | Claims are scope-, version-, evidence-bound; `CDS certified` prohibited. |
| DEC-S-045 | Risk ownership finalized. |
| DEC-S-046 | Five publication states with an explicit gate. |
| DEC-S-047 | Licensing decided per artifact class. |
| DEC-S-048 | Release control requires explicit human approval. |
| DEC-S-049 | WCAG 2.2 Level AA target for the applicable web scope; not a claim. |
| DEC-S-050 | Target, evidence, validation, and claim are separate governance states. |
| DEC-S-051 | Accessibility responsibility is shared by contract (CDS vs consumer). |
| DEC-S-052 | Component/limited-scope evidence cannot be generalized into a product claim. |
| DEC-S-053 | Automated checking is never sufficient alone. |
| DEC-S-054 | Native semantics first; ARIA only where required; APG informative. |
| DEC-S-055 | Mandatory contract areas: keyboard, focus, motion, non-colour, errors, status. |
| DEC-S-056 | Status axes (Unknown ≠ Healthy) distinguishable via accessible semantics. |
| DEC-S-057 | Inclusive design extends beyond WCAG conformance. |
| DEC-S-058 | Each channel needs its own profile; non-web never WCAG-conformant. |
| DEC-S-059 | Accessibility cannot be waived by an ordinary exception. |
| DEC-S-060 | CR-024 resolved at policy level for the CoreOps pilot web scope. |
| DEC-S-061 | Foundation milestone closed with mandatory notes; closure grants no Candidate/Stable/adoption/conformance/release/publication. |
| DEC-S-062 | First post-Foundation phase is Pre-Candidate Operating Enablement. **Superseded for current-state phase designation by DEC-S-127; still Accepted and historically valid.** |
| DEC-S-063 | Operating playbooks and dossiers are non-normative; reduce ceremony, never obligation. |
| DEC-S-064 | Critical risks affecting Elevated work need executor, trigger, expected evidence, and blocking effect first. |
| DEC-S-065 | The Accessibility Support Baseline defines what future evidence targets; not evidence, support, or a claim. |
| DEC-S-066 | Three accessibility baseline tiers (Required / Complementary / Scope-triggered). |
| DEC-S-067 | Required Core Baseline: keyboard, Windows 11, Chromium + Firefox, no-cost screenreader, ≥2 pairings, zoom/reflow, text spacing, forced-colors, reduced motion, accessible status, DE/EN. |
| DEC-S-068 | Product-family baseline vs exact evidence identity separate; `current`/`latest` is not an identity. |
| DEC-S-069 | Complementary/mobile coverage is scope-triggered; undeclared environments not supported. |
| DEC-S-070 | Baseline freshness reviewed on triggers and at least every six months. |
| DEC-S-071 | Immutable, bound, reviewer-identified evidence records; templates/automation/single passes are not global evidence. |
| DEC-S-072 | Accessibility defects/regressions classified separately from risk; Blocking/High regressions block Stable and claims. |
| DEC-S-073 | DTCG 2025.10 (Format/Color/Resolver) is the external format basis; a CG report, not a W3C Standard. |
| DEC-S-074 | Only pinned DTCG 2025.10 is authoritative; previews/drafts are inputs only. |
| DEC-S-075 | Strict JSON (RFC 8259) `.tokens.json` is the normative source form. |
| DEC-S-076 | CDS profile constrains DTCG; metadata only via namespaced `$extensions`; reserved semantics unchanged. |
| DEC-S-077 | JSON Schema 2020-12 is the profile-schema foundation; a schema pass is not full correctness. |
| DEC-S-078 | Token references fail closed on cycles/dangling/type/missing/bad-layer/unresolved-override. |
| DEC-S-079 | Source sets layered (Reference/Semantic/Component/Product Profile); channel outputs generated, not normative. |
| DEC-S-080 | Versioned, non-`latest` provenance identity for sources and outputs. |
| DEC-S-081 | Restrictive, machine-validatable naming; technical IDs separate from display labels. |
| DEC-S-082 | Format/profile/binding upgrades are governed; no automatic upgrade. |
| DEC-S-083 | Bootstrap = CDS-owned JSON Schemas + synthetic fixtures; presence is not conformance. |
| DEC-S-084 | CDS metadata under `io.github.kaykaspers.cds`, requires `profileVersion`; foreign extensions preserved. |
| DEC-S-085 | Source-Set manifests explicitly declare identity/layer/path/graph; no implicit/network sets. |
| DEC-S-086 | Resolver documents: `$ref`/JSON Pointer, explicit local ordered composition; no network resolution. |
| DEC-S-087 | Validation fixtures are synthetic, test-only, non-normative. |
| DEC-S-088 | Duplicate JSON member names prohibited; fail V1; no first/last-key-wins repair. |
| DEC-S-089 | Validation cases bind every fixture to expected V1–V4; no aggregate score. |
| DEC-S-090 | RFC 8785 (JCS) + SHA-256 for canonical content digests. |
| DEC-S-091 | Cross-file references valid only via the declared local graph; else fail closed. |
| DEC-S-092 | Bootstrap stays Experimental until a validator executes, is reviewed, and HM-approved. |

Details: [Decision Index](../docs/decisions/DECISION_INDEX.md) ·
[ADR-0001](../docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) ·
[ADR-0002](../docs/decisions/ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md)

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
| RISK-029 | Governance bottleneck and maintainer overload. | Monitored |
| RISK-030 | Governance role ambiguity. | Monitored |
| RISK-031 | Maturity inflation. | **Mitigating** |
| RISK-032 | Compatibility ambiguity. | Monitored |
| RISK-033 | Deprecation without viable migration. | Monitored |
| RISK-034 | Contribution gate bypass. | Monitored |
| RISK-035 | Exception debt. | Monitored |
| RISK-036 | Product-profile governance bypass. | Monitored |
| RISK-037 | Misleading adoption or conformance claims. | Monitored |
| RISK-038 | Licensing and rights fragmentation. | Monitored |
| RISK-039 | Premature publication. | Monitored |
| RISK-040 | Ceremonial risk governance. | **Mitigating** |
| RISK-041 | Accessibility target mistaken for conformance. | Monitored |
| RISK-042 | Automated-testing substitution. | Monitored |
| RISK-043 | Component-to-product responsibility gap. | Monitored |
| RISK-044 | Accessibility support baseline drift. | **Mitigating** |
| RISK-045 | Accessibility regression. | Monitored |
| RISK-046 | Non-web channel accessibility gap. | Monitored |
| RISK-047 | Inclusive-design undercoverage. | Monitored |
| RISK-048 | Accessibility evidence burden. | Monitored |
| RISK-049 | Accessibility baseline representativeness gap. | Monitored |
| RISK-050 | Baseline interpreted as universal support. | Monitored |
| RISK-051 | Environment availability mismatch. | Monitored |
| RISK-052 | Evidence identity incompleteness. | Monitored |
| RISK-053 | Regression coverage gap. | Monitored |
| RISK-054 | Accessibility defect normalization. | Monitored |
| RISK-055 | Token specification version drift. | Monitored |
| RISK-056 | Preview specification contamination. | Monitored |
| RISK-057 | CDS profile divergence. | Monitored |
| RISK-058 | Schema-validation false assurance. | Monitored |
| RISK-059 | Reference-resolution failure. | Monitored |
| RISK-060 | Cross-layer dependency violation. | Monitored |
| RISK-061 | Token identifier collision. | Monitored |
| RISK-062 | Token provenance incompleteness. | Monitored |
| RISK-063 | Transformation-tool lock-in. | Monitored |
| RISK-064 | CDS schema contract incompleteness. | Monitored |
| RISK-065 | Synthetic fixtures mistaken for design tokens. | Monitored |
| RISK-066 | Schema and validator divergence. | **Mitigating** |
| RISK-067 | Canonicalization and digest mismatch. | **Mitigating** |
| RISK-068 | Duplicate-key ambiguity. | **Mitigating** |
| RISK-069 | Manifest and resolver graph inconsistency. | **Mitigating** |
| RISK-070 | Validation fixture coverage gap. | Monitored |
| RISK-071 | Validation expectation drift. | **Mitigating** |
| RISK-072 | Digest mistaken for authenticity. | Monitored |

**Owner model finalized** (DEC-S-045): Human Maintainer accountable · Nova
controller · executor named per mitigation · reviewer never the executor. Only
the Human Maintainer may accept or close a risk. **CDS-WP-009 moved RISK-040
`Monitored → Mitigating`** via the
[Critical Risk Action Register](../docs/operations/CRITICAL_RISK_ACTION_REGISTER.md)
(DEC-S-064). **CDS-WP-010 added RISK-049…054 and moved RISK-044
`Monitored → Mitigating`** (A11Y-BL-001 defined; DEC-S-070). **CDS-WP-011 added
RISK-055…063** (token-format/spec-drift/reference/provenance risks). **CDS-WP-012 added
RISK-064…072** (schema/fixture/duplicate-key/canonicalization/validation-coverage risks;
all Monitored). **CDS-WP-013 added RISK-073…081** (validator supply-chain/coverage/
reproducibility/evidence risks; all Monitored) **and moved RISK-066/067/068/069/071
`Monitored → Mitigating`** on executed, executor-produced harness evidence
(independently unreviewed; DEC-S-103). No risk accepted or closed.
Details: [Risk Register](../docs/risks/RISK_REGISTER.md)

## Governance model (CDS-WP-006)

**Normative. Selects no licence, publication, technology, or design.**

**Six roles** (DEC-S-033): Human Maintainer (final approval; exclusive Git,
release, publication, licensing; sole risk acceptor) · Nova (governance and risk
control, review — **recommends, never decides**) · Claude (scoped executor — no
approval, no Git) · Consumer Maintainer · Contributor (no acceptance authority) ·
Evidence Reviewer (never the artifact, never the executor). **Creating,
implementing, or using an artifact grants no authority.**

**Two tracks:** Standard and Elevated. **Ceremony scales; obligations do not** —
authority, traceability, evidence, human approval, and fail-closed hold in both.

**Source conflict** (DEC-S-034): neither normative source wins automatically. A
conflict **invalidates the affected state**; `Suspected` already blocks release
and distribution. Recency, tooling, generated output, implementation, and consumer
usage never win.

**Maturity lifecycle** (7 states, DEC-S-035/036): Proposed → Exploratory →
Experimental → **Candidate** → Stable → Deprecated → Removed. Candidate mandatory.
**Maturity, release version, and publication state are separate axes** — collapsing
them is how "released" becomes "stable". **No existing artifact is Candidate or
Stable**; defining a lifecycle did not populate it.

**Versioning and compatibility** (DEC-S-037…040): MAJOR.MINOR.PATCH; pre-1.0
removes the promise, not the duty to document. **`latest` is not an identity.**
Compatibility per **8 axes**; unassessed is never "compatible". Deprecation before
removal; **a deprecation without a migration path is a removal with extra steps**.

**Contribution** (DEC-S-041): 10 steps, 5 outcomes. **`Keep Consumer-local` is a
first-class success** — CDS absorbing everything is the failure mode. No
auto-merge, no self-approval, no urgency bypass. External contribution not yet
possible.

**Exceptions and Profiles** (DEC-S-042/043): exceptions bounded, owned, expiring;
`Expired` is an uncovered deviation; recurring exceptions trigger a core gap
review; **accessibility weakening is not exceptable**. A Product Profile is **not
retrospective legitimation** of an existing consumer design.

**Claims** (DEC-S-044): four graded types, eight mandatory fields each.
**`CDS certified` prohibited.** **No claim is currently valid, by anyone —
including CDS.**

**Publication and licensing** (DEC-S-046/047): five states, current
**`Private Development`**; 15-point gate; **repository visibility is not
publication**. Licensing per **10 artifact classes**, no inheritance, **none
selected**; unknown rights block publication.

**Release** (DEC-S-048): 12 requirements, 6 change classes; no automatic
publication; **Claude never releases**; a green build is not consent.

**Currently blocked:** no artifact can reach Stable · no profile can be approved ·
no publication change · **no release is possible** — all tracing to the largely
absent accessibility evidence (CR-024; every artifact is AE-0 apart from one
admitted source-level AE-1 scope, and no AE-2/AE-3/AE-4 exists) and absent licensing
decisions.

Details: [Governance Operating Model](../docs/governance/GOVERNANCE_OPERATING_MODEL.md) ·
[Risk Governance](../docs/governance/RISK_GOVERNANCE_MODEL.md) ·
[Claims](../docs/governance/ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md)

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

**Requirement coverage:** CR-001…040 fully mapped — **9 addressed, 27 partially
addressed, 0 deferred to a policy work package, 2 consumer-owned, 2 out of
scope** (reconciled by CDS-WP-007). Only 9 of 40 fully addressed is the
**expected** result: an architecture resolving most requirements would be doing
unauthorized design work. CR-024 became `addressed` because the target and policy
now exist — **not because the target was tested against**; every artifact is AE-0
apart from one admitted source-level AE-1 scope.

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
The contract is committed and normative (CDS-WP-004); **entry criteria are unmet
and no pilot has started**.

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
framework, token build system, documentation platform, package
architecture, repository split, license, public release, contribution model,
long-term compatibility commitments, or concrete product signatures.

**No longer open** (previously listed here): **versioning and maturity model**
(CDS-WP-006, DEC-S-035…040), **conformance and adoption policy** (CDS-WP-006,
DEC-S-044), and **Product Profile and override governance** (CDS-WP-005/006,
DEC-S-042, DEC-S-043) — as is the **token format** (CDS-WP-011, ADR-0001), which is
distinct from the still-open token *build system*. **A decided model is not an
applied one:** no Product Profile is activated, no adoption or conformance claim is
valid, no artifact is `Stable`, and no version has been released.

## Accessibility policy (CDS-WP-007)

**Target:** WCAG 2.2 Level AA for the applicable web-based scope (DEC-S-049),
resolving CR-024 at policy level (DEC-S-060). No AAA commitment. **A target is not
conformance** (DEC-S-050) — and nothing has been tested.

**Applicability:** all Level A and AA success criteria mapped — 56 listed (32 A ·
24 AA), 55 applicable (31 A · 24 AA), excluding the obsolete 4.1.1. No pass/fail.

**Responsibility boundary:** shared by contract; **49 of 55 applicable criteria
need both CDS and the consumer** (DEC-S-051, DEC-S-052). CDS supplies contracts,
status semantics, and reference evidence; the consumer supplies accessible
composition, content, complete processes, and product claims. **Accessible
artifacts do not compose into an accessible product by themselves.**

**Evidence:** five levels AE-0 … AE-4 (Evidence and Claims Model); AE-3 needs a
declared support baseline; automated-only never suffices (DEC-S-053). **Every CDS
artifact is AE-0 except the channel-independent Semantic Status source/contract
family at admitted AE-1; the support baseline A11Y-BL-001 is committed but is not
evidence** (RISK-041, RISK-044).

**Channels:** six profiles; only two (Web UI, Web Docs) have a target; **none is
Candidate- or Stable-eligible** (DEC-S-058).

**Limits:** accessibility cannot be waived by an ordinary exception (DEC-S-059);
no legal or certification statement (policy boundary, standard-status doc); native
semantics first, APG
examples informative only (DEC-S-054).

**CR-024 / pilot:** resolved at policy level; entry criterion met with the
CDS-WP-007 commit. **The CoreOps pilot has not started and cannot start; no
WCAG 2.2 Level AA conformance has been demonstrated, reviewed, or approved for
CoreOps** (not assessed, not failed).

Details:
[A11y Policy](../docs/governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) ·
[Matrix](../docs/governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md) ·
[Evidence](../docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) ·
[Channels](../docs/governance/ACCESSIBILITY_CHANNEL_PROFILES.md) ·
[Pilot criterion](../docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md)

## Foundation Milestone Review (CDS-WP-008)

The Foundation was reviewed across twelve dimensions (55 criteria), three
governance dry runs, four-axis Candidate readiness, an eight-criterion CoreOps
pilot entry matrix, and all 48 risks. **Zero Foundation blockers.** Recommended
milestone outcome: **`GO WITH NOTES`** — Claude recommends closure with mandatory
next-phase notes; **Nova review and Human-Maintainer approval are required** before
closure is effective.

Completeness matrix: 55 criteria — 44 Met · 4 Met-with-notes · 3 Partially met · 4
Not met. Twelve findings (FM-F-001…012), all next-phase / Candidate / pilot /
publication prerequisites or long-term operating concerns.

**Governance affordability is the standout note:** the Standard track is
operational, but the Elevated + accessibility path is High burden for a single
approver (Dry Run C), and the risk register is not yet operated as an instrument
(48 risks, 0 executors — RISK-040). **Candidate readiness:** governance yes,
artifact/evidence no (not a blocker). **CoreOps pilot:** inactive; criterion 8
(accessibility target) became Met with the WP-007 commit; no conformance
demonstrated. Critical risks: RISK-029, 040, 048, 044, 017, 028, 020, 021, 023,
026, 031, 038.

**No new Decision or Risk ID, no ADR, no work-package ID** was created. No artifact
promoted; publication state `Private Development`; no claim valid; no release
possible (licence unsatisfiable, DEC-S-047).

## Operating enablement (CDS-WP-009)

The Human Maintainer accepted `GO WITH NOTES` (commit of CDS-WP-008 + initiation of
CDS-WP-009). **Foundation: Closed with Notes.** CDS-WP-009 operationalized the
committed governance without any design, token, component, tool, or product code:

- **Foundation Closure Record** — normative on the fact of closure, the authority
  state, and the phase boundary; no Candidate/claim/licence/publication effect.
- **Operating Playbook + Standard/Elevated dossier templates** — a non-normative
  operational view of the two tracks and the mandatory gates (DEC-S-063).
- **Critical Risk Action Register** — the 12 Critical Risks (RISK-017, 020, 021,
  023, 026, 028, 029, 031, 038, 040, 044, 048) each with an executor role, review
  trigger, expected evidence, and blocking effect (DEC-S-064). On that basis
  **RISK-040 moved `Monitored → Mitigating`** — the only status change.
- **Reference Integrity Review** — PASS; 0 CDS-authored broken links.
- **Pre-Candidate Operating Plan** — phase entry state, prerequisites, Candidate
  entry conditions, exit criteria.

Added DEC-S-061 … DEC-S-064. Publication state `Private Development`; no claim; no
Candidate/Stable artifact; pilot inactive.

## Accessibility support baseline (CDS-WP-010)

Defined the first accessibility support baseline **A11Y-BL-001** (since
committed) using authorized official standards/vendor research
(13 URLs opened, 9 usable) — **no test run, no tool selected, and at that time every
artifact AE-0; still no environment claimed supported**:

- **Three tiers** — Required Core (small, free-software-runnable), Complementary
  (Conditional), Scope-triggered (Deferred) — with a 14-entry
  [Environment and Scope Matrix](../docs/governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
  (Required 6 · Conditional 4 · Deferred 4; 2 Required NVDA×Chromium / NVDA×Firefox
  pairings).
- **Selected families** (officially sourced): Windows 11; Chromium (Edge/Chrome);
  Firefox/ESR; NVDA; forced-colors → Windows High Contrast; reduced-motion → OS
  setting. Product-family baseline vs exact per-run evidence identity kept separate
  (DEC-S-068).
- **Evidence Strategy** (AE-0…AE-4), **Maintenance Policy** (freshness states +
  triggers + six-month max gap), **Defect and Regression Model** (4 impact levels;
  Blocking/High regressions block Stable/claims), and a non-normative **Evidence
  Record Template**.
- The baseline is a **test contract, not evidence** (DEC-S-065); RISK-044 moved to
  `Mitigating`; DEC-S-065…072 and RISK-049…054 added.

## Machine-readable source and token format (CDS-WP-011)

Decided the normative machine-readable source format using authorized official
research (13 DTCG/W3C/RFC/JSON-Schema URLs; stable vs preview separated) — **without
implementing anything**:

- **External basis:** **DTCG 2025.10** (Format, Color, Resolver) — a **Final Community
  Group Report, not a W3C Standard**; only the pinned stable version is authoritative,
  previews are inputs only (DEC-S-073, DEC-S-074).
- **Canonical form:** **strict JSON (RFC 8259), `.tokens.json`**; YAML/JSONC/JSON5/
  tool/CSS/generated forms are not normative sources (DEC-S-075).
- **Profile:** a CDS Token Format Profile over DTCG; metadata only via a
  **`io.github.kaykaspers.cds` `$extensions`** namespace (repository-identity-derived,
  collision-resistant; foreign extensions preserved, not automatically normative);
  reserved DTCG semantics never redefined (DEC-S-076).
- **Schema:** **JSON Schema 2020-12** as the future CDS-owned profile-schema
  foundation (no schema created; a schema pass is not full correctness — DEC-S-077).
- **Source sets:** Reference → Semantic → Component → Product Profile (downward only);
  channel outputs are generated, non-normative (DEC-S-079). **References:** curly-brace
  `{group.token}` for canonical token-to-token authoring; DTCG `$ref` / RFC 6901 JSON
  Pointer for document/property/resolver/source-set and controlled cross-file
  references. Fail-closed on cycles/dangling/type/missing-set/bad-layer/override/
  undeclared-cross-file (DEC-S-078); only the provenance-pointer form stays open.
  Machine-validatable naming (DEC-S-081). Versioned, non-`latest` provenance identity
  (DEC-S-080).
- **Validation:** four layers — V1 Syntax · V2 DTCG · V3 CDS Profile · V4 Semantic/
  Governance; a lower-layer pass proves no higher layer; a tool result is not
  approval.
- Created **ADR-0001** + four architecture docs + evaluation/register + implementation
  plan; DEC-S-073…082 and RISK-055…063 added. **No token/schema/validator/design
  value; publication `Private Development`.**

## Machine-readable bootstrap (CDS-WP-012)

Implemented the value-neutral bootstrap (pending commit) — **no design value, no
productive validator**:

- **4 CDS-owned JSON Schema 2020-12 contracts:** token document, source-set manifest,
  resolver, validation case — stable `tag:` `$id`s, same-document local `$ref`, offline.
- **`io.github.kaykaspers.cds` extension payload** requiring `profileVersion` + source-set
  identity; foreign extensions preserved, not automatically normative (DEC-S-084).
- **6 positive + 9 negative synthetic fixtures** (`testOnly`/`nonNormative`, `fixture/`
  IDs); a **15-case validation-case matrix** binding every fixture to expected V1–V4
  (DEC-S-089); duplicate-key fails V1 (DEC-S-088).
- **V1–V4 Validation Contract** (schema pass ≠ higher-layer pass; no aggregate score) and
  the **RFC 8785 (JCS) + SHA-256** deterministic-serialization decision (**ADR-0002**;
  digest is integrity, not authenticity — RISK-072).
- Local structural validation (parse, duplicate-key, schema-IDs/`$ref`, case coverage,
  ID syntax, dependency/graph consistency) passed via a temporary non-committed script;
  **formal JSON Schema 2020-12 execution `Not assessed`** (no validator available;
  execution is CDS-WP-013). Added DEC-S-083…092 and RISK-064…072; created ADR-0002.
  **Experimental, not Candidate** (DEC-S-092).

## Offline validator and fixture harness (CDS-WP-013)

Implemented and executed the offline validator (pending commit) — **executor-produced,
independently unreviewed, no design value**:

- **Stack (ADR-0003):** Python 3.11+ (executed 3.12.10), pinned `jsonschema==4.26.0`
  + `rfc8785==0.1.4` (7 packages exactly pinned in `requirements-validator.lock`);
  entry point `python -m tools.cds_validator`; no runtime network (DEC-S-093/094).
- **Single duplicate-key-rejecting loader** (DEC-S-095); **local five-schema
  registry** incl. the new `cds-validation-result` schema (DEC-S-096); layered
  V1–V4 with separate states, bounded DTCG V2, declared-graph enforcement
  (DEC-S-097…099); RFC 8785 + SHA-256 digests from parsed content only (DEC-S-100).
- **Executed:** 71/71 unit tests; **15/15 harness cases with 15/15 expected/actual
  matches**; 14 fixtures digested (duplicate-key: none). Evidence:
  `artifacts/validation/wp013-fixture-results.json` + `wp013-fixture-digests.json` +
  [Execution Review](../docs/reviews/OFFLINE_TOKEN_VALIDATOR_EXECUTION_REVIEW.md)
  — `independentReviewState: pending` (DEC-S-101…103).
- Added DEC-S-093…104, RISK-073…081; RISK-066/067/068/069/071 → `Mitigating`;
  created ADR-0003. **No full-DTCG statement, no Candidate (DEC-S-104).**

## Semantic Status Foundation (CDS-WP-014)

Defined the first concrete design foundation (pending commit) — **meaning before
appearance, no visual value, no Candidate**:

- **Five independent axes** with stable IDs (`condition` · `severity` ·
  `confidence` · `freshness` · `evidence`) and a **fixed 25-value vocabulary**
  (5 per axis; `unknown` explicit everywhere, never an omitted default —
  DEC-S-105…106).
- **Ten invariants** incl. no aggregate health score and
  degraded-knowledge-never-as-success (DEC-S-107…108); **11-field status object**,
  **6 review-required combinations**, **8 fail-closed states**, 6-level disclosure
  priority (DEC-S-109).
- **Communication contract:** text-first accessible meaning, no single-modality
  encoding, DE/EN semantic parity, language-neutral IDs (DEC-S-110…111);
  downstream mappings preserve axis distinction and truth (DEC-S-112).
- **Semantic Status Token Contract** (roles only — no token file, no name, no
  value) and the **First Semantic Status Candidate Plan** (8-element package,
  10 unmet prerequisites; promotion gated — DEC-S-113…114). Readiness review is
  executor-produced; Candidate criterion honestly `Not met`.
- Added DEC-S-105…114 and RISK-082…089 (all Monitored; no existing status
  changed).

## Semantic Status Source Set and Candidate Evidence (CDS-WP-015)

Implemented the first real machine-readable source set (pending commit; resume run
after a correctly BLOCKED first run whose conflict Nova resolved by authorizing a
minimal additive validation-case-schema correction):

- **`semantic/status`** (Experimental/Unapproved): 5 axis groups, **25 non-visual
  tokens** `status.<axis>.<value>` with values = technical IDs, manifest +
  resolver, revision `semantic-status-rev-0001` (DEC-S-115…117).
- **Schema correction (Nova-authorized):** fixture-path families widened to
  `semantic-status/` token fixtures + 9 `semantic-status-*` categories; `$id` and
  all existing constraints unchanged; CLI untouched, gate fail closed;
  regression-tested.
- **Semantic-status V4 extension** (`semantic_status.py`, 9 `CDS-V4-STATUS-*`
  codes): objective checks run despite testOnly/nonNormative flags (DEC-S-118);
  1 positive + 8 negative fixtures; **VAL-CASE-016…024** (24-case matrix, WP-013
  baseline byte-identical — DEC-S-120).
- **Executed:** revision-clean WP-013 re-execution (71/71, **15/15 on the
  committed WP-014 revision, worktree clean**); **103/103 unit tests**; **24/24
  harness matches**; source-set validation V1–V3 Pass (exit 0); digests for 23
  fixtures + 3 source files; **25/25 DE/EN terminology**; 4 executor-produced
  reviews; **Draft Candidate Dossier** (gate incomplete — DEC-S-122).
- Added DEC-S-115…124, RISK-090…097; no existing risk status changed.
  **Executor-produced, independently unreviewed (DEC-S-121); Not Candidate
  (DEC-S-124).**

## Next step

**CDS-WP-018 — Deferred Governance and Repository Hygiene Reconciliation** is the
authorized work package. The sections below record how the repository reached that
point.

**CDS-WP-016 — Semantic Status Foundation Independent Evidence Review and
Candidate Gate** is closed, and its review work was **executed**:
the WP-013/WP-015 evidence was independently reviewed by a separately authorized
reviewer (re-execution and artifact assessment), together with
traceability/accessibility/content/dossier review, producing the Candidate-gate
recommendation — **Independent Review PASS**, **Candidate Recommendation GO**
([Candidate Gate Recommendation](../docs/reviews/WP016_CANDIDATE_GATE_RECOMMENDATION.md)).

**GO is not a Candidate award.**

**Candidate Accessibility Gate Remediation.** The **Nova Candidate Maturity Review**
was opened on that GO and returned **NO-GO**: the normative **Candidate
Accessibility Gate was unmet**. A read-only gap assessment **confirmed** it —
**9/9** requirements not demonstrated as satisfied, with 7 Blocking, 2 High, 4
Medium and 1 Low finding — and the Human Maintainer **authorized the CDS-WP-016
Candidate Accessibility Gate Remediation** as **internal rework of CDS-WP-016, not
a new work package**. That remediation is **executed**: DEC-S-125, Candidate-scope
WCAG and responsibility mappings, a **25/25** per-value evidence requirements
matrix, an operational text-first source rule, a test-only statement evidence layer
with **6/6** review-required and **8/8** fail-closed coverage, an
**AE-1** evidence record with results and digests, a reasoned AE-2 plan, a
support-baseline plan on **A11Y-BL-001 freshness `Current`**, a **15-trigger**
regression plan, **16** limitations (0 Critical), and a review addendum
([Addendum](../docs/reviews/WP016_CANDIDATE_ACCESSIBILITY_GATE_ADDENDUM.md)).

The remediation and its clean-HEAD evidence package have since been **independently
reviewed** (**PASS WITH NOTES** and **PASS**) and integrated, and on **2026-08-17 the
Human Maintainer admitted `AE1-CDS-WP016-SEMSTATUS-002` at AE-1** for the
channel-independent Semantic Status source/contract family **only**
([Admission Record](../docs/governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md)).

**Candidate Finalization Governance Rework.** Preparing that closure surfaced a
bootstrap problem, recorded by a read-only assessment on 2026-08-18: a Candidate
revision must declare Candidate/Approved metadata and a **new** source revision,
but the new revision invalidates the AE-1 admitted for `semantic-status-rev-0001`,
so the gate appeared to require an unevidenced preparatory commit to enter. The
Human Maintainer **authorized the CDS-WP-016 Candidate Finalization Governance
Rework** as **internal rework of CDS-WP-016, not a new work package**, and it is
**executed** — governance and tooling only:

- **DEC-S-126** — a named, **non-authoritative Proposed Candidate Revision**;
  target metadata that grants nothing; **evidence never transfers across a source
  revision**; exact-byte pre-commit evidence binding with drift invalidation;
  **AE-1 admission before Candidate approval**; the **Promotion Commit** as the
  actual repository maturity transition point; mandatory post-commit verification.
- **RISK-098** (`Mitigating`) — promotion-evidence circularity and pre-approval
  metadata misrepresentation.
- The [Candidate Approval Record Template](../docs/operations/CANDIDATE_APPROVAL_RECORD_TEMPLATE.md)
  — a **template only**; no instance existed at that milestone. **One instance now
  exists**, `CAR-CDS-WP016-SEMSTATUS-001`.
- **Evidence runner result format v2** — the runner no longer hard-codes
  governance state; it reports `sourceDeclaredMetadata`, a caller-declared
  `sourceAuthorityContext`, an **AE-1 Evidence Candidate**, and seven permanently
  false authority-effect flags, and fails closed on a source-revision mismatch.

At that milestone `semantic-status-rev-0002-candidate` was **reserved and
authorized for the future Candidate revision but not yet created**, and the
authoritative source revision was still `semantic-status-rev-0001`. The rework
itself produced **no Candidate evidence**, admitted **no evidence**, granted **no
Candidate approval**, mutated **no productive source byte**, and touched **no
existing evidence artifact**.

**Candidate authority closure — completed 2026-08-19.** The steps that were then
outstanding have all been performed, in order: fresh revision-bound evidence
**`AE1-CDS-WP016-SEMSTATUS-004`** → **fresh independent evidence review PASS WITH
NOTES** → **Human-Maintainer evidence admission APPROVED / ADMITTED** → **Nova
Candidate Finalization Review GO WITH NOTES** → **Human-Maintainer Candidate
approval `AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`** → **exact-byte Promotion
Commit `22fa0710e2b75df22e7b420c2f9d86bbe67b2777`**, which passed its gate with
15/15 committed blob identities exact and regression
47/47 · 64/64 · 184/184 · 24/24/0/0.

Candidate is **YES** at `semantic-status-rev-0002-candidate`, maturity
**`Candidate`**, approval **`Approved`** — for that one channel-independent
source/contract family. **No artifact is Stable**, claims remain **none**,
conformance remains **none**, **every other CDS artifact remains AE-0**, and there is
no AE-2, AE-3, or AE-4 anywhere — **still no visual values, no component, no
pilot**.

**CDS-WP-016 is closed.** The Human-Maintainer commit
`1fc53ae5afa40807e1950171ab700b0860ee581e` integrated the post-promotion
current-state reconciliation, and closure became effective there.

**CDS-WP-017 — Post-WP-016 Roadmap, Authority and Scope Reconciliation is closed.**
It reconciled the state actually reached with the accepted forward planning basis so
that exactly one active future work-package sequence exists: CDS-WP-016 recorded as
closed, CDS-WP-017 recorded as active at the time, and **CDS-WP-018 … CDS-WP-053
recorded as `Planned`, not active, not authorized, work not started** — a
contiguous, gap-free, duplicate-free sequence held in the
[Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md)
together with its arcs, milestones **M1 … M12**, architecture-layer mapping, standing
gates, and requirement classification model. Closure became effective with the
Human-Maintainer commit `df9b8f21ff3bde4607b1c9ff7fdcbe3144366040`.

**CDS-WP-018 — Deferred Governance and Repository Hygiene Reconciliation is
closed.** It took up the findings CDS-WP-017 routed forward without repairing —
routing is not repair — and reconciled them within a bounded documentary
scope: stale `pending commit` and mirror text against the normative sources
(**NF-R4-OBS-001**, **NF-R3-OBS-001**, **NF-R5R-OBS-001**, **R3R-003**), the
already-decided areas still listed as intentionally open (**F-017-01**,
**F-017-02**), repository hygiene on `.gitattributes` and `.gitignore`
(**NF-R4-OBS-002**, **NF-R5R-OBS-003**), additive dated notes on the two
Candidate-era records that still carry `CDS-WP-017: INACTIVE` (**R1-F-01**), and the
imprecise occurrence and disclosure wording (**R2-N-01**, **R2-N-02**).

CDS-WP-018 produced and admitted **no evidence**, changed **no maturity**, made
**no claim**, **renamed no phase** and created no Decision superseding DEC-S-062,
**registered no capability** for audio/sonic, haptic, multimodal, AI/agent, or
safety subject matter, and activated **no Product Profile, pilot, consumer
integration, release, tag, or publication**. Closure became effective with the
Human-Maintainer commit `e5d5d492619071655ba956713980d1ee261d9213`.

**CDS-WP-019 — Core Visual Foundation Architecture is closed**, authorized
separately by the Human Maintainer on 2026-08-26 and integrated by the
Human-Maintainer commit `538fbccbf6f554de3b872e9fb75a70d13318feb6`. It opened
**Phase V — Visual Foundation** with architecture rather than design: it defines
**how** visual foundations are structured before any visual decision is made — see
[Core Visual Foundation Architecture (CDS-WP-019)](#core-visual-foundation-architecture-cds-wp-019)
below.

The **CDS Phase Transition Governance Package** (**DEC-S-127**) sat between
CDS-WP-019 closure and the CDS-WP-020 authorization. It changed the project-phase
label and nothing else: no maturity, no evidence, no visual value, no capability, no
Product Profile, no pilot, no release, and no activation.

**CDS-WP-020 — Reference and Semantic Token Foundation is `Completed`**: authorized
separately by the Human Maintainer on 2026-08-26, **executed with result
`DECISION_REQUIRED`**, and **integrated** by the Human-Maintainer commit
`42a568d823de3388e45af62967546f13ad67eff6` — see
[Reference and Semantic Token Foundation (CDS-WP-020)](#reference-and-semantic-token-foundation-cds-wp-020)
below. **Its closure was recorded in the working object of the closure and routing
pass and became effective at that object's Human-Maintainer integration commit
`3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`.** **CDS-WP-020 activated no successor.**

**CDS-WP-021 — Adaptive Layout and Responsive Foundation is `Completed`**, having
been authorized for execution by a separate, later, explicit Human-Maintainer
decision: **executed with result
`COMPLETE WITH NOTES`**, **integrated** at
`a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`, and **closed by a further, separate
Human-Maintainer authorization, effective at the Human-Maintainer exact-object
integration commit `01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`**. **`WP021-D1` is
APPROVED** and recorded
as **`DEC-S-136`** with **`ADR-0006`** (**both effective at that integration
commit**, which closure does not alter);
**`WP021-D2` is
DEFERRED**, with the **VF-4 technical root and Source Set identity OPEN** and **no
Decision and no ADR** created for it.

**`CDS-WP-022` — Theme and Environmental Presentation Model is the currently
authorized work package**, **`AUTHORIZED` / `ACTIVE FOR EXECUTION`** by a separate,
explicit Human-Maintainer act taken after that closure. **The next planned work
package is `CDS-WP-020A` — Visual Token Source Authoring and Source Set
Realization** (the `FR-N-03` authoring destination), which **remains inactive until
separately authorized by the Human Maintainer**. **OD-7 is answered by the effective
`DEC-S-135`**, which made **CDS-WP-022** the recommended and sequenced Step-10
candidate. **The Human Maintainer authorized CDS-WP-021 first and CDS-WP-022
afterwards, each by its own explicit act** — **SEQUENCED NEXT ≠ AUTHORIZED**, a
recommendation is not an authorization, and any further step begins only on an
explicit Nova prompt and Human-Maintainer authorization. **CDS-WP-022 first decided no
theme mechanism**, and the `DEC-S-135` gate was **not** cleared before the Human
Maintainer's decisions became effective. **The `DEC-S-135` theme-mechanism sequencing
condition became satisfied at `23914ecc48c1fb3cba5e3dab97a505589e821b6b`**, where
`DEC-S-137` and `DEC-S-138` became effective — and **`THEME GATE SATISFIED ≠ VALUE
SELECTION AUTHORIZED`**, **`THEME GATE SATISFIED ≠ CDS-WP-020A AUTHORIZED`**, **`ONE
PREREQUISITE SATISFIED ≠ ALL PREREQUISITES SATISFIED`**, and **`ALL PREREQUISITES
SATISFIED ≠ WORK PACKAGE AUTHORIZED`**. **`CDS-WP-020A` remains `Planned`, not active,
and not authorized**; **VP-3, VP-5, VP-6 and VP-7 stay `UNSATISFIED`**, and **VP-4
stays `UNSATISFIED` for VF-4**.

## Core Visual Foundation Architecture (CDS-WP-019)

**Architecture only. No visual value exists in CDS, and CDS-WP-019 created none.**
Verified by search at the baseline: the repository contained **no colour value, no
typographic value, and no dimensional value of any kind**.

### What it established

- The [Visual Foundation Architecture](../docs/architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
  as the Layer-3 visual entry point.
- **Nine visual foundation families:** VF-1 Colour · VF-2 Typography · VF-3 Space
  and Size · VF-4 Layout and Grid · VF-5 Shape · VF-6 Surface and Elevation ·
  VF-7 Iconography · VF-8 Motion (boundary only) · VF-9 Theme and Context
  Mechanism. Each is a **separate artifact family**; **maturity is never
  inherited**; all nine are **`Proposed`**.
- **Fourteen visual foundation invariants** (VF-I-1 … VF-I-14).
- Six specialised architectures — colour, typography, spatial, shape and surface,
  iconography and imagery, theme — and four governance documents — accessibility
  mapping, channel mapping, brand and Product Profile boundary, governance and
  lifecycle.

### The load-bearing statements

| Statement | Why it matters |
| --- | --- |
| **The visual foundation introduces no layer** | It occupies positions in the existing eight-layer model and five-layer token flow. The conceptual *primitive → semantic → context → brand* reading maps onto them; **context is not a layer**, and the **Component layer must not be dropped** from that reading |
| **COLOUR ≠ STATUS · ICON ≠ STATUS · MOTION ≠ STATUS** | Status meaning stays with the Semantic Status Foundation. Visual encoding is **redundant** to meaning, never a substitute. The binding itself is **CDS-WP-023's**, gated by CDS-WP-024 |
| **An interaction state is not a semantic status** | A validation outcome is not a status `condition`; conflating them destroys both |
| **A theme re-binds; it never redefines** | It may change which primitive a role resolves to; never what the role means, and never an accessibility guarantee |
| **Roles are mandatory; values vary only at named extension points** | This is why a Core product inherits every Core *role* but not automatically every Core *value* |
| **The named extension-point set is empty** | So **no visual override is currently possible**, and no Product Profile can be approved |
| **Every semantic colour role declares its contrast obligation** | An unstated obligation cannot be validated, themed, or profiled safely |
| **Focus visibility has no permitted mechanism of removal** | Not by a theme, a profile, an exception, or a consumer override |

### Positioned, not registered

Three subjects were **positioned** inside already-registered scope rather than
registered as new scope — in each case the conservative reading:

- **Opacity** — an *attribute* of VF-1 (alpha) and VF-6 (overlay, scrim), because
  it is named in **no** registered scope statement.
- **Illustration and imagery** — **Layer 2 Brand and Identity**, consumed through a
  declared interface, because DEC-S-021 Layer 3 registers *iconography* and not
  them.
- **Focus indication** — a **cross-family role set**, so no single family's change
  can weaken it unnoticed.

### The accessibility finding

Re-counting the WCAG 2.2 AA Applicability Matrix: **14** criteria map to Layer 3,
and **all five** criteria the matrix classifies as `Normative CDS requirement` — the
ones CDS owns **without** the consumer — are among them: **1.3.3, 1.4.1, 1.4.5,
2.3.1, 2.4.7**.

> **Every criterion CDS owns alone is a visual foundation criterion.**

**Evidence state: AE-0 throughout.** No visual artifact exists, none has been
evaluated, and **no accessibility claim of any level is valid**. The single admitted
package `AE1-CDS-WP016-SEMSTATUS-004` covers the Semantic Status source scope only
and **does not transfer**.

### The honesty record

**No registered consumer requirement asks for a colour palette, a typographic
scale, a spacing scale, a radius scale, an elevation model, an icon library, or
illustration.** Six consumer requirements anchor Layer 3 — **CR-002, CR-006,
CR-021, CR-022, CR-023, CR-025** — and four families (**VF-3, VF-5, VF-6, VF-7**)
carry **no consumer demand evidence at all**. Registering structure is not
establishing demand.

### What it deliberately left open

The theme **mechanism** (CDS-WP-022) · the responsive **model** and the Layer 3 /
Layer 5 split (CDS-WP-021) · the status-to-visual **binding** (CDS-WP-023) · the
admitted DTCG `$type` set and the concrete vocabulary (CDS-WP-020 — **still open**;
recorded as **OD-2** and **OD-6**) · the named extension-point set (CDS-WP-032) ·
every visual value.

### What it did not do

It created **no** visual value, token source file, schema, validator rule,
diagnostic, component, channel adapter, brand, identity, or Product Profile;
produced and admitted **no** evidence; changed **no** maturity; **registered no new
Decision, ADR, or risk** — every binding statement applies a decision already in
force; **renamed no phase**; registered **no** capability; made **no** claim; and
activated **no** later work package. It touched **no** Semantic Status source,
revision, maturity, or evidence package.

## Reference and Semantic Token Foundation (CDS-WP-020)

**Contract only. No visual value exists in CDS, and CDS-WP-020 created none** —
verified by search at the baseline, not assumed: no hexadecimal colour literal, no
`colorSpace` or `components` member, and no `px`, `rem`, `em`, or `pt` dimension
literal anywhere in the tracked token sources or schemas. **No identifier was
created either.**

### What it established

- The [Visual Reference Token Foundation](../docs/architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md) —
  token-flow layer **1**. *A reference token is a value without a purpose.* Ten
  obligations (RP-1 … RP-10), seven requirements on any future scale
  (ST-1 … ST-7), the reference naming rules (RN-1 … RN-9), provenance and lifecycle
  (RV-1 … RV-5), the theme and profile boundary (RB-1 … RB-5), the machine-readable
  disposition, and ten validation requirements handed to CDS-WP-024.
- The [Visual Semantic Token Foundation](../docs/architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) —
  token-flow layer **2**. *A semantic role is a named purpose that resolves to a
  value it does not own.* Twelve universal role obligations (SR-1 … SR-12)
  consolidating the CDS-WP-019 family obligations, the **alias model**
  (AL-1 … AL-8), semantic naming (SN-1 … SN-9), channel and product neutrality
  (PN-1 … PN-5), theme compatibility (TC-1 … TC-7), the Semantic Status boundary
  (SS-1 … SS-8), the **focus role set**, state-role constraints (IS-1 … IS-5), and
  fifteen validation requirements.
- The [Visual Token Value Selection Rules](../docs/governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md) —
  *no visual value enters CDS without a recorded reason that someone else can
  disagree with.* Seven prerequisites, a twelve-criterion evaluation, ten
  inadmissible grounds, the eight-field value record, ten accessibility constraints,
  the validation strategy, and the lifecycle disposition.
- The **non-normative**
  [Visual Token Foundation Open Decisions](../docs/roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
  register — **OD-1 … OD-7**.

### The three rules worth remembering

- **A reference token cannot be accessible.** Accessibility is a property of a
  pair, a composition, and a context — none of which exists at layer 1. Obligations
  are declared at the **semantic** layer, where they can be checked.
- **An alias transports a value, never an obligation** (AL-7). If obligations
  travelled along aliases, a theme could satisfy an accessibility obligation by
  re-binding, and the role would stop being where the obligation is checked.
- **The machinery was always sufficient; the decisions were not.** Nothing in the
  format profile, the schemas, the validator, or the serialization contract blocks a
  visual source set. Writing one anyway would have settled OD-1 … OD-5 by
  implication — **acquiring** authority rather than receiving it (DEC-S-033). **All
  seven choices are now made or dispositioned, and a source set still may not be
  written**: **VP-3, VP-5, VP-6 and VP-7 are unsatisfied for every family**, VP-2 is
  unsatisfied for typeface identity, weight identity and composites, and the four
  Step-9 decisions are **effective at `2cb244e8…`**. **Deciding an identifier
  is not creating one.**

### Why it returned `DECISION_REQUIRED`

Seven normative choices that no committed CDS source has made gate every concrete
value and every machine-readable visual source: the **colour space** (OD-1), the
**admitted `$type` set** (OD-2), the **visual source-set identity and topology**
(OD-3), the **identifier grammar** (OD-4), **scale topology** (OD-5), the **role
vocabulary and family granularity** (OD-6), and the **sequencing against
CDS-WP-022** (OD-7). The five earlier work packages that made comparable
first-of-their-kind normative choices — **CDS-WP-011 … CDS-WP-015** — each
registered a Decision block, and three of them an ADR; CDS-WP-020 could register
neither on its own authority, so it escalated instead.

**The escalation was answered on 2026-08-27.** The Human Maintainer separately
authorized a bounded **Decision Integration Pass**, which **prepared** **DEC-S-128**
(one canonical `srgb` colour representation; OKLCH derivational only),
**DEC-S-129** (**WCAG 2.2** contrast evaluation authority; full-precision
comparison; APCA and other methods informational only), **DEC-S-130** (an explicit,
minimal, closed `$type` admission profile — `color`, `dimension`, `number`;
explicit own typing; no composites; **`profileVersion` stays `1`**), **DEC-S-131**
(the **Source Set** as the independently evaluable unit; **AGGREGATED is not
MATURE**) and **ADR-0004**. **All five are effective**, at the Human-Maintainer
integration commit `42a568d8…`. They answer **OD-1, OD-2 and OD-3** and **select no
value**. **The remaining four were decided on 2026-09-05** by the **CDS Step-9
Decision Integration Pass**, which prepared **DEC-S-132** (family-rooted identifier
grammar, the `qualifier` position, the layer kept out of every path, two separate
identity spaces, and the fixed roots and source-set identities), **DEC-S-133**
(per-family scale ownership under the unchanged ST-1 … ST-7 contract, **no
universal cross-family base**, `SCALE TOPOLOGY ≠ SCALE VALUES`), **DEC-S-134** (a
cross-consumer role **admission rule** only), **DEC-S-135** (no default role alias
before CDS-WP-022) and **ADR-0005** — **all effective**, at the Human-Maintainer
integration commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`; **OD-6B needed no
Decision**. **VP-3, VP-5, VP-6 and VP-7
stay unsatisfied**, **a new risk entry is still not recommended and `RISK-099` is
not required**, and the value half stays gated. *(The pass itself did not close CDS-WP-020; its
effectivity qualification was not reconciled by the closure and routing pass, and
has since been reconciled by the separately authorized post-integration
effectiveness reconciliation — see `F-020C-01` in the
[Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md).)*

### What it did not do

It created **no** visual value, identifier, token source file, manifest, resolver,
schema, validator rule, diagnostic, test, fixture, component, channel adapter,
brand, identity, or Product Profile; produced and admitted **no** evidence; changed
**no** maturity — all nine families stay **`Proposed`**, visual source sets stay
**0**, visual Candidate families stay **0**; **registered no new risk** — the Risk
Register stays at **98**, and **`RISK-099` is not required**. *(At the original
milestone it also registered no Decision and no ADR, with the registers at **127**
and the ADR range at **ADR-0001 … ADR-0003**; the separately authorized 2026-08-27
Decision Integration Pass registered **DEC-S-128 … DEC-S-131** and **ADR-0004**,
which are **effective at `42a568d8…`**.)* It **renamed no phase**; registered **no** capability; made
**no** claim; and activated **no** later work package. It touched **no** Semantic
Status source, revision, maturity, approval, or evidence package, and
**`AE1-CDS-WP016-SEMSTATUS-004` was not transferred to anything**. **CR-004's
registered Layer-5 mapping is unchanged**, and **no test expectation was weakened
and no fixture rewritten.**

## Theme and Environmental Presentation Model (CDS-WP-022)

**Contract only. No theme instance, machine-readable context identifier, default
alias, or visual value exists in CDS, and CDS-WP-022 created none.** Verified by
search at the baseline. Result: **`COMPLETE WITH NOTES`**, after first returning
**`DECISION_REQUIRED`** — which **stands as execution history**. **Supported Theme
Resolution Contexts: 0 until `DEC-S-138` is effective; `Light` and `Dark`, with no
default, from then.**

**Authority.** Authorized separately and explicitly by the Human Maintainer after
the CDS-WP-021 closure. **`SEQUENCED NEXT ≠ AUTHORIZED`**, **`CLOSED ≠ SUCCESSOR
AUTHORIZED`**, **`DEPENDENCY SATISFIED ≠ AUTHORITY GRANTED`** — the `DEC-S-135`
recommendation that named CDS-WP-022 authorized nothing, and the authorization came
from the Human Maintainer alone.

### What it established

- **The term.** A **Theme Resolution Context** is a **named presentation condition**
  under which approved semantic roles resolve to approved primitives, with no change
  to what a role means or whether it exists. **"Theme" and "Theme Resolution Context"
  are the same construct.** **Environmental presentation** is the *category* of
  condition arising from the circumstances of viewing — **a category name, not a
  construct**.
- **Context admission (CA-1 … CA-13).** A context is **declared, named and
  enumerable**, admitted **only** by an explicit Human-Maintainer decision as an
  **Elevated** change, must **vary within** a channel rather than **be** one, must
  apply **across** products, carries **no meaning**, resolves every role or
  **declares the limitation**, preserves **every** contrast obligation, pairing and
  the focus indicator, resolves **deterministically and offline with provenance**, is
  **never** a place to repair a Core gap, carries **its own non-transferring
  evidence**, and **presupposes no context count**. **`CANDIDATE ≠ SUPPORTED
  CONTEXT`**, and **CA-1 … CA-13 are satisfiable by zero contexts — which is the
  current state.**
- **Context identity (CI-1 … CI-6).** A context identifier lives in the resolution
  declaration and **nowhere else**: never in a token path (T-8, N-6, TC-1), never in
  a Source Set identifier (**DEC-S-132 clause 12** introduces **no `context` or
  `theme` segment at any position**), and never as a token-flow layer. **No context
  identifier was created, adopted, reserved, or recommended.**
- **Selection and resolution entry (CS-1 … CS-11).** Resolution takes a **requested
  context as an input**, and **CDS resolves for a context without performing the act
  of selecting one** — it cannot, without naming technology or holding runtime state,
  both prohibited. **`DETERMINISTIC RESOLUTION ≠ DETERMINISTIC SELECTION`**: **T-6**
  conditions determinism on a context **already given**, so **CS-8's precedence rule
  is a Human-Maintainer policy decision, not a derivation**.
- **Environmental inputs (CE-1 … CE-5).** **No input kind is registered.** No CDS
  artifact records, stores, transmits, or profiles an environmental input, and **an
  environment is not a context** — it may cause one to be requested, and is never
  itself the context.
- **Fail-closed conditions (CF-1 … CF-11).** An unsupported requested context, an
  unresolvable role, a broken obligation or pairing, a weakened focus role, a
  non-deterministic or online resolution, a missing context provenance, a profile
  reaching through a context, a context identifier in a path or Source Set
  identifier, and a class-1 / class-2 conflict all **fail closed**. **`FAIL CLOSED ≠
  DEGRADED OUTPUT`**, and **no automatic repair exists.**
- **Composition boundaries (CB-1 … CB-7).** Channel, **Spatial Context**, Product
  Profile, semantic role identity, Semantic Status, Source Set, and the five
  token-flow layers. **`SPATIAL CONTEXT ≠ THEME RESOLUTION CONTEXT`** (**DEC-S-136**,
  **CX-9**) and **CDS Core declares no composition** of the two — the conservative
  reading CDS-WP-021 preserved, which **forecloses nothing**.
- **The mechanism, decided.** A **Product Profile** mechanism and a **per-context
  token path** are **excluded**; a **per-context Source Set** is **unavailable** under
  **DEC-S-131 clause 5** and **DEC-S-132 clauses 10 and 12**; making the **Resolver a
  second maturity unit** is excluded by `DEC-S-137` clauses 6 and 8. The Human
  Maintainer chose the **Resolver-Modifier Context over the existing Source-Set
  graph** — **`DEC-S-137`**, **TM-1 … TM-12** — **the only one of the five candidates
  that amends nothing**. Context-specific evidence stays bound to (`sourceSetId`,
  `sourceRevision`) and records the **Resolver / Composition revision** and the
  **Theme Resolution Context** as **exact evidence inputs**: **`EVIDENCE INPUT ≠
  MATURITY CARRIER`**, and **any change to either invalidates or supersedes the
  affected evidence** (**TM-9**).
- **Neutral / document — answered by existing authority, no new Decision required.**
  Its named manifestations (documentation, paginated reports, slide decks) **are
  channels**; **`SYMMETRY IS NOT EVIDENCE`**.
- **A recorded machine-readable gap.** The committed resolver schema **cannot express
  a context condition**, and the validator records **resolver modifier semantics as
  not validated** (DEC-S-098). A **declared coverage boundary, not a DEC-S-034
  conflict** — routed to **`CDS-WP-020A`** and **CDS-WP-024**.

### The five decided questions

**The `WP022-D*` keys were execution-local report keys, not governance identifiers.**
CDS-WP-022 escalated them; **the Human Maintainer decided all five on 2026-09-12**,
and a bounded rework applied them.

| Key | Decision | Recorded as |
| --- | --- | --- |
| **`WP022-D1`** | **Resolver-Modifier Context** over the existing Source-Set graph; context evidence bound to (`sourceSetId`, `sourceRevision`) with the **Resolver / Composition revision** and **Theme Resolution Context** as exact inputs; **no per-context Source Set**; **no second maturity unit**; **Theme and Spatial Context orthogonal**, joint evaluation deferred | **`DEC-S-137`** · **`ADR-0007`** (covering `DEC-S-137` **only**) · **TM-1 … TM-12** |
| **`WP022-D2`** | **`Light` and `Dark`**, equal peers, **neither the default**; **no machine-readable identifier authored** | **`DEC-S-138`** part A |
| **`WP022-D3`** | **Platform condition; no CDS Core High-Contrast Theme at this stage**; binding independently of Theme selection; a future dedicated theme needs separate authorization | **`DEC-S-138`** part B |
| **`WP022-D4`** | **Explicit viewer choice > inferred environment preference**; mandatory platform accessibility conditions **outside** Theme precedence and always binding; consumer or runtime owns sensing, persistence and transport; **no technology named** | **`DEC-S-138`** parts C and D · **CS-8 … CS-11** |
| **`WP022-D5`** | **No default and no fallback Theme**; **fail closed** on missing, unsupported and unresolved conflict; **no silent substitution**; **`Not Applicable`** where genuinely inapplicable | **`DEC-S-138`** parts E, F and G · **CF-9**, **CF-11** |

**Effectivity.** **All three records are `Accepted` and effective at the
Human-Maintainer exact-object integration commit
`23914ecc48c1fb3cba5e3dab97a505589e821b6b`** of the reviewed CDS-WP-022 object —
**`APPROVED PROPOSITION ≠ EFFECTIVE REPOSITORY DECISION`** held until it, and **a
review PASS is not a commit**. **136 decisions and 6 ADRs until it; 138 and 7 from it. Risks stay at 98 throughout — no `RISK-099`, no
`DEC-S-139`, no `ADR-0008`.** **`ACCESSIBILITY OBLIGATION ⇏ CDS SHIPS A HIGH-CONTRAST
THEME`**, and **`COULD` ≠ `MUST`** for CR-025 — admitting `Light` and `Dark` was a
**priority decision, not new evidence**.

### What CDS-WP-022 explicitly did not do### What CDS-WP-022 explicitly did not do

Across both passes it created **no** theme instance, machine-readable context
identifier, default alias, visual value, identifier, role, primitive, alias, source
set, manifest, resolver instance, `sourceSetId`, `sourceRevision`, token source file,
schema, validator rule, test, fixture, component, brand, or Product Profile —
**`Light` and `Dark` are human-readable architectural names, not identifiers**. It
produced and admitted **no** evidence — admitting two contexts adds **two evidence
obligations and zero evidence**; changed **no** maturity — **VF-1 … VF-9 stay
`Proposed`**, visual Candidate families stay **0**; accepted, closed, or re-scored
**no** risk and added **no** risk entry — the register stays at **98** with **no
`RISK-099`**; renamed **no** phase; registered **no** capability; made **no** claim;
determined **no** conformance; and activated **no** work package. It **prepared** two
Decisions and one ADR — **`DEC-S-137`**, **`DEC-S-138`** and **`ADR-0007`**, which were
**not effective until the Human-Maintainer exact-object integration commit of the
reviewed object** and are **`Accepted` and effective at
`23914ecc48c1fb3cba5e3dab97a505589e821b6b`** — and **created no `DEC-S-139` and no
`ADR-0008`**. **`DEC-S-131`,
`DEC-S-132`, `DEC-S-135` and `DEC-S-136` are untouched in byte and in substance**;
**TS-1 still binds** because `DEC-S-138` part E creates no default alias; **`WP021-D2`
stays deferred**; and **VP-3, VP-5, VP-6 and VP-7 stay `UNSATISFIED`** with **VP-4
still `UNSATISFIED` for VF-4**. It touched **no** Semantic Status source, revision,
maturity, approval, or evidence package, and **`AE1-CDS-WP016-SEMSTATUS-004` was not
transferred to anything.** **CDS-WP-022 is not closed.**

## Related documents

- [Concept and Scope](../docs/governance/CONCEPT_AND_SCOPE.md) — normative scope source
- [Consumer and Stakeholder Model](../docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md)
- [Scope Boundary Matrix](../docs/governance/SCOPE_BOUNDARY_MATRIX.md)
- [Foundation Context Pack](../project-system/CONTEXT_PACK_FOUNDATION.md)
- [Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md)
- [Visual Foundation Theme Architecture](../docs/architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md) — VF-9; CDS-WP-019 and CDS-WP-022
- [Project Charter](../docs/governance/PROJECT_CHARTER.md)
- [Project Profile](../project-system/PROJECT_PROFILE.md)
- [Work Packages](../project-system/WORK_PACKAGES.md)
- [Next Phase](../project-system/NEXT_PHASE.md)
- [CDS-WP-001 Governance Bootstrap Notes](CDS_WP_001_GOVERNANCE_BOOTSTRAP_NOTES.md)
- [CDS-WP-002 Concept and Scope Registration Notes](CDS_WP_002_CONCEPT_AND_SCOPE_REGISTRATION_NOTES.md)
- [CDS-WP-003 Benchmark and Differentiation Research Notes](CDS_WP_003_BENCHMARK_AND_DIFFERENTIATION_RESEARCH_NOTES.md)
- [CDS-WP-004 Consumer Requirements and CoreOps Pilot Notes](CDS_WP_004_CONSUMER_REQUIREMENTS_AND_COREOPS_PILOT_NOTES.md)
- [CDS-WP-005 Design System Architecture Notes](CDS_WP_005_DESIGN_SYSTEM_ARCHITECTURE_NOTES.md)
- [CDS-WP-006 Governance, Versioning and Contribution Notes](CDS_WP_006_GOVERNANCE_VERSIONING_AND_CONTRIBUTION_NOTES.md)
- [CDS-WP-007 Accessibility and Inclusive Design Policy Notes](CDS_WP_007_ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY_NOTES.md)
- [CDS-WP-008 Foundation Milestone Review Notes](CDS_WP_008_FOUNDATION_MILESTONE_REVIEW_NOTES.md)
- [CDS-WP-009 Operating Enablement and Pre-Candidate Notes](CDS_WP_009_OPERATING_ENABLEMENT_AND_PRE_CANDIDATE_NOTES.md)
- [CDS-WP-010 Accessibility Support Baseline Notes](CDS_WP_010_ACCESSIBILITY_SUPPORT_BASELINE_NOTES.md)
- [CDS-WP-011 Machine-Readable Source and Token Format Notes](CDS_WP_011_MACHINE_READABLE_SOURCE_AND_TOKEN_FORMAT_NOTES.md)
- [CDS-WP-012 Machine-Readable Bootstrap and Validation Notes](CDS_WP_012_MACHINE_READABLE_BOOTSTRAP_AND_VALIDATION_NOTES.md)
- [CDS-WP-013 Offline Validator and Fixture Harness Notes](CDS_WP_013_OFFLINE_VALIDATOR_AND_FIXTURE_HARNESS_NOTES.md)
- [CDS-WP-014 Semantic Status Foundation Notes](CDS_WP_014_SEMANTIC_STATUS_FOUNDATION_NOTES.md)
- [CDS-WP-015 Semantic Status Source and Evidence Notes](CDS_WP_015_SEMANTIC_STATUS_SOURCE_AND_EVIDENCE_NOTES.md)
- [CDS-WP-017 Post-WP-016 Roadmap Reconciliation Notes](CDS_WP_017_POST_WP016_ROADMAP_RECONCILIATION_NOTES.md)
- [CDS-WP-018 Deferred Governance Hygiene Notes](CDS_WP_018_DEFERRED_GOVERNANCE_HYGIENE_NOTES.md)
- [CDS-WP-019 Core Visual Foundation Architecture Notes](CDS_WP_019_CORE_VISUAL_FOUNDATION_ARCHITECTURE_NOTES.md)
- [CDS-WP-020 Closure and Authoring Routing Notes](CDS_WP_020_CLOSURE_AND_AUTHORING_ROUTING_NOTES.md)
- [CDS-WP-020 Reference and Semantic Token Foundation Notes](CDS_WP_020_REFERENCE_AND_SEMANTIC_TOKEN_FOUNDATION_NOTES.md)
- [Visual Foundation Architecture](../docs/architecture/VISUAL_FOUNDATION_ARCHITECTURE.md) — CDS-WP-019 entry point
- [Visual Reference Token Foundation](../docs/architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md) · [Visual Semantic Token Foundation](../docs/architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) — CDS-WP-020 entry points
- [Visual Token Value Selection Rules](../docs/governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
- [Visual Token Foundation Open Decisions](../docs/roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md) — **non-normative**
- [Foundation Milestone Review](../docs/reviews/FOUNDATION_MILESTONE_REVIEW.md)
- [Foundation Closure Record](../docs/governance/FOUNDATION_CLOSURE_RECORD.md)
- [Accessibility Support Baseline](../docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
- [ADR-0001 — Machine-Readable Token Source Format](../docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
- [ADR-0002 — Deterministic JSON Serialization](../docs/decisions/ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md)
- [ADR-0003 — Offline Token Validator Implementation Stack](../docs/decisions/ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md)
- [ADR-0004 — Visual Token Representation and Source Identity Architecture](../docs/decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md) — **`Accepted`, effective at commit `42a568d8…`**
