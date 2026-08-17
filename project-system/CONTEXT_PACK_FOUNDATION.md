# Foundation Context Pack

> **Normative source documents take precedence over this context summary.**
>
> This pack is a compact handover aid for continuation sessions. It summarizes;
> it never defines. Where it disagrees with a normative source, the normative
> source wins and this pack is wrong and must be corrected.

- **Maintained by:** CDS-WP-015
- **Date:** 2026-07-17

## Project identity

- Project: Core Design System (CDS)
- Repository: KayKaspers/Core-Design-System
- Local path: `D:\Projects\Core-Design-System`
- Framework: Nova Development Framework v1.0.0
- Type: versioned platform product and normative design foundation (DEC-S-001)

## Current phase

Pre-Candidate Operating Enablement — **Foundation / Pre-Design: Closed with
Notes** (CDS-WP-009; DEC-S-061, DEC-S-062).

Governance, scope, architecture, requirements, and accessibility policy are
established; the Foundation is closed with mandatory notes; the committed governance
is operationalized; the accessibility support baseline **A11Y-BL-001** is declared
and committed (CDS-WP-010, **no evidence executed — every artifact AE-0**); and the
**machine-readable source format is decided** (CDS-WP-011: DTCG 2025.10-based CDS
profile, strict JSON, ADR-0001); and the **machine-readable bootstrap is implemented**
(CDS-WP-012: 4 schemas, 15 fixtures, V1–V4 validation contract, RFC 8785/SHA-256, ADR-0002);
and the **offline validator and fixture harness are implemented and executed**
(CDS-WP-013: pinned Python/jsonschema/rfc8785 stack, ADR-0003, 71/71 unit tests,
**15/15 expected/actual case matches**, 14 digests — executor-produced); and the
**Semantic Status Foundation Contract is defined** (CDS-WP-014:
five independent axes, 25 values with explicit `unknown`, ten invariants,
combination/communication/token contracts, gated first Candidate plan); and the
**Semantic Status Source Set is implemented** (CDS-WP-015: `semantic/status`, 25
non-visual tokens with manifest/resolver, semantic-status V4 validation, 24/24
harness matches, 25/25 DE/EN terminology, Draft Candidate Dossier) —
**Experimental, committed, executor-produced, no Candidate status, no visual
value**. That WP-013 and WP-015 evidence has since been **independently reviewed by
CDS-WP-016**: **Independent Review PASS**, **Candidate Recommendation GO** — and
**GO is not a Candidate award**, so Semantic Status remains **Experimental**,
**Candidate No**, every artifact **AE-0**, with the **Nova and Human-Maintainer
Candidate authority gates still open**. Concrete visual design values remain
unauthorized (DEC-S-003). The current authorized work package is **CDS-WP-016 —
Semantic Status Foundation Independent Evidence Review and Candidate Gate**; its
review work is executed and its Candidate authority closure is open.

## Completed work packages

