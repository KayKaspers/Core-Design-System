# Governance Affordability and Operating Readiness

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-008 — Foundation Milestone Review
- **Reviewed revision:** `7b71652`
- **Date:** 2026-07-16
- **Status:** **Review evidence — not a normative source.** This document assesses
  whether the committed governance can be *operated*; it changes no policy.

## Purpose

The governance model (CDS-WP-006) is complete and internally consistent. The open
question this review must answer is different: **can a very small maintainer
group actually run it?** An unaffordable governance model fails not by being
wrong but by being bypassed (RISK-040).

**No policy is changed here.** Where simplification is suggested, it is a
recommendation to Nova and the Human Maintainer, never an edit.

## Current governance complexity

*(Counts re-derived from the committed governance sources.)*

| Element | Count | Source |
| --- | --- | --- |
| Roles | 6 | [Governance Operating Model](../governance/GOVERNANCE_OPERATING_MODEL.md) |
| Tracks | 2 (Standard, Elevated) | DEC-S-033 |
| Approval gates | 9 | maturity ×2, versioning/release, publication, licensing, exception, product-profile, contribution, risk |
| Maturity states | 7 | DEC-S-035 |
| Publication states | 5 | DEC-S-046 |
| Claim types | 4 | DEC-S-044 |
| Licence artifact classes | 10 | DEC-S-047 |
| Change classes | 6 | DEC-S-048 |
| Compatibility axes | 8 | DEC-S-039 |
| Decisions in force | 60 | [Decision Index](../decisions/DECISION_INDEX.md) |
| Risks in force | 48 | [Risk Register](../risks/RISK_REGISTER.md) |

This is a **large** governance surface for a group whose only guaranteed roles
today are the **Human Maintainer** and **Nova**, with **Claude** as a scoped
documentation executor. Three of the six roles (Consumer Maintainer, Contributor,
Evidence Reviewer) are **not yet staffed** by anyone active.

## The nine approval gates

| Gate | Track | Minimum human approval |
| --- | --- | --- |
| Candidate maturity | Standard/Elevated | Human Maintainer after Nova review |
| Stable maturity | Elevated | Human Maintainer after Nova review |
| Versioning / release | Elevated | Human Maintainer |
| Publication-state change | Elevated | Human Maintainer + gate |
| Licensing decision | Elevated | Human Maintainer |
| Exception approval | Elevated | Human Maintainer |
| Product Profile approval | Elevated | Human Maintainer |
| Contribution acceptance | Standard/Elevated | Human Maintainer |
| Risk acceptance/closure | — | Human Maintainer only |

**Every gate terminates at the Human Maintainer.** That is correct for authority
but concentrates all approval load on one person — the core affordability tension.

## Ceremony versus obligation

The model's own principle (DEC-S-033) is **"ceremony scales; obligations do
not."** The obligations that hold in **both** tracks — authority boundaries,
traceability, evidence, human approval, fail-closed — are **not reducible**, and
this review does **not** propose reducing them. What *can* scale is the **ceremony
around them**: how many separate artifacts a change must produce, and how much of
that is duplicated.

## Dry Run A — Editorial correction

*Example: fixing an inaccurate sentence in a non-breaking governance document.*

| Aspect | Finding |
| --- | --- |
| Track | Standard (Editorial change class) |
| Roles required | Claude (executor) → Nova (review) → Human Maintainer (commit) |
| Evidence required | The corrected text and a one-line rationale |
| Approval | Human Maintainer commit |
| Mandatory governance artifacts | ~1 (changelog entry) |
| Duplicate work | None |
| Possible simplification | None needed |
| **Result** | **Operational** |

The Standard track handles the most common change cleanly. This is the affordable
core of the model and it works.

## Dry Run B — Additive Candidate artifact

*Example: a new bounded foundation or component Candidate, no breaking change.*

| Aspect | Finding |
| --- | --- |
| Track | Standard → touches an Elevated trigger (Candidate maturity) ⇒ **Elevated** |
| Roles required | Claude, Nova, Human Maintainer; Evidence Reviewer (≠ author) |
| Evidence required | Candidate gate: problem/scope, normative doc, ownership, source revision, **accessibility mapping + Candidate accessibility gate**, risks, **evidence plan**, consumer-validation plan, provenance, limitations |
| Approval | Human Maintainer after Nova review |
| Mandatory governance artifacts | ~8–10 (Candidate gate items, accessibility mapping, risk entries, changelog, traceability) |
| Duplicate work | Accessibility mapping restated across policy, matrix, and artifact; provenance restated across manifest and artifact |
| Possible simplification | A **single Candidate template** that composes the gate items once; a reusable accessibility-mapping stub referencing the matrix rather than restating it |
| **Result** | **Operational with simplification notes** |

