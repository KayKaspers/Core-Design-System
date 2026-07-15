# Research Limitations

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-003 — Benchmark and Differentiation Research
- **Status:** Research evidence — **not normative**

## Purpose

This document states what CDS-WP-003 could **not** establish. It exists so that
later work packages do not mistake the benchmark for a complete picture.

Read it before citing any finding from
[DESIGN_SYSTEM_BENCHMARK.md](DESIGN_SYSTEM_BENCHMARK.md) or
[CDS_DIFFERENTIATION_HYPOTHESES.md](CDS_DIFFERENTIATION_HYPOTHESES.md).

## Reviewed date range

All sources were accessed on **2026-07-15**. The review is a single-day snapshot.
No historical comparison was performed, and no source was re-checked for
stability.

## Source constraints

- Only official publisher documentation and official publisher repositories were
  used.
- Third-party sources were excluded by rule: encyclopedias, blogs, agency
  articles, comparison portals, social media, search snippets, AI summaries,
  unofficial mirrors, third-party archives.
- **Consequence:** where an official source is silent, this review is silent.
  Practices widely discussed outside official documentation are invisible here —
  by design, and at the cost of coverage.
- No package was installed, executed, or inspected. Distribution and runtime
  observations rest on documentation alone.
- No repository was cloned and no full repository analysis was performed. GitHub
  evidence comes from repository landing pages only.
- No assets were downloaded.

## Unavailable or inaccessible pages

All are registered in the [Source Register](BENCHMARK_SOURCE_REGISTER.md), which
holds the authoritative counts.

**Yielded no usable evidence (6)** — excluded from the evidence base:

| Source | Issue | Status |
| --- | --- | --- |
| `https://experience.sap.com/fiori-design-web/` | HTTP 301 permanent redirect to the corporate domain. The target was used instead. | Not applicable |
| `https://designsystem.digital.gov/components/` | Returned a redirect notice without content; superseded by the overview page. | Not applicable |
| `https://m3.material.io/` | Returned title only via fetch. Strategic position taken from the Foundations page instead. | Not verified due to access limitation |
| `https://m3.material.io/foundations/design-tokens/overview` | Returned title only via fetch; a sibling page was used via the page view. | Not verified due to access limitation |
| `https://carbondesignsystem.com/` | Returned truncated content without a usable body; superseded by deeper pages. | Not verified due to access limitation |
| `https://primer.style/product/getting-started/contributing/` | Returned navigation only. Contribution process not obtained. | Not found in reviewed official sources |

**Access-limited but still usable (4)** — the fetch method failed, the page view
succeeded. These carry full evidence status and count among the usable sources,
not among the six above:

| Source | Issue |
| --- | --- |
| `https://carbondesignsystem.com/all-about-carbon/what-is-carbon/` | Truncated via fetch; read via the page view. |
| `https://www.sap.com/design-system/fiori-design-web/` | HTTP 403 via fetch; read via the page view. |
| `https://spectrum.adobe.com/` | Title only via fetch; read via the page view. |
| `https://www.lightningdesignsystem.com/` | Title only via fetch; read via the page view. |

**Method effect:** several sites are JavaScript-rendered and are invisible to
the fetch method but readable via the page view. Early results from the fetch
method alone would have produced false "not found" conclusions. Any future
research must account for this; a "not found" from one method is not evidence.

## Systems with incomplete documentation coverage in this review

Coverage was uneven, and the unevenness is mostly **review depth**, not system
quality:

- **Deeply reviewed:** USWDS (lifecycle, status, licence), GOV.UK
  (contribution, accessibility, repository), Carbon (identity, accessibility,
  data visualization, repository).
- **Moderately reviewed:** Primer, Fluent, Material, SLDS, Spectrum.
- **Thinly reviewed:** Atlassian (2 pages), SAP (1 usable page).

**Consequence:** Atlassian and SAP carry more `Not found in reviewed official
sources` entries than better-reviewed systems. This must not be read as those
systems being less mature. It reflects how many of their pages were opened.

### Dimensions with the weakest coverage

Coverage counts the systems per dimension with `Verified` or `Partially
verified` evidence. They are reconciled against the
[Evidence Matrix](BENCHMARK_EVIDENCE_MATRIX.md), which holds the authoritative
figures.

| Dimension | Coverage | Note |
| --- | --- | --- |
| K. Localization and content | 2 / 10 | The weakest dimension. Content and localization pages were not systematically opened. This figure reflects review depth, **not** industry practice, and must not be cited as an industry finding. |
| F. Component and pattern maturity | 5 / 10 | Per-component labels require per-component pages. |
| M. Evidence and quality control | 5 / 10 | Testing regimes are rarely on entry-level pages. |
| N. Licensing and publication | 5 / 10 | Licence terms often live in files not opened. |
| H. Governance and contribution | 6 / 10 | Partly review depth, partly genuinely internal. |

