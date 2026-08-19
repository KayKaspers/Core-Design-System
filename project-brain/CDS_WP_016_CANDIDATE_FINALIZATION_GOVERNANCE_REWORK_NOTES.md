# CDS-WP-016 — Candidate Finalization Governance Rework Notes

- **Project:** Core Design System (CDS)
- **Type:** Project-local working notes — **non-normative**
- **Date:** 2026-08-18
- **Scope:** Internal rework of CDS-WP-016. **Not a new work package.**

These notes record what was decided and why. They are **not** a decision record,
**not** evidence, and **not** an approval. The normative records are the
[Decision Index](../docs/decisions/DECISION_INDEX.md) (DEC-S-126) and the
[Risk Register](../docs/risks/RISK_REGISTER.md) (RISK-098).

## Baseline

| Item | Value |
| --- | --- |
| Repository | `D:\Projects\Core-Design-System` |
| Branch | `main` |
| HEAD | `42bcba65aa6767e3f7ebee2a01e496eafcc82a54` |
| Parent | `43a512892e148fc53a5f5bee522ef6c30d848f19` |
| HEAD subject | `docs(cds): reconcile WP-016 AE-1 admission governance` |
| Ahead / behind `origin/main` | 0 / 0 |
| Index · working tree · untracked | clean · clean · 0 |
| Active Git operation | none |

## Bootstrap assessment result

**`CANDIDATE_FINALIZATION_GOVERNANCE_REWORK_REQUIRED`**

A read-only Candidate Finalization Bootstrap Assessment established that the
remaining Candidate gate could not be entered without either an unevidenced
preparatory commit or an invalid evidence transfer.

### Key findings carried into this rework

| ID | Severity |
| --- | --- |
| **FIN-F-001** | **Blocking** |
| **FIN-F-002** | **Blocking** |
| **FIN-F-003** | High |
| **FIN-F-004** | Medium |
| **FIN-F-005** | Medium |

## Authorization

| Role | Act |
| --- | --- |
| **Human Maintainer** | Authorized the Candidate Finalization Governance Rework on **2026-08-18** as **internal rework of CDS-WP-016, not a new work package**. |
| **Nova** | Adjudicated the rework scope and authorized its content (below). |
| **Claude** | Implemented only the authorized scope. Created no authority. Performed no Git write. |

### Nova adjudication

- **DEC-S-126 authorized.**
- **Exact-byte variant α selected** as the transition mechanism.
- **RISK-098 authorized.**
- **Candidate Approval Record Template authorized.**
- **`semantic-status-rev-0002-candidate` reserved and authorized** as the intended
  future Candidate source revision identity.
- **A separate, new AE-1 admission is required before Candidate approval.**
- **The Promotion Commit remains the maturity transition point.**
- **Post-commit exact-byte and regression verification is required.**
- **No second AE cycle is required solely for bit-identical persistence** of
  already-reviewed exact bytes.

## The problem, in one paragraph

Candidate promotion requires the source bytes to declare `Candidate`/`Approved`
and a **new** immutable source revision. Changing the source revision invalidates
the revision-bound AE-1 admitted for `semantic-status-rev-0001` (DEC-S-052,
regression trigger T-12), so fresh AE-1 evidence is required **before** Candidate
approval — yet the Candidate-target metadata must already be present in the very
bytes that have to be evidenced. Read naively, the only entry to the gate is a
preparatory commit of an unevidenced, unapproved Candidate state, which the
governance model forbids.

## The resolution

The circularity comes from conflating **bytes** with **authority**. Bytes may be
prepared, digested, evidenced, and independently reviewed before anything is
authoritative; only integration by the Human Maintainer changes what the
repository asserts.

| Mechanism | Effect |
| --- | --- |
| **Proposed Candidate Revision** | A named, explicitly non-authoritative state. Its bytes may carry target metadata; the bytes are not authority. |
| **Exact-byte pre-commit evidence binding** | Evidence may be produced against the proposed bytes only when identity, revisions, paths, raw SHA-256, canonical digests, tooling revision, and determinism are all recorded. |
| **Exact-byte continuity** | Preserves an **identity**, never transfers an evidence result. Reviewed bytes = staged bytes = committed bytes, or the bridge does not exist. |
| **Byte-drift invalidation** | Any difference in the evidenced scope forces fresh evidence, review, and admission. **No "small fix" exemption.** |
| **Separate decisions** | AE-1 admission and Candidate approval are distinct Human-Maintainer acts, and admission precedes approval. |
| **Promotion Commit** | The actual repository maturity transition point. |

