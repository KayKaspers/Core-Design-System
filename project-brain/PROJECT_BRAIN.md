# Core Design System — Project Brain

Compact long-term orientation for the Core Design System (CDS). This document
summarizes; it does not duplicate the normative documents it points to.

- **Project:** Core Design System (CDS)
- **Repository:** KayKaspers/Core-Design-System
- **Local path:** `D:\Projects\Core-Design-System`
- **Framework:** Nova Development Framework v1.0.0
- **Phase:** Pre-Candidate Operating Enablement — **Foundation / Pre-Design:
  Closed with Notes**

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

- Decisions: DEC-S-001 … DEC-S-124 (124) — 6 foundation + 6 scope + 8 consumer
  and pilot scope + 12 logical architecture + 16 governance + 12 accessibility +
  4 operating enablement and pre-candidate + 8 accessibility support baseline and
  evidence + 10 machine-readable source and token format + 10 machine-readable
  bootstrap and validation + 12 offline validator implementation + 10 semantic
  status foundation + 10 semantic status source and evidence decisions ·
  **ADRs: 3 (ADR-0001, ADR-0002, ADR-0003)**
- Risks: RISK-001 … RISK-097 (97) — **90 Monitored; RISK-040, RISK-044, RISK-066,
  RISK-067, RISK-068, RISK-069, RISK-071 Mitigating**; **owner model finalized**;
  no risk accepted or closed
- Completed work packages: CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005, CDS-WP-006, CDS-WP-007, CDS-WP-008, CDS-WP-009, CDS-WP-010,
  CDS-WP-011, CDS-WP-012, CDS-WP-013, CDS-WP-014, CDS-WP-015
- Next work package: **CDS-WP-016 — Semantic Status Foundation Independent Evidence
  Review and Candidate Gate** (authorized as next; not yet executed). Foundation
  **Closed with Notes**; machine-readable machinery implemented and executed
  (ADR-0001…0003); Semantic Status Foundation **Contract defined (CDS-WP-014)** and
  **machine-readable implemented (CDS-WP-015: `semantic/status`, 25 non-visual
  tokens, 24/24 harness matches, 25/25 DE/EN, Draft dossier — executor-produced,
  independently unreviewed, Not Candidate)**

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
| DEC-S-062 | First post-Foundation phase is Pre-Candidate Operating Enablement. |
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
| RISK-031 | Maturity inflation. | Monitored |
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
| RISK-066 | Schema and validator divergence. | Monitored |
| RISK-067 | Canonicalization and digest mismatch. | Monitored |
| RISK-068 | Duplicate-key ambiguity. | Monitored |
| RISK-069 | Manifest and resolver graph inconsistency. | Monitored |
| RISK-070 | Validation fixture coverage gap. | Monitored |
| RISK-071 | Validation expectation drift. | Monitored |
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
no publication change · **no release is possible** — all tracing to the undefined
accessibility target (CR-024) and absent licensing decisions.

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
now exist — **not because anything was tested; every artifact is AE-0**.

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
framework, token build system, documentation platform, package
architecture, repository split, license, public release, contribution model,
long-term compatibility commitments, concrete product signatures, versioning
and maturity model, conformance and adoption policy, or product profile and
override governance.

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
artifact is
AE-0; no support baseline exists** (RISK-041, RISK-044).

**Channels:** six profiles; only two (Web UI, Web Docs) have a target; **none is
Candidate- or Stable-eligible** (DEC-S-058).

**Limits:** accessibility cannot be waived by an ordinary exception (DEC-S-059);
no legal or certification statement (policy boundary, standard-status doc); native
semantics first, APG
examples informative only (DEC-S-054).

**CR-024 / pilot:** resolved at policy level; entry criterion satisfiable on
Human Maintainer commit. **The CoreOps pilot has not started and cannot start; no
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

Defined the first accessibility support baseline **A11Y-BL-001** (pending
Human-Maintainer commit) using authorized official standards/vendor research
(13 URLs opened, 9 usable) — **no test run, no tool selected, every artifact AE-0,
no environment claimed supported**:

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

**CDS-WP-016 — Semantic Status Foundation Independent Evidence Review and
Candidate Gate** (authorized as next; not yet executed): independent review of the
WP-013/WP-015 evidence by a separately authorized reviewer (re-execution or
artifact assessment), traceability/accessibility/content/dossier review, the
Candidate-gate recommendation, and the Human-Maintainer decision — **no automatic
Candidate promotion, still no visual values, no pilot.** Execution begins only on
an explicit Nova prompt and Human-Maintainer authorization.

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
- [Foundation Milestone Review](../docs/reviews/FOUNDATION_MILESTONE_REVIEW.md)
- [Foundation Closure Record](../docs/governance/FOUNDATION_CLOSURE_RECORD.md)
- [Accessibility Support Baseline](../docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
- [ADR-0001 — Machine-Readable Token Source Format](../docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
- [ADR-0002 — Deterministic JSON Serialization](../docs/decisions/ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md)
- [ADR-0003 — Offline Token Validator Implementation Stack](../docs/decisions/ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md)
