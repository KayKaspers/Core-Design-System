# Project Profile

## Identification

- Project: Core Design System
- Abbreviation: CDS
- Repository: KayKaspers/Core-Design-System
- Local path: `D:\Projects\Core-Design-System`
- Primary pilot consumer: CoreOps
- Framework: Nova Development Framework v1.0.0

## Project type

CDS is a versioned platform product providing shared design, brand,
experience, interface, token, component, and multi-channel foundations.

CDS is not a logo-only project, a branding kit, or an isolated UI component
library (see DEC-S-001).

## Current lifecycle status

Post-Candidate Foundation & Design-System Enablement — **Foundation / Pre-Design:
Closed with Notes**

Set by **DEC-S-127** (2026-08-26), effective at its Human-Maintainer integration
commit. It supersedes `Pre-Candidate Operating Enablement` (**DEC-S-062**) **for
current and future state only**; DEC-S-062 stays `Accepted` and correct for the
period it governed. **A phase is an operating period, not a maturity state** — the
transition grants no maturity, evidence, capability, Product Profile, pilot,
release, or publication authority, and activates no work package.

## Work package status

- **Current work package: none.** **CDS-WP-020 — Reference and Semantic Token
  Foundation** was authorized separately by the Human Maintainer on 2026-08-26,
  **executed with result `DECISION_REQUIRED`**, and its reviewed object was
  **integrated** by the Human-Maintainer commit
  `42a568d823de3388e45af62967546f13ad67eff6`. It is recorded as **`Completed`**;
  **closure was recorded in the CDS-WP-020 closure and routing object and became
  effective at that object's Human-Maintainer integration commit
  `3f37ecfe54dad82f8064aaff521ff9e3aec65fd7`.** **No successor work package is active or authorized.** **Contract
  only.** It defines what a
  visual **reference primitive** and a visual **semantic role** are, what each must
  declare, how a role aliases a primitive, and the discipline any future value must
  satisfy — across the
  [Visual Reference Token Foundation](../docs/architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md),
  the [Visual Semantic Token Foundation](../docs/architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md),
  and the [Visual Token Value Selection Rules](../docs/governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md).
  Its **value and machine-readable** half is **gated** on seven normative choices no
  committed CDS source has made, recorded as **OD-1 … OD-7** in the **non-normative**
  [Visual Token Foundation Open Decisions](../docs/roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
  register. It created **no** visual value, **no** identifier, **no** token source
  file, schema, validator rule, test, component, brand, or Product Profile; produced
  and admitted **no** evidence; changed **no** maturity; added **no** risk entry;
  **renamed no phase**; **registered no capability**; and **activated no later work
  package**. A separately authorized **Decision Integration Pass** (2026-08-27) has
  since registered **DEC-S-128 … DEC-S-131 and ADR-0004**, answering **OD-1, OD-2
  and OD-3**; **they are effective** at commit `42a568d8…`, they select **no** value
  and create **no** identifier. **OD-4 and OD-7 have since been answered, OD-5
  partially answered, OD-6A policy-answered and OD-6B answered by existing
  authority** by the CDS Step-9 Decision Integration Pass (2026-09-05) — **registered
  as DEC-S-132 … DEC-S-135 and ADR-0005, and effective at commit `2cb244e8…`**. **The value half
  stays gated**: VP-3, VP-5, VP-6 and VP-7 remain unsatisfied.
  **`DECISION_REQUIRED` stands as the executed result of the work package**: closing
  it answers **no** open decision, satisfies **no** value prerequisite, and selects
  **no** value. A new risk entry is still **not** recommended, and **`RISK-099` is
  not required**. **The CDS
  Phase Transition Governance Package** (**DEC-S-127**) ran between CDS-WP-019
  closure and this authorization; it occupied no identifier in the
  CDS-WP-020 … CDS-WP-053 sequence and activated nothing.
- **`FR-N-03`: RESOLVED BY EXPLICIT AUTHORING-WP DESTINATION.** Nova adjudicated it
  with Human-Maintainer approval — **Option 2**: **source and value authoring is not
  validation**, and the concrete machine-readable Visual Token Source and Value
  Authoring work must not be absorbed into **CDS-WP-024**. Its destination is
  **`CDS-WP-020A` — Visual Token Source Authoring and Source Set Realization**, an
  **inserted** identifier on the `CDS-WP-001A` precedent that renumbered nothing.
  **`CDS-WP-020A` is `Planned`, not active, and not authorized**, and **CDS-WP-024
  keeps its validation and conformance boundary unchanged**. **AUTHOR is not
  VALIDATE.** See [Work Packages](WORK_PACKAGES.md).
- **Preceding work package: CDS-WP-019 — Core Visual Foundation Architecture**
  (**Completed**; closure became effective with the Human-Maintainer commit
  `538fbccbf6f554de3b872e9fb75a70d13318feb6`). **Architecture
  only.** It defines how the CDS visual foundation is structured, governed,
  represented, extended, validated, and consumed: a Layer-3 entry-point
  architecture, a register of **nine visual foundation families** (VF-1 … VF-9),
  **fourteen invariants**, a naming model, the machine-readable representation
  boundary, a motion boundary, plus specialised colour, typography, spatial, shape
  and surface, iconography and imagery, and theme architectures, and four
  governance documents (accessibility mapping, channel mapping, brand and Product
  Profile boundary, governance and lifecycle). It created **no** visual value,
  token source file, schema, validator rule, component, brand, or Product Profile;
  produced and admitted **no** evidence; changed **no** maturity; added **no** ADR,
  Decision, or risk entry; **renamed no phase**; **registered no capability**; and
  **activated no later work package**.
- **Earlier work package: CDS-WP-018 — Deferred Governance and Repository Hygiene
  Reconciliation.** **Completed**; closure became effective with the
  Human-Maintainer commit `e5d5d492619071655ba956713980d1ee261d9213`. Documentary
  current-state, mirror, and repository-hygiene reconciliation only.
- **Earlier work package: CDS-WP-017 — Post-WP-016 Roadmap, Authority and Scope
  Reconciliation.** **Completed**; closure became effective with the
  Human-Maintainer commit `df9b8f21ff3bde4607b1c9ff7fdcbe3144366040`. It recorded
  CDS-WP-016 as closed, registered CDS-WP-018 … CDS-WP-053 as `Planned` and **not
  active**, and produced the single active
  [Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md).
- **Next planned work package: CDS-WP-021 — Adaptive Layout and Responsive
  Foundation** — **`Planned`, not active, not authorized, work not started.**
  **The effective `DEC-S-135` rules that CDS-WP-022 precedes context-sensitive value
  selection and makes it the recommended and sequenced Step-10 candidate**;
  **SEQUENCED NEXT ≠ AUTHORIZED**, and it authorizes nothing.
- Earlier work package: **CDS-WP-016 — Semantic Status Foundation
  Independent Evidence Review and Candidate Gate.** Its review work was
  **executed**: Independent Review **PASS**, Candidate Recommendation **GO**.
  **GO is not a Candidate award.**
  The **Nova Candidate Maturity Review** then returned **NO-GO** (Candidate
  Accessibility Gate unmet), the gap assessment **confirmed** it (9/9), and the
  Human-Maintainer-authorized **Candidate Accessibility Gate Remediation**
  (internal rework of CDS-WP-016, **not** a new work package) is **executed**.
  The remediation and its clean-HEAD evidence package are **independently reviewed**
  and **admitted**: admitted accessibility evidence **AE-1**
  (`AE1-CDS-WP016-SEMSTATUS-002`, 2026-08-17) for the channel-independent Semantic
  Status source/contract family **only**. A further Human-Maintainer-authorized
  internal rework — the **Candidate Finalization Governance Rework** (2026-08-18,
  again **not** a new work package) — is **executed**: DEC-S-126, RISK-098, the
  Candidate Approval Record **Template**, and evidence-runner result format **v2**.
  It prepared **governance and tooling only**; at that milestone
  `semantic-status-rev-0002-candidate` was **reserved and not created**, and **that
  rework produced no Candidate evidence, admitted none, and granted no Candidate
  approval**.
- **Candidate authority closure: COMPLETE (2026-08-19).** Fresh revision-bound
  evidence **`AE1-CDS-WP016-SEMSTATUS-004`** was produced, independently reviewed
  (**PASS WITH NOTES**), and **admitted at AE-1** by the Human Maintainer; the
  **Nova Candidate Finalization Review returned GO WITH NOTES**; the Human
  Maintainer **approved Candidate** (`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`);
  and the exact-byte **Promotion Commit
  `22fa0710e2b75df22e7b420c2f9d86bbe67b2777`** (parent
  `8d1374fa4c61cc1eed214823681ee1209a2d91f7`) made it effective — gate **PASS**,
  committed blob identity **15/15 exact**, regression
  **47/47 · 64/64 · 184/184 · 24/24/0/0**, remote fast-forward **PASS**.
  **Candidate is YES**, source revision **`semantic-status-rev-0002-candidate`**,
  maturity **`Candidate`**, approval **`Approved`** — for the channel-independent
  Semantic Status Layer-3 source/contract family only.
- **CDS-WP-016 status:** **Completed.** Its post-promotion current-state
  reconciliation was integrated by the Human-Maintainer commit
  `1fc53ae5afa40807e1950171ab700b0860ee581e`, and closure became effective there.
- Completed work packages: CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005, CDS-WP-006, CDS-WP-007, CDS-WP-008, CDS-WP-009, CDS-WP-010,
  CDS-WP-011, CDS-WP-012, CDS-WP-013, CDS-WP-014, CDS-WP-015, **CDS-WP-016**,
  **CDS-WP-017**, **CDS-WP-018**, **CDS-WP-019**, **CDS-WP-020**

## Operating enablement status

- Foundation status: **Closed with Notes** (CDS-WP-009, 2026-07-16) — see the
  [Foundation Closure Record](../docs/governance/FOUNDATION_CLOSURE_RECORD.md);
  normative on closure, authority state, and the phase boundary; no Candidate,
  Stable, claim, licence, or publication effect
- Operating playbook: **Present** (non-normative) —
  [Foundation Operating Playbook](../docs/operations/FOUNDATION_OPERATING_PLAYBOOK.md)
- Standard change dossier template: **Present** —
  [Standard Change Dossier](../docs/operations/STANDARD_CHANGE_DOSSIER_TEMPLATE.md)
- Elevated change dossier template: **Present** —
  [Elevated Change Dossier](../docs/operations/ELEVATED_CHANGE_DOSSIER_TEMPLATE.md)
- Critical risk actionability: **Present** — 12/12 Critical Risks carry an
  executor role, review trigger, expected evidence, and blocking effect
  ([Critical Risk Action Register](../docs/operations/CRITICAL_RISK_ACTION_REGISTER.md))
- Reference integrity status: **Reviewed — PASS** (0 CDS-authored broken links)
  ([Foundation Reference Integrity Review](../docs/reviews/FOUNDATION_REFERENCE_INTEGRITY_REVIEW.md))
- Pre-Candidate operating plan:
  [Pre-Candidate Operating Plan](../docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md)
- **Current publication state: `Private Development`. Current claims: None.
  Conformance: None. Candidate artifact families: 1 — Semantic Status Foundation /
  `semantic/status` at `semantic-status-rev-0002-candidate`. Stable artifacts:
  None. CoreOps pilot: inactive.**

## Accessibility support baseline status

- Accessibility Baseline ID: **A11Y-BL-001**
- Accessibility Baseline Status: **Declared and committed, no evidence executed**
  (CDS-WP-010, 2026-07-16) — a test contract, not evidence
- Baseline tier count: **3** (Required Core · Complementary · Scope-triggered)
- Environment entry count: **14** (A11Y-ENV-001…014) — Required 6 · Conditional 4 ·
  Deferred 4; Required browser/screen-reader pairings **2**
- Accessibility evidence levels: **5** (AE-0 … AE-4) — unchanged
- Accessibility evidence records for the Semantic Status Candidate scope: **4
  produced** — Evidence 001 (remediation-time, **never admitted**), Evidence 002
  (clean-HEAD, independently reviewed, **admitted** for `semantic-status-rev-0001`),
  Evidence 003 (Proposed Candidate, independently reviewed, **NOT ADMITTED** ·
  `SUPERSEDED_FOR_ADMISSION_BY_EVIDENCE_INPUT_CHANGE`), and Evidence 004
  (Proposed Candidate after the test lifecycle rework, independently reviewed,
  **admitted** for `semantic-status-rev-0002-candidate`). **Admitted evidence
  packages: 2** — Evidence 002 and Evidence 004, each bound to its own source
  revision; **evidence never transfers across a source revision**, so the package
  in force for the current revision is **Evidence 004 only**. Every artifact outside
  that scope remains **AE-0**, and **no baseline environment has been exercised**
- RISK-044: **Mitigating** (baseline defined; gate met, DEC-S-070)

Documents:
[Accessibility Support Baseline](../docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md) ·
[Environment and Scope Matrix](../docs/governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md) ·
[Baseline Maintenance Policy](../docs/governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md) ·
[Evidence Strategy](../docs/governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md) ·
[Defect and Regression Model](../docs/governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md) ·
[Evidence Record Template](../docs/operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md) ·
[Source Register](../docs/research/ACCESSIBILITY_BASELINE_SOURCE_REGISTER.md) ·
[Selection Rationale](../docs/research/ACCESSIBILITY_BASELINE_SELECTION_RATIONALE.md)

## Machine-readable source status

- Machine-readable source status: **Decided and committed** (CDS-WP-011,
  2026-07-16; ADR-0001 committed `a81772c`, 2026-07-17). It was *not implemented* at
  CDS-WP-011; it **has since been implemented** — see the bootstrap, validator, and
  Semantic Status Source Set sections below.
- Token Format Profile: **DTCG 2025.10-based CDS profile**
- DTCG binding: **2025.10** (Format, Color, Resolver modules; Final Community Group
  Report — **not** a W3C Standard)
- Canonical source syntax: **strict JSON (RFC 8259), `.tokens.json`**
- Schema foundation: **JSON Schema Draft 2020-12** (CDS-owned profile contracts
  created by CDS-WP-012; executed by the CDS-WP-013 offline validator — see below)
- Extension namespace: **`io.github.kaykaspers.cds`** (single reserved root within DTCG
  `$extensions`; foreign extensions preserved, not automatically normative)
- Source-set layers: Reference · Semantic · Component · Product Profile; channel
  outputs are generated (non-normative)
- Validation layers: **4** (V1 Syntax · V2 DTCG · V3 CDS Profile · V4 Semantic/
  Governance)
- ADR count: **4** (ADR-0001, ADR-0002, ADR-0003, ADR-0004) — **ADR-0004 is
  `Accepted` and effective** at commit `42a568d8…`; the effective count is **4**
- **No visual or design token value is implemented** — the only implemented token
  source set is the non-visual `semantic/status` set (CDS-WP-015). **The schema and
  resolver contracts created by CDS-WP-012 are Experimental and carry no
  Candidate/Stable status; the offline validator exists since CDS-WP-013
  (Experimental; its evidence independently reviewed by CDS-WP-016 — PASS);
  publication state `Private Development`.**

Documents:
[ADR-0001](../docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) ·
[Machine-Readable Source Model](../docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md) ·
[CDS Token Format Profile](../docs/architecture/CDS_TOKEN_FORMAT_PROFILE.md) ·
[Reference, Resolution and Validation Model](../docs/architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md) ·
[Metadata, Provenance and Identity Model](../docs/architecture/TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md) ·
[Token Format Evaluation](../docs/research/TOKEN_FORMAT_EVALUATION.md) ·
[Token Format Source Register](../docs/research/TOKEN_FORMAT_SOURCE_REGISTER.md) ·
[Implementation Plan](../docs/roadmap/MACHINE_READABLE_SOURCE_IMPLEMENTATION_PLAN.md)

## Machine-readable bootstrap status

- Machine-readable bootstrap: **Implemented, Experimental** (CDS-WP-012, 2026-07-17;
  ADR-0002 committed `1ad9787`) — no Candidate status (DEC-S-092)
- Token Document Schema: **Present** · Source-Set Manifest Schema: **Present** ·
  Resolver Schema: **Present** · Validation Case Schema: **Present** (4 CDS-owned JSON
  Schema Draft 2020-12 contracts; stable `tag:` `$id`s; local `$ref`; offline)
- Schema execution: **Executed by the CDS-WP-013 offline validator** (all five
  schemas pass `check_schema`; 15/15 harness matches — executor-produced, since
  independently reviewed by CDS-WP-016 (PASS); the WP-012-era `Not assessed` state is
  superseded)
- Positive fixture count: **6** · Negative fixture file count: **9** · Validation case
  count: **15** (VAL-CASE-001…015); every fixture covered
- Deterministic serialization: **RFC 8785 (JCS)** · Digest: **SHA-256** (`sha256:`
  lowercase hex); computed by the CDS-WP-013 validator for the 14 V1-parsable
  fixtures (evidence artifacts; fixtures' internal `digestState` intentionally
  unchanged)
- Extension namespace: `io.github.kaykaspers.cds` (payload requires `profileVersion`)
- **No real token/design value, transformer, or build; no Candidate/Stable artifact;
  publication state `Private Development`.**

## Offline validator status (CDS-WP-013)

- Validator status: **Implemented, Experimental; its evidence independently reviewed
  by CDS-WP-016 (Independent Review PASS)** (CDS-WP-013, 2026-07-17; ADR-0003
  committed `a7f2691`)
- Validator runtime: **Python 3.12.10** (CPython, win32; requirement ≥ 3.11) ·
  Validator version: **0.1.0** · Entry point: `python -m tools.cds_validator`
- Dependency versions (exact; [lock](../requirements-validator.lock)):
  `jsonschema==4.26.0`, `rfc8785==0.1.4` (+ 5 pinned transitive packages)
- Unit tests: **71** — result: **71 passed, 0 failed, 0 errors** (`unittest`)
- Validation cases: **15** (VAL-CASE-001…015) — **expected/actual matches: 15/15**,
  0 mismatches, 0 execution errors
- Result schema: **Present**
  ([cds-validation-result](../schemas/cds-validation-result.schema.json); all five
  schemas pass `check_schema`; local registry, offline)
- Digest count: **14** fixtures digested (`sha256:` RFC 8785/SHA-256); 1 undigestible
  (duplicate-key fixture, V1-invalid)
- Evidence: [results](../artifacts/validation/wp013-fixture-results.json) ·
  [digests](../artifacts/validation/wp013-fixture-digests.json) ·
  [Execution Review](../docs/reviews/OFFLINE_TOKEN_VALIDATOR_EXECUTION_REVIEW.md) —
  **executor-produced**. The artifacts carry the frozen field
  `independentReviewState: pending` from their CDS-WP-013 production run and are
  **not edited**; the **evidence has since been independently reviewed by
  CDS-WP-016 (PASS)**, so the DEC-S-103 unreviewed state is superseded.
- **No full-DTCG conformance statement (bounded V2, DEC-S-098); no Candidate/Stable
  artifact (DEC-S-104); publication state `Private Development`; current claims:
  None.**

Documents:
[Validator Architecture](../docs/architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md) ·
[Validator Usage](../docs/operations/OFFLINE_TOKEN_VALIDATOR_USAGE.md) ·
[ADR-0003](../docs/decisions/ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md) ·
[Dependency Source Register](../docs/research/OFFLINE_VALIDATOR_DEPENDENCY_SOURCE_REGISTER.md) ·
[Stack Evaluation](../docs/research/OFFLINE_VALIDATOR_STACK_EVALUATION.md)

## Semantic Status Foundation status (CDS-WP-014)

- Semantic Status Foundation: **Contract defined** (CDS-WP-014, 2026-07-17) —
  **Experimental, not Candidate at that milestone** (DEC-S-113, DEC-S-114);
  **now `Candidate` / `Approved`** (see the Candidate status row below)
- Status axis count: **5** (`condition` · `severity` · `confidence` · `freshness` ·
  `evidence`) · Status value count: **25** (5 per axis; `unknown` explicit on every
  axis) · Status invariant count: **10**
- Combination model: 11-field complete status object · 6 review-required
  combinations · 8 fail-closed states · 6-level disclosure priority · **no aggregate
  health score**
- Communication: text-first accessible meaning; no single-modality encoding; DE/EN
  semantic parity; technical IDs language-neutral
- Token contract: value-neutral roles only — **no token source file, no token name,
  no value, no component**
- Candidate status: **Candidate** — the first Candidate, reached through the
  [Candidate Plan](../docs/roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md) gates and
  made effective by Promotion Commit `22fa0710e2b75df22e7b420c2f9d86bbe67b2777` on
  2026-08-19. At CDS-WP-014 it was **Not Candidate**, with 10 prerequisites and none
  met
- Validator independent review: **Complete — PASS** (the executor-produced WP-013
  evidence was independently reviewed by CDS-WP-016)
- **Publication state `Private Development`; current claims: None.**

Documents:
[Foundation Contract](../docs/foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) ·
[Axis Vocabulary](../docs/foundations/STATUS_AXIS_VOCABULARY.md) ·
[Composition Rules](../docs/foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) ·
[Communication Contract](../docs/foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md) ·
[Token Contract](../docs/foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md) ·
[Candidate Plan](../docs/roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md) ·
[Readiness Review](../docs/reviews/SEMANTIC_STATUS_FOUNDATION_READINESS_REVIEW.md)

## Semantic Status Source Set status (CDS-WP-015)

- Semantic Status Source Set: **Implemented; now `Candidate` / `Approved`**
  (implemented in CDS-WP-015, 2026-07-18, Experimental at the time; **committed** by
  the Human Maintainer) — the DEC-S-121 **independently unreviewed** state is
  **superseded**: independently reviewed by CDS-WP-016
  (**Independent Review PASS**, **Candidate Recommendation GO**); **GO is not a
  Candidate award** — the **Nova Candidate Maturity Review** then returned
  **NO-GO** on the Candidate Accessibility Gate, whose remediation is **executed**,
  **independently reviewed**, and admitted at AE-1
  (DEC-S-115, DEC-S-122, DEC-S-125)
- **Current source revision: `semantic-status-rev-0002-candidate`** · maturity
  **`Candidate`** · approval **`Approved`** · admitted evidence in force
  **`AE1-CDS-WP016-SEMSTATUS-004`** at **AE-1**, this source scope only ·
  Promotion Commit `22fa0710e2b75df22e7b420c2f9d86bbe67b2777` (2026-08-19)
- **Stable: No** · claims **None** · conformance **None** · AE-2/AE-3/AE-4 **None**
  · channel evidence **None** · consumer evidence **None**
- Source-Set ID: **`semantic/status`** · Layer: semantic · Revision at CDS-WP-015:
  `semantic-status-rev-0001` (**current revision:
  `semantic-status-rev-0002-candidate`**) · Axis count: **5** · Status token count:
  **25** (non-visual `string` identity values; `status.<axis>.<value>`)
- Manifest/Resolver: present, local-only, identity-aligned; no Product-Profile
  extension points
- Terminology entries: **25 DE / 25 EN** (0 missing;
  [mapping](../docs/foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md))
- Validation cases: **24** (VAL-CASE-001…024; WP-013 baseline immutable) —
  **expected/actual matches: 24/24** · WP-013 clean re-execution: **15/15**
  (committed WP-014 revision, worktree clean) · Unit tests: **103/103**
- Validation-case schema: additively corrected (Nova-authorized; fixture-path
  families + 9 `semantic-status-*` categories; `$id` unchanged; CLI untouched)
- Evidence: **executor-produced** — [results](../artifacts/validation/wp015-fixture-results.json) ·
  [source-set run](../artifacts/validation/wp015-semantic-status-source-results.json) ·
  [re-execution](../artifacts/validation/wp015-wp013-clean-reexecution-results.json);
  independent review: **Pending**
- Candidate dossier: **Candidate gate complete — Candidate promotion effective**
  ([dossier](../docs/operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md))
- Authority records:
  [Candidate Approval Record](../docs/operations/SEMANTIC_STATUS_CANDIDATE_APPROVAL_RECORD.md)
  (`CAR-CDS-WP016-SEMSTATUS-001`) ·
  [AE1-004 Admission Record](../docs/governance/SEMANTIC_STATUS_AE1_004_ADMISSION_RECORD.md) ·
  [Candidate Promotion Effectivity Record](../docs/governance/SEMANTIC_STATUS_CANDIDATE_PROMOTION_EFFECTIVITY_RECORD.md)
  — **authority records, never evidence**
- **Publication state `Private Development`; current claims: None; no Stable
  artifact.**

Documents:
[Machine-Readable Validation Contract](../docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md) ·
[Deterministic Serialization and Digest Model](../docs/architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md) ·
[ADR-0002](../docs/decisions/ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md) ·
[Token Document Schema](../schemas/cds-token-document.schema.json) ·
[Manifest Schema](../schemas/cds-source-set-manifest.schema.json) ·
[Resolver Schema](../schemas/cds-resolver-document.schema.json) ·
[Validation Case Schema](../schemas/cds-validation-case.schema.json) ·
[Validation Cases](../tests/fixtures/machine-readable/VALIDATION_CASES.json)

## Foundation review status

- Foundation review: **Completed** (CDS-WP-008, 2026-07-16), reviewed revision
  `7b71652`
- **Recommended milestone outcome: `GO WITH NOTES`** — *a Claude recommendation,
  not a final Human-Maintainer decision*
- Foundation blocker count: **0**
- Non-blocking findings: **12** (FM-F-001 … FM-F-012)
- Completeness matrix: **55 criteria** — 44 Met · 4 Met-with-notes · 3 Partially
  met · 4 Not met · 0 N/A
- Candidate readiness: governance **Met** · artifact **Not met** (none exists — not
  a blocker) · evidence **Not met** · consumer-validation **Partially met**
- CoreOps pilot entry readiness: **Partially met — pilot inactive** (8 criteria: 3
  Met, 1 partial, 3 not met, 1 not-yet-assessable)
- Governance operating readiness: **Partially met** — Standard track operational;
  Elevated path High burden for current staffing (RISK-029, RISK-040, RISK-048)
- No artifact promoted; no claim created
- **Closure decision (CDS-WP-009):** the Human Maintainer accepted `GO WITH NOTES`
  by committing CDS-WP-008 and initiating CDS-WP-009. **Foundation: Closed with
  Notes.** The next phase (Pre-Candidate Operating Enablement) is authorized; no
  Candidate, pilot, licence, or publication is authorized.

Documents:
[Foundation Milestone Review](../docs/reviews/FOUNDATION_MILESTONE_REVIEW.md) ·
[Completeness Matrix](../docs/reviews/FOUNDATION_COMPLETENESS_MATRIX.md) ·
[Governance Affordability](../docs/reviews/GOVERNANCE_AFFORDABILITY_AND_OPERATING_READINESS.md) ·
[Candidate & Pilot Readiness](../docs/reviews/FOUNDATION_CANDIDATE_AND_PILOT_READINESS.md) ·
[Open Gaps & Dependencies](../docs/reviews/FOUNDATION_OPEN_GAPS_AND_DEPENDENCIES.md) ·
[Next-phase Recommendation](../docs/reviews/NEXT_PHASE_RECOMMENDATION.md)

## Accessibility status

- Accessibility policy status: **Defined** (CDS-WP-007, 2026-07-16)
- Accessibility target: **WCAG 2.2 Level AA** for the applicable web-based scope
  (DEC-S-049) — **a target, not a conformance claim** (DEC-S-050)
- WCAG applicability criterion count: **56 listed** Level A + AA (**32 A · 24
  AA**); **55 applicable** (**31 A · 24 AA**), excluding obsolete 4.1.1
- Accessibility evidence levels: **5** — AE-0 … AE-4 (Accessibility Evidence and
  Claims Model; the responsibility split they record is DEC-S-051)
- Accessibility channel profiles: **6** — 2 with a target, 0 Candidate-eligible
- CR-024 policy status: **Resolved at policy level** (DEC-S-060); entry criterion
  `Accessibility target defined` met with the CDS-WP-007 commit
- **Current accessibility evidence: `AE1-CDS-WP016-SEMSTATUS-004` at AE-1**, bound
  to the current source revision `semantic-status-rev-0002-candidate`, for the
  channel-independent Semantic Status source/contract family; **every other artifact
  is AE-0**. `AE1-CDS-WP016-SEMSTATUS-002` is the **historical
  `semantic-status-rev-0001` admission** and **does not transfer** to a later
  Candidate source revision (DEC-S-126); `AE1-CDS-WP016-SEMSTATUS-003` is **not
  admitted**. A support baseline is **declared and committed** (A11Y-BL-001,
  CDS-WP-010) but **no evidence has been executed in any baseline environment**; no
  AE-2, AE-3, or AE-4 exists; no accessibility claim of any level is valid

Documents:
[Accessibility and Inclusive Design Policy](../docs/governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) ·
[Responsibility Model](../docs/governance/ACCESSIBILITY_RESPONSIBILITY_MODEL.md) ·
[Requirements Baseline](../docs/governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md) ·
[WCAG 2.2 AA Applicability Matrix](../docs/governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md) ·
[Evidence and Claims Model](../docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) ·
[Channel Profiles](../docs/governance/ACCESSIBILITY_CHANNEL_PROFILES.md) ·
[Limitations and Exception Policy](../docs/governance/ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md) ·
[CoreOps Pilot Accessibility Criterion](../docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md) ·
[Architecture Alignment](../docs/architecture/ACCESSIBILITY_ARCHITECTURE_ALIGNMENT.md)

## Governance status

- Governance status: Defined (CDS-WP-006, 2026-07-16)
- Governance roles: **6** — Human Maintainer · Nova · Claude · Consumer
  Maintainer · Contributor · Evidence Reviewer
- Governance tracks: **2** — Standard, Elevated (ceremony scales; obligation
  does not)
- **Maturity states: 7** — Proposed · Exploratory · Experimental · Candidate ·
  Stable · Deprecated · Removed
- **Publication states: 5** — Private Development · Controlled Preview · Public
  Preview · Public Stable · Archived
- **Claim types: 4** — Uses CDS Artifacts · CDS-integrated · CDS-validated ·
  CDS-conformant. `CDS certified` **prohibited**
- Artifact licence classes: **10** · Change classes: **6** · Compatibility axes:
  **8** · Exception statuses: **6** · Risk statuses: **5**
- **Risk owner model: finalized** (DEC-S-045) — Accountable Risk Owner: Human
  Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation
  · Evidence Reviewer: Nova or authorized reviewer. No longer provisional.
- **Current publication state: `Private Development`** — unchanged by CDS-WP-006
- **No licence selected for any artifact class. No release is currently
  possible.** Exactly one artifact family is Candidate: the Semantic Status
  Foundation / `semantic/status` at `semantic-status-rev-0002-candidate`, with
  maturity `Candidate` and approval `Approved`. No artifact is Stable.

Documents:
[Governance Operating Model](../docs/governance/GOVERNANCE_OPERATING_MODEL.md) ·
[Source Conflict Resolution](../docs/governance/SOURCE_CONFLICT_RESOLUTION_POLICY.md) ·
[Artifact Maturity Lifecycle](../docs/governance/ARTIFACT_MATURITY_LIFECYCLE.md) ·
[Versioning, Compatibility and Deprecation](../docs/governance/VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md) ·
[Contribution and Acceptance](../docs/governance/CONTRIBUTION_AND_ACCEPTANCE_MODEL.md) ·
[Exception and Product Profile Governance](../docs/governance/EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md) ·
[Adoption, Conformance and Claims](../docs/governance/ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md) ·
[Risk Governance Model](../docs/governance/RISK_GOVERNANCE_MODEL.md) ·
[Licensing and Publication](../docs/governance/LICENSING_AND_PUBLICATION_DECISION_MODEL.md) ·
[Release and Change Control](../docs/governance/RELEASE_AND_CHANGE_CONTROL_POLICY.md)

## Architecture status

- Architecture status: Logical architecture defined (CDS-WP-005, 2026-07-16);
  **visual foundation architecture defined (CDS-WP-019, 2026-08-26)**;
  **visual reference and semantic token contract defined (CDS-WP-020, 2026-08-26)**
- Architecture layers: **8**
- Architecture documents: **17** — 8 from CDS-WP-005, **7 visual foundation
  documents from CDS-WP-019** (plus 4 CDS-WP-019 governance documents),
  **2 visual token foundation documents from CDS-WP-020** (plus 1 CDS-WP-020
  governance document and 1 **non-normative** open-decision register)
- Artifact classes: 8 · Token flow levels: 5 · Status axes: 5 · Consumer
  contracts: 5 · Architecture invariants: 16 · **Visual foundation families: 9 ·
  Visual foundation invariants: 14**
- Architecture requirement coverage: **40 / 40** requirements mapped —
  **9 Addressed by architecture · 27 Partially addressed · 0 Deferred to
  CDS-WP-006 · 0 Deferred to CDS-WP-007 · 2 Consumer-owned · 2 Out of CDS scope**
  (reconciled by CDS-WP-007; no requirement is deferred to a policy work package
  any longer)
- **The architecture selects no technology, format, tool, or visual design**
  (DEC-S-032). Governance (CDS-WP-006) and the accessibility target (CDS-WP-007)
  now exist; what remains is design, implementation, and evidence — not policy.
- **The visual foundation architecture selects no visual value.** CDS-WP-019
  defines structure only: no colour, typeface, size, spacing, radius, stroke,
  shadow, opacity, icon, illustration, motion value, breakpoint, or theme instance.
  It registers **no new Decision** — every binding statement applies a decision
  already in force — and it grants **no maturity**: all nine visual foundation
  families are **`Proposed`**, and **no visual value exists in CDS**.
- **The visual token foundation selects no value and creates no identifier either.**
  CDS-WP-020 defines the **contract** for token-flow layers 1 and 2 — what a
  reference primitive and a semantic role are, what each must declare, and how a
  role aliases a primitive. It returned **`DECISION_REQUIRED`**: every concrete
  value and every machine-readable visual source was gated on **OD-1 … OD-7**. The
  2026-08-27 Decision Integration Pass answered **OD-1, OD-2 and OD-3**
  (DEC-S-128 … DEC-S-131, ADR-0004 — **effective at `42a568d8…`**) and **selected
  no value**. **OD-4 and OD-7 are since answered, OD-5 partially, OD-6A by policy,
  OD-6B by existing authority** — effective at `2cb244e8…` — and **VP-3, VP-5,
  VP-6 and VP-7 stay unsatisfied**.
  **Visual values: 0. Visual source sets in existence: 0. Visual
  families at Candidate: 0. Visual families at Stable: 0.**

Documents:
[Design System Architecture](../docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md) ·
[Source of Truth and Authority](../docs/architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md) ·
[Token and Theme Architecture](../docs/architecture/TOKEN_AND_THEME_ARCHITECTURE.md) ·
[Product Profile and Extension Model](../docs/architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) ·
[Artifact Distribution and Channel Model](../docs/architecture/ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) ·
[Consumer Contract and Reconciliation Model](../docs/architecture/CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md) ·
[Evidence, Traceability and Status Semantics](../docs/architecture/EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) ·
[Architecture Requirements Traceability](../docs/architecture/ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md)

Visual foundation architecture (CDS-WP-019):
[Visual Foundation Architecture](../docs/architecture/VISUAL_FOUNDATION_ARCHITECTURE.md) ·
[Colour](../docs/architecture/VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md) ·
[Typography](../docs/architecture/VISUAL_FOUNDATION_TYPOGRAPHY_ARCHITECTURE.md) ·
[Spatial](../docs/architecture/VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md) ·
[Shape and Surface](../docs/architecture/VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md) ·
[Iconography and Imagery](../docs/architecture/VISUAL_FOUNDATION_ICONOGRAPHY_AND_IMAGERY_ARCHITECTURE.md) ·
[Theme](../docs/architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md) ·
[Accessibility Mapping](../docs/governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md) ·
[Channel Mapping](../docs/governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md) ·
[Brand and Product Profile Boundary](../docs/governance/VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md) ·
[Governance and Lifecycle](../docs/governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)

Visual token foundation (CDS-WP-020):
[Visual Reference Token Foundation](../docs/architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md) ·
[Visual Semantic Token Foundation](../docs/architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) ·
[Visual Token Value Selection Rules](../docs/governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md) ·
[Visual Token Foundation Open Decisions](../docs/roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
(**non-normative**)

## Consumer research status

- Consumer research status: Completed (CDS-WP-004, evidence dated 2026-07-15)
- Consumer repositories analyzed: 3 — CoreOps (primary pilot), SpeakCore and
  CastCore (secondary)
- Evidence sources read: 15 (14 usable), all bound to committed revisions
- Requirements registered: 40 (CR-001 … CR-040)
- Pilot-relevant requirements: 28 (Must 16, Should 11, Could 1)
- Shared CDS Candidates: 25
- Pilot groups: 5 (A–E) with 9 scenarios
- Hypothesis consumer validation: HYP-001 … HYP-008, all still **research
  hypotheses**
- **Evidence level: documentation only.** No user research, interviews, or
  usability testing took place (RISK-017). No requirement is an accepted CDS
  standard (DEC-S-014). The pilot contract is committed, not active.

Documents:
[Consumer Requirements Model](../docs/governance/CONSUMER_REQUIREMENTS_MODEL.md) ·
[Traceability](../docs/governance/CONSUMER_REQUIREMENTS_TRACEABILITY.md) ·
[Pilot Scope and Scenarios](../docs/governance/COREOPS_PILOT_SCOPE_AND_SCENARIOS.md) ·
[Pilot Contract](../docs/governance/COREOPS_PILOT_CONTRACT.md) ·
[Validation Plan](../docs/governance/CONSUMER_VALIDATION_PLAN.md) ·
[Consumer Evidence Register](../docs/research/CONSUMER_EVIDENCE_REGISTER.md) ·
[Consumer Hypothesis Validation](../docs/research/CONSUMER_HYPOTHESIS_VALIDATION.md)

## Research status

- Research status: Benchmark and differentiation research completed
  (CDS-WP-003, evidence dated 2026-07-15)
- Benchmarked systems: 10
- Benchmark dimensions: 14
- Official sources registered: 33 opened (31 benchmark + 2 standards), 27 with
  usable evidence
- Evidence matrix: 140 cells (10 systems × 14 dimensions), 105 with usable
  evidence
- Differentiation hypotheses: 8 (HYP-001 … HYP-008), all **Research hypothesis**
- **Research findings are non-normative.** They are evidence and hypotheses, not
  decisions, principles, or technology recommendations.

Research documents:
[Design System Benchmark](../docs/research/DESIGN_SYSTEM_BENCHMARK.md) ·
[Benchmark Evidence Matrix](../docs/research/BENCHMARK_EVIDENCE_MATRIX.md) ·
[Benchmark Source Register](../docs/research/BENCHMARK_SOURCE_REGISTER.md) ·
[CDS Differentiation Hypotheses](../docs/research/CDS_DIFFERENTIATION_HYPOTHESES.md) ·
[Research Limitations](../docs/research/RESEARCH_LIMITATIONS.md)

## Registered scope

Six capability domains (DEC-S-007):

1. Brand and Identity
2. Experience and Interaction
3. Foundations and Tokens
4. Components and Patterns
5. Channels and Communication
6. Governance and Enablement

Cross-cutting concerns: accessibility, inclusive design, localization and
internationalization, offline and self-hosted use, security-aware interaction
design, privacy-aware interaction design, maintainability, provenance and
licensing, quality evidence, design-code-documentation alignment.

Registration is scope, not availability. Long-term scope creates no delivery,
stability, support, release, or compatibility commitment (DEC-S-009).

Normative source: [Concept and Scope](../docs/governance/CONCEPT_AND_SCOPE.md)

## Consumer classes

Three relationship classes (DEC-S-010):

- Core Product Consumer
- Associated Project Consumer
- Potential External Consumer

Classification grants no brand endorsement, public availability, licensing
rights, or support.

Normative source:
[Consumer and Stakeholder Model](../docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md)

## NDF Skills

- NDF Skills Version: v1.0.0
- Skills Count: 38
- Skills Status: Verified and locally available
- Skills Source Commit: `9dcadc12fb960914b9a5baeff2ab1aee75912b57`
- Skills-first Operating Mode: Active

Details: [NDF Skills Inventory](NDF_SKILLS_INVENTORY.md),
[NDF Skills Manifest](NDF_SKILLS_MANIFEST.json),
[NDF Skills Provenance](../docs/governance/NDF_SKILLS_PROVENANCE.md)

## Current strategic position

CDS is intended to become the normative design Single Source of Truth for
existing and future Core products.

No final brand, visual, tooling, framework, or licensing decision is currently
authorized.

## Authority model

- Human Maintainer: final normative approvals and exclusive Git-write, release,
  and publication authority
- Nova: strategy, planning, architecture, review, project control, and approval
  recommendations
- Claude: scoped local analysis and file work only
- Consumer projects: requirements and adoption evidence

## Pilot consumer relationship

CoreOps is the first reference consumer of stable CDS foundations. CoreOps is
not the sole design target and not the sole source of requirements
(see DEC-S-002).

Further anticipated consumers:

- SpeakCore
- CastCore
- AirCore
- future Core products

Consumer inclusion does not automatically authorize full brand adoption.
Product-family classes and adoption levels remain to be defined.

CoreOps-specific solutions remain CoreOps-owned unless generalized and
explicitly accepted through a CDS work package (see DEC-S-011). The concrete
pilot contract is defined in CDS-WP-004.

## Register scope

- Decisions: DEC-S-001 … DEC-S-135 (135) — 6 strategic foundation decisions
  (CDS-WP-001), 6 strategic scope decisions (CDS-WP-002), 8 consumer and pilot
  scope decisions (CDS-WP-004), 12 logical architecture decisions (CDS-WP-005),
  16 governance, lifecycle and publication decisions (CDS-WP-006), 12
  accessibility and inclusive design decisions (CDS-WP-007), 4 operating
  enablement and pre-candidate decisions (CDS-WP-009), 8 accessibility support
  baseline and evidence decisions (CDS-WP-010), 10 machine-readable source and
  token format decisions (CDS-WP-011, DEC-S-073 … DEC-S-082), 10 machine-readable
  bootstrap and validation decisions (CDS-WP-012, DEC-S-083 … DEC-S-092), and
  12 offline validator implementation decisions (CDS-WP-013, DEC-S-093 …
  DEC-S-104), 10 semantic status foundation decisions (CDS-WP-014, DEC-S-105 …
  DEC-S-114), 10 semantic status source and evidence decisions (CDS-WP-015,
  DEC-S-115 … DEC-S-124), **1 accessibility / maturity / channel boundary
  decision (CDS-WP-016, DEC-S-125)**, and **1 candidate finalization / maturity /
  evidence transition decision (CDS-WP-016 Candidate Finalization Governance
  Rework, DEC-S-126)**, and **1 phase transition decision (CDS Phase Transition
  Governance Package, DEC-S-127)**, and **4 visual token representation, evaluation
  authority and source identity decisions (CDS-WP-020 Decision Integration Pass,
  DEC-S-128 … DEC-S-131)**, and **4 visual identifier, scale ownership, role
  admission and theme sequencing decisions (CDS Step-9 Decision Integration Pass,
  DEC-S-132 … DEC-S-135)**. DEC-S-001 … DEC-S-114 unchanged by
  CDS-WP-015; DEC-S-001 … DEC-S-125 unchanged by the rework; **DEC-S-001 …
  DEC-S-126 unchanged by the phase transition**; **DEC-S-001 … DEC-S-127 unchanged
  by the Decision Integration Pass**; **DEC-S-001 … DEC-S-131 unchanged by the
  Step-9 Decision Integration Pass**.
  **ADRs: 5 (ADR-0001, ADR-0002, ADR-0003, ADR-0004, ADR-0005).**
  **Effectivity: DEC-S-128 … DEC-S-131 and ADR-0004 are effective**, at the
  Human-Maintainer exact-byte integration commit
  `42a568d823de3388e45af62967546f13ad67eff6`; **DEC-S-132 … DEC-S-135 and ADR-0005
  are effective**, at the Human-Maintainer exact integration commit
  `2cb244e889c1a6b5a278afb233995a0379b5d9ef`. The **effective** register is
  **DEC-S-001 … DEC-S-135 (135)** with **5 ADRs**.
- Risks: RISK-001 … RISK-098 (98) — **89 `Monitored`; RISK-031, RISK-040, RISK-044,
  RISK-066, RISK-067, RISK-068, RISK-069, RISK-071, and RISK-098 `Mitigating`**;
  **risk owner model finalized** by CDS-WP-006; RISK-082 … RISK-089 added by CDS-WP-014;
  **RISK-090 … RISK-097 added by CDS-WP-015** (all `Monitored`; no existing status
  changed); **RISK-098 added by the CDS-WP-016 Candidate Finalization Governance
  Rework** directly as `Mitigating` (no existing status changed). No risk accepted
  or closed.

## Intentionally open decision areas

No final decision exists for:

- logo,
- logo architecture,
- colors,
- typography,
- icons,
- illustration,
- imagery,
- dark theme,
- light theme,
- design tool,
- component framework,
- token build system,
- documentation platform,
- package architecture,
- repository split,
- license,
- public release,
- contribution model,
- long-term compatibility commitments,
- concrete product signatures.

These areas remain open until an explicitly authorized work package decides
them (see DEC-S-003).

**CDS-WP-019 and CDS-WP-020 closed none of them.** Defining the *architecture* of
the visual foundation — what a colour role must declare, what a theme may not do,
how a name is formed — and then defining the *contract* for reference primitives and
semantic roles decides **no colour, typeface, icon, logo, illustration, imagery, or
theme**. Every visual area above is still open, and the two layers are the frame
those later decisions must fit, not a substitute for them.

**CDS-WP-020 additionally recorded why they are still open.** Its
**`DECISION_REQUIRED`** result names seven normative choices — **OD-1 … OD-7** —
that gate every concrete value: the colour space, the admitted `$type` set, the
visual source-set identity and topology, the identifier grammar, scale topology, the
role vocabulary and family granularity, and the sequencing against CDS-WP-022. They
are held in the **non-normative**
[Visual Token Foundation Open Decisions](../docs/roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
register. **Three have since been decided** — the colour space (**DEC-S-128**), the
admitted `$type` set (**DEC-S-130**), and the source-set identity and topology
(**DEC-S-131**), with **DEC-S-129** adding the contrast evaluation authority and
**ADR-0004** the architecture rationale; **all five are effective at commit
`42a568d8…`, and none of them selects a value**. **OD-4 and OD-7 are answered, OD-5
partially answered, OD-6A policy-answered and OD-6B answered by existing authority**
by the CDS Step-9 Decision Integration Pass (2026-09-05), **prepared and not yet
effective**. **What remains undecided:** the concrete role vocabulary, the
per-family scale topology parameters, VF-1 tonal topology, the OD-1 `hex` residual,
the OD-2 font-identity and composite residuals, and any migration compatibility
mechanism outside the normative Semantic alias graph.

**Areas that are no longer open.** Four areas that this list previously carried
have since been decided and are governed by committed normative sources. They are
recorded here so the list is not read as still open:

| Area | Decided by | Normative source |
| --- | --- | --- |
| Token format (machine-readable source format) | CDS-WP-011 · ADR-0001 · DEC-S-073 … DEC-S-082 | [ADR-0001](../docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) · [CDS Token Format Profile](../docs/architecture/CDS_TOKEN_FORMAT_PROFILE.md) |
| Versioning and maturity model | CDS-WP-006 · DEC-S-035 … DEC-S-040 | [Artifact Maturity Lifecycle](../docs/governance/ARTIFACT_MATURITY_LIFECYCLE.md) · [Versioning, Compatibility and Deprecation Policy](../docs/governance/VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md) |
| Conformance and adoption policy | CDS-WP-006 · DEC-S-044 | [Adoption, Conformance and Claims Policy](../docs/governance/ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md) |
| Product Profile and override governance | CDS-WP-005 · CDS-WP-006 · DEC-S-042, DEC-S-043 | [Exception and Product Profile Governance](../docs/governance/EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md) · [Product Profile and Extension Model](../docs/architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) |

**A decided model is not an applied one.** No Product Profile exists or is
activated, no adoption or conformance claim is valid, no artifact is `Stable`, and
no version has been released. **Token build system** remains open and is distinct
from the decided token *format*.

## Related documents

- [Concept and Scope](../docs/governance/CONCEPT_AND_SCOPE.md) — normative scope source
- [Consumer and Stakeholder Model](../docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md)
- [Scope Boundary Matrix](../docs/governance/SCOPE_BOUNDARY_MATRIX.md)
- [Foundation Context Pack](CONTEXT_PACK_FOUNDATION.md)
- [Work Packages](WORK_PACKAGES.md)
- [Next Phase](NEXT_PHASE.md)
- [Project Charter](../docs/governance/PROJECT_CHARTER.md)
- [Decision Index](../docs/decisions/DECISION_INDEX.md)
- [Risk Register](../docs/risks/RISK_REGISTER.md)
- [Project Brain](../project-brain/PROJECT_BRAIN.md)