| WP | Title | Result |
| --- | --- | --- |
| CDS-WP-001 | Project Governance and NDF Bootstrap | Charter, authority model, DEC-S-001…006, RISK-001…005, initial roadmap. |
| CDS-WP-001A | NDF Skills Bootstrap | 38 verified docs-only NDF v1.0.0 Skills; provenance, manifest, inventory; Skills-first mode active. |
| CDS-WP-002 | Concept and Scope Registration | Concept and scope, consumer model, boundary matrix, DEC-S-007…012, RISK-006…009, this pack. |
| CDS-WP-003 | Benchmark and Differentiation Research | Ten systems reviewed against 14 dimensions from official sources; HYP-001…008 assessed; RISK-010…013. **Non-normative.** No decision changed. |
| CDS-WP-004 | Consumer Requirements and CoreOps Pilot Contract | 3 consumers analyzed at committed revisions; CR-001…040 registered and traced; CoreOps pilot Groups A–E with 9 scenarios; pilot contract; HYP consumer layer; DEC-S-013…020; RISK-014…019. |
| CDS-WP-005 | Design System Architecture | Eight-layer logical architecture; authority model; token flow; profiles and reconciliation; channels and distribution; consumer contracts; status semantics; CR mapped to architecture; DEC-S-021…032; RISK-020…028. **No technology or design selected.** |
| CDS-WP-006 | Governance, Versioning, Contribution, Risk and Publication Model | Six roles, two tracks; conflict resolution; 7 maturity states; versioning + 8 compatibility axes; deprecation; contribution; exceptions and profiles; 4 claim types; **risk ownership finalized**; 5 publication states; licensing per 10 classes; release control. DEC-S-033…048; RISK-029…040. **No licence, publication, technology, or design selected.** |
| CDS-WP-007 | Accessibility and Inclusive Design Policy | Target **WCAG 2.2 Level AA** for the applicable web scope (CR-024 resolved at policy level); target-is-not-claim rule; A/AA applicability matrix (56 listed / 55 applicable); shared responsibility (49/55 need both sides); 5 evidence levels AE-0…AE-4; 6 channel profiles; limitations and exception policy; CoreOps pilot criterion. DEC-S-049…060; RISK-041…048. **Nothing tested — every artifact AE-0; no claim; publication state unchanged.** |
| CDS-WP-008 | Foundation Milestone Review | Reviewed the Foundation across 12 dimensions (55 criteria), 3 governance dry runs, 4-axis Candidate readiness, 8-criterion pilot entry matrix, all 48 risks. **0 Foundation blockers**; recommended outcome **GO WITH NOTES**; 12 findings (FM-F-001…012). **No normative source changed; no Decision/Risk/ADR/WP-ID created; no artifact promoted; publication state unchanged.** Non-normative review evidence in `docs/reviews/`. |
| CDS-WP-009 | Operating Enablement and Pre-Candidate Readiness | Recorded **Foundation closure with notes** (accepted by the Human Maintainer); operationalized governance without any design/token/component/tool. Created the Closure Record (normative on closure/authority/phase), Operating Playbook, Standard + Elevated dossier templates, Critical Risk Action Register (12 risks actionable), Reference Integrity Review (PASS), and Pre-Candidate Operating Plan. DEC-S-061…064 added; RISK-040 `Monitored → Mitigating` (only status change; no acceptance/closure). **No artifact promoted; publication state `Private Development`.** |
| CDS-WP-010 | Accessibility Support Baseline and Evidence Strategy | Defined **A11Y-BL-001** (pending commit) via authorized official research — 3 tiers, 14-entry environment matrix (Required 6 · Conditional 4 · Deferred 4), evidence strategy (AE-0…AE-4), maintenance policy (freshness + triggers + 6-month max gap), defect/regression model, evidence record template, source register + selection rationale. DEC-S-065…072 added; RISK-049…054 added; RISK-044 `Monitored → Mitigating`. **A test contract, not evidence — no test run, every artifact AE-0, no environment claimed supported, pilot inactive, publication `Private Development`.** |
| CDS-WP-011 | Machine-Readable Source and Token Format Decision | Decided the normative machine-readable source format via authorized official research (13 URLs; stable vs preview separated): **DTCG 2025.10** (Format/Color/Resolver; a **Final CG Report, not a W3C Standard**) as external basis, **strict JSON `.tokens.json`**, **JSON Schema 2020-12** profile-schema foundation, an `io.github.kaykaspers.cds` `$extensions` namespace, four source-set layers, fail-closed references (curly-brace token-to-token vs `$ref`/JSON-Pointer for document/resolver/cross-file), machine-validatable naming, versioned provenance, and 4 validation layers. Created **ADR-0001** + 4 architecture docs + evaluation/register + implementation plan. DEC-S-073…082 added; RISK-055…063 added. **No token/schema/validator/design value; no Candidate/Stable; pilot inactive; publication `Private Development`.** |
| CDS-WP-012 | Machine-Readable Source Bootstrap and Validation Contract | Implemented the value-neutral bootstrap (pending commit): **4 CDS-owned JSON Schema 2020-12 contracts** (token document, source-set manifest, resolver, validation case; stable `tag:` `$id`s, local `$ref`, offline), the `io.github.kaykaspers.cds` payload contract, **6 positive + 9 negative synthetic fixtures**, a **15-case validation-case matrix** (expected V1–V4 per fixture), an explicit **V1–V4 Validation Contract** (duplicate-key fails V1; no aggregate score), and the **RFC 8785 (JCS) + SHA-256** serialization decision (**ADR-0002**). DEC-S-083…092 added; RISK-064…072 added. **No real token/design value, productive validator, or canonicalizer; formal schema execution `Not assessed`; Experimental, not Candidate; publication `Private Development`. CDS-WP-013 registered Next.** |
| CDS-WP-013 | Offline Token Profile Validator and Fixture Harness | Implemented and executed the offline validator (pending commit): `python -m tools.cds_validator` (Python 3.12.10; pinned `jsonschema==4.26.0` + `rfc8785==0.1.4`, ADR-0003), a single duplicate-key-rejecting loader, a local five-schema registry (incl. the new **validation-result schema**), the layered V1–V4 engine, manifest/resolver graph validation, and RFC 8785 + SHA-256 digests. **71/71 unit tests; 15/15 cases with 15/15 expected/actual matches; 14 fixtures digested** (duplicate-key: none). Evidence in `artifacts/validation/` + Execution Review — **executor-produced, `independentReviewState: pending`**. DEC-S-093…104 added; RISK-073…081 added; RISK-066/067/068/069/071 → `Mitigating`. **Bounded DTCG V2 (no full-DTCG statement); no design value; no Candidate; publication `Private Development`. CDS-WP-014 registered Next.** |
| CDS-WP-014 | Semantic Status Foundation Contract and First Candidate Plan | Defined the first concrete design foundation (pending commit): the **Semantic Status Foundation Contract** — 5 independent axes (`condition`/`severity`/`confidence`/`freshness`/`evidence`), a fixed **25-value vocabulary** with explicit `unknown` everywhere, **10 invariants**, the 11-field status object, **6 review-required combinations + 8 fail-closed states**, disclosure priority without any aggregate score, the text-first **communication/accessibility/localization contract** (DE/EN semantic parity), the value-neutral **Semantic Status Token Contract**, and the **First Semantic Status Candidate Plan** (8-element package, 10 unmet prerequisites) + executor-produced readiness review. DEC-S-105…114 added; RISK-082…089 added. **No visual value, no token file, no component, no Candidate/Stable, no claim; WP-013 evidence stays independently unreviewed; publication `Private Development`. CDS-WP-015 registered Next.** |
| CDS-WP-015 | Semantic Status Foundation Source Set and Candidate Evidence | Implemented the first real, still-Experimental source set (pending commit; resume run after a correctly BLOCKED first run): **`semantic/status`** (5 axes, **25 non-visual tokens** `status.<axis>.<value>`, manifest + resolver), the **Nova-authorized additive validation-case-schema correction** (semantic-status fixture paths + 9 categories; `$id` unchanged; CLI untouched/fail closed), the **semantic-status V4 extension** (9 `CDS-V4-STATUS-*` codes; fixture flags never disable the objective checks), 1+8 status fixtures, **VAL-CASE-016…024** (24-case matrix; WP-013 baseline byte-identical), **25/25 DE/EN terminology**, revision-clean WP-013 re-execution (**15/15, worktree clean**), **103/103 unit tests**, **24/24 harness matches**, source-set validation (V1–V3 Pass, exit 0) + RFC 8785/SHA-256 digests, 4 executor-produced reviews, **Draft Candidate Dossier** (gate incomplete). DEC-S-115…124 added; RISK-090…097 added. **Executor-produced, independently unreviewed; no visual value; Not Candidate; publication `Private Development`. CDS-WP-016 registered Next.** |

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
| **Governance** | [docs/governance/GOVERNANCE_OPERATING_MODEL.md](../docs/governance/GOVERNANCE_OPERATING_MODEL.md) |
| Source conflicts | [docs/governance/SOURCE_CONFLICT_RESOLUTION_POLICY.md](../docs/governance/SOURCE_CONFLICT_RESOLUTION_POLICY.md) |
| Maturity states and gates | [docs/governance/ARTIFACT_MATURITY_LIFECYCLE.md](../docs/governance/ARTIFACT_MATURITY_LIFECYCLE.md) |
| Versioning and compatibility | [docs/governance/VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md](../docs/governance/VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md) |
| Contribution and acceptance | [docs/governance/CONTRIBUTION_AND_ACCEPTANCE_MODEL.md](../docs/governance/CONTRIBUTION_AND_ACCEPTANCE_MODEL.md) |
| Exceptions and Product Profiles | [docs/governance/EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md](../docs/governance/EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md) |
| Adoption and conformance claims | [docs/governance/ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md](../docs/governance/ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md) |
| Risk ownership and control | [docs/governance/RISK_GOVERNANCE_MODEL.md](../docs/governance/RISK_GOVERNANCE_MODEL.md) |
| Licensing and publication | [docs/governance/LICENSING_AND_PUBLICATION_DECISION_MODEL.md](../docs/governance/LICENSING_AND_PUBLICATION_DECISION_MODEL.md) |
| Release and change control | [docs/governance/RELEASE_AND_CHANGE_CONTROL_POLICY.md](../docs/governance/RELEASE_AND_CHANGE_CONTROL_POLICY.md) |
| **Foundation closure (closure/authority/phase)** | [docs/governance/FOUNDATION_CLOSURE_RECORD.md](../docs/governance/FOUNDATION_CLOSURE_RECORD.md) |
| **Accessibility support baseline (A11Y-BL-001)** | [docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md](../docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md) |
| Accessibility environment/scope matrix | [docs/governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md](../docs/governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md) |
| Accessibility baseline maintenance | [docs/governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md](../docs/governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md) |
| Accessibility evidence strategy | [docs/governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md](../docs/governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md) |
| Accessibility defect/regression model | [docs/governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md](../docs/governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md) |
| **Machine-readable source model** | [docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md](../docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md) |
| CDS token format profile | [docs/architecture/CDS_TOKEN_FORMAT_PROFILE.md](../docs/architecture/CDS_TOKEN_FORMAT_PROFILE.md) |
| Token reference/resolution/validation | [docs/architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md](../docs/architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md) |
| Token metadata/provenance/identity | [docs/architecture/TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md](../docs/architecture/TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md) |
| Machine-readable validation contract (V1–V4) | [docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md](../docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md) |
| Deterministic serialization / digest | [docs/architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md](../docs/architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md) |
| Format decision (ADR-0001) | [docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md](../docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) |
| Serialization decision (ADR-0002) | [docs/decisions/ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md](../docs/decisions/ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md) |
| Validator stack decision (ADR-0003) | [docs/decisions/ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md](../docs/decisions/ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md) |
| Offline validator architecture | [docs/architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md](../docs/architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md) |
| Validator usage (non-normative) | [docs/operations/OFFLINE_TOKEN_VALIDATOR_USAGE.md](../docs/operations/OFFLINE_TOKEN_VALIDATOR_USAGE.md) |
| CDS schemas (structural; five, incl. validation result) | [schemas/](../schemas/) |
| Synthetic validation fixtures + case matrix | [tests/fixtures/machine-readable/](../tests/fixtures/machine-readable/) |
| Validator execution evidence (executor-produced) | [artifacts/validation/](../artifacts/validation/) · [Execution Review](../docs/reviews/OFFLINE_TOKEN_VALIDATOR_EXECUTION_REVIEW.md) |
| **Semantic Status Foundation (contract family)** | [docs/foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md](../docs/foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) |
| Status axis vocabulary (5 x 5 = 25) | [docs/foundations/STATUS_AXIS_VOCABULARY.md](../docs/foundations/STATUS_AXIS_VOCABULARY.md) |
| Status composition/conflict rules | [docs/foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md](../docs/foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) |
| Status communication/accessibility contract | [docs/foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md](../docs/foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md) |
| Semantic status token contract (no values) | [docs/foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md](../docs/foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md) |
| First Candidate plan (no promotion) | [docs/roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md](../docs/roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md) |
| **Semantic Status Source Set (`semantic/status`, Experimental)** | [tokens/semantic/status/](../tokens/semantic/status/) |
| Status terminology DE/EN (25/25) | [docs/foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md](../docs/foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md) |
| Candidate dossier (Draft, gate incomplete) | [docs/operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md](../docs/operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md) |
| WP-015 evidence (executor-produced) | [artifacts/validation/](../artifacts/validation/) · [Source-Set Review](../docs/reviews/SEMANTIC_STATUS_SOURCE_SET_EXECUTION_REVIEW.md) · [Re-Execution Review](../docs/reviews/WP013_VALIDATOR_EVIDENCE_REEXECUTION_REVIEW.md) |
| **Logical architecture** | [docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md](../docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md) |
| Artifact classes and authority | [docs/architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md](../docs/architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md) |
| Token flow and theming | [docs/architecture/TOKEN_AND_THEME_ARCHITECTURE.md](../docs/architecture/TOKEN_AND_THEME_ARCHITECTURE.md) |
| Profiles, extensions, reconciliation | [docs/architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md](../docs/architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) |
| Channels and distribution | [docs/architecture/ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md](../docs/architecture/ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) |
| Consumer contracts | [docs/architecture/CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md](../docs/architecture/CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md) |
| Evidence flow and status semantics | [docs/architecture/EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md](../docs/architecture/EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) |
| Architecture requirement coverage | [docs/architecture/ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md](../docs/architecture/ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md) |
| Consumer requirements and classification | [docs/governance/CONSUMER_REQUIREMENTS_MODEL.md](../docs/governance/CONSUMER_REQUIREMENTS_MODEL.md) |
| Requirement provenance | [docs/governance/CONSUMER_REQUIREMENTS_TRACEABILITY.md](../docs/governance/CONSUMER_REQUIREMENTS_TRACEABILITY.md) |
| CoreOps pilot scope | [docs/governance/COREOPS_PILOT_SCOPE_AND_SCENARIOS.md](../docs/governance/COREOPS_PILOT_SCOPE_AND_SCENARIOS.md) |
| CoreOps pilot contract | [docs/governance/COREOPS_PILOT_CONTRACT.md](../docs/governance/COREOPS_PILOT_CONTRACT.md) |
| How pilot evidence is judged | [docs/governance/CONSUMER_VALIDATION_PLAN.md](../docs/governance/CONSUMER_VALIDATION_PLAN.md) |

