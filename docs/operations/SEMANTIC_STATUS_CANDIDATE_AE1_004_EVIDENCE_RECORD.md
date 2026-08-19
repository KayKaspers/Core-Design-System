# Semantic Status Candidate — AE1-004 Revision-Bound AE-1 Evidence Record

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Test-Lifecycle Rework and AE1-004
  Preparation (Human-Maintainer authorized 2026-08-19; internal rework of
  CDS-WP-016, **not** a new work package)
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

The fresh independent review of `AE1-CDS-WP016-SEMSTATUS-003` returned **PASS
WITH NOTES** and raised finding **NF-PREP-001 / F-R1**: seven test premises in
the Candidate-evidence suite still encoded the **pre-preparation** lifecycle
state (`semantic-status-rev-0001`, `Experimental`, `Unapproved`) as a fixed
assumption, and therefore no longer held against the bytes actually under
evidence.

On **2026-08-19** the Human Maintainer authorized closing that finding by making
those seven premises **lifecycle-safe**, and then generating **fresh
revision-bound evidence** against the **unchanged** Proposed Candidate source
bytes.

`tests/validator/test_semantic_status_candidate_evidence.py` is a **bound
evidence input**. Changing it after evidence generation invalidates that evidence
for admission purposes — even though the evidenced **source** bytes did not
change. This record is the fresh evidence that follows from that change, and only
the evidence.

The two historical evidence packages, the rev-0001 admission record, and the
whole `AE1-CDS-WP016-SEMSTATUS-003` package are **unmodified**. This record does
not replace, correct, or absorb them.

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

## Relation to `AE1-CDS-WP016-SEMSTATUS-003`

| Field | Value |
| --- | --- |
| **Previous evidence ID** | `AE1-CDS-WP016-SEMSTATUS-003` |
| **Its fresh independent review** | **Completed — PASS WITH NOTES** |
| **Its evidence admission** | **NOT ADMITTED** |
| **Its admission disposition** | **`SUPERSEDED_FOR_ADMISSION_BY_EVIDENCE_INPUT_CHANGE`** |
| **Changed bound input** | [`tests/validator/test_semantic_status_candidate_evidence.py`](../../tests/validator/test_semantic_status_candidate_evidence.py) |
| **Reason** | Transition-safe correction of the seven confirmed superseded lifecycle premises (NF-PREP-001 / F-R1) |
| **Evidenced source bytes** | **Identical** in both packages — same revision, same bytes, same Source Manifest |
| **Its four files** | **Byte-identical and unmodified** by this rework |

The precise distinction, which must not be blurred:

| Statement | Correct? |
| --- | --- |
| The evidenced **source bytes changed** | **No.** The three Proposed Candidate source files are byte-identical; the Source Manifest SHA-256 is unchanged. |
| The **source revision changed** | **No.** It remains `semantic-status-rev-0002-candidate`. |
| An **evidence-relevant bound test input changed** | **Yes.** That is the sole reason fresh evidence was required. |
| `AE1-CDS-WP016-SEMSTATUS-003` was **invalidated by source drift** | **No.** Stating that would be false. |
| `AE1-CDS-WP016-SEMSTATUS-003` is **superseded for admission** | **Yes** — for admission purposes only, by the bound-input change. |

**This record is not an evidence transfer.** It is fresh evidence generated after
a bound evidence input changed. It inherits **no** independent review and **no**
admission from `AE1-CDS-WP016-SEMSTATUS-003`, and nothing from
`AE1-CDS-WP016-SEMSTATUS-002` (evidence never transfers across a source
revision — DEC-S-126).

## Mandatory fields

### Identity and scope

