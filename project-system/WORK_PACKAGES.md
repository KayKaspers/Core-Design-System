# Work Packages

Controlled work-package roadmap for the Core Design System (CDS).

- **Phase:** Foundation / Pre-Design
- **Completed work packages:** CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005, CDS-WP-006, CDS-WP-007
- **Next work package:** CDS-WP-008

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
| CDS-WP-005 | Design System Architecture | Completed | CDS-WP-003, CDS-WP-004 |
| CDS-WP-006 | Governance, Versioning, and Contribution Model | Completed | CDS-WP-005 |
| CDS-WP-007 | Accessibility and Inclusive Design Policy | Completed | CDS-WP-005 |
| CDS-WP-008 | Foundation Milestone Review | Next | CDS-WP-006, CDS-WP-007 |

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

**Status:** Completed

Defined the eight-layer logical architecture, the source-of-truth and authority
model with eight artifact classes, the five-level conceptual token flow, the
product profile and extension model with existing-product reconciliation, the
channel and distribution model, the five consumer contracts, and the evidence and
status-semantics architecture including the Unknown invariant. Mapped
CR-001 … CR-040 to the architecture. Added DEC-S-021 … DEC-S-032 and
RISK-020 … RISK-028. **No technology, format, or visual decision.** See
[Design System Architecture](../docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md).

### CDS-WP-006 — Governance, Versioning, and Contribution Model

**Status:** Completed

Established the governance operating model (six roles, two tracks), the source
conflict resolution policy, the seven-state artifact maturity lifecycle,
semantic versioning with eight compatibility axes, deprecation and removal,
contribution and acceptance, exception and Product Profile governance, four
graded adoption claim types, the **finalized risk owner model**, five publication
states with a gate, licensing per ten artifact classes, and release and change
control. Added DEC-S-033 … DEC-S-048 and RISK-029 … RISK-040. **No licence,
publication, technology, or design selected.** See
[Governance Operating Model](../docs/governance/GOVERNANCE_OPERATING_MODEL.md).

### CDS-WP-007 — Accessibility and Inclusive Design Policy

**Status:** Completed

Defined the binding accessibility and inclusive-design policy and its
verification approach — the target **WCAG 2.2 Level AA** for the applicable web
scope (resolving CR-024 at policy level), the target-versus-claim boundary,
inclusive-design scope, role boundaries, a complete Level A/AA applicability
matrix (56 listed / 55 applicable), five evidence levels (AE-0…AE-4), six channel
profiles, the limitations and exception policy, and the CoreOps pilot
accessibility criterion. Reconciled CR-021, CR-022, CR-024, and CR-034
traceability. Added DEC-S-049 … DEC-S-060 and RISK-041 … RISK-048. **No artifact
promoted; no claim, tag, or release created; every artifact remains AE-0;
publication state remains `Private Development`.** See
[Accessibility and Inclusive Design Policy](../docs/governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md).

### CDS-WP-008 — Foundation Milestone Review

**Status:** Next

Reviews the completed Foundation phase — decision and risk consistency,
architecture and governance coherence, accessibility-policy completeness,
consumer-requirement coverage, unresolved blockers, governance affordability,
Candidate-readiness, and CoreOps pilot entry readiness — and determines whether
concrete visual and technical design decisions may be authorized. Starts no
implementation.

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
