# Accessibility Limitations and Exception Policy

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-007
- **Date:** 2026-07-16
- **Status:** **Normative** for accessibility limitations and exceptions

## Purpose

Governs how CDS records what it **cannot** do accessibly — and prevents that
record from becoming a way to opt out.

Frame: [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md).

## Limitation versus exception

Two different things, often confused:

| | Limitation | Exception |
| --- | --- | --- |
| **Says** | "This artifact does not meet a requirement, and here is what that costs users." | "This consumer diverges from a CDS contract, with a plan." |
| **About** | An accessibility gap | A contract deviation |
| **Effect** | Restricts maturity and claims | Tracked debt with an expiry |
| **Can waive accessibility?** | **No** | **No** |

**Neither is a passed test.** Recording a barrier does not remove it.

## Limitation record

*(Normative — all mandatory)*

| # | Field |
| --- | --- |
| 1 | ID |
| 2 | Affected artifact |
| 3 | Scope |
| 4 | CDS version or revision |
| 5 | **Affected user needs** |
| 6 | Affected requirements or success criteria |
| 7 | Impact |
| 8 | Cause |
| 9 | **Available alternative or mitigation** |
| 10 | Owner |
| 11 | Evidence |
| 12 | Review trigger |
| 13 | **Expiry or re-assessment point** |
| 14 | **Claim effect** |
| 15 | Approval state |

Field 5 is the one that keeps this honest. A limitation stated as
"2.4.7 not met" is a compliance note. Stated as **"keyboard users cannot see
where they are"** it is a description of someone's blocked day — which is what it
actually is, and which makes the cost visible to whoever must decide.

Fields 9 and 13 prevent permanence: a limitation without an alternative and an
expiry is an undocumented decision to exclude people.

## Impact

Must state, honestly:

- which user needs are affected,
- whether the artifact is **unusable** or **degraded** for them,
- whether an accessible alternative path exists,
- whether the barrier blocks a complete process,
- whether it affects safety-relevant or dangerous actions.

**No aggregation, no score.** A single unmet criterion can make a whole process
unusable for a user group; an average hides exactly that.

## Alternative or mitigation

Every limitation must state what a blocked user can actually do.

| Answer | Meaning |
| --- | --- |
| An equivalent accessible path exists | Degraded, not blocked |
| A partial workaround exists | Its cost must be stated |
| **None** | **The artifact is not Candidate- or Stable-eligible** |

"Users can contact support" is **not** an accessible alternative. It is an
admission that the interface excludes them.

## Review trigger and expiry

Every limitation carries a **review trigger** and an **expiry or re-assessment
point**.

A limitation without one is not a limitation — it is a permanent exclusion nobody
decided to make. Expiry forces the decision back into the open.

Triggers include: the affected artifact changes · the support baseline changes ·
the CDS version changes · a consumer reports impact · a related risk materializes
· the expiry is reached.

## Maturity effect

*(Normative)*

| Limitation severity | Effect |
| --- | --- |
| **Critical** — a user group cannot complete a process; no alternative | **Blocks Stable. Blocks Candidate.** |
| **Significant** — degraded, alternative exists | **Blocks Stable.** Candidate possible if documented |
| **Minor** — narrow, documented, alternative exists | Candidate possible; Stable requires an explicit decision |

- **Experimental artifacts may carry known limitations** — that is what
  Experimental is for — but **may make no unqualified claim**.
- A limitation is **never** grounds for promotion.

## Claim effect

*(Normative)*

Every limitation states its claim effect. Baseline rules:

- A known limitation **must appear in any claim** covering its scope.
- **Critical limitations block the corresponding claims entirely.**
- A claim omitting a known limitation is **invalid** (DEC-S-044).
- Limitations cannot be netted against strengths.

## Exception boundary

*(Normative, DEC-S-059 — the hard rule)*

> **Accessibility requirements for Stable or CDS-conformant scope cannot be
> waived through an ordinary exception.**

Not "requires stronger review" — **not available through that mechanism at all**.

This holds even though the accessibility target only now exists. It also holds
under schedule pressure, which is when it will actually be tested.

### Prohibited waivers

An ordinary exception may **never**:

| # | Prohibited |
| --- | --- |
| 1 | Waive an accessibility requirement for Stable |
| 2 | Waive an accessibility requirement for a CDS-conformant claim |
| 3 | Permit a Product Profile to weaken accessibility (invariant 10) |
| 4 | Suppress a known limitation from a claim |
| 5 | Downgrade a critical limitation by relabelling it |
| 6 | Substitute AE-1 where AE-2 or AE-3 is required |
| 7 | Treat missing capacity as a conformance rationale |
| 8 | **Distort status truth** — the Unknown invariant is not exceptable |

### Capacity is not a rationale

*(Normative)*

**Missing maintainer capacity is a planning limit, not a conformance
justification.**

CDS may legitimately decide it cannot afford to make something accessible yet.
That decision produces:

- a **known limitation**, honestly stated,
- **not Stable**,
- **no claim**.

It does **not** produce a conformant artifact with an asterisk. The evidence
burden may genuinely exceed capacity (RISK-048) — the honest response is a
smaller scope or a lower maturity, never a weaker standard.

### No legal burden determination

**CDS makes no undue-burden or disproportionate-burden determination.** Those are
legal concepts in specific jurisdictions. CDS states engineering policy and makes
**no legal statement whatsoever**.

## Recurring limitations

*(Normative)*

**Recurring limitations trigger an architecture or scope review.**

If the same barrier appears repeatedly, the cause is not the artifact — it is a
foundation, a contract, or a scope that cannot be built accessibly. Repeatedly
recording the same limitation is a symptom of avoiding that finding.

## Escalation

Escalate when: a limitation would be critical · an exception would weaken
accessibility · accessibility and security appear to conflict · a claim omits a
known limitation · a limitation recurs · capacity pressure argues for a waiver ·
an expired limitation is still in force.

Path: **Claude records and reports → Nova reviews and recommends → Human
Maintainer decides.** While open, the affected artifact is not Candidate-,
Stable-, or claim-eligible.

**Only the Human Maintainer may approve a limitation with normative effect.**

## Current state

**No limitation and no exception is created in this work package.**

**No exception has been approved anywhere, and none is in force.**

Known **limitations** have since been recorded for the Semantic Status Candidate
scope, which holds admitted **AE-1** structural and automated evidence. Recording a
limitation is a documentation obligation, **not** an approved exception and **not** a
waiver. Every other CDS artifact is still AE-0 and has not been evaluated, so for
those no barrier is known — **that is not the same as having none**; it means nothing
has been looked at.

## Related documents

- [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Exception and Product Profile Governance](EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md)
- [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md)
- [Adoption, Conformance and Claims Policy](ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md)
