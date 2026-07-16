# Risk Governance Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-006
- **Date:** 2026-07-16
- **Status:** **Normative** for risk ownership and control

## Purpose

Finalizes the risk owner model that has been **provisional since CDS-WP-001** and
was deferred to this work package in every subsequent one.

Frame: [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md).
Register: [Risk Register](../risks/RISK_REGISTER.md).

## Roles

*(Normative, DEC-S-045 — four roles per risk)*

### Accountable Risk Owner — **Human Maintainer**

For **every** CDS project risk.

Decides risk acceptance · prioritizes mitigation · approves closure · carries
final governance responsibility.

**Not delegable.** One accountable owner for all risks is a deliberate choice
consistent with DEC-S-005 — and a known bottleneck (RISK-029).

### Risk Controller — **Nova**

Observes · assesses · **requests evidence** · recommends mitigation · reviews
closure · reports escalation need.

**Nova does not accept or close a risk.** The controller who could accept the
risks they assess is not a control.

### Mitigation Executor — **named per mitigation**

Explicitly assigned per mitigation or work package. May be: Human Maintainer ·
Nova · Claude (scoped) · Consumer Maintainer · a later authorized contributor or
reviewer.

**Default where unassigned: Claude as scoped executor**, for documentation-shaped
mitigations only. A mitigation with no named executor is not being mitigated —
its status must not be `Mitigating`.

### Evidence Reviewer — **Nova or an explicitly authorized reviewer**

Checks mitigation evidence against the claim.

**Never the artifact itself, and never the mitigation's own executor.** Evidence
reviewed only by whoever produced it has not been reviewed.

## Role separation

| Act | Who | Who may **not** |
| --- | --- | --- |
| Assess a risk | Nova | — |
| Request evidence | Nova | — |
| Execute mitigation | Named executor | — |
| Review evidence | Nova / authorized reviewer | The executor of that mitigation |
| **Accept a risk** | **Human Maintainer only** | Nova, Claude, consumers |
| **Close a risk** | **Human Maintainer only** | Nova, Claude, consumers |
| Escalate | Any role | — |

## Risk statuses

*(Normative — exactly five)*

| Status | Meaning | Requires |
| --- | --- | --- |
| **Identified** | Registered; no treatment decided. | Description, impact, initial assessment |
| **Monitored** | Mitigation direction defined; effect observed. | Mitigation direction, review trigger |
| **Mitigating** | Active mitigation in progress. | **A named Mitigation Executor** |
| **Accepted** | Consciously accepted with residual effect. | **Human Maintainer decision** |
| **Closed** | No longer relevant, or fully mitigated. | Evidence, Nova review, **Human Maintainer approval** |

### Current status

**All existing risks remain `Monitored`.** No status changes without concrete
evidence justifying it. Defining this model does not treat a single risk
(RISK-040).

## Risk lifecycle

```
Identified
  → Monitored  (mitigation direction defined)
     → Mitigating  (executor named, work in progress)
        → evidence produced
           → Evidence Reviewer checks
              → Nova reviews
                 → Human Maintainer decides
                    ├→ Closed    (mitigated / no longer relevant)
                    └→ Accepted  (residual risk consciously carried)
                       → review trigger → re-assessed
```

Movement backwards is normal: an Accepted risk whose trigger fires returns to
Monitored or Mitigating.

## Review triggers

A risk is re-assessed when: a related work package completes · evidence
contradicts the assessment · a related decision changes · an Accepted risk's
trigger fires · a related deviation or exception recurs · an incident occurs ·
scope, architecture, or consumer set changes materially.

## Risk acceptance

*(Normative — Human Maintainer only)*

Requires **all**:

| # | Element |
| --- | --- |
| 1 | Reasoned decision |
| 2 | Scope |
| 3 | Residual effect |
| 4 | **Review trigger** |
| 5 | Validity reference |

Acceptance is a **conscious, bounded, revisitable** decision — never an
expiry-by-silence. Element 4 is what makes it revisitable: acceptance without a
trigger is abandonment with paperwork.

**Claude may never accept a risk. Nova may never accept a risk.**

## Risk closure

Requires **all**:

1. mitigation evidence,
2. Nova review,
3. Human Maintainer approval,
4. documented closure reason.

A risk is never closed because it stopped being discussed, because the work
package that raised it finished, or because it feels handled.

## Evidence requirements

Mitigation evidence must: identify what was done · bind to a source revision
where applicable · be reviewable by someone other than its executor · state
residual effect honestly · report at the level it actually reaches (RISK-017).

**Documentation is Level 1 evidence.** Writing a policy is evidence that a policy
exists — never that a risk is controlled. This distinction is the entire content
of RISK-040.

## Escalation

Escalate when: a risk's severity increases materially · a mitigation fails · an
Accepted risk's trigger fires · evidence contradicts the assessment · a risk is
outside the executor's authority · risks accumulate faster than they are treated.

Path: **Claude reports → Nova assesses and recommends → Human Maintainer
decides.**

## Treatment of existing risks

*(Normative)*

All existing risks **RISK-001 … RISK-028** are updated to this finalized model:

- **Accountable Risk Owner:** Human Maintainer — for every risk
- **Risk Controller:** Nova — for every risk
- **Mitigation Executor:** named per mitigation; default Claude (scoped) for
  documentation-shaped mitigations
- **Evidence Reviewer:** Nova or an explicitly authorized reviewer

**What changed:** only the role model. The previous entries carried a single
provisional "Owner role" field, which conflated accountability with control.

**What did not change:** every existing description, impact statement,
likelihood, severity, mitigation direction, and status. **No existing risk
assessment was altered**, because no new evidence justified it.

The previously provisional attributions (Nova on most, Human Maintainer on
RISK-009, RISK-015, RISK-018, RISK-028) are superseded by the four-role model:
accountability now sits uniformly with the Human Maintainer, and control
uniformly with Nova.

## Anti-ceremonial rule

*(Normative — the rule this document most needs)*

> **A register that is updated but drives nothing is not risk governance.**

Therefore:

1. Every risk has a **review trigger** — not a review date nobody honours.
2. Every `Mitigating` risk has a **named executor**. If nobody is named, it is
   `Monitored` — say so.
3. `Monitored` is honest when nothing is being done. Do not dress inaction as
   mitigation.
4. **Documentation is not mitigation.** A policy addressing a risk is a first
   step, not a treatment.
5. A risk that never changes status for a long time is either genuinely stable or
   genuinely ignored — the review must distinguish which.
6. Prefer fewer, real risks over many decorative ones.
7. **Adding a risk is not managing it.** This work package adds twelve risks and
   treats none — which is exactly what RISK-040 warns about, and is recorded
   here rather than obscured.

## Related documents

- [Governance Operating Model](GOVERNANCE_OPERATING_MODEL.md)
- [Risk Register](../risks/RISK_REGISTER.md)
- [Release and Change Control Policy](RELEASE_AND_CHANGE_CONTROL_POLICY.md)
- [Consumer Validation Plan](CONSUMER_VALIDATION_PLAN.md)
