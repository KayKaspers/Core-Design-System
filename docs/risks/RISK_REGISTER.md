# Risk Register

This register records the initial risks of the Core Design System (CDS) that
must be controlled from the start of the project.

## Register scope

- Risk range: RISK-001 … RISK-097
- Number of risks: 97
- Phase: Pre-Candidate Operating Enablement (Foundation / Pre-Design closed with notes)

Risks RISK-001 … RISK-005 were registered by CDS-WP-001. Risks
RISK-006 … RISK-009 were registered by CDS-WP-002 alongside the scope
registration. Risks RISK-010 … RISK-013 were registered by CDS-WP-003 alongside
the benchmark research. Risks RISK-014 … RISK-019 were registered by CDS-WP-004
alongside the consumer requirements and the CoreOps pilot contract. Risks
RISK-020 … RISK-028 were registered by CDS-WP-005 alongside the logical
architecture. Risks RISK-029 … RISK-040 were registered by CDS-WP-006 alongside
the governance model. Risks RISK-041 … RISK-048 were registered by CDS-WP-007
alongside the accessibility and inclusive design policy. Risks
RISK-049 … RISK-054 were registered by CDS-WP-010 alongside the accessibility
support baseline and evidence strategy. Risks RISK-055 … RISK-063 were registered
by CDS-WP-011 alongside the machine-readable source and token format decision. Risks
RISK-064 … RISK-072 were registered by CDS-WP-012 alongside the machine-readable source
bootstrap and validation contract. Risks RISK-073 … RISK-081 were registered by
CDS-WP-013 alongside the offline token profile validator and fixture harness.
Risks RISK-082 … RISK-089 were registered by CDS-WP-014 alongside the semantic
status foundation contract. Risks RISK-090 … RISK-097 were registered by
CDS-WP-015 alongside the semantic status source set and candidate evidence.

### Finalized risk role model

*(Established by CDS-WP-006, DEC-S-045 — no longer provisional)*

Four roles apply to **every** risk in this register:

| Role | Held by | Authority |
| --- | --- | --- |
| **Accountable Risk Owner** | **Human Maintainer** | Decides acceptance, prioritizes mitigation, approves closure, carries final governance responsibility. Not delegable. |
| **Risk Controller** | **Nova** | Observes, assesses, requests evidence, recommends mitigation, reviews closure, reports escalation need. **Does not accept or close a risk.** |
| **Mitigation Executor** | Named per mitigation | Default: Claude (scoped) for documentation-shaped mitigations. A `Mitigating` risk without a named executor is not being mitigated. |
| **Evidence Reviewer** | Nova or an explicitly authorized reviewer | **Never the artifact itself, and never the executor of the work being evidenced.** |

Since these roles are uniform across all risks, they are stated once here rather
than repeated in every entry. Where a risk has a **specific** mitigation
executor, it is named in that entry.

**Only the Human Maintainer may set a risk to `Accepted` or `Closed`.**

Full model: [Risk Governance Model](../governance/RISK_GOVERNANCE_MODEL.md).

### Status values

| Status | Meaning |
| --- | --- |
| **Identified** | Registered; no treatment decided. |
| **Monitored** | Mitigation direction defined; effect observed over time. |
| **Mitigating** | Active mitigation in progress; requires a named executor. |
| **Accepted** | Consciously accepted with residual effect; requires a review trigger. |
| **Closed** | No longer relevant, or fully mitigated with evidence. |

**90 of the 97 risks are currently `Monitored`; RISK-040, RISK-044, RISK-066,
RISK-067, RISK-068, RISK-069, and RISK-071 are `Mitigating`.** CDS-WP-006 finalized
the role model; it treated no risk and changed no assessment, because no evidence
justified a change. CDS-WP-007 added RISK-041 … RISK-048 and likewise treated none.
CDS-WP-009 moved **RISK-040 `Monitored → Mitigating`** on the strength of the
[Critical Risk Action Register](../operations/CRITICAL_RISK_ACTION_REGISTER.md).
CDS-WP-010 added **RISK-049 … RISK-054** and moved **RISK-044
`Monitored → Mitigating`** on the strength of the defined
[Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md).
CDS-WP-011 added **RISK-055 … RISK-063** and changed no existing status. CDS-WP-012
added **RISK-064 … RISK-072** (all `Monitored`) and changed no existing status.
CDS-WP-013 added **RISK-073 … RISK-081** (all `Monitored`) and moved **RISK-066,
RISK-067, RISK-068, RISK-069, and RISK-071 `Monitored → Mitigating`** on the strength
of the executed offline validator and fixture harness — an executor-produced,
independently unreviewed evidence basis (DEC-S-103). CDS-WP-014 added
**RISK-082 … RISK-089** (all `Monitored`, semantic-status truthfulness risks) and
changed no existing status. CDS-WP-015 added **RISK-090 … RISK-097** (all
`Monitored`, status source/evidence risks) and changed no existing status. No description, likelihood, or
severity was changed for any existing risk, and **no risk was accepted or closed** —
only the Human Maintainer may do either.

## Assessment scale

Qualitative values are used deliberately. No numeric probabilities are assigned,
because the project has no empirical basis for them in this phase.

| Value | Meaning |
| --- | --- |
| Low | Unlikely or limited effect under current conditions. |
| Medium | Plausible or noticeable effect under current conditions. |
| High | Likely or severe effect under current conditions. |

---

## RISK-001 — Uncontrolled scope expansion

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
explicit — committed and normative (CDS-WP-004), and currently not active with
entry criteria unmet.

---

## RISK-019 — Secondary consumer underrepresentation

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
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
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Architecture decisions taken before CDS-WP-007 may have constrained the
now-defined accessibility requirements, or made them costly to adopt.

### Impact

Much of the architecture was decided before the accessibility target existed
(CR-024). The target is now defined — **WCAG 2.2 Level AA** (DEC-S-049,
DEC-S-060), committed with CDS-WP-007 — but **almost no accessibility evidence has
been produced**: every CDS artifact is AE-0 except the channel-independent Semantic
Status Layer-3 source/contract family, which holds admitted source-level **AE-1**.
That single bounded package does not close this risk. Whether the existing structure is
compatible with the committed policy is therefore neither demonstrated nor
refuted; the missing evidence is what keeps this risk open, not a missing target.
If a structural decision turns out to preclude the target, the cost lands after
the structure is load-bearing and consumers depend on it. The evidence base makes
this sharper: accessibility is weak in **both** the benchmark and the consumer
layers — CoreOps names a baseline with no level and CastCore documentation
contains none at all — so there is little to steer by. Pilot Group E still cannot
be evidenced.

### Mitigation direction

Keep accessibility in the architecture as a **structural constraint rather than a
threshold**: constraints survive policy revision, whereas specific thresholds
would pre-empt it. Hold the constraints that are safe regardless of level — colour
never the sole meaning carrier, component contracts carry accessibility behavior,
profiles may not weaken guarantees (invariant 10), status perceivable
non-visually. Make **no conformance claim of any kind** meanwhile: the committed
policy is not evidence, and documentation is not mitigation. Validate the existing
architecture against the committed policy once an authorized scope exists for
that work; the architecture's own stale dependency state belongs to the separate
architecture temporal-dependency reconciliation, not here.

---

## RISK-029 — Governance bottleneck and maintainer overload

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: Nova (process design) · Evidence Reviewer: Nova
- **Initial likelihood:** High
- **Initial severity:** High

### Description

Final authority concentrated in one Human Maintainer may delay decisions,
reviews, releases, or risk treatment.

### Impact

Governance becomes the constraint on delivery. Work queues behind a single
approver, and the pressure that builds is precisely the pressure that makes
bypassing a gate look reasonable. The failure is self-reinforcing: the slower the
gate, the stronger the argument for going around it, and each bypass makes the
gate less real.

### Mitigation direction

