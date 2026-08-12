# CDS-WP-016 — Accessibility Current-State Reconciliation R3 Independent Review — Notes

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-016 — Independent Accessibility Current-State
  Reconciliation R3 Review
- **Reviewed commit:** `9f3ec243eda6e3755f68fafda118d8a2b336710d`
- **Parent:** `00150d171c9ae3e5367034148219a5fefea1d34f`
- **Tree:** `38568de26dfddb2b5a27ad47d8d35b9a5d91bf63`
- **Date:** 2026-08-12
- **Status:** **Operational review evidence. Not a normative source.** These Notes
  create no Decision, Risk, or ADR, change no policy, promote nothing, and record
  **no accessibility evidence**. Every CDS artifact remains **AE-0**.

## Outcome

| Item | Value |
| --- | --- |
| Status | **REWORK REQUIRED** |
| Recommendation | **NO-GO** |
| Candidate Decision | **No** |
| Blocking / High / Medium / Low / Observation | 0 / 0 / **1** / 0 / 4 |
| Sentinel | `CDS_WP_016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_REVIEW_REWORK_REQUIRED` |

Full review: [Independent R3 Review](../docs/reviews/WP016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_INDEPENDENT_REVIEW.md).

## The one-sentence result

The R3 reconciliation is **correct and complete as a reconciliation** — 13/13
status-only hunks, zero current WP-010 drift, zero same-file contradictions, all
boundaries preserved, all three sentinels reproduced — and the review nonetheless
returns NO-GO because the forward-looking AE-1 planning inventory inside the
operational Notes omits one normative path, and the gate admits no Medium finding.

## Method

Order of work: Independence Gate → Git identity → Skills verification → exact
delta → complete hunk review → dual-method discovery → per-file consistency →
preservation checks → R3 Notes audit → independent AE-1 / WP-007 / WP-011…015
derivations → governance derivation → fresh runtime and three suites → encoding →
findings → review files.

All discovery scripts were created in the session scratchpad **outside** the
repository. No tooling was added to the repository. The working tree was clean
before and after; the test runs produced no `__pycache__`, no `.pyc`, and no
repository artifact.

### Discovery passes actually run

| Pass | Scope | Result |
| --- | --- | --- |
| A — line-oriented | 249 files, 17 pattern families | 511 hits |
| B — whitespace-normalized whole-file | 249 files, same families | 552 hits |
| Broadened absence-phrasing | whole repository | 11 hits |
| Focused normative / active-control | 80 files across 8 normative trees + `README.md`, `CLAUDE.md`, `PROJECT_BRAIN.md` | 6 hits |
| AE-1 mirror (strict, then loosened) | whole repository minus historical carriers | 31 → 35 paths |
| WP-011…015 / ADR class | whole repository minus historical carriers | 24 paths · 54 occurrences |

**Why four discovery passes and not two.** The mandated pattern list names
absence phrasings built on the word *no* (`no baseline`, `no support baseline
exists`, `support baseline does not exist`). It does not name absence expressed
without it — `none is declared`, `is undeclared`, `remains outstanding`, `has not
been declared`. The reviewer added the broadened pass specifically to close that
gap, and it is what surfaced `FOUNDATION_CLOSURE_RECORD.md:85`. Anyone repeating
this review should keep that pattern family.

## What was independently reproduced, not accepted

