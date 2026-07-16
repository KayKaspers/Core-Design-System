# Consumer Requirements Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract
- **Evidence date:** 2026-07-15
- **Status:** Normative for the **classification** of consumer requirements

## Purpose and normative status

This document registers the requirements derived from committed consumer
documentation, and classifies each one.

**What is normative:** the register itself, the classification of each
requirement, and the rules below.

**What is explicitly not normative:** no requirement here is an accepted CDS
standard. Classification as a `Shared CDS Candidate` records a candidacy, not an
approval (DEC-S-014). Nothing here authorizes visual design, tokens, components,
technology selection, or implementation (DEC-S-020).

Scope authority remains [Concept and Scope](CONCEPT_AND_SCOPE.md); the
per-area split remains the [Scope Boundary Matrix](SCOPE_BOUNDARY_MATRIX.md).

## Methodology

1. Three consumer repositories were verified and read **read-only**, bound to
   their committed HEAD revisions (DEC-S-013).
2. Only permitted documentation areas were read. No product code, secrets, logs,
   or data.
3. Requirements were derived from committed statements, not from memory,
   assumption, or earlier sessions.
4. Each requirement was classified, given an evidence status and strength, a
   pilot priority, an ownership boundary, and a validation method.
5. Counts were derived from the register and independently re-counted.

Evidence sources: [Consumer Evidence Register](../research/CONSUMER_EVIDENCE_REGISTER.md).

### What this evidence is not

**Committed documentation is not user research.** No interviews, observation,
usability testing, or accessibility testing took place in this work package, and
none is claimed. Documentation evidences an *intent* or an *implemented
behavior* — it does not evidence that the resulting experience works for real
people (RISK-017).

## Requirement classifications

| Classification | Meaning |
| --- | --- |
| **Shared CDS Candidate** | Demonstrably relevant to several consumers, or generalizable with a documented rationale. **Not yet an approved CDS standard.** |
| **CoreOps Pilot Requirement** | Needed for the bounded CoreOps pilot. May later become a Shared CDS Candidate, but need not. |
| **Product-local Requirement** | Stays with the consumer project; not CDS-owned. |
| **Deferred Requirement** | Relevant, but outside the first pilot scope or only assessable after architecture, governance, or foundation decisions. |
| **Out of CDS Scope** | Permanently outside CDS responsibility per the Scope Boundary Matrix. |

## Evidence status

`Confirmed by committed evidence` · `Repeated across consumers` ·
`Inferred – Human validation required` · `Deferred – insufficient evidence` ·
`Rejected as CDS requirement`

## Evidence strength

`Explicit committed requirement` · `Repeated committed requirement` ·
`Documented implemented behavior` · `Documented planned capability` ·
`Inferred requirement requiring Human Maintainer validation` · `Context only` ·
`Not usable as requirement evidence`

## Pilot priority

`Must` · `Should` · `Could` · `Not in pilot`

Priority applies **only to the bounded CoreOps pilot**. It is not a general
product priority and says nothing about long-term CDS importance.

---

## Requirement register — definition

Consumers: `CO` CoreOps · `SP` SpeakCore · `CC` CastCore.
Domains per DEC-S-007: `Brand` · `Experience` · `Foundations` · `Components` ·
`Channels` · `Governance`.