Size governance to actual capacity rather than to the benchmark's publishers,
who have dedicated teams (RISK-011). Use the Standard Track to keep low-risk work
moving, and remove ceremony that produces no decision. Treat bottleneck pressure
as a reason to **reduce ceremony or widen authority through an explicit governed
decision** — never as a reason to skip a gate. Concentrated authority is a
deliberate choice (DEC-S-005) whose cost must stay visible rather than be
absorbed silently.

---

## RISK-030 — Governance role ambiguity

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Approval, review, control, execution, contribution, and consumer ownership may be
confused despite the defined role model.

### Impact

A review is mistaken for an approval, or an executor reviews their own evidence,
and the separation of duties quietly disappears. The model still exists on paper
while the practice has collapsed into whoever is available — which is
indistinguishable from having no model.

### Mitigation direction

Keep review and approval as **separate recorded acts** (DEC-S-033). Enforce that
no contributor approves their own contribution, and that an Evidence Reviewer is
never the executor of the work being evidenced. Note that one person may hold
several roles — the separation of duties still applies, and the risk is highest
exactly there. Treat an automated check as input to a review, never the review.

---

## RISK-031 — Maturity inflation

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** High

### Description

Experimental or incomplete artifacts may be presented as Candidate or Stable
without sufficient evidence.

### Impact

Consumers adopt on a promise the artifact cannot keep, and discover it in
production. Once a maturity label is untrustworthy, every label becomes noise —
including the honest ones — which destroys the mechanism DEC-S-009 depends on.

### Mitigation direction

Keep maturity, release version, and publication state on **separate axes**
(DEC-S-035): collapsing them is the mechanism by which "we released it" becomes
"it is stable". Require the Candidate and Stable gates with evidence and explicit
approval (DEC-S-036), and keep Candidate mandatory before Stable. Make demotion
normal and cheap. Note that **no existing artifact is Candidate or Stable** —
defining the lifecycle did not populate it.

---

## RISK-032 — Compatibility ambiguity

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Consumers may assume compatibility that was never assessed or only applies to a
subset of contracts.

### Impact

A consumer upgrades on the strength of "compatible" and breaks on the one axis
nobody evaluated. The damage lands in the consumer's product, and the trust cost
is paid by CDS.

### Mitigation direction

Declare compatibility **per axis**, never as a single verdict (DEC-S-039). Keep
`Not yet assessed` as a first-class statement and let it survive into the release
record — the temptation to round it up to `Compatible` because nothing broke in
testing is the specific failure here. Name the relevant axes in every release
approval, and never guarantee consumer-local artifacts.

---

## RISK-033 — Deprecation without viable migration

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Artifacts may be deprecated or removed without a practical consumer migration
path.

### Impact

Consumers are told to move with nowhere to go. They then either stay on a
deprecated artifact indefinitely — making the deprecation meaningless — or fork,
which is worse. Either way CDS has broken a Stable promise while appearing to
follow process.

### Mitigation direction

Require migration guidance as a **mandatory deprecation field** (DEC-S-040). Treat
a deprecation without a viable path as **a removal with extra steps** and refuse
it: if no migration exists, the artifact is not ready to be deprecated. Require
migration to be versioned, documented, and reversibly plannable, and attach
migration information to the release that causes the need — not to a later one
that notices it.

---

## RISK-034 — Contribution gate bypass

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Existing implementation, urgency, popularity, or consumer pressure may be used to
bypass scope, evidence, architecture, or acceptance review.

### Impact

CDS accepts what was already built rather than what generalizes, and the gate
becomes a formality applied after the decision. Volume of use becomes authority —
the exact mechanism by which CDS would become whatever its loudest consumer
already has (RISK-016).

### Mitigation direction

Enforce the ten-step flow with steps 3–5 positioned to reach a cheap *no*
(DEC-S-041). Prohibit auto-merge, self-approval, urgency bypass, and bundling an
Elevated change into a Standard batch. Hold the line that consumer use proves
need, never fit, and that popularity is not evidence. Keep `Keep Consumer-local`
a first-class success so that declining is a normal outcome rather than a
rejection to be argued around.

---

## RISK-035 — Exception debt

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: Consumer Maintainer (per exception) · Evidence Reviewer: Nova
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

Temporary exceptions may accumulate, expire without review, or become permanent
hidden forks.

### Impact

The exception register becomes a list of divergences nobody is resolving. Each
was individually reasonable and temporary; collectively they are a fork that
happened by increments, with no moment at which anyone decided to fork.

### Mitigation direction

Require an expiry or review point and a migration path as **mandatory fields**
(DEC-S-042) — expiry is what forces the deferred decision. Treat `Expired` as an
**uncovered deviation**, never a grandfathered permission. Trigger a **CDS gap
review on recurring exceptions**: several consumers needing the same exception
means the core is wrong. Never let an exception become a precedent.

---

## RISK-036 — Product-profile governance bypass

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Consumer-local design decisions may be labelled Product Profiles without
reconciliation, validation, or explicit acceptance.

### Impact

Existing divergence is retrospectively legitimised by relabelling. CDS appears to
govern designs it never reviewed, and the profile mechanism — meant to bound
variation — becomes the instrument for laundering it. The risk is live now:
SpeakCore and CastCore already hold their own design decisions (CR-002, CR-037).

### Mitigation direction

Hold that **a Product Profile is not retrospective legitimation** (DEC-S-043).
Consumer-local design stays consumer-local until reconciled and explicitly
accepted (DEC-S-026). Require all twelve profile elements including named
extension points and an anti-fragmentation review. Require the review to ask
whether the request is really a **core gap** or would be better served
additively. Note that no profile can be approved today, since accessibility
evidence is unobtainable.

---

## RISK-037 — Misleading adoption or conformance claims

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: Consumer Maintainer (per claim) · Evidence Reviewer: Nova
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Consumers or public materials may overstate CDS use, validation, conformance,
certification, endorsement, or support.

### Impact

Unearned trust transfers to the claiming project, and any quality failure there
reflects back on CDS. The asymmetry is the problem: an unqualified claim costs
nothing to make and everything to disprove. Once "X is CDS compliant" circulates,
retracting it is far harder than preventing it.

### Mitigation direction

Enforce four graded, scope- and version-bound claim types with eight mandatory
fields (DEC-S-044) — a claim missing any field is not a weaker claim, it is not a
claim. **Prohibit `CDS certified` outright**, since no certification programme
exists. Require re-assessment on eight triggers and treat a stale claim as
withdrawn — silence is not continuation. Hold that pilot completion is not
adoption, naming a consumer is not endorsement, and a hypothesis is not a claim.

---

## RISK-038 — Licensing and rights fragmentation

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: Human Maintainer · Evidence Reviewer: Nova
- **Initial likelihood:** High
- **Initial severity:** High

### Description

Different artifact classes may have incompatible, missing, or misunderstood
rights and licensing conditions.

### Impact

CDS publishes something it has no right to publish, or a consumer relies on a
right that was never granted. Fonts and brand assets are the sharp edges: fonts
are frequently not redistributable, and logos are trademarks whose purpose is to
not be freely usable. A single "the licence" decision fails precisely there — and
rights errors are among the hardest to unwind after distribution.

### Mitigation direction

Decide licensing **per artifact class** across all ten classes (DEC-S-047), with
an eleven-field rights matrix each. Prohibit automatic inheritance: a code licence
never governs documentation, tokens, fonts, icons, templates, examples, or brand
assets. Establish third-party provenance **before** any public state, and treat
unknown or conflicting rights as an **absolute publication blocker** — unknown
provenance is not "probably fine". Keep brand assets separate from open technical
artifacts.

---

## RISK-039 — Premature publication

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: Human Maintainer · Evidence Reviewer: Nova
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

CDS artifacts may be made public before maturity, compatibility, provenance,
accessibility, maintenance, or claim restrictions are adequately documented.

### Impact

Publication creates expectation. Consumers adopt something CDS cannot yet
support, on terms nobody verified, with an accessibility posture nobody defined.
The specific hazard is mundane: **making a repository public is a checkbox**, and
without a gate that checkbox performs a publication decision nobody made.

