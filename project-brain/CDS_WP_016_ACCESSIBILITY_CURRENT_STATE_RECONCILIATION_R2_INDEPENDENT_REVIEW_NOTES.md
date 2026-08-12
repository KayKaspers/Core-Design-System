# CDS-WP-016 — Accessibility Current-State Reconciliation R2 Independent Review Notes

*Non-normative operational evidence for the independent review of commit
`4fe8f605e2df1aa6b6516359e8456e8b04cadbc0`. This run is **read-only** with
respect to the reviewed change: it produced no accessibility evidence, no
AE-1/AE-2/AE-3/AE-4, no Candidate promotion, no Decision, no Risk, no ADR, and no
Git write. These notes are **operational evidence, not normative accessibility
governance**.*

## Independence

Fresh conversation. Confirmed individually before any Skill load, repository
analysis, runtime creation, or test:

- `CURRENT_SESSION_IS_NEW` — the conversation begins with the review prompt.
- `CURRENT_SESSION_DID_NOT_EXECUTE_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R2`
- `CURRENT_SESSION_DID_NOT_EDIT_ANY_OF_THE_25_RECONCILED_FILES`
- `CURRENT_SESSION_DID_NOT_CREATE_THE_R2_NOTES`
- `CURRENT_SESSION_DID_NOT_RUN_THE_PREVIOUS_BLOCKED_REVIEW`
- `REVIEWER_CONTEXT_IS_NOT_EXECUTOR_CONTEXT`
- `REVIEWER_CONTEXT_IS_NOT_PREVIOUS_FAILED_REVIEW_CONTEXT`

**INDEPENDENCE GATE = PASS.** R2 was known only through committed repository
state, the committed R2 Notes, and the review prompt. No executor working
context was imported.

## Scope boundary raised before execution

The prompt (§22) authorizes a fresh virtual environment and installation of
`requirements-validator.lock`, which CLAUDE.md otherwise forbids without explicit
approval, and (§23–§25) test execution, which the accessibility boundary
otherwise forbids without an explicit prompt. Both were treated as explicitly
authorized by this prompt, executed exactly as scoped, and confined to a venv
**outside** the repository. Network was used only for the pinned installation and
not at runtime. This was stated to the Human Maintainer before proceeding.

## Baseline

- **Reviewed HEAD:** `4fe8f605e2df1aa6b6516359e8456e8b04cadbc0` —
  `docs(cds): reconcile accessibility baseline current state`
- **Parent:** `1c72f7c73d1d814d931b1394c6b5b27f70cc6700` —
  `docs(cds): record independent rework review`
- **Tree:** `c11ee9acc6e9a7e0c730fb0f824c98aa6c99af0d`
- **`origin/main`** via read-only `git ls-remote`: `4fe8f60…cadbc0` — identical.
  No fetch, no pull.
- Working tree and index clean before and after; no merge, rebase, or
  cherry-pick.
- **WP-010:** `abe84b6b7267b8b9c5f96609e7c9d1ad1e68bc0a` —
  `git merge-base --is-ancestor … HEAD` → **SUCCESS**.
- **Skills:** 38 directories · 39 files · **39/39 manifest hash matches**,
  0 mismatches, 0 missing, 0 extra.

## Skills used (all explicitly named by the prompt; none auto-selected)

`ndf-work-package-runner` · `ndf-accessibility-reviewer` ·
`ndf-validation-evidence-reviewer` · `ndf-implementation-review-runner` ·
`ndf-adr-governance-review` · `ndf-release-safety` ·
`ndf-existing-project-analysis-runner` · `ndf-feature-scope-runner` ·
`ndf-content-tone-reviewer` · `ndf-context-pack-maintainer` ·
`ndf-compact-context-summary-runner`. No additional Skills. Where a Skill's
docs-only "no scripts" boundary met the prompt's explicit test authorization, the
prompt governs (CLAUDE.md Skills rule 7); Skills granted no authority.

