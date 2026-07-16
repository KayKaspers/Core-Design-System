# Accessibility Standard Status and Limitations

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-007
- **Evidence date:** 2026-07-16
- **Status:** Research evidence — **not normative**

## Purpose

Records the **actual status** of every accessibility standard CDS relies on, and
the limits of what any of them can establish.

This exists because status errors are the cheapest way to build a policy on sand:
adopting a draft as final, or a guidance document as a requirement, produces a
policy that looks rigorous and is not.

Sources: [Accessibility Source Register](ACCESSIBILITY_SOURCE_REGISTER.md).

## Status summary

| Standard | Status | Date | Normative? | CDS use |
| --- | --- | --- | --- | --- |
| **WCAG 2.2** | **W3C Recommendation** | 2024-12-12 | **Yes** | **The normative basis of the CDS target** |
| **WAI-ARIA 1.2** | W3C Recommendation | 2023-06-06 | **Yes** (roles, states, properties, markup use) | Normative where ARIA is used |
| Understanding WCAG 2.2 | Supporting document | — | **No** | Informative only |
| Techniques for WCAG 2.2 | Supporting document | — | **No — explicitly not required** | Informative only |
| ARIA Authoring Practices Guide | Guidance | — | **No — self-declared informative** | Informative only |
| WCAG 2 Supplemental Guidance | Guidance | — | **No — explicitly not required for conformance** | Informative only |
| W3C i18n authoring guidance | Guidance | — | **No** | Informative only |
| **WCAG-EM 2.0** | **W3C Group Note _Draft_** | **2026-02-05** | **No — work in progress** | **Informative methodology reference only** |
| **EN 301 549 V3.2.1** | **Published version** (deliverable not opened) | — | **No — not adopted as a CDS target** | European reference only; no legal claim |
| **EN 301 549 V4.1.0** | **"On Approval"** (in formal approval) | 2026-06 | **No — not final** | **Standards-watch only; re-verify** |

---

## WCAG 2.2

**W3C Recommendation, published 2024-12-12. Normative.** W3C recommends wide
deployment as a web standard.

**Structure as found in the Recommendation:**

- 87 success criteria are listed in total.
- **86 apply**, because **4.1.1 Parsing is marked "Obsolete and removed"**.
- Level A: 32 listed, **31 applicable**.
- Level AA: 24.
- Level AAA: 31.
- **Applicable Level A + AA: 55.**

These counts were extracted from the Recommendation itself and independently
re-counted. They were **not** taken from memory.

### The obsolete criterion

4.1.1 Parsing carries a Level A marker but is explicitly obsolete and removed.
The Recommendation states it was originally adopted for problems assistive
technology had directly parsing HTML, and that assistive technology no longer
has that need.

**Consequence for CDS:** 4.1.1 is carried in the applicability matrix for
completeness and traceability, but is **excluded from the mandatory baseline**.
Silently dropping it would make the matrix uncheckable against the source;
silently requiring it would impose an obsolete obligation.

### The standard's own honesty

The Recommendation states that **even AAA-conformant content will not be
accessible to people with every type, degree, or combination of disability**.

This is the single most important framing in this work package. It means that
conformance — at any level — is **a floor, not a guarantee**. A policy that
presented WCAG AA as "accessible" would be contradicted by the standard it
cites.

## Understanding and Techniques

Both are **informative**. Understanding explicitly states it is not part of the
normative standard. Techniques explicitly states its techniques are **not
required** to meet WCAG — content may satisfy the normative requirements without
using any documented technique.

**Consequence:** CDS may use both for direction. Neither may create a CDS
requirement, and neither may be cited as the reason something is required.

## WAI-ARIA 1.2 and the APG

**WAI-ARIA 1.2 is a W3C Recommendation (2023-06-06) and is normative** for roles,
their characteristics, supported states and properties, and how they may be used
in markup.

**The APG is informative and says so.** Three of its own statements shape CDS
policy directly:

1. **"No ARIA is better than Bad ARIA."** Native semantics are preferable.
2. **ARIA creates an implicit promise.** Applying a role to a generic element
   promises behavior that only the author's code can deliver — unlike native
   elements, ARIA supplies no browser behavior. ARIA can also cloak native
   semantics and harm assistive-technology users.
3. **The APG's objectives explicitly exclude providing a comprehensive design
   system or production-ready code.** Its examples exist to teach accessibility
   concepts, not to be adopted as production components. It states that browser
   and AT support for ARIA 1.2 is incomplete and that **testing with actual
   assistive technologies is essential before using its code in production**.

**Consequence for a design system:** this is a direct, authoritative warning
against the exact shortcut a design system is most tempted by — lifting APG
patterns into a component library and treating them as accessible by provenance.
CDS may not do this (DEC-S-054).

