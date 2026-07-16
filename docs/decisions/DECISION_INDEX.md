# Decision Index

This index records the strategic decisions of the Core Design System (CDS).

All decisions listed here define purpose, boundaries, scope, and authority.
They do **not** select tools, formats, frameworks, repository structures, or
any concrete visual or implementation technology.

Concrete implementation and visual decisions require separate, explicitly
authorized work packages.

## Register scope

- Decision range: DEC-S-001 … DEC-S-048
- Number of decisions: 48
- Decision record format: index entries only; no ADR files exist in this phase.

## Decision types

| Type | Range | Registered by | Character |
| --- | --- | --- | --- |
| Strategic foundation decision | DEC-S-001 … DEC-S-006 | CDS-WP-001 | Purpose, boundaries, and authority of the project. |
| Strategic scope decision | DEC-S-007 … DEC-S-012 | CDS-WP-002 | Scope classification, ownership, consumer relationships, and commitment limits. |
| Consumer and pilot scope decision | DEC-S-013 … DEC-S-020 | CDS-WP-004 | Evidence binding, requirement classification, pilot boundaries, and claim limits. |
| Logical architecture decision | DEC-S-021 … DEC-S-032 | CDS-WP-005 | Layers, authority, token flow, profiles, channels, distribution, traceability, status semantics. |
| Governance, lifecycle and publication decision | DEC-S-033 … DEC-S-048 | CDS-WP-006 | Roles, conflict resolution, maturity, versioning, contribution, exceptions, claims, risk ownership, publication, licensing, release control. |

None of these types is an implementation decision. Logical architecture decisions
define structure, responsibility, and flow — they select no technology, format,
tool, or visual design (DEC-S-032). Governance decisions define who decides and
under what conditions — they select no licence, publication state, technology, or
design.

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
