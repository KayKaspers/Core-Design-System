# Work Packages

Controlled work-package roadmap for the Core Design System (CDS).

- **Phase:** Foundation / Pre-Design
- **Completed work packages:** CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004
- **Next work package:** CDS-WP-005

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
| CDS-WP-002 | Concept and Scope Registration | Completed | CDS-WP-001A |
| CDS-WP-003 | Benchmark and Differentiation Research | Completed | CDS-WP-002 |
| CDS-WP-004 | Consumer Requirements and CoreOps Pilot Contract | Completed | CDS-WP-002 |
| CDS-WP-005 | Design System Architecture | Next | CDS-WP-003, CDS-WP-004 |
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

**Status:** Completed

Registered the CDS concept, six capability domains, cross-cutting concerns,
current and long-term scope, non-goals, user groups, three consumer classes,
ownership boundaries, and the CoreOps pilot boundary. Added DEC-S-007…DEC-S-012
and RISK-006…RISK-009, and established the Foundation Context Pack. See
[Concept and Scope](../docs/governance/CONCEPT_AND_SCOPE.md),
[Consumer and Stakeholder Model](../docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md),
and [Scope Boundary Matrix](../docs/governance/SCOPE_BOUNDARY_MATRIX.md).

### CDS-WP-003 — Benchmark and Differentiation Research

**Status:** Completed

Reviewed ten established design systems against 14 dimensions using official
sources only, and assessed eight CDS differentiation hypotheses
(HYP-001 … HYP-008). Added RISK-010 … RISK-013. Findings are research evidence
and remain **non-normative**; no decision was added or changed. See
[Design System Benchmark](../docs/research/DESIGN_SYSTEM_BENCHMARK.md),
[Evidence Matrix](../docs/research/BENCHMARK_EVIDENCE_MATRIX.md),
[Source Register](../docs/research/BENCHMARK_SOURCE_REGISTER.md),
[Differentiation Hypotheses](../docs/research/CDS_DIFFERENTIATION_HYPOTHESES.md),
and [Research Limitations](../docs/research/RESEARCH_LIMITATIONS.md).

### CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract

**Status:** Completed

Analyzed three consumer repositories at committed revisions, registered
CR-001 … CR-040 with traceability, defined the bounded CoreOps pilot
(Groups A–E, 9 scenarios) and its contract, and assessed HYP-001 … HYP-008
against consumer evidence. Added DEC-S-013 … DEC-S-020 and RISK-014 … RISK-019.
See [Consumer Requirements Model](../docs/governance/CONSUMER_REQUIREMENTS_MODEL.md),
[CoreOps Pilot Contract](../docs/governance/COREOPS_PILOT_CONTRACT.md), and
[Consumer Evidence Register](../docs/research/CONSUMER_EVIDENCE_REGISTER.md).

### CDS-WP-005 — Design System Architecture

**Status:** Next

Defines the architecture of CDS: normative system layers, source-of-truth model,
token flow as architecture without selecting a format, artifact classes, product
profiles, distribution, consumer contracts, and evidence flows — evaluated
against tool-independence (DEC-S-004) and offline usability (DEC-S-006). No final
visual design and no concrete tool, framework, or token-format decision.

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
