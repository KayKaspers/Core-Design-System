# WP-016 Contract Correction Rework R1 — Independent Review (R3)

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Independent Rework Review R3
- **Date:** 2026-08-12
- **Reviewed revision:** `8da3fde52c9f30282f9dbc3714a8edca7f9b6902`
- **Parent revision:** `fe0339fe15850e2d16c59de80519bbddfca5e642`
- **Status:** **Reviewer-produced, revision-bound, non-promotional.** This review
  approves nothing, promotes nothing, and grants no maturity. It is an input to a
  Nova review and a Human-Maintainer decision, never a substitute for either.
- **Result:** **COMPLETE** · **Recommendation: GO** · **Candidate: No**

## Scope and independence

This review examines exactly the committed Rework R1 commit against its parent. It
re-derives every sentinel from the repository and from its own execution rather than
accepting the executor's recorded evidence.

The reviewer context is a fresh session that did not execute the rework, did not edit
the validation contract, did not edit the validator, did not add the trailing-newline
regression test, and did not create the rework notes. Its only inputs are the
committed repository state, the committed rework diff, the committed rework notes,
and the authorized normative CDS artifacts — all legitimate review sources, not
executor session memory.

**Independence gate: PASS.**

This review closes the loop the R1 notes left open. The executor's own evidence was
produced on a **modified worktree** and was explicitly marked as not quotable for a
committed state. The runs recorded here bind to the **committed** revision
`8da3fde…` with a **clean** working tree and index, on a **different interpreter**
(Python 3.13.14) from the executor's (3.12.10).

## Summary

The rework is **exact, minimal, and complete against its three declared findings**.

F-001 is closed in the normative, Elevated contract document: the superseded
unconditional clause is gone, the accurate rule name replaces it, and an explicit
boundary paragraph now names the state machine and the authority limit. No sentence
anywhere in that document still asserts an unconditional Candidate/`Approved`
prohibition, and the cross-reference resolves to a real section.

F-002 is closed: the module docstring now describes the same three-branch state
machine the code implements, including the authority boundary.

F-004 is closed and is a **real behavioural change**, not a cosmetic one. The
reviewer reproduced the defect independently: on the unchanged pattern, the parent's
`.match()` accepts a trailing-newline Candidate revision, and the committed
`.fullmatch()` rejects it while the valid revision still passes.

F-003 remains untouched and deferred — `schemas/` is byte-identical to the parent.
F-005 and F-006 are untouched. Nothing outside the authorized four-file delta moved.
All four sentinels reproduce exactly: 39/39 targeted, 4/4 probes, 112/112 full
regression, 24/24 harness.

No Blocking, High, Medium, or Low finding was raised. Two Observations are recorded;
neither bears on Candidate status and neither calls for action in this work package.

## Repository reconciliation

| Item | Expected | Derived | Result |
| --- | --- | --- | --- |
| Repository root | `D:\Projects\Core-Design-System` | identical | PASS |
| Branch | `main` | `main` | PASS |
| HEAD | `8da3fde…` | `8da3fde52c9f30282f9dbc3714a8edca7f9b6902` | PASS |
| HEAD subject | as specified | `fix(cds): close semantic status contract review findings` | PASS |
| Parent | `fe0339f…` | `fe0339fe15850e2d16c59de80519bbddfca5e642` | PASS |
| Parent subject | as specified | `docs(cds): record independent contract correction review` | PASS |
| `HEAD == origin/main` | yes | identical SHA | PASS |
| Working tree | clean | clean (before and after execution) | PASS |
| Index | clean | clean (before and after execution) | PASS |
| Merge / rebase / cherry-pick | none | none | PASS |
| Untracked files | none | none (before and after) | PASS |
| `origin` | present, plausible | `github.com/KayKaspers/Core-Design-System` | PASS |
| Tags | — | 0 | PASS |
| `git diff --check` | clean | clean | PASS |

## Rework delta

`git diff --name-status fe0339f..8da3fde` yields exactly four entries — three
modified, one added, none deleted:

