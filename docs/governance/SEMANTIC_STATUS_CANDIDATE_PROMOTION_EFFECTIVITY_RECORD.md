# Semantic Status — Candidate Promotion Effectivity Record

- **Project:** Core Design System (CDS)
- **Record type:** **Governance lifecycle effectivity record.**
- **Status:** **Authoritative repository record for the already completed
  Semantic Status Candidate promotion effectivity event.**
- **Date:** 2026-08-19
- **Work package:** CDS-WP-016 — Post-Promotion Current-State Reconciliation
  (Human-Maintainer authorized 2026-08-19; internal reconciliation of
  CDS-WP-016, **not** a new work package)
- **Authority produced by this file:** **NONE**

> **This record does not promote anything.** The promotion already happened, in
> Promotion Commit `22fa0710e2b75df22e7b420c2f9d86bbe67b2777`. This file records
> that completed event so the repository's current lifecycle state is checkable
> from repository bytes.

## What this record is, and is not

**This record IS:**

- documentation that the Semantic Status Candidate promotion **became
  effective**, and of the exact commit that made it effective;
- a statement of which source revision, maturity, approval, and evidence are
  current in the committed repository after that commit;
- independently recomputable from repository bytes and Git object identities.

**This record is NOT:**

| Not | Why it matters |
| --- | --- |
| Evidence | No evidence byte was produced, changed, or admitted here. The admitted evidence is `AE1-CDS-WP016-SEMSTATUS-004` and its own package. |
| A Promotion Commit | The Promotion Commit is `22fa0710e2b75df22e7b420c2f9d86bbe67b2777`, performed by the Human Maintainer. This file is written afterwards and moves nothing. |
| A Candidate approval | The approval is the separate Human-Maintainer decision recorded in the [Candidate Approval Record](../operations/SEMANTIC_STATUS_CANDIDATE_APPROVAL_RECORD.md). |
| An evidence admission | The admission is the separate Human-Maintainer decision recorded in the [AE1-004 Admission Record](SEMANTIC_STATUS_AE1_004_ADMISSION_RECORD.md). |
| A new Decision | No `DEC-S-` identifier is created. The governing decision is DEC-S-126, already accepted. |
| A new Risk or ADR | No `RISK-` and no `ADR-` identifier is created. |
| A precedence policy | It creates **no** general rule about which normative source class wins a conflict. See "Bound Foundation lifecycle-metadata reconciliation" below. |
| Stable maturity | **Not granted.** Candidate is bounded validation only, and is never normative. |
| A claim or conformance statement | **None.** No claim of any level is valid today, for anyone, including CDS. |
| A release, tag, or publication | **None.** Publication remains `Private Development`. |

## Promotion identity

| Field | Value |
| --- | --- |
| Artifact | Semantic Status Foundation |
| Artifact class | Channel-independent Layer-3 Semantic Source / Contract family |
| Source set | `semantic/status` |
| **Promotion Commit** | **`22fa0710e2b75df22e7b420c2f9d86bbe67b2777`** |
| **Promotion Parent** | `8d1374fa4c61cc1eed214823681ee1209a2d91f7` |
| Commit subject | `feat(cds): promote semantic status foundation to Candidate` |
| **Effective source revision** | **`semantic-status-rev-0002-candidate`** |
| **Effective maturity** | **`Candidate`** |
| **Effective approval** | **`Approved`** |
| **Candidate** | **YES** |
| **Effectivity date** | **2026-08-19** |
| Promoting authority | **Human Maintainer** |

### Admitted evidence in force for the effective revision

| Field | Value |
| --- | --- |
| Evidence ID | `AE1-CDS-WP016-SEMSTATUS-004` |
| Evidence level | **AE-1** |
| Evidence scope | Channel-independent Layer-3 Semantic Source / Contract family |
| Admission authority | Human Maintainer |
| Admission record | [Semantic Status AE1-004 AE-1 Admission Record](SEMANTIC_STATUS_AE1_004_ADMISSION_RECORD.md) |

### Exact bound identities

