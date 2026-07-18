# WP-013 Validator Evidence Re-Execution Review

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-015 — Semantic Status Foundation Source Set and
  Candidate Evidence (resume run)
- **Date:** 2026-07-18
- **Evidence class:** **Executor-produced, revision- and content-bound,
  independently unreviewed** (DEC-S-121). This documents a re-execution; it is
  **not** the independent Evidence Review required by the Candidate gates.
  **Candidate: no.**

## Purpose

The WP-013 execution evidence was produced on a modified worktree. This
re-execution repeats the committed WP-013 baseline on the **clean committed
CDS-WP-014 revision**, before any CDS-WP-015 file change, closing the
revision-cleanliness note from the WP-013 report.

## Committed starting revision and tree state

- Repository revision: **`943229dcda15bcc2b4963a55222f6d2c3a4a75eb`**
  (the CDS-WP-014 commit, containing the complete WP-013 validator).
- Working tree: **clean at start and after the run** (`worktreeState: clean`
  in the machine-readable report; bytecode generation suppressed).

## Runtime and dependencies

Python **3.12.10** (CPython, win32); `jsonschema==4.26.0`, `rfc8785==0.1.4`
(exactly the pinned versions from `requirements-validator.lock`; verified in
the environment before the run; no installation, no version change).

## Results

- **Unit tests: 71/71 passed** (the committed WP-013 suite, unmodified).
- **Cases: 15/15 executed — 15/15 expected/actual matches**, 0 mismatches,
  0 internal errors, exit 0. Expected outcomes were byte-identical to the
  committed matrix; none was changed.
- **Digests: 14** fixtures digested; the duplicate-key fixture received
  **no** digest (DEC-S-100) — matching the WP-013 baseline exactly.
- **Result-schema validation:** the report was validated against the CDS
  result schema before writing (CLI-enforced) — passed.

## Expected/actual comparison

Layer-exact agreement on V1–V4 for all 15 cases, including the expected
diagnostic category per negative case. The clean-revision results are
identical to the WP-013 modified-worktree results — no environment- or
revision-dependent divergence was observed.

## Artifacts

[wp015-wp013-clean-reexecution-results.json](../../artifacts/validation/wp015-wp013-clean-reexecution-results.json) ·
[wp015-wp013-clean-reexecution-digests.json](../../artifacts/validation/wp015-wp013-clean-reexecution-digests.json)
(produced outside the repository first, adopted after the run passed).

## Limitations

Same executor, same single environment as WP-013 (RISK-075, RISK-078): this
re-execution proves revision-clean reproducibility on this machine, not
cross-environment reproducibility and not correctness. The bounded DTCG V2
coverage and objective-only V4 limits of WP-013 apply unchanged.

## Review state

- **Independent review: pending.** This document and its artifacts are
  executor-produced and must be assessed by Nova or a separately authorized
  reviewer (never the executor, DEC-S-045).
- **Candidate boundary:** nothing here confers Candidate, Stable, conformance,
  or claim status (DEC-S-104, DEC-S-124).
