# WP-016 Contract Correction — Independent Review (R2)

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Contract Correction Independent Review R2
- **Date:** 2026-08-12
- **Reviewed revision:** `c93cd660ba6a8fe9ee9e54ec1e165d3f1ad1d5ed`
- **Parent revision:** `3619b1af97819740594ef597ed9f812ddb4515fd`
- **Status:** **Reviewer-produced, revision-bound, non-promotional.** This review
  approves nothing, promotes nothing, and grants no maturity. It is an input to a
  Nova review and a Human-Maintainer decision, never a substitute for either.
- **Result:** **REWORK REQUIRED** · **Recommendation: NO-GO** · **Candidate: No**

## Scope and independence

This review examines exactly the committed Contract Correction commit against its
parent. It re-derives every sentinel from the repository and from its own execution
rather than accepting the executor's recorded evidence.

The reviewer context is a fresh session that did not execute the correction, did not
edit the validator, the resolver schema, the correction tests, or the correction
notes. Its only inputs are the committed repository state, the committed correction
diff, the committed correction notes, and the authorized normative CDS artifacts —
all legitimate review sources, not executor session memory.

**Independence gate: PASS.**

## Summary

The correction is **technically sound and scope-disciplined**. The resolver schema
change is strictly additive with a stable `$id`; the Candidate metadata state machine
behaves exactly as specified across all probed states; the full unit regression and
the fixture harness reproduce their sentinels exactly on two independent
interpreters; and no implementation, fixture, case, source, dependency, or governance
artifact outside the declared eight-file delta was touched.

The review nevertheless resolves to **NO-GO** on a single documentation defect: the
correction added its new contract sections but did not reconcile two pre-existing
statements that assert the *superseded* unconditional prohibition. One of them sits
inside a **normative, Elevated** contract document, which therefore now states both
rules at once. Under the CDS conflict rule a reviewer may not resolve this by
recency, and the conservative reading negates the correction's stated purpose.

The remedy is two small, precise edits. No technical rework is indicated.

## Repository reconciliation

| Item | Expected | Derived | Result |
| --- | --- | --- | --- |
| Repository root | `D:\Projects\Core-Design-System` | identical | PASS |
| Branch | `main` | `main` | PASS |
| HEAD | `c93cd660…` | `c93cd660ba6a8fe9ee9e54ec1e165d3f1ad1d5ed` | PASS |
| Parent | `3619b1a…` | `3619b1af97819740594ef597ed9f812ddb4515fd` | PASS |
| HEAD subject | as specified | `fix(cds): reconcile candidate metadata validation contract` | PASS |
| Working tree | clean | clean (before and after) | PASS |
| Index | clean | clean (before and after) | PASS |
| Merge / rebase / cherry-pick | none | none | PASS |
| `origin` | present, plausible | `github.com/KayKaspers/Core-Design-System`, `origin/main == HEAD` | PASS |
| Tags | — | 0 | PASS |

## Correction delta

`git diff --name-status` over parent→HEAD yields **exactly eight paths — 7 modified,
1 added, 0 deleted**, matching the authorized list with no ninth file:

| # | Path | Status |
| --- | --- | --- |
| 1 | `schemas/cds-resolver-document.schema.json` | M |
| 2 | `tools/cds_validator/semantic_status.py` | M |
| 3 | `tests/validator/test_semantic_status.py` | M |
| 4 | `docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md` | M |
| 5 | `docs/architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md` | M |
| 6 | `docs/operations/OFFLINE_TOKEN_VALIDATOR_USAGE.md` | M |
| 7 | `docs/foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md` | M |
| 8 | `project-brain/CDS_WP_016_CONTRACT_CORRECTION_NOTES.md` | A |

## Resolver schema review

| Check | Result |
| --- | --- |
| `digestState.status` enum 2 → 3, strictly additive | PASS (parent set is a subset; 1 added, 0 removed) |
| Historical value still valid | PASS |
| New precise value valid | PASS |
| `Computed` valid | PASS |
| Unknown value invalid | PASS (`Not computed`, lowercase, ASCII-hyphen, empty, free string all rejected) |
| No free strings | PASS (`type: string` + `enum`, `additionalProperties: false`) |
| No further enum values | PASS (exactly 3) |
| `$id` unchanged | PASS (`tag:github.com,2026:…/cds-resolver-document/1`) |
| `$schema` unchanged, Draft 2020-12 | PASS |
| No new schema version | PASS |
| No remote dependency | PASS (validated under a registry that raises on any fetch) |
| Committed resolver instance still valid | PASS (valid under **both** parent and corrected schema) |
| All five CDS schemas `check_schema` | PASS (5/5) |
| Local `$ref` integrity | PASS (51 refs, 0 remote, 0 broken) |
| Nothing else in the schema moved | PASS (byte-identical outside the `status` subschema) |

