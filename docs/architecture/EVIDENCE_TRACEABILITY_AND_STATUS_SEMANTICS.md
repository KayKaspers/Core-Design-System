# Evidence, Traceability and Status Semantics

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-005 — Design System Architecture
- **Date:** 2026-07-16
- **Status:** **Normative** for the evidence flow and status axes

## Purpose

Two things that look separate and are not:

1. **Traceability** — can we prove where an artifact came from?
2. **Status semantics** — can the system tell the truth about what it knows?

Both are the same discipline: **not claiming more certainty than exists**. One
applies to CDS's own artifacts, the other to what consumers' interfaces say.

Frame: [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) — Layer 8.

---

# Part 1 — Evidence and Traceability

## Traceability flow

*(Normative, DEC-S-031)*

```
Requirement or Decision
  → Normative Source
     → Machine-readable Source (where applicable)
        → Transformation
           → Generated Artifact
              → Reference or Consumer Implementation
                 → Validation Evidence
                    → Consumer Feedback
                       → Controlled Change Decision
                          ↺ (back to Requirement or Decision)
```

The loop closes deliberately. Feedback does not mutate a source; it produces a
**controlled change decision** that may (DEC-S-023, authority class 6).

Every step must later be **identifiable and revision-bound**.

## Required logical identities

*(Normative — logical identities, no format selected)*

| Identity | Answers | Without it |
| --- | --- | --- |
| **Source Revision** | Which normative source state | Nothing downstream is attributable |
| **Transformation Revision** | Which transformation ran | Output cannot be reproduced |
| **Output Identity** | Which artifact this is | Artifacts cannot be distinguished |
| **Consumer Revision** | Which consumer state integrated it | No adoption claim possible |
| **Evidence Identity** | Which evidence, of what, when | Evidence cannot be re-examined |
| **Deviation Record** | What diverged, why, scope, owner, expiry | Divergence becomes an invisible fork |
| **Approval State** | What was accepted, by whom, when | Authority is unreconstructable |

**No metadata structure or file format is selected** (DEC-S-032).

## Traceability chain

The chain must answer, for any artifact: *which source revision, through which
transformation, produced this, integrated at which consumer revision, evidenced
by what, with which deviations, approved by whom.*

A break anywhere breaks the whole chain. An artifact whose origin cannot be
established is functionally normative — nobody can contradict it (RISK-025).

## Deviation flow

```
Deviation detected
  → Recorded (what, why, scope, owner, affected version)
     → Classified
        ├→ Justified product-local  → Consumer-owned; not a CDS defect
        ├→ CDS gap                  → Candidate; requires the DEC-S-016 gate
        ├→ CDS defect               → Must be fixed; strongest signal
        ├→ Scope pressure           → Registered as deferred; does not widen scope
        └→ Unresolved               → Stays visible; never silently closed
           → Review / expiry
              → Migration or acceptance decision
```

A deviation is never resolved by widening the system to accommodate it
(RISK-015), and never closed by being ignored.

## Feedback flow

Consumer feedback is **evidence** (authority class 6). It is recorded as given,
not summarized into agreement — disagreement between CDS and a consumer is itself
evidence and must survive to review.

Feedback changes nothing automatically. It triggers a controlled decision.

## Evidence honesty

*(Normative)*

Evidence must be reported **only at the level it actually reaches**.

Current state: all consumer requirements rest on **committed documentation**. No
interviews, observation, usability testing, or accessibility testing have taken
place, and **none may be implied** (RISK-017).

Documentation evidences *stated intent* or *built behavior*. It does not evidence
that anything works for anyone.

**`Not tested` must remain available and must be used.** Absence of a failure is
not evidence of success.

---

# Part 2 — Status Semantics

## The architectural invariant

*(Normative, DEC-S-028)*

> **Unknown, stale, unavailable, incomplete, or unverified information must not
> be represented as healthy, successful, current, or verified.**

This is architecture, not styling. It is placed here — in the structure — because
a convention can be forgotten by any implementer under deadline, while a
structural separation cannot be quietly ignored.