**Research documents are evidence, not normative sources.** They inform later
work packages; they decide nothing:
[Benchmark](../docs/research/DESIGN_SYSTEM_BENCHMARK.md) ·
[Evidence Matrix](../docs/research/BENCHMARK_EVIDENCE_MATRIX.md) ·
[Source Register](../docs/research/BENCHMARK_SOURCE_REGISTER.md) ·
[Hypotheses](../docs/research/CDS_DIFFERENTIATION_HYPOTHESES.md) ·
[Limitations](../docs/research/RESEARCH_LIMITATIONS.md) ·
[Consumer Evidence Register](../docs/research/CONSUMER_EVIDENCE_REGISTER.md) ·
[Consumer Hypothesis Validation](../docs/research/CONSUMER_HYPOTHESIS_VALIDATION.md)

**Operating views (non-normative — CDS-WP-009).** These make governance runnable
and reference the normative policies; they do not replace them (DEC-S-063):
[Operating Playbook](../docs/operations/FOUNDATION_OPERATING_PLAYBOOK.md) ·
[Standard Dossier](../docs/operations/STANDARD_CHANGE_DOSSIER_TEMPLATE.md) ·
[Elevated Dossier](../docs/operations/ELEVATED_CHANGE_DOSSIER_TEMPLATE.md) ·
[Critical Risk Action Register](../docs/operations/CRITICAL_RISK_ACTION_REGISTER.md) ·
[Reference Integrity Review](../docs/reviews/FOUNDATION_REFERENCE_INTEGRITY_REVIEW.md) ·
[Pre-Candidate Operating Plan](../docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md).

