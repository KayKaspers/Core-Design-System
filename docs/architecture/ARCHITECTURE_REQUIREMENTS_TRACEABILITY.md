# Architecture Requirements Traceability

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-005 - Design System Architecture
- **Date:** 2026-07-16
- **Status:** **Normative** for architecture coverage

## Purpose

Every registered consumer requirement (CR-001 ... CR-040) is mapped here to the
CDS logical architecture, so that no requirement is silently lost and no deferred
requirement is presented as solved.

This matrix was **generated from the requirement register** rather than written by
hand, so requirement IDs cannot drift between the two documents.

## What a mapping means

A mapping records an **architectural response**, never an approval.

- `Shared CDS Candidate` remains a candidate (DEC-S-014). The architecture
  positions it; it does not accept it.
- `Addressed by architecture` means the architecture answers the requirement
  structurally - not that anything is designed, built, or validated.
- `Partially addressed` means the architecture positions it and a real design
  decision remains.
- Product-local and Out-of-Scope classifications are respected, not quietly
  absorbed.
- Pilot requirements do not become Shared CDS Standards by being mapped
  (DEC-S-016).

## Architecture status vocabulary

`Addressed by architecture` - the architecture answers it structurally.

`Partially addressed - later design decision required` - positioned, but a design
decision remains.

`Deferred to CDS-WP-006` - needs the governance, versioning, or contribution
model.

`Deferred to CDS-WP-007` - needs the accessibility policy.

`Consumer-owned` - belongs to the consumer project.

`Out of CDS scope` - permanent non-goal.

## Traceability matrix

