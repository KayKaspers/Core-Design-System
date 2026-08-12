# Pre-Candidate Operating Plan

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-009 — Operating Enablement and Pre-Candidate Readiness
- **Date:** 2026-07-16
- **Status:** **Roadmap / planning view — NOT normative and NOT an authorization.**
  It sequences work; it activates no phase beyond what the Human Maintainer has
  approved, assigns no maturity, and starts no pilot (DEC-S-062, DEC-S-063).

## Phase purpose

The **Pre-Candidate Operating Enablement** phase makes the closed Foundation
**operable** and prepares the prerequisites for the **first design Candidate**,
without producing any design, token, component, or product artifact. Governance
operationalization, role readiness, critical-risk actionability, and
accessibility-support planning **precede** the first Candidate (DEC-S-062).

## Phase entry state

- **Foundation:** Closed with Notes (see
  [Foundation Closure Record](../governance/FOUNDATION_CLOSURE_RECORD.md)).
- **Milestone outcome:** `GO WITH NOTES`, accepted by the Human Maintainer.
- **Foundation blockers:** 0.
- **Publication state:** `Private Development`. **Claims:** none valid.
  **Maturity:** no artifact is Candidate or Stable. **Pilot:** inactive.
- **Registers:** DEC-S-001 … DEC-S-064 (64); RISK-001 … RISK-048 (48);
  CR-001 … CR-040 (40); FM-F-001 … FM-F-012 (12).

## Foundation closure notes carried into this phase

The eight mandatory closure notes (Foundation Closure Record) frame this phase.
Chiefly: governance affordability, the accessibility support baseline, risk
actionability, no real user research, no Candidate/Stable artifacts, no
licence/publication, the completed reference-integrity check, and no automatic
pilot activation.

## Immediate prerequisites (before the first Candidate or any pilot)

*(Cross-referenced to the Next-phase Recommendation and Open Gaps.)*

1. **A lightweight operating playbook and dossier templates** — **delivered** by
   CDS-WP-009 ([Operating Playbook](../operations/FOUNDATION_OPERATING_PLAYBOOK.md),
   [Standard](../operations/STANDARD_CHANGE_DOSSIER_TEMPLATE.md) and
   [Elevated](../operations/ELEVATED_CHANGE_DOSSIER_TEMPLATE.md) dossiers).
   (FM-F-002, FM-F-012; RISK-029, RISK-040.)
2. **Critical-risk actionability** — **delivered** by CDS-WP-009
   ([Critical Risk Action Register](../operations/CRITICAL_RISK_ACTION_REGISTER.md)).
   (FM-F-003; RISK-040.)
3. **Declare an accessibility support baseline** — **delivered (policy-side) by
   CDS-WP-010**: A11Y-BL-001, three tiers, environment matrix, evidence strategy,
   maintenance policy, and defect/regression model, declared and committed.
   **No evidence executed** (every artifact AE-0). (FM-F-001; RISK-044 → Mitigating.)
4. **Staff the Evidence Reviewer role** (and, for a profile, a Consumer
   Maintainer) — **not yet done**; the reviewer may never be the author.
   (FM-F-006; DEC-S-045.)
5. **Machine-readable-source and token-format decision** — **not yet made**;
   the subject of the next work package, CDS-WP-011. (FM-F-011.)

## Operating enablement status

| Enablement | Status after CDS-WP-009 |
| --- | --- |
| Operating playbook | **Present** (non-normative operational view) |
| Standard change dossier template | **Present** |
| Elevated change dossier template | **Present** |
| Critical Risk Action Register | **Present** — 12/12 risks actionable |
| Reference-integrity review | **Complete** — PASS, 0 CDS-authored broken links |
| Foundation closure record | **Present** — normative on closure/authority/phase |
| Accessibility support baseline (A11Y-BL-001) | **Declared and committed (CDS-WP-010) — no evidence executed** |
| Accessibility evidence strategy + maintenance + defect model | **Present** (CDS-WP-010) |

## Role readiness

| Role | Readiness |
| --- | --- |
| Human Maintainer | Active |
| Nova | Active |
| Claude (scoped executor) | Active |
| Consumer Maintainer | **Unstaffed** (needed for a Product Profile) — FM-F-006 |
| Contributor | **Unstaffed** (external contribution not yet possible) — FM-F-006 |
| Evidence Reviewer | **Unstaffed** — required before an Elevated/Stable change and where Nova is the Mitigation Executor — FM-F-006 |

## Critical-risk readiness