| Field | Value |
| --- | --- |
| **Evidence ID** | `AE1-CDS-WP016-SEMSTATUS-004` |
| **Evidence level represented** | **AE-1 (provisional candidate)** — structural and automated evidence only |
| **Evidence class** | **Structural and Automated Evidence** — an **AE-1 Evidence Candidate**, not admitted evidence |
| **Artifact or consumer** | The **Semantic Status Candidate source and contract family**: [Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) · [Status Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) · [Composition and Conflict Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) · [Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md) · [Terminology DE/EN](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md) · the `semantic/status` source set with manifest and resolver, **at the Proposed Candidate bytes**. **No consumer** — none exists and none is authorized. |
| **Declared scope** | **Channel-independent Layer-3 semantic source and contract family; source-level structural and rule-level checks only.** Explicitly outside scope: rendering, interaction, presentation, composition, product content, complete processes, and every consumer surface. |
| **CDS baseline revision** | **`8d1374fa4c61cc1eed214823681ee1209a2d91f7`** — the committed authoritative baseline **from which** the Proposed Candidate was prepared. **This does not claim that the Proposed Candidate bytes, or the reworked test file, are contained in that commit. They are not.** |
| **Artifact revision (the evidenced bytes)** | **`semantic-status-rev-0002-candidate`** — uncommitted Proposed Candidate source bytes, frozen before and re-verified after the test rework |
| **Worktree state at execution** | **`modified worktree`** |
| **Baseline version** | **A11Y-BL-001**, revision declared 2026-07-16, committed with CDS-WP-010 |
| **Freshness state (baseline)** | **`Current`** — determined 2026-08-17 by the [WP-016 Baseline Freshness Review](../reviews/WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md) |
| **Freshness state (this record)** | **`Current`** as of the test date and bound to it. It decays with the artifact, the baseline, the test suite, and the validator contract. |
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
| Determinism | The evidence runner was executed **twice** to two separate outputs **outside** the repository; the results were **byte-identical** (SHA-256 `cc918d562a8d7da17f462ce8a3040933d6c5fb850dbb8f85bd07464a2bbae1d0`, 30 432 bytes each). The digest package was likewise generated **twice** externally and was **byte-identical** (SHA-256 `d8e7732add7be12cea9168483501389f354e0bce36cd6f6309c48f2e6dd1d27a`, 19 631 bytes each). |

### People

| Field | Value |
| --- | --- |
| **Executor** | Claude Opus 5 (`claude-opus-5`), acting as the scoped CDS-WP-016 **Candidate Test-Lifecycle Rework and AE1-004 Preparation Executor** in a single authorized session. This executor authored **no** rule, fixture, expectation, runner, or validator in this run — all were read unmodified. This executor **did** author the transition-safe test rework, this record, the digest artifact, and the rework notes. |
| **Reviewer** | **PENDING — a fresh independent evidence reviewer is required.** Must be neither this executor nor the artifact itself (DEC-S-045). **Evidence reviewed only by its own executor has not been reviewed** (Evidence Strategy, *Review independence*). The executor has **not** self-reviewed this run, and no reviewer identity is invented here. |
| **Nova evidence review / adjudication** | **PENDING.** |
| **Human-Maintainer evidence admission** | **NOT GRANTED.** |
| **Human-Maintainer Candidate approval** | **NOT GRANTED.** Final maturity authority is not delegable (DEC-S-036). |
| **Approval state** | **Unapproved / pending fresh independent evidence review.** |

## The complete machine Evidence Package — NF-R11-001

**NF-R11-001 is binding for this evidence: the Runner Result alone is NOT a
complete Evidence Package.**

The complete machine Evidence Package for `AE1-CDS-WP016-SEMSTATUS-004` is the
**pair**:

| # | Member | Path |
| --- | --- | --- |
| 1 | **Runner Result** | [`artifacts/validation/wp016-candidate-finalization-ae1-004-results.json`](../../artifacts/validation/wp016-candidate-finalization-ae1-004-results.json) |
| 2 | **Digest Package** | [`artifacts/validation/wp016-candidate-finalization-ae1-004-digests.json`](../../artifacts/validation/wp016-candidate-finalization-ae1-004-digests.json) |

**Neither artifact alone is sufficient for review.** The result states what was
checked; the digest package states *which exact bytes* were checked.

### Exact-byte identities

| Item | Value |
| --- | --- |
| Result — raw SHA-256 | `cc918d562a8d7da17f462ce8a3040933d6c5fb850dbb8f85bd07464a2bbae1d0` |
| Result — byte length | `30432` |
| Result — RFC 8785 content digest | `sha256:0b299fc99fe96f86075c94a01eb517efbfa37a876386e6d8f7a6acd7c924f96b` |
| Digest Package — raw SHA-256 | `d8e7732add7be12cea9168483501389f354e0bce36cd6f6309c48f2e6dd1d27a` |
| Digest Package — byte length | `19631` |
| Source Manifest — SHA-256 | `3b80d1483ceba4de61c5f9b1f99e10ff00f6da17ac935a1ddfa643a413204ebf` |
| Source Manifest — entries / bytes | `3` / `497` |
| Bound test file — raw SHA-256 | `93091d4b6f353b19977af0d7aa1b93b9281972152716c8897eca1c2f9e460b70` |
| Bound test file — byte length / Git raw object | `43960` / `f275d73a3e9bfafc937dd6dfc967850f9cd11a9c` |
| Bound test file — SHA-256 bound by AE1-003 | `4b636faacb9e16cdb082022b4aa90ae153b7f7111909a2346b9aec0bc6e187d3` |

