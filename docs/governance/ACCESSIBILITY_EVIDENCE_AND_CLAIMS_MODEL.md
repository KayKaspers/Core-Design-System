# Accessibility Evidence and Claims Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-007
- **Date:** 2026-07-16
- **Status:** **Normative** for accessibility evidence and claims

## Purpose

Defines what counts as accessibility evidence, how strong each kind is, and what
may be claimed on it.

Frame: [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md).

## The five evidence levels

*(Normative — exactly five)*

| Level | Name | Establishes | Sufficient for |
| --- | --- | --- | --- |
| **AE-0** | **Not Assessed** | Nothing. | Nothing |
| **AE-1** | **Structural and Automated Evidence** | Machine-checkable properties hold. | Candidate (partly) |
| **AE-2** | **Manual Interaction Evidence** | A human exercised the artifact. | Candidate; part of Stable |
| **AE-3** | **Assistive Technology Evidence** | It works against a **declared** support baseline. | Stable (interactive web) |
| **AE-4** | **Consumer Scope and Complete-process Evidence** | A real product scope works end to end. | Conformance claims |

### AE-0 — Not Assessed

No reliable accessibility evidence.

**Every CDS artifact is currently AE-0.** Nothing has been tested.

### AE-1 — Structural and Automated Evidence

Structural checks, automatable rules, static analysis, machine-readable
traceability.

**AE-1 alone is never sufficient for a conformance claim** (DEC-S-053).

Automated checking finds a minority of real barriers and cannot evaluate meaning,
order, clarity, or whether a process is usable. W3C's own guidance is explicit
that the tooling **does not do the checking**.

### AE-2 — Manual Interaction Evidence

A human exercises the artifact against, at minimum: keyboard · focus · states ·
errors · content · reflow and magnification · motion and non-visual meaning —
with **documented results**.

### AE-3 — Assistive Technology Evidence

Testing against an **explicitly declared Accessibility Support Baseline**.

**The concrete baseline must be named later. No assistive-technology combination
is selected in this work package** (DEC-S-032).

AE-3 matters because ARIA support is incomplete across browsers and assistive
technology — the APG itself states that testing with real assistive technology is
essential before production use.

### AE-4 — Consumer Scope and Complete-process Evidence

Additionally: declared product or pilot scope · complete relevant processes ·
consumer revision · consumer feedback · known limitations · deviations · review
and approval state.

**Only AE-4 can support a conformance claim**, because only AE-4 covers
composition, content, and process — where accessibility is usually lost.

## Evidence rules

*(Normative)*

| # | Rule |
| --- | --- |
| 1 | **Automated-only is never sufficient** for Stable interactive artifacts or any conformance claim (DEC-S-053). |
| 2 | Evidence is **artifact-, scope-, version-, and revision-bound**. |
| 3 | Evidence must not be transferred across channels. |
| 4 | **Component evidence is not product evidence** (DEC-S-052). |
| 5 | Test-harness evidence is valid **for the harness only**. |
| 6 | Known limitations are never hidden behind an aggregate. |
| 7 | **No numeric accessibility score.** |
| 8 | Untested criteria are reported as **not tested**. |
| 9 | **A tool result is not human approval.** |
| 10 | Evidence reviewed only by its own executor has not been reviewed. |

### Why no score

A percentage invites the reading "87% accessible", which is meaningless: a single
unmet criterion can make a process unusable for a whole user group. Scores
average away exactly the information that matters, and they make a partial result
look complete.

## Accessibility Support Baseline

*(Normative process; no products selected)*

Per claim or evidence scope, the baseline must name:

| # | Element |
| --- | --- |
| 1 | Platform family |
| 2 | Browser or rendering environment |
| 3 | Input methods |
| 4 | Assistive-technology category |
| 5 | Relevant language |
| 6 | Relevant channel or artifact class |
| 7 | Test date |
| 8 | Versions or revisions |
| 9 | Known limitations |

A baseline **may not**:

- remain implicit,
- consist of a single automated tool,
- use outdated combinations without marking them,
- be presented as universal support for all technologies.

**No concrete product or version is chosen here.** Baselines drift as browsers
and assistive technology change (RISK-044); each is a dated snapshot with a
review trigger.

### Reconciliation with A11Y-BL-001 (CDS-WP-010)

*(Additive — the five evidence-level meanings above are unchanged)*

The concrete initial baseline is now **A11Y-BL-001**
([Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md)), pending
Human-Maintainer commit. It supplies the nine baseline elements above through three
tiers (Required / Complementary / Scope-triggered) and an
[Environment and Scope Matrix](ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md).
Applying it to this model:

- **Product-family vs execution baseline** (DEC-S-068): A11Y-BL-001 names product
  *families*; each AE-2/AE-3/AE-4 evidence run binds **exact** OS, browser,
  renderer, assistive-technology, artifact, consumer, CDS, language, channel, and
  date values. `current`/`latest` alone is not an evidence identity.
- **Exact environment identity** is recorded in the
  [Evidence Record](../operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md).
- **Evidence freshness** (DEC-S-070): evidence carries a freshness state; `Unknown`/
  `Stale` evidence is **not current** and satisfies no gate — see the
  [Baseline Maintenance Policy](ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md).
- **A baseline alone is not evidence** (DEC-S-065): declaring A11Y-BL-001 records
  what future evidence will target; it establishes nothing. **Every artifact remains
  AE-0.**
- **Support-claim boundary**: a *support claim* (environments actually supported) is
  distinct from the baseline and requires evidence plus the eight claim elements;
  none is valid today (DEC-S-044).

## Candidate accessibility gate

*(Normative — for accessibility-relevant artifacts)*

| # | Requirement |
| --- | --- |
| 1 | WCAG applicability mapping |
| 2 | Responsibility mapping |
| 3 | Known accessibility requirements |
| 4 | **AE-1** |
| 5 | Relevant **AE-2** evidence, or a reasoned evidence plan |
| 6 | Known limitations |
| 7 | Support baseline plan |
| 8 | Regression plan |
| 9 | Human Maintainer approval after Nova review |

## Stable accessibility gate

*(Normative — for interactive web-based artifacts)*

| # | Requirement |
| --- | --- |
| 1 | Candidate gate satisfied |
| 2 | **Complete applicable AE-2 evidence** |
| 3 | **AE-3 against the declared support baseline** |
| 4 | Required consumer or pilot evidence |
| 5 | **No unresolved critical accessibility deviations** |
| 6 | Documented known limits |
| 7 | Migration and compatibility statement |
| 8 | Human Maintainer approval after Nova review |

### Current state

**No artifact can pass either gate today.** All artifacts are AE-0; no support
baseline exists; no evidence exists.

This policy **promotes nothing** and **invents no retroactive evidence**.
Non-interactive artifacts require a channel profile first. **`Not tested` may
never be read as `Passed`.**

## Component evidence boundary

Component or pattern evidence establishes that **the component's contract holds
in isolation**, under the declared baseline, at a specific revision.

It does **not** establish an accessible page, workflow, complete process, or
conformant product — because composition, content, and process are consumer-owned
and can each break what the component guarantees.

## Product evidence boundary

Product evidence (AE-4) is **the consumer's**, for the consumer's declared scope
and revision. It does not transfer to another product, scope, revision, or
channel, and it does not make a CDS artifact Stable.

## Claim boundary

*(Normative, DEC-S-044 applied to accessibility)*

An accessibility claim requires:

| # | Element |
| --- | --- |
| 1 | CDS version or revision |
| 2 | Consumer and consumer revision |
| 3 | **Declared scope** |
| 4 | **Accessibility support baseline** |
| 5 | Evidence identity and level |
| 6 | Known limitations |
| 7 | Review and approval state |
| 8 | Date or validity reference |

Prohibited: **any global accessibility claim** · "CDS is accessible" · "WCAG
compliant" without scope, version, and baseline · **`CDS certified`** ·
conformance on AE-1 alone · a claim from component evidence · a legal-compliance
statement.

**Current claim status: none valid, for anyone, including CDS.**

A target is not a claim (DEC-S-050). Even a valid future claim would be bounded —
WCAG 2.2 states that even AAA conformance will not serve every disability.

## Regression evidence

Accessibility regresses silently: a token change removes contrast, an override
suppresses focus, a refactor drops a role.

Therefore: Stable artifacts require a **regression plan** · accessibility-relevant
changes require re-evidence at the affected level · evidence is bound to a
revision and **does not carry forward** across a change to what it evidenced ·
a regression is a **deviation**, not a limitation (RISK-045).

## Limitation reporting

Known limitations are recorded, never averaged away — see the
[Accessibility Limitations and Exception Policy](ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md).

**A limitation is not a passed test.** Critical limitations block Stable and the
corresponding claims.

## Related documents

- [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [Accessibility Responsibility Model](ACCESSIBILITY_RESPONSIBILITY_MODEL.md)
- [WCAG 2.2 AA Applicability Matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md)
- [Accessibility Limitations and Exception Policy](ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md)
- [Adoption, Conformance and Claims Policy](ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md)
- [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md)