### Mitigation direction

Keep publication state and repository visibility **strictly separate**
(DEC-S-046) — visibility is a technical setting, publication is a commitment.
Require the fifteen-point publication gate including per-class licence review,
third-party provenance, and an accessibility statement. Note that requirements 8,
9, and 11 are **currently unsatisfiable**, so no publication-state change is
possible today. Failing the gate is **NO-GO**, never "go with notes". Require any
public state to say plainly what CDS does not offer.

---

## RISK-040 — Ceremonial risk governance

- **Status:** Mitigating *(changed from `Monitored` by CDS-WP-009; see the status note below)*
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: Nova · Evidence Reviewer: a separately authorized reviewer (Nova is precluded here as the Mitigation Executor; currently unstaffed — FM-F-006)
- **Initial likelihood:** High
- **Initial severity:** Medium

### Status note (CDS-WP-009)

RISK-040 moved from `Monitored` to `Mitigating`. The mitigation is the
[Critical Risk Action Register](../operations/CRITICAL_RISK_ACTION_REGISTER.md),
which gives all twelve Critical Risks (RISK-017, 020, 021, 023, 026, 028, 029,
031, 038, 040, 044, 048) a named Mitigation Executor role, a review trigger, a
next expected evidence artifact, and a blocking effect — the gate DEC-S-064
requires. Nova is the named executor. Neither likelihood nor severity changed; the
risk was neither accepted nor closed. This is the only risk status change
authorized in CDS-WP-009.

### Description

The risk register may be updated formally without driving mitigation, evidence,
escalation, acceptance, or closure decisions.

### Impact

The register becomes an artifact of diligence rather than an instrument of
control. Risks are recorded, described well, reviewed on schedule — and nothing
changes. This is worse than having no register, because it produces the
confidence of managed risk without the substance, and it is the most likely
failure mode for a project with one maintainer and forty risks.

### Mitigation direction

Require a **review trigger** per risk rather than a review date nobody honours.
Require a **named executor** for any `Mitigating` risk — without one it is
`Monitored`, and saying so is the honest act. Hold that **documentation is not
mitigation**: a policy addressing a risk is a first step, not a treatment. Prefer
fewer real risks over many decorative ones, and distinguish a long-unchanged risk
that is genuinely stable from one that is genuinely ignored. Note honestly that
**CDS-WP-006 added twelve risks and treated none** — which is exactly what this
risk warns about, and is recorded rather than obscured. **CDS-WP-007 added eight
more and treated none**, bringing the register to 48 risks, **none `Mitigating`,
none with a named executor**. The pattern this risk describes is now two work
packages long and getting stronger, not weaker.

---

## RISK-041 — Accessibility target mistaken for conformance

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** High

### Description

The **WCAG 2.2 Level AA target** may be communicated as if CDS or a consumer had
already demonstrated conformance — the documented target, applicability matrix,
evidence model, and channel profiles read, internally or by consumers, as evidence
that CDS is accessible.

### Impact

CDS-WP-007 produced eleven substantial accessibility documents and **zero
accessibility**. That asymmetry is itself the hazard: the volume and specificity
of the policy make it *more* credible as an achievement, not less. A consumer
reading "WCAG 2.2 AA" in a CDS document may reasonably assume artifacts meet it,
build on that assumption, and inherit barriers they never tested for — while
believing the question was already answered.

This is the same failure the project's core invariant names: **Unverified ≠
Verified**. Every CDS artifact is **AE-0** except the channel-independent Semantic
Status Layer-3 source/contract family at admitted **AE-1** — a structural and
automated level that is **not** conformance, **not** a claim, and **not** a
demonstration that the WCAG target is met.

### Mitigation direction

Carry the **target-versus-claim boundary** explicitly in every accessibility
document (DEC-S-050). **State the actual, scope-bound evidence level truthfully
wherever the target is stated, and never let a target imply a higher evidence or
claim state.** Permit no
claim without evidence. Treat any statement implying conformance as a defect.
**The honest sentence is: nothing has been tested against the target — the only
admitted evidence is structural and automated, for one bounded source scope.**

---

## RISK-042 — Automated-testing substitution

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

Automated checks may be treated as a **replacement** for manual interaction,
assistive-technology, complete-process, or consumer-scope evidence — a clean
automated run read as accessibility evidence or as a pass.

### Impact

Automated tools detect a minority of barriers and cannot judge **meaning**:
whether alternative text is correct, whether focus order is comprehensible,
whether a status is honest. A clean run is fully consistent with an unusable
product.

This risk is attractive rather than merely possible: automation is cheap,
repeatable, and produces a green result — everything the evidence model demands is
expensive, manual, and produces a nuanced one. Under capacity pressure (RISK-048)
the tool's silence becomes the claim.

### Mitigation direction

Enforce **DEC-S-053**: automated results may support evidence, never constitute
it. Require AE-2 manual and AE-3 assistive-technology evidence against a declared
baseline for Stable. Never present a tool result as a conformance statement. **No
tooling is selected and no checks have been run.**

---

## RISK-043 — Component-to-product responsibility gap

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** High

### Description

CDS and consumer maintainers may **each assume the other side owns** composition,
content, runtime, process, or integration accessibility. With **49 of 55
applicable criteria requiring action from both**, shared responsibility may become
no responsibility.

### Impact

CDS assumes the consumer handles composition; the consumer assumes CDS handled
accessibility because the components are "accessible components". Both assumptions
are individually reasonable and jointly produce an inaccessible product that
nobody believes they own.

The structural asymmetry makes this worse: CDS has the authority to define but
cannot test the product, and the consumer can test but cannot change the contract.
The gap sits exactly where 49 criteria live.

### Mitigation direction

Hold the responsibility model per criterion, not per artifact. Enforce
**DEC-S-052**: accessible artifacts do not produce accessible products. Require
**AE-4** for any consumer claim. Make the Integration Contract carry the
consumer's obligation explicitly rather than by implication.

---

## RISK-044 — Accessibility support baseline drift

- **Status:** Mitigating *(changed from `Monitored` by CDS-WP-010; see the status note below)*
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: Claude as scoped executor (baseline/evidence-strategy documentation); baseline **approval** is the Human Maintainer's · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** High

### Status note (CDS-WP-010)

