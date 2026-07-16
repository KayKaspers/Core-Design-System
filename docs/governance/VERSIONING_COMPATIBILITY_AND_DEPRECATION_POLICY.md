# Versioning, Compatibility and Deprecation Policy

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-006
- **Date:** 2026-07-16
- **Status:** **Normative** for versioning, compatibility, deprecation, and removal

## Purpose

Gives "revision" a concrete meaning — the dependency CDS-WP-005 left open for
DEC-S-031, the Adoption Evidence Contract, and CR-034.

Frame: [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md).

## Versioning model

*(Normative, DEC-S-037)*

**`MAJOR.MINOR.PATCH`**

| Part | Increments when |
| --- | --- |
| **MAJOR** | A breaking change to a **Stable** contract, or removal of a Stable artifact outside an explicitly permitted exception. |
| **MINOR** | A backward-compatible addition or new capability within existing Stable contracts. |
| **PATCH** | A backward-compatible correction, with no new mandatory capability and no contract break. |

The version describes the **released state**, never an artifact's maturity
(DEC-S-035). A MINOR release may add an Experimental artifact; that artifact is
not Stable because the release shipped.

## Pre-1.0 policy

*(Normative)*

CDS is currently pre-1.0. **No blanket long-term backward-compatibility promise
exists.**

This is honest positioning, not a loophole. Even pre-1.0, the following remain
mandatory:

- breaking changes are **identified as breaking**,
- migrations are **documented**,
- source revisions are **bound**,
- deprecations are **handled traceably**.

Pre-1.0 removes the *compatibility promise*. It does not remove *traceability,
honesty, or migration duty*. A pre-1.0 project that breaks consumers silently is
not exercising a licence; it is failing at governance it already owes.

**The concrete v1.x commitment begins only with an explicitly approved v1.0.0
release.** Claude may never assert that v1.0.0 has been reached, and nothing in
this policy schedules it.

## Pre-release identity

Pre-release states may be marked. **Naming a pre-release channel is not a
publication commitment** and does not imply availability, support, or a schedule.
Publication is governed separately (DEC-S-046).

## Release identity

*(Normative, DEC-S-038)*

Every released CDS state requires, logically:

| # | Element |
| --- | --- |
| 1 | Release Version |
| 2 | **Immutable Source Revision** |
| 3 | Normative Source Set |
| 4 | Artifact Manifest |
| 5 | Maturity Declaration |
| 6 | Compatibility Declaration |
| 7 | Change Summary |
| 8 | Migration Information |
| 9 | Evidence References |
| 10 | Approval State |

### Identity rules

- **`latest` is not an identity.** It is insufficient for evidence, adoption,
  migration, or conformance. A consumer that can only say "latest" cannot make
  any claim (DEC-S-044).
- Consumer evidence must point to a version or an immutable revision.
- Generated outputs must make their source and transformation revision provable
  (DEC-S-031).
- **A rebuild must not silently reuse the same release identifier with different
  content.** Identity that can change underneath a consumer is not identity.

**No manifest structure or technical format is selected** (DEC-S-032).

## Compatibility model

*(Normative, DEC-S-039)*

Compatibility is declared **per contract axis**. There is no single answer.

### The eight compatibility axes

| # | Axis |
| --- | --- |
| 1 | Normative Documentation Contract |
| 2 | Machine-readable Source Contract |
| 3 | Token Contract |
| 4 | Component Contract |
| 5 | Product Profile Contract |
| 6 | Channel Output Contract |
| 7 | Consumer Integration Contract |
| 8 | Evidence Contract |

### Permitted compatibility statements

| Statement | Meaning |
| --- | --- |
| **Compatible** | No consumer action required on this axis. |
| **Compatible with documented limitations** | Works, with stated constraints. |
| **Migration required** | Consumer action required; migration information provided. |
| **Breaking** | Contract broken on this axis; MAJOR. |
| **Not applicable** | The axis does not apply to this release. |
| **Not yet assessed** | **Not evaluated.** Must never be read as compatible. |

### Compatibility rules

- **No blanket compatibility claim.** A release is never "compatible" as a whole.
- Every release approval names the relevant axes.
- **An unassessed axis is never presented as compatible.** `Not yet assessed`
  must survive into the release record — the temptation to round it up to
  `Compatible` because nothing broke in testing is exactly RISK-032.
- Consumer-local artifacts are never automatically guaranteed by CDS.
- Stable contracts within the same MAJOR line should remain compatible.
- The concrete v1.x promise begins only with an approved v1.0.0 release.

## Deprecation

*(Normative, DEC-S-040)*

A Stable artifact must be Deprecated before regular removal.

### Deprecation record — required

| # | Field |
| --- | --- |
| 1 | Affected version or revision |
| 2 | Reason |
| 3 | Replacement or target state |
| 4 | Consumer impact |
| 5 | Migration guidance |
| 6 | Planned earliest removal boundary |
| 7 | Owner |
| 8 | Evidence |
| 9 | Known exceptions |

Field 5 is the one that matters: **a deprecation without a viable migration path
is not a deprecation — it is a removal with extra steps** (RISK-033). If no
migration exists, the artifact is not ready to be deprecated.

Field 6 is a **boundary, not a schedule**. No time-based support or release
cadence is invented here; CDS has no evidence for what cadence it could sustain.

## Removal

### Regular removal of a Stable contract

Requires **all** of:

- a **MAJOR** change,
- documented prior deprecation,
- migration information,
- Human Maintainer approval.

### Emergency removal

*(Normative — narrowly bounded)*

Permitted **only** for:

1. a severe security risk,
2. legal impermissibility,
3. an unfixable provenance or rights violation,
4. demonstrably dangerous behavior.

Requires: explicit Human Maintainer decision · documented reason · impact
assessment · replacement, rollback, or mitigation plan · **full evidence
afterwards**.

Emergency removal bypasses the deprecation sequence — **never** the Human
Maintainer, and never the evidence obligation. The evidence is deferred, not
waived. "Emergency" describes the timeline, not the standard.

Convenience, embarrassment, schedule pressure, and maintenance burden are **not**
emergencies.

## Migration requirements

Every migration must be **versioned** (from which version to which),
**documented** (what changes, why, what it costs), and **reversibly plannable** —
a migration nobody can back out of is a one-way door and must be recognised as
one before it opens.

Migration information belongs to the release that causes the need, not to a later
release that notices it.

## Open implementation questions

*(Deliberately deferred — DEC-S-032)*

1. What technical form does the release identity take?
2. What manifest structure lists artifacts and maturities?
3. How is an immutable revision expressed concretely?
4. How is compatibility assessed per axis — by what method, by whom?
5. What is the practical cadence CDS can sustain? **No cadence is invented.**
6. How is migration information delivered to consumers?
7. What tooling validates that a rebuild reproduces a release identity?

Questions 1–3 and 6–7 require a distribution technology decision, which is
deferred. Questions 4–5 require capacity CDS has not yet tested (RISK-026).

## Related documents

- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
- [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md)
- [Release and Change Control Policy](RELEASE_AND_CHANGE_CONTROL_POLICY.md)
- [Adoption, Conformance and Claims Policy](ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md)
- [Artifact Distribution and Channel Model](../architecture/ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md)