| Executor claim | Reviewer method | Reviewer result |
| --- | --- | --- |
| 5 WP-010 sites in the pilot criterion | read the complete parent-revision file | **5 — match** (the R2 review's 4 was the under-count) |
| Category A = 0 after repair | two-method repository scan + two extra passes | **0 — match** |
| Category B = 0 after repair | same | **0 — match** |
| 9 modified + 1 added + 0 deleted | `git diff --name-status` | **match** |
| 29 insertions / 27 deletions in the nine files | diffstat minus the 503-line Notes | **match** |
| Decisions 124 | `^## DEC-S-` count at parent and HEAD | **124 / 124 — match** |
| Risks 97, 90/7/0/0 | status-line count | **match** |
| ADRs 3 | file count | **match** |
| WP-007: 5 sites / 3 files | independent derivation | **match** |
| WP-011…015: 24 paths | independent derivation | **24 — exact membership match** |
| WP-011…015: 52 occurrences | independent derivation | **54 — counting granularity, OBS-003** |
| AE-1 inventory: 32 paths | independent derivation | **33 — one omission, F-001** |
| Ambiguous set: 1 | independent derivation | **match** |
| 39 / 112 / 24 | fresh venv, fresh runs | **match** |

## The finding

**F-001 (Medium).** `docs/foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md`
is missing from the R3 Notes' AE-1 mirror inventory. Line 51–53: "These are
component-contract obligations to be evidenced later (AE-graded, **currently AE-0
everywhere**); this contract creates the requirement, not the evidence." The file
header declares it **Normative**. The statement is true today and becomes false
at the AE-0 → AE-1 transition, which is precisely what the inventory exists to
enumerate — and the inventory calls itself "**The exact set**".

The executor scanned this file (it appears in the WP-011…015 drift list at R3
Notes L390) but did not carry it into the AE-1 inventory. No exclusion rationale
is recorded, so this reads as a gap rather than a judgement.

**Correction is cheap and contained:** the AE-1 inventory lives in operational
Notes, so extending it from 32 to 33 touches no normative source, no Decision, no
Risk, and no ADR. The nine-file reconciliation needs no change whatsoever.

## The near-miss worth recording

`docs/governance/FOUNDATION_CLOSURE_RECORD.md:85` — mandatory closure note 2 —
reads "**Accessibility support baseline** — none is declared" in the present
tense, with no temporal marker on its section, while the very next table is
explicitly headed "State **at closure**". Neither R2 nor R3 ever examined this
line; both examined only line 99 of the same file.

The reviewer initially leaned toward calling it current normative drift, on the
reasoning that note 3 in the same table carries an "Addressed … by the Critical
Risk Action Register" marker and therefore proved the table was maintained after
closure. **`git log` refuted that:** the file has exactly one commit
(`144cc58`, CDS-WP-009) and has never been revised — note 3's marker was written
at authoring time, because WP-009 created both the closure record and the
Critical Risk Action Register. The table is a frozen dated record, not a
maintained tracker.

Combined with the header bounding the document's normative force to closure fact,
authority state at closure, and phase boundary, plus its explicit subordination
clause ("Where it summarizes a normative policy, the policy remains the source of
truth"), the correct classification is **Category C — historical /
revision-bound**, matching how the Independent R2 Review classified line 99 of the
same file. R3 was right not to touch it; the file is not in its Allowed Files.

Recorded as **OBS-001** because a future authorized reconciliation should consider
a temporal marker or an "addressed policy-side by CDS-WP-010" gates-column note in
the style note 3 already uses. **Verifying the commit history before grading was
what changed this from a Medium to an Observation** — worth repeating in any
similar call.

## Runtime

Windows 11 Pro 10.0.26200.9168 · Python **3.13.15** · fresh venv outside the
repository · `requirements-validator.lock` only · **7 pins**, `pip freeze`
identical to the lock with no extra package · `PYTHONDONTWRITEBYTECODE=1` and
`python -B` on every run · no runtime network after installation.

| Suite | Expected | Actual |
| --- | --- | --- |
| `tests.validator.test_semantic_status` | 39 | 39 run · 39 passed · 0 failed · 0 errors · 0 skipped |
| `discover -s tests/validator -p "test_*.py"` | 112 | 112 run · 112 passed · 0 failed · 0 errors · 0 skipped |
| `validate-cases … VALIDATION_CASES.json` | 24 / 24 | 24 cases · 24 matches · 0 mismatches · 0 internal errors · exit 0 |

The executor recorded Python 3.13.14; this review ran 3.13.15 (**OBS-002**). Pins
identical, sentinels identical, result unaffected.

**These runs are validator regression only. They produce no accessibility
evidence and no AE-1.**

## Open items carried forward

1. **F-001** — extend the AE-1 mirror inventory to 33 paths. Separately
   authorized WP; Notes-only correction.
2. **WP-007 temporal drift** — 5 sites / 3 files, untouched and confirmed.
   *Separate reconciliation required before Candidate Finalization.*
3. **WP-004 pilot-contract temporal state** — adjacent class, registered,
   untouched.
4. **WP-011…015 / ADR drift** — 24 paths, untouched and confirmed.
   *Separate reconciliation required before Candidate Finalization.*
5. **OBS-001** — `FOUNDATION_CLOSURE_RECORD.md:85` temporal marker, for a future
   authorized pass.
6. `CONTEXT_PACK_FOUNDATION.md:60` — the WP-010 compact-history row should move
   together with the WP-012…015 rows in the separate reconciliation, not alone.

## Authority statement

This review changed **no** implementation file, **no** Decision, **no** Risk,
**no** ADR, **no** maturity state, and **no** Candidate state. It created exactly
two files and modified none:

- `docs/reviews/WP016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_INDEPENDENT_REVIEW.md`
- `project-brain/CDS_WP_016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_INDEPENDENT_REVIEW_NOTES.md`

No Git write action of any kind was performed: no commit, push, pull, fetch,
merge, rebase, cherry-pick, reset, restore, clean, branch change, tag, release, or
history change. Remote inspection was read-only (`git ls-remote`). HEAD and the
index are unchanged.

Candidate promotion, Stable promotion, Candidate Finalization, and CDS-WP-017
were **not** begun. Further progress requires **Nova review + Human-Maintainer
authorization**.

## Related documents

- [Independent R3 Review](../docs/reviews/WP016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_INDEPENDENT_REVIEW.md)
- [R3 Notes (executor evidence)](CDS_WP_016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_NOTES.md)
- [R2 Notes (historical, immutable)](CDS_WP_016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R2_NOTES.md)
- [Independent R2 Review](../docs/reviews/WP016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R2_INDEPENDENT_REVIEW.md)
- [Accessibility Support Baseline](../docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