| Status | Path | +/− |
| --- | --- | --- |
| M | `docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md` | +14 / −6 |
| M | `tools/cds_validator/semantic_status.py` | +11 / −3 |
| M | `tests/validator/test_semantic_status.py` | +7 / −0 |
| A | `project-brain/CDS_WP_016_CONTRACT_CORRECTION_R1_NOTES.md` | +171 / −0 |

Totals: **203 insertions, 9 deletions, 4 files**. There is no fifth file and no
deletion. The full diff was reviewed line by line, not only the file names: two hunks
in the contract, two in the validator (docstring, matcher), one in the tests.

**Delta scope: PASS.**

## F-001 — Normative contract self-contradiction (was High)

File: `docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md`.

| # | Required | Derived | Result |
| --- | --- | --- | --- |
| 1 | The unconditional `no Candidate/approval statement` clause is removed | The rule list at line 77 now reads `maturity/approval metadata coherence`; the phrase occurs nowhere in the document | PASS |
| 2 | Replaced by a maturity/approval coherence description | Lines 77–78 and the new paragraph at lines 88–94 | PASS |
| 3 | `Experimental` coherent only with `Unapproved` | Line 88–89, and line 150 in the binding section | PASS |
| 4 | `Candidate` structurally coherent only with `Approved` + Candidate revision + non-fixture | Lines 89–91, and lines 151–155 | PASS |
| 5 | `Stable` remains inadmissible | Line 91 (`remains inadmissible under the current contract`); line 156 (`stays outside this contract`) | PASS |
| 6 | A pass proves metadata coherence only | Lines 91–92; lines 159–161 | PASS |
| 7 | The validator never grants Candidate governance authority | Line 92; lines 159–164 name the Candidate Approval Record, the Nova finalization review, and the Human-Maintainer commit as the sole sources | PASS |

Every occurrence of `Candidate`, `Approved`, `approval`, `maturity`, and `authority`
in the document was evaluated semantically (lines 57, 66–67, 77, 88–93, 109, 133,
142, 145–164, 169). Two need explicit clearing:

- **Line 142–143** — "confer **no Candidate, Stable, conformance, or claim status**".
  This is scoped to the CDS-WP-013 *execution evidence* and states what evidence does
  not confer. It is an authority statement, not a prohibition on declaring metadata,
  and is consistent with the new rule.
- **Line 67** — V4 checks "maturity; approval". A check list, not a prohibition.

**No contradictory unconditional Candidate/`Approved` prohibition remains anywhere in
the document.**

The new cross-reference `(#candidate-metadata-coherence-cds-wp-016)` at line 93
resolves to the real H2 `## Candidate metadata coherence (CDS-WP-016)` at line 145,
which pre-existed at the parent. The link is not dangling.

**F-001: CLOSED.**

## F-002 — Stale validator module docstring (was Medium)

File: `tools/cds_validator/semantic_status.py`.

The docstring (lines 1–21) was compared clause by clause against the state machine
(lines 203–234):

| Docstring claim | Implementation | Result |
| --- | --- | --- |
| `Experimental` coherent with `Unapproved` | No branch fires; no diagnostic | PASS |
| `Candidate` only with `Approved`, a Candidate source revision, and a non-fixture source | Lines 208–226: fixture → error; `approval != "Approved"` → error; revision failing `fullmatch` → error; otherwise no diagnostic | PASS |
| `Stable` stays rejected | Lines 203–207 emit `CDS-V4-STATUS-IDENTITY` | PASS |
| A pass proves coherence only and never grants Candidate governance authority | Docstring lines 12–16 and the in-code authority-boundary comment at lines 188–195; no code path sets or grants any status | PASS |

The superseded phrase "no Candidate/approval statements" is gone from the module.
The docstring and the state machine agree. See OBS-002 for one residual imprecision
that is bound to the deferred F-003 and does not reopen this finding.

**F-002: CLOSED.**

## F-004 — Candidate revision matcher hardening (was Low)

File: `tools/cds_validator/semantic_status.py`, line 220.

The **only** matcher change is `CANDIDATE_REVISION_PATTERN.match(revision)` →
`CANDIDATE_REVISION_PATTERN.fullmatch(revision)`.

