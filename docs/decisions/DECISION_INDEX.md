# Decision Index

This index records the strategic decisions of the Core Design System (CDS).

All decisions listed here define purpose, boundaries, scope, and authority.
They do **not** select tools, formats, frameworks, repository structures, or
any concrete visual or implementation technology.

Concrete implementation and visual decisions require separate, explicitly
authorized work packages.

## Register scope

- Decision range: DEC-S-001 … DEC-S-020
- Number of decisions: 20
- Decision record format: index entries only; no ADR files exist in this phase.

## Decision types

| Type | Range | Registered by | Character |
| --- | --- | --- | --- |
| Strategic foundation decision | DEC-S-001 … DEC-S-006 | CDS-WP-001 | Purpose, boundaries, and authority of the project. |
| Strategic scope decision | DEC-S-007 … DEC-S-012 | CDS-WP-002 | Scope classification, ownership, consumer relationships, and commitment limits. |
| Consumer and pilot scope decision | DEC-S-013 … DEC-S-020 | CDS-WP-004 | Evidence binding, requirement classification, pilot boundaries, and claim limits. |

None of these types is an implementation decision.

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

---

## DEC-S-013 — Consumer evidence must be bound to a committed revision

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Consumer and pilot scope decision
- **Work package:** CDS-WP-004

### Decision

Consumer requirements used by CDS must be traceable to a specific committed
source revision and classified by evidence strength.

Uncommitted consumer content is not normative evidence.

### Rationale

A requirement that cannot be traced to a committed revision cannot be verified,
re-checked, or defended later. Working-tree content is unreviewed, may be
abandoned, and is invisible to anyone else — treating it as evidence would build
CDS on sand.

### Consequences

- Consumer content is read from the committed HEAD revision, never from the
  working tree, even when a local file is available.
- A dirty consumer working tree is recorded rather than silently ignored; two of
  the three consumers were dirty at evidence time.
- Every requirement carries a traceable source and an evidence strength.
- Nothing may be reconstructed from memory or earlier sessions.
- Evidence is a dated snapshot and decays; addresses RISK-014.

---

## DEC-S-014 — Consumer requirement classification

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Consumer and pilot scope decision
- **Work package:** CDS-WP-004

### Decision

CDS consumer requirements are classified as:

- Shared CDS Candidate,
- CoreOps Pilot Requirement,
- Product-local Requirement,
- Deferred Requirement,
- Out of CDS Scope.

Classification does not itself make a requirement an accepted CDS standard.

### Rationale

Without explicit classes, every documented consumer need silently becomes a CDS
obligation. The classes separate "someone needs this" from "CDS owns this", and
keep the ownership boundary (DEC-S-008) operational rather than theoretical.

### Consequences

- Every requirement carries exactly one classification.
- `Shared CDS Candidate` records candidacy, not approval.
- Product-local requirements stay with the consumer; CDS must not absorb them
  (RISK-016).
- Permanent non-goals are registered as `Out of CDS Scope` so the boundary stays
  visible where consumer documentation is dense with them.
- Acceptance as a standard requires the path in DEC-S-016.

---

## DEC-S-015 — The initial pilot is a bounded slice

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Consumer and pilot scope decision
- **Work package:** CDS-WP-004

### Decision

The initial CoreOps pilot is a bounded representative experience slice and does
not constitute a full CoreOps redesign, full CDS adoption, or CDS conformance.

### Rationale

An unbounded pilot becomes a redesign, consumes the capacity CDS does not have,
and produces a result that proves nothing transferable. A bounded slice can
actually be finished and judged.

### Consequences

- The pilot covers Pilot Groups A–E only.
- The out-of-scope list is explicit and binding.
- Real needs discovered during the pilot are registered as deferred rather than
  absorbed (RISK-015).
- Neither existence nor completion of the pilot implies adoption or conformance
  (RISK-018).

---

## DEC-S-016 — Generalization requires explicit review and acceptance

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Consumer and pilot scope decision
- **Work package:** CDS-WP-004

### Decision

A CoreOps-specific requirement or solution becomes a Shared CDS Candidate only
after explicit generalizability review and CDS acceptance.

CoreOps origin alone is insufficient.

### Rationale

