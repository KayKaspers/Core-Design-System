# CDS-WP-016 — Contract Correction Rework R1 Independent Review (R3) Notes

*Non-normative reviewer working notes for the CDS-WP-016 Independent Rework Review
R3. This run performs **no** implementation, schema, test, fixture, case, or
governance change, **no** Candidate promotion, and **no** Git write action. It adds
exactly two review artifacts and modifies or deletes nothing.*

## Reviewer independence

Fresh session. It did not execute the Rework R1, did not edit
`MACHINE_READABLE_VALIDATION_CONTRACT.md`, did not edit `semantic_status.py`, did not
add the trailing-newline regression test, and did not create
`CDS_WP_016_CONTRACT_CORRECTION_R1_NOTES.md`. No executor working context was
inherited; the rework is visible only as committed evidence.

**Independence gate: PASS** — evaluated before any repository analysis and before any
Skill was loaded, as the prompt requires.

Two deliberate independence measures beyond the gate:

1. **A different interpreter.** Python 3.13.14 rather than the executor's 3.12.10,
   so the sentinels are not reproduced on an identical stack.
2. **Reviewer-authored probes.** The four direct probes build their documents from
   scratch instead of reusing the committed `SemanticStatusMaturityApprovalTests.doc`
   helper, so a defect in the helper could not mask a defect in the validator.

This review also supplies what the R1 notes explicitly said they could not: the
executor's runs bound to a **modified worktree** and were marked as not quotable for
a committed state. These runs bind to committed `8da3fde…` with a clean tree and
index.

## Baseline

- **HEAD:** `8da3fde52c9f30282f9dbc3714a8edca7f9b6902` —
  `fix(cds): close semantic status contract review findings`, identical to
  `origin/main`.
- **Parent:** `fe0339fe15850e2d16c59de80519bbddfca5e642` —
  `docs(cds): record independent contract correction review`.
- Working tree and index clean before and after execution; no untracked files; no
  merge, rebase, or cherry-pick; 0 tags; `git diff --check` clean.
- Delta: **3 modified, 1 added, 0 deleted** — 203 insertions, 9 deletions.

## Skills

Skill inventory verified before use: **38 directories, 39 files, 39/39 manifest
matches** by SHA-256 and byte size against
`project-system/NDF_SKILLS_MANIFEST.json` (pinned to NDF v1.0.0, source commit
`9dcadc1…`). Exactly the ten authorized Skills were read; no other Skill was loaded.
No Skill file was modified.

**Boundary note.** The NDF Skills are docs-only and forbid running scripts. This work
package explicitly authorizes a fresh runtime, the unit suites, the direct probes,
and the validation harness. Per the Skills-first operating mode, the explicit
work-package prompt overrides a Skill, so this is not a conflict and did not trigger
fail-closed. Skills were used as procedural aid only; none extended scope or
authority.

## What was checked, and how

| Item | Method |
| --- | --- |
| Repository state | `git rev-parse`, `git branch`, `git status`, `git remote -v`, `.git` state files |
| Delta | `git diff --name-status`, `--numstat`, and the full `-U10` diff read line by line |
| F-001 | Full re-read of the contract document plus a semantic sweep of every `Candidate` / `Approved` / `approval` / `maturity` / `authority` occurrence; anchor-target resolution check |
| F-002 | Clause-by-clause comparison of the docstring against the state machine at lines 203–234 |
| F-004 | Diff inspection; parent-vs-HEAD pattern comparison; an independent differential reproduction of the defect |
| Tests | Parent-vs-HEAD test-name set comparison via `comm`; inspection of the assertion helper |
| F-003 / F-005 / F-006 | `git diff` scoped to `schemas/` and `.gitignore`; direct inspection of the committed content |
| Authority boundary | Targeted greps across all five named documents, read in context |
| Evidence | Four executions on a fresh venv outside the repository |
| Governance | Counts and states derived from the registers, source set, dossier, and project-control files — never copied from the prompt |

## Result

**COMPLETE · GO · Candidate = No.**

- **F-001 CLOSED.** The unconditional clause is gone from the normative, Elevated
  contract; the coherence rule replaces it; the new boundary paragraph states the
  three-state machine and the authority limit; the cross-reference resolves to the
  real pre-existing section at line 145. No contradictory prohibition remains
  anywhere in the document.
