# Concept and Scope

- **Project:** Core Design System (CDS)
- **Phase:** Foundation / Pre-Design
- **Registered by:** CDS-WP-002 — Concept and Scope Registration
- **Date:** 2026-07-15

## Document purpose and authority

This document is the **normative source** for the registered CDS concept and
scope. Where other documents summarize scope, this document takes precedence.

It registers what CDS is, what it will cover long-term, what it covers in the
current phase, what it will never cover, and where its responsibility ends. It
does **not** decide visual design, tooling, or implementation technology.

### Statement classes

Statements in this document are classified. The class determines what a
statement commits CDS to.

| Class | Meaning |
| --- | --- |
| **Normative** | Binding now. Later work packages must comply or change it through governance. |
| **Current phase scope** | Actively worked in the Foundation / Pre-Design phase. |
| **Long-term direction** | Registered as intended scope. Not a delivery, availability, or schedule commitment. |
| **Deferred decision** | Explicitly not decided. Requires a later authorized work package. |
| **Assumption** | Believed true, not yet validated. May change. |

## Problem statement

*(Normative)*

The Core ecosystem builds multiple products across multiple channels without a
shared, governed design foundation. This produces recurring problems:

1. Each product re-decides the same design questions locally, with different
   answers and no shared rationale.
2. Design intent lives in tools, screenshots, and individual memory rather than
   in a reviewable, versioned source.
3. Products drift apart visually and behaviorally, so the ecosystem reads as
   unrelated tools rather than one family.
4. Accessibility and quality are handled per product, late, and inconsistently.
5. Design, code, and documentation describe different realities, and no source
   is authoritative.
6. Cross-channel artifacts — documents, reports, presentations, diagrams,
   repository presentation — have no shared standard at all.
7. Without a shared foundation, every new product pays the full design cost
   again.

CDS exists to solve these problems structurally rather than per product.

## Mission

*(Normative)*

CDS is the central design and brand foundation for the Core ecosystem. It
provides a versioned, normative Single Source of Truth for how Core products
look, behave, communicate, and remain accessible across channels.

## Vision

*(Long-term direction)*

Every Core product — existing and future — derives its design, brand, and
experience foundations from CDS rather than from product-local conventions.
Design, code, and documentation converge on one governed source that is
reviewable, versionable, and usable offline.

## Strategic objectives

*(Normative)*

1. Establish one governed, versioned source for shared design decisions.
2. Keep normative sources tool-independent and reviewable (DEC-S-004).
3. Make the ecosystem recognizable as one family while permitting controlled
   product individuality.
4. Treat accessibility as a designed-in quality area, not a late correction.
5. Support offline and self-hosted use without mandatory external runtime
   services (DEC-S-006).
6. Enable real adoption by real products, validated against a pilot consumer.
7. Keep design, code, and documentation aligned over time.
8. Keep authority human: AI assists, humans approve (DEC-S-005).

## Capability domains

*(Long-term direction — scope taxonomy, see DEC-S-007)*

CDS scope is classified through six capability domains. This taxonomy is a
**scope model**. It does not define technical architecture, repository
architecture, or implementation tooling, and it authorizes no concrete design
work in any domain.

### 1. Brand and Identity

Brand strategy, corporate identity, corporate design, product-family
expression, naming guidance, logos and marks, verbal identity, tone of voice.

This enumeration authorizes no concrete design.

### 2. Experience and Interaction

UX principles, interaction principles, navigation behavior, task flows,
feedback behavior, error handling, complex operational experiences.

### 3. Foundations and Tokens

Color systems, typography systems, spacing, layout, grids, shape, elevation,
motion, design tokens, themes.

No token format, tool, or concrete value is selected.

### 4. Components and Patterns

Reusable components, component contracts, states and variants, accessibility
behavior, compound patterns, operational patterns, content guidance.

### 5. Channels and Communication

Product interfaces, GitHub presentation, documentation, PDF reports,
presentations, diagrams, dashboards, release materials, marketing materials.

