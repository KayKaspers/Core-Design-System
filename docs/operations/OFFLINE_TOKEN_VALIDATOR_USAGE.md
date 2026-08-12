# Offline Token Validator Usage

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-013 — Offline Token Profile Validator and Fixture Harness
- **Date:** 2026-07-17
- **Status:** **Non-normative** operator guide for the Experimental validator. The
  contracts it executes are normative; this guide never overrides them.

## Prerequisites

- Python **3.11 or later** with `pip`.
- The pinned dependencies from
  [requirements-validator.lock](../../requirements-validator.lock), installed into a
  **temporary virtual environment outside the repository** (never inside it, never
  committed, never vendored):

```
python -m venv <outside-the-repo>\cds-validator-venv
<venv>\Scripts\python -m pip install -r requirements-validator.lock
```

After installation the validator needs **no network access**. Commands below run from
the repository root with the venv's `python`.

## Commands

### version

```
python -m tools.cds_validator version
```

Prints validator, Python, CDS profile, and DTCG report versions, the five schema
identities, and the exact dependency versions.

### validate-file

```
python -m tools.cds_validator validate-file <document> [--manifest <path>] [--resolver <path>] [--report <out.json>]
```

Runs the applicable V1–V4 layers on one document (optionally with its manifest and
resolver in scope). Exit codes: **0** Pass / Pass with limitations · **1** Fail ·
**2** Blocked · **3** configuration/contract/internal error.

### validate-cases

```
python -m tools.cds_validator validate-cases tests/fixtures/machine-readable/VALIDATION_CASES.json --report artifacts/validation/wp013-fixture-results.json --digests artifacts/validation/wp013-fixture-digests.json
```

Schema-validates the case matrix, executes all cases (**24** since CDS-WP-015:
15 machine-readable + 9 semantic-status), compares actual against the committed
expected outcomes, and writes schema-validated machine-readable reports.
Documents with a root `status` group additionally receive the objective
semantic-status V4 checks (`CDS-V4-STATUS-*`), which fixture flags never
disable.
Exit codes: **0** all actual results match expected · **1** at least one mismatch ·
**2** blocked (contract/input/dependency problem) · **3** internal error.
An expected failure of a negative fixture that is recognized correctly is a
**successful** observation (exit 0), not a harness failure.

### digest

```
python -m tools.cds_validator digest <document>
```

Prints the `sha256:`-prefixed RFC 8785/SHA-256 content digest — only if the V1 parse
succeeds. Duplicate-key input receives **no** digest (exit 1).

## Unit tests

```
python -m unittest discover -s tests/validator
```

## Reading results honestly

- Four layer states per case; **no aggregate score**. `Not assessed` means blocked or
  not executed — never "passed".
- A green harness is executor-produced, **independently unreviewed** evidence
  (`independentReviewState: pending`). It is **not** a Candidate/Stable status, not a
  DTCG/accessibility/CDS conformance statement, and not a release approval
  (DEC-S-103, DEC-S-104, DEC-S-044).
- A digest is an integrity aid, never authenticity or approval (DEC-S-100).
- A `modified worktree` report binds to uncommitted content and must not be quoted as
  the committed revision's result.

## Candidate metadata on Semantic Status documents (CDS-WP-016)

Since CDS-WP-016 the semantic-status V4 checks apply a maturity/approval state
machine instead of an unconditional block:

- **Experimental/Unapproved** (or absent) is the current committed state and
  passes.
- **Candidate/Approved** is validator-conformant **only** when it is internally
  coherent: `maturityState: Candidate` **with** `approvalState: Approved`, a
  Candidate source revision (`semantic-status-rev-NNNN-candidate`), and **not** a
  `testOnly`/`nonNormative` fixture. Incoherent combinations (Candidate without
  Approved, Approved without Candidate, a wrong revision form, Candidate/Approved
  on a fixture) fail closed with `CDS-V4-STATUS-IDENTITY`.
- **Stable** stays blocked; it needs a later explicit gate and a separate
  validator-contract change.

**A validator pass is not a maturity grant.** The CLI never awards a maturity
level: a Candidate/Approved pass proves only metadata coherence. It does **not**
prove the governance gate was authorized and does **not** replace the Candidate
Approval Record, the Nova finalization review, or the Human-Maintainer commit —
the only sources of real Candidate authority (DEC-S-115, DEC-S-122, DEC-S-124).

## Boundaries for operators

Never edit expected outcomes to make a run succeed (DEC-S-102); never add a
dependency or network path (DEC-S-093, RISK-079); never commit the venv or any
generated report as a normative source. Only the Human Maintainer commits, tags,
releases, or changes maturity.
