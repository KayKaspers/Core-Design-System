# Semantic Status — AE1-004 AE-1 Admission Record

- **Status:** **Authoritative for the fact and the exact scope of this specific
  Human-Maintainer `AE1-CDS-WP016-SEMSTATUS-004` admission decision.**
- **Record type:** Governance authority record — **not evidence**.
- **Human-Maintainer admission decision date:** 2026-08-19
- **Repository materialization:** 2026-08-19, during the CDS-WP-016 Candidate
  Authority Record Materialization (Human-Maintainer authorized 2026-08-19;
  internal rework of CDS-WP-016, **not** a new work package)
- **Authority produced by this file:** **NONE**

## Temporal truth — the decision came first, this file afterwards

The Human-Maintainer admission decision was made on **2026-08-19**, after all
substantive preconditions had been satisfied: the exact Proposed Candidate bytes
were prepared and enumerated, fresh revision-bound evidence was produced against
them, a fresh independent evidence review was completed, and Nova adjudicated.

**This repository file is the subsequent repository-local materialization of that
already-made decision.** It does not retroactively pretend to have existed at
decision time, it did not itself grant the admission, and it is not the decision.
Writing it down changes nothing about what was decided; it only makes the fact,
the scope, and the exact bound bytes independently checkable inside the
repository.

Exact wall-clock times, reviewer session identifiers, and reviewer cryptographic
identities were not recorded in the repository at decision time. They are
**omitted here rather than reconstructed**. Only the calendar date is stated.

## What this record is, and is not

**This record IS:**

- documentation that a Human-Maintainer AE-1 admission decision **was made**;
- a statement of that admission's exact, revision-bound, exact-byte scope;
- independently recomputable from repository bytes.

**This record is NOT:**

| Not | Why it matters |
| --- | --- |
| Evidence | The evidence is the admitted package itself; this record only records that it was admitted. |
| The admission decision | The decision was made by the Human Maintainer before this file existed. |
| A new evidence level | AE-0 … AE-4 are unchanged in definition, scope, and sufficiency. |
| A general policy | It governs one artifact family, one proposed source revision, one evidence package. |
| Candidate maturity | Repository Candidate status remains **No**. |
| Candidate approval | Evidence admission and Candidate approval are separate Human-Maintainer decisions (DEC-S-126). |
| A Promotion Commit | Nothing has been staged, committed, or integrated. |
| Stable maturity | **Not granted.** No AE-2, AE-3, or AE-4 exists anywhere. |
| An accessibility claim | No claim of any level is valid today, for anyone, including CDS. |
| WCAG conformance | Nothing here demonstrates any WCAG success criterion. |
| A certification | No certification programme exists; `CDS certified` is prohibited (DEC-S-044). |
| A channel statement | No channel evidence exists. |
| Consumer evidence | No consumer has been evaluated, and none is authorized. |
| A Decision, a Risk, or an ADR | No new governance identifier is created. |

## Admission identity

| Item | Value |
| --- | --- |
| **Artifact** | Semantic Status Foundation |
| **Artifact class** | Channel-independent Layer-3 Semantic Source / Contract family |
| **Source set** | `semantic/status` |
| **Proposed Candidate source revision** | `semantic-status-rev-0002-candidate` |
| **Admitted evidence ID** | `AE1-CDS-WP016-SEMSTATUS-004` |
| **Admitted level** | **AE-1** |
| **Evidence class** | **Structural and Automated Evidence** |
| **Evidence execution state** | **Proposed Candidate / modified Working Tree** — uncommitted, non-authoritative bytes |
| **Evidence base repository revision** | `8d1374fa4c61cc1eed214823681ee1209a2d91f7` |
| **Evidence result** | **Pass with limitations** |
| **Fresh independent evidence review** | **PASS WITH NOTES** |
| **Nova admission recommendation** | **GO WITH NOTES** |
| **Human-Maintainer admission decision** | **APPROVED / ADMITTED** |
| **Admission date** | 2026-08-19 |
| **Admission authority** | Human Maintainer |

The evidence base repository revision is the committed baseline **from which** the
Proposed Candidate was prepared. It does **not** state that the admitted bytes are
contained in that commit. They are not.

## Admitted byte identity

The admission is bound to exact bytes. Canonical manifest line format, ordinal
sorted by path, UTF-8 without BOM, LF-only, final LF:

`<STATUS>\t<SHA256>\t<BYTES>\t<GIT_RAW_OBJECT_ID>\t<PATH>\n`

### Proposed Candidate Source Manifest

| Item | Value |
| --- | --- |
| Entries | `3` |
| Manifest byte length | `497` |
| Manifest SHA-256 | `3b80d1483ceba4de61c5f9b1f99e10ff00f6da17ac935a1ddfa643a413204ebf` |

