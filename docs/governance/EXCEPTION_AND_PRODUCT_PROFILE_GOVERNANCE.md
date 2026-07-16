# Exception and Product Profile Governance

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-006
- **Date:** 2026-07-16
- **Status:** **Normative** for exceptions and Product Profiles

## Purpose

Governs the two mechanisms by which CDS permits legitimate divergence — and
prevents both from becoming invisible forks.

Operationalizes DEC-S-025 (profiles are bounded) and DEC-S-026 (existing designs
are reconciled) into approval processes.

Frame: [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md).
Architecture: [Product Profile and Extension Model](../architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md).

---

# Part 1 — Exception Governance

## What an exception is

A **Local Exception** is a bounded, recorded, owned, expiring deviation from a
CDS contract.

It is **tracked debt**, not a contract amendment. An exception does not change
CDS; it records that a consumer is knowingly outside it, with a plan.

## Required fields

*(Normative, DEC-S-042 — all mandatory)*

| # | Field |
| --- | --- |
| 1 | Exception ID |
| 2 | Affected CDS version or revision |
| 3 | Consumer |
| 4 | Scope |
| 5 | Reason |
| 6 | Owner |
| 7 | Risk assessment |
| 8 | Affected contracts |
| 9 | **Impact on accessibility and status truth** |
| 10 | Start |
| 11 | **Review or expiry point** |
| 12 | Migration or acceptance path |
| 13 | Approval state |

Fields 11 and 12 are what separate an exception from a fork. **An exception
without an expiry and a path is an undocumented fork wearing a label.**

## Exception statuses

*(Normative — exactly six)*

| Status | Meaning |
| --- | --- |
| **Proposed** | Requested; not approved. Not yet valid. |
| **Approved** | Human Maintainer approved; not yet in force. |
| **Active** | In force, within its bounds. |
| **Expired** | Passed its point without renewal. **No longer covered.** |
| **Superseded** | Replaced by another exception or a CDS change. |
| **Closed** | Resolved — migrated, accepted into CDS, or no longer needed. |

`Expired` is a real state with real consequences: an expired exception is not a
grandfathered permission. It is an **uncovered deviation** and must be treated as
one.

## Exception rules

*(Normative)*

1. **No silent exception.** Unrecorded divergence is a fork (DEC-S-042).
2. **No indefinite exception without renewed approval.** Expiry forces a decision.
3. **Exceptions never extend CDS.** An exception is not a precedent, and citing
   one is not an argument.
4. **Recurring exceptions trigger a CDS gap review.** If several consumers need
   the same exception, the core is wrong — fix the core (RISK-035).
5. **An exception must not distort shared semantics or status truth.** The
   Unknown invariant (DEC-S-028) is not exceptable.
6. **Accessibility weakening is not approvable through a normal exception.**

### The accessibility limit

*(Normative — explicit)*

**A normal exception may never weaken accessibility.** Not "requires stronger
review" — **not approvable through this mechanism at all**.

*(Reconciled by CDS-WP-007)*

This rule was written while the accessibility target was still undefined, to
protect a requirement whose value was unknown. **The target now exists** —
**WCAG 2.2 Level AA** for the applicable web scope (CR-024, DEC-S-049,
DEC-S-060) — and the prohibition is **unchanged and now concrete**: it protects a
requirement whose value is known.

The binding statement, the prohibited waivers, and the rule that **missing
capacity is never a conformance rationale** are held by the
[Accessibility Limitations and Exception Policy](ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md)
(DEC-S-059), which is normative for this limit.

If a real case demands it, it requires an explicit, separately governed decision
by the Human Maintainer under that policy — **never this route**.

## Exception lifecycle

```
Proposed → risk assessment → Nova review → Human Maintainer approval
   → Approved → Active
      → review/expiry point reached
         ├→ renewed (requires re-approval) → Active
         ├→ migrated → Closed
         ├→ accepted into CDS (via contribution) → Superseded
         └→ lapsed → Expired  ← uncovered deviation
```

