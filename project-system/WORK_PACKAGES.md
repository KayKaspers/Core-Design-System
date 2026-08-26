# Work Packages

Controlled work-package roadmap for the Core Design System (CDS).

- **Phase:** Post-Candidate Foundation & Design-System Enablement — **Foundation /
  Pre-Design: Closed with Notes**. Set by **DEC-S-127** (2026-08-26), effective at
  its Human-Maintainer integration commit; it supersedes `Pre-Candidate Operating
  Enablement` (**DEC-S-062**) **for current and future state only**. **A phase is an
  operating period, not a maturity state**, and it authorizes no work package.
- **Completed work packages:** CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005, CDS-WP-006, CDS-WP-007, CDS-WP-008, CDS-WP-009, CDS-WP-010,
  CDS-WP-011, CDS-WP-012, CDS-WP-013, CDS-WP-014, CDS-WP-015, **CDS-WP-016**,
  **CDS-WP-017**, **CDS-WP-018**, **CDS-WP-019**
- **CDS-WP-016 is `Completed`.** Its Candidate authority sequence completed
  (`AE1-CDS-WP016-SEMSTATUS-004` admitted at AE-1, Human-Maintainer Candidate
  approval granted, exact-byte **Promotion Commit
  `22fa0710e2b75df22e7b420c2f9d86bbe67b2777`** on 2026-08-19), and its
  post-promotion current-state reconciliation was closed by the Human-Maintainer
  commit **`1fc53ae5afa40807e1950171ab700b0860ee581e`**.
- **CDS-WP-017 is `Completed`.** Its reconciliation was integrated by the
  Human-Maintainer commit **`df9b8f21ff3bde4607b1c9ff7fdcbe3144366040`**, and
  closure became effective there.
- **CDS-WP-018 is `Completed`.** Its deferred-governance and repository-hygiene
  reconciliation was integrated by the Human-Maintainer commit
  **`e5d5d492619071655ba956713980d1ee261d9213`**, and closure became effective
  there.
- **CDS-WP-019 is `Completed`.** Core Visual Foundation Architecture. It defines
  the **architecture** of the CDS visual foundation — structure, layer position,
  naming, machine-readable boundary, accessibility, channels, brand and profile
  boundary, governance. It created **no** visual value, **no** token source file,
  **no** component, **no** brand, and **no** Product Profile; produced and admitted
  **no** evidence; changed **no** maturity; added **no** ADR, Decision, or risk;
  **renamed no phase**; registered **no** capability; made **no** claim; and
  activated **no** later work package. Its architecture was integrated by the
  Human-Maintainer commit **`538fbccbf6f554de3b872e9fb75a70d13318feb6`**, and
  closure became effective there.
- **Current work package:** **none.** The **CDS Phase Transition Governance
  Package** (**DEC-S-127**) runs between CDS-WP-019 closure and any CDS-WP-020
  authorization. It is **not** a numbered work package, occupies no identifier in
  the CDS-WP-020 … CDS-WP-053 sequence, changes **only** project-phase authority,
  and activates nothing.
- **Next planned work package:** **CDS-WP-020 — Reference and Semantic Token
  Foundation.** **`Planned`, not active, and not authorized**; it starts only on
  separate Human-Maintainer authorization.
- **Forward roadmap:** CDS-WP-017 … CDS-WP-053 are recorded in the
  [Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md).
  **CDS-WP-020 … CDS-WP-053 are `Planned` only.**

## Status values

| Status | Meaning |
| --- | --- |
| Completed | Work package finished and reported for review. |
| Next | Authorized as the immediate next work package. |
| Planned | Part of the roadmap; not yet authorized to start. |

`Next` records **roadmap authorization only**. It states which work package is the
current authorized one — never that its execution has or has not started. Execution,
review, and authority state are recorded per work package below.

## Roadmap

