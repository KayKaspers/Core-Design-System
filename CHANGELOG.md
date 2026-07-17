# Changelog

All notable changes to the Core Design System project will be documented here.

The format will be refined before the first CDS release. No version has been
released and no release is announced.

## Unreleased

### Added

- Offline token profile validator implemented (CDS-WP-013): entry point
  `python -m tools.cds_validator` with `version`, `validate-file`, `validate-cases`,
  and `digest` commands and a stable exit-code contract; Python 3.11+ with exactly
  pinned `jsonschema==4.26.0` and `rfc8785==0.1.4` (`requirements-validator.lock`);
  no runtime network access. (CDS-WP-013)
- Single duplicate-key-rejecting JSON loader and a local five-schema registry
  implemented; unknown or network schema resolution fails closed. (CDS-WP-013)
- CDS validation-result schema created
  (`schemas/cds-validation-result.schema.json`) binding runtime, dependency, schema,
  case, source-revision, digest, and review-state identities; no numeric score.
  (CDS-WP-013)
- Layered V1–V4 validation executed against all fixtures: the fixture harness ran
  **15/15 validation cases with 15/15 expected/actual matches** (71/71 unit tests);
  machine-readable evidence recorded in `artifacts/validation/` and reviewed in the
  Offline Token Validator Execution Review — executor-produced, independently
  unreviewed. (CDS-WP-013)
- RFC 8785 + SHA-256 content digests computed for the 14 V1-parsable fixtures; the
  duplicate-key fixture received no digest. (CDS-WP-013)
- ADR-0003 created (Offline Token Validator Implementation Stack); dependency
  provenance recorded in the Offline Validator Dependency Source Register and Stack
  Evaluation; validator architecture and usage documented. (CDS-WP-013)
- DEC-S-093 … DEC-S-104 added (validator stack, CLI contract, controlled loader,
  local registry, layered states, bounded DTCG coverage, graph enforcement, digest
  boundary, result contract, harness semantics, evidence class, Candidate gate).
  (CDS-WP-013)
- RISK-073 … RISK-081 added; RISK-066, RISK-067, RISK-068, RISK-069, and RISK-071
  moved `Monitored → Mitigating` on executed harness evidence (executor-produced,
  independently unreviewed); no risk accepted or closed. (CDS-WP-013)
- CDS-WP-014 — Semantic Status Foundation Contract and First Candidate Plan
  activated as the next work package. (CDS-WP-013)
- Four CDS-owned JSON Schema Draft 2020-12 contracts created (CDS-WP-012): token
  document, source-set manifest, resolver document, and validation case — each with a
  stable `tag:` `$id`, same-document local `$ref`, and no remote dependency
  (`schemas/`). (CDS-WP-012)
- CDS extension payload contract implemented under `io.github.kaykaspers.cds`
  (requiring `profileVersion` and source-set identity; foreign extensions preserved and
  not automatically normative). (CDS-WP-012)
- Source-Set Manifest schema and Resolver schema created — explicit local declaration of
  identity, layer, path, dependency graph, and ordered composition; no implicit or
  network-discovered sets. (CDS-WP-012)
- Validation Case schema created; a 15-case validation-case matrix
  (`tests/fixtures/machine-readable/VALIDATION_CASES.json`) binds every fixture to
  expected V1–V4 outcomes with contiguous `VAL-CASE-###` IDs. (CDS-WP-012)
- Six synthetic positive fixtures and nine synthetic negative fixtures created (test-only,
  non-normative; `fixture/` IDs). (CDS-WP-012)
- V1–V4 Validation Contract created; the duplicate-key policy operationalized (duplicate
  object member names fail V1; no first/last-key-wins repair; a duplicate-key-aware parser
  is required). (CDS-WP-012)
- RFC 8785 (JSON Canonicalization Scheme) and SHA-256 digest model decided
  ([Deterministic Serialization and Digest Model](docs/architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md));
  a content digest is an integrity aid, not authenticity, and no canonicalizer is
  implemented. (CDS-WP-012)
- **ADR-0002 — Deterministic JSON Serialization** created (the second ADR; accepted upon
  Human-Maintainer commit following Nova approval). (CDS-WP-012)
- Work-package evidence notes for CDS-WP-012. (CDS-WP-012)
- Machine-readable source model defined (CDS-WP-011): the normative machine-readable
  CDS source (artifact class 2) with eight source-set classes, a strictly downward
  dependency model, and the boundary to generated artifacts and human-readable sources
  ([Machine-Readable Source Model](docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md)).
  (CDS-WP-011)
