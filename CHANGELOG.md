# Changelog

All notable changes to the Core Design System project will be documented here.

The format will be refined before the first CDS release. No version has been
released and no release is announced.

## Unreleased

### Added

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