## Method notes worth carrying forward

**Line-based search under-reports in this repository.** The Markdown sources
hard-wrap at ~80 columns, so a phrase such as "…), pending / Human-Maintainer
commit." is invisible to `grep`. A whitespace-normalized whole-file pass was run
in addition, and **three of the four Category-A findings are visible only to
it** — `ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md:128`,
`COREOPS_PILOT_ACCESSIBILITY_CRITERION.md:122`, and `DECISION_INDEX.md:2316`.
Any future drift reconciliation must normalize before searching.

**Two measurement artifacts were caught and discarded**, not reported as
findings:

- `git show <rev>:<path>` piped through MSYS reported CR on every line of every
  file. Re-measured with `git cat-file blob` read as raw bytes in native Python:
  **0 CRLF sequences in all 26 blobs**.
- A UTF-8 check that wrote to `/tmp/...` from Git Bash and read it from native
  Python reported all 26 files invalid. The path did not resolve across the
  boundary; re-measured natively: **26/26 valid UTF-8, no BOM**.

**One table "defect" was a checker false positive.** `R2_NOTES.md:67` uses a
correctly escaped `\|` inside a cell; a naive pipe count mis-reads it.

## What the review confirmed

- Exact committed delta: **25 modified · 1 added · 0 deleted**, membership
  identical to the expected list.
- **All 25 diffs are status-only.** Zero Category-B (unrelated or semantic)
  hunks. Several repairs strengthen the baseline≠evidence boundary rather than
  merely restating it.
- Protected files clean: `CLAUDE.md` preserves **"No test execution without an
  explicit prompt."** verbatim and every authority rule; RISK-044's Status,
  Roles, Initial likelihood, and Initial severity are **byte-identical to the
  parent**; `WORK_PACKAGES.md` keeps CDS-WP-016 `Next` and CDS-WP-017 absent.
- Governance unchanged: 124 Decisions · 97 Risks (90 Monitored, 7 Mitigating,
  0 Accepted, 0 Closed) · 3 ADRs · Candidate `No` ·
  `semantic-status-rev-0001` · Experimental · Unapproved · Dossier `Draft` ·
  Private Development · Claims None · Pilot inactive.
- AE-0 preserved; no AE-1 artifact anywhere; `artifacts/validation/` holds only
  validator digests and results.
- WP-012…015 drift untouched and not made inconsistent.
- Sentinels reproduced exactly: **39/39 · 112/112 · 24/24 (exit 0)** on Python
  3.13.14, Windows-11-10.0.26200-SP0, 7 exact pins, fresh venv outside the repo,
  `PYTHONDONTWRITEBYTECODE=1`, no runtime network, repository clean afterwards.
- `git diff --check` PASS · 754 relative links checked, 0 broken · LF-only ·
  no full-file churn. `ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md`, flagged by the
  executor for an intermediate CRLF conversion, is **LF-only at the committed
  revision** — the correction held.

## Why the review still recommends NO-GO

Nine current WP-010 statements survive at the reviewed revision.

**Root cause — misattribution, not carelessness.** The executor's WP-012…015
deferred list (Notes:149–170) contains `README.md`, `PROJECT_PROFILE.md`,
`NEXT_PHASE.md`, `CONTEXT_PACK_FOUNDATION.md`, and `DECISION_INDEX.md`. Those
files genuinely do carry WP-012…015 `pending commit` text — but they *also* carry
**WP-010 / A11Y-BL-001** occurrences, which belong to R2's own scope. Filing the
path under the deferred class retired the whole file from consideration. Three
further paths (`ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md`,
`PRE_CANDIDATE_OPERATING_PLAN.md`, `COREOPS_PILOT_ACCESSIBILITY_CRITERION.md`)
appear in neither list and were simply missed — two of them line-wrapped.

The consequence is that **five documents this commit repaired now contradict
themselves**, stating both that A11Y-BL-001 is committed and that it is pending.

