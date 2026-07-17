# Next Phase

- **Phase:** Pre-Candidate Operating Enablement — **Foundation / Pre-Design:
  Closed with Notes**
- **Completed work packages:** CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005, CDS-WP-006, CDS-WP-007, CDS-WP-008, CDS-WP-009, CDS-WP-010,
  CDS-WP-011, CDS-WP-012
- **Next work package:** **CDS-WP-013 — Offline Token Profile Validator and Fixture
  Harness** (authorized as next; not yet executed). The Foundation is closed with notes;
  operating enablement is in place; the accessibility support baseline (A11Y-BL-001) is
  defined; the machine-readable source format is decided (ADR-0001); and the
  value-neutral bootstrap (4 schemas, 15 fixtures, V1–V4 contract, RFC 8785/SHA-256
  serialization, ADR-0002) is implemented but Experimental and not executed.

## Status of completed work packages

### CDS-WP-001 — Project Governance and NDF Bootstrap — Completed

Charter, role and authority model, DEC-S-001 … DEC-S-006, RISK-001 … RISK-005,
controlled roadmap.

### CDS-WP-001A — NDF Skills Bootstrap — Completed

38 verified docs-only NDF v1.0.0 Skills pinned to commit
`9dcadc12fb960914b9a5baeff2ab1aee75912b57`; Skills-first mode active.

### CDS-WP-002 — Concept and Scope Registration — Completed

Six capability domains, ten cross-cutting concerns, twelve non-goals, three
consumer classes, ownership boundaries. DEC-S-007 … DEC-S-012,
RISK-006 … RISK-009.

### CDS-WP-003 — Benchmark and Differentiation Research — Completed

Ten design systems reviewed from official sources; HYP-001 … HYP-008 assessed.
RISK-010 … RISK-013. **Non-normative.**

### CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract — Completed

Three consumers analyzed at committed revisions; CR-001 … CR-040 registered and
traced; bounded CoreOps pilot and contract. DEC-S-013 … DEC-S-020,
RISK-014 … RISK-019.

### CDS-WP-005 — Design System Architecture — Completed

Eight-layer logical architecture, authority model, token flow, profiles and
reconciliation, channels and distribution, consumer contracts, status semantics.
DEC-S-021 … DEC-S-032, RISK-020 … RISK-028. **No technology or design selected.**

### CDS-WP-006 — Governance, Versioning, Contribution, Risk and Publication Model — Completed

Operationalized the architecture into governance:

- **Governance operating model** — six roles, Standard and Elevated tracks, an
  authority matrix, and the rule that ceremony scales but obligation does not
  (DEC-S-033).
- **Source conflict resolution** — neither normative source wins automatically; a
  conflict invalidates the affected state (DEC-S-034).
- **Seven-state maturity lifecycle** — Proposed → Exploratory → Experimental →
  Candidate → Stable → Deprecated → Removed, on an axis separate from release
  version and publication state (DEC-S-035, DEC-S-036).
- **Versioning and compatibility** — MAJOR.MINOR.PATCH, an honest pre-1.0
  policy, immutable release identity, and compatibility declared across eight
  axes (DEC-S-037 … DEC-S-039).
- **Deprecation and removal** — deprecation before removal, bounded emergency
  removal (DEC-S-040).
- **Contribution and acceptance** — a ten-step flow with five outcomes
  (DEC-S-041).
- **Exceptions and Product Profiles** — bounded, expiring, and never
  retrospective legitimation (DEC-S-042, DEC-S-043).
- **Adoption claims** — four graded types; `CDS certified` prohibited
  (DEC-S-044).
- **Risk ownership finalized** — Human Maintainer accountable, Nova controller
  (DEC-S-045).
- **Publication and licensing** — five states with a gate; licensing decided per
  ten artifact classes (DEC-S-046, DEC-S-047).
- **Release control** — no automated approval or publication (DEC-S-048).

Added DEC-S-033 … DEC-S-048 and RISK-029 … RISK-040.

**No licence was selected, no publication approved, no technology or design
chosen, and no accessibility level set.** The current publication state remains
`Private Development`.

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

Completion is reported for Human Maintainer review. No Git write action was
performed.

### CDS-WP-007 — Accessibility and Inclusive Design Policy — Completed

