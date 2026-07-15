# Work Packages

Controlled work-package roadmap for the Core Design System (CDS).

- **Phase:** Foundation / Pre-Design
- **Completed work packages:** CDS-WP-001, CDS-WP-001A
- **Next work package:** CDS-WP-002

## Status values

| Status | Meaning |
| --- | --- |
| Completed | Work package finished and reported for review. |
| Next | Authorized as the immediate next work package. |
| Planned | Part of the roadmap; not yet authorized to start. |

## Roadmap

| ID | Title | Status | Depends on |
| --- | --- | --- | --- |
| CDS-WP-001 | Project Governance and NDF Bootstrap | Completed | — |
| CDS-WP-001A | NDF Skills Bootstrap | Completed | CDS-WP-001 |
| CDS-WP-002 | Concept and Scope Registration | Next | CDS-WP-001A |
| CDS-WP-003 | Benchmark and Differentiation Research | Planned | CDS-WP-002 |
| CDS-WP-004 | Consumer Requirements and CoreOps Pilot Contract | Planned | CDS-WP-002 |
| CDS-WP-005 | Design System Architecture | Planned | CDS-WP-003, CDS-WP-004 |
| CDS-WP-006 | Governance, Versioning, and Contribution Model | Planned | CDS-WP-005 |
| CDS-WP-007 | Accessibility and Inclusive Design Policy | Planned | CDS-WP-005 |
| CDS-WP-008 | Foundation Milestone Review | Planned | CDS-WP-006, CDS-WP-007 |

## Descriptions

### CDS-WP-001 — Project Governance and NDF Bootstrap

**Status:** Completed

Establishes the minimal governance and project-control foundation: project
identity, mission and boundaries, role and authority model, strategic
foundation decisions, initial risks, and the controlled work-package roadmap.
Governance and documentation work only; no visual design.

### CDS-WP-001A — NDF Skills Bootstrap

**Status:** Completed

Controlled adoption and verification of the approved NDF v1.0.0 Skills into
this repository, without modifying their normative upstream content. Adopted 38
verified docs-only Skills pinned to NDF v1.0.0 and activated the Skills-first
operating mode. See
[NDF Skills Provenance](../docs/governance/NDF_SKILLS_PROVENANCE.md) and
[NDF Skills Inventory](NDF_SKILLS_INVENTORY.md).

### CDS-WP-002 — Concept and Scope Registration

**Status:** Next

Formally registers the CDS concept, scope, non-goals, target audiences,
consumer classes, and project boundaries, separating long-term scope from
currently authorized scope. No concrete visual or technical design decisions.

### CDS-WP-003 — Benchmark and Differentiation Research

**Status:** Planned

Analyzes established design systems and derives the differentiation position of
CDS within the Core ecosystem.

### CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract

**Status:** Planned

Collects requirements from Core consumer products and defines the pilot
contract with CoreOps, including adoption expectations and evidence
obligations.

### CDS-WP-005 — Design System Architecture

**Status:** Planned

Defines the architecture of CDS: layer model, separation of normative sources
from generated artifacts, and distribution direction — evaluated against
tool-independence (DEC-S-004) and offline usability (DEC-S-006).

### CDS-WP-006 — Governance, Versioning, and Contribution Model

**Status:** Planned

Establishes versioning, release, review, deprecation, adoption levels, and the
contribution model.

### CDS-WP-007 — Accessibility and Inclusive Design Policy

**Status:** Planned

Defines the binding accessibility and inclusive-design policy and its
verification approach.

### CDS-WP-008 — Foundation Milestone Review

**Status:** Planned

Reviews the completed Foundation phase and determines whether concrete visual
and technical design decisions may be authorized.

## Roadmap evolution

This roadmap is the initial controlled sequence. It may be extended or refined
in a controlled manner after later reviews. Extensions require Nova planning and
Human Maintainer approval; work packages are not added ad hoc during execution.

## Related documents

- [Next Phase](NEXT_PHASE.md)
- [Project Profile](PROJECT_PROFILE.md)
- [Project Charter](../docs/governance/PROJECT_CHARTER.md)
- [Decision Index](../docs/decisions/DECISION_INDEX.md)
- [Risk Register](../docs/risks/RISK_REGISTER.md)
