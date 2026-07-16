# Risk Register

This register records the initial risks of the Core Design System (CDS) that
must be controlled from the start of the project.

## Register scope

- Risk range: RISK-001 … RISK-028
- Number of risks: 28
- Phase: Foundation / Pre-Design

Risks RISK-001 … RISK-005 were registered by CDS-WP-001. Risks
RISK-006 … RISK-009 were registered by CDS-WP-002 alongside the scope
registration. Risks RISK-010 … RISK-013 were registered by CDS-WP-003 alongside
the benchmark research. Risks RISK-014 … RISK-019 were registered by CDS-WP-004
alongside the consumer requirements and the CoreOps pilot contract. Risks
RISK-020 … RISK-028 were registered by CDS-WP-005 alongside the logical
architecture.

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

---

## RISK-020 — Normative-source authority ambiguity

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Human-readable and machine-readable normative sources may conflict without a
sufficiently precise ownership and precedence model.

### Impact

The system has two authorities that disagree, and no rule to settle it. Meaning
says one thing while approved values say another, so every downstream artifact
inherits a contradiction. Because both sources are legitimately normative, the
conflict cannot be resolved by demoting one — it stalls the whole chain until
someone decides, and the temptation is to resolve it by whichever is easier to
edit.

### Mitigation direction

Split authority precisely by artifact class: meaning belongs to human-readable
sources, approved values to machine-readable sources (DEC-S-022). Never let the
two overlap — a machine-readable source that carries meaning, or a human-readable
source that carries authoritative values, is the defect that creates this risk.
On conflict, fail closed and escalate rather than picking a winner (DEC-S-023).
The detailed conflict authority and escalation path are deferred to CDS-WP-006;
until then Nova recommends and the Human Maintainer decides.

---

## RISK-021 — Token and override proliferation

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

Token layers, aliases, component tokens, Product Profiles, and local exceptions
may expand faster than they can be governed or validated.

### Impact

The system becomes technically correct and practically unusable. Every layer is
individually justified while the total is incomprehensible, so nobody can predict
what changing a semantic token affects. Governance degrades into rubber-stamping
because reviewing the volume costs more than the maintainer capacity available.

### Mitigation direction

Constrain direction structurally — five layers, strictly downward dependency, no
cycles (DEC-S-024). Note honestly that the architecture constrains *direction*
but not *volume*: direction rules alone will not stop proliferation. Require
machine-checkable validation for cycles, orphans, unused tokens, layer
violations, and illegal overrides. Prefer additive extensions over overrides, and
treat repeated overrides of the same thing as a core defect to fix rather than a
pattern to accommodate. Profile and exception limits are deferred to CDS-WP-006,
which must set an actual budget.

---

## RISK-022 — Existing-product reconciliation failure

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Existing product-local design decisions may be overwritten, incompletely mapped,
or forced into CDS without adequate migration and evidence.

### Impact

Consumers lose shipped decisions they had good reasons for, or are pushed into a
migration they cannot afford. Either outcome makes CDS something done *to*
products rather than *for* them — and a consumer burned once will route around
the design system permanently. Incomplete mapping is the quieter failure: a
decision is carried across without its meaning, and the loss surfaces much later.

### Mitigation direction

Follow the reconciliation flow: inventory, semantic mapping, conflict
identification, classification, retention or migration, evidence and review
(DEC-S-026). Map **semantics, not values** — the question is what a decision
meant, never whether a value is right. Treat consumer-local retention as a valid
final outcome rather than a failure to converge. No automatic adoption, no
automatic overwrite, no retrospective conformance. Migration must be versioned,
documented, and reversibly plannable before it is proposed.

---

## RISK-023 — Domain-pattern leakage into the universal foundation

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** High

### Description

Operations-oriented requirements may become universal CDS rules despite limited
evidence from non-operational consumers.

### Impact

CDS becomes an operations design system wearing a universal label. Every future
non-operational consumer inherits assumptions about density, severity, and
monitoring that do not fit, and pays for them in complexity. The failure is
insidious because the evidence *feels* overwhelming — all three reviewed
consumers genuinely need these patterns.

### Mitigation direction

Model operations patterns as a Domain Pattern Family above the universal
foundation, adopted only by consumers in that domain (DEC-S-027). Forbid domain
requirements from pushing into Layers 3 and 4 without multi-consumer evidence
from **outside** that domain — evidence from three infrastructure products is not
evidence about products in general. Keep the sample bias explicit wherever
operations patterns are argued: the benchmark could not verify generalizability
either, so both evidence layers are silent on the same question.

---

## RISK-024 — Channel divergence

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Product UI, documentation, PDF, presentation, diagram, and communication outputs
may drift into inconsistent semantic or visual systems.

### Impact

