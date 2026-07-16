# Critical Risk Action Register

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-009 — Operating Enablement and Pre-Candidate Readiness
- **Date:** 2026-07-16
- **Status:** **Operational instrument — NOT a normative source.** This register
  operationalizes the twelve Critical Risks identified by CDS-WP-008. It changes
  no risk description, likelihood, or severity, and it accepts and closes no risk.
  The [Risk Register](../risks/RISK_REGISTER.md) remains the normative source
  (DEC-S-045, DEC-S-063).

## Purpose

The Foundation Milestone Review found the risk register was **not yet operated as
an instrument** — 48 risks, 0 named executors (FM-F-003; RISK-040). This document
makes the **twelve Critical Risks** actionable: for each, a named default
Mitigation Executor **role**, a review trigger, the next expected evidence, and a
blocking effect (DEC-S-064). It drives no work by itself.

## Roles and rules

- **Accountable Risk Owner — Human Maintainer** for every risk. The **only** role
  that may set a risk `Accepted` or `Closed`.
- **Risk Controller — Nova** for every risk. Observes, assesses, recommends;
  never accepts or closes.
- **Mitigation Executor** — a **role**, named per risk below. A named executor
  **authorizes no work**: every actual mitigation still requires an authorized
  work package or an explicitly approved task.
- **Evidence Reviewer** — Nova or a separately authorized reviewer, **never the
  executor of the evidenced work and never the artifact itself** (DEC-S-045,
  RISK-030). Where the executor is Nova, a **separately authorized Evidence
  Reviewer** is required and is currently **unstaffed** (FM-F-006).
- **Documentation is not mitigation** (RISK-040). A `Mitigating` risk without a
  named executor is not being mitigated.
- No new Risk ID is created here; the only status change authorized in CDS-WP-009
  is **RISK-040 Monitored → Mitigating** (see the gate below).

## The twelve Critical Risks

Titles are quoted from the committed [Risk Register](../risks/RISK_REGISTER.md).

---

### RISK-017 — Document evidence mistaken for user validation

- **Current status:** Monitored
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Claude as scoped executor (evidence-level
  discipline in documentation)
- **Evidence Reviewer:** Nova
- **Next review trigger:** before any statement that CDS or a consumer "works
  for", is "usable by", or is "validated by" users; and at each consumer-validation
  step of a Candidate/pilot.
- **Next expected evidence:** an explicit evidence-level statement per requirement
  and artifact (Level 1 / AE-0 today); real user-validation evidence exists only
  when a Human-Maintainer-authorized study produces it.
- **Affected upcoming work:** first design-slice consumer validation; CoreOps
  pilot; any inclusive-design claim.
- **Blocking effect:** blocks any "validated / usable / accessible / works"
  statement and any consumer or Stable claim until real validation exists.
- **Permitted status transition:** Monitored → Mitigating only when a named
  executor drives authorized user-validation work; acceptance/closure by Human
  Maintainer only.
- **Notes:** the sharpest case is accessibility — a documented baseline with no
  test evidences nothing.

---

### RISK-020 — Normative-source authority ambiguity

- **Current status:** Monitored
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Claude as scoped executor (artifact-class
  authority documentation)
- **Evidence Reviewer:** Nova
- **Next review trigger:** when a machine-readable normative source (approved
  values) is first introduced — i.e. the token-format decision (FM-F-011) — or on
  any detected meaning-vs-values conflict.
- **Next expected evidence:** a documented, non-overlapping artifact-class
  authority mapping; a fail-closed conflict record for any conflict detected.
- **Affected upcoming work:** token-format decision; first token/component
  artifacts; consumer contracts.
- **Blocking effect:** a meaning-vs-values conflict **invalidates the affected
  artifact state** and blocks release/distribution until resolved (DEC-S-034).
- **Permitted status transition:** Monitored → Mitigating when a machine-readable
  source exists and class-boundary control is active.
- **Notes:** meaning belongs to human-readable sources, values to machine-readable
  ones; overlap is the defect that creates this risk.

---

### RISK-021 — Token and override proliferation

- **Current status:** Monitored
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Claude as scoped executor (token-layer and
  override validation documentation)
