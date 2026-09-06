# Decision Index

This index records the strategic decisions of the Core Design System (CDS).

All decisions listed here define purpose, boundaries, scope, and authority.
They do **not** select tools, formats, frameworks, repository structures, or
any concrete visual or implementation technology.

Concrete implementation and visual decisions require separate, explicitly
authorized work packages.

## Register scope

- **Effective decision range: DEC-S-001 … DEC-S-135**
- **Number of effective decisions: 135**
- **Effectivity.** **DEC-S-128 … DEC-S-131 are effective.** The condition their
  entries stated — the Human-Maintainer exact-byte integration commit of the
  CDS-WP-020 Decision Integration Pass, following a Fresh Independent Review and
  Nova integration adjudication — occurred on 2026-08-27 at commit
  `42a568d823de3388e45af62967546f13ad67eff6`, which integrated the reviewed object.
  **DEC-S-132 … DEC-S-135 and
  [ADR-0005](ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md) are
  effective.** They were approved by the Human Maintainer on **2026-09-05** as the
  CDS Step-9 decisions on **OD-4, OD-5, OD-6A and OD-7**, prepared under that
  authorization as **`PROPOSED / AUTHORIZED FOR INTEGRATION`**, and the condition
  their entries stated — the Human-Maintainer exact integration commit of the exact
  reviewed Working Tree object, following a Fresh Independent Review and Nova
  integration adjudication — occurred on 2026-09-05 at commit
  `2cb244e889c1a6b5a278afb233995a0379b5d9ef`, which integrated the reviewed object.
  The **effective** register is therefore **DEC-S-001 … DEC-S-135 (135 decisions)**
  and the **effective** ADR range is **ADR-0001 … ADR-0005 (5 ADRs)**. **No
  decision beyond DEC-S-135 is effective and none is prepared, and no `DEC-S-136`
  and no `ADR-0006` exists.** This section is the maintained current carrier; a
  statement inside an individual decision entry is point-in-time and is not edited
  when a later event occurs. **A review PASS is not a commit, and a Nova
  recommendation is not an approval** — effectivity followed from the commit, and
  no earlier wording conferred it.
- Decision record format: index entries, plus ADR files where a decision warrants an
  Architecture Decision Record. **Effective ADR range: ADR-0001 … ADR-0005
  (5 ADRs).**