| Finding | Severity | Site |
| --- | --- | --- |
| F-001 | Blocking | `ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md:127–129` vs its own repaired 183–186 |
| F-002 | Blocking | `COREOPS_PILOT_ACCESSIBILITY_CRITERION.md:121–123, 133–134, 165, 175` — normative; line 175 asserts the baseline "**Does not exist**" |
| F-003 | Blocking | `DECISION_INDEX.md:2314–2317` — normative Decision consequence |
| F-004 | High | `PRE_CANDIDATE_OPERATING_PLAN.md:49–52` vs its own repaired line 66 |
| F-005 | High | `README.md:27–28` · `PROJECT_PROFILE.md:58–60` · `NEXT_PHASE.md:197–198` · `CONTEXT_PACK_FOUNDATION.md:773–774` |
| F-006 | Medium | AE-1 inventory missing `docs/operations/CRITICAL_RISK_ACTION_REGISTER.md` |
| F-007 | Medium | R2 Notes:50–54 record a discovery-gate **PASS** the repository contradicts |
| F-008 | Observation | `CONTEXT_PACK_FOUNDATION.md:60` — executor's historical classification **accepted as legitimate** |
| F-009 | Observation | `CHANGELOG.md:173–175` — properly historical, but classified in neither list |

## AE-1 transition inventory — independent derivation

Scanned every `.md`/`.json` for AE-0 / no-evidence current-state language: **46
files**. Removed the historical class — 7 `docs/reviews/`, 2 `docs/research/`,
3 WP-notes — and `CHANGELOG.md`. Remainder **33** = 32 exact paths + 1 ambiguous.

- Executor: **31** exact + 1 ambiguous. Reviewer: **32** exact + 1 ambiguous.
- **Extra (executor-only): 0.** Membership of all 31 matches exactly.
- **Missing (reviewer-only): 1** — `docs/operations/CRITICAL_RISK_ACTION_REGISTER.md`,
  whose RISK-044 note (rewritten by this very commit, lines 303–304) asserts
  "every artifact remains AE-0".
- Ambiguous entry `ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md` — **agreed**;
  a structural AE-1 is not a WCAG test, so the myth-busting row may survive, but
  it must be re-read deliberately.

The Category 1–5 scheme is sound, and Category 4's principle — *evidence never
transfers between artifacts* — is correctly stated and worth preserving.

## Files changed by this review

**Added (2):**

```text
docs/reviews/WP016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R2_INDEPENDENT_REVIEW.md
project-brain/CDS_WP_016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R2_INDEPENDENT_REVIEW_NOTES.md
```

**Modified: 0 · Deleted: 0.** No third review file. Nothing under `docs/`,
`tokens/`, `schemas/`, `tests/`, `tools/`, `artifacts/`, or any reviewed path was
altered.

## Git

HEAD `4fe8f605e2df1aa6b6516359e8456e8b04cadbc0` and the index are unchanged. No
commit, push, pull, fetch, merge, rebase, cherry-pick, reset, restore, clean,
branch change, tag, release, or history change. Remote access was limited to a
read-only `git ls-remote origin refs/heads/main`. Git authority remains
exclusively with the Human Maintainer.

## Next safe step

Nova review of these findings, then a Human-Maintainer-authorized **R3**
reconciliation covering the nine residual WP-010 sites (F-001 … F-005) plus the
two Notes corrections (F-006, F-007). R3 should treat
`COREOPS_PILOT_ACCESSIBILITY_CRITERION.md` and `DECISION_INDEX.md` as newly
authorized paths and must **separate WP-010 occurrences from WP-012…015
occurrences path by path** rather than by filename. Afterwards: an independent
R3 review, then the separately scoped WP-012…015 reconciliation, and only then
the AE-1 executor run against the corrected 32-path set.

**Not authorized and not begun:** AE-1 production, Candidate promotion, Candidate
Finalization, CDS-WP-017.