Defined the normative CDS accessibility and inclusive-design policy:

- **Target** — **WCAG 2.2 Level AA** for the applicable web-based scope
  (DEC-S-049), resolving **CR-024** at policy level (DEC-S-060). No AAA
  commitment. **A target is not a conformance claim** (DEC-S-050).
- **Applicability matrix** — all Level A and AA success criteria: **56 listed**
  (32 A · 24 AA), **55 applicable** (31 A · 24 AA), excluding the obsolete 4.1.1.
  No pass/fail statement.
- **Responsibility** — shared by contract; **49 of 55 applicable criteria require
  both CDS and the consumer** (DEC-S-051, DEC-S-052).
- **Evidence** — five levels AE-0 … AE-4 (Evidence and Claims Model); automated-
  only is never sufficient (DEC-S-053). Every artifact is **AE-0**; no support
  baseline exists.
- **Channels** — six profiles; only two have a target; **none is Candidate- or
  Stable-eligible** (DEC-S-058).
- **Limits** — accessibility cannot be waived by an ordinary exception
  (DEC-S-059); no legal or certification statement (policy boundary, standard-
  status doc); native semantics first and APG examples are informative only
  (DEC-S-054).
- **Pilot** — CR-024 resolved at policy level; entry criterion satisfiable on
  Human Maintainer commit; **the pilot has not started and cannot start.**

Reconciled CR-021, CR-022, CR-024, and CR-034 traceability. Added
DEC-S-049 … DEC-S-060 and RISK-041 … RISK-048.

**No artifact was promoted, no claim, tag, or release created, and every artifact
remains AE-0.** Publication state remains `Private Development`. No Git write
action was performed.

Documents:
[Accessibility and Inclusive Design Policy](../docs/governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) ·
[WCAG 2.2 AA Applicability Matrix](../docs/governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md) ·
[Evidence and Claims Model](../docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) ·
[Channel Profiles](../docs/governance/ACCESSIBILITY_CHANNEL_PROFILES.md) ·
[CoreOps Pilot Accessibility Criterion](../docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md)

### CDS-WP-008 — Foundation Milestone Review — Completed

Reviewed the completed Foundation phase across twelve dimensions (55 criteria),
three governance dry runs, four-axis Candidate readiness, an eight-criterion
CoreOps pilot entry matrix, and all 48 risks.

- **Result: zero Foundation blockers.** No normative contradiction; every register
  balances (DEC 60 · RISK 48 · CR 40 · arch-status 9/27/2/2 · WCAG 55 applicable).
- **Recommended milestone outcome: `GO WITH NOTES`** — the Foundation can be
  closed with mandatory next-phase notes.
- **12 findings (FM-F-001 … FM-F-012)**, all next-phase / Candidate / pilot /
  publication prerequisites or long-term operating concerns — none a blocker.
- **No normative source changed; no Decision, Risk, ADR, or work-package ID
  created; no artifact promoted; publication state `Private Development`.**

Documents:
[Foundation Milestone Review](../docs/reviews/FOUNDATION_MILESTONE_REVIEW.md) ·
[Completeness Matrix](../docs/reviews/FOUNDATION_COMPLETENESS_MATRIX.md) ·
[Governance Affordability](../docs/reviews/GOVERNANCE_AFFORDABILITY_AND_OPERATING_READINESS.md) ·
[Candidate & Pilot Readiness](../docs/reviews/FOUNDATION_CANDIDATE_AND_PILOT_READINESS.md) ·
[Open Gaps](../docs/reviews/FOUNDATION_OPEN_GAPS_AND_DEPENDENCIES.md) ·
[Next-phase Recommendation](../docs/reviews/NEXT_PHASE_RECOMMENDATION.md)

### CDS-WP-009 — Operating Enablement and Pre-Candidate Readiness — Completed

Recorded Foundation closure with notes and operationalized the committed
governance without producing any design, token, component, tool, or product code:

- **Foundation Closure Record** — normative on the fact of closure, the authority
  state, and the phase boundary (`GO WITH NOTES` accepted by the Human Maintainer
  via commit of CDS-WP-008 and initiation of CDS-WP-009); no Candidate, claim,
  licence, or publication effect.
- **Operating playbook + Standard/Elevated change-dossier templates** — a
  lightweight, non-normative operational view of the governance (DEC-S-063).
