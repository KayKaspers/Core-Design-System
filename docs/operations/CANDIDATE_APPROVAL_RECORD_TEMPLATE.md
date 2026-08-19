# Candidate Approval Record Template

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Finalization Governance Rework
- **Date:** 2026-08-18
- **Status:** **Template. Non-normative operating instrument.**
- **Authorized by:** DEC-S-126 (Human-Maintainer authorization 2026-08-18)

## This document is a template

**This file is an empty form. It records nothing and approves nothing.**

| This document is **not** | Why the distinction matters |
| --- | --- |
| A Candidate approval | No Human Maintainer has decided anything here. |
| A concrete Semantic Status Candidate Approval Record | No instance of this template exists anywhere in the repository. |
| Evidence | It is a decision instrument; evidence is produced, reviewed, and admitted elsewhere. |
| A maturity change | Nothing in CDS changes maturity because this template exists. |
| A promotion | Promotion happens only at a Human-Maintainer exact-byte Promotion Commit. |
| A claim, conformance, or release statement | None of those is created here, or valid today for anyone. |

**Current CDS state, unchanged by this template:** Candidate **No** · maturity
**Experimental** · approval **Unapproved** · authoritative Semantic Status source
revision **`semantic-status-rev-0001`** · claims **none** · publication
**`Private Development`** · CDS-WP-017 **not activated**.

Instantiating this template is a **future, separately authorized act**. An
instance may be created only at the Candidate finalization authority step defined
by DEC-S-126, after fresh revision-bound AE-1 evidence, a fresh independent
evidence review, a Human-Maintainer AE-1 admission, and a Nova Candidate
finalization review.

Frame: [Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md) ·
[Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) ·
[Governance Operating Model](../governance/GOVERNANCE_OPERATING_MODEL.md).

## How to use the form

1. Copy this file to a new record path and give it a Record ID.
2. Fill every field. **An unfilled field is an open field, never an implied
   pass.** `Not tested`, `Not reviewed`, and `Not decided` may never be read as
   satisfied.
3. Fill sections 1 to 6 **before** the Human-Maintainer decision in section 7.
4. Leave section 9 (Integration) pending until the Human Maintainer has performed
   the Promotion Commit; complete it afterwards **without mutating the evidenced
   source bytes**.
5. If any check in section 10 fails, the record is invalidated — do not repair it
   in place.

---

## 1. Identity

| Field | Value |
| --- | --- |
| Record ID | *(e.g. `CAR-CDS-<WP>-<ARTIFACT>-<NNN>`)* |
| Work package | |
| Artifact | |
| Artifact class | *(e.g. channel-independent Layer-3 Semantic Source / Contract family)* |
| Source set | |
| Proposed Candidate source revision | *(the reserved identity; not current until integrated)* |
| Authoritative pre-promotion baseline | *(repository revision the proposed bytes are based on)* |
| Authoritative pre-promotion source revision | *(what the repository still asserts today)* |
| Record date | |

## 2. Candidate bytes identity

*(The exact bytes being approved. If this section cannot be filled precisely, the
approval has no defined subject and must not be granted.)*

| Field | Value |
| --- | --- |
| Exact Candidate file scope | *(complete enumerated path list — no wildcards)* |
| Raw SHA-256 per path | *(one entry per path above)* |
| Manifest byte length | |
| Manifest entry count | |
| Canonical digest identity where applicable | *(RFC 8785 + SHA-256, ADR-0002)* |
| Canonicalization method | |
| Digest algorithm | |
| Transformation / tooling revision where applicable | |
| Digest boundary | A digest is an integrity aid. It is **not** a signature and proves no authorship, approval, authenticity, or release (DEC-S-100, RISK-072). |

## 3. Evidence

| Field | Value |
| --- | --- |
| Evidence ID | |
| Evidence level | |
| Evidence type | |
| Evidence source revision | *(must equal the Proposed Candidate source revision above)* |
| Evidence base repository revision | |
| Evidence execution state | *(clean · proposed-candidate worktree · other, stated exactly)* |
| Evidence result | |
| Runner / tooling revision | |
| Deterministic execution identity | |
| Independent Evidence Review result | *(reviewer ≠ executor, DEC-S-045)* |
| Independent Evidence Review date | |
| Evidence limitations | *(enumerated; an empty list is a finding, not a pass)* |
| Evidence Admission state | |
| Evidence Admission decision date | |
| Evidence Admission authority | *(Human Maintainer only)* |

**Prior-revision evidence does not transfer** (DEC-S-052, DEC-S-126 §4). Evidence
admitted for an earlier source revision may not be cited here.

## 4. Candidate gate

| Field | Value |
| --- | --- |
| General Candidate Gate state | *(per the ten requirements of the Artifact Maturity Lifecycle)* |
| Accessibility Candidate Gate state | *(per the nine requirements of the Accessibility Evidence and Claims Model)* |
| Per-requirement table | *(reproduce both gates requirement by requirement; no aggregate)* |
| Unresolved blockers | |
| Unresolved limitations | |
| Critical limitations | *(any Critical limitation blocks approval)* |