| ID | Title | Status | Depends on |
| --- | --- | --- | --- |
| CDS-WP-001 | Project Governance and NDF Bootstrap | Completed | — |
| CDS-WP-001A | NDF Skills Bootstrap | Completed | CDS-WP-001 |
| CDS-WP-002 | Concept and Scope Registration | Completed | CDS-WP-001A |
| CDS-WP-003 | Benchmark and Differentiation Research | Completed | CDS-WP-002 |
| CDS-WP-004 | Consumer Requirements and CoreOps Pilot Contract | Completed | CDS-WP-002 |
| CDS-WP-005 | Design System Architecture | Completed | CDS-WP-003, CDS-WP-004 |
| CDS-WP-006 | Governance, Versioning, and Contribution Model | Completed | CDS-WP-005 |
| CDS-WP-007 | Accessibility and Inclusive Design Policy | Completed | CDS-WP-005 |
| CDS-WP-008 | Foundation Milestone Review | Completed | CDS-WP-006, CDS-WP-007 |
| CDS-WP-009 | Operating Enablement and Pre-Candidate Readiness | Completed | CDS-WP-008 |
| CDS-WP-010 | Accessibility Support Baseline and Evidence Strategy | Completed | CDS-WP-009 |
| CDS-WP-011 | Machine-Readable Source and Token Format Decision | Completed | CDS-WP-010 |
| CDS-WP-012 | Machine-Readable Source Bootstrap and Validation Contract | Completed | CDS-WP-011 |
| CDS-WP-013 | Offline Token Profile Validator and Fixture Harness | Completed | CDS-WP-012 |
| CDS-WP-014 | Semantic Status Foundation Contract and First Candidate Plan | Completed | CDS-WP-013 |
| CDS-WP-015 | Semantic Status Foundation Source Set and Candidate Evidence | Completed | CDS-WP-014 |
| CDS-WP-016 | Semantic Status Foundation Independent Evidence Review and Candidate Gate | Completed | CDS-WP-015 |
| CDS-WP-017 | Post-WP-016 Roadmap, Authority and Scope Reconciliation | Completed | CDS-WP-016 |
| CDS-WP-018 | Deferred Governance and Repository Hygiene Reconciliation | Completed | CDS-WP-017 |
| CDS-WP-019 | Core Visual Foundation Architecture | Completed | CDS-WP-018 |
| CDS-WP-020 | Reference and Semantic Token Foundation | Planned | CDS-WP-019 |
| CDS-WP-021 | Adaptive Layout and Responsive Foundation | Planned | CDS-WP-020 |
| CDS-WP-022 | Theme and Environmental Presentation Model | Planned | CDS-WP-021 |
| CDS-WP-023 | Semantic Status Visual Binding Contract | Planned | CDS-WP-022 |
| CDS-WP-024 | Semantic Validation and Render-Gate Architecture | Planned | CDS-WP-023 |
| CDS-WP-025 | Semantic Validation Negative-Fixture Expansion | Planned | CDS-WP-024 |
| CDS-WP-026 | Universal Component Contract Model | Planned | CDS-WP-025 |
| CDS-WP-027 | StatusDisclosure Component Contract | Planned | CDS-WP-026 |
| CDS-WP-028 | Core Controls Component Set | Planned | CDS-WP-027 |
| CDS-WP-029 | Core Feedback and Disclosure Component Set | Planned | CDS-WP-028 |
| CDS-WP-030 | Component Accessibility Evidence Framework | Planned | CDS-WP-029 |
| CDS-WP-031 | Rendering Matrix and Visual Regression Evidence | Planned | CDS-WP-030 |
| CDS-WP-032 | Product Profile and Brand Extension Governance | Planned | CDS-WP-031 |
| CDS-WP-033 | Second Consumer Validation — Real Core Product | Planned | CDS-WP-032 |
| CDS-WP-034 | Multi-Channel and Localization Preservation | Planned | CDS-WP-033 |
| CDS-WP-035 | Motion System | Planned | CDS-WP-034 |
| CDS-WP-036 | Content Design, Voice and Tone | Planned | CDS-WP-035 |
| CDS-WP-037 | Iconography and Symbol System | Planned | CDS-WP-036 |
| CDS-WP-038 | Forms and Validation Pattern Family | Planned | CDS-WP-037 |
| CDS-WP-039 | Data Visualization Foundation | Planned | CDS-WP-038 |
| CDS-WP-040 | Sonic Design / Audio Foundation | Planned | CDS-WP-039 + scope registration |
| CDS-WP-041 | Multimodal Feedback Contract | Planned | CDS-WP-040 + scope registration |
| CDS-WP-042 | Haptic Feedback Extension Model | Planned | CDS-WP-041 + scope registration |
| CDS-WP-043 | Security and Safety Interaction Patterns | Planned | CDS-WP-042 |
| CDS-WP-044 | AI and Agent Interaction Design | Planned | CDS-WP-043 + scope registration |
| CDS-WP-045 | Advanced Brand Identity Model | Planned | CDS-WP-044 |
| CDS-WP-046 | Asset Governance and Provenance | Planned | CDS-WP-045 |
| CDS-WP-047 | Internationalization and Locale Architecture | Planned | CDS-WP-046 |
| CDS-WP-048 | Machine-Readable Distribution Contract | Planned | CDS-WP-047 |
| CDS-WP-049 | Design Tool Adapter Architecture | Planned | CDS-WP-048 |
| CDS-WP-050 | Runtime Adapter Reference Architecture | Planned | CDS-WP-049 |
| CDS-WP-051 | Cross-Consumer Conformance Evidence Model | Planned | CDS-WP-050 |
| CDS-WP-052 | Candidate-to-Stable Readiness Review | Planned | CDS-WP-051 |
| CDS-WP-053 | Stable Gate and Distribution Readiness | Planned | CDS-WP-052 |

### How to read this table

**`Planned` is not `Active` and not authorization.** CDS-WP-020 … CDS-WP-053 are
recorded so the direction is legible and so no competing roadmap can arise. Work on
them has **not started**, and each is executable only on an explicit Nova prompt
**and** Human-Maintainer authorization, one work package at a time. Listing
CDS-WP-020 immediately after CDS-WP-019 activates nothing.

**CDS-WP-019 proved the rule rather than breaking it:** it left `Planned` only when
the Human Maintainer authorized it separately — **not** because the roadmap listed
it next. **The phase transition does not change this.** DEC-S-127 relabels the
project phase and grants no authority: CDS-WP-020 stays `Planned`, not active, and
not authorized until the Human Maintainer authorizes it separately.