| Required | Derived | Result |
| --- | --- | --- |
| Pattern unchanged | `^semantic-status-rev-[0-9]{4}-candidate$` at parent line 24 and HEAD line 32 — byte-identical | PASS |
| No other state-machine logic changed | The validator diff contains exactly two hunks: the docstring and this one line | PASS |
| No diagnostics changed | `CDS-V4-STATUS-IDENTITY` is the only code emitted; no code added, renamed, or removed | PASS |
| No error messages changed | All four message strings are identical to the parent | PASS |
| A valid Candidate revision stays accepted | Probe P1: no identity diagnostic | PASS |
| A trailing newline is rejected fail-closed | Probe P2: `CDS-V4-STATUS-IDENTITY` | PASS |

The reviewer confirmed the change is behaviourally meaningful by reproducing the
defect independently on the unchanged pattern:

| Input | parent `.match` | HEAD `.fullmatch` |
| --- | --- | --- |
| `semantic-status-rev-0002-candidate` | accepted | accepted |
| `semantic-status-rev-0002-candidate\n` | **accepted (the defect)** | **rejected** |

This is the documented Python behaviour of `$`, which also matches immediately before
a trailing newline. The fix is correct and minimal.

**F-004: CLOSED.**

## Regression test review

File: `tests/validator/test_semantic_status.py`.

Comparing the parent and HEAD test-name sets: **38 → 39 tests**, exactly one added,
**none removed**.

- Added: `test_candidate_revision_trailing_newline_fails`, in the existing
  `SemanticStatusMaturityApprovalTests` class.
- Semantics: `Candidate` + `Approved` + `"semantic-status-rev-0002-candidate\n"` on a
  non-fixture source must produce `CDS-V4-STATUS-IDENTITY`. The shared
  `assert_identity_error` helper asserts exactly one such diagnostic — an equality
  assertion, not a membership check, so it cannot pass by accident.
- No existing assertion was weakened; the test file diff is purely additive (+7/−0).
- The valid Candidate revision stays separately covered by the untouched
  `test_candidate_approved_valid_revision_passes`.

**Regression test: PASS.**

## Deferred findings

| Finding | Required state | Derived | Result |
| --- | --- | --- | --- |
| **F-003** (Medium) — no enums on `maturityState`/`approvalState` | unchanged, deferred | `git diff fe0339f..8da3fde -- schemas/` is **empty**; `schemas/cds-token-document.schema.json` lines 67–68 and 87–88 still declare both as bare `{ "type": "string" }`; no new diagnostic introduced | **Unchanged — remains a deferred hardening need** |
| **F-005** (Observation) — `__pycache__` not ignored | unchanged | `.gitignore` byte-identical to the parent; `git check-ignore` confirms `__pycache__` is still not ignored | Unchanged |
| **F-006** (Observation) — en-dash in the digest-state enum | unchanged | `schemas/cds-resolver-document.schema.json` byte-identical; both `Not computed – …` enum values retain the en-dash | Unchanged |

No opportunistic cleanup was performed by the rework, and none was performed by this
review.

## Authority boundary

Checked for consistency across all five required documents:

| Document | Statement | Result |
| --- | --- | --- |
| `tools/cds_validator/semantic_status.py` | Docstring lines 12–16 and comment lines 188–195: coherence only; authority external | PASS |
| `docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md` | Lines 91–94 and 159–164: "A validator pass is not governance authorization" | PASS |
| `docs/architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md` | Lines 105–109 and 119: "not governance authorization"; "a coherence pass is not a maturity grant" | PASS |
| `docs/operations/OFFLINE_TOKEN_VALIDATOR_USAGE.md` | Lines 106–110 and 117: "A validator pass is not a maturity grant"; the CLI "never awards a maturity level" | PASS |
| `docs/foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md` | Lines 138–155: "Candidate authority lives outside the token document and the validator" | PASS |

All five agree that a validator pass means **metadata coherence, Candidate-revision
validity, and non-fixture status only**, and that it means neither Nova approval,
Human-Maintainer approval, Candidate promotion, Stable, conformance, accessibility
conformance, complete DTCG conformance, nor publication. All five name the same three
external sources of real authority (DEC-S-115, DEC-S-122, DEC-S-124).

