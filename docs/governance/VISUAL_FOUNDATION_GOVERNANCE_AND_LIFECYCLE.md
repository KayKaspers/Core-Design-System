# Visual Foundation Governance and Lifecycle

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Amended by:** CDS-WP-020 (Decision Integration Pass), 2026-08-27 — the
  *Where maturity binds, and what aggregation confers* subsection, under
  **DEC-S-131**. **That subsection is effective** at the Human-Maintainer
  exact-byte integration commit `42a568d823de3388e45af62967546f13ad67eff6`
  (2026-08-27). It **applies** AF-1 … AF-5 and adds **no** maturity rule, gate, or evidence
  requirement; AF-1 … AF-5 and VR-1 … VR-5 are unchanged.
- **Amended by:** CDS Step-9 Decision Integration Pass, 2026-09-05 — the additive
  *OD-6B disposition* note under *Governance capacity*. **That note is effective**
  at the Human-Maintainer exact integration commit
  `2cb244e889c1a6b5a278afb233995a0379b5d9ef` (2026-09-05). **It adds
  no Decision, no rule, no gate, and no construct**, registers **no** maturity
  group or aggregate gate, and grants **no** maturity; AF-1 … AF-5, VR-1 … VR-5 and
  the artifact-family model are unchanged.
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for how visual foundation artifacts are owned, changed,
  matured, validated, and retired.** It **grants no maturity**.
- **Maturity:** **`Proposed`** — this document promotes nothing.

## Purpose and boundary

This document states **how the visual foundation is governed**: who owns what, how
a change is classified, what counts as breaking, how a family matures, what
evidence each gate requires, and how something is deprecated or removed.

**It grants no maturity to anything**, admits no evidence, accepts and closes no
risk, approves no change, and creates no release.

It **introduces no governance rule**. Every rule below is an application of the
[Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md), the
[Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md), and the
[Versioning, Compatibility and Deprecation Policy](VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md)
to the visual foundation. On conflict, **those policies win** and this document is
corrected.

## Ownership

*(Normative — the six roles are unchanged)*

| Role | Authority over the visual foundation |
| --- | --- |
| **Human Maintainer** | **Decides.** Normative approval, Candidate and Stable transitions, evidence admission, risk acceptance, Product Profile acceptance, exception approval, licensing, publication, release, tag, and every Git write. **Not delegable.** |
| **Nova** | **Recommends.** Architecture, planning, review, scope and consistency checks, approval recommendations. Holds **no** Git, publication, risk-acceptance, or claim authority. |
| **Claude** | **Proposes.** Scoped local analysis and documentation only. May never activate a policy, accept a risk, approve a maturity state, or perform any Git write. Output is always a proposal. |
| **Consumer Maintainer** | Accountable **within their own project** for integration, local deviations, migration, and honest claims. Holds **no CDS core approval authority**. **Currently unstaffed** (FM-F-006). |
| **Contributor** | Supplies proposals and evidence. **Never approves their own contribution.** |
| **Evidence Reviewer** | Checks evidence against a contract. **Never the artifact itself, and never the executor of the work being evidenced.** |

**Authority is granted, never acquired** (DEC-S-033). No role gains authority over
a visual family by creating, editing, implementing, rendering, or citing it.

## The artifact-family model

*(Normative)*

Each visual foundation family (**VF-1 … VF-9**) is a **separate artifact family**
with its own maturity, evidence, gate, and compatibility statement.

| Rule | Statement |
| --- | --- |
| **AF-1** | **Maturity is never inherited.** No family acquires a state from another family, from an architecture document, from metadata that says so, from a validator pass, or from a renderer. |
| **AF-2** | **Evidence is bound to a source revision** and **never transfers** across a revision, a family, a channel, a context, or a consumer (DEC-S-126). |
| **AF-3** | **A family may mature at its own pace.** One family reaching Candidate grants nothing to any other. |
| **AF-4** | **A cross-family construct matures no faster than its weakest constituent.** The focus role set spans VF-1, VF-5, and VF-3; it is not Candidate while any of them is not. |
| **AF-5** | **An architecture document is not the artifact.** These documents describe the families; they are not the source sets, and committing them matures nothing. |

### Where maturity binds, and what aggregation confers