- **Critical Risk Action Register** — the 12 Critical Risks made actionable with an
  executor role, review trigger, expected evidence, and blocking effect (DEC-S-064).
- **Foundation Reference Integrity Review** — PASS; 0 CDS-authored broken links.
- **Pre-Candidate Operating Plan** — the phase entry state, prerequisites, and
  Candidate entry conditions.

Added DEC-S-061 … DEC-S-064; moved RISK-040 `Monitored → Mitigating` (the only risk
status change; no acceptance or closure). Publication state remains `Private
Development`. No Git write action was performed.

Documents:
[Foundation Closure Record](../docs/governance/FOUNDATION_CLOSURE_RECORD.md) ·
[Operating Playbook](../docs/operations/FOUNDATION_OPERATING_PLAYBOOK.md) ·
[Standard Dossier](../docs/operations/STANDARD_CHANGE_DOSSIER_TEMPLATE.md) ·
[Elevated Dossier](../docs/operations/ELEVATED_CHANGE_DOSSIER_TEMPLATE.md) ·
[Critical Risk Action Register](../docs/operations/CRITICAL_RISK_ACTION_REGISTER.md) ·
[Reference Integrity Review](../docs/reviews/FOUNDATION_REFERENCE_INTEGRITY_REVIEW.md) ·
[Pre-Candidate Operating Plan](../docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md)

### CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy — Completed

Defined the first accessibility support baseline and its supporting policies using
authorized official standards/vendor research — without running any test or
selecting any tool:

- **A11Y-BL-001** ([Accessibility Support Baseline](../docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md)),
  pending Human-Maintainer commit — a **test contract, not evidence**.
