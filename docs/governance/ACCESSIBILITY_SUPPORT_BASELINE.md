# Accessibility Support Baseline

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy
- **Date:** 2026-07-16
- **Baseline ID:** **A11Y-BL-001**
- **Status:** **Normative and in effect** for the accessibility support baseline.
  It became effective with the Human-Maintainer commit of CDS-WP-010
  (`abe84b6b7267b8b9c5f96609e7c9d1ad1e68bc0a`). It is a **test contract** — **not**
  evidence, **not** a support guarantee, and **not** a conformance claim.

## Purpose and authority

A11Y-BL-001 declares the **environments against which future accessibility
evidence will be produced and evaluated** (DEC-S-065). It is the missing gate the
Foundation review named: AE-3 and therefore Stable are unreachable without a
declared support baseline (RISK-044, FM-F-001;
[Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)).

This document is normative for **which environments are Required, Complementary, or
Scope-triggered**, and for the boundary between a baseline and a claim. It selects
no design value, no token, no component, and no test tool.

## Target-versus-support-versus-claim boundary

*(Normative — four distinct states; do not conflate)*

| State | Meaning | Current CDS state |
| --- | --- | --- |
| **Target** | The standard CDS aims at | WCAG 2.2 Level AA for the applicable web scope (DEC-S-049) |
| **Support baseline** | The environments future evidence will be produced against | **A11Y-BL-001 (this document), declared and committed (CDS-WP-010)** |
| **Evidence** | Results of actually testing an artifact in an environment | **None — every artifact is AE-0** |
| **Support / conformance claim** | A stated, evidence-backed assertion about real environments | **None valid, for anyone** (DEC-S-044) |

**A declared baseline proves nothing** (DEC-S-050). It says *what will be tested*,
never *that anything passed*. Listing an environment here is **not** a statement
that CDS works in it or supports it.

## The three baseline tiers

*(Normative, DEC-S-066)*

| Tier | Name | Obligation |
| --- | --- | --- |
| **Tier 1** | Required Core Baseline | Must be covered for interactive desktop-web Candidate/Stable accessibility evidence in the declared scope |
| **Tier 2** | Complementary Coverage | Mandatory only when scope, Product Profile, Consumer Contract, claim, or documented risk requires it |
| **Tier 3** | Scope-triggered Coverage | Mandatory only when the declared scope/contract/profile/risk explicitly includes it |

Per-environment detail, IDs, and triggers are in the
[Accessibility Environment and Scope Matrix](ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md).

## Tier 1 — Required Core Baseline

*(Normative, DEC-S-067 — for interactive **desktop-web** evidence in the declared scope)*

| # | Required category |
| --- | --- |
| 1 | Full **keyboard-only** operation (no pointer) |
| 2 | At least one **supported desktop OS family** — Windows 11 (a currently supported version; S-03) |
| 3 | A **Chromium-based** browser family (Edge as officially-sourced representative; Chrome shares the engine; S-02, S-09) |
| 4 | **Firefox** as the second engine family (Gecko; S-06) |
| 5 | At least one **no-cost desktop screen-reader** family — **NVDA** (S-04) |
| 6 | **At least two** browser/screen-reader pairings — NVDA×Chromium and NVDA×Firefox (**2**; the cap is 3) |
| 7 | **Zoom and reflow** |
| 8 | **Text spacing** |
| 9 | **Forced colors / high contrast** where the platform offers it (Windows; S-08) |
| 10 | **Reduced motion** (S-07) |
| 11 | **Focus and keyboard** behavior (order, visibility, management, no trap) |
| 12 | **Status, alert, and dynamic-content** communication reaching assistive technology (the Unknown invariant, DEC-S-056) |
| 13 | **DE and EN** for the declared scope |

**Rules:** Required holds **no more than three** screen-reader/browser pairings
unless additional consumer or risk evidence justifies expansion; it is composed
from **official-source-verifiable, currently supported** products; **no local
availability is invented**; and any missing local execution capability is recorded
as an **Execution Gap** in the matrix (RISK-051), never silently assumed.

## Tier 2 — Complementary Coverage

Assessed (see matrix): Safari + VoiceOver on a current Apple platform (S-05); a
second desktop screen reader (**JAWS** — official requirements **not retrievable**,
S-12/S-13, kept conditional); Narrator (Windows built-in); alternative input
methods. Tier 2 becomes mandatory before a matching platform/support claim, when
the declared consumer scope includes it, or when evidence/risk shows a relevant
coverage gap. It is **not** automatically required for every Candidate.

