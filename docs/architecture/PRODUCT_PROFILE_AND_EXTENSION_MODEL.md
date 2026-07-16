# Product Profile and Extension Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-005 — Design System Architecture
- **Date:** 2026-07-16
- **Status:** **Normative** for the extension structure

## Purpose

This document defines how CDS permits variation without fragmenting.

It answers the question the benchmark left open: **every mature system permits
product variation; none published its limits.** CDS publishes them.

It also answers a fact from consumer evidence: **SpeakCore and CastCore already
hold their own product-local design decisions and token sets** (CR-002, CR-037).
CDS is not starting on a blank slate — it is arriving late, and the architecture
must say what that means.

Frame: [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md).

## The five constructs

*(Normative)*

| Construct | Owner | Binding | Becomes CDS? |
| --- | --- | --- | --- |
| **Core Foundation** | CDS | Mandatory for all consumers | Is CDS |
| **Product Profile** | CDS (approved), applied by consumer | Bounded, at approved extension points | Governed part of CDS |
| **Consumer Extension** | Consumer | None on CDS | Only via explicit acceptance |
| **Domain Pattern Family** | CDS (optional module) | Only for adopters of that domain | Part of CDS, **not** of the universal foundation |
| **Local Exception** | Consumer, CDS-recorded | Time- or scope-bounded | No — it is a tracked deviation |

### Core Foundation

The shared, mandatory basis. Common semantics, status foundations, component
contracts, accessibility guarantees.

A consumer does not opt out of the Core Foundation. If a consumer cannot accept
it, that is a signal about the foundation — not a licence to diverge quietly.

### Product Profile

Controlled, approved product-specific expression.

A Product Profile **may**:

- override values at **explicitly approved extension points** (DEC-S-024,
  layer 4),
- express product identity within the family,
- select among approved options.

A Product Profile **may not**:

- redefine shared semantics,
- weaken accessibility requirements (invariant 10),
- distort status truth — see the Unknown invariant,
- break consumer contracts,
- create an independent, incompatible design world (RISK-027).

The last four are absolute. A profile that needs any of them is not a profile; it
is a fork, and must be named as one.

### Consumer Extension

Product-specific building blocks outside the shared core. **Remains
consumer-owned** unless explicitly accepted into CDS (DEC-S-016).

Consumer extensions are legitimate and expected. Most product-specific work
should live here permanently — CDS absorbing everything is the failure mode
(Non-goal 11, RISK-016), not the goal.

### Domain Pattern Family

An **optional, generalizable pattern set** for an application domain — for
example, operations.

*(Normative, DEC-S-027)*

- Sits **above** the generic foundations and components, never inside them.
- Is **not automatically part of the universal foundation** (invariant 11).
- Adopted only by consumers in that domain.
- Requirements from a domain family must not push down into Layers 3 or 4
  without multi-consumer evidence from **outside** that domain.

This construct exists for a specific, evidenced reason. All three reviewed
consumers are infrastructure products, so the operations evidence is strong
(HYP-003: *Confirmed consumer need*) while its generalizability is **entirely
untested** — the sample cannot distinguish "operational products need this" from
"all products need this" (RISK-016, RISK-023). Modelling operations as a domain
family lets CDS serve that real need without silently redefining itself as an
operations design system.

### Local Exception

A time- or scope-bounded deviation. Must record:

- reason,
- owner,
- scope,
- affected CDS version,
- review or expiry point,
- migration or acceptance decision.

An exception without an expiry is not an exception — it is an undocumented fork.
**Detailed exception governance is deferred to CDS-WP-006.**

## Override categories

*(Normative)*

### Permitted

| Category | Condition |
| --- | --- |
| Value override at an approved extension point | Point is explicitly approved |
| Selection among approved options | Options defined by the core |
| Product identity expression | Within brand governance (Layer 2) |
| Additive consumer extension | Outside the core; consumer-owned |
| Domain family adoption | Consumer is in that domain |
| Recorded local exception | Bounded, owned, expiring |

### Forbidden