The correction adds the precise value but does **not** apply it to the committed
resolver instance, which still carries the historical value. That is correct scope
discipline for this run, not an omission.

## Candidate metadata state machine

Confirmed **from the committed code**, not from tests alone
([`semantic_status.py:173`](../../tools/cds_validator/semantic_status.py)):

- **Stable** → always Error, regardless of approval state. Out of contract.
- **Candidate** → Error unless *all* hold: not a `testOnly`/`nonNormative` fixture,
  `approvalState == "Approved"`, and `sourceRevision` matching
  `^semantic-status-rev-[0-9]{4}-candidate$`.
- **`Approved` outside a coherent Candidate source** → Error.
- **Experimental/Unapproved or absent** → no diagnostic.

Only the existing `CDS-V4-STATUS-IDENTITY` code is used; no new diagnostic was
introduced. The manifest identity check remains an **independent second gate**: a
Candidate document whose revision disagrees with the manifest still fails closed, so
a Candidate finalization cannot be completed in the token document alone.

### Direct metadata probes

In-memory copies of the committed HEAD source; nothing written to the repository.
Run twice — without a manifest (state machine isolated) and with the committed
manifest (coupled behaviour).

| Probe | State | Expected | Actual | Result |
| --- | --- | --- | --- | --- |
| P1 | Experimental + Unapproved | PASS | PASS | MATCH |
| P2 | Candidate + Approved + `rev-0002-candidate` | no identity error | no identity error | MATCH |
| P3 | Candidate + Unapproved | ERROR | ERROR | MATCH |
| P4 | Candidate + Approved + `rev-0002` | ERROR | ERROR | MATCH |
| P5 | Experimental + Approved | ERROR | ERROR | MATCH |
| P6 | Candidate + Approved + `testOnly` | ERROR | ERROR | MATCH |
| P7 | Candidate + Approved + `nonNormative` | ERROR | ERROR | MATCH |
| P8 | Stable + Approved | ERROR | ERROR | MATCH |

**8/8 as expected.** With the committed manifest in scope, P2 additionally fails
closed on revision disagreement — the correct coupled behaviour.

## Bypass analysis

Where the schema already blocks a state, it is recorded as `SCHEMA_FAIL_CLOSED`
rather than treated as a missing validator check.

| Class | Validator | Schema | Assessment |
| --- | --- | --- | --- |
| Metadata absent | pass | accept | Correct default |
| `Approved` without maturity | Error | accept | Correct |
| Candidate without approval | Error | accept | Correct |
| `maturityState` / `approvalState` null | pass | **reject** | `SCHEMA_FAIL_CLOSED` |
| Non-string maturity | Error | **reject** | Correct + `SCHEMA_FAIL_CLOSED` |
| `testOnly` null / `"true"` / `1` | pass | **reject** | `SCHEMA_FAIL_CLOSED` |
| Unknown extension field | pass | **reject** | `SCHEMA_FAIL_CLOSED` |
| Revision absent / 5-digit / suffixed / leading newline | Error | mixed | Correct |
| Revision **trailing newline** | **pass** | accept | **F-004 (Low)** |
| Mis-cased `candidate` + `approved` | **pass** | accept | **F-003 (Medium)** |
| Mis-cased `stable` | **pass** | accept | **F-003 (Medium)** |
| Whitespace / Unicode lookalike maturity (approval exact) | Error | accept | Fails closed via the approval branch |

No bypass reaches the *pass* state of a contract-recognized Candidate claim. The two
gaps found are a strictness weakness in the new revision pattern and a pre-existing
case-sensitivity gap that the correction neither introduced nor worsened.

## Authority boundary

All five artifacts state the same boundary, with no contradiction: a validator pass
on a coherent Candidate/Approved source proves **metadata coherence and an allowed
revision form only** — never governance authorization, Human-Maintainer approval,
promotion, Stable, conformance, accessibility conformance, complete DTCG conformance,
or publication. Real Candidate authority rests solely with the Candidate Approval
Record, the Nova finalization review, and the Human-Maintainer commit (DEC-S-115,
DEC-S-122, DEC-S-124).

The governing Decisions were checked directly and are **consistent** with the
correction: DEC-S-115 constrains the source set's actual state (which remains
Experimental and unchanged), not the validator's capacity to evaluate a future
Candidate document. **No authority conflict exists.**

The defect recorded below is a *rule-description* inconsistency, not an authority
inconsistency.

## Runtime and execution evidence

Fresh virtual environment created **outside** the repository; no executor venv, no
global environment; installed exclusively from `requirements-validator.lock`
(**7 exact pins**: `attrs 26.1.0`, `jsonschema 4.26.0`,
`jsonschema-specifications 2025.9.1`, `referencing 0.37.0`, `rfc8785 0.1.4`,
`rpds-py 2026.6.3`, `typing_extensions 4.16.0`). After installation the runs used no
network; the harness reports `offlineMode: true`.