*(Normative — **DEC-S-131**,
[ADR-0004](../decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md),
CDS-WP-020 Decision Integration Pass, 2026-08-27. **Effective** at the
Human-Maintainer exact-byte integration commit
`42a568d823de3388e45af62967546f13ad67eff6`. It applies AF-1 … AF-5 and **adds no new maturity rule, gate, or evidence
requirement**.)*

- **The Source Set is the independently evaluable unit**, and the visual topology
  is **one source set per independently evaluable Family × Token-Flow-Layer unit**.
  A family occupying token-flow layers 1 and 2 may therefore have two.
- **Maturity binds to the pair (`sourceSetId`, `sourceRevision`)** and to nothing
  else. **A new revision inherits no evidence and no admission** (AF-2, DEC-S-126).
- **One manifest may aggregate several source sets**, and a manifest's own
  `maturityState` and `approvalState` describe **only the manifest artifact
  itself** — **not** a roll-up, **not** a maximum, **not** a minimum, **not**
  inherited in either direction.
- **AGGREGATED is not MATURE.** Declaring an inventory is a structural act; it
  confers nothing on what is inventoried, and nothing on the inventory. This is
  AF-1 restated at the point where it is easiest to lose quietly, alongside the
  three cases CDS already names: metadata is not authority (VR-4), a validator pass
  is not maturity authority (DEC-S-053), and a digest is not a signature
  (DEC-S-090).
- **A `sourceSetId` change invalidates admitted evidence** and is a migration and
  identity event; **a file move alone is not a `sourceSetId` change.**

**This changes no gate and promotes nothing.** Visual foundation source sets in
existence remain **0**, and **VF-1 … VF-9 remain `Proposed`**.

## Current maturity state

*(Normative current-state statement)*

| Item | State |
| --- | --- |
| Visual foundation source sets in existence | **0** |
| Visual foundation families at `Candidate` | **0** |
| Visual foundation families at `Stable` | **0** |
| Maturity of VF-1 … VF-9 | **`Proposed`** — a registered need with scope, no approved solution |
| Maturity of the CDS-WP-019 architecture documents | **`Proposed`** |
| Candidate artifact families in all of CDS | **1** — the channel-independent Semantic Status Layer-3 source/contract family, **not a visual family** |
| Stable artifacts in all of CDS | **0** |
| Releases · tags · publication | **None** · **0** · **`Private Development`** |

**Nothing acquires maturity by having existed before a policy** — the *No
retrospective maturity* rule applies to these documents as it applies to everything
else.

## Change classification

*(Normative — an application of DEC-S-033. **Ceremony scales; obligations do
not.**)*

| Change | Track | Why |
| --- | --- | --- |
| Correcting a typo or a broken link in a visual foundation document | **Standard** | Low-risk documentation |
| Adding a **reference primitive** that no role yet binds | **Standard** | Bounded, non-breaking addition |
| Clarifying a role's stated purpose without changing it | **Standard** | Correction |
| **Adding a semantic role** | **Elevated** | Extends the shared vocabulary; carries an accessibility obligation from the moment it exists |
| **Changing a role's declared contrast obligation or pairing set** | **Elevated** | Accessibility obligation |
| **Changing what a role means** | **Elevated** | Shared semantics |
| **Renaming or removing a role** | **Elevated** | Breaking; a migration event (DEC-S-082) |
| **Naming an extension point** | **Elevated** | Product Profile trigger |
| **Adding, changing, or removing a context** | **Elevated** | Accessibility obligation across every role |
| **Anything touching the focus role set** | **Elevated** | A CDS-alone accessibility obligation |
| **Selecting a typeface, icon set, or any external asset** | **Elevated** | Licensing, provenance, and distribution triggers |
| **Any change to a family that has reached Candidate or Stable** | **Elevated** | Maturity trigger |

> **A change that looks Standard but touches an Elevated trigger is Elevated.** The
> trigger wins over the estimate.

**In both tracks, these remain mandatory and may not be reduced:** authority
boundaries, traceability to a source revision, evidence where an obligation exists,
human approval before anything becomes normative, and fail-closed behaviour on
unclear authority or evidence.

## Compatibility and breaking changes

*(Normative — an application of DEC-S-039. Compatibility is declared **per axis**;
there is no single answer.)*

The axis that carries the visual foundation is **axis 3 — Token Contract**, with
**axis 2** (machine-readable source), **axis 5** (Product Profile), **axis 6**
(channel output), and **axis 8** (evidence) engaged as applicable.