| Requirement | Source classification | Architecture layer | Architecture response | Document | Remaining decision | Follow-up | Architecture status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR-001 | Shared CDS Candidate | 2 Brand and Identity | Layer 2 positions product identity profiles within brand governance; family expression is a Layer 2 concern, not a foundation concern. | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | Which brand expression, and how much identity a profile may carry. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-002 | Shared CDS Candidate | 3 Foundations and Tokens | Reconciliation flow defined: inventory, semantic mapping, conflict identification, classification, retention or migration. Consumer token sets are Consumer-local Artifacts (class 7), not overrides. | [Profiles](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) | Which decisions map, retain, or migrate - per consumer, later. | CDS-WP-006 | Addressed by architecture |
| CR-003 | CoreOps Pilot Requirement | 5 Patterns and Experiences | Layer 5 owns navigation and orientation patterns; the shell is a pattern, not a component or foundation. | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | The shell pattern itself; generalizability beyond CoreOps (DEC-S-016). | CDS-WP-006 | Partially addressed - later design decision required |
| CR-004 | Shared CDS Candidate | 5 Patterns and Experiences | Layer 5 pattern concern; channel constraints separated at Layer 6. | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | Viewport strategy and breakpoints. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-005 | Shared CDS Candidate | 5 Patterns and Experiences | Layer 5, modelled as a Domain Pattern Family (operations) above the universal foundation (DEC-S-027). | [Profiles](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) | The overview pattern; whether it generalizes beyond operational products. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-006 | Shared CDS Candidate | 3 Foundations and Tokens | Semantic status foundations at Layer 3; semantic-first principle forbids appearance-derived naming; colour never sole carrier; axes separated (DEC-S-028). | [Evidence & Status](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) | Concrete taxonomy and state names. | CDS-WP-007 | Addressed by architecture |
| CR-007 | Shared CDS Candidate | 8 Evidence and Quality | Architectural invariant 7 plus separated Knowledge Confidence and Freshness axes (DEC-S-028). Structurally impossible to merge unknown into healthy. | [Evidence & Status](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) | Minimum honest representation of unknown. | CDS-WP-006 | Addressed by architecture |
| CR-008 | Shared CDS Candidate | 4 Components | Layer 4 component contracts carry states, variants, and accessibility behavior; empty state is a contract state (CR-015). | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | The component contracts themselves. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-009 | Deferred Requirement | 5 Patterns and Experiences | Positioned as a Domain Pattern Family candidate; not universal foundation (DEC-S-027). | [Profiles](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) | Whether multi-consumer demand exists at all. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-010 | Shared CDS Candidate | 4 Components | Layer 4 contracts distinguish risk tier; Layer 3 supplies semantic (not colour) encoding. | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | Tier taxonomy and contracts. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-011 | Shared CDS Candidate | 5 Patterns and Experiences | Layer 5 safe-action pattern; preview is a pattern obligation preceding execution. | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | The preview pattern; CDS versus domain boundary of preview content. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-012 | Shared CDS Candidate | 4 Components | Layer 4 contract: confirmation and cancel are contract states, not styling. | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | What makes a confirmation deliberate rather than habitual. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-013 | Shared CDS Candidate | 8 Evidence and Quality | Invariant 9 (Unverified is not Verified) plus the Availability-of-Evidence axis; transformation may not collapse axes. | [Evidence & Status](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) | Representation of partial and unknown outcomes. | CDS-WP-006 | Addressed by architecture |
| CR-014 | CoreOps Pilot Requirement | 8 Evidence and Quality | Layer 8 traceability chain and Approval State identity; auditability is an evidence concern. | [Evidence & Status](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) | Whether it generalizes beyond CoreOps (DEC-S-016); surfacing model. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-015 | Shared CDS Candidate | 4 Components | Five separated status axes (DEC-S-028) span the full state set; Layer 4 contracts carry states. | [Evidence & Status](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) | Concrete taxonomy; resolution of combined states. | CDS-WP-007 | Addressed by architecture |
| CR-016 | Shared CDS Candidate | 8 Evidence and Quality | Invariant: degraded and unavailable stay distinguishable; capability visibility is a status-axis concern. | [Evidence & Status](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) | Capability representation. | CDS-WP-006 | Addressed by architecture |
| CR-017 | Shared CDS Candidate | 5 Patterns and Experiences | Layer 5 setup pattern; graded result governed by the status axes (never colour-only). | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | Whether setup is a CDS or a product pattern - all three consumers built their own. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-018 | Shared CDS Candidate | 5 Patterns and Experiences | Layer 5 pattern; mode must be programmatically determinable, not colour-signalled. | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | Whether mode is CDS, product, or both. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-019 | Shared CDS Candidate | 6 Channels and Communication | Layer 6 documentation channel; must degrade honestly offline (CR-031). | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Help delivery model. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-020 | Shared CDS Candidate | 5 Patterns and Experiences | Layer 5 and 6: plain language alongside, never instead of, technical detail. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Error content model; DE/EN parity. | CDS-WP-007 | Partially addressed - later design decision required |
| CR-021 | Shared CDS Candidate | 3 Foundations and Tokens | Architectural constraint: component contracts carry accessibility behavior; profiles may not weaken it (invariant 10). | [Evidence & Status](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) | The target level and evidence method are undefined (CR-024). | CDS-WP-007 | Deferred to CDS-WP-007 |
| CR-022 | Shared CDS Candidate | 3 Foundations and Tokens | Layer 3 motion foundation; reduced-motion is a foundation concern. | [Evidence & Status](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) | Motion policy and thresholds. | CDS-WP-007 | Deferred to CDS-WP-007 |
| CR-023 | Shared CDS Candidate | 3 Foundations and Tokens | Layer 3 foundations plus Layer 6 channel parity; layouts must tolerate variable text length. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Localization model; DE/EN parity mechanism. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-024 | Deferred Requirement | 1 Strategy and Governance | Layer 1 governance placement; architecture treats accessibility as a structural constraint without choosing a level. | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | The entire policy - target, method, evidence. | CDS-WP-007 | Deferred to CDS-WP-007 |
| CR-025 | Shared CDS Candidate | 3 Foundations and Tokens | Layer 3 theme mechanism; theming flows through semantic tokens, never raw values. | [Tokens](TOKEN_AND_THEME_ARCHITECTURE.md) | Whether theme is a profile or a semantic concern; the token layering it implies. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-026 | Deferred Requirement | 6 Channels and Communication | Registered as a channel class at Layer 6. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Whether demand justifies the scope. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-027 | Deferred Requirement | 6 Channels and Communication | Layer 6 documentation channel with DE/EN parity and staleness control as channel constraints. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Standards themselves; parity mechanism. Strong evidence but outside the pilot. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-028 | Deferred Requirement | 6 Channels and Communication | Registered as a channel class; paginated, non-interactive constraints stated - status must survive without hover, colour, or motion. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Whether demand justifies it. Evidence weak. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-029 | Deferred Requirement | 6 Channels and Communication | Registered as a channel class; structural meaning must survive export. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Whether demand justifies it. Evidence weak. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-030 | Deferred Requirement | 6 Channels and Communication | Registered as a channel class only, to close the multi-channel set. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | No consumer evidence exists. Demand entirely unestablished. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-031 | Shared CDS Candidate | 7 Distribution and Enablement | DEC-S-030 and invariant 12: no mandatory external runtime service; local assets; air-gap tolerance; distribution neutrality. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Distribution technology (deliberately open). | CDS-WP-006 | Addressed by architecture |
| CR-032 | Shared CDS Candidate | 8 Evidence and Quality | Offline, degraded, and restricted are distinct states across the five axes; degraded stays distinguishable from unavailable. | [Evidence & Status](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) | Concrete state taxonomy. | CDS-WP-006 | Addressed by architecture |
| CR-033 | Shared CDS Candidate | 1 Strategy and Governance | Layer 1 governance; the semantic-first principle makes shared vocabulary an architectural property of the token flow. | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | Glossary and terminology governance. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-034 | Shared CDS Candidate | 1 Strategy and Governance | Layer 8 traceability chain plus the required revision identities (DEC-S-031) supply the mechanism. | [Evidence & Status](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) | The versioning and maturity model itself. | CDS-WP-006 | Deferred to CDS-WP-006 |
| CR-035 | Out of CDS Scope | Not applicable | Permanent non-goal. Consumer-owned business logic and domain semantics. | - | None. The boundary is final. | - | Out of CDS scope |
| CR-036 | Out of CDS Scope | Not applicable | Permanent non-goal. Consumer-owned backend, infrastructure, and security architecture. | - | None. The boundary is final. | - | Out of CDS scope |
| CR-037 | Product-local Requirement | 2 Brand and Identity | Consumer-local Artifact (class 7). Not CDS, not an override, not a defect. Enters only via reconciliation. | [Profiles](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) | Whether any part becomes a Profile Candidate - later, per consumer. | CDS-WP-006 | Consumer-owned |
| CR-038 | Product-local Requirement | 5 Patterns and Experiences | Consumer Extension: product-specific, consumer-owned unless explicitly accepted (DEC-S-016). | [Profiles](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) | Whether any part generalizes. | - | Consumer-owned |
| CR-039 | Deferred Requirement | 5 Patterns and Experiences | Layer 5 pattern; relates to degraded and restricted operation states. | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | Single-consumer need; pattern undefined. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-040 | Deferred Requirement | 1 Strategy and Governance | Layer 1 governance constraint: reference implementations may not extend a norm; contracts bind all consumers equally. | [Authority](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md) | Parity enforcement mechanism. | CDS-WP-006 | Partially addressed - later design decision required |

