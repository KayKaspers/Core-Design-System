# Semantic Status — Candidate Approval Record

- **Project:** Core Design System (CDS)
- **Record ID:** `CAR-CDS-WP016-SEMSTATUS-001`
- **Instance of:** [Candidate Approval Record Template](CANDIDATE_APPROVAL_RECORD_TEMPLATE.md)
- **Status:** **Human-Maintainer Candidate decision recorded.**
- **Decision state:** **`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`**
- **Decision date:** 2026-08-19
- **Repository materialization:** 2026-08-19, during the CDS-WP-016 Candidate
  Authority Record Materialization (Human-Maintainer authorized 2026-08-19;
  internal rework of CDS-WP-016, **not** a new work package)

> **The repository is not Candidate while this state holds.**
>
> Current committed authoritative state, unchanged by this record: Candidate
> **No** · maturity **Experimental** · approval **Unapproved** · authoritative
> Semantic Status source revision **`semantic-status-rev-0001`** · claims
> **none** · publication **`Private Development`** · CDS-WP-017 **inactive**.

## Temporal truth — what happened when

This repository instance **materializes a Human-Maintainer Candidate decision
that was already made on 2026-08-19.** The sequence is stated here exactly as it
occurred, and must not be read in any other order:

| # | Event | When, relative to this file |
| --- | --- | --- |
| 1 | Proposed Candidate bytes prepared and enumerated | **Before** the decision |
| 2 | Fresh revision-bound AE-1 evidence produced (`AE1-CDS-WP016-SEMSTATUS-004`) | **Before** the decision |
| 3 | Fresh independent evidence review completed — **PASS WITH NOTES** | **Before** the decision |
| 4 | **Human-Maintainer evidence admission — APPROVED / ADMITTED** | **Before** the decision |
| 5 | Nova Candidate Finalization Review — **GO WITH NOTES** | **Before** the decision |
| 6 | **Human-Maintainer Candidate decision — `AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`** | The decision itself |
| 7 | This repository file created under a separate Human-Maintainer materialization authorization | **After** the decision |
| 8 | Human-Maintainer exact-byte Promotion Commit | **Has not happened** |

**The prerequisite facts represented in sections 1 to 6 were established before
the Human-Maintainer Candidate decision. The repository instance itself was
persisted afterwards.** This file did not exist at decision time, did not grant
the decision, and does not claim otherwise. Nothing here is backdated, and no
wall-clock time is reconstructed — only the calendar date 2026-08-19 is stated,
because only the calendar date is supportable from the recorded project workflow.

---

## 1. Identity

| Field | Value |
| --- | --- |
| Record ID | `CAR-CDS-WP016-SEMSTATUS-001` |
| Work package | CDS-WP-016 |
| Artifact | Semantic Status Foundation |
| Artifact class | Channel-independent Layer-3 Semantic Source / Contract family |
| Source set | `semantic/status` |
| Proposed Candidate source revision | `semantic-status-rev-0002-candidate` — reserved identity; **not current until integrated** |
| Authoritative pre-promotion baseline | `8d1374fa4c61cc1eed214823681ee1209a2d91f7` |
| Authoritative pre-promotion source revision | `semantic-status-rev-0001` — what the repository still asserts today |
| Record date | 2026-08-19 |

## 2. Candidate bytes identity

*(The exact bytes being approved.)*

| Field | Value |
| --- | --- |
| Exact Candidate file scope | Three files, enumerated below — no wildcards |
| Manifest entry count | `3` |
| Manifest byte length | `497` |
| Manifest SHA-256 | `3b80d1483ceba4de61c5f9b1f99e10ff00f6da17ac935a1ddfa643a413204ebf` |
| Canonical manifest line format | `<STATUS>\t<SHA256>\t<BYTES>\t<GIT_RAW_OBJECT_ID>\t<PATH>\n`, ordinal-sorted by path, UTF-8 without BOM, LF-only, final LF |
| Canonicalization method | RFC 8785 (JSON Canonicalization Scheme), per ADR-0002 |
| Digest algorithm | SHA-256 |
| Transformation / tooling revision | No transformation. The approved bytes are the source bytes themselves; the tooling that evidenced them is recorded in section 3. |
| Digest boundary | A digest is an integrity aid. It is **not** a signature and proves no authorship, approval, authenticity, or release (DEC-S-090, DEC-S-100, RISK-072). |