> ### The Runner Result is byte-identical to the AE1-003 result — and that is correct
>
> The runner bytes, the runner inputs, the caller-declared context, and the three
> evidenced source files are all unchanged, so the runner legitimately produced
> the same result bytes. **Identical result bytes are not the same Evidence
> Package identity once another bound input has changed.** The difference between
> the two evidence packages lives in the **digest package**, which binds the new
> transition-safe test file and records the supersession. This identity was
> derived, not forced in either direction.

### The three evidenced Proposed Candidate source files

| Path | Raw SHA-256 | Bytes | RFC 8785 content digest |
| --- | --- | --- | --- |
| `tokens/semantic/status/semantic-status.tokens.json` | `53312e93810a6296c2b82b9365d17d14e7e74485cdeb5e13bba149634d4cb55e` | `6358` | `sha256:317c464807c04b9b0f6cc05f46cab955f58f5739d7c39fe61d55702a20412c34` |
| `tokens/semantic/status/semantic-status.source-set.json` | `8dda44d28ac654c33892e4c362c83260ba2bd1ab97526ef90dbddb6f72d52ef6` | `1041` | `sha256:db5626e648d1076200ca16ece8adf5ba4dcd6077210cff76092707de9d6fb12d` |
| `tokens/semantic/status/semantic-status.resolver.json` | `0d9ff65fb65c9eca3abe5f3bd6bf37492b043c8308191feda9c8319a43c45004` | `572` | `sha256:c73a6fa34c40de3cc1ace2a69e9e3f7f82b07d6cb5927e673c96f1c0e242a8be` |

**Identical to the source identities bound by `AE1-CDS-WP016-SEMSTATUS-003`.**

## The transition-safe test lifecycle rework

### The seven confirmed superseded premises

Finding **NF-PREP-001 / F-R1**. Confirmed superseded premise count: **7** — not
three. Each old premise was replaced by an invariant derived from the **evidenced
bytes**, never by a literal for either lifecycle state.

| # | Old test | Superseded premise | Lifecycle-safe invariant | New test | Strength |
| --- | --- | --- | --- | --- | --- |
| 1 | `ResultFormatV2Tests.test_source_declared_metadata_is_read_from_the_evidenced_bytes` | Asserted the evidenced source declares `semantic-status-rev-0001`, `Experimental`, `Unapproved`, and `declaresCandidateTargetMetadata` false | The result restates exactly what the evidenced bytes declare; the Candidate-target flag is derived from the declared maturity state; the declared triple must be coherent for its own revision identity | *(name unchanged)* | **STRENGTHENED** |
| 2 | `ProposedCandidateContextTests.test_the_real_source_still_declares_the_experimental_revision` | Asserted the real source declares the Experimental baseline revision, using revision equality as the non-mutation proxy | Non-mutation of the real source is proven on captured **bytes**; the declared lifecycle state must be one of the two authorized revision identities and coherent for it | `test_the_real_source_declares_a_coherent_lifecycle_state` | **STRENGTHENED** |
| 3 | `ProposedCandidateContextTests.test_no_candidate_revision_artifact_exists_in_the_repository` | Asserted the universal absence of any Candidate revision declaration under `tokens/` | A Candidate revision identity may appear **only** where the authorized Semantic Status Layer-3 source family declares the one revision under evaluation; absence is still required while no Candidate revision is current; a partial, premature, foreign, or second Candidate revision identity still fails closed | `test_candidate_revision_declarations_stay_in_the_authorized_family` | **STRENGTHENED** |
| 4 | `ResultBoundaryTests.test_current_run_passes_with_declared_limitations` | The shared helper supplied the baseline revision as a fixed default, so a valid run against the evidenced bytes blocked on the cross-check | A run against the revision the evidenced bytes actually declare matches the cross-check, raises no execution error, and passes with the declared limitations | *(name unchanged)* | **STRENGTHENED** |
| 5 | `ResultFormatV2Tests.test_source_revision_mismatch_fails_closed` | Asserted `declaredBySource` equals the baseline revision literal, using a fixed mismatch value | The mismatch input is **derived** so it can never equal the evidenced revision in any lifecycle state; the cross-check still reports no match, the declared source revision, the argument, a `Blocked` result, and execution errors | *(name unchanged)* | **STRENGTHENED** |
| 6 | `ResultFormatV2Tests.test_the_source_wins_over_the_cli_argument` | Asserted the surviving source revision equals the baseline revision literal | The surviving source revision equals the revision the evidenced bytes declare and never the argument; the boundary text and the controlled failure still state that the CLI never overrides the source | *(name unchanged)* | **STRENGTHENED** |
| 7 | `RuleCoverageTests.test_expected_and_actual_classifications_agree` | Inherited the fixed baseline revision default, so the run blocked before the classifications could be compared | Unchanged rule expectations, now evaluated against a valid run of the evidenced bytes | *(name unchanged)* | **PRESERVED** |

