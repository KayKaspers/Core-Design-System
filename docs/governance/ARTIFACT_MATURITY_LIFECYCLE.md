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
| 5 | Known accessibility requirements stated, per the [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) — incl. the **Candidate accessibility gate** (mapping, responsibility, **AE-1**, AE-2 or plan, limitations, baseline plan, regression plan) |
| 6 | Known risks registered |
| 7 | Evidence plan |
| 8 | Consumer validation plan |
| 9 | Provenance |
| 10 | Open limitations stated honestly |

Requirement 10 is a gate, not a footnote: a Candidate that claims no limitations
has not been examined.

## Reaching the Candidate gate — Proposed Candidate Revisions (CDS-WP-016)

*(Additive, normative, DEC-S-126. This section defines **how** a proposed change
reaches the Candidate gate. It **waives no gate**, removes **no** Candidate
requirement, and changes **no** Stable requirement.)*

A Candidate promotion often requires the artifact's own bytes to declare the
Candidate state — a Candidate source revision and Candidate/Approved metadata —
while the gate simultaneously requires revision-bound evidence for exactly those
bytes. Without a named intermediate state, the only way in is an unevidenced,
unapproved preparatory commit, which rule 1 above forbids. The intermediate state
is named here instead.

### Proposed Candidate Revision

| Property | Rule |
| --- | --- |
| **What it is** | An explicitly identified revision of an artifact, prepared as uncommitted working-tree or equivalent review material, intended to become the Candidate. |
| **What it is not** | Current maturity · current approval · a claim · a release · distributable current CDS Source · consumer-authoritative. |
| **Metadata** | Its bytes **may** carry the intended future `Candidate`/`Approved` metadata, **only** where the surrounding context states explicitly that this is the **proposed future state** and not the current authoritative repository state. |
| **Authority** | **None.** Proposed Candidate Bytes are not Candidate authority; target metadata is not current maturity. |
| **Maturity while it exists** | The artifact's maturity is unchanged — typically **Experimental** — for as long as the proposal is not integrated. |

Evidence may be produced against a Proposed Candidate Revision only under the
exact-byte binding conditions of DEC-S-126: the evidence package must bind the
exact proposed bytes by identity, revision, path, raw SHA-256, canonical digest
where applicable, tooling revision, and deterministic execution. Such evidence is
an **Evidence Candidate** until it is independently reviewed and admitted by the
Human Maintainer. **Evidence never transfers across a source revision.**

### Candidate approval pending exact-byte integration

A Candidate approval may be reached **before** integration. It is recorded as
**`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`** in an instance of the
[Candidate Approval Record Template](../operations/CANDIDATE_APPROVAL_RECORD_TEMPLATE.md),
and it means: *these exact bytes are approved for Candidate, conditional on their
unmodified integration.*

**While that state holds, the repository is not Candidate.** Maturity, approval,
and consumer promise are unchanged.

The order of authority steps is fixed (DEC-S-126): proposed bytes → fresh
revision-bound evidence → fresh independent evidence review → **Human-Maintainer
evidence admission** → Nova finalization review → **Human-Maintainer Candidate
approval** → **exact-byte Promotion Commit** → post-commit verification. Evidence
admission and Candidate approval are **separate** Human-Maintainer decisions, and
admission **precedes** approval.

### Effectivity — the Promotion Commit

**The Promotion Commit is the actual repository maturity transition point.**

`Experimental → Candidate` in the transition matrix above becomes effective when,
and only when, the Human Maintainer integrates the exact approved bytes. Before
that moment the artifact is Experimental regardless of what any record, any
review, or any metadata inside the proposed bytes says. Rule 1 is unchanged: no
artifact promotes itself, and no document promotes one either.

### Exact-byte invalidation

Any difference between the approved, reviewed, and evidenced Candidate bytes and
the integrated source **invalidates** the pending approval. Fresh evidence, a
fresh independent review, a fresh admission, and a fresh approval are then
required. **There is no "small fix" exemption** — a whitespace change, a
reordering, and a trailing-newline change all count.

Where the committed bytes **are** identical, the mandatory post-commit
verification confirms the same evidence binding and does not by itself require a
second evidence, review, and admission cycle solely because Git persisted
already-reviewed exact bytes.

### What this section does not do

It grants **no** Candidate, creates **no** Proposed Candidate Revision, and
authorizes **no** promotion. The Semantic Status Foundation remains **Candidate:
No · Experimental · Unapproved**, at authoritative source revision
`semantic-status-rev-0001`; `semantic-status-rev-0002-candidate` is a **reserved
future identity that has not been created**.

## Minimum Stable gate

*(Normative — all required, in addition to the Candidate gate)*

| # | Requirement |
| --- | --- |
| 1 | Candidate gate satisfied |
| 2 | Implementation or render evidence, where applicable |
| 3 | **Accessibility evidence** per the [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md): **AE-2 complete + AE-3 against a declared support baseline** + consumer evidence + no critical limitations |
| 4 | At least one bounded consumer validation |
| 5 | Migration and compatibility statement |
| 6 | No unresolved critical deviations |
| 7 | Human Maintainer approval following Nova review |

### The accessibility blocker

*(Reconciled by CDS-WP-007)*

Requirement 3 **still cannot be satisfied** — but for a different reason than
before.

| | Before CDS-WP-007 | After CDS-WP-007 |
| --- | --- | --- |
| **Target** | Did not exist | **WCAG 2.2 Level AA** for the applicable web scope (DEC-S-049) |
| **Evidence method** | Did not exist | **AE-0 … AE-4** (Evidence and Claims Model) |
| **Blocker** | *"Against what?"* | *"Show it."* |

The target and the evidence method now exist, and so does the support baseline:
**A11Y-BL-001 is declared and committed** (CDS-WP-010). **Almost no evidence
exists.** Every CDS artifact is **AE-0** except the channel-independent Semantic
Status Layer-3 source/contract family, which holds admitted **AE-1** structural and
automated evidence — and a declared baseline is a test contract, never evidence,
support, or conformance — so **AE-2 and AE-3 do not exist anywhere**, and Stable
remains unreachable (RISK-044, RISK-048).

Therefore, unchanged in effect: **no artifact with an accessibility obligation
can reach Stable today**, and the Candidate accessibility gate is equally unmet.
This is recorded, not worked around (RISK-028).

**CDS-WP-007 promoted no artifact.** A policy is an input to a gate, never a pass
through one — and defining a target proves nothing (DEC-S-050).

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
- [Candidate Approval Record Template](../operations/CANDIDATE_APPROVAL_RECORD_TEMPLATE.md)
