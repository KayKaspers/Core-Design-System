# CDS-WP-016 — Contract Correction Rework R1 Notes

*Non-normative working notes for the CDS-WP-016 Contract Correction Rework R1
(normative contract reconciliation and Candidate revision matcher hardening). This
run performs **no** Candidate promotion and **no** status advancement. It does not
change the main [PROJECT_BRAIN](PROJECT_BRAIN.md), any decision, risk, or ADR, any
schema, any source set, or any project-status file.*

## Baseline

- **Starting HEAD:** `fe0339fe15850e2d16c59de80519bbddfca5e642` —
  `docs(cds): record independent contract correction review`, identical to
  `origin/main`; working tree and index clean; no merge, rebase, or cherry-pick.
- **Independent Review commit:** the same `fe0339f…`, a direct child of the technical
  correction `c93cd660ba6a8fe9ee9e54ec1e165d3f1ad1d5ed`, adding exactly the two
  reviewer artifacts and modifying or deleting nothing.
- **Committed technical baseline:** 111 unit tests, 24 validation cases, 24/24
  harness matches, Candidate No, `semantic-status-rev-0001`, Experimental,
  Unapproved.

This rework closes three findings of the
[Independent Review](../docs/reviews/WP016_CONTRACT_CORRECTION_INDEPENDENT_REVIEW.md):
F-001 (High), F-002 (Medium), and F-004 (Low).

## F-001 — Normative contract self-contradiction (High)

File: `docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md`.

The *Semantic-status V4 extension (CDS-WP-015)* section still listed the superseded
unconditional rule "no Candidate/approval statement" while the later CDS-WP-016
section described the conditional state machine — so the normative, Elevated document
asserted both rules at once.

**Edit 1 — the rule list.** The stale clause is replaced by the accurate rule name:

- **Before:** `aggregate- and appearance-role prohibition, no Candidate/approval
  statement, and source/manifest identity agreement`
- **After:** `aggregate- and appearance-role prohibition, maturity/approval metadata
  coherence, and source/manifest identity agreement`

**Edit 2 — an explicit boundary paragraph** closing the section, stating that
`Experimental` is coherent only with `Unapproved`; `Candidate` only together with
`Approved`, a Candidate source revision, and a non-fixture source; that `Stable`
remains inadmissible under the current contract; that a pass proves **metadata
coherence only**; and that it **never grants Candidate governance authority** — with
a link to the binding CDS-WP-016 section.

No other semantic change. After the edit **no sentence anywhere in the document
claims that Candidate metadata or `Approved` is unconditionally forbidden**, and no
sentence claims the validator confers governance authority.

## F-002 — Stale validator module docstring (Medium)

File: `tools/cds_validator/semantic_status.py`.

The module docstring still advertised "no Candidate/approval statements" as an
enforced rule, contradicting the state machine in the same file.

- **Before:** `… no aggregate or appearance-oriented status roles, no
  Candidate/approval statements, and source/manifest identity agreement.`
- **After:** the same list with `maturity/approval metadata coherence`, plus a short
  paragraph naming the actual contract: Experimental only with Unapproved; Candidate
  only with Approved, a Candidate source revision, and a non-fixture source; Stable
  stays rejected; a pass proves coherence only and never grants Candidate governance
  authority (DEC-S-115, DEC-S-122, DEC-S-124).

Documentation only — **no runtime behaviour changed by this edit**.

## F-004 — Candidate revision matcher hardening (Low)

File: `tools/cds_validator/semantic_status.py`.

Python's `$` anchor also matches immediately before a trailing newline, so
`re.match()` accepted `"semantic-status-rev-0002-candidate\n"` as a valid Candidate
revision.

- **Before:** `CANDIDATE_REVISION_PATTERN.match(revision)`
- **After:** `CANDIDATE_REVISION_PATTERN.fullmatch(revision)`

**The pattern itself is unchanged:** `^semantic-status-rev-[0-9]{4}-candidate$`. This
is a one-call change; no other state-machine logic, diagnostic code, message, or
branch was touched, as the diff confirms.

Behavioural effect — the valid Candidate revision still passes, the trailing-newline
variant now fails closed, and every previously rejected form stays rejected:

