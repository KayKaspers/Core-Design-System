# Semantic Status Candidate — AE-1 Evidence Record (Provisional)

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Accessibility Gate Remediation
- **Template:** [Accessibility Evidence Record Template](ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md)
- **Baseline:** A11Y-BL-001

> ## Evidence level
>
> ### **PROVISIONAL AE-1 EVIDENCE CANDIDATE — PENDING FRESH INDEPENDENT REVIEW**
>
> This record is **not admitted AE-1**. It is a provisional package offered *for*
> an independent review that has **not yet taken place**.
>
> **The admitted accessibility evidence level of every CDS artifact remains
> AE-0**, and stays AE-0 until a fresh independent reviewer — who is not this
> record's executor — evaluates this package and it is accepted through the Nova
> and Human-Maintainer gates.
>
> **Result is not Candidate. Result is not admitted AE-1. Result is not a claim.
> Result is not human approval.**

## Mandatory fields

### Identity and scope

| Field | Value |
| --- | --- |
| **Evidence ID** | `AE1-CDS-WP016-SEMSTATUS-001` |
| **Evidence level** | **AE-1 (provisional candidate)** — structural and automated evidence only |
| **Artifact or consumer** | The **Semantic Status Candidate source and contract family**: [Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) · [Status Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) · [Composition and Conflict Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) · [Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md) · [Terminology DE/EN](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md) · the `semantic/status` source set with manifest and resolver. **No consumer** — none exists and none is authorized. |
| **Declared scope** | **Source-level and contract-level structural properties only**, for a channel-independent Layer-3 semantic source and contract. Explicitly outside scope: rendering, interaction, presentation, composition, product content, complete processes, and every consumer surface. |
| **CDS version or revision** | `7ac8a9e7be021a05e517adda64751920a5eff247` (committed HEAD) **plus the uncommitted CDS-WP-016 working-tree changes** |
| **Worktree state** | **`modified worktree`.** This run binds to uncommitted content and **must never be presented as the committed revision's result**. |
| **Artifact revision** | Source set `semantic-status-rev-0001`; contract family at the revision above |
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
| Python | 3.13.15, run with `-B` and `PYTHONDONTWRITEBYTECODE=1` |
| Dependencies | Exact pins from `requirements-validator.lock`: `attrs==26.1.0`, `jsonschema==4.26.0`, `jsonschema-specifications==2025.9.1`, `referencing==0.37.0`, `rfc8785==0.1.4`, `rpds-py==2026.6.3`, `typing_extensions==4.16.0` |
| Isolation | Fresh virtual environment created **outside** the repository; offline after installation; no network access at runtime |
| Determinism | The evidence runner was executed **twice** to separate outputs; the results were **byte-identical** |

### People

| Field | Value |
| --- | --- |
| **Executor** | Claude Opus 5 (`claude-opus-5`), acting as the CDS-WP-016 Candidate Accessibility Gate Remediation Executor R1, in a single authorized session. The executor authored the validator rule, the fixtures, the expected classifications, the runner, and the tests. |
| **Reviewer** | **PENDING — a fresh independent reviewer is required.** Must be neither this executor nor the artifact itself (DEC-S-045). **Evidence reviewed only by its own executor has not been reviewed** (evidence rule 10). The executor's identity is deliberately **not** entered here. |
| **Nova review** | **Open.** |
| **Human-Maintainer approval** | **Open.** Final maturity authority is not delegable (DEC-S-036). |
| **Approval state** | **Unapproved / pending independent review.** |

## Test cases, expected and actual

*(All results produced by actual execution. Nothing below is hand-authored.)*

