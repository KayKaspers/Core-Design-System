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

**No validator is implemented in CDS-WP-012.** Structural checks (strict JSON parse,
duplicate-key detection, schema-ID and local-`$ref` integrity, case coverage and
contiguity, source-set-ID syntax, manifest dependency/graph consistency) were run
locally with a temporary, non-committed, read-only script. **Formal JSON Schema
2020-12 execution against the fixtures was `Not assessed`** — no standards-conformant
validator was available locally and none was installed; validator execution and the
resulting evidence are **CDS-WP-013**. No validation result is invented; no schema pass
is claimed (DEC-S-092).

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
