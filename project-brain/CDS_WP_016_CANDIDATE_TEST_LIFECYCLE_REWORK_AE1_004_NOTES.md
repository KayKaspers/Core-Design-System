# CDS-WP-016 — Candidate Test-Lifecycle Rework and AE1-004 Preparation Notes

Internal work-package evidence for the **CDS-WP-016 Candidate Test-Lifecycle
Rework and AE1-004 Preparation** — a Human-Maintainer-authorized internal rework
of CDS-WP-016, **not** a new work package.

- **Date:** 2026-08-19
- **Human-Maintainer authorization:** 2026-08-19
- **Executed by:** Claude Opus 5 (`claude-opus-5`), scoped Implementation Executor
- **Final status:** Completed — rework and evidence preparation only
- **Authority produced:** **NONE**

> **This rework made seven superseded test premises lifecycle-safe and generated
> fresh, unreviewed evidence. It granted no maturity, no approval, no Candidate
> status, no evidence admission, and no promotion. Nothing was staged, committed,
> or pushed.**

## Authoritative baseline

| Field | Value |
| --- | --- |
| Repository | `D:\Projects\Core-Design-System` |
| Branch | `main` |
| HEAD | `8d1374fa4c61cc1eed214823681ee1209a2d91f7` |
| `origin/main` | `8d1374fa4c61cc1eed214823681ee1209a2d91f7` |
| Parent | `42bcba65aa6767e3f7ebee2a01e496eafcc82a54` |
| Subject | `feat(cds): establish WP-016 candidate finalization governance` |
| Ahead / behind | `0 / 0` |
| Index | **CLEAN** — 0 staged |
| Active Git operation | none |

## The finding this rework closes

**NF-PREP-001 / F-R1**, raised by the fresh independent review of
`AE1-CDS-WP016-SEMSTATUS-003` (**PASS WITH NOTES**).

**Confirmed superseded pre-preparation test premises: 7** — not three. All seven
encoded the pre-preparation lifecycle state (`semantic-status-rev-0001`,
`Experimental`, `Unapproved`) as a fixed assumption in
`tests/validator/test_semantic_status_candidate_evidence.py`.

The shared root was the `execute()` helper, whose `source_revision` default was
the frozen baseline revision even when the evidenced source bytes declared
`semantic-status-rev-0002-candidate`.

### The seven superseded premises

| # | Old test | New test | Strength |
| --- | --- | --- | --- |
| 1 | `ResultFormatV2Tests.test_source_declared_metadata_is_read_from_the_evidenced_bytes` | *(name unchanged)* | STRENGTHENED |
| 2 | `ProposedCandidateContextTests.test_the_real_source_still_declares_the_experimental_revision` | `ProposedCandidateContextTests.test_the_real_source_declares_a_coherent_lifecycle_state` | STRENGTHENED |
| 3 | `ProposedCandidateContextTests.test_no_candidate_revision_artifact_exists_in_the_repository` | `ProposedCandidateContextTests.test_candidate_revision_declarations_stay_in_the_authorized_family` | STRENGTHENED |
| 4 | `ResultBoundaryTests.test_current_run_passes_with_declared_limitations` | *(name unchanged)* | STRENGTHENED |
| 5 | `ResultFormatV2Tests.test_source_revision_mismatch_fails_closed` | *(name unchanged)* | STRENGTHENED |
| 6 | `ResultFormatV2Tests.test_the_source_wins_over_the_cli_argument` | *(name unchanged)* | STRENGTHENED |
| 7 | `RuleCoverageTests.test_expected_and_actual_classifications_agree` | *(name unchanged)* | PRESERVED |

**Assertions weakened: 0.** Tests deleted: 0. Tests skipped: 0. Expected
failures: 0. Test count before: **64**. Test count after: **64**.

One further test — `ResultFormatV2Tests.test_execution_context_is_caller_declared_and_bounded`
— was adjusted for coherence, **not** because its premise was superseded: it
round-tripped whatever authority context the suite declared and never became
false. It now expects the **derived** context, because the helper derives that
declaration from the evidenced bytes instead of stating a frozen
`authoritative-current` literal. **STRENGTHENED.**

