# CDS-WP-012 — Machine-Readable Source Bootstrap and Validation Contract — Work Package Notes

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-012 — Machine-Readable Source Bootstrap and Validation Contract
- **Date:** 2026-07-17
- **Status:** Work-package evidence — **non-normative**.

## Assignment

Implement the value-neutral machine-readable bootstrap of the CDS Token Format Profile:
CDS-owned JSON Schema 2020-12 contracts, the extension payload contract, source-set
manifest and resolver contracts, an explicit V1–V4 validation contract, synthetic positive
and negative fixtures, a machine-readable validation-case matrix, the deterministic
canonicalization/digest decision, and ADR-0002 — with no real design values, no productive
validator, no build, and no Candidate.

## Preflight

- Root `D:/Projects/Core-Design-System`; branch `main`; working tree clean; no merge/rebase;
  `origin` correct. Last commit `a81772c` (CDS-WP-011).
- Foundation Closed with Notes; Phase Pre-Candidate Operating Enablement.
- Registers re-derived: Decisions 82 (DEC-S-001…082); Risks 63 (61 Monitored, RISK-040 +
  RISK-044 Mitigating); Requirements 40; ADRs 1 (ADR-0001); namespace consistent
  (`io.github.kaykaspers.cds`); token flow (5) and validation layers (V1–V4) confirmed;
  Skills 39 files / manifest 38·39. Publication `Private Development`; no Candidate/Stable;
  no claim; pilot inactive; no pre-existing schemas/tests. Fail-closed conditions: none
  triggered.

## Skills used (10, only the authorized set)

ndf-work-package-runner (frame) · ndf-architecture-blueprint-runner (schema/contract
blueprint) · ndf-implementation-review-runner (structural review of schemas/fixtures) ·
ndf-adr-governance-review (ADR-0002 number derived, not invented) ·
ndf-validation-evidence-reviewer (honest schema-execution status; schema-not-correctness) ·
ndf-existing-project-analysis-runner (structured bootstrap layout) ·
ndf-feature-scope-runner (scope/non-goals) · ndf-release-safety (no release/claim; NO-GO on
unclear readiness) · ndf-context-pack-maintainer (Context Pack) ·
ndf-compact-context-summary-runner (closing blocks). No other skill was used.

## Schema identity

Four schemas, all JSON Schema Draft 2020-12, strict JSON, UTF-8, offline, with the pinned
`tag:` `$id`s and same-document `#/$defs` `$ref` (41 refs, all same-document; 0 remote):
`cds-token-document/1`, `cds-source-set-manifest/1`, `cds-resolver-document/1`,
`cds-validation-case/1`.

## Extension payload

`$extensions.io.github.kaykaspers.cds` — required `profileVersion` (`1`) and source-set
identity (sourceSetId, layer, dtcgReportVersion `2025.10`, sourceRevision); optional
governance metadata and fixture flags (`testOnly`, `nonNormative`); unknown CDS payload
fields fail closed (additionalProperties false); foreign `$extensions` preserved
(additionalProperties true), not automatically normative; no secrets/personal data.

## Source-Set manifest

`.source-set.json` (CDS-owned extension) requiring manifest identity, versions, revision,
maturity/approval, ownerRole, sourceSets, an explicit dependency graph consistent with
per-entry dependencies, resolver documents, product-profile boundary, provenance state, and
digest state (`Not computed – validator implementation pending`). Local paths only (no
network/UNC).

## Resolver contract

`.resolver.json` requiring resolver identity, versions, revision, `localOnly` = true, an
ordered source-set list using local `$ref` + RFC 6901 JSON Pointer, optional modifiers, and
a generated (non-normative) output-identity placeholder. No network resolution.

## V1–V4

V1 Syntax/File (strict JSON, duplicate-key, file identity, valid `$ref`/pointer, no network
refs) · V2 DTCG 2025.10 (groups/tokens/types/references/color/resolver, no preview) · V3 CDS
Profile (schemas, namespace, naming, layer, manifest agreement, dependencies, product-profile
bounds, local cross-file binding) · V4 Semantic/Governance (layer direction, status truth,
a11y relevance, traceability, provenance, maturity, approval, approved overrides). A lower
pass proves no higher pass; blocked/unexecuted layers stay `Not assessed`; no aggregate
score; a tool result is not approval.

## Positive fixtures (6)

reference-set, semantic-set, component-set, product-profile-set (`.tokens.json`);
source-set-manifest (`.source-set.json`); resolver (`.resolver.json`). All `testOnly:true`,
`nonNormative:true`, `fixture/` IDs, neutral placeholder values (no design values). The
component references semantic (not reference directly); the product profile overrides only
an approved test extension point.

## Negative fixtures (9)

duplicate-key, dangling-reference, circular-reference-a, circular-reference-b, type-mismatch,
undeclared-cross-file-reference, invalid-extension, preview-feature (`.tokens.json`);
backward-layer-dependency (`.source-set.json`). Each has one primary intended failure.

