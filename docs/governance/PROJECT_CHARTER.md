# Core Design System — Project Charter

- **Project:** Core Design System
- **Abbreviation:** CDS
- **Repository:** KayKaspers/Core-Design-System
- **Local path:** `D:\Projects\Core-Design-System`
- **Framework:** Nova Development Framework v1.0.0
- **Phase:** Foundation / Pre-Design

## Mission

CDS is the central design and brand foundation for the Core ecosystem. It
provides a versioned, normative Single Source of Truth for how Core products
look, behave, communicate, and remain accessible across channels.

## Vision

Every Core product — existing and future — derives its design, brand, and
experience foundations from CDS rather than from product-local conventions.
Design, code, and documentation converge on one governed source that is
reviewable, versionable, and usable offline.

## Strategic purpose

CDS exists to make design decisions durable and shared. A design decision
becomes part of CDS only when it is strategically justified, documented,
implementable, reviewable, and versionable.

CDS is deliberately **not**:

- a logo-only project,
- a branding kit,
- an isolated UI component library,
- a design project scoped exclusively to CoreOps.

## Scope categories

The CDS scope is registered normatively in
[Concept and Scope](CONCEPT_AND_SCOPE.md). That document takes precedence over
this summary.

The long-term scope is classified through six capability domains (DEC-S-007):

1. **Brand and Identity**
2. **Experience and Interaction**
3. **Foundations and Tokens**
4. **Components and Patterns**
5. **Channels and Communication**
6. **Governance and Enablement**

Cross-cutting quality concerns apply across all six: accessibility, inclusive
design, localization and internationalization, offline and self-hosted use,
security-aware interaction design, privacy-aware interaction design,
maintainability, provenance and licensing, quality evidence, and
design-code-documentation alignment. These are quality requirements — not
certification, legal-compliance, or conformance commitments.

This describes the long-term scope. It does **not** authorize concrete work in
any of these areas, and inclusion creates no delivery, stability, support,
release, or compatibility commitment (DEC-S-009). Each area requires an
explicitly authorized work package before implementation begins.

The per-area responsibility split between CDS and its consumers is registered
in the [Scope Boundary Matrix](SCOPE_BOUNDARY_MATRIX.md); the non-goals are
registered in [Concept and Scope](CONCEPT_AND_SCOPE.md).

## Current phase boundary

The current phase establishes governance, scope, architecture, and
requirements. It does not authorize concrete visual or technical design
decisions (see DEC-S-003).

### Non-goals of the current phase

The following are explicitly out of scope until a later work package authorizes
them:

- selecting or creating logos and logo architecture,
- selecting colors, typography, icons, illustration, or imagery,
- defining light or dark themes,
- selecting a design tool,
- selecting a component framework,
- selecting a token format or token build system,
- selecting a documentation platform,
- deciding package architecture or repository split,
- selecting a license,
- deciding public release, contribution model, or compatibility commitments,
- defining concrete product signatures.

## Pilot-consumer relationship

CoreOps is the first reference consumer of CDS. It provides adoption evidence
and real-world validation for stable foundations.

CoreOps is not the sole design target and not the sole source of requirements
(see DEC-S-002). Further Core products — including SpeakCore, CastCore, and
AirCore — are anticipated consumers. Consumer inclusion does not automatically
authorize full brand adoption; product-family classes and adoption levels remain
to be defined.

CDS distinguishes three consumer relationship classes — Core Product Consumer,
Associated Project Consumer, and Potential External Consumer (DEC-S-010).
Classification grants no brand endorsement, public availability, licensing
rights, or support. The full model is registered in the
[Consumer and Stakeholder Model](CONSUMER_AND_STAKEHOLDER_MODEL.md).

CoreOps-specific solutions remain CoreOps-owned unless they are generalized and
explicitly accepted through a CDS work package (DEC-S-011). The concrete pilot
contract is defined in CDS-WP-004.

## Authority model

| Role | Authority |
| --- | --- |
| Human Maintainer | Final normative approvals; exclusive authority over commit, push, merge, branch operations, tag, release, publication, and repository visibility. |
| Nova | Strategy, project architecture, work-package planning, review, project control, and approval recommendations. |
| Claude | Scoped local analysis and file work within explicitly allowed scope. No Git writes, no publication. |
| Consumer projects | Requirements input and adoption evidence. |

AI assistance is permitted throughout. Normative approval remains human
(see DEC-S-005).

## Quality commitments

- Accessibility is a first-class quality area, designed in rather than added
  later.
- Offline and self-hosted usability are core requirements (see DEC-S-006).
- Normative sources must remain tool-independent (see DEC-S-004).
- Product individuality must remain controlled and governable.

## Foundation completion direction

The Foundation phase is complete when scope is registered, benchmark and
differentiation research is available, consumer requirements including the
CoreOps pilot contract are captured, the design-system architecture is defined,
the governance/versioning/contribution model is established, the accessibility
policy is set, and the Foundation Milestone Review has passed.

Only after that review may concrete visual and technical design decisions be
authorized.

### Foundation status

| Step | Status |
| --- | --- |
| Governance foundation established (CDS-WP-001) | Done |
| NDF Skills adopted and verified (CDS-WP-001A) | Done |
| Concept and scope registered (CDS-WP-002) | Done |
| Benchmark and differentiation research (CDS-WP-003) | Next |
| Consumer requirements and CoreOps pilot contract (CDS-WP-004) | Planned |
| Design-system architecture (CDS-WP-005) | Planned |
| Governance, versioning, contribution model (CDS-WP-006) | Planned |
| Accessibility and inclusive-design policy (CDS-WP-007) | Planned |
| Foundation Milestone Review (CDS-WP-008) | Planned |

## Related documents

- [Concept and Scope](CONCEPT_AND_SCOPE.md) — normative scope source
- [Consumer and Stakeholder Model](CONSUMER_AND_STAKEHOLDER_MODEL.md)
- [Scope Boundary Matrix](SCOPE_BOUNDARY_MATRIX.md)
- [Decision Index](../decisions/DECISION_INDEX.md)
- [Risk Register](../risks/RISK_REGISTER.md)
- [Project Profile](../../project-system/PROJECT_PROFILE.md)
- [Work Packages](../../project-system/WORK_PACKAGES.md)
- [Next Phase](../../project-system/NEXT_PHASE.md)
- [Foundation Context Pack](../../project-system/CONTEXT_PACK_FOUNDATION.md)
- [Project Brain](../../project-brain/PROJECT_BRAIN.md)