- **Three tiers** (Required / Complementary / Scope-triggered) and a 14-entry
  [Environment and Scope Matrix](../docs/governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
  (Required 6 · Conditional 4 · Deferred 4).
- **Evidence Strategy** (AE-0…AE-4), **Maintenance Policy** (freshness + triggers +
  six-month max gap), **Defect and Regression Model**, and a non-normative
  **Evidence Record Template**.
- Research evidence: **source register** (13 URLs opened; 9 usable) and **selection
  rationale**.

Added DEC-S-065…072 and RISK-049…054; moved RISK-044 `Monitored → Mitigating`. **No
test executed; every artifact AE-0; no environment claimed as supported; pilot
inactive; publication state `Private Development`.** No Git write action was
performed.

Documents:
[Support Baseline](../docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md) ·
[Environment Matrix](../docs/governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md) ·
[Maintenance Policy](../docs/governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md) ·
[Evidence Strategy](../docs/governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md) ·
[Defect and Regression Model](../docs/governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md) ·
[Evidence Record Template](../docs/operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md) ·
[Source Register](../docs/research/ACCESSIBILITY_BASELINE_SOURCE_REGISTER.md) ·
[Selection Rationale](../docs/research/ACCESSIBILITY_BASELINE_SELECTION_RATIONALE.md)

### CDS-WP-011 — Machine-Readable Source and Token Format Decision — Completed

Decided the normative machine-readable source format using authorized official
research, without implementing anything:

- **DTCG 2025.10** (Format, Color, Resolver) as the external basis — a **Final
  Community Group Report, not a W3C Standard**; only the pinned stable version is
  authoritative, previews are inputs only ([ADR-0001](../docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)).
- **Strict JSON `.tokens.json`**; YAML/JSONC/JSON5/tool/CSS/generated forms are not
  normative sources.
- **JSON Schema 2020-12** as the future CDS-owned profile-schema foundation (no schema
  created; a schema pass is not full correctness).
- **CDS Token Format Profile** over DTCG with an `io.github.kaykaspers.cds`
  `$extensions` namespace (foreign extensions preserved, not automatically normative);
  reserved DTCG semantics never redefined.
- **Four source-set layers** (Reference/Semantic/Component/Product Profile); channel
  outputs are generated, non-normative; fail-closed references/resolution; a
  machine-validatable naming profile; versioned, non-`latest` provenance identity;
  **four validation layers** (V1 Syntax · V2 DTCG · V3 CDS Profile · V4 Semantic/
  Governance).

Added DEC-S-073…082 and RISK-055…063; created ADR-0001. **No token value, schema,
resolver, validator, or design value; no Candidate/Stable; pilot inactive; publication
state `Private Development`.** No Git write action was performed.

Documents:
[ADR-0001](../docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) ·
[Machine-Readable Source Model](../docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md) ·
[CDS Token Format Profile](../docs/architecture/CDS_TOKEN_FORMAT_PROFILE.md) ·
[Reference, Resolution and Validation Model](../docs/architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md) ·
[Metadata, Provenance and Identity Model](../docs/architecture/TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md) ·
[Evaluation](../docs/research/TOKEN_FORMAT_EVALUATION.md) ·
[Source Register](../docs/research/TOKEN_FORMAT_SOURCE_REGISTER.md) ·
[Implementation Plan](../docs/roadmap/MACHINE_READABLE_SOURCE_IMPLEMENTATION_PLAN.md)

### CDS-WP-012 — Machine-Readable Source Bootstrap and Validation Contract — Completed

Implemented the value-neutral machine-readable bootstrap without any design value or
productive validator:

- **Four CDS-owned JSON Schema 2020-12 contracts** (token document, source-set manifest,
  resolver document, validation case) with stable `tag:` `$id`s, local `$ref`, offline.
- **`io.github.kaykaspers.cds` extension payload** requiring `profileVersion` and
  source-set identity; foreign extensions preserved, not automatically normative.
- **6 synthetic positive + 9 synthetic negative fixtures** (testOnly / nonNormative;
  `fixture/` IDs); a **15-case validation-case matrix** binding every fixture to expected
  V1–V4 outcomes.
- An explicit **V1–V4 Validation Contract** (duplicate-key fails V1; no aggregate score;
  a schema pass proves no higher layer) and the **RFC 8785 (JCS) + SHA-256** deterministic
  serialization decision (**ADR-0002**).

Added DEC-S-083…092 and RISK-064…072; created ADR-0002. **No real token/design value, no
productive validator/canonicalizer/transformer/build; formal schema execution `Not
assessed` (no local validator available, none installed); Experimental, not Candidate;
publication `Private Development`.** No Git write action was performed.

Documents:
[Validation Contract](../docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md) ·
[Serialization/Digest Model](../docs/architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md) ·
[ADR-0002](../docs/decisions/ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md) ·
[Validation Cases](../tests/fixtures/machine-readable/VALIDATION_CASES.json)

## Next work package — CDS-WP-013 (authorized)

The value-neutral bootstrap is defined (Experimental; not executed by a validator). The
next authorized work package is:

**CDS-WP-013 — Offline Token Profile Validator and Fixture Harness.**

### Objective of CDS-WP-013

- an **offline validator architecture**;
- **JSON parsing with duplicate-key detection**;
- **V1 validation**; the **V2 DTCG validation boundary**; **V3 CDS schema and profile
  validation**; the **V4 governance hook contract**;
- a **fixture harness** executing the validation cases;
- **RFC 8785 canonicalization** and **SHA-256 digest generation**;
- **machine-readable validation results**;
- an **independent evidence-review boundary**.

### CDS-WP-013 explicitly establishes none of the following

- no design values; no Candidate or Stable artifact; no component work; no CoreOps pilot
  start; no licence; no publication.

### Still prohibited in the Pre-Candidate phase

- concrete visual design; selecting colours, typography, icons, logos, or themes,
- creating real token values or names,
- implementing components or product code,
- executing accessibility tests or asserting accessibility evidence (every artifact
  is AE-0),
- selecting a licence or approving publication,
- claiming conformance, accessibility, adoption, or certification,
- promoting any artifact to Candidate or Stable,
- starting the CoreOps pilot,
- modifying Skill files or consumer repositories,
- creating a new work-package ID beyond CDS-WP-013 without Human-Maintainer
  approval.

### Authorization note

CDS-WP-013 is registered as `Next`; its execution requires an explicit work-package
prompt from Nova and Human-Maintainer authorization. Registration is not execution.

## Related documents

- [Work Packages](WORK_PACKAGES.md)
- [Project Profile](PROJECT_PROFILE.md)
- [Foundation Context Pack](CONTEXT_PACK_FOUNDATION.md)
- [Governance Operating Model](../docs/governance/GOVERNANCE_OPERATING_MODEL.md)