## Validation cases

15 cases `VAL-CASE-001…015` (contiguous, unique). Positive cases 001–007 (007 integrates all
six positive fixtures); negative cases 008–015. Every fixture is assigned to ≥1 case; no case
points to a missing file; expected V1–V4 declared per case; primary failure reasons,
blocking layers, diagnostic categories, and applicable Decision/Risk IDs recorded; no numeric
score.

## Duplicate-key check

Prohibited; fails V1; encoded in `duplicate-key.tokens.json`. A temporary non-committed node
script with a duplicate-key-aware parser confirmed the duplicate is detected only in that
fixture and in no positive fixture.

## Schema execution status

**Not assessed.** No standards-conformant JSON Schema 2020-12 validator (e.g. ajv) was
available locally, and none was installed (prohibited). Structural checks (strict parse,
duplicate-key detection, schema-ID and same-document `$ref` integrity, case coverage and
contiguity, source-set-ID syntax, manifest dependency/graph consistency) were run via a
temporary, non-committed, read-only node script and **passed with 0 errors**. Formal schema
execution against the fixtures and the validation-case run are **CDS-WP-013**; no schema pass
is invented (DEC-S-092).

## Deterministic serialization

RFC 8785 (JCS) + SHA-256, lowercase hex, `sha256:` prefix (ADR-0002, DEC-S-090). Authoring
formatting is separate from canonicalization; the digest is an integrity aid, not
authenticity (RISK-072), and never replaces revision/approval/provenance. No canonicalizer
implemented; digests `Not computed`.

## ADR-0002

Second ADR; "Deterministic JSON Serialization"; status "Accepted upon Human-Maintainer commit
following Nova approval"; alternatives (raw bytes, ad-hoc sorted, RFC 8785, tool-specific, no
digest); decision RFC 8785 + SHA-256; authoring/canonicalization boundary; identity model;
security/authenticity boundary; determinism/offline; implementation deferral (CDS-WP-013);
risks; authority boundary.

## New decisions

DEC-S-083…092 (bootstrap-is-not-conformance; extension payload; manifest declaration;
resolver declaration; synthetic fixtures; duplicate-key prohibition; bound validation cases;
RFC 8785 + SHA-256; declared-graph cross-file references; Experimental-until-executed). Range
DEC-S-001…092 (92); DEC-S-001…082 unchanged; ADRs 2.

## New risks

RISK-064…072 (schema incompleteness; fixtures mistaken for tokens; schema/validator
divergence; canonicalization/digest mismatch; duplicate-key ambiguity; manifest/resolver
inconsistency; fixture coverage gap; expectation drift; digest mistaken for authenticity),
all Monitored. Range RISK-001…072 (72): 70 Monitored, 2 Mitigating (RISK-040, RISK-044). No
existing status changed; no acceptance/closure.

## Changed or created files

Created (24): 4 schemas (`schemas/*.schema.json`); 6 positive fixtures + 9 negative fixtures +
VALIDATION_CASES.json (`tests/fixtures/machine-readable/**`);
`docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md`;
`docs/architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md`;
`docs/decisions/ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md`; this notes file.
Changed (11): `docs/roadmap/MACHINE_READABLE_SOURCE_IMPLEMENTATION_PLAN.md`,
`docs/decisions/DECISION_INDEX.md`, `docs/risks/RISK_REGISTER.md`,
`project-system/CONTEXT_PACK_FOUNDATION.md`, `PROJECT_PROFILE.md`, `NEXT_PHASE.md`,
`WORK_PACKAGES.md`, `project-brain/PROJECT_BRAIN.md`, `README.md`, `CLAUDE.md`, `CHANGELOG.md`.

## Quantitative validation

See the Report to Nova (§13). Key figures: 4 schemas · 4 schema IDs · 41 same-document $refs
(0 remote) · ~11 extension-payload fields · 6 positive + 9 negative fixtures · 15 validation
cases · 0 unassigned fixtures · 0 missing paths · 4 source sets · 4 dependency edges · 4
validation layers · 6 result states · 92 decisions · 2 ADRs · 72 risks (70/2) · 13 work-package
IDs · 10 skills.

## Deviations

None from the prompt. All work in the 35 Allowed Files. No real design value, productive
validator, canonicalizer, transformer, build, or tool decision. No dependency installed. No
Git write. Temporary validation script used outside the repository and not committed.

## Open validator questions

- Validator engine/tool selection under offline + tool-neutrality constraints (CDS-WP-013).
- Duplicate-key-aware parser choice; JSON Pointer/`$ref` resolution engine.
- RFC 8785 canonicalizer implementation and digest reproducibility evidence.
- Whether additional negative fixtures are needed for further failure classes (RISK-070).
- Evidence Reviewer role remains unstaffed (FM-F-006); must not be the executor (DEC-S-045).

## Completion status

**PASS.** All Definition-of-Done items met; only Allowed Files changed; no Git write action
performed.
