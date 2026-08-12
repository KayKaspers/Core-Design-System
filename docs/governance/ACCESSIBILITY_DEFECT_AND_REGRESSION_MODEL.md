# Accessibility Defect and Regression Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy
- **Baseline:** A11Y-BL-001
- **Date:** 2026-07-16
- **Status:** **Normative and in effect** for classifying accessibility defects and
  regressions, committed with CDS-WP-010
  (`abe84b6b7267b8b9c5f96609e7c9d1ad1e68bc0a`). **No defect is registered today** —
  nothing has been tested (AE-0).

## Purpose

Keeps known accessibility barriers and regressions **explicit, classified, and
consequential** rather than normalized, hidden in an aggregate, or carried forward
silently (RISK-054, RISK-045). Defect impact is classified **separately from risk
severity** and stays traceable to requirements, environments, evidence, scope,
maturity, and claims.

## Impact levels

*(Normative — exactly four)*

| Level | Definition |
| --- | --- |
| **Blocking** | A declared task or required access is **not performable**, and there is **no equivalent accessible alternative**. |
| **High** | A substantial barrier prevents or endangers essential use; a limited workaround may exist. |
| **Medium** | A relevant barrier makes use significantly harder but does not fully prevent the declared scope. |
| **Low** | Limited accessibility friction without a material task blockage. |

Impact is about the **user's ability to complete the declared task**, not about how
hard the fix is.

## Defect record

*(Normative fields — per defect)*

- Defect ID
- affected requirement or Success Criterion
- environment and exact versions (per A11Y-BL-001 / evidence record)
- affected users or access needs
- reproducible steps
- expected behavior
- actual behavior
- impact (Blocking / High / Medium / Low)
- scope (artifact / channel / consumer / process)
- workaround (or `none`)
- owner
- status
- regression status
- evidence reference
- review trigger
- maturity and claim effect

## Defect statuses

*(Normative)*

| Status | Meaning |
| --- | --- |
| **Open** | Registered; not yet assessed |
| **Triaged** | Impact, scope, and owner assigned |
| **Mitigating** | Active work by a named owner |
| **Ready for revalidation** | Fix in place; awaiting re-evidence |
| **Closed** | Re-evidenced as resolved at the affected level |
| **Accepted limitation** | Consciously retained barrier — **Human-Maintainer decision required**, visible in every affected claim |

**`Accepted limitation`** is never a silent pass: it names affected user needs, an
alternative, and an expiry/review point, blocks the corresponding claim scope where
critical, and remains visible (DEC-S-059; Accessibility Limitations and Exception
Policy). Accessibility is not waivable by an ordinary exception.

## Regression definition

A **regression** is a previously **passed** environment/criterion combination that
later **fails**. Because it defeats past evidence — an artifact that once met AE-2/
AE-3 can carry old evidence while no longer holding the property — a regression is a
**deviation, not a limitation** (RISK-045).

### Regression rule

- A regression **must not** be hidden behind an aggregate or a score.
- Evidence **does not carry forward** across a change to what it evidenced; a change
  to a mandatory contract area (keyboard, focus, non-colour meaning, status)
  invalidates dependent evidence until re-verified.
- A likely vector is **copying a WAI-ARIA APG example as a production component**;
  APG examples are research artifacts, never evidence (DEC-S-054) — a
  pattern-derived artifact needs independent evidence.

### Blocking / High regression effects

A Blocking or High regression blocks, for the **affected scope**:

- **Stable**;
- the corresponding **pilot or consumer evidence**;
- **claims**;
- **distribution as unchanged-compatible** (the compatibility axis cannot be stated
  as compatible — DEC-S-039).

## Revalidation flow

1. Register the defect/regression with the record fields.
2. Triage impact, scope, owner.
3. Set affected evidence to **Review due**; mark dependent claims not current.
4. Mitigate (named owner) → **Ready for revalidation**.
5. Re-evidence against the current A11Y-BL-001 environment identity → **Closed**, or
   record an **Accepted limitation** (Human-Maintainer decision).

## Maturity effect

- Unresolved **critical** (Blocking/High) accessibility defects **block Candidate
  and Stable** for the affected scope.
- Demotion on discovery of a critical defect is normal and cheap (DEC-S-035).

## Pilot effect

A Blocking/High defect or regression in pilot scope blocks the affected Pilot Group
E evidence and any pilot accessibility statement; the pilot stays inactive
regardless (DEC-S-015).

## Claim effect

A defect that is an `Accepted limitation` must appear in every affected claim; a
claim omitting a known limitation is **invalid** (DEC-S-044). No claim exists today.

## Limitation boundary

A limitation is **not a passed test**. Critical limitations block Stable and claims.
Recurring limitations trigger an architecture or scope review (DEC-S-059). The full
limitation record and prohibited waivers live in the
[Accessibility Limitations and Exception Policy](ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md).

## Human-Maintainer authority

Only the Human Maintainer may set `Accepted limitation`, approve a maturity change,
or approve a claim. Nova reviews and recommends; Claude records and proposes.

## Currently registered defects

**None.** No artifact has been tested; every artifact is **AE-0**. An empty defect
list here means *nothing has been examined* — not *nothing is wrong*.

## Related documents

- [Accessibility Evidence Strategy](ACCESSIBILITY_EVIDENCE_STRATEGY.md)
- [Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Baseline Maintenance Policy](ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md)
- [Accessibility Limitations and Exception Policy](ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
