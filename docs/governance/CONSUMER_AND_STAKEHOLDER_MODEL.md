# Consumer and Stakeholder Model

- **Project:** Core Design System (CDS)
- **Phase:** Foundation / Pre-Design
- **Registered by:** CDS-WP-002 — Concept and Scope Registration
- **Date:** 2026-07-15

## Purpose

This document registers who uses CDS, who benefits from it indirectly, and what
kinds of consumer relationship CDS distinguishes.

It is normative for the consumer classification. It is **not** a brand
architecture, not an adoption plan, and not a commitment to serve any listed
party. Scope itself is registered in
[Concept and Scope](CONCEPT_AND_SCOPE.md), which takes precedence.

## Direct users

*(Normative)*

People who work with CDS artifacts directly:

| Role | Relationship to CDS |
| --- | --- |
| CDS maintainers and governance owners | Define, review, and version the normative foundation. |
| Product maintainers | Choose a CDS version, adopt it, and own their product's integration. |
| UX and UI contributors | Apply and propose experience and interface guidance. |
| Frontend and application implementers | Implement against CDS foundations, components, and contracts. |
| Documentation and technical-writing contributors | Apply documentation and content guidance. |
| Report and presentation authors | Apply channel standards to documents, reports, and presentations. |
| Brand and communication contributors | Apply and propose brand and identity guidance. |
| QA, accessibility, and validation reviewers | Verify adoption and quality against CDS requirements. |

These roles are **functions, not positions**. In small projects the same person
may hold several of them, and often will. CDS assumes no organizational size,
no formal design department, and no dedicated design staffing.

## Indirect beneficiaries

*(Normative)*

People and groups affected by CDS without working on it:

- administrators and operators using Core products,
- technical and non-technical end users,
- self-hosted users and organizations,
- maintainers of associated projects,
- future external adopters, if and when later authorized.

Indirect beneficiaries shape quality requirements — particularly accessibility,
clarity, and offline usability — but they are not a requirements channel and
not a support relationship.

## Stakeholder roles

*(Normative — mirrors the established authority model)*

| Role | Stake |
| --- | --- |
| Human Maintainer | Final normative approvals; exclusive authority over Git writes, releases, publication, and repository visibility (DEC-S-005). |
| Nova | Strategy, architecture, work-package planning, review, project control, approval recommendations. |
| Claude | Scoped local analysis and documentation work only. No authority. |
| Consumer projects | Requirements input and adoption evidence. Not decision authority over CDS. |
| CoreOps (pilot) | First reference consumer; supplies real requirements and validation cases (DEC-S-002). |

## Consumer relationship classes

*(Normative, see DEC-S-010)*

CDS recognizes exactly three consumer relationship classes.

### Core Product Consumer

A product of the Core ecosystem that may in future pursue comprehensive or
controlled, profiled CDS adoption.

Examples that may be named: CoreOps, SpeakCore, CastCore, AirCore.

Naming a product here is **not** a statement that adoption has occurred, been
agreed, been scheduled, or been approved.

### Associated Project Consumer

An associated or affiliated project that may use selected CDS foundations,
components, or channel standards without automatically becoming a full part of
the Core master brand.

### Potential External Consumer

A future external user or external self-hosted project that could use published
CDS artifacts.

For this class specifically:

- public availability remains **undecided**,
- support remains **undecided**,
- licensing remains **undecided**,
- external use is **not** a current commitment.

## Channel-consumer categories

*(Long-term direction)*

Consumption is not only by products. CDS anticipates these channel-consumer
categories, matching the Channels and Communication domain:

| Category | Consumes |
| --- | --- |
| Product interfaces | Foundations, components, patterns, interaction guidance. |
| Repository and GitHub presentation | Presentation and content standards. |
| Documentation | Documentation standards and content guidance. |
| Reports and PDF | Document and report standards. |
| Presentations | Presentation standards. |
| Diagrams | Diagram standards. |
| Dashboards | Data-presentation and component guidance. |
| Release and marketing materials | Brand, verbal identity, and channel standards. |

Listing a category registers intent. It authorizes no concrete work and
promises no artifact.

## Limitations of the classification

*(Normative)*

The consumer classification is a **relationship model only**. Classification by
itself grants none of the following:

- brand endorsement or recommendation,
- permission to use Core brand assets,
- public availability of CDS artifacts,
- licensing rights,
- support commitments,
- delivery or scheduling commitments,
- influence over CDS decisions,
- conformance status.

### No automatic endorsement

Being listed as a possible consumer of any class is not an endorsement, not an
approval of the project, and not a brand-usage grant. Brand usage is governed
separately and is a deferred decision.

### No public-release commitment

Nothing in this document commits CDS to publish artifacts, to license them for
external use, to support external consumers, or to make any artifact available
outside the ecosystem. Public availability, licensing, and support are
**deferred decisions**.

### Not a final brand architecture

This model classifies **relationships**, not brand hierarchy. Product-family
classes, brand tiers, adoption levels, and product profiles are deferred to
later work packages (CDS-WP-004, CDS-WP-005, CDS-WP-006).

## CoreOps reference-consumer role

*(Normative)*

CoreOps is the first reference consumer. It supplies real requirements and real
validation cases, and it produces the first adoption evidence.

Its influence is explicitly bounded:

- CoreOps does not alone determine CDS architecture,
- CoreOps requirements are inputs, not definitions (DEC-S-002),
- CoreOps-specific solutions remain CoreOps-owned by default (DEC-S-011),
- generalization into CDS requires explicit acceptance through a CDS work
  package.

The full pilot boundary is registered in
[Concept and Scope](CONCEPT_AND_SCOPE.md). The concrete pilot contract is
deferred to CDS-WP-004.

## Future validation direction

*(Long-term direction)*

The consumer model is a registered hypothesis and must be validated rather than
assumed:

1. **CDS-WP-004** collects requirements from Core consumers beyond the pilot and
   establishes the CoreOps pilot contract, testing whether the three classes
   hold against real needs.
2. **CDS-WP-005** tests whether the classes can be served by one architecture
   with controlled profiling, or whether the model needs revision.
3. **CDS-WP-006** defines adoption levels, conformance, and the evidence model
   that turns a relationship class into a verifiable status (DEC-S-012).

If validation contradicts this model, the model changes through governance —
not the validation.

## Related documents

- [Concept and Scope](CONCEPT_AND_SCOPE.md) — normative scope source
- [Scope Boundary Matrix](SCOPE_BOUNDARY_MATRIX.md)
- [Decision Index](../decisions/DECISION_INDEX.md)
- [Risk Register](../risks/RISK_REGISTER.md)
