# Scope Boundary Matrix

- **Project:** Core Design System (CDS)
- **Phase:** Foundation / Pre-Design
- **Registered by:** CDS-WP-002 — Concept and Scope Registration
- **Date:** 2026-07-15

## Purpose

This matrix registers, per domain or concern, who is responsible: CDS, the
consumer project, or both under an explicit contract. It also records the
current Foundation status and where the concrete decision is made.

The matrix **selects no technical solution**. It assigns responsibility only.

Normative scope is registered in [Concept and Scope](CONCEPT_AND_SCOPE.md),
which takes precedence over this summary.

## Reading the matrix

| Column | Meaning |
| --- | --- |
| CDS responsibility | What CDS owns, long-term. |
| Consumer responsibility | What the consumer project owns. |
| Shared / contract-controlled | What requires explicit coordination between both. |
| Current Foundation status | What is actually true today. |
| Future decision / WP | Where the concrete decision is made. |

**Status values:** `Not started` · `Planning` · `Registered` · `Deferred` ·
`Out of scope (permanent)`

Long-term responsibility is **not** a delivery commitment (DEC-S-009).

## Matrix

| Domain or concern | CDS responsibility | Consumer responsibility | Shared or contract-controlled | Current Foundation status | Future decision / WP |
| --- | --- | --- | --- | --- | --- |
| Brand strategy | Normative brand strategy and product-family expression for the ecosystem | Correct application within the product; product-local voice within permitted limits | Product profiles; brand-usage grants; deviations | Registered as scope; no concrete brand work | CDS-WP-005, CDS-WP-006 |
| Visual foundations | Normative visual foundations once approved | Correct application of a chosen CDS version | Product-specific overrides | Registered as scope; no concrete values chosen | Post-Foundation, after CDS-WP-008 |
| Design tokens | Shared token definitions, subject to later definition | Integration of the chosen token distribution into the product build | Product-specific token extensions and overrides | Registered as scope; no format, tooling, or values chosen | CDS-WP-005 (architecture), CDS-WP-006 (versioning) |
| UI components | Approved shared components and their contracts, states, variants, and accessibility behavior | Product-specific components not adopted into CDS; correct integration | New shared components; extensions; breaking changes; migrations | Registered as scope; no components built | CDS-WP-005 |
| UX patterns | Approved shared patterns and interaction principles | Product-specific flows and domain UX not adopted into CDS | New shared patterns; generalization of product patterns | Registered as scope; no patterns defined | CDS-WP-005 |
| Accessibility | Normative accessibility and inclusive-design requirements for CDS artifacts | Accessibility of product-specific implementation and content; verification in the product | Evidence model; conformance claims; exceptions | Registered as cross-cutting concern; **no conformance or certification claim** | CDS-WP-007 |
| Product business logic | — | Full ownership | — | **Out of scope (permanent)** — Non-goal 4 | None |
| Domain data | — | Full ownership: data models, domain data, semantics | Data-presentation guidance only, where it becomes a shared pattern | **Out of scope (permanent)** — Non-goal 5 | None |
| Backend architecture | — | Full ownership | — | **Out of scope (permanent)** — Non-goal 7 | None |
| Security architecture | Security-aware interaction design only | Security architecture, permission models, threat handling | Interaction patterns with security implications | **Out of scope (permanent)** for architecture; interaction design registered as cross-cutting | CDS-WP-005 (interaction design only) |
| Deployment and operations | — | Full ownership, including operating the product | Distribution format of CDS artifacts and its offline constraints | **Out of scope (permanent)** — Non-goal 6 and 7 | CDS-WP-005 (artifact distribution only) |
| Documentation | Design-system documentation and shared documentation standards | Product documentation content | Documentation platform; adoption guidance | Registered as scope; standards not defined | CDS-WP-005, CDS-WP-006 |
| PDF and reports | Shared document and report standards | Product-specific report content and data | Product-specific report profiles | Registered as scope; no standards defined | Post-Foundation |
| Presentations | Shared presentation standards | Presentation content | Product-specific presentation profiles | Registered as scope; no standards defined | Post-Foundation |
| Diagrams | Shared diagram standards | Diagram content and domain semantics | Product-specific diagram conventions | Registered as scope; no standards defined | Post-Foundation |
| GitHub presentation | Shared repository-presentation and content standards | Repository-specific content | Deviations for project-specific needs | Registered as scope; no standards defined | Post-Foundation |
| Marketing materials | Shared brand, verbal identity, and channel standards | Product-specific campaign content and claims | Product-specific marketing profiles | Registered as scope; no standards defined | Post-Foundation |
| Product profiles | The profile mechanism and its governance | Requesting and applying a profile; product-local decisions inside it | Every profile and override; the permitted degree of individuality | Registered as concept; mechanism not defined | CDS-WP-005 (mechanism), CDS-WP-006 (governance) |
| Adoption and conformance | Adoption levels, conformance criteria, and the evidence model | Producing adoption evidence; claiming only what is evidenced | Every conformance or adoption claim; version reference | Registered as concept; **no claim may be made today** (DEC-S-012) | CDS-WP-006 |
| Licensing and publication | Licensing and publication of CDS artifacts | Compliance with the chosen license once decided | External distribution of CDS artifacts | **Deferred** — undecided; no public availability, licensing, or support commitment | Deferred, no WP assigned |

## Boundary notes

*(Normative)*

1. **Permanent out-of-scope entries** are non-goals, not deferrals. They do not
   become CDS responsibility in a later phase. Reversing one requires a
   governance decision, not a work package assumption.
2. **Registered ≠ available.** A domain marked `Registered` is in the long-term
   scope with no delivery, stability, support, or schedule commitment
   (DEC-S-009).
3. **Shared means contract-controlled, not informal.** Anything in the shared
   column requires explicit coordination. The governance for that coordination
   is deferred to CDS-WP-006.
4. **Consumer responsibility includes integration.** Choosing and correctly
   integrating a specific CDS version is always the consumer's responsibility.
5. **The pilot is not an exception.** CoreOps entries follow this matrix.
   CoreOps-specific solutions remain CoreOps-owned unless explicitly
   generalized and accepted (DEC-S-011).
6. **This matrix chooses nothing technical.** No tool, format, framework,
   platform, or value is selected in any row.

## Open boundary questions

*(Deferred decisions)*

1. Where exactly does a shared pattern end and product-specific UX begin? →
   CDS-WP-004, CDS-WP-005
2. How much individuality may a product profile express before it fragments the
   system? → CDS-WP-005, CDS-WP-006
3. Who owns a component that only one consumer currently needs? → CDS-WP-004
4. What evidence makes an adoption claim legitimate? → CDS-WP-006
5. Does data-presentation guidance for dashboards reach into domain semantics,
   and if so, how far? → CDS-WP-005

## Related documents

- [Concept and Scope](CONCEPT_AND_SCOPE.md) — normative scope source
- [Consumer and Stakeholder Model](CONSUMER_AND_STAKEHOLDER_MODEL.md)
- [Decision Index](../decisions/DECISION_INDEX.md)
- [Risk Register](../risks/RISK_REGISTER.md)
