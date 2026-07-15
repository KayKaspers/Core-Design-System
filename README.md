# Core Design System

The Core Design System (CDS) is the central design, brand, user-experience,
interface, component, token, document, and multi-channel foundation for the Core
product ecosystem.

CDS is being built as a versioned platform product with a normative Single
Source of Truth. It is deliberately **not**:

- a logo-only project,
- a branding kit,
- an isolated UI component library,
- a design project scoped exclusively to CoreOps.

## Project status

**Foundation / Pre-Design**

The project currently establishes governance, scope, architecture, and
requirements. It does not yet produce visual design.

No final decision exists for:

- logo and logo architecture,
- colors,
- typography,
- icons, illustration, and imagery,
- light and dark themes,
- design tool,
- component framework,
- token format and token build system,
- documentation platform,
- package architecture and repository split,
- license, public release, and contribution model,
- long-term compatibility commitments,
- concrete product signatures.

These areas remain open until an explicitly authorized work package decides
them.

## Pilot consumer

CoreOps is the first reference consumer of stable CDS foundations and provides
adoption evidence.

CoreOps is a reference consumer — not the sole design target and not the sole
source of requirements. SpeakCore, CastCore, AirCore, and future Core products
are anticipated consumers.

## Operating model

This project follows the Nova Development Framework v1.0.0.

| Role | Authority |
| --- | --- |
| Human Maintainer | Final normative approvals; exclusive authority over commit, push, merge, branch operations, tag, release, and publication. |
| Nova | Strategy, architecture, work-package planning, review, project control, approval recommendations. |
| Claude | Scoped local analysis and file work; no Git writes, no publication. |
| Consumer projects | Requirements input and adoption evidence. |

Claude Desktop with a locally connected repository is the execution environment
for Claude work.

## Work packages

- **Completed:** CDS-WP-001 — Project Governance and NDF Bootstrap
- **Next:** CDS-WP-001A — NDF Skills Bootstrap

The full controlled roadmap is in
[project-system/WORK_PACKAGES.md](project-system/WORK_PACKAGES.md).

## Registers

- Decisions: DEC-S-001 … DEC-S-006 (6 strategic foundation decisions)
- Risks: RISK-001 … RISK-005 (5 initial risks)

## Governance documents

- [Project Charter](docs/governance/PROJECT_CHARTER.md)
- [Decision Index](docs/decisions/DECISION_INDEX.md)
- [Risk Register](docs/risks/RISK_REGISTER.md)
- [Project Profile](project-system/PROJECT_PROFILE.md)
- [Work Packages](project-system/WORK_PACKAGES.md)
- [Next Phase](project-system/NEXT_PHASE.md)
- [Project Brain](project-brain/PROJECT_BRAIN.md)
- [Claude working instructions](CLAUDE.md)

## Repository status

This repository is initially private.

Licensing, public-release policy, contribution policy, and compatibility
commitments remain intentionally undecided.
