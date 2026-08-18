# Accessibility Requirements Baseline

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-007
- **Date:** 2026-07-16
- **Status:** **Normative** for accessibility requirement areas

## Purpose

The ten requirement areas CDS accessibility work must cover, stated as policy.

Criterion-level mapping lives in the
[WCAG 2.2 AA Applicability Matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md). This
document states **what CDS requires**; the matrix states **who owns each
criterion**.

**No concrete visual value is defined here.** Where a value is required, it is
required *by the cited WCAG criterion*, and is referenced rather than restated.

## Requirement classes

Each requirement carries one class:

| Class | Meaning |
| --- | --- |
| **Normative** | Binding on CDS artifacts now, as policy. |
| **Implementation-dependent** | Binding, but only assessable once an artifact exists. |
| **Consumer-scope** | The consumer owns it; CDS may expose a mechanism. |
| **Channel-specific** | Requires a channel profile first. |
| **Deferred** | A decision that does not yet exist. |

---

## 1. Structure and Semantics

| # | Requirement | Class |
| --- | --- | --- |
| 1.1 | Logical structure with programmatically determinable relationships (1.3.1) | Normative |
| 1.2 | Correct names, roles, values, and states (4.1.2) | Normative |
| 1.3 | Meaningful sequence preserved (1.3.2) | Implementation-dependent |
| 1.4 | **Native semantics before custom semantics** | Normative |
| 1.5 | ARIA only where native mechanisms are inadequate (DEC-S-054) | Normative |
| 1.6 | Structure survives composition | Consumer-scope |

Component contracts must state the semantics they guarantee. A contract that
omits accessibility semantics is incomplete, not merely undocumented — a consumer
cannot compensate for what the contract never promised.

## 2. Keyboard and Focus

*(CR-021 — a mandatory contract area, DEC-S-055)*

| # | Requirement | Class |
| --- | --- | --- |
| 2.1 | Full keyboard operability (2.1.1) | Normative |
| 2.2 | Comprehensible focus order (2.4.3) | Implementation-dependent |
| 2.3 | Visible focus (2.4.7) | Normative |
| 2.4 | Focus must not be obscured or lost (2.4.11) | Implementation-dependent |
| 2.5 | Focus management under dynamic state change | Implementation-dependent |
| 2.6 | **No keyboard trap** (2.1.2) | Normative |
| 2.7 | Documented keyboard contracts for complex patterns | Normative |

Requirement 2.7 is what makes the rest reviewable: an undocumented keyboard
contract cannot be verified, composed against, or regression-tested.

A trap can arise **purely from composition** of individually trap-free
components — which is why 2.6 is shared, not CDS-alone.

## 3. Visual Access

| # | Requirement | Class |
| --- | --- | --- |
| 3.1 | Contrast per 1.4.3 and 1.4.11 | Implementation-dependent |
| 3.2 | Reflow (1.4.10) | Implementation-dependent |
| 3.3 | Resize and magnification (1.4.4) | Implementation-dependent |
| 3.4 | Text spacing tolerance (1.4.12) | Implementation-dependent |
| 3.5 | Forced-colors and high-contrast conditions remain usable | Implementation-dependent |
| 3.6 | **Meaning without colour** (1.4.1) | Normative |
| 3.7 | No information by visual proximity or position alone (1.3.3) | Normative |

**No CDS colour is defined here** (DEC-S-032). Semantic colour roles must permit
conforming contrast; the values are a later decision.

Reflow and text spacing are the hardest cases for dense operational data — CDS's
most-evidenced consumer need. Unresolved until implementation.

## 4. Motion, Animation and Time

*(CR-022)*

| # | Requirement | Class |
| --- | --- | --- |
| 4.1 | Reduced-motion support | Normative |
| 4.2 | No unnecessary or hazardous motion (2.3.1) | Normative |
| 4.3 | Control of moving or auto-updating content (2.2.2) | Implementation-dependent |
| 4.4 | Appropriate handling of time limits (2.2.1) | Implementation-dependent |
| 4.5 | **Motion never the sole carrier of meaning** | Normative |

Live operational updates are the tension: honest status changes must be conveyed
without interrupting users uncontrollably.

## 5. Content and Cognitive Accessibility

| # | Requirement | Class |
| --- | --- | --- |
| 5.1 | Clear, consistent naming (2.4.6, 3.2.4) | Shared |
| 5.2 | Understandable instructions (3.3.2) | Shared |
| 5.3 | Explicable consequences | Normative (pattern contracts) |
| 5.4 | Consistent help (3.2.6) | Consumer-scope |
| 5.5 | Error prevention and recovery (3.3.1, 3.3.3, 3.3.4) | Shared |
| 5.6 | Progressive complexity | Implementation-dependent |
| 5.7 | **Simple/Expert mode without hiding function or status** | Normative |
| 5.8 | No manipulative or unnecessarily burdensome interaction | Normative |

Requirement 5.7 is the sharp one. All three consumers documented Simple/Expert
modes (CR-018). A reduced mode may hide **complexity**; it may never hide that an
option exists, misrepresent status, or conceal a risk. Hiding a warning is not
simplification.

WCAG supplemental guidance is **informative** and adds no conformance level
(DEC-S-057).

## 6. Forms, Authentication and Errors