| Item | Value |
| --- | --- |
| **Candidate Source Manifest** | `3` entries · `497` bytes · SHA-256 `3b80d1483ceba4de61c5f9b1f99e10ff00f6da17ac935a1ddfa643a413204ebf` |
| **Machine Evidence Package Manifest** | `2` entries · `370` bytes · SHA-256 `02ca4b8170b6257b8ef2ff09da28125df77455179dee1da88c5a17694bec16f9` |
| Canonical manifest line format | `<STATUS>`, `<SHA256>`, `<BYTES>`, `<GIT_RAW_OBJECT_ID>`, `<PATH>` — tab-separated, one line per entry, ordinal-sorted by path, UTF-8 without BOM, LF-only, final LF |

A digest is an integrity aid. It is **not** a signature and proves no authorship,
approval, authenticity, or release (DEC-S-090, DEC-S-100, RISK-072).

### Promotion gate result

| Check | Result |
| --- | --- |
| Exact-byte Promotion Gate | **PASS** |
| Committed blob identity | **15 / 15 exact** |
| PRE regression | **47/47 · 64/64 · 184/184 · 24/24/0/0** |
| POST regression | **47/47 · 64/64 · 184/184 · 24/24/0/0** |
| Remote Fast-Forward Gate | **PASS** |
| `origin/main` | `22fa0710e2b75df22e7b420c2f9d86bbe67b2777` |

The regression figures are, in order: semantic-status tests, Candidate evidence
tests, full validator suite, and the validation-case harness reported as
`totalCases / expectedMatches / expectedMismatches / executionErrors`.

## Bound Foundation lifecycle-metadata reconciliation

Five normative Foundation documents are **bound evidence inputs** of
`AE1-CDS-WP016-SEMSTATUS-004`. They were **not** edited by the promotion and are
**not** edited by this reconciliation. Their bytes are unchanged.

| # | Path | Current Git blob | Semantic authority | Byte mutation | Lifecycle-metadata classification |
| --- | --- | --- | --- | --- | --- |
| 1 | [`SEMANTIC_STATUS_FOUNDATION_CONTRACT.md`](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) | `72a2f7128b9397456c8b6fda8b4db41a2dd2fc79` | **UNCHANGED / NORMATIVE** | **NONE** | `HISTORICAL_FOR_CURRENT_LIFECYCLE_STATE` |
| 2 | [`STATUS_AXIS_VOCABULARY.md`](../foundations/STATUS_AXIS_VOCABULARY.md) | `325f8a57d53129d00e826eebdfdf38ec0d2f47ef` | **UNCHANGED / NORMATIVE** | **NONE** | `HISTORICAL_FOR_CURRENT_LIFECYCLE_STATE` |
| 3 | [`STATUS_COMPOSITION_AND_CONFLICT_RULES.md`](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) | `c31ccb830f8586b78a3d88d67c467aae1f44f52a` | **UNCHANGED / NORMATIVE** | **NONE** | `HISTORICAL_FOR_CURRENT_LIFECYCLE_STATE` |
| 4 | [`STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md`](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md) | `24eaf274f78ef7e680e337f7ec6ffb6fac9c3710` | **UNCHANGED / NORMATIVE** | **NONE** | `HISTORICAL_FOR_CURRENT_LIFECYCLE_STATE` |
| 5 | [`SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md`](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md) | `4a1d213e5932b08e38ac54b72ac6f599960e6a2e` | **UNCHANGED / NORMATIVE** | **NONE** | `HISTORICAL_FOR_CURRENT_LIFECYCLE_STATE` |

For all five, uniformly:

- **Semantic content:** UNCHANGED / NORMATIVE.
- **Pre-promotion lifecycle metadata:** `HISTORICAL_FOR_CURRENT_LIFECYCLE_STATE`.
- **Current lifecycle state:** supplied by the already authorized and completed
  Candidate promotion event recorded above.
- **Byte mutation:** NONE.

### What this reconciliation says, and does not say

The embedded pre-promotion labels in these frozen, evidence-bound documents —
`Experimental`, `Unapproved`, and "no Candidate status" — remain part of their
historical bytes and are **NOT edited**.

They are **not** used as the current lifecycle-state mirror after Promotion
Commit `22fa0710e2b75df22e7b420c2f9d86bbe67b2777`.

This scoped reconciliation does **NOT** establish a general precedence rule
between human-readable and machine-readable normative sources.

