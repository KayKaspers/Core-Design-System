# CDS-WP-007 — Accessibility and Inclusive Design Policy — Work-Package Notes

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-007 — Accessibility and Inclusive Design Policy
- **Date:** 2026-07-16
- **Status:** Completed (pending Human Maintainer commit)
- **Character:** Evidence and process notes. **Not a normative source.**

## Auftrag

Define the normative CDS accessibility and inclusive-design policy; resolve
**CR-024** at policy level with the target **WCAG 2.2 Level AA** for the
applicable web-based scope; define the responsibility model, a complete Level
A/AA applicability matrix, five evidence levels (AE-0…AE-4), six channel
profiles, the limitations and exception policy, and the CoreOps pilot
accessibility criterion; reconcile the affected governance and traceability
documents; add DEC-S-049…060 and RISK-041…048; and, on PASS, advance the roadmap
to CDS-WP-008.

The work package **implements nothing, tests nothing, claims nothing, and starts
no pilot.**

## Preflight

- Repository root: `D:\Projects\Core-Design-System` — confirmed.
- Branch: `main` — confirmed.
- Working tree at start: clean; last commit carried CDS-WP-006.
- No merge, rebase, or cherry-pick active.
- Starting registers: DEC-S-001…048 (48), RISK-001…040 (40), CR-001…040 (40).
- Governance and architecture invariants as recorded by CDS-WP-005/006.
- Skills pinned to NDF v1.0.0; manifest unchanged.

## Verwendete Skills

Ten authorized skills only:

1. `ndf-work-package-runner` — work-package execution discipline, Allowed-Files
   enforcement, fail-closed gates.
2. `ndf-accessibility-reviewer` — accessibility policy structure, WCAG mapping
   discipline, evidence-not-claim separation.
3. `ndf-ux-flow-reviewer` — complete-process and composition framing for the
   component-to-product boundary.
4. `ndf-content-tone-reviewer` — inclusive content and cognitive-accessibility
   requirements.
5. `ndf-onboarding-friction-reviewer` — setup, help, and error-recovery
   requirement framing (pilot Group E).
6. `ndf-privacy-data-minimization-reviewer` — accessible privacy, security, and
   dangerous-action requirements.
7. `ndf-validation-evidence-reviewer` — evidence levels, support baseline,
   generate-then-count quantitative discipline.
8. `ndf-public-neutrality-guard` — no conformance/certification/legal claims.
9. `ndf-context-pack-maintainer` — non-normative context-pack update.
10. `ndf-compact-context-summary-runner` — continuation summary.

No other skills were loaded. Skills were used as procedural aid only; none
extended scope, authority, or Allowed Files.

## Webzugriffsmethode

Integrated Claude Desktop web search and page view only. No `curl`, `wget`,
`Invoke-WebRequest`, GitHub CLI, scraping, automated download, or third-party
summary was used. No standards PDF was downloaded. Search snippets were not used
as evidence.

## Geöffnete Quellen

**13 official URLs** opened and registered in
[ACCESSIBILITY_SOURCE_REGISTER.md](../docs/research/ACCESSIBILITY_SOURCE_REGISTER.md):

- **W3C / WAI (normative):** WCAG 2.2 Recommendation; WAI-ARIA 1.2 Recommendation.
- **W3C / WAI (informative):** WCAG 2.2 Understanding; WCAG 2.2 Techniques; APG
  introduction, read-me-first, keyboard-interface; WAI test-evaluate overview and
  conformance; WCAG2 supplemental guidance; W3C i18n techniques.
- **W3C (draft):** WCAG-EM 2.0 — **Group Note Draft**.
- **ETSI (publisher listing / status):** EN 301 549 page — the ETSI deliverable
  fetch returned HTTP 403; the human-facing status page was viewed instead.

The EN 301 549 V3.2.1 PDF was **deliberately not opened** (no PDF download; status
determined from the ETSI page and the version listing).

## Source Status

- **WCAG 2.2** — W3C Recommendation (2024-12-12). Normative basis.
- **Understanding / Techniques** — supporting / informative. Not normative.
- **WAI-ARIA 1.2** — Recommendation (2023-06-06). Normative for roles/states/
  properties.
- **APG** — informative; self-excludes production-ready code and comprehensive
  design systems.
- **WCAG-EM 2.0** — Group Note **Draft**; not adopted as the CDS conformance
  method.
- **EN 301 549** — V4.1.0 (2026-06) is **`On Approval`**, not final; tracked as
  standards-watch, not adopted. No EN 301 549 conformance claimed.

Full analysis:
[ACCESSIBILITY_STANDARD_STATUS_AND_LIMITATIONS.md](../docs/research/ACCESSIBILITY_STANDARD_STATUS_AND_LIMITATIONS.md).