**Assertions weakened: 0. Tests deleted: 0. Tests skipped: 0. Expected failures:
0.** No rule expectation, authority-effect check, fail-closed check, determinism
check, or historical-evidence immutability check was removed or relaxed.

### One additional coherence adjustment — not an eighth superseded premise

`ResultFormatV2Tests.test_execution_context_is_caller_declared_and_bounded`
round-tripped whatever authority context the suite declared, and therefore never
became false. It was adjusted only because the shared helper now **derives** that
declaration from the evidenced bytes instead of stating a frozen
`authoritative-current` literal — which would otherwise have declared the
Proposed Candidate bytes to be the integrated current source. The test now
expects the derived context and additionally requires it to be one of the two
bounded values. **STRENGTHENED.** The runner still never infers the context.

After the final static audit, **no eighth superseded lifecycle premise remains**
and **zero stale preparation assumptions** are left in the file.

### Dual-state proof — the same test bytes hold in both lifecycle states

The **identical** final test bytes
(SHA-256 `93091d4b6f353b19977af0d7aa1b93b9281972152716c8897eca1c2f9e460b70`)
were executed against both lifecycle states.

| State | Source revision | Maturity / Approval | Candidate-evidence | Full validator |
| --- | --- | --- | --- | --- |
| **Committed baseline** (external read-only sandbox of `8d1374fa…`) | `semantic-status-rev-0001` | `Experimental` / `Unapproved` | **64 / 64** | **184 / 184** |
| **Real Proposed Candidate** (working tree) | `semantic-status-rev-0002-candidate` | `Candidate` / `Approved` | **64 / 64** | **184 / 184** |

Additional gates on the real Proposed Candidate working tree:
**`tests.validator.test_semantic_status` 47 / 47**, and the validator harness
**24 total, 24 expected matches, 0 mismatches, 0 execution errors**, exit `0`.

**Classification: `TRANSITION_SAFE_DUAL_STATE_TEST_GATE_PASS`.**

The sandbox was created **read-only** by `git archive` of the committed baseline
revision, extracted **outside** the repository, with only the reworked test file
overlaid. No checkout, worktree, branch, reset, or stash was used, and the
repository was not mutated by the sandbox.

> A passing dual-state test gate is **structural and automated test evidence
> only**. It is not accessibility, not assistive-technology behaviour, not
> comprehension, not an independent review, not an Evidence Admission, and not a
> Candidate Approval.

## What the run reported

| Check | Result |
| --- | --- |
| Result format | `cds-wp016-candidate-accessibility-evidence-result/2` |
| Source revision cross-check | **match `true`** — `semantic-status-rev-0002-candidate` declared by both source and argument |
| Source-declared metadata | `sourceRevision` `semantic-status-rev-0002-candidate`, `maturityState` `Candidate`, `approvalState` `Approved`, `declaresCandidateTargetMetadata` `true` — **read from the evidenced bytes, granting nothing** |
| Source authority context | `proposed-candidate` — caller-declared |
| Per-value evidence requirements | **25 / 25** mapped, 0 unmapped, 0 duplicate, 0 unauthorized |
| Source `$description` coverage | **25 / 25**, 0 missing — existence only, **never comprehension** |
| DE/EN structural coverage | **25 / 25** rows, 25 English labels, 25 German labels — **structure, not semantic equivalence** |
| Review-required coverage | **6 / 6** (RR-1 … RR-6) |
| Fail-closed coverage | **8 / 8** (FC-1 … FC-8) |
| Failures / blocked / execution errors | **0 / 0 / 0** |
| Numeric accessibility score | **None produced** |
| Authority effects | **All seven permanently `false`** |
| Claims / conformance / human approval | **`none` / `none` / `none`** |