- **DTCG 2025.10 selected** as the external normative format basis (Format, Color,
  Resolver modules) — a Final Community Group Report, **not** a W3C Standard; only the
  pinned stable version is authoritative, previews are inputs only. Chosen from a
  seven-option evaluation using authorized official research (13 DTCG/W3C/RFC/
  JSON-Schema URLs). (CDS-WP-011)
- CDS Token Format Profile defined over DTCG with an `io.github.kaykaspers.cds`
  `$extensions` namespace (a collision-resistant, repository-identity-derived reserved
  root; foreign extensions preserved, not automatically normative), a
  machine-validatable naming/identifier profile, and Product-Profile bounds
  ([CDS Token Format Profile](docs/architecture/CDS_TOKEN_FORMAT_PROFILE.md)).
  (CDS-WP-011)
- **Strict JSON (RFC 8259) and `.tokens.json`** selected as the normative source form;
  YAML/JSONC/JSON5/tool-native/CSS/generated forms are not normative sources.
  (CDS-WP-011)
- **JSON Schema 2020-12** selected as the foundation for a future CDS-owned profile
  validator (no schema created; a schema pass is not full correctness). (CDS-WP-011)
- Token reference, resolution, and validation model defined: curly-brace
  `{group.token}` for canonical token-to-token references and DTCG `$ref` / RFC 6901
  JSON Pointer for document/property/resolver/source-set and controlled cross-file
  references; the resolver relationship; fail-closed cycle/dangling/type/layer/
  missing-set/undeclared-cross-file handling; and **four validation layers** (V1 Syntax
  · V2 DTCG · V3 CDS Profile · V4 Semantic/Governance)
  ([model](docs/architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)).
  (CDS-WP-011)
- Token metadata, provenance, and identity model defined: source-set identity,
  governance metadata, versioned non-`latest` provenance, and an open
  canonicalization decision state (RFC 8785 evaluated, not selected)
  ([model](docs/architecture/TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md)).
  (CDS-WP-011)
- **ADR-0001 — Machine-Readable Token Source Format** created (the first ADR; accepted
  upon Human-Maintainer commit following Nova approval)
  ([ADR-0001](docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)).
  (CDS-WP-011)
- Token format source register and evaluation created (non-normative research
  evidence); machine-readable source implementation plan created (roadmap for
  CDS-WP-012). (CDS-WP-011)
- Work-package evidence notes for CDS-WP-011. (CDS-WP-011)
- Initial accessibility support baseline defined (CDS-WP-010): **A11Y-BL-001**
  ([Accessibility Support Baseline](docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md)),
  pending Human-Maintainer commit — a **test contract, not evidence**; it declares
  the environments future evidence will target and asserts no support and no
  conformance. Composed from authorized official standards/vendor research only
  (13 URLs opened, 9 usable). (CDS-WP-010)
- Three-tier baseline model created — Required Core, Complementary, Scope-triggered
  (DEC-S-066). (CDS-WP-010)
- Accessibility environment and scope matrix created — 14 entries
  (A11Y-ENV-001…014): Required 6, Conditional 4, Deferred 4; 2 Required
  browser/screen-reader pairings. (CDS-WP-010)
- Accessibility evidence strategy created — operationalizes AE-0…AE-4, required
  evidence by maturity, manual/AT/consumer/pilot strategy, review independence, and
  a capacity-aware execution rule; **no evidence executed**. (CDS-WP-010)
- Accessibility evidence record template created — a non-normative operational form
  binding exact environment identity; **not evidence**. (CDS-WP-010)
- Accessibility baseline maintenance policy created — five freshness states, nine
  review triggers, and a six-month maximum review gap; no automatic claim renewal.
  (CDS-WP-010)
- Accessibility defect and regression model created — four impact levels, six defect
  statuses, and the rule that Blocking/High regressions block Stable and claims for
  the affected scope; **no defect registered (AE-0)**. (CDS-WP-010)
- Accessibility baseline source register and selection rationale created
  (non-normative research evidence), recording every opened official URL and the
  capacity-aware selection with its coverage gaps. (CDS-WP-010)
- Work-package evidence notes for CDS-WP-010. (CDS-WP-010)
- Foundation closure recorded (CDS-WP-009): the
  [Foundation Closure Record](docs/governance/FOUNDATION_CLOSURE_RECORD.md)
  registers the Foundation / Pre-Design milestone as **Closed with Notes** after
  CDS-WP-008, Nova review, and Human-Maintainer acceptance (commit of CDS-WP-008 +
  initiation of CDS-WP-009). It is normative for the fact of closure, the authority
  state, and the phase boundary; it grants no Candidate, Stable, claim, licence, or
  publication status. (CDS-WP-009)
