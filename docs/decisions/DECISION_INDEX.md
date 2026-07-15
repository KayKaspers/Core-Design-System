# Decision Index

This index records the strategic decisions of the Core Design System (CDS).

All decisions listed here define purpose, boundaries, scope, and authority.
They do **not** select tools, formats, frameworks, repository structures, or
any concrete visual or implementation technology.

Concrete implementation and visual decisions require separate, explicitly
authorized work packages.

## Register scope

- Decision range: DEC-S-001 … DEC-S-012
- Number of decisions: 12
- Decision record format: index entries only; no ADR files exist in this phase.

## Decision types

| Type | Range | Registered by | Character |
| --- | --- | --- | --- |
| Strategic foundation decision | DEC-S-001 … DEC-S-006 | CDS-WP-001 | Purpose, boundaries, and authority of the project. |
| Strategic scope decision | DEC-S-007 … DEC-S-012 | CDS-WP-002 | Scope classification, ownership, consumer relationships, and commitment limits. |

Neither type is an implementation decision.

## Status values

| Status | Meaning |
| --- | --- |
| Accepted | Decision is normative for the project. |
| Superseded | Decision has been replaced by a later decision. |
| Withdrawn | Decision was revoked without replacement. |

---

## DEC-S-001 — CDS is a versioned platform product

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic foundation decision
- **Work package:** CDS-WP-001

### Decision

CDS is a versioned platform product and normative design foundation, not a
logo-only project, branding kit, or isolated component library.

### Rationale

The Core ecosystem needs a durable, governed foundation that spans brand,
experience, interface, tokens, components, documents, and further channels.
A narrower framing would produce artifacts that cannot be governed, versioned,
or consumed consistently across products.

### Consequences

- CDS requires product-grade governance, versioning, and release discipline.
- Deliverables must be reviewable, versionable, and consumable by real products.
- Work that only produces isolated visual assets does not satisfy the mission.

---

## DEC-S-002 — CoreOps is the first reference consumer, not the sole target

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic foundation decision
- **Work package:** CDS-WP-001

### Decision

CoreOps is the first reference consumer of CDS but is not the sole design
target or sole source of requirements.

### Rationale

A pilot consumer provides essential adoption evidence and real-world
validation. Treating that pilot as the only requirement source would produce a
system that fits one product and fails the rest of the ecosystem.

### Consequences

- CoreOps requirements are inputs, not the definition of CDS scope.
- Requirements from further Core products must be collected before foundations
  are frozen.
- Generalization must be evaluated deliberately rather than assumed.

---

## DEC-S-003 — Governance precedes concrete design decisions

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic foundation decision
- **Work package:** CDS-WP-001

### Decision

Governance, scope, architecture, and requirements must be established before
concrete visual or technical design decisions are authorized.

### Rationale

Design decisions made without documented strategy, requirements, and review
paths cannot be justified, evaluated, or safely revised later.

### Consequences

- The current phase produces governance and documentation only.
- Visual and technical decisions require explicit authorization in a later work
  package.
- Any premature decision must be treated as a deviation and reported.

---

## DEC-S-004 — Normative sources must remain tool-independent

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic foundation decision
- **Work package:** CDS-WP-001

### Decision

Normative CDS sources must remain tool-independent enough to prevent a
proprietary design tool from becoming the only source of truth.

This decision does not select a token format, tool, repository structure, or
implementation technology.

### Rationale

If normative content exists only inside a proprietary tool, the project loses
reviewability, portability, and long-term control over its own foundation.

### Consequences

- A clear distinction between normative sources and generated artifacts must be
  maintained.
- Tool selection in later work packages must be evaluated against this
  constraint.
- Generated output must never be treated as an authoritative source.

---

## DEC-S-005 — Human Maintainer retains exclusive publication authority

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic foundation decision
- **Work package:** CDS-WP-001

### Decision

The Human Maintainer retains exclusive authority over Git writes, releases,
publication, and final normative approvals.

Claude performs scoped local work only.

### Rationale

Normative design authority and outward-facing publication carry consequences
that must remain under human control, independent of how much of the work is
AI-assisted.

### Consequences

- Claude must not commit, push, merge, tag, release, or publish.
- Approval recommendations are advisory; approval itself is human.
- Every completed work package ends with a report for human review.

---

## DEC-S-006 — Offline and self-hosted operation must remain possible

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic foundation decision
- **Work package:** CDS-WP-001

### Decision

CDS runtime artifacts and consumer usage must be capable of supporting offline
and self-hosted environments without mandatory external runtime services.

### Rationale

Core products must be deployable in environments without dependable or
permitted external network access. A design foundation that requires external
runtime services would block those deployments.

### Consequences

- Later architecture work must evaluate distribution formats against offline
  use.
- Mandatory external runtime dependencies are not acceptable in CDS artifacts.
- Optional external services remain possible only as non-mandatory additions.

---

## DEC-S-007 — CDS scope is classified through capability domains

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic scope decision
- **Work package:** CDS-WP-002

### Decision