| # | Test case | Expected | Actual | Match |
| --- | --- | --- | --- | --- |
| 1 | Every authorized status token carries a non-empty textual `$description` in the real source | 25 / 25 | **25 / 25**, 0 missing | ✅ |
| 2 | DE/EN structural coverage of the 25 authorized technical identifiers | 25 / 25 rows, 25 EN, 25 DE, 0 duplicate, 0 unauthorized, 0 missing | **25 / 25 rows, 25 EN, 25 DE, 0 / 0 / 0** | ✅ |
| 3 | Per-value Candidate evidence requirement coverage (GAP-H-02) | 25 / 25 mapped, 0 `UNMAPPED` | **25 / 25**, 0 unmapped, 0 duplicate ids, 0 unauthorized ids | ✅ |
| 4 | Review-required combination coverage | 6 / 6 (RR-1 … RR-6) | **6 / 6** | ✅ |
| 5 | Fail-closed condition coverage | 8 / 8 (FC-1 … FC-8) | **8 / 8** | ✅ |
| 6 | Statement-case expected/actual classification agreement | 32 / 32 match | **32 / 32**, 0 failures, 0 blocked | ✅ |
| 7 | Text-first rule fails closed on missing, whitespace-only, and non-string `$description` | Fail closed in all three forms | **Fails closed in all three**; `CDS-V4-STATUS-DESCRIPTION`, category `semantic-status-description` | ✅ |
| 8 | Negative fixture `missing-description.tokens.json` blocks at V4 | V4 `Fail`, blocking layer V4 | **V4 `Fail`, blocking layer V4** | ✅ |
| 9 | Real source set still passes the full validator scope | V1–V3 Pass, V4 not `Fail`/`Blocked`, 0 status errors | **Unchanged; 0 status errors** | ✅ |
| 10 | Pre-existing targeted semantic-status test IDs preserved and passing | 39 / 39 | **39 / 39 preserved and passing** (suite now 47) | ✅ |
| 11 | Pre-existing full validator test IDs preserved and passing | 112 / 112 | **112 / 112 preserved and passing** (suite now 160) | ✅ |
| 12 | Immutable WP-013/WP-015 24-case harness unchanged | 24 total, 24 matches, 0 mismatches, 0 execution errors, exit 0 | **24 / 24 / 0 / 0, exit 0** | ✅ |
| 13 | Evidence runner determinism | Two runs byte-identical | **Byte-identical** (`0DBD26FD…E79C`) | ✅ |
| 14 | Digest recomputation | All digests identical on recomputation | **18 / 18 identical** | ✅ |
| 15 | Neither fixture nor result asserts Candidate, Stable, or conformance | No prohibited claim phrase; boundaries explicit | **Confirmed** — `maturityState: Experimental`, `approvalState: Unapproved`, `candidateStatus: Not Candidate`, `admittedAccessibilityEvidenceLevel: AE-0`, `claims: none` | ✅ |

**Execution errors: 0. Blocked cases: 0. Expected/actual mismatches: 0.**
**No numeric or percentage accessibility score was produced** — none exists.

## Result status

> ### **`Pass with limitations`**

`Pass with limitations` is the honest status because three of the 25 per-value
requirements are `COVERED_WITH_LIMITATION` rather than `COVERED`
([matrix](SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md) rows 12, 13,
22), and because the whole package carries the sixteen limitations below.

**What this result is bound to:** this artifact family, this revision, this
declared source-level scope, this baseline revision, these two languages, and
this test date. Nothing else.

**What this result is not:**

| It is **not** | Because |
| --- | --- |
| Accessibility | Nothing was tested with a user, an assistive technology, a browser, or a keyboard. |
| A WCAG statement | 50 of 55 applicable criteria were not assessable at this scope; the other 5 have only a source-level component. |
| Admitted AE-1 | The independent review has not happened. |
| A Candidate award | Candidate remains **No**. |
| Human approval | An automated result is input to a review, never the review (DEC-S-053). |

## Known limitations

All sixteen are recorded in full, with the normative 15 fields each, in the
[Semantic Status Candidate Accessibility Limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md):

**0 Critical · 11 Significant · 5 Minor.** Zero Critical is a statement about the
artifact's scope, not about its quality — no user-facing process exists that a
user group could be blocked from completing.

The limitation that bears most directly on **this record** is **SSC-LIM-015 —
executor self-confirmation partially mitigated, not erased**: the same executor
wrote the rule, the fixtures, the expectations, and the tests. That is precisely
why this record is provisional.

## Defects

**None known and open** against the contract family or the source set at record
time. Any Blocking or High defect found in the independent review re-opens this
record and invalidates its result for the affected scope.

## Deviations

**None.** No normative source was deviated from, no gate was bypassed, and the
immutable WP-013/WP-015 24-case matrix was not modified (DEC-S-120).

## Source references

| Kind | Path |
| --- | --- |
| Results artifact | [`artifacts/validation/wp016-candidate-accessibility-remediation-results.json`](../../artifacts/validation/wp016-candidate-accessibility-remediation-results.json) |
| Digest artifact | [`artifacts/validation/wp016-candidate-accessibility-remediation-digests.json`](../../artifacts/validation/wp016-candidate-accessibility-remediation-digests.json) |
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

## Next review trigger

This record must be re-executed and re-reviewed on **any** of the following.

| # | Trigger |
| --- | --- |
| 1 | **Immediately — the fresh independent review**, which is the reason this record is provisional (SSC-LIM-015). |
| 2 | Any of the **15 accessibility regression triggers** (T-01 … T-15) in the [regression plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md). |
| 3 | **A11Y-BL-001 revision or freshness change** — including the forward-looking Windows 11 24H2 servicing end on **2026-10-14 (PT)**, and the six-month maximum review gap on **2027-02-17**. |
| 4 | **Commit of the CDS-WP-016 working-tree changes** — this record currently binds to a `modified worktree` and must be re-executed against the committed revision before it can be presented as that revision's result. |
| 5 | Any **validator-contract change** affecting the diagnostics, categories, or check semantics used here. |
| 6 | The **first rendered representation**, at which point AE-2 and AE-3 become required and this record's scope explicitly does not extend. |

## Closing boundary

**Candidate = No. Maturity = Experimental. Approval = Unapproved. Admitted
accessibility evidence level = AE-0. Claims = none. Pilot = inactive.
Publication = Private Development.**

None of these changes because this record exists.