The `Depends on` column records **sequence intent**, not permission. Four entries
additionally require a **prior extension of the registered CDS scope** through an
Elevated change with Human-Maintainer approval, because their subject matter —
audio and sonic design, haptics, multimodal feedback, and AI/agent interaction — is
registered in **none** of the six capability domains today. Full arc, milestone,
gate, and disposition detail is in the
[Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md).

### CDS-WP-016 history

The Foundation is closed with notes and the Pre-Candidate Operating Enablement
phase is active. The Semantic Status Foundation was **Contract defined
(CDS-WP-014)** and **machine-readable implemented (CDS-WP-015: `semantic/status`,
25 non-visual tokens, 24/24 harness matches, executor-produced evidence)** —
**Experimental, no Candidate status, no visual value at that point**. That evidence
was then **independently reviewed by CDS-WP-016**: **Independent Review PASS**,
**Candidate Recommendation GO** — and **GO is not a Candidate award**. The **Nova
Candidate Maturity Review** returned **NO-GO** (Candidate Accessibility Gate unmet),
the gap assessment **confirmed** it, and the Human Maintainer **authorized the
Candidate Accessibility Gate Remediation** as **internal rework of CDS-WP-016**.
That remediation was **executed**, then **independently reviewed** together with its
clean-HEAD evidence package (**PASS WITH NOTES** and **PASS**), and the Human
Maintainer **admitted `AE1-CDS-WP016-SEMSTATUS-002` at AE-1** on 2026-08-17 for the
channel-independent Semantic Status source/contract family only, bound to
`semantic-status-rev-0001`.

A further internal rework — the **Candidate Finalization Governance Rework**
(2026-08-18, DEC-S-126) — defined the promotion sequence. That sequence then ran to
completion:

| # | Step | Authority | Result |
| --- | --- | --- | --- |
| 1 | Candidate Finalization Preparation — Proposed Candidate bytes enumerated | Executor | Complete |
| 2 | `AE1-CDS-WP016-SEMSTATUS-003` produced and independently reviewed | Executor / Reviewer | **PASS WITH NOTES** · **NOT ADMITTED** (`SUPERSEDED_FOR_ADMISSION_BY_EVIDENCE_INPUT_CHANGE`) |
| 3 | Candidate test lifecycle rework — bound test input made transition-safe | Executor | Complete |
| 4 | `AE1-CDS-WP016-SEMSTATUS-004` produced against the exact bytes | Executor | **Pass with limitations** |
| 5 | Fresh independent evidence review (reviewer ≠ executor) | Reviewer | **PASS WITH NOTES** |
| 6 | Human-Maintainer AE1-004 evidence admission | Human Maintainer | **APPROVED / ADMITTED** |
| 7 | Nova Candidate Finalization Review | Nova | **GO WITH NOTES** (recommendation only) |
| 8 | Human-Maintainer Candidate approval | Human Maintainer | **`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`** |
| 9 | **Exact-byte Promotion Commit** | Human Maintainer | **`22fa0710e2b75df22e7b420c2f9d86bbe67b2777`**, 2026-08-19 — gate **PASS**, committed blob identity **15/15 exact**, regression **47/47 · 64/64 · 184/184 · 24/24/0/0** |
| 10 | Post-Promotion Current-State Reconciliation | Executor / Human Maintainer | **Closed** — Human-Maintainer commit `1fc53ae5afa40807e1950171ab700b0860ee581e` |

**Current state:** Candidate **YES** for the Semantic Status Foundation /
`semantic/status` at `semantic-status-rev-0002-candidate`, maturity **`Candidate`**,
approval **`Approved`**, admitted evidence **`AE1-CDS-WP016-SEMSTATUS-004`** at
**AE-1** (source/contract scope only). **No artifact is Stable**, every other
artifact remains **AE-0**, claims **none**, conformance **none**, publication
**`Private Development`**.

**CDS-WP-016 is closed.** Closure became effective with the Human-Maintainer
commit `1fc53ae5afa40807e1950171ab700b0860ee581e`, which integrated the
post-promotion current-state reconciliation. The work package created no Stable
artifact, no claim, no conformance, no release, and no publication transition.

## Descriptions

### CDS-WP-001 — Project Governance and NDF Bootstrap

**Status:** Completed

Establishes the minimal governance and project-control foundation: project
identity, mission and boundaries, role and authority model, strategic
foundation decisions, initial risks, and the controlled work-package roadmap.
Governance and documentation work only; no visual design.

### CDS-WP-001A — NDF Skills Bootstrap

**Status:** Completed

Controlled adoption and verification of the approved NDF v1.0.0 Skills into
this repository, without modifying their normative upstream content. Adopted 38
verified docs-only Skills pinned to NDF v1.0.0 and activated the Skills-first
operating mode. See
[NDF Skills Provenance](../docs/governance/NDF_SKILLS_PROVENANCE.md) and
[NDF Skills Inventory](NDF_SKILLS_INVENTORY.md).

### CDS-WP-002 — Concept and Scope Registration

**Status:** Completed

Registered the CDS concept, six capability domains, cross-cutting concerns,
current and long-term scope, non-goals, user groups, three consumer classes,
ownership boundaries, and the CoreOps pilot boundary. Added DEC-S-007…DEC-S-012
and RISK-006…RISK-009, and established the Foundation Context Pack. See
[Concept and Scope](../docs/governance/CONCEPT_AND_SCOPE.md),
[Consumer and Stakeholder Model](../docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md),
and [Scope Boundary Matrix](../docs/governance/SCOPE_BOUNDARY_MATRIX.md).

