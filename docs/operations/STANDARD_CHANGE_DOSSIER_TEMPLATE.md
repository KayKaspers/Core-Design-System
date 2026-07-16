# Standard Change Dossier — Template

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-009 — Operating Enablement and Pre-Candidate Readiness
- **Date:** 2026-07-16
- **Status:** **Operational template — NOT normative.** A completed dossier is a
  record of one Standard-Track change. It references normative policies; it does
  not restate or replace them, and it grants no approval (DEC-S-063).

## How to use

Copy the template below into a per-change working file. Keep it **compact and
reference-oriented**: cite the normative source by link, do not paste policy text.
The dossier records a change; it never authorizes one. Approval is a separate act
by the Human Maintainer after Nova review (see
[Foundation Operating Playbook](FOUNDATION_OPERATING_PLAYBOOK.md) → Standard Track).

**Track guard:** if the change touches **any** Elevated trigger (breaking change,
Stable artifact, accessibility obligation, Product Profile, exception, adoption or
conformance claim, licensing or publication, removal, security- or legally-relevant
change), **stop** and use the
[Elevated Change Dossier Template](ELEVATED_CHANGE_DOSSIER_TEMPLATE.md) instead.

## Mandatory fields (19)

Every field is required. Where a field does not apply, write
`None` or `Not applicable with rationale` — never delete the field.

---

## Standard Change Dossier

### 1. Change ID
`CDS-CHG-S-###` (or the authorized work-package ID).

### 2. Title
One line naming the change.

### 3. Change class
One of: Editorial · Corrective · Additive (bounded, non-breaking). (Elevated
classes are out of scope for this template.)

### 4. Standard-Track rationale
Why this is Standard and not Elevated. State explicitly that **no Elevated
trigger is present**.

### 5. Scope
What the change does, precisely and minimally.

### 6. Non-Goals
What the change deliberately does not do.

### 7. Normative sources
Links to the governing policy/policies. No policy text is restated here.

### 8. Affected artifacts
Documents/registers touched, by path.

### 9. Affected contracts
Consumer/architecture contracts touched, or `None`.

### 10. Allowed Files
The exact file list the change may create or modify. Nothing outside it is
touched.

### 11. Decision impact
New/changed `DEC-S-###` (next number **derived, never invented**), or
`No decision impact`.

### 12. Risk impact
Affected risk IDs; note that **no new Risk ID** is created without an authorized
work package, and that **only the Human Maintainer** may accept or close a risk.

### 13. Evidence plan
What evidence the change produces, and at what level. May be `None` **only** where
no evidence obligation exists. An automated check is input to review, never the
review.

### 14. Validation plan
Concrete checks to run (Allowed-Files-only diff, register balance, link integrity,
independent re-count of any figure).

### 15. Rollback or correction path
How the change is reverted or corrected if wrong.

### 16. Nova review
Reviewer recommendation (`GO` / `GO WITH NOTES` / `REWORK` / `STOP`) and notes.
A review is not an approval.

### 17. Human-Maintainer approval
Recorded decision, separate from review. Blank until the Human Maintainer decides.

### 18. Implementation or documentation result
What was actually done, within Allowed Files.

### 19. Post-change status
Final state: committed?/pending, registers balanced, reconciliation done, open
notes.

---

## Rules for this dossier

- **Compact and reference-oriented** — link the normative source, do not restate it.
- **Not itself normative** — the dossier records a change; the policy governs it.
- **No automatic approval** — a completed dossier is not consent; the Human
  Maintainer approves after Nova review.
- **Mandatory gates are preserved** — authority, traceability, evidence, human
  approval, and fail-closed hold on this track exactly as on the Elevated Track
  (ceremony scales; obligations do not).

## Related documents

- [Foundation Operating Playbook](FOUNDATION_OPERATING_PLAYBOOK.md)
- [Elevated Change Dossier Template](ELEVATED_CHANGE_DOSSIER_TEMPLATE.md)
- [Governance Operating Model](../governance/GOVERNANCE_OPERATING_MODEL.md)