| Status | Path | Raw SHA-256 | Bytes | Git raw object |
| --- | --- | --- | --- | --- |
| `M` | [`semantic-status.resolver.json`](../../tokens/semantic/status/semantic-status.resolver.json) | `0d9ff65fb65c9eca3abe5f3bd6bf37492b043c8308191feda9c8319a43c45004` | `572` | `d6d75f981ff7d8ad556ce98387453402d458437e` |
| `M` | [`semantic-status.source-set.json`](../../tokens/semantic/status/semantic-status.source-set.json) | `8dda44d28ac654c33892e4c362c83260ba2bd1ab97526ef90dbddb6f72d52ef6` | `1041` | `fe7bbf1e7af49f753bd9cd75547ad69a5ae92ca9` |
| `M` | [`semantic-status.tokens.json`](../../tokens/semantic/status/semantic-status.tokens.json) | `53312e93810a6296c2b82b9365d17d14e7e74485cdeb5e13bba149634d4cb55e` | `6358` | `7d6b3499d1b291c04e1a3b6eca1b4ca54baf2df2` |

RFC 8785 (JCS) canonical content digests for the same three files, as bound by the
admitted digest package (ADR-0002):

| Path | RFC 8785 content digest |
| --- | --- |
| `tokens/semantic/status/semantic-status.resolver.json` | `sha256:c73a6fa34c40de3cc1ace2a69e9e3f7f82b07d6cb5927e673c96f1c0e242a8be` |
| `tokens/semantic/status/semantic-status.source-set.json` | `sha256:db5626e648d1076200ca16ece8adf5ba4dcd6077210cff76092707de9d6fb12d` |
| `tokens/semantic/status/semantic-status.tokens.json` | `sha256:317c464807c04b9b0f6cc05f46cab955f58f5739d7c39fe61d55702a20412c34` |

These three files declare `sourceRevision` `semantic-status-rev-0002-candidate`,
`maturityState` `Candidate`, and `approvalState` `Approved`. Those values are
**TARGET metadata inside uncommitted, non-authoritative bytes**. They are a
target, never a current state, and they grant nothing.

### Complete machine Evidence Package Manifest — NF-R11-001

| Item | Value |
| --- | --- |
| Entries | `2` |
| Manifest byte length | `370` |
| Manifest SHA-256 | `02ca4b8170b6257b8ef2ff09da28125df77455179dee1da88c5a17694bec16f9` |

| Status | Member | Path | Raw SHA-256 | Bytes | Git raw object |
| --- | --- | --- | --- | --- | --- |
| `U` | Digest Package | [`wp016-candidate-finalization-ae1-004-digests.json`](../../artifacts/validation/wp016-candidate-finalization-ae1-004-digests.json) | `d8e7732add7be12cea9168483501389f354e0bce36cd6f6309c48f2e6dd1d27a` | `19631` | `82bcf59fe604edb1210d211ce7a06dd259c3fbba` |
| `U` | Runner Result | [`wp016-candidate-finalization-ae1-004-results.json`](../../artifacts/validation/wp016-candidate-finalization-ae1-004-results.json) | `cc918d562a8d7da17f462ce8a3040933d6c5fb850dbb8f85bd07464a2bbae1d0` | `30432` | `7b16acad468d28e4e7bbccf14a67f1b81963f2d0` |

**Under NF-R11-001, the Result and the Digest Package jointly form the complete
machine Evidence Package.** Neither artifact alone is sufficient for review, and
neither alone was admitted: the Result states what was checked, the Digest
Package states which exact bytes were checked.

### Bound transition-safe test input

| Item | Value |
| --- | --- |
| Path | [`tests/validator/test_semantic_status_candidate_evidence.py`](../../tests/validator/test_semantic_status_candidate_evidence.py) |
| Raw SHA-256 | `93091d4b6f353b19977af0d7aa1b93b9281972152716c8897eca1c2f9e460b70` |
| Byte length | `43960` |
| Git raw object | `f275d73a3e9bfafc937dd6dfc967850f9cd11a9c` |

This file is a **bound evidence input**, not merely a test. Changing it after
evidence generation invalidates that evidence for admission purposes, even when
the evidenced source bytes are untouched — which is precisely why
`AE1-CDS-WP016-SEMSTATUS-004` exists at all.

### Bound review provenance

