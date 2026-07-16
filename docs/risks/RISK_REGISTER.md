# Risk Register

This register records the initial risks of the Core Design System (CDS) that
must be controlled from the start of the project.

## Register scope

- Risk range: RISK-001 … RISK-019
- Number of risks: 19
- Phase: Foundation / Pre-Design

Risks RISK-001 … RISK-005 were registered by CDS-WP-001. Risks
RISK-006 … RISK-009 were registered by CDS-WP-002 alongside the scope
registration. Risks RISK-010 … RISK-013 were registered by CDS-WP-003 alongside
the benchmark research. Risks RISK-014 … RISK-019 were registered by CDS-WP-004
alongside the consumer requirements and the CoreOps pilot contract.

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

---

## RISK-010 — Benchmark imitation

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Research findings may cause CDS to reproduce the visual identity, distinctive
taxonomy, component structure, or wording of another design system instead of
developing an independent identity.

### Impact

CDS becomes a derivative of the systems it studied, with no independent
rationale for its own decisions. Beyond the loss of identity, reproducing a
distinctive taxonomy, structure, or wording raises copyright and attribution
exposure, and imports design decisions whose original context does not apply to
the Core ecosystem.

### Mitigation direction

Synthesize rather than imitate. Describe foreign taxonomies abstractly only.
Copy no design content, token values, naming schemes, palettes, typography,
icon forms, layouts, long text passages, or documentation structures. Use system
names solely for source attribution. Keep the non-copying boundary explicit in
every research artifact, and treat any adoption of an observed practice as a
decision requiring its own CDS rationale rather than a citation.

---

## RISK-011 — Research and source bias

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

Publicly documented systems and accessible English-language sources may
overrepresent large technology companies and public-sector organizations.

### Impact

Conclusions reflect the practices of well-resourced publishers with dedicated
teams, and are then applied to a project with fundamentally different capacity.
Practices that are normal at that scale — public comment periods, parallel
maintained generations, published conformance reports — may be mistaken for
baseline expectations. Smaller, community, and commercial systems remain
invisible, so any claim about what "no one does" is unsafe.

### Mitigation direction

State the bias wherever benchmark conclusions are used. The reviewed set was
fixed in advance and consists only of large technology companies and national
governments; it cannot speak to smaller or community systems, which directly
caps hypotheses about small-team applicability. Test observed practices against
actual CDS maintainer capacity before adopting them. Any broadening of the
sample requires its own authorized work package.

---

## RISK-012 — Source volatility

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** Low

### Description

Referenced design-system documentation, releases, URLs, and publicly visible
practices may change after the benchmark is completed.

### Impact

Findings decay. Later work packages may rely on observations that no longer
hold, or cite URLs that have moved or disappeared. Evidence already exists that
this is not hypothetical: one reviewed documentation domain has permanently
redirected, and two reviewed systems are mid-generational-transition.

### Mitigation direction

Treat the benchmark as a dated snapshot rather than a standing description.
Every observation carries its access date and a registered URL, so any finding
can be re-checked. Re-verify a source before relying on it in a later decision.
Do not restate benchmark findings as current fact without checking. Record
redirects and access failures rather than silently substituting sources.

---

## RISK-013 — Differentiation overstatement

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** High

### Description

Common industry practices may be incorrectly presented as unique CDS
differentiators.

### Impact

CDS claims distinction it does not have. Strategy is then built on a false
premise, effort is spent defending a non-advantage, and credibility suffers when
the claim meets an informed reader. The risk is structural rather than
accidental: differentiation claims here rest on absence from public
documentation, which is systematically weaker evidence than presence.

### Mitigation direction

Keep hypotheses labelled as hypotheses until validated against real consumer
requirements (see the differentiation assessments and DEC-S-009). Require
counterevidence and an explicit uniqueness risk for every hypothesis. Prefer the
defensible framing — "no reviewed system publicly documented this" — over "no
one does this." Assess common practice honestly as common, even when it is
valuable. Make no claim that CDS is better than any reviewed system, and no
comparative first/only/best claim without comparison evidence.

Consumer evidence sharpens this risk rather than resolving it: a confirmed
consumer need justifies building a capability but says nothing about
uniqueness (DEC-S-019).

---

## RISK-014 — Consumer evidence staleness

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** Low

### Description

Consumer requirements derived from repository documentation may become outdated
as consumer projects evolve.

### Impact

CDS builds against needs that have moved. Requirements traced to a commit that
no longer reflects the consumer become misleading rather than merely stale, and
the traceability that made them credible now points at superseded content.

### Mitigation direction