- **Evidence Reviewer:** Nova
- **Next review trigger:** at the first token layer, first component token, and
  first Product Profile override in the design slice.
- **Next expected evidence:** machine-checkable validation results for cycles,
  orphans, unused tokens, layer violations, and illegal overrides; a profile and
  exception budget.
- **Affected upcoming work:** token-format decision; first design-slice tokens;
  Product Profiles.
- **Blocking effect:** unresolved layer violations or illegal overrides block the
  Candidate of the affected token/component artifact.
- **Permitted status transition:** Monitored → Mitigating when the first tokens
  exist and validation runs.
- **Notes:** the architecture constrains direction, not volume — direction rules
  alone will not stop proliferation.

---

### RISK-023 — Domain-pattern leakage into the universal foundation

- **Current status:** Monitored
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Claude as scoped executor (domain-family
  boundary documentation)
- **Evidence Reviewer:** Nova
- **Next review trigger:** whenever an operations-shaped requirement is proposed
  for Layer 3 or 4, or a Domain Pattern Family artifact is created.
- **Next expected evidence:** multi-consumer evidence from **outside** the
  operations domain before any operations pattern enters the universal foundation;
  otherwise it stays in the Domain Pattern Family.
- **Affected upcoming work:** first design slice (status foundation); any
  operations-pattern work; Product Profiles.
- **Blocking effect:** blocks promotion of an operations pattern into Layers 3–4
  without outside-domain evidence.
- **Permitted status transition:** Monitored → Mitigating when a domain-family
  artifact or a leakage decision is under active control.
- **Notes:** all three reviewed consumers are infrastructure products — the sample
  cannot distinguish "operational products need this" from "all products need this".

---

### RISK-026 — Architecture overdesign

- **Current status:** Monitored
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Nova (architecture-scope control)
- **Evidence Reviewer:** separately authorized Evidence Reviewer (Nova precluded
  as executor; currently unstaffed — FM-F-006)
- **Next review trigger:** at the first design slice (first real implementation
  contact) and at each Candidate exercising a new architectural structure.
- **Next expected evidence:** slice/pilot friction recorded as evidence *about the
  architecture*; a keep-or-remove decision for each structure that earns nothing.
- **Affected upcoming work:** first design slice; component contract; maturity
  gates.
- **Blocking effect:** non-blocking for Foundation closure; a structure that
  cannot be operated in the slice blocks scaling it to breadth.
- **Permitted status transition:** Monitored → Mitigating when the first slice
  produces architecture-friction evidence.
- **Notes:** prefer removing structure that earns nothing over defending it.

---

### RISK-028 — Deferred accessibility policy creates architecture debt

- **Current status:** Monitored
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Claude as scoped executor (structural
  accessibility-constraint documentation)
- **Evidence Reviewer:** Nova
- **Next review trigger:** at the accessibility support-baseline definition
  (CDS-WP-010) and at the first component contract carrying accessibility contract
  areas (DEC-S-055).
- **Next expected evidence:** confirmation that the safe structural constraints
  (invariant 10, non-colour meaning, status perceivable non-visually) hold in the
  first slice; the support baseline defined.
- **Affected upcoming work:** CDS-WP-010; first component contract; Pilot Group E.
- **Blocking effect:** a structural decision that precludes the target blocks the
  affected artifact until reworked.
- **Permitted status transition:** Monitored → Mitigating when CDS-WP-010 baseline
  and constraint work is active.
- **Notes:** WP-007 reframed this — the target now exists; the evidence does not.

---

### RISK-029 — Governance bottleneck and maintainer overload

- **Current status:** Monitored
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Nova (process design) — as named in the
  Risk Register
- **Evidence Reviewer:** separately authorized Evidence Reviewer (Nova precluded
  as executor; currently unstaffed — FM-F-006)
- **Next review trigger:** before the first Elevated change; and whenever approval
  backlog or bypass pressure appears.
- **Next expected evidence:** the operating playbook and dossier templates in use
  (delivered by CDS-WP-009); observed ceremony reduction without gate loss; a
  governed decision if authority is ever widened.