| ID | Title | Requirement statement | Consumers | Domain | Cross-cutting |
| --- | --- | --- | --- | --- | --- |
| CR-001 | Core product-family recognition | Products must be recognizable as members of the Core family while retaining controlled individuality. | CO, SP, CC | Brand | Maintainability |
| CR-002 | Existing product-local design systems | Consumers already hold product-local design decisions and token sets; CDS must reconcile with them rather than assume a greenfield. | SP, CC | Foundations | Maintainability, provenance |
| CR-003 | Application shell and navigation | A consistent application shell with global and local navigation, page titling, and orientation. | CO | Experience | Accessibility |
| CR-004 | Multi-viewport behavior | Interfaces must remain usable across viewport situations, including core functions on small screens. | CO, CC | Experience | Accessibility |
| CR-005 | Dense operations overview | A dense operations overview presenting prioritized status without losing scanability. | CO, SP, CC | Experience | Accessibility |
| CR-006 | Semantic status representation | Health, severity, and alert states must be semantic, never colour-only, and always carry text or icon. | CO, SP, CC | Foundations | Accessibility, inclusive design |
| CR-007 | Unknown is not healthy | Missing, stale, or unknown data must never be presented as healthy. Unknown is a distinct state. | CO, CC | Experience | Quality evidence |
| CR-008 | Inventory and dense data | Inventory, table, and list presentation with filtering, sorting, and a defined empty state. | CO, SP, CC | Components | Accessibility |
| CR-009 | Topology and relationship views | Representation of topology, relationships, and dependency graphs. | CO | Experience | Accessibility |
| CR-010 | Risk-tiered actions | Actions must be distinguishable by risk tier: primary, secondary, and dangerous. | CO, SP | Components | Security-aware design |
| CR-011 | Preview before execute | Risk-bearing operations must offer an understandable preview or plan before execution. | CO, CC | Experience | Security-aware design |
| CR-012 | Confirmation and cancel path | Destructive actions require deliberate confirmation and an unambiguous cancel path. | CO, SP, CC | Components | Security-aware design |
| CR-013 | No misleading success | Success must not be indicated where it is not established. | CO, CC | Experience | Quality evidence |
| CR-014 | Action auditability | Actions and their outcomes must be traceable in the interface, not only in backend logs. | CO | Experience | Quality evidence, security-aware design |
| CR-015 | Complete system state set | A defined, consistent state set: loading, empty, success, warning, critical, error, offline, degraded, permission denied, unavailable capability. | CO, SP, CC | Components | Accessibility |
| CR-016 | Capability and degraded visibility | The interface must show which capabilities and support level actually apply, including restricted and degraded operation. | CO, CC | Experience | Security-aware design |
| CR-017 | Setup and preflight check | Guided setup with an environment or system check whose result is presented as a graded status. | CO, SP, CC | Experience | Accessibility |
| CR-018 | Simple and expert mode | A reduced mode hiding risk options, and an expert mode exposing detail and overrides. | CO, SP, CC | Experience | Inclusive design |
| CR-019 | Contextual help | Context-bound help and guidance available at the point of use. | CO, CC | Channels | Inclusive design |
| CR-020 | Plain-language errors | Errors must be explained in plain language alongside, not instead of, technical detail. | CO, CC | Experience | Inclusive design, accessibility |
| CR-021 | Keyboard operability and focus | Keyboard operability with visible focus states and sufficient contrast. | SP | Foundations | Accessibility |
| CR-022 | Motion restraint | Restrained animation, honouring reduced-motion preferences. | SP | Foundations | Accessibility |
| CR-023 | DE/EN and flexible text | German and English as product-facing languages, with layouts tolerating variable text length. | CO, CC | Foundations | Localization |
| CR-024 | Accessibility target undefined | The accessibility level CDS commits to, and its evidence method, are undefined and must be decided. | CO, SP | Governance | Accessibility, quality evidence |
| CR-025 | Light and dark themes | Support for light and dark presentation. | CO, SP | Foundations | Accessibility |
| CR-026 | Repository presentation | Standards for repository and GitHub-facing presentation. | CC | Channels | Maintainability |
| CR-027 | Documentation standards | Documentation standards including DE/EN parity and staleness control. | CO, CC | Channels | Localization, quality evidence |
| CR-028 | PDF and report output | Standards for PDF reports and exported documents. | CO | Channels | Accessibility |
| CR-029 | Diagram standards | Standards for diagrams. | CO | Channels | Accessibility |
| CR-030 | Presentation standards | Standards for presentations. | — | Channels | Accessibility |
| CR-031 | No mandatory external runtime | Consumer artifacts must not require external runtime services; assets must be locally servable. | CO, SP, CC | Foundations | Offline and self-hosted use |
| CR-032 | Offline and degraded states | Offline, restricted, air-gapped, and degraded conditions must be representable states. | CO, CC | Experience | Offline and self-hosted use |
| CR-033 | Shared terminology | Design, code, and documentation must use one governed vocabulary. | CO | Governance | Design-code-documentation alignment |
| CR-034 | Versioned foundations and traceable adoption | Foundations must be versioned, and adoption traceable to a specific version. | CO | Governance | Quality evidence, provenance |
| CR-035 | Product business logic and domain semantics | Business logic, domain data models, and domain semantics. | CO, SP, CC | — | — |
| CR-036 | Backend, infrastructure, security architecture | Backend, deployment, infrastructure, and security architecture. | CO, SP, CC | — | — |
| CR-037 | Product-local brand expression | Product-local style direction, palette values, and typography choices. | SP, CC | Brand | — |
| CR-038 | Product-specific domain views | Domain-specific views such as process supervision or media-pipeline diagnostics. | SP, CC | — | — |
| CR-039 | Recovery mode interface | A reduced emergency interface remaining available during recovery. | CO | Experience | Security-aware design |
| CR-040 | API and interface parity | The interface must not rely on privileged internal shortcuts unavailable to API consumers. | CO | Governance | Maintainability |