**No eighth superseded premise exists after the final static audit; 0 stale
preparation assumptions remain.**

### F-R2 — numerical quantification

**Closed in this record and in the AE1-004 Evidence Record.** The exact seven-test
identity, the old/new test identity, the assertion-strength verdicts, and the
dual-state results are all stated explicitly and numerically.

## Exact-byte identities

### Bound test file

| Field | Value |
| --- | --- |
| Path | `tests/validator/test_semantic_status_candidate_evidence.py` |
| PRE raw SHA-256 | `4b636faacb9e16cdb082022b4aa90ae153b7f7111909a2346b9aec0bc6e187d3` |
| PRE bytes / Git raw object | `35127` / `7f85c64723de961420933b0aa4cc33bf0d602911` |
| POST raw SHA-256 | `93091d4b6f353b19977af0d7aa1b93b9281972152716c8897eca1c2f9e460b70` |
| POST bytes / Git raw object | `43960` / `f275d73a3e9bfafc937dd6dfc967850f9cd11a9c` |
| Changed | **YES** — an actual test lifecycle rework occurred |

### Proposed Candidate Source Manifest — **unchanged**

| Field | Value |
| --- | --- |
| Entries | `3` |
| Byte length | `497` |
| SHA-256 | `3b80d1483ceba4de61c5f9b1f99e10ff00f6da17ac935a1ddfa643a413204ebf` |

```text
M	0d9ff65fb65c9eca3abe5f3bd6bf37492b043c8308191feda9c8319a43c45004	572	d6d75f981ff7d8ad556ce98387453402d458437e	tokens/semantic/status/semantic-status.resolver.json
M	8dda44d28ac654c33892e4c362c83260ba2bd1ab97526ef90dbddb6f72d52ef6	1041	fe7bbf1e7af49f753bd9cd75547ad69a5ae92ca9	tokens/semantic/status/semantic-status.source-set.json
M	53312e93810a6296c2b82b9365d17d14e7e74485cdeb5e13bba149634d4cb55e	6358	7d6b3499d1b291c04e1a3b6eca1b4ca54baf2df2	tokens/semantic/status/semantic-status.tokens.json
```

### AE1-004 machine Evidence Package (NF-R11-001 — the pair)

| Member | Raw SHA-256 | Bytes |
| --- | --- | --- |
| `artifacts/validation/wp016-candidate-finalization-ae1-004-results.json` | `cc918d562a8d7da17f462ce8a3040933d6c5fb850dbb8f85bd07464a2bbae1d0` | `30432` |
| `artifacts/validation/wp016-candidate-finalization-ae1-004-digests.json` | `d8e7732add7be12cea9168483501389f354e0bce36cd6f6309c48f2e6dd1d27a` | `19631` |

Result RFC 8785 content digest:
`sha256:0b299fc99fe96f86075c94a01eb517efbfa37a876386e6d8f7a6acd7c924f96b`.

The Runner Result is **byte-identical** to the `AE1-CDS-WP016-SEMSTATUS-003`
result, because the runner, its inputs, and the evidenced source bytes are all
unchanged. That identity was **derived, not forced**. Identical result bytes are
**not** the same Evidence Package identity once another bound input has changed;
the difference lives in the digest package.

## Evidence states

### `AE1-CDS-WP016-SEMSTATUS-003`

| Field | Value |
| --- | --- |
| Fresh independent review | **PASS WITH NOTES** |
| Evidence admission | **NOT ADMITTED** |
| Admission disposition | **`SUPERSEDED_FOR_ADMISSION_BY_EVIDENCE_INPUT_CHANGE`** |
| Reason | The bound evidence input `tests/validator/test_semantic_status_candidate_evidence.py` changed after its evidence was generated |
| Source bytes changed | **NO** |
| Source revision changed | **NO** |
| Its four files | **byte-identical, unmodified** |

**It was not invalidated by source drift. Stating that would be false.**

### `AE1-CDS-WP016-SEMSTATUS-004`

