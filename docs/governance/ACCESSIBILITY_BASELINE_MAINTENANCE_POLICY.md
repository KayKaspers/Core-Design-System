# Accessibility Baseline Maintenance Policy

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy
- **Baseline:** A11Y-BL-001
- **Date:** 2026-07-16
- **Status:** **Normative** for baseline version handling, freshness, and review
  triggers, **pending Human-Maintainer commit**. It executes no test and renews no
  claim automatically.

## Purpose

Browser, platform, input, rendering, and assistive-technology combinations change,
and evidence gathered against an old combination silently becomes false (RISK-044).
This policy keeps A11Y-BL-001 current and keeps evidence honest across change. It
governs *when the baseline is reviewed* and *when dependent evidence is
invalidated* — never *that anything passed*.

## Version policy

*(Normative, DEC-S-068)*

- **Product-family baseline vs exact evidence version are separate.** A11Y-BL-001
  names product **families** (intended environments); each **evidence run** binds
  exact OS, browser, renderer, assistive-technology, artifact, consumer, CDS,
  language, channel, and date values (Evidence Record).
- **`current` / `latest` / `supported` alone is not an evidence identity.** An
  evidence record that does not name exact versions is incomplete (RISK-052).
- The baseline **may use a rolling family policy** (e.g. "a currently supported
  Windows 11 version; current Chromium/Firefox stable or ESR"); the **evidence
  itself remains immutable and version-bound** once produced.
- **Superseded product versions are not silently carried forward.** When a product
  version leaves vendor support, evidence bound to it is marked and no longer
  counts as current.

## Freshness states

*(Normative — exactly five)*

| State | Meaning |
| --- | --- |
| **Current** | Reviewed against the present environment reality; within the review window |
| **Review due** | A review trigger has fired; re-verification pending |
| **Stale** | Past the maximum review gap, or a Major-version/support-end change occurred, without re-verification |
| **Superseded** | Replaced by a newer baseline revision |
| **Unknown** | Freshness cannot be established |

**`Unknown` and `Stale` are not `Current`.** Evidence resting on a non-Current
baseline is **not Current Evidence** and cannot satisfy a Candidate, Stable, pilot,
or claim gate that requires current evidence.

## Review triggers

*(Normative — a trigger-based review, not a date nobody honours; DEC-S-070)*

A baseline (freshness) review is required:

1. **before the first Candidate** with an accessibility obligation;
2. **before Stable**;
3. **before pilot** evidence;
4. **before an accessibility or conformance claim**;
5. on a **Major version** release of a baseline OS, browser, renderer, or
   assistive technology;
6. on a **support-end / lifecycle change** of a baseline product;
7. on a **critical or High accessibility regression** or a compatibility warning;
8. on a **declared-scope or Product-Profile change** that alters environments;
9. **at least every six months** since the last baseline review.

### The six-month rule

The six-month interval is a **maximum review gap**, not an obligation to re-run
every combination without cause. A review confirms whether the environment reality
and the baseline still match and whether any dependent evidence must be re-checked;
it does not mandate blanket re-testing absent a trigger.

## Lifecycle and support-end handling

When a baseline product version reaches vendor support end (e.g. a Windows 11
version's retirement date, S-03), the baseline is reviewed: the family entry rolls
to a currently supported version, and evidence bound to the retired version is
marked `Superseded` and revalidated before it can support a current claim.

## Major-version and scope-change handling

A Major OS/browser/renderer/AT release, or a change to declared scope or a Product
Profile, sets affected evidence to **Review due** and requires targeted
revalidation of the affected environments and artifacts before the affected
maturity or claim is treated as current.

## Regression trigger

A critical or High accessibility regression (see the
[Accessibility Defect and Regression Model](ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md))
invalidates dependent evidence for the affected scope until re-verified and
triggers a baseline/freshness review.

## Revalidation boundary

- Revalidation is **targeted** to the affected environments/artifacts, bound to the
  new versions, and recorded as new immutable evidence.
- Evidence **does not carry forward** across a change to what it evidenced, the
  baseline it was produced against, the channel, or the scope (DEC-S-052).
- Candidate, Stable, pilot, and claim gates **check evidence freshness**; evidence
  with `Unknown`/`Stale` freshness does not pass.

## Baseline history

Each A11Y-BL revision records: revision ID, date, changed Required/Conditional/
Deferred composition, changed declared scope, rationale, superseded revision,
approval state, and the freshness impact on existing evidence. History is retained;
a superseded baseline stays traceable.

## Approval

Changes to A11Y-BL-001 (Required composition, tiers, declared scope, family
selection) are **Elevated** and require Nova review and Human-Maintainer approval.
Claude proposes; Nova reviews; the Human Maintainer decides and commits.

## No automatic claim renewal

A baseline review, a version roll, or the passage of time **never** renews a
support or conformance claim. A claim is re-established only through fresh evidence
and explicit Human-Maintainer approval (DEC-S-044). Silence is not continuation.

## Related documents

- [Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Environment and Scope Matrix](ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
- [Accessibility Evidence Strategy](ACCESSIBILITY_EVIDENCE_STRATEGY.md)
- [Accessibility Defect and Regression Model](ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