Reaching Candidate is achievable, but the artifact count is high and some
restating is avoidable. A template would preserve every gate while cutting the
ceremony.

## Dry Run C — Elevated Product Profile or accessibility-relevant change

*Example: a Product Profile with accessibility impact, or a Stable-relevant
contract change.*

| Aspect | Finding |
| --- | --- |
| Track | Elevated |
| Roles required | Claude, Nova, Human Maintainer, Evidence Reviewer, Consumer Maintainer (for a profile) — **5 roles, 3 unstaffed today** |
| Evidence required | Full Candidate gate **plus** AE-2 + **AE-3 against a declared support baseline** + consumer evidence + anti-fragmentation review + compatibility declaration + migration + limitations |
| Approval | Human Maintainer after Nova review; profile separately governed |
| Mandatory governance artifacts | ~15+ |
| Duplicate work | Accessibility evidence, compatibility, and limitation records each restated in profile, artifact, and claim contexts |
| Possible simplification | None **at the obligation level** — every item guards a real risk. Ceremony could be reduced by **one combined Elevated dossier** rather than many separate documents |
| **Result** | **High burden** |

This path is where affordability is genuinely strained. It is **not currently
executable end-to-end** because AE-3 needs a support baseline that does not exist
(RISK-044) and three required roles are unstaffed — but that is a **prerequisite
gap, not a broken process**. When those prerequisites exist, the burden remains
high, and the honest response is a **smaller scope**, not a weaker gate
(DEC-S-059).

## Recognised duplicate work

- **Accessibility mapping** is expressed in the policy, the applicability matrix,
  the architecture alignment, and would be restated per artifact.
- **Provenance** is expressed in the manifest, the provenance policy, and per
  artifact.
- **Compatibility and limitations** recur across artifact, profile, and claim.

None of these is *wrong* — each serves a distinct authority — but a small team
will feel the restating. Templates and by-reference citation (rather than
re-statement) are the safe simplification.

## Small-maintainer limits

- **All approval concentrates on one person.** Throughput, not correctness, is the
  constraint (RISK-029).
- **Three of six roles are unstaffed.** Elevated changes needing a distinct
  Evidence Reviewer or a Consumer Maintainer cannot proceed until those roles are
  filled — by policy, the Evidence Reviewer may **never** be the author (DEC-S-045).
- **48 risks, 0 mitigating, 0 named executors.** The register is currently a
  catalogue, not an operating instrument — exactly the RISK-040 failure mode,
  recorded openly rather than hidden.

## Risk assessment (operating-relevant)

| Risk | Relevance | Assessment |
| --- | --- | --- |
| **RISK-026** Architecture overdesign | Medium | The architecture is broad but each element traces to a requirement; the *governance* surface is the sharper overdesign exposure, not the architecture. |
| **RISK-029** Governance bottleneck & maintainer overload | **High** | The central affordability risk. Single-approver concentration is real and present. |
| **RISK-040** Ceremonial risk governance | **High** | Already materialising: two work packages added 20 risks and treated none; 0 executors. |
| **RISK-048** Accessibility evidence burden | **High** | Dry Run C confirms the Elevated + accessibility path is the most burdensome and the most likely to invite prohibited shortcuts. |

**No risk status is changed** by this review. These are assessments for Nova's
control, not acceptances or closures.

## Operating-readiness conclusion

**Partially met.** The governance is **correct and internally applicable** — the
Standard track is operational, and the Elevated track is *definable and
consistent*. It is **not yet comfortably operable at Elevated scope** for the
current staffing, and the risk register is not yet run as an instrument.

This is an **operating concern, not a normative inconsistency**, and therefore
**not a Foundation blocker**. It is the single most important thing to address
*before* the first Candidate or pilot, and it is carried forward as a mandatory
next-phase note (FM-F findings in
[Open Gaps and Dependencies](FOUNDATION_OPEN_GAPS_AND_DEPENDENCIES.md)).

### Recommended simplifications (for Nova / Human Maintainer decision — not applied here)

1. A **single Candidate dossier template** and a **single Elevated dossier
   template** that compose existing gate items once.
2. **Cite the matrix/policy by reference** from artifacts instead of restating
   accessibility mappings.
3. On any change moving to `Mitigating`, **require a named executor and trigger**
   (already policy — make it the operating default).
4. Keep a **short operating playbook** distinct from the normative policies, so the
   day-to-day path is not re-derived from 60 decisions each time.

## Related documents

- [Foundation Milestone Review](FOUNDATION_MILESTONE_REVIEW.md)
- [Foundation Completeness Matrix](FOUNDATION_COMPLETENESS_MATRIX.md)
- [Governance Operating Model](../governance/GOVERNANCE_OPERATING_MODEL.md)
- [Risk Register](../risks/RISK_REGISTER.md)
