# Risk Register

This register records the initial risks of the Core Design System (CDS) that
must be controlled from the start of the project.

## Register scope

- Risk range: RISK-001 … RISK-009
- Number of risks: 9
- Phase: Foundation / Pre-Design

Risks RISK-001 … RISK-005 were registered by CDS-WP-001. Risks
RISK-006 … RISK-009 were registered by CDS-WP-002 alongside the scope
registration.

### Provisional owner model

The owner role recorded for each risk is **provisional** until CDS-WP-006
establishes the governance, versioning, and contribution model. Owner roles
reflect the current authority model and are not a final governance assignment.

## Assessment scale

Qualitative values are used deliberately. No numeric probabilities are assigned,
because the project has no empirical basis for them in this phase.

| Value | Meaning |
| --- | --- |
| Low | Unlikely or limited effect under current conditions. |
| Medium | Plausible or noticeable effect under current conditions. |
| High | Likely or severe effect under current conditions. |

## Status values

| Status | Meaning |
| --- | --- |
| Open | Identified; mitigation not yet established. |
| Monitored | Mitigation direction defined; effect observed over time. |
| Mitigated | Mitigation established and effective. |
| Closed | No longer relevant. |

---

## RISK-001 — Uncontrolled scope expansion

- **Status:** Monitored
- **Owner role:** Nova
- **Initial likelihood:** High
- **Initial severity:** High

### Description

CDS may become too broad to deliver because it covers many products, channels,
and design disciplines.

### Impact

The project produces breadth without depth, no area reaches usable quality, and
no consumer can adopt the system. Delivery credibility erodes before the first
foundation is complete.

### Mitigation direction

Maintain a controlled work-package roadmap with explicit scope boundaries per
package. Distinguish long-term scope from currently authorized scope. Require
explicit authorization before new areas are opened.

---

## RISK-002 — CoreOps overfitting

- **Status:** Monitored
- **Owner role:** Nova
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

The first reference consumer may dominate the system and reduce its suitability
for other Core products.

### Impact

CDS becomes an implicit CoreOps design library. Later consumers require forks,
exceptions, or parallel systems, which defeats the Single Source of Truth
purpose.

### Mitigation direction

Treat CoreOps requirements as inputs rather than definitions (see DEC-S-002).
Collect requirements from further Core products before foundations are frozen.
Review generalization explicitly during architecture work.

The CoreOps pilot boundary registered in CDS-WP-002 sets the concrete
acceptance conditions for generalizing a CoreOps solution into CDS (see
DEC-S-011 and
[Concept and Scope](../governance/CONCEPT_AND_SCOPE.md)).

---

## RISK-003 — Premature design decisions

- **Status:** Monitored
- **Owner role:** Nova
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Visual or technical decisions may be made before strategy, requirements, and
governance are sufficiently defined.

### Impact

Decisions become difficult to justify or revise, consume effort that must later
be discarded, and constrain the system before its requirements are understood.

### Mitigation direction

Enforce the phase boundary defined in DEC-S-003. Maintain an explicit list of
intentionally open decisions. Treat any premature decision as a reportable
deviation.

---

## RISK-004 — Tool lock-in and source divergence

- **Status:** Monitored
- **Owner role:** Nova
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

A design tool or generated artifact may incorrectly become a competing source
of truth.

### Impact

Normative content becomes unreviewable, non-portable, and dependent on a
third-party product. Conflicting sources make it impossible to determine what
CDS actually specifies.

### Mitigation direction

Apply DEC-S-004 when evaluating tools. Maintain a documented separation between
normative sources and generated artifacts. Never treat generated output as
authoritative.

---

## RISK-005 — Design, code, and documentation drift

- **Status:** Monitored
- **Owner role:** Nova
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

Implemented products may diverge from normative CDS guidance over time.

### Impact

CDS documents an intent that no product actually follows. The system loses
authority and consumers stop treating it as normative.

### Mitigation direction

Plan for controlled convergence of design, code, and documentation. Establish
versioning, adoption levels, and review paths in the governance work package.
Use the pilot consumer to produce adoption evidence.

---

## RISK-006 — Ownership boundary ambiguity

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

CDS and consumer projects may both assume that the other side owns a required
decision, artifact, implementation, or maintenance obligation.

### Impact

Required work is never done because each side believes it belongs to the other.
Gaps surface late, during integration or after release, when they are most
expensive. Repeated ambiguity erodes trust between CDS and its consumers.

### Mitigation direction

Maintain the explicit per-area split in the
[Scope Boundary Matrix](../governance/SCOPE_BOUNDARY_MATRIX.md) (see
DEC-S-008). Distinguish permanent non-goals from deferred decisions. Require
explicit coordination for shared and contract-controlled areas, and define that
coordination in CDS-WP-006. Test the boundary against real needs in
CDS-WP-004.

---

## RISK-007 — Long-term scope interpreted as current commitment

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

Stakeholders may interpret long-term scope categories as already available,
stable, supported, or scheduled deliverables.

### Impact

Consumers plan against artifacts that do not exist, and adopt prematurely.
Expectations are missed, and the credibility of the whole registered scope
suffers — including the parts that are real.

### Mitigation direction

Apply DEC-S-009 consistently: separate long-term direction from current phase
scope in every document, and classify statements explicitly. Never present a
registered domain as available. Govern availability through the roadmap and the
maturity model defined in CDS-WP-006.

---

## RISK-008 — Consumer fragmentation

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Different consumer classes may create conflicting requirements and drive CDS
toward incompatible variants or uncontrolled exceptions.

### Impact

CDS degrades into a collection of product-specific special solutions — exactly
the outcome Non-goal 11 forbids. Shared substance shrinks, maintenance cost
grows per consumer, and the Single Source of Truth stops being single.

### Mitigation direction

Maintain the three relationship classes and their limits (see DEC-S-010).
Require generalization and explicit acceptance before a product-specific
solution becomes normative (see DEC-S-011). Determine in CDS-WP-005 whether one
architecture with controlled profiling can serve all classes, and govern
profiles and overrides in CDS-WP-006.

---

## RISK-009 — Misleading adoption or association claims

- **Status:** Monitored
- **Owner role:** Human Maintainer (provisional)
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Projects may claim CDS compliance, Core association, brand endorsement, or
support without an approved version reference and evidence.

### Impact

Unearned trust transfers to the claiming project, and any quality failure there
reflects back on CDS and the Core ecosystem. Unverifiable claims also make real
conformance meaningless once it exists.

### Mitigation direction

Apply DEC-S-012: claims require a specific CDS version reference and an
evidence model. State explicitly that consumer classification grants no
endorsement, availability, licensing, or support (see DEC-S-010). Define
conformance criteria, adoption levels, and the evidence model in CDS-WP-006.
Until then, no adoption or conformance claim is legitimate.