### Per-path identity

| Status | Path | Raw SHA-256 | Bytes | Git raw object |
| --- | --- | --- | --- | --- |
| `M` | [`tokens/semantic/status/semantic-status.resolver.json`](../../tokens/semantic/status/semantic-status.resolver.json) | `0d9ff65fb65c9eca3abe5f3bd6bf37492b043c8308191feda9c8319a43c45004` | `572` | `d6d75f981ff7d8ad556ce98387453402d458437e` |
| `M` | [`tokens/semantic/status/semantic-status.source-set.json`](../../tokens/semantic/status/semantic-status.source-set.json) | `8dda44d28ac654c33892e4c362c83260ba2bd1ab97526ef90dbddb6f72d52ef6` | `1041` | `fe7bbf1e7af49f753bd9cd75547ad69a5ae92ca9` |
| `M` | [`tokens/semantic/status/semantic-status.tokens.json`](../../tokens/semantic/status/semantic-status.tokens.json) | `53312e93810a6296c2b82b9365d17d14e7e74485cdeb5e13bba149634d4cb55e` | `6358` | `7d6b3499d1b291c04e1a3b6eca1b4ca54baf2df2` |

### RFC 8785 canonical content digests

Taken unchanged from the admitted `AE1-CDS-WP016-SEMSTATUS-004` digest package.
No different digest semantics are introduced here.

| Path | RFC 8785 content digest |
| --- | --- |
| `tokens/semantic/status/semantic-status.resolver.json` | `sha256:c73a6fa34c40de3cc1ace2a69e9e3f7f82b07d6cb5927e673c96f1c0e242a8be` |
| `tokens/semantic/status/semantic-status.source-set.json` | `sha256:db5626e648d1076200ca16ece8adf5ba4dcd6077210cff76092707de9d6fb12d` |
| `tokens/semantic/status/semantic-status.tokens.json` | `sha256:317c464807c04b9b0f6cc05f46cab955f58f5739d7c39fe61d55702a20412c34` |

### Additional bound identities

| Item | Path | Raw SHA-256 | Bytes | Git raw object |
| --- | --- | --- | --- | --- |
| Bound transition-safe test input | [`tests/validator/test_semantic_status_candidate_evidence.py`](../../tests/validator/test_semantic_status_candidate_evidence.py) | `93091d4b6f353b19977af0d7aa1b93b9281972152716c8897eca1c2f9e460b70` | `43960` | `f275d73a3e9bfafc937dd6dfc967850f9cd11a9c` |
| Review provenance | [`docs/reviews/WP016_CANDIDATE_FINALIZATION_EVIDENCE_REVIEW_PROVENANCE.md`](../reviews/WP016_CANDIDATE_FINALIZATION_EVIDENCE_REVIEW_PROVENANCE.md) | `0dcf6ff94a79f24c2ddd3834aec6a5b869cc7aef3585e0fa2977cb8b0bdf472a` | `13884` | `2be794d6534249dcabfbf9e40fd564de036d68d4` |

The three approved source files declare `sourceRevision`
`semantic-status-rev-0002-candidate`, `maturityState` `Candidate`, and
`approvalState` `Approved`. Those are **TARGET metadata inside uncommitted,
non-authoritative bytes** — the proposed future state, never the current
authoritative repository state, and never authority of any kind.

## 3. Evidence