- **F-002 CLOSED.** All four docstring claims match the implementation.
- **F-004 CLOSED**, and behaviourally real: on the unchanged pattern the parent's
  `.match` accepts `…-candidate\n` and the committed `.fullmatch` rejects it, while
  the valid revision still passes. Pattern, branches, diagnostic code, and all four
  messages are unchanged.
- **Exactly one test added, none removed, no assertion weakened.**
- **F-003 unchanged and deferred** — `schemas/` is byte-identical to the parent;
  both fields remain bare strings. **F-005 and F-006 unchanged.**
- **Authority boundary consistent** across all five documents.
- **Sentinels reproduced exactly:** 39/39 targeted · 4/4 probes · 112/112 full
  regression · 24/24 harness (0 mismatches, 0 internal errors, exit 0).
- **Governance unchanged:** Candidate No · `semantic-status-rev-0001` · Experimental ·
  Unapproved · Dossier `Draft – Candidate gate incomplete` · 124 Decisions ·
  97 Risks (0 Accepted, 0 Closed) · 3 ADRs · WP-016 open · WP-017 not activated ·
  Private Development · no claims · pilot inactive.

**0 Blocking · 0 High · 0 Medium · 0 Low · 2 Observations.**

## Judgement calls worth recording

**OBS-001 was not escalated.** The `$`-anchored `.match()` pattern that caused F-004
recurs at six sites in `graph.py` and `validation.py`. It was tempting to treat this
as an incomplete fix, but F-004 was scoped to the Candidate-revision matcher, those
sites are pre-existing and untouched, and none of them can produce a Candidate
bypass — Candidate coherence turns on exact string equality for `maturityState` and
`approvalState`, and `sourceSetId` is compared by equality, so a stray newline there
fails closed rather than opening anything. Recorded as an Observation for a later
scoped hardening package. Repairing it here would have been scope drift.

**OBS-002 does not reopen F-002.** The docstring says `Experimental` is coherent only
with `Unapproved`, but the code only rejects `Approved`, so an unrecognized approval
value passes silently. That is the deferred F-003 root cause — no enums on
`maturityState`/`approvalState` — surfacing at the docstring rather than a new
divergence, and the normative contract uses the same wording. No Candidate impact.

**The line-35 phrasing in the validator architecture document was not raised.** It
still summarizes the module as performing "approval-statement … checks". That names a
check, not a prohibition, is unchanged from the parent, and the same document expands
it correctly at lines 86–109.

## Hygiene

Every invocation ran with `PYTHONDONTWRITEBYTECODE=1` and `python -B`. No
`__pycache__` was created anywhere in the repository — relevant because F-005 records
that `__pycache__` is still not gitignored. The venv, the probe script, and the
differential script live in the session scratchpad outside the repository. The
working tree and index were verified clean after execution.

## Explicitly NOT done

No repair, refactoring, or cleanup; no Candidate or Stable promotion; no source
revision, approval, dossier, decision, risk, ADR, or risk-state change; no schema
hardening; no F-003 implementation; no `.gitignore` or digest-enum change; no
presentation mapping; CDS-WP-017 not activated; no consumer integration; no commit,
push, pull, fetch, merge, rebase, cherry-pick, reset, restore, clean, branch change,
tag, release, or history change.

## Files added (2)

1. `docs/reviews/WP016_CONTRACT_CORRECTION_R1_INDEPENDENT_REVIEW.md`
2. `project-brain/CDS_WP_016_CONTRACT_CORRECTION_R1_INDEPENDENT_REVIEW_NOTES.md`

0 modified · 0 deleted.

## Next step

Nova review of this R3 result, then the Human-Maintainer decision on committing the
two review artifacts. Only afterwards does the CDS-WP-016 Candidate-gate work resume.
F-003 and OBS-001 stay queued for a separate, explicitly scoped hardening work
package. **This review approves nothing and promotes nothing.**

## Related

- [Independent Rework Review R3](../docs/reviews/WP016_CONTRACT_CORRECTION_R1_INDEPENDENT_REVIEW.md)
- [Rework R1 Notes](CDS_WP_016_CONTRACT_CORRECTION_R1_NOTES.md)
- [Contract Correction Independent Review (R2)](../docs/reviews/WP016_CONTRACT_CORRECTION_INDEPENDENT_REVIEW.md)
- [Independent Review Notes (R2)](CDS_WP_016_CONTRACT_CORRECTION_INDEPENDENT_REVIEW_NOTES.md)