## Result status

> ### **`Pass with limitations`**

`Pass with limitations` is the honest status because three of the 25 per-value
requirements are `COVERED_WITH_LIMITATION` rather than `COVERED`
([matrix](SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md) rows 12, 13,
22 — `confidence.supported`, `confidence.uncertain`, `evidence.partial`), and
because the whole package carries the sixteen recorded
[limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md)
(0 Critical).

**What this result is bound to:** this artifact family, **these exact uncommitted
Proposed Candidate bytes**, **these exact transition-safe test bytes**, this
declared source-level scope, this baseline revision, these two languages, and
this test date. Nothing else.

**What this result is not:**

| It is **not** | Because |
| --- | --- |
| Accessibility | Nothing was tested with a user, an assistive technology, a browser, or a keyboard. |
| A WCAG statement | 50 of 55 applicable criteria were not assessable at this scope; the other 5 have only a source-level component. |
| Admitted AE-1 | The fresh independent evidence review of **this** run has not happened. |
| A Candidate award | Candidate remains **No**. A validator pass on `Candidate`+`Approved` proves **metadata coherence only** (DEC-S-122). |
| Human approval | An automated result is input to a review, never the review (DEC-S-053). |
| Inherited from `AE1-CDS-WP016-SEMSTATUS-002` | Evidence never transfers across a source revision (DEC-S-126). |
| Inherited from `AE1-CDS-WP016-SEMSTATUS-003` | That package was reviewed but **never admitted**, and is superseded for admission by the bound-input change. |
| A statement about the committed repository | The evidenced bytes and the reworked test bytes are uncommitted and non-authoritative. |

## Evidence level and boundaries

| Field | Value |
| --- | --- |
| **Evidence level represented** | **AE-1** |
| **Evidence class** | **Structural and Automated Evidence — AE-1 Evidence Candidate** |
| **Independent review** | **PENDING** |
| **Evidence admission** | **NOT ADMITTED** |
| **Candidate approval** | **NOT GRANTED** |
| **Candidate promotion** | **NOT PERFORMED** |
| **Stable** | **NO** |
| **Claims** | **NONE** |
| **Conformance** | **NONE** |
| **WCAG claim** | **NONE** |
| **AE-2** | **NONE** |
| **AE-3** | **NONE** |
| **AE-4** | **NONE** |
| **Channel evidence** | **NONE** |
| **Consumer evidence** | **NONE** |
| **Numeric score** | **NONE** |

## Known limitations

The sixteen recorded
[Candidate accessibility limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md)
(0 Critical) apply unchanged. This rework added no limitation, removed none, and
downgraded none. In addition, for this record specifically:

1. The evidenced bytes are **uncommitted**. Every statement here is bound to
   working-tree content that no commit contains.
2. The bound test suite is likewise **uncommitted**.
3. Structural DE/EN coverage is **not** a translation-quality or comprehension
   statement.
4. `$description` existence is **not** a readability, plain-language, or
   comprehension statement.
5. The dual-state proof establishes **test-suite lifecycle safety**, not artifact
   accessibility.

## Defects

**None recorded by this run.** 0 failures, 0 blocked cases, 0 execution errors.
The absence of a defect in a source-level structural run is **not** evidence of
accessibility.

## Deviations

1. The digest package binds **two additional actual runtime inputs**
   (`tools/cds_validator/__init__.py`, `tools/cds_validator/version.py`) that
   `AE1-CDS-WP016-SEMSTATUS-003` did not bind. Both are executed at import time
   of the runner. This is an **additive integrity binding** and changes no
   existing bound value.
2. The source manifest entries additionally carry an `rfc8785ContentDigest` per
   source file. Additive; the manifest identity itself is unchanged.

No other deviation from the authorized scope.

## Invalidation

**This evidence is invalidated, in full, by any of the following:**

| Trigger | Effect |
| --- | --- |
| Any change to the **three evidenced Proposed Candidate source bytes** | **AE1-004 is invalid.** Fresh evidence, fresh independent review, and fresh admission are required. |
| Any change to the **bound transition-safe test file** | Re-evidence required — the same rule that produced this record from `AE1-CDS-WP016-SEMSTATUS-003`. |
| Any change to the **evidence runner** | Re-evidence required. |
| Any change to the **evidence fixtures** (`CANDIDATE_EVIDENCE_CASES.json`) | Re-evidence required. |
| Any change to the **validator modules** bound in the digest package | Re-evidence required. |
| Any change to the **Foundation contract, vocabulary, composition rules, communication contract, or DE/EN terminology** | Re-evidence required. |
| Any change to `requirements-validator.lock` | Re-evidence required. |
| A **source revision change** | Evidence never transfers; a new revision needs its own evidence (DEC-S-126). |

