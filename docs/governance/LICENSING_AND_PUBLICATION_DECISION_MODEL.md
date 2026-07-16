# Licensing and Publication Decision Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-006
- **Date:** 2026-07-16
- **Status:** **Normative** for how licensing and publication are decided

## Purpose and hard boundary

Defines **how** licensing and publication decisions are made — and decides
**neither**.

> **No licence is selected. No `LICENSE` file is created. No publication is
> approved. The current publication state is `Private Development` and this work
> package does not change it.**

This document supplies the decision model that has had **no assigned work package
since CDS-WP-002** flagged the gap.

Frame: [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md).

## Why licensing is not one decision

*(Normative, DEC-S-047)*

The benchmark found this consistently: documentation, code, fonts, icons, and
brand assets routinely sit on **different terms**, and brand assets are the most
restricted category almost everywhere. One reviewed system states a permissive
licence for repository files while fonts and icons are governed by a **separate
assets licence agreement**.

Treating "the licence" as a single choice is therefore not a simplification — it
is an error that fails at exactly the point brand assets are involved.

## The ten artifact classes

*(Normative — each decided independently)*

| # | Class | Typical distinctive concern |
| --- | --- | --- |
| 1 | **Documentation** | Reuse, attribution, derivative works |
| 2 | **Source Code** | Reuse, modification, redistribution, patents |
| 3 | **Machine-readable Tokens and Metadata** | Are approved values data, code, or brand? |
| 4 | **Components and Reference Implementations** | Reuse and modification |
| 5 | **Icons** | Frequently third-party or restrictively licensed |
| 6 | **Fonts** | **Usually separately licensed; often not redistributable** |
| 7 | **Illustrations and Images** | Origin and model or property rights |
| 8 | **Templates for Documents, Reports and Presentations** | Reuse of the template versus its content |
| 9 | **Examples and Samples** | Reuse without implying support |
| 10 | **Logos, Marks and Brand Assets** | **Trademark, not copyright. Usually not licensed for reuse at all.** |

Classes 6 and 10 are where naive licensing breaks. Fonts are commonly licensed on
terms that forbid redistribution outright; logos are trademarks whose whole
purpose is to **not** be freely usable.

## Rights and licence matrix

*(Normative — required per class before any public state)*

| # | Field | Question |
| --- | --- | --- |
| 1 | Owner | Who holds the rights? |
| 2 | Origin | Where did it come from? |
| 3 | Third-party Content | Anything not ours? |
| 4 | Intended Use | What should consumers be able to do? |
| 5 | Modification Rights | May it be changed? |
| 6 | Redistribution Rights | May it be passed on? |
| 7 | Trademark or Brand Restrictions | What is protected regardless of licence? |
| 8 | Attribution Requirements | What must a consumer state? |
| 9 | Selected Licence or Usage Terms | **Undecided for every class** |
| 10 | Compatibility with Distribution Model | Do the terms permit the intended distribution? |
| 11 | Approval State | Human Maintainer decision |

**Field 9 is undecided for all ten classes.** That is the current, accurate state.

## Licensing rules

*(Normative)*

| Rule | Consequence |
| --- | --- |
| **Licensing is not one decision** | Ten classes, ten decisions (DEC-S-047). |
| **No automatic inheritance** | A code licence never governs documentation, tokens, fonts, icons, templates, examples, or brand assets. |
| **Brand assets stay separate** | Trademark is not a licensing afterthought. |
| **Repository presence grants nothing** | No file becomes freely usable by being committed. |
| **Unknown or conflicting rights block publication** | Fail closed — this is absolute (RISK-038). |
| **Only the Human Maintainer selects terms** | Nova recommends; Claude never proposes a licence. |
| **Third-party provenance must be established first** | Unclear provenance is unclear rights. |

## Third-party provenance

Before any public state, per artifact: origin identified · rights holder known ·
terms known and compatible with intended use · attribution obligations recorded ·
redistribution permitted for the intended distribution · **modifications
permitted if CDS modifies it**.

**Unknown provenance is not "probably fine". It is a publication blocker.**

## Publication states

*(Normative, DEC-S-046 — exactly five)*

