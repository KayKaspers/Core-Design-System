# Foundation Operating Playbook

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-009 — Operating Enablement and Pre-Candidate Readiness
- **Date:** 2026-07-16
- **Status:** **Operational view — NOT normative.** This playbook makes the
  committed governance runnable day to day. It **references** the normative
  policies; it does not replace, weaken, or reinterpret them (DEC-S-063).

## Purpose and non-normativity boundary

The governance model (CDS-WP-006) is complete and consistent, but a small
maintainer group must be able to *run* it without bypassing it (RISK-029,
RISK-040). This playbook is the operating checklist for a single change,
end to end.

**What this playbook may do:** sequence the existing gates, point to the right
normative source at each step, and reduce duplicated effort.

**What this playbook may never do:** change authority, scope, traceability,
evidence obligations, risk review, human approval, or fail-closed behavior. On
any conflict between this playbook and a normative policy, **the policy wins and
this playbook is wrong** (DEC-S-034,
[Source Conflict Resolution Policy](../governance/SOURCE_CONFLICT_RESOLUTION_POLICY.md)).

## Source map — where the authority actually lives

Read the source, not this summary, when the detail matters.

| Operating topic | Normative source |
| --- | --- |
| Roles, tracks, approval gates, escalation | [Governance Operating Model](../governance/GOVERNANCE_OPERATING_MODEL.md) |
| Source conflicts (fail closed) | [Source Conflict Resolution Policy](../governance/SOURCE_CONFLICT_RESOLUTION_POLICY.md) |
| Maturity states and Candidate/Stable gates | [Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md) |
| Versioning, compatibility, deprecation | [Versioning, Compatibility and Deprecation Policy](../governance/VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md) |
| Contribution and acceptance | [Contribution and Acceptance Model](../governance/CONTRIBUTION_AND_ACCEPTANCE_MODEL.md) |
| Exceptions and Product Profiles | [Exception and Product Profile Governance](../governance/EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md) |
| Adoption, conformance, claims | [Adoption, Conformance and Claims Policy](../governance/ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md) |
| Risk ownership and control | [Risk Governance Model](../governance/RISK_GOVERNANCE_MODEL.md) |
| Licensing and publication | [Licensing and Publication Decision Model](../governance/LICENSING_AND_PUBLICATION_DECISION_MODEL.md) |
| Release and change control | [Release and Change Control Policy](../governance/RELEASE_AND_CHANGE_CONTROL_POLICY.md) |
| Accessibility evidence and claims | [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) |
| Logical architecture | [Design System Architecture](../architecture/DESIGN_SYSTEM_ARCHITECTURE.md) |
| Critical-risk actionability | [Critical Risk Action Register](CRITICAL_RISK_ACTION_REGISTER.md) |
| Foundation closure and phase boundary | [Foundation Closure Record](../governance/FOUNDATION_CLOSURE_RECORD.md) |

## Roles at a glance

Six roles (DEC-S-033). Authoritative detail in the
[Governance Operating Model](../governance/GOVERNANCE_OPERATING_MODEL.md).

- **Human Maintainer** — decides; sole Git-write, release, publication,
  licensing, risk-acceptance, and maturity-approval authority. Not delegable.
- **Nova** — reviews, controls governance and risk, recommends. Never decides,
  never accepts a risk.
- **Claude** — scoped executor of documentation-shaped work. Proposes only;
  no approval, no Git write.
- **Consumer Maintainer** — accountable within their own project; no CDS core
  approval authority.
- **Contributor** — submits; never approves their own contribution.
- **Evidence Reviewer** — checks evidence; never the artifact itself and never
  the executor of the work being evidenced.

## Intake and change classification

Every change enters here.

1. **Describe the change** in one sentence and open the appropriate dossier
   (Standard or Elevated — see below).
2. **Classify the track.** Standard is for corrections, clearly bounded
   non-breaking additions, and low-risk documentation. **Elevated is mandatory**
   for any of: breaking change · Stable artifact · accessibility obligation ·
   Product Profile · exception · adoption or conformance claim · licensing or
   publication decision · removal · security- or legally-relevant change.
3. **Apply the trigger rule.** If a change *looks* Standard but touches **any**
   Elevated trigger, **it is Elevated** — the trigger wins, never the estimate.
