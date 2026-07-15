# CDS-WP-003 — Benchmark and Differentiation Research Notes

Internal work-package evidence for CDS-WP-003 — Benchmark and Differentiation
Research.

- **Date:** 2026-07-15
- **Executed by:** Claude (scoped local work and authorized web research)
- **Final status:** Completed

## Assignment

Examine ten named design systems using official sources, document structural
models and trade-offs, identify patterns relevant to CDS, assess eight
differentiation hypotheses evidence-based, register four new risks, and advance
the status to CDS-WP-003 Completed / CDS-WP-004 Next.

All results remain research evidence and differentiation hypotheses — not
visual, technical, or normative design decisions.

## Preflight

| Check | Result |
| --- | --- |
| Repository root | `D:/Projects/Core-Design-System` — matches. |
| Branch | `main` — as required. |
| Working tree | Clean. |
| Last commit | `c5c815c docs(cds): register concept and scope` — contains CDS-WP-002. |
| Remote (read-only) | `origin` → `https://github.com/KayKaspers/Core-Design-System.git` |
| Merge / rebase / cherry-pick | None active. |
| WP status at start | 001 Completed, 001A Completed, 002 Completed, 003 Next. |
| Decisions at start | DEC-S-001 … DEC-S-012, exactly 12. |
| Risks at start | RISK-001 … RISK-009, exactly 9. |
| Skills | 38 directories, 39 files, NDF v1.0.0, commit `9dcadc12fb960914b9a5baeff2ab1aee75912b57`. |
| Skills manifest | Valid JSON; 39/39 files hash-match. |
| Web access | Available via the integrated methods — the gating fail-closed condition. |

No fail-closed condition was triggered. All thirteen required normative
documents were read before any change.

## Skills used

Only the seven authorized Skills were loaded. The five prohibited design-oriented
Skills (`ndf-branding-kit-runner`, `ndf-creative-direction-runner`,
`ndf-ui-style-system-runner`, `ndf-landing-page-concept-runner`,
`ndf-naming-runner`) were **not** loaded.

| Skill | Purpose | Section used |
| --- | --- | --- |
| `ndf-work-package-runner` | WP frame: pre-checks, guardrails, closing structure. | Purpose, Allowed/Forbidden actions, Fail-closed, Output contract |
| `ndf-existing-project-analysis-runner` | Structure for neutral, advisory analysis of existing systems. | Expected outputs, Forbidden actions, Fail-closed |
| `ndf-product-discovery-runner` | Differentiation framing: audience, problem, value proposition, risks. | Expected outputs, Ethical-use boundaries |
| `ndf-accessibility-reviewer` | Framing accessibility findings as advisory, never certification. | Forbidden actions, Specific risk boundaries, Output contract |
| `ndf-context-pack-maintainer` | Context Pack update; references over repetition; no invented status. | Expected outputs, Forbidden actions |
| `ndf-compact-context-summary-runner` | Report and Compact Context Summary structure. | Expected outputs, Output contract |
| `ndf-public-neutrality-guard` | Neutrality check of produced text. | Public-neutrality requirements, Output contract |

The accessibility reviewer's boundary — advisory only, never a certification or
conformance claim — directly shaped how dimension G and HYP-007 were written.

## Web access method

- **Integrated page view** (renders JavaScript) and **integrated fetch** of
  Claude Desktop.
- **No terminal network commands were used.** No curl, wget, Invoke-WebRequest,
  Invoke-RestMethod, git clone, git fetch, GitHub CLI, scraping, or automated
  downloads.
- No assets, images, fonts, icons, UI kits, packages, or repositories were
  downloaded. No repository was cloned. No package was installed or inspected.
- No screenshots were saved.

**Method finding worth carrying forward:** several sites are JavaScript-rendered
and return only a title via the fetch method while reading correctly via the
page view (Material, Spectrum, SLDS, Carbon). Relying on one method alone would
have produced false "not found" conclusions. One source (SAP) refused fetch with
HTTP 403 but read via the page view.

## Source restrictions

- Official publisher documentation, official standards pages, and official
  publisher repositories only.
- Excluded by rule and in practice: encyclopedias, blogs, agency articles,
  comparison portals, social media, search snippets, AI summaries, unofficial
  mirrors, third-party archives.
- **No search snippets were used as evidence.** No third-party source was used.
- Every observation carries a registered URL and the access date 2026-07-15.
- Redirects and access failures were recorded rather than hidden.

## Systems examined

Exactly the ten authorized systems. None added, none substituted. Spectrum and
Spectrum 2 were treated as one evolution line, not two entries.

