# Accessibility and Inclusive Design Policy

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-007 — Accessibility and Inclusive Design Policy
- **Date:** 2026-07-16
- **Status:** **Normative** for accessibility and inclusive design

## Purpose and authority

This document is the **normative source for CDS accessibility**. It resolves
CR-024 at policy level — the question every work package since CDS-WP-004 has
deferred.

It is the accessibility entry point. The specialised documents under
[Related documents](#related-documents) hold the detail.

## The target

*(Normative, DEC-S-049)*

> **For applicable web-based CDS artifacts, and for the declared web scope of
> future consumer validation: WCAG 2.2 Level AA.**

Basis: the WCAG 2.2 W3C Recommendation of 2024-12-12 — the only normative source
of CDS accessibility requirements.

Applies to, once such artifacts exist:

- web-based product UI,
- web-based documentation,
- web-based reference implementations,
- component and pattern examples,
- the declared web scope of the future CoreOps pilot.

## Target versus claim

*(Normative, DEC-S-050 — the most important boundary in this document)*

**Defining a target proves nothing.**

This target does **not** mean:

| Not implied | Reality |
| --- | --- |
| CDS currently meets WCAG 2.2 AA | **Nothing has been tested.** |
| Any CDS artifact has been evaluated | No artifact has accessibility evidence. |
| Any consumer product is conformant | No consumer has been evaluated. |
| An accessible building block makes an application conformant | It does not (DEC-S-052). |
| Non-web channels are WCAG-assessable | They are not, without a channel profile (DEC-S-058). |
| A legal requirement is satisfied | **CDS makes no legal statement.** |
| AAA is promised | It is not. |

**Current conformance status: none. Current accessibility claim: none.** No
claim of any level is valid today — by anyone, including CDS itself.

Four governance states are separate and must stay separate (DEC-S-050):

```
Target defined  →  Implementation evidence  →  Consumer evidence  →  Conformance claim
   (here)              (does not exist)          (does not exist)       (not possible)
```

### The standard's own limit

WCAG 2.2 states that **even AAA-conformant content will not be accessible to
people with every type, degree, or combination of disability**.

Conformance is therefore a **floor, not a guarantee**. CDS must never present
WCAG AA as "accessible" — the standard CDS cites contradicts that reading.

### AAA

**No general AAA commitment exists.** Individual AAA success criteria may later
be adopted selectively as additional quality goals. Doing so creates no AAA
claim and no additional conformance level.

## Scope

**In scope of the target:** web-based CDS artifacts and the declared web scope of
future consumer validation.

**Requires a channel profile before Candidate or Stable** (DEC-S-058): PDF and
reports · presentations · diagrams and data visualization · brand and
communication materials. WCAG 2.2 is written for web content; a web target
cannot simply be asserted for a paginated print artifact.

**Consumer-owned:** product composition, content, domain semantics, complete
processes, runtime behavior, consumer-local extensions, and the consumer's own
claims (DEC-S-051).

## Principles

*(Normative)*

### Accessibility by contract

Accessibility is part of normative foundations, component contracts, pattern
contracts, Product Profiles, channel profiles, consumer contracts, and evidence
gates.

**It is not a review step appended at the end.** A review can be skipped under
deadline; a contract cannot be met without meeting it.

### No component-to-product shortcut

*(DEC-S-052)*

An accessible CDS building block does **not** prove an accessible page, an
accessible workflow, an accessible complete process, or a conformant consumer
product.

This is the most common way a design system misleads its consumers: shipping
accessible parts and letting adopters infer an accessible whole. Composition,
content, and context are where accessibility is usually lost — and all three are
consumer-owned.

### Native semantics first

*(DEC-S-054)*

- Prefer native semantic mechanisms.
- Use ARIA only where required to express semantics native mechanisms do not
  adequately provide.
- ARIA does not substitute for correct structure or interaction.
- **APG examples are guidance, not production components.**

This follows the APG's own statements: *No ARIA is better than Bad ARIA*; ARIA
creates a promise that only the author's code fulfils and can cloak native
semantics; and the APG's objectives **explicitly exclude** providing a design
system or production-ready code, with testing against real assistive technology
essential before production use.

For a design system this is a direct warning against the shortcut it is most
tempted by: lifting APG patterns and treating them as accessible by provenance.

### Multi-modal meaning

Meaning must never be carried **solely** by colour, position, shape, animation,
sound, hover, or any single sensory modality.

### Honest states

*(DEC-S-056)*

The existing architecture invariant remains binding:

> **Unknown ≠ Healthy · Stale ≠ Current · Unverified ≠ Verified**

These distinctions must be perceivable **non-visually and to assistive
technology**. A status that is honest only to a sighted user is not honest.

Operational condition, severity, knowledge confidence, freshness, and evidence
availability must remain distinguishable through accessible semantics.

### Accessibility and safety

Dangerous, irreversible, or far-reaching actions later require: understandable
naming · predictable consequences · error prevention · confirmation · a cancel or
return path · accessible feedback · **no manipulative urgency**.

Accessibility and safety reinforce each other. A confirmation a user cannot
perceive is not a safeguard.

## Shared responsibility

*(Normative, DEC-S-051 — summary; detail in the responsibility model)*

| | Owns |
| --- | --- |
| **CDS** | The target and policy; accessibility requirements of shared foundations; component and pattern contracts; status and state semantics; Product Profile limits; accessibility documentation; reference evidence for CDS artifacts; known limitations; channel profile requirements; regression gates for its own artifacts. |
| **Consumer** | Accessible composition; product content; domain semantics; complete processes; consumer-local components and extensions; runtime behavior; third-party content; authentication and session behavior; local overrides; product testing in the declared scope; the consumer's claims. |
| **Shared** | Support baseline; browser/platform/AT matrix; Product Profile; exceptions and known limitations; CoreOps pilot evidence; complete-process evaluation; consumer feedback; regression handling; scope- and revision-bound claims. |

**Using accessible CDS artifacts does not make a product accessible or
conformant.**

## Architecture integration

Accessibility binds to the existing architecture rather than sitting beside it —
see [Accessibility Architecture Alignment](../architecture/ACCESSIBILITY_ARCHITECTURE_ALIGNMENT.md).

In short: Layer 3 carries semantic status foundations and non-colour meaning ·
Layer 4 carries component accessibility behavior in contracts · Layer 5 carries
pattern-level flows · Layer 6 carries channel profiles · Layer 8 carries evidence
· Product Profiles may never weaken it (invariant 10) · the token flow must not
allow colour to become the sole carrier.

## Candidate and Stable

*(Normative, DEC-S-036 applied)*

Accessibility gates are part of the maturity gates. Detail:
[Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md).

**This policy promotes nothing.** No existing artifact becomes Candidate or
Stable by virtue of this policy existing, and no evidence is retroactively
invented. Every artifact remains where it was.

## Inclusive design scope

*(Normative, DEC-S-057)*

WCAG conformance is a **minimum for the declared web scope, not the boundary of
inclusive-design work**.

Inclusive design considers: permanent disabilities · temporary impairments ·
situational constraints · vision, hearing, motor, and cognitive needs · differing
language and reading abilities · differing technical environments · low bandwidth
and offline situations · high information density · stress, error, and danger
situations · differing experience levels.

**Boundaries:**

- Inclusive design is not a blanket claim to cover every need.
- User feedback must not be replaced by assumption.
- **The same small maintainer group is not representative user research.**
- No persona or disability is invented.
- No real user validation is claimed — **none has occurred**.
- Known evidence gaps stay visible.

## Source hierarchy

*(Normative)*

| Rank | Source | Weight |
| --- | --- | --- |
| 1 | **WCAG 2.2 Recommendation** | **Normative** — the sole basis of requirements |
| 2 | **WAI-ARIA 1.2 Recommendation** | **Normative** where ARIA is used |
| 3 | Understanding, Techniques, APG, supplemental guidance, i18n guidance | **Informative** — direction only, never an obligation |
| 4 | WCAG-EM 2.0 | **Informative methodology reference** — a draft, explicitly not citable as more than work in progress; **not adopted** |
| 5 | EN 301 549 | **Standards watch only** — V4.1.0 is On Approval, not final; no conformance claimed |

Status detail:
[Accessibility Standard Status and Limitations](../research/ACCESSIBILITY_STANDARD_STATUS_AND_LIMITATIONS.md).

## Deferred implementation decisions

*(Deliberately open)*

Concrete colours, contrast values beyond what the cited criteria themselves
require, fonts, sizes, breakpoints, components · the accessibility support
baseline (products, versions, AT combinations) · testing tools and platforms ·
PDF, document, and presentation accessibility standards · the concrete status
taxonomy · AAA criteria adopted selectively · evaluation cadence · the
conformance evaluation method, pending WCAG-EM 2.0 leaving draft.

**No test product, browser, or assistive technology is selected here.**

## Change control

Normative. Changes require an authorized work package, a corresponding decision
entry where a registered decision changes, consistency updates across the
dependent documents, Nova review, and Human Maintainer approval.

**Accessibility requirements for Stable or CDS-conformant scope cannot be waived
through an ordinary exception** (DEC-S-059).

## Related documents

| Topic | Document |
| --- | --- |
| Who owns what | [Accessibility Responsibility Model](ACCESSIBILITY_RESPONSIBILITY_MODEL.md) |
| Requirement areas | [Accessibility Requirements Baseline](ACCESSIBILITY_REQUIREMENTS_BASELINE.md) |
| Criterion-level mapping | [WCAG 2.2 AA Applicability Matrix](WCAG_2_2_AA_APPLICABILITY_MATRIX.md) |
| Evidence and claims | [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) |
| Per-channel targets | [Accessibility Channel Profiles](ACCESSIBILITY_CHANNEL_PROFILES.md) |
| Limitations and exceptions | [Accessibility Limitations and Exception Policy](ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md) |
| CoreOps pilot criterion | [CoreOps Pilot Accessibility Criterion](COREOPS_PILOT_ACCESSIBILITY_CRITERION.md) |
| Architecture binding | [Accessibility Architecture Alignment](../architecture/ACCESSIBILITY_ARCHITECTURE_ALIGNMENT.md) |
| Standard status | [Accessibility Standard Status and Limitations](../research/ACCESSIBILITY_STANDARD_STATUS_AND_LIMITATIONS.md) |
| Sources | [Accessibility Source Register](../research/ACCESSIBILITY_SOURCE_REGISTER.md) |
| Governance frame | [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md) |