| Field | Value |
| --- | --- |
| Evidence ID | `AE1-CDS-WP016-SEMSTATUS-004` |
| Evidence level | **AE-1** |
| Evidence type | Structural and Automated Evidence |
| Evidence source revision | `semantic-status-rev-0002-candidate` — equal to the Proposed Candidate source revision in section 1 |
| Evidence base repository revision | `8d1374fa4c61cc1eed214823681ee1209a2d91f7` |
| Evidence execution state | **proposed-candidate worktree** (`modified worktree`; caller-declared authority context `proposed-candidate`, never inferred from ambient Git state) |
| Evidence result | **Pass with limitations** |
| Runner / tooling revision | Runner [`tests/validator/semantic_status_candidate_evidence_runner.py`](../../tests/validator/semantic_status_candidate_evidence_runner.py) `sha256:946ccf484bf774424705b727e60a959ea62d06dd8ff604e8e05b30d50d9227e3`; result format `cds-wp016-candidate-accessibility-evidence-result/2`; bound validator modules `tools/cds_validator/semantic_status.py` `sha256:1ec690c4444aa5e5730786ac97b45e6dc5760549223fa1c0d5cb0f055560df61`, `diagnostics.py` `sha256:11316e2cd947383c374e0a109d5f4a37518b74e3036e0dbdee033849392c97a4`, `canonicalization.py` `sha256:f8e9b64522a61fcf8e46b192bf18f1f1277f356271486ae6ae08d559f7a56823`, `json_loader.py` `sha256:de5c2dea9d7e2b53d6ee9f48905cfadf5d88dcfe27087c41f1f20551ac0f3653`, `models.py` `sha256:5b9272a138c5d5146753338b223ac5a23cdac67a2ef87a4afb907d45e11eb541`, `__init__.py` `sha256:b3f7feca44ba8de6a8c2f9cb37ea4d9a1eea05c81ce6bb1c84d3ead4b0ca89d0`, `version.py` `sha256:744facb700c5c0c0686af39a2524ff1fef30483b45d3546d8ff8f47a33eb47af`; dependency pins [`requirements-validator.lock`](../../requirements-validator.lock) `sha256:9179039c098bf3acaef88ba559759a53c69dcc70caa18648b99b93107adc9505` |
| Deterministic execution identity | Python 3.13.15 on Windows 11, run with `-B`, `PYTHONDONTWRITEBYTECODE=1`, `PYTHONNOUSERSITE=1`, external `PYTHONPYCACHEPREFIX`, in a fresh virtual environment created outside the repository. The runner was executed **twice** to separate external outputs and produced **byte-identical** results (`cc918d562a8d7da17f462ce8a3040933d6c5fb850dbb8f85bd07464a2bbae1d0`, `30432` bytes); the digest package was likewise generated **twice** externally and was **byte-identical** (`d8e7732add7be12cea9168483501389f354e0bce36cd6f6309c48f2e6dd1d27a`, `19631` bytes). Case-manifest digest `sha256:6ab8ae5f0b15017d18d5efa18b23db1439d6d153015bcc860930cb97eab6ee55`. |
| Machine Evidence Package (NF-R11-001) | Result **and** Digest Package **jointly**; manifest `2` entries, `370` bytes, SHA-256 `02ca4b8170b6257b8ef2ff09da28125df77455179dee1da88c5a17694bec16f9`. Neither member alone is a complete Evidence Package. |
| Independent Evidence Review result | **PASS WITH NOTES** (reviewer ≠ executor, DEC-S-045) |
| Independent Evidence Review date | **2026-08-19** — the calendar date of the recorded project workflow. This is **not** a reconstructed precise review timestamp; no wall-clock time was recorded in the repository at review time. |
| Evidence limitations | Enumerated below — **not** an empty list |
| Evidence Admission state | **APPROVED / ADMITTED** |
| Evidence Admission decision date | 2026-08-19 |
| Evidence Admission authority | Human Maintainer |
| Admission record | [Semantic Status AE1-004 AE-1 Admission Record](../governance/SEMANTIC_STATUS_AE1_004_ADMISSION_RECORD.md) |

### Evidence limitations