- **Affected upcoming work:** every Elevated change; first Candidate; CDS-WP-010.
- **Blocking effect:** non-blocking to closure; bottleneck pressure may **never**
  justify skipping a gate — an ungoverned bypass blocks the change.
- **Permitted status transition:** Monitored → Mitigating when the playbook and
  dossiers are actively used to reduce ceremony (subject to Human-Maintainer
  decision).
- **Notes:** the central affordability risk; concentrated authority is deliberate
  (DEC-S-005) and its cost must stay visible.

---

### RISK-031 — Maturity inflation

- **Current status:** Monitored
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Nova (maturity-gate review)
- **Evidence Reviewer:** separately authorized Evidence Reviewer (Nova precluded
  as executor; currently unstaffed — FM-F-006)
- **Next review trigger:** at every Candidate and Stable transition request.
- **Next expected evidence:** the full Candidate/Stable gate evidence per
  DEC-S-036; demotion recorded as a normal, cheap act.
- **Affected upcoming work:** first Candidate; first Stable (currently unreachable).
- **Blocking effect:** an artifact lacking gate evidence cannot be promoted —
  blocks Candidate and Stable.
- **Permitted status transition:** Monitored → Mitigating when the first Candidate
  transition is under active gate control.
- **Notes:** no existing artifact is Candidate or Stable; defining the lifecycle
  did not populate it.

---

### RISK-038 — Licensing and rights fragmentation

- **Current status:** Monitored
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Human Maintainer — as named in the Risk
  Register (Claude never proposes a licence)
- **Evidence Reviewer:** Nova
- **Next review trigger:** before any publication-state change and before any
  external distribution of any artifact class.
- **Next expected evidence:** per-artifact-class rights decisions across the ten
  classes; third-party provenance established **before** any public state.
- **Affected upcoming work:** any publication; font/icon/brand-asset decisions;
  external contribution intake.
- **Blocking effect:** unknown or conflicting rights are an **absolute publication
  blocker** (DEC-S-047).
- **Permitted status transition:** Monitored → Mitigating when the Human
  Maintainer begins per-class licensing decisions.
- **Notes:** a single "the licence" decision fails precisely at fonts and brand
  assets.

---

### RISK-040 — Ceremonial risk governance

- **Current status:** **Mitigating** (changed from Monitored by CDS-WP-009 — see
  the gate below)
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Nova — as named in the Risk Register
- **Evidence Reviewer:** separately authorized Evidence Reviewer (Nova precluded
  as executor; currently unstaffed — FM-F-006)
- **Next review trigger:** at each work-package close and each risk review;
  specifically when a critical risk becomes active in upcoming Elevated work.
- **Next expected evidence:** this Critical Risk Action Register (executor,
  trigger, expected evidence, and blocking effect for all twelve critical risks —
  delivered by CDS-WP-009); subsequent evidence that risks drive decisions, not
  only records.
- **Affected upcoming work:** all critical-risk-bearing Elevated work; CDS-WP-010.
- **Blocking effect:** a critical risk lacking an executor, review trigger,
  expected evidence, and blocking effect blocks the affected Elevated work it
  bears on (DEC-S-064).
- **Permitted status transition:** **Monitored → Mitigating — applied by
  CDS-WP-009.** No further transition is authorized here; acceptance/closure by
  the Human Maintainer only.
- **Notes:** the register is now an instrument for the twelve critical risks with
  a named executor (Nova); this is the mitigation the risk demanded.

---

### RISK-044 — Accessibility support baseline drift

- **Current status:** Monitored
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Claude as scoped executor (baseline and
  evidence-strategy documentation in CDS-WP-010); the baseline **decision** is the
  Human Maintainer's
- **Evidence Reviewer:** Nova
- **Next review trigger:** before any AE-3 evidence is accepted; at CDS-WP-010;
  and on any baseline-composition change.
- **Next expected evidence:** a **declared accessibility support baseline**
  (browser / platform / input / assistive-technology / language matrix), approved
  by the Human Maintainer.
- **Affected upcoming work:** CDS-WP-010; every AE-3/Stable artifact; Pilot Group E.
- **Blocking effect:** without a declared baseline, AE-3 and therefore **Stable
  are unreachable** for any artifact with an accessibility obligation.