### Breaking criteria for a visual family

| # | A change is **breaking** if it |
| --- | --- |
| **BC-1** | Removes a semantic role, or renames one without an alias and a migration path |
| **BC-2** | Changes what a role means |
| **BC-3** | Weakens or removes a declared contrast obligation, pairing, or non-colour carrier |
| **BC-4** | Removes, weakens, or obscures the focus indicator |
| **BC-5** | Removes a supported context, or makes a role unresolvable in one |
| **BC-6** | Changes the layer or dependency direction of a source set |
| **BC-7** | Removes or narrows a named extension point a profile relies on |
| **BC-8** | Changes a token's `$type` incompatibly |
| **BC-9** | Alters a source-set identity or source revision in a way that invalidates admitted evidence |

**BC-3 and BC-4 are the ones a design system breaks accidentally**, usually while
adjusting values that look purely aesthetic. They are breaking because a consumer's
conformance capability depends on them.

### Compatibility statements

`Compatible` · `Compatible with documented limitations` · `Migration required` ·
`Breaking` · `Not applicable` · **`Not yet assessed`**.

> **`Not yet assessed` must never be read as compatible**, and must survive into
> the release record. Rounding it up because nothing broke in testing is exactly
> RISK-032.

**Every visual foundation axis is `Not yet assessed` today**, because there is
nothing to assess.

### Pre-1.0 position

CDS is **pre-1.0**. **No blanket long-term backward-compatibility promise exists**
for any visual family. Pre-1.0 removes the *compatibility promise*; it removes
**none** of the following, which remain mandatory: breaking changes are identified
as breaking, migrations are documented, source revisions are bound, and
deprecations are handled traceably.

**No v1.0.0 is scheduled, implied, or asserted.**

## Maturity path for a visual family

*(Normative — the existing gates, applied. **This is a route to a gate, never a
pass through one.**)*

```text
Proposed  →  Exploratory  →  Experimental  →  Candidate  →  Stable
                                                  ↓            ↓
                                              Demoted     Deprecated → Removed
```

| Transition | Requires |
| --- | --- |
| **Proposed → Exploratory / Experimental** | A registered need, then a draft solution with known limitations |
| **Experimental → Candidate** | The **Minimum Candidate gate** (10 requirements), including the **Candidate accessibility gate**; fresh revision-bound evidence; an **independent review by a reviewer who is not the executor**; **Human-Maintainer evidence admission**; Nova review; **Human-Maintainer Candidate approval**; and the **exact-byte Promotion Commit** that makes it effective (DEC-S-126) |
| **Candidate → Stable** | The **Minimum Stable gate**, including **AE-2 complete + AE-3 against a declared support baseline**, consumer evidence, and no critical limitations |
| **Any → demoted** | Documented rationale. **Demotion is always allowed and is a healthy act** |
| **Stable → Deprecated → Removed** | A deprecation record with a **viable migration path**; regular removal of a Stable contract is a **MAJOR** change |

### The blocker, stated plainly

**No visual family can reach Stable**, and the reason is not procedural:

- **AE-2 and AE-3 exist nowhere in CDS.**
- **No baseline environment has ever been exercised.** A11Y-BL-001 is a **test
  contract, not evidence**.
- **No consumer validation exists**; the CoreOps pilot is **inactive**.

**No visual family can reach Candidate today either**, because no visual artifact
exists to evidence. **This is recorded, not worked around** (RISK-028, RISK-044,
RISK-048).

## Evidence expectations

*(Normative — an application of the Accessibility Evidence and Claims Model)*

| Gate | Minimum evidence | Present for any visual family? |
| --- | --- | --- |
| **Candidate** | **AE-1** structural and automated evidence, revision-bound, independently reviewed and **admitted** | **No** |
| **Stable** | **AE-2** complete **+ AE-3** against a declared baseline **+** consumer evidence | **No — nowhere in CDS** |
| **Product Profile** | Scope-appropriate accessibility evidence | **No** |
| **Any claim** | Scope, versions, and an evidence bundle, approved by the Human Maintainer | **No claim is valid** |