- Pre-Candidate Operating Enablement phase activated; the
  [Pre-Candidate Operating Plan](docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md)
  records the phase entry state, prerequisites, Candidate entry conditions, and
  exit criteria. (CDS-WP-009)
- Foundation Operating Playbook created — a **non-normative** operational view that
  makes the committed governance runnable (intake and classification, Standard and
  Elevated tracks, stop conditions, decision/risk/evidence checks, approval gates,
  post-commit reconciliation, and the lean operating rule). (CDS-WP-009)
- Standard and Elevated change-dossier templates created — non-normative,
  reference-oriented per-change records (19 Standard fields; 36 Elevated fields,
  scalable via `Not applicable with rationale`). (CDS-WP-009)
- Critical Risk Action Register created — the twelve Critical Risks (RISK-017,
  020, 021, 023, 026, 028, 029, 031, 038, 040, 044, 048) each made actionable with
  a named Mitigation Executor role, review trigger, expected evidence, and blocking
  effect. (CDS-WP-009)
- Full repository reference-integrity review completed (CDS-WP-009): 112 text files
  in scope, 829 markdown links checked, **0 CDS-authored broken links**; the five
  broken links are confined to the vendored, pinned `.claude/skills/README.md` and
  are non-blocking; **PASS**. (CDS-WP-009)
- Work-package evidence notes for CDS-WP-009. (CDS-WP-009)
- Foundation Milestone Review completed (CDS-WP-008): a close-out review of the
  Foundation / Pre-Design phase across twelve dimensions, three governance dry
  runs, four-axis Candidate readiness, an eight-criterion CoreOps pilot entry
  matrix, and all 48 risks. Review evidence only — normative, no source changed.
  (CDS-WP-008)
- Foundation completeness matrix: 55 criteria (44 Met · 4 Met-with-notes · 3
  Partially met · 4 Not met), **0 Foundation blockers**. (CDS-WP-008)
- Governance affordability and operating-readiness review with three dry runs
  (Editorial → Operational; Additive Candidate → Operational with simplification
  notes; Elevated/accessibility → High burden). (CDS-WP-008)
- Foundation Candidate and CoreOps pilot entry readiness assessed; pilot remains
  inactive and no conformance is demonstrated; no artifact promoted. (CDS-WP-008)
- Open gaps and dependencies classified as twelve review findings
  (FM-F-001 … FM-F-012); none is a Foundation blocker. (CDS-WP-008)
- Next-phase recommendation created (advisory; no phase activated, no work-package
  ID assigned). (CDS-WP-008)
- Work-package evidence notes for CDS-WP-008. (CDS-WP-008)

### Changed

- Decision index extended to DEC-S-001 … DEC-S-092 with a tenth decision type for
  machine-readable bootstrap and validation decisions (DEC-S-083 … DEC-S-092);
  DEC-S-001 … DEC-S-082 unchanged. **ADR range is now ADR-0001 … ADR-0002 (2 ADRs).**
  (CDS-WP-012)
- Risk register extended to RISK-001 … RISK-072: added **RISK-064 … RISK-072** (CDS schema
  contract incompleteness, synthetic fixtures mistaken for design tokens, schema/validator
  divergence, canonicalization/digest mismatch, duplicate-key ambiguity, manifest/resolver
  graph inconsistency, validation fixture coverage gap, validation expectation drift,
  digest mistaken for authenticity), all `Monitored`; no existing risk changed; no risk
  accepted or closed. RISK-040 and RISK-044 remain `Mitigating`. (CDS-WP-012)
- Work-package status advanced: CDS-WP-012 completed; **CDS-WP-013 — Offline Token Profile
  Validator and Fixture Harness** activated as the next work package (not yet executed).
  Foundation Context Pack, project profile, project brain, README, work packages, next
  phase, implementation plan, and Claude working instructions updated. Publication state
  remains `Private Development`; no real token/design value; no productive validator or
  canonicalizer; formal schema execution not assessed; the bootstrap is Experimental, not
  Candidate; pilot inactive. (CDS-WP-012)
- Decision index extended to DEC-S-001 … DEC-S-082 with a ninth decision type for
  machine-readable source and token format decisions (DEC-S-073 … DEC-S-082);
  DEC-S-001 … DEC-S-072 unchanged. **ADR-0001 is the first ADR**; the decision-record
  format note now covers ADR files. (CDS-WP-011)
- Risk register extended to RISK-001 … RISK-063: added **RISK-055 … RISK-063** (token
  specification version drift, preview contamination, profile divergence,
  schema-validation false assurance, reference-resolution failure, cross-layer
  dependency violation, token identifier collision, provenance incompleteness,
  transformation-tool lock-in), all `Monitored`; no existing risk changed; no risk
  accepted or closed. RISK-040 and RISK-044 remain `Mitigating`. (CDS-WP-011)