**No Candidate-relevant contradiction. Authority boundary: CONSISTENT.**

## Runtime and dependencies

| Item | Derived |
| --- | --- |
| Virtual environment | Created fresh **outside** the repository, in the session scratchpad |
| Python | **3.13.14** (CPython, win32 / Windows 11) — satisfies the ≥ 3.11 requirement (DEC-S-093, ADR-0003); deliberately a different interpreter from the executor's 3.12.10 |
| Source | `requirements-validator.lock` only |
| Direct dependencies | 2 — `jsonschema==4.26.0`, `rfc8785==0.1.4` |
| Transitive dependencies | 5 — `attrs==26.1.0`, `jsonschema-specifications==2025.9.1`, `referencing==0.37.0`, `rpds-py==2026.6.3`, `typing_extensions==4.16.0` |
| **Exact pins** | **7** — all installed at the pinned versions, verified by `pip list --format=freeze` |
| Bytecode | `PYTHONDONTWRITEBYTECODE=1` plus `python -B`; no `__pycache__` was created anywhere in the repository |
| Runtime network | **None after installation.** The validator resolves schemas from a local registry; no network call is made at run time |

## Executed evidence

All four sentinels were re-derived by execution, not read from the executor's record.

### Targeted tests

`python -B -m unittest tests.validator.test_semantic_status -v`

| Expected | Actual |
| --- | --- |
| 39 | **39** |

**39 passed · 0 failed · 0 errors · 0 skipped · exit 0.** PASS.

### Direct probes

Executed in-memory from a reviewer-authored script outside the repository, building
the probe documents from scratch rather than reusing the committed test helper.

| Probe | Input | Expected | Actual | Result |
| --- | --- | --- | --- | --- |
| P1 | `Candidate` + `Approved` + `semantic-status-rev-0002-candidate` | no `CDS-V4-STATUS-IDENTITY` | 0 diagnostics | MATCH |
| P2 | `Candidate` + `Approved` + `semantic-status-rev-0002-candidate\n` | `CDS-V4-STATUS-IDENTITY` | 1 × `CDS-V4-STATUS-IDENTITY` ("a Candidate revision must match 'semantic-status-rev-NNNN-candidate'") | MATCH |
| P3 | `Candidate` + `Approved` + `semantic-status-rev-0002` | `CDS-V4-STATUS-IDENTITY` | 1 × `CDS-V4-STATUS-IDENTITY` (same message) | MATCH |
| P4 | `Stable` + `Approved` | `CDS-V4-STATUS-IDENTITY` | 1 × `CDS-V4-STATUS-IDENTITY` ("Stable maturity is out of contract") | MATCH |

**4/4 MATCH.** PASS.

### Full regression

`python -B -m unittest discover -s tests/validator` (the command documented in the
validator usage guide).

| Expected | Actual |
| --- | --- |
| 112 | **112** |

**112 passed · 0 failures · 0 errors · 0 skips · exit 0.** PASS.

### Validation harness

`python -B -m tools.cds_validator validate-cases tests/fixtures/machine-readable/VALIDATION_CASES.json`

| Item | Expected | Actual |
| --- | --- | --- |
| Cases | 24 | **24** |
| Expected/actual matches | 24 | **24** |
| Mismatches | 0 | **0** |
| Internal errors | 0 | **0** |
| Exit code | 0 | **0** |

Canonicalization `RFC 8785 (JSON Canonicalization Scheme)`, digest `SHA-256`.
Fixtures, `VALIDATION_CASES.json`, and all expected outcomes are byte-identical to
the parent. PASS.

## Regression boundary

`git diff --name-status fe0339f..8da3fde` restricted to the protected paths returns
**empty** for every one of them:

`schemas/**` · `tools/cds_validator/cli.py` · `tools/cds_validator/validation.py` ·
`tools/cds_validator/diagnostics.py` · `tests/fixtures/**` ·
`tests/fixtures/machine-readable/VALIDATION_CASES.json` · `tokens/semantic/status/**` ·
`requirements-validator.lock` · `docs/decisions/**` (including all ADRs) ·
`docs/risks/**` · the Candidate Dossier · `project-system/**` ·
`project-brain/PROJECT_BRAIN.md` · `README.md` · `CLAUDE.md` · `CHANGELOG.md` ·
`.claude/**`.

