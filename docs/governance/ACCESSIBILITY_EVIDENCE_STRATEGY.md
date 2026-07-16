# Accessibility Evidence Strategy

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy
- **Baseline:** A11Y-BL-001
- **Date:** 2026-07-16
- **Status:** **Normative** for how accessibility evidence is planned and recorded,
  **pending Human-Maintainer commit**. It **produces no evidence** and asserts no
  conformance. The evidence-level *meanings* remain owned by the
  [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md);
  this document operationalizes them.

## Purpose

Turns AE-0 … AE-4 into an operable, capacity-aware process bound to A11Y-BL-001 —
what to gather, at which maturity, against which environment identity, reviewed by
whom, and how freshness is kept. No test is run and no tool is selected.

## AE-0 … AE-4 operationalization

*(Meanings per the Evidence and Claims Model; this is the operating view)*

### AE-0 — Not Assessed
No usable evidence. **Every CDS artifact is AE-0 today.** Not a passing state.

### AE-1 — Structural and Automated
- Structural checks, automatable rules, static analysis; machine-readable
  traceability where available; documented tool and scope limits.
- **No tool is selected here.** An automated result is **input to review, never the
  review** (DEC-S-053) — W3C/WAI: tools *assist*, they do not *determine*
  accessibility (S-01).

### AE-2 — Manual Interaction
Documented human results, at minimum: keyboard-only · focus order · focus
visibility · focus management · reflow and zoom · text spacing · motion
(reduced-motion) · forms and errors · status and dynamic updates · dangerous
actions · DE/EN content and meaning. Bound to an artifact and revision.

### AE-3 — Assistive Technology
Testing against **declared A11Y-BL-001 pairings** (Required Tier-1; plus scope-
relevant Tier-2/Tier-3), recording expected vs actual behavior, task and state
coverage, known limitations, and **exact environment identity**. **AE-3 without a
declared, current baseline is unverifiable.**

### AE-4 — Consumer Scope and Complete-process
The consumer's, for a declared consumer/pilot scope: complete relevant processes,
consumer revision, consumer feedback, runtime/integration evidence, deviations,
review state, and Human-Maintainer approval state. **Only AE-4 can support a
conformance claim.**

## Evidence scope

Evidence is **artifact-, scope-, version-, revision-, environment-, and
channel-bound** and **never transfers** across any of them (DEC-S-052). Component
evidence is not product evidence. Declared channels: Web Product UI, Web
Documentation (DEC-S-058).

## Required evidence by maturity

*(Operating view of the Candidate/Stable accessibility gates)*

| Maturity | Required accessibility evidence |
| --- | --- |
| Proposed → Experimental | none required (must not be presented as evidenced) |
| **Candidate** (a11y-relevant) | WCAG mapping · responsibility mapping · AE-1 · relevant AE-2 or a reasoned AE-2 plan · known limitations · **support-baseline plan (A11Y-BL-001 pairings)** · regression plan · Human-Maintainer approval after Nova review |
| **Stable** (interactive web) | Candidate satisfied · complete applicable AE-2 · **AE-3 against declared current A11Y-BL-001 pairings** · required consumer/pilot evidence · no unresolved critical deviations · documented limits · migration/compatibility statement · Human-Maintainer approval after Nova review |
| **Conformance claim** | **AE-4** + declared scope + versions + baseline + limitations + approval |

## Manual strategy (AE-2)

Task-based manual checks per the AE-2 categories above, executed on the Required
Tier-1 non-AT environments (keyboard-only, forced-colors, reduced-motion,
zoom/reflow — A11Y-ENV-003…006), with documented expected/actual results and
`Not tested` used honestly.

## Assistive-technology strategy (AE-3)

Executed on the Required Tier-1 pairings (NVDA × Chromium, NVDA × Firefox —
A11Y-ENV-001/002), and on scope-triggered Tier-2/Tier-3 pairings when their trigger
fires. Records exact AT/browser/OS versions. **JAWS (A11Y-ENV-008) needs its
official requirements verified before use** (S-12/S-13 not retrievable).

## Consumer strategy (AE-4)

The Consumer Maintainer produces AE-4 for the consumer's declared scope, complete
processes, and revision, with feedback and deviations. CDS supplies contracts,
status semantics, and reference component evidence; it cannot produce AE-4 for a
product it does not own (DEC-S-051, DEC-S-052).

## Pilot strategy

For the CoreOps web pilot (when activated): apply the Required Tier-1 baseline plus
any consumer-declared additions; evidence Pilot Group E's thirteen requirements at
AE-2/AE-3 for CDS artifacts and AE-4 for the CoreOps slice
([CoreOps Pilot Accessibility Criterion](COREOPS_PILOT_ACCESSIBILITY_CRITERION.md)).
**The pilot has not started; no pilot evidence exists.**

## Environment identity

Every evidence run binds exact OS, browser/renderer, assistive technology, input,
language, channel, artifact/consumer revision, CDS version/revision, baseline
version, and date via the
[Evidence Record](../operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md)
(DEC-S-071, RISK-052).

## Review independence

An Evidence Reviewer checks evidence and is **never the executor of the evidenced
work and never the artifact itself** (DEC-S-045). Evidence reviewed only by its own
executor has not been reviewed. The Evidence Reviewer role is currently **unstaffed**
(FM-F-006) and must be staffed before Stable/claim evidence is accepted.

## Evidence freshness

Evidence carries a freshness state
([Maintenance Policy](ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md)); `Unknown`/
`Stale` evidence is not current and does not pass a gate. Evidence is immutable once
produced; change forces new evidence.

## Known limitations

Limitations are recorded per evidence run and **never averaged away**; there is
**no numeric or percentage accessibility score** (a single unmet criterion can make
a process unusable). Critical limitations block Stable and the corresponding claims.

## Capacity-aware execution

The Required baseline is deliberately small and free-software-runnable so evidence
is achievable without procurement (RISK-048). When demand exceeds capacity, the
honest responses are **smaller declared scope** or **lower maturity** — never a
weakened standard and never a conformant artifact with an asterisk (DEC-S-059).

## No current evidence

**No accessibility evidence exists.** Every CDS artifact is **AE-0**. This strategy
describes intent, not activity; it runs no test, selects no tool, and enables no
claim. A target and a baseline are not conformance (DEC-S-050).

## Claim boundary

An accessibility claim requires the eight claim elements (DEC-S-044 applied to
accessibility), including a **declared, current support baseline** and AE-4. **No
claim of any level is valid today, for anyone, including CDS.** `CDS certified` is
prohibited; no global "CDS is accessible" is permitted; non-web channels are never
presented as WCAG conformant.

## Related documents

- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) — normative evidence-level meanings
- [Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Environment and Scope Matrix](ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
- [Accessibility Baseline Maintenance Policy](ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md)
- [Accessibility Defect and Regression Model](ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md)
- [Accessibility Evidence Record Template](../operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md)