## Requirement register — classification and governance

| ID | Classification | Evidence status | Evidence strength | Priority | Ownership boundary | Validation method | Follow-up | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR-001 | Shared CDS Candidate | Inferred – Human validation required | Inferred requirement requiring Human Maintainer validation | Should | Shared or contract-controlled | Human Maintainer decision on family expression | CDS-WP-005 | Open |
| CR-002 | Shared CDS Candidate | Repeated across consumers | Explicit committed requirement | Should | Shared or contract-controlled | Reconciliation review against product-local token sets | CDS-WP-005 | Open |
| CR-003 | CoreOps Pilot Requirement | Confirmed by committed evidence | Explicit committed requirement | Must | Shared or contract-controlled | Pilot Group A scenario evidence | CDS-WP-005 | Open |
| CR-004 | Shared CDS Candidate | Repeated across consumers | Documented implemented behavior | Should | Shared or contract-controlled | Pilot Group A scenario evidence | CDS-WP-005 | Open |
| CR-005 | Shared CDS Candidate | Repeated across consumers | Documented implemented behavior | Must | Shared or contract-controlled | Pilot Group B scenario evidence | CDS-WP-005 | Open |
| CR-006 | Shared CDS Candidate | Repeated across consumers | Repeated committed requirement | Must | CDS-owned candidate | Pilot Group B and D evidence; non-colour check | CDS-WP-005 | Open |
| CR-007 | Shared CDS Candidate | Repeated across consumers | Explicit committed requirement | Must | CDS-owned candidate | Pilot Group B and D state coverage | CDS-WP-005 | Open |
| CR-008 | Shared CDS Candidate | Repeated across consumers | Documented implemented behavior | Must | CDS-owned candidate | Pilot Group C scenario evidence | CDS-WP-005 | Open |
| CR-009 | Deferred Requirement | Deferred – insufficient evidence | Documented planned capability | Not in pilot | Shared or contract-controlled | Deferred; needs multi-consumer demand | CDS-WP-005 | Deferred |
| CR-010 | Shared CDS Candidate | Repeated across consumers | Explicit committed requirement | Must | CDS-owned candidate | Pilot Group D scenario evidence | CDS-WP-005 | Open |
| CR-011 | Shared CDS Candidate | Repeated across consumers | Explicit committed requirement | Must | Shared or contract-controlled | Pilot Group D scenario evidence | CDS-WP-005 | Open |
| CR-012 | Shared CDS Candidate | Repeated across consumers | Repeated committed requirement | Must | CDS-owned candidate | Pilot Group D scenario evidence | CDS-WP-005 | Open |
| CR-013 | Shared CDS Candidate | Repeated across consumers | Explicit committed requirement | Must | CDS-owned candidate | Pilot Group D state coverage | CDS-WP-005 | Open |
| CR-014 | CoreOps Pilot Requirement | Confirmed by committed evidence | Explicit committed requirement | Should | Shared or contract-controlled | Pilot Group D evidence; generalizability review | CDS-WP-004 follow-up | Open |
| CR-015 | Shared CDS Candidate | Repeated across consumers | Repeated committed requirement | Must | CDS-owned candidate | Pilot Group D full state coverage | CDS-WP-005 | Open |
| CR-016 | Shared CDS Candidate | Repeated across consumers | Documented planned capability | Must | Shared or contract-controlled | Pilot Group D scenario evidence | CDS-WP-005 | Open |
| CR-017 | Shared CDS Candidate | Repeated across consumers | Documented implemented behavior | Should | Shared or contract-controlled | Pilot Group E scenario evidence | CDS-WP-005 | Open |
| CR-018 | Shared CDS Candidate | Repeated across consumers | Repeated committed requirement | Should | Shared or contract-controlled | Pilot Group A and E evidence | CDS-WP-005 | Open |
| CR-019 | Shared CDS Candidate | Repeated across consumers | Documented implemented behavior | Should | Shared or contract-controlled | Pilot Group E scenario evidence | CDS-WP-005 | Open |
| CR-020 | Shared CDS Candidate | Repeated across consumers | Documented implemented behavior | Must | Shared or contract-controlled | Pilot Group D and E evidence | CDS-WP-005 | Open |
| CR-021 | Shared CDS Candidate | Confirmed by committed evidence | Explicit committed requirement | Must | CDS-owned candidate | Pilot Group E keyboard and focus check | CDS-WP-007 | Open |
| CR-022 | Shared CDS Candidate | Confirmed by committed evidence | Explicit committed requirement | Should | CDS-owned candidate | Pilot Group E reduced-motion check | CDS-WP-007 | Open |
| CR-023 | Shared CDS Candidate | Repeated across consumers | Explicit committed requirement | Must | Shared or contract-controlled | Pilot Group E text-length and DE/EN check | CDS-WP-005 | Open |
| CR-024 | Deferred Requirement | Inferred – Human validation required | Inferred requirement requiring Human Maintainer validation | Should | CDS-owned candidate | Human Maintainer decision; no conformance claim meanwhile | CDS-WP-007 | Deferred |
| CR-025 | Shared CDS Candidate | Repeated across consumers | Documented planned capability | Could | Shared or contract-controlled | Deferred to foundations work | CDS-WP-005 | Open |
| CR-026 | Deferred Requirement | Deferred – insufficient evidence | Documented implemented behavior | Not in pilot | Shared or contract-controlled | Deferred; needs multi-consumer demand | CDS-WP-005 | Deferred |
| CR-027 | Deferred Requirement | Repeated across consumers | Explicit committed requirement | Not in pilot | Shared or contract-controlled | Deferred; strong evidence but outside pilot | CDS-WP-005 | Deferred |
| CR-028 | Deferred Requirement | Deferred – insufficient evidence | Context only | Not in pilot | Shared or contract-controlled | Deferred; demand unproven | CDS-WP-005 | Deferred |
| CR-029 | Deferred Requirement | Deferred – insufficient evidence | Context only | Not in pilot | Shared or contract-controlled | Deferred; demand unproven | CDS-WP-005 | Deferred |
| CR-030 | Deferred Requirement | Deferred – insufficient evidence | Not usable as requirement evidence | Not in pilot | Shared or contract-controlled | **No consumer evidence found.** Registered only to close the multi-channel set | CDS-WP-005 | Deferred |
| CR-031 | Shared CDS Candidate | Repeated across consumers | Explicit committed requirement | Must | CDS-owned candidate | Pilot artifact review against offline constraint | CDS-WP-005 | Open |
| CR-032 | Shared CDS Candidate | Repeated across consumers | Documented planned capability | Must | Shared or contract-controlled | Pilot Group D state coverage | CDS-WP-005 | Open |
| CR-033 | Shared CDS Candidate | Confirmed by committed evidence | Explicit committed requirement | Should | Shared or contract-controlled | Terminology review across pilot artifacts | CDS-WP-005 | Open |
| CR-034 | Shared CDS Candidate | Confirmed by committed evidence | Documented planned capability | Should | CDS-owned candidate | Version-bound traceability in pilot evidence | CDS-WP-006 | Open |
| CR-035 | Out of CDS Scope | Rejected as CDS requirement | Explicit committed requirement | Not in pilot | Consumer-owned | None — permanent non-goal | — | Closed |
| CR-036 | Out of CDS Scope | Rejected as CDS requirement | Explicit committed requirement | Not in pilot | Consumer-owned | None — permanent non-goal | — | Closed |
| CR-037 | Product-local Requirement | Confirmed by committed evidence | Explicit committed requirement | Not in pilot | Consumer-owned | Product-local; reconcile only via CR-002 | CDS-WP-005 | Open |
| CR-038 | Product-local Requirement | Confirmed by committed evidence | Documented implemented behavior | Not in pilot | Consumer-owned | Product-local unless generalized under DEC-S-016 | — | Open |
| CR-039 | Deferred Requirement | Deferred – insufficient evidence | Documented planned capability | Not in pilot | Shared or contract-controlled | Deferred; single-consumer need | CDS-WP-005 | Deferred |
| CR-040 | Deferred Requirement | Confirmed by committed evidence | Explicit committed requirement | Not in pilot | Shared or contract-controlled | Deferred; architectural constraint for CDS-WP-005 | CDS-WP-005 | Deferred |