**No exception is created in this work package.**

---

# Part 2 — Product Profile Governance

## What a Product Profile is

A **separately governed, version-bound CDS artifact** expressing approved
product-specific variation at named extension points.

A profile is **part of CDS** — governed, versioned, and approved. This
distinguishes it from a Consumer Extension, which is consumer-owned.

## Required elements

*(Normative, DEC-S-043 — all mandatory)*

| # | Element |
| --- | --- |
| 1 | Unambiguous scope |
| 2 | Responsible owner |
| 3 | Associated CDS version or revision |
| 4 | **Named extension points** |
| 5 | Profile-specific normative sources |
| 6 | Compatibility declaration |
| 7 | **Scope-appropriate accessibility evidence** per the [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) |
| 8 | **Anti-fragmentation review** |
| 9 | Migration information |
| 10 | Consumer validation |
| 11 | Maturity state |
| 12 | Human Maintainer approval |

Element 4 is the boundary: a profile that cannot name the points it touches is
not scoped.

Element 7 **still cannot be satisfied** — so **no Product Profile can be approved
today**. *(Reconciled by CDS-WP-007: the obstacle is no longer a missing target
but missing evidence. Every artifact is **AE-0** and no support baseline is
declared — DEC-S-050, RISK-048.)* This is recorded, not worked around.

## Profile rules

*(Normative, DEC-S-025, DEC-S-043)*

A Product Profile **may not**:

| Prohibition | Why |
| --- | --- |
| Redefine shared semantics | Destroys the common meaning that makes CDS a system |
| **Weaken accessibility** | Invariant 10 |
| **Alter status truth** | Unknown must never read as healthy (DEC-S-028) |
| Break consumer contracts | Contracts are the interface |
| Use unnamed extension points | Unnamed means unapproved |

**A profile exceeding these bounds is a fork and must be treated as one.** Naming
it honestly is the correct outcome — an honest fork is manageable; a profile
pretending not to be one is not (RISK-027).

### No retrospective legitimation

*(Normative — the rule that matters most here)*

**A Product Profile is not retrospective legitimation of an existing consumer
design.**

SpeakCore and CastCore already hold their own style direction, palette, and token
sets (CR-002, CR-037). Those are **Consumer-local Artifacts** — not profiles, not
defects, and not CDS.

Consumer-local design **stays consumer-local** until it has been reconciled and
explicitly accepted (DEC-S-026). Labelling existing work a "Product Profile" to
make it look governed is exactly RISK-036, and it is prohibited.

## Anti-fragmentation review

*(Normative — required for every profile)*

Must establish:

1. Which extension points are touched, and are all approved?
2. Is shared semantics preserved?
3. Are accessibility guarantees preserved?
4. Is status truth preserved?
5. Do other consumers need this? If so, it may be a **core gap**, not a profile.
6. Could this be an **additive extension** instead? Additive is preferred.
7. What is the cumulative profile and exception load (RISK-021, RISK-027)?

Question 5 is the important one: **repeated profile requests for the same thing
mean the core is wrong.**

## Existing-product reconciliation

Governed by DEC-S-026; architecture in the
[Product Profile and Extension Model](../architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md).

Governance additions:

- Reconciliation is an **Elevated Track** activity.
- Each outcome — Profile Candidate, Consumer-local Retention, Migration Candidate
  — requires an explicit recorded decision.
- **Consumer-local Retention is a valid final outcome**, not a failure to
  converge.
- No automatic adoption, no automatic overwrite, no retrospective conformance.
- Mapping is **semantic, not value-level**.
- **No concrete consumer values are evaluated** in this work package.

**No Product Profile is approved in this work package.**

## Related documents

- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
- [Contribution and Acceptance Model](CONTRIBUTION_AND_ACCEPTANCE_MODEL.md)
- [Adoption, Conformance and Claims Policy](ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md)
- [Product Profile and Extension Model](../architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md)
- [Consumer Contract and Reconciliation Model](../architecture/CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md)
