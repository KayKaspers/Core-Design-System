# CDS-WP-016 — Accessibility Current-State Reconciliation R3 — Independent Review

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-016 — Independent Accessibility Current-State
  Reconciliation R3 Review
- **Reviewed commit:** `9f3ec243eda6e3755f68fafda118d8a2b336710d`
- **Reviewed subject:** `docs(cds): complete accessibility baseline current-state reconciliation`
- **Reviewed tree:** `38568de26dfddb2b5a27ad47d8d35b9a5d91bf63`
- **Parent:** `00150d171c9ae3e5367034148219a5fefea1d34f`
- **Date:** 2026-08-12
- **Status:** **Independent review evidence — not a normative source.** This review
  changes no Decision, Risk, ADR, policy, or maturity state, promotes nothing,
  produces **no accessibility evidence**, and grants no Candidate, Stable,
  adoption, conformance, support, release, or publication status. Every CDS
  artifact remains **AE-0**.

## Result

| Item | Value |
| --- | --- |
| Status | **REWORK REQUIRED** |
| Recommendation | **NO-GO** |
| Candidate Decision | **No** |
| Blocking / High / Medium / Low / Observation | **0 / 0 / 1 / 0 / 4** |

**The reconciliation itself is correct.** All thirteen committed sites are
temporal status-only corrections, current WP-010 Category A and Category B drift
are independently reproduced as **zero**, same-file current contradictions are
**zero**, every accessibility, evidence, support, conformance, Candidate, and
pilot boundary is preserved, and all three technical sentinels reproduce exactly
(39/39 · 112/112 · 24/24).

The single Medium finding lies **not in the reconciliation** but in the
forward-looking AE-1 planning inventory inside the operational R3 Notes: the
"exact set" of 32 paths omits one **normative** Semantic Status contract that
carries a current AE-0 assertion. Under the review gate (§33), which requires
0 Medium, this yields NO-GO. The proportionate correction is to amend the
inventory in the Notes — **not** to redo the reconciliation.

## 1. Independence

| Gate statement | Result |
| --- | --- |
| `CURRENT_SESSION_IS_NEW` | TRUE |
| `CURRENT_SESSION_DID_NOT_EXECUTE_R3` | TRUE |
| `CURRENT_SESSION_DID_NOT_EXECUTE_THE_BLOCKED_R3_DISCOVERY` | TRUE |
| `CURRENT_SESSION_DID_NOT_EXECUTE_R2` | TRUE |
| `CURRENT_SESSION_DID_NOT_EDIT_ANY_R3_FILE` | TRUE |
| `CURRENT_SESSION_DID_NOT_CREATE_R3_NOTES` | TRUE |
| `CURRENT_SESSION_DID_NOT_CREATE_R2_NOTES` | TRUE |
| `CURRENT_SESSION_IS_NOT_THE_INDEPENDENT_R2_REVIEW_CONTEXT` | TRUE |
| `REVIEWER_CONTEXT_IS_NOT_EXECUTOR_CONTEXT` | TRUE |
| `REVIEWER_CONTEXT_IS_NOT_PREVIOUS_REVIEW_CONTEXT` | TRUE |

**INDEPENDENCE = PASS.**

R3 was known to this review only through the committed repository state,
committed historical review/evidence artifacts, and the review prompt.

**Declared boundary.** The reviewer can attest only to the contents of its own
context, in which no R2/R3 executor work appears. Whether the session was
launched fresh rather than duplicated is a property of the execution harness and
is not verifiable from inside the session. The attestation above is the strongest
statement available to the reviewer role.

## 2. Repository identity

| Item | Expected | Observed | Result |
| --- | --- | --- | --- |
| Repository root | `D:\Projects\Core-Design-System` | `D:/Projects/Core-Design-System` | PASS |
| Branch | `main` | `main` | PASS |
| HEAD | `9f3ec243…6710d` | `9f3ec243eda6e3755f68fafda118d8a2b336710d` | PASS |
| HEAD subject | as expected | `docs(cds): complete accessibility baseline current-state reconciliation` | PASS |
| HEAD tree | `38568de2…1bf63` | `38568de26dfddb2b5a27ad47d8d35b9a5d91bf63` | PASS |
| Parent | `00150d17…a1d34f` | `00150d171c9ae3e5367034148219a5fefea1d34f` | PASS |
| Parent subject | as expected | `docs(cds): record independent accessibility reconciliation review` | PASS |
| Parent tree | `60323d17…6fab9a` | `60323d17887826bca616eddaa73f847bce6fab9a` | PASS |
| `origin/main` (read-only `git ls-remote`) | == HEAD | `9f3ec243…6710d` | PASS |
| Working tree | CLEAN | clean (0 porcelain entries) | PASS |
| Index | CLEAN | clean | PASS |
| Merge / rebase / cherry-pick | none | none | PASS |

No `git fetch` and no `git pull` were executed. Remote state was read with
`git ls-remote origin refs/heads/main` only.

## 3. Skills

| # | Skill | Path | Selection | Purpose in this review |
| --- | --- | --- | --- | --- |
| 1 | `ndf-work-package-runner` | `.claude/skills/ndf-work-package-runner/SKILL.md` | prompt-mandated | WP frame, guardrails, closing structure |
| 2 | `ndf-accessibility-reviewer` | `.claude/skills/ndf-accessibility-reviewer/SKILL.md` | prompt-mandated | accessibility boundary review, no certification |
| 3 | `ndf-validation-evidence-reviewer` | `.claude/skills/ndf-validation-evidence-reviewer/SKILL.md` | prompt-mandated | honest evidence-strength rating |
| 4 | `ndf-implementation-review-runner` | `.claude/skills/ndf-implementation-review-runner/SKILL.md` | prompt-mandated | scope-fit and hunk review |
| 5 | `ndf-adr-governance-review` | `.claude/skills/ndf-adr-governance-review/SKILL.md` | prompt-mandated | ADR/Decision boundary integrity |
| 6 | `ndf-release-safety` | `.claude/skills/ndf-release-safety/SKILL.md` | prompt-mandated | release/tag/publication boundary |
| 7 | `ndf-existing-project-analysis-runner` | `.claude/skills/ndf-existing-project-analysis-runner/SKILL.md` | prompt-mandated | repository-wide structural analysis |
| 8 | `ndf-feature-scope-runner` | `.claude/skills/ndf-feature-scope-runner/SKILL.md` | prompt-mandated | scope-boundary discipline |
| 9 | `ndf-content-tone-reviewer` | `.claude/skills/ndf-content-tone-reviewer/SKILL.md` | prompt-mandated | claim/tone integrity of changed text |
| 10 | `ndf-context-pack-maintainer` | `.claude/skills/ndf-context-pack-maintainer/SKILL.md` | prompt-mandated | context-pack consistency review |
| 11 | `ndf-compact-context-summary-runner` | `.claude/skills/ndf-compact-context-summary-runner/SKILL.md` | prompt-mandated | mandatory closing blocks |