### CDS-WP-003 — Benchmark and Differentiation Research

**Status:** Completed

Reviewed ten established design systems against 14 dimensions using official
sources only, and assessed eight CDS differentiation hypotheses
(HYP-001 … HYP-008). Added RISK-010 … RISK-013. Findings are research evidence
and remain **non-normative**; no decision was added or changed. See
[Design System Benchmark](../docs/research/DESIGN_SYSTEM_BENCHMARK.md),
[Evidence Matrix](../docs/research/BENCHMARK_EVIDENCE_MATRIX.md),
[Source Register](../docs/research/BENCHMARK_SOURCE_REGISTER.md),
[Differentiation Hypotheses](../docs/research/CDS_DIFFERENTIATION_HYPOTHESES.md),
and [Research Limitations](../docs/research/RESEARCH_LIMITATIONS.md).

### CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract

**Status:** Completed

Analyzed three consumer repositories at committed revisions, registered
CR-001 … CR-040 with traceability, defined the bounded CoreOps pilot
(Groups A–E, 9 scenarios) and its contract, and assessed HYP-001 … HYP-008
against consumer evidence. Added DEC-S-013 … DEC-S-020 and RISK-014 … RISK-019.
See [Consumer Requirements Model](../docs/governance/CONSUMER_REQUIREMENTS_MODEL.md),
[CoreOps Pilot Contract](../docs/governance/COREOPS_PILOT_CONTRACT.md), and
[Consumer Evidence Register](../docs/research/CONSUMER_EVIDENCE_REGISTER.md).

### CDS-WP-005 — Design System Architecture

**Status:** Completed

Defined the eight-layer logical architecture, the source-of-truth and authority
model with eight artifact classes, the five-level conceptual token flow, the
product profile and extension model with existing-product reconciliation, the
channel and distribution model, the five consumer contracts, and the evidence and
status-semantics architecture including the Unknown invariant. Mapped
CR-001 … CR-040 to the architecture. Added DEC-S-021 … DEC-S-032 and
RISK-020 … RISK-028. **No technology, format, or visual decision.** See
[Design System Architecture](../docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md).

### CDS-WP-006 — Governance, Versioning, and Contribution Model

**Status:** Completed

Established the governance operating model (six roles, two tracks), the source
conflict resolution policy, the seven-state artifact maturity lifecycle,
semantic versioning with eight compatibility axes, deprecation and removal,
contribution and acceptance, exception and Product Profile governance, four
graded adoption claim types, the **finalized risk owner model**, five publication
states with a gate, licensing per ten artifact classes, and release and change
control. Added DEC-S-033 … DEC-S-048 and RISK-029 … RISK-040. **No licence,
publication, technology, or design selected.** See
[Governance Operating Model](../docs/governance/GOVERNANCE_OPERATING_MODEL.md).

### CDS-WP-007 — Accessibility and Inclusive Design Policy

**Status:** Completed

Defined the binding accessibility and inclusive-design policy and its
verification approach — the target **WCAG 2.2 Level AA** for the applicable web
scope (resolving CR-024 at policy level), the target-versus-claim boundary,
inclusive-design scope, role boundaries, a complete Level A/AA applicability
matrix (56 listed / 55 applicable), five evidence levels (AE-0…AE-4), six channel
profiles, the limitations and exception policy, and the CoreOps pilot
accessibility criterion. Reconciled CR-021, CR-022, CR-024, and CR-034
traceability. Added DEC-S-049 … DEC-S-060 and RISK-041 … RISK-048. **No artifact
promoted; no claim, tag, or release created; every artifact remains AE-0;
publication state remains `Private Development`.** See
[Accessibility and Inclusive Design Policy](../docs/governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md).

### CDS-WP-008 — Foundation Milestone Review

**Status:** Completed

Reviewed the completed Foundation phase across twelve dimensions (55 criteria),
three governance dry runs, four-axis Candidate readiness, an eight-criterion
CoreOps pilot entry matrix, and all 48 risks. **Result: zero Foundation blockers.**
Recommended milestone outcome **GO WITH NOTES** — the Foundation can be closed with
mandatory next-phase notes (governance affordability, accessibility support
baseline, licensing, role staffing, user-research honesty). **No normative source
was changed; no Decision, Risk, ADR, or work-package ID was created; no artifact
was promoted; publication state remains `Private Development`.** The milestone
decision belongs to Nova and the Human Maintainer. See
[Foundation Milestone Review](../docs/reviews/FOUNDATION_MILESTONE_REVIEW.md).

### CDS-WP-009 — Operating Enablement and Pre-Candidate Readiness

**Status:** Completed

