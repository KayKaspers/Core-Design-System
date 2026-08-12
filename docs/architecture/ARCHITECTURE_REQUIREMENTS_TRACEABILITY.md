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
model. **Retired by CDS-WP-007: no requirement carries this status (0 rows).**
CDS-WP-006 supplied the model.

`Deferred to CDS-WP-007` - needs the accessibility policy. **Retired by
CDS-WP-007: no requirement carries this status (0 rows).** The policy exists.

Both values are retained in this vocabulary for **historical readability** of
earlier revisions. **Neither may be assigned again** — a requirement needing
policy that does not exist must name the work package that will supply it.

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
| CR-021 | Shared CDS Candidate | 3 Foundations and Tokens | Policy now mandates keyboard operability, visible focus, and no keyboard trap as a contract area (DEC-S-055); WCAG 2.1.1, 2.1.2, 2.4.3, 2.4.7, 2.4.11 mapped with responsibility. | [A11y Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) | Component and pattern keyboard contracts; implementation evidence (AE-2, AE-3). Policy defines the duty; nothing is evidenced. | CDS-WP-008 | Partially addressed - later design decision required |
| CR-022 | Shared CDS Candidate | 3 Foundations and Tokens | Policy mandates reduced-motion support and forbids motion as sole meaning carrier; Layer 3 motion foundation confirmed. | [A11y Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) | Motion thresholds and the concrete mechanism; implementation evidence. | CDS-WP-008 | Partially addressed - later design decision required |
| CR-023 | Shared CDS Candidate | 3 Foundations and Tokens | Layer 3 foundations plus Layer 6 channel parity; layouts must tolerate variable text length. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Localization model; DE/EN parity mechanism. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-024 | Deferred Requirement | 1 Strategy and Governance | **Resolved at policy level: WCAG 2.2 Level AA for the applicable web scope** (DEC-S-049, DEC-S-060). Target, scope, responsibilities, evidence model (AE-0…AE-4), and gates are defined. | [A11y Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) | None at policy level. **The target is not conformance** — evidence remains absent (all artifacts AE-0); the support baseline A11Y-BL-001 is committed but is not evidence. | — | Addressed by architecture |
| CR-025 | Shared CDS Candidate | 3 Foundations and Tokens | Layer 3 theme mechanism; theming flows through semantic tokens, never raw values. | [Tokens](TOKEN_AND_THEME_ARCHITECTURE.md) | Whether theme is a profile or a semantic concern; the token layering it implies. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-026 | Deferred Requirement | 6 Channels and Communication | Registered as a channel class at Layer 6. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Whether demand justifies the scope. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-027 | Deferred Requirement | 6 Channels and Communication | Layer 6 documentation channel with DE/EN parity and staleness control as channel constraints. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Standards themselves; parity mechanism. Strong evidence but outside the pilot. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-028 | Deferred Requirement | 6 Channels and Communication | Registered as a channel class; paginated, non-interactive constraints stated - status must survive without hover, colour, or motion. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Whether demand justifies it. Evidence weak. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-029 | Deferred Requirement | 6 Channels and Communication | Registered as a channel class; structural meaning must survive export. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Whether demand justifies it. Evidence weak. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-030 | Deferred Requirement | 6 Channels and Communication | Registered as a channel class only, to close the multi-channel set. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | No consumer evidence exists. Demand entirely unestablished. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-031 | Shared CDS Candidate | 7 Distribution and Enablement | DEC-S-030 and invariant 12: no mandatory external runtime service; local assets; air-gap tolerance; distribution neutrality. | [Channels](ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) | Distribution technology (deliberately open). | CDS-WP-006 | Addressed by architecture |
| CR-032 | Shared CDS Candidate | 8 Evidence and Quality | Offline, degraded, and restricted are distinct states across the five axes; degraded stays distinguishable from unavailable. | [Evidence & Status](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) | Concrete state taxonomy. | CDS-WP-006 | Addressed by architecture |
| CR-033 | Shared CDS Candidate | 1 Strategy and Governance | Layer 1 governance; the semantic-first principle makes shared vocabulary an architectural property of the token flow. | [Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) | Glossary and terminology governance. | CDS-WP-006 | Partially addressed - later design decision required |
| CR-034 | Shared CDS Candidate | 1 Strategy and Governance | Versioning governance now defined: MAJOR.MINOR.PATCH, immutable release identity, seven maturity states, eight compatibility axes (DEC-S-035…DEC-S-039). Layer 8 traceability supplies the mechanism (DEC-S-031). | [Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md) | Concrete foundations and implementation. Governance exists; **no artifact is versioned, Candidate, or Stable**. | CDS-WP-008 | Partially addressed - later design decision required |
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