CDS scope is classified through six capability domains and cross-cutting
quality concerns.

This taxonomy is a scope model and does not yet define the technical
architecture, repository architecture, or implementation tooling.

### Rationale

A long-term scope spanning brand, experience, foundations, components,
channels, and governance is unmanageable as a flat list. A stable
classification makes scope reviewable, lets each area be authorized
independently, and prevents breadth from being mistaken for progress.

### Consequences

- The six domains and the cross-cutting concerns are registered in
  [Concept and Scope](../governance/CONCEPT_AND_SCOPE.md).
- Scope discussions reference domains rather than ad-hoc groupings.
- The taxonomy must not be read as an architecture; the architecture is decided
  in CDS-WP-005.
- Cross-cutting concerns are quality requirements, not conformance claims.

---

## DEC-S-008 — CDS owns shared design rules; consumers own their products

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic scope decision
- **Work package:** CDS-WP-002

### Decision

CDS owns normative shared design rules and accepted shared design artifacts.

Consumer projects retain ownership of product strategy, business logic, domain
data, runtime operations, infrastructure, and product-specific implementation
decisions outside accepted CDS contracts.

### Rationale

Without an explicit boundary, both sides assume the other owns a required
decision or obligation, and the gap is discovered late. A design foundation
that absorbs product concerns also becomes unmaintainable and product-specific.

### Consequences

- The per-area split is registered in the
  [Scope Boundary Matrix](../governance/SCOPE_BOUNDARY_MATRIX.md).
- Business logic, domain data, backend, security architecture, and operations
  are permanent non-goals for CDS.
- Shared and contract-controlled areas require explicit coordination; their
  governance is deferred to CDS-WP-006.
- Correct integration of a chosen CDS version is always the consumer's
  responsibility.
- Addresses RISK-006.

---

## DEC-S-009 — Long-term scope is not a current commitment

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic scope decision
- **Work package:** CDS-WP-002

### Decision

Inclusion in the long-term CDS scope does not create an immediate delivery,
stability, support, release, or compatibility commitment.

Availability is governed by roadmap and maturity status.

### Rationale

Registering intended scope is necessary for planning, but a registered scope
list reads as a feature promise unless the difference is stated explicitly.
Overstated availability damages credibility and drives premature adoption.

### Consequences

- Scope documents must separate long-term direction from current phase scope.
- No document may present a registered domain as available, stable, supported,
  or scheduled.
- The roadmap and maturity model that govern availability are deferred to
  CDS-WP-006.
- Addresses RISK-007.

---

## DEC-S-010 — Three consumer relationship classes

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic scope decision
- **Work package:** CDS-WP-002

### Decision

CDS recognizes three consumer relationship classes:

- Core Product Consumer,
- Associated Project Consumer,
- Potential External Consumer.

Classification does not itself grant brand endorsement, public availability,
licensing rights, or support commitments.

### Rationale

Different consumers need different degrees of adoption and brand association.
Without explicit classes, every consumer implicitly claims the strongest
relationship, and requirements from incompatible relationships collide.

### Consequences

- The classes are registered in the
  [Consumer and Stakeholder Model](../governance/CONSUMER_AND_STAKEHOLDER_MODEL.md).
- Naming a project in any class is not adoption, endorsement, or approval.
- Public availability, licensing, and support remain undecided, particularly
  for potential external consumers.
- This is a relationship model, not a brand architecture; product-family
  classes and adoption levels are deferred to CDS-WP-004 through CDS-WP-006.
- Addresses RISK-008.

---

## DEC-S-011 — Pilot results become normative only when generalized and accepted

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic scope decision
- **Work package:** CDS-WP-002

### Decision

CoreOps-specific needs may be used for pilot validation.

Only generalized and explicitly accepted results become normative CDS
artifacts. Other CoreOps-specific solutions remain owned by CoreOps.

### Rationale

The pilot must supply real requirements without silently becoming the
specification. A validation case is evidence, not a norm.

### Consequences

- CoreOps-specific solutions are CoreOps-owned by default.
- Generalization requires multi-consumer relevance or a documented rationale, a
  check against CDS principles, explicit acceptance through a CDS work package,
  and the ability to document, test, and version the result.
- The concrete pilot contract is deferred to CDS-WP-004.
- Refines the application of DEC-S-002 without changing it; addresses RISK-002.

---

## DEC-S-012 — Adoption and conformance claims require a version and evidence

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Strategic scope decision
- **Work package:** CDS-WP-002

### Decision

Future CDS adoption or conformance claims must reference a specific CDS version
and an evidence model.

The detailed conformance and adoption policy is deferred to CDS-WP-006.

### Rationale

An unqualified claim of CDS compliance is unverifiable and misleading, because
CDS is versioned and its artifacts change. A claim without evidence transfers
unearned trust to the claiming project and to CDS.

### Consequences

- No adoption or conformance claim may be made today; no version and no
  evidence model exist yet.
- Claims must name a specific CDS version once versioning exists.
- The conformance criteria, adoption levels, and evidence model are defined in
  CDS-WP-006.
- Addresses RISK-009.