---

## Counts

All counts are derived from the register above and were independently
re-counted. Every total resolves to **40**.

### By classification

| Classification | Count |
| --- | --- |
| Shared CDS Candidate | 25 |
| CoreOps Pilot Requirement | 2 |
| Product-local Requirement | 2 |
| Deferred Requirement | 9 |
| Out of CDS Scope | 2 |
| **Total** | **40** |

### By evidence status

| Evidence status | Count |
| --- | --- |
| Repeated across consumers | 21 |
| Confirmed by committed evidence | 9 |
| Deferred – insufficient evidence | 6 |
| Inferred – Human validation required | 2 |
| Rejected as CDS requirement | 2 |
| **Total** | **40** |

### By pilot priority

| Priority | Count |
| --- | --- |
| Must | 16 |
| Should | 11 |
| Could | 1 |
| Not in pilot | 12 |
| **Total** | **40** |

Pilot-relevant requirements (Must, Should, Could): **28**.

### By consumer

A requirement may cite several consumers, so these counts overlap by design and
do **not** sum to 40.

| Consumer | Requirements citing it |
| --- | --- |
| CoreOps | 33 |
| SpeakCore | 19 |
| CastCore | 25 |
| No consumer evidence | 1 (CR-030) |

## Key requirements by classification

**Strongest Shared CDS Candidates** — each evidenced across all three
consumers: CR-006 semantic status representation, CR-012 confirmation and cancel
path, CR-015 complete system state set, CR-018 simple and expert mode, CR-031 no
mandatory external runtime, CR-005 dense operations overview, CR-008 inventory
and dense data, CR-017 setup and preflight check, CR-001 product-family
recognition.