Every invocation ran with bytecode writing disabled so the working tree stayed
pristine.

| Run | Python 3.12.10 | Python 3.13.14 |
| --- | --- | --- |
| Targeted `test_semantic_status` | 38/38 pass | — |
| Full unit regression | **111/111 pass**, 0 failures, 0 errors, 0 skips | **111/111 pass** |
| Fixture harness | **24 cases, 24/24 matches**, 0 mismatches, 0 internal errors, exit 0 | **24/24 matches** |

Both sentinels reproduce exactly, and reproduce identically on a second
contract-permitted interpreter, so the result is not interpreter-specific. The
harness bound itself to `repositoryRevision c93cd660…` with `worktreeState: clean`
and retained `independentReviewState: pending`.

The eight new Candidate-metadata tests were identified and executed individually; all
pass. The two pre-existing Candidate/approval tests were re-read and remain
meaningful under the new state machine — one now exercises the fixture boundary, the
other `Approved` without Candidate. No existing test was modified or weakened.

## Regression boundary

Verified unchanged against the parent: `cli.py`, `validation.py`, `diagnostics.py`,
`tests/fixtures/**`, `VALIDATION_CASES.json`, `tokens/semantic/status/**`,
`requirements-validator.lock`, `DECISION_INDEX.md`, `RISK_REGISTER.md`, all ADR
files, the Candidate Dossier, `project-system/**`, `PROJECT_BRAIN.md`, `README.md`,
`CLAUDE.md`, and `CHANGELOG.md`. Expected outcomes and fixtures are untouched.

## Governance reconciliation

Independently re-derived; **nothing was changed**.

| Item | Derived |
| --- | --- |
| Candidate | **No** |
| Source revision | `semantic-status-rev-0001` |
| Maturity | `Experimental` |
| Approval | `Unapproved` |
| Dossier | `Draft – Candidate gate incomplete` |
| Decisions | 124 (DEC-S-001 … DEC-S-124) |
| Risks | 97 (RISK-001 … RISK-097) |
| Risk severity | 53 High · 42 Medium · 2 Low |
| Risk status | 90 Monitored · 7 Mitigating · 0 Accepted · 0 Closed |
| ADRs | 3 |
| CDS-WP-016 | open (`Next`) |
| CDS-WP-017 | not activated (no occurrence in the repository) |
| Publication | `Private Development` |
| Claims | None |
| Pilot | inactive — not started and cannot start |

## Findings

### CDS-WP016-CCR-R2-F-001 — High

- **File:** `docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md:77`
- **Reference:** CDS-WP-016 correction contract; DEC-S-118; CDS conflict rule
  (DEC-S-023, DEC-S-034)
- **Expected:** After the correction, the document states one coherent rule for
  Candidate/approval metadata on Semantic Status documents.
- **Actual:** The document states two contradictory rules. Line 77, in
  *Semantic-status V4 extension (CDS-WP-015)*, still lists the superseded
  unconditional prohibition — "no Candidate/approval statement" — as part of the V4
  rule set, while *Candidate metadata coherence (CDS-WP-016)* at line 137 ff.
  describes the conditional state machine that permits a coherent Candidate/Approved
  source.
- **Evidence:** `sed -n '66,92p'` and `sed -n '134,158p'` on the file at HEAD.
- **Candidate impact:** No promotion and no authority effect. The document is a
  **normative, Elevated** source, so the contradiction cannot be resolved by the
  reviewer: the CDS rule forbids resolving conflicts by recency, and the conservative
  reading (line 77) prohibits exactly the Candidate metadata this correction was
  authorized to enable. The next Candidate finalization run would cite a
  self-contradicting contract.
- **Correction:** Reconcile line 77 with the CDS-WP-016 section — replace the
  unconditional clause with a reference to the Candidate metadata coherence state
  machine. No behavioural change.
- **Recommendation:** Fix before the Candidate finalization resume run.

### CDS-WP016-CCR-R2-F-002 — Medium

- **File:** `tools/cds_validator/semantic_status.py:6-8`
- **Reference:** CDS-WP-016 correction contract
- **Expected:** The module docstring describes the behaviour the module implements.
- **Actual:** The docstring still lists "no Candidate/approval statements" among the
  rules enforced, contradicting the state machine implemented at line 173 ff. of the
  same file.
- **Evidence:** `sed -n '1,13p' tools/cds_validator/semantic_status.py` at HEAD.
- **Candidate impact:** None on authority or behaviour; the code is a class-3
  reference implementation. It misleads maintainers about the module contract.
- **Correction:** Update the docstring to name the maturity/approval state machine.
- **Recommendation:** Fix together with F-001.

### CDS-WP016-CCR-R2-F-003 — Medium

