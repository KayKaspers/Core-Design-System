# Source of Truth and Authority Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-005 — Design System Architecture
- **Date:** 2026-07-16
- **Status:** **Normative** for artifact classes and authority

## Purpose

This document answers one question precisely: **when two artifacts disagree,
which one is right?**

It exists because the benchmark found that tool coupling in token workflows is
common, largely undocumented, and not presented as a risk by the systems that
have it — and because no reviewed system documented tool-independence as an
explicit goal. CDS makes the opposite choice explicit (DEC-S-004, RISK-004).

Frame: [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md).

## Artifact classes

*(Normative, DEC-S-022)*

Every artifact in or around CDS belongs to exactly one class. The class
determines its authority.

### 1. Normative Human-readable Source

**Authority: highest. Defines meaning.**

Defines intent, meaning, governance, usage rules, boundaries, accessibility
requirements, and change control.

This class exists because meaning must be reviewable by a human without a tool.
If intent lives only in a machine format, it cannot be argued with.

### 2. Normative Machine-readable Source

**Authority: high, bounded. Defines approved values.**

Will later define approved values, semantic relationships, metadata, alias
relationships, and platform or profile assignment.

Bounded: it holds *what the values are*, never *what they mean*. Meaning stays in
class 1. **No format is selected** (DEC-S-032).

### 3. Generated Artifact

**Authority: none. Derived only.**

Produced deterministically from normative sources.

- **Never an independent normative source** (invariant 1).
- Must not contradict its source.
- Manual edits are invalid. A manual edit is either discarded or reconciled back
  into the normative source — it never stands.
- Must identify its source and transformation revision (DEC-S-031).

### 4. Reference Implementation

**Authority: none over the contract. Demonstrates it.**

Shows correct use of a CDS contract.

- Not automatically the only permitted implementation.
- Must not extend a norm on its own authority. If it needs something the contract
  lacks, that is a contract gap to raise — not a licence to invent.

### 5. Authoring and Design-tool Representation

**Authority: none. Working surface only.**

Serves creation, visualization, and collaboration.

- **Must not become the sole truth** (invariant 4, DEC-S-004).
- Divergence from the normative source must be detectable.
- A tool may lead the *thinking*; it may not hold the *decision*.

This is the class the benchmark showed most systems handle implicitly. CDS names
it deliberately.

### 6. Evidence Artifact

**Authority: none over sources. Records reality.**

Substantiates validation, accessibility, rendering, adoption, migration, consumer
feedback, and deviations.

- **Does not automatically change a normative source.** Evidence that contradicts
  a source is a signal, and triggers a controlled decision (invariant 6 of the
  dependency rules).
- Evidence never silently rewrites intent.

### 7. Consumer-local Artifact

**Authority: none over CDS. Owned by the consumer.**

Belongs to a consumer project. May use or map CDS.

- **Does not become CDS by existing** (invariant 5).
- Legitimate on its own terms — consumers already hold product-local design
  decisions (CR-002, CR-037) and may keep them.

### 8. Research and Example Artifact

**Authority: none. Informative only.**

- **Never normative** (invariants 2 and 3).
- Must not acquire covert normative force through repeated citation.

Registered because CDS already holds a substantial research corpus that must not
drift into authority.

## Authority matrix

*(Normative)*

| Class | Defines meaning | Defines values | Binding on consumers | May contradict a normative source | May change a source |
| --- | --- | --- | --- | --- | --- |
| 1 Normative Human-readable Source | **Yes** | No | Yes | — | Via change control |
| 2 Normative Machine-readable Source | No | **Yes** | Yes | **No** | Via change control |
| 3 Generated Artifact | No | No | Only as a faithful derivative | **No** | **No** |
| 4 Reference Implementation | No | No | No | **No** | **No** |
| 5 Authoring / Design-tool Representation | No | No | No | **No — divergence must be detectable** | **No** |
| 6 Evidence Artifact | No | No | No | May *report* a contradiction | **No — triggers a decision** |
| 7 Consumer-local Artifact | No | No | No (consumer-owned) | Not applicable — outside CDS | **No** |
| 8 Research / Example Artifact | No | No | No | Not applicable | **No** |

Read the matrix as a single rule: **only classes 1 and 2 are normative, and only
through change control.**

## Conflict scenarios

*(Normative)*