The single most convergent finding is **status semantics**: all three consumers
independently document graded status, and two of them independently document
that *unknown must not read as healthy* (CR-007). That is the clearest
multi-consumer signal in this work package.

**CoreOps Pilot Requirements:** CR-003 application shell and navigation, CR-014
action auditability. Both are currently single-consumer and must pass a
generalizability review before becoming shared (DEC-S-016).

**Product-local Requirements:** CR-037 product-local brand expression, CR-038
product-specific domain views. SpeakCore and CastCore hold their own style
direction, palette, and domain views. CDS must not absorb them (RISK-016).

**Deferred Requirements:** CR-009 topology, CR-024 accessibility target, CR-026
repository presentation, CR-027 documentation standards, CR-028 PDF and reports,
CR-029 diagrams, CR-030 presentations, CR-039 recovery mode, CR-040 API parity.

Note that CR-027 carries **strong** evidence (repeated across consumers, CI
enforced in one) yet is still deferred — because it lies outside the bounded
pilot, not because the evidence is weak. Deferral is a scope decision, not an
evidence verdict.

**Out of CDS Scope:** CR-035 business logic and domain semantics, CR-036
backend, infrastructure, and security architecture. Both are permanent non-goals
per the Scope Boundary Matrix. They are registered so the boundary is explicit
where consumer documentation is dense with them.

## Open Human-validation questions

1. **What accessibility level does CDS commit to, and how is it evidenced?**
   CoreOps names an accessibility baseline with no conformance level; CastCore
   documentation contains no accessibility evidence at all. CR-024. → CDS-WP-007
2. **How much product individuality is permitted?** SpeakCore and CastCore
   already hold product-local design decisions. CR-001, CR-002, CR-037. →
   CDS-WP-005
3. **Is CR-003 or CR-014 generalizable beyond CoreOps?** Both are single-consumer
   today. → generalizability review under DEC-S-016
4. **Do consumers need the deferred channels** (PDF, diagrams, presentations)
   enough to justify the scope? CR-028, CR-029, CR-030 have weak or no evidence.
5. **Should AirCore and further projects be reviewed** before foundations are
   frozen? Not authorized here. → Nova decision
6. **Does documentation evidence suffice**, or is real user validation required
   before Must requirements are accepted? RISK-017.

## Change control

This register is normative for classification. Changes require an authorized CDS
work package or an explicit Nova/Human Maintainer correction. A requirement does
not become an accepted CDS standard by appearing here; that requires the
generalizability review and acceptance path in DEC-S-016.

## Related documents

- [Consumer Requirements Traceability](CONSUMER_REQUIREMENTS_TRACEABILITY.md)
- [Consumer Evidence Register](../research/CONSUMER_EVIDENCE_REGISTER.md)
- [CoreOps Pilot Scope and Scenarios](COREOPS_PILOT_SCOPE_AND_SCENARIOS.md)
- [CoreOps Pilot Contract](COREOPS_PILOT_CONTRACT.md)
- [Consumer Validation Plan](CONSUMER_VALIDATION_PLAN.md)
- [Concept and Scope](CONCEPT_AND_SCOPE.md) — normative scope source