Across the whole matrix, 105 of 140 cells carry usable evidence; the remaining
35 are recorded as `Not found in reviewed official sources`.

## Public documentation versus unknown internal practice

This is the single most important limitation.

Every system reviewed is maintained by an organization with internal processes
this research **cannot see**: design review, testing, acceptance, governance,
synchronization between design and code. Public documentation is a marketing and
enablement surface as much as a process record.

**Therefore:**

- No conclusion is drawn about any system's actual internal quality.
- `Not found in reviewed official sources` means exactly that — not "does not
  exist" and not "is weak."
- Undocumented internal processes were never inferred, per the work-package
  rule.
- Statements about what systems "do not do" are statements about their
  **public documentation only**.

## Language limitations

All sources were reviewed in English. Several systems serve international
organizations and may publish localized documentation with different or
additional content. Non-English documentation was not searched. This particularly
weakens dimension K (localization), where a language-limited review is close to
self-defeating.

## Version and update volatility

- Design systems ship continuously. One reviewed system displayed a
  same-day last-updated date and a specific implementation version; another
  displayed a page updated hours before access.
- Two systems (Spectrum, SLDS) are mid-generational-transition, so their
  documentation describes a moving target.
- One system's documentation domain has already moved (SAP), demonstrating that
  even URLs are not stable.
- **Consequence:** every finding here decays. Citing this benchmark in a later
  work package requires checking whether the source still says what it said on
  2026-07-15. This is registered as RISK-012.

## Copyright and non-copying boundary

Observed and enforced throughout:

- No design content, taxonomy, component structure, wording, palette,
  typography, icon form, or layout was reproduced.
- No token values or proprietary token naming schemes were copied.
- No logos or brand assets entered the repository.
- No long text passages, full tables, or documentation structures were copied.
- Foreign taxonomies are described abstractly only.
- Findings are synthesized, not imitated.
- Product and system names are used solely for source attribution.

This boundary intentionally reduces detail. Where a precise description would
have required reproducing a system's own structure, the observation was
generalized instead — losing specificity to stay inside the rule. This is
registered as RISK-010.

## Limits of the licensing observations

- Licence observations are **descriptive only**. No legal assessment, opinion,
  or advice is given or implied.
- Only 5 of 10 systems yielded licence terms in reviewed pages.
- Where a licence was named, its terms were not read, analyzed, or compared.
- The interaction between documentation, code, fonts, icons, and brand assets
  was observed in one case (Fluent) and inferred nowhere else.
- **No CDS licence is recommended, selected, or excluded.** Licensing,
  publication, and contribution rights remain undecided and are routed to
  CDS-WP-006.

## Limits of the differentiation assessment

- All eight hypotheses rest on **absence of public documentation**, which is
  systematically weaker than presence.
- **No hypothesis reached "Strongly supported."** The evidence does not
  currently justify a confident differentiation claim anywhere.
- One hypothesis (HYP-003) could not be assessed at all: pattern libraries were
  not opened, and the most likely counterexamples (enterprise systems) were the
  thinnest-reviewed.
- The benchmark set was fixed in advance and consists exclusively of large
  technology companies and national governments. It cannot speak to smaller,
  community, or commercial design systems — which directly caps HYP-008. This is
  registered as RISK-011.
- Comparative claims of the form "CDS would be first/only/best" are **not
  supported by this research** and were not made. This is registered as
  RISK-013.
- No claim is made that CDS is better than any reviewed system.

## Required future validation

Before any hypothesis becomes a decision:

1. **Real consumer demand** must be established, especially for HYP-001 and
   HYP-003. → CDS-WP-004
2. **Enterprise pattern libraries** (SAP, SLDS, Carbon) need targeted review
   before any operational-patterns claim. → requires explicit authorization
3. **Localization coverage** needs proper review before any claim about industry
   practice in dimension K. → requires explicit authorization
4. **Feasibility** of tool-independent normative sources must be demonstrated,
   not assumed. → CDS-WP-005
5. **Source re-verification** is required for any finding cited later, given
   RISK-012.
6. **Capacity realism**: several observed practices (public proposal periods,
   parallel generations, published conformance reports) carry costs CDS has not
   yet assessed against its maintainer capacity.

Any research extension needs its own authorized work package with named sources
and method. **The roadmap is not extended by this document.**

## Related documents

- [Benchmark Source Register](BENCHMARK_SOURCE_REGISTER.md)
- [Design System Benchmark](DESIGN_SYSTEM_BENCHMARK.md)
- [Benchmark Evidence Matrix](BENCHMARK_EVIDENCE_MATRIX.md)
- [CDS Differentiation Hypotheses](CDS_DIFFERENTIATION_HYPOTHESES.md)
- [Risk Register](../risks/RISK_REGISTER.md) — RISK-010 … RISK-013
