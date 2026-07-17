# CDS-WP-013 — Offline Token Profile Validator and Fixture Harness — Notes

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-013 (Completed; pending Human-Maintainer commit)
- **Date:** 2026-07-17
- **Executor:** Claude (scoped executor). This evidence is **executor-produced and
  independently unreviewed** (DEC-S-103).

## Assignment

Implement the first offline-executable validator and fixture harness for the pinned
CDS Token Format Profile v1 over DTCG 2025.10; execute the committed 15 validation
cases; produce revision- and content-bound machine-readable execution evidence;
decide the implementation stack (ADR-0003); register DEC-S-093…104 and
RISK-073…081; register CDS-WP-014 as Next. Explicitly out of scope: real design
tokens/values, components, Product Profiles, consumer integrations, Candidate/Stable
status, any DTCG/accessibility/CDS conformance statement, release or publication.

## Preflight

- Repository `D:\Projects\Core-Design-System`, branch `main`, **working tree clean**,
  no merge/rebase/cherry-pick, `origin` = KayKaspers/Core-Design-System.
- Last commit `1ad9787` ("feat(cds): bootstrap token validation contracts") —
  **CDS-WP-012 committed**.
- Registers verified by script: Decisions 92 (DEC-S-001…092, contiguous) · Risks 72
  (70 Monitored; RISK-040 + RISK-044 Mitigating) · CR-001…040 (40, contiguous) ·
  ADRs 2 · Schemas 4 (all `$id`s exact) · positive fixtures 6 · negative fixture
  files 9 · cases VAL-CASE-001…015 (15).
- Runtime: Python 3.12.10 (≥ 3.11 ✓), pip 26.1.2 ✓.
- Skills: 38 directories, 39 files, **39/39 manifest SHA-256 matches** (an initial
  38/39 reading was a script path-resolution artifact — the manifest's `README.md`
  entry resolved against the repository root instead of `.claude/skills/`; corrected
  and re-verified 39/39).
- Publication `Private Development`; no Candidate/Stable/claim; pilot inactive.
- Fail-closed conditions: **none triggered**.

## Skills used (11; only the authorized set)

ndf-work-package-runner (WP frame/guardrails/closing structure) ·
ndf-architecture-blueprint-runner (validator module architecture) ·
ndf-implementation-review-runner (self-review of scope/architecture fit) ·
ndf-adr-governance-review (ADR-0003 number/status derivation) ·
ndf-validation-evidence-reviewer (honest evidence classification/limits) ·
ndf-existing-project-analysis-runner (preflight structure) ·
ndf-feature-scope-runner (scope/acceptance sharpening) ·
ndf-privacy-data-minimization-reviewer (no personal data/telemetry in reports) ·
ndf-release-safety (no release/tag/claim language) ·
ndf-context-pack-maintainer (context pack update) ·
ndf-compact-context-summary-runner (closing blocks). No further skill was read or
used; per CLAUDE.md the WP prompt overrides the skills' generic docs-only framing
for the explicitly authorized implementation work.

## Dependency research and environment

Opened official URLs (4): pypi.org/project/jsonschema/ · pypi.org/project/rfc8785/ ·
python-jsonschema.readthedocs.io/en/stable/referencing/ ·
github.com/trailofbits/rfc8785.py (linked from the PyPI page). Selected:
`jsonschema==4.26.0` (MIT; Draft 2020-12 + local `referencing.Registry`) and
`rfc8785==0.1.4` (Apache-2.0; pure Python, zero dependencies). Transitive (pinned):
attrs 26.1.0, jsonschema-specifications 2025.9.1, referencing 0.37.0,
rpds-py 2026.6.3, typing_extensions 4.16.0 → 7 packages total in
`requirements-validator.lock`. Installed into a temporary venv **outside the
repository** (session scratchpad; not committed). After installation the validator
ran with no network access. Details:
[Dependency Source Register](../docs/research/OFFLINE_VALIDATOR_DEPENDENCY_SOURCE_REGISTER.md) ·
[Stack Evaluation](../docs/research/OFFLINE_VALIDATOR_STACK_EVALUATION.md) ·
[ADR-0003](../docs/decisions/ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md).

## Implementation

13 modules under `tools/cds_validator/` (+ `tools/__init__.py`); see the
[Validator Architecture](../docs/architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md):

