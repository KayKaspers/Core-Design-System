# Consumer Contract and Reconciliation Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-005 — Design System Architecture
- **Date:** 2026-07-16
- **Status:** **Normative** for the contract structure

## Purpose

This document defines the **logical interface between CDS and a consumer**: what
CDS owes, what the consumer owes, and what either may claim.

It gives DEC-S-008 (CDS owns shared design rules; consumers own their products) a
structure that survives contact with a real product.

Frame: [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md).

## The five contracts

*(Normative)*

| Contract | Question it answers |
| --- | --- |
| **Source Contract** | Which normative sources define an artifact state? |
| **Transformation Contract** | How is a generated artifact produced, and how is its origin provable? |
| **Distribution Contract** | How does a consumer obtain a defined CDS version? |
| **Integration Contract** | What does the consumer owe? |
| **Adoption Evidence Contract** | What is required before anything may be claimed? |

### Source Contract

Defines which **normative sources** (authority classes 1 and 2) constitute a
given artifact state.

- Names the normative sources and their revisions.
- States what is **not** covered.
- Human-readable sources define meaning; machine-readable sources define values
  (DEC-S-022).
- Generated artifacts, tool state, examples, and research are **not** part of the
  source contract (invariants 1–4).

### Transformation Contract

Defines how a normative source becomes a consumable artifact.

- Deterministic and reproducible: same source revision + same transformation
  revision = same output.
- Emits source revision, transformation revision, and output identity
  (DEC-S-031).
- Introduces no decision absent from the source.
- Preserves semantics — notably the separated status axes (DEC-S-028).
- An output without provable origin is a defect (RISK-025).

### Distribution Contract

Defines how a consumer obtains a defined CDS version or revision.

- The consumer **pins** to an identifiable version or revision. "Latest" is not a
  pin.
- Consumption requires **no mandatory external runtime service** (DEC-S-030,
  invariant 12).
- Artifacts are locally obtainable and usable, including air-gapped.
- **No distribution technology is selected** (DEC-S-032).

### Integration Contract

Defines **consumer obligations**:

| Obligation | Meaning |
| --- | --- |
| **Correct integration** | Use the artifact as its contract describes. |
| **No illegal overrides** | Only approved extension points (DEC-S-025). |
| **Preserve semantic meaning** | A consumer may restyle; it may not re-mean. Unknown stays unknown (invariant 7). |
| **Preserve accessibility requirements** | A consumer must not remove a guarantee (invariant 10). |
| **Document deviations** | Every divergence is recorded. Silent divergence is a fork. |
| **Name the pinned revision** | Required for any later claim. |

### Adoption Evidence Contract

Defines what is required **before an adoption or conformance claim is legitimate**
(DEC-S-012, DEC-S-017).

Required: a specific CDS version, a specific consumer revision, requirement
traceability, documented deviations, and — once CDS-WP-007 defines a target —
accessibility evidence.

**Until those exist, no adoption or conformance claim may be made by anyone**
(RISK-018). The pilot's existence or completion is not adoption (DEC-S-015).

## CDS obligations

*(Normative — the other half of the boundary)*

CDS owes its consumers:

1. **Identifiable revisions.** A consumer cannot pin to something CDS cannot
   name.
2. **Meaning, not just values.** Values without semantics force consumers to
   guess intent.
3. **Named, finite extension points.** Otherwise the only options are compliance
   or a fork.
4. **Honest maturity.** A consumer must be able to tell what is stable from what
   is not — model deferred to CDS-WP-006.
5. **Provenance.** Every artifact identifies its origin.
6. **Offline consumability.** No mandatory external runtime.
7. **A migration path.** Change is legitimate; changing without a path is not.
8. **Truthful semantics.** CDS must not ship a structure that makes unknown look
   healthy.
9. **Stated boundaries.** CDS must say what it does not do — the clearest
   practice found in the benchmark.

## Reconciliation flow

*(Normative, DEC-S-026)*

For consumers that already hold product-local design decisions — the actual case
for SpeakCore and CastCore (CR-002, CR-037).

