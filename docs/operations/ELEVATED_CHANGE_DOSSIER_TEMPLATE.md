# Elevated Change Dossier — Template

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-009 — Operating Enablement and Pre-Candidate Readiness
- **Date:** 2026-07-16
- **Status:** **Operational template — NOT normative.** A completed dossier is a
  record of one Elevated-Track change. It references normative policies; it does
  not restate or replace them, and it grants no approval (DEC-S-063).

## How to use

Copy the template below into a per-change working file. It contains **all
Standard-Track fields plus the Elevated-only fields**. Keep it compact and
reference-oriented. The dossier records a change; it never authorizes one.

**When Elevated is mandatory:** breaking change · Stable artifact · accessibility
obligation · Product Profile · exception · adoption or conformance claim ·
licensing or publication decision · removal · security- or legally-relevant
change. A change that *looks* Standard but touches any of these **is Elevated**.

**Scalability:** the template scales through optional sections. A section that
does not apply is marked **`Not applicable with rationale`** — it is **never
silently removed**. Removing a heading hides a decision; naming it "not
applicable" records one.

## Field set

- **Base fields (19)** — identical in intent to the
  [Standard Change Dossier Template](STANDARD_CHANGE_DOSSIER_TEMPLATE.md).
- **Elevated-only fields (17)** — below.
- **Total mandatory fields: 36.**

---

## Elevated Change Dossier

### Part A — Base fields (19)

1. **Change ID** — `CDS-CHG-E-###` or the authorized work-package ID.
2. **Title.**
3. **Change class** — Editorial · Corrective · Additive · Deprecating · Breaking ·
   Emergency (DEC-S-048).
4. **Track rationale** — the Elevated triggers that apply (cross-reference Part B.1).
5. **Scope.**
6. **Non-Goals.**
7. **Normative sources** — linked, not restated.
8. **Affected artifacts.**
9. **Affected contracts.**
10. **Allowed Files.**
11. **Decision impact** — new/changed `DEC-S-###` (number derived, never invented).
12. **Risk impact** — affected risk IDs; no new Risk ID without an authorized WP;
    only the Human Maintainer accepts/closes a risk.
13. **Evidence plan** — cross-reference the Evidence Bundle (Part B.8).
14. **Validation plan.**
15. **Rollback or correction path.**
16. **Nova review** — recommendation and notes (cross-reference Part B.14).
17. **Human-Maintainer approval** — recorded, separate act (cross-reference Part B.17).
18. **Implementation or documentation result.**
19. **Post-change status.**

### Part B — Elevated-only fields (17)

1. **Elevated trigger(s)** — every applicable trigger, named explicitly.
2. **Affected maturity states** — which artifacts change maturity, and to what
   (DEC-S-035); or `Not applicable with rationale`.
3. **Compatibility axes** — per-axis statement across the eight axes; an
   unassessed axis is **never** reported as compatible (DEC-S-039).
4. **Migration impact** — required migration; a deprecation without a viable
   migration path is a removal with extra steps (DEC-S-040); or
   `Not applicable with rationale`.
5. **Accessibility impact** — affected criteria/contract areas, evidence level,
   and honest AE-state; note that accessibility cannot be waived by an ordinary
   exception (DEC-S-059); or `Not applicable with rationale`.
6. **Product Profile or Exception impact** — bounds, extension points,
   anti-fragmentation review, expiry; a profile is not retrospective legitimation
   (DEC-S-042, DEC-S-043); or `Not applicable with rationale`.
7. **Consumer impact** — which consumers are affected and how; consumer repos are
   read-only from committed HEAD; or `Not applicable with rationale`.
8. **Evidence Bundle** — the concrete evidence, its level, and its limits; an
   automated result never constitutes evidence on its own (DEC-S-053).
9. **Support Baseline relevance** — whether AE-3/Stable evidence depends on the
   accessibility support baseline (which does not yet exist — RISK-044); or
   `Not applicable with rationale`.
10. **Licensing and rights impact** — per-artifact-class rights; unknown or
    conflicting rights **block publication** (DEC-S-047); or
    `Not applicable with rationale`.
11. **Publication impact** — any publication-state effect; the current state is
    `Private Development` and does not change without the gate (DEC-S-046); or
    `Not applicable with rationale`.
12. **Claim impact** — any adoption/conformance claim; graded, scope- and
    version-bound; `CDS certified` prohibited; no claim currently valid
    (DEC-S-044); or `Not applicable with rationale`.
13. **Critical deviations** — any deviation from a normative policy, with its
    handling; unresolved deviation fails closed.
14. **Risk Controller review** — Nova's control assessment and recommendation.
15. **Evidence Reviewer** — named; **never the executor of the evidenced work,
    never the artifact itself** (DEC-S-045). If unstaffed, record the gap
    (FM-F-006) and do not proceed past the gate.
16. **Approval Gate** — the specific gate(s) crossed (Candidate · Stable ·
    Exception · Product Profile · Claim · Release · Publication · Risk
    acceptance), each terminating at the Human Maintainer.
17. **Final Human-Maintainer decision** — the recorded approval or rejection.
    Unclear readiness ⇒ **NO-GO**, never "go with notes".

---

## Rules for this dossier

- **Compact and reference-oriented** — link the normative source, do not restate it.
- **Scalable, never silently trimmed** — inapplicable sections are marked
  `Not applicable with rationale`.
- **Not itself normative** — it records a change; the policy governs it.
- **No automatic approval** — separate Nova review and Human-Maintainer approval
  are mandatory; a clean build or diff is not consent.
- **Mandatory gates are preserved** — authority, traceability, evidence, risk
  review, human approval, and fail-closed are non-negotiable on this track.

## Related documents

- [Foundation Operating Playbook](FOUNDATION_OPERATING_PLAYBOOK.md)
- [Standard Change Dossier Template](STANDARD_CHANGE_DOSSIER_TEMPLATE.md)
- [Critical Risk Action Register](CRITICAL_RISK_ACTION_REGISTER.md)
- [Governance Operating Model](../governance/GOVERNANCE_OPERATING_MODEL.md) ·
  [Release and Change Control Policy](../governance/RELEASE_AND_CHANGE_CONTROL_POLICY.md)