## Active decisions

- Range: DEC-S-001 … DEC-S-124 · Count: 124 · All Accepted · ADRs: 3 (ADR-0001,
  ADR-0002, ADR-0003)
- DEC-S-001…006: strategic foundation decisions (CDS-WP-001)
- DEC-S-007…012: strategic scope decisions (CDS-WP-002)
- DEC-S-013…020: consumer and pilot scope decisions (CDS-WP-004)
- DEC-S-021…032: logical architecture decisions (CDS-WP-005) — unchanged by
  CDS-WP-006
- DEC-S-033…048: governance, lifecycle and publication decisions (CDS-WP-006)
- DEC-S-049…060: accessibility and inclusive design decisions (CDS-WP-007) —
  DEC-S-001…048 unchanged
- DEC-S-061…064: operating enablement and pre-candidate decisions (CDS-WP-009) —
  DEC-S-001…060 unchanged
- DEC-S-065…072: accessibility support baseline and evidence decisions (CDS-WP-010)
  — DEC-S-001…064 unchanged
- DEC-S-073…082: machine-readable source and token format decisions (CDS-WP-011) —
  DEC-S-001…072 unchanged
- DEC-S-083…092: machine-readable bootstrap and validation decisions (CDS-WP-012) —
  DEC-S-001…082 unchanged
- DEC-S-093…104: offline validator implementation decisions (CDS-WP-013) —
  DEC-S-001…092 unchanged
- DEC-S-105…114: semantic status foundation decisions (CDS-WP-014) —
  DEC-S-001…104 unchanged
- DEC-S-115…124: semantic status source and evidence decisions (CDS-WP-015) —
  DEC-S-001…114 unchanged