| Item | Expected | Observed |
| --- | --- | --- |
| Skill directories | 38 | **38** |
| Skill files | 39 | **39** |
| Manifest matches (SHA-256) | 39/39 | **39/39** (`NDF_SKILLS_MANIFEST.json`, tag `v1.0.0`) |
| Additional Skills loaded | none | **none** |

**Prompt-over-Skill note.** The Skills carry a generic ADR-0032 "no scripts"
boundary. The work-package prompt (§27–§30) explicitly mandates creating a
runtime and executing three test suites. Per `CLAUDE.md` *Skills-first operating
mode* item 7, the explicit work-package prompt is binding and overrides a Skill.
Test execution was therefore performed as instructed; it produced **no
accessibility evidence** and remains validator regression only.

## 4. Exact committed delta

`00150d17…a1d34f` → `9f3ec243…6710d`

| Class | Expected | Observed | Result |
| --- | --- | --- | --- |
| Modified | 9 | **9** | PASS |
| Added | 1 | **1** | PASS |
| Deleted | 0 | **0** | PASS |

Modified: `README.md` · `docs/decisions/DECISION_INDEX.md` ·
`docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md` ·
`docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md` ·
`docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md` ·
`docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md` ·
`project-system/CONTEXT_PACK_FOUNDATION.md` · `project-system/NEXT_PHASE.md` ·
`project-system/PROJECT_PROFILE.md`.

Added: `project-brain/CDS_WP_016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_NOTES.md`.

**No eleventh file.** Diffstat: 10 files · 532 insertions · 27 deletions; the
added Notes account for 503 insertions, leaving **29 insertions / 27 deletions**
across the nine modified files — matching the R3 Notes' own figure exactly.

### Protected paths — verified blob-identical parent → HEAD

`docs/risks/RISK_REGISTER.md` · `docs/operations/CRITICAL_RISK_ACTION_REGISTER.md` ·
`CLAUDE.md` · `project-system/WORK_PACKAGES.md` · `project-brain/PROJECT_BRAIN.md` ·
`CHANGELOG.md` · `docs/foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md`.

`schemas/`, `tokens/`, `tools/`, `tests/` — **zero paths** in the delta.

## 5. Full hunk classification

Every implementation hunk was read; none was sampled. Classification key:
**A** = WP-010 / A11Y-BL-001 temporal status-only reconciliation;
**B** = unauthorized semantic / policy / scope change.

| # | File | Old semantic state | New semantic state | Class | Authority impact |
| --- | --- | --- | --- | --- | --- |
| 1 | `ACCESSIBILITY_SUPPORT_BASELINE.md` § Current approval state | "Pending Nova review and Human-Maintainer commit. Until then A11Y-BL-001 is a proposal." | "Approved and in effect … committed baseline and a **test contract**, no longer a proposal." | **A** | none — the following bullet (no evidence · no environment claimed · no WCAG conformance · `Private Development`) is untouched |
| 2 | `ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md` § Reconciliation with A11Y-BL-001 | "is now A11Y-BL-001 …, pending Human-Maintainer commit" | "is A11Y-BL-001 …, declared and committed by CDS-WP-010" | **A** | none — nine baseline elements, three tiers, matrix reference unchanged |
| 3 | `COREOPS_PILOT_ACCESSIBILITY_CRITERION.md` site 1 | "The **future** support baseline is now …, pending Human-Maintainer commit" | "The support baseline is …, declared and committed by CDS-WP-010" | **A** | none |
| 4 | — site 2 | "may be treated as policy-side present **upon** Human-Maintainer commit" | "is policy-side present — CDS-WP-010 is committed — … *policy* level only. Policy-side presence satisfies **no** evidence requirement." | **A** | **strengthens** the evidence boundary by adding an explicit non-satisfaction sentence |
| 5 | — site 3 | "no artifact can reach Candidate (no evidence, **no baseline**)" | "(**no evidence exists** — every artifact is AE-0; the support baseline itself is declared)" | **A** | none — the criterion remains structurally unmet for its true reason |
| 6 | — site 4 | "\| Support baseline \| **Does not exist** \|" | "\| Support baseline \| **Declared and committed — A11Y-BL-001; a test contract, never evidence** \|" | **A** | none — "never evidence" carried inline |
| 7 | — site 5 § Missing evidence | "Before Pilot Group E can be evidenced: **a declared support baseline** · …" | "The declared support baseline is in place (A11Y-BL-001); everything below remains outstanding. Before … : …" | **A** | none — remaining eight items verbatim |
| 8 | `DECISION_INDEX.md` DEC-S-065 § Consequences | "…is normative for Required/Complementary/Scope-triggered environments, **pending Human-Maintainer commit**." | "… environments, as the declared and committed baseline under CDS-WP-010." | **A** | none — see §8 |
| 9 | `PRE_CANDIDATE_OPERATING_PLAN.md` prerequisite 3 | "…defect/regression model, **pending Human-Maintainer commit**." | "…defect/regression model, declared and committed." | **A** | none — "**No evidence executed** (every artifact AE-0)" retained in the same bullet |
| 10 | `README.md` | "is **defined** (CDS-WP-010, **pending commit**)" | "is **declared and committed** (CDS-WP-010)" | **A** | none — "a **test contract, not evidence**" retained |
| 11 | `PROJECT_PROFILE.md` | "**Defined, no evidence executed** … — **pending Human-Maintainer commit**; a test contract, not evidence" | "**Declared and committed, no evidence executed** … — a test contract, not evidence" | **A** | none — tier count 3, env count 14, AE levels 5, evidence records 0, RISK-044 Mitigating all unchanged |
| 12 | `NEXT_PHASE.md` | "**A11Y-BL-001** (…), **pending Human-Maintainer commit** — a test contract, not evidence." | "**A11Y-BL-001** (…), declared and committed — a test contract, not evidence." | **A** | none |
| 13 | `CONTEXT_PACK_FOUNDATION.md` | "…A11Y-BL-001 is defined (CDS-WP-010, **pending commit**, no evidence executed)" | "…is declared and committed (CDS-WP-010, no evidence executed)" | **A** | none — WP-011…015 clauses in the same sentence untouched |