| Field | Value |
| --- | --- |
| Independent review | **PENDING — not reviewed** |
| Evidence admission | **NOT ADMITTED** |
| Evidence class | **AE-1 Evidence Candidate** |
| Candidate approval | **NOT GRANTED** |
| Candidate promotion | **NOT PERFORMED** |
| Claims / conformance | **none / none** |
| Nature | **Fresh evidence generated after a bound input changed — never an evidence transfer** |

## Test gates

### Real Proposed Candidate working tree (`semantic-status-rev-0002-candidate`)

| Gate | Result | Exit |
| --- | --- | --- |
| `tests.validator.test_semantic_status` | **47 / 47** | `0` |
| `tests.validator.test_semantic_status_candidate_evidence` | **64 / 64** | `0` |
| `unittest discover -s tests/validator` | **184 / 184** | `0` |
| `tools.cds_validator validate-cases` | **24 total, 24 expected matches, 0 mismatches, 0 execution errors** | `0` |

### External committed baseline sandbox (`semantic-status-rev-0001`)

| Gate | Result | Exit |
| --- | --- | --- |
| `tests.validator.test_semantic_status_candidate_evidence` | **64 / 64** | `0` |
| `unittest discover -s tests/validator` | **184 / 184** | `0` |

Sandbox creation: read-only `git archive` of `8d1374fa4c61cc1eed214823681ee1209a2d91f7`
(with `core.eol=lf`, `core.autocrlf=false` so the extracted bytes are the exact
committed blobs — verified for **all 286 tracked blobs**), extracted **outside**
the repository, with **only** the reworked test file overlaid. No `checkout`, no
`worktree add`, no branch, no `reset`, no `stash`. Exactly **one** file in the
sandbox differs from HEAD.

**Same test bytes in both states: YES**
(`93091d4b6f353b19977af0d7aa1b93b9281972152716c8897eca1c2f9e460b70`).

**Classification: `TRANSITION_SAFE_DUAL_STATE_TEST_GATE_PASS`.**

## Deterministic execution

| Item | Result |
| --- | --- |
| Runner executed twice, outputs outside the repository | **byte-identical**, exit `0` / `0` |
| Digest package generated twice, outputs outside the repository | **byte-identical** |
| Persisted result == run A == run B | **YES** |
| Persisted digest package == run A == run B | **YES** |
| Timestamps / absolute paths / usernames / machine ids in evidence | **none** |

Python 3.13.15 in a fresh virtual environment **outside** the repository, exact
pins from `requirements-validator.lock` installed with `pip --isolated`, no extra
package, no upgrade. Network used only for that one dependency bootstrap.
`PYTHONDONTWRITEBYTECODE=1`, `PYTHONNOUSERSITE=1`, external
`PYTHONPYCACHEPREFIX`, `-B` on every invocation. No `__pycache__`, `*.pyc`,
`*.pyo`, coverage output, or temporary file inside the repository.

## What was not changed

| Item | State |
| --- | --- |
| Proposed Candidate source bytes (3 files) | **UNCHANGED** — manifest identity re-verified after the rework |
| `AE1-CDS-WP016-SEMSTATUS-003` (4 files) | **UNCHANGED** — 4 / 4 byte-identical |
| Evidence 001 / 002 / rev-0001 admission record (7 files) | **UNCHANGED** — 7 / 7 byte-identical |
| Evidence runner | **UNCHANGED** |
| Validator (`tools/cds_validator/**`) | **UNCHANGED** |
| Fixtures (`tests/fixtures/**`) | **UNCHANGED** |
| Schemas (`schemas/**`) | **UNCHANGED** |
| `tests/validator/test_semantic_status.py` | **UNCHANGED** |
| `requirements-validator.lock` | **UNCHANGED** |
| Governance, decisions, risks, ADRs, README, CLAUDE.md, project-system | **UNCHANGED** |
| DEC-S-125, DEC-S-126, RISK-098 | **UNCHANGED** |
| Decisions / Risks / ADRs counts | `126` / `98` / `3` — no DEC-S-127, no RISK-099, no ADR-0004 |
| CDS-WP-017 | **INACTIVE** |
| Git writes by Claude | **NONE** |

The only pre-existing tracked file changed by this rework is
`tests/validator/test_semantic_status_candidate_evidence.py`.

## Exact changed and created paths

### Modified (1) — the only pre-existing file touched by this rework