- ADR-0001 (Machine-Readable Token Source Format), ADR-0002 (Deterministic JSON
  Serialization), and ADR-0003 (Offline Token Validator Implementation Stack)
  exist — 3 ADRs.

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
| DEC-S-013 | Consumer evidence must be bound to a committed revision. |
| DEC-S-014 | Consumer requirements are classified; classification is not approval. |
| DEC-S-015 | The initial CoreOps pilot is a bounded slice, not adoption or conformance. |
| DEC-S-016 | Generalization requires explicit review and acceptance; CoreOps origin is insufficient. |
| DEC-S-017 | Pilot outcomes are evaluated through version-bound evidence. |
| DEC-S-018 | Secondary consumers provide evidence, not pilot authority. |
| DEC-S-019 | Consumer need does not establish differentiation. |
| DEC-S-020 | CDS-WP-004 authorizes requirements and a contract only. |
| DEC-S-021 | Eight-layer logical architecture; selects no topology or technology. |
| DEC-S-022 | Authority divided by artifact class; only normative sources bind. |
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
| DEC-S-034 | Neither normative source wins automatically; a conflict invalidates the state. |
| DEC-S-035 | Seven maturity states, separate from version and publication. |
| DEC-S-036 | Candidate and Stable need evidence and approval; Candidate is mandatory. |
| DEC-S-037 | MAJOR.MINOR.PATCH; honest pre-1.0 policy. |
| DEC-S-038 | Releases need an immutable identity; `latest` is not one. |
| DEC-S-039 | Compatibility declared per axis; no blanket claim. |
| DEC-S-040 | Stable requires deprecation before removal; removal is MAJOR. |
| DEC-S-041 | Controlled contribution process; use never equals acceptance. |
| DEC-S-042 | Exceptions are explicit, bounded, expiring. |
| DEC-S-043 | Product Profiles are separately governed; never retrospective legitimation. |
| DEC-S-044 | Claims are scope-, version-, evidence-bound; `CDS certified` prohibited. |
| DEC-S-045 | Risk ownership finalized: Human Maintainer accountable, Nova controller. |
| DEC-S-046 | Five publication states with an explicit gate. |
| DEC-S-047 | Licensing decided per artifact class; no inheritance. |
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
| DEC-S-058 | Each channel needs its own profile; non-web is never WCAG-conformant. |
| DEC-S-059 | Accessibility cannot be waived by an ordinary exception. |
| DEC-S-060 | CR-024 resolved at policy level for the CoreOps pilot web scope. |
| DEC-S-061 | Foundation milestone closed with mandatory notes; closure grants no Candidate/Stable/adoption/conformance/release/publication. |
| DEC-S-062 | First post-Foundation phase is Pre-Candidate Operating Enablement; it precedes the first design Candidate. |
| DEC-S-063 | Operating playbooks and dossiers are non-normative; they may reduce ceremony but never obligation. |
| DEC-S-064 | Critical risks affecting Elevated work need an executor role, review trigger, expected evidence, and blocking effect first. |
| DEC-S-065 | The Accessibility Support Baseline defines what future evidence targets; it is not evidence, support, or a claim. |
| DEC-S-066 | Three accessibility baseline tiers (Required / Complementary / Scope-triggered). |
| DEC-S-067 | The Required Core Baseline: keyboard, Windows 11, Chromium + Firefox, a no-cost screenreader, ≥2 pairings, zoom/reflow, text spacing, forced-colors, reduced motion, accessible status, DE/EN. |
| DEC-S-068 | Product-family baseline vs exact evidence identity are separate; `current`/`latest` is not an identity. |
| DEC-S-069 | Complementary/mobile coverage is scope-triggered; undeclared environments are not supported. |
| DEC-S-070 | Baseline freshness reviewed on gate/version/lifecycle/regression/scope triggers and ≥ every six months. |
| DEC-S-071 | Evidence recorded through immutable, bound, reviewer-identified records; templates/automation/single passes are not global evidence. |
| DEC-S-072 | Accessibility defects/regressions classified separately from risk; Blocking/High regressions block Stable and claims. |
| DEC-S-073 | DTCG 2025.10 (Format/Color/Resolver) is the external normative format basis; a CG report, not a W3C Standard. |
| DEC-S-074 | Only pinned DTCG 2025.10 is authoritative; previews/drafts are inputs until a governed migration accepts them. |
| DEC-S-075 | Strict JSON (RFC 8259) `.tokens.json` is the normative source form; YAML/JSONC/JSON5/tool/CSS/generated are not. |
| DEC-S-076 | The CDS profile constrains DTCG and adds metadata only via namespaced `$extensions`; reserved DTCG semantics unchanged. |
| DEC-S-077 | JSON Schema 2020-12 is the profile-schema foundation; a schema pass is not full/semantic/a11y/governance correctness. |
| DEC-S-078 | Token references follow DTCG rules; cycles, dangling refs, type conflicts, missing sets, bad layers, unresolved overrides fail closed. |
| DEC-S-079 | Source sets are layered (Reference/Semantic/Component/Product Profile); channel outputs are generated, not normative. |
| DEC-S-080 | Sources/outputs carry versioned identity (profile+DTCG version, immutable revision, deps, transformation, maturity, approval, provenance); no `latest`. |
| DEC-S-081 | A restrictive, machine-validatable naming profile; technical IDs separate from display labels. |
| DEC-S-082 | Format/profile/binding/reference/extension/validation upgrades are governed; no automatic upgrade. |
| DEC-S-083 | Bootstrap = CDS-owned JSON Schemas + synthetic fixtures; presence is not conformance. |
| DEC-S-084 | CDS metadata under `io.github.kaykaspers.cds`, requires `profileVersion`; foreign extensions preserved, not normative. |
| DEC-S-085 | Source-Set manifests explicitly declare identity/layer/path/graph; no implicit or network-discovered sets. |
| DEC-S-086 | Resolver documents: strict JSON, `$ref`/JSON Pointer, explicit local ordered composition; no network resolution. |
| DEC-S-087 | Validation fixtures are synthetic, test-only, non-normative; never real tokens/profiles. |
| DEC-S-088 | Duplicate JSON member names prohibited; fail V1; no first/last-key-wins repair. |
| DEC-S-089 | Validation cases bind every fixture to expected V1–V4; layers stay visible; no aggregate score. |
| DEC-S-090 | RFC 8785 (JCS) + SHA-256 for canonical content digests; supplements, not replaces, revision/approval/provenance. |
| DEC-S-091 | Cross-file references valid only via the declared local graph; undeclared/network/missing/cyclic fail closed. |
| DEC-S-092 | Bootstrap stays Experimental until a validator executes, results are reviewed, and the Human Maintainer approves. |
| DEC-S-093 | Validator stack: Python 3.11+, stdlib-first, pinned jsonschema + rfc8785; no runtime network. |
| DEC-S-094 | Entry point `python -m tools.cds_validator`; version/validate-file/validate-cases/digest + exit-code contract. |
| DEC-S-095 | Every validation path uses the duplicate-key-rejecting loader; bypassing parse paths prohibited. |
| DEC-S-096 | Schema resolution via a committed local registry only; unknown/network resolution fails closed. |
| DEC-S-097 | V1–V4 states stay separate and visible; no aggregate score. |
| DEC-S-098 | DTCG coverage explicitly bounded; unsupported areas are limitations, never passes. |
| DEC-S-099 | Manifest/resolver validation enforces the declared graph; implicit discovery prohibited. |
| DEC-S-100 | Digests only from parsed content; never authenticity, approval, or revision replacement. |
| DEC-S-101 | Results use the CDS-owned result schema binding runtime/dependency/case/digest/review identities. |
| DEC-S-102 | Harness success = actual matches committed expected; a recognized negative is an observation, not approval. |
| DEC-S-103 | WP-013 reports are Experimental executor-produced evidence; independently unreviewed until separately reviewed. |
| DEC-S-104 | No Candidate before full harness pass, complete provenance, independent review, Nova review, and Human-Maintainer approval. |
| DEC-S-105 | Five independent status axes; no axis substitutes for another. |
| DEC-S-106 | Fixed five-value vocabulary per axis; unknown explicit, never an omitted default. |
| DEC-S-107 | Degraded knowledge (unknown/stale/expired/unverified/partial/unavailable) is never represented as success. |
| DEC-S-108 | No normative aggregate health score; summaries preserve material qualifiers. |
| DEC-S-109 | Combinations stay independent under explicit conflict/rationale/provenance rules; contradictions fail closed. |
| DEC-S-110 | Language-neutral technical IDs; localized labels preserve normative meaning. |
| DEC-S-111 | Status meaning is textual/accessible; never color/icon/position/shape/motion alone. |
| DEC-S-112 | Channels, components, profiles, and extensions preserve axis distinction and truthfulness. |
| DEC-S-113 | First planned Candidate: the Semantic Status Foundation (contract + future source set); visuals excluded. |
| DEC-S-114 | No Candidate until source set, validation/accessibility/content evidence, independent review, Nova review, and Human-Maintainer approval are complete. |
| DEC-S-115 | The Semantic Status Source Set is `semantic/status` and stays Experimental; implementation grants no status. |
| DEC-S-116 | One non-visual token per authorized axis value: 5 axis groups, 25 status tokens. |
| DEC-S-117 | Token paths `status.<axis>.<value>`; values = stable technical IDs; 1:1 vocabulary traceability. |
| DEC-S-118 | Status validation fails closed on missing axis/value/unknown, path-value disagreement, case collision, aggregate or appearance roles. |
| DEC-S-119 | DE/EN terminology is separate from technical IDs and must preserve normative meaning. |
| DEC-S-120 | WP-013 cases are immutable baseline expectations; WP-015 adds VAL-CASE-016…024 append-only. |
| DEC-S-121 | WP-015 execution and review evidence is executor-produced and independently unreviewed until separately assessed. |
| DEC-S-122 | The Candidate Dossier stays Draft while review/approval gates are open; a full-looking dossier grants nothing. |
| DEC-S-123 | Source set, manifest, resolver, and outputs stay identity- and digest-aligned; disagreement fails closed. |
| DEC-S-124 | No downstream artifact may present the Experimental status source as an approved Candidate before the gate succeeds. |

## Active risks

- Range: RISK-001 … RISK-097 · Count: 97 · **90 Monitored; RISK-040, RISK-044,
  RISK-066, RISK-067, RISK-068, RISK-069, RISK-071 Mitigating**
- **Owner model finalized** (DEC-S-045): Accountable Risk Owner — Human
  Maintainer · Risk Controller — Nova · Mitigation Executor — named per
  mitigation · Evidence Reviewer — Nova or authorized reviewer (never the executor).