- Work-package status advanced: CDS-WP-011 completed; **CDS-WP-012 — Machine-Readable
  Source Bootstrap and Validation Contract** activated as the next work package (not
  yet executed). Foundation Context Pack, project profile, project brain, README, work
  packages, next phase, and Claude working instructions updated; "token format" removed
  from the intentionally-open-decisions list. Publication state remains `Private
  Development`; no token/schema/validator/design value; no Candidate/Stable; pilot
  inactive. (CDS-WP-011)
- Decision index extended to DEC-S-001 … DEC-S-072 with an eighth decision type for
  accessibility support baseline and evidence decisions (DEC-S-065 … DEC-S-072);
  DEC-S-001 … DEC-S-064 unchanged; no ADR. (CDS-WP-010)
- Risk register extended to RISK-001 … RISK-054: added **RISK-049 … RISK-054**
  (accessibility baseline representativeness, universal-support misreading,
  environment-availability mismatch, evidence-identity incompleteness,
  regression-coverage gap, defect normalization), all `Monitored`; moved **RISK-044
  `Monitored → Mitigating`** on the strength of the defined baseline; no existing
  risk description/likelihood/severity changed; no risk accepted or closed.
  (CDS-WP-010)
- Accessibility Evidence and Claims Model, CoreOps Pilot Accessibility Criterion, and
  Consumer Validation Plan reconciled to reference A11Y-BL-001 (product-family vs
  execution identity, freshness, regression, complete-process evidence, claim
  boundary); the AE-0…AE-4 meanings are unchanged. (CDS-WP-010)
- Critical Risk Action Register updated: RISK-044 expected evidence delivered and set
  to `Mitigating`; RISK-048 capacity-aware tiering recorded as partial mitigation;
  RISK-040 first follow-evidence noted. RISK-049…054 not auto-added to the Critical
  group. (CDS-WP-010)
- Work-package status advanced: CDS-WP-010 completed; **CDS-WP-011 — Machine-Readable
  Source and Token Format Decision** activated as the next work package (not yet
  executed). Foundation Context Pack, project profile, project brain, README, work
  packages, next phase, Pre-Candidate Operating Plan, and Claude working instructions
  updated. Publication state remains `Private Development`; every artifact remains
  AE-0; no environment claimed supported; pilot inactive. (CDS-WP-010)
- Foundation status: **Closed with Notes** — the Human Maintainer accepted the
  `GO WITH NOTES` outcome; the Pre-Candidate Operating Enablement phase is active.
  No version, Candidate, Stable, claim, release, or publication status is asserted;
  publication state remains `Private Development`. (CDS-WP-009)
- Decision index extended to DEC-S-001 … DEC-S-064 with a seventh decision type for
  operating enablement and pre-candidate decisions (DEC-S-061 … DEC-S-064);
  DEC-S-001 … DEC-S-060 unchanged; no ADR. (CDS-WP-009)
- Risk register: **RISK-040 moved `Monitored → Mitigating`** on the strength of the
  Critical Risk Action Register (DEC-S-064) — the only risk status change; no
  description, likelihood, or severity changed; no risk accepted or closed; range
  remains RISK-001 … RISK-048 (48). (CDS-WP-009)
- Work-package status advanced: CDS-WP-009 completed; **CDS-WP-010 — Accessibility
  Support Baseline and Evidence Strategy** activated as the next work package (not
  yet executed). (CDS-WP-009)
- Foundation Context Pack, project profile, project brain, README, work packages,
  next phase, and Claude working instructions updated for Foundation closure,
  operating enablement, the non-normative operating views, the critical-risk action
  rule, and the CDS-WP-010 pointer. (CDS-WP-009)
- Recommended milestone outcome: **GO WITH NOTES** — Foundation closable with
  mandatory next-phase notes, pending Nova review and Human-Maintainer approval.
  (CDS-WP-008)
- Work-package status: CDS-WP-008 completed; **no next work package authorized**;
  next-phase roadmap pending decision. No new Decision or Risk IDs; no ADR; no new
  work-package ID. Publication state remains `Private Development`. (CDS-WP-008)

- Accessibility and inclusive-design policy defined as the normative
  accessibility source: purpose and authority, the target-versus-claim boundary,
  principles, shared responsibility, architecture integration, maturity
  relationship, inclusive-design scope, source hierarchy, and change control.
  (CDS-WP-007)
- **WCAG 2.2 Level AA** target defined for the applicable web-based scope,
  resolving CR-024 at policy level. A target, not a conformance claim. (CDS-WP-007)
