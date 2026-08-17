# CDS-WP-016 — Candidate Accessibility Gate Remediation — Notes

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-016 — Candidate Accessibility Gate Remediation
  (**internal rework of CDS-WP-016 — NOT a new work package; CDS-WP-017 is not
  created, not authorized, and not activated**)
- **Date:** 2026-08-17
- **Executor:** Claude Opus 5 (`claude-opus-5`), Executor R1, single session
- **Runs:** **R1** (full remediation) · **R1.1** (narrow current-state count rework
  — Nova-authorized correction of F-001 only) · **R1.2** (narrow README
  register-mirror rework — Nova-authorized correction of F-006 only); see the
  final two sections
- **Status:** **NON-NORMATIVE EXECUTION / EVIDENCE NOTES.** Not a normative
  source, not evidence, not a review, not an approval.

## Baseline at start

| Property | Value |
| --- | --- |
| Repository root | `D:\Projects\Core-Design-System` |
| Branch | `main` |
| HEAD | `7ac8a9e7be021a05e517adda64751920a5eff247` |
| `origin/main` | `7ac8a9e7be021a05e517adda64751920a5eff247` |
| Ahead / behind | 0 / 0 |
| Index | CLEAN |
| Working tree | CLEAN |
| Untracked | 0 |
| Merge / rebase / cherry-pick / revert | none active |

Baseline gate: **PASS.**

## Human-Maintainer authorization

Authorized on 2026-08-17: the CDS-WP-016 Candidate Accessibility Gate
Remediation; acceptance of the Nova resolution of **GAP-B-07**; preparation of
**DEC-S-125** as a normative clarification; **GAP-H-02** to be closed before
Candidate promotion. Explicitly excluded: Candidate promotion, Stable promotion,
claims, pilot start, Product Profiles, visual foundations, a repository-presentation
work package, CDS-WP-017, external benchmark provenance, and any Git write by
Claude. Human-Maintainer Git and maturity authority unchanged.

## Nova resolution of GAP-B-07

A Channel Accessibility Profile applies when an artifact **instantiates,
transforms, renders, or communicates** CDS meaning through a named CDS channel. A
channel-independent Layer-3 Semantic Source or Contract may be assessed for
Candidate under its own **source-level** maturity and accessibility gates without
selecting an artificial channel. Before any downstream channel representation may
itself reach Candidate or Stable, its applicable Channel Accessibility Profile and
revision-bound channel evidence must exist. **Source evidence does not transfer to
the channel; channel evidence does not transfer back to the source.** The
resolution waives no accessibility requirement, waives no AE-1, creates no
channel, and authorizes no UI, repository presentation, PDF, Product Profile, or
consumer evidence.

## DEC-S-125

Prepared as **DEC-S-125 — Channel accessibility profiles gate channel artifacts,
not channel-independent semantic sources**; Status **Accepted**; Date
**2026-08-17**; Type **Accessibility / maturity / channel boundary decision**;
Work package **CDS-WP-016**. It records the six substantive points of the Nova
resolution, preserves **DEC-S-058** and **DEC-S-029**, keeps the AE-1 requirement,
and grants no Candidate status. **Decision count 124 → 125. No Risk ID was added.**

The over-broad sentence *"Non-interactive artifacts require a channel profile
first"* in `ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md` was **narrowly
reconciled** by an additive subsection: the profile requirement now attaches to
channel representations/outputs, while channel-independent source/contract
artifacts are governed by their own source-level Candidate accessibility gate.
Nothing was weakened. `ACCESSIBILITY_CHANNEL_PROFILES.md` was **not touched**, and
**GAP-L-01 was deliberately not repaired**.

## PRE sentinels (independently verified before mutation)

| Sentinel | PRE value |
| --- | --- |
| Decisions | **124** (headings 124, `Accepted` 124) |
| Superseded / Withdrawn | **0 / 0** |
| Risks | **97** (headings 97) |
| Risk distribution | **90 Monitored · 7 Mitigating · 0 Accepted · 0 Closed** |
| ADRs | **3** |
| AE-1 Future Mirror Inventory | **33** |
| Ambiguous paths | **1** |
| CDS-WP-017 | not activated |
| Candidate / Maturity / Approval | No / Experimental / Unapproved |
| Admitted AE | **AE-0** |
| Claims / Pilot / Publication | none / inactive / `Private Development` |
| Targeted semantic-status tests | **39 / 39** unique IDs, OK |
| Full validator tests | **112 / 112** unique IDs, OK |
| 24-case harness | **24 total · 24 matches · 0 mismatches · 0 execution errors**, exit 0 |
| Real source `$description` coverage | **25 / 25** non-empty (STOP condition not triggered) |

## POST sentinels

