# Contribution and Acceptance Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-006
- **Date:** 2026-07-16
- **Status:** **Normative** for contributions and acceptance

## Purpose

Defines how something gets **into** CDS — and, more often, why it correctly does
not.

This operationalizes DEC-S-016 (generalization requires explicit review and
acceptance) into a process, and enforces the benchmark's clearest lesson: the
harvesting model works only if it has a gate.

Frame: [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md).

## Contribution types

| Type | Example |
| --- | --- |
| **Problem report** | A gap or defect in a normative source |
| **Proposal** | A suggested addition or change |
| **Evidence** | Validation, accessibility, adoption, or migration evidence |
| **Implementation** | A reference or candidate implementation |
| **Generalization candidate** | A consumer-local solution proposed as shared |
| **Documentation improvement** | Clarity, structure, correction |
| **Migration contribution** | Guidance or tooling for a transition |

## The ten-step flow

*(Normative)*

```
1  Intake
2  Triage
3  Problem and Scope Validation
4  Evidence Review
5  Architecture and Governance Review
6  Proposal
7  Experimental or Candidate Implementation
8  Validation
9  Accept | Revise | Defer | Reject | Keep Consumer-local
10 Release and Migration Preparation
```

| Step | Purpose | Who |
| --- | --- | --- |
| **1 Intake** | Record it. Nothing is lost, nothing is accepted. | Any role |
| **2 Triage** | Classify; assign a track. | Nova |
| **3 Problem and Scope Validation** | Is the problem real, and is it CDS's? | Nova |
| **4 Evidence Review** | What is actually evidenced versus asserted? | Evidence Reviewer |
| **5 Architecture and Governance Review** | Does it fit the layers, authority, and invariants? | Nova |
| **6 Proposal** | A concrete, reviewable proposal. | Contributor / Claude |
| **7 Experimental or Candidate Implementation** | Make it real enough to test. | Contributor |
| **8 Validation** | Bounded validation against the plan. | Consumer Maintainer / Evidence Reviewer |
| **9 Outcome** | One of five. | **Human Maintainer** |
| **10 Release and Migration Preparation** | Only if accepted. | Human Maintainer |

Steps 3–5 exist to reach a *no* cheaply. Most contributions should end there, and
that is the process working.

## Minimum contribution information

*(Normative — where applicable)*

| # | Information |
| --- | --- |
| 1 | Problem statement |
| 2 | Affected consumers |
| 3 | **Generalizability rationale** |
| 4 | Scope and non-goals |
| 5 | Ownership boundary |
| 6 | Accessibility impact |
| 7 | Privacy and security impact |
| 8 | Migration impact |
| 9 | Provenance and rights |
| 10 | Evidence plan |
| 11 | Withdrawal or revision path |

Item 3 is the gate. "One consumer needs it" is a fact, not a rationale — DEC-S-016
requires multi-consumer relevance **or** a documented argument for why it
generalizes. Item 9 exists because a contribution with unclear rights blocks
publication permanently (RISK-038).

## Track assignment

| Track | Applies to |
| --- | --- |
| **Standard** | Documentation improvements · corrections · clearly bounded non-breaking additions · problem reports |
| **Elevated** | Generalization candidates · anything touching a Stable contract · accessibility impact · Product Profiles · breaking changes · anything with unclear rights · security-relevant changes |

**A contribution touching an Elevated trigger is Elevated**, regardless of how
small it looks. Both tracks keep every mandatory gate — only ceremony scales.

## Acceptance criteria

*(Normative — all must hold)*

1. The problem is real and within CDS scope (DEC-S-014).
2. Generalizability is demonstrated or argued, not assumed (DEC-S-016).
3. It fits the architecture — layers, authority, invariants (DEC-S-021…032).
4. It does not weaken shared semantics, accessibility, or status truth.
5. Evidence exists at the level claimed (RISK-017).
6. Ownership is unambiguous.
7. Rights and provenance are clear.
8. Migration impact is understood.
9. It is affordable to maintain (RISK-026).
10. Human Maintainer approval after Nova review.

## Outcomes

*(Normative — exactly five)*

| Outcome | Meaning |
| --- | --- |
| **Accept** | Enters CDS at a maturity state. Never straight to Stable. |
| **Revise** | Real, not ready. Returns with specified changes. |
| **Defer** | Real, but blocked by a missing decision or dependency. Registered, not forgotten. |
| **Reject** | Not a CDS concern, or contrary to a principle. Recorded with rationale. |
| **Keep Consumer-local** | Real and legitimate — but it belongs to the consumer. |

**`Keep Consumer-local` is a first-class success, not a soft rejection.** Most
product-specific work should live there permanently. CDS absorbing everything is
Non-goal 11 and RISK-016, not the goal.

Every outcome is recorded with rationale. A silent outcome is indistinguishable
from neglect.

## Prohibited shortcuts

*(Normative, DEC-S-041)*

| Forbidden | Why |
| --- | --- |
| **Consumer use = acceptance** | Being used proves need, never fit. |
| **Popularity = quality** | Frequency is not evidence. |
| **Implementation before governance = authority** | Building first must not create a fait accompli. |
| **Auto-merge** | No automated process accepts a contribution. |
| **Self-approval** | No contributor approves their own contribution — including Claude. |
| **Urgency bypass** | Pressure is a reason to reduce ceremony, never to skip a gate. |
| **Bundling** | An Elevated change hidden inside a Standard batch. |

RISK-034 names this collectively: existing implementation, urgency, popularity,
or consumer pressure used to bypass review.

## External contributions

*(Normative — currently closed)*

**External contributions are not yet possible.** They require:

1. an approved publication state permitting external participation
   (DEC-S-046) — currently `Private Development`,
2. an approved contribution licensing model (DEC-S-047),
3. a decided contribution rights framework.

None exists. Until then, contributions come from within the Core ecosystem under
this model.

**No `CONTRIBUTING.md` is created here**, and no external contribution invitation
is implied. Publishing a contribution process before deciding rights would invite
work CDS cannot lawfully accept.

## Related documents

- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
- [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md)
- [Exception and Product Profile Governance](EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md)
- [Licensing and Publication Decision Model](LICENSING_AND_PUBLICATION_DECISION_MODEL.md)
- [Product Profile and Extension Model](../architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md)