## Counts

All counts are derived from the matrix above and were independently re-counted.
Every total resolves to **40**.

### By architecture status

| Status | Count |
| --- | --- |
| Partially addressed - later design decision required | 24 |
| Addressed by architecture | 8 |
| Deferred to CDS-WP-007 | 3 |
| Consumer-owned | 2 |
| Out of CDS scope | 2 |
| Deferred to CDS-WP-006 | 1 |
| **Total** | **40** |

### By architecture layer

| Layer | Count |
| --- | --- |
| 1 Strategy and Governance | 4 |
| 2 Brand and Identity | 2 |
| 3 Foundations and Tokens | 6 |
| 4 Components | 4 |
| 5 Patterns and Experiences | 10 |
| 6 Channels and Communication | 6 |
| 7 Distribution and Enablement | 1 |
| 8 Evidence and Quality | 5 |
| Not applicable (out of CDS scope) | 2 |
| **Total** | **40** |

## Reading the distribution honestly

**Only 8 of 40 requirements are fully addressed by architecture, and that is the
expected result.** An architecture that claimed to resolve most requirements
would be doing design work it is not authorized to do (DEC-S-020, DEC-S-032).

The 8 fully addressed requirements cluster tightly, and not by accident:

- **Status truthfulness** - CR-006, CR-007, CR-013, CR-015, CR-016, CR-032.
- **Offline capability** - CR-031.
- **Reconciliation** - CR-002.

These are exactly the areas where the architecture *itself* is the answer: they
are structural guarantees, not design choices. Unknown-is-not-healthy cannot be
delegated to a later styling decision, and offline capability cannot be retrofitted
onto a distribution model that assumed a service.

The 24 partially addressed requirements are positioned and await design. The 4
deferred ones await policy that does not exist yet. This is deferral, not
avoidance - each names its follow-up work package.

## Open architecture gaps

Requirements whose architectural answer is weakest, and why:

1. **CR-024 accessibility target** - the architecture treats accessibility as a
   constraint but **cannot choose a level**. Deferred to CDS-WP-007. This blocks
   CR-021 and CR-022 and a CoreOps pilot entry criterion, and it is the single
   most consequential gap (RISK-028).
2. **CR-030 presentations** - registered as a channel class with **no consumer
   evidence at all**. Structure without demand.
3. **CR-028, CR-029 PDF and diagrams** - weak consumer evidence; registered but
   unjustified.
4. **CR-003, CR-014** - single-consumer CoreOps requirements. The architecture
   positions them, but generalizability is untested (DEC-S-016).
5. **CR-005, CR-009** - operations patterns confirmed as a real consumer need,
   but modelled as a Domain Pattern Family precisely because generalizability is
   unproven (DEC-S-027, RISK-023).
6. **CR-034 versioning** - the traceability mechanism exists; the versioning and
   maturity model does not (CDS-WP-006).
7. **CR-017 setup** - all three consumers built their own. Whether this is a CDS
   pattern at all is unresolved.

## Limitations

- Mapping is to **architecture**, not to implementation or validation. No
  requirement is validated by appearing here.
- The underlying evidence is committed documentation only. No user research took
  place (RISK-017).
- Consumer requirements decay as consumer projects evolve (RISK-014).
- `Addressed by architecture` is the strongest claim available and still means
  only that the structure answers it.

## Related documents

- [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md)
- [Consumer Requirements Model](../governance/CONSUMER_REQUIREMENTS_MODEL.md)
- [Consumer Requirements Traceability](../governance/CONSUMER_REQUIREMENTS_TRACEABILITY.md)
- [Evidence, Traceability and Status Semantics](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md)