- Accessibility responsibility model: CDS, consumer, and shared/contract-
  controlled responsibilities, a RACI-style matrix, the component-to-product and
  Product Profile boundaries, claim responsibility, and escalation. (CDS-WP-007)
- Accessibility requirements baseline across ten areas, separating normative,
  implementation-dependent, consumer-scope, channel-specific, and deferred
  requirements. (CDS-WP-007)
- WCAG 2.2 Level A and AA applicability matrix: 56 displayed rows — 31 current
  Level A, 24 Level AA, and 1 historical removed reference row (4.1.1, obsolete
  and removed by the standard) — for 55 currently applicable criteria, with
  per-criterion
  responsibility, policy status, architecture layers, and required evidence — no
  pass/fail statement. (CDS-WP-007)
- Five-level accessibility evidence model AE-0 … AE-4 with Candidate and Stable
  gates, a support-baseline process, the automated-only insufficiency rule, the
  component/product evidence boundaries, claim boundaries, and no numeric score.
  (CDS-WP-007)
- Six accessibility channel profiles, each with scope, target, owner, minimum
  future evidence, current gap, and Candidate/Stable boundaries; only web UI and
  web documentation carry a target; none is Candidate- or Stable-eligible.
  (CDS-WP-007)
- Accessibility limitation and exception policy: a fifteen-field limitation
  record, impact and mitigation rules, maturity and claim effects, the exception
  boundary and prohibited waivers, and the capacity-is-not-a-rationale rule.
  (CDS-WP-007)
- CoreOps pilot accessibility criterion operationalizing CR-024, with the entry
  criterion `Accessibility target defined` satisfiable on Human Maintainer commit,
  Pilot Group E minimum evidence, and confirmation that the pilot has not started.
  (CDS-WP-007)
- Accessibility source register (13 opened official W3C/WAI/ETSI URLs) and a
  standard-status and limitations record (WCAG 2.2, WAI-ARIA, APG, WCAG-EM 2.0
  draft, EN 301 549 on-approval), with no legal-advice statement. (CDS-WP-007)
- Accessibility architecture alignment mapping accessibility onto the eight
  layers, eight artifact classes, five token-flow levels, profiles, contracts,
  status axes, channels, evidence flow, and maturity gates. (CDS-WP-007)
- Accessibility and inclusive-design decisions DEC-S-049 … DEC-S-060. (CDS-WP-007)
- Risks RISK-041 … RISK-048 covering target-mistaken-for-conformance,
  automated-testing substitution, the component-to-product responsibility gap,
  accessibility support-baseline drift, accessibility regression, the non-web
  channel gap, inclusive-design undercoverage, and the accessibility evidence
  burden. (CDS-WP-007)
- Work-package evidence notes for CDS-WP-007.

### Changed

- CR-021, CR-022, CR-024, and CR-034 traceability reconciled: no requirement is
  deferred to a policy work package any longer; the architecture status
  distribution is 9 addressed, 27 partially addressed, 2 consumer-owned, 2 out of
  scope. CR-024 is addressed because the target and policy exist — not because
  anything was tested. (CDS-WP-007)
- Artifact maturity lifecycle, exception and Product Profile governance, adoption
  and claims policy, licensing and publication model, CoreOps pilot contract, and
  consumer validation plan reconciled to reference the accessibility policy and
  evidence model. No artifact was promoted; publication state remains
  `Private Development`. (CDS-WP-007)
- Work-package status advanced: CDS-WP-007 completed, CDS-WP-008 — Foundation
  Milestone Review activated as the next work package. (CDS-WP-007)
- Decision index extended to DEC-S-001 … DEC-S-060 with a sixth decision type for
  accessibility and inclusive design; DEC-S-001 … DEC-S-048 unchanged; no ADR.
  (CDS-WP-007)
- Risk register extended to RISK-001 … RISK-048; existing risks unchanged; the
  finalized four-role model applied. (CDS-WP-007)

- Governance operating model defined as the normative governance source: six
  roles, an authority matrix, Standard and Elevated tracks, approval gates,
  separation of review and approval, the consumer governance boundary, and
  escalation. (CDS-WP-006)
- Normative source conflict policy: neither source wins automatically, five
  conflict states, an eight-step fail-closed procedure, and prohibited automatic
  precedence rules. (CDS-WP-006)
- Seven-state artifact maturity lifecycle with entry and exit criteria, a full
  transition matrix, Candidate and Stable gates, and maturity kept separate from
  release version and publication state. (CDS-WP-006)
- Semantic versioning and compatibility policy: MAJOR.MINOR.PATCH, a pre-1.0
  policy, ten release identity elements, eight compatibility axes, and six
  permitted compatibility statements. (CDS-WP-006)
