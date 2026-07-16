# CDS-WP-009 — Operating Enablement and Pre-Candidate Readiness — Work Package Notes

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-009 — Operating Enablement and Pre-Candidate Readiness
- **Date:** 2026-07-16
- **Status:** Work-package evidence — **non-normative**. Records what CDS-WP-009
  did and how it was validated.

## Assignment

Open the controlled **Pre-Candidate** phase by operationalizing the committed
governance, without creating any design, tokens, components, tools, or product
code. Register Foundation closure with its notes; provide a lean Standard-Track
and a robust Elevated-Track operating flow with reusable dossier templates; make
the twelve Critical Risks from CDS-WP-008 actionable; review the whole committed
document inventory for reference integrity; make the first-Candidate prerequisites
visible; activate the Pre-Candidate phase; and register CDS-WP-010 as next.

## Preflight

- Repository root `D:/Projects/Core-Design-System`; branch `main`; working tree
  clean; no merge/rebase/cherry-pick active; `origin` remote correct.
- Last commit `6ceda35` — "docs(cds): complete foundation milestone review"
  (CDS-WP-008). CDS-WP-001 … CDS-WP-008 committed.
- Milestone outcome `GO WITH NOTES`; Foundation blockers 0.
- Registers re-derived and independently counted: Decisions 60 (DEC-S-001 …
  DEC-S-060), Risks 48 (RISK-001 … RISK-048), Requirements 40 (CR-001 … CR-040),
  Findings 12 (FM-F-001 … FM-F-012).
- Publication state `Private Development`; no Candidate/Stable artifact; no claim;
  CoreOps pilot inactive.
- Skills: NDF v1.0.0; 38 skill directories, 39 files; manifest `skillCount` 38,
  `fileCount` 39 — 39/39 match.
- Fail-closed conditions: none triggered.

## Skills used (8, only the authorized set)

- **ndf-work-package-runner** — WP execution frame, guardrails, closing structure.
- **ndf-adr-governance-review** — confirmed no ADR is needed; DEC-S numbers derived
  from the register, not invented.
- **ndf-validation-evidence-reviewer** — honest evidence-level framing for the
  Critical Risk Action Register and the reference-integrity review.
- **ndf-release-safety** — kept all release/publication statements as
  Human-Maintainer-only; unclear readiness ⇒ NO-GO; no tag/release action.
- **ndf-existing-project-analysis-runner** — structured the repository-wide
  reference-integrity analysis neutrally.
- **ndf-feature-scope-runner** — sharpened the scope/non-goals of the operating
  playbook and dossier templates.
- **ndf-context-pack-maintainer** — consistent, reference-first Context Pack update.
- **ndf-compact-context-summary-runner** — the mandatory Report-to-Nova and Compact
  Context Summary closing blocks.

No other skill was loaded or used.

## Foundation closure

Recorded in [Foundation Closure Record](../docs/governance/FOUNDATION_CLOSURE_RECORD.md).
Reviewed content revision `7b71652` (Foundation), review evidence committed at
`6ceda35`. Nova outcome `GO WITH NOTES`; Human-Maintainer acceptance by commit of
CDS-WP-008 + initiation of CDS-WP-009. Closure scope CDS-WP-001 … CDS-WP-008; 0
blockers. Eight mandatory notes recorded. Explicit non-effects: no Candidate,
Stable, adoption, conformance, release, publication, licence, or support.

## Operating playbook

[Foundation Operating Playbook](../docs/operations/FOUNDATION_OPERATING_PLAYBOOK.md)
— non-normative operational view. Source map to the normative policies; intake and
classification; Standard Track; Elevated Track; stop conditions; decision-need,
risk, and evidence checks; Allowed-Files/scope; execution; validation; Nova review;
Human-Maintainer approval; commit/push; post-commit reconciliation; Candidate and
release boundary; emergency escalation; the lean operating rule. It references the
governance policies and never overrides them.

## Standard dossier

[Standard Change Dossier Template](../docs/operations/STANDARD_CHANGE_DOSSIER_TEMPLATE.md)
— 19 mandatory fields, compact and reference-oriented, non-normative, no automatic
approval; a track guard routes any Elevated trigger to the Elevated template.

## Elevated dossier

[Elevated Change Dossier Template](../docs/operations/ELEVATED_CHANGE_DOSSIER_TEMPLATE.md)
— 19 base fields + 17 Elevated-only fields (36 total), scalable via
`Not applicable with rationale`, non-normative, separate Nova review and
Human-Maintainer approval preserved.

## Critical risk actions

[Critical Risk Action Register](../docs/operations/CRITICAL_RISK_ACTION_REGISTER.md)
— exactly the twelve CDS-WP-008 Critical Risks: RISK-017, 020, 021, 023, 026, 028,
029, 031, 038, 040, 044, 048. Each carries current status, accountable owner (Human
Maintainer), Risk Controller (Nova), a named default Mitigation Executor role,
Evidence Reviewer, next review trigger, next expected evidence, affected upcoming
work, blocking effect, permitted status transition, and notes. Where Nova is the
executor, the Evidence Reviewer is a separately authorized reviewer (Nova precluded;
unstaffed — FM-F-006). **RISK-040 gate met (12/12 on all four attributes) → RISK-040
`Monitored → Mitigating`**, the only status change; no acceptance or closure.