| # | Conflict | Resolution |
| --- | --- | --- |
| 1 | Human-readable source vs machine-readable source | **Fail closed.** Meaning (1) and values (2) must not disagree. Neither silently wins. Escalate — RISK-020. |
| 2 | Generated artifact vs its source | Source wins. The artifact is stale or the transformation is faulty. Regenerate; never patch the output. |
| 3 | Design tool vs normative source | Source wins. Tool divergence is a detectable defect, never an update. |
| 4 | Reference implementation vs contract | Contract wins. The implementation is wrong, or the contract has a gap to raise. |
| 5 | Consumer artifact vs CDS source | No conflict — different ownership. Becomes a CDS question only via a named extension point or reconciliation. |
| 6 | Evidence vs normative source | Neither wins automatically. Evidence is real and the source is authoritative: escalate to a controlled decision. |
| 7 | Research or example vs normative source | Source wins. Research never binds. |
| 8 | Two consumers need incompatible things | **Fail closed.** Not resolvable at artifact level — a Product Profile or governance question (RISK-008, RISK-027). |
| 9 | Two artifacts of the same class disagree | **Fail closed.** Recency is irrelevant (invariant 6). |

## Fail-closed behavior

*(Normative, DEC-S-023)*

When authority is unclear:

1. **Stop.** Do not guess.
2. **Do not resolve by recency.** The most recently edited artifact has no
   privilege whatsoever. This is the single most important rule here, because
   recency-wins is the default behavior of almost every tool.
3. **Do not resolve by convenience** — not by whichever is easier to change, not
   by whichever unblocks the current task.
4. **Record the conflict** as a deviation (Layer 8).
5. **Escalate** to the decision authority.
6. **Prefer the more conservative reading** until resolved. If one reading claims
   something is verified and another does not, the unverified reading holds
   (invariant 9).

Failing closed is expected to be occasionally inconvenient. That is the cost of
not silently shipping a contradiction.

## Normative-source responsibilities

A normative source must:

- state its own scope and boundaries,
- be human-reviewable and diffable,
- carry an identifiable revision (DEC-S-031),
- state what it does **not** cover,
- never depend on a proprietary tool to be read or understood (DEC-S-004),
- route changes through change control.

## Generated-artifact rules

- Deterministic: same source revision + same transformation revision = same
  output.
- Identifies source revision, transformation revision, and output identity.
- Carries no decision that is absent from its source.
- Never hand-edited. A hand edit is a reconciliation event, not a change.
- Distribution of an output without its provenance is a defect (RISK-025).

## Authoring-tool rules

- A tool may hold a *representation*, never *the* source.
- Divergence between tool state and normative source must be detectable — a
  divergence nobody can see is indistinguishable from authority.
- No CDS process may require a specific proprietary tool to determine what is
  normative.
- Tool convenience never justifies inverting the authority direction.

## Reference-implementation limits

- Demonstrates a contract; does not define it.
- Must not add behavior the contract does not describe and then rely on it.
- Multiple implementations may coexist; none becomes normative by being first,
  most used, or most complete.
- An implementation revealing a contract gap produces a **contract change
  request**, not a local extension.

## Consumer-artifact limits

- Consumer-local artifacts are outside CDS authority (DEC-S-008).
- Using CDS does not transfer ownership of a consumer artifact to CDS.
- Reuse requires explicit generalization and acceptance (DEC-S-016) — presence in
  a consumer is never sufficient.
- CDS does not retrospectively certify a consumer artifact (DEC-S-026).

## Research and example boundaries

- Research (benchmark, hypotheses, consumer evidence) is **evidence**, never a
  decision (DEC-S-019).
- Examples illustrate; they do not specify.
- Neither acquires authority through age, repetition, or citation.
- A research finding becomes normative only by passing through a decision.

## Future governance dependencies

**Deferred to CDS-WP-006:**

- who holds the detailed conflict-resolution authority, and the escalation path,
- the change-control process that turns an escalation into a decision,
- how a deviation is formally recorded, reviewed, and expired,
- maturity states that qualify a normative source,
- the versioning scheme that gives "revision" a concrete meaning,
- conformance rules for what a consumer may claim.

This document establishes **that** authority is bounded and that conflicts fail
closed. It does not establish **who** decides. Until CDS-WP-006, escalation goes
to Nova for recommendation and the Human Maintainer for decision (DEC-S-005).

## Related documents

- [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) — frame and invariants
- [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md)
- [Evidence, Traceability and Status Semantics](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md)
- [Consumer Contract and Reconciliation Model](CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md)
