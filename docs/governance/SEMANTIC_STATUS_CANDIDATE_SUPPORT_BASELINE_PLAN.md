# Semantic Status Candidate — Support Baseline Plan

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Accessibility Gate Remediation
- **Date:** 2026-08-17
- **Baseline bound:** **A11Y-BL-001**
  ([Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md))
- **Baseline revision:** the revision declared 2026-07-16 and committed with
  CDS-WP-010 (`abe84b6b7267b8b9c5f96609e7c9d1ad1e68bc0a`). **No newer A11Y-BL
  revision exists**; none is proposed here.
- **Baseline freshness state:** **`Current`**, determined on 2026-08-17 by the
  [WP-016 Baseline Freshness Review](../reviews/WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md)
  (maintenance-policy trigger 1) against official primary sources.
- **Status:** **Plan — NOT normative, NOT evidence, NOT a support claim.**

## The three sentences that govern this document

> **A baseline is not evidence** (DEC-S-065).
> **A listed environment is not a supported environment** (DEC-S-069).
> **A `Current` baseline is not an accessibility pass.**

Declaring a baseline records *what future evidence will be produced against*. It
establishes nothing about any artifact. Every CDS artifact remains **AE-0**, with
exactly one bounded exception — the channel-independent Semantic Status Layer-3
source/contract family holds admitted **AE-1**
(`AE1-CDS-WP016-SEMSTATUS-002`, source scope only), which was **not** produced in
any baseline environment. **No baseline environment has been exercised**, and no
environment is supported.

## What this plan does

