# Semantic Status Candidate — AE-2 Evidence Plan

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Accessibility Gate Remediation
- **Date:** 2026-08-17
- **Scope:** the **Semantic Status Candidate source and contract family**
- **Status:** **A reasoned plan — NOT evidence, NOT a schedule, NOT an
  authorization to execute.**

## Why this document exists

Requirement 5 of the [Candidate accessibility gate](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md#candidate-accessibility-gate)
is *"relevant **AE-2** evidence, **or a reasoned evidence plan**"*. The gate
offers that alternative precisely for artifacts where manual interaction evidence
would be meaningless. This is that case, and this is that plan.

> **A plan is not evidence.** This document establishes nothing about any
> artifact. **Every CDS artifact remains AE-0.**

## 1 — Why AE-2 execution is not meaningful today

**AE-2 is Manual Interaction Evidence**: a human exercises the artifact against,
at minimum, keyboard · focus · states · errors · content · reflow and
magnification · motion and non-visual meaning, with documented results.

**The Semantic Status Candidate has no interactive or rendered surface to
exercise.** It consists of:

- four normative contract documents (meaning definitions and rules),
- a DE/EN terminology mapping,
- a 25-token strict-JSON source set with a manifest and a resolver.

There is no keyboard surface, no focus, no state transition a user can trigger,
no error a user can encounter, no layout to reflow, no magnification target, and
no motion. Per **DEC-S-125** it is a channel-independent Layer-3 source and
contract and is not assigned an artificial channel.

Running an "AE-2" against it would mean one of two things, and both are
prohibited:

| # | What a forced AE-2 would actually be | Why it is prohibited |
| --- | --- | --- |
| 1 | A human reading contract documents and recording that they read them | That is a **content review**, which already exists and is already recorded as such. Relabelling it AE-2 would misstate the evidence level and inflate what the Candidate rests on. |
| 2 | A human exercising some *ad hoc* rendering built for the test | The evidence would be for **that rendering**, not for the source — and evidence never transfers across artifacts (DEC-S-052, DEC-S-125). It would also create an unauthorized representation. |

**Fabricating AE-2 is worse than having none.** An honest `not applicable at this
scope` is a true statement a reviewer can check; a manufactured AE-2 is a false
one that would then be relied on.

## 2 — When AE-2 becomes applicable

AE-2 becomes applicable **the moment a rendered or interactive representation of
the Semantic Status Foundation exists** — not before, and not by the passage of
time, a version bump, or a Candidate award.

The trigger is **the existence of the artifact**, not a date. Nothing in this
plan schedules or authorizes creating one.

## 3 — First triggering artifacts

Any one of the following creates the AE-2 obligation **for itself**, under its
own Channel Accessibility Profile:

| # | Triggering artifact | Applicable channel profile |
| --- | --- | --- |
| 1 | The first **component** or **pattern** that displays a CDS status | 1 — Web Product UI |
| 2 | The first **rendered documentation surface** that presents status values interactively (e.g. a browsable vocabulary) | 2 — Web Documentation and Repository Presentation |
| 3 | The first **generated channel output** carrying status meaning (a token build consumed by a UI) | 1, per the consuming surface |
| 4 | The first **diagram or data visualization** encoding status | 5 — Diagrams and Data Visualization (web-embedded); **exported is blocked, no profile exists** |
| 5 | The first **PDF or report** carrying status | 3 — **blocked; no profile exists** |

**None of these artifacts exists, is authorized, or is proposed by this plan.**
Creating any of them requires an explicit, separately authorized design work
package.

## 4 — AE-2 test categories that will apply

*(Derived from the Evidence and Claims Model's AE-2 definition and the Status
Communication and Accessibility Contract. Each will need documented expected and
actual results per case.)*

| # | Category | What must be demonstrated for status meaning specifically |
| --- | --- | --- |
| 1 | **Keyboard** | Every status representation is reachable and operable without a pointer; drill-down from a summary to all five axes is keyboard-operable. |
| 2 | **Focus** | Focus is visible, ordered, managed, and never trapped; focus is not obscured by overlays. |
| 3 | **States** | All five axes and their 25 values are distinguishable; `unknown` is explicitly perceivable and never rendered as neutral silence, an empty cell, or a positive default. |
| 4 | **Errors** | Fail-closed states are communicated as **system** states with a path to resolution, never as user faults; language is plain and non-blaming. |
| 5 | **Content** | Material qualifiers travel with every summary; no unqualified "healthy", "good", "current", "verified", or "all systems normal" appears where the axes do not carry it; "no known impact" is not rendered as "no impact". |
| 6 | **Reflow and magnification** | Meaning and qualifiers survive reflow and zoom; no qualifier is truncated away; dense status displays are the known hard case. |
| 7 | **Motion and non-visual meaning** | Colour, icon, shape, position, and motion never carry status meaning alone; reduced-motion preferences are honoured without losing meaning; forced-colors mode preserves every distinction. |
| 8 | **Truthfulness under representation** | `stale`/`expired` never read as `current`; `unverified`/`supported` never read as `verified`; `partial`/`unavailable`/`unknown` evidence is never hidden. |

Category 8 is specific to this Foundation: it is the representation-level
counterpart of the source-level rules the provisional AE-1 evidence covers, and
it is the reason AE-1 alone can never close this out.

## 5 — Applicable baseline environments

AE-2 will be produced against **A11Y-BL-001** Tier-1 (see the
[Support Baseline Plan](SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md)):

- **Windows 11** (a currently supported version) as the desktop OS family;
- a **Chromium** browser family (Edge as the officially-sourced representative);
- **Firefox** as the second engine family (Gecko);
- keyboard-only operation, zoom and reflow, text spacing, forced colors, and
  reduced motion.

**AE-3 is separate and additional**: assistive-technology evidence against
**NVDA** on both pairings (A11Y-ENV-001 and A11Y-ENV-002). AE-2 does not
substitute for AE-3, and an ordinary exception may never substitute AE-1 where
AE-2 or AE-3 is required (DEC-S-059).

**Execution availability does not exist today** for any of these environments
(RISK-051). A capacity-checked execution slot is a precondition of this plan
being runnable, not a detail of it.

## 6 — Version binding requirement

Every AE-2 run must bind **exact** values (DEC-S-068, DEC-S-071, RISK-052), via
the [Evidence Record Template](../operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md):

operating-system family **and exact version** · browser or renderer **and exact
version** · input methods · artifact **and revision** · consumer **and revision**,
where one exists · **CDS revision** · language · channel · **A11Y-BL-001 revision
and its freshness state** · test date.

> **`current` / `latest` / `supported` alone is not an evidence identity.** A
> record that does not name exact versions is incomplete, and an incomplete
> record satisfies no gate.

Baseline freshness must be `Current` at execution time; `Unknown` or `Stale`
evidence is not current and passes no gate (DEC-S-070).

## 7 — Language scope

**DE and EN, both.** The declared baseline scope names both languages, and status
truthfulness is a language property: a German label that reads as *verifiziert*
where the value is `supported` is an accessibility defect, not a translation
preference.

A single-language AE-2 run **does not** satisfy the Required baseline and must be
recorded as partial coverage with the missing language named. Languages beyond
DE/EN are Tier-3 and are **not supported by omission** (DEC-S-069).

## 8 — Executor and reviewer separation

| Role | Rule |
| --- | --- |
| **Executor** | Whoever performs the AE-2 run. Recorded by identity in the evidence record. |
| **Evidence Reviewer** | **Never the executor of the work being evidenced, and never the artifact itself** (DEC-S-045). |
| **Nova** | Reviews governance, scope, and evidence sufficiency; recommends. **Declares no conformance and accepts no risk.** |
| **Human Maintainer** | Approves the maturity transition and any limitation with normative effect. **Not delegable.** |

**Evidence reviewed only by its own executor has not been reviewed** (evidence
rule 10). This is the same separation the CDS-WP-016 provisional AE-1 package is
currently waiting on.

## 9 — No evidence transfer

*(DEC-S-052, DEC-S-125, evidence rule 3)*

- AE-2 evidence for one representation does **not** transfer to another
  representation, another channel, another revision, another language, or another
  consumer.
- AE-2 evidence for a representation does **not** flow back to the
  channel-independent source; the source's provisional AE-1 does **not** flow
  forward into a representation.
- **Component evidence is not product evidence.** A conforming status component
  does not make a page, a workflow, or a process accessible.

## 10 — Fail-closed readiness rule

An AE-2 run may only begin when **all** of the following hold. If any is unclear,
the answer is **NO-GO**, never "go with notes" (DEC-S-048).

| # | Precondition |
| --- | --- |
| 1 | A real rendered or interactive representation exists as a named, revision-bound artifact. |
| 2 | Its applicable **Channel Accessibility Profile** exists (DEC-S-058). |
| 3 | **A11Y-BL-001 freshness is `Current`** at execution time. |
| 4 | A real, capacity-checked **execution environment** exists for each Required pairing (RISK-051 closed for those environments). |
| 5 | An **Evidence Reviewer ≠ executor** is authorized in advance. |
| 6 | The run is **explicitly authorized** by a work package; Claude runs no accessibility test, installs no browser or screen reader, and selects no tool without one. |
| 7 | Both **DE and EN** are in scope, or the partial coverage is declared up front. |

## 11 — This plan is not evidence

> Writing this plan produced **no** accessibility evidence, **no** AE-2, **no**
> AE-3, and **no** claim.
>
> It does **not** promote the Candidate. Candidate remains **No**; maturity
> remains **Experimental**; approval remains **Unapproved**; the admitted
> accessibility evidence level of every CDS artifact remains **AE-0**.
>
> It authorizes **no** representation, **no** component, **no** channel, **no**
> Product Profile, and **no** consumer integration.

## Related documents

- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) — normative
- [Accessibility Evidence Strategy](ACCESSIBILITY_EVIDENCE_STRATEGY.md)
- [Semantic Status Candidate Support Baseline Plan](SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md)
- [Semantic Status Candidate WCAG Applicability Mapping](SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md)
- [Semantic Status Candidate Accessibility Regression Plan](SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md)
- [Status Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md)
- [Accessibility Evidence Record Template](../operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md)