| Sentinel | POST value | Expected |
| --- | --- | --- |
| Decisions | **125** (headings 125, `Accepted` 125) | 125 ✅ |
| Superseded / Withdrawn | **0 / 0** | ✅ |
| Risks | **97** | 97 ✅ |
| Risk distribution | **90 / 7 / 0 / 0** | ✅ |
| ADRs | **3** | ✅ |
| AE-1 Future Mirror Inventory | **33** — unchanged, not edited | ✅ |
| Ambiguous paths | **1** — unchanged | ✅ |
| CDS-WP-017 | not activated | ✅ |
| Candidate / Maturity / Approval | **No / Experimental / Unapproved** | ✅ |
| Admitted AE | **AE-0** | ✅ |
| Provisional AE-1 package | present, independent review **pending** | ✅ |
| Claims / Pilot / Publication | none / inactive / `Private Development` | ✅ |
| Targeted semantic-status tests | **47** (39 PRE preserved + 8 new), OK | ✅ |
| New Candidate evidence suite | **40**, OK | ✅ |
| Full validator tests | **160** (112 PRE preserved + 48 new), OK | ✅ |
| 24-case harness | **24 / 24 / 0 / 0**, exit 0 | unchanged ✅ |

## Remediation artifacts

### Created (17)

| # | Path |
| --- | --- |
| 1 | `docs/governance/SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md` |
| 2 | `docs/governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_RESPONSIBILITY_MAPPING.md` |
| 3 | `docs/governance/SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md` |
| 4 | `docs/governance/SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md` |
| 5 | `docs/governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md` |
| 6 | `docs/governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md` |
| 7 | `docs/operations/SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md` |
| 8 | `docs/operations/SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md` |
| 9 | `docs/reviews/WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md` |
| 10 | `docs/reviews/WP016_CANDIDATE_ACCESSIBILITY_GATE_ADDENDUM.md` |
| 11 | `artifacts/validation/wp016-candidate-accessibility-remediation-results.json` |
| 12 | `artifacts/validation/wp016-candidate-accessibility-remediation-digests.json` |
| 13 | `tests/fixtures/semantic-status/negative/missing-description.tokens.json` |
| 14 | `tests/fixtures/semantic-status-statements/CANDIDATE_EVIDENCE_CASES.json` |
| 15 | `tests/validator/test_semantic_status_candidate_evidence.py` |
| 16 | `tests/validator/semantic_status_candidate_evidence_runner.py` |
| 17 | `project-brain/CDS_WP_016_CANDIDATE_ACCESSIBILITY_GATE_REMEDIATION_NOTES.md` (this file) |

### Modified (15)

`README.md` · `CLAUDE.md` · `docs/decisions/DECISION_INDEX.md` ·
`docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md` ·
`docs/operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md` ·
`docs/operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md` ·
`docs/roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md` ·
`tools/cds_validator/semantic_status.py` · `tools/cds_validator/diagnostics.py` ·
`tests/validator/test_semantic_status.py` · `project-system/NEXT_PHASE.md` ·
`project-system/WORK_PACKAGES.md` · `project-system/PROJECT_PROFILE.md` ·
`project-system/CONTEXT_PACK_FOUNDATION.md` · `project-brain/PROJECT_BRAIN.md`

**Total candidate scope: 32 files (15 existing + 17 new) — the maximum permitted.
No 33rd file was required and no forbidden file was modified.**

## Gap coverage

| Gap | Disposition |
| --- | --- |
| GAP-B-01 Candidate Plan omits the gate | Additive correction section + current blockers list; historical ten-prerequisite plan retained |
| GAP-B-02 No AE-1 / no instantiated record | Provisional AE-1 evidence record + results and digest artifacts |
| GAP-B-03 No baseline plan, Trigger-1 review missing | Support baseline plan + freshness review (result **`Current`**) |
| GAP-B-04 No regression plan | 15-trigger regression plan (13 assessed, 2 traceable splits, 0 losses) |
| GAP-B-05 No candidate-scope WCAG / responsibility mapping | Both mappings created |
| GAP-B-06 No reasoned AE-2 plan | AE-2 plan with 11 required elements |
| GAP-B-07 Channel-profile applicability ambiguous | **DEC-S-125** + narrow policy reconciliation |
| GAP-H-01 GO scoped against incomplete prerequisites | Recorded in the review addendum and the plan correction; **GO not revoked** |
| GAP-H-02 25 per-value requirements unmapped | Evidence requirements matrix — **25/25 mapped, 0 UNMAPPED** |
| GAP-M-01 Text-first not machine-enforced | `CDS-V4-STATUS-DESCRIPTION` + negative fixture + tests |
| GAP-M-02 DE/EN parity not machine-enforced | Structural 25/25 check; **meaning explicitly not machine-checked** |
| GAP-M-03 Template lacks an AE-1 rule for non-rendered artifacts | Additive template section; no mandatory field weakened |
| GAP-M-04 Dossier limitations insufficient | 16-entry limitations set with the normative 15 fields |
| GAP-L-01 Channel-profiles wording inconsistency | **Deliberately NOT repaired.** Preserved follow-up (WP-007/WP-010 temporal reconciliation class) |
| WP016-OBS-001/002/003 | **Preserved, unresolved, unchanged** |