- Deprecation and removal policy with nine required deprecation fields and
  narrowly bounded emergency removal. (CDS-WP-006)
- Contribution and acceptance model: a ten-step flow, eleven required inputs,
  five outcomes, and prohibited shortcuts. (CDS-WP-006)
- Exception and Product Profile governance: thirteen exception fields, six
  exception statuses, twelve Product Profile elements, and an anti-fragmentation
  review. (CDS-WP-006)
- Adoption and conformance claims policy: four graded claim types, eight
  mandatory claim fields, eight re-assessment triggers, and a prohibited
  certification claim. (CDS-WP-006)
- Risk governance model finalizing the risk owner model across all risks:
  Accountable Risk Owner, Risk Controller, Mitigation Executor, and Evidence
  Reviewer, with five risk statuses and an anti-ceremonial rule. (CDS-WP-006)
- Licensing and publication decision model: ten artifact classes with an
  eleven-field rights matrix, five publication states, and a fifteen-point
  publication gate. (CDS-WP-006)
- Release and change control policy: twelve release candidate requirements, six
  change classes, and release authority reserved to the Human Maintainer.
  (CDS-WP-006)
- Governance, lifecycle and publication decisions DEC-S-033 … DEC-S-048.
  (CDS-WP-006)
- Risks RISK-029 … RISK-040 covering governance bottleneck, role ambiguity,
  maturity inflation, compatibility ambiguity, deprecation without migration,
  contribution gate bypass, exception debt, Product Profile governance bypass,
  misleading claims, licensing fragmentation, premature publication, and
  ceremonial risk governance. (CDS-WP-006)
- Work-package evidence notes for CDS-WP-006.
- Logical design-system architecture defined as the normative architecture
  source, with architecture objectives, quality attributes, allowed and
  prohibited dependency directions, and sixteen architecture invariants.
  (CDS-WP-005)
- Eight architecture layers registered: Strategy and Governance, Brand and
  Identity, Foundations and Tokens, Components, Patterns and Experiences,
  Channels and Communication, Distribution and Enablement, Evidence and Quality.
  (CDS-WP-005)
- Source-of-Truth and Authority Model with eight artifact classes, an authority
  matrix, nine conflict scenarios, and fail-closed behavior. (CDS-WP-005)
- Conceptual Token and Theme Architecture with five token layers, the
  semantic-first principle, alias and dependency direction, validation
  requirements, and prohibited shortcuts. No values, names, format, or tooling
  selected. (CDS-WP-005)
- Product Profile and Extension Model with Core Foundation, Product Profile,
  Consumer Extension, Domain Pattern Family, and Local Exception; permitted and
  forbidden override categories; anti-fragmentation rules; and the
  existing-product reconciliation flow. (CDS-WP-005)
- Artifact Distribution and Channel Model with logical artifact families, nine
  channel classes, transformation boundaries, offline and self-hosted
  requirements, provenance and pinning, and distribution neutrality.
  (CDS-WP-005)
- Consumer Contract and Reconciliation Model with the Source, Transformation,
  Distribution, Integration, and Adoption Evidence contracts, plus CDS
  obligations and the reconciliation flow. (CDS-WP-005)
- Evidence, Traceability and Status Semantics architecture with the traceability
  flow, required logical identities, deviation and feedback flows, five separated
  status axes, and the Unknown invariant. (CDS-WP-005)
- CR-001 … CR-040 mapped to the architecture with per-requirement layer,
  response, remaining decision, follow-up, and status. (CDS-WP-005)
- Logical architecture decisions DEC-S-021 … DEC-S-032. (CDS-WP-005)
- Risks RISK-020 … RISK-028 covering authority ambiguity, token proliferation,
  reconciliation failure, domain-pattern leakage, channel divergence, provenance
  loss, architecture overdesign, profile fragmentation, and deferred
  accessibility debt. (CDS-WP-005)
- Work-package evidence notes for CDS-WP-005.
- Consumer evidence registered from three consumer repositories analyzed
  read-only at committed revisions — CoreOps as primary pilot consumer,
  SpeakCore and CastCore as secondary evidence. 15 sources, 14 usable, each
  bound to a committed HEAD revision. (CDS-WP-004)
- Consumer requirements model registering CR-001 … CR-040 with classification,
  evidence status and strength, pilot priority, ownership boundary, and
  validation method. (CDS-WP-004)
- Consumer requirements traceability matrix mapping every requirement to its
  committed consumer source. (CDS-WP-004)
- CoreOps pilot scope and scenarios: five pilot groups (A–E) with nine
  scenarios, an explicit out-of-scope list, and open design questions.
  (CDS-WP-004)