- Only the Human Maintainer may set a risk `Accepted` or `Closed`.
- RISK-041…048 (accessibility) added by CDS-WP-007. **CDS-WP-009 moved RISK-040
  `Monitored → Mitigating`** via the
  [Critical Risk Action Register](../docs/operations/CRITICAL_RISK_ACTION_REGISTER.md)
  (12 Critical Risks made actionable; DEC-S-064). **CDS-WP-010 added RISK-049…054**
  and moved **RISK-044 `Monitored → Mitigating`** (A11Y-BL-001 defined).
  **CDS-WP-011 added RISK-055…063** (token-format/spec-drift/reference/provenance risks).
  **CDS-WP-012 added RISK-064…072** (all Monitored; schema/fixture/duplicate-key/
  canonicalization/validation-coverage risks). **CDS-WP-013 added RISK-073…081**
  (validator supply-chain/coverage/reproducibility/evidence risks, all Monitored) and
  moved **RISK-066/067/068/069/071 `Monitored → Mitigating`** on executed,
  executor-produced harness evidence (independently unreviewed). **CDS-WP-014 added
  RISK-082…089** (semantic-status truthfulness risks, all Monitored). **CDS-WP-015
  added RISK-090…097** (status source/evidence risks, all Monitored; no existing
  status changed). No risk accepted or closed.

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
| RISK-010 | Benchmark imitation. |
| RISK-011 | Research and source bias. |
| RISK-012 | Source volatility. |
| RISK-013 | Differentiation overstatement. |
| RISK-014 | Consumer evidence staleness. |
| RISK-015 | Pilot scope inflation. |
| RISK-016 | Product-specific requirement contamination. |
| RISK-017 | Document evidence mistaken for user validation. |
| RISK-018 | Pilot contract mistaken for adoption or conformance. |
| RISK-019 | Secondary consumer underrepresentation. |
| RISK-020 | Normative-source authority ambiguity. |
| RISK-021 | Token and override proliferation. |
| RISK-022 | Existing-product reconciliation failure. |
| RISK-023 | Domain-pattern leakage into the universal foundation. |
| RISK-024 | Channel divergence. |
| RISK-025 | Generated-artifact provenance loss. |
| RISK-026 | Architecture overdesign. |
| RISK-027 | Product-profile fragmentation. |
| RISK-028 | Deferred accessibility policy creates architecture debt. |
| RISK-029 | Governance bottleneck and maintainer overload. |
| RISK-030 | Governance role ambiguity. |
| RISK-031 | Maturity inflation. |
| RISK-032 | Compatibility ambiguity. |
| RISK-033 | Deprecation without viable migration. |
| RISK-034 | Contribution gate bypass. |
| RISK-035 | Exception debt. |
| RISK-036 | Product-profile governance bypass. |
| RISK-037 | Misleading adoption or conformance claims. |
| RISK-038 | Licensing and rights fragmentation. |
| RISK-039 | Premature publication. |
| RISK-040 | Ceremonial risk governance. |
| RISK-041 | Accessibility target mistaken for conformance. |
| RISK-042 | Automated-testing substitution. |
| RISK-043 | Component-to-product responsibility gap. |
| RISK-044 | Accessibility support baseline drift. |
| RISK-045 | Accessibility regression. |
| RISK-046 | Non-web channel accessibility gap. |
| RISK-047 | Inclusive-design undercoverage. |
| RISK-048 | Accessibility evidence burden. |
| RISK-049 | Accessibility baseline representativeness gap. |
| RISK-050 | Baseline interpreted as universal support. |
| RISK-051 | Environment availability mismatch. |
| RISK-052 | Evidence identity incompleteness. |
| RISK-053 | Regression coverage gap. |
| RISK-054 | Accessibility defect normalization. |
| RISK-055 | Token specification version drift. |
| RISK-056 | Preview specification contamination. |
| RISK-057 | CDS profile divergence. |
| RISK-058 | Schema-validation false assurance. |
| RISK-059 | Reference-resolution failure. |
| RISK-060 | Cross-layer dependency violation. |
| RISK-061 | Token identifier collision. |
| RISK-062 | Token provenance incompleteness. |
| RISK-063 | Transformation-tool lock-in. |
| RISK-064 | CDS schema contract incompleteness. |
| RISK-065 | Synthetic fixtures mistaken for design tokens. |
| RISK-066 | Schema and validator divergence. |
| RISK-067 | Canonicalization and digest mismatch. |
| RISK-068 | Duplicate-key ambiguity. |
| RISK-069 | Manifest and resolver graph inconsistency. |
| RISK-070 | Validation fixture coverage gap. |
| RISK-071 | Validation expectation drift. |
| RISK-072 | Digest mistaken for authenticity. |
| RISK-073 | Validator dependency supply-chain exposure. |
| RISK-074 | Partial DTCG coverage overstated. |
| RISK-075 | Runtime reproducibility gap. |
| RISK-076 | Duplicate-key loader bypass. |
| RISK-077 | Diagnostic contract instability. |
| RISK-078 | Fixture expectation self-confirmation. |
| RISK-079 | Offline-boundary regression. |
| RISK-080 | Validation-result provenance gap. |
| RISK-081 | Validator evidence mistaken for Candidate approval. |
| RISK-082 | Status-axis conflation. |
| RISK-083 | Unknown-state optimism. |
| RISK-084 | Aggregate-status masking. |
| RISK-085 | Status-combination ambiguity. |
| RISK-086 | Status-localization drift. |
| RISK-087 | Visual-only status encoding. |
| RISK-088 | Consumer status remapping divergence. |
| RISK-089 | First-candidate scope expansion. |
| RISK-090 | Status source and contract drift. |
| RISK-091 | Semantic status tokens mistaken for visual tokens. |
| RISK-092 | Status token path migration instability. |
| RISK-093 | Semantic validator blind spot. |
| RISK-094 | Semantic fixture overfitting. |
| RISK-095 | Status localization parity false assurance. |
| RISK-096 | Candidate dossier completeness illusion. |
| RISK-097 | Experimental status source consumed prematurely. |

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
conformance claims. Governance defined by CDS-WP-006; accessibility governance by
CDS-WP-007.

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

## Benchmark research (CDS-WP-003)

**Non-normative.** Evidence and hypotheses only — no decisions, no principles,
no design brief, no technology recommendation. Snapshot dated 2026-07-15.