The pilot consumer produces the most evidence simply by being the pilot. Without
a gate, volume of evidence becomes authority, and CDS quietly becomes a CoreOps
design library — the exact outcome DEC-S-002 and Non-goal 11 forbid.

### Consequences

- Single-consumer requirements stay CoreOps Pilot Requirements until reviewed.
- Generalization requires multi-consumer relevance or a documented rationale, a
  check against CDS principles, explicit acceptance via a CDS work package, and
  the ability to document, test, and version the result.
- Applies with particular force to operations-shaped patterns, where the
  consumer evidence is strongest and the overfitting risk is highest.
- Refines DEC-S-011 without changing it; addresses RISK-002 and RISK-016.

---

## DEC-S-017 — Pilot outcomes are evaluated through version-bound evidence

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Consumer and pilot scope decision
- **Work package:** CDS-WP-004

### Decision

CoreOps pilot outcomes must be evaluated through version-bound requirements,
entry and exit criteria, traceability, accessibility evidence, documented
limitations, and consumer feedback.

### Rationale

An unversioned outcome cannot be reproduced or contested. Without stated entry
and exit criteria a pilot has no end, and without documented limitations a
partial result reads as a complete one.

### Consequences

- Evidence names a specific CDS version and a specific CoreOps revision.
- Entry criteria gate the start; exit criteria gate the conclusion.
- Success is recorded per requirement in categories, never as a numeric or
  overall score.
- `Not tested` must be used where a requirement was not exercised; absence of
  failure is not evidence of success.
- Accessibility evidence requires a target that does not yet exist (CDS-WP-007);
  until then no accessibility claim may be made.

---

## DEC-S-018 — Secondary consumers provide evidence, not authority

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Consumer and pilot scope decision
- **Work package:** CDS-WP-004

### Decision

SpeakCore and CastCore may provide secondary cross-product evidence.

They do not share CoreOps pilot authority and their inclusion does not imply
completed CDS adoption.

### Rationale

Secondary consumers are the only defence against CoreOps overfitting — their
value is precisely that they are *not* the pilot. Granting them pilot authority
would blur the pilot; implying adoption would misrepresent them.

### Consequences

- Secondary evidence tests whether a CoreOps need generalizes.
- Secondary consumers do not set pilot scope, priority, or exit criteria.
- Naming them implies no adoption, endorsement, or brand grant (DEC-S-010).
- Their existing product-local design decisions are respected, not overwritten.
- Their evidence is incomplete and may not represent future consumers
  (RISK-019).

---

## DEC-S-019 — Consumer need does not establish differentiation

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Consumer and pilot scope decision
- **Work package:** CDS-WP-004

### Decision

Consumer evidence may validate a need represented by HYP-001 … HYP-008 but does
not prove that the capability is unique to CDS.

Differentiation claims remain separately governed.

### Rationale

"Our consumers need this" and "we are distinctive in providing this" are
different claims resting on different evidence. Conflating them is the most
natural error available here: consumer evidence is vivid and close at hand, and
it says nothing whatsoever about what other design systems do.

### Consequences

- A `Confirmed consumer need` justifies building something, never claiming
  uniqueness.
- Differentiation remains governed by the research layer and its limitations.
- The consumer hypothesis layer is validation evidence, not a decision.
- No hypothesis becomes an accepted decision through consumer evidence.
- Addresses RISK-013.

---

## DEC-S-020 — CDS-WP-004 authorizes requirements and a contract only

- **Status:** Accepted
- **Date:** 2026-07-15
- **Type:** Consumer and pilot scope decision
- **Work package:** CDS-WP-004

### Decision

CDS-WP-004 defines requirements and a pilot contract only.

It does not authorize visual design, token creation, component implementation,
technology selection, or CoreOps implementation work.

### Rationale

Requirements work sits adjacent to design work and slides into it easily —
particularly when consumer documentation already contains concrete palettes,
type choices, and component structures. The boundary must be stated, not
assumed.

### Consequences

- No visual, token, component, or technology decision follows from this work
  package.
- Concrete values found in consumer documentation are recorded as *the existence
  of product-local decisions*, never imported into CDS.
- Scenarios describe what must be expressible and safe, never how it should look.
- The pilot contract starts no implementation; entry criteria are unmet.
- Implementation requires separate, explicitly authorized work packages.
