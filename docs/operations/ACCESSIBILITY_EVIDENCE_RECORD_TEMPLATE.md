# Accessibility Evidence Record — Template

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy
- **Baseline:** A11Y-BL-001
- **Date:** 2026-07-16
- **Status:** **Operational template — NOT normative, NOT evidence.** A blank
  reusable record. Copying it creates **no** evidence and **no** claim, and grants
  **no** approval. The evidence-level meanings are owned by the
  [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md).

## How to use

Copy this template into a per-run record for a single artifact/consumer in a single
environment. Bind **exact** versions (DEC-S-071, RISK-052); `current`/`latest` is
not an identity. A single `Pass` is one environment at one revision — it creates
**no global claim** (DEC-S-044, DEC-S-052). `Not tested` and `Not applicable with
rationale` are first-class and must be used honestly.

## Mandatory fields

- **Evidence ID**
- **Evidence level** — AE-1 · AE-2 · AE-3 · AE-4
- **Artifact or consumer**
- **Declared scope**
- **CDS version or revision**
- **Artifact or consumer revision**
- **Baseline version** — A11Y-BL-001 revision + freshness state
- **Operating-system family and exact version**
- **Browser or renderer and exact version**
- **Assistive technology and exact version**
- **Input methods**
- **Language**
- **Channel**
- **Test date**
- **Reviewer** — never the executor, never the artifact (DEC-S-045)
- **Executor**
- **Test cases**
- **Expected result**
- **Actual result**
- **Result status** — see below
- **Defects** — references into the [Defect and Regression Model](../governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md)
- **Known limitations**
- **Deviations**
- **Source references**
- **Approval state** — Human-Maintainer approval is separate and later
- **Freshness state** — Current · Review due · Stale · Superseded · Unknown
- **Next review trigger**

## Result status values

`Pass` · `Pass with limitations` · `Fail` · `Blocked` · `Not tested` ·
`Not applicable with rationale`

- A `Pass` is bound to this record's artifact, revision, environment, and channel.
- **No numeric or percentage score** is produced (a single unmet criterion can make
  a process unusable).
- **`Not tested` is never read as `Passed`.**

## Rules for this record

- **Not normative and not evidence-by-existence** — a filled record is evidence
  *for its exact environment identity only*; a blank template is neither.
- **No automatic approval** — Nova review and Human-Maintainer approval are separate
  acts; an automated result is input to review, never the review (DEC-S-053).
- **No transfer** — evidence never transfers across artifact, revision, environment,
  channel, scope, or consumer (DEC-S-052).
- **Freshness-bound** — `Unknown`/`Stale` evidence is not current and passes no gate.

## Related documents

- [Accessibility Evidence Strategy](../governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md)
- [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Environment and Scope Matrix](../governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
- [Accessibility Defect and Regression Model](../governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md)
