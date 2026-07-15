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

The long-term scope of CDS includes:

- brand strategy,
- corporate identity,
- corporate design,
- design principles,
- UX,
- UI,
- components,
- design tokens,
- colors,
- typography,
- icons,
- logos,
- GitHub presentation,
- document design,
- PDF layouts,
- presentations,
- diagram standards,
- dashboards,
- accessibility,
- motion,
- marketing materials,
- product-family governance.

This list describes the long-term scope. It does **not** authorize concrete work
in any of these areas. Each area requires an explicitly authorized work package
before implementation begins.

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

## Related documents

- [Decision Index](../decisions/DECISION_INDEX.md)
- [Risk Register](../risks/RISK_REGISTER.md)
- [Project Profile](../../project-system/PROJECT_PROFILE.md)
- [Work Packages](../../project-system/WORK_PACKAGES.md)
- [Next Phase](../../project-system/NEXT_PHASE.md)
- [Project Brain](../../project-brain/PROJECT_BRAIN.md)