**Category A: 13. Category B: 0.**

Every Category A hunk was verified for: stale temporal state removed · current
repository state reflected · original authority retained · evidence boundary
retained · support boundary retained · conformance boundary retained ·
Candidate boundary retained. **All 13 pass on all seven checks.**

## 6. Accessibility Support Baseline review

The R3 change is confined to the `## Current approval state` section — a single
hunk of 2 removed / 3 added lines.

| Element | Result |
| --- | --- |
| Top status header ("Normative and in effect") | unchanged (repaired in R2) |
| Baseline ID `A11Y-BL-001` | unchanged |
| Required Tier-1 / Complementary Tier-2 / Scope-triggered Tier-3 | unchanged |
| Environment and scope matrix, ownership, browser/AT pairings | unchanged |
| Change control · freshness · review triggers · evidence rules | unchanged |
| "No evidence produced" | **present** |
| "No environment claimed as supported" | **present** |
| "No WCAG conformance asserted" | **present** |
| Publication `Private Development` | **present** |
| Candidate authority | not conferred anywhere in the file |
| Same-file current contradiction | **0** (3 committed/effective assertions · 0 contradicting) |

Current truth established: A11Y-BL-001 is normative and in effect; the WP-010
Human-Maintainer commit is complete; the baseline is a committed baseline and
test contract, not a proposal. **Confirmed.**

## 7. Accessibility Evidence and Claims Model review

Single hunk, within the additive `### Reconciliation with A11Y-BL-001 (CDS-WP-010)`
subsection, whose own parenthetical "*(Additive — the five evidence-level
meanings above are unchanged)*" is untouched.

Unchanged and verified: AE-0, AE-1, AE-2, AE-3, AE-4 meanings · Candidate
Accessibility Gate · Stable Gate · the nine baseline elements · evidence
requirements · responsibility model · the current Semantic Status AE state.

Expected/actual: A11Y-BL-001 = declared and committed ✓; Semantic Status = AE-0 ✓.

## 8. CoreOps Pilot Accessibility Criterion review

**Independently derived WP-010 baseline-state site count: 5** — derived by
reading the complete parent-revision file, not by accepting the executor figure.

| Site | Location (HEAD) | Pre-R3 assertion | Result |
| --- | --- | --- | --- |
| 1 | 121–123 | "future support baseline … pending Human-Maintainer commit" | reconciled |
| 2 | 133–135 | "may be treated as policy-side present **upon** … commit" | reconciled |
| 3 | 164–166 | "no artifact can reach Candidate (no evidence, **no baseline**)" | reconciled |
| 4 | 175 | "\| Support baseline \| **Does not exist** \|" | reconciled |
| 5 | 182–186 | "Before Pilot Group E can be evidenced: **a declared support baseline** · …" | reconciled |

The reviewer's independent count **matches** the executor's five. The four-site
figure in the Independent R2 Review is confirmed as the under-count.

§15 requirement verification:

| # | Requirement | Result |
| --- | --- | --- |
| 1 | A11Y-BL-001 exists and is committed | established (L121–123) |
| 2 | Policy-side baseline presence established | established (L133–134) |
| 3 | Policy-side presence satisfies no evidence requirement | **explicitly added** (L135) |
| 4 | No-baseline no longer used as a Candidate blocker | corrected (L164–166) |
| 5 | Support baseline table no longer says `Does not exist` | corrected (L175) |
| 6 | Declared baseline not listed as future missing work | corrected (L182–183) |

Preserved and verified in the committed file: pilot inactive (L138, L164, L176,
L195) · no Candidate artifact (L159) · every artifact AE-0 (L137, L165, L174,
L203) · no AE-1/AE-2/AE-3/AE-4 (L137) · consumer evidence missing (L129–132) ·
feedback missing (L183–186) · remaining limitations and review requirements
(L183–186) · no support claim · no conformance claim (L198–209).

**No accidental pilot activation. Not blocking.**

## 9. Decision Index review

| Item | Value |
| --- | --- |
| Decision context | DEC-S-065 § Consequences, first bullet |
| Exact R3 hunk | single line, `@@ -2317 +2317 @@` |
| Decisions before | **124** (independently counted at parent revision) |
| Decisions after | **124** (independently counted at HEAD; max `DEC-S-124`) |
| Decision ID / title / rationale / policy / scope | unchanged |
| Consequences added or deleted | **none** — bullets 2 and 3 ("Listing an environment is never a statement that CDS works in or supports it", "Every CDS artifact remains AE-0; no support or conformance claim is valid") untouched |
| Candidate gate change | none |

The changed clause replaces a temporal qualifier only: "pending Human-Maintainer
commit" → "as the declared and committed baseline under CDS-WP-010". The
normativity statement it qualifies is unchanged.

Unrelated occurrences verified untouched: DEC-S-060 (WP-007 target, L2128–2130),
the three ADR-list entries, and the DEC-S-036 consequence. The single hunk at
L2317 is nowhere near any of them.

## 10. Pre-Candidate Operating Plan review

