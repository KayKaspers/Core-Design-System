# Semantic Status — AE-1 Admission Record

- **Status:** **Authoritative for the fact and scope of this specific
  Human-Maintainer AE-1 admission.**
- **Record type:** Governance authority record — **not evidence**.
- **Created:** 2026-08-17, during the CDS-WP-016 AE-1 Admission and Governance
  Reconciliation.

## What this record is, and is not

This record documents that a Human-Maintainer admission decision **was made**, and
states its exact scope. It executes existing governance under the
[Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md);
it creates no new policy and no new Decision ID.

**This record is not:**

| Not | Why it matters |
| --- | --- |
| Evidence | The evidence is the admitted package itself; this record only admits it. |
| A new evidence level | AE-0 … AE-4 are unchanged. |
| A general policy | It governs one artifact family, one revision, one package. |
| Candidate status | Candidate remains **No**. |
| Stable status | Stable is unreachable; no AE-2, AE-3, or AE-4 exists. |
| An accessibility claim | No claim of any level is valid, for anyone, including CDS. |
| WCAG conformance | Nothing here demonstrates any WCAG success criterion. |
| A channel claim | No channel evidence exists. |
| Consumer evidence | No consumer has been evaluated. |

## Admission identity

| Item | Value |
| --- | --- |
| **Artifact** | Semantic Status Foundation |
| **Artifact class** | Channel-independent Layer-3 Semantic Source / Contract family |
| **Source set** | `semantic/status` |
| **Source revision** | `semantic-status-rev-0001` |
| **Admitted evidence** | `AE1-CDS-WP016-SEMSTATUS-002` |
| **Admitted level** | **AE-1** |
| **Evidence type** | Structural and Automated Evidence |
| **Evidenced implementation revision** | `e6cb6fae63b1548ce4dabb7f5548116e4c61d622` |
| **Evidence integration revision** | `43a512892e148fc53a5f5bee522ef6c30d848f19` |
| **Evidence execution worktree state** | clean |
| **Evidence result** | Pass with limitations |
| **Fresh independent evidence review** | **PASS** |
| **Nova admission recommendation** | GO — AE-1 admission recommended |
| **Human-Maintainer admission decision** | **APPROVED / ADMITTED** |
| **Admission date** | 2026-08-17 |

## Governance state after this admission

| Item | Value |
| --- | --- |
| Candidate | **No** |
| Maturity | **Experimental** |
| Artifact approval | **Unapproved** |
| Claims | **None** |
| Publication | `Private Development` |
| CoreOps pilot | inactive |
| CDS-WP-017 | not activated |

**All other CDS artifacts remain AE-0** unless a separate authoritative admission
record exists for them. None does.

## Admission authority is not Candidate authority

**Human-Maintainer AE-1 admission approval ≠ Human-Maintainer Candidate approval.**
They are separate decisions with separate scopes.

This admission satisfies Candidate accessibility gate element **4 (AE-1)**. It does
**not** satisfy element **9 — Human-Maintainer Candidate approval after Nova
review**, which remains **open**.

The next authority steps, in order:

1. **Nova post-admission Candidate Maturity Re-Review** — not yet performed.
2. Only if that returns GO: a **separate Human-Maintainer Candidate decision** —
   not granted.

Until both complete, the artifact remains **Experimental**, **Unapproved**, and
**not Candidate**.

## Scope boundary

The admitted AE-1 applies **only** to the channel-independent source/contract scope.
It establishes **none** of the following:

rendering behaviour · interaction behaviour · keyboard accessibility · focus
behaviour · screen-reader behaviour · assistive-technology support · browser
behaviour · platform support · visual contrast · non-textual meaning behaviour ·
component accessibility · pattern accessibility · consumer composition · complete
processes · product accessibility · CoreOps accessibility · any claim · any
conformance state.

**No baseline environment was exercised.** The evidence references A11Y-BL-001 as its
test contract without testing in any environment listed there, so **no environment is
supported** and no support claim exists (DEC-S-069).

Every future channel representation requires **its own applicable Channel
Accessibility Profile** and **its own revision-bound evidence**. **Evidence transfers
in neither direction** — source evidence never becomes channel evidence, and channel
evidence never becomes source evidence. DEC-S-125 and DEC-S-058 are preserved in
full.

## Revision binding

Three revisions are distinct and must not be conflated:

| Role | Revision |
| --- | --- |
| **Source revision** — what the contract says | `semantic-status-rev-0001` |
| **Evidenced implementation revision** — what the evidence runner actually executed against | `e6cb6fae63b1548ce4dabb7f5548116e4c61d622` |
| **Evidence integration revision** — the repository commit that added the evidence package | `43a512892e148fc53a5f5bee522ef6c30d848f19` |

The evidence was executed against the exact bytes of `e6cb6fa`. Later
governance-only or evidence-integration commits **do not** rebind that run to a newer
repository SHA, and do not extend the admission to changed source or contract bytes.

## Re-evidence and expiry triggers

This admission does not silently carry forward. Fresh evidence and a fresh
independent review are required if any of the following occurs:

1. the `semantic/status` source revision changes;
2. any evidenced status value changes;
3. a status technical identifier changes;
4. the Semantic Status Foundation contract semantics change;
5. the combination, fail-closed, or review-required rules change;
6. the terminology structure changes within the evidenced scope;
7. the relevant accessibility baseline evidence ceases to be `Current`;
8. an invalidating Blocking or High accessibility defect is discovered;
9. any future representation attempts to reuse this source evidence as channel
   evidence.

Historical evidence remains valid **as history**. Current gate eligibility does not
automatically survive a change to the evidenced subject.

## Related documents

- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) — normative evidence levels and gates
- [Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md) — A11Y-BL-001
- [Semantic Status Candidate Dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md)
- [Clean Re-execution Evidence Record](../operations/SEMANTIC_STATUS_CANDIDATE_AE1_CLEAN_REEXECUTION_EVIDENCE_RECORD.md) — the admitted package (immutable)
- [Review Provenance Record](../reviews/WP016_ACCESSIBILITY_REMEDIATION_REVIEW_PROVENANCE.md)
- [Decision Index](../decisions/DECISION_INDEX.md) — DEC-S-125