The sixteen recorded
[Candidate accessibility limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md)
(**0 Critical · 11 Significant · 5 Minor**) apply unchanged; the evidence run
added none, removed none, and downgraded none. In addition, specific to
`AE1-CDS-WP016-SEMSTATUS-004`:

| # | Limitation |
| --- | --- |
| 1 | The evidenced bytes are **uncommitted**. Every evidence statement is bound to working-tree content that no commit contains. |
| 2 | The bound test suite is likewise **uncommitted**. |
| 3 | Structural DE/EN coverage is **not** a translation-quality or comprehension statement. |
| 4 | `$description` existence is **not** a readability, plain-language, or comprehension statement. |
| 5 | The dual-state proof establishes **test-suite lifecycle safety**, not artifact accessibility. |
| 6 | Three of the 25 per-value requirements are `COVERED_WITH_LIMITATION` rather than `COVERED` — rows 12, 13, and 22 of the [evidence requirements matrix](SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md) (`confidence.supported`, `confidence.uncertain`, `evidence.partial`). |
| 7 | No baseline environment was exercised; no assistive technology, browser, keyboard, or user was involved. AE-2, AE-3, and AE-4 are absent. |

**Prior-revision evidence does not transfer** (DEC-S-052, DEC-S-126 §4).
`AE1-CDS-WP016-SEMSTATUS-002` is admitted for `semantic-status-rev-0001` only and
is **not** cited here as evidence for these bytes.
`AE1-CDS-WP016-SEMSTATUS-003` was reviewed **PASS WITH NOTES**, is **NOT
ADMITTED**, and carries the disposition
`SUPERSEDED_FOR_ADMISSION_BY_EVIDENCE_INPUT_CHANGE`; it is likewise not cited as
evidence here.

## 4. Candidate gate

Both gates are reproduced **requirement by requirement**, in the normative
wording of the current committed sources. **No aggregate score is produced**;
partial satisfaction is never averaged into a pass (evidence rules 6 and 7).

### 4.1 Minimum Candidate gate — [Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md)

| # | Requirement | Pre-decision state | Supporting fact | Post-decision authority state |
| --- | --- | --- | --- | --- |
| 1 | Problem and scope stated | Satisfied | [Candidate Dossier](SEMANTIC_STATUS_CANDIDATE_DOSSIER.md) — target artifact, scope (5 axes, 25 values, ten invariants, combination/conflict rules, communication contract, token role contract, DE/EN parity, source set), and explicit exclusions | Unchanged — satisfied |
| 2 | Normative documentation exists | Satisfied | [Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md), [Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md), [Composition and Conflict Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md), [Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md), [Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md), [Terminology DE/EN](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md) | Unchanged — satisfied |
| 3 | Ownership assigned | Satisfied | CDS owns normative shared design rules and shared foundations ([Concept and Scope](../governance/CONCEPT_AND_SCOPE.md), DEC-S-008; [Scope Boundary Matrix](../governance/SCOPE_BOUNDARY_MATRIX.md)) | Unchanged — satisfied |
| 4 | Source revision identified | Satisfied | Proposed Candidate source revision `semantic-status-rev-0002-candidate`, declared inside the approved bytes and cross-checked by the runner (`match true`); authoritative pre-promotion revision `semantic-status-rev-0001` | Unchanged — satisfied for the identified proposed revision; the authoritative revision is still `semantic-status-rev-0001` |
| 5 | Known accessibility requirements stated, per the [Accessibility and Inclusive Design Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) — incl. the **Candidate accessibility gate** (mapping, responsibility, AE-1, AE-2 or plan, limitations, baseline plan, regression plan) | Elements 1–8 supported; element 9 **open** | See section 4.2, requirement by requirement | **Element 9 closed by the Human-Maintainer Candidate decision of 2026-08-19 for these exact bytes.** Elements 1–8 unchanged |
| 6 | Known risks registered | Satisfied | RISK-089, RISK-092, RISK-093, RISK-094, RISK-097, RISK-098, and the executor-self-confirmation and single-environment risks RISK-075 / RISK-078, all in the [Risk Register](../risks/RISK_REGISTER.md) | Unchanged — satisfied. **Documentation is not mitigation**, and no risk is accepted or closed here |
| 7 | Evidence plan | Satisfied | [Accessibility Evidence Strategy](../governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md) and the [Candidate AE-2 Evidence Plan](../governance/SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md) | Unchanged — satisfied. A plan is not evidence |
| 8 | Consumer validation plan | Satisfied as a plan | [Consumer Validation Plan](../governance/CONSUMER_VALIDATION_PLAN.md) — normative for how pilot evidence is judged. **No consumer validation has been executed**; no consumer integration exists or is authorized | Unchanged — the plan exists; **no consumer evidence exists** |
| 9 | Provenance | Satisfied | [Token Metadata, Provenance and Identity Model](../architecture/TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md); exact-byte identities in section 2; review provenance in [WP016 Candidate Finalization Evidence Review Provenance](../reviews/WP016_CANDIDATE_FINALIZATION_EVIDENCE_REVIEW_PROVENANCE.md) | Unchanged — satisfied |
| 10 | Open limitations stated honestly | Satisfied | 16 recorded [Candidate accessibility limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md) (0 Critical) plus the seven evidence limitations in section 3 | Unchanged — satisfied. Requirement 10 is a gate, not a footnote |