| # | Requirement | Class |
| --- | --- | --- |
| 6.1 | Labels and instructions (3.3.2) | Shared |
| 6.2 | Error identification (3.3.1) | Shared |
| 6.3 | Correction help (3.3.3) | Shared |
| 6.4 | Data-loss prevention (3.3.4, 3.3.7) | Shared |
| 6.5 | Accessible authentication (3.3.8) | Shared |
| 6.6 | No unnecessary cognitive load | Normative |
| 6.7 | **Security must not silently override accessibility** | Normative |

Requirement 6.7 is a governance rule, not a design preference. Where security and
accessibility appear to conflict, the conflict is **escalated to a controlled
design and risk decision** — never resolved locally by degrading accessibility.

## 7. Status, Alerts and Dense Operational Data

*(The area with CDS's strongest consumer evidence — CR-006, CR-007)*

| # | Requirement | Class |
| --- | --- | --- |
| 7.1 | Status programmatically available (4.1.2, 4.1.3) | Normative |
| 7.2 | Alerts prioritized and understandable | Implementation-dependent |
| 7.3 | **Colour never the sole carrier** (1.4.1) | Normative |
| 7.4 | **Unknown, freshness, and confidence perceivable** | Normative |
| 7.5 | Tables and dense data structurally navigable (1.3.1) | Shared |
| 7.6 | Changes not visible-only | Normative |
| 7.7 | Live updates must not interrupt uncontrollably (2.2.2) | Implementation-dependent |

Requirement 7.4 makes the architecture invariant accessible (DEC-S-056):

> **Unknown ≠ Healthy · Stale ≠ Current · Unverified ≠ Verified**

These distinctions must reach **assistive technology and non-visual perception**.
A status honest only to a sighted user is not honest — and an operator acting on a
green that means *we have no idea* is the failure this exists to prevent.

## 8. Localization and Internationalization

*(CR-023)*

| # | Requirement | Class |
| --- | --- | --- |
| 8.1 | Correct language declaration (3.1.1, 3.1.2) | Consumer-scope (CDS exposes the mechanism) |
| 8.2 | DE/EN parity in the intended scope | Shared |
| 8.3 | Flexible text lengths | Normative |
| 8.4 | No layout-critical text assumptions | Normative |
| 8.5 | Internationalization capability for further languages | Normative |
| 8.6 | **Text direction and bidirectional content not architecturally excluded** | Normative |
| 8.7 | No meaning-bearing abbreviations without understandable context | Shared |

Requirement 8.6 is a **structural constraint, not a commitment to ship RTL**. The
architecture must not foreclose it; whether CDS supports RTL is a later decision.

## 9. Documents and Non-web Channels

*(All channel-specific — DEC-S-058)*

| # | Requirement | Class |
| --- | --- | --- |
| 9.1 | Semantic structure | Channel-specific |
| 9.2 | Alternative text | Channel-specific |
| 9.3 | Reading order | Channel-specific |
| 9.4 | Headings | Channel-specific |
| 9.5 | Table accessibility | Channel-specific |
| 9.6 | Language and metadata | Channel-specific |
| 9.7 | Meaning without colour | Channel-specific |
| 9.8 | Accessible alternative representation for diagrams and visualizations | Channel-specific |

**WCAG 2.2 is written for web content.** These requirements are real but cannot
be assessed until each channel has a profile.

**No PDF, presentation, or document standard is selected** (DEC-S-032).

## 10. Privacy, Security and Dangerous Actions

| # | Requirement | Class |
| --- | --- | --- |
| 10.1 | Privacy notices understandable | Shared |
| 10.2 | Security mechanisms operable | Shared |
| 10.3 | Session and timeout states comprehensible (2.2.1) | Shared |
| 10.4 | No security-by-obscurity interaction | Normative |
| 10.5 | **Dangerous actions accessibly confirmable and cancellable** | Normative |
| 10.6 | **Accessibility must not be traded against security** | Normative |
| 10.7 | A conflict requires a controlled design and risk decision | Normative |

Requirement 10.5 binds accessibility to the pilot's Group D safety patterns
(CR-010 … CR-013). A confirmation a user cannot perceive is not a safeguard, and
an inaccessible cancel path is not a cancel path.

---

## Summary

| Area | Requirements |
| --- | --- |
| 1 Structure and Semantics | 6 |
| 2 Keyboard and Focus | 7 |
| 3 Visual Access | 7 |
| 4 Motion, Animation and Time | 5 |
| 5 Content and Cognitive Accessibility | 8 |
| 6 Forms, Authentication and Errors | 7 |
| 7 Status, Alerts and Dense Operational Data | 7 |
| 8 Localization and Internationalization | 7 |
| 9 Documents and Non-web Channels | 8 |
| 10 Privacy, Security and Dangerous Actions | 7 |
| **Total** | **69** |

## Deferred decisions

Concrete contrast values beyond what the cited criteria require · colours, fonts,
sizes, breakpoints · the status taxonomy · Simple/Expert mechanism · reduced-motion
thresholds · RTL support scope · PDF, document, and presentation standards ·
target-size values · the support baseline · selectively adopted AAA criteria.

**No requirement here is evidenced by manual, keyboard, or assistive-technology
testing.** Every CDS artifact is AE-0 except the channel-independent Semantic Status
Layer-3 source/contract family, whose admitted **AE-1** evidence covers structural
and automated properties of that source scope only.

## Related documents

- [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [WCAG 2.2 AA Applicability Matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md)
- [Accessibility Responsibility Model](ACCESSIBILITY_RESPONSIBILITY_MODEL.md)
- [Accessibility Channel Profiles](ACCESSIBILITY_CHANNEL_PROFILES.md)
