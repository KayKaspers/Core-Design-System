# Artifact Maturity Lifecycle

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-006
- **Date:** 2026-07-16
- **Status:** **Normative** for artifact maturity

## Purpose

Defines how a CDS artifact moves from idea to normative and out again — and what
must be true at each step.

This makes DEC-S-009 operational: "registered scope is not availability" is only
enforceable if availability has a name, criteria, and a gate.

Frame: [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md).

## Three independent axes

*(Normative, DEC-S-035 — the most misread part of this policy)*

| Axis | Answers | Governed by |
| --- | --- | --- |
| **Artifact Maturity** | How ready is *this artifact*? | This document |
| **Release Version** | Which released *state* contains it? | [Versioning Policy](VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md) |
| **Publication State** | Who can *see* it? | [Licensing and Publication](LICENSING_AND_PUBLICATION_DECISION_MODEL.md) |

They are **orthogonal**. A release may contain artifacts of several maturities. A
release version never makes an artifact Stable. A public artifact is not thereby
mature, and a Stable artifact is not thereby public.

Collapsing these axes is the mechanism by which "we released it" silently becomes
"it is stable", which is RISK-031.

## The seven maturity states

*(Normative)*

| # | State | Meaning | Consumer promise |
| --- | --- | --- | --- |
| 1 | **Proposed** | Need or idea registered; no solution approved. | None |
| 2 | **Exploratory** | Alternatives under investigation. | **None** — explicitly no consumer commitment |
| 3 | **Experimental** | A usable draft may exist, without compatibility commitment. | Usable at own risk; may change without notice |
| 4 | **Candidate** | Documented and ready for bounded validation. | Bounded validation only; not yet normative |
| 5 | **Stable** | Normatively approved. | Compatibility, deprecation, and migration rules apply |
| 6 | **Deprecated** | Still available; not recommended for new adoption. | Continues to work; migration path exists |
| 7 | **Removed** | No longer part of a supported active CDS state. | None — historical traceability retained |

## Entry and exit criteria

| State | Entry requires | Exit to |
| --- | --- | --- |
| **Proposed** | A registered need with scope | Exploratory, Experimental, or closed |
| **Exploratory** | A proposed need worth investigating | Experimental, Candidate, or back to Proposed |
| **Experimental** | A draft solution with known limitations | Candidate, or withdrawn |
| **Candidate** | **Candidate gate** (below) | Stable, or demoted |
| **Stable** | **Stable gate** (below) | Deprecated |
| **Deprecated** | Deprecation record with migration path | Removed |
| **Removed** | MAJOR change, or emergency removal | — (terminal; traceability retained) |

## Transition matrix

*(Normative — `—` means the transition is prohibited)*

| From \ To | Proposed | Exploratory | Experimental | Candidate | Stable | Deprecated | Removed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Proposed** | — | Yes | Yes | Yes¹ | **—** | — | — |
| **Exploratory** | Yes² | — | Yes | Yes¹ | **—** | — | — |
| **Experimental** | Yes² | Yes² | — | Yes¹ | **—** | — | Yes³ |
| **Candidate** | — | Yes² | Yes² | — | Yes¹ | Yes | Yes³ |
| **Stable** | — | — | — | Yes² | — | Yes | **—**⁴ |
| **Deprecated** | — | — | — | — | Yes² ⁵ | — | Yes |
| **Removed** | — | — | — | — | — | — | — |

¹ Requires the corresponding gate and Human Maintainer approval.
² Demotion — permitted, but requires documented rationale.
³ Only for artifacts that never reached Stable; no deprecation obligation.
⁴ **Stable may never go directly to Removed** — deprecation first (DEC-S-040),
except under emergency removal.
⁵ Un-deprecation is possible but requires the Stable gate again.

### Transition rules

*(Normative, DEC-S-036)*

1. **No artifact promotes itself.** Every promotion is an approval by the Human
   Maintainer after Nova review.
2. **Stable is unreachable from Proposed, Exploratory, or Experimental.**
   Candidate is mandatory — it is the only state where a bounded, honest failure
   is cheap.
3. **Candidate and Stable require evidence and explicit Human Maintainer
   approval.**
4. **Demotion is always allowed**, and requires documented rationale. Demoting is
   a healthy act, not an admission of failure.
5. **Deprecation and removal require impact and migration assessment.**
6. **Maturity, release version, and publication state stay separate.**

## Minimum Candidate gate

*(Normative — all required)*

| # | Requirement |
| --- | --- |
| 1 | Problem and scope stated |
| 2 | Normative documentation exists |
| 3 | Ownership assigned |
| 4 | Source revision identified |
| 5 | Known accessibility requirements stated |
| 6 | Known risks registered |
| 7 | Evidence plan |
| 8 | Consumer validation plan |
| 9 | Provenance |
| 10 | Open limitations stated honestly |

Requirement 10 is a gate, not a footnote: a Candidate that claims no limitations
has not been examined.

## Minimum Stable gate

*(Normative — all required, in addition to the Candidate gate)*

| # | Requirement |
| --- | --- |
| 1 | Candidate gate satisfied |
| 2 | Implementation or render evidence, where applicable |
| 3 | **Accessibility evidence per the later policy** |
| 4 | At least one bounded consumer validation |
| 5 | Migration and compatibility statement |
| 6 | No unresolved critical deviations |
| 7 | Human Maintainer approval following Nova review |

### The accessibility blocker

Requirement 3 **cannot currently be satisfied**. The accessibility target and its
evidence method do not exist (CR-024, CDS-WP-007).

Therefore: **no artifact with an accessibility obligation can reach Stable
today.** This is recorded, not worked around (RISK-028). It is a real constraint
on the roadmap, and Nova may wish to advance CDS-WP-007.

## No retrospective maturity

*(Normative)*

**CDS-WP-006 declares no existing artifact Candidate or Stable.**

Defining a lifecycle does not populate it. Every artifact currently in CDS is at
most `Proposed` or `Exploratory` until it passes a gate — governance documents
included. Nothing acquires maturity by having existed before the policy.

This prevents the specific failure where writing the lifecycle is mistaken for
having run it (RISK-031, RISK-040).

## Demotion

Permitted from any state; requires: rationale · affected version or revision ·
consumer impact · notification path where consumers exist · Human Maintainer
approval.

Demotion is the correct response to evidence that a promotion was premature. It
is cheaper than defending an inaccurate state, and is expected during
CDS-WP-005's architecture validation.

## Deprecation and removal

Summarised here; governed by the
[Versioning, Compatibility and Deprecation Policy](VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md).

- A **Stable** artifact must be Deprecated before regular removal (DEC-S-040).
- Regular removal of a Stable contract is a **MAJOR** change.
- Removal requires migration information and Human Maintainer approval.
- **Emergency removal** is narrowly bounded — see the versioning policy.
- Removed artifacts retain historical traceability. Removal deletes availability,
  never the record.

## Related documents

- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
- [Versioning, Compatibility and Deprecation Policy](VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md)
- [Release and Change Control Policy](RELEASE_AND_CHANGE_CONTROL_POLICY.md)
- [Adoption, Conformance and Claims Policy](ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md)
- [Design System Architecture](../architecture/DESIGN_SYSTEM_ARCHITECTURE.md)