### 6. Governance and Enablement

Normative documentation, maturity states, versioning, contribution governance,
adoption guidance, migration guidance, evidence and quality control,
distribution and enablement.

The concrete versioning, contribution, and conformance policy is a **deferred
decision** (CDS-WP-006).

## Cross-cutting concerns

*(Normative as quality requirements — not conformance claims)*

These concerns apply across all six domains:

- accessibility,
- inclusive design,
- localization and internationalization,
- offline and self-hosted use,
- security-aware interaction design,
- privacy-aware interaction design,
- maintainability,
- provenance and licensing,
- quality evidence,
- design-code-documentation alignment.

These are **quality requirements**. They are explicitly **not** a
certification, legal-compliance, or full accessibility-conformance commitment.

## Current Foundation scope

*(Current phase scope)*

Actively worked in the Foundation / Pre-Design phase:

- project concept,
- scope and non-goal definition,
- target and user groups,
- consumer classes,
- ownership boundaries,
- governance foundations,
- benchmark and differentiation planning,
- consumer-requirements planning,
- design-system architecture planning,
- accessibility-policy planning,
- release, contribution, and maturity planning.

**Not yet actively implemented** in this phase:

- concrete brand identity,
- concrete visual designs,
- concrete components,
- concrete design tokens,
- concrete tools or frameworks,
- production packages,
- public releases.

## Long-term scope

*(Long-term direction)*

The long-term scope is the six capability domains plus the cross-cutting
concerns above.

Registration in the long-term scope creates **no** delivery, stability,
support, release, or compatibility commitment (DEC-S-009). Availability is
governed by roadmap and maturity status, both of which are deferred decisions.

## Non-goals

*(Normative)*

1. CDS does not design logos, colors, typography, icons, illustrations, or
   themes in the Foundation phase.
2. CDS does not immediately perform a full redesign of all Core products.
3. CDS replaces neither the Nova Development Framework nor Core Vision nor the
   product governance of individual projects.
4. CDS does not take over product business logic.
5. CDS does not take over product data models or domain data.
6. CDS does not take over operational responsibility for consumer products.
7. CDS does not define backend, network, deployment, or infrastructure
   architecture.
8. CDS currently guarantees neither public availability nor third-party
   support.
9. CDS currently makes no certification, legal-compliance, or full
   accessibility-conformance claim.
10. CDS does not yet promise long-term API or token compatibility.
11. CDS does not become an arbitrary collection of product-specific special
    solutions.
12. Listing a project as a possible consumer is not an automatic brand
    endorsement or recommendation.

## Ownership boundaries

*(Normative, see DEC-S-008)*

CDS owns normative shared design rules and accepted shared design artifacts.
Consumer projects retain ownership of product strategy, business logic, domain
data, runtime operations, infrastructure, and product-specific implementation
decisions outside accepted CDS contracts.

The detailed per-area split is registered in the
[Scope Boundary Matrix](SCOPE_BOUNDARY_MATRIX.md).

### CDS owns

Long-term:

- normative shared design rules,
- approved shared foundations,
- shared tokens, subject to later definition,
- approved components and patterns,
- shared channel standards,
- quality and accessibility requirements,
- design-system documentation,
- maturity and adoption evidence, subject to later definition.

### Consumer projects own

- business logic,
- product strategy,
- domain requirements,
- product data,
- backend and infrastructure,
- security architecture,
- permission models,
- deployment and operations,
- product-specific content,
- product-specific UX decisions not adopted into CDS,
- correct integration of a chosen CDS version.

### Shared or contract-controlled

Explicit coordination is required for:

- new shared components,
- new shared patterns,
- product profile overrides,
- product-specific extensions,
- migrations,
- breaking changes,
- pilot requirements,
- conformance or adoption claims.

The detailed governance for these is a **deferred decision** (CDS-WP-006).

## CoreOps pilot boundary

*(Normative, see DEC-S-002 and DEC-S-011)*