Ten systems reviewed against 14 dimensions using official publisher sources
only: Carbon · Fluent 2 · Material 3 · Primer · Atlassian · Spectrum (with
Spectrum 2) · SAP Fiori · SLDS 2 · GOV.UK · USWDS. 33 official URLs opened
(31 benchmark + 2 standards), 27 with usable evidence. Evidence matrix: 140
cells, 105 with usable evidence.

Most decision-relevant findings:

- Tool coupling in token workflows is common and rarely documented as a risk —
  supports DEC-S-004 and RISK-004 with evidence.
- No reviewed system documented PDF, presentation, or diagram standards; they
  are product-interface systems.
- No reviewed system stated an offline or self-hosted guarantee.
- Every system permits product variation; none published its limits.
- Strongest practices found: published per-component maturity states, published
  conformance evidence, and explicitly stating what the system does not do.

Hypotheses HYP-001 … HYP-008, all **Research hypothesis**: none reached
"Strongly supported"; HYP-006 assessed as common industry practice; HYP-003 not
verifiable. All rest on absence from public documentation, which is weaker
evidence than presence.

## Consumer requirements and the CoreOps pilot (CDS-WP-004)

**Evidence sources**, all bound to committed revisions (DEC-S-013):

| Consumer | Role | HEAD commit | Tree |
| --- | --- | --- | --- |
| CoreOps | Primary pilot | `399de21c2d76cf84279badfcde58dacbb9eec1a2` | Dirty — read from HEAD only |
| SpeakCore | Secondary | `a5e697715c1c7077bc6c53400b3e6411730720ba` | Clean |
| CastCore | Secondary | `6c7614e3192a11479ae1c7431195daa042d38250` | Dirty — read from HEAD only |

15 sources read (14 usable). **Documentation only — Level 1 evidence.** No user
research took place (RISK-017).

**Requirements:** CR-001 … CR-040 (40). Shared CDS Candidate 25 · CoreOps Pilot
Requirement 2 · Product-local 2 · Deferred 9 · Out of CDS Scope 2. Priority:
Must 16 · Should 11 · Could 1 · Not in pilot 12. **Classification is not
approval** (DEC-S-014).

**Strongest signal:** status semantics. All three consumers document graded
status; two independently require that *unknown must never read as healthy*
(CR-006, CR-007). Consumers also already hold **product-local design decisions
and token sets** (CR-002, CR-037) — CDS arrives after them.

**CoreOps pilot groups** (bounded slice, DEC-S-015) — 9 scenarios:

| Group | Focus |
| --- | --- |
| A | Application Foundation — shell, navigation, orientation, modes |
| B | Operations Overview — prioritized status, honest unknown |
| C | Inventory and Dense Data — list/table, filter, sort, empty state |
| D | State and Safety Patterns — full state set, dangerous action, confirmation |
| E | Help, Accessibility, Localization — setup check, help, keyboard, DE/EN |

**Pilot contract:** committed and normative (CDS-WP-004). **Not active; entry
criteria unmet** — CDS-WP-005 architecture and a maturity model are missing; the
accessibility target (CR-024) is decided (WCAG 2.2 Level AA, CDS-WP-007), but
**no accessibility evidence exists**. Neither existence nor completion implies
adoption or conformance (RISK-018).

**Hypothesis consumer layer:** HYP-002, HYP-003, HYP-005 are *Confirmed consumer
need*; HYP-007 needs *Human validation*; the rest are partially supported.
Research assessments from CDS-WP-003 are **unchanged**. A confirmed need is not a
differentiation claim (DEC-S-019).

## Logical architecture (CDS-WP-005)

**Normative.** Selects no technology and no design (DEC-S-032).

**Eight layers** (DEC-S-021): 1 Strategy and Governance · 2 Brand and Identity ·
3 Foundations and Tokens · 4 Components · 5 Patterns and Experiences ·
6 Channels and Communication · 7 Distribution and Enablement · 8 Evidence and
Quality. Dependencies flow **downward only**; upward dependencies are defects.

**Source of truth** (DEC-S-022, DEC-S-023): eight artifact classes. Only
*Normative Human-readable* (meaning) and *Normative Machine-readable* (values)
bind, and only through change control. Generated artifacts, design-tool state,
reference implementations, evidence, consumer-local artifacts, and research are
**not normative**. Conflicts **fail closed**; recency never confers authority.

**Token flow** (DEC-S-024), five levels, strictly downward: Reference → Semantic
→ Component → Product Profile Overrides → Channel/Platform Outputs.
Semantic-first; no format, naming, or tool selected.

**Profiles and reconciliation** (DEC-S-025, DEC-S-026): Core Foundation · Product
Profile · Consumer Extension · Domain Pattern Family · Local Exception. Profiles
touch approved extension points only and may never redefine shared semantics,
weaken accessibility, distort status truth, or break contracts. Existing consumer
designs are **reconciled, not overwritten** — inventory → semantic mapping →
conflict identification → classification → retention or migration. Consumer-local
retention is a valid outcome.

**Operations patterns** are a **Domain Pattern Family** above the universal
foundation, not part of it (DEC-S-027) — the need is confirmed, generalizability
is not.

**Channels and distribution** (DEC-S-029, DEC-S-030, DEC-S-031): channels share
semantics and may differ in rendering. Distribution requires **no mandatory
external runtime**, supports offline and air-gap, is reproducible, and pins to an
identifiable revision. Every artifact carries provenance.

**Status invariants** (DEC-S-028): five separated axes — operational condition,
severity, knowledge confidence, freshness, evidence availability. **Unknown is
not Healthy. Stale is not Current. Unverified is not Verified.** Colour is never
the sole meaning carrier.

**Requirement coverage:** CR-001…040 all mapped — **9 addressed by architecture,
27 partially addressed, 0 deferred to CDS-WP-006, 0 deferred to CDS-WP-007, 2
consumer-owned, 2 out of scope** (reconciled by CDS-WP-007; no requirement is
deferred to a policy work package any longer — CR-024 is addressed because the
target/policy exist, not because anything was tested).

## Governance (CDS-WP-006)

**Normative.** Selects no licence, publication state, technology, or design.

**Roles (6):** Human Maintainer (final approval, exclusive Git/release/
publication/licensing authority, sole risk acceptor) · Nova (governance and risk
controller, review — **recommends, never decides**) · Claude (scoped executor —
no approval, no Git) · Consumer Maintainer (own project only) · Contributor (no
acceptance authority) · Evidence Reviewer (never the artifact itself, never the
executor). **Activity grants no authority** (DEC-S-033).