Carbon · Fluent 2 · Material 3 · Primer · Atlassian · Spectrum / Spectrum 2 ·
SAP Fiori · SLDS 2 · GOV.UK · USWDS.

Additional design systems were neither analyzed nor registered as benchmark
entries.

## Sources opened

Reconciled machine-readably against the source register on 2026-07-15 (see the
correction record at the end of this document).

| Metric | Count |
| --- | --- |
| Benchmark source URLs | 31 |
| Standards reference URLs | 2 |
| **Total opened official URLs** | **33** |
| Sources with usable evidence | 27 |
| Sources without usable evidence | 6 |
| Access-limited but still usable | 4 |

Per system (URLs / usable): Carbon 5/4 · Fluent 2/2 · Material 4/2 · Primer 3/2
· Atlassian 2/2 · Spectrum 2/2 · SAP 2/1 · SLDS 1/1 · GOV.UK 4/4 · USWDS 6/5.
Benchmark subtotal 31/25, plus standards 2/2 = 33/27.

Standards: WCAG 2.2 and the Design Tokens Format Module — used only for framing,
never as benchmark entries.

## Benchmark dimensions

All 14 dimensions (A–N) were examined for all 10 systems, giving **140 matrix
cells**, each carrying exactly one permitted status.

Distribution over the 140 cells: Verified 68 · Partially verified 37 · Not found
in reviewed official sources 35 · Not applicable 0 · Not verified due to access
limitation 0. Usable evidence covers 105 of 140 cells.

Coverage ranged from 10/10 (A, B, C, G, L) down to 2/10 (K — localization). Gaps
were recorded with the permitted evidence-status vocabulary rather than filled
from memory or inference.

## Central findings

1. **Tool coupling in token workflows is common, largely undocumented, and not
   presented as a risk by the systems themselves.** Material documents a token
   workflow running through a proprietary design tool and its plugin. This is
   the single most decision-relevant finding: it validates DEC-S-004 and
   RISK-004 with evidence rather than intuition. No reviewed system documented
   tool-independence as an explicit goal.
2. **No reviewed system documented PDF, presentation, or diagram standards.**
   Reviewed systems are product-interface systems that touch brand at the edges.
   This is the largest apparent white space — and the most tempting to overstate.
3. **No reviewed system stated an offline or self-hosted guarantee**, though
   self-containable distribution is common. The differentiator would be the
   commitment, not the capability.
4. **Every system permits product-level variation; none published its limits.**
   The mechanism is universal; the governed constraint is the open question.
5. **Foundations → components → patterns is settled industry structure** and is
   not a differentiator.
6. **The four strongest observed practices are all governance, not design:**
   published per-component maturity states (USWDS), published conformance
   evidence (Primer), explicitly stating what the system does not guarantee
   (GOV.UK), and naming who maintains each contributed part (Carbon).
7. **WCAG 2.2 itself states that even AAA conformance will not serve every
   disability** — decisive for how CDS may ever phrase an accessibility
   statement.
8. **The reviewed token interoperability draft is explicitly a preview** that
   instructs readers not to implement it or cite it as authoritative — so no
   token format may be selected on its basis.
9. **Licensing is never one decision.** Documentation, code, fonts, icons, and
   brand assets routinely sit on different terms; brand assets are the most
   restricted category almost everywhere.
10. **Contribution governance is the thinnest area in public documentation** —
    six of ten systems yielded no external contribution process in reviewed
    pages.

## Hypothesis assessments

| ID | Assessment | Uniqueness risk |
| --- | --- | --- |
| HYP-001 Unified multi-channel foundation | Moderately supported | High |
| HYP-002 Offline and self-hosted consumption | Moderately supported | Medium |
| HYP-003 Operations-oriented experience patterns | Not verifiable in this research | High |
| HYP-004 Design-code-documentation convergence | Moderately supported | Medium |
| HYP-005 Governed product-family flexibility | Moderately supported | Medium-high |
| HYP-006 Evidence-based adoption | Common industry practice, not differentiating alone | Low |
| HYP-007 Accessibility, localization, privacy, security | Weakly supported | High |
| HYP-008 Small-team and enterprise applicability | Weakly supported | High |

**No hypothesis reached "Strongly supported."** That is itself the key result.
Every hypothesis received counterevidence or an explicit limitation. All eight
remain labelled Research hypothesis; none was presented as an accepted decision.
Exactly HYP-001 … HYP-008 exist; no further hypothesis IDs were created.

## New risks

RISK-010 … RISK-013 added, all Monitored, qualitative assessment only, owner
roles marked provisional until CDS-WP-006. Range now RISK-001 … RISK-013,
count 13. Existing risks were not redefined.