The single `project-brain/` addition is the rework notes file; `PROJECT_BRAIN.md`
itself is untouched.

**Regression boundary: PASS.**

## Governance reconciliation

Every value re-derived from the repository, not copied from the prompt.

| Item | Expected | Derived | Source | Result |
| --- | --- | --- | --- | --- |
| Candidate | No | **No** — "Candidate Status = Not Candidate" | Candidate Dossier | PASS |
| Source revision | `semantic-status-rev-0001` | `semantic-status-rev-0001` in both the token document and the manifest entry | `tokens/semantic/status/` | PASS |
| Maturity | Experimental | `maturityState: Experimental` | source set + manifest | PASS |
| Approval | Unapproved | `approvalState: Unapproved` | source set + manifest | PASS |
| Dossier | Draft – Candidate gate incomplete | "Draft – Candidate gate incomplete" | Candidate Dossier | PASS |
| Decisions | 124 | **124** (highest `DEC-S-124`) | Decision Index | PASS |
| Risks | 97 | **97** (highest `RISK-097`) | Risk Register | PASS |
| Risk distribution | — | Initial severity: High 53 · Medium 42 · Low 2. Status: Monitored 90 · Mitigating 7 · **Accepted 0 · Closed 0** | Risk Register | PASS |
| ADRs | 3 | **3** (ADR-0001, ADR-0002, ADR-0003) | `docs/decisions/` | PASS |
| CDS-WP-016 | open | registered `Next`, not completed | Work Packages | PASS |
| CDS-WP-017 | not activated | absent from the work-package table | Work Packages | PASS |
| Phase | Pre-Candidate Operating Enablement | unchanged | project control | PASS |
| Publication | Private Development | `Private Development` | README, Context Pack | PASS |
| Claims | None | "No claim is currently valid, by anyone" | Context Pack | PASS |
| Pilot | inactive | "CoreOps pilot inactive" | Candidate Dossier | PASS |

**Governance: UNCHANGED by the rework.**

## Findings

**0 Blocking · 0 High · 0 Medium · 0 Low · 2 Observations.**

### CDS-WP016-R3-OBS-001 — The `.match()` anchor-defect class persists outside the reviewed scope

- **Severity:** Observation
- **Files:** `tools/cds_validator/graph.py:41`; `tools/cds_validator/validation.py:142`, `:231`, `:239`, `:693`, `:791`
- **Reference:** the same root cause as F-004; DEC-S-078 (fail-closed)
- **Expected:** F-004 closes the trailing-newline acceptance at the Candidate-revision
  matcher, which it does.
- **Actual:** Six further call sites apply `.match()` to `$`-anchored patterns
  (`SOURCE_SET_ID_RE`, `JSON_POINTER_RE`, `ALIAS_RE`, `NAME_SEGMENT_RE`, and the
  inline `^DEC-S-[0-9]{3}$` / `^CR-[0-9]{3}$` provenance patterns) and would therefore
  accept a trailing newline in the same way.
- **Evidence:** `grep -rn "\.match(" tools/cds_validator/` against the committed HEAD;
  the pattern definitions at `graph.py:16` and `validation.py:53–56` all end with `$`.
- **Candidate impact:** **None.** These sites govern source-set identity, references,
  naming, and provenance — not Candidate authority. Candidate coherence additionally
  requires an exact `maturityState == "Candidate"` and `approvalState == "Approved"`
  string comparison, and `sourceSetId` is compared by equality against the manifest,
  so a trailing newline there fails closed rather than bypassing anything.
- **Status:** Pre-existing at the parent; neither introduced nor worsened by R1;
  outside the authorized four-file scope. F-004 was scoped to the Candidate-revision
  matcher and is fully closed at that scope.
- **Required correction:** None in this work package.
- **Recommendation:** Register for a separately scoped hardening work package
  alongside F-003. **Not a NO-GO trigger.**

### CDS-WP016-R3-OBS-002 — Docstring precision on non-enumerated approval values