**Tracks (2):** Standard (corrections, bounded non-breaking additions) ·
Elevated (breaking, Stable, accessibility, profiles, exceptions, claims,
licensing, publication, removal, security/legal). **Ceremony scales; obligations
do not.** A change touching an Elevated trigger is Elevated.

**Source conflict** (DEC-S-034): neither normative source wins automatically. A
conflict **invalidates the affected state** and blocks release and distribution
from `Suspected` onward. Prohibited: recency wins · design tool wins · generated
wins · implementation wins · consumer usage wins · silent overwrite · automatic
resolution.

**Maturity (7):** Proposed → Exploratory → Experimental → **Candidate** →
Stable → Deprecated → Removed. Candidate is mandatory before Stable. Maturity,
release version, and publication state are **three separate axes**. **No existing
artifact is Candidate or Stable.**

**Versioning:** MAJOR.MINOR.PATCH. Pre-1.0 = no blanket compatibility promise,
but breaking changes, migrations, revisions, and deprecations stay documented.
**`latest` is not an identity.** Compatibility declared across **8 axes**; an
unassessed axis is never "compatible".

**Contribution:** 10-step flow, 5 outcomes. **`Keep Consumer-local` is a
first-class success.** No auto-merge, no self-approval, no urgency bypass.
**External contribution is not yet possible.**

**Exceptions:** 13 mandatory fields, 6 statuses, expiry required. `Expired` = an
**uncovered deviation**. Recurring exceptions trigger a **CDS gap review**.
**Accessibility weakening is not approvable through a normal exception.**

**Product Profiles:** 12 required elements. **Not retrospective legitimation** of
an existing consumer design (RISK-036). A profile exceeding its bounds is a fork.

**Claims (4):** Uses CDS Artifacts → CDS-integrated → CDS-validated →
CDS-conformant, each scope- and version-bound with 8 mandatory fields.
**`CDS certified` prohibited.** **No claim is currently valid, by anyone.**

**Risk ownership finalized:** Human Maintainer accountable · Nova controller ·
executor named per mitigation · reviewer never the executor. **Documentation is
not mitigation** (RISK-040).

**Publication (5 states):** Private Development · Controlled Preview · Public
Preview · Public Stable · Archived. **Current: `Private Development`.**
15-point gate. **Repository visibility is not a publication state.**

**Licensing:** decided per **10 artifact classes**; no inheritance; **no licence
selected**. Unknown rights **block publication**.

**Release:** 12 requirements, **6 change classes**. No automatic publication from
`main`; no tag without a Human Maintainer action; **Claude never releases**. A
green build is not consent.

### Currently blocked

**No artifact can reach Stable · no Product Profile can be approved · no
publication-state change is possible · no CDS release is possible.** The
accessibility target now exists (CR-024 resolved, DEC-S-049), so the blocker
moved from *"against what?"* to *"show it"*: the remaining obstacles are the
**absent accessibility evidence** (every artifact is AE-0; the support baseline
A11Y-BL-001 is committed but is not evidence — RISK-041, RISK-044) and the
**absent licensing decisions** (DEC-S-047,
RISK-038). No gate opened.

## Foundation Milestone Review (CDS-WP-008)

- **Completed:** CDS-WP-008 — Foundation Milestone Review (reviewed revision
  `7b71652`). **No next work package authorized.**
- **Recommended milestone outcome: `GO WITH NOTES`** — Claude recommendation,
  pending Nova review and Human-Maintainer approval.
- **Foundation blockers: 0.** Completeness matrix: 55 criteria — 44 Met · 4
  Met-with-notes · 3 Partially met · 4 Not met.
- **Candidate readiness:** governance Met; artifact/evidence Not met (not a
  blocker); consumer-validation Partially met.
- **CoreOps pilot entry:** Partially met — pilot inactive (8 criteria: 3 Met, 1
  partial, 3 not met, 1 not-yet-assessable).
- **Governance affordability:** Partially met — Standard track operational,
  Elevated path High burden for current staffing (RISK-029, RISK-040, RISK-048).
- **Critical risks (12):** RISK-029, 040, 048, 044, 017, 028, 020, 021, 023, 026,
  031, 038.
- **No new phase authorized; no work-package ID created; no artifact promoted; no
  claim; publication state `Private Development`.**

Review docs: [Milestone Review](../docs/reviews/FOUNDATION_MILESTONE_REVIEW.md) ·
[Completeness Matrix](../docs/reviews/FOUNDATION_COMPLETENESS_MATRIX.md) ·
[Affordability](../docs/reviews/GOVERNANCE_AFFORDABILITY_AND_OPERATING_READINESS.md) ·
[Candidate & Pilot](../docs/reviews/FOUNDATION_CANDIDATE_AND_PILOT_READINESS.md) ·
[Open Gaps](../docs/reviews/FOUNDATION_OPEN_GAPS_AND_DEPENDENCIES.md) ·
[Next-phase](../docs/reviews/NEXT_PHASE_RECOMMENDATION.md)

Foundation closure and the next phase were subsequently **decided**: the Human
Maintainer accepted `GO WITH NOTES` (commit of CDS-WP-008 + initiation of
CDS-WP-009). **Foundation: Closed with Notes.** Operating enablement is in place
(CDS-WP-009), the accessibility support baseline A11Y-BL-001 is declared and
committed (CDS-WP-010, no evidence executed), the machine-readable source format is
decided (CDS-WP-011, ADR-0001), the machine-readable bootstrap is implemented
(CDS-WP-012, Experimental, ADR-0002), and the offline validator and fixture harness
are implemented and executed (CDS-WP-013, Experimental, ADR-0003, 15/15
expected/actual matches, executor-produced), and the
Semantic Status Foundation Contract is defined (CDS-WP-014) and its machine-readable
source set is implemented (CDS-WP-015, `semantic/status`, Experimental, committed,
executor-produced 24/24 evidence, Not Candidate). That WP-013 and WP-015 evidence
has since been **independently reviewed by CDS-WP-016** — **Independent Review
PASS**, **Candidate Recommendation GO** — and **GO is not a Candidate award**:
Candidate remains **No**, maturity **Experimental**, approval **Unapproved**, every
artifact **AE-0**. The current authorized work package is **CDS-WP-016 — Semantic
Status Foundation Independent Evidence Review and Candidate Gate**; its review work
is executed, while the Candidate authority closure stays open — **Nova Candidate
gate open**, **Human-Maintainer Candidate gate open**. No follow-up work package is
authorized and CDS-WP-017 is not activated. See the
[Foundation Closure Record](../docs/governance/FOUNDATION_CLOSURE_RECORD.md).