Each new risk is tied to a concrete research exposure: RISK-010 to the
non-copying boundary, RISK-011 to the fixed large-publisher sample, RISK-012 to
the dated snapshot (already evidenced by one moved domain and two systems
mid-transition), RISK-013 to the fact that every differentiation claim rests on
absence from public documentation.

## Decisions

**Unchanged.** DEC-S-001 … DEC-S-012, exactly 12. No new decision, no
modification, no ADR. Research findings and hypotheses are not normative design
or architecture decisions.

## Files created and changed

### Created

| Path | Content |
| --- | --- |
| `docs/research/BENCHMARK_SOURCE_REGISTER.md` | Every official URL opened, per system, with title, type, method, dimensions, evidence status, access date, and notes on redirects and failures. |
| `docs/research/DESIGN_SYSTEM_BENCHMARK.md` | Purpose, non-normative status, methodology, source rules, ten system profiles, cross-system findings, practices not to copy, implications for CDS-WP-004/005/006/007, unresolved questions. |
| `docs/research/BENCHMARK_EVIDENCE_MATRIX.md` | Ten systems × 14 dimensions with evidence status and short observations; coverage summary. No scores, no ranking. |
| `docs/research/CDS_DIFFERENTIATION_HYPOTHESES.md` | HYP-001…008 with assessment, supporting evidence, counterevidence, uniqueness risk, potential value, validation required, follow-up WP, status. |
| `docs/research/RESEARCH_LIMITATIONS.md` | Date range, source and access constraints, unavailable pages, uneven depth, public-vs-internal boundary, language, volatility, copyright boundary, limits of licensing and differentiation claims, required future validation. |
| `project-brain/CDS_WP_003_BENCHMARK_AND_DIFFERENTIATION_RESEARCH_NOTES.md` | This document. |

### Changed

| Path | Change |
| --- | --- |
| `docs/risks/RISK_REGISTER.md` | Range extended to RISK-001…013; RISK-010…013 appended. Existing risks unchanged. |
| `project-system/PROJECT_PROFILE.md` | WP status, research status, benchmarked systems count, hypotheses count, risk range, research links. |
| `project-system/NEXT_PHASE.md` | Rewritten for CDS-WP-004 including objective, research input to carry forward, and prohibitions. |
| `project-system/WORK_PACKAGES.md` | CDS-WP-003 Completed, CDS-WP-004 Next. No new WPs. |
| `project-system/CONTEXT_PACK_FOUNDATION.md` | Benchmark section, risk range, research links, next WP. Remains explicitly non-normative. |
| `project-brain/PROJECT_BRAIN.md` | Benchmark scope, cross-system findings, hypotheses, new risks, next step. No benchmark table duplicated. |
| `README.md` | Benchmark research section, WP status, register ranges, research links. |
| `CLAUDE.md` | WP pointers; note that `docs/research/` is evidence, not normative. Skills-first, fail-closed, Allowed-Files, and Git rules preserved. |
| `CHANGELOG.md` | CDS-WP-003 entries under Unreleased, attributed per WP. No version or release announced. |

## Validations performed

All 35 required checks were executed. Summary: only Allowed Files touched; git
status and full diff reviewed; `git diff --check` clean; internal links resolve;
exactly ten systems with no additions; all 14 dimensions covered; every
observation carries an official source and access date; no search snippets or
third-party sources; permitted evidence vocabulary only; no numeric scores,
rankings, or winner; HYP-001…008 exactly, each with counterevidence, none as an
accepted decision; DEC-S-001…012 unchanged at exactly 12 with no ADR;
RISK-010…013 added for a total of 13; no visual, technology, tool, token-format,
licensing, or publication decision; no assets downloaded; skill files, manifest,
and provenance unchanged; only the seven authorized Skills used; Context Pack
still explicitly non-normative; WP status consistent; no Git write action.

## Deviations

None. The work package was executed within the defined scope, Allowed Files,
authorized Skills, and authorized sources.

## Access problems

| Source | Problem | Handling |
| --- | --- | --- |
| `experience.sap.com/fiori-design-web/` | HTTP 301 to the corporate domain. | Redirect recorded; target used. |
| `www.sap.com/design-system/fiori-design-web/` | HTTP 403 via fetch. | Read via page view; both recorded. |
| `m3.material.io/` and `/foundations/design-tokens/overview` | Title only via fetch. | Marked `Not verified due to access limitation`; sibling pages used via page view. |
| `primer.style/product/getting-started/contributing/` | Navigation only. | Marked `Not found in reviewed official sources`. Contribution process not obtained. |
| `designsystem.digital.gov/components/` | Redirect notice without content. | Recorded; superseded by the overview page. |
| `spectrum.adobe.com/`, `lightningdesignsystem.com/` | Title only via fetch. | Read successfully via page view. |

