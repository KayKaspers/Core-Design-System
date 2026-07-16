# Release and Change Control Policy

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-006
- **Date:** 2026-07-16
- **Status:** **Normative** for releases and change control

## Purpose

Defines what a release requires and who may perform one.

Frame: [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md).

## Release candidate requirements

*(Normative, DEC-S-048 — all required)*

| # | Requirement |
| --- | --- |
| 1 | Release identity |
| 2 | **Immutable source revision** |
| 3 | Contained artifacts |
| 4 | Their maturity states |
| 5 | Compatibility declaration (per axis) |
| 6 | Change summary |
| 7 | Deprecation and removal notes |
| 8 | Migration information |
| 9 | Evidence bundle |
| 10 | Risk review |
| 11 | Licence and publication review |
| 12 | Approval state |

Requirement 4 exists because a release contains artifacts of **mixed maturity**.
Listing them individually is what stops "we released it" from becoming "it is
stable" (DEC-S-035, RISK-031).

## Change classes

*(Normative — exactly six)*

| Class | Meaning | Track | Evidence | Review | Versioning | Migration | Approval |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Editorial** | Wording, formatting, no semantic change | Standard | None | Nova (light) | PATCH or none | None | Human Maintainer |
| **Corrective** | Fixes a defect without changing a contract | Standard | Defect + fix evidence | Nova | PATCH | None | Human Maintainer |
| **Additive** | Backward-compatible addition | Standard¹ | Per maturity gate | Nova | MINOR | None | Human Maintainer |
| **Deprecating** | Marks a Stable artifact deprecated | **Elevated** | Impact + migration path | Nova + Evidence Reviewer | MINOR² | **Required** | Human Maintainer |
| **Breaking** | Breaks a Stable contract | **Elevated** | Full bundle + consumer impact | Nova + Evidence Reviewer | **MAJOR** | **Required** | Human Maintainer |
| **Emergency** | Security, legal, rights, or dangerous behavior | **Elevated** | **Deferred, then full** | Nova (post-hoc if needed) | Per impact | Where possible | **Human Maintainer** |

¹ Elevated if it touches a Stable contract, accessibility, or a Product Profile.
² The deprecation itself is MINOR; the eventual removal is MAJOR (DEC-S-040).

### Emergency change control

Permitted only for: a severe security risk · legal impermissibility · an
unfixable provenance or rights violation · demonstrably dangerous behavior.

An emergency change **defers** evidence and ceremony. It **never** waives:

- the **Human Maintainer decision** — no automated or delegated emergency path,
- a documented reason,
- an impact assessment,
- a replacement, rollback, or mitigation plan,
- **full evidence afterwards**.

"Emergency" describes the **timeline**, not the standard. Schedule pressure,
embarrassment, and maintenance burden are not emergencies.

## Review and approval

*(Normative)*

- **Review establishes** whether criteria are met. **Approval decides** to
  proceed. Different acts, recorded separately.
- Nova reviews and recommends; the **Human Maintainer approves**.
- An Evidence Reviewer checks evidence against the claim — never the executor of
  that work.
- **A clean build or diff is not approval.** Automated checks are input to a
  review; they are evidence, not consent.
- Unclear readiness ⇒ **NO-GO**, not "go with notes".

## Risk review

Every release candidate requires a risk review establishing: whether any risk's
severity changed · whether any `Accepted` risk's trigger fired · whether the
release creates new risk · whether unresolved critical deviations exist.

**An unresolved critical deviation blocks the release.**

## Licence and publication review

Every release candidate requires, per artifact class: rights and licence status ·
third-party provenance · brand asset boundaries · compatibility of terms with the
intended distribution.

**Unknown or conflicting rights block the release** (RISK-038). This is currently
unsatisfiable — no licensing decision exists for any of the ten classes.

## Release authority

*(Normative, DEC-S-048)*

| Rule | |
| --- | --- |
| **No automatic publication from `main`** | Being on the default branch releases nothing. |
| **No tag or release without a Human Maintainer action** | Not delegable, not automatable. |
| **Nova reviews and recommends** | Never releases. |
| **Claude never creates a release or tag** | Under any circumstance, including emergencies. |
| **A clean build or diff is not release approval** | Green is not consent. |
| **No automated process may independently approve or publish** | The gate is a human. |

**Claude may document release steps as instructions for the Human Maintainer. It
may never execute them.**

## Release readiness

A release is ready only when **all** hold:

1. all release candidate requirements met,
2. all contained artifacts have declared maturity states,
3. compatibility declared per relevant axis, with unassessed axes marked
   `Not yet assessed` rather than rounded up,
4. deprecations and removals documented with migration,
5. evidence bundle complete at the level claimed,
6. risk review complete, no unresolved critical deviations,
7. licence and publication review complete,
8. Nova review complete,
9. **Human Maintainer approval**.

**Currently unreachable:** requirement 7 cannot be satisfied (no licensing
decisions), and no artifact can reach Stable while the accessibility target is
undefined (CR-024). **No CDS release is possible today.** Recorded, not worked
around.

## Change control for this policy set

Changes to any CDS-WP-006 governance document require: an authorized work
package · a corresponding decision entry where a registered decision changes ·
consistency updates across dependent policies · Nova review · Human Maintainer
approval.

Governance does not amend itself, and no policy here is self-activating.

## Related documents

- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
- [Versioning, Compatibility and Deprecation Policy](VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md)
- [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md)
- [Licensing and Publication Decision Model](LICENSING_AND_PUBLICATION_DECISION_MODEL.md)
- [Risk Governance Model](RISK_GOVERNANCE_MODEL.md)
- [Source Conflict Resolution Policy](SOURCE_CONFLICT_RESOLUTION_POLICY.md)