### 4.2 Candidate accessibility gate — [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)

| # | Requirement | Pre-decision state | Evidence / authority basis | Post-decision state |
| --- | --- | --- | --- | --- |
| 1 | WCAG applicability mapping | Satisfied for the declared source scope | [Candidate WCAG Applicability Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md) — 56 rows: 5 direct, 30 representation-triggered, 20 consumer-owned, 1 historical not-applicable | Unchanged — satisfied |
| 2 | Responsibility mapping | Satisfied | [Candidate Accessibility Responsibility Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_RESPONSIBILITY_MAPPING.md) — 13 subjects: 5 CDS, 8 Shared, 0 Consumer-only | Unchanged — satisfied |
| 3 | Known accessibility requirements | Satisfied | [Candidate Evidence Requirements Matrix](SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md) — 25/25 mapped, 0 unmapped, 22 `COVERED` + 3 `COVERED_WITH_LIMITATION` | Unchanged — satisfied |
| 4 | **AE-1** | Satisfied **only** by `AE1-CDS-WP016-SEMSTATUS-002` for `semantic-status-rev-0001`; **not** satisfied for the Proposed Candidate revision until its own evidence was admitted | `AE1-CDS-WP016-SEMSTATUS-004` — result **Pass with limitations**, independent review **PASS WITH NOTES**, Human-Maintainer admission **APPROVED / ADMITTED** 2026-08-19, bound to `semantic-status-rev-0002-candidate` | **Satisfied for `semantic-status-rev-0002-candidate`**, source/contract scope only |
| 5 | Relevant **AE-2** evidence, or a reasoned evidence plan | Satisfied by reasoned plan | [Candidate AE-2 Evidence Plan](../governance/SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md) — AE-2 execution is not meaningful against an artifact with no interactive surface and was **not** fabricated | Unchanged — satisfied by plan. **AE-2 evidence does not exist** |
| 6 | Known limitations | Satisfied as a documentation requirement | 16 entries with the normative 15 fields: **0 Critical · 11 Significant · 5 Minor**; none approved as an exception; no waiver | Unchanged — satisfied. **No Critical limitation exists**, so no Critical limitation blocks approval |
| 7 | Support baseline plan | Satisfied | [Candidate Support Baseline Plan](../governance/SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md) on A11Y-BL-001 with freshness **`Current`** ([freshness review](../reviews/WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md), 2026-08-17) | Unchanged — satisfied. **A baseline is not evidence** |
| 8 | Regression plan | Satisfied | [Candidate Accessibility Regression Plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md) — 15 triggers; **T-12 is not waived** | Unchanged — satisfied |
| 9 | **Human Maintainer approval after Nova review** | **OPEN** — the final open authority requirement | Nova Candidate Finalization Review **GO WITH NOTES** (recommendation only, 2026-08-19), then the Human-Maintainer decision of 2026-08-19 | **Decided for these exact Proposed Candidate bytes** — `AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION` |