| Rule | Statement |
| --- | --- |
| **EV-1** | **An automated check is never sufficient** (DEC-S-053). A validator pass is input to a review, never consent. |
| **EV-2** | **A digest is not a signature** and proves no authorship, approval, or release. |
| **EV-3** | **Evidence must be reported only at the level it actually reaches.** `Not tested` must remain available and be used. |
| **EV-4** | **Absence of a failure is not evidence of success.** |
| **EV-5** | **Evidence never transfers** across a source revision, family, channel, context, or consumer. |
| **EV-6** | **The Evidence Reviewer may never be the executor** of the work being evidenced. |
| **EV-7** | **Rendering evidence is required** for reflow, resize, magnification, target size, focus visibility, and print degradation — none of which is structurally checkable. That evidence is **CDS-WP-031's** and does not exist. |

## Validation responsibilities

*(Normative as a **requirement statement**. **CDS-WP-019 changes no validator, adds
no schema, and introduces no diagnostic.**)*

| Layer | What it must cover for visual sources |
| --- | --- |
| **V1 — Syntax** | Strict JSON, UTF-8, duplicate-member prohibition, file identity, no network references |
| **V2 — DTCG** | Groups, tokens, `$value` / `$type` / `$description` / `$extensions`, reference resolution, type compatibility, resolver semantics, **no preview features** |
| **V3 — CDS profile** | Naming profile, declared layer, manifest and document identity agreement, dependency graph, Product-Profile bounds, maturity and approval metadata, local cross-file binding |
| **V4 — Semantic and governance** | Downward layer direction, **non-colour meaning**, accessibility relevance, Decision and Requirement traceability, provenance completeness, approved overrides only |

The visual-foundation-specific detections that later validation work must supply
are listed in each family's architecture document. They are **requirements on
CDS-WP-024**, not implementations.

| Rule | Statement |
| --- | --- |
| **VR-1** | **A pass at one layer proves nothing about the next.** |
| **VR-2** | A `Fail` or `Blocked` **stops** later layers, which are recorded **`Not assessed`** — never assumed passed. |
| **VR-3** | **No numeric or aggregate score.** A blocked layer stays individually visible. |
| **VR-4** | **Metadata coherence is not maturity authority.** A coherent `Candidate`/`Approved` pass proves internal consistency only. |
| **VR-5** | **The validation contract wins** over any implementation that diverges from it (DEC-S-102). |

## Deprecation and removal

- A **Stable** visual family must be **Deprecated before regular removal**
  (DEC-S-040); regular removal of a Stable contract is a **MAJOR** change.
- A deprecation record requires all nine fields — and **field 5, migration
  guidance, is the one that matters**: *a deprecation without a viable migration
  path is not a deprecation, it is a removal with extra steps* (RISK-033).
- **Field 6 is a boundary, not a schedule.** No support or release cadence is
  invented; CDS has no evidence for what cadence it could sustain.
- **Emergency removal** is narrowly bounded to a severe security risk, legal
  impermissibility, an **unfixable provenance or rights violation**, or
  demonstrably dangerous behaviour. For visual assets, the **provenance and rights
  ground is the realistic one** — which is why licensing and provenance are an
  Elevated gate before an asset ever enters.
- **Convenience, embarrassment, schedule pressure, and maintenance burden are not
  emergencies.**

## Override and exception limits

| Mechanism | Limit |
| --- | --- |
| **Product Profile** | Values at **named, approved** extension points only — **the set is empty** |
| **Consumer Extension** | Consumer-owned; enters CDS only by explicit acceptance (DEC-S-016) |
| **Local Exception** | Bounded, owned, **expiring**; an exception without an expiry and a migration path is *an undocumented fork wearing a label* |
| **Accessibility** | **Not waivable through an ordinary exception at all** (DEC-S-059). Not "requires stronger review" — **not approvable through that mechanism** |
| **Recurring overrides** | If several consumers need the same override, **the core is wrong** — fix the core (RISK-035, anti-fragmentation rule 3) |

## Escalation

Escalate — do not resolve locally — when: authority is unclear; normative sources
conflict; evidence is missing, contradictory, or unreviewable; a change looks
Standard but touches an Elevated trigger; a role would approve its own work; an
override would weaken accessibility or status truth; a claim cannot be
substantiated; or a risk requires acceptance.

Path: **Claude records and reports → Nova reviews and recommends → Human Maintainer
decides.** While an escalation is open, the affected state is **not releasable and
not distributable**.

## Governance capacity