It rests on the strongest multi-consumer evidence CDS has: **all three reviewed
consumers document graded status, and two independently require that unknown must
not read as healthy** (CR-006, CR-007).

## The five status axes

*(Normative — separate, never merged)*

| Axis | Answers | Example question |
| --- | --- | --- |
| **Operational Condition** | What state is the thing in? | Is it working? |
| **Severity or Impact** | How much does it matter? | Does it need attention now? |
| **Knowledge Confidence** | How sure are we? | Do we actually know this? |
| **Freshness** | How current is this? | When was this last true? |
| **Availability of Evidence** | Is this backed by evidence? | Can we show why we believe it? |

### Why they must stay separate

Merging them destroys the information that matters most.

Collapse **Operational Condition** and **Knowledge Confidence** into one value and
"unknown" has nowhere to live — so it becomes either a false healthy or a false
alarm. Both are lies, and the first is the dangerous one: an operator acts on a
green that means *we have no idea*.

Collapse **Freshness** and you cannot distinguish *healthy now* from *healthy an
hour ago, before the network dropped*.

Collapse **Availability of Evidence** and a claim and a guess look identical.

## Status rules

*(Normative)*

1. **Health and Knowledge Confidence must never merge** into one opaque value.
2. **Colour must never be the sole meaning carrier** (CR-006, CR-021).
3. **Unknown is not a neutral shorthand for Healthy** (invariant 7).
4. **Degraded and unavailable must stay distinguishable.** Working badly and not
   working are different problems.
5. **Stale is not Current** (invariant 8).
6. **Unverified is not Verified** (invariant 9).
7. **Status semantics stay consistent across channels**, and are rendered
   channel-appropriately (DEC-S-029, invariant 13).
8. **No transformation may collapse the axes** — see the transformation
   boundaries.
9. **No Product Profile may distort status truth** (DEC-S-025, invariant 10).

## Channel consistency

Meaning is constant; presentation is not.

The hard cases are the non-interactive channels: a PDF has no hover, no live
update, and may be printed in greyscale. A status that depends on colour,
interaction, or refresh to be understood **fails there** — which makes the
non-colour rule an architectural necessity rather than an accessibility courtesy.

Data visualization is where this bites hardest: dense encoding tempts every
shortcut this section forbids.

## Accessibility and non-colour requirements

*(Architectural constraint — **not** a conformance claim)*

- Meaning must not depend on colour alone (CR-006).
- Status must be perceivable non-visually.
- Component contracts carry accessibility behavior (Layer 4).
- A Product Profile must not weaken an accessibility requirement (invariant 10).
- Keyboard operability and visible focus are component-contract concerns
  (CR-021).
- Motion restraint and reduced-motion preferences are foundation concerns
  (CR-022).

**No conformance level is chosen and nothing is certified here** (CR-024). The
architecture ensures a later target *can* be met; it does not say what it is.

This ordering is a real cost: architecture decided before the accessibility
policy may constrain that policy or make it expensive to adopt (RISK-028). The
mitigation is that accessibility appears here as a **constraint on structure**
rather than as a set of thresholds — constraints survive a later policy; specific
thresholds would have pre-empted it.

## Unresolved taxonomy decisions

*(Deliberately open)*

1. What is the concrete status taxonomy, and what are the states called?
2. How are the five axes represented — separate values, a composite with visible
   parts, or something else?
3. How are combined states resolved — for example degraded **and** permission
   denied simultaneously (Pilot Scenario D-1)?
4. What is the minimum honest representation of "unknown"?
5. How is freshness expressed when the clock itself is uncertain?
6. Where does CDS status semantics end and consumer domain semantics begin
   (CR-035)?
7. What evidence identity structure is used?
8. How is a deviation record represented?

Questions 1–5 need design work after architecture approval. Question 6 is the
open boundary question carried from CDS-WP-002 and CDS-WP-004. Questions 7–8
touch CDS-WP-006.

## Related documents

- [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md)
- [Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)
- [Artifact Distribution and Channel Model](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md)
- [Consumer Contract and Reconciliation Model](CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md)
- [Consumer Validation Plan](../governance/CONSUMER_VALIDATION_PLAN.md)