```
Inventory
  → Semantic Mapping
     → Conflict Identification
        → Classification
           ├→ Product Profile Candidate
           ├→ Consumer-local Retention
           └→ Migration Candidate
              → Evidence and Review
```

| Step | Produces | Rule |
| --- | --- | --- |
| **Inventory** | What product-local decisions exist | Existence only; no judgement |
| **Semantic Mapping** | What each decision *means* in shared terms | **Semantic, never value-level** |
| **Conflict Identification** | Where meaning genuinely diverges | A different value is not a conflict; a different *meaning* is |
| **Classification** | One of the three outcomes | Explicit, recorded |
| **Product Profile Candidate** | Belongs in the family at an extension point | Requires approval (DEC-S-025) |
| **Consumer-local Retention** | Legitimately stays with the product | **A valid final outcome, not a failure** |
| **Migration Candidate** | Should converge over time | Requires a versioned, documented, reversibly planned path |
| **Evidence and Review** | Recorded outcome and rationale | Reviewable later |

### Reconciliation rules

- No automatic adoption, no automatic overwrite, no retrospective conformance
  (invariant 14).
- **No evaluation of concrete consumer values in this work package.**
- Product-local decisions may legitimately persist.
- Reusable insight requires explicit acceptance (DEC-S-016) — presence in a
  consumer is never sufficient.
- Migration must be versioned, documented, and reversibly plannable.
- Forcing convergence without migration and evidence is RISK-022.

## Exception boundary

A **Local Exception** is a bounded, recorded deviation carrying reason, owner,
scope, affected CDS version, review or expiry point, and a migration or
acceptance decision.

An exception is **not** a contract amendment. It is a tracked debt with an expiry.
An exception without an expiry is an undocumented fork.

Detailed exception governance: **CDS-WP-006**.

## Migration direction

*(Normative direction; no model)*

- Migration is **planned, versioned, and documented** — never implicit.
- A consumer must be able to know what changes, why, and what it costs.
- Reversibility must be *plannable*: a migration nobody can back out of is a
  one-way door and must be recognised as such before it is opened.
- Breaking changes are contract events, governed in CDS-WP-006.
- **No migration model, versioning scheme, or compatibility policy is set here.**

## CoreOps pilot relationship

The [CoreOps Pilot Contract](../governance/COREOPS_PILOT_CONTRACT.md) is the
**first instance** of this contract structure — not a special case.

- The pilot is a bounded slice; it is not adoption or conformance (DEC-S-015).
- Its entry criteria include **approved CDS-WP-005 architecture** — this work
  package supplies that input, and the Human Maintainer supplies the approval.
- Pilot outcomes are evaluated through version-bound evidence (DEC-S-017), which
  is the Adoption Evidence Contract applied.
- CoreOps-specific results become shared only through the gate (DEC-S-016).
- **This architecture does not start the pilot.** Entry criteria remain unmet:
  the architecture needs approval, no maturity model exists, and the accessibility
  target is undefined (CR-024).

Secondary consumers hold evidence value, not pilot authority (DEC-S-018).

## CDS-WP-006 dependencies

Deferred, and required before any contract can be operated:

- the versioning scheme that gives "revision" a concrete meaning,
- the compatibility model that makes pinning safe,
- maturity states that make "stable" checkable,
- deprecation policy,
- which extension points are approved, and who approves them,
- exception governance and expiry,
- conformance criteria and adoption levels,
- the evidence model behind the Adoption Evidence Contract,
- contribution and acceptance process,
- licensing and publication decision model.

**Deferred to CDS-WP-007:** the accessibility target the Integration Contract
requires a consumer to preserve. The obligation exists architecturally; its value
is unknown (CR-024, RISK-028).

Until these exist, the contracts are **structure without settled policy**. They
define the shape of the agreement, not its terms.

## Related documents

- [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md)
- [Product Profile and Extension Model](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md)
- [Artifact Distribution and Channel Model](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md)
- [Evidence, Traceability and Status Semantics](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md)
- [CoreOps Pilot Contract](../governance/COREOPS_PILOT_CONTRACT.md)
- [Consumer Requirements Model](../governance/CONSUMER_REQUIREMENTS_MODEL.md)