- **Severity:** Observation
- **File:** `tools/cds_validator/semantic_status.py:10–11`
- **Reference:** F-002; deferred F-003
- **Expected:** The docstring statement "`Experimental` is coherent only with
  `Unapproved`" describes what the state machine enforces.
- **Actual:** The state machine's final branch is `elif approval == "Approved"`, so
  `Experimental` combined with any approval value **other than** `Approved` (for
  example an unrecognized string) passes without a diagnostic.
- **Evidence:** `semantic_status.py:227–234`; `schemas/cds-token-document.schema.json:67–68`
  types `approvalState` as a bare string with no enum.
- **Candidate impact:** **None.** The Candidate branch requires
  `maturityState == "Candidate"` exactly, and then `approvalState == "Approved"`
  exactly, so no unrecognized value can produce a coherent Candidate.
- **Status:** This is the deferred **F-003** root cause (no enums on
  `maturityState`/`approvalState`), not a new code/docstring divergence. The
  docstring is faithful to the normative contract, which uses the same wording
  (`MACHINE_READABLE_VALIDATION_CONTRACT.md:150`). **It does not reopen F-002.**
- **Required correction:** None in this work package.
- **Recommendation:** Fold into the F-003 schema-hardening work package.
  **Not a NO-GO trigger.**

For completeness: `docs/architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md:35`
still summarizes the module as performing "approval-statement and manifest-identity
checks". This names a check, not a prohibition, is unchanged from the parent, and is
correctly expanded by the same document's CDS-WP-016 section at lines 86–109. It is
not a normative conflict and is not raised as a finding.

## Review gate

| Gate criterion | Required | Derived |
| --- | --- | --- |
| Independence | PASS | PASS |
| Blocking findings | 0 | 0 |
| High findings | 0 | 0 |
| Rework scope | exactly four files | exactly four files |
| F-001 | closed | closed |
| F-002 | closed | closed |
| F-004 | closed | closed |
| F-003 | unchanged / deferred | unchanged / deferred |
| F-005 | unchanged | unchanged |
| F-006 | unchanged | unchanged |
| Authority boundary | consistent | consistent |
| Targeted tests | 39/39 | 39/39 |
| Direct probes | 4/4 | 4/4 |
| Full regression | 112/112 | 112/112 |
| Harness | 24/24 | 24/24 |
| Candidate | remains No | remains No |
| Governance | unchanged | unchanged |

**Every gate criterion is met. Recommendation: GO.** There is no
"GO WITH NOTES" outcome in this review.

## Limits of this review

- This review is **evidence and analysis, not approval**. It promotes nothing, sets
  no maturity, closes no risk, and accepts no risk.
- It confirms that the rework closes F-001, F-002, and F-004 and introduces no
  regression. It is **not** a statement that the Semantic Status Foundation is
  Candidate-ready; that gate is separate and remains incomplete.
- Coverage is bounded to the reviewed diff, the named authority documents, the
  committed test suite, and the committed 24-case matrix. V2 remains a bounded DTCG
  subset (DEC-S-098); V4 automates only the objective edge.
- The evidence binds to `8da3fde…` on Python 3.13.14 with a clean worktree. A
  different interpreter or a changed revision requires re-execution.
- Every CDS artifact remains **AE-0**. No accessibility test was run, and this review
  makes no accessibility statement.
- No Git write action of any kind was performed.

## Related documents

- [Machine-Readable Validation Contract](../architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)
- [Offline Token Validator Architecture](../architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md)
- [Offline Token Validator Usage](../operations/OFFLINE_TOKEN_VALIDATOR_USAGE.md)
- [Semantic Status Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md)
- [WP-016 Contract Correction Independent Review (R2)](WP016_CONTRACT_CORRECTION_INDEPENDENT_REVIEW.md)
- [Semantic Status Candidate Dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md)
- [Rework R1 Notes](../../project-brain/CDS_WP_016_CONTRACT_CORRECTION_R1_NOTES.md)
- [Reviewer Notes (R3)](../../project-brain/CDS_WP_016_CONTRACT_CORRECTION_R1_INDEPENDENT_REVIEW_NOTES.md)