## Reference integrity review

[Foundation Reference Integrity Review](../docs/reviews/FOUNDATION_REFERENCE_INTEGRITY_REVIEW.md)
— 112 text files in scope; 829 markdown links checked; 56 external URLs (syntax
only); 5 broken links, all inside the vendored, pinned `.claude/skills/README.md`
(upstream NDF paths — FRI-F-001), non-blocking and not correctable within product
work; 0 CDS-authored broken links. 170 backtick path-like refs examined; 0 genuine
CDS-internal broken refs (the flagged ones are consumer-repository provenance paths
under DEC-S-013 — FRI-F-003). WP-006/WP-007 deferrals are historical/reconciled
(FRI-F-002); review-document pre-closure language is dated evidence (FRI-F-004).
Result: **PASS**; no normative source corrected; no Foundation-closure contradiction.

## Link and status problems found

- 5 broken links in the vendored skills README (FRI-F-001) — outside Allowed Files;
  pinned; not corrected.
- Historical WP-006/WP-007 deferral mentions in `docs/architecture/**` and WP-005
  notes (FRI-F-002) — reconciled to 0 in the traceability source; not active; not
  corrected.
- Consumer-repository provenance backtick paths (FRI-F-003) — external by design.
- Pre-closure language in `docs/reviews/**` (FRI-F-004) — dated review evidence;
  superseded by the Closure Record for status; preserved.

None blocks Foundation closure; none required editing a non-allowed normative file.

## Pre-candidate plan

[Pre-Candidate Operating Plan](../docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md)
— phase purpose and entry state, closure notes, immediate prerequisites, operating
enablement status, role readiness (Consumer Maintainer / Contributor / Evidence
Reviewer unstaffed — FM-F-006), critical-risk readiness, accessibility support
baseline as the next topic, Candidate entry conditions, prohibited work, exit
criteria, and CDS-WP-010 as next.

## New decisions

DEC-S-061 (closure with notes), DEC-S-062 (Pre-Candidate phase), DEC-S-063
(operating views non-normative), DEC-S-064 (critical-risk actionability before
Elevated work). Range now DEC-S-001 … DEC-S-064 (64); DEC-S-001 … DEC-S-060
unchanged; no ADR.

## Risk status check

Only RISK-040 changed: `Monitored → Mitigating`, gated by the Critical Risk Action
Register and documented in the Risk Register. No new Risk ID; no acceptance; no
closure. Range remains RISK-001 … RISK-048 (48).

## Changed or created files

Created: `docs/governance/FOUNDATION_CLOSURE_RECORD.md`,
`docs/operations/FOUNDATION_OPERATING_PLAYBOOK.md`,
`docs/operations/STANDARD_CHANGE_DOSSIER_TEMPLATE.md`,
`docs/operations/ELEVATED_CHANGE_DOSSIER_TEMPLATE.md`,
`docs/operations/CRITICAL_RISK_ACTION_REGISTER.md`,
`docs/reviews/FOUNDATION_REFERENCE_INTEGRITY_REVIEW.md`,
`docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md`, and this notes file.
Changed: `docs/decisions/DECISION_INDEX.md`, `docs/risks/RISK_REGISTER.md`,
`project-system/PROJECT_PROFILE.md`, `project-system/NEXT_PHASE.md`,
`project-system/WORK_PACKAGES.md`, `project-system/CONTEXT_PACK_FOUNDATION.md`,
`project-brain/PROJECT_BRAIN.md`, `README.md`, `CLAUDE.md`, `CHANGELOG.md`.

## Quantitative validation

All figures re-derived from artifacts and independently re-counted — see the Report
to Nova (§13). Key figures: 6 roles · 2 tracks · 9 approval gates · 12 Critical
Risks (12/12 actionable) · 19 Standard-dossier fields · 36 Elevated-dossier fields
· 64 decisions · 48 risks · 11 work-package IDs · 8 skills · 112 scope files · 829
markdown links · 5 broken (all vendored) · 0 CDS-authored broken.

## Deviations

None from the prompt. All work confined to the 18 Allowed Files. No Git write.

## Open notes

- Evidence Reviewer, Consumer Maintainer, and Contributor roles remain unstaffed
  (FM-F-006) — required before an Elevated/Stable change and where Nova is a
  Mitigation Executor.
- The accessibility support baseline is undeclared (FM-F-001; RISK-044) — the
  subject of CDS-WP-010.
- Machine-readable-source / token-format decision remains open (FM-F-011).
- Vendored skills README broken links (FRI-F-001) belong to a Skill-Maintenance WP.

## Completion status

**PASS.** All Definition-of-Done items met; only Allowed Files changed; no Git
write action performed.
