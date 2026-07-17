# Offline Token Validator Execution Review

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-013 — Offline Token Profile Validator and Fixture Harness
- **Date:** 2026-07-17
- **Evidence class:** **Executor-produced, pre-commit, content-bound, independently
  unreviewed** (DEC-S-103). This review documents an execution; it is **not** an
  independent Evidence Review, not a Nova review, and not a Human-Maintainer
  approval. **Candidate: no** (DEC-S-104).

## Runtime and dependencies

- Runtime: **Python 3.12.10** (CPython, win32) — satisfies the ≥ 3.11 requirement.
- Direct dependencies (exact): `jsonschema==4.26.0`, `rfc8785==0.1.4`.
- Transitive (exact): `attrs==26.1.0`, `jsonschema-specifications==2025.9.1`,
  `referencing==0.37.0`, `rpds-py==2026.6.3`, `typing_extensions==4.16.0`.
- Installed into a temporary virtual environment **outside** the repository; the
  execution required no network access.

## Commands executed

```
python -m tools.cds_validator version
python -m unittest discover -s tests/validator
python -m tools.cds_validator validate-cases tests/fixtures/machine-readable/VALIDATION_CASES.json --report artifacts/validation/wp013-fixture-results.json --digests artifacts/validation/wp013-fixture-digests.json
```

## Schema check

All **five** CDS schemas (token document, source-set manifest, resolver document,
validation case, validation result) loaded from the local registry, passed
`Draft202012Validator.check_schema`, and carry exactly their expected `tag:` `$id`s.
No remote reference exists; an unknown schema identity fails closed (verified by unit
test).

## Unit-test result

- **71 tests, 71 passed, 0 failures, 0 errors** across 8 test modules
  (`test_json_loader`, `test_schema_registry`, `test_graph`,
  `test_canonicalization`, `test_validation`, `test_reporting`, `test_cli`,
  `test_fixture_harness`).

## Case result

- **15/15 cases executed** (VAL-CASE-001 … VAL-CASE-015); exit code **0**.
- **Expected/actual matches: 15/15** — layer-exact on V1–V4, plus the expected
  diagnostic category for every negative case. **0 mismatches, 0 internal errors,
  0 unassigned fixtures, 0 missing paths.**
- Key recognitions: duplicate-key blocked at **V1**; dangling reference, cross-file
  cycle, type mismatch, and preview feature failed at **V2**; backward layer
  dependency, undeclared cross-file reference, and invalid extension failed at
  **V3**; positive fixtures reached V3 `Pass` with V4
  `Not applicable with rationale` (synthetic, non-normative — DEC-S-087).

## Diagnostic count

**11 diagnostics, all severity `error`,** across the executed cases:

| Code | Count | Layer |
| --- | --- | --- |
| CDS-V1-DUPLICATE-KEY | 1 | V1 |
| CDS-V2-DTCG-REFERENCE | 3 | V2 |
| CDS-V2-PREVIEW-FEATURE | 1 | V2 |
| CDS-V3-EXTENSION | 2 | V3 |
| CDS-V3-MANIFEST | 3 | V3 |
| CDS-V3-UNDECLARED-CROSS-FILE | 1 | V3 |

(V4 informational `CDS-V4-NOT-ASSESSED` diagnostics do not occur in the harness:
every fixture reaching V4 is `Not applicable with rationale`. The two secondary
`missing-source-set` diagnostics of VAL-CASE-011 are inside the CDS-V3-MANIFEST
count; the case's primary reason remains `backward-layer-dependency`.)

## Digest count

- **14 fixtures digested** (`sha256:` lowercase hex, RFC 8785 canonical content);
  **1 undigestible input**: the duplicate-key fixture (V1-invalid ⇒ no digest,
  DEC-S-100). Digests: [wp013-fixture-digests.json](../../artifacts/validation/wp013-fixture-digests.json).

## Execution identity

- Repository revision at execution: `1ad9787012aaf507f2483dc891d4cb03e12c1b5b`
  (the CDS-WP-012 commit) with **`worktreeState: modified worktree`** — the run
  binds to the uncommitted CDS-WP-013 worktree content and must **not** be quoted as
  the committed revision's result.
- Reports: [wp013-fixture-results.json](../../artifacts/validation/wp013-fixture-results.json)
  (validated against the CDS result schema before writing);
  `independentReviewState: pending`.

## Limitations

- **V2 is a bounded DTCG 2025.10 subset** (DEC-S-098): color-module value semantics,
  resolver modifier semantics, and composite-type internals are not validated and
  are not represented as passed (RISK-074).
- **V4** automates only the objective edge; status truth, semantics, accessibility
  relevance, and compatibility remain human/governance review (`Not assessed`).
- Single-environment execution (one OS, one runtime); cross-environment
  reproducibility is unverified (RISK-075).
- The same executor wrote the fixtures, expectations, and validator — the 15/15
  result proves internal consistency, not correctness (RISK-078).

## Review state

- **Independent review: pending.** The Evidence Reviewer must be Nova or a
  separately authorized reviewer — never this executor (DEC-S-045, DEC-S-103).
- **Candidate: no.** Nothing in this execution confers Candidate, Stable,
  conformance, claim, release, or publication status (DEC-S-104, DEC-S-044).
