# CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy — Work Package Notes

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy
- **Baseline:** A11Y-BL-001
- **Date:** 2026-07-16
- **Status:** Work-package evidence — **non-normative**.

## Assignment

Define the first controlled accessibility support baseline and evidence strategy —
the environments future evidence targets, the tiering, version handling, evidence
process (AE-1…AE-4), evidence records, defect/regression classification, and
maintenance — using authorized official research. Run no test, select no tool,
create no Candidate, and assert no evidence.

## Preflight

- Root `D:/Projects/Core-Design-System`; branch `main`; working tree clean; no
  merge/rebase; `origin` correct. Last commit `144cc58` (CDS-WP-009).
- Foundation Status Closed with Notes; Phase Pre-Candidate Operating Enablement.
- Registers re-derived and counted: Decisions 64; Risks 48 (47 Monitored,
  RISK-040 Mitigating); Requirements 40; Critical Risk Register 12 entries; Skills
  39 files / manifest 38·39. Publication `Private Development`; no Candidate/Stable;
  no claim; pilot inactive.
- Fail-closed conditions: none triggered.

## Skills used (10, only the authorized set)

ndf-work-package-runner (frame) · ndf-accessibility-reviewer (advisory a11y framing;
no certification) · ndf-validation-evidence-reviewer (honest evidence strength /
AE-0 discipline) · ndf-existing-project-analysis-runner (structured baseline
analysis) · ndf-feature-scope-runner (scope/non-goals of baseline and tiers) ·
ndf-privacy-data-minimization-reviewer (no personal/telemetry data; official sources
only) · ndf-release-safety (no release/claim; NO-GO on unclear readiness) ·
ndf-public-neutrality-guard (neutral phrasing; no private data) ·
ndf-context-pack-maintainer (Context Pack update) ·
ndf-compact-context-summary-runner (closing blocks). No other skill was used.

## Web research

Authorized official-source research via the integrated web view only; no curl/wget,
no downloads, no installs, no third-party/comparison/snippet evidence, no
market-share data. **13 URLs opened; 9 usable; 4 not usable** (S-10 redirect, S-11
load error, S-12/S-13 HTTP 403). Full register:
[Accessibility Baseline Source Register](../docs/research/ACCESSIBILITY_BASELINE_SOURCE_REGISTER.md).

## Product-family and version findings (official, dated 2026-07-16)

- **Windows 11** (S-03): Modern Lifecycle; supported 24H2 / 25H2 / 26H1.
- **Chromium** (S-02 Edge, S-09 Chrome): rapid release (Edge 2-week from v152;
  Chrome 4-week; both 8-week Extended Stable); Edge trigger = Chromium release.
- **Firefox** (S-06): rapid release 4-week + annual ESR with security updates.
- **NVDA** (S-04): free/open source; 64-bit Windows 10/11.
- **VoiceOver** (S-05): built into macOS/iOS/iPadOS.
- **forced-colors** (S-08): tied to Windows High Contrast / Contrast Themes.
- **prefers-reduced-motion** (S-07): tied to OS reduced-motion setting.
- **W3C/WAI** (S-01): tools *assist*, do not *determine* accessibility.
- **JAWS**: official requirements **not retrievable** (S-12/S-13, HTTP 403) — kept
  Tier-2 conditional with a source limitation.

## Baseline tiers

Three tiers (DEC-S-066): **Tier 1 Required Core** (small, free-software-runnable,
desktop web), **Tier 2 Complementary** (Conditional), **Tier 3 Scope-triggered**
(Deferred). Required composition per DEC-S-067.

## Selected environment entries

14 entries, A11Y-ENV-001…014 (contiguous, no gaps/duplicates): **Required 6**
(001–006), **Conditional 4** (007–010), **Deferred 4** (011–014). Required
browser/screen-reader pairings **2** (NVDA×Chromium, NVDA×Firefox). OS families 4;
browser families 3; AT families 5; languages 2 (DE/EN); channels 2 (Web Product UI,
Web Documentation).

## Selection rationale and capacity trade-offs

Two engines + a no-cost screen reader on a supported OS, runnable without
procurement (RISK-048); Apple/WebKit, JAWS, mobile, and further languages held to
Conditional/Deferred with visible coverage gaps (RISK-049). No local availability
invented; every row's local execution availability is `Not asserted` (RISK-051).
Full rationale:
[Selection Rationale](../docs/research/ACCESSIBILITY_BASELINE_SELECTION_RATIONALE.md).