## Evidence identities

| Artifact | Identity |
| --- | --- |
| Results artifact | `artifacts/validation/wp016-candidate-accessibility-remediation-results.json` — file SHA-256 `0dbd26fd323f9a2f90fc79c25354c644ebbae931aca1df0bc98df28d7289e79c` |
| Case manifest content digest | `sha256:6ab8ae5f0b15017d18d5efa18b23db1439d6d153015bcc860930cb97eab6ee55` (RFC 8785 + SHA-256) |
| Digest artifact | `artifacts/validation/wp016-candidate-accessibility-remediation-digests.json` — **18 digest entries** (6 JSON content digests, 10 non-JSON file digests, 2 results-artifact entries) |
| Evidence Record ID | `AE1-CDS-WP016-SEMSTATUS-001` |
| Bound CDS revision | `7ac8a9e7be021a05e517adda64751920a5eff247` |
| Worktree state recorded | **`modified worktree`** — binds to uncommitted content; **never** to be presented as the committed revision's result |
| Source revision | `semantic-status-rev-0001` |

## Test and execution commands

Isolated virtual environment created **outside** the repository, from
`requirements-validator.lock` (7/7 exact pins), Python 3.13.15, offline after
install, `PYTHONDONTWRITEBYTECODE=1` and `python -B` throughout.

```
python -m venv <outside-repo>/cds-validator-venv
<venv>/Scripts/python -m pip install -r requirements-validator.lock
```

```
python -B -m unittest tests.validator.test_semantic_status -v
python -B -m unittest tests.validator.test_semantic_status_candidate_evidence -v
python -B -m unittest discover -s tests/validator -t . -p "test_*.py" -v
python -B -m tools.cds_validator validate-cases tests/fixtures/machine-readable/VALIDATION_CASES.json
python -B -m tests.validator.semantic_status_candidate_evidence_runner \
  --cases tests/fixtures/semantic-status-statements/CANDIDATE_EVIDENCE_CASES.json \
  --token-source tokens/semantic/status/semantic-status.tokens.json \
  --terminology docs/foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md \
  --cds-revision 7ac8a9e7be021a05e517adda64751920a5eff247 \
  --source-revision semantic-status-rev-0001 \
  --worktree-state "modified worktree" --output <outside-repo>/out.json
```

## Test results

| Layer | Result |
| --- | --- |
| A — pre-existing targeted regression | **39 / 39** PRE test IDs preserved and passing |
| B — updated semantic-status module | **47** tests, OK |
| C — new Candidate evidence suite | **40** tests, OK |
| D — full validator regression | **160** tests, OK; **112 / 112** PRE test IDs preserved and passing; **0 missing** |
| E — existing 24-case harness | **24 total · 24 matches · 0 mismatches · 0 execution errors**, exit 0 — matrix unmodified |
| F — Candidate evidence runner | `Pass with limitations`, exit 0 |
| G — deterministic re-execution | two runs, **byte-identical** (`0DBD26FD…E79C`, 27 943 bytes each) |
| H — digest verification | **18 / 18** digests identical on recomputation |

## Coverage sentinels

| Sentinel | Value |
| --- | --- |
| Value-requirement coverage (GAP-H-02) | **25 / 25** · 0 `UNMAPPED` · 0 duplicate ids · 0 unauthorized ids |
| Review-required coverage | **6 / 6** (RR-1 … RR-6) |
| Fail-closed coverage | **8 / 8** (FC-1 … FC-8) |
| Source `$description` coverage | **25 / 25** |
| DE/EN structural coverage | **25 / 25** rows · 25 EN · 25 DE · 0 duplicate · 0 unauthorized · 0 missing |
| Statement cases | **32**, 32 expected/actual matches |
| Failures / blocked / execution errors | **0 / 0 / 0** |

## Baseline freshness result

**A11Y-BL-001 freshness = `Current`** (2026-08-17), determined by
maintenance-policy trigger 1 against **official primary sources only**: W3C
(WCAG 2.2 still a Recommendation, 2024-12-12, no superseding version), Microsoft
Lifecycle (Windows 11 24H2 / 25H2 / 26H1 all in support), Microsoft Edge release
schedule (2-week Stable cadence from v152 — **already recorded on 2026-07-16**,
therefore not a change since the baseline), Mozilla (Firefox 4-week rapid release,
annual ESR), NV Access (NVDA free/open source, 64-bit Windows 10/11 and Server
2016+). **Zero drift** against the recorded facts. Two non-blocking observations
recorded (OBS-BFR-001 end-date rendering convention; OBS-BFR-002 NVDA platform
note — no CDS Required entry affected). No benchmark, brand, or design-inspiration
source was consulted or introduced.

## Limitations