| Revision | `.match` (before) | `.fullmatch` (after) |
| --- | --- | --- |
| `semantic-status-rev-0002-candidate` | accepted | accepted |
| `semantic-status-rev-0002-candidate\n` | **accepted** | **rejected** |
| `…-candidate\n\n`, `\n…-candidate`, `…-candidate `, `…-candidate-x`, 5-digit | rejected | rejected |

## Test — exactly one new regression test

`tests/validator/test_semantic_status.py`, one test added to the existing
`SemanticStatusMaturityApprovalTests`:

`test_candidate_revision_trailing_newline_fails` — Candidate + Approved +
`"semantic-status-rev-0002-candidate\n"` on a non-fixture source must emit
`CDS-V4-STATUS-IDENTITY`.

The valid-revision case is already covered by the existing
`test_candidate_approved_valid_revision_passes`, so no second test was added. No
existing test was modified, weakened, or removed; no fixture and no validation case
was touched.

## Validation results

Runtime: the venv outside the repository from the R2 review, Python 3.12.10, exact
`requirements-validator.lock` pins, no runtime network. Every invocation ran with
bytecode writing disabled so no `__pycache__` was created in the repository.

- **Targeted:** `tests/validator/test_semantic_status.py` — **39/39 passed**
  (38 existing + 1 new), 0 failures, 0 errors, 0 skips.
- **Direct probes:** **4/4 as expected** — A valid Candidate revision → no identity
  error; B trailing newline → `CDS-V4-STATUS-IDENTITY`; C non-Candidate revision →
  `CDS-V4-STATUS-IDENTITY`; D Stable + Approved → `CDS-V4-STATUS-IDENTITY`.
- **Full regression:** **112/112 passed** (baseline 111 + 1), 0 failures, 0 errors,
  0 skips.
- **Harness:** **24 cases, 24/24 expected/actual matches**, 0 mismatches, 0 internal
  errors, exit 0. Fixtures, `VALIDATION_CASES.json`, and expected outcomes unchanged.
- **Contract consistency search** across all four correction-scope documents plus the
  validator module: **no remaining unconditional Candidate/Approved prohibition**. No
  new contradiction was found in the three documents outside this run's scope, so no
  scope extension was required.

**Evidence honesty:** these runs report `worktreeState: modified worktree` and bind
to uncommitted content. They are **not** a committed-revision result and must not be
quoted as one. Evidence for a committed state requires a re-run after the
Human-Maintainer commit.

## Deferred and untouched

- **F-003 (Medium) — deliberately deferred.** `schemas/cds-token-document.schema.json`
  still types `maturityState`/`approvalState` as bare strings without enums, so a
  mis-cased `candidate`/`stable` passes silently. This is pre-existing, was neither
  introduced nor worsened by the contract correction, and produces no successful
  contract-recognized Candidate claim. **No schema was changed in this run.** It
  remains an open schema-hardening need for a separate, explicitly scoped work
  package.
- **F-005 (Observation)** — `__pycache__` / `.gitignore`: unchanged.
- **F-006 (Observation)** — en-dash in the digest-state enum: unchanged.

## Explicitly NOT done

No Candidate promotion; no Candidate/Stable metadata on the real source set, manifest,
or resolver instance; no Candidate Approval Record; the Candidate Dossier stays
`Draft – Candidate gate incomplete`; no schema change; no source-set change; no
project-status advancement; no new Decision, Risk, or ADR; no risk-status change;
publication stays Private Development; claims none; pilot inactive; no Git write
action of any kind.

## Changed files (4 Allowed Files)

1. `docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md` — F-001 reconciliation.
2. `tools/cds_validator/semantic_status.py` — F-002 docstring, F-004 `fullmatch`.
3. `tests/validator/test_semantic_status.py` — one F-004 regression test.
4. `project-brain/CDS_WP_016_CONTRACT_CORRECTION_R1_NOTES.md` — this file.

## Next step

Nova review of this rework, then the Human-Maintainer commit. Afterwards the R2 gate
can be re-run against the committed state, and only then does the Candidate
finalization resume run become executable. F-003 stays queued separately.

## Related

- [Contract Correction Independent Review](../docs/reviews/WP016_CONTRACT_CORRECTION_INDEPENDENT_REVIEW.md)
- [Independent Review Notes](CDS_WP_016_CONTRACT_CORRECTION_INDEPENDENT_REVIEW_NOTES.md)
- [Contract Correction Notes](CDS_WP_016_CONTRACT_CORRECTION_NOTES.md)
- [Machine-Readable Validation Contract](../docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)