One hunk, in prerequisite 3. Only the WP-010 prerequisite temporal status
changed. Preserved: Candidate No · AE-0 · "**No evidence executed** (every
artifact AE-0)" in the same bullet · prerequisite 4 Evidence Reviewer staffing
"**not yet done**; the reviewer may never be the author" · prerequisites 1, 2, 5
· the "Explicitly not permitted in this phase" list including "executing
accessibility tests or asserting any accessibility evidence" · no automatic phase
transition.

## 11. Mixed control file review

| File | R3 hunks | Semantic subject of every hunk | Foreign-subject mutation |
| --- | --- | --- | --- |
| `README.md` | 1 (2 lines) | A11Y-BL-001 / WP-010 current state | **none** — the WP-011/012/ADR-0001/ADR-0002 clauses in the same paragraph are byte-identical |
| `project-system/PROJECT_PROFILE.md` | 1 (2 lines) | A11Y-BL-001 baseline status line | **none** |
| `project-system/NEXT_PHASE.md` | 1 (1 line) | A11Y-BL-001 bullet under CDS-WP-010 | **none** |
| `project-system/CONTEXT_PACK_FOUNDATION.md` | 1 (2 lines) | A11Y-BL-001 clause inside the phase sentence | **none** — the CDS-WP-011/012/013/014/015 clauses in the same sentence are unchanged |

**Zero R3 mutation** to current statements belonging to WP-007, WP-011, WP-012,
WP-013, WP-014, WP-015, ADR-0001, ADR-0002, ADR-0003, the WP-004 pilot-contract
temporal state, or historical WP-010 snapshots.

`CONTEXT_PACK_FOUNDATION.md` line 60 — the CDS-WP-010 row of the compact per-work-package
history table, reading "Defined **A11Y-BL-001** (pending commit)" — **remains
unchanged**, and the reviewer independently confirms the historical
classification: the adjacent CDS-WP-012 row of the same table uses the identical
"(pending commit)" convention, so the table records each work package's state as
of its own completion. Repairing only the WP-010 row would introduce a different
internal inconsistency.

## 12. Dual-method WP-010 discovery

Both methods were run by the reviewer independently, over the committed working
tree (clean, therefore identical to HEAD). All discovery scripts were created
**outside** the repository; no discovery tooling was added to it.

### Method A — line-oriented

249 files scanned across 17 semantic pattern families; **511 raw hits**.
Confirmed to under-report: statements hard-wrapped at ~80 columns
(e.g. `DECISION_INDEX.md:2128–2130`) are invisible to it.

### Method B — whitespace-normalized whole-file

Strict UTF-8 whole-file read · consecutive whitespace collapsed to one space ·
case-insensitive matching · every candidate re-read in original context.
249 files; **552 raw hits**. Two further passes were added by the reviewer after
noticing a phrasing class the mandated pattern list does not name — absence
expressed without the word *no* (`none is declared`, `is undeclared`,
`remains outstanding`, `has not been declared`): a broadened pass (11 hits) and a
focused normative/active-control pass restricted to 80 files across
`docs/governance`, `docs/architecture`, `docs/roadmap`, `docs/operations`,
`docs/decisions`, `docs/risks`, `docs/foundations`, `project-system`, plus
`README.md`, `CLAUDE.md`, `project-brain/PROJECT_BRAIN.md` (6 hits).

### Classification

| Category | Meaning | Reviewer result |
| --- | --- | --- |
| **A** | current **normative** WP-010 drift | **0** |
| **B** | current **active-control** WP-010 drift | **0** |
| **C** | historical / revision-bound WP-010 | present and correctly preserved |
| **D** | current and true | all repaired statements plus the R2-era true statements |
| **E** | WP-011…015 / ADR separate drift | 24 paths — untouched |
| **F** | WP-007 separate drift | 5 sites / 3 files — untouched |
| **G** | other / ambiguous | WP-004 pilot-contract commit-state statements — untouched |

**Independent GO requirement (Category A = 0, Category B = 0): satisfied.**

Category C sites individually inspected and confirmed historical:
`FOUNDATION_CLOSURE_RECORD.md` (see Observation 1) ·
`FOUNDATION_MILESTONE_REVIEW.md` and `GOVERNANCE_AFFORDABILITY_AND_OPERATING_READINESS.md`
(both headed "**Review evidence — not a normative source**", bound to reviewed
revision `7b71652`, dated 2026-07-16) · `FOUNDATION_COMPLETENESS_MATRIX.md` ·
`FOUNDATION_OPEN_GAPS_AND_DEPENDENCIES.md` · `CHANGELOG.md` (change-event record;
also on the must-not-modify list) · the per-WP `project-brain/CDS_WP_007/008/009/010`
notes · the R2 executor and reviewer evidence · `CONTEXT_PACK_FOUNDATION.md:60`.