No source was skipped while still reporting PASS. No conclusion was added from
memory to fill a gap.

## Open notes

- **Coverage is uneven and the unevenness is review depth, not system quality.**
  Atlassian (2 pages) and SAP (1 usable page) carry more "not found" entries than
  better-reviewed systems. This is stated in the limitations and must not be read
  as those systems being less mature.
- **Dimension K (localization) at 2/10 is the weakest result** and reflects
  review depth plus an English-only review. It must not be cited as an industry
  finding.
- **HYP-003 could not be assessed at all**, and the most likely counterexamples
  (enterprise pattern libraries at SAP, SLDS, Carbon) were the thinnest-reviewed.
  A deeper pattern review would need its own authorized work package.
- Licensing and publication still carry no assigned work package in the boundary
  matrix; the benchmark strengthens the case that this needs one, but **Claude
  does not extend the roadmap**. Nova decision required.
- All changes are uncommitted. Commit authority rests with the Human Maintainer.

---

## Correction record — Research Metrics and Evidence Reconciliation

- **Date:** 2026-07-15
- **Trigger:** The commit was held because the quantitative research metrics were
  inconsistent across artifacts.
- **Character:** A bounded correction and reconciliation run **inside**
  CDS-WP-003. Not a new work package; not added to the roadmap.
- **Method:** Machine-readable counting of the register tables and the matrix
  cells, then documentary consistency checking. **No new web research; no source
  reopened; no benchmark content extended.**

### Defects found and corrected

| # | Defect | Was | Now |
| --- | --- | --- | --- |
| 1 | Sources with usable evidence — arithmetic error. Per-system usable counts sum to 25 benchmark + 2 standards. | 26 | **27** |
| 2 | "Entries recording a redirect or access failure: 5" — matched no verifiable set, and conflated *access-limited but usable* with *no usable evidence*. | 5 | Replaced by two separate, classified counts: **6** without usable evidence, **4** access-limited but still usable. |
| 3 | Two opened URLs were never registered, contradicting the register's own rule that every opened page is registered: `carbondesignsystem.com/` and `m3.material.io/foundations/design-tokens/overview`. Both were opened, both yielded no usable body, both were superseded. | 31 opened | **33 opened** (31 benchmark + 2 standards) |
| 4 | Dimension F coverage miscounted in the matrix summary. Actual F cells: 2 Verified + 3 Partially verified. | F 6/10 | **F 5/10** |
| 5 | `RESEARCH_LIMITATIONS.md` cited `m3.material.io/foundations/design-tokens/overview`, a URL absent from the register. | Dangling reference | URL registered; limitations aligned to the register |
| 6 | The status distribution reported to Nova (70/40/37/1/1 = 149) was a whole-document text count, not the matrix cells. | 149 "cells" | **140 cells**: 68 / 37 / 35 / 0 / 0 |

### Verified figures after reconciliation

- Benchmark source URLs **31** · Standards **2** · Total opened **33**
- Usable evidence **27** · Without usable evidence **6** · Access-limited but
  still usable **4**
- Matrix **140 cells** (10 × 14) · usable **105** · Verified **68** ·
  Partially verified **37** · Not found **35** · Not applicable **0** · Not
  verified due to access limitation **0**

### Root cause

The original figures were asserted from working memory during writing rather
than derived from the artifacts. The two `Not applicable` redirect rows were
double-counted against the access-failure line while also being netted out of
the usable count, and the status distribution was produced by a text grep that
swept prose, legends, and the coverage summary alongside the table cells. Nothing
in the research method was wrong; the **reporting arithmetic** was.

### Unchanged by this run

No finding, hypothesis, assessment, decision, risk, or work package was altered.
Decisions remain DEC-S-001 … DEC-S-012 (12), risks RISK-001 … RISK-013 (13),
hypotheses HYP-001 … HYP-008 (8), all still Research hypothesis. The ten
benchmark systems are unchanged. **No hypothesis assessment moved**, and the
headline conclusion is untouched: no hypothesis reached "Strongly supported".

The corrections are quantitative and classificatory only. The `F 6/10 → 5/10`
change slightly weakens component-maturity coverage and therefore strengthens,
rather than weakens, the caution already recorded around maturity evidence.

## Completion status

CDS-WP-003 is Completed against its Definition of Done, with metrics reconciled,
and reported for Human Maintainer review.