- **Loader** (`json_loader.py`): the single controlled path — UTF-8, strict JSON,
  duplicate-key rejection via `object_pairs_hook`; no repair, no network. No other
  module calls `json.load` on validation input (`reporting.py` only *writes* JSON).
- **Schema registry** (`schema_registry.py`): exactly the 5 CDS schemas,
  `check_schema` on load, `$id`-bound local resolution via `referencing.Registry`;
  unknown identity fails closed.
- **Layered engine** (`validation.py`): scope-based V1→V2→V3→V4 with blocking
  (`Fail`/`Blocked` ⇒ later layers `Not assessed`), per-layer scope aggregation,
  bounded DTCG V2 (known-2025.10 `$type` set; unknown ⇒ preview-feature), in-scope
  alias resolution (dangling/cycle/type), cross-file candidates deferred to the V3
  declared-graph boundary, manifest/resolver identity + graph + order + extension
  boundary + product-profile bounds, V4 objective subset (fixtures ⇒
  `Not applicable with rationale`).
- **Graph** (`graph.py`): registration, case-insensitive collision, self/backward/
  cycle detection, transitive closure, resolver order.
- **Digests** (`canonicalization.py`): `rfc8785.dumps` + SHA-256, `sha256:` lowercase
  hex, parsed-content only; `DigestError` on unsupported input.
- **Reporting/CLI** (`reporting.py`, `cli.py`, `__main__.py`): result-schema-bound
  reports; `version` / `validate-file` / `validate-cases` / `digest`; exit codes
  0/1/2/3; `independentReviewState: pending`; worktree state reported honestly.

During implementation two engine defects were found and fixed before any evidence
run: the token index was initially rebuilt between V2 and V3 (losing deferred
cross-file marks), and alias-cycle detection initially ran per document (missing the
committed cross-file cycle pair). Both were corrected; the committed expected
outcomes were never modified.

## V1–V4 execution and fixture harness

Official evidence run (venv Python, repo root):

```
python -m tools.cds_validator validate-cases tests/fixtures/machine-readable/VALIDATION_CASES.json \
  --report artifacts/validation/wp013-fixture-results.json \
  --digests artifacts/validation/wp013-fixture-digests.json   → exit 0
```

- Case matrix schema-validated first; **15/15 cases executed**; **15/15
  expected/actual matches** (layer-exact V1–V4 + expected diagnostic category per
  negative case); 0 mismatches, 0 internal errors, 0 missing fixture paths, 0
  unassigned fixtures.
- Key recognitions: duplicate-key → V1 Fail; dangling/cycle/type-mismatch/preview →
  V2 Fail; backward-layer manifest, undeclared cross-file, invalid extension → V3
  Fail; positives → V3 Pass with V4 `Not applicable with rationale`. VAL-CASE-011
  additionally shows 2 documented secondary `missing-source-set` diagnostics
  (declaratively unmaterialized paths); its primary category stays
  `backward-layer-dependency`.
- Diagnostics: **11 total, all `error`** — CDS-V1-DUPLICATE-KEY 1 ·
  CDS-V2-DTCG-REFERENCE 3 · CDS-V2-PREVIEW-FEATURE 1 · CDS-V3-EXTENSION 2 ·
  CDS-V3-MANIFEST 3 · CDS-V3-UNDECLARED-CROSS-FILE 1 (V1:1, V2:4, V3:6, V4:0).
- Digests: **14** fixtures digested; **1 undigestible** (duplicate-key fixture — no
  digest by contract, DEC-S-100).
- Manifest graph (positive): 4 nodes, 3 edges, 0 cycles; negative manifest: 1
  backward edge detected. Remote references blocked at V1 by design (0 present in
  fixtures; loader/V1 tests cover the blockade).

## Unit tests

`python -m unittest discover -s tests/validator` → **71 tests, 71 passed, 0
failures, 0 errors** across 8 modules + package marker (9 files): loader (8) ·
schema registry (6) · graph (14) · canonicalization (8) · validation engine (13) ·
reporting (7) · CLI (7) · fixture harness (8) — counts per module independently
re-derived from the verbose run (a first manual count recorded graph as 13; the
re-count corrected it to 14; 8+6+14+8+13+7+7+8 = 71). Covers every mandated area including duplicate-key loader, unknown
schema ID, remote-ref absence, ID syntax/collision, dependencies, layer direction,
cycles, dangling, type mismatch, undeclared cross-file, preview feature, RFC-8785
invariance (indentation/key-order/value-change/duplicate-key/unsupported-input),
SHA-256 format + known vector, result schema, CLI exit codes, and expected/actual
comparison. No test touches a network.