## Zielentscheidung

**WCAG 2.2 Level AA** for the applicable web-based scope (DEC-S-049), resolving
CR-024 at policy level (DEC-S-060). No AAA commitment. **The target is not
conformance** (DEC-S-050). Effective on Human Maintainer commit.

## Policy Scope

Applies to web product UI, web documentation, web reference implementations,
component/pattern examples, and the declared web scope of the future CoreOps
pilot. Non-web channels require their own profile (DEC-S-058). Inclusive design
extends beyond WCAG (DEC-S-057).

## Responsibility Model

CDS owns requirements, contracts, status semantics, and reference evidence;
consumers own composition, content, domain semantics, complete processes,
runtime, and product claims; support baseline, browser/AT matrix, pilot
evidence, and claims are shared or contract-controlled. **49 of 55 applicable
criteria require both sides** (DEC-S-051, DEC-S-052).

## WCAG Matrix

[WCAG_2_2_AA_APPLICABILITY_MATRIX.md](../docs/governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md),
generated from the criteria list and independently re-counted:

- **56 listed** Level A + AA criteria — **32 A, 24 AA**.
- **55 applicable** — **31 A, 24 AA** — excluding **4.1.1 Parsing** (obsolete and
  removed by WCAG 2.2 itself; not a CDS opt-out).
- No AAA criterion in the mandatory matrix; no duplicates.
- Policy status: 35 shared · 15 consumer-scope · 5 CDS-alone · 1 not-applicable
  (4.1.1) · 0 channel-profile-decision · 0 not-yet-assessable.
- Responsibility: 49 both · 7 alone-or-N/A.
- **No pass/fail statement.** Mapping is policy, not evaluation.

## Evidence Model