- **File:** `schemas/cds-token-document.schema.json:67-68` with
  `tools/cds_validator/semantic_status.py:195-226`
- **Reference:** CDS-WP-016 state machine; DEC-S-115
- **Expected:** A metadata combination that reads as a Candidate or Stable claim is
  either recognized and evaluated, or rejected.
- **Actual:** `maturityState` and `approvalState` are declared as bare
  `{"type": "string"}` with **no enum**, and the validator compares them by exact
  equality. A document carrying `maturityState: "candidate"` with
  `approvalState: "approved"` — or `maturityState: "stable"` — therefore passes the
  entire pipeline with **zero diagnostics**, schema included.
- **Evidence:** Probes B23/B26 (mis-cased pair, revision left at the manifest value,
  manifest in scope) → no diagnostic; schema probes S04–S06 → accept.
- **Candidate impact:** No Candidate authority is created and no contract-recognized
  Candidate claim passes the gate. **Pre-existing:** the parent behaved identically,
  so the correction neither introduced nor worsened this. It is nevertheless a real
  gap against the newly documented promise that incoherent combinations fail closed.
- **Correction:** Constrain `maturityState` and `approvalState` to enums in
  `cds-token-document.schema.json` (and correspondingly in the manifest schema, which
  already defines such `$defs`).
- **Recommendation:** Separate, explicitly scoped hardening change — **out of scope
  for this correction**; do not fold it into the finalization run.

### CDS-WP016-CCR-R2-F-004 — Low

- **File:** `tools/cds_validator/semantic_status.py:24,211`
- **Reference:** CDS-WP-016 Candidate revision contract; DEC-S-117, DEC-S-122
- **Expected:** A Candidate `sourceRevision` matches the canonical form exactly.
- **Actual:** `CANDIDATE_REVISION_PATTERN.match()` with a `$` anchor accepts a
  **trailing newline**: `"semantic-status-rev-0002-candidate\n"` satisfies the
  Candidate revision gate, and the schema accepts it too (`minLength: 1`, no
  pattern).
- **Evidence:** Probe B13 → validator pass; pattern probe → `match=True`,
  `fullmatch=False`. All other manipulations (leading newline, trailing space, five
  digits, extra suffix, prefix) are correctly rejected.
- **Candidate impact:** Minimal. It grants no authority, requires an embedded newline
  visible in the JSON source, and the manifest identity check fails closed on any
  disagreement. It is nonetheless a strictness gap in code **introduced by this
  correction**, in exactly the mechanism under review.
- **Correction:** Use `fullmatch()` (or the `\Z` anchor).
- **Recommendation:** Fix together with F-001; low urgency.

### CDS-WP016-CCR-R2-F-005 — Observation

`__pycache__` is absent from `.gitignore`, so a validator or test run performed
without disabling bytecode writing leaves untracked directories and dirties the
working tree — directly at odds with the clean-tree discipline every run report
binds to. Pre-existing and out of scope; recorded for a future hygiene change.

### CDS-WP016-CCR-R2-F-006 — Observation

The `digestState.status` enum values use an en-dash (U+2013), consistent with the
pre-existing value. ASCII-hyphen and lowercase variants are correctly rejected,
which is desirable strictness but a plausible operator typo source when the value is
written by hand.

### Finding counts

**Blocking 0 · High 1 · Medium 2 · Low 1 · Observation 2.**

## Review gate

`GO` requires zero Blocking and zero High findings. One High finding stands, so the
gate resolves — as specified, with no `GO WITH NOTES` available — to:

**Recommendation: NO-GO. Status: REWORK REQUIRED. Candidate Decision: No.**

This verdict rests solely on F-001. The independence gate, baseline, correction
delta, resolver schema, state machine, bypass analysis, authority boundary, targeted
tests, all eight probes, the 111/111 regression, the 24/24 harness, the regression
boundary, and the governance reconciliation all passed.

## Boundaries of this review

- Reviewer-produced evidence, bound to revision `c93cd660…`; it does not change
  `independentReviewState`.
- A green regression and a green harness are **not** correctness, conformance, or
  release approval; V2 remains a bounded DTCG subset and V4 automates only the
  objective edge.
- This review promotes nothing, accepts and closes no risk, and grants no maturity.
  Candidate remains **No**; the source set remains Experimental and Unapproved.
- No Git write action of any kind was performed.

## Related documents

- [Contract Correction Notes](../../project-brain/CDS_WP_016_CONTRACT_CORRECTION_NOTES.md)
- [Machine-Readable Validation Contract](../architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)
- [Offline Token Validator Architecture](../architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md)
- [Offline Token Validator Usage](../operations/OFFLINE_TOKEN_VALIDATOR_USAGE.md)
- [Semantic Status Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md)
- [Candidate Gate Recommendation](WP016_CANDIDATE_GATE_RECOMMENDATION.md)