RISK-044 moved from `Monitored` to `Mitigating`. The mitigation is the defined
[Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
(A11Y-BL-001) and its
[Maintenance Policy](../governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md):
a concrete initial baseline is defined, maintenance/review triggers exist, a maximum
six-month review gap is set, version and freshness are bound in the evidence model
(DEC-S-068, DEC-S-070, DEC-S-071), and the next expected evidence artifact (AE-1 +
AE-2 for the first Candidate slice against the Required Tier-1 pairings) is defined.
Neither likelihood nor severity changed; the risk was neither accepted nor closed.
The baseline itself is committed (CDS-WP-010) and produces no evidence.

### Description

Browser, platform, input, rendering, and assistive-technology combinations may
change **without evidence being reassessed** against the new baseline. The prior,
sharper form of this risk — that **no accessibility support baseline had been
declared at all** — no longer applies: A11Y-BL-001 is declared and committed
(CDS-WP-010). The drift form of the risk remains fully in force.

### Impact

**AE-3 is unreachable, therefore Stable is unreachable**, for every artifact with
an accessibility obligation. The baseline is a small-looking document that
silently gates the entire maturity model, and once one exists, silent drift makes
evidence gathered against the old combination quietly false.

An undeclared or stale baseline also invites evidence produced against whatever
the tester happened to have installed, which reads as verification and verifies
nothing. **Accessibility evidence without a current declared baseline is
unverifiable.**

### Mitigation direction

Require a declared baseline before any AE-3 evidence is accepted, and name
baseline definition as an explicit roadmap prerequisite rather than assuming it
appears with the first test. Treat a baseline change as **invalidating dependent
evidence and triggering a claim review** (DEC-S-044). Re-verify the baseline on a
defined trigger, not a date nobody honours.

---

## RISK-045 — Accessibility regression

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Previously reviewed **semantics, keyboard behavior, focus, states, content, or
channel output may regress** through later changes — a fix, a refactor, a profile
override, or a copied pattern silently removing an accessibility property that was
once present.

### Impact

Regression is uniquely corrosive because it defeats past evidence: an artifact
that once satisfied AE-2 or AE-3 can become inaccessible while still *carrying* the
old evidence, so the record asserts a property the artifact no longer has. Under
the mandatory contract areas (DEC-S-055) any of keyboard operability, visible
focus, non-colour meaning, or accessible status can be the casualty.

A specific and likely vector: **copying a WAI-ARIA APG example as if it were a
production component.** The APG states its objectives exclude production-ready
code, so a pasted pattern is AE-0 code carrying an implicit reputation of
correctness — a regression introduced under borrowed authority (DEC-S-054).

### Mitigation direction

Require a **regression plan** as part of the Candidate accessibility gate, and
treat any change touching a mandatory contract area as invalidating dependent
evidence until re-verified. Enforce **DEC-S-054**: APG examples are class 8
research artifacts, never normative and never evidence; a pattern-derived artifact
needs independent evidence regardless of source. Bind evidence to a revision so a
later change cannot silently inherit it.

---

## RISK-046 — Non-web channel accessibility gap

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

PDFs, reports, presentations, diagrams, visualizations, and communication
materials may be **published without channel-specific accessibility requirements
or evidence** — or the web target (WCAG 2.2 AA) may be wrongly asserted across
channels for which no profile and no target exist.

### Impact

Two failures share this risk. A non-web artifact may ship with **no accessibility
requirements at all**, because WCAG is web-oriented and the channel has no profile
yet. Or the web target may be **asserted where it does not apply** — a status
error dressed as a standard, most tempting precisely where CDS has done the least
work. Applying web success criteria to a paginated print artifact is a category
error in some cases and undefined in others.

**Four of six channel profiles have no target. Zero channels are Candidate- or
Stable-eligible.**

### Mitigation direction

Enforce **DEC-S-058**: a channel without a profile cannot reach Candidate or
Stable, and **non-web channels are never presented as WCAG conformant**. Keep
per-channel targets explicit and separately evidenced, and hold that **evidence
never transfers between channels**.

---

## RISK-047 — Inclusive-design undercoverage

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

WCAG-focused work may **underrepresent cognitive, language, situational,
low-bandwidth, stress, complexity, or other user needs** not fully captured by a
conformance target.

### Impact

WCAG AA is a floor, and DEC-S-057 states plainly that conformance does not by
itself prove every inclusive-design need is met. The realistic failure is quiet: a
team treats the 55-criterion matrix as the whole job, and the 69 inclusive-design
requirements across the ten baseline areas — clear content, error recovery,
flexible text, DE/EN parity, safe handling of dangerous actions — receive less
attention because they do not carry a numbered success criterion.

CDS consumers are operations products where the user is often tired, interrupted,
and acting on consequential information — exactly the population an inclusive-design
gap harms most. **No user research exists and none is planned** (RISK-017), so the
gap would not be detected by evidence.

### Mitigation direction

Hold the inclusive-design requirements (DEC-S-057) as **first-class**, not as an
appendix to WCAG. Keep the requirements baseline visible in Candidate and Stable
gates. State honestly that meeting all 55 criteria is **necessary, not
sufficient**, and that inclusive design is currently asserted from documentation,
not validated with people.

### Related documented concern — standards status

*(Note, not a separate risk ID.)* Referenced standards can be cited at a status
they do not hold — **EN 301 549 V4.1.0 is `On Approval`** and **WCAG-EM 2.0 is a
Group Note Draft**. This is governed as an **evidence limitation** in the
[Accessibility Standard Status and Limitations](../research/ACCESSIBILITY_STANDARD_STATUS_AND_LIMITATIONS.md):
status is recorded as retrieved and dated, EN 301 549 is tracked as standards-watch
and never adopted, WCAG-EM 2.0 is not adopted as the CDS conformance method, and
status is re-verified at each accessibility work package.

---

## RISK-048 — Accessibility evidence burden exceeds maintainer capacity

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** High

### Description

The evidence the policy requires — AE-1 through AE-3 against a declared baseline
per artifact, AE-4 per consumer scope, manual and assistive-technology testing,
per-channel profiles — may exceed what a single maintainer can produce.

### Impact

This is the risk most likely to break the policy, and it will not break it
honestly. When the burden bites, the available shortcuts are all the ones already
prohibited: substitute AE-1 where AE-3 is required, lean on automated checks
(RISK-042), copy APG patterns as production components (RISK-045), or relabel a
critical limitation (DEC-S-059).

The realistic failure is not a decision to abandon accessibility. It is a series
of individually defensible compromises under deadline, each one small.

**No user research exists and none is planned** (RISK-017) — capacity is already
binding before any evidence work has begun.

### Mitigation direction

Enforce **DEC-S-059**: **missing capacity is a planning limit, never a conformance
justification.** The honest responses are a **smaller scope** or a **lower
maturity** — never a weaker standard, and never a conformant artifact with an
asterisk. Prefer few artifacts with real AE-3 evidence over many at AE-0 with a
policy. Escalate capacity pressure as a governance decision for the Human
Maintainer, rather than absorbing it as a quiet reduction in evidence.

---

## RISK-049 — Accessibility baseline representativeness gap

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

A small capacity-aware baseline may fail to represent important user, platform,
language, input, or assistive-technology environments.

### Impact

Evidence produced only against the Required Tier-1 environments may miss barriers
that appear on WebKit/Safari, on mobile/touch, with commercial screen readers, with
alternative input, or in languages beyond DE/EN. A baseline that is affordable but
narrow can read as thorough while leaving whole user groups unevidenced.

### Mitigation direction

Keep the Required baseline honestly small **and** keep its coverage gaps visible
(A11Y-BL-001, Environment and Scope Matrix). Assign Complementary and Scope-triggered
tiers with explicit triggers so the declared scope, a Consumer Contract, a Product
Profile, or a documented risk expands coverage before a matching claim. Never present
Tier-1 coverage as universal (DEC-S-066, DEC-S-069).

---

## RISK-050 — Baseline interpreted as universal support

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Consumers may treat the declared evidence baseline as a guarantee that all listed or
unlisted environment combinations are supported.

### Impact

A baseline is a *test contract*, not a support statement. If it is read as "these
environments are supported", a consumer builds on an assurance CDS never gave —
inheriting untested barriers while believing the question was answered, and any later
failure discredits the whole baseline.

### Mitigation direction

Carry the target-versus-support-versus-claim boundary in the baseline (DEC-S-065):
listing an environment is never support. Permit no support or conformance claim
without evidence, a declared scope, and approval (DEC-S-044). State plainly that
no baseline environment has been exercised, that every artifact is AE-0 apart from
one bounded admitted source-level AE-1 scope, and that undeclared environments are
not supported (DEC-S-069).

---

## RISK-051 — Environment availability mismatch

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

The approved baseline may include hardware, operating systems, browsers, or
assistive technologies that the current maintainers cannot practically access for
evidence execution.

### Impact

A baseline that names environments no one can run produces either no evidence or
invented evidence. The sharp case is a commercial screen reader whose official
requirements could not even be retrieved (JAWS, S-12/S-13) or an Apple/mobile
platform no maintainer currently has — each a Required-looking commitment with no
execution path.

### Mitigation direction

Never invent local availability. Record every environment's local execution
availability as `Not asserted` until a real, capacity-checked slot exists, and track
Execution Gaps in the matrix. Keep unrunnable environments in Complementary/
Scope-triggered tiers with their gaps named, and verify official requirements before
any environment becomes Required or claimed (DEC-S-067).

---

## RISK-052 — Evidence identity incompleteness

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

Evidence may omit exact versions, language, channel, revisions, scope, or review
identity and therefore become irreproducible or misleading.

### Impact

Evidence that only says `current` or `latest`, or that omits the reviewer or the
artifact revision, cannot be reproduced or contested; it asserts a result no one can
re-check. Under baseline drift such evidence quietly becomes false while still on the
record.

### Mitigation direction

Require immutable evidence records binding exact OS, browser/renderer, assistive
technology, input, language, channel, artifact/consumer revision, CDS version,
baseline version, date, executor, and reviewer (DEC-S-071). Separate product-family
rules from exact evidence identity (DEC-S-068). Carry a freshness state so stale
evidence is not read as current.

---

## RISK-053 — Regression coverage gap

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Changes may invalidate previously gathered accessibility evidence without triggering
targeted revalidation.

### Impact

Accessibility regresses silently — a token change removes contrast, an override
suppresses focus, a copied APG pattern drops a role — and the old evidence still
asserts a property the artifact no longer has. Without a revalidation trigger, the
record lies (this is the operational face of RISK-045).

### Mitigation direction

Bind evidence to a revision and hold that it **does not carry forward** across a
change to what it evidenced or to the baseline. Trigger targeted revalidation on any
change to a mandatory contract area and on any Blocking/High regression (Defect and
Regression Model; Maintenance Policy, DEC-S-070, DEC-S-072). Treat a regression as a
deviation, never a limitation.

---

## RISK-054 — Accessibility defect normalization

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: named per mitigation · Evidence Reviewer: Nova or authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Known barriers or failed combinations may be accepted informally, hidden in
aggregate reporting, or carried forward without explicit maturity and claim effects.

### Impact

A barrier that is quietly tolerated becomes permanent, and an aggregate or score
hides exactly the unmet criterion that makes a process unusable for a user group.
Informal acceptance turns the evidence model into paperwork that certifies comfort
rather than accessibility.

### Mitigation direction

Classify every defect on its own four-level impact scale, separate from risk
severity, and bind it to requirement, environment, evidence, scope, maturity, and
claim effects (DEC-S-072). Forbid numeric/percentage accessibility scores and
aggregate hiding (Evidence and Claims Model). Make `Accepted limitation` a
Human-Maintainer decision that stays visible in every affected claim, and trigger an
architecture/scope review on recurring limitations (DEC-S-059).

---

## RISK-055 — Token specification version drift

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

The pinned DTCG version may become outdated while later reports introduce changes
relevant to interoperability, types, references, or tooling.

### Impact

CDS pins DTCG 2025.10, but the Community Group will publish further reports. If CDS
drifts far behind, external tooling and consumers may expect newer behavior, and a
late catch-up upgrade could be large and breaking. The report is a CG report, not a
standard, so its evolution is not guaranteed stable.

### Mitigation direction

Pin only the stable 2025.10 reports (DEC-S-073, DEC-S-074) and treat later reports as
research inputs until a governed compatibility and migration decision accepts them
(DEC-S-082). Watch DTCG releases as a standards-watch item; re-verify the pinned
version's status before each format-affecting change. No upgrade is automatic.

---

## RISK-056 — Preview specification contamination

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Preview or draft DTCG behavior may be implemented or documented as if it were part of
the pinned stable profile.

### Impact

The DTCG preview drafts explicitly say "do not implement." A preview feature that
leaks into the normative profile ties CDS to shifting, unstable behavior and breaks
the pinned-stable guarantee — the format equivalent of building on sand.

### Mitigation direction

Hold that only pinned 2025.10 is authoritative (DEC-S-074); previews are for
status and future-change awareness only. Fail closed on use of a non-approved draft
feature (DEC-S-078). Keep stable and preview sources separated in the source register
and forbid preview features in the profile and any later implementation.

---

## RISK-057 — CDS profile divergence

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

CDS-specific restrictions or extensions may diverge from DTCG semantics and reduce
interoperability with external tools.

### Impact

CDS adds constraints and metadata a generic DTCG tool will not enforce or understand.
If CDS extensions or restrictions drift from DTCG semantics, sources may round-trip
incorrectly through external tools, eroding the interoperability that motivated
adopting DTCG.

### Mitigation direction

Constrain and extend only through documented, namespaced `$extensions` and added
validation gates; never redefine reserved DTCG semantics (DEC-S-076). Keep extensions
additive so a DTCG-only tool still reads a valid token. Document the profile centrally
and version it; treat divergence as a defect to reconcile, not a feature.

---

## RISK-058 — Schema-validation false assurance

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

A successful JSON Schema validation may be mistaken for complete token, semantic,
accessibility, governance, or interoperability correctness.

### Impact

A green schema result is attractive and cheap, and it is easy to read as "the tokens
are correct." But a schema checks structure, not meaning: semantic layer direction,
accessibility relevance, status truth, and governance traceability are beyond its
reach. A clean schema pass is fully consistent with a semantically wrong or
inaccessible token set.

### Mitigation direction

Enforce four separate validation layers (DEC-S-077, DEC-S-078); a V1/V2 or schema pass
proves no V3/V4 pass. Hold that a tool result is input to review, never approval
(DEC-S-053 applied to format), and that there is no aggregate score. Require V4
semantic and governance review, and Human-Maintainer approval, before any maturity or
claim.

---

## RISK-059 — Reference-resolution failure

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Cycles, dangling references, ambiguous resolution, type conflicts, or missing source
sets may produce invalid or misleading generated artifacts.

### Impact

A reference graph that resolves incorrectly can emit outputs that look valid but carry
wrong or missing values — a silent corruption that reaches consumers through generated
channel outputs. Ambiguous resolution order in multi-context theming is a particular
hazard.

### Mitigation direction

Fail closed on cycles, dangling references, type conflicts, and missing source sets
(DEC-S-078); no automatic repair. Require deterministic resolution order via the DTCG
resolver and the declared source-set graph (DEC-S-080). Make reference/cycle/type
checks part of the future validation contract and its negative fixtures (CDS-WP-012).

---

## RISK-060 — Cross-layer dependency violation

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Reference, Semantic, Component, Product Profile, or Channel layers may depend on one
another in prohibited directions and undermine the architecture.

### Impact

An upward or cyclic dependency — a component binding a reference token directly, or a
profile reaching into the core — silently strips meaning and defeats the five-layer
flow (DEC-S-024). The system becomes technically working but architecturally
incoherent, and theming/profiling foreclose.

### Mitigation direction

Make the downward dependency direction machine-checkable from declared layer and
dependency-set metadata (DEC-S-079); fail closed on any upward/cyclic dependency,
component→reference bypass, or profile→core redefinition (DEC-S-078). Encode these as
negative validation fixtures in CDS-WP-012.

---

## RISK-061 — Token identifier collision

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Case conversion, reserved characters, export transformation, renaming, or platform
constraints may cause distinct token identifiers to collide.

### Impact

Two identifiers that differ only by case, or that normalize to the same string on a
platform, silently overwrite each other in a generated output — a corruption that is
hard to detect and easy to ship. Reserved-character or empty-segment names break
tooling unpredictably.

### Mitigation direction

Enforce a restrictive, machine-validatable naming profile (DEC-S-081): no case-only
collisions, no reserved characters, no empty segments, a checkable segment syntax, and
a technical/display-label split. Treat renames as governed migration events
(DEC-S-082). Validate naming at V3.

---

## RISK-062 — Token provenance incompleteness

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Token sources or generated outputs may lack profile version, source revision,
dependency, transformation, approval, maturity, or provenance identity.

### Impact

An artifact whose origin cannot be established becomes functionally normative because
nobody can contradict it (RISK-025). A consumer integrating an output cannot tell what
it derived from, cannot reproduce it, and cannot know whether it is current; a
`latest`-only reference is unfalsifiable.

### Mitigation direction

Require complete identity on every source set and output — CDS profile version, DTCG
report version, immutable source revision, dependency set, transformation revision,
maturity, approval, provenance — and fail closed on a missing element (DEC-S-080). Ban
`latest` as an identity. No secrets or personal data in provenance.

---

## RISK-063 — Transformation-tool lock-in

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

A future transformation tool may introduce proprietary assumptions or extensions that
become de facto normative and obstruct offline or tool-neutral operation.

### Impact

If a transformation tool adds behavior or extensions the normative source depends on,
the tool quietly becomes the source of truth — the exact coupling DEC-S-004 forbids
(RISK-004) — and offline/self-hosted operation and reproducibility are lost.

### Mitigation direction

Keep the normative source strict-JSON DTCG and tool-independent (DEC-S-004, DEC-S-075);
require offline, deterministic, registry-free processing (DEC-S-030, DEC-S-080). Treat
any tool-specific assumption in a normative source as a defect. Select tools in a later
work package under explicit tool-neutrality and offline constraints; never let a
generated output or tool state become normative (DEC-S-079).

---

## RISK-064 — CDS schema contract incompleteness

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** Medium

### Description

The initial CDS schemas may fail to express required DTCG or CDS profile constraints and
therefore accept structurally misleading documents.

### Impact

A schema that under-constrains lets an invalid document pass V1/V3 structurally, and a
green schema result then reads as "correct" while the document violates DTCG semantics,
the profile, or governance. The gap is quiet because the tooling reports success.

### Mitigation direction

Keep the schemas as a bounded structural layer and hold that a schema pass proves no V2/
V3/V4 correctness (DEC-S-083, DEC-S-089). Cover known failure classes with negative
fixtures and validation cases; extend the schemas under governed change (DEC-S-082) as
gaps are found; require V4 human review before any maturity.

---

## RISK-065 — Synthetic fixtures mistaken for design tokens

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Test-only fixture names or values may be copied, distributed, or interpreted as approved
CDS design decisions.

### Impact

A synthetic placeholder read as a real token injects an unauthorized, unreviewed design
value into a consumer or a later build — the precise "premature design decision" the phase
forbids (RISK-003). Once copied, a fixture value is hard to retract.

### Mitigation direction

Mark every fixture `testOnly: true` and `nonNormative: true`, use `fixture/` IDs and
neutral placeholder values, and state the boundary in each fixture and in the validation
cases (DEC-S-087). Never publish fixtures as sources; keep them under `tests/fixtures/`.
No fixture is Candidate or approved.

---

## RISK-066 — Schema and validator divergence

- **Status:** Mitigating *(changed from `Monitored` by CDS-WP-013: the committed schemas and the offline validator are now bound by 15/15 expected/actual matches across VAL-CASE-001…015; executor-produced, independently unreviewed. Mitigation Executor: Claude (scoped, validator/harness maintenance).)*
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

A future validator may implement behavior that differs from the committed schemas or
validation-case expectations.

### Impact

If the validator and the schemas/cases disagree, "validated" means different things in
different runs, and the evidence is untrustworthy. Divergence is easy to introduce quietly
when the validator is built separately (CDS-WP-013).

### Mitigation direction

Treat the schemas and the validation-case matrix's
expected outcomes as the contract the validator must satisfy (DEC-S-089), and keep the
bootstrap Experimental until executed results match the declared expectations under
independent review (DEC-S-092). Re-verify on any schema/profile/DTCG change (RISK-071).

---

## RISK-067 — Canonicalization and digest mismatch

- **Status:** Mitigating *(changed from `Monitored` by CDS-WP-013: RFC 8785 canonicalization invariance tests (indentation, key order, value change, duplicate-key, unsupported input) pass on the exactly pinned `rfc8785` implementation; executor-produced. Mitigation Executor: Claude (scoped, canonicalization tests).)*
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Different implementations may canonicalize or hash the same logical JSON content
differently and produce conflicting identities.

### Impact

If two tools compute different digests for the same content, content identity becomes
unreliable and reproducibility — the point of the digest — is lost. Divergence typically
comes from number formatting, key ordering, or Unicode handling.

### Mitigation direction

Fix a specified canonicalization (RFC 8785 / JCS) plus SHA-256 (DEC-S-090, ADR-0002) so
independent implementations agree; compute digests from the parsed content, not authoring
bytes; require offline deterministic computation. Validate digest reproducibility in
CDS-WP-013 before any digest is used as evidence.

---

## RISK-068 — Duplicate-key ambiguity

- **Status:** Mitigating *(changed from `Monitored` by CDS-WP-013: every validator JSON input uses the single duplicate-key-rejecting loader, and the duplicate-key fixture is blocked at V1 in the executed harness; executor-produced. Mitigation Executor: Claude (scoped, loader maintenance).)*
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Parsers without duplicate-key detection may silently accept invalid CDS sources using
first-key-wins or last-key-wins behavior.

### Impact

A duplicate member silently overwrites a value, so the source that ships differs from the
source that was reviewed — an undetected corruption. JSON Schema alone cannot catch this.

### Mitigation direction

Prohibit duplicate object member names and fail them at V1 without repair (DEC-S-088);
require the future validator to use a duplicate-key-aware parser; encode the case as a
negative fixture. Never rely on first/last-key-wins.

---

## RISK-069 — Manifest and resolver graph inconsistency

- **Status:** Mitigating *(changed from `Monitored` by CDS-WP-013: manifest, resolver, cycle, and layer-direction cases are recognized exactly as expected in the executed harness (VAL-CASE-005/006/007/010/011); executor-produced. Mitigation Executor: Claude (scoped, graph validation).)*
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Token documents, Source-Set manifests, resolver order, embedded identities, and dependency
declarations may drift apart.

### Impact

If the manifest's declared graph, the per-entry dependencies, the embedded source-set
identities, and the resolver order disagree, resolution produces wrong or unpredictable
output while every individual file looks valid.

### Mitigation direction

Require the manifest to declare identity, layer, path, dependencies, and a dependency graph
consistent with per-entry dependencies, and require manifest ↔ document identity agreement
(DEC-S-085); the resolver references only declared source sets (DEC-S-086). Cross-check
consistency at V3 and fail closed on mismatch.

---

## RISK-070 — Validation fixture coverage gap

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

The positive and negative fixtures may omit important profile, reference, type, layer,
metadata, or interoperability failures.

### Impact

A failure class with no fixture is a validation blind spot: a future validator may pass it
by omission, and the contract's "coverage" is overstated. Coverage gaps are invisible until
a real document hits the untested case.

### Mitigation direction

Bind every fixture to a validation case and keep the case matrix the visible coverage
record (DEC-S-089); extend fixtures and cases under governed change as new failure classes
are identified; state known coverage gaps honestly rather than implying completeness.

---

## RISK-071 — Validation expectation drift

- **Status:** Mitigating *(changed from `Monitored` by CDS-WP-013: actual results are machine-compared against the committed expected results and stored revision-bound in `artifacts/validation/wp013-fixture-results.json`; executor-produced. Mitigation Executor: Claude (scoped, harness reporting).)*
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Expected V1…V4 outcomes may become stale after profile, DTCG, schema, or governance
changes.

### Impact

Stale expected outcomes make the validation cases assert the wrong result, so a validator
"passing" the suite proves the wrong thing — or a correct change is flagged as a
regression. The record silently decays.

### Mitigation direction

Treat the expected outcomes as revision-bound and re-verify them on any profile, DTCG,
schema, or governance change (DEC-S-089, DEC-S-082); keep the case matrix under governed
change; bind cases to the applicable Decision and Risk IDs so impact is traceable.

---

## RISK-072 — Digest mistaken for authenticity

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

A matching content digest may be treated as proof of authorship, approval, trust,
security, or release legitimacy.

### Impact

A digest proves only that content is unchanged, not who made it, whether it was approved,
or whether it is safe to ship. Reading a digest as a signature or an approval would let an
unreviewed, unapproved artifact circulate as trusted.

### Mitigation direction

Hold that a content digest is an integrity/reproducibility aid only — not a signature and
not proof of authorship, approval, trust, security, or release (DEC-S-090, ADR-0002). A
digest never replaces the immutable source revision, approval, or provenance evidence, and
never confers Candidate/Stable or a claim.

---

## RISK-073 — Validator dependency supply-chain exposure

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

The validator depends on external Python packages whose provenance, maintenance,
transitive dependencies, or compromise could affect validation trust.

### Impact

A compromised or silently changed dependency can alter validation outcomes, forge or
weaken digests, or exfiltrate content — and its output would still read as a trusted
green result. Validation trust then rests on an unaudited third party instead of the
committed CDS contracts.

### Mitigation direction

Pin every direct and transitive dependency to an exact version in
`requirements-validator.lock` (DEC-S-093); install only into a temporary environment
outside the repository; keep the runtime fully offline; document provenance in the
[Dependency Source Register](../research/OFFLINE_VALIDATOR_DEPENDENCY_SOURCE_REGISTER.md);
upgrade only through a governed change with re-run evidence (ADR-0003).

---

## RISK-074 — Partial DTCG coverage overstated

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

The implemented DTCG subset may be represented as complete DTCG-2025.10 validation.

### Impact

A "V2 Pass" read as full DTCG conformance would let documents that violate unimplemented
DTCG rules (color-module value semantics, resolver modifier semantics, composite-type
internals) circulate as DTCG-clean, and would turn the bounded validator into an
unearned conformance authority.

### Mitigation direction

Bound V2 explicitly to the pinned subset required by the CDS profile and committed
fixtures (DEC-S-098); report unsupported DTCG areas as limitations in every
machine-readable result; never emit or accept a "full DTCG conformance" statement from
validator output (DEC-S-044).

---

## RISK-075 — Runtime reproducibility gap

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Different Python, dependency, operating-system, locale, or filesystem environments may
produce different validation behavior.

### Impact

Evidence produced on one machine may not reproduce on another; a divergence between
environments silently undermines the deterministic-resolution guarantee (DEC-S-080) and
makes expected/actual comparisons environment-dependent instead of contract-dependent.

### Mitigation direction

Bind every execution report to the exact runtime and dependency identities
(DEC-S-101); pin dependencies exactly; avoid locale-, ordering-, and
path-separator-dependent logic; treat a cross-environment divergence as a defect, never
as tolerable noise. Independent re-execution in a second environment is future review
work.

---

## RISK-076 — Duplicate-key loader bypass

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

A future code path may bypass the controlled loader and silently accept duplicate object
member names.

### Impact

A bypassing path re-introduces first-key-wins/last-key-wins ambiguity (RISK-068): the
same document then parses differently in different code paths, and a V1-invalid source
can reach V2–V4 or receive a digest it must never have.

### Mitigation direction

Route every JSON input through the single controlled loader (DEC-S-095); prohibit direct
`json.load` paths in the validator; cover the loader and the duplicate-key fixture in
unit tests and the harness; review any new input path against this rule before merge.

---

## RISK-077 — Diagnostic contract instability

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Diagnostic identifiers or meanings may change and make automation or evidence comparison
unreliable.

### Impact

If `CDS-V…` codes or their meanings drift, stored evidence, case expectations, and any
future automation compare against a moving target; historical reports become
unintelligible and regression detection silently breaks.

### Mitigation direction

Treat the diagnostic code set as a published contract: codes are added, never silently
renamed or redefined; changes run through governed change control (DEC-S-082) with a
migration note; every report binds the validator version so old evidence stays
interpretable (DEC-S-101).

---

## RISK-078 — Fixture expectation self-confirmation

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

The implementation and expected outcomes may reinforce the same mistaken assumption
without independent review.

### Impact

When the same executor writes the fixtures, the expected outcomes, and the validator, a
shared misunderstanding produces a green 15/15 harness that proves internal consistency,
not correctness. The error becomes invisible precisely because everything agrees.

### Mitigation direction

Keep expected outcomes committed and unchangeable by the implementation (DEC-S-102);
record every harness result as executor-produced and independently unreviewed
(DEC-S-103); require a separately authorized Evidence Review before any maturity
transition (DEC-S-104); never let the executor review its own evidence (DEC-S-045).

---

## RISK-079 — Offline-boundary regression

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Low
- **Initial severity:** High

### Description

A dependency or future feature may introduce remote schema, registry, telemetry, or
reference access.

### Impact

A single network-touching path breaks the offline guarantee (DEC-S-093), makes
validation results dependent on external availability and mutable remote content, and
can leak private development content — all invisibly, because the result still renders
locally.

### Mitigation direction

Keep the schema registry local-only and fail closed on unknown identities (DEC-S-096);
reject network references at V1; add no dependency without governed review (ADR-0003);
verify on every dependency upgrade that no network path was introduced.

---

## RISK-080 — Validation-result provenance gap

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Execution reports may omit runtime, dependency, input, revision, digest, or review-state
identity.

### Impact

A result without complete provenance cannot be tied to what was actually validated,
with what, by whom, in which state — it becomes unusable as evidence and dangerous as a
basis for review or maturity decisions (RISK-072 applied to reports).

### Mitigation direction

Require the CDS-owned result schema for every machine-readable report (DEC-S-101):
runtime, dependency, schema, profile, DTCG, case, source-revision, digest, worktree, and
review-state identities are mandatory; a worktree execution is never presented as a
committed revision; schema-validate every report before use.

---

## RISK-081 — Validator evidence mistaken for Candidate approval

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

A successful fixture harness may be communicated as Candidate, Stable, token, consumer,
or product conformance.

### Impact

A green harness is fifteen synthetic observations about a bounded contract — nothing
more. Read as an approval, it would skip independent review, Nova review, and the
Human-Maintainer maturity gate (DEC-S-104), and would create exactly the unearned claim
DEC-S-044 prohibits.

### Mitigation direction

Bind every report to `independentReviewState: pending` and an executor-produced evidence
class (DEC-S-103); hold that harness success is a successful observation, never a
passing token artifact or maturity transition (DEC-S-102, DEC-S-104); keep all claim
language prohibited (DEC-S-044).

---

## RISK-082 — Status-axis conflation

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** High

### Description

Consumers or implementations may collapse condition, severity, confidence,
freshness, or evidence into a single ambiguous status.

### Impact

A merged status destroys exactly the information the axes protect: unknown has
nowhere to live and becomes a false green or a false alarm; a claim and a guess
become indistinguishable. The operator acting on a green that means "we have no
idea" is the failure the entire foundation exists to prevent (DEC-S-028).

### Mitigation direction

Keep the five axes independent and named (DEC-S-105); prohibit irreversible token
aggregation ([Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md));
cover conflation with future negative fixtures; treat any collapsing
transformation as fail-closed (DEC-S-112).

---

## RISK-083 — Unknown-state optimism

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** High
- **Initial severity:** High

### Description

Unknown or unavailable information may be displayed or interpreted as nominal,
successful, current, or verified.

### Impact

Silent-positive defaults are the most dangerous truthfulness failure: they are
invisible precisely when they are wrong, and they train users to trust green
states that carry no knowledge. Every downstream decision inherits the false
optimism.

### Mitigation direction

`unknown` is explicit on every axis and never an omitted default (DEC-S-106,
DEC-S-107); a missing axis fails closed; future fixtures must prove
unknown-never-validates-as-positive; communication rules require perceivable,
non-visual unknown language (baseline 7.4).

---

## RISK-084 — Aggregate-status masking

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

A summary status, score, badge, color, or icon may hide material limitations on
one or more axes.

### Impact

An aggregate that swallows a stale, unverified, or evidence-free qualifier
converts an honest multi-axis state into an overclaim — the summary becomes the
lie even though every underlying value is true.

### Mitigation direction

No normative aggregate health score (DEC-S-108); disclosure priority orders
attention without overriding semantics; summaries must carry material qualifiers
and offer full five-axis disclosure
([Communication Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md)).

---

## RISK-085 — Status-combination ambiguity

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Valid but unusual combinations may be treated as contradictions, while actually
contradictory combinations may pass without rationale.

### Impact

Both directions damage truth: rejecting honest-but-unusual states (nominal with
stale knowledge) forces false simplification, while accepting unexplained
contradictions (verified without evidence) lets overclaims through unreviewed.

### Mitigation direction

Explicit review-required combinations with mandatory rationale, and explicit
fail-closed states — kept distinct (DEC-S-109,
[Composition Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md));
future fixtures exercise both directions.

---

## RISK-086 — Status-localization drift

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Localized labels or descriptions may change or weaken the normative meaning of a
status value.

### Impact

A DE label that reads `supported` as *geprüft* (verified) or renders `unknown`
as a neutral positive silently breaks the truthfulness invariants for every
German-language user while the English contract stays formally intact.

### Mitigation direction

Language-neutral technical IDs separate from localized labels (DEC-S-110);
DE/EN semantic parity with prohibited contradictory translations; parity review
as Candidate evidence; label changes never change meaning without a governed
vocabulary change.

---

## RISK-087 — Visual-only status encoding

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Status meaning may rely on color, icon, position, shape, or motion without an
equivalent textual and semantic representation.

### Impact

Meaning that lives only in a visual channel fails assistive technology,
greyscale documents, and reduced-motion users — and fails silently: the sighted
majority never notices the loss. This also breaks the non-interactive channels
architecturally (channel consistency).

### Mitigation direction

Text-first meaning with accessible semantics; visual channels are redundant
modalities only (DEC-S-111); non-visual perceivability of unknown/freshness/
confidence is a normative baseline requirement (7.3/7.4); future accessibility
evidence must cover non-visual expression.

---

## RISK-088 — Consumer status remapping divergence

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Consumer Extensions or Product Profiles may rename, merge, or remap status
values in ways that break CDS meaning and evidence traceability.

### Impact

A remapped status severs the traceability chain (which CDS value did this
represent?) and can invert truthfulness locally — one consumer's "OK" may be
another's `unknown`. Divergence is invisible at the CDS layer and surfaces as
inconsistent operator behavior across products.

### Mitigation direction

Meaning-preserving mappings only; approved extension points only; remappings
with meaning loss fail closed (DEC-S-112, fail-closed state 8); the CDS/consumer
semantic boundary (CR-035) stays an explicit open question, not a blur zone;
future CoreOps reconciliation is read-only, revision-bound evidence.

---

## RISK-089 — First-candidate scope expansion

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

The initial Semantic Status Foundation Candidate may expand into visual
foundations, components, Product Profiles, or CoreOps implementation before its
contract and evidence are ready.

### Impact

Scope creep at the first Candidate would smuggle unreviewed design decisions in
under the momentum of the status work — precisely the premature design decision
the phase forbids (RISK-003) — and would dilute the evidence discipline the
first promotion is meant to establish.

### Mitigation direction

Fixed Candidate scope and exclusions with expansion as a NO-GO trigger
(DEC-S-113, [Candidate Plan](../roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md));
ten cumulative prerequisites (DEC-S-114); visual values enter only through a
later explicitly authorized design work package.

---

## RISK-090 — Status source and contract drift

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

The machine-readable Semantic Status Source Set may diverge from the human-readable
contract, vocabulary, or invariants.

### Impact

A drifted source silently redefines the meaning foundation: tokens and contract
then disagree about the same identifier, and every consumer inherits whichever
side it happens to read — the exact dual-source conflict DEC-S-034 fails closed.

### Mitigation direction

Keep the vocabulary/source 1:1 mapping machine-verified (DEC-S-117, unit-tested);
run the status V4 checks on every change; treat any disagreement as an invalidating
conflict (DEC-S-034), never resolved by recency.

---

## RISK-091 — Semantic status tokens mistaken for visual tokens

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

Consumers may treat non-visual status identity tokens as direct color, icon,
component, or presentation values.

### Impact

A consumer binding `status.condition.nominal` to a colour turns a meaning
identifier into an appearance value, bypassing the still-missing visual layer and
recreating colour-as-sole-carrier failures (CR-006) under a CDS name.

### Mitigation direction

Non-visual `string` identity values only (DEC-S-116); visual-leakage validation
(CDS-V4-STATUS-VISUAL-LEAKAGE); the token contract's role boundary; future visual
bindings arrive only through an authorized design work package.

---

## RISK-092 — Status token path migration instability

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Low
- **Initial severity:** High

### Description

Changes to status token paths, axis IDs, or value IDs may break references,
localization mappings, validation evidence, or consumer integrations.

### Impact

The 25 IDs are the anchor for the terminology mapping, the fixtures, the case
matrix, and future consumer bindings; an unmanaged rename desynchronizes all of
them at once and silently invalidates recorded evidence.

### Mitigation direction

Stable IDs with renames as governed migration events (DEC-S-082, DEC-S-117);
path/value and collision validation; evidence binds revisions and digests so drift
is detectable (DEC-S-123).

---

## RISK-093 — Semantic validator blind spot

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

The status-specific validator may enforce the fixed vocabulary while missing
meaning loss, misleading summaries, localization drift, or channel-level
truthfulness failures.

### Impact

A green status validation covers the vocabulary shape only; a UI can still render
`unknown` as a friendly green dot without any validator objection — shape-valid,
truth-broken.

### Mitigation direction

State the coverage boundary explicitly in every review (DEC-S-121); keep
communication/channel truthfulness in the human review scope of the Candidate
gates (prerequisites 6–8); never present a validator pass as truthfulness
evidence.

---

## RISK-094 — Semantic fixture overfitting

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

The validator may match the committed status fixtures while failing to detect
unrepresented invalid states or future profile variations.

### Impact

Nine negative fixtures exercise nine failure classes; invalid states outside them
(combined defects, structural oddities, future profile changes) may pass unnoticed
while the 24/24 result reads as complete coverage (RISK-070 pattern at the status
layer).

### Mitigation direction

Treat the fixture set as a floor, not a proof (DEC-S-102); extend fixtures under
governed change when new failure classes are identified; keep the independent
review focused on unrepresented states.

---

## RISK-095 — Status localization parity false assurance

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** Medium

### Description

A complete DE/EN mapping may be mistaken for validated comprehension, usability, or
cultural suitability.

### Impact

25/25 parity rows prove structural completeness and executor-assessed meaning
parity — not that any German or English speaker understands the labels correctly.
Acting on the mapping as usability evidence repeats the documentation-as-user-
research failure (RISK-017).

### Mitigation direction

Label the parity review as executor-produced structural evidence (DEC-S-121);
keep comprehension validation an explicit open Candidate concern; no claim of
validated understandability.

---

## RISK-096 — Candidate dossier completeness illusion

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

A populated Candidate Dossier may be treated as Candidate approval despite open
independent-review and Human-Maintainer gates.

### Impact

The dossier now contains real evidence links and looks finished; reading
completeness as approval would skip exactly the review and approval steps that
distinguish evidence from a decision (RISK-081 pattern at dossier level).

### Mitigation direction

Explicit `Draft – Candidate gate incomplete` status with a gate-state table
(DEC-S-122); the decision field stays empty; unclear readiness is NO-GO
(DEC-S-048).

---

## RISK-097 — Experimental status source consumed prematurely

- **Status:** Monitored
- **Roles:** per the finalized model — Accountable Risk Owner: Human Maintainer · Risk Controller: Nova · Mitigation Executor: scope-dependent · Evidence Reviewer: Nova or separately authorized reviewer
- **Initial likelihood:** Medium
- **Initial severity:** High

### Description

Consumers may integrate or distribute the Experimental Semantic Status Source Set
before Candidate approval.

### Impact

Early consumption freezes unreviewed identifiers into products, creates de-facto
compatibility pressure against a source that may still change, and turns the
Experimental state into an implicit claim (DEC-S-044 violation by usage).

### Mitigation direction

Prohibit representing the source as approved before the gate (DEC-S-124); keep the
approval-statement check active at the source; publication state stays
`Private Development`; consumer integration remains unauthorized until the gate
succeeds.