**16 recorded · 0 Critical · 11 Significant · 5 Minor.** All actual user impacts
are `Unknown / not directly evaluated at source-only scope`, because no
user-facing representation exists. **Zero Critical is a statement about the
artifact's scope, not about its quality**, and the reasoning is stated openly in
the limitations document for the reviewer to test first. The most load-bearing
entry is **SSC-LIM-015 — executor self-confirmation partially mitigated, not
erased**: the same executor wrote the rule, the fixtures, the expectations, and
the tests.

## Open reviewer gate

**A fresh independent review of this remediation is required and has not
happened.** Until it does:

- the AE-1 evidence is **provisional**, never admitted AE-1;
- the **admitted accessibility evidence level of every CDS artifact remains
  AE-0**;
- the **Nova Candidate gate is open**;
- the **Human-Maintainer Candidate gate is not yet reached**.

## What this remediation did not do

**No Candidate promotion. No AE-1 admission. No Stable. No claim of any kind. No
Product Profile. No visual value. No new channel. No consumer integration. No
pilot start. No AE-2/AE-3/AE-4 execution. No CDS-WP-017. No repository
presentation or GitHub profile work. No PB001 use. No external benchmark
provenance. No new Risk ID. No new work-package ID. No Git write of any kind —
no `add`, `commit`, `push`, `pull`, `fetch`, `merge`, `rebase`, `cherry-pick`,
`reset`, `restore`, `checkout`, `clean`, `stash`, branch, tag, or release.**

The index remained **CLEAN** throughout; only the working tree carries the
32 candidate files.

## Drift disclosure

**No repository-wide zero-drift claim is made.** Discovery was scoped to the
Candidate-Accessibility-Gate remediation current-state class. Pre-existing drift
outside that class is preserved and unrepaired, including:

- **`project-system/PROJECT_PROFILE.md` "Register scope"** — **F-001, reported by
  R1 as preserved-and-unfixed, CLOSED by R1.1.** R1 recorded that the bullet still
  opened with `Decisions: DEC-S-001 … DEC-S-104 (104)` while enumerating groups
  through DEC-S-125, judged it a pre-existing WP-011…015-class drift, and
  deliberately did not repair it. **Nova rejected that disposition**: the file is an
  explicitly authorized active Current-State Mirror, and the R1 prompt required
  current Decision-count mirrors inside the authorized seven to be reconciled. The
  correction was made in R1.1 — see
  [R1.1 Narrow Current-State Count Rework](#r11-narrow-current-state-count-rework).
  The R1 disposition is retained above as execution history, not as the current
  state.
- GAP-L-01 · F-N1 · F-C · F-A · F-B · F-N2 · F-R4 · F-R5 · F-R6 · F-03…F-07 ·
  the 52/54 reconciliation · the WP-007 drift class · the WP-011…015 / ADR drift
  class · the architecture residual · risk-review-trigger governance · decision
  supersession policy work · WP016-OBS-001…003.

## Skills

NDF Skills inventory and provenance inspected
(`project-system/NDF_SKILLS_INVENTORY.md`, 38 docs-only Skills under
`.claude/skills/`). **No Skill was loaded or applied**: this work package's binding
procedure is fully specified by the authorized prompt, `CLAUDE.md`, and the
normative accessibility, evidence, limitation, and maturity policies, and no
installed docs-only Skill would have materially improved or constrained it beyond
those. **Skills grant no authority in any case.** No Skill file was modified.

## R1.1 Narrow Current-State Count Rework

*(Additive. Nova-authorized narrow correction of **F-001 only**. This is **not** a
new remediation round and **not** a new work package.)*

### Nova reclassification of F-001

R1 reported F-001 as **Medium**, *old residual*, non-blocking, "separate
reconciliation". **Nova rejected that disposition for this Candidate.**

**Reason:** `project-system/PROJECT_PROFILE.md` was an **explicitly authorized
active Current-State Mirror**, and the R1 prompt explicitly required current
Decision-count mirrors inside the authorized seven mirrors to be reconciled. A
stale current mirror in an authorized mirror file is a reconciliation failure, not
an inherited residual.

Binding reclassification:

| Property | Value |
| --- | --- |
| Severity | Medium |
| Candidate Blocking | **NO** |
| Commit Blocking | **YES** until corrected |
| Independent Review Readiness Blocking | **YES** until corrected |

### Pre-state and authoritative state

| | Value |
| --- | --- |
| Path | `project-system/PROJECT_PROFILE.md`, section `## Register scope` |
| Stale current boundary | `Decisions: DEC-S-001 … DEC-S-104 (104)` |
| Authoritative current state | **`DEC-S-001 … DEC-S-125`**, count **125** |
| Why it was current, not historical | The bullet carries no date, no work-package snapshot label, and no "as of" qualifier; the Risks bullet directly below it uses the same syntax and states the **current** total (97). The section's convention is current-state totals. |
| Internal proof of the target value | The bullet's own group enumeration sums to exactly **125**: 6 + 6 + 8 + 12 + 16 + 12 + 4 + 8 + 10 + 10 + 12 + 10 + 10 + 1. Only the header boundary was stale. |

### Correction performed

The header boundary was updated from `DEC-S-001 … DEC-S-104 (104)` to
`DEC-S-001 … DEC-S-125 (125)`. **One line changed. Repository syntax and style
preserved.**

Explicitly **not** changed:

- historical Decision counts anywhere in the repository;
- the CDS-WP-013 group range `DEC-S-093 … DEC-S-104`, which is a correct **group**
  range and not a register boundary;
- the decision reference `DEC-S-104` elsewhere in the file;
- Risk counts, ADR counts, AE counts;
- unrelated register semantics;
- any historical snapshot.

**No historical count normalization was performed. No scope expansion occurred.**

### Digest conditional gate

The declared scope of
`artifacts/validation/wp016-candidate-accessibility-remediation-digests.json` is
**18 entries**: 6 RFC 8785 content digests, 10 non-JSON file digests, and 2
results-artifact entries. **Neither `project-system/PROJECT_PROFILE.md` nor these
Notes is in that scope.** Per the R1.1 rule, the digest artifact was therefore
**not modified and remains byte-identical to R1**, and digest coverage was **not**
expanded merely because a file changed.

### Files changed relative to R1

Exactly **2**:

1. `project-system/PROJECT_PROFILE.md`
2. `project-brain/CDS_WP_016_CANDIDATE_ACCESSIBILITY_GATE_REMEDIATION_NOTES.md`
   (this file)

The remaining **30** candidate files are **byte-identical to R1**. Candidate shape
unchanged: 15 modified · 17 untracked · 0 deleted · **32 total** · Index **CLEAN**.

### Findings disposition after R1.1

| Finding | State |
| --- | --- |
| **F-001** current Decision-count mirror | **CLOSED** by this rework. The original R1 report of it is retained in the drift-disclosure section as execution history. |
| **F-002** executor self-confirmation | **Open — reviewer-owned.** Not touched, not weakened, not self-resolved. |
| **F-003** evidence bound to `modified worktree` | **Open — post-commit sequencing.** Deliberately not solved here; see below. |
| **F-004** "0 Critical" premise | **Open — reviewer-owned.** Premise to be verified first by the fresh independent reviewer. |
| **F-005** three `COVERED_WITH_LIMITATION` rows | **Open — reviewer judgement required.** |
| OBS-BFR-001, OBS-BFR-002 | Preserved, unchanged. |

### F-003 sequencing boundary

R1.1 does **not** attempt to solve F-003. The provisional evidence package remains
correctly bound to the **committed baseline HEAD plus a modified worktree**, and is
**not** relabelled as committed-revision evidence. The expected future sequence,
subject to the fresh independent review, is: independent review of the
implementation candidate → Human-Maintainer implementation commit if authorized →
clean post-commit re-execution against that exact implementation revision →
revision-bound evidence finalization → independent evidence review → Nova Candidate
re-review → Human-Maintainer maturity decision. **R1.1 collapses none of these
authorities.**

### State after R1.1 — unchanged

**Candidate No · Maturity Experimental · Approval Unapproved · admitted
accessibility evidence AE-0 · provisional AE-1 present and pending fresh
independent review · Claims none · Pilot inactive · Publication Private
Development · CDS-WP-017 not activated.**

Decisions **125** · Accepted **125** · Superseded **0** · Withdrawn **0** · Risks
**97** (90/7/0/0) · ADRs **3** · AE-1 Mirror **33** · Ambiguous **1** — unchanged
from R1 apart from nothing at all: R1.1 changed **no** sentinel.

**No Git write of any kind was performed in R1.1. The index remained CLEAN.**

## R1.2 Narrow README Register-Mirror Rework

*(Additive. Nova-authorized narrow correction of **F-006 only**. Not a new
remediation round and not a new work package.)*

### Why R1.2 exists

**R1.1 final decision: `REMEDIATION_REWORK_REQUIRED`.** The F-001 correction
itself succeeded, but the recount mandated by the R1.1 prompt surfaced a **second
active register mirror of the same defect class**, in `README.md` — a file inside
the authorized seven current-state mirrors but **outside the R1.1 allowed file
set**. R1.1 therefore reported it instead of fixing it, and did not self-authorize
a scope expansion. Nova verified F-006 independently against the committed
baseline and authorized this narrow R1.2.

**F-001 remains CLOSED.** `project-system/PROJECT_PROFILE.md` was **not** touched
in R1.2; its R1.1 bytes are unchanged.

### F-006 — the finding

| | |
| --- | --- |
| Path | `README.md`, section `## Registers` |
| Discovered | R1.1, during the mandated targeted recount |
| Why it is a **current-state mirror**, not a historical snapshot | No date qualifier; no "as of WP-x" qualifier; presented under the current README `## Registers` heading; sits directly above the links to the current Decision and Risk registers; the same semantic role as the `## Register scope` section of `PROJECT_PROFILE.md`; and its values materially conflicted with the current authoritative registers. |
| Pre-existing | Yes — already stale at the committed baseline `7ac8a9e…`, from the CDS-WP-011/012 era. Verified with `git show HEAD:README.md`. Neither R1 nor R1.1 touched the section. |
| Why R1 missed it | The R1 recount searched for the **previous** count value (`124`). The README mirror stood at `82` and therefore never matched. **The R1 report's claim that the current mirrors had been reconciled was, to that extent, incomplete.** R1.2 replaced the value-pattern search with a per-file semantic inspection of every register region. |

### Pre-state and authoritative state

| Register | Pre-state in README | Authoritative current state |
| --- | --- | --- |
| Decisions | `DEC-S-001 … DEC-S-082 (82)` | **`DEC-S-001 … DEC-S-125`, 125** (Accepted 125, Superseded 0, Withdrawn 0) |
| ADRs | `2 (ADR-0001, ADR-0002)` | **3 (ADR-0001, ADR-0002, ADR-0003)** |
| Risks | `RISK-001 … RISK-072 (72)` | **`RISK-001 … RISK-097`, 97** |
| Risk distribution | `70 Monitored, RISK-040 and RISK-044 Mitigating` | **90 Monitored · 7 Mitigating · 0 Accepted · 0 Closed** |

The bullet was additionally **internally inconsistent before the correction**: its
own category breakdown already listed ten groups summing to **92** while the
headline read **82**, because CDS-WP-012 appended its group without updating the
headline.

### Authoritative sources used

Every value was re-derived read-only from the current registers, not carried over
from a prior report:

| Source | What was derived |
| --- | --- |
| `docs/decisions/DECISION_INDEX.md` | 125 `## DEC-S-nnn` headings, 125 unique IDs, range DEC-S-001 … DEC-S-125, 125 `Accepted`, 0 `Superseded`, 0 `Withdrawn`, `DEC-S-125` present exactly once; and the **"Decision types" table** as the authoritative group breakdown |
| `docs/risks/RISK_REGISTER.md` | 97 `## RISK-nnn` headings, 97 unique IDs, range RISK-001 … RISK-097, 90 `Monitored`, 7 `Mitigating`, 0 `Accepted`, 0 `Closed`; the **seven Mitigating IDs derived by nearest-preceding-heading association**, not inferred: RISK-040, RISK-044, RISK-066, RISK-067, RISK-068, RISK-069, RISK-071 |
| `docs/decisions/ADR-*.md` + the ADR-range line in the Decision Index | 3 ADR files; `ADR range: ADR-0001 … ADR-0003 (3 ADRs)` |

### Correction performed

The **detailed category breakdown was retained**, not simplified — the
`DECISION_INDEX` "Decision types" table supplies an authoritative, stable group
classification, so no category had to be invented and nothing was lost. The four
missing post-DEC-S-092 groups were appended verbatim from that table:

- 12 offline validator implementation decisions (CDS-WP-013)
- 10 semantic status foundation decisions (CDS-WP-014)
- 10 semantic status source and evidence decisions (CDS-WP-015)
- 1 accessibility / maturity / channel boundary decision (CDS-WP-016)

**Breakdown arithmetic after correction:**
6 + 6 + 8 + 12 + 16 + 12 + 4 + 8 + 10 + 10 + 12 + 10 + 10 + 1 = **125**, equal to
the headline. The bullet is now internally and externally consistent.

The Risk bullet now states the range, the total, an explicit **7 Mitigating** with
all seven IDs, and retains the repository's existing `owner model finalized; no
risk accepted or closed` wording, which carries the 0 Accepted / 0 Closed state.

**Explicitly not changed:** links above and below the section · Foundation review
history · historical work-package descriptions · Candidate state · accessibility
state · publication wording · any unrelated README prose. **No reformatting, no
navigation change, no badges, no branding, no Repository Presentation work.**

### Digest conditional gate

The declared scope of
`artifacts/validation/wp016-candidate-accessibility-remediation-digests.json`
remains **18 entries** (6 RFC 8785 content digests, 10 non-JSON file digests, 2
results-artifact entries). **Neither `README.md` nor these Notes is in that
scope.** The digest artifact was therefore **not modified** and remains
byte-identical to R1, and digest coverage was **not** expanded merely because a
file changed.

### Files changed relative to R1.1

Exactly **2**:

1. `README.md`
2. `project-brain/CDS_WP_016_CANDIDATE_ACCESSIBILITY_GATE_REMEDIATION_NOTES.md`
   (this file)

The remaining **30** candidate files are byte-identical to R1.1. Candidate shape
unchanged: 15 modified · 17 untracked · 0 deleted · **32 total** · Index **CLEAN**.
A README edit does not increase the candidate count, because README was already an
R1 candidate file.

### Findings disposition after R1.2

| Finding | State |
| --- | --- |
| **F-001** stale Decision boundary in `PROJECT_PROFILE.md` | **CLOSED** in R1.1. Untouched by R1.2. |
| **F-006** stale register mirror in `README.md` | **CLOSED** by this rework. Its R1.1 discovery record is retained above and in the R1.1 section — the execution trace stays visible. |
| **F-002** executor self-confirmation | **Open — reviewer-owned.** Untouched. |
| **F-003** evidence bound to `modified worktree` | **Open — post-commit sequencing.** Untouched; provisional evidence is **not** relabelled as committed-revision evidence. |
| **F-004** "0 Critical" premise | **Open — reviewer-owned.** Untouched. |
| **F-005** three `COVERED_WITH_LIMITATION` rows | **Open — reviewer judgement required.** Not upgraded to `COVERED`. |
| OBS-BFR-001, OBS-BFR-002 | Preserved, unchanged. |

### Register-mirror audit across the authorized seven

Each file was inspected **semantically** for any current region carrying
`Decisions`, `DEC-S-`, `Risks`, `RISK-`, `ADRs`, `Registers`, or `Register scope`
— no expected old value was used as a search trigger.

| File | Decision mirror | Risk mirror | ADR mirror | Classification |
| --- | --- | --- | --- | --- |
| `README.md` | 125 | 97 · 90/7/0/0 | 3 | **CURRENT_TRUE** (corrected by R1.2) |
| `CLAUDE.md` | none | none | none | n/a — no register mirror |
| `project-system/NEXT_PHASE.md` | none | none | none | n/a |
| `project-system/WORK_PACKAGES.md` | none | none | none | n/a |
| `project-system/PROJECT_PROFILE.md` | 125 | 97 · 90/7 | 3 | **CURRENT_TRUE** (corrected by R1.1) |
| `project-system/CONTEXT_PACK_FOUNDATION.md` | 125 | 97 · 90/7 | 3 | **CURRENT_TRUE** |
| `project-brain/PROJECT_BRAIN.md` | 125 | 97 · 90/7 | 3 | **CURRENT_TRUE** |

**Unresolved CURRENT_DRIFT in the Decision / Risk / ADR register-mirror class
across the seven active orientation files: 0.**

Historical counts in review evidence and prior work-package notes remain unchanged
and are classified **HISTORICAL_IMMUTABLE** / **REVIEW_EVIDENCE**. **No historical
count was normalized.**

### State after R1.2 — unchanged

**Candidate No · Maturity Experimental · Approval Unapproved · admitted
accessibility evidence AE-0 · provisional AE-1 present and pending fresh
independent review · Claims none · Pilot inactive · Publication Private
Development · CDS-WP-017 not activated.**

Decisions **125** · Accepted **125** · Superseded **0** · Withdrawn **0** · Risks
**97** (90/7/0/0) · ADRs **3** · AE-1 Mirror **33** · Ambiguous **1**. **R1.2
changed no sentinel** — it only made an orientation document agree with registers
that already held these values.

**No Git write of any kind was performed in R1.2. The index remained CLEAN.**

## Post-Commit Clean-HEAD Revision-Bound Evidence Reexecution

**Run:** R2 — scoped **Evidence Executor** run, separate session. **Not** a new
work package, **not** a new remediation run, **not** a review, **not** an
approval. No code, fixture, test, rule, or semantic source was authored or
touched in this run.

### Human-Maintainer integration state

| Property | Value |
| --- | --- |
| Implementation commit | `e6cb6fae63b1548ce4dabb7f5548116e4c61d622` |
| `origin/main` | `e6cb6fae63b1548ce4dabb7f5548116e4c61d622` (identical) |
| Parent | `7ac8a9e7be021a05e517adda64751920a5eff247` |
| Subject | `feat(cds): remediate WP-016 candidate accessibility gate` |
| Ahead / behind | 0 / 0 |
| Implementation gate | **PASS** |
| Fresh Independent Implementation Review | **PASS WITH NOTES** |
| Repository before evidence execution | Index CLEAN · working tree CLEAN · 0 untracked · no merge/rebase/cherry-pick/revert |

Baseline gate for this run: **PASS.**

### Evidence identities

| Property | Historical (pre-commit) | New (clean HEAD) |
| --- | --- | --- |
| Evidence ID | `AE1-CDS-WP016-SEMSTATUS-001` | **`AE1-CDS-WP016-SEMSTATUS-002`** |
| Bound CDS revision | `7ac8a9e7be021a05e517adda64751920a5eff247` **+ uncommitted CDS-WP-016 working-tree changes** | **`e6cb6fae63b1548ce4dabb7f5548116e4c61d622`** |
| Worktree state at execution | `modified worktree` | **`clean`** |
| Source revision | `semantic-status-rev-0001` | `semantic-status-rev-0001` (unchanged) |
| Status | **Preserved immutable — byte-identical before and after this run** | Provisional; fresh evidence review **PENDING** |

The three historical artifacts —
`artifacts/validation/wp016-candidate-accessibility-remediation-results.json`,
`artifacts/validation/wp016-candidate-accessibility-remediation-digests.json`, and
`docs/operations/SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md` — were **not
edited, not rewritten, and not superseded**. Evidence is immutable once produced;
change forces new evidence.

### Execution

Isolated virtual environment **outside** the repository, Python **3.13.15**, the
seven exact pins from `requirements-validator.lock` and nothing else, offline
after installation, `python -B` with `PYTHONDONTWRITEBYTECODE=1` and
`PYTHONNOUSERSITE=1`. Both runner executions wrote to temporary paths **outside**
the repository, before any repository mutation.

| Run | Exit | SHA-256 | Bytes |
| --- | --- | --- | --- |
| Clean-HEAD run 1 | **0** | `2efbf8d0052add97d3acd4794ecf0d0d3817fb2876c8f0504e053582a0f06731` | 27 971 |
| Clean-HEAD run 2 | **0** | `2efbf8d0052add97d3acd4794ecf0d0d3817fb2876c8f0504e053582a0f06731` | 27 971 |

**Byte-identical and hash-identical — determinism gate PASS.**

Runner result: **`Pass with limitations`**, `caseTotal` **32**, failures **0**,
blocked **0**, execution errors **0**, `scoreProduced` **false**.

### Coverage

| Sentinel | Value |
| --- | --- |
| Per-value requirement coverage (GAP-H-02) | **25 / 25** · 0 unmapped · 0 duplicate · 0 unauthorized |
| Review-required combinations | **6 / 6** (RR-1 … RR-6) |
| Fail-closed conditions | **8 / 8** (FC-1 … FC-8) |
| Source `$description` coverage | **25 / 25** · 0 missing |
| DE/EN structural coverage | **25 / 25** rows · 25 EN · 25 DE · 0 duplicate · 0 unauthorized · 0 missing |

### Regression (identical before and after evidence persistence)

| Suite | Result |
| --- | --- |
| `tests.validator.test_semantic_status` | **47 / 47** · 0 failures · 0 skips · 0 errors |
| `tests.validator.test_semantic_status_candidate_evidence` | **40 / 40** · 0 failures · 0 skips · 0 errors |
| Full `tests/validator` discovery | **160 / 160** · 0 failures · 0 skips · 0 errors |
| Immutable WP-013/WP-015 24-case harness | **24 total · 24 matches · 0 mismatches · 0 execution errors**, exit 0 |

No test count was normalized. The immutable 24-case matrix was not modified
(DEC-S-120).

### Result delta versus the historical pre-commit run

Field-by-field comparison of the two result payloads: **exactly 2 semantic
deltas**, both intended — `cdsRevision` and `worktreeState`. **Unexpected deltas:
0.** All other generated fields, including all 32 case results and all 25
value-requirement rows, are identical.

### New digest artifact

`artifacts/validation/wp016-candidate-accessibility-clean-reexecution-digests.json`
— **18 / 18** entries independently recomputed, **0 mismatches**: 6 RFC 8785
canonical-content digests, 10 raw file digests, 1 results canonical-content
digest, 1 results raw file digest. The **16** unchanged source, contract, fixture,
validator, and test digests are **identical** to the predecessor digest artifact —
**no input digest drift**.

### Limitations — unchanged

**16 total · 0 Critical · 11 Significant · 5 Minor.** The three
`COVERED_WITH_LIMITATION` rows remain `confidence.supported`,
`confidence.uncertain`, and `evidence.partial`. Nothing was closed, downgraded,
averaged, or upgraded to `COVERED`. No representation behaviour is claimed.

### Disposition

| Item | State |
| --- | --- |
| F-003 revision-binding requirement | **SATISFIED_BY_CLEAN_HEAD_REEXECUTION** |
| F-003 governance closure | **NOT closed** — the fresh independent evidence review of this new package has not happened |
| Fresh independent evidence review | **PENDING** |
| F-002 (executor self-confirmation) | Independently assessed in the implementation review; **not reopened**. Method independence review completed ≠ evidence admission completed. |
| Admitted accessibility evidence level | **AE-0** |
| Candidate | **No** |
| Maturity | **Experimental** |
| Approval | **Unapproved** |
| Claims | **None** |
| Pilot | **inactive** |
| CDS-WP-017 | **not activated** |

The new evidence files did **not** exist in `e6cb6fa`; they are evidence **about**
that revision. The repository is clean *at execution* and modified *after
persistence* by exactly the four authorized candidate files — these are two
different states and are not conflated.

**No Git write of any kind was performed in R2. The index remained CLEAN. No
staging occurred. Historical R1 / R1.1 / R1.2 sections above are unchanged.**
