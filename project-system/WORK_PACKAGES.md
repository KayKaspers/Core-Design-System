# Work Packages

Controlled work-package roadmap for the Core Design System (CDS).

- **Phase:** Pre-Candidate Operating Enablement — **Foundation / Pre-Design:
  Closed with Notes**
- **Completed work packages:** CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005, CDS-WP-006, CDS-WP-007, CDS-WP-008, CDS-WP-009, CDS-WP-010,
  CDS-WP-011, CDS-WP-012, CDS-WP-013, CDS-WP-014, CDS-WP-015
- **Next work package:** **CDS-WP-016 — Semantic Status Foundation Independent
  Evidence Review and Candidate Gate** (authorized as the next work package; not yet
  executed)

## Status values

| Status | Meaning |
| --- | --- |
| Completed | Work package finished and reported for review. |
| Next | Authorized as the immediate next work package. |
| Planned | Part of the roadmap; not yet authorized to start. |

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
| CDS-WP-016 | Semantic Status Foundation Independent Evidence Review and Candidate Gate | Next | CDS-WP-015 |

**CDS-WP-016 is authorized as the next Work Package.** The Foundation is closed with
notes; the Pre-Candidate Operating Enablement phase is active; the Semantic Status
Foundation is **Contract defined (CDS-WP-014) and machine-readable implemented
(CDS-WP-015: `semantic/status`, 25 non-visual tokens, 24/24 harness matches,
executor-produced evidence)** — **Experimental, independently unreviewed, no
Candidate status, no visual value**. CDS-WP-016 is registered as `Next` and is not
yet executed. No further work-package ID is created.

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

Defined the first accessibility support baseline (**A11Y-BL-001**, pending commit)
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

**Status:** Next

Will independently review the WP-013 and WP-015 evidence (re-execution or artifact
assessment by a separately authorized reviewer), review source/contract/terminology
traceability, accessibility and content evidence, and the Candidate dossier, and
prepare the Candidate-gate recommendation for the Human-Maintainer decision — **no
automatic Candidate promotion**. Not yet executed; begins only on an explicit Nova
prompt and Human-Maintainer authorization.

## Roadmap evolution

This roadmap is the initial controlled sequence. It may be extended or refined
in a controlled manner after later reviews. Extensions require Nova planning and
Human Maintainer approval; work packages are not added ad hoc during execution.

## Related documents

- [Next Phase](NEXT_PHASE.md)
- [Project Profile](PROJECT_PROFILE.md)
- [Project Charter](../docs/governance/PROJECT_CHARTER.md)
- [Decision Index](../docs/decisions/DECISION_INDEX.md)
- [Risk Register](../docs/risks/RISK_REGISTER.md)