4. **Run the Decision Need Check and Risk Review** (below) before execution.

The two tracks **carry the same mandatory gates**; only ceremony and scope
differ. Ceremony scales; **obligations do not**.

## Standard Track

Use the [Standard Change Dossier Template](STANDARD_CHANGE_DOSSIER_TEMPLATE.md).

1. Open a Standard dossier; record change class and the Standard-Track rationale.
2. Confirm no Elevated trigger is present (if any is, stop and switch to Elevated).
3. Name normative sources, affected artifacts, affected contracts, and the
   **Allowed Files** for the change.
4. Decision Need Check; Risk Review; Evidence plan (may be "none" only where no
   evidence obligation exists).
5. Single Nova review pass.
6. Human-Maintainer approval (consolidated is permitted on this track).
7. Execute documentation or (in a later phase) implementation within Allowed
   Files only.
8. Validate; record the result and post-change status in the dossier.
9. Human Maintainer commits and, if applicable, pushes.
10. Post-commit reconciliation (below).

## Elevated Track

Use the [Elevated Change Dossier Template](ELEVATED_CHANGE_DOSSIER_TEMPLATE.md).

1. Open an Elevated dossier; record every Elevated trigger that applies.
2. Everything in the Standard Track **plus**: explicit Evidence Bundle, affected
   maturity states, compatibility axes, migration impact, accessibility impact,
   Product-Profile/exception impact, consumer impact, support-baseline relevance,
   licensing/rights impact, publication impact, and claim impact.
3. **Separate review and approval acts** — Nova (Risk Controller) review and a
   distinct **Evidence Reviewer** who is never the executor and never the
   artifact.
4. Individual Human-Maintainer approval per change — never consolidated away.
5. Pass the specific gate(s) the change touches (Candidate, Stable, Exception,
   Product Profile, Claim, Release, Publication, Risk acceptance) as defined in
   the relevant normative policy.
6. Execute within Allowed Files; validate against the Evidence Bundle.
7. Human-Maintainer approval → Human Maintainer commits/tags/releases as
   applicable. Claude never performs a Git write, tag, release, or publication.
8. Post-commit reconciliation.

## Stop conditions (fail closed)

Stop and escalate — do not resolve locally — when any of the following holds
(DEC-S-023, DEC-S-034; Governance Operating Model → Escalation):

- authority is unclear;
- normative sources conflict (meaning vs values, or intra-class);
- evidence is missing, contradictory, or unreviewable;
- a change looks Standard but touches an Elevated trigger;
- a role would have to approve its own work, or review its own evidence;
- an exception would weaken accessibility or distort status truth;
- a claim cannot be substantiated;
- a risk would require acceptance or closure;
- readiness is unclear (unclear readiness ⇒ **NO-GO**, never "go with notes").

While an escalation is open, the affected state is **not releasable and not
distributable**. Escalation path: **Claude records and reports → Nova reviews and
recommends → Human Maintainer decides.**

## Decision Need Check

Before execution, ask whether the change **creates or alters a registered
Decision**. If it does:

- a new `DEC-S-###` (next number **derived from the register, never invented**)
  or an amendment to an existing decision is required, on the Elevated Track;
- Claude proposes; Nova reviews; the Human Maintainer approves. Claude never
  finalizes a decision and never creates an ADR outside an authorized scope.

If it does not, record "no decision impact" in the dossier and continue.

## Risk Review

For every change (DEC-S-045; [Risk Governance Model](../governance/RISK_GOVERNANCE_MODEL.md)):

- identify affected risks by ID (no new Risk ID without an authorized work
  package);
- for a critical risk, consult the
  [Critical Risk Action Register](CRITICAL_RISK_ACTION_REGISTER.md) for its
  executor role, review trigger, expected evidence, and blocking effect;
- **only the Human Maintainer may set a risk `Accepted` or `Closed`**;
- **documentation is not mitigation** — a policy addressing a risk is a first
  step, not a treatment;
- a `Mitigating` risk without a named executor is not being mitigated.

## Evidence Review

- State the evidence level honestly and report outcomes only at the level the
  evidence reaches (RISK-017; Accessibility Evidence and Claims Model, AE-0…AE-4).
- An **automated check is input to a review, never the review** (DEC-S-053) — a
  green build, a clean diff, and a passing validation are evidence, not consent.