- CoreOps is the first reference consumer.
- CoreOps supplies real requirements and validation cases.
- CoreOps does **not** alone determine CDS architecture.
- CoreOps-specific solutions remain CoreOps-owned by default.

A CoreOps solution becomes a normative CDS artifact only when all of the
following hold:

1. it is relevant to multiple consumers, or is generalizable with a documented
   rationale,
2. it has been checked against CDS principles,
3. it has been explicitly accepted through a CDS work package,
4. it can be documented, tested, and versioned.

The concrete pilot contract is a **deferred decision** (CDS-WP-004).

## Assumptions

*(Assumptions — believed true, not yet validated)*

1. The Core ecosystem will continue to comprise multiple products with a shared
   design need.
2. CoreOps is representative enough to expose real requirements, but not
   representative enough to define the system alone.
3. Enough shared design substance exists across products to justify a shared
   foundation.
4. Offline and self-hosted use will remain a requirement for consumers.
5. Maintainer capacity will stay limited, so scope control and maintainability
   matter more than breadth.
6. Roles may be filled by the same people; no formal design department or
   organizational size is assumed.

Assumptions are validated in CDS-WP-003 and CDS-WP-004.

## Open questions and deferred decisions

*(Deferred decisions)*

No final decision exists for:

- logo and logo architecture,
- colors, typography, icons, illustration, imagery,
- light and dark themes,
- design tool,
- component framework,
- token format and token build system,
- documentation platform,
- package architecture and repository split,
- license,
- public release,
- contribution model,
- long-term compatibility commitments,
- concrete product signatures,
- versioning and maturity model,
- conformance and adoption policy,
- product profile and override governance.

Open questions carried into later work packages:

1. Which shared substance actually generalizes across consumers? → CDS-WP-004
2. How does CDS differentiate from established design systems? → CDS-WP-003
3. What layer model separates normative sources from generated artifacts? →
   CDS-WP-005
4. How are versioning, contribution, and conformance governed? → CDS-WP-006
5. What accessibility level is committed, and how is it evidenced? →
   CDS-WP-007
6. How much product individuality is permitted, and through what mechanism? →
   CDS-WP-005 and CDS-WP-006

## Relationship to later work packages

| Work package | Consumes from this document |
| --- | --- |
| CDS-WP-003 — Benchmark and Differentiation Research | Problem statement, objectives, capability domains, differentiation questions. |
| CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract | Consumer classes, ownership boundaries, CoreOps pilot boundary, assumptions. |
| CDS-WP-005 — Design System Architecture | Capability domains, cross-cutting concerns, ownership boundaries, open questions. |
| CDS-WP-006 — Governance, Versioning, and Contribution Model | Shared/contract-controlled areas, DEC-S-009, DEC-S-012. |
| CDS-WP-007 — Accessibility and Inclusive Design Policy | Cross-cutting concerns, non-goal 9. |
| CDS-WP-008 — Foundation Milestone Review | The whole registered scope, as the review baseline. |

## Change control

*(Normative)*

This document is normative. Changes require:

1. an explicitly authorized work package,
2. a corresponding decision in the
   [Decision Index](../decisions/DECISION_INDEX.md) where the change alters a
   registered decision,
3. consistency updates across the documents that summarize this scope,
4. Human Maintainer approval.

Scope is not extended implicitly, and not by a Skill, a summary document, or a
consumer request. The
[Foundation Context Pack](../../project-system/CONTEXT_PACK_FOUNDATION.md)
summarizes this document; it never overrides it.

## Related documents

- [Consumer and Stakeholder Model](CONSUMER_AND_STAKEHOLDER_MODEL.md)
- [Scope Boundary Matrix](SCOPE_BOUNDARY_MATRIX.md)
- [Project Charter](PROJECT_CHARTER.md)
- [Decision Index](../decisions/DECISION_INDEX.md)
- [Risk Register](../risks/RISK_REGISTER.md)
- [Foundation Context Pack](../../project-system/CONTEXT_PACK_FOUNDATION.md)
