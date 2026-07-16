# Governance Operating Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-006 — Governance, Versioning, Contribution, Risk and Publication Model
- **Date:** 2026-07-16
- **Status:** **Normative** for roles, authority, and approval gates

## Purpose and authority

This document is the **normative source for how CDS is governed**: who decides
what, who reviews, who executes, and what may never be delegated.

It operationalizes the architecture from CDS-WP-005 without selecting any
technology or design. Where CDS-WP-005 defined *structure*, this document defines
*who may change it and under what conditions*.

It is the governance entry point. The specialised policies listed under
[Related documents](#related-documents) hold the detail.

## Governance principles

1. **Authority is granted, never acquired.** No role gains authority by creating,
   editing, implementing, using, or citing an artifact (DEC-S-033).
2. **Review and approval are separate acts.** The reviewer recommends; the
   approver decides. One person may hold both roles only where explicitly
   permitted, and never silently.
3. **Fail closed.** Unclear authority, unclear evidence, or an unresolved
   conflict stops the process. It does not default to permission.
4. **Ceremony scales; obligations do not.** Governance effort is proportional to
   risk. The mandatory gates are not.
5. **Nothing self-promotes.** No artifact, claim, profile, exception, or risk
   changes state on its own authority.
6. **Honesty over convenience.** A conservative statement backed by evidence
   beats a confident one that is not.
7. **Governance must be affordable.** A process the maintainer cannot run is not
   governance — it is theatre (RISK-026, RISK-040).

## Roles

*(Normative, DEC-S-033)*

Six roles. Each is a **function**, not a person — one person may hold several,
but the separation of duties below still applies.

### Human Maintainer

**Accountable, and the final approving authority.**

Exclusively decides: normative approvals · risk acceptance · commit, push, merge,
branch operations, tag, release · publication · licensing · repository
visibility · Product Profile acceptance · exception acceptance · adoption and
conformance approvals · Candidate and Stable transitions.

This authority is **not delegable** to Nova, Claude, a contributor, or an
automated process.

### Nova

**Governance Controller, Risk Controller, and independent review role.**

Provides: strategic governance control · risk control · review · project
control · approval recommendations · scope and consistency checks · prompts.

Nova **recommends; it does not decide**. Nova holds no Git authority, no
publication authority, and cannot accept a risk or approve a claim.

### Claude

**Scoped executor.**

Performs only: local analysis · policy documentation · register maintenance ·
quantitative validation · structured reporting.

Claude may **not**: activate a policy · accept a risk · approve a maturity state ·
approve a release or claim · perform any Git write action. Claude's output is
always a proposal.

### Consumer Maintainer

**Accountable within their own project** for: correct CDS integration · consumer
evidence · local deviations · migration execution · consumer-owned artifacts ·
honest adoption claims.

Consumer Maintainers hold **no CDS core approval authority**.

### Contributor

May supply proposals, evidence, or implementations. Holds **no acceptance
authority**. A contributor never approves their own contribution.

### Evidence Reviewer

Checks evidence against a defined contract.

May be filled by Nova or a later explicitly authorized reviewer. **The role may
never be filled by the artifact itself** — an artifact asserting its own evidence
has not been reviewed.

## Authority matrix

*(Normative)*

| Act | Human Maintainer | Nova | Claude | Consumer Maintainer | Contributor | Evidence Reviewer |
| --- | --- | --- | --- | --- | --- | --- |
| Normative approval | **Decides** | Recommends | Proposes | — | — | — |
| Candidate / Stable transition | **Decides** | Reviews | Proposes | Supplies evidence | — | Reviews evidence |
| Risk acceptance | **Decides** | Recommends | — | — | — | — |
| Risk closure | **Decides** | Reviews | Proposes | — | — | Reviews evidence |
| Contribution acceptance | **Decides** | Reviews | Proposes | — | Submits | Reviews evidence |
| Exception approval | **Decides** | Reviews | Proposes | Requests | — | Reviews evidence |
| Product Profile acceptance | **Decides** | Reviews | Proposes | Requests | — | Reviews evidence |
| Adoption / conformance claim | **Approves** | Reviews | — | **Makes the claim** | — | Reviews evidence |
| Release / tag | **Performs** | Recommends | **Never** | — | — | — |
| Publication state change | **Decides** | Recommends | — | — | — | — |
| Licensing decision | **Decides** | Recommends | — | — | — | — |
| Git write | **Exclusive** | **Never** | **Never** | Own repo only | — | — |
| Consumer integration | — | — | — | **Accountable** | — | — |

## Governance tracks

*(Normative)*

Two tracks. **Both carry the same mandatory gates.** Only scope and ceremony
differ.

### Standard Track

For: corrections · clearly bounded non-breaking additions · low-risk
documentation changes.

Lighter ceremony: a single review pass, no separate evidence bundle where the
change carries no evidence obligation, and consolidated approval.

### Elevated Track

**Mandatory** for: breaking changes · Stable artifacts · accessibility
obligations · Product Profiles · exceptions · adoption or conformance claims ·
licensing and publication decisions · removal · security- or legally relevant
changes.

Full ceremony: explicit evidence, separate review, documented rationale, and
individual Human Maintainer approval.

### The proportionality rule

*(Normative — the load-bearing sentence of this section)*

**Proportional governance scales ceremony, never obligation.** In both tracks the
following remain mandatory and may not be reduced:

- authority boundaries (only the Human Maintainer approves),
- traceability to a source revision,
- evidence where an evidence obligation exists,
- Human approval before anything becomes normative,
- fail-closed on unclear authority or evidence.

A Standard Track change is **smaller**, never **less governed**. If a change
looks Standard but touches an Elevated trigger, it is Elevated — the trigger
wins, not the estimate.

## Approval gates

*(Normative)*

| Gate | Requires | Approver |
| --- | --- | --- |
| **Candidate** | Candidate gate criteria met | Human Maintainer after Nova review |
| **Stable** | Stable gate criteria met | Human Maintainer after Nova review |
| **Contribution acceptance** | Scope, evidence, architecture and governance review | Human Maintainer |
| **Exception** | Scope, owner, risk assessment, expiry | Human Maintainer |
| **Product Profile** | Extension points, evidence, anti-fragmentation review | Human Maintainer |
| **Claim** | Scope, versions, evidence bundle | Human Maintainer after Nova review |
| **Risk acceptance** | Rationale, scope, residual effect, review trigger | Human Maintainer |
| **Release** | Release candidate requirements | Human Maintainer |
| **Publication state change** | Publication gate | Human Maintainer |

Gate criteria live in the specialised policies. No gate may be satisfied by the
artifact's own assertion.

## Separation of review and approval

*(Normative)*

- **Review** establishes whether criteria are met. **Approval** decides whether
  to proceed. They are different acts and are recorded separately.
- Nova reviews; the Human Maintainer approves. A Nova review is never an
  approval, and an approval without review is a gap to record — not a shortcut
  to normalise.
- A contributor never approves their own contribution.
- An automated check is **input to** a review, never the review itself. A green
  build, a clean diff, and a passing validation are evidence — not consent.

## Consumer governance boundary

*(Normative)*

CDS governs **CDS**. Consumers govern **their products** (DEC-S-008).

- A Consumer Maintainer is accountable for integration, local deviations,
  migration, and honest claims within their project.
- A Consumer Maintainer holds no CDS core approval authority.
- Consumer usage never creates CDS acceptance (DEC-S-041).
- CDS does not govern consumer-local artifacts, and does not retrospectively
  certify them (DEC-S-026).
- A consumer may request; only CDS may accept.

## Escalation

*(Normative)*

Escalate — do not resolve locally — when:

- authority is unclear,
- normative sources conflict (DEC-S-034),
- evidence is missing, contradictory, or unreviewable,
- a change looks Standard but touches an Elevated trigger,
- a role would have to approve its own work,
- an exception would weaken accessibility or status truth,
- a claim cannot be substantiated,
- a risk requires acceptance.

Path: **Claude records and reports → Nova reviews and recommends → Human
Maintainer decides.**

While an escalation is open the affected state is **not releasable and not
distributable**.

## Governance capacity

*(Normative constraint, not an aspiration)*

Final authority currently rests with **one Human Maintainer**. This is a
deliberate choice (DEC-S-005) and a real bottleneck (RISK-029).

Consequences that must stay true:

- Governance must be sized to that reality — the benchmark's most rigorous
  practices come from publishers with dedicated teams (RISK-011), and copying
  their ceremony without their capacity produces RISK-040: a register that is
  updated but drives nothing.
- The Standard Track exists to keep low-risk work moving.
- Ceremony that produces no decision should be removed, not defended.
- Bottleneck pressure is **never** a reason to bypass a gate. It is a reason to
  reduce ceremony or to widen authority through an explicit, governed decision.

## Open accessibility dependency

*(Deferred — CDS-WP-007)*

Several gates reference accessibility evidence. **The accessibility target and
its evidence method do not yet exist** (CR-024).

Until CDS-WP-007 defines them:

- no accessibility claim may be made at any level,
- the Stable gate cannot be fully satisfied for artifacts with accessibility
  obligations,
- exceptions may not weaken accessibility — including a requirement whose value
  is unknown, which is a real constraint that is currently unmeasurable
  (RISK-028),
- a CoreOps pilot entry criterion remains unmet.

This is recorded rather than worked around. Nova may wish to advance CDS-WP-007.

## Change control

This document is normative. Changes require an authorized work package, a
corresponding decision entry where a registered decision changes, consistency
updates across the dependent policies, and Human Maintainer approval.

## Related documents

| Topic | Document |
| --- | --- |
| Conflicts between normative sources | [Source Conflict Resolution Policy](SOURCE_CONFLICT_RESOLUTION_POLICY.md) |
| Maturity states and gates | [Artifact Maturity Lifecycle](ARTIFACT_MATURITY_LIFECYCLE.md) |
| Versioning, compatibility, deprecation | [Versioning, Compatibility and Deprecation Policy](VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md) |
| Contribution and acceptance | [Contribution and Acceptance Model](CONTRIBUTION_AND_ACCEPTANCE_MODEL.md) |
| Exceptions and Product Profiles | [Exception and Product Profile Governance](EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md) |
| Adoption and conformance claims | [Adoption, Conformance and Claims Policy](ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md) |
| Risk ownership and control | [Risk Governance Model](RISK_GOVERNANCE_MODEL.md) |
| Licensing and publication | [Licensing and Publication Decision Model](LICENSING_AND_PUBLICATION_DECISION_MODEL.md) |
| Release and change control | [Release and Change Control Policy](RELEASE_AND_CHANGE_CONTROL_POLICY.md) |
| Logical architecture | [Design System Architecture](../architecture/DESIGN_SYSTEM_ARCHITECTURE.md) |
| Normative scope | [Concept and Scope](CONCEPT_AND_SCOPE.md) |