Recorded Foundation closure with mandatory notes; operationalized the committed
governance for daily use without creating any design, token, component, tool, or
product code. Created the [Foundation Closure Record](../docs/governance/FOUNDATION_CLOSURE_RECORD.md),
the [Foundation Operating Playbook](../docs/operations/FOUNDATION_OPERATING_PLAYBOOK.md),
the [Standard](../docs/operations/STANDARD_CHANGE_DOSSIER_TEMPLATE.md) and
[Elevated](../docs/operations/ELEVATED_CHANGE_DOSSIER_TEMPLATE.md) change-dossier
templates, the [Critical Risk Action Register](../docs/operations/CRITICAL_RISK_ACTION_REGISTER.md)
(12 Critical Risks made actionable), the
[Foundation Reference Integrity Review](../docs/reviews/FOUNDATION_REFERENCE_INTEGRITY_REVIEW.md)
(PASS), and the [Pre-Candidate Operating Plan](../docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md).
Added DEC-S-061 … DEC-S-064; moved RISK-040 `Monitored → Mitigating` (the only risk
status change, no acceptance or closure). **No artifact promoted; no claim, tag,
or release created; publication state remains `Private Development`.**

### CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy

**Status:** Completed

Defined the first accessibility support baseline (**A11Y-BL-001**, since committed)
and its supporting policies, using authorized official standards/vendor research —
three tiers (Required/Complementary/Scope-triggered), a 14-entry
[Environment and Scope Matrix](../docs/governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md),
an [Evidence Strategy](../docs/governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md)
operationalizing AE-0…AE-4, a
[Maintenance Policy](../docs/governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md)
(freshness + triggers + six-month max gap), a
[Defect and Regression Model](../docs/governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md),
a non-normative [Evidence Record Template](../docs/operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md),
and research evidence (source register + selection rationale). Added DEC-S-065…072
and RISK-049…054; moved RISK-044 `Monitored → Mitigating`. **No test was run, no tool
selected, every artifact remains AE-0, no environment is claimed as supported, the
CoreOps pilot stays inactive, and the publication state remains `Private
Development`.**

### CDS-WP-011 — Machine-Readable Source and Token Format Decision

**Status:** Completed

Decided the normative machine-readable source format using authorized official
research (13 DTCG/W3C/RFC/JSON-Schema URLs; stable vs preview separated). Selected
**DTCG 2025.10** (Format, Color, Resolver; a Final Community Group Report, **not** a
W3C Standard) as the external basis, in **strict JSON `.tokens.json`**, under a
**CDS Token Format Profile**, with **JSON Schema 2020-12** as the future
profile-schema foundation, an `io.github.kaykaspers.cds` `$extensions` namespace, a
four-layer source-set model, fail-closed reference/resolution rules (curly-brace
`{group.token}` for canonical token-to-token references and DTCG `$ref` / RFC 6901
JSON Pointer for document/property/resolver/source-set and controlled cross-file
references), a machine-validatable naming profile, versioned provenance identity, and
governed upgrades. Created
[ADR-0001](../docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md), four
normative architecture docs, an evaluation and source register, and an implementation
plan. Added DEC-S-073…082 and RISK-055…063. **No token value, schema, resolver,
validator, or design value created; no Candidate/Stable; pilot inactive; publication
state `Private Development`.**

### CDS-WP-012 — Machine-Readable Source Bootstrap and Validation Contract

**Status:** Completed

Implemented the value-neutral machine-readable bootstrap (pending commit): four CDS-owned
JSON Schema Draft 2020-12 contracts ([token document](../schemas/cds-token-document.schema.json),
[source-set manifest](../schemas/cds-source-set-manifest.schema.json),
[resolver](../schemas/cds-resolver-document.schema.json),
[validation case](../schemas/cds-validation-case.schema.json)); the
`io.github.kaykaspers.cds` extension payload contract; six synthetic positive fixtures and
nine synthetic negative fixtures under `tests/fixtures/machine-readable/`; a 15-case
[validation-case matrix](../tests/fixtures/machine-readable/VALIDATION_CASES.json); an
explicit [V1–V4 Validation Contract](../docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)
with a duplicate-key prohibition; and the
[deterministic-serialization decision](../docs/architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md)
(RFC 8785 + SHA-256, ADR-0002). Added DEC-S-083…092 and RISK-064…072; created ADR-0002.
**No real token/design value, productive validator, canonicalizer, transformer, or build;
formal schema execution `Not assessed`; Experimental, not Candidate; publication state
`Private Development`.**

### CDS-WP-013 — Offline Token Profile Validator and Fixture Harness

**Status:** Completed

Implemented and executed the offline validator (pending commit): the
`python -m tools.cds_validator` CLI on Python 3.11+ with exactly pinned `jsonschema`
4.26.0 and `rfc8785` 0.1.4 ([lock](../requirements-validator.lock), ADR-0003); a single
duplicate-key-rejecting JSON loader; a local five-schema registry including the new
[validation-result schema](../schemas/cds-validation-result.schema.json); the layered
V1–V4 engine with manifest/resolver graph validation; RFC 8785 + SHA-256 digests; and
71 passing unit tests. The fixture harness executed **15/15 validation cases with 15/15
expected/actual matches** and produced machine-readable, revision-bound evidence
([results](../artifacts/validation/wp013-fixture-results.json),
[digests](../artifacts/validation/wp013-fixture-digests.json),
[Execution Review](../docs/reviews/OFFLINE_TOKEN_VALIDATOR_EXECUTION_REVIEW.md)).
Added DEC-S-093…104 and RISK-073…081; moved RISK-066/067/068/069/071 to `Mitigating`;
created ADR-0003. **Executor-produced, independently unreviewed; no real design value,
no full-DTCG claim, no Candidate; publication state `Private Development`.**