- CoreOps pilot contract with purpose, parties, entry criteria, evidence
  requirements, exit criteria, success categories, and change control. Normative
  only upon Human Maintainer commit following Nova approval; not active.
  (CDS-WP-004)
- Consumer validation plan defining evidence levels, the deviation model, the
  exit review, and the explicit absence of any conformance promise.
  (CDS-WP-004)
- Consumer hypothesis validation layer assessing HYP-001 … HYP-008 against
  consumer evidence, leaving the CDS-WP-003 research assessments unchanged.
  (CDS-WP-004)
- Consumer and pilot scope decisions DEC-S-013 … DEC-S-020. (CDS-WP-004)
- Risks RISK-014 … RISK-019 covering consumer evidence staleness, pilot scope
  inflation, product-specific contamination, document evidence mistaken for user
  validation, pilot mistaken for adoption, and secondary consumer
  underrepresentation. (CDS-WP-004)
- Work-package evidence notes for CDS-WP-004.
- Official-source benchmark of ten established design systems against 14
  dimensions, reviewed on 2026-07-15. Findings are research evidence and are
  explicitly **non-normative**. (CDS-WP-003)
- Benchmark source register recording every official URL opened, with access
  date, evidence status, redirects, and access failures. (CDS-WP-003)
- Benchmark evidence matrix covering all ten systems across all 14 dimensions,
  using a fixed evidence-status vocabulary and no numeric scores or rankings.
  (CDS-WP-003)
- Assessment of the eight CDS differentiation hypotheses HYP-001 … HYP-008, each
  with supporting evidence, counterevidence, and an explicit uniqueness risk. No
  hypothesis reached "Strongly supported"; all remain research hypotheses.
  (CDS-WP-003)
- Research limitations documenting source, access, depth, language, version, and
  copyright boundaries, and the difference between public documentation and
  unknown internal practice. (CDS-WP-003)
- Risks RISK-010 … RISK-013 covering benchmark imitation, research and source
  bias, source volatility, and differentiation overstatement. (CDS-WP-003)
- Work-package evidence notes for CDS-WP-003.
- Registered concept and scope as the normative scope source: problem
  statement, mission, vision, strategic objectives, six capability domains,
  cross-cutting concerns, current Foundation scope separated from long-term
  scope, twelve binding non-goals, ownership boundaries, CoreOps pilot
  boundary, assumptions, and deferred decisions. (CDS-WP-002)
- Consumer and Stakeholder Model with direct users, indirect beneficiaries,
  stakeholder roles, three consumer relationship classes, channel-consumer
  categories, and the limits of the classification. (CDS-WP-002)
- Scope Boundary Matrix registering the per-area split between CDS
  responsibility, consumer responsibility, and shared or contract-controlled
  responsibility. (CDS-WP-002)
- Foundation Context Pack as a compact, explicitly non-normative continuation
  summary. (CDS-WP-002)
- Strategic scope decisions DEC-S-007 … DEC-S-012. (CDS-WP-002)
- Risks RISK-006 … RISK-009. (CDS-WP-002)
- Work-package evidence notes for CDS-WP-002.
- Verified local adoption of the 38 docs-only NDF v1.0.0 Claude Skills under
  `.claude/skills/`, extracted byte-identically from the released NDF v1.0.0
  tag (commit `9dcadc12fb960914b9a5baeff2ab1aee75912b57`). Upstream contents
  unmodified. (CDS-WP-001A)
- NDF Skills provenance documentation recording source, tag, commit,
  verification method, verification result, and the update rule. (CDS-WP-001A)
- Machine-readable SHA-256 hash manifest of every adopted Skill file.
  (CDS-WP-001A)
- NDF Skills inventory covering all 38 Skills. (CDS-WP-001A)
- Work-package evidence notes for CDS-WP-001A.
- Project charter defining mission, vision, strategic purpose, scope
  categories, current phase boundary, non-goals, pilot relationship, and
  authority model. (CDS-WP-001)
- Decision index with the strategic foundation decisions DEC-S-001 …
  DEC-S-006. (CDS-WP-001)
- Risk register with the initial risks RISK-001 … RISK-005. (CDS-WP-001)
- Initial controlled work-package roadmap CDS-WP-001 … CDS-WP-008.
  (CDS-WP-001)
- Work-package evidence notes for CDS-WP-001.

### Changed

- Work-package status advanced: CDS-WP-006 completed, CDS-WP-007 activated as
  the next work package. (CDS-WP-006)
- Decision index extended to DEC-S-001 … DEC-S-048 with a fifth decision type for
  governance, lifecycle and publication. DEC-S-001 … DEC-S-032 unchanged.
  (CDS-WP-006)
