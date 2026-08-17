# Semantic Status Candidate — AE-1 Clean-HEAD Reexecution Evidence Record (Provisional)

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Accessibility Gate Remediation,
  Post-Commit Clean-HEAD Revision-Bound Evidence Reexecution
- **Template:** [Accessibility Evidence Record Template](ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md)
- **Baseline:** A11Y-BL-001

> ## Evidence level
>
> ### **PROVISIONAL REVISION-BOUND AE-1 EVIDENCE CANDIDATE — PENDING FRESH INDEPENDENT EVIDENCE REVIEW**
>
> This record is **not admitted AE-1**. It is a provisional package offered *for*
> an independent **evidence** review that has **not yet taken place**.
>
> **The admitted accessibility evidence level of every CDS artifact remains
> AE-0**, and stays AE-0 until a fresh independent reviewer — who is not this
> record's executor — evaluates **this** package and it is accepted through the
> Nova and Human-Maintainer gates.
>
> **Result is not Candidate. Result is not admitted AE-1. Result is not a claim.
> Result is not WCAG conformance. Result is not accessibility certification.
> Result is not human approval.**

## Why this record exists

The predecessor record
[`AE1-CDS-WP016-SEMSTATUS-001`](SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md)
truthfully bound to `7ac8a9e7be021a05e517adda64751920a5eff247` **plus uncommitted
CDS-WP-016 working-tree changes**, with worktree state `modified worktree`. That
record's own next-review trigger 4 required re-execution against the committed
revision before the run could be presented as that revision's result.

The CDS-WP-016 remediation implementation has since been committed by the Human
Maintainer as `e6cb6fae63b1548ce4dabb7f5548116e4c61d622` and pushed
fast-forward to `origin/main`. This record is the **new, separate, immutable
per-run record** for a re-execution against that **clean committed revision**.

**Evidence is immutable once produced; change forces new evidence.** The
predecessor record and its two artifacts are therefore **unmodified** and remain
valid as **historical pre-commit evidence**. This record does not replace,
supersede, correct, or absorb them.

## Mandatory fields

### Identity and scope