*(Reconciled by CDS-WP-007 — counts re-derived from the matrix above.)*

| Status | Count | Change |
| --- | --- | --- |
| Partially addressed - later design decision required | **27** | +3 (CR-021, CR-022, CR-034) |
| Addressed by architecture | **9** | +1 (CR-024) |
| Consumer-owned | 2 | — |
| Out of CDS scope | 2 | — |
| Deferred to CDS-WP-006 | **0** | −1 (CR-034 reconciled) |
| Deferred to CDS-WP-007 | **0** | −3 (CR-021, CR-022, CR-024 reconciled) |
| **Total** | **40** | — |

**No requirement is deferred to a policy work package any longer.** CDS-WP-006
supplied governance and CDS-WP-007 supplied the accessibility target, so the four
deferred requirements moved to their real state: three await *design and
evidence*, one is answered at policy level.

**This is not progress toward conformance.** CR-024 is `Addressed by
architecture` because the **target and policy exist** — not because anything was
tested. Every artifact remains AE-0.

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

**Only 9 of 40 requirements are fully addressed by architecture, and that is the
expected result.** An architecture that claimed to resolve most requirements
would be doing design work it is not authorized to do (DEC-S-020, DEC-S-032).

The 9 fully addressed requirements cluster tightly, and not by accident:

- **Status truthfulness** - CR-006, CR-007, CR-013, CR-015, CR-016, CR-032.
- **Offline capability** - CR-031.
- **Reconciliation** - CR-002.
- **Accessibility target** - CR-024 *(added by CDS-WP-007)*.

These are exactly the areas where the architecture or policy *itself* is the
answer: they are structural guarantees and governance decisions, not design
choices. Unknown-is-not-healthy cannot be delegated to a later styling decision;
offline capability cannot be retrofitted onto a distribution model that assumed a
service; and an accessibility target is a decision, not an implementation.

The 27 partially addressed requirements are positioned and await design and
evidence.

**Nothing is deferred to a policy work package any longer.** CDS-WP-006 supplied
governance and CDS-WP-007 supplied the accessibility target. What remains is
design, implementation, and evidence — not policy.

That shift is real but narrow: **the blocker moved from "against what?" to "show
it".** No artifact became more mature, and nothing was tested.

## Open architecture gaps

Requirements whose architectural answer is weakest, and why:

1. **CR-024 accessibility evidence** - *(reframed by CDS-WP-007)* the target is
   now decided: **WCAG 2.2 Level AA** for the applicable web scope (DEC-S-049,
   DEC-S-060). The gap is no longer the level — it is that **no artifact has been
   evaluated against it**. Every artifact is **AE-0**; the support baseline
   **A11Y-BL-001 is declared and committed** (CDS-WP-010) and is a test contract,
   not evidence (RISK-044, RISK-048). This still blocks the Stable gate, Product
   Profile approval, and the CoreOps pilot; only the *reason* changed.
2. **CR-030 presentations** - registered as a channel class with **no consumer
   evidence at all**. Structure without demand.
3. **CR-028, CR-029 PDF and diagrams** - weak consumer evidence; registered but
   unjustified.
4. **CR-003, CR-014** - single-consumer CoreOps requirements. The architecture
   positions them, but generalizability is untested (DEC-S-016).
5. **CR-005, CR-009** - operations patterns confirmed as a real consumer need,
   but modelled as a Domain Pattern Family precisely because generalizability is
   unproven (DEC-S-027, RISK-023).
6. **CR-034 versioning** - *(reframed by CDS-WP-007)* the traceability mechanism
   exists and CDS-WP-006 supplied the versioning and maturity model. What is
   missing is a **versioned artifact to apply it to** — the model has never been
   exercised, because nothing has reached Candidate.
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