### CDS-WP-014 — Semantic Status Foundation Contract and First Candidate Plan

**Status:** Completed

Defined the first concrete CDS design foundation (pending commit): the **Semantic
Status Foundation Contract** with **five independent axes** (`condition`, `severity`,
`confidence`, `freshness`, `evidence`), a **fixed 25-value vocabulary** with explicit
`unknown` on every axis, **ten invariants**, the complete 11-field status object with
**combination/conflict rules** (6 review-required combinations, 8 fail-closed states,
disclosure priority, no aggregate score), the **communication/accessibility/
localization contract** (text-first meaning, DE/EN semantic parity, no single-modality
encoding), the **value-neutral Semantic Status Token Contract**, the
**[First Semantic Status Candidate Plan](../docs/roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md)**
(8-element package, 10 gated prerequisites — none met), and an executor-produced
readiness review. Added DEC-S-105…114 and RISK-082…089. **No visual value, no token
source file, no component, no Candidate/Stable, no claim; WP-013 evidence stays
independently unreviewed; publication `Private Development`.**

### CDS-WP-015 — Semantic Status Foundation Source Set and Candidate Evidence

**Status:** Completed

Implemented the first real, still-Experimental machine-readable source set (pending
commit; resume run after a correctly BLOCKED first run): **[`semantic/status`](../tokens/semantic/status/semantic-status.tokens.json)**
(5 axis groups, **25 non-visual status tokens** `status.<axis>.<value>`, manifest,
resolver, revision `semantic-status-rev-0001`), the **Nova-authorized additive
validation-case-schema correction** (fixture-path families + 9 `semantic-status-*`
categories; `$id` unchanged; CLI untouched and fail closed), the **semantic-status V4
validator extension** (9 `CDS-V4-STATUS-*` diagnostics; fixture flags never disable
the objective checks), **1 positive + 8 negative status fixtures**, **VAL-CASE-016…024**
(24-case matrix; WP-013 baseline byte-identical, DEC-S-120), a **25/25 DE/EN
terminology mapping**, a **revision-clean WP-013 re-execution** (71/71 tests, 15/15
matches, worktree clean), **103/103 unit tests**, a **24/24 fixture harness**,
source-set validation (V1–V3 Pass, exit 0) with RFC 8785 + SHA-256 digests, four
executor-produced evidence reviews, and the **Draft Candidate Dossier** (gate
incomplete). Added DEC-S-115…124 and RISK-090…097. **Executor-produced, independently
unreviewed; no visual value, no Candidate, no claim; publication `Private
Development`.**

### CDS-WP-016 — Semantic Status Foundation Independent Evidence Review and Candidate Gate

**Status:** Completed *(closed by Human-Maintainer commit
`1fc53ae5afa40807e1950171ab700b0860ee581e`)*

Independently reviewed the WP-013 and WP-015 evidence (re-execution and artifact
assessment by a separately authorized reviewer — never the executor), reviewed
source/contract/terminology traceability, accessibility and content evidence, and the
Candidate dossier, and produced the Candidate-gate recommendation for the
Human-Maintainer decision — **no automatic Candidate promotion**. Result:
**Independent Review PASS**, **Candidate Recommendation GO** (0 Blocking, 0 High,
3 Observations) — see the
[Candidate Gate Recommendation](../docs/reviews/WP016_CANDIDATE_GATE_RECOMMENDATION.md).
**GO is not a Candidate award.**

**Candidate Accessibility Gate Remediation (internal rework of CDS-WP-016; not a
new work package).** The **Nova Candidate Maturity Review** returned **NO-GO** —
the normative Candidate Accessibility Gate was unmet — and a read-only gap
assessment **confirmed** it (**9/9** requirements not demonstrated). On
Human-Maintainer authorization the remediation was executed: **DEC-S-125**
(channel profiles gate channel artifacts, not channel-independent semantic
sources; no waiver, no Candidate award), Candidate-scope **WCAG applicability** and
**responsibility** mappings, a **25/25** per-value evidence requirements matrix
(GAP-H-02 closed as a mapping), an operational **text-first** source rule
(`CDS-V4-STATUS-DESCRIPTION`), a test-only statement evidence layer with **6/6**
review-required and **8/8** fail-closed coverage, **25/25** source descriptions and
**25/25** DE/EN structural coverage, an **AE-1** evidence record with
results and digests, a reasoned **AE-2 plan**, a **support-baseline plan** on
A11Y-BL-001 freshness **`Current`**, a **15-trigger regression plan**, **16**
recorded limitations (0 Critical), and a review addendum. The WP-013/WP-015
**24-case harness is unchanged** (24/24/0/0) and all **112** pre-existing validator
test IDs still pass.

**Candidate Finalization Governance Rework (internal rework of CDS-WP-016; not a
new work package).** A read-only Candidate Finalization Bootstrap Assessment on
2026-08-18 found a circular gate dependency: a Candidate revision must declare
`Candidate`/`Approved` metadata and a **new** source revision, but that new
revision invalidates the AE-1 admitted for `semantic-status-rev-0001`, so the
gate appeared enterable only through an unevidenced preparatory commit. On
Human-Maintainer authorization the rework was executed — **governance and tooling
only**:

- **DEC-S-126** — a named, **non-authoritative Proposed Candidate Revision**;
  target metadata that grants nothing; **evidence never transfers across a source
  revision**; exact-byte pre-commit evidence binding with byte-drift invalidation
  and no "small fix" exemption; **AE-1 admission before Candidate approval**; the
  **Promotion Commit** as the actual repository maturity transition point;
  mandatory post-commit verification.
- **RISK-098** (`Mitigating`) — Candidate-promotion evidence bootstrap
  circularity and pre-approval metadata misrepresentation.
- The **Candidate Approval Record Template** — a template only, with
  `NOT_DECIDED` / `NOT_APPROVED` / `AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION` as
  the only decision states. No instance existed at the time of the rework; **one
  instance now exists**, `CAR-CDS-WP016-SEMSTATUS-001`.
- **Evidence runner result format v2** — `sourceDeclaredMetadata` read from the
  evidenced bytes instead of hard-coded governance literals, a caller-declared
  `sourceAuthorityContext` enum, an **AE-1 Evidence Candidate** that is neither
  reviewed nor admitted by the run, seven permanently false authority-effect
  flags, and a fail-closed source-revision cross-check.

The rework created **no** Candidate source, produced **no** Candidate evidence,
admitted **no** evidence, granted **no** Candidate approval, and mutated **no**
productive Semantic Status source byte or existing evidence artifact. At that
milestone `semantic-status-rev-0002-candidate` was **reserved and not created**, and
the authoritative source revision was still `semantic-status-rev-0001`. No ADR was
added; the ADR range stays ADR-0001 … ADR-0003. Regression trigger **T-12 is not
waived**: the Candidate revision took a full fresh evidence, review, and admission
cycle — and did so.

**Promotion completed.** The three then-outstanding steps — a fresh independent
review, Nova's Candidate-gate review, and the Human Maintainer's maturity approval —
have all been performed, together with the exact-byte Promotion Commit. See the
CDS-WP-016 history table above, the
[Candidate Approval Record](../docs/operations/SEMANTIC_STATUS_CANDIDATE_APPROVAL_RECORD.md),
the [AE1-004 Admission Record](../docs/governance/SEMANTIC_STATUS_AE1_004_ADMISSION_RECORD.md),
and the
[Candidate Promotion Effectivity Record](../docs/governance/SEMANTIC_STATUS_CANDIDATE_PROMOTION_EFFECTIVITY_RECORD.md).

**Candidate is now YES** for that one family; **no artifact is Stable**, claims
remain **none**, conformance remains **none**, and **every other artifact remains
AE-0**. Further steps begin only on an explicit Nova prompt and Human-Maintainer
authorization.

### CDS-WP-017 — Post-WP-016 Roadmap, Authority and Scope Reconciliation

**Status:** Completed *(closed by Human-Maintainer commit
`df9b8f21ff3bde4607b1c9ff7fdcbe3144366040`)*

Reconciles the repository state actually reached after CDS-WP-016 with the accepted
forward planning basis, so that exactly **one** active future work-package sequence
exists. Governance, roadmap, context, and project-state documentation only.

- Records **CDS-WP-016 as `Completed`** against its closure commit, replacing the
  superseded two-stage closure statement that predated it.
- Registers **CDS-WP-017 as the active work package** and **CDS-WP-018 …
  CDS-WP-053 as `Planned`, not active, and not authorized** — a contiguous,
  gap-free, duplicate-free sequence with no competing active roadmap.
- Creates the
  [Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md):
  twelve development arcs, milestones **M1 … M12** as roadmap states that grant
  nothing, a per-work-package mapping to the normative eight-layer architecture,
  the standing gates (Product Profile · real consumer · generated-output authority ·
  semantic validation priority · multimodal and AI scope registration · Stable),
  and the eleven-way requirement classification model in which **Consumer-local**
  and **Reject** are valid outcomes.
- Records the **PB001 disposition** — PB001 is **not held in this repository**;
  it stays **Experimental Evidence, AE-0, non-normative**, with no conformance,
  Product Profile, or universal-core authority, and **no PB001 evidence is
  upgraded**. Its finding topics are routed by destination only.
- Routes the deferred findings **`R3R-003`, `NF-R3-OBS-001`, `NF-R4-OBS-001`,
  `NF-R4-OBS-002`, `NF-R5R-OBS-001`, `NF-R5R-OBS-003`** to **CDS-WP-018**, and
  keeps **`NF-R5R-OBS-002`** as **informational, a historical evidence limitation
  requiring no repair**. None is repaired here; routing is not repair.

**CDS-WP-017 creates no design, token, component, or visual value; produces and
admits no evidence; accepts and closes no risk; adds no ADR; promotes nothing to
Candidate or Stable; makes no claim; activates no Product Profile, pilot, consumer
integration, release, tag, or publication; and performs no Git write.**

### CDS-WP-018 — Deferred Governance and Repository Hygiene Reconciliation

**Status:** Completed *(integrated by the Human-Maintainer commit
`e5d5d492619071655ba956713980d1ee261d9213`)*

A bounded, documentary current-state, mirror, and repository-hygiene reconciliation
pass following the closure of CDS-WP-017. It takes up the findings CDS-WP-017 routed
to it, and nothing beyond that class.