### 4.3 Gate outcome

| Field | Value |
| --- | --- |
| Unresolved blockers | **None** for these exact approved bytes |
| Unresolved limitations | 16 recorded accessibility limitations + the 7 evidence limitations of section 3 — all recorded, none hidden, none waived |
| Critical limitations | **0** — no Critical limitation exists, and none blocks this approval |
| Candidate gate prerequisites + approval decision | **SATISFIED FOR THE EXACT APPROVED PROPOSED BYTES** |
| **Repository Candidate maturity** | **NOT YET EFFECTIVE** |
| Reason | **Promotion Commit: PENDING** |

**The repository is not Candidate.** Gate satisfaction for a set of proposed
bytes is not a maturity state; only the Human-Maintainer exact-byte Promotion
Commit makes `Experimental → Candidate` effective (DEC-S-126 §9).

## 5. Nova review

| Field | Value |
| --- | --- |
| Nova Finalization Review result | **GO WITH NOTES** |
| Date | 2026-08-19 |

### Notes

| # | Note |
| --- | --- |
| 1 | `AE1-CDS-WP016-SEMSTATUS-004` fresh independent review: **PASS WITH NOTES**. |
| 2 | `AE1-CDS-WP016-SEMSTATUS-004` Human-Maintainer admission: **APPROVED / ADMITTED**. |
| 3 | **NF-PREP-001 / F-R1: CLOSED** — the seven confirmed superseded lifecycle premises were made transition-safe; 0 assertions weakened, 0 tests deleted, 0 skipped, 0 expected failures. |
| 4 | **F-R2: CLOSED.** |
| 5 | **NF-REV004-002: CLOSED** — repository review provenance for the AE1-003 and AE1-004 review events now exists. |
| 6 | **OBS-TLR-001** remains **non-blocking**: a future Promotion verification must use the committed Git blob identity or an equivalently controlled LF materialization, because `.py` is not explicitly `eol=lf` pinned. |
| 7 | **NF-REV004-001** remains **Low / non-blocking**: the AE1-004 artifacts do not themselves carry the blob-verification implementation note; the Promotion procedure must bind the method explicitly. |
| 8 | **NF-REV004-003** remains an **Observation / non-blocking**: the twice-generated digest identity is not independently reproducible without a committed digest generator; 43/43 declared identities were independently recomputed with 0 mismatches. |
| 9 | **Exact-byte Promotion and committed Git-blob verification remain mandatory.** |

**A Nova GO is a recommendation, never an approval.** Unclear readiness resolves
as NO-GO, never as "go with notes" (DEC-S-048). The Human-Maintainer decision in
section 7 is the approval authority.

## 6. Preconditions confirmed

| # | Precondition | Confirmed |
| --- | --- | --- |
| 1 | Proposed Candidate bytes prepared and enumerated (section 2) | **YES** |
| 2 | Fresh revision-bound evidence produced (section 3) | **YES** |
| 3 | Fresh independent evidence review completed (section 3) | **YES** |
| 4 | **Human-Maintainer evidence admission granted** (section 3) | **YES** |
| 5 | Nova Candidate finalization review completed (section 5) | **YES** |

**All five substantive prerequisites were complete before the Human-Maintainer
Candidate decision in section 7.** Evidence admission and Candidate approval are
separate Human-Maintainer decisions, and admission preceded approval
(DEC-S-126 §8).

## 7. Human-Maintainer Candidate decision

| Field | Value |
| --- | --- |
| Decision | **`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`** |
| Decision date | 2026-08-19 |
| Deciding authority | **Human Maintainer** |

### Rationale