The ecosystem produces artifacts that contradict each other. A status means one
thing in a dashboard and another in the report about that dashboard, which is
worse than having no standard at all — readers trust the inconsistency. Divergence
also compounds: each channel that drifts makes the shared semantic source look
more optional.

### Mitigation direction

Bind all channels to one governed semantic source while permitting
channel-specific transformation, layout, and interaction (DEC-S-029). Enforce the
line precisely: presentation may differ, meaning may not. Forbid transformations
that collapse status axes or make colour the sole carrier — the non-interactive
channels break first, and they break silently. Note that the shared source
constrains divergence but does not eliminate it; governance of channel additions
is deferred to CDS-WP-006. Registering a channel class is not a commitment to
build it.

---

## RISK-025 — Generated-artifact provenance loss

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Generated outputs may be distributed or edited without a reliable binding to
their normative sources and transformation revision.

### Impact

An artifact whose origin cannot be established becomes **functionally normative**,
because nobody can contradict it. A consumer integrating it cannot tell what it
was derived from, cannot reproduce it, and cannot know whether it is current. A
hand-edited output is worse: it is a decision that never passed through
governance and now circulates as if it had.

### Mitigation direction

Require source revision, transformation revision, and output identity on every
generated artifact (DEC-S-031). Require reproducibility — same source revision
plus same transformation revision equals same output — since provenance without
reproducibility is a claim rather than a fact. Treat manual edits to generated
artifacts as invalid: they are discarded or reconciled back into the source,
never allowed to stand. Treat distribution without provenance as a defect, not an
oversight.

---

## RISK-026 — Architecture overdesign

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

The logical architecture may become too complex for the available maintainer
capacity before implementation evidence exists.

### Impact

CDS spends its capacity maintaining structure instead of producing anything
consumers can use. Eight layers, eight artifact classes, five token levels, five
status axes, and five contracts are each defensible and collectively substantial
— and none has yet met a real implementation. The architecture may be describing
a system that a larger team would build.

### Mitigation direction

Recognise that this architecture is currently **unvalidated by implementation**:
the benchmark's most rigorous practices come from publishers with dedicated teams
(RISK-011), and adopting their structure without their capacity is the specific
failure mode here. Use the bounded CoreOps pilot as the first real test, and
treat pilot friction as evidence about the architecture rather than about the
pilot. Prefer removing structure that earns nothing over defending it. Keep
deferred decisions deferred — every decision not yet made is complexity not yet
paid for.

---

## RISK-027 — Product-profile fragmentation

- **Status:** Monitored
- **Owner role:** Nova (provisional)
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Product Profiles and consumer extensions may become de facto independent design
systems.

### Impact

CDS becomes a shared vocabulary for systems that no longer share anything.
Profiles accumulate overrides until each product effectively runs its own design
system with a CDS label, and the label then misleads: consumers believe they are
aligned when they are not. This is the endpoint RISK-008 describes, reached
through legitimate-looking steps.

### Mitigation direction

Bound profiles absolutely: approved extension points only, and never redefining
shared semantics, weakening accessibility, distorting status truth, or breaking
contracts (DEC-S-025). Treat a profile that needs a prohibited change as a fork
and name it as one — an honest fork is manageable; a profile pretending not to be
one is not. Prefer additive extensions. Treat repeated identical overrides as a
core defect. Note that consumers already hold their own design decisions
(CR-002, CR-037), so the starting position is closer to fragmentation than to
alignment. Profile governance and limits are deferred to CDS-WP-006.

---

## RISK-028 — Deferred accessibility policy creates architecture debt

- **Status:** Monitored
- **Owner role:** Human Maintainer (provisional)
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Architecture decisions made before CDS-WP-007 may inadvertently constrain future
accessibility requirements or make them costly to adopt.

### Impact

The architecture is being decided while the accessibility target is undefined
(CR-024). If a structural decision turns out to preclude a later target, the cost
lands after the structure is load-bearing and consumers depend on it. The
evidence base makes this sharper: accessibility is weak in **both** the benchmark
and the consumer layers — CoreOps names a baseline with no level and CastCore
documentation contains none at all — so there is little to steer by. A CoreOps
pilot entry criterion is also blocked until the target exists.

### Mitigation direction

Keep accessibility in the architecture as a **structural constraint rather than a
threshold**: constraints survive a later policy, whereas specific thresholds would
pre-empt it. Hold the constraints that are safe regardless of level — colour never
the sole meaning carrier, component contracts carry accessibility behavior,
profiles may not weaken guarantees (invariant 10), status perceivable
non-visually. Make **no conformance claim of any kind** meanwhile. Consider
advancing CDS-WP-007 or deciding the target earlier than the roadmap implies,
since the architecture cannot fully validate Pilot Group E without it.
