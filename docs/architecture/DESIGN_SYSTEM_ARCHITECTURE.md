# Design System Architecture

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-005 — Design System Architecture
- **Date:** 2026-07-16
- **Status:** **Normative** for the logical architecture

## Purpose and authority

This document is the **normative source for the CDS logical architecture**. It
defines what layers exist, what each owns, how they may depend on one another,
and which invariants hold across the system.

It is the architecture entry point. The specialised documents listed under
[Related documents](#related-documents) hold the detail; this document defines
the frame and must not duplicate them.

### What this architecture is

A **logical** architecture. It describes structure, responsibility, authority,
and flow.

### What this architecture is not

It selects **no technology and no design**. Specifically, it does not choose a
repository topology, design tool, token format, naming convention, component
framework, programming language, build system, documentation platform, package
manager, licence, or any colour, typography, icon, logo, or component
(DEC-S-032).

Where a decision is not yet possible, it is recorded as a deferred decision
rather than assumed.

Scope authority remains [Concept and Scope](../governance/CONCEPT_AND_SCOPE.md).
This document is subordinate to it.

## Architecture objectives

1. Make the normative source of truth unambiguous and tool-independent
   (DEC-S-004, RISK-004).
2. Let design, code, documentation, and evidence converge without forcing them
   into one artifact (RISK-005).
3. Permit controlled product individuality without fragmentation (RISK-008,
   RISK-027).
4. Reconcile with product-local design decisions that already exist, rather than
   overwrite them (DEC-S-026, RISK-022).
5. Keep operational patterns useful without letting them define the universal
   foundation (DEC-S-027, RISK-016, RISK-023).
6. Protect status truthfulness architecturally, not by convention (DEC-S-028).
7. Support offline and self-hosted consumption as a structural property, not an
   afterthought (DEC-S-006, DEC-S-030).
8. Keep every artifact traceable to a source revision (DEC-S-031).
9. Stay affordable for the actual maintainer capacity (RISK-026).

## Quality attributes

| Attribute | Architectural meaning |
| --- | --- |
| **Truthfulness** | The system cannot make an honest state look better than it is. Status axes stay separate; unknown never reads as healthy. |
| **Reviewability** | Every normative statement is human-readable, versioned, and diffable. |
| **Portability** | No proprietary tool sits in the source-of-truth path. |
| **Reproducibility** | The same source revision plus the same transformation yields the same artifact. |
| **Traceability** | Every generated artifact identifies its source and transformation revision. |
| **Governability** | Variation happens through named extension points, not ad hoc. |
| **Offline capability** | Consumption requires no mandatory external runtime service. |
| **Maintainability** | The architecture is no larger than the capacity that must run it. |
| **Accessibility readiness** | The structure cannot prevent a later accessibility target from being met. No level is claimed here. |

## The eight-layer model

*(Normative, DEC-S-021)*

The model is **logical**. It maps to no directory, repository, package, team, or
tool.

| # | Layer | Owns |
| --- | --- | --- |
| **1** | **Strategy and Governance** | Mission, scope, design principles, brand governance, decision authority, versioning, contribution, maturity, adoption, conformance, change control. |
| **2** | **Brand and Identity** | Masterbrand rules, product-family relationship, brand roles, product identity profiles, verbal identity, logos and brand assets. |
| **3** | **Foundations and Tokens** | Colour, typography, space and size, grid and layout, shape, elevation, motion, iconography, design tokens, theme mechanisms, semantic status foundations. |
| **4** | **Components** | Component contracts, anatomy, states, variants, content rules, accessibility behavior, interaction behavior, component evidence. |
| **5** | **Patterns and Experiences** | Recurring task flows, navigation, setup, feedback, safe actions, status communication, complex data, operations-oriented patterns, domain pattern families. |
| **6** | **Channels and Communication** | Product UI, repository presentation, documentation, PDF and reports, presentations, diagrams, data visualization, release materials, selected communication materials. |
| **7** | **Distribution and Enablement** | Consumable artifacts, local use, offline availability, transformation, distribution, consumer integration, migration guidance, developer and author enablement. |
| **8** | **Evidence and Quality** | Traceability, provenance, accessibility evidence, validation evidence, visual or render evidence, consumer adoption evidence, migration evidence, deviations, quality gates. |

### Layer responsibilities in this work package

CDS-WP-005 defines each layer's **position and responsibility**. It does not
populate any layer.

- **Layer 1** — only the placement of governance topics. The concrete
  governance, versioning, contribution, and conformance rules are **CDS-WP-006**.
- **Layer 2** — only the system position. **No brand decision and no asset.**
- **Layer 3** — only the token flow and theme mechanism as structure. **No values,
  no format.**
- **Layer 4** — only that components are contract-bearing. **No component is
  specified.**
- **Layer 5** — only the pattern structure and the domain-family boundary.
- **Layer 6** — only channel classes and their transformation boundary.
- **Layer 7** — only artifact families and distribution properties. **No package
  manager, repository, or build decision.**
- **Layer 8** — only the evidence and traceability flow.

## Allowed dependencies

*(Normative)*

Dependency direction is **downward-to-upward only**: a layer may depend on the
layers above it in the table, never below.

| Layer | May depend on |
| --- | --- |
| 1 Strategy and Governance | — (depends on nothing) |
| 2 Brand and Identity | 1 |
| 3 Foundations and Tokens | 1, 2 |
| 4 Components | 1, 2, 3 |
| 5 Patterns and Experiences | 1, 2, 3, 4 |
| 6 Channels and Communication | 1, 2, 3, 4, 5 |
| 7 Distribution and Enablement | 1–6 |
| 8 Evidence and Quality | 1–7 (observes all; commands none) |

## Prohibited dependency directions

*(Normative — these are the load-bearing rules)*

1. **No upward dependency.** Foundations must not depend on components;
   components must not depend on patterns; patterns must not depend on channels.
   A lower-numbered layer never learns about a higher-numbered one.
2. **No component-specific foundation.** A token must not exist because one
   component wants it. Semantics precede components.
3. **No channel-specific semantics.** A channel may transform presentation; it
   must not redefine meaning (DEC-S-029).
4. **No domain family in the universal foundation.** Operations patterns must not
   push requirements down into Layers 3 or 4 without multi-consumer evidence
   (DEC-S-027, RISK-023).
5. **No consumer-driven core change.** A Product Profile must not reach into the
   core to redefine it; it uses approved extension points only (DEC-S-025).
6. **No evidence-driven mutation.** Layer 8 records reality. It never silently
   changes a normative source; it triggers a controlled decision instead.
7. **No distribution-driven semantics.** A packaging or delivery convenience must
   not shape what something means.
8. **No tool-driven authority.** An authoring or design tool must not sit in the
   source-of-truth path (DEC-S-004, DEC-S-022).

## Architecture invariants

*(Normative — each is validated in CDS-WP-005 and must hold thereafter)*

| # | Invariant |
| --- | --- |
| 1 | Generated is not normative. |
| 2 | Research is not normative. |
| 3 | Example is not normative. |
| 4 | Design-tool state is not independently normative. |
| 5 | Consumer-local state is not automatically CDS. |
| 6 | Latest edit does not determine authority. |
| 7 | **Unknown is not Healthy.** |
| 8 | **Stale is not Current.** |
| 9 | **Unverified is not Verified.** |
| 10 | A Product Profile cannot weaken shared semantics or accessibility. |
| 11 | A Domain Pattern Family does not automatically become universal. |
| 12 | Distribution requires no mandatory external runtime service. |
| 13 | Channel-specific rendering does not permit semantic divergence. |
| 14 | Existing products are reconciled, not overwritten. |
| 15 | Adoption claims require revision-bound evidence. |
| 16 | The architecture does not select final tools, formats, or repository topology. |

Invariants 7–9 exist because the strongest multi-consumer evidence in CDS-WP-004
was status semantics: all three consumers document graded status, and two
independently require that unknown must never read as healthy (CR-006, CR-007).
This is architecture, not styling — see
[Evidence, Traceability and Status Semantics](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md).

## Relationship to consumer requirements

All 40 registered consumer requirements (CR-001 … CR-040) are mapped to this
architecture in
[Architecture Requirements Traceability](ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md).

Mapping records an **architectural response**, never an approval. A requirement
classified `Shared CDS Candidate` remains a candidate (DEC-S-014); the
architecture positions it, it does not accept it.

Two consumer facts shaped this architecture directly:

1. **Consumers already hold product-local design decisions and token sets**
   (CR-002, CR-037). CDS arrives after them. The architecture therefore contains
   a reconciliation flow, not an adoption assumption (DEC-S-026).
2. **The consumer evidence is operations-shaped** — all three reviewed consumers
   are infrastructure products. The architecture therefore isolates operations
   patterns as a domain family rather than promoting them to the universal
   foundation (DEC-S-027).

## Relationship to CDS-WP-006 and CDS-WP-007

This architecture stops precisely where policy begins.

**Deferred to CDS-WP-006 — Governance, Versioning, and Contribution Model:**

- concrete governance roles and risk ownership,
- maturity states and their criteria,
- the versioning and compatibility model,
- deprecation policy,
- contribution and acceptance process,
- exception governance and expiry,
- Product Profile governance and approval,
- conformance and adoption claim rules,
- the detailed conflict-resolution authority (see
  [Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)),
- licensing and publication decision model.

**Deferred to CDS-WP-007 — Accessibility and Inclusive Design Policy:**

- the accessibility target CDS commits to,
- the evidence method that substantiates it,
- keyboard, focus, and motion requirements as policy.

**Accessibility in this architecture is a constraint, not a claim.** The
structure must not prevent a later target from being met — a Product Profile
cannot weaken accessibility (invariant 10), colour cannot be the sole carrier of
meaning, and component contracts carry accessibility behavior. **No conformance
level is chosen and nothing is certified here** (CR-024).

This ordering carries a real cost, recorded as RISK-028: architecture decided
before the accessibility policy may constrain that policy or make it expensive.

## Deferred technical decisions

*(Deliberately open — DEC-S-032)*

Repository topology · design tool · token format · token naming convention ·
component framework · programming language · build system · documentation
platform · package manager · distribution service · metadata structure · file
formats · licence · public release · maturity model · versioning scheme ·
accessibility conformance level · concrete status taxonomy and naming · concrete
colours, typography, icons, logos, components, and token values.

The architecture is designed to survive any reasonable choice among these. If a
later choice cannot satisfy an invariant above, the choice is wrong — not the
invariant.

## Change control

*(Normative)*

This document is normative. Changes require an authorized CDS work package, a
corresponding entry in the
[Decision Index](../decisions/DECISION_INDEX.md) where a registered decision
changes, consistency updates across the dependent architecture documents, and
Human Maintainer approval.

The architecture is not extended implicitly — not by a Skill, not by a consumer
request, not by an implementation convenience, and not by a generated artifact.

## Related documents

| Topic | Document |
| --- | --- |
| Artifact classes, authority, conflicts | [Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md) |
| Token layers and theming | [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md) |
| Profiles, extensions, domain families | [Product Profile and Extension Model](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) |
| Artifact families, channels, distribution | [Artifact Distribution and Channel Model](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) |
| Consumer contracts and reconciliation | [Consumer Contract and Reconciliation Model](CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md) |
| Evidence flow and status semantics | [Evidence, Traceability and Status Semantics](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) |
| Requirement coverage | [Architecture Requirements Traceability](ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md) |
| Normative scope | [Concept and Scope](../governance/CONCEPT_AND_SCOPE.md) |
| Decisions | [Decision Index](../decisions/DECISION_INDEX.md) |
| Risks | [Risk Register](../risks/RISK_REGISTER.md) |