| # | Basis |
| --- | --- |
| 1 | The exact Proposed Candidate bytes were prepared, frozen, and enumerated by identity (3 files, manifest `497` bytes, SHA-256 `3b80d148…`). |
| 2 | Fresh revision-bound AE-1 evidence `AE1-CDS-WP016-SEMSTATUS-004` was produced against exactly those bytes, result **Pass with limitations**. |
| 3 | A fresh independent evidence review by a reviewer who was neither executor returned **PASS WITH NOTES**. |
| 4 | The Human Maintainer admitted `AE1-CDS-WP016-SEMSTATUS-004` at **AE-1** on 2026-08-19, closing Candidate accessibility gate element 4 for the Proposed Candidate revision. |
| 5 | The Nova Candidate Finalization Review returned **GO WITH NOTES**, with all remaining notes classified non-blocking. |
| 6 | No Candidate-approval blocker remained: 0 Critical limitations, 0 unresolved blockers, 0 open Candidate gate requirements for these exact bytes. |

### Conditions

This approval covers **these exact bytes only**, and holds only while every
condition below holds:

| # | Condition |
| --- | --- |
| 1 | The three approved source files remain **byte-identical** to the identities recorded in section 2. |
| 2 | The bound transition-safe test bytes remain **unchanged** (`93091d4b…`, `43960` bytes). |
| 3 | The admitted `AE1-CDS-WP016-SEMSTATUS-004` package — Result and Digest Package — remains **unchanged**. |
| 4 | The bound review provenance record remains **unchanged** (`0dcf6ff9…`, `13884` bytes). |
| 5 | The authority records — this record and the [AE1-004 Admission Record](../governance/SEMANTIC_STATUS_AE1_004_ADMISSION_RECORD.md) — remain **truthful**, and are corrected rather than stretched if any fact changes. |
| 6 | The **staged and committed Git blobs must match the approved identities** exactly. |
| 7 | **OBS-TLR-001 / NF-REV004-001 blob verification is mandatory**: verification uses the committed Git blob identity, or an equivalently controlled LF materialization, never an unpinned working-tree hash. |
| 8 | A **full post-commit regression verification** is performed. |
| 9 | The **remote must fast-forward**; no history rewrite, no force. |
| 10 | **Any drift invalidates this authorization** — see section 10. |

### Allowed decision states, for reference

| State | Meaning |
| --- | --- |
| `NOT_DECIDED` | No Candidate decision has been made. |
| `NOT_APPROVED` | The Human Maintainer examined the package and declined. |
| **`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`** | **The recorded state.** These exact bytes are approved for Candidate, conditional on their unmodified integration. **The repository is not Candidate while this state holds.** |

No other decision state exists, and **no state in this record makes the
repository Candidate**.

## 8. Effectivity

> **A Candidate Approval Record is not a Promotion Commit.**
>
> **Candidate maturity becomes effective in the repository only after the exact
> approved bytes have been successfully integrated by the Human Maintainer.**

### Current committed repository

| Field | Value |
| --- | --- |
| Source revision | **`semantic-status-rev-0001`** |
| Maturity | **`Experimental`** |
| Approval | **`Unapproved`** |
| Candidate | **No** |
| Admitted evidence | `AE1-CDS-WP016-SEMSTATUS-002` (rev-0001 scope) and `AE1-CDS-WP016-SEMSTATUS-004` (rev-0002-candidate scope, uncommitted bytes) |

### Approved Proposed Candidate

| Field | Value |
| --- | --- |
| Source revision | `semantic-status-rev-0002-candidate` |
| Target maturity | `Candidate` |
| Target approval | `Approved` |
| **Effectivity** | **PENDING EXACT-BYTE PROMOTION COMMIT** |

Before integration the authoritative repository state remains **Candidate: No ·
Maturity: Experimental · Approval: Unapproved**, whatever this record says and
whatever metadata the proposed bytes declare. The Promotion Commit is the actual
maturity transition point (DEC-S-126 §9).

## 9. Integration