## Schema execution status

All **5** schemas pass `Draft202012Validator.check_schema` and execute offline from
the local registry (the WP-012 `Not assessed` state is superseded by this executed,
executor-produced evidence — recorded in the updated
[Validation Contract](../docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)).

## Deterministic serialization

RFC 8785 + SHA-256 via the pinned `rfc8785` 0.1.4; digests only from parsed content;
duplicate-key input undigestible; digest ≠ signature/approval/authenticity
(DEC-S-100). The fixtures' internal `digestState` fields intentionally remain
`Not computed` (fixtures are frozen inputs; recorded digests live in the evidence
artifacts) — documented in the updated
[Serialization/Digest Model](../docs/architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md).

## ADR-0003, Decisions, Risks

- **ADR-0003** created (Accepted upon Human-Maintainer commit following Nova
  approval); ADR count now 3.
- **DEC-S-093…104** added exactly (12); total 104, contiguous; DEC-S-001…092
  textually unchanged.
- **RISK-073…081** added exactly (9); total 81, contiguous. Authorized status
  changes executed with met evidence gates: RISK-066/067/068/069/071
  `Monitored → Mitigating` (each with named scoped executor). RISK-040 + RISK-044
  stay Mitigating. Distribution derived from the register: **74 Monitored / 7
  Mitigating**. No acceptance or closure.

## Changed files (67 allowed; 46 touched — 33 created + 13 modified; an initial
count of 44 was corrected by the independent `git status` re-count)

Created: `requirements-validator.lock`; 13 validator modules + `tools/__init__.py`;
9 test files; `schemas/cds-validation-result.schema.json`; 2 evidence artifacts;
Execution Review; 2 research docs; ADR-0003; validator architecture + usage docs;
these notes. Modified: `MACHINE_READABLE_VALIDATION_CONTRACT.md` (execution status),
`DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md` (WP-013 digest update),
`MACHINE_READABLE_SOURCE_IMPLEMENTATION_PLAN.md` (WP-013 outcome; WP-014 next; one
stale "Currently open" serialization-table cell corrected to the ADR-0002 state),
`DECISION_INDEX.md`, `RISK_REGISTER.md`, `WORK_PACKAGES.md`, `NEXT_PHASE.md`,
`PROJECT_PROFILE.md`, `CONTEXT_PACK_FOUNDATION.md`, `PROJECT_BRAIN.md`, `README.md`,
`CLAUDE.md`, `CHANGELOG.md`. **Not modified:** the 4 committed WP-012 schemas, all
15 fixtures, `VALIDATION_CASES.json` (expected outcomes untouched),
`CRITICAL_RISK_ACTION_REGISTER.md` (its twelve Critical Risks are unaffected by this
WP; listed as allowed but no change was needed), ADR-0001/0002, skills, consumer
files.

## Deviations

1. The venv Python was 3.12.10 (requirement "3.11 or later" — satisfied; recorded
   exactly).
2. `CRITICAL_RISK_ACTION_REGISTER.md` was allowed but intentionally unchanged (no
   critical-risk trigger).
3. Skills were read in full but their generic "docs-only/no scripts" framing is
   overridden by this WP prompt's explicit implementation authorization (per
   CLAUDE.md precedence); noted for transparency.

## Open validator questions (for CDS-WP-014 / independent review)

- Independent re-execution in a second OS/runtime environment (RISK-075).
- V2 breadth beyond the fixture-required subset (color-module value semantics,
  resolver modifier semantics, composite types — DEC-S-098 limitation list).
- Governance of the known-DTCG-`$type` list as DTCG evolves (RISK-056/071).
- Provenance-pointer byte-precision form (open point carried from WP-011/012).

## Completion status

**PASS** against the Definition of Done, with the notes above. Evidence is
executor-produced, pre-commit, content-bound, independently unreviewed; **no
Candidate, no claim, no release**. No Git write action was performed.