Requirement 7 of the [Candidate accessibility gate](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md#candidate-accessibility-gate):
it binds the Semantic Status Candidate scope to A11Y-BL-001, and states —
honestly and per entry — which parts of the Required baseline are applicable to a
**channel-independent, non-rendered source and contract family today**, and which
become applicable only when a representation exists.

It **changes no baseline composition, tier, family, or declared scope.** Such a
change is Elevated and requires Nova review and Human-Maintainer approval.

## Candidate scope against the baseline's declared scope

| Baseline declared scope | Semantic Status Candidate | Fit |
| --- | --- | --- |
| Channels: Web Product UI · Web Documentation | **None.** Per DEC-S-125 this is a channel-independent Layer-3 source/contract and is **not** assigned an artificial channel. | The Candidate sits *before* the channel scope. |
| Interaction: interactive desktop web | **None.** No interactive surface exists. | Not yet reached. |
| Languages: **DE, EN** | **DE and EN** — 25/25 identifiers with both labels. | **Direct fit; applicable now.** |
| Applies to: future CDS component/pattern evidence in this scope | The Candidate is neither a component nor a pattern. | Applies to its future representations, not to it. |

The honest summary: **one of the four declared-scope dimensions (language) engages
the Candidate today.** The other three engage its future representations.

## Tier-1 Required Core Baseline — applicability per entry

*(The 13 Required categories of A11Y-BL-001, classified for this Candidate.
`Representation-triggered` means the obligation is **live and unwaived** but not
assessable until a rendered or interactive artifact exists — it is never a
waiver.)*

| # | Required category | Applicability to the Candidate today | Why |
| --- | --- | --- | --- |
| 1 | Full keyboard-only operation (no pointer) | **Representation-triggered** | Nothing is operable; a JSON source and a contract document have no keyboard surface. |
| 2 | A supported desktop OS family — Windows 11 | **Representation-triggered** | No OS behaviour is exercised by reading a source file. |
| 3 | A Chromium-based browser family (Edge as representative) | **Representation-triggered** | Nothing is rendered in a browser. |
| 4 | Firefox as the second engine family (Gecko) | **Representation-triggered** | Same. |
| 5 | A no-cost desktop screen reader — NVDA | **Representation-triggered** | There is no accessibility tree to expose; AE-3 is structurally unreachable. |
| 6 | At least two browser/screen-reader pairings | **Representation-triggered** | Follows from 3, 4, and 5. |
| 7 | Zoom and reflow | **Representation-triggered** | Requires a layout. |
| 8 | Text spacing | **Representation-triggered** | Requires rendered text. The Candidate's contribution now is the flexible-label rule: no representation may assume a fixed label length or truncate away a material qualifier. |
| 9 | Forced colors / high contrast (Windows) | **Representation-triggered** | Requires colour. The Candidate defines **no colour value and no colour role**, which is what makes forced-colors survivable later. |
| 10 | Reduced motion | **Representation-triggered** | Requires motion. The Candidate defines none; motion is contracted as a redundant modality only, so removing it can never remove meaning. |
| 11 | Focus and keyboard behaviour (order, visibility, management, no trap) | **Representation-triggered** | Requires focus. |
| 12 | Status, alert, and dynamic-content communication reaching assistive technology (the Unknown invariant, DEC-S-056) | **Representation-triggered** — with a **source-level precondition applicable now** | The AT-exposure half needs a live region and a rendering. The precondition half — that the distinctions exist at all, that `unknown` is explicit on every axis, and that `stale`/`unverified` cannot be collapsed — is exactly what the CDS-WP-016 admitted AE-1 evidence covers. **The precondition being met is not the criterion being met.** |
| 13 | **DE and EN** for the declared scope | **Applicable now** | The terminology mapping is DE/EN and structurally verified: 25/25 identifiers, 25 EN labels, 25 DE labels, no duplicate, no missing, no unauthorized. |

### Counts

| Applicability | Entries |
| --- | --- |
| **Applicable now** | **1** (entry 13) |
| **Representation-triggered** | **12** (entries 1–12; entry 12 with a source-level precondition applicable now) |
| **Not applicable with rationale** | **0** |
| **Total Tier-1 Required categories** | **13** |

**Zero entries are `not applicable`.** Nothing in the Required baseline was
declared inapplicable to this Candidate. Twelve entries are simply not yet
assessable, and they keep their full force.

## Tier 2 and Tier 3

**Not required for this Candidate**, and **not** made applicable by it.

- **Tier 2 (Complementary):** Safari + VoiceOver, a second desktop screen reader
  (JAWS), Narrator, alternative input methods. Becomes mandatory only before a
  matching platform or support claim, or when a declared consumer scope or a
  documented risk requires it. None of those conditions exists.
- **Tier 3 (Scope-triggered):** mobile web, touch, iOS + VoiceOver, Android +
  TalkBack, further languages, enterprise/procurement or air-gapped environments,
  further assistive technologies. Mandatory only when the declared scope, a
  Consumer Contract, a Product Profile, or a documented risk requires it. None
  exists. **Undeclared Tier-3 environments are not represented as supported.**

**The JAWS gap stands unchanged:** its official system requirements were **not
retrievable** (S-12/S-13, HTTP 403) and were **not** re-verified by this plan.
JAWS remains conditional and is claimed nowhere.

## Execution availability — the binding limitation

*(RISK-051, recorded and not hidden)*

> **A11Y-BL-001 asserts no local execution availability for any listed
> environment.**

Every Required pairing still needs a real, capacity-checked execution slot before
AE-2 or AE-3 can be produced. This plan **does not create one, does not assert
one, and does not schedule one.** Concretely:

- **No environment has been provisioned** for Windows 11 × Edge × NVDA
  (A11Y-ENV-001) or Windows 11 × Firefox × NVDA (A11Y-ENV-002).
- **No accessibility test tool has been selected or installed**, and none may be
  without an explicit authorization.
- This limitation is **not** blocking for the Candidate at source scope, because
  the twelve representation-triggered entries are not yet assessable anyway. It
  **is** blocking for anything beyond it: AE-2, AE-3, Stable, a pilot, and any
  claim.

Recording an execution gap is **not** mitigating it. Documentation is not
mitigation.

## Obligations that activate on the first representation

The moment any rendered, interactive, or channel-bound representation of the
Semantic Status Foundation is created, the following become live **for that
artifact**, under its own Channel Accessibility Profile (DEC-S-058, DEC-S-125):

| # | Obligation |
| --- | --- |
| 1 | Status and its changes must be **programmatically available to assistive technology**, exercised on both Required pairings. |
| 2 | `unknown`, freshness, and confidence must be **perceivable visually and non-visually**. A status honest only to a sighted user is not honest. |
| 3 | Interactive status representations must be **keyboard-reachable and keyboard-operable with visible focus**; drill-down from a summary to all five axes must be keyboard-operable and AT-exposed. |
| 4 | Live updates must **not interrupt uncontrollably** while still conveying honest status changes. |
| 5 | Meaning must survive **zoom, reflow, text spacing, forced colors, and reduced motion** without losing a qualifier. |
| 6 | **DE and EN** must both be exercised — a single-language evidence run does not satisfy the Required baseline. |
| 7 | Exact OS, browser, renderer, assistive-technology, artifact, consumer, CDS, language, channel, and date values must be bound per run; **`current`/`latest` is not an evidence identity** (DEC-S-068, DEC-S-071). |

Producing this evidence requires the execution availability that does not exist
today. Until it does, the honest state is **not tested**.

## Re-review triggers for this plan

This plan must be re-reviewed — and the freshness determination re-made — on any
of the following. The first four mirror the
[Baseline Maintenance Policy](ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md);
the last three are specific to this Candidate.

| # | Trigger | Effect |
| --- | --- | --- |
| 1 | **2026-10-14 (PT)** — Windows 11 24H2 servicing end | Trigger-6 lifecycle event on a Required family; the family entry rolls and this plan is re-checked. |
| 2 | **By 2027-02-17** — six months after the last baseline review | Maximum review gap; a review is required with or without another trigger. |
| 3 | A **Major version** release of a baseline OS, browser, renderer, or AT that breaks a family entry rather than rolling within it | Affected evidence (when any exists) goes to `Review due`. |
| 4 | A **support-end or lifecycle change** of any baseline product | Family entry rolls; bound evidence is marked `Superseded` and revalidated before it supports anything. |
| 5 | **The first representation** of the Semantic Status Foundation | The twelve representation-triggered entries become live and assessable; a Channel Accessibility Profile becomes mandatory for that artifact. |
| 6 | **A change to the Candidate's declared language scope** (adding a language beyond DE/EN) | Tier-3 language coverage is triggered; the DE/EN structural evidence does not extend to it. |
| 7 | **A change to A11Y-BL-001 itself** (Required composition, tiers, families, declared scope) | Elevated; Nova review and Human-Maintainer approval; this plan is re-derived. |

## What this plan does not do

- It **does not claim** that CDS works in Windows 11, Edge, Firefox, or NVDA, or
  in any combination of them. It claims nothing.
- It **does not promote** anything. Candidate remains **No**, maturity remains
  **Experimental**, approval remains **Unapproved**.
- It **admits nothing.** The AE-1 admission it references was made elsewhere:
  Evidence 002 was independently reviewed **PASS**, integrated, and admitted at
  **AE-1** by the Human Maintainer for the channel-independent source/contract
  scope only (`AE1-CDS-WP016-SEMSTATUS-002`). This plan neither produced nor
  granted it. The admitted accessibility evidence level of every **other** CDS
  artifact remains **AE-0**, and the admission establishes **no AE-2, no AE-3, and
  no support claim** for any environment named below.
- It **does not select** a test tool, install anything, or run any test.

## Related documents

- [Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md) — normative
- [Accessibility Baseline Maintenance Policy](ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md) — normative
- [Accessibility Environment and Scope Matrix](ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
- [WP-016 A11Y Baseline Freshness Review](../reviews/WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md)
- [Semantic Status Candidate AE-2 Evidence Plan](SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md)
- [Semantic Status Candidate AE-1 Evidence Record](../operations/SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md)