- Reconciles **stale current-state and mirror text** against the normative sources:
  `pending Human-Maintainer commit` statements for artifacts the repository history
  shows as committed (**NF-R4-OBS-001**), the `PROJECT_BRAIN.md` risk-status mirror
  for RISK-066/067/068/069/071 (**NF-R3-OBS-001**), the post-Candidate precision of
  the validator-architecture maturity/approval wording (**NF-R5R-OBS-001**), and the
  research-baseline status wording (**R3R-003**).
- Corrects the **intentionally open decision areas** lists that still carried
  already-decided areas — token format, versioning and maturity model, conformance
  and adoption policy, product profile and override governance (**F-017-01**,
  **F-017-02**).
- Repairs **repository hygiene**: the UTF-8 BOM on `.gitattributes` and `.gitignore`
  and the missing Python ignore entries (**NF-R4-OBS-002**, **NF-R5R-OBS-003**).
- Adds **additive, dated current-state notes** to the two Candidate-era records that
  still carry `CDS-WP-017: INACTIVE` (**R1-F-01**) — neither dated table is
  rewritten.
- Corrects the self-referentially imprecise "none of these identifiers occurs in
  this repository" wording (**R2-N-01**) and completes the **F-017-04** disclosure
  with its stale next-work-package references (**R2-N-02**).

**Explicitly outside CDS-WP-018.** The phase label set by **DEC-S-062** is **not
renamed** and no Decision superseding it is created (**F-017-04**); no capability is
registered for audio/sonic, haptic, multimodal, AI/agent, or safety subject matter
(**F-017-03**, **R1-F-05**); and the five `AE1-CDS-WP016-SEMSTATUS-004`-bound
Foundation documents, the ADRs, the Decision Index, and every evidence artifact are
**not** edited.

**CDS-WP-018 creates no design, token, component, or visual value; produces and
admits no evidence; changes no maturity; accepts or closes no risk; adds no ADR or
Decision; makes no claim; activates no Product Profile, pilot, consumer integration,
release, tag, or publication; and performs no Git write.**

### CDS-WP-019 — Core Visual Foundation Architecture

**Status:** Next *(the current authorized work package)*

The first work package of **Phase V — Visual Foundation**. It defines **how** the
CDS visual foundation is structured, governed, represented, extended, validated, and
consumed — and it produces **no finished Core brand**.

- Establishes the [Visual Foundation Architecture](../docs/architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
  as the Layer-3 visual entry point: the position in the eight-layer model and the
  five-layer token flow, a register of **nine visual foundation families**
  (VF-1 … VF-9), **fourteen visual foundation invariants**, the naming model, the
  machine-readable representation boundary, and the motion boundary.
- Establishes six specialised architecture documents — **colour**, **typography**,
  **spatial and layout**, **shape and surface**, **iconography and imagery**, and
  **theme** — each stating structure, obligations, degradation, profile limits, and
  future validation requirements.
- Establishes four governance documents — the **accessibility mapping** (14 Layer-3
  WCAG criteria; **all five CDS-alone criteria are visual foundation criteria**),
  the **channel mapping** (nine families × nine channels), the **brand and Product
  Profile boundary** (the named extension-point set is **empty**), and the
  **governance and lifecycle** model.
- **Positions rather than registers** three subjects: opacity is an *attribute* of
  colour and surface, illustration and imagery are *Layer 2*, and focus indication
  is a *cross-family role set* — each the conservative reading, registering less
  scope rather than more.
- **Registers no new Decision.** Every binding statement is an application of a
  decision already in force; the derivation is recorded in the architecture
  document's *Authority basis* section.

**Explicitly outside CDS-WP-019.** No colour, palette, typeface, size, spacing,
radius, stroke, shadow, opacity, icon, illustration, motion value, breakpoint, or
theme instance is selected; no token source file, schema, validator rule, component,
channel adapter, or asset is created; no extension point is named; and the theme
**mechanism**, the responsive **model**, and the status-to-visual **binding** are
left explicitly open for CDS-WP-022, CDS-WP-021, and CDS-WP-023.

**CDS-WP-019 creates no visual value, brand, or Product Profile; produces and
admits no evidence; changes no maturity; accepts or closes no risk; adds no ADR,
Decision, or risk entry; makes no claim; renames no phase; registers no capability;
activates no pilot, consumer integration, release, tag, or publication; activates no
later work package; and performs no Git write.**

## Roadmap evolution

This roadmap is the controlled sequence. It may be extended or refined in a
controlled manner after later reviews. Extensions require Nova planning and Human
Maintainer approval; work packages are not added ad hoc during execution.

**CDS-WP-017 extended the sequence to CDS-WP-053 as a planning record only.** The
extension activated nothing: exactly one work package is authorized at a time, and
the roadmap grants no maturity, evidence, claim, or publication effect. The forward
arcs, milestones, and gates are held in the
[Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md),
which is a planning view and is **not normative**.

## Related documents

- [Next Phase](NEXT_PHASE.md)
- [Project Profile](PROJECT_PROFILE.md)
- [Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md)
- [Project Charter](../docs/governance/PROJECT_CHARTER.md)
- [Decision Index](../docs/decisions/DECISION_INDEX.md)
- [Risk Register](../docs/risks/RISK_REGISTER.md)