| Category | Why |
| --- | --- |
| Redefining shared semantics | Destroys the common meaning that makes CDS a system |
| Weakening accessibility | Invariant 10 — a profile must never remove a guarantee |
| Distorting status truth | Unknown must not read as healthy (invariant 7) |
| Breaking a consumer contract | Contracts are the interface |
| Silent divergence | An unrecorded deviation is indistinguishable from a fork |
| Overriding to fill a core gap | The gap is the finding; raise it |
| Reaching past extension points into the core | Inverts the dependency direction |
| Creating an independent design system | RISK-027 — the outcome this model exists to prevent |

## Anti-fragmentation rules

*(Normative)*

1. **Extension points are named, finite, and approved.** Anything not named is
   not an extension point.
2. **Additive beats overriding.** A consumer extension alongside the core is
   safer than an override inside it.
3. **A gap is a finding, not an override.** If several consumers override the
   same thing, the core is wrong — fix the core.
4. **Every deviation is visible.** Exceptions are recorded and expire.
5. **Domain families stay above the foundation.**
6. **Generalization requires the gate** — multi-consumer relevance or documented
   rationale, a principles check, explicit acceptance, and the ability to
   document, test, and version (DEC-S-016). Origin in any one consumer, including
   the pilot, is never sufficient.
7. **Profile count is a governed quantity.** Profiles and exceptions can multiply
   faster than they can be governed (RISK-021, RISK-027); the governance is
   CDS-WP-006's to set.

## Existing-product reconciliation

*(Normative, DEC-S-026)*

CDS arrives after SpeakCore and CastCore have shipped their own design decisions.
The architecture treats this as the normal case.

### Reconciliation flow

| # | Step | Produces |
| --- | --- | --- |
| 1 | **Inventory** | What product-local decisions exist |
| 2 | **Semantic Mapping** | What each decision *means*, expressed in shared semantic terms |
| 3 | **Conflict Identification** | Where meaning genuinely diverges from the core |
| 4 | **Classification** | Which of the outcomes below applies |
| 5 | **Product Profile Candidate** | Belongs in the family, at an extension point |
| 6 | **Consumer-local Retention** | Legitimately stays with the product |
| 7 | **Migration Candidate** | Should converge, over time, with a versioned path |
| 8 | **Evidence and Review** | Recorded outcome and rationale |

Step 2 is the load-bearing one. Mapping is **semantic, not value-level**: the
question is "what did this decision mean?", never "is this value right?".

### Reconciliation rules

- **No automatic adoption.** A consumer decision does not become CDS by existing.
- **No automatic overwrite.** CDS does not replace a shipped decision by
  appearing (invariant 14).
- **No retrospective conformance.** Existing consumer designs are not certified
  by CDS after the fact.
- **No evaluation of concrete consumer values in this work package.** The
  architecture defines the flow; it judges nothing.
- **Product-local decisions may legitimately persist.** Retention is a valid,
  final outcome — not a failure.
- **Reusable insight requires explicit acceptance** (DEC-S-016).
- **Migration must later be versioned, documented, and reversibly planned.**

### Relationship to SpeakCore and CastCore

Registered as **fact**, without inspecting their values:

- Both hold their own style direction, palette, and token sets (CR-002, CR-037,
  classified `Product-local Requirement`).
- Their authoritative token and brand sources were **outside the permitted read
  areas in CDS-WP-004 and were not read**. The architecture therefore knows *that*
  they exist, not *what they contain*.
- They are **Consumer-local Artifacts** (authority class 7): not CDS, not
  overrides, not defects.
- They are secondary consumers — evidence, not pilot authority (DEC-S-018).
- Whether any of it converges is a **later, evidence-based decision** under this
  flow.

Failing this reconciliation — overwriting, mapping incompletely, or forcing
convergence without migration and evidence — is RISK-022.

## Future migration and governance dependencies

**Deferred to CDS-WP-006:**

- which extension points are approved, and who approves them,
- Product Profile governance, review, and revocation,
- exception governance, expiry, and escalation,
- the acceptance process behind DEC-S-016,
- profile and exception limits,
- the versioning model that makes migration plannable,
- the compatibility model that makes it safe.

**Deferred to CDS-WP-007:** the accessibility target a profile may not weaken.
The guarantee is architectural (invariant 10); its **level** is undefined
(CR-024). Until then, a profile must not weaken an accessibility requirement
whose value is not yet known — a constraint that is real but currently
unmeasurable, and part of RISK-028.

## Related documents

- [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md)
- [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md)
- [Consumer Contract and Reconciliation Model](CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md)
- [Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)
