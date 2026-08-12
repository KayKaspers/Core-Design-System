# Machine-Readable Validation Contract

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-012 — Machine-Readable Source Bootstrap and Validation Contract
- **Date:** 2026-07-17
- **Status:** **Normative** for the CDS machine-readable validation contract,
  **pending Human-Maintainer commit** of CDS-WP-012 and ADR-0002. It defines what a
  future offline validator must check; it **implements no validator** and executes no
  validation. It operationalizes DEC-S-078 and the
  [Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md).

## Purpose

Turns the four-layer validation model into an explicit, machine-readable contract:
what each layer checks, what blocks, and how expected outcomes are recorded per
fixture. A future validator (CDS-WP-013) must satisfy this contract; the
[validation-case matrix](../../tests/fixtures/machine-readable/VALIDATION_CASES.json)
declares the expected outcomes for the synthetic fixtures.

## Artifacts this contract governs

- CDS token source documents (`.tokens.json`) — [schema](../../schemas/cds-token-document.schema.json)
- CDS Source-Set manifests (`.source-set.json`) — [schema](../../schemas/cds-source-set-manifest.schema.json)
- CDS Resolver documents (`.resolver.json`) — [schema](../../schemas/cds-resolver-document.schema.json)
- the validation-case matrix — [schema](../../schemas/cds-validation-case.schema.json)

Fixtures are **synthetic, test-only, non-normative** (DEC-S-087); they are never real
CDS design tokens or Product Profiles.

## V1 — Syntax and File Contract

Checks: UTF-8 encoding; strict JSON per RFC 8259; **duplicate object member names**
(prohibited — DEC-S-088); file extension and local file identity (`.tokens.json`,
`.source-set.json`, `.resolver.json`); syntactically valid `$ref` and RFC 6901 JSON
Pointer expressions; no forbidden network references (no `http(s):`/`file:`/UNC).

**Duplicate-key note:** JSON Schema alone cannot reliably detect duplicate keys; a
duplicate-key-aware parser is required (DEC-S-088). Duplicate-key input **fails V1**
and is never repaired via first-key-wins or last-key-wins.

## V2 — DTCG 2025.10 Contract

Checks (against the pinned DTCG 2025.10 Format, Color, and Resolver modules —
DEC-S-073, DEC-S-074): groups and tokens; `$value`/`$type`/`$description`/
`$extensions`; token types; token-to-token `{group.token}` reference resolution and
type compatibility; color token structure; resolver sets/modifiers/ordering
semantics; **no preview/draft features**. V2 applies to DTCG token and resolver
documents; it is **Not applicable with rationale** for a Source-Set manifest (a
CDS-owned, non-DTCG document).

## V3 — CDS Profile Contract

Checks (the CDS profile over DTCG): the CDS JSON Schemas; the
`io.github.kaykaspers.cds` extension namespace and required `profileVersion`
(DEC-S-084); source-set identity and the segment naming profile (DEC-S-081);
declared layer; manifest ↔ document identity agreement; the dependency graph;
Product-Profile bounds (approved extension points only); maturity and approval state;
and **local cross-file binding** — a reference must stay within the declared Manifest/
Resolver graph, to a known source-set identity, offline-resolvable (DEC-S-085,
DEC-S-086, DEC-S-091). Unknown CDS payload fields fail closed.

## V4 — Semantic and Governance Contract

Checks (human/governance review, beyond schema reach): downward layer direction
(DEC-S-079); status truth; semantics; accessibility relevance (e.g. non-colour
meaning); Decision and Requirement traceability; provenance completeness; maturity;
approval; compatibility; and approved-overrides-only. V4 is **Not applicable with
rationale** for synthetic non-normative fixtures (they carry no real semantics or
governance).

## Semantic-status V4 extension (CDS-WP-015)

For documents recognized as a **Semantic Status vocabulary** (a root group
`status`), V4 additionally executes the objective status rules of DEC-S-118:
authorized axis/value sets, explicit `unknown`, the 25-token count,
`status.<axis>.<value>` path/value agreement, case-only collision rejection,
aggregate- and appearance-role prohibition, no Candidate/approval statement,
and source/manifest identity agreement — with the stable `CDS-V4-STATUS-*`
diagnostics. **The testOnly/nonNormative fixture boundary never disables these
objective checks**; non-objective V4 aspects stay `Not assessed` /
`Not applicable with rationale`. The case matrix now binds **24 cases**
(VAL-CASE-001…024); the WP-013 baseline expectations VAL-CASE-001…015 are
immutable (DEC-S-120). The validation-case schema was additively corrected
(Nova-authorized, CDS-WP-015) to admit `tests/fixtures/semantic-status/`
token-fixture paths and the nine `semantic-status-*` diagnostic categories;
its `$id` and all existing constraints are unchanged.