**There is no small-fix exemption.** A change that "obviously cannot matter" still
invalidates the exact-byte binding, because the binding is the whole mechanism.

## Required remaining order

No gate may be skipped, reordered, or merged.

| # | Step | Authority | State |
| --- | --- | --- | --- |
| 1 | **Fresh independent AE1-004 evidence review** | Reviewer ≠ executor | **PENDING** |
| 2 | **Nova evidence / admission adjudication** | Nova | **PENDING** |
| 3 | **Human-Maintainer AE1-004 evidence admission** | Human Maintainer | **NOT GRANTED** |
| 4 | **Nova Candidate Finalization Review** | Nova | **NOT REACHED** |
| 5 | **Human-Maintainer Candidate approval** | Human Maintainer | **NOT GRANTED** |
| 6 | **Human-Maintainer exact-byte Promotion Commit** | Human Maintainer | **NOT PERFORMED** |
| 7 | **Post-commit full regression and exact-byte verification** | Human Maintainer | **NOT REACHED** |

**The Promotion Commit is the actual repository maturity transition point**
(DEC-S-126). Until it happens, the repository is `semantic-status-rev-0001`,
`Experimental`, `Unapproved`, Candidate `No`.

## Source references

### This run (current, Proposed-Candidate-revision-bound)

- [`artifacts/validation/wp016-candidate-finalization-ae1-004-results.json`](../../artifacts/validation/wp016-candidate-finalization-ae1-004-results.json)
- [`artifacts/validation/wp016-candidate-finalization-ae1-004-digests.json`](../../artifacts/validation/wp016-candidate-finalization-ae1-004-digests.json)
- [`tests/validator/test_semantic_status_candidate_evidence.py`](../../tests/validator/test_semantic_status_candidate_evidence.py) — the reworked bound test input
- [CDS-WP-016 Candidate Test-Lifecycle Rework notes](../../project-brain/CDS_WP_016_CANDIDATE_TEST_LIFECYCLE_REWORK_AE1_004_NOTES.md)

### Prior evidence — reviewed but **not admitted**, and **not** transferable

- [`AE1-CDS-WP016-SEMSTATUS-003` record](SEMANTIC_STATUS_CANDIDATE_AE1_PROPOSED_CANDIDATE_EVIDENCE_RECORD.md)
  — PASS WITH NOTES, **not admitted**, superseded for admission by the
  bound-input change. **Unmodified by this rework.**
- [`AE1-CDS-WP016-SEMSTATUS-001` record](SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md)
  — rev-0001. **Unmodified.**
- [Clean re-execution record](SEMANTIC_STATUS_CANDIDATE_AE1_CLEAN_REEXECUTION_EVIDENCE_RECORD.md)
  — rev-0001. **Unmodified.**
- [AE-1 Admission Record](../governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md)
  — `AE1-CDS-WP016-SEMSTATUS-002`, bound to `semantic-status-rev-0001` **only**.
  **Unmodified.**

### Unchanged inputs and governing documents

- [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md) (A11Y-BL-001)
- [Accessibility Evidence Strategy](../governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md)
- [Candidate accessibility limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md)
- [Candidate evidence requirements matrix](SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md)
- [Candidate Approval Record Template](CANDIDATE_APPROVAL_RECORD_TEMPLATE.md) — **a template; no instance exists**
- DEC-S-125, DEC-S-126, RISK-098 — **unchanged by this rework**

## Next review trigger

Whichever comes first: the fresh independent AE1-004 evidence review; any change
to a bound input listed under [Invalidation](#invalidation); an A11Y-BL-001
freshness change; the six-month periodic review; or a regression trigger from the
[Candidate Accessibility Regression Plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md).
Regression trigger **T-12 is not waived**.

## Closing boundary

This record is **executor-produced, unreviewed, unadmitted** provisional
evidence about **uncommitted, non-authoritative bytes**. It grants nothing. It
awards nothing. It approves nothing. It promotes nothing.

Git authority, evidence-admission authority, and maturity authority remain
**exclusively** with the Human Maintainer.
