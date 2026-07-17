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

**Pre-Candidate Operating Enablement — Foundation / Pre-Design: Closed with Notes**

The Foundation is **closed with mandatory notes** (CDS-WP-009): governance, scope,
architecture, requirements, and the accessibility policy are established, and the
committed governance is now operationalized for daily use. A lightweight
[operating playbook](docs/operations/FOUNDATION_OPERATING_PLAYBOOK.md) and
[Standard](docs/operations/STANDARD_CHANGE_DOSSIER_TEMPLATE.md) /
[Elevated](docs/operations/ELEVATED_CHANGE_DOSSIER_TEMPLATE.md) change-dossier
templates exist, and the twelve Critical Risks are made actionable in a
[Critical Risk Action Register](docs/operations/CRITICAL_RISK_ACTION_REGISTER.md).
The first **accessibility support baseline** (A11Y-BL-001) is **defined** (CDS-WP-010,
pending commit) — a **test contract, not evidence**. The **machine-readable source
format is decided** (CDS-WP-011): a **DTCG 2025.10-based CDS profile** in **strict
JSON**, recorded in [ADR-0001](docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
(pending commit) — **no token value or schema is implemented**. **No accessibility test
has been run, every artifact is AE-0, no Candidate or Stable artifact exists, no claim
is valid, no licence is selected, and the publication state remains `Private
Development`.** The next work package is **CDS-WP-012 — Machine-Readable Source
Bootstrap and Validation Contract**.

The project does not yet produce visual design.

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
- token build system,
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

## Benchmark research

Benchmark and differentiation research is complete. Ten established design
systems were reviewed against 14 dimensions using official publisher sources
only, and eight CDS differentiation hypotheses were assessed.

**The research is not normative.** It is evidence and hypotheses — not
decisions, principles, or technology recommendations. No hypothesis reached
"Strongly supported", and no decision was added or changed by the research.

- [Design System Benchmark](docs/research/DESIGN_SYSTEM_BENCHMARK.md)
- [Benchmark Evidence Matrix](docs/research/BENCHMARK_EVIDENCE_MATRIX.md)
- [Benchmark Source Register](docs/research/BENCHMARK_SOURCE_REGISTER.md)
- [CDS Differentiation Hypotheses](docs/research/CDS_DIFFERENTIATION_HYPOTHESES.md)
- [Research Limitations](docs/research/RESEARCH_LIMITATIONS.md)

## Consumer requirements and the CoreOps pilot

Requirements from real consumer projects are registered, and a bounded CoreOps
pilot contract is defined.

Three consumers were analyzed **read-only** at committed revisions: CoreOps as
primary pilot consumer, with SpeakCore and CastCore as secondary cross-product
evidence. 40 requirements (CR-001 … CR-040) are registered and traced to their
source revisions.

The CoreOps pilot is a **bounded representative slice**, not a redesign, across
five groups: Application Foundation · Operations Overview · Inventory and Dense
Data · State and Safety Patterns · Help, Accessibility and Localization.

The eight research hypotheses were assessed against consumer evidence.

**Boundaries:** evidence is committed documentation only — no user research,
interviews, or usability testing took place. No requirement is an accepted CDS
standard. The pilot contract is a proposal and is not active. **Nothing here
constitutes CDS adoption, conformance, certification, or endorsement.**

- [Consumer Requirements Model](docs/governance/CONSUMER_REQUIREMENTS_MODEL.md)
- [Consumer Requirements Traceability](docs/governance/CONSUMER_REQUIREMENTS_TRACEABILITY.md)
- [CoreOps Pilot Scope and Scenarios](docs/governance/COREOPS_PILOT_SCOPE_AND_SCENARIOS.md)
- [CoreOps Pilot Contract](docs/governance/COREOPS_PILOT_CONTRACT.md)
- [Consumer Validation Plan](docs/governance/CONSUMER_VALIDATION_PLAN.md)
- [Consumer Evidence Register](docs/research/CONSUMER_EVIDENCE_REGISTER.md)
- [Consumer Hypothesis Validation](docs/research/CONSUMER_HYPOTHESIS_VALIDATION.md)

## Logical architecture

The CDS logical architecture is defined. It describes structure, responsibility,
authority, and flow — and **selects no technology and no design**.

**Eight architecture layers:** Strategy and Governance · Brand and Identity ·
Foundations and Tokens · Components · Patterns and Experiences · Channels and
Communication · Distribution and Enablement · Evidence and Quality.

**Source-of-Truth and Authority Model** — eight artifact classes with an explicit
authority matrix. Only normative sources bind; generated artifacts, design-tool
state, examples, and research never do. Conflicts fail closed, and recency
confers no authority.

**Conceptual token flow** — Reference → Semantic → Component → Product Profile
Overrides → Channel/Platform Outputs. Semantic-first. No format, naming
convention, or tool is chosen.

**Product Profile and Reconciliation Model** — variation happens at approved
extension points only, and may never redefine shared semantics, weaken
accessibility, distort status truth, or break contracts. Consumers that already
hold their own design decisions are **reconciled, not overwritten**.

**Architecture traceability** — all 40 consumer requirements (CR-001 … CR-040)
are mapped to the architecture, with deferred items named rather than hidden.

**Boundaries:** this is structure, not implementation. Nothing is built, no
component or token exists, no repository topology, tool, format, framework, or
licence is selected, and no accessibility conformance level is claimed. Governance
policy and an accessibility target now exist; the architecture still awaits design,
implementation, and evidence.

- [Design System Architecture](docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md)
- [Source of Truth and Authority Model](docs/architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)
- [Token and Theme Architecture](docs/architecture/TOKEN_AND_THEME_ARCHITECTURE.md)
- [Product Profile and Extension Model](docs/architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md)
- [Artifact Distribution and Channel Model](docs/architecture/ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md)
- [Consumer Contract and Reconciliation Model](docs/architecture/CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md)
- [Evidence, Traceability and Status Semantics](docs/architecture/EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md)
- [Architecture Requirements Traceability](docs/architecture/ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md)

## Governance

The CDS governance model is defined. It states who decides what, and under which
conditions — and **selects no licence, publication state, technology, or design**.

**Six roles** — Human Maintainer (final approval; exclusive Git, release,
publication, and licensing authority) · Nova (governance and risk control,
review) · Claude (scoped executor) · Consumer Maintainer · Contributor ·
Evidence Reviewer. Creating, implementing, or using an artifact grants no
authority.

**Two governance tracks** — Standard and Elevated. Ceremony scales with risk;
the mandatory gates do not.

**Seven maturity states** — Proposed · Exploratory · Experimental · Candidate ·
Stable · Deprecated · Removed. Candidate is mandatory before Stable. Maturity,
release version, and publication state are three **independent** axes. **No
artifact is currently Candidate or Stable.**

**Versioning and compatibility** — MAJOR.MINOR.PATCH with an honest pre-1.0
policy. Compatibility is declared across eight contract axes; an unassessed axis
is never reported as compatible. `latest` is not a valid identity.

**Contribution and exception governance** — a controlled acceptance process where
keeping something consumer-local is a first-class outcome. Exceptions are
bounded, owned, and expiring.

**Adoption claims** — four graded, scope- and version-bound claim types. The
claim `CDS certified` is prohibited. **No adoption, validation, or conformance
claim is currently valid — by anyone, including CDS itself.**

**Risk ownership is finalized** — the Human Maintainer is accountable for all 48
risks; Nova is the Risk Controller.

**Publication state: `Private Development`.** Licensing is decided per ten
artifact classes, and **no licence has been selected for any of them**. A
publication-state change requires an explicit gate that cannot currently be
satisfied.

- [Governance Operating Model](docs/governance/GOVERNANCE_OPERATING_MODEL.md)
- [Source Conflict Resolution Policy](docs/governance/SOURCE_CONFLICT_RESOLUTION_POLICY.md)
- [Artifact Maturity Lifecycle](docs/governance/ARTIFACT_MATURITY_LIFECYCLE.md)
- [Versioning, Compatibility and Deprecation Policy](docs/governance/VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md)
- [Contribution and Acceptance Model](docs/governance/CONTRIBUTION_AND_ACCEPTANCE_MODEL.md)
- [Exception and Product Profile Governance](docs/governance/EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md)
- [Adoption, Conformance and Claims Policy](docs/governance/ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md)
- [Risk Governance Model](docs/governance/RISK_GOVERNANCE_MODEL.md)
- [Licensing and Publication Decision Model](docs/governance/LICENSING_AND_PUBLICATION_DECISION_MODEL.md)
- [Release and Change Control Policy](docs/governance/RELEASE_AND_CHANGE_CONTROL_POLICY.md)

## Accessibility

The CDS **accessibility and inclusive-design policy is defined**. It sets a
target and an evidence discipline — and **claims nothing**.

**Target: WCAG 2.2 Level AA** for the applicable web-based scope, resolving CR-024
at policy level. This is a **target, not current conformance** — no CDS artifact
has been evaluated, every artifact is at evidence level **AE-0**, and **no
accessibility claim of any level is valid**, by anyone.

**Applicability matrix** — all Level A and AA success criteria are mapped: 56
listed, 55 applicable (the obsolete 4.1.1 excluded by the standard itself). No
pass/fail judgement is made. **49 of the 55 need action from both CDS and the
consumer** — accessible artifacts do not compose into an accessible product by
themselves.

**Five evidence levels** — AE-0 (not assessed) through AE-4 (consumer complete
process). Automated checking alone is never sufficient; AE-3 requires a declared
support baseline — now **defined** as **A11Y-BL-001** (CDS-WP-010, pending commit):
three tiers, a 14-entry environment matrix, an evidence strategy, a maintenance
policy, and a defect/regression model. The baseline is a **test contract, not
evidence** — **no test has been run and every artifact remains AE-0**.

**Six channel profiles** — only web UI and web documentation carry a WCAG target;
non-web channels each need their own profile and are never presented as WCAG
conformant. None is Candidate- or Stable-eligible today.

Accessibility cannot be waived by an ordinary exception, and CDS makes no legal or
certification statement.

- [Accessibility and Inclusive Design Policy](docs/governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [Accessibility Responsibility Model](docs/governance/ACCESSIBILITY_RESPONSIBILITY_MODEL.md)
- [Accessibility Requirements Baseline](docs/governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [WCAG 2.2 AA Applicability Matrix](docs/governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md)
- [Accessibility Evidence and Claims Model](docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Accessibility Channel Profiles](docs/governance/ACCESSIBILITY_CHANNEL_PROFILES.md)
- [Accessibility Limitations and Exception Policy](docs/governance/ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md)
- [CoreOps Pilot Accessibility Criterion](docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md)
- [Accessibility Architecture Alignment](docs/architecture/ACCESSIBILITY_ARCHITECTURE_ALIGNMENT.md)
- [Accessibility Support Baseline (A11Y-BL-001)](docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Environment and Scope Matrix](docs/governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
- [Accessibility Baseline Maintenance Policy](docs/governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md)
- [Accessibility Evidence Strategy](docs/governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md)
- [Accessibility Defect and Regression Model](docs/governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md)

## Machine-readable source and token format

The **normative machine-readable source format is decided** (CDS-WP-011), and
**nothing is implemented**. CDS adopts the **Design Tokens Community Group Technical
Reports 2025.10** (Format, Color, Resolver) — a **Final Community Group Report, not a
W3C Standard** — as the external basis, in **strict JSON (`.tokens.json`)**, under a
**CDS Token Format Profile**, with **JSON Schema 2020-12** as the future
profile-schema foundation. Source sets are layered (Reference → Semantic → Component →
Product Profile); channel outputs are generated and non-normative; references and
resolution **fail closed**; four validation layers separate syntax, DTCG, CDS profile,
and semantic/governance checks. **No token value, schema, resolver, or validator
exists.**

- [ADR-0001 — Machine-Readable Token Source Format](docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
- [Machine-Readable Source Model](docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md)
- [CDS Token Format Profile](docs/architecture/CDS_TOKEN_FORMAT_PROFILE.md)
- [Token Reference, Resolution and Validation Model](docs/architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
- [Token Metadata, Provenance and Identity Model](docs/architecture/TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md)
- [Token Format Evaluation](docs/research/TOKEN_FORMAT_EVALUATION.md) ·
  [Source Register](docs/research/TOKEN_FORMAT_SOURCE_REGISTER.md)
- [Implementation Plan](docs/roadmap/MACHINE_READABLE_SOURCE_IMPLEMENTATION_PLAN.md)

## Work packages

- **Completed:** CDS-WP-001 — Project Governance and NDF Bootstrap
- **Completed:** CDS-WP-001A — NDF Skills Bootstrap
- **Completed:** CDS-WP-002 — Concept and Scope Registration
- **Completed:** CDS-WP-003 — Benchmark and Differentiation Research
- **Completed:** CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract
- **Completed:** CDS-WP-005 — Design System Architecture
- **Completed:** CDS-WP-006 — Governance, Versioning, and Contribution Model
- **Completed:** CDS-WP-007 — Accessibility and Inclusive Design Policy
- **Completed:** CDS-WP-008 — Foundation Milestone Review
- **Completed:** CDS-WP-009 — Operating Enablement and Pre-Candidate Readiness
- **Completed:** CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy
- **Completed:** CDS-WP-011 — Machine-Readable Source and Token Format Decision
- **Next:** **CDS-WP-012 — Machine-Readable Source Bootstrap and Validation Contract**
  (authorized; not yet executed)

The full controlled roadmap is in
[project-system/WORK_PACKAGES.md](project-system/WORK_PACKAGES.md).

## Foundation Milestone Review

The Foundation / Pre-Design phase has been **reviewed** (CDS-WP-008). Across twelve
dimensions (55 criteria), three governance dry runs, four-axis Candidate readiness,
an eight-criterion CoreOps pilot entry matrix, and all 48 risks, the review found
**zero Foundation blockers** and recommends the milestone outcome **`GO WITH
NOTES`**.

The review was a **recommendation, not an approval**. The Human Maintainer
subsequently **accepted `GO WITH NOTES`** — by committing CDS-WP-008 and initiating
CDS-WP-009 — so the **Foundation is now Closed with Notes** (see the
[Foundation Closure Record](docs/governance/FOUNDATION_CLOSURE_RECORD.md)). Closure
promoted, designed, and published nothing: **no artifact is Candidate or Stable, no
claim is made, no licence or technology is selected, and the publication state
remains `Private Development`.** The mandatory notes — governance affordability, an
accessibility support baseline, risk actionability, licensing, role staffing, and
user-research honesty — are carried into the Pre-Candidate Operating Enablement
phase.

- [Foundation Milestone Review](docs/reviews/FOUNDATION_MILESTONE_REVIEW.md)
- [Foundation Closure Record](docs/governance/FOUNDATION_CLOSURE_RECORD.md)
- [Foundation Completeness Matrix](docs/reviews/FOUNDATION_COMPLETENESS_MATRIX.md)
- [Governance Affordability and Operating Readiness](docs/reviews/GOVERNANCE_AFFORDABILITY_AND_OPERATING_READINESS.md)
- [Foundation Candidate and Pilot Readiness](docs/reviews/FOUNDATION_CANDIDATE_AND_PILOT_READINESS.md)
- [Foundation Open Gaps and Dependencies](docs/reviews/FOUNDATION_OPEN_GAPS_AND_DEPENDENCIES.md)
- [Next-phase Recommendation](docs/reviews/NEXT_PHASE_RECOMMENDATION.md)
- [Foundation Reference Integrity Review](docs/reviews/FOUNDATION_REFERENCE_INTEGRITY_REVIEW.md)
- [Pre-Candidate Operating Plan](docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md)

## Registers

- Decisions: DEC-S-001 … DEC-S-082 (82) — 6 strategic foundation decisions,
  6 strategic scope decisions, 8 consumer and pilot scope decisions,
  12 logical architecture decisions, 16 governance, lifecycle and publication
  decisions, 12 accessibility and inclusive design decisions, 4 operating
  enablement and pre-candidate decisions, 8 accessibility support baseline and
  evidence decisions, 10 machine-readable source and token format decisions ·
  ADRs: 1 (ADR-0001)
- Risks: RISK-001 … RISK-063 (63) — 61 Monitored, RISK-040 and RISK-044 Mitigating;
  owner model finalized; no risk accepted or closed

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