| # | State | Meaning |
| --- | --- | --- |
| 1 | **Private Development** | Not publicly released. **Current state.** |
| 2 | **Controlled Preview** | Bounded, named recipients. No general support or compatibility commitment. |
| 3 | **Public Preview** | Publicly accessible, not Stable, with clear limitation marking. |
| 4 | **Public Stable** | Publicly released with documented maturity, compatibility, licence, and support statements. |
| 5 | **Archived** | No active development or regular adoption. |

**These states are not a roadmap.** Listing them commits CDS to nothing — no
sequence, no schedule, no intention to reach any of them.

### Current state

> **`Private Development`.**
>
> **CDS-WP-006 does not change it.**

## Publication gate

*(Normative — required before any move to a more public state)*

| # | Requirement |
| --- | --- |
| 1 | Approved scope |
| 2 | Source revision |
| 3 | Artifact manifest |
| 4 | Maturity declaration |
| 5 | Compatibility declaration |
| 6 | Changelog |
| 7 | Migration information, where relevant |
| 8 | **Licence and rights review per artifact class** |
| 9 | **Third-party provenance** |
| 10 | Security and privacy review, where relevant |
| 11 | **Accessibility statement** per the [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) |
| 12 | Support and maintenance statement |
| 13 | Claim restrictions |
| 14 | Nova review |
| 15 | **Human Maintainer approval** |

### Currently unmet

Requirements **8 and 9 cannot be satisfied today**:

- **8 and 9** — no licensing decision exists for any of the ten classes
  (DEC-S-047).

**Therefore no publication-state change is possible.** The
**publication state remains `Private Development`.** Recorded, not worked around.

#### Requirement 11 — reconciled by CDS-WP-007

Requirement 11 was previously unmet because no accessibility target existed. It
is **now definable**: the policy exists, and the statement is simply *what the
policy says*.

What it would have to say is unflattering, and that is the point:

> **Nothing has been tested. Every CDS artifact is AE-0. No support baseline is
> declared. No accessibility claim of any level is valid.**

An accessibility statement is **a disclosure obligation, not a quality claim**
(DEC-S-050). Requirement 11 becoming satisfiable **does not move CDS toward
publication** — it means CDS could now honestly describe its accessibility as
*unknown*. Publication remains blocked by 8 and 9 regardless.

### Gate rules

- **Repository visibility is not a publication state.** Making a repository
  public does not move CDS to Public Preview — it would simply be publication
  without a gate (RISK-039).
- Release maturity does not imply publication. The axes are independent
  (DEC-S-035).
- Each step toward more public requires its own gate pass.
- A move toward **less** public (for example to Archived) still requires a
  decision, but not this gate.
- Failing the gate means **NO-GO**, not "go with notes".

## Publication and support honesty

Publication implies availability, and availability implies expectation. CDS must
therefore state plainly, at any public state, what it does **not** offer:

- what is Stable and what is not (DEC-S-035),
- what compatibility is declared, per axis (DEC-S-039),
- what support exists — currently none,
- what claims are permitted (DEC-S-044),
- what is **not** licensed for reuse — particularly brand assets.

**No pressure to adopt, no implied endorsement, no overstated maturity.** A
consumer must be able to decline CDS without friction, and must not be able to
mistake a preview for a commitment.

## Deliberately open decisions

*(Normative — none is decided here)*

1. Which licence, per each of the ten classes.
2. Whether CDS is published at all.
3. Which publication state, and when.
4. Whether external contribution is permitted (DEC-S-041).
5. How brand assets are protected.
6. Font rights, since fonts are frequently not redistributable.
7. Icon provenance.
8. Whether documentation and code diverge in terms.
9. What support statement, if any, is sustainable (RISK-029).
10. Trademark handling for the Core marks.

**These are Human Maintainer decisions and remain open.** No `LICENSE` file, no
`CONTRIBUTING.md`, and no publication commitment is created here.

## Related documents

- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
- [Release and Change Control Policy](RELEASE_AND_CHANGE_CONTROL_POLICY.md)
- [Adoption, Conformance and Claims Policy](ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md)
- [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md)
- [Artifact Distribution and Channel Model](../architecture/ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md)
