# Semantic Status Candidate — Proposed Candidate Revision-Bound AE-1 Evidence Record

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Finalization Preparation
  (Human-Maintainer authorized 2026-08-19; internal preparation, **not** a new
  work package)
- **Template:** [Accessibility Evidence Record Template](ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md)
- **Baseline:** A11Y-BL-001

> ## Evidence level
>
> ### **PROVISIONAL REVISION-BOUND AE-1 EVIDENCE CANDIDATE — UNREVIEWED — NOT ADMITTED**
>
> This record is **not admitted AE-1**. It is a provisional package offered *for*
> a **fresh independent evidence review that has not yet taken place**.
>
> It is bound to **uncommitted, non-authoritative Proposed Candidate bytes**
> (`semantic-status-rev-0002-candidate`). Those bytes carry **no authority of any
> kind**.
>
> **Result is not Candidate. Result is not admitted AE-1. Result is not a claim.
> Result is not WCAG conformance. Result is not accessibility certification.
> Result is not human approval. Result is not a promotion.**

## Why this record exists

The Human Maintainer authorized, on **2026-08-19**, the preparation of a named
**Proposed Candidate Revision** and of **fresh revision-bound evidence** against
exactly those bytes.

**Evidence never transfers across a source revision** (DEC-S-126). The admitted
`AE1-CDS-WP016-SEMSTATUS-002` is bound exclusively to
`semantic-status-rev-0001`. It therefore says nothing about
`semantic-status-rev-0002-candidate`, and could not be reused for it. A later
Candidate revision requires **fresh evidence, a fresh independent review, and a
fresh admission**. This record is that fresh evidence — and only the evidence.

The two historical evidence packages and the rev-0001 admission record are
**unmodified**. This record does not replace, supersede, correct, or absorb them.

## Authority distinction — the two states this record keeps apart

Conflating these two states would be the single most damaging error a reader
could make here, so they are stated separately and explicitly.

### A. Current authoritative committed repository

| Field | Value |
| --- | --- |
| **Baseline commit** | **`8d1374fa4c61cc1eed214823681ee1209a2d91f7`** — identical to `origin/main`, parent `42bcba65aa6767e3f7ebee2a01e496eafcc82a54`, subject `feat(cds): establish WP-016 candidate finalization governance` |
| **Authoritative Semantic Status source revision** | **`semantic-status-rev-0001`** |
| **Maturity** | **`Experimental`** |
| **Approval** | **`Unapproved`** |
| **Candidate** | **No** |
| **Current admitted accessibility evidence** | **`AE1-CDS-WP016-SEMSTATUS-002`, AE-1**, admitted 2026-08-17 — see the [AE-1 Admission Record](../governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md) |
| **Scope of that admission** | The channel-independent Semantic Status Layer-3 **source/contract family at `semantic-status-rev-0001` only**. Every other CDS artifact remains **AE-0**. |

### B. Proposed source bytes under evidence in this record

| Field | Value |
| --- | --- |
| **Source revision** | **`semantic-status-rev-0002-candidate`** |
| **Source-declared TARGET maturity** | `Candidate` |
| **Source-declared TARGET approval** | `Approved` |
| **Authority context** | **`proposed-candidate`** — caller-declared, never inferred from ambient Git state |
| **Status** | **uncommitted · non-authoritative · not current · not promoted** |

> **TARGET METADATA IN PROPOSED BYTES DOES NOT CHANGE CURRENT REPOSITORY
> MATURITY.**
>
> The values `Candidate` and `Approved` exist inside the proposed bytes so that
> those bytes are internally coherent as the **exact future Candidate bytes**.
> They are a *target*, not a state. Until a Human-Maintainer **Promotion Commit**,
> the authoritative source revision remains `semantic-status-rev-0001` with
> maturity `Experimental`, approval `Unapproved`, and Candidate `No`.

## Mandatory fields

### Identity and scope