Five levels, defined by the
[Accessibility Evidence and Claims Model](../docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
(the responsibility split they record is DEC-S-051):
AE-0 not assessed · AE-1 structural/automated · AE-2 manual interaction · AE-3
assistive technology against a **declared support baseline** · AE-4 consumer
scope / complete process. Automated-only is never sufficient (DEC-S-053). No
numeric score. **Every CDS artifact is AE-0; no baseline is declared.**

## Channel Profiles

Six profiles
([ACCESSIBILITY_CHANNEL_PROFILES.md](../docs/governance/ACCESSIBILITY_CHANNEL_PROFILES.md)):
Web Product UI (AA) · Web Documentation (AA) · PDF/Reports (undefined) ·
Presentations (undefined) · Diagrams/Data-Viz (mixed) · Brand/Communication
(undefined). **2 of 6 have a target; 0 are Candidate- or Stable-eligible today.**

## CoreOps Pilot Criterion

[COREOPS_PILOT_ACCESSIBILITY_CRITERION.md](../docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md):
CR-024 resolved at policy level; entry criterion `Accessibility target defined`
is satisfiable **on Human Maintainer commit**, not declared by Claude. Pilot
Group E carries 13 minimum evidence requirements, **none met** (not assessed, not
failed). The pilot has not started and cannot start (two entry criteria
structurally unmet). **No WCAG 2.2 Level AA conformance has been demonstrated,
reviewed, or approved for CoreOps.**

## Traceability-Reconciliation

Architecture traceability
([ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md](../docs/architecture/ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md)):

- CR-021 → `Partially addressed - later design decision required`
- CR-022 → `Partially addressed - later design decision required`
- CR-024 → `Addressed by architecture` (target/policy exist; not conformance)
- CR-034 → `Partially addressed - later design decision required`

New distribution (independently re-counted): **9 Addressed · 27 Partially · 0
Deferred-006 · 0 Deferred-007 · 2 Consumer-owned · 2 Out of scope = 40.** No
requirement is deferred to a policy work package any longer. Requirement
statements and evidence classifications were **not** rewritten. Consumer-side
follow-up pointers (CONSUMER_REQUIREMENTS_MODEL / _TRACEABILITY) reconciled from
CDS-WP-007 to CDS-WP-008; CR-024 status advanced from `Deferred` while its
original classification is retained as the historical verdict.

## Neue Decisions

DEC-S-049…DEC-S-060 (12) added; total **60**; DEC-S-001…048 unchanged; no ADR.
Type: *Accessibility and inclusive design decision*.

## Neue Risiken

RISK-041…RISK-048 (8) added; total **48**; existing risks unchanged; finalized
four-role model (DEC-S-045). None `Mitigating`; none with a named executor — the
RISK-040 anti-ceremonial pattern is explicitly recorded as extending.

## Geänderte Dateien

11 new accessibility documents; 8 governance/traceability reconciliations;
DECISION_INDEX and RISK_REGISTER extended; 8 status/index files updated; these
notes created. Full list in the Rückmeldung, section 15.

## Quantitative Validierung

Every metric was generated from the artifacts and independently re-counted via
scripts (generate-then-count): opened sources (13), Level A (32/31), Level AA
(24), matrix rows (56/55), policy-status distribution (35/15/5/1/0/0), shared
responsibility (49/7), architecture status distribution (9/27/0/0/2/2 = 40),
layer distribution (4/2/6/4/10/6/1/5/2 = 40), evidence levels (5), channel
profiles (6), decisions (60), risks (48), requirements (40). No count was taken
from working memory. No unbound full-text grep was used as a count basis.

## Correction Run (2026-07-16)

A bounded correction run within CDS-WP-007 realigned four governance items to
Nova's authorized mapping before commit:

- **DEC-S-049 … DEC-S-060 reassigned to the authorized ID→content mapping.** The
  first draft had reorganized the twelve decisions into a self-chosen thematic
  order. Corrected so DEC-S-051 = *responsibility shared by contract*, DEC-S-052 =
  *component evidence not generalizable to a product claim*, DEC-S-054 =
  *native-semantics-first (APG informative)*, DEC-S-055 = *mandatory contract
  areas*, DEC-S-056 = *status axes distinguishable*, DEC-S-057 = *inclusive design
  beyond WCAG*. The **AE-0 … AE-4 levels** are normative in the Evidence and
  Claims Model and are **not** a decision (they no longer occupy DEC-S-051). The
  **no-legal/no-certification** statement is a policy boundary, **not** a numbered
  decision (it no longer occupies DEC-S-057). All AE-level and no-legal citations
  across the repo were repointed accordingly.
- **RISK-041 … RISK-048 reassigned to the authorized titles/descriptions.** RISK-042
  = *automated-testing substitution*, RISK-044 = *support-baseline drift*, RISK-045
  = *accessibility regression*, RISK-046 = *non-web channel gap*, RISK-047 =
  *inclusive-design undercoverage*. The previously over-numbered concerns —
  *no-baseline-exists*, *APG-as-production*, *standards-status-misrepresentation* —
  were folded into RISK-044, RISK-045, and a note under RISK-047 respectively, and
  no longer occupy authorized risk IDs. All risk citations were repointed.
- **Claim language softened.** Unproven negative statements ("CoreOps is not WCAG
  conformant", "CDS is not WCAG conformant") were replaced by the evidence-correct
  form: *no WCAG 2.2 Level AA conformance has been demonstrated, reviewed, or
  approved* for CoreOps, and *no current CDS artifact has an approved WCAG 2.2
  Level AA conformance claim*. AE-0 is stated as *Not Assessed* — neither pass nor
  fail.
- **EN 301 549 versions separated.** V3.2.1 (published reference, not adopted, no
  legal claim) is now distinguished from V4.1.0 (On Approval, standards-watch,
  re-verify before normative use).
- **WCAG matrix summary** relabelled to state *31 current Level A · 24 current
  Level AA · 55 current applicable · 1 historical removed reference row (4.1.1) ·
  56 total displayed rows*, so no reading claims 32 current Level-A criteria.

No new decision, risk, or accessibility requirement was introduced; DEC-S-001 …
DEC-S-048 and RISK-001 … RISK-040 remain untouched; counts stay 60 / 48.

## Abweichungen

- Two pre-existing files (ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md,
  CONSUMER_REQUIREMENTS_TRACEABILITY.md) carry **mixed CRLF line endings at HEAD**
  (183 and 114 CR characters respectively, from the bootstrap commit). Edits were
  minimal and did not introduce this; `git diff --check` is clean. Not
  normalized, to avoid a whole-file diff that would obscure the reconciliation.
- Consumer-side traceability follow-up reconciliation (WP-007 → WP-008) was not
  spelled out in the prompt's reconciliation section but is required to keep the
  registers internally consistent after CDS-WP-007 completes; done conservatively
  without touching statements, classifications, or count tables.

## Offene Accessibility-Fragen

- No accessibility support baseline exists (RISK-044) — AE-3 and Stable are
  unreachable until one is declared.
- No test tooling, browser, or assistive-technology is selected (deliberately).
- No user research exists or is planned (RISK-017) — inclusive design is asserted
  from documentation, not validated with people.
- PDF/presentation/diagram/brand accessibility standards are undefined
  (DEC-S-058).
- Evidence-burden versus maintainer capacity is unresolved (RISK-048).

## Abschlussstatus

PASS, pending Human Maintainer commit. No artifact promoted; no claim, tag, or
release created; publication state remains `Private Development`; no Git write
action performed.