| Item | Value |
| --- | --- |
| Path | [`WP016_CANDIDATE_FINALIZATION_EVIDENCE_REVIEW_PROVENANCE.md`](../reviews/WP016_CANDIDATE_FINALIZATION_EVIDENCE_REVIEW_PROVENANCE.md) |
| Raw SHA-256 | `0dcf6ff94a79f24c2ddd3834aec6a5b869cc7aef3585e0fa2977cb8b0bdf472a` |
| Byte length | `13884` |
| Git raw object | `2be794d6534249dcabfbf9e40fd564de036d68d4` |

**A digest is an integrity aid.** It is not a signature and proves no authorship,
approval, authenticity, or release (DEC-S-090, DEC-S-100, RISK-072).

## Admission scope boundary

This admission applies **only** to the exact-byte, revision-bound,
channel-independent Semantic Status Layer-3 Source / Contract family identified
above.

It grants **none** of the following:

| Not granted | State |
| --- | --- |
| Candidate maturity | **No** |
| Stable maturity | **No** |
| Candidate Promotion | **Not performed** |
| Any claim of any level | **None** |
| Conformance of any kind | **None** |
| WCAG conformance | **None** |
| AE-2 | **None** |
| AE-3 | **None** |
| AE-4 | **None** |
| Channel evidence | **None** |
| Consumer evidence | **None** |
| Rendering behaviour evidence | **None** |
| Interaction behaviour evidence | **None** |
| Keyboard evidence | **None** |
| Focus behaviour evidence | **None** |
| Screen-reader / assistive-technology evidence | **None** |
| Browser or platform support | **None** |
| Product Profile authority | **None** |
| Consumer pilot authority | **None** |
| Publication | `Private Development`, unchanged |
| Release | **None** |
| Tag | **None** |

**No baseline environment was exercised.** The evidence references A11Y-BL-001 as
its test contract without testing in any environment listed there, so **no
environment is supported** and no support claim exists (DEC-S-069). No assistive
technology was used, no keyboard testing was performed, and no user research
exists.

Every future channel representation of this source requires **its own applicable
Channel Accessibility Profile** and **its own revision-bound evidence**. Evidence
transfers in neither direction: source evidence never becomes channel evidence,
and channel evidence never becomes source evidence (evidence rule 3, DEC-S-052,
DEC-S-058, DEC-S-125).

## Relation to the other Semantic Status evidence packages

| Evidence ID | Bound source revision | Independent review | Admission state |
| --- | --- | --- | --- |
| `AE1-CDS-WP016-SEMSTATUS-002` | `semantic-status-rev-0001` | PASS | **Historically admitted — for `semantic-status-rev-0001` only** |
| `AE1-CDS-WP016-SEMSTATUS-003` | `semantic-status-rev-0002-candidate` | PASS WITH NOTES | **NOT ADMITTED** · `SUPERSEDED_FOR_ADMISSION_BY_EVIDENCE_INPUT_CHANGE` |
| `AE1-CDS-WP016-SEMSTATUS-004` | `semantic-status-rev-0002-candidate` | PASS WITH NOTES | **APPROVED / ADMITTED** (this record) |

`AE1-CDS-WP016-SEMSTATUS-002` remains admitted for `semantic-status-rev-0001` and
nothing else; it evidences the earlier bytes and does **not** transfer to the
Proposed Candidate. `AE1-CDS-WP016-SEMSTATUS-003` was **not** superseded by source
drift — the three evidenced source files are byte-identical across both packages
and the source revision is unchanged. It is superseded for admission purposes
only, because a bound evidence input changed after its evidence was generated.

`AE1-CDS-WP016-SEMSTATUS-004` inherits **no** review and **no** admission from
either package. **Evidence never transfers across a source revision**
(DEC-S-126).

The bytes of `AE1-CDS-WP016-SEMSTATUS-002`, `AE1-CDS-WP016-SEMSTATUS-003`, and
`AE1-CDS-WP016-SEMSTATUS-004` are **unmodified** by this record.

## Current authority state

### Current committed authoritative repository

| Item | Value |
| --- | --- |
| HEAD | `8d1374fa4c61cc1eed214823681ee1209a2d91f7` |
| **Source revision** | **`semantic-status-rev-0001`** |
| **Maturity** | **`Experimental`** |
| **Approval** | **`Unapproved`** |
| **Candidate** | **No** |
| Claims | **None** |
| Publication | `Private Development` |
| CoreOps pilot | inactive |
| CDS-WP-017 | **inactive** |

### Admitted Proposed Candidate

| Item | Value |
| --- | --- |
| Source revision | `semantic-status-rev-0002-candidate` |
| Source-declared TARGET maturity | `Candidate` |
| Source-declared TARGET approval | `Approved` |
| Authority context | `proposed-candidate` — caller-declared, never inferred from ambient Git state |
| **Authority before the Promotion Commit** | **NONE** |