## Evidence strategy

AE-0…AE-4 operationalized (meanings unchanged from the Evidence and Claims Model);
required evidence by maturity; manual (AE-2) and AT (AE-3) strategies bound to
Required pairings; consumer (AE-4) and pilot strategies; exact environment identity;
reviewer independence (unstaffed — FM-F-006); capacity-aware execution; **no current
evidence — every artifact AE-0**.

## Maintenance policy

Product-family vs exact evidence identity (DEC-S-068); five freshness states
(Current/Review due/Stale/Superseded/Unknown); nine review triggers; a six-month
maximum review gap (DEC-S-070); no automatic claim renewal.

## Defect and regression model

Four impact levels (Blocking/High/Medium/Low); a defect record; six defect statuses
(`Accepted limitation` = Human-Maintainer decision, visible in claims); regression
definition; Blocking/High regressions block Stable, pilot/consumer evidence, claims,
and "unchanged-compatible" distribution; no defect registered (AE-0).

## Reconciliation

Reconciled (additively, no meaning changed): Accessibility Evidence and Claims Model,
CoreOps Pilot Accessibility Criterion, Consumer Validation Plan, Critical Risk Action
Register (RISK-044 → Mitigating; RISK-048 partial; RISK-040 follow-evidence),
Pre-Candidate Operating Plan (CDS-WP-010 complete; CDS-WP-011 next).

## New decisions

DEC-S-065…072 added (baseline-not-evidence; three tiers; Required Core composition;
family-vs-execution identity; scope-triggered coverage; freshness review; immutable
evidence records; defect/regression classification). Range DEC-S-001…072 (72);
DEC-S-001…064 unchanged; no ADR.

## New risks and status check

RISK-049…054 added (all Monitored). RISK-044 moved `Monitored → Mitigating` — gate
met: baseline defined, maintenance triggers present, six-month max review gap set,
version/freshness bound in the evidence model, next expected evidence artifact
defined. RISK-040 remains Mitigating. No other existing status changed; no acceptance
or closure. Range RISK-001…054 (54): 52 Monitored, 2 Mitigating.

## Changed or created files

Created (10): `docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md`,
`ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md`, `ACCESSIBILITY_EVIDENCE_STRATEGY.md`,
`ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md`,
`ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md`,
`docs/operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md`,
`docs/research/ACCESSIBILITY_BASELINE_SOURCE_REGISTER.md`,
`ACCESSIBILITY_BASELINE_SELECTION_RATIONALE.md`, and this notes file (plus the WP is
counted once). Changed (13): `docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md`,
`COREOPS_PILOT_ACCESSIBILITY_CRITERION.md`, `CONSUMER_VALIDATION_PLAN.md`,
`docs/operations/CRITICAL_RISK_ACTION_REGISTER.md`,
`docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md`, `docs/decisions/DECISION_INDEX.md`,
`docs/risks/RISK_REGISTER.md`, `project-system/CONTEXT_PACK_FOUNDATION.md`,
`PROJECT_PROFILE.md`, `NEXT_PHASE.md`, `WORK_PACKAGES.md`,
`project-brain/PROJECT_BRAIN.md`, `README.md`, `CLAUDE.md`, `CHANGELOG.md`.

## Quantitative validation

See the Report to Nova (§14). Key figures: 13 URLs opened / 9 usable · 3 tiers · 14
environment entries (6/4/4) · 2 Required pairings · 5 AE levels · 27 evidence-record
fields · 4 defect impact levels · 6 defect statuses · 9 review triggers · 72
decisions · 54 risks (52/2) · 12 work-package IDs · 10 skills.

## Deviations

None from the prompt. All work confined to the 24 Allowed Files. No test executed,
no tool/browser/AT selected or installed. No Git write.

## Open notes

- A11Y-BL-001 pending Human-Maintainer commit; **no evidence executed — AE-0**.
- Evidence Reviewer / Consumer Maintainer / Contributor roles unstaffed (FM-F-006).
- WebKit/Safari and JAWS unverified; JAWS official requirements not retrievable
  (S-12/S-13). Mobile/touch Deferred. No local execution availability asserted.
- Machine-readable-source/token-format decision open (FM-F-011) → CDS-WP-011.

## Completion status

**PASS.** All Definition-of-Done items met; only Allowed Files changed; no Git
write action performed.