**No gate was waived, weakened, or removed.** Nothing is admitted earlier,
approved earlier, or promoted earlier than before.

## What was implemented

| # | Artifact | Kind |
| --- | --- | --- |
| 1 | **DEC-S-126** | New decision (Accepted, 2026-08-18) |
| 2 | **RISK-098** | New risk (`Mitigating`) |
| 3 | `docs/operations/CANDIDATE_APPROVAL_RECORD_TEMPLATE.md` | New **template** |
| 4 | Artifact Maturity Lifecycle | Narrow additive reconciliation |
| 5 | Accessibility Evidence and Claims Model | Narrow additive reconciliation |
| 6 | Semantic Status Token Contract | Narrow additive clarification |
| 7 | Machine-Readable Validation Contract | Narrow additive clarification |
| 8 | Offline Token Validator Usage | Narrow DEC-S-126 exception |
| 9 | Candidate Accessibility Regression Plan | T-12 clarification (**not waived**) |
| 10 | Evidence runner → result format **v2** | Test tooling |
| 11 | Evidence runner unit tests | Test tooling |
| 12 | Current-state mirrors | Reconciliation |

## What was explicitly **not** done

- **No source mutation.** The three productive Semantic Status source files are
  byte-identical to HEAD.
- **No `semantic-status-rev-0002-candidate` bytes were created.** The identity is
  reserved only.
- **No Candidate evidence** was produced, and no evidence artifact was written.
- **No Candidate Approval Record instance** was created — only the template.
- **No evidence admission**, **no Candidate approval**, **no Candidate promotion**.
- **No Stable**, **no claim**, **no conformance**, **no channel or consumer
  evidence**, **no Product Profile**, **no pilot**.
- **No ADR.** The range stays ADR-0001 … ADR-0003; this is authority sequencing,
  not an architecture or technology selection.
- **No CDS-WP-017 activation.**
- **No Git write by Claude** — no add, stage, commit, push, fetch, pull, merge,
  branch, or tag. The index stayed clean throughout.
- **No existing evidence artifact touched.** Evidence 001 and 002, and the AE-1
  Admission Record, are unchanged.

## State after the rework

| Item | Value |
| --- | --- |
| Decisions | **126** (max DEC-S-126) |
| Risks | **98** (max RISK-098) · 90 Monitored · 8 Mitigating · 0 Accepted · 0 Closed |
| ADRs | **3** |
| Authoritative source revision | **`semantic-status-rev-0001`** |
| Reserved future Candidate revision | `semantic-status-rev-0002-candidate` — **not created** |
| Candidate | **No** |
| Maturity | **Experimental** |
| Approval | **Unapproved** |
| Admitted accessibility evidence | `AE1-CDS-WP016-SEMSTATUS-002` — **AE-1**, source scope, rev-0001 only |
| Claims | **None** |
| Publication | `Private Development` |
| CoreOps pilot | inactive |
| CDS-WP-017 | inactive |
| Candidate finalization preparation | **not yet authorized** |

## Open items

1. **Fresh independent governance and tooling review** of this rework, in a
   separate session, by a reviewer who is not its executor.
2. Human-Maintainer decision on integrating the rework.
3. Only afterwards: the Nova post-admission Candidate Maturity Re-Review.
4. Candidate finalization preparation remains **unauthorized** until separately
   prompted.

## Related documents

- [Decision Index](../docs/decisions/DECISION_INDEX.md) — DEC-S-126
- [Risk Register](../docs/risks/RISK_REGISTER.md) — RISK-098
- [Candidate Approval Record Template](../docs/operations/CANDIDATE_APPROVAL_RECORD_TEMPLATE.md)
- [Artifact Maturity Lifecycle](../docs/governance/ARTIFACT_MATURITY_LIFECYCLE.md)
- [Accessibility Evidence and Claims Model](../docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Semantic Status AE-1 Admission Record](../docs/governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md)
- [Semantic Status Candidate Dossier](../docs/operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md)
- [First Semantic Status Candidate Plan](../docs/roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md)