## Tier 3 — Scope-triggered Coverage

Assessed (see matrix): mobile web, touch, iOS + VoiceOver, Android + TalkBack,
further languages, enterprise/procurement or air-gapped environments, additional
assistive technologies. Mandatory **only** when the declared scope, a Consumer
Contract, a Product Profile, or a documented risk requires it. **Undeclared Tier-3
environments must not be represented as supported** (DEC-S-069).

## Selected product families

*(Product-family baseline — not a per-version support guarantee; DEC-S-068)*

| Role | Family | Officially-sourced status (2026-07-16) | Source |
| --- | --- | --- | --- |
| Desktop OS | Windows 11 | Supported versions 24H2 / 25H2 / 26H1 | S-03 |
| Browser (Chromium) | Microsoft Edge / Chrome | Rapid release; Stable + Extended Stable | S-02, S-09 |
| Browser (Gecko) | Firefox (release or ESR) | Rapid release 4-week + annual ESR | S-06 |
| Screen reader (no-cost) | NVDA | Free/open source; Windows 10/11 | S-04 |

Product families name the **intended** environments. The **exact** OS, browser,
renderer, and assistive-technology **versions** are bound per evidence run in the
[Evidence Record](../operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md), never
by this document (DEC-S-068). `current` / `latest` / `supported` alone is **not**
an evidence identity.

## Declared initial scope

- **Channels:** Web Product UI; Web Documentation (the two profiles that carry a
  target — DEC-S-058).
- **Interaction:** interactive desktop web.
- **Languages:** DE, EN.
- **Applies to:** future CDS component/pattern accessibility evidence in this scope
  and, when activated, the CoreOps web pilot scope (with consumer additions).

## Explicitly not-declared scope

Non-web channels (PDF, presentations, diagrams, brand — no profile, DEC-S-058);
mobile/touch web; Apple/WebKit; commercial screen readers as Required; languages
beyond DE/EN; the complete CoreOps product; enterprise/procurement environments.
These are **not supported by omission and not by inclusion** — they are simply not
yet in the Required baseline.

## Environment availability gaps

*(RISK-051 — recorded, not hidden)*

- **No local execution availability is asserted** for any listed environment. Each
  Required pairing still needs a real, capacity-checked execution slot before AE-2/
  AE-3 can be produced.
- **WebKit/Safari and JAWS are not currently verified as available**; JAWS official
  requirements were not retrievable (S-12/S-13).
- Gaps are tracked per environment in the matrix and must be closed before the
  affected evidence level is claimed.

## Consumer scope override boundary

A Consumer Maintainer may **declare additional** environments for their product's
evidence (Tier 2/Tier 3), and is accountable for that consumer evidence
(DEC-S-051, DEC-S-052). A consumer may **not** narrow the CDS Required Tier-1
baseline for a shared CDS artifact, and consumer evidence does **not** transfer to
CDS or to another consumer. Using accessible CDS artifacts does not make a consumer
product accessible.

## Current approval state

- **Pending Nova review and Human-Maintainer commit.** Until then A11Y-BL-001 is a
  proposal.
- **No evidence** has been produced against it. **No environment is claimed as
  supported.** **No WCAG conformance is asserted.** Publication state remains
  `Private Development`.

## Change control

A11Y-BL-001 is versioned and revision-bound. Changes to Required composition, tiers,
or declared scope are **Elevated** (accessibility obligation) and require Nova
review and Human-Maintainer approval. Freshness, review triggers, and version
handling are governed by the
[Accessibility Baseline Maintenance Policy](ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md).
On any conflict with the
[Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md),
that model's evidence-level meanings win.

## Related documents

- [Accessibility Environment and Scope Matrix](ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
- [Accessibility Baseline Maintenance Policy](ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md)
- [Accessibility Evidence Strategy](ACCESSIBILITY_EVIDENCE_STRATEGY.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Accessibility Defect and Regression Model](ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md)
- [Accessibility Baseline Source Register](../research/ACCESSIBILITY_BASELINE_SOURCE_REGISTER.md) ·
  [Selection Rationale](../research/ACCESSIBILITY_BASELINE_SELECTION_RATIONALE.md)
- [CoreOps Pilot Accessibility Criterion](COREOPS_PILOT_ACCESSIBILITY_CRITERION.md)