All twelve Critical Risks (RISK-017, 020, 021, 023, 026, 028, 029, 031, 038, 040,
044, 048) now carry a named executor role, a review trigger, expected evidence, and
a blocking effect (Critical Risk Action Register). **RISK-040** is `Mitigating`;
the other eleven remain `Monitored`. No risk is accepted or closed.

## Accessibility support baseline — delivered by CDS-WP-010

The accessibility support baseline gates AE-3 and therefore Stable for any artifact
with an accessibility obligation (RISK-044). **CDS-WP-010 defined it** — A11Y-BL-001,
three tiers (Required/Complementary/Scope-triggered), the Environment and Scope
Matrix, the Evidence Strategy, the Baseline Maintenance Policy, and the Defect and
Regression Model — **committed with CDS-WP-010**. The baseline is a **test
contract, not evidence**: **no test was run, every artifact is AE-0**, and no
environment is claimed as supported. RISK-044 moved `Monitored → Mitigating` on the
strength of the definition. The **next substantive topic** is the machine-readable
source and token-format decision (CDS-WP-011).

## Candidate entry conditions

Before the **first** design Candidate may be attempted (each condition owned by the
named role; none satisfied by CDS-WP-009 alone):

1. An accessibility support baseline is **declared** — **satisfied: A11Y-BL-001
   is declared and committed (CDS-WP-010)**. The condition itself is met; the
   first AE-1/AE-2 evidence is still to be produced, and this condition confers
   no evidence, support, or conformance — RISK-044.
2. The **Evidence Reviewer** role is staffed (never the author) — FM-F-006,
   DEC-S-045.
3. The machine-readable-source / token-format decision is made (CDS-WP-011) —
   FM-F-011.
4. A first design slice exists to promote — one Layer-3 semantic status foundation
   plus one Layer-4 component contract carrying the mandatory accessibility
   contract areas (DEC-S-055).
5. The **Candidate gate** evidence (DEC-S-036) is produced and reviewed, with
   honest open limitations — RISK-031.

## Explicitly not permitted in this phase

- token-format decision or any token/value creation;
- concrete design foundations, colours, typography, icons, logos, or themes;
- component or pattern design;
- design, build, or test tool selection;
- **executing accessibility tests or asserting any accessibility evidence** (the
  baseline is defined, but no evidence has been produced — every artifact is AE-0);
- installing browsers, screen readers, or test tools;
- Product Profiles;
- promoting any artifact to Candidate or Stable;
- starting the CoreOps pilot;
- any claim, licence selection, or publication.

## Exit criteria

This phase is complete, and the project is ready to attempt a first Candidate,
when: the accessibility support baseline and evidence strategy exist (CDS-WP-010);
the Evidence Reviewer is staffed; the machine-readable-source/token-format decision
is made; and the critical risks bearing on the first slice remain actionable with
current triggers and evidence. Each is a Human-Maintainer-approved step, not an
automatic transition.

## Mandatory sequencing and next work package

CDS-WP-010 (Accessibility Support Baseline and Evidence Strategy) is **complete**:
the baseline and its supporting policies are defined and committed, no evidence
was executed, and RISK-044 moved to `Mitigating`. The next authorized work package
is:

**CDS-WP-011 — Machine-Readable Source and Token Format Decision.**

CDS-WP-011 is registered as **`Next`** only; it is **not executed** here. Its
objective is to establish normative machine-readable-source requirements, evaluate
token-format options against interoperability, alias/reference validation, metadata
and provenance, and the offline tooling boundary, and to prepare the corresponding
decision — with **no concrete design values, no Candidate, no pilot start, and no
component work**.

Still not authorized (require their own explicit work packages): concrete design
foundations, component work, Product Profiles, the CoreOps pilot, and publication.

## Related documents

- [Foundation Closure Record](../governance/FOUNDATION_CLOSURE_RECORD.md)
- [Foundation Operating Playbook](../operations/FOUNDATION_OPERATING_PLAYBOOK.md)
- [Critical Risk Action Register](../operations/CRITICAL_RISK_ACTION_REGISTER.md)
- [Foundation Reference Integrity Review](../reviews/FOUNDATION_REFERENCE_INTEGRITY_REVIEW.md)
- [Next-phase Recommendation](../reviews/NEXT_PHASE_RECOMMENDATION.md)
- [Foundation Open Gaps and Dependencies](../reviews/FOUNDATION_OPEN_GAPS_AND_DEPENDENCIES.md)
- [Work Packages](../../project-system/WORK_PACKAGES.md) ·
  [Next Phase](../../project-system/NEXT_PHASE.md)