- **Permitted status transition:** Monitored → Mitigating when CDS-WP-010 baseline
  work is active.
- **Notes:** accessibility evidence without a current declared baseline is
  unverifiable.

---

### RISK-048 — Accessibility evidence burden exceeds maintainer capacity

- **Current status:** Monitored
- **Accountable owner:** Human Maintainer · **Risk Controller:** Nova
- **Default Mitigation Executor role:** Nova (capacity-aware scope planning); scope
  or maturity **reductions** are Human-Maintainer decisions
- **Evidence Reviewer:** separately authorized Evidence Reviewer (Nova precluded
  as executor; currently unstaffed — FM-F-006)
- **Next review trigger:** at CDS-WP-010 (capacity-aware test matrix) and whenever
  evidence demand is planned for a Candidate/Stable artifact.
- **Next expected evidence:** a capacity-aware evidence/test matrix; scope or
  maturity chosen to fit capacity — never a weakened standard.
- **Affected upcoming work:** CDS-WP-010; every accessibility-evidence effort;
  first Candidate.
- **Blocking effect:** missing capacity is a **planning limit, never a conformance
  justification** (DEC-S-059) — a capacity shortfall blocks the maturity or claim,
  not the standard.
- **Permitted status transition:** Monitored → Mitigating when CDS-WP-010 capacity
  planning is active.
- **Notes:** the realistic failure is a series of individually defensible
  compromises under deadline; the honest responses are smaller scope or lower
  maturity.

---

## Actionability summary

| Risk | Executor role | Review trigger | Expected evidence | Blocking effect | Status |
| --- | --- | --- | --- | --- | --- |
| RISK-017 | Claude (scoped) | ✓ | ✓ | ✓ | Monitored |
| RISK-020 | Claude (scoped) | ✓ | ✓ | ✓ | Monitored |
| RISK-021 | Claude (scoped) | ✓ | ✓ | ✓ | Monitored |
| RISK-023 | Claude (scoped) | ✓ | ✓ | ✓ | Monitored |
| RISK-026 | Nova | ✓ | ✓ | ✓ | Monitored |
| RISK-028 | Claude (scoped) | ✓ | ✓ | ✓ | Monitored |
| RISK-029 | Nova | ✓ | ✓ | ✓ | Monitored |
| RISK-031 | Nova | ✓ | ✓ | ✓ | Monitored |
| RISK-038 | Human Maintainer | ✓ | ✓ | ✓ | Monitored |
| RISK-040 | Nova | ✓ | ✓ | ✓ | **Mitigating** |
| RISK-044 | Claude (scoped) | ✓ | ✓ | ✓ | Monitored |
| RISK-048 | Nova | ✓ | ✓ | ✓ | Monitored |

**All twelve** carry a named executor role, a review trigger, expected evidence,
and a blocking effect.

## RISK-040 gate — evaluated and met

RISK-040 may move from `Monitored` to `Mitigating` **only** if all twelve Critical
Risks have a named executor role, a review trigger, a next expected evidence
artifact, and a clear blocking effect.

- **Gate condition:** met — see the summary table above (12/12 on all four
  attributes).
- **Action taken:** RISK-040 is set to **`Mitigating`**, recorded in the
  [Risk Register](../risks/RISK_REGISTER.md) with executor Nova.
- **Boundary:** this is the **only** risk status change authorized in CDS-WP-009.
  **No risk is accepted or closed.** All other risks remain `Monitored`.

## Related documents

- [Risk Register](../risks/RISK_REGISTER.md) — normative source
- [Risk Governance Model](../governance/RISK_GOVERNANCE_MODEL.md)
- [Foundation Operating Playbook](FOUNDATION_OPERATING_PLAYBOOK.md)
- [Foundation Open Gaps and Dependencies](../reviews/FOUNDATION_OPEN_GAPS_AND_DEPENDENCIES.md)
- [Foundation Closure Record](../governance/FOUNDATION_CLOSURE_RECORD.md)
- [Pre-Candidate Operating Plan](../roadmap/PRE_CANDIDATE_OPERATING_PLAN.md)