**No aggregate score.** Gate states are reported requirement by requirement;
partial satisfaction is never averaged into a pass (evidence rules 6 and 7).

## 5. Nova review

| Field | Value |
| --- | --- |
| Nova Finalization Review result | |
| Date | |
| Notes | |

Unclear readiness resolves as **NO-GO**, never as "go with notes" (DEC-S-048).
A Nova GO is a recommendation, never an approval.

## 6. Preconditions confirmed

| # | Precondition | Confirmed |
| --- | --- | --- |
| 1 | Proposed Candidate bytes prepared and enumerated (section 2) | |
| 2 | Fresh revision-bound evidence produced (section 3) | |
| 3 | Fresh independent evidence review completed (section 3) | |
| 4 | **Human-Maintainer evidence admission granted** (section 3) | |
| 5 | Nova Candidate finalization review completed (section 5) | |

**Steps 1 to 5 must all be complete before section 7.** Evidence admission and
Candidate approval are separate Human-Maintainer decisions, and **admission must
precede approval** (DEC-S-126 §8).

## 7. Human-Maintainer Candidate decision

*(Only the Human Maintainer may complete this section.)*

| Field | Value |
| --- | --- |
| Decision | *(one of the states below)* |
| Decision date | |
| Deciding authority | Human Maintainer |
| Rationale | |
| Conditions | |

### Allowed decision states

| State | Meaning |
| --- | --- |
| **`NOT_DECIDED`** | No Candidate decision has been made. The default; also the correct state whenever any precondition in section 6 is open. |
| **`NOT_APPROVED`** | The Human Maintainer examined the package and declined. The artifact stays Experimental and Unapproved. |
| **`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`** | The Human Maintainer approves **these exact bytes** for Candidate, conditional on their unmodified integration. **The repository is not Candidate while this state holds.** |

No other decision state exists, and **no state in this record makes the
repository Candidate**. A state that implied current Candidate maturity before
integration would be a false record and is deliberately not offered.

## 8. Effectivity

> **A Candidate Approval Record is not a Promotion Commit.**
>
> **Candidate maturity becomes effective in the repository only after the exact
> approved bytes have been successfully integrated by the Human Maintainer.**

Before integration, the authoritative repository state remains **Candidate: No ·
Maturity: Experimental · Approval: Unapproved**, whatever this record says and
whatever metadata the proposed bytes declare. The Promotion Commit is the actual
maturity transition point (DEC-S-126 §9).

## 9. Integration

*(Pending until the Human Maintainer performs the Promotion Commit. Completing
this section must not require any mutation of the evidenced source bytes.)*

| Field | Value |
| --- | --- |
| Promotion Commit | **pending** *(until integrated)* |
| Parent revision | |
| Exact-byte result | *(approved bytes vs. working-tree bytes)* |
| Staged blob result | *(approved bytes vs. staged blobs)* |
| Committed blob result | *(approved bytes vs. committed blobs)* |
| Source revision after integration | |
| Post-commit validation result | |
| Post-commit regression verification result | |
| Remote result | |
| Integration date | |

Where the committed source is byte-identical to the independently reviewed,
evidence-bound proposed source, the post-commit verification **confirms the same
evidence binding**. It does not by itself require another Evidence ID, another
independent evidence review, or another admission solely because Git persisted
already-reviewed exact bytes (DEC-S-126 §10).

## 10. Invalidation

Any mismatch between the approved, reviewed, and evidenced Candidate bytes and
the integrated source **invalidates**
`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`.

On any such mismatch:

1. The approval no longer covers the integrated content. Do not amend this
   record to fit the new bytes.
2. Fresh evidence is required for the changed bytes.
3. A fresh independent evidence review is required.
4. A fresh Human-Maintainer evidence admission is required.
5. A fresh Candidate approval is required, recorded in a new instance.

**There is no "small fix" exemption** (DEC-S-126 §7). This applies equally to a
whitespace change, a reordering, a trailing-newline change, and a correction the
executor believes to be harmless.

## 11. Boundaries

A completed instance of this record establishes **none** of the following:

Stable status · any claim of any level · conformance of any kind · channel
evidence · consumer evidence · assistive-technology support · a Product Profile ·
a CoreOps or other consumer pilot · CDS-WP-017 activation · a licence selection ·
a publication, release, or tag.

Candidate is bounded validation only, and is never normative
([Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md)).
`CDS certified` is prohibited; no certification programme exists (DEC-S-044).

## Related documents

- [Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md) — normative
- [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) — normative
- [Elevated Change Dossier Template](ELEVATED_CHANGE_DOSSIER_TEMPLATE.md)
- [Accessibility Evidence Record Template](ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md)
- [Semantic Status AE-1 Admission Record](../governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md) — the existing, separate admission instrument
- [Semantic Status Candidate Dossier](SEMANTIC_STATUS_CANDIDATE_DOSSIER.md)
- [Decision Index](../decisions/DECISION_INDEX.md) — DEC-S-126
- [Risk Register](../risks/RISK_REGISTER.md) — RISK-098