*(Pending until the Human Maintainer performs the Promotion Commit. Completing
this section must not require any mutation of the evidenced source bytes.)*

| Field | Value |
| --- | --- |
| Promotion Commit | **PENDING** |
| Parent revision | `8d1374fa4c61cc1eed214823681ee1209a2d91f7` |
| Exact-byte result | **PENDING PROMOTION GATE** |
| Staged blob result | **PENDING PROMOTION GATE** |
| Committed blob result | **PENDING PROMOTION COMMIT** |
| Source revision after integration | **PENDING** — expected `semantic-status-rev-0002-candidate` only after exact promotion |
| Post-commit validation result | **PENDING** |
| Post-commit regression verification result | **PENDING** |
| Remote result | **PENDING** |
| Integration date | **PENDING** |

**This section must be completed after a successful Promotion.** The future
Promotion Commit SHA is deliberately **not predicted**, and no result above is
invented.

Where the committed source is byte-identical to the independently reviewed,
evidence-bound proposed source, the post-commit verification **confirms the same
evidence binding**. It does not by itself require another Evidence ID, another
independent evidence review, or another admission solely because Git persisted
already-reviewed exact bytes (DEC-S-126 §10).

## 10. Invalidation

Any mismatch between the approved, reviewed, and evidenced Candidate bytes and
the integrated source — including any mismatch between approved bytes, staged
blobs, and committed blobs — **invalidates**
`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`.

On any such mismatch:

1. The approval no longer covers the integrated content. **Do not amend this
   record to fit the new bytes.**
2. Fresh evidence is required for the changed bytes.
3. A fresh independent evidence review is required.
4. A fresh Human-Maintainer evidence admission is required.
5. A fresh Candidate approval is required, recorded in a **new instance** with a
   new Record ID.

**There is no "small fix" exemption** (DEC-S-126 §7). This applies equally to a
whitespace change, a reordering, a trailing-newline change, and a correction the
executor believes to be harmless.

## 11. Boundaries

This record establishes **none** of the following:

| Not established | State |
| --- | --- |
| Stable maturity | **No** |
| Any claim of any level | **None** |
| Conformance of any kind | **None** |
| WCAG conformance | **None** |
| AE-2 | **None** |
| AE-3 | **None** |
| AE-4 | **None** |
| Channel evidence | **None** |
| Consumer evidence | **None** |
| Assistive-technology support | **None** |
| Product Profile | **None** |
| CoreOps or other consumer pilot | **inactive** |
| CDS-WP-017 activation | **inactive** |
| Licence selection | **None** |
| Publication | `Private Development`, unchanged |
| Release | **None** |
| Tag | **None** |

Candidate is **bounded validation only, and is never normative**
([Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md)).
`CDS certified` is prohibited; no certification programme exists (DEC-S-044).

## Related documents

- [Candidate Approval Record Template](CANDIDATE_APPROVAL_RECORD_TEMPLATE.md) — the form this record instantiates
- [Semantic Status Candidate Dossier](SEMANTIC_STATUS_CANDIDATE_DOSSIER.md)
- [AE1-004 Evidence Record](SEMANTIC_STATUS_CANDIDATE_AE1_004_EVIDENCE_RECORD.md) — the admitted evidence package's human-readable record
- [Semantic Status AE1-004 AE-1 Admission Record](../governance/SEMANTIC_STATUS_AE1_004_ADMISSION_RECORD.md) — the separate evidence-admission instrument
- [Candidate Finalization Evidence Review Provenance](../reviews/WP016_CANDIDATE_FINALIZATION_EVIDENCE_REVIEW_PROVENANCE.md)
- [Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md) — normative
- [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) — normative
- [Semantic Status AE-1 Admission Record](../governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md) — `AE1-CDS-WP016-SEMSTATUS-002`, `semantic-status-rev-0001` scope only
- [Decision Index](../decisions/DECISION_INDEX.md) — DEC-S-125, DEC-S-126
- [Risk Register](../risks/RISK_REGISTER.md) — RISK-098