It does **NOT** say that recency wins.

It does **NOT** say that machine-readable sources override human-readable
meaning.

It records **one completed lifecycle transition**, already governed by DEC-S-126
and approved by the Human Maintainer.

The distinction is binding:

- **Lifecycle effectivity ≠ semantic rewrite.**
- **Current maturity state ≠ meaning precedence.**

The five documents remain **normative for their actual semantic content**. The
authority and conflict rules of the
[Source of Truth and Authority Model](../architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)
and the
[Source Conflict Resolution Policy](SOURCE_CONFLICT_RESOLUTION_POLICY.md)
are unchanged by this record, including the rule that a conflict is **never**
resolved by recency or by convenience (DEC-S-023).

## Evidence boundary

| Statement | State |
| --- | --- |
| Evidence bytes changed | **NONE** |
| Source bytes changed | **NONE** |
| Foundation bound-input bytes changed | **NONE** |
| Evidence transferred | **NONE** |
| Evidence waiver | **NONE** |
| New evidence ID created | **NONE** |
| New evidence admission performed | **NONE** |

`AE1-CDS-WP016-SEMSTATUS-004` remains **exact-byte bound** to the identities
recorded in its admission record.

`AE1-CDS-WP016-SEMSTATUS-002` remains a **historical `semantic-status-rev-0001`
admission only**, and does not cover the effective revision.

`AE1-CDS-WP016-SEMSTATUS-003` remains **NOT ADMITTED** with the disposition
`SUPERSEDED_FOR_ADMISSION_BY_EVIDENCE_INPUT_CHANGE`.

**Evidence never transfers across a source revision** (DEC-S-126). A future
Candidate or Stable revision requires fresh evidence, a fresh independent review,
and a fresh admission.

Any future change to **any** of the five frozen Foundation documents above still
triggers the existing re-evidence rule recorded in the
[AE1-004 Admission Record](SEMANTIC_STATUS_AE1_004_ADMISSION_RECORD.md) and in
regression trigger **T-12** of the
[Candidate Accessibility Regression Plan](SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md),
which is **not waived**. **No "small fix" exemption is created** by this record.

## Boundaries

| Item | State |
| --- | --- |
| **Candidate** | **YES** |
| **Stable** | **NO** |
| Claims | **NONE** |
| Conformance | **NONE** |
| WCAG conformance | **NONE** |
| AE-2 | **NONE** |
| AE-3 | **NONE** |
| AE-4 | **NONE** |
| Channel evidence | **NONE** |
| Consumer evidence | **NONE** |
| Product Profile authority | **NONE** |
| CoreOps pilot | **INACTIVE** |
| Publication | **`Private Development`** |
| Release | **NONE** |
| Tag | **NONE** |
| CDS-WP-017 | **INACTIVE / NOT AUTHORIZED / NOT DEFINED** |

Candidate is **bounded validation only, and is never normative**
([Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md)). `CDS certified`
is prohibited; no certification programme exists (DEC-S-044).

**No baseline environment has been exercised.** No assistive technology, browser,
keyboard, renderer, or user was involved in any admitted evidence, so no
environment is supported and no support claim exists (DEC-S-069).

## Related documents

- [Semantic Status Candidate Approval Record](../operations/SEMANTIC_STATUS_CANDIDATE_APPROVAL_RECORD.md) — the Human-Maintainer Candidate decision instrument
- [Semantic Status AE1-004 AE-1 Admission Record](SEMANTIC_STATUS_AE1_004_ADMISSION_RECORD.md) — the separate evidence-admission instrument
- [Semantic Status AE-1 Admission Record](SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md) — `AE1-CDS-WP016-SEMSTATUS-002`, `semantic-status-rev-0001` scope only
- [Semantic Status Candidate Dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md)
- [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md) — normative
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) — normative
- [Semantic Status Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md)
- [Candidate Finalization Evidence Review Provenance](../reviews/WP016_CANDIDATE_FINALIZATION_EVIDENCE_REVIEW_PROVENANCE.md)
- [Decision Index](../decisions/DECISION_INDEX.md) — DEC-S-125, DEC-S-126
- [Risk Register](../risks/RISK_REGISTER.md) — RISK-031, RISK-098