## Result vocabulary

`Pass` · `Pass with limitations` · `Fail` · `Blocked` · `Not assessed` ·
`Not applicable with rationale`.

## Blocking rules

- A **`Fail` or `Blocked`** at a layer **stops** the subsequent layers; those layers
  are recorded as **`Not assessed`**, never assumed passed.
- **A V1 pass proves no V2 pass; a V2 pass proves no V3 pass; a V3 pass proves no V4
  pass** (DEC-S-089, RISK-058).
- **No numeric or aggregate score** — a blocked or unexecuted layer stays individually
  visible (DEC-S-089).
- **A tool result is input to review, never Human-Maintainer approval** (DEC-S-053
  applied to format validation). A schema pass is not correctness.

## Fail-closed conditions

Any of the following blocks transformation and distribution (DEC-S-078, DEC-S-091);
no automatic repair: invalid/malformed JSON; duplicate object member; invalid file
identity; DTCG profile violation; unresolvable or dangling reference; reference cycle;
type mismatch; backward (upward) layer dependency; missing source set; undeclared or
ad-hoc cross-file reference; illegal override; invalid/absent CDS extension; missing
mandatory metadata; use of a preview/draft feature; unknown source revision;
conflicting source-set identity.

## Validation-case matrix

Every fixture is bound to explicit expected `V1`…`V4` outcomes, a blocking layer, a
primary failure reason (negative cases), and applicable Decision/Risk IDs, in the
[validation-case matrix](../../tests/fixtures/machine-readable/VALIDATION_CASES.json)
(validated by [cds-validation-case schema](../../schemas/cds-validation-case.schema.json)).
Case IDs are contiguous `VAL-CASE-###`; every fixture appears in at least one case; no
case points to a missing file (DEC-S-089).

## Execution status

**CDS-WP-013 implemented and executed the offline validator** (Experimental —
[architecture](OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md), ADR-0003): the five CDS
schemas pass `check_schema` and execute from a local registry, and the full
fixture harness ran **15/15 cases with 15/15 expected/actual matches**
([execution review](../reviews/OFFLINE_TOKEN_VALIDATOR_EXECUTION_REVIEW.md),
[machine-readable results](../../artifacts/validation/wp013-fixture-results.json)).
V2 covers only the bounded DTCG 2025.10 subset required by this contract and the
committed fixtures (DEC-S-098); V4 automates only the objective edge. The results are
**executor-produced, pre-commit, independently unreviewed evidence**
(`independentReviewState: pending`, DEC-S-103) and confer **no Candidate, Stable,
conformance, or claim status** (DEC-S-092, DEC-S-104).

## Candidate metadata coherence (CDS-WP-016)

On Semantic Status documents the objective V4 edge checks the coherence of the
`maturityState`/`approvalState` metadata as a small state machine:

- **Experimental/Unapproved** (or absent) is coherent (the committed default).
- **Candidate/Approved** is coherent **only** together — with a Candidate source
  revision (`semantic-status-rev-NNNN-candidate`) and no `testOnly`/`nonNormative`
  fixture marker. Incoherent combinations (Candidate without Approved, Approved
  without Candidate, wrong revision form, Candidate/Approved on a fixture) fail
  closed with `CDS-V4-STATUS-IDENTITY`.
- **Stable stays outside this contract**; it requires a later explicit gate and a
  separate validator-contract change.

**A validator pass is not governance authorization.** A coherent Candidate/Approved
pass proves internal metadata consistency only — never that the governance gate was
authorized, nor Human-Maintainer approval, promotion, Stable, conformance, or
publication. Real Candidate authority is established by the Candidate Approval
Record, the Nova finalization review, and the Human-Maintainer commit (DEC-S-115,
DEC-S-122, DEC-S-124). The diagnostic code is unchanged; no new code is introduced.

## Change control

This contract is Elevated; changes require compatibility, migration, evidence, Nova
review, and Human-Maintainer approval (DEC-S-082). Expected outcomes are re-verified
after any profile, DTCG, schema, or governance change (RISK-071).

## Related documents

- [Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
- [CDS Token Format Profile](CDS_TOKEN_FORMAT_PROFILE.md)
- [Machine-Readable Source Model](MACHINE_READABLE_SOURCE_MODEL.md)
- [Deterministic Serialization and Digest Model](DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md)
- [ADR-0002 — Deterministic JSON Serialization](../decisions/ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md)