- The Evidence Reviewer is never the executor of the evidenced work and never the
  artifact itself.
- Accessibility evidence requires a **declared support baseline**, which does not
  yet exist — so AE-3 and Stable remain unreachable (RISK-044).

## Allowed Files and scope

- Every change names its **Allowed Files** and touches nothing outside them.
- Missing parent folders of Allowed Files may be created; no other file or
  folder is created.
- Consumer repositories (CoreOps, SpeakCore, CastCore, any other) are **strictly
  read-only**, read from the committed HEAD revision only (DEC-S-013).
- `.claude/skills/**`, provenance, manifest, and inventory are changed only in an
  explicitly authorized Skill-Maintenance work package.

## Implementation or documentation execution

- In the current phase, execution is **documentation-shaped only**; no product
  code, token, component, colour, typography, tool, or format is created or
  selected.
- Preserve the distinction between **normative sources** and **generated
  artifacts**; a generated artifact never stands against its source, and a manual
  edit to a generated artifact is invalid and reconciled back into the source
  (DEC-S-022, DEC-S-031).

## Validation

- Verify only Allowed Files changed; inspect the full diff; confirm the change
  meets its dossier's validation plan.
- Re-derive every quantitative figure from the artifacts and **independently
  count it again** — never carry a number from working memory.
- Confirm no register range or ID contiguity broke.

## Nova review

Nova reviews scope-fit, consistency, evidence sufficiency, and risk. Nova
**recommends** an outcome (`GO` / `GO WITH NOTES` / `REWORK` / `STOP`). A Nova
review is never an approval.

## Human-Maintainer approval

Approval is a **separate recorded act** from review. Only the Human Maintainer
approves anything normative, accepts a risk, approves a maturity transition, or
authorizes a release or publication. Approval is per-change and does not
generalize to the next change.

## Commit and push

- The Human Maintainer performs **all** Git writes. Claude's changes stay
  uncommitted until then.
- No automatic publication from `main`; no tag or release without an explicit
  Human-Maintainer action — including in an emergency (DEC-S-048).

## Post-commit reconciliation

After a commit, reconcile the operational and summary views to the new committed
state:

- update the Context Pack, Project Profile, Project Brain, README, Work Packages,
  and Next Phase as the change requires (these are summaries, never sources);
- confirm the registers (Decision Index, Risk Register) still balance;
- if any generated artifact drifted from its source, reconcile it back — never
  let the derivative stand.

## Candidate and release boundary

- No artifact is promoted to Candidate or Stable, no pilot is started, no claim
  is made, no licence is selected, and no publication occurs **in this phase**.
- The Candidate gate, Stable gate, and publication gate live in their normative
  policies and each terminate at the Human Maintainer. **A clean build or diff is
  not approval.**
- Current publication state: **`Private Development`**.

## Emergency escalation

An emergency compresses the **timeline**, never the standard (DEC-S-048).
Emergency changes still require a Human-Maintainer decision and eventual full
evidence; they defer ceremony, not authority. Route every emergency through the
escalation path above.

## Lean operating rule

A single change should capture information **once**. Other documents and dossiers
**reference** that record rather than copying it.

**May be reduced:** duplicate descriptions, repeated tables, unnecessary
free-text reports, repeated manual counts, and identical evidence references.

**May never be reduced:** authority, scope, traceability, evidence, risk review,
human approval, and fail-closed behavior.

## Change control

This playbook is an operational view maintained by authorized work packages. It
does not self-amend and it grants no authority. Changing it does not change any
governance policy; changing a governance policy obliges a corresponding update
here.

## Related documents

- [Foundation Closure Record](../governance/FOUNDATION_CLOSURE_RECORD.md)
- [Standard Change Dossier Template](STANDARD_CHANGE_DOSSIER_TEMPLATE.md)
- [Elevated Change Dossier Template](ELEVATED_CHANGE_DOSSIER_TEMPLATE.md)
- [Critical Risk Action Register](CRITICAL_RISK_ACTION_REGISTER.md)
- [Pre-Candidate Operating Plan](../roadmap/PRE_CANDIDATE_OPERATING_PLAN.md)
- [Governance Operating Model](../governance/GOVERNANCE_OPERATING_MODEL.md)