**All other CDS artifacts remain AE-0** unless a separate authoritative admission
record exists for them. Two do: this record, and the
[`AE1-CDS-WP016-SEMSTATUS-002` admission](SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md)
for `semantic-status-rev-0001`. Both cover the same channel-independent
source/contract family and nothing else.

## Admission authority is not Candidate authority

**Human-Maintainer AE-1 admission ≠ Human-Maintainer Candidate approval ≠
Promotion Commit.** These are three separate acts, in a fixed order (DEC-S-126).

| # | Step | Authority | State |
| --- | --- | --- | --- |
| 1 | Proposed Candidate bytes prepared and enumerated | Executor | Complete |
| 2 | Fresh revision-bound AE-1 evidence produced | Executor | Complete |
| 3 | Fresh independent evidence review | Reviewer ≠ executor | Complete — **PASS WITH NOTES** |
| 4 | **Human-Maintainer evidence admission** | Human Maintainer | **APPROVED / ADMITTED — recorded here** |
| 5 | Nova Candidate Finalization Review | Nova | Complete — **GO WITH NOTES** (recommendation only) |
| 6 | **Human-Maintainer Candidate approval** | Human Maintainer | **`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`** — see the [Candidate Approval Record](../operations/SEMANTIC_STATUS_CANDIDATE_APPROVAL_RECORD.md) |
| 7 | **Human-Maintainer exact-byte Promotion Commit** | Human Maintainer | **PENDING** |
| 8 | Post-commit exact-byte Git-blob verification and full regression | Human Maintainer | **PENDING** |

This admission satisfies Candidate accessibility gate element **4 (AE-1)** for the
Proposed Candidate source revision. It satisfies **no other element**, and it does
not by itself make the repository Candidate. **The Promotion Commit is the actual
repository maturity transition point.**

## Invalidation — fail-closed

Any byte drift in the admitted Proposed Candidate source, or in any applicable
bound evidence input, **invalidates current admission eligibility for promotion**.

| Trigger | Effect |
| --- | --- |
| Any change to the three admitted Proposed Candidate source files | Current promotion eligibility ends. Fresh evidence, fresh independent review, and a fresh admission are required. |
| Any change to the bound transition-safe test file | Re-evidence required — the same rule that produced `AE1-CDS-WP016-SEMSTATUS-004` from `AE1-CDS-WP016-SEMSTATUS-003`. |
| Any change to the evidence runner, the evidence fixtures, or a bound validator module | Re-evidence required. |
| Any change to `requirements-validator.lock` | Re-evidence required. |
| Any change to the Foundation contract, vocabulary, composition rules, communication contract, or DE/EN terminology | Re-evidence required. |
| A source revision change | Evidence never transfers; a new revision needs its own evidence, review, and admission. |
| A11Y-BL-001 freshness ceasing to be `Current` | The evidence is no longer current and passes no gate. |
| An invalidating Blocking or High accessibility defect | Admission eligibility ends pending re-assessment. |
| Any attempt to reuse this source evidence as channel evidence | Rejected — evidence transfers in neither direction. |

**There is no "small fix" exemption.** A whitespace change, a reordering, and a
trailing-newline change all count, because the exact-byte binding is the entire
mechanism.

The historical fact of this admission remains a historical fact. **Current
promotion eligibility does not survive changed bytes automatically.** Regression
trigger **T-12 is not waived**.

## Related documents

- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) — normative evidence levels and gates
- [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md) — normative Candidate gate, Proposed Candidate Revisions, Promotion Commit effectivity
- [Semantic Status AE-1 Admission Record](SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md) — the separate `AE1-CDS-WP016-SEMSTATUS-002` admission, `semantic-status-rev-0001` scope only
- [Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md) — A11Y-BL-001
- [Candidate accessibility limitations](SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md) — 16 recorded, 0 Critical
- [AE1-004 Evidence Record](../operations/SEMANTIC_STATUS_CANDIDATE_AE1_004_EVIDENCE_RECORD.md) — the admitted package's human-readable record
- [Candidate Finalization Evidence Review Provenance](../reviews/WP016_CANDIDATE_FINALIZATION_EVIDENCE_REVIEW_PROVENANCE.md) — the two completed independent review events
- [Semantic Status Candidate Approval Record](../operations/SEMANTIC_STATUS_CANDIDATE_APPROVAL_RECORD.md) — the separate Candidate decision instrument
- [Semantic Status Candidate Dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md)
- [Decision Index](../decisions/DECISION_INDEX.md) — DEC-S-125, DEC-S-126
- [Risk Register](../risks/RISK_REGISTER.md) — RISK-098