| Field | Value |
| --- | --- |
| **Evidence ID** | `AE1-CDS-WP016-SEMSTATUS-002` |
| **Evidence level** | **AE-1 (provisional candidate)** — structural and automated evidence only |
| **Artifact or consumer** | The **Semantic Status Candidate source and contract family**: [Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) · [Status Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) · [Composition and Conflict Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) · [Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md) · [Terminology DE/EN](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md) · the `semantic/status` source set with manifest and resolver. **No consumer** — none exists and none is authorized. |
| **Declared scope** | **Channel-independent Layer-3 semantic source and contract family; source-level structural and rule-level checks only.** Explicitly outside scope: rendering, interaction, presentation, composition, product content, complete processes, and every consumer surface. |
| **CDS implementation revision** | **`e6cb6fae63b1548ce4dabb7f5548116e4c61d622`** — the committed HEAD, identical to `origin/main`, parent `7ac8a9e7be021a05e517adda64751920a5eff247`, subject `feat(cds): remediate WP-016 candidate accessibility gate` |
| **Worktree state at execution** | **`clean`.** Index CLEAN, working tree CLEAN, 0 untracked, no merge/rebase/cherry-pick/revert active — verified immediately before the run. See [Worktree state — execution versus persistence](#worktree-state--execution-versus-persistence). |
| **Artifact revision** | Source set **`semantic-status-rev-0001`** — unchanged by the remediation, which added validation and evidence capability, not token source content; contract family at the implementation revision above |
| **Baseline version** | **A11Y-BL-001**, revision declared 2026-07-16 and committed with CDS-WP-010 (`abe84b6b7267b8b9c5f96609e7c9d1ad1e68bc0a`) |
| **Freshness state (baseline)** | **`Current`** — determined 2026-08-17 by the [WP-016 Baseline Freshness Review](../reviews/WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md) against official primary sources (maintenance-policy trigger 1) |
| **Freshness state (this record)** | **`Current`** as of the test date, and bound to it. It decays with the artifact, the baseline, and the validator contract — see the [regression plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md). |
| **Language** | **DE and EN** — both, for the structural coverage checks |
| **Test date** | **2026-08-17** |

### Environment

*(Per the template's AE-1 rule for non-rendered source and contract artifacts.
Fields genuinely not exercised are recorded as `Not applicable with rationale`.
**No environment value is omitted, invented, inherited, or treated as passed.**)*

| Field | Value |
| --- | --- |
| **Channel** | **Not applicable — channel-independent Layer-3 semantic source/contract, per DEC-S-125.** No channel is assigned, because assigning one the artifact does not have would make the scope of this evidence untrue. Every future representation is a separate artifact with its own Channel Accessibility Profile and its own evidence; **nothing in this record transfers to it.** |
| **Operating-system family and exact version** | **Not applicable with rationale.** The artifact has no rendered surface, so no operating-system accessibility behaviour is exercised. *(The evidence was **produced** on Windows 11 with Python 3.13.15 — that is the tooling environment, recorded below under Execution environment. It is **not** an accessibility support environment and must not be read as one.)* |
| **Browser or renderer and exact version** | **Not applicable with rationale.** Nothing is rendered. No browser was involved in producing this evidence. |
| **Assistive technology and exact version** | **Not applicable with rationale.** There is no accessibility tree to expose. **No assistive technology was used, and none is claimed.** AE-3 remains absent (SSC-LIM-009). |
| **Input methods** | **Not applicable with rationale.** Nothing is operable; there is no keyboard, pointer, or touch surface. **No keyboard testing was performed, and none is claimed.** |
| **User testing** | **Not applicable with rationale — and not performed.** No user research exists (SSC-LIM-001). |

### Execution environment (tooling, not an accessibility environment)

| Field | Value |
| --- | --- |
| Platform | Windows 11 |
| Python | 3.13.15, run with `-B`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONNOUSERSITE=1` |
| Dependencies | Exact pins from `requirements-validator.lock`: `attrs==26.1.0`, `jsonschema==4.26.0`, `jsonschema-specifications==2025.9.1`, `referencing==0.37.0`, `rfc8785==0.1.4`, `rpds-py==2026.6.3`, `typing_extensions==4.16.0` — installed and verified exactly, with no additional package |
| Isolation | Fresh virtual environment created **outside** the repository; offline after installation; no network access at runtime; no bytecode written inside the repository |
| Determinism | The evidence runner was executed **twice** to two separate outputs **outside** the repository; the results were **byte-identical** (SHA-256 `2efbf8d0052add97d3acd4794ecf0d0d3817fb2876c8f0504e053582a0f06731`, 27 971 bytes each) |

### Worktree state — execution versus persistence

Two different states must not be conflated.

| # | State | Value |
| --- | --- | --- |
| A | **Evidence execution state** — the repository at the moment the runner read its inputs and produced the result | **CLEAN**, at `e6cb6fae63b1548ce4dabb7f5548116e4c61d622`, identical to `origin/main`, 0 untracked |
| B | **Repository state after this evidence package was persisted** | **Modified** — by exactly the four authorized evidence/notes candidate files of this run, and by nothing else |

State B does **not** retro-label state A. The recorded `worktreeState: clean` is a
true statement about the inputs the runner read, which were the committed bytes of
`e6cb6fa` and nothing else.

**The four files of this evidence package did not exist in `e6cb6fae63b1548ce4dabb7f5548116e4c61d622`.**
They are evidence **about** that implementation revision, produced after it, and
are themselves uncommitted at the time of writing. Presenting them as part of that
commit would be false.

### People

| Field | Value |
| --- | --- |
| **Executor** | Claude Opus 5 (`claude-opus-5`), acting as the scoped CDS-WP-016 **Evidence Executor** for the Post-Commit Clean-HEAD Revision-Bound AE-1 Evidence Reexecution, in a single authorized session, separate from the remediation implementation session. This executor authored **no** rule, fixture, expectation, runner, or test in this run — all of those were read unmodified from the committed revision. This executor **did** author this record, the digest artifact, and the notes section. |
| **Reviewer** | **PENDING — a fresh independent evidence reviewer is required.** Must be neither this executor nor the artifact itself (DEC-S-045). **Evidence reviewed only by its own executor has not been reviewed** (Evidence Strategy, *Review independence*). The executor has **not** self-reviewed this run and no reviewer identity is invented here. |
| **Nova review** | **Open.** |
| **Human-Maintainer approval** | **Open.** Final maturity authority is not delegable (DEC-S-036). |
| **Approval state** | **Unapproved / pending fresh independent evidence review.** |

## Review history — what has been reviewed and what has not

This record must not be read as claiming that no independent review has ever
happened. It also must not be read as claiming that the review that *did* happen
covers this run.

| Review | Subject | State |
| --- | --- | --- |
| **Fresh Independent Implementation Review** | The 32-file CDS-WP-016 remediation implementation candidate — including the authored validator rule, fixtures, expected classifications, runner, and tests, and the executor-self-confirmation / independence concern (F-002) | **Completed — PASS WITH NOTES**, and subsequently committed by the Human Maintainer as `e6cb6fa` |
| **Historical pre-commit evidence** (`AE1-CDS-WP016-SEMSTATUS-001`) | The pre-commit run against `7ac8a9e…` + modified worktree | Considered during that implementation review; **never admitted as AE-1** |
| **This run's evidence review** (`AE1-CDS-WP016-SEMSTATUS-002`) | This new clean-HEAD execution and its three new immutable artifacts | **PENDING — not started** |

**Admission does not transfer.** A completed review of the *implementation* and of
a *prior* run is not a review of *this* run's artifacts. `Review of prior run ≠
review of new run.` Consequently the admitted level stays **AE-0**.

**On F-002 specifically:** the independence concern about the authored rules,
fixtures, expectations, and tests was independently assessed in the implementation
review, and that assessment is **not reopened, rewritten, or re-litigated here**.
What that assessment does *not* do is admit a later evidence run. Method
independence review completed ≠ evidence admission completed. SSC-LIM-015 remains
recorded and remains the reason this record is provisional.

## Test cases, expected and actual

*(All results produced by actual execution against the committed revision.
Nothing below is hand-authored or carried over.)*

| # | Test case | Expected | Actual | Match |
| --- | --- | --- | --- | --- |
| 1 | Every authorized status token carries a non-empty textual `$description` in the real source | 25 / 25 | **25 / 25**, 0 missing | ✅ |
| 2 | DE/EN structural coverage of the 25 authorized technical identifiers | 25 / 25 rows, 25 EN, 25 DE, 0 duplicate, 0 unauthorized, 0 missing | **25 / 25 rows, 25 EN, 25 DE, 0 / 0 / 0** | ✅ |
| 3 | Per-value Candidate evidence requirement coverage (GAP-H-02) | 25 / 25 mapped, 0 `UNMAPPED` | **25 / 25**, 0 unmapped, 0 duplicate ids, 0 unauthorized ids | ✅ |
| 4 | Review-required combination coverage | 6 / 6 (RR-1 … RR-6) | **6 / 6** | ✅ |
| 5 | Fail-closed condition coverage | 8 / 8 (FC-1 … FC-8) | **8 / 8** | ✅ |
| 6 | Statement-case expected/actual classification agreement | 32 / 32 match | **32 / 32**, 0 failures, 0 blocked | ✅ |
| 7 | Targeted semantic-status suite at the committed revision | 47 / 47 | **47 / 47**, 0 failures, 0 skips, 0 errors | ✅ |
| 8 | Candidate-evidence suite at the committed revision | 40 / 40 | **40 / 40**, 0 failures, 0 skips, 0 errors | ✅ |
| 9 | Full `tests/validator` discovery at the committed revision | 160 / 160 | **160 / 160**, 0 failures, 0 skips, 0 errors | ✅ |
| 10 | Immutable WP-013/WP-015 24-case harness unchanged | 24 total, 24 matches, 0 mismatches, 0 execution errors, exit 0 | **24 / 24 / 0 / 0, exit 0** | ✅ |
| 11 | Evidence runner determinism at clean HEAD | Two runs byte-identical | **Byte-identical** — SHA-256 `2EFBF8D0…6731`, 27 971 bytes each | ✅ |
| 12 | Digest recomputation for this run | All entries identical on independent recomputation | **18 / 18 identical**, 0 mismatches | ✅ |
| 13 | Sixteen unchanged source, contract, fixture, validator, and test inputs digest-stable versus the predecessor evidence | No input digest drift | **16 / 16 unchanged** | ✅ |
| 14 | Historical pre-commit evidence artifacts unchanged by this run | Byte-identical before and after | **3 / 3 byte-identical** | ✅ |
| 15 | Neither fixture nor result asserts Candidate, Stable, or conformance | No prohibited claim phrase; boundaries explicit | **Confirmed** — `maturityState: Experimental`, `approvalState: Unapproved`, `candidateStatus: Not Candidate`, `admittedAccessibilityEvidenceLevel: AE-0`, `claims: none`, `conformanceStatement: none`, `humanApproval: none` | ✅ |

**Execution errors: 0. Blocked cases: 0. Expected/actual mismatches: 0.**
**No numeric or percentage accessibility score was produced** — `scoreProduced:
false`, and none exists.

### Delta against the historical pre-commit run

The runner code, fixtures, token source, terminology, source revision, and
normative rules are all unchanged. A field-by-field comparison of the two result
payloads produced **exactly two** semantic deltas, both of them the intended ones:

| Field | Historical pre-commit run | This clean-HEAD run |
| --- | --- | --- |
| `cdsRevision` | `7ac8a9e7be021a05e517adda64751920a5eff247` | **`e6cb6fae63b1548ce4dabb7f5548116e4c61d622`** |
| `worktreeState` | `modified worktree` | **`clean`** |

**Unexpected semantic deltas: 0.** Every other generated field — `schemaVersion`,
`testOnly`, `nonNormative`, `authority`, `workPackage`, `evidenceScope`,
`sourceRevision`, `inputs`, `caseManifestDigest`, `canonicalizationMethod`,
`digestAlgorithm`, `caseTotal`, all 32 case results, all 25 value-requirement
rows, `reviewRequiredCoverage`, `failClosedCoverage`, `sourceDescriptionCoverage`,
`deEnStructuralCoverage`, `failures`, `blocked`, `executionErrors`,
`resultStatus`, `coverageStatesWithLimitation`, `scoreProduced`, and
`boundaries` — is identical.

That the two runs agree is a **consistency** observation, not a strengthening of
either. It adds no evidence level and admits nothing.

## Result status

> ### **`Pass with limitations`**

`Pass with limitations` is the honest status because three of the 25 per-value
requirements are `COVERED_WITH_LIMITATION` rather than `COVERED`
([matrix](SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md) rows 12, 13,
22 — `confidence.supported`, `confidence.uncertain`, `evidence.partial`), and
because the whole package carries the sixteen limitations below.

**What this result is bound to:** this artifact family, **this committed
implementation revision**, this declared source-level scope, this baseline
revision, these two languages, and this test date. Nothing else.

**What this result is not:**

| It is **not** | Because |
| --- | --- |
| Accessibility | Nothing was tested with a user, an assistive technology, a browser, or a keyboard. |
| A WCAG statement | 50 of 55 applicable criteria were not assessable at this scope; the other 5 have only a source-level component. |
| Admitted AE-1 | The fresh independent evidence review of **this** run has not happened. |
| A Candidate award | Candidate remains **No**. |
| Human approval | An automated result is input to a review, never the review (DEC-S-053). |
| Transferable to the historical run, or from it | Evidence never transfers across revision or worktree state (DEC-S-052). |

## Known limitations

All sixteen are recorded in full, with the normative 15 fields each, in the
[Semantic Status Candidate Accessibility Limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md):

**0 Critical · 11 Significant · 5 Minor.** Zero Critical is a statement about the
artifact's scope, not about its quality — no user-facing process exists that a
user group could be blocked from completing.

**No limitation was closed, downgraded, averaged, or converted by this run.** The
three `COVERED_WITH_LIMITATION` rows remain exactly
`confidence.supported`, `confidence.uncertain`, and `evidence.partial`; none was
upgraded to `COVERED`. No representation behaviour is claimed. The inputs are
unchanged, so no limitation change was expected and none was made.

The limitation that bears most directly on **this** record is **SSC-LIM-015 —
executor self-confirmation partially mitigated, not erased**. It is not erased by
this run: although this executor authored no rule, fixture, expectation, or test
here, the artifacts of this run are still executor-produced and still unreviewed.
That is precisely why this record is provisional.

## Defects

**None known and open** against the contract family or the source set at record
time. Any Blocking or High defect found in the fresh independent evidence review
re-opens this record and invalidates its result for the affected scope.

## Deviations

**None.** No normative source was deviated from, no gate was bypassed, the
immutable WP-013/WP-015 24-case matrix was not modified (DEC-S-120), and the three
historical pre-commit evidence artifacts were not modified.

## Source references

### This run (current, revision-bound)

| Kind | Path |
| --- | --- |
| Results artifact | [`artifacts/validation/wp016-candidate-accessibility-clean-reexecution-results.json`](../../artifacts/validation/wp016-candidate-accessibility-clean-reexecution-results.json) |
| Digest artifact | [`artifacts/validation/wp016-candidate-accessibility-clean-reexecution-digests.json`](../../artifacts/validation/wp016-candidate-accessibility-clean-reexecution-digests.json) |

### Predecessor (historical pre-commit evidence — **not** this revision's result)

| Kind | Path |
| --- | --- |
| Historical evidence record `…-001` | [`SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md`](SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md) |
| Historical results artifact | [`artifacts/validation/wp016-candidate-accessibility-remediation-results.json`](../../artifacts/validation/wp016-candidate-accessibility-remediation-results.json) |
| Historical digest artifact | [`artifacts/validation/wp016-candidate-accessibility-remediation-digests.json`](../../artifacts/validation/wp016-candidate-accessibility-remediation-digests.json) |

These three are **historical pre-commit evidence**, bound to
`7ac8a9e7be021a05e517adda64751920a5eff247` plus a `modified worktree`. They are
referenced for traceability only and **must never be presented as this committed
revision's result**.

### Unchanged inputs and governing documents

| Kind | Path |
| --- | --- |
| Evidence runner | [`tests/validator/semantic_status_candidate_evidence_runner.py`](../../tests/validator/semantic_status_candidate_evidence_runner.py) |
| Evidence suite | [`tests/validator/test_semantic_status_candidate_evidence.py`](../../tests/validator/test_semantic_status_candidate_evidence.py) |
| Statement fixture (test-only) | [`tests/fixtures/semantic-status-statements/CANDIDATE_EVIDENCE_CASES.json`](../../tests/fixtures/semantic-status-statements/CANDIDATE_EVIDENCE_CASES.json) |
| Negative token fixture | [`tests/fixtures/semantic-status/negative/missing-description.tokens.json`](../../tests/fixtures/semantic-status/negative/missing-description.tokens.json) |
| Requirements matrix | [Evidence Requirements Matrix](SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md) |
| WCAG mapping | [WCAG Applicability Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md) |
| Responsibility mapping | [Accessibility Responsibility Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_RESPONSIBILITY_MAPPING.md) |
| Baseline plan | [Support Baseline Plan](../governance/SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md) |
| AE-2 plan | [AE-2 Evidence Plan](../governance/SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md) |
| Regression plan | [Accessibility Regression Plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md) |
| Limitations | [Accessibility Limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md) |
| Baseline freshness | [WP-016 A11Y Baseline Freshness Review](../reviews/WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md) |

## Fulfilled transition (historical, not an open trigger)

The predecessor record's next-review trigger 4 — *commit of the CDS-WP-016
working-tree changes* — **has occurred**, on `e6cb6fae63b1548ce4dabb7f5548116e4c61d622`.
This record is the re-execution that trigger required. It is recorded here as a
**fulfilled historical transition** and is **not** carried forward as an open
trigger.

## Next review trigger

This record must be re-executed and re-reviewed on **any** of the following.

| # | Trigger |
| --- | --- |
| 1 | **Immediately — the fresh independent evidence review of this run**, which is the reason this record is provisional. Until it completes, nothing here is admitted. |
| 2 | Any of the **15 accessibility regression triggers** (T-01 … T-15) in the [regression plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md). |
| 3 | **A11Y-BL-001 revision or freshness change** — including the forward-looking Windows 11 24H2 servicing end on **2026-10-14 (PT)**, and the six-month maximum review gap on **2027-02-17**. |
| 4 | **Semantic Status source or contract revision change** — any move away from `semantic-status-rev-0001`, or any change to the five normative contract documents. |
| 5 | Any **validator-contract change** affecting the diagnostics, categories, or check semantics used here. |
| 6 | Any **terminology or DE/EN change** affecting the 25 authorized identifiers or their labels. |
| 7 | The **first rendered or channel representation**, at which point AE-2 and AE-3 become required, a Channel Accessibility Profile applies, and this record's scope explicitly does not extend. |
| 8 | **Any change that invalidates the exact bound implementation revision or declared scope** — including a new commit that touches any of the sixteen frozen inputs. |

**No evidence transfers across any of these.** A new trigger means a new run and a
new record, not an amendment of this one.

## Closing boundary

**Candidate = No. Maturity = Experimental. Approval = Unapproved. Admitted
accessibility evidence level = AE-0. Claims = none. Pilot = inactive.
CDS-WP-017 = not activated. Publication = Private Development.**

None of these changes because this record exists.