- `tests/validator/test_semantic_status_candidate_evidence.py`

### Created (4)

- `artifacts/validation/wp016-candidate-finalization-ae1-004-results.json`
- `artifacts/validation/wp016-candidate-finalization-ae1-004-digests.json`
- `docs/operations/SEMANTIC_STATUS_CANDIDATE_AE1_004_EVIDENCE_RECORD.md`
- `project-brain/CDS_WP_016_CANDIDATE_TEST_LIFECYCLE_REWORK_AE1_004_NOTES.md`

The three Proposed Candidate source files and the four
`AE1-CDS-WP016-SEMSTATUS-003` files remain in the working tree, unmodified, from
the preceding preparation. Final working tree: **4 modified, 8 untracked, 0
deleted, 0 staged, 12 dirty paths.**

## Authority boundaries — what this rework did not grant

- **Test rework is not evidence admission.**
- **Evidence is not authority.**
- **Proposed Candidate bytes are not Candidate authority.**
- **Target metadata is not current maturity.**
- **`AE1-CDS-WP016-SEMSTATUS-004` is not admitted AE-1.**
- **Evidence admission is not Candidate approval.**
- **Candidate approval is not a Promotion Commit.**
- The **Promotion Commit** remains the actual repository maturity transition
  point (DEC-S-126).
- The committed authoritative state remains `semantic-status-rev-0001`,
  `Experimental`, `Unapproved`, Candidate **No**.
- `semantic-status-rev-0002-candidate` remains **reserved and authorized but not
  promoted**; the repository declares it only in uncommitted working-tree bytes.
- Regression trigger **T-12 is not waived**.
- Git authority, evidence-admission authority, and maturity authority remain
  **exclusively** with the Human Maintainer.

## Required next order

1. **Fresh independent AE1-004 evidence review** (reviewer ≠ executor) — in a
   new session. **No self-review.**
2. Nova evidence / admission adjudication.
3. Human-Maintainer AE1-004 evidence admission.
4. Nova Candidate Finalization Review.
5. Human-Maintainer Candidate approval.
6. Human-Maintainer exact-byte Promotion Commit.
7. Post-commit full regression and exact-byte verification.

No gate may be skipped.

## Skills used

| Skill | Path | Purpose |
| --- | --- | --- |
| `ndf-work-package-runner` | `.claude/skills/ndf-work-package-runner/SKILL.md` | Execution frame, guardrails, closing structure |
| `ndf-validation-evidence-reviewer` | `.claude/skills/ndf-validation-evidence-reviewer/SKILL.md` | Honest evidence classification and limit statements |
| `ndf-release-safety` | `.claude/skills/ndf-release-safety/SKILL.md` | Promotion/release boundary discipline |
| `ndf-adr-governance-review` | `.claude/skills/ndf-adr-governance-review/SKILL.md` | ADR-need check — result: **no ADR required** |
| `ndf-context-pack-maintainer` | `.claude/skills/ndf-context-pack-maintainer/SKILL.md` | Handover consistency (read-only in this rework) |
| `ndf-compact-context-summary-runner` | `.claude/skills/ndf-compact-context-summary-runner/SKILL.md` | Closing report and compact context summary |

Skills grant no Git, admission, approval, or maturity authority. Where a skill's
generic docs-only boundary met the explicitly Human-Maintainer-authorized test
execution of this rework, the **work-package prompt governed** and the skill
boundary was treated as procedural guidance only.

## Related documents

- [AE1-004 Evidence Record](../docs/operations/SEMANTIC_STATUS_CANDIDATE_AE1_004_EVIDENCE_RECORD.md)
- [AE1-003 Evidence Record](../docs/operations/SEMANTIC_STATUS_CANDIDATE_AE1_PROPOSED_CANDIDATE_EVIDENCE_RECORD.md)
- [Candidate Finalization Preparation notes](CDS_WP_016_CANDIDATE_FINALIZATION_PREPARATION_NOTES.md)
- [AE-1 Admission Record](../docs/governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md)
- [Candidate Approval Record Template](../docs/operations/CANDIDATE_APPROVAL_RECORD_TEMPLATE.md) — a template; **no instance exists**