## WCAG-EM 2.0 — current status

**W3C Group Note _Draft_, 2026-02-05. Non-normative, work in progress.**

The document states it is a draft that may be updated, replaced, or obsoleted at
any time, and that **it is inappropriate to cite it as other than a work in
progress**. It adds nothing to and changes nothing in the normative WCAG 2
standard.

**CDS decision: not adopted as the CDS conformance method.** It is used as an
**informative methodology reference** only.

Its structure — define scope, explore, sample, evaluate, report — remains useful
direction. The related W3C conformance guidance confirms the important point:
**the report tool does not do the checking**, evaluation requires expertise
across standards, design, assistive technology, and how people with disabilities
actually use the web, and involving real users with disabilities is recommended.

## EN 301 549 — European reference and standards watch

A version transition is visibly in progress, so the two versions are documented
**separately** and must never be conflated.

### Published reference — EN 301 549 V3.2.1

- The **published version** and the current European accessibility reference,
  listed by ETSI among the related published deliverables.
- **Not adopted as a CDS conformance target.**
- **No legal or procurement applicability claim** is made from it.
- Its deliverable PDF was **not opened** (downloading standards PDFs is prohibited
  by this work package), so its contents were **not independently verified here** —
  it is cited only as the published-version reference, per the source register.

### Pending version — EN 301 549 V4.1.0

- Listed by ETSI as **"On Approval"** (that is, **in formal approval**) as of
  2026-06 — **not yet a published standard**.
- **Not** treated as the published CDS reference.
- **Standards-watch only**, and **must be re-verified** before any later normative
  use.

### CDS position (both versions)

- EN 301 549 is documented as a **European reference and a standards-watch item**,
  nothing more.
- **No EN 301 549 conformance is claimed**, against either version.
- **No draft or On-Approval version is adopted as final** — V4.1.0 explicitly is
  not, and V3.2.1 is a reference, not an adopted target.
- **No legal or procurement applicability statement is made.**

## No legal advice

**This document, and the CDS accessibility policy, contain no legal advice.**

CDS makes no statement about:

- whether any law applies to any consumer,
- whether any consumer satisfies a legal obligation,
- procurement eligibility,
- regulatory compliance in any jurisdiction,
- undue or disproportionate burden determinations.

Standards interpretation here is **engineering policy, not legal opinion**.
Legal questions belong to the Human Maintainer and, where relevant, to qualified
advice outside CDS.

## Non-web limitations

WCAG 2.2 is written for **web content**. CDS scope includes non-web channels —
PDF and reports, presentations, diagrams, brand materials.

**Consequence:** a WCAG AA target cannot simply be asserted for non-web channels.
Applying web success criteria to a paginated print artifact is a category error
in some cases and merely undefined in others. Each non-web channel requires a
channel-appropriate profile with its own requirements and evidence (DEC-S-058).

**No PDF, document, or presentation accessibility standard is selected here.**

## Source volatility

Every finding is a **dated snapshot** (2026-07-16) and decays:

- WCAG-EM 2.0 is an active draft and will change.
- **EN 301 549 V4.1.0 is On Approval** and its status will change — possibly
  soon.
- W3C guidance pages are edited continuously.
- Browser and assistive-technology support shifts underneath any support
  baseline (RISK-044).

**Re-verify any status before relying on it in a later decision.** A standards
watch is a recurring obligation, not a one-time check.

## What these standards cannot establish

Recorded plainly, because the gap is where overclaiming happens:

1. **Conformance ≠ accessible.** The standard says so itself.
2. **A target is not a claim.** Defining WCAG 2.2 AA proves nothing about any
   artifact.
3. **Guidance is not a requirement.** Understanding, Techniques, APG, and
   supplemental guidance create no obligation.
4. **A methodology draft is not a method.** WCAG-EM 2.0 is not adopted.
5. **Automated checks are not evaluation.** Tools do not do the checking.
6. **Component evidence is not product evidence.**
7. **No standard substitutes for real users.** W3C recommends involving people
   with disabilities; CDS has done no user research (RISK-017).

## Future standards-watch requirement

CDS must maintain an ongoing watch on: WCAG 2.2 errata and successor work ·
WAI-ARIA versions · **WCAG-EM 2.0 progression out of draft** · **EN 301 549
V4.1.0 approval status** · assistive-technology and browser support shifts ·
supplemental and cognitive guidance.

Each is a **review trigger**, not a background task. The concrete cadence is
deferred — CDS has no evidence for what it can sustain (RISK-048).

## Related documents

- [Accessibility Source Register](ACCESSIBILITY_SOURCE_REGISTER.md)
- [Accessibility and Inclusive Design Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [WCAG 2.2 AA Applicability Matrix](../governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md)
- [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
