# Offline Token Validator Architecture

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-013 — Offline Token Profile Validator and Fixture Harness
- **Date:** 2026-07-17
- **Status:** Describes the **Experimental** validator implementation. The normative
  contracts remain the
  [Machine-Readable Validation Contract](MACHINE_READABLE_VALIDATION_CONTRACT.md), the
  committed schemas, and
  [VALIDATION_CASES.json](../../tests/fixtures/machine-readable/VALIDATION_CASES.json);
  on any divergence the contracts win and the implementation is corrected
  (never the reverse — DEC-S-102).

## Position in the architecture

The validator is **tooling, never a source of truth** (DEC-S-004): it executes the
committed contracts against committed fixtures and produces evidence. Its output is
class-3 generated content — input to review, never approval (DEC-S-053).

## Module map (`tools/cds_validator/`)

| Module | Responsibility |
| --- | --- |
| `__main__.py` | Entry point `python -m tools.cds_validator` (DEC-S-094). |
| `cli.py` | Commands `version` / `validate-file` / `validate-cases` / `digest`; exit codes 0/1/2/3. |
| `json_loader.py` | **The single controlled loader**: UTF-8, strict JSON, duplicate-key rejection via `object_pairs_hook`; no repair, no network (DEC-S-095). |
| `schema_registry.py` | Local-only registry of the five CDS schemas; `check_schema` on load; `$id`-bound resolution via `referencing.Registry`; unknown identity fails closed (DEC-S-096). |
| `models.py` | Layers V1–V4, six-state result vocabulary, diagnostics, per-layer aggregation across a scope (never across layers). |
| `diagnostics.py` | Stable `CDS-V…` diagnostic codes with layer, severity, category, and Decision/Risk references (RISK-077). |
| `graph.py` | Manifest graph: registration, case-collision, dependency direction, cycles, resolver order (DEC-S-099). |
| `validation.py` | The layered V1–V4 engine (see below). |
| `canonicalization.py` | RFC 8785 + SHA-256 `sha256:` digests from parsed content only (DEC-S-100, ADR-0002). |
| `reporting.py` | Machine-readable reports per the CDS result schema; runtime/dependency/revision binding; `independentReviewState: pending` (DEC-S-101, DEC-S-103). |
| `version.py` | Validator/profile/DTCG/schema/dependency identities. |
| `semantic_status.py` | **(CDS-WP-015)** Objective V4 semantic-status rules for `status`-vocabulary documents: axis/value sets, explicit `unknown`, 25-token count, path/value agreement, case-collision, aggregate/appearance-role prohibition, approval-statement and manifest-identity checks (`CDS-V4-STATUS-*`). Runs **before** the fixture N/A shortcut — testOnly/nonNormative never disables it. |

## Layered execution

A **scope** is the set of documents validated together (a case's fixture paths, or
one input plus optional manifest/resolver). Per scope:

1. **V1** per file: UTF-8 → strict parse with duplicate-key rejection → file
   identity (`.tokens.json` / `.source-set.json` / `.resolver.json`) → RFC 6901
   pointer syntax → no network/UNC/backslash references → no path escape beyond the
   repository root. Fail ⇒ V2–V4 `Not assessed`.
2. **V2** (bounded DTCG 2025.10 subset — DEC-S-098): group/token structure, reserved
   members, known `$type` set (unknown ⇒ preview-feature, DEC-S-074), full-string
   `{group.token}` alias syntax and naming profile, in-scope reference resolution
   (dangling, cross-document cycles, type compatibility). A reference whose root
   group is unknown in scope is a **cross-file candidate** deferred to V3.
   Manifests are `Not applicable with rationale`. Fail ⇒ V3–V4 `Not assessed`.
3. **V3** (CDS profile): JSON-Schema execution from the local registry; extension
   root and `profileVersion`; manifest binding via the in-scope manifest or the
   document's `manifestRef`; identity agreement (ID, layer, revision, versions);
   deferred cross-file references resolved **only** through the declared transitive
   dependency closure (undeclared/missing/mis-typed/upward ⇒ fail closed,
   DEC-S-091); manifest graph rules; resolver `$ref`/pointer targets, order, and
   manifest declaration; product-profile approved-extension-point bounds.
   Fail ⇒ V4 `Not assessed`.
4. **V4**: synthetic `testOnly`/`nonNormative` fixtures ⇒
   `Not applicable with rationale` (DEC-S-087). Otherwise the objective subset
   (provenance presence, Decision/Requirement ID syntax) runs and everything
   non-objective stays `Not assessed` with a rationale.

Per-layer scope aggregation: Fail ≻ Blocked ≻ Not assessed ≻ Pass-with-limitations;
a mix of Pass and Not-applicable is Pass; all-Not-applicable stays Not applicable.
Layers are never merged and no score exists (DEC-S-097).

## Fixture harness

`validate-cases` first schema-validates the case matrix, then executes every case
scope, compares actual against the **unchanged** committed expected outcomes
(layer-exact, plus expected diagnostic category for negative cases), digests every
V1-parsable fixture, and writes the result and digest reports — schema-validated
before writing. Expected failure recognized correctly is harness success
(DEC-S-102); an implementation/expectation conflict is BLOCKED for Nova, never an
expectation edit.

## Evidence boundary

Reports bind runtime, dependencies, schemas, repository revision, and worktree state;
a worktree run is never presented as a committed revision. All output is
executor-produced, independently unreviewed evidence (DEC-S-103) and confers no
Candidate, Stable, conformance, or claim status (DEC-S-104, DEC-S-044).

## Semantic Status maturity/approval state machine (CDS-WP-016)

On a Semantic Status document (root `status` group) the objective V4 checker
evaluates a maturity/approval state machine over the CDS extension payload:

- **Experimental source:** `maturityState: Experimental` with
  `approvalState: Unapproved` (or absent metadata) — coherent, the committed
  default.
- **Candidate source:** `maturityState: Candidate` **and** `approvalState:
  Approved`, **and** a `sourceRevision` matching the Candidate-revision pattern
  `^semantic-status-rev-[0-9]{4}-candidate$`, **and** not a fixture
  (`testOnly`/`nonNormative` not true). Only this exact combination is coherent.
- **Fixture boundary:** Candidate/Approved metadata may never be embedded in a
  `testOnly`/`nonNormative` fixture — it fails closed.
- **Stable boundary:** `maturityState: Stable` remains blocked; a later explicit
  gate and a separate validator-contract change are required.
- Any incoherent or contradictory combination emits `CDS-V4-STATUS-IDENTITY`
  (Error). No new diagnostic code is introduced.

**Authority boundary:** a coherent Candidate/Approved pass proves metadata
consistency and an allowed revision form only. It is **not** governance
authorization — Candidate authority comes solely from the Candidate Approval
Record, the Nova finalization review, and the Human-Maintainer commit (DEC-S-115,
DEC-S-122, DEC-S-124).

## Known boundaries

- V2 is a bounded subset: color-module value semantics, resolver modifier semantics,
  and composite-type internals are unvalidated limitations (DEC-S-098, RISK-074).
- V4 is largely human/governance review; the validator only automates the objective
  edge.
- The validator validates CDS documents — it transforms nothing, builds nothing, and
  emits no design values.
- A maturity/approval coherence pass is not a maturity grant (CDS-WP-016).
