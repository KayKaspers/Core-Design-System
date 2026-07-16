# Source Conflict Resolution Policy

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-006
- **Date:** 2026-07-16
- **Status:** **Normative** for conflicts between normative sources

## Purpose

CDS-WP-005 established *that* conflicts fail closed (DEC-S-023). This document
establishes **what actually happens** when they do.

It operationalizes DEC-S-022 and DEC-S-023 and adds the rule those decisions
deliberately left open: **neither normative source wins automatically**
(DEC-S-034).

Frame: [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md).
Architecture: [Source of Truth and Authority Model](../architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md).

## Normative source classes

*(Normative, DEC-S-022)*

Only two classes are normative. Each owns a distinct question.

### Human-readable normative source

**Governs:** intent · meaning · permitted use · boundaries · governance ·
accessibility obligations.

It answers *what this is for and what it means*.

### Machine-readable normative source

**Governs:** approved values · relationships · alias structures · metadata ·
profile and channel assignment.

It answers *what the approved values and relationships are*.

### The boundary

The classes must not overlap. A machine-readable source carrying meaning, or a
human-readable source carrying authoritative values, **is itself the defect** —
it manufactures the ambiguity this policy then has to resolve (RISK-020).

Every other artifact class — generated, tool representation, reference
implementation, evidence, consumer-local, research, example — is **not
normative** and cannot participate in a conflict as an authority. Its
disagreement with a normative source is a defect in the artifact, not a conflict.

## The conflict rule

*(Normative, DEC-S-034)*

> **No normative source has blanket precedence across all conflicts.**

Intent without approved values is unimplementable. Approved values without intent
are meaningless. Neither is subordinate, so neither can be the automatic winner —
and a policy that picked one would simply be discarding half the truth.

Instead: **a conflict invalidates the affected artifact state** until a
controlled decision restores consistency.

## Conflict types

| # | Type | Nature |
| --- | --- | --- |
| 1 | **Meaning vs values** | Human-readable intent contradicts machine-readable values. The core case. |
| 2 | **Intra-class** | Two human-readable sources, or two machine-readable sources, disagree. |
| 3 | **Coverage gap** | Neither source covers a case both are assumed to. |
| 4 | **Stale derivative** | A generated artifact contradicts its source. *Not a conflict* — the artifact is wrong. |
| 5 | **Tool divergence** | Design-tool state contradicts a source. *Not a conflict* — the tool is a working surface. |
| 6 | **Implementation gap** | An implementation needs something the contract lacks. *Not a conflict* — a contract gap to raise. |
| 7 | **Evidence contradiction** | Evidence shows a source is wrong in practice. *Not a conflict* — a trigger for a decision. |
| 8 | **Consumer divergence** | A consumer artifact differs. *Not a conflict* — different ownership. |

**Only types 1–3 are conflicts.** Types 4–8 have a determinate answer already and
must not be escalated as if they were undecidable — treating them as conflicts
would make the process unusable.

## Conflict states

*(Normative)*

| State | Meaning | Releasable? |
| --- | --- | --- |
| **Consistent** | No known conflict | Yes |
| **Suspected** | A conflict is reported, not confirmed | **No** |
| **Confirmed** | A conflict exists in a normative source set | **No** |
| **Under Resolution** | A controlled decision is in progress | **No** |
| **Resolved** | Sources reconciled, validation and evidence renewed | Yes |

`Suspected` blocks. A suspected conflict that is later disproven costs a review;
a suspected conflict that is shipped costs a contradiction in a consumer's
product.

## Fail-closed procedure

*(Normative — the eight-step sequence)*

1. **Mark the affected artifact state not releasable.**
2. **Stop transformation and distribution** for that state, fail closed.
3. **Register the conflict as a deviation** (Layer 8) with scope, sources, and
   discoverer.
4. **Examine normative intent and machine-readable representation** — which is
   wrong, or are both?
5. **A controlled decision determines the correction.** Nova reviews; the Human
   Maintainer decides.
6. **Re-synchronize both normative sources.**
7. **Renew validation and evidence.**
8. **Only then** may the state be approved or distributed.

Steps 1–2 happen immediately on `Suspected` — before diagnosis. Blocking is not
the conclusion of the investigation; it is the precondition for it.

## Prohibited automatic precedence

*(Normative — none of these may ever resolve a conflict)*

| Forbidden rule | Why |
| --- | --- |
| **Recency wins** | The silent default of nearly every tool and merge strategy. A system resolving design conflicts by timestamp has a race condition, not an authority model. |
| **Design tool wins** | Would make a proprietary tool the source of truth (DEC-S-004). |
| **Generated output wins** | Inverts the derivation direction entirely. |
| **Implementation wins** | Rewards whoever built first. |
| **Consumer usage wins** | Popularity is not correctness (DEC-S-041). |
| **Silent overwrite** | Removes the conflict without deciding it — the worst outcome, because the loss is invisible. |
| **Convenience wins** | Whichever is easier to edit is not an argument. |
| **Automatic resolution** | No process may close a normative conflict without a human decision. |

## Deviation registration

Every confirmed conflict is recorded with: identity · affected sources and
revisions · scope · discovery context · conflict state · blocked artifacts ·
owner · resolution decision · resolution evidence · closure approval.

An unrecorded conflict is indistinguishable from a decision nobody made.

## Resolution flow

```
Suspected → block → register deviation
   → diagnose (intent vs representation)
      → controlled decision (Nova reviews, Human Maintainer decides)
         → correct the wrong source
            → re-synchronize both sources
               → revalidate
                  → renew evidence
                     → approve
                        → Resolved
```

Possible corrections: the human-readable source was wrong (intent was
mis-stated) · the machine-readable source was wrong (values drifted) · **both
were wrong** (a real coverage gap) · the apparent conflict was a class-boundary
violation, and the fix is to restore the boundary.

The last is the one worth naming: recurring type-1 conflicts usually mean meaning
and values have started to overlap. Repeated conflict is a **structural signal**,
not a run of bad luck.

## Revalidation

Before a `Resolved` state is releasable:

- both normative sources are consistent,
- affected generated artifacts are **regenerated, never patched**,
- token and structural validations re-run,
- affected evidence is renewed — evidence collected against a contradictory state
  proves nothing,
- affected claims are re-assessed (DEC-S-044),
- the deviation record is closed with rationale.

## Approval and closure

Closure requires: the corrective decision recorded · both sources re-synchronized
· revalidation complete · renewed evidence · **Nova review** · **Human Maintainer
approval**.

Claude may propose and document. Claude may **not** close a conflict.

## Related documents

- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
- [Source of Truth and Authority Model](../architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)
- [Release and Change Control Policy](RELEASE_AND_CHANGE_CONTROL_POLICY.md)
- [Risk Governance Model](RISK_GOVERNANCE_MODEL.md) — RISK-020
