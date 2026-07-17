# Machine-Readable Source Implementation Plan

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-011 — Machine-Readable Source and Token Format Decision
- **Date:** 2026-07-16
- **Status:** **Roadmap / planning view — NON-normative and NOT an authorization.**
  It prepares the next work package; it implements nothing, selects no tool, and
  creates no token or schema.

## Decision outcome

CDS adopts DTCG 2025.10 (Format, Color, Resolver) as the external normative basis of
the **CDS Token Format Profile**, in **strict JSON `.tokens.json`**, with **JSON
Schema 2020-12** as the future profile-schema foundation, a four-layer validation
contract, and an `io.github.kaykaspers.cds` `$extensions` namespace — per
[ADR-0001](../decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) (pending
commit). **No token, schema, resolver, validator, or design value exists.**

## CDS-WP-012 outcome (bootstrap delivered)

**CDS-WP-012 implemented the value-neutral bootstrap** (pending commit): four CDS-owned
JSON Schema 2020-12 contracts (token document, source-set manifest, resolver document,
validation case), the `io.github.kaykaspers.cds` extension payload contract, six
synthetic positive fixtures and nine synthetic negative fixtures, a 15-case
[validation-case matrix](../../tests/fixtures/machine-readable/VALIDATION_CASES.json),
an explicit [V1–V4 Validation Contract](../architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md),
and the [deterministic-serialization decision](../architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md)
(RFC 8785 + SHA-256, ADR-0002). **No productive validator or canonicalizer was
implemented; no design value was created; formal schema execution against the fixtures
is `Not assessed`.** The bootstrap is **Experimental**, not Candidate (DEC-S-092).

## Implementation scope (next work package)

Turn the decided profile and bootstrap into an **executing offline validator with
evidence** — still without any real design value. Nothing here is authorized until
CDS-WP-013 is prompted.

## Required future artifacts

| Artifact | Purpose | Boundary |
| --- | --- | --- |
| **CDS profile JSON Schema** | Structural V1–V3 validation of `.tokens.json` sources | CDS-owned; not an official DTCG schema; schema pass ≠ full correctness (RISK-058) |
| **Source-Set Manifest schema** | Validate set inventory, identity, layer, dependencies | Enforces downward dependency + identity (DEC-S-079, DEC-S-080) |
| **Validation fixtures** | Positive and negative cases per V1–V4 | Value-neutral; exercise rules, not design |
| **Resolver fixtures** | Multi-context composition (e.g. two abstract contexts) | Value-neutral; test ordering/determinism |
| **Deterministic-serialization decision** | Choose canonicalization (RFC 8785 or alternative) | Currently open (DEC-S-080) |
| **Provenance evidence** | Bind source/transformation/output identity | No `latest`; offline-computable (DEC-S-031) |

## CDS profile schema

A CDS-owned JSON Schema 2020-12 document validating the CDS profile (naming, layer
metadata, `$type` presence, `io.github.kaykaspers.cds` extension boundary, prohibited
features). It is
**not** an official DTCG schema and cannot alone prove DTCG, semantic, accessibility,
or governance conformance (DEC-S-077, RISK-058). V4 remains human/governance review.

## Manifest schema

A JSON Schema for the Source-Set Manifest: required source-set identity fields
(DEC-S-080), declared layer, and dependency set — so the layer-dependency contract is
machine-checkable (DEC-S-079).

## Validation fixtures

Value-neutral positive and negative fixtures covering: valid minimal token; missing
`$value`; unknown property outside `$extensions`; case-only collision; illegal
segment characters; **cycle**; **dangling reference**; **missing source set**;
**upward dependency**; **type conflict**; **unapproved override**; preview-feature
use. Each negative fixture must **fail closed** (DEC-S-078).

## Resolver fixtures

Value-neutral fixtures exercising DTCG resolver sets/modifiers in a defined order for
two abstract contexts, asserting deterministic resolution and no upward dependency.

## Positive and negative test cases

Positive cases assert `Pass`; negative cases assert `Fail`/`Blocked`; unrun layers
report `Not assessed`. **No numeric or aggregate score** (Reference/Resolution/
Validation Model).

## Deterministic serialization decision

**Decided by CDS-WP-012** (ADR-0002, DEC-S-090): **RFC 8785 (JCS) + SHA-256** for
canonical content digests, enabling reproducible identity (DEC-S-080); no canonicalizer
is implemented (execution is CDS-WP-013).

## Offline validation

All schemas, fixtures, and validation must run **locally with no mandatory external
runtime or registry** (DEC-S-006, DEC-S-030). **Validator/tool selection is CDS-WP-013**
(not CDS-WP-012), constrained by offline and tool-neutrality requirements (RISK-063).

## Provenance evidence

Fixtures and any generated output must carry source revision, transformation
revision, and output identity; **`latest` is not an identity** (DEC-S-031,
DEC-S-080). No secrets or personal data.

## No-design-values boundary

CDS-WP-012 remains **value-neutral**: no colour, typography, spacing, size, real
token name, component, or Product Profile. It builds the machinery that a *later*
authorized design work package will fill. No Candidate or Stable artifact; no pilot;
no claim; no licence; no publication.

## Exit criteria (to hand off to a design work package)

The machine-readable machinery is ready when: an **offline validator executes** the
validation cases with results matching the declared expected V1–V4 outcomes; duplicate
keys are detected; RFC 8785 canonicalization and SHA-256 digests are computed and bound;
the offline-validation boundary holds; and the results are **independently reviewed**
and Human-Maintainer approved — all with **still no design values**. CDS-WP-012 defined
the schemas, fixtures, contract, and serialization decision; **CDS-WP-013 executes them**.

## Next work package

**CDS-WP-013 — Offline Token Profile Validator and Fixture Harness** (registered as
`Next`; not executed here): an offline validator (with duplicate-key detection), a
fixture harness executing the validation cases, RFC 8785 canonicalization + SHA-256
digest generation, machine-readable validation results, and an independent
evidence-review boundary — **no design values, no Candidate, no pilot**. It requires an
explicit Nova prompt and Human-Maintainer authorization. Registration is not execution.

## Related documents

- [ADR-0001](../decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
- [Machine-Readable Source Model](../architecture/MACHINE_READABLE_SOURCE_MODEL.md)
- [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md)
- [Token Reference, Resolution and Validation Model](../architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
- [Token Metadata, Provenance and Identity Model](../architecture/TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md)
- [Pre-Candidate Operating Plan](PRE_CANDIDATE_OPERATING_PLAN.md)
