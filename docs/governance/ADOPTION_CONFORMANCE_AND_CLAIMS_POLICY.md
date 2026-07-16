# Adoption, Conformance and Claims Policy

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-006
- **Date:** 2026-07-16
- **Status:** **Normative** for what may be claimed about CDS

## Purpose

Defines exactly what anyone may say about their relationship to CDS, and what
evidence each statement costs.

Operationalizes DEC-S-012 (claims require a version and evidence) into four
graded claim types with gates — the mechanism the benchmark showed working at
one reviewed system, and absent almost everywhere else.

Frame: [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md).

## The core rule

*(Normative, DEC-S-044)*

> **Every claim is scope-bound, version-bound, consumer-revision-bound,
> evidence-backed, and explicitly approved.**
>
> **A global or unqualified `CDS compliant` claim is invalid.**

An unqualified claim is unfalsifiable — CDS is versioned, so "compliant" without
a version says nothing checkable, while transferring real trust. That asymmetry
is the whole problem (RISK-037).

## The four claim types

*(Normative — a ladder; each step adds evidence)*

### 1. Uses CDS Artifacts

**Means only:** a named CDS version or revision is used.

**Says nothing about** quality, completeness, correctness, or validation.

| | |
| --- | --- |
| **Minimum evidence** | Named CDS version or revision |
| **Approval** | None required — it is a statement of fact |
| **Limits** | Not an integration, validation, or conformance claim. Not endorsement. |

The honest floor. Most consumers should be here for a long time.

### 2. CDS-integrated for Declared Scope

**Means:** within a declared scope, CDS is integrated as its contracts describe.

| | |
| --- | --- |
| **Minimum evidence** | Defined scope · consumer revision · CDS version or revision · integration traceability · documented overrides and exceptions |
| **Approval** | Consumer Maintainer; Nova may review |
| **Limits** | **Not validated.** Integration is not evidence that it works. |

### 3. CDS-validated for Declared Scope

**Means:** within a declared scope, the integration has been validated and the
results are recorded.

| | |
| --- | --- |
| **Minimum evidence** | Everything from *CDS-integrated*, plus an evidence bundle · validation results · **known limitations** · review state |
| **Approval** | Human Maintainer after Nova review |
| **Limits** | **Not conformance.** Validated means examined, not compliant. |

"Known limitations" is mandatory: a validation reporting no limitations has not
been performed rigorously enough to be believed.

### 4. CDS-conformant for Declared Scope

**Means:** within a declared scope, all mandatory Stable contracts are met.

| | |
| --- | --- |
| **Minimum evidence** | Everything from *CDS-validated*, plus fulfilment of all mandatory **Stable** contracts for the scope · permitted and documented exceptions · **no unresolved critical deviations** |
| **Approval** | **Human Maintainer after Nova review** |
| **Limits** | Scope-bound. Not certification. Not endorsement. Not global. |

**No conformance claim is currently possible.** It requires Stable contracts, and
no artifact can reach Stable while the accessibility target is undefined
(CR-024, RISK-028).

## The prohibited claim

*(Normative)*

> ### `CDS certified` — **prohibited**

Invalid for anyone, in any context, at any scope.

Certification implies an independent programme with defined criteria, assessors,
and a revocation path. **No such programme exists**, and none is defined or
approved. Until one is normatively defined and approved, the word is unavailable
— not "discouraged".

## Mandatory claim contents

*(Normative — every valid claim, all fields)*

| # | Field |
| --- | --- |
| 1 | CDS version or revision |
| 2 | Consumer and consumer revision |
| 3 | Scope |
| 4 | Product Profile, if any |
| 5 | Exceptions |
| 6 | Evidence identity |
| 7 | Review and approval state |
| 8 | Date or validity reference |

A claim missing any field is **not a weaker claim — it is not a claim.**

## Claim rules

*(Normative)*

| Rule | Meaning |
| --- | --- |
| **No global `CDS compliant`** | Scope is mandatory. |
| **Pilot completion is not adoption** | The CoreOps pilot is a bounded slice (DEC-S-015). |
| **Naming a consumer is not endorsement** | Classification grants nothing (DEC-S-010, DEC-S-018). |
| **A differentiation hypothesis is not a claim** | HYP-001…008 remain research hypotheses (DEC-S-019). |
| **Claims are re-assessed on relevant change** | See triggers below. |
| **`latest` is not a version** | An unpinnable claim is unverifiable (DEC-S-038). |
| **Evidence must reach the claimed level** | Documentation is Level 1 evidence and supports no validation claim (RISK-017). |

## Re-assessment triggers

A claim becomes **stale — not automatically false, but no longer supported** —
when:

1. the CDS version or revision changes,
2. the consumer revision changes materially in scope,
3. a relied-upon contract is deprecated or removed,
4. an exception expires or changes,
5. a Product Profile changes,
6. the accessibility policy is established or changes (CR-024),
7. a critical deviation is discovered,
8. the declared scope changes.

A stale claim must be withdrawn or re-established. **Silence is not
continuation.**

## Pilot boundary

The CoreOps pilot establishes **none** of these claims (DEC-S-015, RISK-018):

- not adoption, not conformance, not certification, not endorsement,
- not that CDS is differentiated (DEC-S-019).

Its existence and its completion are both governed by the
[CoreOps Pilot Contract](COREOPS_PILOT_CONTRACT.md), whose entry criteria remain
unmet.

## Brand endorsement boundary

*(Normative)*

No claim in this policy grants brand rights.

- Consumer classification grants no endorsement, brand usage, availability,
  licensing, or support (DEC-S-010).
- Secondary consumers hold evidence value, not authority (DEC-S-018).
- Brand asset rights are governed separately and remain undecided (DEC-S-047).
- Even `CDS-conformant` grants **no** brand usage right.

## Current claim status

*(Normative — as of this work package)*

| Claim | Possible today? |
| --- | --- |
| Uses CDS Artifacts | Only once a CDS release with an identifiable version exists |
| CDS-integrated | No — no release, no integration |
| CDS-validated | No — no validation has occurred |
| CDS-conformant | **No — no Stable contracts exist** |
| CDS certified | **Prohibited** |

**No CDS adoption, validation, conformance, certification, or endorsement claim
is currently valid — by anyone, including CDS itself.**

## Related documents

- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
- [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md)
- [Versioning, Compatibility and Deprecation Policy](VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md)
- [Exception and Product Profile Governance](EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md)
- [CoreOps Pilot Contract](COREOPS_PILOT_CONTRACT.md)
- [Consumer Validation Plan](CONSUMER_VALIDATION_PLAN.md)