| Field | Value |
| --- | --- |
| **Evidence ID** | `AE1-CDS-WP016-SEMSTATUS-003` |
| **Evidence level represented** | **AE-1 (provisional candidate)** — structural and automated evidence only |
| **Evidence class** | **Structural and Automated Evidence** — an **AE-1 Evidence Candidate**, not admitted evidence |
| **Artifact or consumer** | The **Semantic Status Candidate source and contract family**: [Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) · [Status Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) · [Composition and Conflict Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) · [Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md) · [Terminology DE/EN](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md) · the `semantic/status` source set with manifest and resolver, **at the Proposed Candidate bytes**. **No consumer** — none exists and none is authorized. |
| **Declared scope** | **Channel-independent Layer-3 semantic source and contract family; source-level structural and rule-level checks only.** Explicitly outside scope: rendering, interaction, presentation, composition, product content, complete processes, and every consumer surface. |
| **CDS baseline revision** | **`8d1374fa4c61cc1eed214823681ee1209a2d91f7`** — the committed authoritative baseline **from which** the Proposed Candidate was prepared. **This does not claim that the Proposed Candidate bytes are contained in that commit. They are not.** |
| **Artifact revision (the evidenced bytes)** | **`semantic-status-rev-0002-candidate`** — uncommitted Proposed Candidate source bytes, frozen before evidence execution |
| **Worktree state at execution** | **`modified worktree`** — see [Execution versus persistence](#worktree-state--execution-versus-persistence) |
| **Baseline version** | **A11Y-BL-001**, revision declared 2026-07-16, committed with CDS-WP-010 |
| **Freshness state (baseline)** | **`Current`** — determined 2026-08-17 by the [WP-016 Baseline Freshness Review](../reviews/WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md) |
| **Freshness state (this record)** | **`Current`** as of the test date and bound to it. It decays with the artifact, the baseline, and the validator contract. |
| **Language** | **DE and EN** — both, for the structural coverage checks |
| **Test date** | **2026-08-19** |

### Environment

*(Per the template's AE-1 rule for non-rendered source and contract artifacts.
Fields genuinely not exercised are recorded as `Not applicable with rationale`.
**No environment value is omitted, invented, inherited, or treated as passed.**)*

| Field | Value |
| --- | --- |
| **Channel** | **Not applicable — channel-independent Layer-3 semantic source/contract, per DEC-S-125.** No channel is assigned. Every future representation is a separate artifact with its own Channel Accessibility Profile and its own evidence; **nothing in this record transfers to it.** |
| **Operating-system family and exact version** | **Not applicable with rationale.** The artifact has no rendered surface, so no operating-system accessibility behaviour is exercised. *(The evidence was **produced** on Windows 11 with Python 3.13.15 — tooling only, recorded below. It is **not** an accessibility support environment.)* |
| **Browser or renderer and exact version** | **Not applicable with rationale.** Nothing is rendered. No browser was involved. |
| **Assistive technology and exact version** | **Not applicable with rationale.** There is no accessibility tree to expose. **No assistive technology was used, and none is claimed.** AE-3 remains absent (SSC-LIM-009). |
| **Input methods** | **Not applicable with rationale.** Nothing is operable. **No keyboard testing was performed, and none is claimed.** |
| **User testing** | **Not applicable with rationale — and not performed.** No user research exists (SSC-LIM-001). |

### Execution environment (tooling, not an accessibility environment)

| Field | Value |
| --- | --- |
| Platform | Windows 11 |
| Python | 3.13.15, run with `-B`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONNOUSERSITE=1`, external `PYTHONPYCACHEPREFIX` |
| Dependencies | Exact pins from `requirements-validator.lock`: `attrs==26.1.0`, `jsonschema==4.26.0`, `jsonschema-specifications==2025.9.1`, `referencing==0.37.0`, `rfc8785==0.1.4`, `rpds-py==2026.6.3`, `typing_extensions==4.16.0` — installed with `pip --isolated`, no upgrade, no additional package |
| Isolation | Fresh virtual environment created **outside** the repository; network used only for that one dependency bootstrap; offline afterwards; no bytecode written inside the repository |
| Determinism | The evidence runner was executed **twice** to two separate outputs **outside** the repository; the results were **byte-identical** (SHA-256 `cc918d562a8d7da17f462ce8a3040933d6c5fb850dbb8f85bd07464a2bbae1d0`, 30 432 bytes each). The digest package was likewise generated **twice** externally and was **byte-identical** (SHA-256 `8902b12285091cbc4e921dd8675ed8937b98374dc7cdc556b55062da7ee4feee`, 8 445 bytes each). |

### Worktree state — execution versus persistence

Two different states must not be conflated, and the later one must not retro-label
the earlier one.

| # | State | Value |
| --- | --- | --- |
| A | **Evidence execution state** — the repository at the moment the runner read its inputs and produced the result | HEAD `8d1374fa4c61cc1eed214823681ee1209a2d91f7`, **index CLEAN**, tracked working-tree changes = **exactly the three frozen Proposed Candidate source files and nothing else**, source authority context `proposed-candidate` |
| B | **Repository state after this evidence package was persisted** | Additionally contains the results artifact, the digest artifact, this record, and the preparation notes — the four authorized new files of this preparation, and nothing else |

Evidence execution occurred **after** the three Proposed Candidate source files
were frozen but **before** the repository evidence files were persisted. State B
does **not** retro-label state A.

**None of the seven files of this preparation exist in
`8d1374fa4c61cc1eed214823681ee1209a2d91f7`.** They are, respectively, proposed
bytes for a future revision and evidence *about* those bytes. Presenting either as
part of that commit would be false.

### People

| Field | Value |
| --- | --- |
| **Executor** | Claude Opus 5 (`claude-opus-5`), acting as the scoped CDS-WP-016 **Candidate Finalization Preparation Executor** in a single authorized session. This executor authored **no** rule, fixture, expectation, runner, validator, or test in this run — all were read unmodified from the committed baseline. This executor **did** author the three Proposed Candidate metadata mutations, this record, the digest artifact, and the preparation notes. |
| **Reviewer** | **PENDING — a fresh independent evidence reviewer is required.** Must be neither this executor nor the artifact itself (DEC-S-045). **Evidence reviewed only by its own executor has not been reviewed** (Evidence Strategy, *Review independence*). The executor has **not** self-reviewed this run, and no reviewer identity is invented here. |
| **Nova evidence review / adjudication** | **PENDING.** |
| **Human-Maintainer evidence admission** | **NOT GRANTED.** |
| **Human-Maintainer Candidate approval** | **NOT GRANTED.** Final maturity authority is not delegable (DEC-S-036). |
| **Approval state** | **Unapproved / pending fresh independent evidence review.** |

## The complete machine Evidence Package — NF-R11-001

**NF-R11-001 is binding for this evidence: the Runner Result alone is NOT a
complete Evidence Package.**

The complete machine Evidence Package for `AE1-CDS-WP016-SEMSTATUS-003` is the
**pair**:

| # | Member | Path |
| --- | --- | --- |
| 1 | **Runner Result** | [`artifacts/validation/wp016-candidate-finalization-proposed-candidate-results.json`](../../artifacts/validation/wp016-candidate-finalization-proposed-candidate-results.json) |
| 2 | **Digest Package** | [`artifacts/validation/wp016-candidate-finalization-proposed-candidate-digests.json`](../../artifacts/validation/wp016-candidate-finalization-proposed-candidate-digests.json) |

**Neither artifact alone is sufficient for review.** The result states what was
checked; the digest package states *which exact bytes* were checked. A review of
one without the other cannot establish that the reviewed bytes are the evidenced
bytes. This record binds and explains the pair.

### Exact-byte identities

| Item | Value |
| --- | --- |
| Result — raw SHA-256 | `cc918d562a8d7da17f462ce8a3040933d6c5fb850dbb8f85bd07464a2bbae1d0` |
| Result — byte length | `30432` |
| Result — RFC 8785 content digest | `sha256:0b299fc99fe96f86075c94a01eb517efbfa37a876386e6d8f7a6acd7c924f96b` |
| Digest Package — raw SHA-256 | `8902b12285091cbc4e921dd8675ed8937b98374dc7cdc556b55062da7ee4feee` |
| Digest Package — byte length | `8445` |
| Source Manifest — SHA-256 | `3b80d1483ceba4de61c5f9b1f99e10ff00f6da17ac935a1ddfa643a413204ebf` |
| Source Manifest — entries / bytes | `3` / `497` |

### The three evidenced Proposed Candidate source files

| Path | Raw SHA-256 | Bytes |
| --- | --- | --- |
| `tokens/semantic/status/semantic-status.tokens.json` | `53312e93810a6296c2b82b9365d17d14e7e74485cdeb5e13bba149634d4cb55e` | `6358` |
| `tokens/semantic/status/semantic-status.source-set.json` | `8dda44d28ac654c33892e4c362c83260ba2bd1ab97526ef90dbddb6f72d52ef6` | `1041` |
| `tokens/semantic/status/semantic-status.resolver.json` | `0d9ff65fb65c9eca3abe5f3bd6bf37492b043c8308191feda9c8319a43c45004` | `572` |

## What the run reported

| Property | Value |
| --- | --- |
| Result schema version | `cds-wp016-candidate-accessibility-evidence-result/2` |
| `sourceDeclaredMetadata.sourceRevision` | `semantic-status-rev-0002-candidate` |
| `sourceDeclaredMetadata.maturityState` | `Candidate` (**target metadata**) |
| `sourceDeclaredMetadata.approvalState` | `Approved` (**target metadata**) |
| `sourceDeclaredMetadata.declaresCandidateTargetMetadata` | `true` |
| `executionContext.sourceAuthorityContext` | `proposed-candidate` |
| `executionContext.derivedFromAmbientGitState` | `false` |
| `sourceRevisionCrossCheck.match` | `true` (source is authoritative over the CLI argument) |
| Cases | `32` total, `32` expected-match |
| Failures / Blocked / Execution errors | `0` / `0` / `0` |
| Review-required coverage | **6 / 6** (RR-1 … RR-6) |
| Fail-closed coverage | **8 / 8** (FC-1 … FC-8) |
| Per-value requirement coverage | **25 / 25** |
| Source `$description` coverage | **25 / 25** |
| DE / EN structural coverage | **25 / 25** each |
| Evidence class | **AE-1 Evidence Candidate** |
| Independent review | **not performed by this run** |
| Admission | **not admitted by this run** |
| All seven authority effects | **`false`** — maturity, approval, Candidate, evidence admission, claim, conformance, human approval |
| Claims / Conformance | `none` / `none` |
| `scoreProduced` | `false` |

## Semantic immutability of the evidenced source

The Proposed Candidate differs from `semantic-status-rev-0001` **only** in
governance and target metadata. Independently audited after mutation:

**5** axes · **25** values · **25** technical identifiers · **25/25** `$value`
unchanged · **25/25** `$type` unchanged · **25/25** semantic `$description`
unchanged · **5/5** axis group descriptions unchanged · root group description
unchanged · DE **25** and EN **25** labels unchanged · **RR-1 … RR-6** unchanged ·
**FC-1 … FC-8** unchanged · dependencies, dependency graph, and Product-Profile
boundary unchanged · no visual value · no aggregate health · no consumer or
Product-Profile semantics.

Exactly **12** logical JSON paths changed in total (4 in the token document, 7 in
the source-set manifest, 1 in the resolver), with **zero** added and **zero**
removed leaves.

> **MATURITY METADATA CHANGE IS NOT A SEMANTIC CONTRACT CHANGE.**

## Result status

> ### **`Pass with limitations`**

`Pass with limitations` is the honest status because three of the 25 per-value
requirements are `COVERED_WITH_LIMITATION` rather than `COVERED`
([matrix](SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md) rows 12, 13,
22 — `confidence.supported`, `confidence.uncertain`, `evidence.partial`), and
because the whole package carries the sixteen limitations below.

**What this result is bound to:** this artifact family, **these exact uncommitted
Proposed Candidate bytes**, this declared source-level scope, this baseline
revision, these two languages, and this test date. Nothing else.

**What this result is not:**

| It is **not** | Because |
| --- | --- |
| Accessibility | Nothing was tested with a user, an assistive technology, a browser, or a keyboard. |
| A WCAG statement | 50 of 55 applicable criteria were not assessable at this scope; the other 5 have only a source-level component. |
| Admitted AE-1 | The fresh independent evidence review of **this** run has not happened. |
| A Candidate award | Candidate remains **No**. A validator pass on `Candidate`+`Approved` proves **metadata coherence only** (DEC-S-122). |
| Human approval | An automated result is input to a review, never the review (DEC-S-053). |
| Inherited from `AE1-CDS-WP016-SEMSTATUS-002` | Evidence never transfers across a source revision (DEC-S-126). |
| A statement about the committed repository | The evidenced bytes are uncommitted and non-authoritative. |

## Validator disposition of the Proposed Candidate source

The three Proposed Candidate documents were validated directly through the
documented CLI command
`python -B -m tools.cds_validator validate-file <tokens> --manifest <source-set> --resolver <resolver>`:

**V1 `Pass` · V2 `Pass` · V3 `Pass` · V4 `Not assessed`**, blocking layer `none`,
diagnostics `CDS-V4-NOT-ASSESSED` (severity `info`) only — **no Fail, no Blocked,
no error diagnostic**, exit code `0`. The diagnostic profile is identical to the
`semantic-status-rev-0001` baseline.

> **Validator PASS means metadata coherence only. It grants no Candidate
> authority.** Real Candidate authority arises solely from the Candidate Approval
> Record, the Nova finalization review, the Human-Maintainer Candidate approval,
> and the Human-Maintainer exact-byte Promotion Commit (DEC-S-126).

## Evidence level and boundaries

| Field | Value |
| --- | --- |
| **Evidence level represented** | **AE-1** |
| **Evidence class** | **Structural and Automated Evidence** |
| **Evidence admission** | **NOT ADMITTED** |
| **Independent Evidence Review** | **PENDING** |
| **Nova evidence review / adjudication** | **PENDING** |
| **Human-Maintainer Evidence Admission** | **NOT GRANTED** |
| **Candidate Approval** | **NOT GRANTED** |
| **Candidate Promotion** | **NOT PERFORMED** |
| **Stable** | **NO** |
| **Claims** | **NONE** |
| **Conformance** | **NONE** |
| **WCAG claim** | **NONE** |
| **AE-2 / AE-3 / AE-4** | **NONE / NONE / NONE** |
| **Consumer evidence** | **NONE** |
| **Channel evidence** | **NONE** |

**No numeric or percentage accessibility score exists. No certification exists.**

## Known limitations

All sixteen are recorded in full, with the normative 15 fields each, in the
[Semantic Status Candidate Accessibility Limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md):

**0 Critical · 11 Significant · 5 Minor.** Zero Critical is a statement about the
artifact's scope, not about its quality.

**No limitation was closed, downgraded, averaged, or converted by this run.** The
three `COVERED_WITH_LIMITATION` rows remain exactly `confidence.supported`,
`confidence.uncertain`, and `evidence.partial`.

The limitation bearing most directly on **this** record is **SSC-LIM-015 —
executor self-confirmation partially mitigated, not erased**. This run's artifacts
are executor-produced and unreviewed. That is precisely why this record is
provisional.

## Defects

**None known and open** against the contract family or the source set at record
time. Any Blocking or High defect found in the fresh independent evidence review
re-opens this record and invalidates its result for the affected scope.

## Deviations

**None.** No normative source was deviated from, no gate was bypassed, the
immutable WP-013/WP-015 24-case matrix was not modified (DEC-S-120), no tooling,
test, fixture, validator, or schema was modified, and the two historical evidence
packages and the rev-0001 admission record were not modified.

## Required remaining order

These steps must not be skipped, reordered, or combined.

| # | Step | State |
| --- | --- | --- |
| 1 | **Fresh Independent Evidence Review of `AE1-CDS-WP016-SEMSTATUS-003`** (reviewer ≠ executor) | **PENDING** |
| 2 | **Nova evidence / admission adjudication** | **PENDING** |
| 3 | **Human-Maintainer AE-1 Admission for `semantic-status-rev-0002-candidate`** | **NOT GRANTED** |
| 4 | **Nova Candidate Finalization Review** | **NOT YET READY** |
| 5 | **Human-Maintainer Candidate Approval** (Candidate Approval Record instance) | **NOT GRANTED** |
| 6 | **Human-Maintainer exact-byte Promotion Commit** — the actual repository maturity transition point | **NOT PERFORMED** |
| 7 | **Post-commit exact-byte and regression verification** | **NOT PERFORMED** |

> **AE-1 admission precedes Candidate approval. Candidate approval precedes the
> Promotion Commit. The Promotion Commit — not this record, not the source bytes,
> not the validator — is where repository maturity actually changes (DEC-S-126).**

## Invalidation

**ANY byte change to the evidenced Proposed Candidate Source scope after this
evidence execution INVALIDATES `AE1-CDS-WP016-SEMSTATUS-003`** and requires:

1. **fresh Evidence**,
2. **a fresh Independent Review**, and
3. **a fresh Admission**.

**There is no small-fix exemption.** A one-character correction to any of the three
source files invalidates this evidence exactly as completely as a rewrite would.
The exact-byte identities recorded above are the test: if a reviewer recomputes
them and any value differs, this evidence does not describe the bytes in front of
them.

Changes to evidence-relevant fixtures, tooling, or contract documents likewise
trigger re-evidence under the
[regression plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md);
trigger **T-12 is not waived**.

## Source references

### This run (current, Proposed-Candidate-revision-bound)

| Kind | Path |
| --- | --- |
| Results artifact | [`artifacts/validation/wp016-candidate-finalization-proposed-candidate-results.json`](../../artifacts/validation/wp016-candidate-finalization-proposed-candidate-results.json) |
| Digest artifact | [`artifacts/validation/wp016-candidate-finalization-proposed-candidate-digests.json`](../../artifacts/validation/wp016-candidate-finalization-proposed-candidate-digests.json) |
| Preparation notes | [`project-brain/CDS_WP_016_CANDIDATE_FINALIZATION_PREPARATION_NOTES.md`](../../project-brain/CDS_WP_016_CANDIDATE_FINALIZATION_PREPARATION_NOTES.md) |

### Prior evidence (rev-0001 — **not** this revision's result, and not transferable)

| Kind | Path |
| --- | --- |
| Evidence record `…-001` (historical, pre-commit) | [`SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md`](SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md) |
| Evidence record `…-002` (admitted, rev-0001) | [`SEMANTIC_STATUS_CANDIDATE_AE1_CLEAN_REEXECUTION_EVIDENCE_RECORD.md`](SEMANTIC_STATUS_CANDIDATE_AE1_CLEAN_REEXECUTION_EVIDENCE_RECORD.md) |
| AE-1 Admission Record (rev-0001) | [`SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md`](../governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md) |

These are bound to `semantic-status-rev-0001`. They are referenced for
traceability only and **must never be presented as the Proposed Candidate
revision's result**.

### Unchanged inputs and governing documents

| Kind | Path |
| --- | --- |
| Evidence runner (unmodified) | [`tests/validator/semantic_status_candidate_evidence_runner.py`](../../tests/validator/semantic_status_candidate_evidence_runner.py) |
| Evidence suite (unmodified) | [`tests/validator/test_semantic_status_candidate_evidence.py`](../../tests/validator/test_semantic_status_candidate_evidence.py) |
| Semantic status suite (unmodified) | [`tests/validator/test_semantic_status.py`](../../tests/validator/test_semantic_status.py) |
| Statement fixture (test-only, unmodified) | [`tests/fixtures/semantic-status-statements/CANDIDATE_EVIDENCE_CASES.json`](../../tests/fixtures/semantic-status-statements/CANDIDATE_EVIDENCE_CASES.json) |
| Requirements matrix | [Evidence Requirements Matrix](SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md) |
| Candidate Approval Record template (**no instance exists**) | [Candidate Approval Record Template](CANDIDATE_APPROVAL_RECORD_TEMPLATE.md) |
| WCAG mapping | [WCAG Applicability Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md) |
| Responsibility mapping | [Accessibility Responsibility Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_RESPONSIBILITY_MAPPING.md) |
| Baseline plan | [Support Baseline Plan](../governance/SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md) |
| AE-2 plan | [AE-2 Evidence Plan](../governance/SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md) |
| Regression plan | [Accessibility Regression Plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md) |
| Limitations | [Accessibility Limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md) |
| Baseline freshness | [WP-016 A11Y Baseline Freshness Review](../reviews/WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md) |

## Next review trigger

| # | Trigger |
| --- | --- |
| 1 | **Immediately — the fresh independent evidence review of this run**, which is the reason this record is provisional. Until it completes, nothing here is admitted. |
| 2 | Any **byte change to the three evidenced Proposed Candidate source files** — see [Invalidation](#invalidation). No small-fix exemption. |
| 3 | Any of the **15 accessibility regression triggers** (T-01 … T-15) in the [regression plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md); **T-12 is not waived**. |
| 4 | **A11Y-BL-001 revision or freshness change** — including the Windows 11 24H2 servicing end on **2026-10-14 (PT)**, and the six-month maximum review gap on **2027-02-19**. |
| 5 | Any further **Semantic Status source or contract revision change** — including any move away from `semantic-status-rev-0002-candidate`. |
| 6 | Any **validator-contract change** affecting the diagnostics, categories, or check semantics used here. |
| 7 | Any **terminology or DE/EN change** affecting the 25 authorized identifiers or their labels. |
| 8 | The **Human-Maintainer Promotion Commit**, after which post-commit exact-byte and regression verification is mandatory (DEC-S-126). |
| 9 | The **first rendered or channel representation**, at which point AE-2 and AE-3 become required and this record's scope explicitly does not extend. |

**No evidence transfers across any of these.** A new trigger means a new run and a
new record, not an amendment of this one.

## Closing boundary

**Authoritative source revision = `semantic-status-rev-0001`. Candidate = No.
Maturity = Experimental. Approval = Unapproved. Admitted accessibility evidence =
`AE1-CDS-WP016-SEMSTATUS-002` at AE-1, bound to `semantic-status-rev-0001` only;
every other CDS artifact = AE-0. Claims = none. Conformance = none. Pilot =
inactive. CDS-WP-017 = not activated. Publication = Private Development.**

**None of these changes because this record exists, because the Proposed Candidate
bytes exist, or because the validator passed.**