Category D sites spot-verified as current and true: `RISK_REGISTER.md` RISK-044
("The baseline itself is committed (CDS-WP-010) and produces no evidence") ·
`ACCESSIBILITY_CHANNEL_PROFILES.md` ("the support baseline is no longer
deferred — A11Y-BL-001 is committed") · `ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md`
("the support baseline A11Y-BL-001 is committed but is not evidence") ·
`PRE_CANDIDATE_OPERATING_PLAN.md:128` ("the baseline is defined, but no evidence
has been produced — every artifact is AE-0") · the generic requirement statements
in `ARTIFACT_MATURITY_LIFECYCLE.md`, `CONSUMER_VALIDATION_PLAN.md`, and
`COREOPS_PILOT_CONTRACT.md` ("AE-3 against **a** declared support baseline"),
which are obligations, not state assertions.

## 13. Same-file consistency

Each of the nine modified existing files was tested for a current claim that
A11Y-BL-001 is committed/effective **together with** a current claim that it is
pending / proposed / nonexistent / missing / deferred.

| # | File | Committed/effective | Contradicting | Result |
| --- | --- | --- | --- | --- |
| 1 | `README.md` | 2 | 0 | **No contradiction** |
| 2 | `docs/decisions/DECISION_INDEX.md` | 1 | 0 | **No contradiction** |
| 3 | `docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md` | 1 | 0 | **No contradiction** |
| 4 | `docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md` | 3 | 0 | **No contradiction** |
| 5 | `docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md` | 2 | 0 | **No contradiction** |
| 6 | `docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md` | 3 | 0 | **No contradiction** |
| 7 | `project-system/CONTEXT_PACK_FOUNDATION.md` | 3 | 1 — historical only | **No current contradiction** |
| 8 | `project-system/NEXT_PHASE.md` | 1 | 0 | **No contradiction** |
| 9 | `project-system/PROJECT_PROFILE.md` | 2 | 0 | **No contradiction** |

**Current same-file contradictions: 0.** The single residual in file 7 is the
per-WP compact-history row at line 60, independently confirmed historical (§11).

## 14. R2 historical evidence preservation

Verified at Git blob level, parent → HEAD:

| Path | Blob | Result |
| --- | --- | --- |
| `project-brain/…_R2_NOTES.md` | `f2d2229d…9b9a1c` | **IDENTICAL** |
| `docs/reviews/WP016_…_R2_INDEPENDENT_REVIEW.md` | `ccd4532b…84d8f8` | **IDENTICAL** |
| `project-brain/…_R2_INDEPENDENT_REVIEW_NOTES.md` | `b164206f…82ec2ff` | **IDENTICAL** |

R3 rewrote no historical executor or reviewer evidence.

## 15. R3 Notes review

`project-brain/CDS_WP_016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_NOTES.md`
is headed "**Operational reconciliation evidence. Not a normative source.**" and
creates no Decision, Risk, or ADR, changes no accessibility policy, promotes
nothing, and records no accessibility evidence. **`CDS_R3_NOTES_ARE_OPERATIONAL_NOT_NORMATIVE`: PASS.**

Every §22 required record was verified present and accurate:

| Required record | Notes location | Verified |
| --- | --- | --- |
| baseline parent `00150d17…` | L6, L20–21 | ✓ |
| R2 implementation commit `4fe8f605…` | L19 | ✓ |
| Independent R2 Review evidence commit `00150d17…` | L20 | ✓ |
| Independent R2 Review = REWORK REQUIRED / NO-GO | L35 | ✓ |
| previous R3 attempt = `R3_SCOPE_INCOMPLETE` / zero mutations | L43–45 | ✓ |
| pre-R3 WP-010 drift = 13 sites / 9 files | L130 | ✓ (reviewer-reproduced) |
| post-R3 Category A = 0 | L207 | ✓ (reviewer-reproduced) |
| post-R3 Category B = 0 | L208 | ✓ (reviewer-reproduced) |
| R3-F-001 closed | L256 | ✓ |
| R3-F-002 closed | L257 | ✓ |
| R3-F-003 registered / not repaired | L258 | ✓ |
| R2 Notes historical and unchanged | L262–263, L278 | ✓ (blob-verified) |
| R2 Discovery-PASS superseded for current operational planning | L276–278 | ✓ |
| AE-1 inventory 31 → 32 | L283, L326 | ✓ recorded — **but see F-001** |
| ambiguous set = 1 | L284, L333–336 | ✓ |
| WP-007 separate | L341, L367 | ✓ |
| WP-011…015 / ADR separate | L370, L413 | ✓ |
| Candidate = No | L451 | ✓ |
| Semantic Status = AE-0 | L456 | ✓ |
| AE-1 = none | L457 | ✓ |
| technical regression 39 / 112 / 24 | L429–431 | ✓ (reviewer-reproduced) |
| executor Git writes = none | L470–474 | ✓ |

Internal arithmetic checks: Category A 4 files / 8 sites (L115–118 sums to 8) ·
Category B 5 files / 5 sites (L124–128) · total 9 paths / 13 sites (L130) ·
"9 files changed · 29 insertions · 27 deletions" (L183) matches the diffstat
exactly. The Notes create **no** new normative accessibility policy.

## 16. Future AE-1 mirror inventory review

Independently re-derived repository-wide, assuming a later transition of the
Semantic Status Foundation from **AE-0** to **executor-produced AE-1 pending
independent review**, excluding historical carriers by the same construction the
executor states (`docs/reviews/`, `docs/research/`, `CHANGELOG.md`, per-WP
`project-brain/CDS_WP_*` notes).

| Item | Value |
| --- | --- |
| Executor count | **32** (+1 ambiguous) |
| Reviewer count | **33** (+1 ambiguous) |
| Exact membership match | **NO** |
| Missing paths (in reviewer set, absent from executor set) | **1** — `docs/foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md` |
| Extra paths (in executor set, absent from reviewer set) | **0** |
| Ambiguous paths | **1** — `docs/governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md` (agreed) |
| Classification differences | **1** — see below |

The executor's 32 paths were reviewed **path by path**. All 32 were independently
reproduced; none is spurious. The reviewer's first pass returned 31 and missed
two that the executor correctly included — `CONSUMER_VALIDATION_PLAN.md`
("**Currently AE-0.**", "**None — AE-0 for every artifact**") and
`SEMANTIC_STATUS_CANDIDATE_DOSSIER.md` ("every artifact AE-0") — both recovered
on a loosened pass. The executor's addition of
`docs/operations/CRITICAL_RISK_ACTION_REGISTER.md` against the R2 inventory of 31
is independently confirmed correct.

**Classification difference.** `docs/governance/FOUNDATION_CLOSURE_RECORD.md`
carries "**AE-0** for every artifact" but sits in the table explicitly headed
"State **at closure**"; the reviewer agrees with its exclusion as
historical/revision-bound.

**Omission — finding F-001.**
`docs/foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md:51–53` reads
"These are component-contract obligations to be evidenced later (AE-graded,
**currently AE-0 everywhere**); this contract creates the requirement, not the
evidence." The document's own header declares it "**Normative** communication
obligations of the Semantic Status Foundation Contract". It is a current AE-state
assertion in a normative Semantic Status contract and breaks at exactly the
AE-0 → AE-1 transition the inventory exists to plan for. The executor scanned
this file — it appears in the WP-011…015 drift list — but did not carry it into
the AE-1 inventory, which claims to be "**The exact set**".

## 17. WP-007 separate drift

Independently derived; **not** accepted from the executor.

| # | Path | Line | Occurrence |
| --- | --- | --- | --- |
| 1 | `docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md` | 33 | "The policy can serve as a normative basis after Human Maintainer commit" |
| 2 | `docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md` | 147 | "`Accessibility target defined` — **satisfiable upon Human Maintainer commit of CDS-WP-007**" |
| 3 | `docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md` | 162 | "\| **Accessibility target decided** \| **Satisfiable on commit** \|" |
| 4 | `docs/governance/COREOPS_PILOT_CONTRACT.md` | 68 | "satisfiable upon Human Maintainer commit of CDS-WP-007" |
| 5 | `docs/decisions/DECISION_INDEX.md` | 2128–2130 | DEC-S-060 — "becomes `Accessibility target defined` — satisfiable upon Human Maintainer commit of CDS-WP-007" |

**Reviewer count: 5 sites / 3 files — matches the executor exactly.** Site 5 is
hard-wrapped across lines 2128–2130 and was invisible to the reviewer's
line-oriented pass; it was recovered by the normalized pass, independently
re-confirming the methodological finding of the Independent R2 Review.

**R3 mutation count in this class: 0**, verified by filtering the committed diff
for every WP-007 / target / "satisfiable" token — no such line appears on either
side of the diff.

**Adjacent WP-004 pilot-contract temporal state** is present and untouched:
`COREOPS_PILOT_CONTRACT.md` ("Normative upon Human Maintainer commit … a
**proposal** until then") plus the corresponding statements in `README.md`,
`PROJECT_PROFILE.md`, `CONTEXT_PACK_FOUNDATION.md`, `PROJECT_BRAIN.md`, and
`RISK_REGISTER.md`. The executor registered this class separately; the reviewer
confirms it.

**Disposition: SEPARATE RECONCILIATION REQUIRED BEFORE CANDIDATE FINALIZATION.**

## 18. WP-011…015 / ADR separate drift

Independently derived at the reviewed revision.

| Item | Executor | Reviewer | Result |
| --- | --- | --- | --- |
| Paths | 24 | **24** | **exact membership match** |
| Occurrences | 52 | **54** | counting granularity |

All 24 paths match one-for-one. The occurrence delta is confined to
`ADR-0001` (reviewer 3 / executor 2) and `ADR-0002` (reviewer 3 / executor 2) and
reflects how many distinct pre-commit clauses each ADR's status block is counted
as. No substantive disagreement; no path is missing on either side.

**R3 mutation count in this class: 0.** Every `WP-011…015` / `ADR-000x` token on
the added side of the diff occurs inside the new R3 Notes file, describing the
class; not one is a mutation of a document in the class.

**Disposition: SEPARATE RECONCILIATION REQUIRED BEFORE CANDIDATE FINALIZATION.**

## 19. Governance (independently derived)

| Item | Expected | Derived | Result |
| --- | --- | --- | --- |
| Candidate | No | **No** | PASS |
| Semantic source revision | `semantic-status-rev-0001` | `semantic-status-rev-0001` | PASS |
| Maturity | Experimental | Experimental | PASS |
| Approval | Unapproved | Unapproved | PASS |
| Candidate Dossier | Draft – Candidate gate incomplete | Draft – Candidate gate incomplete | PASS |
| Semantic Status AE | AE-0 | **AE-0** | PASS |
| A11Y-BL-001 | committed baseline | committed baseline, normative and in effect | PASS |
| AE-1 / AE-2 / AE-3 / AE-4 | NONE | **NONE** | PASS |
| Decisions | 124 | **124** (`^## DEC-S-` count; max `DEC-S-124`) | PASS |
| Risks | 97 | **97** (max `RISK-097`) | PASS |
| Monitored | 90 | **90** | PASS |
| Mitigating | 7 | **7** | PASS |
| Accepted | 0 | **0** | PASS |
| Closed | 0 | **0** | PASS |
| ADRs | 3 | **3** | PASS |
| CDS-WP-016 | open | open | PASS |
| CDS-WP-017 | not activated | not activated | PASS |
| Publication | `Private Development` | `Private Development` | PASS |
| Claims | None | None | PASS |
| CoreOps pilot | inactive | inactive | PASS |

## 20. Runtime, tests, and harness

| Item | Value |
| --- | --- |
| OS | Windows 11 Pro — 10.0.26200.9168 |
| Python | **3.13.15** (executor recorded 3.13.14 — see Observation 2) |
| Virtual environment | created **outside** the repository, in the session scratchpad |
| Installed from | `requirements-validator.lock` only |
| Pin count | **7** — `attrs==26.1.0`, `jsonschema==4.26.0`, `jsonschema-specifications==2025.9.1`, `referencing==0.37.0`, `rfc8785==0.1.4`, `rpds-py==2026.6.3`, `typing_extensions==4.16.0` |
| `pip freeze` vs lock | **identical, no extra package** |
| `PYTHONDONTWRITEBYTECODE=1` · `python -B` | set for every run |
| Runtime network after installation | **none** |

| Suite | Command | Expected | Actual | Result |
| --- | --- | --- | --- | --- |
| Targeted | `python -B -m unittest tests.validator.test_semantic_status -v` | 39 | **39 run · 39 passed · 0 failed · 0 errors · 0 skipped** | **PASS** |
| Full | `python -B -m unittest discover -s tests/validator -p "test_*.py" -v` | 112 | **112 run · 112 passed · 0 failed · 0 errors · 0 skipped** | **PASS** |
| Harness | `python -B -m tools.cds_validator validate-cases tests/fixtures/machine-readable/VALIDATION_CASES.json` | 24 / 24 | **24 cases · 24 matches · 0 mismatches · 0 execution errors · exit 0** | **PASS** |

Stable sentinels **39 · 112 · 24** all reproduce. The working tree remained clean
after execution; no `__pycache__`, no `.pyc`, no repository artifact was created.

**This produced no accessibility evidence and no AE-1.** It is validator
regression only.

## 21. Markdown / encoding

| Check | Result |
| --- | --- |
| `git diff --check` (parent → HEAD) | **PASS (exit 0)** |
| Strict UTF-8, all 10 changed files | **10/10 valid** |
| BOM | **none in any file** |
| CRLF | **0 sequences in any file** |
| Malformed Markdown table rows | **0** |
| Relative links on changed lines | **10 checked · 0 broken** |
| Changed anchors | none introduced |
| Formatting-only full-file rewrap | **none** — every hunk is 1–3 lines |
| Unrelated whitespace churn | **none** |

Particular attention was given to hard-wrapped current-state statements, the
mechanism by which the earlier defects escaped detection. The normalized
whole-file pass was applied to all discovery, and it is precisely what recovered
`DECISION_INDEX.md:2128–2130` and `FOUNDATION_CLOSURE_RECORD.md:85`.

## 22. Findings

### CDS-WP016-RECON-R3-RV-F-001 — Medium

- **File:** `project-brain/CDS_WP_016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_NOTES.md`
  § "F-006 — corrected AE-1 transition inventory (32 paths)" (L286–339)
- **Authority / contract:** review prompt §23 (future AE-1 mirror inventory must be
  materially complete; "material normative omission" = Medium); the inventory's own
  claim to be "**The exact set** of paths whose current-state statements will
  require change at the Semantic Status AE-0 → AE-1 transition"
- **Expected:** every path carrying a current-state statement that breaks at the
  AE-0 → AE-1 transition, or an explicit exclusion rationale
- **Actual:** `docs/foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md`
  is absent from the 32 and from the 1-item ambiguous set. Line 51–53 reads
  "These are component-contract obligations to be evidenced later (AE-graded,
  **currently AE-0 everywhere**); this contract creates the requirement, not the
  evidence." The document header declares it "**Normative** communication
  obligations of the [Semantic Status Foundation Contract]".
- **Reproducible evidence:** repository-wide normalized scan at HEAD
  `9f3ec243…6710d`, excluding historical carriers by the executor's own stated
  construction, returns 35 paths: the executor's 32, plus the declared ambiguous
  path, plus `FOUNDATION_CLOSURE_RECORD.md` (correctly excluded as the "State at
  closure" table), plus this file. The executor demonstrably scanned the file —
  it appears in the WP-011…015 drift list at R3 Notes L390 — but did not carry it
  into the AE-1 inventory.
- **Candidate impact:** none today. Nothing is promoted, no evidence exists, and
  the statement is **true at the reviewed revision**. The impact is on the future
  transition the inventory exists to plan: the Semantic Status Foundation is the
  planned first Candidate, and a maintainer executing AE-1 from the 32-path list
  would leave a false current-state assertion inside a normative Semantic Status
  contract — the exact defect class R2 and R3 were convened to eliminate.
- **Required correction:** extend the inventory to **33** paths, adding
  `docs/foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md`, in a
  separately authorized work package. The R3 Notes are operational evidence, so
  the correction touches no normative source, no Decision, no Risk, and no ADR.
- **Recommendation:** correct before Candidate Finalization. **Do not** redo the
  reconciliation — the nine-file implementation is correct and needs no change.

### Observations

**CDS-WP016-RECON-R3-RV-OBS-001** —
`docs/governance/FOUNDATION_CLOSURE_RECORD.md:85`, mandatory closure note 2,
reads "**Accessibility support baseline** — none is declared; AE-3 and therefore
Stable are unreachable." in the present tense, and the section carries no
temporal marker, unlike the adjacent table explicitly headed "State **at
closure**" (line 95). The reviewer classified this **Category C (historical /
revision-bound)**, not drift, on decisive evidence: the file has exactly **one**
commit in its entire history (`144cc58`, CDS-WP-009) and has never been revised,
so the table is a frozen dated record, not a maintained tracker; the header
bounds the document's normative force to closure fact, authority state at
closure, and phase boundary, and explicitly subordinates its summaries to the
source policies. It is also outside R3's Allowed Files, so R3 was correct not to
touch it. Note that the second half of the sentence ("AE-3 and therefore Stable
are unreachable") remains true today. Neither R2 nor R3 examined this line — both
examined only line 99 of the same file. A future authorized reconciliation should
consider adding an explicit temporal marker, or an "addressed policy-side by
CDS-WP-010" note in the gates column, in the style already used for note 3.

**CDS-WP016-RECON-R3-RV-OBS-002** — Runtime patch drift: the executor recorded
Python 3.13.14; this review ran Python 3.13.15. The seven dependency pins are
byte-identical and all three sentinels reproduce exactly, so the drift is
immaterial to the result. Recorded because DEC-S-068 / DEC-S-071 hold that
`latest` is not an identity, and the same discipline is worth applying to the
validator runtime when evidence-grade runs eventually occur.

**CDS-WP016-RECON-R3-RV-OBS-003** — WP-011…015 / ADR occurrence count: reviewer
54 versus executor 52, from `ADR-0001` and `ADR-0002` each being counted as 3
rather than 2 pre-commit clauses. Path membership is an exact 24/24 match. A
counting-criterion difference, not a substantive disagreement.

**CDS-WP016-RECON-R3-RV-OBS-004** — In
`docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md`, the section
"## Available evidence" opens with "**None.**" and its table now carries
"\| Support baseline \| **Declared and committed — A11Y-BL-001; a test contract,
never evidence** \|". The boundary holds — the row states inline that it is never
evidence — but an evidence inventory listing a non-evidence artifact invites
misreading. Optional editorial improvement for a future authorized pass; **not**
a defect and **not** a reason to change the row now.

### Counts

| Severity | Count |
| --- | --- |
| Blocking | **0** |
| High | **0** |
| Medium | **1** |
| Low | **0** |
| Observation | **4** |

## 23. Review gate

| Gate condition | Result |
| --- | --- |
| Independence PASS | ✓ |
| HEAD / Parent / Tree exact | ✓ |
| HEAD == origin/main | ✓ |
| Working tree and index CLEAN | ✓ |
| Delta = 9 modified + 1 added + 0 deleted | ✓ |
| Every implementation hunk status-only | ✓ (13/13 Category A, 0 Category B) |
| Accessibility Support Baseline self-consistent | ✓ |
| Evidence and Claims Model semantics unchanged | ✓ |
| All current CoreOps Pilot WP-010 sites reconciled | ✓ (5/5) |
| Decision semantics unchanged | ✓ (124 → 124) |
| Pre-Candidate plan scope clean | ✓ |
| Mixed control files WP-subject clean | ✓ |
| Current WP-010 Category A = 0 | ✓ |
| Current WP-010 Category B = 0 | ✓ |
| Same-file current contradictions = 0 | ✓ |
| R2 historical evidence unchanged | ✓ (blob-identical) |
| R3 Notes materially accurate | ✓ |
| **Future AE-1 inventory materially complete** | **✗ — F-001** |
| WP-007 drift untouched | ✓ |
| WP-011…015 / ADR drift untouched | ✓ |
| Candidate No · Semantic Status AE-0 · no AE-1/2/3/4 | ✓ |
| Governance unchanged | ✓ |
| 39/39 · 112/112 · 24/24 | ✓ |
| Markdown / encoding PASS | ✓ |
| 0 Blocking · 0 High · **0 Medium** | **✗ — 1 Medium** |

**Recommendation: NO-GO.** There is no `GO WITH NOTES` in this review.

## 24. Files changed by this review

### Added

- `docs/reviews/WP016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_INDEPENDENT_REVIEW.md`
- `project-brain/CDS_WP_016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_INDEPENDENT_REVIEW_NOTES.md`

### Modified

**NONE.**

### Deleted

**NONE.**

## 25. Binding review invariants

| Invariant | Result |
| --- | --- |
| `CDS_REVIEWER_IS_INDEPENDENT` | **PASS** |
| `CDS_REVIEWED_COMMIT_IDENTITY_IS_EXACT` | **PASS** |
| `CDS_R3_COMMITTED_SCOPE_IS_EXACT` | **PASS** |
| `CDS_R3_IMPLEMENTATION_IS_STATUS_ONLY` | **PASS** |
| `CDS_CURRENT_WP010_CATEGORY_A_IS_ZERO` | **PASS** |
| `CDS_CURRENT_WP010_CATEGORY_B_IS_ZERO` | **PASS** |
| `CDS_A11Y_BL_001_IS_COMMITTED` | **PASS** |
| `CDS_A11Y_BL_001_IS_NORMATIVE_AND_IN_EFFECT` | **PASS** |
| `CDS_BASELINE_IS_NOT_EVIDENCE` | **PASS** |
| `CDS_BASELINE_IS_NOT_SUPPORT` | **PASS** |
| `CDS_BASELINE_IS_NOT_CONFORMANCE` | **PASS** |
| `CDS_BASELINE_IS_NOT_CANDIDATE_AUTHORITY` | **PASS** |
| `CDS_ACCESSIBILITY_SUPPORT_BASELINE_IS_SELF_CONSISTENT` | **PASS** |
| `CDS_PILOT_CRITERION_BASELINE_STATE_IS_SELF_CONSISTENT` | **PASS** |
| `CDS_DECISION_SEMANTICS_ARE_UNCHANGED` | **PASS** |
| `CDS_MIXED_CONTROL_FILES_CHANGED_ONLY_FOR_WP010` | **PASS** |
| `CDS_R2_HISTORICAL_EVIDENCE_IS_UNCHANGED` | **PASS** |
| `CDS_R3_NOTES_ARE_OPERATIONAL_NOT_NORMATIVE` | **PASS** |
| `CDS_SEMANTIC_STATUS_REMAINS_AE0` | **PASS** |
| `CDS_NO_AE1_EXISTS` | **PASS** |
| `CDS_NO_AE2_EXISTS` | **PASS** |
| `CDS_NO_AE3_EXISTS` | **PASS** |
| `CDS_NO_AE4_EXISTS` | **PASS** |
| `CDS_CANDIDATE_REMAINS_NO` | **PASS** |
| `CDS_DECISION_COUNT_REMAINS_124` | **PASS** |
| `CDS_RISK_COUNT_REMAINS_97` | **PASS** |
| `CDS_RISK_DISTRIBUTION_REMAINS_90_7_0_0` | **PASS** |
| `CDS_ADR_COUNT_REMAINS_3` | **PASS** |
| `CDS_WP007_DRIFT_IS_UNTOUCHED` | **PASS** |
| `CDS_WP011_015_ADR_DRIFT_IS_UNTOUCHED` | **PASS** |
| `CDS_AE1_FUTURE_CURRENT_STATE_SET_IS_MATERIALLY_COMPLETE` | **FAIL** — F-001 |
| `CDS_HUMAN_MAINTAINER_RETAINS_GIT_AUTHORITY` | **PASS** |

## 26. Git / GitHub

| Action | State |
| --- | --- |
| HEAD | **unchanged** — `9f3ec243…6710d` |
| Index | **unchanged** |
| Commit / Push / Pull / Fetch | **NONE** |
| Merge / Rebase / Cherry-pick | **NONE** |
| Reset / Restore / Clean | **NONE** |
| Branch change / Tag / Release | **NONE** |
| History change | **NONE** |

Remote access was limited to read-only `git ls-remote origin refs/heads/main`.

## 27. Candidate decision

`CDS_WP_016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_REVIEW_REWORK_REQUIRED`

**Candidate Decision: No.** No artifact is promoted, no claim is created, no
accessibility evidence exists, and every CDS artifact remains **AE-0**.

## Related documents

- [R3 Notes (executor evidence)](../../project-brain/CDS_WP_016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R3_NOTES.md)
- [Independent R2 Review](WP016_ACCESSIBILITY_CURRENT_STATE_RECONCILIATION_R2_INDEPENDENT_REVIEW.md)
- [Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [CoreOps Pilot Accessibility Criterion](../governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md)
- [Pre-Candidate Operating Plan](../roadmap/PRE_CANDIDATE_OPERATING_PLAN.md)
- [Decision Index](../decisions/DECISION_INDEX.md)
- [Risk Register](../risks/RISK_REGISTER.md)