- Risk register extended to RISK-001 … RISK-040. **The provisional owner model
  was replaced by the finalized four-role model across all existing risks**; no
  existing description, assessment, or status was changed. (CDS-WP-006)
- Foundation Context Pack, project profile, project brain, and README extended
  with the governance roles, tracks, maturity states, claim types, risk
  ownership, publication state, and licensing model. (CDS-WP-006)
- Claude working instructions extended with the governance entry point, the
  Standard and Elevated track rule, the source conflict rule, claim and release
  boundaries, and the finalized risk roles. (CDS-WP-006)
- Work-package status advanced: CDS-WP-005 completed, CDS-WP-006 activated as
  the next work package. (CDS-WP-005)
- Decision index extended to DEC-S-001 … DEC-S-032 with a fourth decision type
  for logical architecture. DEC-S-001 … DEC-S-020 unchanged. (CDS-WP-005)
- Risk register extended to RISK-001 … RISK-028. The provisional owner model is
  unchanged. (CDS-WP-005)
- Foundation Context Pack, project profile, project brain, and README extended
  with the architecture layers, authority model, token flow, status invariants,
  and requirement coverage. (CDS-WP-005)
- Claude working instructions extended with the architecture entry point and a
  binding authority and conflict rule. (CDS-WP-005)
- Work-package status advanced: CDS-WP-004 completed, CDS-WP-005 activated as
  the next work package. (CDS-WP-004)
- Decision index extended to DEC-S-001 … DEC-S-020 with a third decision type
  for consumer and pilot scope. DEC-S-001 … DEC-S-012 unchanged. (CDS-WP-004)
- Risk register extended to RISK-001 … RISK-019. The provisional owner model is
  unchanged. (CDS-WP-004)
- Foundation Context Pack, project profile, project brain, and README extended
  with consumer evidence sources, requirement counts, pilot groups, and the
  hypothesis consumer layer. (CDS-WP-004)
- Claude working instructions extended with a binding consumer-repository
  read-only rule and the committed-evidence requirement. (CDS-WP-004)
- Work-package status advanced: CDS-WP-003 completed, CDS-WP-004 activated as
  the next work package. (CDS-WP-003)
- Risk register extended to RISK-001 … RISK-013. The provisional owner model is
  unchanged. (CDS-WP-003)
- Foundation Context Pack, project profile, project brain, and README extended
  with the benchmark scope, hypotheses, and the non-normative status of
  research. (CDS-WP-003)
- Claude working instructions note that `docs/research/` is evidence rather than
  a normative source. (CDS-WP-003)
- Project charter consolidated with the registered scope: capability domains,
  consumer classes, pilot boundary, and Foundation status; it now references
  the normative scope source instead of carrying its own scope list.
  (CDS-WP-002)
- Decision index extended to DEC-S-001 … DEC-S-012 and now distinguishes
  strategic foundation decisions from strategic scope decisions.
  DEC-S-001 … DEC-S-006 unchanged. (CDS-WP-002)
- Risk register extended to RISK-001 … RISK-009 with an explicit note that the
  risk owner model is provisional until CDS-WP-006. RISK-002 gained a
  cross-reference to the CoreOps pilot boundary without changing its meaning.
  (CDS-WP-002)
- Work-package status advanced: CDS-WP-002 completed, CDS-WP-003 next.
  (CDS-WP-002)
- README, project profile, project brain, and next-phase definition updated
  with the registered scope, consumer classes, register ranges, and the
  CDS-WP-003 boundaries. (CDS-WP-002)
- Claude working instructions updated with the context-pack and normative scope
  references and the current work-package pointers. (CDS-WP-002)
- Skills-first operating mode activated in the Claude working instructions,
  including selection, context-economy, authority-boundary, fail-closed, and
  Skill-maintenance rules. (CDS-WP-001A)
- Work-package status advanced: CDS-WP-001 and CDS-WP-001A completed,
  CDS-WP-002 next. (CDS-WP-001A)
- Project profile extended with NDF Skills version, count, status, source
  commit, and Skills-first operating mode. (CDS-WP-001A)
- README and project brain extended with the Skills-first operating mode and
  links to provenance and inventory. (CDS-WP-001A)
- Project profile extended with work-package status, register scope, and the
  intentionally open decision areas. (CDS-WP-001)
- Project brain restructured as a compact long-term orientation document.
  (CDS-WP-001)
- README updated with project status, pilot role, operating model, registers,
  and governance links. (CDS-WP-001)
- Claude working instructions rewritten for Claude Desktop with a locally
  connected repository. (CDS-WP-001)

### Removed

- `.claude/skills/.gitkeep` placeholder, superseded by the verified Skills
  adoption. (CDS-WP-001A)