- [ADR-0001 — Machine-Readable Token Source Format](ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
  (accepted upon Human-Maintainer commit following Nova approval).
- [ADR-0002 — Deterministic JSON Serialization](ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md)
  (accepted upon Human-Maintainer commit following Nova approval).
- [ADR-0003 — Offline Token Validator Implementation Stack](ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md)
  (accepted upon Human-Maintainer commit following Nova approval).
- [ADR-0004 — Visual Token Representation and Source Identity Architecture](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md)
  (accepted upon the Human-Maintainer integration commit
  `42a568d823de3388e45af62967546f13ad67eff6` following Nova approval). It records
  the rationale for DEC-S-128, DEC-S-130 and DEC-S-131, and **DEC-S-129 is
  deliberately not an architecture dependency of it.**
- [ADR-0005 — Visual Identifier Grammar and Identity Spaces](ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md)
  (accepted upon the Human-Maintainer integration commit
  `2cb244e889c1a6b5a278afb233995a0379b5d9ef` following Nova approval). It records
  the rationale for **DEC-S-132 only**; **DEC-S-133, DEC-S-134 and DEC-S-135 are
  deliberately not architecture dependencies of it.**

## Decision types

| Type | Range | Registered by | Character |
| --- | --- | --- | --- |
| Strategic foundation decision | DEC-S-001 … DEC-S-006 | CDS-WP-001 | Purpose, boundaries, and authority of the project. |
| Strategic scope decision | DEC-S-007 … DEC-S-012 | CDS-WP-002 | Scope classification, ownership, consumer relationships, and commitment limits. |
| Consumer and pilot scope decision | DEC-S-013 … DEC-S-020 | CDS-WP-004 | Evidence binding, requirement classification, pilot boundaries, and claim limits. |
| Logical architecture decision | DEC-S-021 … DEC-S-032 | CDS-WP-005 | Layers, authority, token flow, profiles, channels, distribution, traceability, status semantics. |
| Governance, lifecycle and publication decision | DEC-S-033 … DEC-S-048 | CDS-WP-006 | Roles, conflict resolution, maturity, versioning, contribution, exceptions, claims, risk ownership, publication, licensing, release control. |
| Accessibility and inclusive design decision | DEC-S-049 … DEC-S-060 | CDS-WP-007 | Accessibility target, target-versus-claim boundary, evidence levels, responsibility split, tooling limits, source authority, inclusive design, status truth, legal boundary, channel profiles, exception limit, CR-024 resolution. |
| Operating enablement and pre-candidate decision | DEC-S-061 … DEC-S-064 | CDS-WP-009 | Foundation closure with notes, the Pre-Candidate phase, non-normativity of operating views, and critical-risk actionability before Elevated work. |
| Accessibility support baseline and evidence decision | DEC-S-065 … DEC-S-072 | CDS-WP-010 | Support baseline as a test contract not evidence, three baseline tiers, the Required Core Baseline, family-vs-execution identity, scope-triggered coverage, freshness review, immutable evidence records, and defect/regression classification. |
| Machine-readable source and token format decision | DEC-S-073 … DEC-S-082 | CDS-WP-011 | DTCG 2025.10 as external format basis, pinned-stable-only, strict JSON `.tokens.json`, CDS profile over DTCG, JSON Schema 2020-12 foundation, fail-closed references, source-set layers, versioned provenance identity, machine-validatable naming, and governed format upgrades (ADR-0001). |
| Machine-readable bootstrap and validation decision | DEC-S-083 … DEC-S-092 | CDS-WP-012 | CDS-owned schema + fixture bootstrap, `io.github.kaykaspers.cds` payload, strict-JSON manifests and resolvers, synthetic non-normative fixtures, duplicate-key prohibition, bound V1–V4 validation cases, RFC 8785 + SHA-256 digests (ADR-0002), fail-closed local references, and Experimental-not-Candidate status. |
| Offline validator implementation decision | DEC-S-093 … DEC-S-104 | CDS-WP-013 | Pinned Python/jsonschema/rfc8785 stack, the `python -m tools.cds_validator` CLI contract, the single duplicate-key loader, the local-only schema registry, separated V1–V4 states, bounded DTCG coverage, declared-graph enforcement, digest boundaries, the CDS-owned result schema, expected/actual harness semantics, executor-produced evidence, and the Candidate gate (ADR-0003). |
| Semantic status foundation decision | DEC-S-105 … DEC-S-114 | CDS-WP-014 | Five independent status axes with a fixed 25-value vocabulary and explicit `unknown`, no degraded-knowledge-as-success, no aggregate health score, explicit combination/conflict rules, language-neutral IDs with meaning-preserving localization, text-first accessible meaning, truth-preserving downstream mappings, and the gated first Candidate plan (no promotion). |
| Semantic status source and evidence decision | DEC-S-115 … DEC-S-124 | CDS-WP-015 | The `semantic/status` Experimental source set (5 axes, 25 non-visual tokens, `status.<axis>.<value>` with 1:1 vocabulary traceability), fail-closed status validation, separate meaning-preserving DE/EN terminology, immutable WP-013 baseline cases, executor-produced evidence class, the Draft-only dossier rule, identity/digest alignment, and the no-premature-consumption boundary. |
| Accessibility / maturity / channel boundary decision | DEC-S-125 | CDS-WP-016 | Channel Accessibility Profiles gate channel artifacts, not channel-independent Layer-3 semantic sources and contracts; evidence transfers in neither direction; no waiver of any accessibility requirement and no Candidate award. |
| Candidate finalization / maturity / evidence transition decision | DEC-S-126 | CDS-WP-016 | A named non-authoritative Proposed Candidate Revision, target metadata that grants nothing, revision-bound evidence that never transfers, exact-byte pre-commit evidence binding, the fixed admission-before-approval authority order, and the Promotion Commit as the actual maturity transition point. |
| Phase transition decision | DEC-S-127 | — (CDS Phase Transition Governance Package) | The phase established by DEC-S-062 completed its operating purpose; for current and future state the project phase is `Post-Candidate Foundation & Design-System Enablement`. Prospective, partial supersession of the phase designation only — no maturity, no evidence, no activation, and no authority is granted. |
| Visual token representation, evaluation authority and source identity decision | DEC-S-128 … DEC-S-131 | CDS-WP-020 (Decision Integration Pass) | One canonical `srgb` colour representation with perceptual spaces admitted as derivation only; WCAG 2.2 as the contrast evaluation authority with full-precision comparison and additional methods informational only; an explicit, minimal, closed CDS `$type` admission profile with explicit own typing; and the Source Set as the independently evaluable unit to which maturity binds, with aggregation conferring nothing (ADR-0004 for DEC-S-128, DEC-S-130, DEC-S-131). **Effective at the Human-Maintainer integration commit `42a568d823de3388e45af62967546f13ad67eff6`.** They select **no** value, create **no** identifier, and grant **no** maturity. |
| Visual identifier, scale ownership, role admission and theme sequencing decision | DEC-S-132 … DEC-S-135 | — (CDS Step-9 Decision Integration Pass) | A family-rooted visual identifier grammar with a declared `qualifier` position, the layer kept out of every token path, two separate identity spaces, and the concrete source-set root identities; per-family ownership of every ordered scale under the common ST-1 … ST-7 contract with no universal cross-family base and `SCALE TOPOLOGY ≠ SCALE VALUES`; a cross-consumer role admission rule with the concrete vocabulary left open; and the rule that no semantic role carries a default alias before CDS-WP-022 decides the theme mechanism (ADR-0005 for DEC-S-132 only). **Effective at the Human-Maintainer integration commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`.** They select **no** value, create **no** token identifier, role identifier or source set, and grant **no** maturity. |

None of these types is an implementation decision. Logical architecture decisions
define structure, responsibility, and flow — they select no technology, format,
tool, or visual design (DEC-S-032). Governance decisions define who decides and
under what conditions — they select no licence, publication state, technology, or
design. Accessibility decisions define a **target and an evidence discipline** —
they select no test tooling, no component, no colour value, and **no conformance**
(DEC-S-050).

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

---

## DEC-S-021 — Eight-layer logical architecture

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

CDS uses an eight-layer logical architecture:

1. Strategy and Governance
2. Brand and Identity
3. Foundations and Tokens
4. Components
5. Patterns and Experiences
6. Channels and Communication
7. Distribution and Enablement
8. Evidence and Quality

The layer model is logical and does not select repository topology,
implementation technology, or organizational structure.

### Rationale

The benchmark found foundations → components → patterns to be settled industry
structure — expected by consumers and therefore not a differentiator worth
inventing around. CDS adopts the convention and extends it where its own scope
demands: brand, channels, distribution, and evidence are layers because CDS's
registered scope covers them.

Layering exists to make dependency direction arguable. Without it, "the token is
like this because the component needs it" is unanswerable.

### Consequences

- Each layer has one clear responsibility and a defined dependency direction.
- Upward dependencies are prohibited; violations are architectural defects.
- The model maps to no directory, repository, package, team, or tool.
- CDS-WP-005 positions each layer; it populates none.

---

## DEC-S-022 — Authority is divided by artifact class

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

CDS authority is divided by artifact class.

Human-readable normative sources define intent, governance, meaning, and usage
constraints.

Machine-readable normative sources define approved values, relationships, and
metadata where applicable.

Generated artifacts, tool representations, examples, research, and consumer
copies are not independently normative.

### Rationale

"Where is the truth?" must have one answer per question. Splitting meaning from
values keeps intent reviewable by a human without a tool — the operational core
of DEC-S-004. The benchmark found tool coupling common, largely undocumented, and
never presented as a risk by the systems that have it; naming the classes makes
the coupling visible instead of ambient.

### Consequences

- Eight artifact classes with an explicit authority matrix.
- Only classes 1 and 2 are normative, and only through change control.
- Generated artifacts never stand against their source; manual edits are invalid.
- Research and examples cannot acquire covert authority — relevant because CDS
  already holds a large research corpus.
- Addresses RISK-004; introduces RISK-020 (human/machine source ambiguity).

---

## DEC-S-023 — Conflicts fail closed

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

Conflicts between normative sources, generated artifacts, design-tool
representations, reference implementations, and consumer artifacts must fail
closed.

No artifact gains authority merely because it was edited most recently.

### Rationale

Recency-wins is the default behavior of nearly every tool and merge strategy, and
it is silent. A system that resolves design conflicts by timestamp has no
authority model — it has a race condition.

### Consequences

- On unclear authority: stop, record the conflict, escalate; never guess.
- Never resolve by recency or convenience.
- Prefer the more conservative reading until resolved — an unverified reading
  beats a verified one.
- Failing closed is sometimes inconvenient; that is the cost of not shipping a
  contradiction.
- The detailed conflict authority is deferred to CDS-WP-006; until then Nova
  recommends and the Human Maintainer decides (DEC-S-005).

---

## DEC-S-024 — Conceptual token flow

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

The conceptual CDS token flow is:

Reference Tokens → Semantic Tokens → Component Tokens → Product Profile Overrides
→ Channel or Platform Outputs.

This decision does not select a token format, naming convention, build tool, or
design tool.

### Rationale

Semantics must sit between raw values and consumers. Without a semantic layer,
consumers bind to values and lose meaning — which forecloses theming, profiles,
and channel transformation simultaneously, and makes CR-006 impossible to keep.

The reviewed token interoperability draft identifies itself as a preview that
instructs readers not to implement it or cite it as authoritative. A flow can be
decided today; a format cannot.

### Consequences

- Five layers with a strictly downward dependency direction.
- Semantic-first: appearance-derived names in meaning-carrying positions are
  defects.
- A component binding a reference token directly is a defect — the most tempting
  and most damaging shortcut.
- Raw values in consumer projects become a reconciliation or migration topic.
- Cycles, orphans, layer violations, and illegal overrides must be
  machine-checkable later; no tool is chosen.
- Introduces RISK-021 (token and override proliferation).

---

## DEC-S-025 — Product Profiles are bounded

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

Product Profiles may modify only explicitly approved extension points.

They must not redefine shared semantics, weaken accessibility requirements, break
consumer contracts, or create an incompatible independent design system.

### Rationale

Every mature system reviewed permits product variation; **none published its
limits**. That silence is where fragmentation lives. The four prohibitions are
absolute because each, if permitted, dissolves the reason CDS exists: shared
meaning, accessibility, contracts, and one system.

### Consequences

- Extension points are named, finite, and approved. Anything unnamed is not one.
- A profile needing a prohibited change is not a profile — it is a fork, and must
  be named as one.
- Additive consumer extensions are preferred over overrides.
- Repeated overrides of the same thing indicate a core defect; fix the core.
- Which points are approved, and who approves, is deferred to CDS-WP-006.
- Addresses RISK-008; introduces RISK-027 (profile fragmentation).

---

## DEC-S-026 — Existing product-local designs are reconciled, not overwritten

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

Existing product-local design decisions are reconciled through inventory,
semantic mapping, conflict identification, classification, and controlled
migration.

CDS does not automatically overwrite, absorb, or retrospectively certify existing
consumer designs.

### Rationale

SpeakCore and CastCore already hold their own style direction, palette, and token
sets (CR-002, CR-037). CDS is arriving late, and an architecture that assumes a
blank slate would be describing a project that does not exist.

### Consequences

- An eight-step reconciliation flow, with semantic mapping as its core: the
  question is what a decision *meant*, never whether a value is right.
- Consumer-local retention is a **valid final outcome**, not a failure.
- No automatic adoption, no automatic overwrite, no retrospective conformance.
- Reusable insight still requires the DEC-S-016 gate.
- Migration must later be versioned, documented, and reversibly plannable.
- Addresses RISK-022.

---

## DEC-S-027 — Operations patterns are a domain family, not the foundation

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

Operations-oriented patterns are modeled as a potentially reusable domain pattern
family above generic foundations and components.

They do not automatically define the universal CDS foundation.

### Rationale

The consumer evidence for operations patterns is strong (HYP-003: *Confirmed
consumer need*), and its generalizability is **entirely untested**: all three
reviewed consumers are infrastructure products, so the sample cannot distinguish
"operational products need this" from "all products need this". The benchmark
could not verify it either — both evidence layers are silent on the same
question.

A domain family lets CDS serve a real need without silently redefining itself as
an operations design system.

### Consequences

- Domain families sit above the universal foundation and are adopted only by
  consumers in that domain.
- Domain requirements must not push into Layers 3 or 4 without multi-consumer
  evidence from **outside** that domain.
- Addresses RISK-002 and RISK-016; introduces RISK-023 (domain-pattern leakage).

---

## DEC-S-028 — Status semantics are separated by axis

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

CDS status architecture separates operational condition, severity, knowledge
confidence, freshness, and evidence availability.

Unknown, stale, unavailable, incomplete, or unverified information must not be
represented as healthy, successful, current, or verified.

### Rationale

This is the strongest multi-consumer evidence CDS holds: all three consumers
document graded status, and two independently require that unknown must not read
as healthy (CR-006, CR-007).

Merging condition with knowledge confidence leaves "unknown" nowhere to live, so
it becomes a false healthy — and an operator acts on a green that means *we have
no idea*. Placing the separation in the architecture rather than in a convention
is deliberate: a convention can be forgotten under deadline; a structural
separation cannot be quietly ignored.

### Consequences

- Five axes that must never merge into one opaque value.
- Colour may never be the sole meaning carrier.
- Degraded and unavailable stay distinguishable; stale is not current;
  unverified is not verified.
- No transformation may collapse the axes; no profile may distort them.
- Semantics stay consistent across channels while rendering may differ.
- The concrete taxonomy and naming are deliberately deferred.

---

## DEC-S-029 — Channels share semantics and differ in presentation

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

CDS channels share governed semantic foundations while retaining channel-specific
transformation, layout, interaction, and evidence requirements.

Multi-channel governance does not require identical rendering across channels.

### Rationale

A paginated report and an interactive dashboard have different physics. Forcing
visual identity on them produces bad artifacts in both. What must not vary is
meaning — a status that means unknown in the UI means unknown in the PDF.

The non-interactive channels are the hard case: no hover, no live update,
possibly greyscale print. A status depending on colour, interaction, or refresh
fails there — which makes the non-colour rule an architectural necessity rather
than a courtesy.

### Consequences

- Nine channel classes registered as structure, not as demand.
- Channels may transform presentation; they may not redefine meaning.
- The benchmark found no reviewed system documenting PDF, presentation, or
  diagram standards, and consumer evidence for them is weak to absent — CR-030
  has none at all. Registration is not a commitment to build.
- Introduces RISK-024 (channel divergence).

---

## DEC-S-030 — Distribution must support offline and self-hosted use

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

CDS distribution must support local and offline consumption, reproducible
transformation, version or revision pinning, and operation without mandatory
external runtime services.

This decision does not select a distribution technology or package manager.

### Rationale

This is a confirmed consumer need, not a hypothesis: offline and air-gap capable
operation is an accepted product requirement of the pilot consumer, and all three
consumers position as self-hosted (CR-031, CR-032, HYP-002).

The benchmark found no reviewed system stating an offline guarantee — self-
containable distribution is common, but committing to it is not. CDS commits
architecturally. That is a commitment, not a claim of uniqueness (DEC-S-019).

### Consequences

- No mandatory external runtime service; local assets; air-gap tolerance.
- Optional services must stay optional.
- Reproducibility makes provenance meaningful rather than merely asserted.
- Consumers pin to an identifiable revision; "latest" is not a pin.
- The architecture constrains properties, not mechanisms — any mechanism
  satisfying them is acceptable; any that does not, is not.

---

## DEC-S-031 — Artifacts remain traceable to source revisions

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

Generated artifacts, consumer integrations, adoption evidence, and migration
evidence must remain traceable to identified normative source revisions and
transformation paths.

### Rationale

An artifact whose origin cannot be established is functionally normative, because
nobody can contradict it. Traceability is what keeps a generated artifact
subordinate to its source in practice rather than only on paper.

### Consequences

- Required logical identities: source revision, transformation revision, output
  identity, consumer revision, evidence identity, deviation record, approval
  state.
- A break anywhere breaks the chain.
- Distributing an output without provenance is a defect (RISK-025).
- No metadata structure or file format is selected.
- Underpins the Adoption Evidence Contract and DEC-S-012.

---

## DEC-S-032 — The architecture is technology-independent

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Logical architecture decision
- **Work package:** CDS-WP-005

### Decision

The CDS logical architecture remains independent of final repository topology,
design-tool choice, token format, component framework, programming language,
build system, documentation platform, and package manager.

### Rationale

DEC-S-003 requires governance and architecture before concrete decisions, and
DEC-S-004 requires tool independence. An architecture that embeds a tool choice
inherits that tool's lifetime — and the benchmark showed exactly this pattern
going undocumented elsewhere.

Deciding structure now and technology later is only possible if the structure
does not smuggle a technology in.

### Consequences

- The architecture is designed to survive any reasonable technology choice.
- If a later choice cannot satisfy an architectural invariant, the **choice** is
  wrong — not the invariant.
- Deferred: repository topology, design tool, token format and naming, component
  framework, language, build system, documentation platform, package manager,
  distribution service, metadata structure, file formats, licence, publication,
  maturity model, versioning scheme, accessibility level, status taxonomy, and
  all concrete visual decisions.
- Introduces RISK-026 (architecture overdesign): structure without
  implementation evidence can outgrow the capacity that must run it.

---

## DEC-S-033 — Governance separates authority by function

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

CDS governance separates final approval, governance control, scoped execution,
consumer responsibility, contribution, and evidence review.

Creating, implementing, or frequently using an artifact does not grant normative
authority.

### Rationale

Authority acquired by proximity is the most common governance failure: whoever
built it decides what it means. Separating the functions makes authority a grant
rather than a side effect of activity.

### Consequences

- Six roles: Human Maintainer, Nova, Claude, Consumer Maintainer, Contributor,
  Evidence Reviewer.
- Review and approval are separate acts, recorded separately.
- A contributor never approves their own contribution — including Claude.
- The Evidence Reviewer may never be the artifact itself or the executor of the
  work being evidenced.
- An automated check is input to a review, never the review.
- Addresses RISK-030; concentrating final approval introduces RISK-029.

---

## DEC-S-034 — Neither normative source wins automatically

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

A conflict between human-readable and machine-readable normative sources
invalidates the affected artifact state until a controlled decision restores
consistency.

Neither source wins automatically across all conflict types.

### Rationale

Intent without approved values is unimplementable; approved values without intent
are meaningless. Neither is subordinate, so a blanket precedence rule would
discard half the truth. The honest answer is that a conflict means the state is
wrong — not that one side is.

### Consequences

- Conflict states: Consistent, Suspected, Confirmed, Under Resolution, Resolved.
- `Suspected` already blocks release and distribution — blocking precedes
  diagnosis.
- Eight-step fail-closed procedure ending in re-synchronization and renewed
  evidence.
- Prohibited: recency wins, design tool wins, generated output wins,
  implementation wins, consumer usage wins, silent overwrite, convenience,
  automatic resolution.
- Only meaning-vs-values, intra-class, and coverage-gap conflicts are true
  conflicts; stale derivatives, tool divergence, and implementation gaps have
  determinate answers already.
- Recurring conflicts signal a class-boundary violation (RISK-020).

---

## DEC-S-035 — Seven-state artifact maturity lifecycle

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

CDS artifacts use the lifecycle:

Proposed → Exploratory → Experimental → Candidate → Stable → Deprecated →
Removed.

Artifact maturity is separate from release version and publication state.

### Rationale

DEC-S-009 states that registered scope is not availability. That is only
enforceable if availability has a name, criteria, and a gate. The benchmark's most
effective observed practice was published per-component maturity.

The three axes are separated because collapsing them is the mechanism by which
"we released it" silently becomes "it is stable".

### Consequences

- Seven states with entry and exit criteria and a full transition matrix.
- A release may contain artifacts of several maturities; the release version
  never makes an artifact Stable.
- Publication state is independent: public does not mean mature, and Stable does
  not mean public.
- **No existing artifact is declared Candidate or Stable by this work package.**
  Defining a lifecycle does not populate it.
- Addresses RISK-031.

---

## DEC-S-036 — Candidate and Stable require evidence and approval

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

Candidate and Stable transitions require evidence and explicit Human-Maintainer
approval following Nova review.

Stable cannot be reached directly from Proposed, Exploratory, or Experimental.

### Rationale

Candidate is the only state where a bounded, honest failure is cheap. Skipping it
moves the discovery of a mistake to where it is expensive — after consumers
depend on it.

### Consequences

- Candidate gate: ten requirements including an evidence plan and honest open
  limitations.
- Stable gate: seven further requirements including consumer validation and
  accessibility evidence.
- No artifact promotes itself.
- Demotion is always permitted with rationale, and is a healthy act.
- **The Stable gate is currently unsatisfiable** for artifacts with accessibility
  obligations, because the accessibility target does not exist (CR-024,
  RISK-028).

---

## DEC-S-037 — Semantic versioning with an honest pre-1.0 policy

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

CDS uses MAJOR.MINOR.PATCH semantic versioning for releases.

Before v1.0.0 no blanket long-term compatibility promise exists, but breaking
changes, migration needs, revisions, and deprecations remain documented.

### Rationale

Pre-1.0 removes the compatibility *promise*. It does not remove traceability,
honesty, or migration duty — a pre-1.0 project that breaks consumers silently is
not exercising a licence, it is failing at governance it already owes.

### Consequences

- MAJOR breaks a Stable contract; MINOR adds compatibly; PATCH corrects
  compatibly.
- The version describes the released state, never an artifact's maturity.
- Pre-release states may be marked; naming a channel is not a publication
  commitment.
- The v1.x commitment begins only with an explicitly approved v1.0.0 release.
  Claude may never assert that v1.0.0 has been reached.
- No time-based cadence is invented — CDS has no evidence for what it could
  sustain.

---

## DEC-S-038 — Releases require an immutable identity

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

Every released CDS state must be identifiable through a release version and an
immutable source revision.

`latest` is not a sufficient identity for evidence, adoption, migration, or
conformance.

### Rationale

A consumer that can only say "latest" cannot make any checkable statement about
what it uses. Identity that changes underneath a consumer is not identity —
it makes every downstream claim unfalsifiable.

### Consequences

- Ten required release identity elements, including an artifact manifest, maturity
  and compatibility declarations, and an approval state.
- Consumer evidence must point to a version or immutable revision.
- Generated outputs must prove their source and transformation revision
  (DEC-S-031).
- **A rebuild must not silently reuse the same identifier with different
  content.**
- No manifest structure or format is selected.

---

## DEC-S-039 — Compatibility is declared per contract axis

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

Compatibility is declared separately for relevant CDS contract axes.

No blanket compatibility claim is valid when individual axes are unassessed,
limited, migrating, or breaking.

### Rationale

"Compatible" as a single verdict hides which part a consumer actually depends on.
A release may be compatible for documentation and breaking for tokens, and a
consumer needs to know which applies to them.

### Consequences

- Eight axes: normative documentation, machine-readable source, token, component,
  Product Profile, channel output, consumer integration, evidence.
- Six permitted statements including `Not yet assessed`.
- **An unassessed axis is never presented as compatible** — the temptation to
  round it up because nothing broke in testing is exactly RISK-032.
- Every release approval names the relevant axes.
- Consumer-local artifacts are never automatically guaranteed.

---

## DEC-S-040 — Stable artifacts require deprecation before removal

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

Stable artifacts require documented deprecation and migration treatment before
regular removal.

Regular removal of a Stable contract is a MAJOR change.

### Rationale

A Stable artifact carries a promise. Removing it without a deprecation and a
migration path breaks that promise silently, and a consumer discovers it at the
worst possible moment.

### Consequences

- Nine required deprecation fields including migration guidance and a planned
  earliest removal boundary.
- **A deprecation without a viable migration path is a removal with extra steps**
  (RISK-033). If no migration exists, the artifact is not ready to be deprecated.
- The removal boundary is a boundary, not a schedule.
- Emergency removal is narrowly bounded to security, legal, rights, or dangerous
  behavior — and defers evidence rather than waiving it.
- Removed artifacts retain historical traceability.

---

## DEC-S-041 — Contributions follow a controlled acceptance process

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

CDS contributions follow a controlled intake, evidence, review, validation,
acceptance, deferral, rejection, or consumer-local retention process.

Consumer use or popularity does not create automatic CDS acceptance.

### Rationale

The benchmark showed harvesting from real products works — but only with a gate.
Without one, volume of use becomes authority and CDS becomes whatever its loudest
consumer already built.

### Consequences

- Ten-step flow; steps 3–5 exist to reach a cheap *no*.
- Eleven required contribution inputs, including a generalizability rationale and
  rights provenance.
- Five outcomes; **`Keep Consumer-local` is a first-class success**, not a soft
  rejection.
- Prohibited: auto-merge, self-approval, urgency bypass, bundling an Elevated
  change into a Standard batch.
- **External contributions are not yet possible** — they require an approved
  publication state and a contribution licensing model, neither of which exists.
- Addresses RISK-034.

---

## DEC-S-042 — Exceptions are explicit, bounded, and expiring

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

CDS exceptions must be explicit, scoped, owned, revision-bound, risk-assessed,
reviewable, and time- or event-bounded.

Silent or permanent unmanaged exceptions are prohibited.

### Rationale

An exception without an expiry and a path is an undocumented fork wearing a
label. The expiry is what forces the decision that the exception was deferring.

### Consequences

- Thirteen required fields including impact on accessibility and status truth.
- Six statuses; `Expired` is an **uncovered deviation**, not a grandfathered
  permission.
- Exceptions never extend CDS and are never a precedent.
- **Recurring exceptions trigger a CDS gap review** — if several consumers need
  the same exception, the core is wrong.
- **Accessibility weakening is not approvable through a normal exception** — this
  holds even though the target is currently undefined.
- Status truth is not exceptable.
- Addresses RISK-035.

---

## DEC-S-043 — Product Profiles are separately governed artifacts

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

Product Profiles are separately governed, version-bound CDS artifacts.

They require approved extension points, compatibility and accessibility evidence,
anti-fragmentation review, migration information, and explicit acceptance.

### Rationale

A profile is part of CDS, not a consumer's private arrangement. Governing it as a
first-class artifact is what stops "profile" from becoming a label applied to
divergence after the fact.

### Consequences

- Twelve required elements including named extension points and an
  anti-fragmentation review.
- **A Product Profile is not retrospective legitimation of an existing consumer
  design.** Consumer-local design stays consumer-local until reconciled and
  accepted (RISK-036).
- A profile exceeding the DEC-S-025 bounds is a fork and must be named as one.
- The anti-fragmentation review asks whether the request is really a core gap,
  and whether an additive extension would serve instead.
- **No Product Profile can be approved today** — accessibility evidence is
  unobtainable (CR-024).
- Addresses RISK-027.

---

## DEC-S-044 — Claims are scope-, version-, and evidence-bound

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

CDS adoption and conformance claims must be scope-bound, version-bound,
consumer-revision-bound, evidence-backed, and explicitly approved.

A global or unqualified `CDS compliant` claim is invalid.

### Rationale

An unqualified claim is unfalsifiable while transferring real trust. That
asymmetry is the whole problem: the claim costs nothing to make and everything to
disprove.

### Consequences

- Four graded claim types: Uses CDS Artifacts · CDS-integrated · CDS-validated ·
  CDS-conformant. Each adds evidence.
- **`CDS certified` is prohibited** — no certification programme exists, so the
  word is unavailable rather than discouraged.
- Eight mandatory claim fields; a claim missing any is not a weaker claim, it is
  not a claim.
- Eight re-assessment triggers; a stale claim must be withdrawn — silence is not
  continuation.
- Pilot completion is not adoption; naming a consumer is not endorsement; a
  hypothesis is not a claim.
- **No claim is currently valid, by anyone, including CDS itself.**
- Addresses RISK-037.

---

## DEC-S-045 — Risk ownership is finalized

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

The Human Maintainer is the accountable owner for CDS project risks.

Nova is the Risk Controller.

Mitigation execution and evidence review are separately assigned roles.

### Rationale

The owner model has been provisional since CDS-WP-001 and deferred by every work
package since. Separating accountability from control matters: a controller who
could accept the risks they assess is not a control.

### Consequences

- Four roles per risk: Accountable Risk Owner (Human Maintainer), Risk Controller
  (Nova), Mitigation Executor (named per mitigation), Evidence Reviewer (Nova or
  an authorized reviewer, never the executor).
- **Only the Human Maintainer may accept or close a risk.**
- Five statuses; a `Mitigating` risk without a named executor is not mitigating.
- Acceptance requires a review trigger — acceptance without one is abandonment
  with paperwork.
- All existing risks RISK-001…RISK-028 are updated to this model; **no
  description, assessment, or status changed**, because no evidence justified it.
- Anti-ceremonial rule: **documentation is not mitigation** (RISK-040).

---

## DEC-S-046 — Five publication states with an explicit gate

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

CDS publication states are: Private Development, Controlled Preview, Public
Preview, Public Stable, Archived.

A publication-state change requires an explicit publication gate and does not
follow automatically from repository visibility or release maturity.

### Rationale

Repository visibility is a technical setting; publication is a commitment.
Conflating them means CDS could become public by a checkbox, without licence
review, provenance, or an accessibility statement (RISK-039).

### Consequences

- Fifteen-requirement publication gate including per-class licence review,
  third-party provenance, and an accessibility statement.
- **The current state is `Private Development`, and this work package does not
  change it.**
- The states are not a roadmap and commit CDS to nothing.
- **Requirements 8, 9, and 11 are currently unsatisfiable** — no licensing
  decision exists and no accessibility target exists. **No publication-state
  change is possible today.**
- Failing the gate is NO-GO, not "go with notes".
- Publication requires stating plainly what CDS does not offer.

---

## DEC-S-047 — Licensing is decided per artifact class

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

Licensing and usage rights are decided separately by artifact class.

No code, documentation, token, component, font, icon, template, example, or
brand-asset license automatically governs the other classes.

### Rationale

The benchmark found this consistently: documentation, code, fonts, icons, and
brand assets routinely sit on different terms, and brand assets are the most
restricted almost everywhere. One reviewed system licenses repository files
permissively while fonts and icons fall under a separate assets agreement.
Treating licensing as one choice is an error that fails precisely where brand
assets are involved.

### Consequences

- Ten artifact classes, each decided independently, with an eleven-field rights
  and licence matrix.
- **No licence is selected for any class**, and no `LICENSE` file is created.
- Fonts are frequently not redistributable; logos are trademarks whose purpose is
  to not be freely usable.
- **Repository presence grants nothing.**
- **Unknown or conflicting rights block publication** — absolute, fail closed.
- Only the Human Maintainer selects terms; Claude never proposes a licence.
- Addresses RISK-038.

---

## DEC-S-048 — Release control requires explicit human approval

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Governance, lifecycle and publication decision
- **Work package:** CDS-WP-006

### Decision

CDS release and change control requires immutable revision identity, maturity and
compatibility declarations, change and migration information, evidence, risk
review, licensing and publication review, and explicit Human-Maintainer approval.

No automated process may independently approve or publish a CDS release.

### Rationale

A release is the moment every other governance decision either holds or is
bypassed. Automating that moment would automate the bypass — and a green build is
evidence, not consent.

### Consequences

- Twelve release candidate requirements, including per-artifact maturity states.
- Six change classes: Editorial, Corrective, Additive, Deprecating, Breaking,
  Emergency — each with its own track, evidence, review, versioning, migration,
  and approval profile.
- Emergency changes defer evidence and ceremony, never the Human Maintainer
  decision or the eventual full evidence. "Emergency" describes the timeline, not
  the standard.
- **No automatic publication from `main`; no tag or release without a Human
  Maintainer action; Claude never creates a release or tag.**
- Unclear readiness ⇒ NO-GO.
- **No CDS release is currently possible** — licence review is unsatisfiable and
  no artifact can reach Stable.

---

## DEC-S-049 — WCAG 2.2 Level AA is the accessibility target for web-based scope

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

The CDS accessibility target for the **applicable web-based scope** is **WCAG 2.2
Level AA** (W3C Recommendation, 2024-12-12). This resolves **CR-024 at policy
level**.

Level AAA is **not** a target. Non-web channels are **not** covered by this target
(DEC-S-058).

### Rationale

CR-024 had blocked the Stable gate, Product Profile approval, the publication
gate, and a pilot entry criterion simultaneously — the single most consequential
open requirement (RISK-028). WCAG 2.2 AA is the current W3C Recommendation and
the level referenced by the regulatory environment CDS consumers operate in.

W3C itself does not recommend AAA as a general policy for entire sites. Adopting
it would be a claim CDS cannot support with an evidence capacity it does not have.

### Consequences

- A target exists for the first time. **It is a target, not conformance**
  (DEC-S-050).
- **55 applicable Level A and AA success criteria** — 31 A and 24 AA — per the
  [WCAG 2.2 AA Applicability Matrix](../governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md).
- **4.1.1 Parsing is excluded** because **WCAG 2.2 itself marks it obsolete and
  removed** — this is the standard's own status, not a CDS opt-out.
- The target takes normative effect **on the Human Maintainer's commit**.
- **No CDS artifact has been evaluated against it.** Every artifact is AE-0.
  *(Decision-time state. On 2026-08-17 the Human Maintainer admitted
  `AE1-CDS-WP016-SEMSTATUS-002` as **AE-1** for the channel-independent Semantic
  Status Layer-3 source/contract family only — see the
  [Semantic Status AE-1 Admission Record](../governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md).
  No artifact has been evaluated against the WCAG target itself; Candidate remains
  **No**; no claim exists; this Decision remains **Accepted** and unchanged.)*
- **No legal, regulatory-compliance, or certification statement is made** — see the
  [Accessibility Standard Status and Limitations](../research/ACCESSIBILITY_STANDARD_STATUS_AND_LIMITATIONS.md).

---

## DEC-S-050 — Target, evidence, validation, and claim are separate governance states

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

Accessibility **targets, implementation evidence, consumer evidence, and
conformance claims are separate governance states**. Defining a target does **not**
prove that an artifact or a consumer satisfies it.

Consequently: **no current CDS artifact has an approved WCAG 2.2 Level AA
conformance claim**, and **no WCAG 2.2 Level AA conformance has been demonstrated,
reviewed, or approved** for any consumer. Absence of evidence is **not** a pass
and is **not** a demonstrated failure — every artifact is simply **AE-0, Not
Assessed**.

*(Decision-time state. Since 2026-08-17 one bounded exception exists: admitted
source-level **AE-1** for the channel-independent Semantic Status Layer-3
source/contract family. No consumer, product, or channel has been evaluated, no
WCAG conformance has been demonstrated, and this Decision remains **Accepted** and
unchanged.)*

### Rationale

The failure mode this decision exists to prevent is the most common one in design
systems: a published policy read as an achievement. A target describes an
intention; only evidence describes reality, and CDS has produced none yet.

This mirrors the project's governing invariant — **Unverified ≠ Verified**. An
accessibility policy without evidence is precisely an unverified state, and
presenting it as either verified *or* failed would be the same category of
dishonesty the architecture was built to make structurally impossible.

### Consequences

- The **target-versus-claim boundary** is normative in every accessibility
  document, and the four states are never collapsed.
- CDS-WP-007 **promotes no artifact** and **opens no gate**.
- An accessibility statement is a **disclosure obligation, not a quality claim**.
- The honest current statement is: *nothing has been assessed* — neither passed
  nor failed.

---

## DEC-S-051 — Accessibility responsibility is shared by contract

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

Accessibility responsibility is **shared by contract**.

- **CDS owns** the accessibility requirements and reference evidence for **shared
  CDS artifacts** — foundations, component and pattern contracts, status and state
  semantics, channel-profile requirements, and known limitations.
- **Consumers own** accessible **composition**, product content, domain behavior,
  consumer-local extensions, complete processes, runtime behavior, and
  **product-scope claims**.

The graded evidence levels **AE-0 … AE-4** that record this responsibility are
defined normatively by the
[Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md);
they are a model, not a separate decision.

### Rationale

The single most consequential fact of the applicability matrix is that most
criteria cannot be satisfied by either party alone. Leaving that split implicit is
how shared responsibility becomes no responsibility: CDS assumes the consumer
composes correctly, the consumer assumes the components are already accessible, and
the gap between them is exactly where accessibility is lost.

Naming the boundary per artifact class — not per project — is what makes it
enforceable through the consumer contracts.

### Consequences

- **49 of 55 applicable criteria require action from both CDS and the consumer**
  (see DEC-S-052).
- The **Integration Contract** carries the consumer's accessibility obligation.
- CDS **certifies no consumer product** (DEC-S-026, class 7 artifacts).
- Responsibility, like evidence, is **scope- and revision-bound** and does not
  transfer between consumers or channels.

---

## DEC-S-052 — Component evidence cannot be generalized into a product claim

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

Accessibility evidence for a **component, pattern, test harness, reference
implementation, channel, or any limited scope cannot be generalized into a
product-wide conformance claim**.

It follows that **using accessible CDS artifacts does not make a consumer product
accessible** — accessible composition, complete processes, and runtime behavior
remain the consumer's (DEC-S-051). Evidence never transfers across scope, revision,
channel, or consumer.

### Rationale

This is the central false promise of design systems, and the one CDS is best
positioned to make by accident. Conforming components can be assembled into an
unusable process: a correct focus order per component says nothing about focus
order across a flow, and a perfect status token says nothing about whether the
flow using it can be completed.

CDS cannot supply composition, because composition is where the product is.

### Consequences

- **49 of 55 applicable criteria require action from both CDS and the consumer** —
  the operative fact of the pilot.
- CDS **certifies no consumer product** (DEC-S-026, class 7 artifacts).
- A consumer claim requires **AE-4** — CDS artifact evidence is insufficient for
  it, and a limited-scope result is never presented as a product-wide claim.

---

## DEC-S-053 — Automated checking alone is never sufficient

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

Automated accessibility checking is **never sufficient** as evidence for AE-2,
AE-3, AE-4, or any claim. **No test tooling is selected** (DEC-S-032).

### Rationale

Automated tools detect a minority of barriers and cannot judge meaning: whether
alternative text is *correct*, whether a focus order is *comprehensible*, whether
a status is *honest*. A clean automated run is consistent with an unusable
product, and treating it as a pass converts a tool's silence into a claim.

### Consequences

- Automated results may **support** evidence, never constitute it.
- AE-3 requires verification against a declared baseline, incl. assistive
  technology.
- **No checks have been run** — no tooling exists and none is selected.

---

## DEC-S-054 — Native semantics first; ARIA only where required; APG informative

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

CDS follows a **native-semantics-first** principle. **WAI-ARIA is used only where
required** to express semantics that native mechanisms do not adequately provide.

The **WAI-ARIA Authoring Practices Guide (APG)** is **informative guidance** and
**does not create an automatic production implementation**. APG patterns are
**class 8 research / example artifacts** — never normative, never production-ready,
never accessibility evidence. **WAI-ARIA 1.2** (W3C Recommendation) is normative
for roles, states, and properties; the APG is not.

### Rationale

ARIA layered onto incorrect structure produces worse outcomes than correct native
structure alone — it overrides the semantics the platform already gets right.
Native-first keeps the accessible name, role, and state coming from the element
rather than from a parallel declaration that can drift.

On the APG the point is decisive and in its own words: it states that its
objectives **exclude** providing a comprehensive design system or production-ready
code. Treating an APG example as a component because it carries a W3C URL is
exactly the shortcut the APG warns against — and the provenance makes the shortcut
more tempting, not less wrong.

### Consequences

- ARIA is a **fallback**, not a default; a contract prefers native semantics.
- An APG pattern is a **learning example, not an accessible component**; copying
  one produces **AE-0 code**, not evidence.
- Class 8 authority applies: the APG is never normative.

---

## DEC-S-055 — Mandatory accessibility contract areas

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

The following are **mandatory accessibility contract areas** for CDS components
and patterns:

- **keyboard operability**,
- **visible and managed focus**,
- **reduced-motion support**,
- **non-colour meaning** (colour is never the sole carrier),
- **understandable errors**,
- **accessible status communication**.

A component or pattern contract that omits any applicable area is **incomplete**,
regardless of visual quality.

### Rationale

These are the areas where composition-level accessibility most often fails and
where the contract — not the consumer — is the right place to hold the obligation.
A keyboard trap, an invisible focus ring, a colour-only status, or an error a
screen-reader user cannot recover from are defects the design system can and must
prevent at the contract, before any product composes them.

### Consequences

- Accessibility behavior is part of the **component contract** (Layer 4), not a
  later review step.
- CR-021 (keyboard and focus) and CR-022 (motion) map here with responsibility.
- A contract missing an applicable area **cannot reach Candidate**.
- The concrete thresholds and mechanisms are later design and evidence work; the
  **obligation** is fixed now.

---

## DEC-S-056 — Status axes must be distinguishable through accessible semantics

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

**Operational condition, severity, knowledge confidence, freshness, and evidence
availability** must remain **distinguishable through accessible semantics** and
**must not rely on a single sensory modality**.

The architectural status invariant thereby becomes an accessibility invariant:

> **Unknown ≠ Healthy · Stale ≠ Current · Unverified ≠ Verified — for every user,
> through every modality.**

All five axes must be perceivable **non-visually**. **Colour is never the sole
carrier** (1.4.1), on **every channel**, including print.

### Rationale

Merging condition and confidence leaves "unknown" nowhere to live; conveying it
only visually leaves it nowhere to live **for a screen-reader user**. Both are the
same failure.

An operator acting on a green that actually means *we have no idea* is the exact
harm this project's status semantics exist to prevent — and the harm does not
lessen because the operator could not see the green.

### Consequences

- 4.1.2 and 4.1.3 are where this is caught.
- The **semantic-first token principle is an accessibility mechanism**: a token
  named for appearance cannot express *unknown*.
- Pilot Group E requirement 5 carries this into the pilot.
- **The Unknown invariant is not exceptable** (DEC-S-059).

---

## DEC-S-057 — Inclusive design extends beyond WCAG conformance

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

The CDS inclusive-design policy **includes cognitive accessibility, clear content,
localization, internationalization, flexible text, error recovery, and different
levels of user experience**.

**WCAG conformance does not by itself prove that every inclusive-design need is
met.** Meeting all 55 applicable criteria is **necessary, not sufficient**.

### Rationale

WCAG is a floor with real gaps — a fully conformant interface can still be
incomprehensible under pressure. CDS consumers are operations products where the
user is often tired, interrupted, and acting on consequential information; a
technically conformant screen that misleads such a user has failed the person
while passing the standard.

### Consequences

- **69 requirements across 10 areas** in the
  [Accessibility Requirements Baseline](../governance/ACCESSIBILITY_REQUIREMENTS_BASELINE.md).
- Requirements exceeding WCAG are **CDS requirements**, not WCAG criteria, and may
  never be presented as WCAG conformance.
- **No user research exists and none is planned** (RISK-017) — inclusive design is
  asserted from documentation, not validated with people.
- CDS makes **no legal, regulatory-compliance, or certification statement** (a
  policy boundary held by the
  [Accessibility Standard Status and Limitations](../research/ACCESSIBILITY_STANDARD_STATUS_AND_LIMITATIONS.md),
  not a separate decision).

---

## DEC-S-058 — Each channel requires its own accessibility profile

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

**Six accessibility channel profiles** are registered. Each channel requires an
explicit profile before its artifacts may become Candidate or Stable.

**Non-web channels are never presented as WCAG conformant.**

### Rationale

WCAG 2.2 is written for web content. Applying web success criteria to a paginated
print artifact is a category error in some cases and undefined in others — and
asserting a web standard outside the web is a status error, not a courtesy.

### Consequences

- **Only 2 of 6 profiles have a target** (Web Product UI; Web Documentation).
  Profiles 3–6 are **undefined pending a profile**.
- **0 channels are Candidate- or Stable-eligible today.**
- No PDF, presentation, diagram, or brand accessibility standard is selected.
- Semantics stay constant across channels; presentation may differ (DEC-S-029).

---

## DEC-S-059 — Accessibility cannot be waived by an ordinary exception

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

> **Accessibility requirements for Stable or CDS-conformant scope cannot be waived
> through an ordinary exception.**

Not "requires stronger review" — **not available through that mechanism at all**.
A Product Profile **may never weaken accessibility** (invariant 10).

**Missing maintainer capacity is a planning limit, never a conformance
justification.**

### Rationale

Exceptions exist to make deviation honest and bounded. Accessibility is where that
mechanism would be abused first and most plausibly, under schedule pressure —
which is precisely when the rule must already be in place, because that is when it
will be tested.

CDS may legitimately decide it cannot afford accessibility yet. That produces a
**known limitation, no Stable, and no claim** — never a conformant artifact with
an asterisk. The honest response to insufficient capacity is a smaller scope or a
lower maturity, never a weaker standard.

### Consequences

- **Eight prohibited waivers**, including suppressing a known limitation from a
  claim and **distorting status truth**.
- Every limitation requires **affected user needs**, an **alternative**, and an
  **expiry** — a limitation without them is an undecided permanent exclusion.
- Critical limitations **block Candidate and Stable**.
- **Recurring limitations trigger an architecture or scope review.**
- **No limitation and no exception is created here** — nothing has been examined,
  which is not the same as having none.

---

## DEC-S-060 — CR-024 is resolved at policy level for the CoreOps pilot

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility and inclusive design decision
- **Work package:** CDS-WP-007

### Decision

**CR-024 is resolved at policy level: WCAG 2.2 Level AA for the declared
web-based CoreOps pilot scope.**

The pilot entry criterion **"the accessibility target and its evidence method are
decided"** becomes **`Accessibility target defined` — met by the Human-Maintainer
commit of CDS-WP-007**.

### Rationale

CR-024 was the requirement everything else waited on. Closing it at policy level
is the whole of what CDS-WP-007 was authorized to do — and the whole of what it
did.

### Consequences

- **This closes a policy gap, not an evidence gap.**
- **The pilot has not started and cannot start.** Two entry criteria remain
  structurally unmet: no artifact can reach Candidate, and the architecture awaits
  approval.
- **Pilot Group E has not passed**; its 13 minimum evidence requirements are
  defined and **none is met** — which is *not assessed*, not *failed*.
- **No WCAG 2.2 Level AA conformance has been demonstrated, reviewed, or approved
  for CoreOps.** No evaluation has occurred, so no pass or fail can be stated.
- **Claude does not declare the criterion met. The Human Maintainer's commit
  does.**

---

## DEC-S-061 — The Foundation milestone is closed with mandatory notes

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Operating enablement and pre-candidate decision
- **Work package:** CDS-WP-009

### Decision

The CDS Foundation / Pre-Design milestone is closed with mandatory notes after
completion of CDS-WP-008, Nova review, and Human-Maintainer approval.

Foundation closure does not grant Candidate, Stable, adoption, conformance,
release, or publication status.

### Rationale

The Foundation is complete, consistent, traceable, and free of blockers, and the
Human Maintainer accepted closure by committing CDS-WP-008 and initiating
CDS-WP-009. Closure must be recorded as a fact, together with an explicit statement
of the many statuses it does **not** confer, so that a closed foundation is never
misread as a released, mature, or conformant one.

### Consequences

- The [Foundation Closure Record](../governance/FOUNDATION_CLOSURE_RECORD.md) is
  normative for the fact of closure, the authority state, and the phase boundary.
- The mandatory closure notes (governance affordability, accessibility support
  baseline, risk actionability, no user research, no Candidate/Stable, no
  licence/publication, reference integrity, no automatic pilot) are carried into
  the next phase.
- Publication state remains `Private Development`; no claim is valid; no artifact
  is Candidate or Stable; the CoreOps pilot stays inactive.

---

## DEC-S-062 — The first post-Foundation phase is Pre-Candidate Operating Enablement

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Operating enablement and pre-candidate decision
- **Work package:** CDS-WP-009

### Decision

The first post-Foundation phase is Pre-Candidate Operating Enablement.

Governance operationalization, role readiness, critical-risk actionability, and
accessibility-support planning precede the first design Candidate.

### Rationale

An unaffordable or unstaffed governance model fails by being bypassed, not by being
wrong (RISK-029, RISK-040). Making the governance runnable, staffing the reviewing
roles, turning the critical risks into an instrument, and planning accessibility
support must come **before** any design Candidate, or the first Candidate would be
attempted on machinery that cannot carry it.

### Consequences

- The next phase produces operating enablement and prerequisite planning only —
  no design, token, component, tool, or product artifact.
- Candidate entry conditions are made explicit in the
  [Pre-Candidate Operating Plan](../roadmap/PRE_CANDIDATE_OPERATING_PLAN.md).
- The next authorized work package is CDS-WP-010 (Accessibility Support Baseline
  and Evidence Strategy); design work begins only on an explicit Nova prompt and
  Human-Maintainer authorization.

---

## DEC-S-063 — Operating playbooks and change dossiers are non-normative operational views

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Operating enablement and pre-candidate decision
- **Work package:** CDS-WP-009

### Decision

Operating playbooks and change dossiers are non-normative operational views.

They may reduce duplication and ceremony but may not replace normative policies,
authority boundaries, traceability, evidence, approval gates, or fail-closed
behavior.

### Rationale

Operationalizing governance is necessary for affordability, but an operational
view that acquired normative force would become a second, competing source of
truth — precisely the authority ambiguity the architecture forbids (DEC-S-022,
DEC-S-034). The operating layer must lighten ceremony without ever lightening
obligation.

### Consequences

- The [Foundation Operating Playbook](../operations/FOUNDATION_OPERATING_PLAYBOOK.md)
  and the [Standard](../operations/STANDARD_CHANGE_DOSSIER_TEMPLATE.md) and
  [Elevated](../operations/ELEVATED_CHANGE_DOSSIER_TEMPLATE.md) dossier templates
  are explicitly non-normative and reference the governing policies.
- Reducible: duplicate descriptions, repeated tables, unnecessary reports,
  repeated manual counts, identical evidence references.
- Never reducible: authority, scope, traceability, evidence, risk review, human
  approval, and fail-closed behavior. On conflict, the normative policy wins.

---

## DEC-S-064 — Critical risks affecting Elevated work must be actionable first

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Operating enablement and pre-candidate decision
- **Work package:** CDS-WP-009

### Decision

Critical risks affecting Candidate, Pilot, release, or publication work must have
an explicitly named Mitigation Executor role, review trigger, expected evidence,
and blocking effect before the affected Elevated work begins.

### Rationale

A register that records risks without driving mitigation is ceremonial (RISK-040).
Requiring the four actionability attributes before the Elevated work a risk bears
on is what turns the register from a diligence artifact into an instrument of
control, without pretending that naming an executor is itself a mitigation.

### Consequences

- The [Critical Risk Action Register](../operations/CRITICAL_RISK_ACTION_REGISTER.md)
  records the four attributes for the twelve Critical Risks; a named executor role
  authorizes no work by itself.
- On the strength of that register, RISK-040 moves `Monitored → Mitigating`; no
  risk is accepted or closed, and only the Human Maintainer may do either.
- Elevated work bearing on a critical risk that lacks the four attributes is
  blocked until they exist. Documentation is not mitigation (DEC-S-045).

---

## DEC-S-065 — The Accessibility Support Baseline defines what future evidence targets

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility support baseline and evidence decision
- **Work package:** CDS-WP-010

### Decision

The CDS Accessibility Support Baseline defines the environments against which
future evidence is planned and evaluated.

The baseline is not itself evidence, a support guarantee, or a conformance claim.

### Rationale

AE-3 and therefore Stable are unreachable without a declared support baseline
(RISK-044, FM-F-001). But a baseline is a *test contract*: naming the environments
future evidence will target says nothing about whether anything has been tested or
works. Conflating the baseline with evidence would manufacture the appearance of
accessibility from a planning document.

### Consequences

- [Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
  (A11Y-BL-001) is normative for Required/Complementary/Scope-triggered environments,
  as the declared and committed baseline under CDS-WP-010.
- Listing an environment is never a statement that CDS works in or supports it.
- Every CDS artifact remains AE-0; no support or conformance claim is valid.
  *(Decision-time state. Since 2026-08-17 the Semantic Status source/contract family
  holds admitted source-level **AE-1**, produced **without exercising any baseline
  environment**. No environment is supported, no support or conformance claim is
  valid, and this Decision remains **Accepted** and unchanged.)*

---

## DEC-S-066 — Three accessibility baseline tiers

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility support baseline and evidence decision
- **Work package:** CDS-WP-010

### Decision

CDS uses three accessibility baseline tiers:

- Required Core Baseline,
- Complementary Coverage,
- Scope-triggered Coverage.

Tier assignment is governed by declared scope, risk, consumer requirements, and
maintainer capacity.

### Rationale

A single flat "supported environments" list either over-commits a small team or
under-covers real needs. Tiering separates what must always be evidenced (small,
executable) from what becomes mandatory only when scope, a contract, a profile, or
risk requires it — keeping the obligation honest and affordable (RISK-048,
RISK-049).

### Consequences

- Tier 1 is mandatory for interactive desktop-web Candidate/Stable evidence in the
  declared scope; Tier 2 and Tier 3 are trigger-bound.
- Environment assignment is recorded in the
  [Environment and Scope Matrix](../governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md).
- Undeclared Tier-2/Tier-3 environments are not represented as supported.

---

## DEC-S-067 — The Required Core Baseline composition

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility support baseline and evidence decision
- **Work package:** CDS-WP-010

### Decision

The Required Core Baseline for interactive desktop-web Candidate evidence covers
keyboard-only operation, at least one supported desktop operating-system family,
Chromium and Firefox browser families, at least one no-cost desktop screenreader
family, at least two browser/screenreader pairings, zoom and reflow, text spacing,
forced-colors or high-contrast behavior where available, reduced motion, accessible
dynamic status communication, and DE/EN scope.

### Rationale

This is the smallest set that exercises two rendering engines and a real
screen reader on a supported OS while remaining runnable with free software, so
capacity pressure cannot force a shortcut (RISK-048, DEC-S-059). The composition is
justified by official current-support sources, not popularity (RISK-011).

### Consequences

- Required holds no more than three screen-reader/browser pairings unless
  consumer/risk evidence justifies expansion.
- No local execution availability is invented; missing capability is an Execution
  Gap (RISK-051).
- Concrete Required environments are A11Y-ENV-001 … A11Y-ENV-006.

---

## DEC-S-068 — Product-family baseline and exact evidence identity are separate

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility support baseline and evidence decision
- **Work package:** CDS-WP-010

### Decision

Product-family baseline rules and concrete evidence execution identities are
separate.

Every evidence record must bind exact operating-system, browser, renderer,
assistive-technology, artifact, consumer, CDS, language, channel, and date
information.

### Rationale

Browsers and assistive technology release rapidly (official rolling/rapid-release
cadences), so a family-level baseline must be allowed to roll while each piece of
evidence stays immutable and reproducible. Evidence that only says `current` or
`latest` is irreproducible and misleading (RISK-052).

### Consequences

- The baseline may use a rolling family policy; produced evidence is immutable and
  version-bound.
- `current` / `latest` / `supported` alone is not an evidence identity.
- The [Evidence Record](../operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md)
  binds exact versions.

---

## DEC-S-069 — Complementary and mobile coverage is scope-triggered

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility support baseline and evidence decision
- **Work package:** CDS-WP-010

### Decision

Complementary and mobile accessibility coverage becomes mandatory only when the
declared scope, Product Profile, Consumer Contract, claim, or documented risk
requires it.

Undeclared environments must not be represented as supported.

### Rationale

A small team cannot evidence every platform at once; forcing all environments into
Required would either exceed capacity or produce shallow evidence. Coverage must
follow declared scope and real triggers, and the silence about untested
environments must never read as support (RISK-049, RISK-050).

### Consequences

- Apple/WebKit, JAWS, Narrator, alternative input (Tier 2) and mobile/touch,
  further languages, enterprise environments (Tier 3) are trigger-bound.
- A consumer may declare additional environments for their evidence but may not
  narrow the CDS Required baseline for a shared artifact.

---

## DEC-S-070 — Baseline freshness is reviewed on triggers and at least six-monthly

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility support baseline and evidence decision
- **Work package:** CDS-WP-010

### Decision

Accessibility baseline freshness is reviewed before Candidate, Stable, pilot, and
claim gates and after relevant version, lifecycle, regression, scope, or
Product-Profile changes.

The baseline must also receive a review at least every six months.

### Rationale

Evidence gathered against an old combination becomes quietly false as browsers and
assistive technology change (RISK-044). A trigger-based review keeps evidence honest;
the six-month interval is a maximum gap so a quiet baseline is still revisited.

### Consequences

- Freshness states: Current, Review due, Stale, Superseded, Unknown; `Unknown`/
  `Stale` evidence is not current and passes no gate.
- The six-month rule is a maximum review gap, not blanket re-testing without cause.
- Governed by the
  [Baseline Maintenance Policy](../governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md).

---

## DEC-S-071 — Evidence is recorded through immutable, bound evidence records

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility support baseline and evidence decision
- **Work package:** CDS-WP-010

### Decision

Accessibility evidence is recorded through immutable, scope-bound, revision-bound,
environment-bound, and reviewer-identified evidence records.

Templates, plans, automated results, and single-environment passes do not create
global evidence or claims.

### Rationale

Reproducible, reviewer-identified records are what let a reviewer check evidence
rather than trust an assertion, and what stop a single green result from being read
as a global claim (RISK-052, DEC-S-044). A template is not evidence; an automated
result is input to review, not the review (DEC-S-053).

### Consequences

- The [Evidence Record Template](../operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md)
  is a non-normative operational form; a filled record is evidence only for its
  exact environment identity.
- The Evidence Reviewer is never the executor or the artifact (DEC-S-045).
- No numeric accessibility score; `Not tested` is never read as `Passed`.

---

## DEC-S-072 — Accessibility defects and regressions are classified separately

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Accessibility support baseline and evidence decision
- **Work package:** CDS-WP-010

### Decision

Accessibility defects and regressions are classified separately from risk severity
and remain traceable to requirements, environments, evidence, scope, maturity, and
claim effects.

Blocking or High regressions block Stable and claims for the affected scope.

### Rationale

Regressions defeat past evidence: an artifact can keep old evidence while no longer
holding the property (RISK-045). Classifying defects on their own scale — separate
from project risk severity — and binding them to consequences prevents barriers from
being normalized or averaged away (RISK-054).

### Consequences

- Four impact levels (Blocking, High, Medium, Low) and six defect statuses;
  `Accepted limitation` requires Human-Maintainer decision and stays visible in
  claims.
- Blocking/High regressions block Stable, pilot/consumer evidence, claims, and
  "unchanged-compatible" distribution for the affected scope.
- Governed by the
  [Defect and Regression Model](../governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md);
  no defect is registered today (AE-0).
  *(Decision-time state. Still no defect is registered. Since 2026-08-17 the Semantic
  Status source/contract family holds admitted source-level **AE-1**; recorded known
  limitations for that scope are not defects. This Decision remains **Accepted** and
  unchanged.)*

---

## DEC-S-073 — DTCG 2025.10 is the external normative format basis

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Machine-readable source and token format decision
- **Work package:** CDS-WP-011

### Decision

CDS adopts the Design Tokens Community Group Technical Reports 2025.10, including the
Format, Color, and Resolver modules where applicable, as the external normative basis
of the CDS Token Format Profile.

The reports are stable Community Group reports and are not W3C Standards.

### Rationale

DTCG 2025.10 is the first stable, implementation-ready, vendor-neutral token format
(published 2025-10-28), giving CDS interoperability without tool lock-in (DEC-S-004,
RISK-004) while keeping sources human-reviewable and offline-processable. It is a
Community Group report, not a W3C Standard, so CDS retains responsibility for its own
profile and records the status honestly.

### Consequences

- The [ADR-0001](ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) and the
  [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md) bind to
  DTCG 2025.10 (Format, Color, Resolver).
- DTCG conformance is not a CDS quality, semantic, or accessibility statement.
- No token value is created; the format is a constraint, not content.

---

## DEC-S-074 — Only pinned DTCG 2025.10 is authoritative; previews are inputs

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Machine-readable source and token format decision
- **Work package:** CDS-WP-011

### Decision

Only the pinned DTCG 2025.10 reports are authoritative for the initial CDS profile.

Preview, draft, editor, or future report versions are research inputs only until a
controlled compatibility and migration decision accepts them.

### Rationale

The DTCG preview drafts explicitly state "do not implement … do not reference as
authoritative." Pinning a stable version and treating previews as inputs prevents
unstable behavior from contaminating the normative profile (RISK-056) and keeps
upgrades controlled (RISK-055).

### Consequences

- No preview/draft feature may be implemented or documented as part of the stable
  profile.
- A later DTCG report is adopted only through a governed compatibility and migration
  decision (DEC-S-082).

---

## DEC-S-075 — Strict JSON and `.tokens.json` are the normative source form

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Machine-readable source and token format decision
- **Work package:** CDS-WP-011

### Decision

Normative CDS token source documents use strict JSON according to RFC 8259 and the
`.tokens.json` file extension.

YAML, JSONC, JSON5, tool-native formats, CSS, generated code, and platform outputs
are not normative CDS token sources.

### Rationale

Strict JSON is interoperable with DTCG tooling, human-reviewable, deterministically
parseable, and offline-validatable. Comment-bearing or non-strict encodings undermine
determinism and invite out-of-band meaning; generated forms invert the authority
model.

### Consequences

- Non-strict-JSON and generated forms may be authoring input or generated output,
  never a normative source without controlled reconciliation (DEC-S-026).
- A generated artifact is never a normative source (DEC-S-079).

---

## DEC-S-076 — The CDS profile constrains DTCG and adds metadata only via extensions

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Machine-readable source and token format decision
- **Work package:** CDS-WP-011

### Decision

The CDS Token Format Profile applies DTCG rules and adds CDS-specific constraints and
metadata only through documented, namespaced extension and validation mechanisms.

CDS must not redefine reserved DTCG semantics.

### Rationale

Adding constraints and governance metadata through DTCG `$extensions` keeps CDS
sources interoperable (a generic tool still reads them) while CDS validation enforces
what a generic tool cannot. Redefining reserved DTCG semantics would break
interoperability and hide meaning (RISK-057).

### Consequences

- CDS metadata lives only inside `$extensions` under the `io.github.kaykaspers.cds`
  namespace (ADR-0001); foreign extensions are preserved and not automatically
  normative.
- The profile may restrict and add validation gates; it may not reinterpret reserved
  `$`-properties.

---

## DEC-S-077 — JSON Schema 2020-12 is the profile-validation foundation

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Machine-readable source and token format decision
- **Work package:** CDS-WP-011

### Decision

CDS uses JSON Schema Draft 2020-12 as the structural-schema foundation for a future
CDS-owned profile validator.

A CDS schema is not an official DTCG schema and cannot alone prove DTCG, semantic,
accessibility, or governance conformance.

### Rationale

2020-12 is the current JSON Schema version and expresses the structural constraints of
the CDS profile. But structure is not semantics: a schema pass does not establish
correct meaning, accessibility, or governance (RISK-058), which remain V4 human
review.

### Consequences

- CDS-WP-011 creates no schema; the schema is a CDS-WP-012 artifact, CDS-owned.
- A schema pass is input to review, never approval (DEC-S-053 applied to format).

---

## DEC-S-078 — Token references and resolution fail closed

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Machine-readable source and token format decision
- **Work package:** CDS-WP-011

### Decision

Token and Source-Set references follow the pinned DTCG 2025.10 reference and resolver
rules.

Cycles, dangling references, type conflicts, missing source sets, invalid layer
dependencies, and unresolved overrides fail closed.

### Rationale

A reference graph that silently tolerates cycles or dangling links produces invalid or
misleading generated artifacts (RISK-059, RISK-060). Failing closed keeps a
contradiction from shipping (DEC-S-023, DEC-S-034).

### Consequences

- The [Token Reference, Resolution and Validation Model](../architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
  lists the fail-closed conditions; no automatic repair.
- Failing states block transformation and distribution until corrected at the source.

---

## DEC-S-079 — Normative source sets are layered; outputs are not normative

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Machine-readable source and token format decision
- **Work package:** CDS-WP-011

### Decision

Normative machine-readable source sets are separated into Reference, Semantic,
Component, and Product Profile layers.

Channel and platform outputs are generated artifacts and are not independently
normative.

### Rationale

The layer separation operationalizes the five-layer token flow (DEC-S-024) and the
class-1/class-2/class-3 authority split (DEC-S-022) in the machine-readable source,
keeping meaning, values, and generated forms distinct.

### Consequences

- Dependencies flow strictly downward; upward/cyclic dependencies fail closed
  (DEC-S-078).
- Product Profiles override only approved extension points (DEC-S-025); generated
  outputs carry provenance and are never hand-edited (DEC-S-031).

---

## DEC-S-080 — Sources and outputs carry versioned, non-`latest` identity

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Machine-readable source and token format decision
- **Work package:** CDS-WP-011

### Decision

Every normative Source Set and generated output must remain bound to an identified CDS
profile version, DTCG report version, immutable source revision, dependency set,
transformation revision where applicable, maturity state, approval state, and
provenance record.

`latest` is not a sufficient evidence identity.

### Rationale

An artifact whose origin cannot be established becomes functionally normative because
nobody can contradict it (RISK-025, RISK-062). Versioned, immutable identity keeps
generated artifacts subordinate to their sources and makes processing reproducible
(DEC-S-031, DEC-S-038).

### Consequences

- The [Token Metadata, Provenance and Identity Model](../architecture/TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md)
  defines required identity; a missing element fails closed.
- Deterministic serialization/canonicalization is required; the concrete mechanism
  (e.g. RFC 8785) is deferred to CDS-WP-012.

---

## DEC-S-081 — A restrictive, machine-validatable naming profile

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Machine-readable source and token format decision
- **Work package:** CDS-WP-011

### Decision

CDS uses a restrictive, machine-validatable naming and identifier profile that
prevents case-only collisions, reserved-character conflicts, empty segments, and
tool-specific shared semantics.

Technical identifiers and human-facing display labels are separate concerns.

### Rationale

Case conversion, reserved characters, and export transformations cause distinct
identifiers to collide across tools and platforms (RISK-061). A restrictive,
checkable syntax and a technical/display split keep identity stable and portable.

### Consequences

- The [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md) fixes a
  segment syntax; renames are migration events (DEC-S-082).
- No real token name is created.

---

## DEC-S-082 — Format, profile, and contract upgrades are governed

- **Status:** Accepted
- **Date:** 2026-07-16
- **Type:** Machine-readable source and token format decision
- **Work package:** CDS-WP-011

### Decision

Changes to the CDS Token Format Profile, DTCG version binding, reference model,
extension model, or validation contract require compatibility, migration, evidence,
Nova review, and explicit Human-Maintainer approval.

No format upgrade is automatic.

### Rationale

The pinned DTCG version will drift as the CG publishes (RISK-055), and a silent
upgrade could break interoperability or consumers. Governed upgrades keep the format
stable and migrations honest (DEC-S-037 … DEC-S-040 applied to the format).

### Consequences

- Adopting a later DTCG report or a preview feature is an Elevated, governed decision
  (DEC-S-074).
- The profile version, DTCG report version, and CDS release version stay distinct.

---

## DEC-S-083 — The machine-readable bootstrap is CDS-owned schemas plus synthetic fixtures

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Machine-readable bootstrap and validation decision
- **Work package:** CDS-WP-012

### Decision

The initial CDS machine-readable bootstrap consists of CDS-owned JSON Schema Draft
2020-12 contracts and synthetic validation fixtures.

Schema or fixture presence does not establish complete DTCG, semantic, accessibility,
governance, Candidate, or Stable conformance.

### Rationale

Structural schemas and fixtures make the format profile testable, but structure is not
correctness (RISK-058, RISK-064): a schema pass proves no semantic, accessibility, or
governance validity, and a synthetic fixture is not a real source. Recording the
boundary keeps the bootstrap honest.

### Consequences

- Four schemas ([token document](../../schemas/cds-token-document.schema.json),
  [manifest](../../schemas/cds-source-set-manifest.schema.json),
  [resolver](../../schemas/cds-resolver-document.schema.json),
  [validation case](../../schemas/cds-validation-case.schema.json)) and synthetic
  fixtures under `tests/fixtures/machine-readable/`.
- The bootstrap is Experimental, not Candidate (DEC-S-092).

---

## DEC-S-084 — CDS profile metadata lives under a stable extension root requiring profileVersion

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Machine-readable bootstrap and validation decision
- **Work package:** CDS-WP-012

### Decision

CDS profile metadata is carried under the stable `io.github.kaykaspers.cds` extension
root. The payload requires `profileVersion` and source-set identity metadata.

Foreign extensions must be preserved but are not automatically normative for CDS.

### Rationale

A required, versioned payload under a single stable root makes CDS metadata
machine-checkable while keeping DTCG interoperability — a generic tool ignores it, and
CDS validation enforces it (DEC-S-076). Preserving foreign extensions honours the
DTCG ecosystem without granting foreign data CDS authority.

### Consequences

- The token-document schema requires the CDS namespace with `profileVersion` at the
  document root; unknown CDS payload fields fail closed.
- An old/unknown namespace or a missing `profileVersion` fails V3 (RISK-064).

---

## DEC-S-085 — Source-Set manifests explicitly declare identity, layer, path, and graph

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Machine-readable bootstrap and validation decision
- **Work package:** CDS-WP-012

### Decision

CDS Source-Set manifests are strict JSON documents that explicitly declare source-set
identity, layer, local path, dependency graph, revisions, profile and DTCG versions,
maturity, approval, and provenance state.

Implicit or network-discovered source sets are prohibited.

### Rationale

An explicit, local, declared graph is what makes dependency direction, cross-file
references, and provenance machine-checkable and offline-resolvable (RISK-069). Implicit
or network discovery would reintroduce hidden coupling and non-reproducibility.

### Consequences

- The manifest schema requires the full identity/graph fields; the dependency graph
  must be consistent with per-entry dependencies (V3).
- Manifests use the CDS-owned `.source-set.json` extension (not a DTCG extension).

---

## DEC-S-086 — Resolver documents declare explicit, local, ordered composition

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Machine-readable bootstrap and validation decision
- **Work package:** CDS-WP-012

### Decision

CDS Resolver documents use strict JSON, DTCG-compatible resolver concepts, `$ref`,
RFC-6901 JSON Pointer, explicit ordered composition, and locally declared source sets.

Hidden network resolution is prohibited.

### Rationale

Explicit, reproducible ordering over locally declared sets makes multi-context
composition deterministic and offline (DEC-S-080), and keeps `$ref`/JSON Pointer as the
resolver reference form (ADR-0001). Automatic discovery or network resolution would break
reproducibility and tool neutrality (RISK-063).

### Consequences

- The resolver schema requires an ordered source-set list with local `$ref` (optional
  JSON Pointer) and a `localOnly` flag; resolver output is generated and non-normative.
- Resolver documents use the CDS-owned `.resolver.json` extension.

---

## DEC-S-087 — Validation fixtures are synthetic, test-only, non-normative

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Machine-readable bootstrap and validation decision
- **Work package:** CDS-WP-012

### Decision

CDS validation fixtures are synthetic, test-only, non-normative artifacts.

They must not be published, consumed, or described as real CDS design tokens or Product
Profiles.

### Rationale

Fixtures exercise the contract, not the design; treating a fixture value as a design
decision would smuggle unauthorized design into the system (RISK-065). Explicit
`testOnly`/`nonNormative` marking keeps the boundary unambiguous.

### Consequences

- Every fixture carries `testOnly: true` and `nonNormative: true`, uses `fixture/` IDs,
  and contains only neutral placeholder values.
- No fixture is marked Candidate or approved.

---

## DEC-S-088 — Duplicate JSON object member names are prohibited and fail V1

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Machine-readable bootstrap and validation decision
- **Work package:** CDS-WP-012

### Decision

Duplicate JSON object member names are prohibited in normative CDS machine-readable
sources.

Duplicate-key input fails V1 and is not repaired through first-key-wins or
last-key-wins behavior.

### Rationale

Duplicate keys are silently accepted by many parsers (last-wins), corrupting content
undetectably (RISK-068). Prohibiting them and failing V1 — rather than "repairing" —
keeps the source unambiguous; JSON Schema alone cannot detect this, so a duplicate-key-
aware parser is required.

### Consequences

- The Validation Contract V1 rejects duplicate members; the `duplicate-key` fixture
  encodes this and the future validator must detect it.
- Later layers are `Not assessed` when V1 fails.

---

## DEC-S-089 — Validation cases bind every fixture to explicit expected outcomes

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Machine-readable bootstrap and validation decision
- **Work package:** CDS-WP-012

### Decision

CDS validation cases bind every fixture to explicit expected outcomes for V1, V2, V3,
and V4.

A blocked or unexecuted validation layer remains visible and cannot be collapsed into an
aggregate score.

### Rationale

Declared per-layer expectations make a future validator's behavior checkable and keep a
partial result honest (RISK-058, RISK-071). An aggregate score would hide exactly the
layer that failed.

### Consequences

- The [validation-case matrix](../../tests/fixtures/machine-readable/VALIDATION_CASES.json)
  records expected V1–V4 per case with contiguous `VAL-CASE-###` IDs; every fixture is
  covered; no numeric score.

---

## DEC-S-090 — CDS uses RFC 8785 JCS with SHA-256 for canonical content digests

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Machine-readable bootstrap and validation decision
- **Work package:** CDS-WP-012

### Decision

CDS uses RFC 8785 JSON Canonicalization Scheme with SHA-256 for future canonical content
digests.

Canonical content digests supplement but do not replace immutable source revision,
approval, provenance, or signature evidence.

### Rationale

A specified canonicalization plus a standard hash gives reproducible content identity
across implementations, offline (RISK-067), while a digest remains an integrity aid, not
authenticity (RISK-072). See [ADR-0002](ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md).

### Consequences

- Digest representation is lowercase hex prefixed `sha256:`; authoring formatting is
  separate from canonicalization.
- No canonicalizer is implemented in CDS-WP-012; digests are `Not computed – validator
  implementation pending`.

---

## DEC-S-091 — Cross-file references are valid only through the declared local graph

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Machine-readable bootstrap and validation decision
- **Work package:** CDS-WP-012

### Decision

Cross-file token, resolver, and source-set references are valid only through the declared
local Manifest and Resolver graph.

Undeclared, network-dependent, missing, circular, or provenance-unknown references fail
closed.

### Rationale

Confining cross-file references to the declared, local, offline-resolvable graph is what
keeps resolution reproducible and prevents hidden coupling or silent corruption
(RISK-059, RISK-069). This operationalizes DEC-S-078 for the bootstrap.

### Consequences

- The schemas restrict references to local paths (no network scheme/UNC); the future
  validator fails closed on undeclared/missing/cyclic/provenance-unknown references.
- Negative fixtures encode dangling, cyclic, and undeclared-cross-file cases.

---

## DEC-S-092 — The bootstrap stays Experimental until an authorized validator executes and is reviewed

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Machine-readable bootstrap and validation decision
- **Work package:** CDS-WP-012

### Decision

The CDS schemas and fixture bootstrap remain Experimental and do not become Candidate
until an authorized offline validator executes the defined cases, the results are
independently reviewed, and Human-Maintainer approval is recorded.

### Rationale

A defined-but-unexecuted contract is not evidence; only executed, independently reviewed
results justify maturity (RISK-066, DEC-S-053, DEC-S-036). Claiming Candidate now would
be maturity inflation (RISK-031).

### Consequences

- The bootstrap is Experimental; no Candidate/Stable status is conferred; formal schema
  execution is `Not assessed` in CDS-WP-012.
- Validator execution, evidence, and review are CDS-WP-013; the Evidence Reviewer must
  not be the executor (DEC-S-045).

---

## DEC-S-093 — The offline validator stack is Python 3.11+, pinned jsonschema, and pinned rfc8785

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

The initial CDS offline token validator is implemented in Python 3.11 or later using
the standard library, the pinned `jsonschema` implementation for Draft 2020-12
execution, and the pinned `rfc8785` implementation for canonical JSON.

No runtime network access is permitted.

### Rationale

The two pinned packages implement exactly the standards CDS already decided
(JSON Schema Draft 2020-12, DEC-S-077; RFC 8785, DEC-S-090) — re-implementing either
would create untested standards code, while any broader framework would add unneeded
supply-chain surface (RISK-073). Standard-library-first keeps the validator auditable
and offline (ADR-0003).

### Consequences

- Exact pins live in [requirements-validator.lock](../../requirements-validator.lock);
  `latest` is not an identity; upgrades are governed changes.
- Installation happens only in a temporary environment outside the repository; after
  installation the validator runs fully offline (RISK-079).

---

## DEC-S-094 — The validator entry point and CLI contract

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

The validator entry point is `python -m tools.cds_validator`.

Its `version`, `validate-file`, `validate-cases`, and `digest` commands and their
documented exit-code contract form the initial operational interface.

### Consequences

- Exit codes are stable: 0 pass/match, 1 fail/mismatch, 2 blocked, 3 internal error;
  a recognized expected failure of a negative fixture is exit 0 (DEC-S-102).
- The interface is documented in the
  [Validator Usage guide](../operations/OFFLINE_TOKEN_VALIDATOR_USAGE.md); changes are
  governed (DEC-S-082, RISK-077).

---

## DEC-S-095 — Every validation path uses the duplicate-key-rejecting loader

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

Every CDS JSON validation path uses a duplicate-key-rejecting loader.

Direct parsing paths that can silently apply first-key-wins or last-key-wins behavior
are prohibited.

### Rationale

DEC-S-088 prohibits duplicate members, but a single bypassing `json.load` call would
silently re-introduce the ambiguity (RISK-068, RISK-076). Centralizing the loader makes
the prohibition testable.

### Consequences

- The single loader lives in `tools/cds_validator/json_loader.py`; unit tests and the
  duplicate-key fixture verify the rejection at V1.

---

## DEC-S-096 — Schema resolution is a committed local registry only

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

Schema resolution uses a committed local registry containing only approved CDS schema
identities and local references.

Unknown or network-dependent schema resolution fails closed.

### Consequences

- The registry contains exactly the five committed CDS schemas (token document,
  manifest, resolver, validation case, validation result), `check_schema`-verified,
  resolved via their stable `tag:` identities without HTTP (RISK-079).

---

## DEC-S-097 — Layered execution states stay separate

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

Validator execution preserves the V1, V2, V3, and V4 layers separately.

Blocked, failed, limited, and not-assessed states remain visible and are not collapsed
into an aggregate score.

### Consequences

- Machine-readable results carry four explicit layer states per case (DEC-S-089);
  the result schema contains no numeric quality score.

---

## DEC-S-098 — Initial DTCG coverage is explicitly bounded

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

The initial DTCG validator coverage is explicitly bounded to the pinned DTCG-2025.10
rules required by the CDS profile and committed fixtures.

Unsupported DTCG areas are reported as limitations and are not represented as passed.

### Rationale

A bounded, honest V2 beats a broad, unverified one (RISK-074): a fixture-scope pass is
only a pass of the declared validator scope, never full DTCG conformance.

### Consequences

- Every machine-readable report lists the unsupported areas under `limitations`;
  no full-conformance statement is ever emitted (DEC-S-044).

---

## DEC-S-099 — Manifest and resolver validation enforces the declared graph

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

Manifest and Resolver validation enforces registered identity, local paths, dependency
order, layer direction, cycle freedom, resolver order, and declared cross-file
boundaries.

Implicit discovery is prohibited.

### Consequences

- Graph checks run in `tools/cds_validator/graph.py` and the V3 layer; undeclared,
  cyclic, backward, or unregistered references fail closed (DEC-S-091, RISK-069).

---

## DEC-S-100 — Digests only from parsed content; never authenticity

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

RFC-8785/SHA-256 content digests are produced only from successfully parsed JSON and
never replace source revision, provenance, approval, signature, or authenticity
evidence.

### Consequences

- Duplicate-key or otherwise V1-invalid input receives no digest; the digest report
  records such inputs as undigestible (DEC-S-088, DEC-S-090, RISK-072).

---

## DEC-S-101 — Machine-readable results use the CDS-owned result schema

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

Machine-readable validator results use a CDS-owned result schema and bind runtime,
dependency, schema, profile, DTCG, case, source, expected-result, actual-result,
diagnostic, digest, and review-state identities.

### Consequences

- The [result schema](../../schemas/cds-validation-result.schema.json) is the fifth
  registry schema; every report is schema-validated before use; a worktree execution is
  never presented as a committed revision (RISK-080).

---

## DEC-S-102 — Harness success is expected/actual agreement, not artifact approval

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

Fixture-harness success means that actual layered outcomes match the committed expected
outcomes.

Expected failure of a negative fixture is a successful harness observation, not a
passing token artifact.

### Consequences

- Expected outcomes are never edited to make the implementation succeed; a conflict
  between implementation and committed expectations is a BLOCKED state for Nova
  (RISK-071, RISK-078).

---

## DEC-S-103 — Validator reports are Experimental, executor-produced evidence

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

Validator execution reports produced in CDS-WP-013 are Experimental, executor-produced
evidence.

They remain independently unreviewed until a separately authorized reviewer assesses
the implementation and results.

### Consequences

- Every report carries `independentReviewState: pending` and an executor-produced
  evidence class; the executor never reviews its own evidence (DEC-S-045, RISK-078).

---

## DEC-S-104 — No Candidate before harness, provenance, independent review, and approval

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Offline validator implementation decision
- **Work package:** CDS-WP-013

### Decision

Neither the validator nor the machine-readable bootstrap may become Candidate until the
full committed harness passes, dependency and execution provenance are complete, an
independent Evidence Review is recorded, Nova reviews the result, and the Human
Maintainer approves the maturity transition.

### Consequences

- A green harness alone confers nothing (RISK-081); the maturity gate remains a
  Human-Maintainer decision on top of independent review and Nova review (DEC-S-036,
  DEC-S-092).

---

## DEC-S-105 — Status semantics consist of five independent axes

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Semantic status foundation decision
- **Work package:** CDS-WP-014

### Decision

CDS status semantics consist of five independent axes:

- Operational Condition,
- Severity and Impact,
- Knowledge Confidence,
- Freshness,
- Evidence Availability.

No axis substitutes for another.

### Rationale

The architecture separates these axes because merging them destroys exactly the
information that matters most — an unknown collapsed into a health value becomes a
false green or a false alarm (DEC-S-028, CR-006/CR-007). The
[Semantic Status Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
makes the separation a concrete, named contract.

### Consequences

- Five technical axis IDs (`condition`, `severity`, `confidence`, `freshness`,
  `evidence`) become the stable semantic backbone for tokens, components, and
  channels (RISK-082 controlled).

---

## DEC-S-106 — Each axis uses the fixed initial five-value vocabulary; unknown is explicit

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Semantic status foundation decision
- **Work package:** CDS-WP-014

### Decision

Each status axis uses the fixed initial five-value vocabulary defined by the
Semantic Status Foundation Contract.

Unknown is an explicit value on every axis and is never an omitted default.

### Consequences

- Exactly 25 normative axis values ([Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md));
  vocabulary changes are governed, Elevated changes (DEC-S-082 applied).
- A missing axis is a fail-closed state, never an implicit positive.

---

## DEC-S-107 — Degraded knowledge is never represented as success

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Semantic status foundation decision
- **Work package:** CDS-WP-014

### Decision

Unknown, stale, expired, unverified, partial, or unavailable information must not
be represented as nominal, current, verified, complete, healthy, or successful.

### Rationale

This operationalizes architecture invariants 7–9 (Unknown ≠ Healthy, Stale ≠
Current, Unverified ≠ Verified) at the vocabulary level, backed by the strongest
multi-consumer evidence CDS has (CR-006, CR-007).

### Consequences

- Fail-closed conditions 3–5 of the
  [Composition Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md);
  future validator fixtures must prove the prohibition (RISK-083).

---

## DEC-S-108 — No normative aggregate health score

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Semantic status foundation decision
- **Work package:** CDS-WP-014

### Decision

CDS does not use a normative aggregate health score that hides the five status
axes.

Summaries may prioritize disclosure but must preserve material qualifiers.

### Consequences

- The disclosure priority is an attention ordering, never a semantic override;
  prohibited unqualified claims are named in the
  [Communication Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md)
  (RISK-084 controlled).

---

## DEC-S-109 — Combinations stay independent under explicit conflict rules

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Semantic status foundation decision
- **Work package:** CDS-WP-014

### Decision

Status combinations remain independently represented and are subject to explicit
conflict, rationale, evidence, and provenance rules.

Contradictory or insufficiently explained combinations fail closed.

### Consequences

- Six review-required combinations and eight fail-closed states are the mandated
  minimum ([Composition Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md));
  RISK-085 is controlled by treating unusual-but-honest combinations as
  representable with rationale.

---

## DEC-S-110 — Technical IDs are language-neutral; labels are localized separately

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Semantic status foundation decision
- **Work package:** CDS-WP-014

### Decision

Technical status identifiers are stable and language-neutral.

Human-facing labels and descriptions are localized separately and must preserve
the normative semantic meaning.

### Consequences

- DE/EN semantic parity with no contradictory translations (RISK-086); label
  length flexibility; renames are migration events (DEC-S-082).

---

## DEC-S-111 — Status meaning is textual and accessible, never single-modality

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Semantic status foundation decision
- **Work package:** CDS-WP-014

### Decision

Status meaning must be available through text and accessible semantics and must
not rely solely on color, iconography, position, shape, or motion.

### Consequences

- Non-visual perceivability of unknown/freshness/confidence (baseline 7.4)
  becomes a contract obligation on every future representation (RISK-087);
  reduced-motion never removes meaning.

---

## DEC-S-112 — Downstream artifacts preserve axis distinction and truthfulness

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Semantic status foundation decision
- **Work package:** CDS-WP-014

### Decision

Channel outputs, Component Contracts, Product Profiles, and Consumer Extensions
must preserve the semantic distinction and truthfulness of every status axis.

### Consequences

- Meaning-losing remappings fail closed (fail-closed state 8); Product Profiles
  touch approved extension points only; consumer remapping divergence is a
  registered risk (RISK-088).

---

## DEC-S-113 — The first planned Candidate is the Semantic Status Foundation

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Semantic status foundation decision
- **Work package:** CDS-WP-014

### Decision

The first planned CDS design Candidate is the Semantic Status Foundation Contract
and its future machine-readable Semantic Source Set.

The planned Candidate excludes visual values, product integration, Product
Profiles, and Stable or conformance claims.

### Consequences

- The Candidate Package, scope, and exclusions are fixed in the
  [First Semantic Status Candidate Plan](../roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md);
  scope expansion before readiness is a NO-GO trigger (RISK-089).

---

## DEC-S-114 — Candidate promotion is gated on complete evidence and approval

- **Status:** Accepted
- **Date:** 2026-07-17
- **Type:** Semantic status foundation decision
- **Work package:** CDS-WP-014

### Decision

The Semantic Status Foundation cannot become Candidate until its machine-readable
source, validation evidence, accessibility and content evidence, independent
Evidence Review, Nova review, and Human-Maintainer approval are complete.

### Consequences

- Ten cumulative prerequisites, none met or waived by CDS-WP-014; the WP-013
  harness result is executor-produced observation, never Candidate evidence
  (DEC-S-104 applied to the first design foundation).

---

## DEC-S-115 — The Semantic Status Source Set is `semantic/status` and stays Experimental

- **Status:** Accepted
- **Date:** 2026-07-18
- **Type:** Semantic status source and evidence decision
- **Work package:** CDS-WP-015

### Decision

The initial machine-readable Semantic Status Source Set has the stable source-set
identity `semantic/status` and remains Experimental.

Its implementation does not grant Candidate, Stable, consumer, or claim status.

### Consequences

- The source set lives at `tokens/semantic/status/` with manifest and resolver;
  maturity Experimental, approval Unapproved (RISK-097 controlled by DEC-S-124).

---

## DEC-S-116 — One non-visual token per authorized axis value

- **Status:** Accepted
- **Date:** 2026-07-18
- **Type:** Semantic status source and evidence decision
- **Work package:** CDS-WP-015

### Decision

The Semantic Status Source Set contains exactly one non-visual semantic token for
each authorized axis value.

The initial source contains five axis groups and twenty-five status tokens.

### Consequences

- The 25-token count is machine-enforced (CDS-V4-STATUS-COUNT); no visual role
  exists in the source (DEC-S-111 applied machine-side).

---

## DEC-S-117 — Token paths are `status.<axis>.<value>` and stay 1:1 traceable

- **Status:** Accepted
- **Date:** 2026-07-18
- **Type:** Semantic status source and evidence decision
- **Work package:** CDS-WP-015

### Decision

Semantic Status token paths use the form `status.<axis>.<value>`.

Each token value preserves the corresponding stable technical value identifier and
must remain one-to-one traceable to the human-readable Status Axis Vocabulary.

### Consequences

- Path/value agreement is machine-enforced (CDS-V4-STATUS-PATH-VALUE); the
  vocabulary/source 1:1 mapping is unit-verified; renames are migration events
  (DEC-S-082, RISK-092).

---

## DEC-S-118 — Semantic Status validation fails closed on vocabulary violations

- **Status:** Accepted
- **Date:** 2026-07-18
- **Type:** Semantic status source and evidence decision
- **Work package:** CDS-WP-015

### Decision

Semantic Status machine-readable validation fails closed when an authorized axis or
value is missing, `unknown` is absent, an unauthorized value exists, a path and
value disagree, identifiers collide by case, or aggregate or appearance-oriented
status roles are introduced.

### Consequences

- Implemented as the status-specific V4 extension with nine stable
  `CDS-V4-STATUS-*` diagnostics; the testOnly/nonNormative fixture boundary never
  disables these objective checks (resume-run V4 ordering rule).

---

## DEC-S-119 — DE/EN terminology is separate and meaning-preserving

- **Status:** Accepted
- **Date:** 2026-07-18
- **Type:** Semantic status source and evidence decision
- **Work package:** CDS-WP-015

### Decision

German and English Semantic Status terminology is maintained separately from stable
technical identifiers.

Localization must preserve normative meaning and may not strengthen, weaken, merge,
or replace a technical status value.

### Consequences

- The 25-entry [DE/EN mapping](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md)
  records per-value prohibited shortenings (`supported` never upgrades to
  „verifiziert"/„geprüft"; `unknown` never reads as neutral success) (RISK-086,
  RISK-095).

---

## DEC-S-120 — The committed WP-013 cases are immutable baseline expectations

- **Status:** Accepted
- **Date:** 2026-07-18
- **Type:** Semantic status source and evidence decision
- **Work package:** CDS-WP-015

### Decision

The committed WP-013 cases remain immutable baseline expectations.

CDS-WP-015 adds VAL-CASE-016…VAL-CASE-024 without changing
VAL-CASE-001…VAL-CASE-015.

### Consequences

- The case matrix grew append-only to 24 cases; byte-identity of the first 15 is
  verified against the committed state (RISK-071 discipline continued).

---

## DEC-S-121 — WP-015 evidence is executor-produced and independently unreviewed

- **Status:** Accepted
- **Date:** 2026-07-18
- **Type:** Semantic status source and evidence decision
- **Work package:** CDS-WP-015

### Decision

Semantic Status Source Set execution, terminology review, accessibility review,
content review, and localization review produced in CDS-WP-015 are
executor-produced evidence.

They remain independently unreviewed until an authorized Evidence Reviewer records
a separate assessment.

### Consequences

- Every WP-015 report and review carries the executor-produced class and
  `independentReviewState: pending` (DEC-S-045, RISK-078).

---

## DEC-S-122 — The Candidate Dossier stays Draft until every gate closes

- **Status:** Accepted
- **Date:** 2026-07-18
- **Type:** Semantic status source and evidence decision
- **Work package:** CDS-WP-015

### Decision

The Semantic Status Candidate Dossier remains Draft while independent evidence
review, Nova Candidate review, and Human-Maintainer approval are open.

A complete-looking dossier does not grant Candidate status.

### Consequences

- The [dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md) carries an
  explicit gate-state table; unclear readiness resolves as NO-GO (DEC-S-048,
  RISK-096).

---

## DEC-S-123 — Source set, manifest, resolver, and outputs stay identity-aligned

- **Status:** Accepted
- **Date:** 2026-07-18
- **Type:** Semantic status source and evidence decision
- **Work package:** CDS-WP-015

### Decision

Semantic Status Source Set, Manifest, Resolver, and generated validation outputs
must remain aligned by source-set identity, profile version, DTCG version,
revision, provenance, and content digest.

Identity disagreement fails closed.

### Consequences

- Enforced at V3 (manifest binding) and V4 (CDS-V4-STATUS-IDENTITY); evidence
  artifacts bind revision, worktree state, and `sha256:` digests (RISK-090).

---

## DEC-S-124 — No downstream artifact may present the Experimental source as Candidate

- **Status:** Accepted
- **Date:** 2026-07-18
- **Type:** Semantic status source and evidence decision
- **Work package:** CDS-WP-015

### Decision

No Consumer, Product Profile, component, UI, or channel implementation may
represent the Experimental Semantic Status Source Set as an approved CDS Candidate
before the explicit Candidate gate succeeds.

### Consequences

- Premature consumption is a registered risk (RISK-097); the approval-statement
  check (CDS-V4-STATUS-IDENTITY) rejects embedded Candidate/Approved claims at the
  source.

---

## DEC-S-125 — Channel accessibility profiles gate channel artifacts, not channel-independent semantic sources

- **Status:** Accepted
- **Date:** 2026-08-17
- **Type:** Accessibility / maturity / channel boundary decision
- **Work package:** CDS-WP-016
- **Human-Maintainer authorization:** 2026-08-17 (CDS-WP-016 Candidate
  Accessibility Gate Remediation), accepting the Nova resolution of GAP-B-07.

### Decision

1. **Channel Accessibility Profiles govern channel artifacts.** A Channel
   Accessibility Profile applies when an artifact **instantiates, transforms,
   renders, or communicates** CDS meaning through a named CDS channel.
2. **A channel-independent Layer-3 Semantic Source or Contract may pass its
   applicable source-level Candidate accessibility gate without being assigned
   an artificial channel.** Requiring a channel profile for an artifact that is
   not a channel representation would force a false channel declaration and
   produce an untruthful scope, which the accessibility policy forbids more
   fundamentally than it requires a profile.
3. **No source-level evidence transfers into a channel representation.**
4. **No channel evidence transfers back to the source.**
5. **Every later Channel artifact remains subject to its applicable Channel
   Accessibility Profile before Candidate or Stable** — with its own target, its
   own revision-bound evidence, and its own known limitations.
6. **This decision grants no Candidate status and waives no accessibility
   requirement.**

### Rationale

The Semantic Status Foundation is a channel-independent meaning contract: it
defines what status values mean and what every representation must preserve, and
it deliberately ships no colour, icon, component, layout, or rendered output. It
therefore has no channel, and inventing one for it would misdescribe the artifact
in a normative record. The accessibility obligations that genuinely apply to it —
textual meaning at the source, `unknown` remaining explicit, DE/EN parity,
truthful summaries, and the review-required and fail-closed rules — are all
source-level and are assessable without a channel.

The obligations that genuinely need a channel — contrast, focus visibility,
keyboard operation, assistive-technology exposure, reflow, print/greyscale
behaviour — are exactly the ones that only become assessable once a
representation exists, and they are preserved unchanged for that moment.

### Consequences

- **GAP-B-07 is clarified.** Channel-profile applicability for the Semantic
  Status Candidate is no longer ambiguous.
- Wording in the
  [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
  that over-generalized "non-interactive artifacts require a channel profile
  first" is **narrowly reconciled** — narrowed in reach, not weakened in force.
  The [Accessibility Channel Profiles](../governance/ACCESSIBILITY_CHANNEL_PROFILES.md)
  document is unchanged.
- **DEC-S-058 remains in force**: each channel still requires an explicit
  accessibility profile before *its* artifacts may become Candidate or Stable,
  and non-web channels are still never presented as WCAG-conformant.
- **DEC-S-029 remains in force**: meaning stays constant across channels; a
  channel that cannot preserve a distinction must declare the limitation rather
  than drop it silently.
- **DEC-S-052 remains in force**: evidence never transfers across artifact,
  revision, environment, channel, scope, or consumer.
- Candidate still requires the applicable **source-level** accessibility
  evidence, including AE-1; the Candidate accessibility gate is unchanged in
  substance.
- This decision creates **no new channel**, authorizes **no UI**, **no
  repository presentation**, **no PDF**, **no Product Profile**, and **no
  consumer evidence**.

### Boundary

Accepted here means accepted as a governance decision record. It awards no
maturity: Candidate remains **No**, maturity remains **Experimental**, approval
remains **Unapproved**, the admitted accessibility evidence level of every CDS
artifact remains **AE-0**, and no claim of any kind becomes valid.

*Current-state note (2026-08-17, additive — the Decision above is unchanged and
remains **Accepted**).* The `AE-0` sentence records the **effect of DEC-S-125
itself**: accepting this decision awarded no evidence and no maturity. It does not
bar evidence admitted later under the existing Evidence and Claims governance. On
2026-08-17 the Human Maintainer separately admitted `AE1-CDS-WP016-SEMSTATUS-002`
as **AE-1** for the channel-independent Semantic Status Layer-3 source/contract
family only — see the
[Semantic Status AE-1 Admission Record](../governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md).
That admission is **compatible with DEC-S-125**: channel profiles still gate channel
artifacts, a channel-independent semantic source still needs no artificial channel,
and **evidence still transfers in neither direction**. Candidate remains **No**,
maturity **Experimental**, artifact approval **Unapproved**, and no claim exists.

---

## DEC-S-126 — Proposed Candidate revisions may be evidenced before promotion through exact-byte binding

- **Status:** Accepted
- **Date:** 2026-08-18
- **Type:** Candidate finalization / maturity / evidence transition decision
- **Work package:** CDS-WP-016
- **Human-Maintainer authorization:** 2026-08-18 (CDS-WP-016 Candidate
  Finalization Governance Rework), accepting the Nova adjudication of the
  read-only Candidate Finalization Bootstrap Assessment.

### Decision

1. **A Proposed Candidate Revision is a named, non-authoritative state.** An
   explicitly identified Proposed Candidate Revision may exist as uncommitted
   working-tree or equivalent review material. It is **not** current CDS
   maturity, **not** current CDS approval, **not** a claim, **not** a release,
   **not** distributable as current CDS Source, and **not**
   consumer-authoritative.

2. **Proposed Candidate Bytes may carry target metadata.** The proposed bytes
   may contain the metadata intended for the future Candidate revision —
   including `maturityState: Candidate` and `approvalState: Approved` — **only**
   where their context makes explicit that those values are the **proposed
   future state** and **not** the current authoritative repository state.

   > **Proposed Candidate Bytes are not Candidate authority.**
   > **Target metadata is not current maturity.**

3. **The first Semantic Status Candidate source revision identity is
   reserved.** The Human Maintainer authorizes
   `semantic-status-rev-0002-candidate` as the intended identity of the future
   Proposed Candidate Revision of the `semantic/status` source set. It is
   **reserved and authorized, not created**. Until the Human-Maintainer
   exact-byte Promotion Commit occurs, the authoritative source revision remains
   **`semantic-status-rev-0001`**, and no artifact may present
   `semantic-status-rev-0002-candidate` as current.

4. **Evidence does not transfer across a source revision.** The future Candidate
   source revision requires **fresh, revision-bound AE-1 evidence**. The admitted
   `AE1-CDS-WP016-SEMSTATUS-002` is bound to `semantic-status-rev-0001` and
   **does not transfer** to it. This restates, and does not relax, evidence
   rule 2 and DEC-S-052.

5. **Pre-commit evidence is permitted only under exact-byte binding.** Fresh
   AE-1 evidence **may** be produced against an uncommitted Proposed Candidate
   Revision **if and only if** the evidence package binds the exact proposed
   bytes and identifies at minimum: source-set identity · proposed source
   revision · authoritative base repository revision · worktree /
   proposed-candidate state · exact evidenced input paths · raw-byte SHA-256
   identity · canonical RFC 8785 content digests where applicable · runner and
   tooling revision · deterministic execution identity · limitations · review
   state · admission state.

   Evidence produced in this state is an **Evidence Candidate**. It is **not
   admitted evidence** and **not maturity authority**.

6. **Exact-byte continuity may bridge pre-commit evidence across the Promotion
   Commit.** A pre-commit evidence package remains valid across the later
   Promotion Commit **only** where all of the following hold: the independently
   reviewed proposed source bytes are exact · the staged bytes are exact · the
   committed blobs are exact · the source revision is unchanged ·
   evidence-relevant inputs are unchanged · raw SHA-256 identities match ·
   canonical content digests match where applicable · the required Git blob and
   object identity checks match.

7. **Any byte drift in the evidenced source or input scope invalidates the
   bridge** and requires fresh evidence, a fresh independent review, and a fresh
   admission. **There is no "small fix" exemption.**

8. **The authority order for a future Candidate revision is fixed:**

   | # | Step |
   | --- | --- |
   | 1 | Proposed Candidate bytes prepared |
   | 2 | Fresh AE-1 evidence produced |
   | 3 | Fresh independent evidence review |
   | 4 | **Human-Maintainer AE-1 admission** |
   | 5 | Nova Candidate finalization review |
   | 6 | **Human-Maintainer Candidate approval** |
   | 7 | **Human-Maintainer exact-byte Promotion Commit** |
   | 8 | Post-commit regression and identity verification |

   AE-1 admission and Candidate approval are **separate Human-Maintainer
   decisions**, and **AE-1 admission must precede Candidate approval**.

9. **Effectivity is the Promotion Commit.** A Candidate approval reached before
   integration is recorded as **`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`** (or
   the repository-native equivalent). Before the Promotion Commit the current
   authoritative repository state remains **Candidate: No**, **Maturity:
   Experimental**, **Approval: Unapproved**. Only after a successful exact-byte
   Promotion Commit, and only when every preceding gate is satisfied, may the
   integrated source become Candidate and Approved. **The Promotion Commit is the
   actual repository maturity transition point.**

10. **Post-commit verification is mandatory.** A full post-commit regression and
    exact-byte verification is required. Where the committed source is
    byte-identical to the independently reviewed, evidence-bound Proposed
    Candidate source, that verification is **confirmation of the same evidence
    binding**: it does not by itself require another Evidence ID, another
    independent evidence review, or another AE-1 admission **solely because Git
    persisted already-reviewed exact bytes**. Where any byte differs, fresh
    evidence is mandatory.

### Rationale

Candidate promotion of the Semantic Status source requires two things at once
that, without this decision, require each other: the source bytes must declare
`Candidate`/`Approved` and a Candidate source revision, and those exact bytes
must carry fresh revision-bound AE-1 evidence — but a new source revision
invalidates the evidence admitted for the old one (DEC-S-052, trigger T-12).
Read naively, the gate can only be entered by first committing an unevidenced,
unapproved Candidate state, which is precisely the preparatory commit the
governance model forbids.

The circularity is an artifact of conflating **bytes** with **authority**. Bytes
can be prepared, digested, evidenced, and reviewed before anything is
authoritative; only integration by the Human Maintainer changes what the
repository asserts. Naming the Proposed Candidate state, binding evidence to
exact bytes, and declaring the Promotion Commit as the transition point resolves
the cycle without weakening a single gate: nothing is admitted earlier, nothing
is approved earlier, and nothing is promoted earlier.

Exact-byte continuity is deliberately narrow. It preserves an **identity**; it
never transfers an evidence result. The bytes that were reviewed and the bytes
that were committed are the same bytes, or the bridge does not exist. Requiring a
second full evidence and review cycle for a bit-identical persistence would
purchase no additional truth, and would create an incentive to skip the
pre-commit review instead.

### Consequences

- The Candidate finalization flow is unblocked **as a governance sequence only**.
  No step of it is executed by this decision.
- `semantic-status-rev-0002-candidate` becomes a reserved identity. It is not
  created, not current, and not Candidate.
- Every current-state artifact continues to describe `semantic-status-rev-0001`
  as the authoritative source revision.
- The [Candidate Approval Record Template](../operations/CANDIDATE_APPROVAL_RECORD_TEMPLATE.md)
  becomes the instrument for step 6; instantiating it is a future, separately
  authorized act.
- **RISK-098** is registered for the circularity and the metadata-
  misrepresentation exposure this decision controls.
- Trigger T-12 of the
  [Candidate Accessibility Regression Plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md)
  is **not waived**: a source-revision change still invalidates prior evidence and
  still requires a full fresh execution, review, and admission cycle.
- DEC-S-125 is unchanged; the source-versus-channel rule remains binding.
- No ADR is created. This is authority sequencing, not an architecture or
  technology selection.

### Boundary

Accepted here means accepted as a governance decision record. It awards **no**
Candidate today, **no** Stable, **no** claim, **no** conformance, **no** channel
evidence, **no** consumer evidence, **no** Product Profile, **no** CoreOps pilot,
**no** CDS-WP-017 activation, **no** visual foundation, and **no** release or
publication authority. Candidate remains **No**, maturity **Experimental**,
approval **Unapproved**, the authoritative source revision
**`semantic-status-rev-0001`**, and the only admitted accessibility evidence
remains `AE1-CDS-WP016-SEMSTATUS-002` at **AE-1** for the channel-independent
Semantic Status source/contract family; every other CDS artifact remains
**AE-0**.

---

## Post-Promotion Current-State Note — 2026-08-19

**This is a current-state note, not a Decision.** It carries no `DEC-S-`
identifier, decides nothing, and changes no accepted Decision above. Every
accepted Decision text, status, date, rationale, and consequence in this index —
DEC-S-001 through DEC-S-126 — is **unchanged**. The decision count remains
**126** and the highest identifier remains **DEC-S-126**; **no decision beyond
DEC-S-126 is created, here or anywhere else.**

The note exists because accepted Decision texts are written at their own moment
and are never rewritten. Where DEC-S-126 above states the state as it stood on
2026-08-18 — Candidate **No**, maturity **Experimental**, approval
**Unapproved**, authoritative source revision `semantic-status-rev-0001`,
admitted evidence `AE1-CDS-WP016-SEMSTATUS-002` — that text is
**correct as written for its date and is not edited**. What follows is what is
true today.

### What completed

The DEC-S-126 promotion sequence completed successfully:

| # | Step | Result |
| --- | --- | --- |
| 1 | Fresh revision-bound AE-1 evidence `AE1-CDS-WP016-SEMSTATUS-004` | Produced |
| 2 | Fresh independent evidence review (reviewer ≠ executor) | **PASS WITH NOTES** |
| 3 | Human-Maintainer evidence admission | **APPROVED / ADMITTED** |
| 4 | Nova Candidate Finalization Review | **GO WITH NOTES** (recommendation only) |
| 5 | Human-Maintainer Candidate approval | **`AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION`** |
| 6 | **Exact-byte Promotion Commit** | **`22fa0710e2b75df22e7b420c2f9d86bbe67b2777`** |

### Current state

| Item | Value |
| --- | --- |
| Semantic Status source revision | **`semantic-status-rev-0002-candidate`** |
| Maturity | **`Candidate`** |
| Approval | **`Approved`** |
| Admitted accessibility evidence in force | **`AE1-CDS-WP016-SEMSTATUS-004`** at **AE-1**, channel-independent source/contract scope only |
| `AE1-CDS-WP016-SEMSTATUS-002` | Historical `semantic-status-rev-0001` admission only |
| Stable | **No** — **Candidate is not Stable** |
| Claims | **None** |
| Conformance | **None** |
| Every other CDS artifact | **AE-0** |

### Bound Foundation documents

The five `AE1-CDS-WP016-SEMSTATUS-004`-bound normative Foundation documents —
the [Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md),
[Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md),
[Composition and Conflict Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md),
[Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md),
and [Terminology DE/EN](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md) —
**remain byte-for-byte unmodified**.

Their embedded pre-promotion lifecycle labels are **historical for the current
maturity state** under the scoped Human-Maintainer resolution of 2026-08-19. Their
semantic content remains **normative and unchanged**.

**No general source-precedence rule is created.** This note does not say that
recency wins, does not say that machine-readable sources override human-readable
meaning, and does not alter DEC-S-022, DEC-S-023, or DEC-S-034. A conflict is
still never resolved by recency or by convenience. See the
[Candidate Promotion Effectivity Record](../governance/SEMANTIC_STATUS_CANDIDATE_PROMOTION_EFFECTIVITY_RECORD.md).

---

## DEC-S-127 — The current project phase is Post-Candidate Foundation & Design-System Enablement

- **Status:** Accepted — **effective at the Human-Maintainer integration commit**
  of the phase-transition package (see *Effectivity* below). Until that commit this
  entry is uncommitted executor output and changes **no** authoritative phase state.
- **Date:** 2026-08-26
- **Type:** Phase transition decision
- **Work package:** None. Registered by the **CDS Phase Transition Governance
  Package**, a bounded governance package executed after CDS-WP-019 closure and
  before any CDS-WP-020 authorization. **It is not a numbered work package** and
  does not occupy an identifier in the CDS-WP-020 … CDS-WP-053 planning sequence.
- **Human-Maintainer authorization:** 2026-08-26 (CDS Phase Transition Governance
  Package), following the Nova adjudication that a superseding Decision is required
  before CDS-WP-020 may be authorized.

### Decision

1. **The phase established by DEC-S-062 has completed its intended operating
   purpose.** Governance operationalization, role readiness, critical-risk
   actionability, and accessibility-support planning — the four prerequisites
   DEC-S-062 placed before the first design Candidate — are established and
   committed, and the first Candidate transition completed on 2026-08-19.

2. **For current and future project state the authoritative project phase is
   `Post-Candidate Foundation & Design-System Enablement`.** This label replaces
   `Pre-Candidate Operating Enablement` in every carrier that states the
   **maintained current phase**.

3. **DEC-S-062 is not deleted, withdrawn, or retroactively invalidated.** Its
   text, status, date, rationale, and consequences are **unchanged**, and it
   remains the correct phase authority for the period it governed
   (2026-07-16 … the effectivity of this decision). DEC-S-127 supersedes it
   **only** for **current and future** phase designation. This is a
   **prospective, partial supersession of the phase-designation effect**, not a
   replacement of the decision record.

4. **Historical carriers remain correct for their date and are not rewritten.**
   Dated records — the [Foundation Closure Record](../governance/FOUNDATION_CLOSURE_RECORD.md),
   the historical CDS-WP-009 [Pre-Candidate Operating Plan](../roadmap/PRE_CANDIDATE_OPERATING_PLAN.md),
   prior review reports, prior work-package notes, prior closure and evidence
   records, and historical changelog entries — continue to name
   `Pre-Candidate Operating Enablement` and are **correct as written**.
   **Historical state is not current state**, and a stale-looking phase label
   inside a dated record is not drift.

5. **Phase is not maturity.** A phase names an **operating period**, not an
   artifact state. Entering this phase awards **no** maturity to anything.

6. **Nothing is promoted.** No artifact becomes Candidate, and no artifact
   becomes Stable, because of this decision. **Stable remains `No` across the
   entire repository.**

7. **Semantic Status is unchanged.** The `semantic/status` family remains at
   source revision **`semantic-status-rev-0002-candidate`**, maturity
   **`Candidate`**, approval **`Approved`**, **Candidate YES** — for the
   channel-independent Layer-3 Semantic Source / Contract family **only**. The
   admitted evidence in force remains **`AE1-CDS-WP016-SEMSTATUS-004`** at
   **AE-1**, source/contract scope only.

8. **The nine visual foundation families remain `Proposed`.** VF-1 … VF-9 gain
   no maturity, no evidence, and no values. **There are zero Candidate visual
   families.**

9. **Evidence does not transfer because of a phase change.** A phase transition
   is not an evidence event. It admits no evidence, produces no evidence,
   revalidates no evidence, and extends no admission to any other artifact,
   channel, consumer, or source revision. Every artifact remains **AE-0** apart
   from the single admitted AE-1 source/contract scope above.

10. **The Artifact Maturity Lifecycle remains authoritative.** This decision
    changes no maturity state, no gate, no promotion rule, and no evidence
    requirement in the
    [Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md).
    DEC-S-125 and DEC-S-126 remain binding and unmodified.

11. **CDS-WP-020 is not activated and not authorized.** It remains
    `Planned / not active / not authorized`, as do CDS-WP-021 … CDS-WP-053.
    This decision is a **prerequisite** for a possible CDS-WP-020 authorization,
    never the authorization itself.

12. **Every future work package remains separately authorization-gated.**
    Entering this phase authorizes no specific work package. Each begins only on
    an explicit Nova prompt and Human-Maintainer authorization, one at a time.
    **A roadmap is not an authorization.**

13. **No visual value is created.** No colour, typeface, size, spacing, radius,
    stroke, shadow, opacity value, icon, illustration, motion value, breakpoint,
    or theme instance is selected — and no token source file, schema, validator
    rule, or component is created.

14. **No Product Profile, consumer, or pilot is activated.** No Product Profile
    is authorized or approved, no consumer integration begins, and the CoreOps
    pilot stays inactive. The named extension-point set remains **empty**.

15. **No publication or release authority is created.** Publication remains
    **`Private Development`**; no release, tag, licence, claim, or conformance
    statement exists or becomes possible through this decision.

16. **No capability is registered.** Audio and sonic design, haptics, multimodal
    feedback, and AI/agent interaction design remain registered in **none** of the
    six capability domains and in **no** channel model. F-017-03 remains a future
    **Elevated** scope / capability-registration gate.

### Phase definition

**`Post-Candidate Foundation & Design-System Enablement`** covers the period in
which CDS develops and validates the shared design-system foundation **after the
first Candidate artifact family exists**, and before any Stable, release, or
adoption state.

The phase **admits** work of these classes — it does not schedule or authorize
any of them:

- concrete Visual Foundation development and visual value selection;
- visual token architecture implementation and the concrete token vocabulary;
- semantic-to-visual binding, under its own gates;
- validation of visual foundations;
- controlled foundation maturity progression;
- component and pattern preparation;
- theme and Product Profile **architecture** progression;
- channel preservation work;
- accessibility evidence preparation.

**The phase authorizes no specific work package by itself.** Naming a work class
here creates neither scope nor permission; scope still comes from the
[Scope Boundary Matrix](../governance/SCOPE_BOUNDARY_MATRIX.md) and permission
still comes from an explicit Human-Maintainer authorization.

### What this phase is not

The phase is explicitly **not** any of the following, and entering it moves CDS
toward none of them automatically:

| Not | State |
| --- | --- |
| Stable | No artifact is Stable; **Candidate is not Stable** |
| Release | No release exists; no tag exists |
| Publication | Remains **`Private Development`** |
| Production rollout | None |
| Consumer adoption | None; naming a consumer is not endorsement |
| Product Profile activation | Zero active; **no Product Profile can currently be approved** |
| Full component maturity | No component exists |
| Ecosystem-wide deployment | None |
| Conformance or claim | **No claim of any type is valid, by anyone, including CDS itself** |

**No successor phase is named.** Naming the phase that follows this one would
require its own Decision, and that decision is **deferred**.

### Effectivity

**The new phase begins only at the Human-Maintainer integration commit** of the
phase-transition package. Before that commit:

- the authoritative phase remains `Pre-Candidate Operating Enablement` (DEC-S-062);
- uncommitted executor output changes no authoritative phase state;
- a review PASS is not a commit, and a Nova recommendation is not an approval.

This mirrors the effectivity rule already in force for maturity transitions
(DEC-S-126, clause 9): **the commit is the transition point**, not the drafting,
not the review, and not the recommendation.

### Rationale

DEC-S-062 was written on 2026-07-16 to place four prerequisites **before** the
first design Candidate, and its consequences state that the phase produces
operating enablement and prerequisite planning only — no design, token, component,
tool, or product artifact. That description has been outgrown by committed
reality: ADR-0001 selected a machine-readable source format, `tools/cds_validator`
was implemented and executed, the `semantic/status` source set exists, and on
2026-08-19 one artifact family was promoted to **Candidate**. The label survived
this because it names an *operating phase, not a maturity state* — a reading
recorded explicitly rather than assumed.

That reading stops being sufficient at CDS-WP-020. CDS-WP-019 remained compatible
with the old phase because **architecture is not visual value**: it defined how
visual foundations are structured, governed, represented, extended, validated, and
consumed, and selected no palette, typeface, spacing scale, radius scale,
elevation model, icon library, motion value, token source, or Product Profile.
CDS-WP-020 is the first work package that would create **real** visual values, and
a phase whose own operating description says that no design value is selected
cannot honestly govern that work.

Continuing under the old label would resolve the tension the way the architecture
forbids — by convenience, and by letting a stale label acquire meaning through
drift rather than through decision. The conservative correction is to decide the
phase explicitly, prospectively, and without granting anything: a new label, no
new maturity, no new authority, and no activation.

### Consequences

- Carriers that state the **maintained current phase** read
  `Post-Candidate Foundation & Design-System Enablement` from this decision's
  effectivity: [README](../../README.md), [CLAUDE.md](../../CLAUDE.md),
  [Project Profile](../../project-system/PROJECT_PROFILE.md),
  [Next Phase](../../project-system/NEXT_PHASE.md),
  [Work Packages](../../project-system/WORK_PACKAGES.md),
  [Foundation Context Pack](../../project-system/CONTEXT_PACK_FOUNDATION.md),
  [Project Brain](../../project-brain/PROJECT_BRAIN.md), the
  [Risk Register](../risks/RISK_REGISTER.md) scope header, and the
  [Post-Candidate Development Roadmap](../roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md).
- **F-017-04** — its **phase-label governance portion is closed by this decision**.
  The dependent-document hygiene CDS-WP-018 already repaired stays closed, and its
  dated historical references stay historical.
- **F-019-08 (`PHASE_TRANSITION_RECOMMENDED`)** is **closed and satisfied** by this
  decision together with the accompanying carrier reconciliation.
- **No risk is registered, accepted, or closed.** A governance-state transition
  that grants no authority and changes no artifact creates no new technical
  exposure; the register stays at **RISK-098**.
- **No ADR is created.** This is phase designation, not an architecture or
  technology selection. The register stays at **ADR-0003**.
- The dated *Post-Promotion Current-State Note — 2026-08-19* above records a
  decision count of **126** and states that no decision beyond DEC-S-126 was
  created. That statement is **correct for its date** and is **not edited**. From
  this decision's effectivity the register holds **127** decisions with highest
  identifier **DEC-S-127**; the *Register scope* section at the head of this index
  is the maintained current carrier.
- **DEC-S-062 keeps `Status: Accepted`.** The register's `Superseded` status means
  a decision replaced in full; this supersession is **prospective and partial**,
  reaching only the current-state phase designation. Marking DEC-S-062
  `Superseded` would overstate it and would edit a decision record this package is
  required to leave unchanged.

### Boundary

Accepted here means accepted as a governance decision record, effective at the
Human-Maintainer integration commit. It awards **no** maturity, **no** Candidate,
**no** Stable, **no** evidence, **no** admission, **no** claim, **no**
conformance, **no** capability registration, **no** Product Profile, **no**
consumer activation, **no** pilot, **no** licence, **no** release, **no** tag, and
**no** publication authority. It activates **no** work package — **CDS-WP-020
remains `Planned`, not active, and not authorized**. Semantic Status stays exactly
as admitted; VF-1 … VF-9 stay `Proposed`; publication stays
**`Private Development`**.

---

## DEC-S-128 — CDS authors visual colour in exactly one canonical sRGB representation

- **Status:** Accepted — **effective at the Human-Maintainer exact-byte integration
  commit `42a568d823de3388e45af62967546f13ad67eff6`** of the CDS-WP-020 Decision
  Integration Pass, which followed a Fresh Independent Review and Nova integration
  adjudication. Before that commit this entry was uncommitted executor output
  prepared under an explicit Human-Maintainer authorization and changed **no**
  authoritative CDS state; no earlier wording conferred effectivity.
- **Date:** 2026-08-27
- **Type:** Visual token representation, evaluation authority and source identity
  decision
- **Work package:** CDS-WP-020 — Reference and Semantic Token Foundation (Decision
  Integration Pass)
- **Human-Maintainer authorization:** 2026-08-27, following the Nova adjudication of
  **OD-1** of the
  [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
  register
- **Architecture record:** [ADR-0004](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md)

### Decision

1. **Exactly one canonical normative CDS visual colour space exists:** the DTCG
   2025.10 Color Module colour space identified by the `colorSpace` key **`srgb`**.
   A normative CDS visual colour source value is authored in that representation and
   in no other.

2. **OKLCH may be used as the preferred derivation and design-analysis space.**
   Computing a tonal step, a lightness relationship, or a candidate scale
   perceptually is admissible and encouraged where it produces a better-reasoned
   result.

3. **OKLCH is explicitly none of the following:** a normative source space; a second
   canonical representation; authority for a value; or an evidence carrier. A
   perceptual computation is a calculation, and a calculation demonstrates nothing
   about perceivability (DEC-S-053, EV-4).

4. **The result of an OKLCH or other perceptual derivation is recorded as the
   canonical sRGB source value**, with the derivation method and inputs recorded as
   **provenance** where a record is required. The provenance record is
   non-authoritative and never stands against the canonical value (DEC-S-022,
   DEC-S-031).

5. **Canonical component representation and range follow the pinned DTCG 2025.10
   Color Module as defined** — the sRGB components in that report's order and
   numeric range. **No 8-bit-only, integer-only, or `n/255` restriction is
   introduced**, and none may be inferred from this decision.

6. **Delivery quantization belongs to the channel and generated-output boundary.**
   A channel or platform output may quantize, encode, or round for delivery; it
   **must not** rewrite, replace, or be read back into a canonical source value
   (DEC-S-029, DEC-S-079).

7. **A normative source value outside the admitted canonical model fails closed.**
   It is not repaired, coerced, normalized, or accepted with a warning
   (DEC-S-023, DEC-S-078).

8. **A colour-space transformation is a generated, class-3 output** and does not
   mutate normative source identity. The source revision, digest, and identity of
   the source are unaffected by any transformation performed downstream.

9. **A transformation remains subject to the existing boundary, alias and
   provenance rules** (TB rules of the channel mapping, AL-1 … AL-8, DEC-S-031). It
   may not introduce a decision absent from the source, and it may not discard,
   weaken, or silently erase a declared contrast obligation or pairing.

10. **`alpha` remains part of the colour value where the pinned report admits it.**
    It is a property of the colour value, not a separate construct.

11. **No standalone opacity family is introduced.** Opacity stays what the visual
    foundation architecture already positions it as: an attribute of **VF-1**
    (alpha within a colour value) and **VF-6** (overlay and scrim). An opacity
    change is a colour change or a surface change and inherits that family's
    obligations.

12. **Translucency creates no accessibility exception.** A translucent value used by
    a contrast-sensitive role still resolves to a **pair**, and a pairing outside a
    role's declared pairing set is **undefined and fails closed** (Colour
    Architecture pairing rule 2; SR-3, SR-4). This clause adds no obligation; it
    records that `alpha` removes none.

13. **HEX disposition — no new authority and no new prohibition.** The pinned DTCG
    2025.10 Color Module permits an optional `hex` member in a colour value, and the
    [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md) already
    admits the Color Module structure **as defined**. This decision therefore
    **creates no normative hex authority** and **creates no new hard prohibition**.
    What it does state is the boundary: **`hex` may never become a second source of
    truth for a CDS colour value.** The CDS-specific question of whether `hex` is
    admitted, required, or prohibited in a normative CDS visual source **remains
    deferred**, recorded as a residual open item under **OD-1**.

14. **No colour value is selected.** No palette, no hue, no scale, no tonal step, no
    light or dark instance, no high-contrast instance, no brand colour, and no
    product colour is created, adopted, reserved, or recommended.

15. **No identifier is created.** This decision names no token, no group, and no
    source set.

### External authority verification

The colour-space key and the component model were verified **directly against the
final published reports**, not inferred from CDS tooling:

| Verified item | Literal | Source |
| --- | --- | --- |
| sRGB `colorSpace` key | `srgb` | Design Tokens **Color Module 2025.10**, Final Community Group Report, 28 October 2025 |
| sRGB components and range | Red, Green, Blue, each in the range 0 – 1 | Design Tokens **Color Module 2025.10**, Final Community Group Report, 28 October 2025 |
| Optional `hex` member | Optional string fallback in 6-digit CSS hex notation | Design Tokens **Color Module 2025.10**, Final Community Group Report, 28 October 2025 |
| Optional `alpha` member | Optional number in the range 0 – 1; assumed fully opaque when omitted | Design Tokens **Color Module 2025.10**, Final Community Group Report, 28 October 2025 |

**Preview, draft, editor and future reports are not part of this profile**
(DEC-S-074, RISK-056), and the 2026 draft and preview material is **not** authority
for anything in this decision. **A tool accepting a literal is not the profile
admitting it**; committed CDS validator strings were treated as corroboration only.

### Rationale

WCAG's contrast obligation is defined over relative luminance computed from sRGB
components. Authoring the normative source in that representation makes a role
pairing's declared contrast obligation computable **directly from the source**,
offline and deterministically, with **no conversion inside the normative path**.
Every conversion in that path is a place where an accessibility obligation can
change without any artifact recording that it did — and the visual foundation
carries all five WCAG 2.2 criteria CDS owns without the consumer.

The registered channel model is not screen-only: it includes paginated, printed,
projected and exported channels, and **four of nine channels have no accessibility
profile at all** (RISK-046). A representation strongest on screen and weakest in
print would be strongest exactly where CDS has the least registered obligation.

The perceptual argument is nevertheless real, and it is granted in full where it
belongs: **in how a value is arrived at**. Making a perceptual space canonical —
alone or alongside `srgb` — would manufacture two normative sources for one value,
and DEC-S-034 does not resolve such a conflict by recency or convenience; it
**invalidates the affected artifact state**. Synchronization is not a mitigation.

Full architecture rationale:
[ADR-0004](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md).

### Consequences

- The [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md) and
  the [Visual Foundation Colour Architecture](../architecture/VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
  state the canonical representation; the colour architecture's *colour space and
  encoding* deferral is closed and **all its other deferrals stand**.
- **OD-1 is answered**, with the `hex` question recorded as an explicit residual.
- **VP-2** of the value-selection prerequisites is satisfied for colour.
  **VP-3, VP-4 and VP-5 remain unsatisfied**, so **no colour value may be
  selected**.
- **No schema, validator, test, or fixture changes.** `profileVersion` stays `"1"`.
- Enforcement of clause 7 is a stated obligation on **CDS-WP-024** and is **not
  implemented**.
- **No accessibility claim, no evidence, and no maturity results.** Every visual
  artifact stays **AE-0**; VF-1 stays `Proposed`.

### Boundary

This decision selects a **representation**, not a value. It awards no maturity, no
Candidate, no Stable, no evidence, no admission, no claim, no conformance, no
Product Profile, no consumer activation, no pilot, no licence, no release, no tag,
and no publication authority, and it activates no work package.

---

## DEC-S-129 — WCAG 2.2 is the contrast evaluation authority; additional methods are informational only

- **Status:** Accepted — **effective at the Human-Maintainer exact-byte integration
  commit `42a568d823de3388e45af62967546f13ad67eff6`** of the CDS-WP-020 Decision
  Integration Pass, which followed a Fresh Independent Review and Nova integration
  adjudication. Before that commit this entry was uncommitted executor output
  prepared under an explicit Human-Maintainer authorization and changed **no**
  authoritative CDS state.
- **Date:** 2026-08-27
- **Type:** Visual token representation, evaluation authority and source identity
  decision
- **Work package:** CDS-WP-020 — Reference and Semantic Token Foundation (Decision
  Integration Pass)
- **Human-Maintainer authorization:** 2026-08-27
- **Architecture record:** none. **DEC-S-129 is deliberately not an architecture
  dependency of [ADR-0004](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md)**
  — it is an accessibility-methodology decision, not a representation or
  source-identity decision.

### Decision

1. **The normative contrast evaluation baseline is WCAG 2.2** — the W3C
   Recommendation already established as the sole normative accessibility basis
   (DEC-S-049, DEC-S-054). **Not `WCAG 2.x`. Not `latest`.** A floating version is
   not an identity, exactly as `latest` is not an identity for a source revision
   (DEC-S-080).

2. **Contrast is computed by the contrast-ratio method that the WCAG 2.2 contrast
   criteria already cited in CDS scope themselves require.** CDS adopts that method
   by reference and defines no method of its own.

3. **CDS restates no criterion threshold and invents none.** The obligation is
   whatever the cited criterion itself requires. This continues the position the
   Accessibility Requirements Baseline and the Colour Architecture already hold, and
   changes it in no way.

4. **Contrast is contextual and pair-based.** It is a property of a **pair, in a
   context, in a channel** — never of a single colour value. A record that states a
   single value's contrast has evaluated nothing (CR-2, CR-3, SR-3, SR-4, VE-1).

5. **Pass and fail comparison uses the full available computation precision.**

6. **No rounding is performed before comparison.** A value is not rounded,
   truncated, or snapped and then compared.

7. **Presentation and display rounding cannot alter the decision.** A rounded figure
   shown in a report, a table, or a user interface is a presentation artifact; the
   comparison outcome is computed from the unrounded result.

8. **Additional contrast methods, including APCA, may be calculated and recorded**
   as **informational or experimental analysis** alongside the normative evaluation.

9. **Calculating an additional method grants it no normative authority whatsoever.**
   Recording a figure is not adopting a method.

10. **An additional method satisfies no CDS obligation and supports no claim merely
    by being computed.** It may not be used to argue that a pairing meets an
    obligation, to substitute for the normative evaluation, or to relax one.

11. **An automated contrast calculation is not accessibility evidence and grants no
    AE level** (DEC-S-053, EV-1). It is input to a review, never consent, and
    **absence of a failure is not evidence of success** (EV-4).

12. **This decision creates no conformance claim.** A target is not a claim
    (DEC-S-050), and **no accessibility claim of any level is valid today**, by
    anyone, including CDS itself.

13. **No contrast evaluation is performed by this work package.** No pair exists to
    evaluate: **no visual value exists in CDS**, and none is created here.

### Rationale

Two failure modes are being closed before either can occur.

The first is **version drift**. A baseline recorded as `WCAG 2.x` or `latest` cannot
be bound to an evidence record, cannot be reviewed for freshness, and silently
changes what an artifact was evaluated against. CDS already refuses floating
identities for source revisions and for baseline environments (DEC-S-068,
DEC-S-071, DEC-S-080); the same refusal applies here.

The second is **precision laundering**. Rounding before comparison converts a fail
into a pass at the boundary, and it does so invisibly, in a step that looks like
formatting rather than like a decision. Fixing the rule now — full precision for the
comparison, rounding only for presentation — costs nothing while no value exists,
and is very hard to retrofit once evidence records exist that were produced the
other way.

The third concern is the standing of **alternative perceptual contrast models**.
They are genuinely interesting and may well be more predictive for some conditions,
and CDS has no reason to forbid computing them. What CDS must forbid is the quiet
promotion from *computed* to *authoritative* — the same pattern as a validator pass
becoming maturity authority (VR-4) or a digest becoming a signature (DEC-S-090).
**Calculation is not adoption.**

### Consequences

- The
  [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
  and the [Visual Foundation Colour Architecture](../architecture/VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
  name the evaluation authority and the precision rule; **no threshold is added to
  either**.
- Any future evidence record carrying a contrast figure must state the method, the
  pair, the context, the channel, and the WCAG 2.2 criterion — and must not round
  before comparing.
- **No new accessibility requirement is created**, and the WCAG 2.2 AA target and
  the applicability matrix are unchanged.
- **No evidence is produced or admitted.** Every visual artifact stays **AE-0**;
  `AE1-CDS-WP016-SEMSTATUS-004` is unaffected and does not transfer.
- **No risk is registered, accepted, or closed.**

### Boundary

This decision names an **evaluation authority and a precision rule**. It evaluates
nothing, measures nothing, and claims nothing. It awards no maturity, no Candidate,
no Stable, no evidence, no admission, no claim, and no conformance, and it activates
no work package.

---

## DEC-S-130 — The CDS profile admits an explicit, minimal, closed visual token type set

- **Status:** Accepted — **effective at the Human-Maintainer exact-byte integration
  commit `42a568d823de3388e45af62967546f13ad67eff6`** of the CDS-WP-020 Decision
  Integration Pass, which followed a Fresh Independent Review and Nova integration
  adjudication. Before that commit this entry was uncommitted executor output
  prepared under an explicit Human-Maintainer authorization and changed **no**
  authoritative CDS state.
- **Date:** 2026-08-27
- **Type:** Visual token representation, evaluation authority and source identity
  decision
- **Work package:** CDS-WP-020 — Reference and Semantic Token Foundation (Decision
  Integration Pass)
- **Human-Maintainer authorization:** 2026-08-27, following the Nova adjudication of
  **OD-2**
- **Architecture record:** [ADR-0004](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md)

### Decision

1. **The CDS Token Format Profile carries an explicit `$type` admission profile.**
   The profile previously required an explicit `$type` *"from the DTCG-defined types
   applicable to CDS scope"* and **enumerated no set**. That set is now enumerated.

2. **The initial admitted visual token type set is exactly three values:**

   | Admitted `$type` | Verified against |
   | --- | --- |
   | `color` | Design Tokens **Format Module 2025.10**, Final Community Group Report, 28 October 2025 |
   | `dimension` | Design Tokens **Format Module 2025.10**, Final Community Group Report, 28 October 2025 |
   | `number` | Design Tokens **Format Module 2025.10**, Final Community Group Report, 28 October 2025 |

   Each literal was verified **directly against the final published report**, not
   inferred from CDS tooling.

3. **No arbitrary or free-form type admission exists.** A `$type` that is not in the
   admitted set is not admitted, whatever its provenance.

4. **DTCG-defined is not CDS-admitted.** The pinned report defines further types;
   CDS admits three. The difference is deliberate and is the substance of this
   decision.

5. **A `$type` the pinned report does not define fails closed at the applicable
   lower validation layer** — the DTCG contract layer, where the type is unknown to
   the external basis itself.

6. **A `$type` the pinned report defines but CDS does not admit fails closed at CDS
   profile validation.** The two cases are distinct and must remain distinguishable:
   one is *not a DTCG type*, the other is *not a CDS-admitted type*.

7. **No composite type is admitted now.** A composite bundles several decisions into
   one token — a shadow bundles colour with offsets and blur; a typography token
   bundles family, weight, size and line height — and that bundling is exactly where
   the semantic layer loses the ability to declare a **per-part** obligation under
   SR-3, SR-4 and SR-5.

8. **Font-family and font-weight identity is not admitted prematurely.** The
   representation of a typeface identity and a weight identity remains **deferred**,
   recorded as a residual open item under **OD-2**, and it stays subject to the
   Typography Architecture's FP-1 … FP-8 licensing, provenance, offline, fallback,
   script-coverage and distribution gate, which is an **Elevated** change.

9. **Every normative CDS visual token carries its own explicit `$type`.**
   **Inheritance-only typing is not sufficient for CDS profile conformance.** This
   restates and applies the CDS Token Format Profile's existing explicit-typing
   requirement; it introduces no new obligation.

10. **A normative visual source must not rely on a group-level or root-level
    `$type` as typing authority.** This is a **CDS profile restriction only**. It
    **does not redefine DTCG**, which remains free to permit what it permits; CDS
    simply requires more of its own normative sources than the external basis
    requires of a document in general (DEC-S-076).

11. **`$type` carries value-type semantics only.** It **must not** imply, encode, or
    be read as maturity, evidence, approval, lifecycle, authority, publication, or
    conformance. A type is what a value *is*, never what an artifact has *earned*.

12. **`$type` is identity-affecting and digest-affecting.** Adding, removing, or
    changing a `$type` changes the canonical source bytes and therefore the RFC 8785
    canonicalization and its SHA-256 digest (ADR-0002, DEC-S-090).

13. **Existing evidence never transfers over that revision change.** A `$type` change
    is a source-revision change, and evidence is bound to a source revision
    (DEC-S-126, AF-2, RV-4). Fresh evidence, a fresh independent review, and a fresh
    admission are required.

14. **`profileVersion` remains exactly `"1"`.** It is **not** bumped by this
    decision. The admitted set is an explicit statement of what the profile already
    required but never enumerated; it constrains **no existing artifact**, because no
    visual token exists and the one existing normative token source
    (`semantic/status`) is non-visual and untouched. A `profileVersion` change is a
    compatibility and migration event under DEC-S-082 and belongs to the work package
    that implements enforcement, if that implementation requires one.

15. **This decision modifies no `schemas/`, no `tools/`, and no `tests/` artifact.**
    In particular, the committed token-document schema still constrains `$type` **not
    at all**, and the offline validator's bounded token-`$type` set remains a
    **DEC-S-098 V2 coverage boundary and not a profile admission** — reading it as one
    is **RISK-074**, and this decision exists partly to close that misreading.

16. **Implementation requirements recorded for CDS-WP-024, and not implemented
    here:** explicit-own-`$type` enforcement; CDS admitted-set validation, distinct
    from unknown-DTCG-type handling; and fail-closed handling for both.

17. **Extension is additive and governed.** A later family needing a further type
    obtains it through an **Elevated** profile change with compatibility, migration,
    evidence, Nova review, and Human-Maintainer approval (DEC-S-082) — never by a
    tool accepting it, a fixture using it, or a document containing it.

18. **No token, no value, and no identifier is created.**

### Rationale

Minimal is the only setting in which **admitted does not exceed validated**, and the
gap between those two is precisely the shape RISK-074 describes. Two repository
facts make the risk concrete and both are easy to misread: the committed
token-document schema places **no** `$type` constraint, and the validator's bounded
type set is a **coverage boundary** rather than an admission. Neither states what
CDS admits, and neither may be read as though it did — so the admission has to be
stated explicitly, in a normative human-readable source.

Composites are excluded now for a reason that is structural rather than
conservative: a bundled token cannot carry a per-part accessibility obligation, and
admitting one before the roles that would use it exist would decide the granularity
question by implication — the failure mode this entire pass exists to avoid.

Clause 11 closes the other direction of the same confusion. `$type` is metadata a
tool reads, and metadata is routinely over-read as standing: a source set declaring
`Candidate` is not Candidate (VR-3, VR-4, DEC-S-126). A type is a value-shape
statement and nothing more.

Full architecture rationale:
[ADR-0004](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md).

### Consequences

- The [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md) states
  the admitted set; the
  [Machine-Readable Validation Contract](../architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)
  records the two-layer fail-closed split as a requirement on CDS-WP-024.
- The [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
  deferral *"the admitted DTCG `$type` set for visual families"* is closed; **its
  other fourteen deferrals stand**.
- **OD-2 is answered**, with font-family and font-weight identity recorded as an
  explicit residual.
- **VP-2** is satisfied for the families expressible in `color`, `dimension` and
  `number`; it is **not** satisfied for typeface and weight identity.
  **VP-3, VP-4 and VP-5 remain unsatisfied**, so **no value may be selected**.
- **No schema, validator, test, or fixture changes**, and **`profileVersion` stays
  `"1"`**.
- **No maturity, no evidence, and no claim results.**

### Boundary

This decision admits **types**, not values. It awards no maturity, no Candidate, no
Stable, no evidence, no admission, no claim, no conformance, no Product Profile, no
consumer activation, no pilot, no licence, no release, no tag, and no publication
authority, and it activates no work package.

---

## DEC-S-131 — The Source Set is the independently evaluable unit; aggregation confers no maturity

- **Status:** Accepted — **effective at the Human-Maintainer exact-byte integration
  commit `42a568d823de3388e45af62967546f13ad67eff6`** of the CDS-WP-020 Decision
  Integration Pass, which followed a Fresh Independent Review and Nova integration
  adjudication. Before that commit this entry was uncommitted executor output
  prepared under an explicit Human-Maintainer authorization and changed **no**
  authoritative CDS state.
- **Date:** 2026-08-27
- **Type:** Visual token representation, evaluation authority and source identity
  decision
- **Work package:** CDS-WP-020 — Reference and Semantic Token Foundation (Decision
  Integration Pass)
- **Human-Maintainer authorization:** 2026-08-27, following the Nova adjudication of
  **OD-3**
- **Architecture record:** [ADR-0004](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md)

### Decision

1. **The Source Set is the canonical independently evaluable unit** of a CDS
   machine-readable source. Evaluation, evidence, maturity, and approval attach
   there.

2. **Each source set independently carries** its `sourceSetId`, its
   `sourceRevision`, its `layer`, its dependency set where applicable, its
   `maturityState`, and its `approvalState`.

3. **Identity is stable and explicit.** A source set's identity is declared, not
   derived from a path, a file name, a directory, or a tool's convention.

4. **The root vocabulary is controlled by the registered CDS Visual Foundation
   families** (VF-1 … VF-9). **No concrete root identifier is invented, adopted,
   reserved, or recommended by this decision**; the concrete identifiers remain a
   residual open item under **OD-3**, coupled to **OD-4**.

5. **Topology: one source set per independently evaluable Family × Token-Flow-Layer
   unit.**

6. **A family occupying token-flow layer 1 and token-flow layer 2 may therefore have
   two source sets** — one Reference, one Semantic — each independently evaluable.

7. **One manifest may aggregate multiple source sets.** **A source set is not a
   manifest, and one source set must never be equated with one manifest.** The
   committed Source-Set Manifest contract carries an inventory of entries, each with
   its own identity, revision, maturity and approval.

8. **Correction of finding CDS-WP-020-R1-F-02 (recorded as `F-020-02`).** Its
   **conclusion stands**: a source-set payload carries **one** `maturityState`, so a
   single shared visual source set spanning several families cannot express the
   per-family, never-inherited maturity that **AF-1** and **AF-3** require. Its
   **artifact-count mechanism was imprecise**: it implied that per-family, per-layer
   source sets multiply manifests and resolvers at the same rate. They do not —
   clause 7 is why. The governance cost of preserving AF-1 and AF-3 is a source set
   per independently evaluable unit, not a manifest per family.

9. **Maturity binds to the pair (`sourceSetId`, `sourceRevision`)**, and to nothing
   else.

10. **A new source revision inherits no evidence and no admission.** Evidence is
    revision-bound and never transfers (DEC-S-126, AF-2, RV-4). A later revision
    requires fresh evidence, a fresh independent review, and a fresh
    Human-Maintainer admission.

11. **No maturity propagation exists** — in either direction — between source sets,
    between token-flow layers, between families, from a manifest to its entries,
    from entries to their manifest, to or from generated artifacts, out of metadata,
    or out of a validator result.

12. **Manifest-level maturity and approval describe only the manifest artifact
    itself.** They are **not** a roll-up, **not** a maximum, **not** a minimum, and
    **not** inherited.

13. **Binding invariant: AGGREGATED is not MATURE.** Declaring an inventory is a
    structural act and confers nothing on what is inventoried, and nothing on the
    inventory.

14. **Evidence remains exact-byte and revision-bound**, with byte-drift
    invalidation, exactly as DEC-S-126 already requires.

15. **A source-set rename is a migration and identity event**, carrying a migration
    reference (DEC-S-082, DEC-S-040).

16. **A file move alone is not a `sourceSetId` change.** Location is not identity.

17. **A `sourceSetId` change invalidates admitted evidence.** The evaluated thing is
    no longer the same thing.

18. **Cross-family aliases and references stay governed by the existing rules** —
    strictly downward dependency, offline resolvability, declared local
    Manifest/Resolver graph, fail-closed on anything dangling, cyclic, undeclared,
    type-incompatible, or non-local (DEC-S-078, DEC-S-079, DEC-S-091, AL-1 … AL-8).

19. **No source set, manifest, resolver, identifier, or value is created by this
    decision.** Visual source sets in existence remain **0**.

### Rationale

**AF-1** forbids inherited maturity and **AF-3** grants each family its own pace.
Both were written knowing the governance cost, and a topology that cannot express
them is the wrong topology — the reason to reject one is not expense but
correctness.

The imprecision corrected in clause 8 matters because it changed the apparent price
of doing the right thing. Reading the committed manifest contract rather than
reasoning about it shows that a manifest declares an **inventory of entries**, each
carrying its own identity, revision, maturity and approval. Per-family, per-layer
source sets therefore do not multiply manifests, and the argument for collapsing
independent maturities into one shared artifact loses the cost basis it rested on.

Clauses 11 to 13 exist because **aggregation is where maturity is most likely to be
lost quietly**. It is the same failure CDS has already had to name three times: a
source set declaring `Candidate` is not Candidate (VR-4, RV-3), a validator pass is
metadata coherence and never maturity authority (VR-4, DEC-S-053), and a digest is
not a signature (DEC-S-090). A manifest that appeared to roll up its entries would
be a fourth instance, and the most convincing one, because a roll-up looks like
bookkeeping rather than like a claim.

Full architecture rationale:
[ADR-0004](ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md).

### Consequences

- The [Machine-Readable Source Model](../architecture/MACHINE_READABLE_SOURCE_MODEL.md)
  and the
  [Visual Foundation Governance and Lifecycle](../governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
  record the source-set unit, the manifest boundary, and the aggregation invariant.
- **OD-3 is answered** for identity, topology and maturity granularity, with the
  concrete root identifiers recorded as an explicit residual coupled to **OD-4**.
- **`F-020-02` is corrected as stated in clause 8** — conclusion upheld, mechanism
  corrected — in the forward roadmap and the CDS-WP-020 notes.
- **VP-5 remains unsatisfied**: the topology rule is decided, but **no concrete
  source-set identity and no source revision exists**, so no value may be selected
  against one.
- **`OD-6` is unaffected.** How many families CDS matures separately remains open,
  and this decision pre-answers none of it.
- **No schema, validator, test, or fixture changes**, and **`profileVersion` stays
  `"1"`**.
- Enforcement of clauses 9 to 13 is a stated obligation on **CDS-WP-024** and is
  **not implemented**.
- **`semantic/status` is entirely unaffected** — its source set, revision, maturity,
  approval, and admitted evidence are unchanged, and
  `AE1-CDS-WP016-SEMSTATUS-004` transfers to nothing.

### Boundary

This decision fixes a **unit of evaluation**, not an artifact. It awards no
maturity, no Candidate, no Stable, no evidence, no admission, no claim, no
conformance, no Product Profile, no consumer activation, no pilot, no licence, no
release, no tag, and no publication authority, and it activates no work package.
**VF-1 … VF-9 stay `Proposed`; visual source sets stay 0; Stable stays `No`.**

---

## DEC-S-132 — Visual Identifier Grammar and the Two Identity Spaces

- **Status:** Accepted — **effective at the Human-Maintainer exact integration
  commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`** of the exact reviewed Working
  Tree object of the CDS Step-9 Decision Integration Pass, which followed a Fresh
  Independent Review and Nova integration adjudication. Before that commit this
  entry was uncommitted executor output prepared under an explicit Human-Maintainer
  authorization given on 2026-09-05 and changed **no** authoritative CDS state; no
  earlier wording conferred effectivity. **A review PASS is not a commit.**
- **Date:** 2026-09-05
- **Type:** Visual identifier, scale ownership, role admission and theme sequencing
  decision
- **Work package:** — none. Prepared by the **CDS Step-9 Decision Integration
  Pass**; **no work package is authorized**, and this decision authorizes none.
- **Human-Maintainer authorization:** 2026-09-05, following the Nova adjudication of
  the CDS Step-9 R1/R2 decision package — **OD-4**, with the **OD-3** concrete-root
  residual
- **Architecture record:** [ADR-0005](ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md)

### Decision

1. **Visual token paths are family-rooted.** The root of a visual token path is a
   single segment naming a registered visual foundation family, and the token-flow
   layer is not part of it.

2. **Reference grammar:** `<family>.<primitive-group>.<step>[.<qualifier>]`. The
   qualifier position is **declared and optional**; **no concrete qualifier is
   created**, and declaring the position is not permission to populate it.

3. **Semantic grammar:** `<family>.<role>[.<qualifier>]`, with the same declared,
   optional, unpopulated qualifier position.

4. **The term is `qualifier`, not `modifier`.** *Conditional modifier* is already
   bound in CDS to **Resolver / Theme composition** semantics — the construct that
   composes source sets into a resolved context. Re-using it for a path segment
   would collide the identity vocabulary with the theme-mechanism vocabulary in the
   one area where **N-6** and **T-8** prohibit theme terms in paths. **This renames
   the N-6 path slot; N-6's principle is unchanged and its wording is reconciled to
   `qualifier` in the Visual Foundation Architecture.**

5. **The token-flow layer is never a token-path segment.** It remains the existing
   explicit `layer` field, already enumerated as `reference`, `semantic`,
   `component`, `product-profile` in the committed token-document and source-set
   manifest schemas.

6. **Token-path identity and Source Set identity are two separate identity
   spaces.** Neither is computable from the other, and neither may be presented as
   a rendering of the other.

7. **`sourceSetId` is declared, never derived** — not from a path, a file name, a
   directory, or a tool convention (DEC-S-131 clause 3, restated and applied, not
   changed).

8. **The `sourceSetId` form for these visual source sets is `<layer>/<family>`**,
   following the committed `semantic/status` precedent (DEC-S-115) and the
   `sourceSetId` syntax the committed schemas already enforce.

9. **Root vocabulary.** The technical root segment of each registered visual family
   in current scope is fixed as:

   | Family | Technical root |
   | --- | --- |
   | **VF-1 Colour** | `color` |
   | **VF-2 Typography** | `typography` |
   | **VF-3 Space and Size** | `space` |
   | **VF-5 Shape** | `shape` |
   | **VF-6 Surface and Elevation** | `surface` |

   `color` is the technical identifier; **`Colour` remains the display and prose
   term**, exactly as DEC-S-110 separates technical identifiers from display
   labels.

10. **Exact source-set root identities.** The following ten identities are fixed as
    **identifier authority**:

    | Family | Reference | Semantic |
    | --- | --- | --- |
    | **VF-1** | `reference/color` | `semantic/color` |
    | **VF-2** | `reference/typography` | `semantic/typography` |
    | **VF-3** | `reference/space` | `semantic/space` |
    | **VF-5** | `reference/shape` | `semantic/shape` |
    | **VF-6** | `reference/surface` | `semantic/surface` |

    **These are identifier-authority statements only. They create no Source Set
    instance, no `sourceRevision`, no manifest, no resolver, no token, and no
    file.** Nothing here is instantiated, and **visual source sets remain 0.**

11. **Root granularity: one root per registered family in this scope.** A compound
    display family name does not produce two roots. **VF-3 Space and Size takes the
    single root `space`; VF-6 Surface and Elevation takes the single root
    `surface`.** Internal constructs are differentiated by the
    **`<primitive-group>`** position — which may, for example, distinguish
    space, size and density within `space`, or surface, elevation, overlay and
    scrim within `surface`. **Those primitive-group examples create no concrete
    token identifier**, are not an enumeration, and reserve nothing.

12. **The namespace is flat: `<layer>/<family>`.** No `visual`, `foundation`,
    `brand`, `product`, `channel`, `context`, or `theme` namespace segment is
    introduced at any position.

13. **Every existing identifier constraint is preserved and unchanged.** The
    restrictive lower-case technical identifier profile and its segment syntax
    (DEC-S-081); technical identifier separate from display label (DEC-S-110);
    case-only collisions prohibited; no product, brand, customer, consumer,
    channel, component, status-axis, theme, context or profile term in a shared
    foundation identifier (N-2 … N-6, RN-3 … RN-7, SN-2 … SN-6); appearance names
    permitted **only** at reference positions (N-1, RN-1) and prohibited at
    semantic positions (SN-1, VF-I-2); a name states a purpose, not a rank (N-7);
    every rule machine-checkable (N-8).

14. **A rename is an identity migration event**, carrying a migration reference
    (DEC-S-082, DEC-S-040, RN-9, SN-9, RP-10, SR-12). A `sourceSetId` rename is
    additionally an identity event that **invalidates admitted evidence**
    (DEC-S-131 clauses 15 and 17).

15. **A file move alone is not an identity change.** Location is not identity
    (DEC-S-131 clause 16).

16. **AL-2 is unchanged: a semantic role never aliases another semantic role.** A
    post-rename compatibility alias implemented as a semantic-role alias edge is
    therefore prohibited, and this decision creates no exception to it.

17. **Any migration or deprecation compatibility mechanism outside the normative
    Semantic alias graph is OPEN and is not decided here.** DEC-S-039 declares
    compatibility per contract axis and DEC-S-040 requires a viable migration path
    for a Stable artifact, but **no committed CDS source specifies a technical
    mechanism**, and this decision specifies none. Silence is recorded as silence.

18. **The OD-3 concrete-root residual is RESOLVED by this decision** once effective.
    DEC-S-131 clause 4 controlled the root vocabulary through the registered
    families and deliberately invented, adopted, reserved and recommended no
    concrete identifier; clauses 9 and 10 above supply them.

19. **OD-4 is ANSWERED by this decision** once effective.

20. **VP-4 becomes satisfied for VF-1, VF-2, VF-3, VF-5 and VF-6** once effective —
    the identifier grammar and the concrete roots are both decided, so a value
    would have somewhere to live that will not be renamed. **This states nothing
    else.** No identifier instance exists; no Source Set exists; no
    `sourceRevision` exists; **VP-5 remains UNSATISFIED**; and no value may be
    selected, because VP-3, VP-5, VP-6 and VP-7 are not satisfied.

### Rationale

The repository already fixed identifier **form** — segment syntax, case rules,
prohibited terms, rename semantics — and left identifier **structure** undecided.
That gap was load-bearing: **VP-4** requires *"somewhere to live that will not be
renamed"*, and a grammar without roots does not provide one, so no authoring work
package could be authorized while it stood open.

Family-rooted paths match the one committed precedent. The `semantic/status` source
set carries `sourceSetId` `semantic/status` and `layer` `semantic`, while its token
document's root group is `status` — the layer appears in the source-set identity
and **not** in the token path. That asymmetry is not an accident of that work
package; it is the correct shape, and clauses 5 to 8 make it a rule rather than a
habit.

Layer-rooted token paths were rejected because the layer is already an enumerated,
schema-validated field in both committed schemas. Encoding it a second time in
every identifier would make a layer change a mass rename — a DEC-S-082 migration
event that, for source sets, additionally invalidates admitted evidence under
DEC-S-131 clause 17 — for information the manifest already holds.

The `qualifier` rename is the smallest change that prevents a genuine collision.
The repository uses *conditional modifier* for the Resolver construct that resolves
a theme context; **N-6** and **T-8** simultaneously forbid theme terms inside a
path. Leaving one word to mean both a path segment and a theme-composition operator
would have put the collision precisely where the prohibition lives.

The compound-family question was decided in the direction that registers **less**.
VF-3 and VF-5 and VF-6 carry **no consumer demand evidence at all**, and splitting
a display name into two roots would have multiplied identity surface for families
with no demonstrated need — RISK-021 and RISK-026 in the one place where the cost
is permanent, because a root rename is an evidence-invalidating identity event.

Full architecture rationale:
[ADR-0005](ADR-0005-VISUAL_IDENTIFIER_GRAMMAR_AND_IDENTITY_SPACES.md).

### Consequences

- The [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
  naming model reconciles **N-6** to `qualifier` and records the fixed roots; the
  [Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md)
  and the
  [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
  record the two grammars and the root authority at their respective positions.
- **`OD-4` is answered and the `OD-3` concrete-root residual is resolved**; both are
  reconciled in the **non-normative**
  [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
  register.
- **VP-4 is satisfied for VF-1, VF-2, VF-3, VF-5 and VF-6**; **VP-5 is not**, and
  visual source sets remain **0**.
- Enforcement of the grammar and the root vocabulary is a stated obligation on
  **CDS-WP-024**, and is **not implemented**. **No schema, validator, test, or
  fixture is changed, and `profileVersion` stays `"1"`.**
- **`semantic/status` is entirely unaffected.** Its `sourceSetId`, revision,
  maturity, approval and admitted evidence are unchanged, and
  `AE1-CDS-WP016-SEMSTATUS-004` transfers to nothing.

### Boundary

This decision fixes **identity**, not artifacts. It creates no token, no
identifier instance, no Source Set, no manifest, no resolver, no file, and no
value. It awards no maturity, no Candidate, no Stable, no evidence, no admission,
no claim, no conformance, no Product Profile, no consumer activation, no pilot, no
licence, no release, no tag, and no publication authority, and **it activates no
work package** — **`CDS-WP-020A` and CDS-WP-021 … CDS-WP-053 remain `Planned`, not
active, and not authorized.** **VF-1 … VF-9 stay `Proposed`; visual values stay 0;
visual source sets stay 0; Stable stays `No`.**

---

## DEC-S-133 — Per-Scale Topology Under the Common Scale Contract

- **Status:** Accepted — **effective at the Human-Maintainer exact integration
  commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`** of the exact reviewed Working
  Tree object of the CDS Step-9 Decision Integration Pass, which followed a Fresh
  Independent Review and Nova integration adjudication. Before that commit this
  entry was uncommitted executor output prepared under an explicit Human-Maintainer
  authorization given on 2026-09-05 and changed **no** authoritative CDS state; no
  earlier wording conferred effectivity.
- **Date:** 2026-09-05
- **Type:** Visual identifier, scale ownership, role admission and theme sequencing
  decision
- **Work package:** — none. Prepared by the **CDS Step-9 Decision Integration
  Pass**; **no work package is authorized**, and this decision authorizes none.
- **Human-Maintainer authorization:** 2026-09-05, following the Nova adjudication of
  the CDS Step-9 R1/R2 decision package — **OD-5**
- **Architecture record:** none. **DEC-S-133 is deliberately not an architecture
  dependency of ADR-0005**: it applies the existing ST-1 … ST-7 contract and changes
  nothing about what the machine-readable profile admits or what the validator
  enforces.

### Decision

1. **ST-1 … ST-7 remain the common normative contract** binding every ordered
   primitive set. This decision adds no requirement to them and weakens none.

2. **There is no universal cross-family scale base.** A single base shared across
   heterogeneous visual families is **rejected**.

3. **Each ordered primitive set independently owns** its **anchor declaration**, its
   **ordering**, its **progression-rule kind**, its **step-count decision**, its
   **extension behaviour**, and its **exclusions and declared deviations**.

4. **No family's ordered scale derives its authority, base, rule, or values from
   another family's scale.** ST-5's *"computable … from its declared base and
   rule"* is per-scale, and it is read that way.

5. **Binding invariant: `SCALE TOPOLOGY ≠ SCALE VALUES`.** A topology states how a
   scale is structured; it states no magnitude, and structuring a scale selects
   nothing that renders.

6. **VP-3's "base" means the anchor declaration — the structural anchor position
   and the fact that other steps stand in a declared relation to it. It does not
   mean a numeric anchor magnitude.** A magnitude is a value and is governed by
   value selection.

7. **This decision selects no value.** No base magnitude, no ratio magnitude, no
   step magnitude, no colour, no dimension, and no number.

8. **Current scope:** **VF-2 Typography**, **VF-3 Space and Size**, **VF-5 Shape**,
   **VF-6 Surface and Elevation**.

9. **Opacity remains an attribute** of **VF-1** (alpha within a colour value) and
   **VF-6** (overlay and scrim), where an ordered opacity set is already governed.
   **No standalone opacity family is introduced** (DEC-S-128 clause 11, restated,
   not changed).

10. **Excluded from this decision:** **VF-1 Colour tonal topology**, **VF-4 Layout
    and Grid** (CDS-WP-021), **VF-7 Iconography** (CDS-WP-037), **VF-8 Motion**
    (CDS-WP-035), **VF-9 Theme and Context Mechanism** (CDS-WP-022, which holds no
    primitive of its own).

11. **VF-1 tonal topology is OPEN and DEFERRED, and this decision answers no part
    of it.** A colour tonal set is not enumerated among the ordered primitive sets
    the Visual Reference Token Foundation lists; it would be ordered by a perceptual
    property while **OKLCH is a derivation and analysis space only** (DEC-S-128
    clauses 2 and 3) and the canonical `srgb` space is not perceptually uniform; and
    it is coupled both to the open **OD-1 `hex`** residual and to **CDS-WP-022**,
    because how many tonal ranges a palette needs depends on how many contexts
    exist. It requires its own separately authorized decision.

12. **OD-5 is PARTIALLY ANSWERED by this decision.** The **scale ownership model**
    and the **topology/value boundary** are decided. **The per-family topology
    parameters are not**: for every family in scope, the concrete anchor
    declaration, progression-rule kind, step count, extension behaviour, and
    exclusions **remain OPEN**, and this decision invents none of them. The
    residual is recorded as **per-family topology parameters remain open**,
    alongside the separate **VF-1 tonal topology** residual.

13. **VP-3 remains UNSATISFIED for every family, and fails closed.** VP-3 requires
    the family's **base, progression rule, step count, and extension behaviour** to
    be decided. This decision fixes **who owns them and what kind of statement they
    are**; it does not decide them for any family. **VP-3 is therefore not
    satisfied by the ownership model alone**, is **UNSATISFIED for VF-2, VF-3, VF-5
    and VF-6**, and is **UNSATISFIED for VF-1** for the additional reason in clause
    11. **No value may be selected.**

### Rationale

The recommendation this decision replaced proposed one declared base unit with
per-family step sets derived from it. **ST-5 does not support it.** The requirement
reads *"computable offline and deterministically **from its declared base and
rule**"*, and the section that carries ST-1 … ST-7 is introduced as *"Normative as
requirements on a scale, not as a scale."* Both are per-scale. A universal base
would have created exactly the coupling **AF-3** exists to prevent: a change made
for one family would propagate silently into every other, and radius, stroke and
elevation have no honest reason to share a spacing rhythm.

Clause 6 exists because VP-3's word *base* is genuinely ambiguous and the ambiguity
is not harmless. Read as a magnitude, VP-3 would require a value in order to permit
a value — a circularity under which **no visual value could ever be selected**.
Read as an anchor declaration, VP-3 is a structural gate that a decision can
satisfy. The repository never stated which reading applies, so the reading is fixed
here rather than assumed, and clause 5 records the boundary it rests on — the same
move DEC-S-131 clause 13 made for `AGGREGATED is not MATURE`.

Clause 13 is the conservative consequence and is deliberate. Deciding **who owns a
scale** is not deciding **what the scale is**, and reporting VP-3 as satisfied
because the ownership model is settled would be exactly the overstatement the value
selection rules exist to prevent. The gate fails closed.

### Consequences

- The
  [Visual Reference Token Foundation](../architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md)
  records the ownership model and the topology/value boundary against ST-1 … ST-7;
  the
  [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
  record the VP-3 reading and the unchanged **UNSATISFIED** state.
- **`OD-5` is partially answered**, with two residuals — **per-family topology
  parameters** and **VF-1 tonal topology** — recorded in the **non-normative**
  [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
  register.
- **VP-3 stays UNSATISFIED for every family**, so **no visual value may be
  selected** and visual values remain **0**.
- **No schema, validator, test, or fixture is changed**, and `profileVersion` stays
  `"1"`.

### Boundary

This decision fixes **ownership and a boundary**, not a scale. It selects no base,
no ratio, no step, and no value; it creates no token, identifier, or source set. It
awards no maturity, no Candidate, no Stable, no evidence, no admission, no claim,
no conformance, no Product Profile, no pilot, no licence, no release, no tag, and
no publication authority, and **it activates no work package**. **VF-1 … VF-9 stay
`Proposed`; visual values stay 0; visual source sets stay 0; Stable stays `No`.**

---

## DEC-S-134 — Visual Role Admission Rule

- **Status:** Accepted — **effective at the Human-Maintainer exact integration
  commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`** of the exact reviewed Working
  Tree object of the CDS Step-9 Decision Integration Pass, which followed a Fresh
  Independent Review and Nova integration adjudication. Before that commit this
  entry was uncommitted executor output prepared under an explicit Human-Maintainer
  authorization given on 2026-09-05 and changed **no** authoritative CDS state; no
  earlier wording conferred effectivity.
- **Date:** 2026-09-05
- **Type:** Visual identifier, scale ownership, role admission and theme sequencing
  decision
- **Work package:** — none. Prepared by the **CDS Step-9 Decision Integration
  Pass**; **no work package is authorized**, and this decision authorizes none.
- **Human-Maintainer authorization:** 2026-09-05, following the Nova adjudication of
  the CDS Step-9 R1/R2 decision package — **OD-6A**
- **Architecture record:** none. **DEC-S-134 is deliberately not an architecture
  dependency of ADR-0005**: it is a semantic and accessibility-obligation decision,
  not representation or identity architecture — the same boundary DEC-S-129 holds
  against ADR-0004.

### Decision

1. **Model B is adopted:** an **admission rule** is decided; **the concrete role
   vocabulary is not.**

2. **The concrete visual Core role vocabulary is OPEN.** No role identifier is
   created, adopted, reserved, or recommended by this decision.

3. **A visual semantic role enters CDS Core only on demonstrated cross-consumer
   need.** A need evidenced by one consumer is a consumer-local concern until it is
   shown to be shared (PN-2, IG-3).

4. **Requirement classification precedes design.** A candidate role is classified
   under the registered requirement classification model before any role is
   designed, named, or authored.

5. **Every admitted role satisfies SR-1 … SR-12 from the moment it exists.** A role
   whose obligations are undeclared is **inadmissible, not provisional** — an
   accessibility obligation attaches to a role as soon as the role exists.

6. **The role classification is closed and unchanged.** The registered semantic role
   classes established by the CDS-WP-019 family architectures and consolidated by
   the
   [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
   — for **VF-1**, **VF-2**, **VF-3**, **VF-5** and **VF-6**, together with the two
   cross-family role sets — stand as they are. **A future vocabulary populates
   these classes and adds none**, and **this decision adds no class.**

7. **`CDS-WP-020A` may not invent, adopt, reserve, or recommend a CDS Core role
   identifier.** A concrete vocabulary requires its own separately authorized
   decision, taken under this rule.

8. **`selected` is not a CDS Core role today.**

9. **`active` is not a CDS Core role today.**

10. **`current` is not a CDS Core role today.**

11. **Clauses 8 to 10 are not a permanent prohibition.** They record that **no
    current cross-consumer authority supports admitting them into CDS Core**, not
    that they may never be admitted. **IS-1 and IS-5 already bind whatever a
    consumer builds** — such a state must be programmatically determinable and must
    never be conveyed by colour or position alone — so leaving them out of Core
    removes no protection. **Their future distinctness remains coupled to a
    separately authorized concrete vocabulary decision**, and deciding the count now
    would decide the vocabulary by implication.

12. **OD-6A is POLICY ANSWERED; the concrete role vocabulary REMAINS OPEN.** The
    register models the vocabulary itself as part of OD-6A, so **OD-6A is not fully
    resolved by this decision.**

13. **VP-6 remains UNSATISFIED for every family.** VP-6 requires that every role a
    value will serve **declares its obligations**. **A policy is not an authored
    role with SR-1 … SR-12 declarations**, and no role exists to declare anything.

14. **This decision creates no role identifier, no role binding, no value, no named
    extension point, and no status-to-visual binding.** **SR-10 is unchanged: no
    role is a named extension point today**, and the status-to-visual binding
    remains CDS-WP-023's, gated by CDS-WP-024 and CDS-WP-025.

### Rationale

A concrete vocabulary was tested against the registered Layer-3 consumer anchors
and could not be supported by them. **CR-002** defines a reconciliation flow and
names no role. **CR-006** anchors the Semantic Status foundation and the rule that
colour is never the sole carrier — and **VF-I-6** forbids a visual role from
replacing a status axis, so it cannot be read as demanding visual roles.
**CR-023** requires tolerance of variable text length, which is an obligation
(SR-8), not a role. Only **CR-021** is role-shaped, and the focus role set it
anchors may not be defined *"before the values it would be built from exist."*
**VF-3, VF-5, VF-6 and VF-7 carry no consumer demand evidence at all.**

Inventing a vocabulary against that evidence base would have been **IG-2**,
**IG-3**, **RISK-021** and **RISK-026** at once, and every invented role would have
carried an accessibility obligation from the moment it existed. The honest
instrument was therefore a gate, not a list.

Clauses 8 to 11 answer **IS-5**, which explicitly routed the question of whether
*selected*, *active* and *current* are distinct roles to OD-6. The answer is given
as a **disposition under the admission rule** rather than as a count, because a
count is a vocabulary statement and would have decided by implication precisely
what Model B declines to decide.

### Consequences

- The
  [Visual Semantic Token Foundation](../architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
  records the admission rule and the IS-5 disposition; the closed role
  classification is unchanged.
- **`OD-6A` is policy-answered with the concrete vocabulary open**, reconciled in
  the **non-normative**
  [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
  register.
- **VP-6 stays UNSATISFIED**, so **no visual value may be selected** against a role
  that does not exist.
- **No schema, validator, test, or fixture is changed.**

### Boundary

This decision fixes an **admission gate**, not a vocabulary. It creates no role, no
role identifier, no binding, and no value. It awards no maturity, no Candidate, no
Stable, no evidence, no admission, no claim, no conformance, no Product Profile, no
pilot, no licence, no release, no tag, and no publication authority, and **it
activates no work package**. **VF-1 … VF-9 stay `Proposed`; visual values stay 0;
visual source sets stay 0; Stable stays `No`.**

---

## DEC-S-135 — Theme Sequencing Before Context-Sensitive Value Selection

- **Status:** Accepted — **effective at the Human-Maintainer exact integration
  commit `2cb244e889c1a6b5a278afb233995a0379b5d9ef`** of the exact reviewed Working
  Tree object of the CDS Step-9 Decision Integration Pass, which followed a Fresh
  Independent Review and Nova integration adjudication. Before that commit this
  entry was uncommitted executor output prepared under an explicit Human-Maintainer
  authorization given on 2026-09-05 and changed **no** authoritative CDS state; no
  earlier wording conferred effectivity.
- **Date:** 2026-09-05
- **Type:** Visual identifier, scale ownership, role admission and theme sequencing
  decision
- **Work package:** — none. Prepared by the **CDS Step-9 Decision Integration
  Pass**; **no work package is authorized**, and this decision authorizes none.
- **Human-Maintainer authorization:** 2026-09-05, following the Nova adjudication of
  the CDS Step-9 R1/R2 decision package — **OD-7**
- **Architecture record:** none. **DEC-S-135 is deliberately not an architecture
  dependency of ADR-0005**: it is a sequencing and authority decision, not
  representation or identity architecture.

### Decision

1. **No semantic visual role carries a default alias to a reference primitive
   before CDS-WP-022 decides the Theme and Context Mechanism.**

2. **CDS-WP-022 precedes context-sensitive value selection.**

3. **This prohibits no context-independent work.** Clause 2 gates values and
   bindings, not structure.

4. **Context-independent work includes, in principle:** the identifier grammar; the
   scale ownership and topology rules; the role admission policy; family maturity
   governance; and **source-set structural identity**. Each is context-independent
   by **TC-1** (a role's identity is context-independent), **TC-2** (its meaning is
   context-independent), **T-8** and **N-6** (a context is a resolution input, never
   a path segment), and **RB-1** (a theme never adds, removes, or edits a reference
   token).

5. **`CDS-WP-022 BEFORE VALUE SELECTION` does not mean `CDS-WP-022 BEFORE EVERY
   SOURCE-STRUCTURE OR IDENTITY ACTIVITY`.** Declaring a source set's identity —
   its `sourceSetId`, `sourceRevision`, `layer` and provenance — is a structural
   act; what clause 2 gates is its **content**.

6. **A theme remains a Resolution Context and is not a sixth token-flow layer.**
   DEC-S-024 defines exactly five, and a context selects among approved values
   without ever creating one.

7. **`A THEME RE-BINDS; IT NEVER REDEFINES` is preserved** (T-1, VF-I-9), together
   with T-2 … T-10 and TC-1 … TC-7 unchanged. **TC-6 continues to bind
   independently of this decision**: the semantic layer presupposes no context count
   and no context set.

8. **This decision authorizes no work package.**

9. **CDS-WP-022 becomes the recommended and sequenced Step-10 candidate only.**

10. **`SEQUENCED NEXT ≠ AUTHORIZED`.** **CDS-WP-022 remains `Planned`, not active,
    and not authorized**, as do **`CDS-WP-020A`** and CDS-WP-021 … CDS-WP-053.
    Authorization is a separate, explicit Human-Maintainer act at **step 10**, and
    it has not occurred. **No work package is currently authorized.**

11. **OD-7 is ANSWERED by this decision** once effective.

### Rationale

**T-2** requires that every semantic role resolve in every supported context — and
**zero contexts are supported**, which makes the requirement vacuously satisfiable
and useless as a guide. No committed source permitted or forbade a default binding,
so the question was genuinely open.

Allowing a default binding now would have made that default *the light theme* by
implication and handed CDS-WP-022 a decision it exists to make: **TC-6 would be
satisfied in form and violated in substance.** A context-neutral binding carrying a
re-evaluation obligation was admissible only with a named enforcing owner, and the
Consumer Maintainer role is **unstaffed (FM-F-006)** against a Human Maintainer who
is already the bottleneck (RISK-029) — so in practice it degrades to the same
default.

Clauses 3 to 5 exist because the sequencing rule is easy to over-read. Colour
values and the light and dark token layering are the same decision seen from two
sides; **identity, topology and governance are not**, and idling them would have
cost the project four decidable questions for no governance benefit. The asymmetry
is real rather than convenient: a populated colour reference source set **is**
value selection, while a spacing step is never re-bound by a theme (RB-1).

The evidence consequence is decisive. A value selected before the context model and
re-selected after it produces a new source revision, and **a new revision inherits
no evidence and no admission** (AF-2, RV-4, DEC-S-126, DEC-S-131 clause 10). The
rework would discard its own evidence.

### Consequences

- The
  [Visual Foundation Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
  records the sequencing rule and the no-default-binding rule; **T-1 … T-10 are
  unchanged** and the theme mechanism remains CDS-WP-022's, undecided.
- **`OD-7` is answered**, reconciled in the **non-normative**
  [Visual Token Foundation Open Decisions](../roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
  register.
- **CDS-WP-022 is the recommended Step-10 candidate and is not authorized.** The
  [Post-Candidate Development Roadmap](../roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md)
  records the recommendation as a plan, never as permission.
- **No schema, validator, test, or fixture is changed.**

### Boundary

This decision fixes an **ordering rule and a prohibition**, not an authorization.
It selects no value, creates no role, no binding, no identifier, and no source set.
It awards no maturity, no Candidate, no Stable, no evidence, no admission, no
claim, no conformance, no Product Profile, no pilot, no licence, no release, no
tag, and no publication authority, and **it activates no work package**.
**VF-1 … VF-9 stay `Proposed`; visual values stay 0; visual source sets stay 0;
Stable stays `No`.**