Bind every requirement to a specific committed revision with a recorded date
(DEC-S-013), so any trace can be re-checked rather than trusted. Treat the
requirement register as a dated snapshot, not a standing description.
Re-verify consumer sources before relying on a requirement in a later decision,
particularly before foundations freeze. Consumer projects are active: two of the
three carried uncommitted changes at evidence time.

---

## RISK-015 — Pilot scope inflation

- **Status:** Monitored
- **Owner role:** Human Maintainer (provisional)
- **Initial likelihood:** High
- **Initial severity:** High

### Description

The bounded CoreOps pilot may expand into a de facto redesign of the complete
product or an attempt to implement the complete CDS.

### Impact

The pilot never finishes, consumes capacity CDS does not have, and produces no
transferable result. It also becomes indistinguishable from a CoreOps redesign,
which was never authorized and which no one agreed to resource.

### Mitigation direction

Hold the bounded slice defined in DEC-S-015: Pilot Groups A–E with an explicit,
binding out-of-scope list. Register real needs discovered during the pilot as
deferred candidates rather than absorbing them. Treat scope pressure as a
classified deviation with a defined handling, never as a reason to widen the
pilot. Scope changes require an authorized work package or an explicit
Human Maintainer correction — the pilot cannot extend itself.

---

## RISK-016 — Product-specific requirement contamination

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** High

### Description

CoreOps-specific requirements may be generalized prematurely and become
unnecessary complexity for other consumers.

### Impact

CDS accumulates operations-shaped complexity that other consumers must carry
without needing it. The foundation grows heavier and less adoptable with each
premature generalization, and eventually CDS becomes a CoreOps design library
serving one product — the outcome Non-goal 11 and DEC-S-002 forbid.

### Mitigation direction

Require the generalizability gate in DEC-S-016 before any CoreOps-specific
requirement becomes shared; origin in the pilot is never sufficient. Classify
requirements explicitly (DEC-S-014) and keep product-local requirements with
their products. Use secondary consumers to test whether a need generalizes.
Apply particular scepticism to operations-shaped patterns, where consumer
evidence is strongest and all reviewed consumers are infrastructure products —
a sample that cannot distinguish "operational products need this" from "all
products need this".

---

## RISK-017 — Document evidence mistaken for user validation

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

Committed documentation may be treated as equivalent to interviews,
observational research, accessibility testing, or usability validation.

### Impact

CDS believes its requirements are validated when they are merely written down.
Documented intent proves that someone considered a need; it does not prove the
resulting experience works for anyone. Accessibility is the sharpest case: a
documented "baseline" with no target, no method, and no test evidences nothing,
yet reads as diligence.

### Mitigation direction

State the evidence level explicitly and report outcomes only at the level the
evidence reaches. Documentation is Level 1 evidence and supports "documented as
needed" — never "works", "validated", "usable", or "accessible". Never claim
user research, interviews, or usability testing that did not happen. Keep
`Not tested` available and use it. Require Human Maintainer validation before
requirements are accepted, and real verification before any accessibility claim.

---

## RISK-018 — Pilot contract mistaken for adoption or conformance

- **Status:** Monitored
- **Owner role:** Human Maintainer (provisional)
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

The existence or completion of the pilot may be represented as full CDS
adoption, certification, endorsement, or conformance.

### Impact

Unearned credibility transfers to both CDS and CoreOps. Other consumers adopt on
the strength of a claim that a bounded slice cannot support, and any later
quality failure discredits the whole foundation. Once "CoreOps is CDS compliant"
circulates, it is very hard to retract.

### Mitigation direction

Apply DEC-S-015: the pilot is a bounded slice and constitutes neither adoption
nor conformance. Apply DEC-S-012: any future claim requires a specific version
reference and an evidence model, neither of which exists. Forbid informal
"CDS compliant" statements in every pilot output. Keep the contract status
explicit — normative only upon Human Maintainer commit following Nova approval,
and currently not active with entry criteria unmet.

---

## RISK-019 — Secondary consumer underrepresentation

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

SpeakCore and CastCore evidence may be incomplete, outdated, or insufficient to
represent future Core products, associated projects, and external consumers.

### Impact

Generalization is tested against a sample too narrow to detect overfitting. All
three reviewed consumers are self-hosted infrastructure products maintained by
the same small maintainer base, so agreement between them may reflect a shared
origin rather than a genuinely general need. Associated projects and potential
external consumers (DEC-S-010) are entirely unrepresented.

### Mitigation direction

Treat cross-consumer agreement as suggestive rather than conclusive, and record
the sample's narrowness wherever generalization is argued. Note that secondary
evidence is documentation-only and that authoritative design sources in those
projects were outside the permitted read areas. Register unreviewed consumers —
AirCore and further projects — as an open validation question rather than
assuming they fit. Broadening the consumer sample requires its own authorized
work package.