*(A normative constraint, not an aspiration)*

Final authority rests with **one Human Maintainer** (DEC-S-005), and that is a real
bottleneck (RISK-029). Nine visual families, each with its own maturity, evidence,
and gate, is **a substantial governance load that has never been run**.

- **Ceremony that produces no decision should be removed, not defended** (RISK-040).
- **Prefer removing structure that earns nothing over defending it** (RISK-026).
- **Bottleneck pressure is never a reason to bypass a gate.** It is a reason to
  reduce ceremony, or to widen authority through an explicit, governed decision.
- **Fewer families that actually reach a gate beat nine that do not.** Whether all
  nine are worth maturing separately is a real question for CDS-WP-020, and this
  document does not pre-answer it. **DEC-S-131 does not pre-answer it either:** it
  fixes the *unit* of evaluation, not how many families CDS chooses to mature. That
  question stays open as **OD-6**, and the cost basis it rests on has been
  corrected — per-family, per-layer source sets do **not** multiply manifests,
  because one manifest may aggregate many source sets.

### OD-6B disposition — 2026-09-05

*(An additive dated note. **It changes no rule**, registers no new construct, and
**adds no Decision** — AF-1 … AF-5 and the artifact-family model above are
unchanged. Effective at the Human-Maintainer exact integration commit
`2cb244e889c1a6b5a278afb233995a0379b5d9ef`.)*

The maturity-granularity half of **OD-6** — how many families mature separately — is
**answered by the existing normative authority on this page**, and the Human
Maintainer confirmed it on 2026-09-05 as requiring **no new Decision**:

> **VF-1 … VF-9 remain separate artifact families**, each retaining **its own
> maturity, its own evidence, its own gate, and its own compatibility statement**.
> **AF-1**, **AF-3** and **AF-4** are unchanged and binding.

**Administrative batching may occur.** Evidence preparation, independent review, and
Human-Maintainer sessions may be scheduled together as a convenience. But:

> **BATCHED REVIEW ≠ SHARED MATURITY.**
> **BATCHED GATE PREPARATION ≠ MATURITY INHERITANCE.**

**One family passing grants nothing to any other.** Each family passes its own gate
on its own evidence, bound to its own (`sourceSetId`, `sourceRevision`). **No
maturity group, no family-cluster maturity, no roll-up maturity, no inherited
maturity, and no aggregate gate exists or may be created.** A family CDS does not
pursue simply **stays `Proposed`**, which asserts nothing and costs nothing. **How
many families CDS chooses to pursue, and in what order, is a scheduling and
authorization matter settled work package by work package — never a maturity rule.**

## Risks this governance is answering

*(Existing registered risks. **No new risk is registered by CDS-WP-019**, and none
is accepted or closed.)*

| Risk | Relevance to the visual foundation |
| --- | --- |
| **RISK-003** Premature design decisions | The reason no value is chosen here |
| **RISK-021** Token and override proliferation | Nine families multiply faster than they can be governed |
| **RISK-022** Existing-product reconciliation failure | Consumers already hold visual decisions |
| **RISK-024** Channel divergence | Nine channels × nine families |
| **RISK-026** Architecture overdesign | The capacity question above |
| **RISK-027** Product-profile fragmentation | The empty extension-point set is the current control |
| **RISK-028** Deferred accessibility policy creates architecture debt | Accessibility appears here as a structural constraint, not a threshold |
| **RISK-031** Maturity inflation | AF-1 … AF-5 exist to prevent it |
| **RISK-041** Accessibility target mistaken for conformance | Restated in every visual document |
| **RISK-046** Non-web channel accessibility gap | Four of nine channels have no profile |
| **RISK-060** Cross-layer dependency violation | The prohibited-dependency rules |
| **RISK-061** Token identifier collision | The naming model |
| **RISK-087** Visual-only status encoding | VF-I-5, VF-I-6 |
| **RISK-091** Semantic status tokens mistaken for visual tokens | The status boundary |

## Related documents

- [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Accessibility Mapping](VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md)
- [Visual Foundation Brand and Product Profile Boundary](VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md)
- [Visual Foundation Channel Mapping](VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
- [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md)
- [Versioning, Compatibility and Deprecation Policy](VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Machine-Readable Validation Contract](../architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)
- [Risk Governance Model](RISK_GOVERNANCE_MODEL.md)
