# Benchmark Source Register

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-003 — Benchmark and Differentiation Research
- **Access date for all entries:** 2026-07-15
- **Status:** Research evidence — **not normative**

## Purpose

This register lists every official source actually opened during CDS-WP-003. It
exists so that every observation in
[DESIGN_SYSTEM_BENCHMARK.md](DESIGN_SYSTEM_BENCHMARK.md) and
[BENCHMARK_EVIDENCE_MATRIX.md](BENCHMARK_EVIDENCE_MATRIX.md) can be traced to a
concrete URL.

## Rules applied

- Only pages actually opened are registered. Search results are not sources.
- Only official publisher domains and their official public repositories.
- No third-party sources: no encyclopedias, blogs, agency articles, comparison
  portals, social media, search snippets, AI summaries, mirrors, or third-party
  archives.
- Redirects and access failures are recorded rather than hidden.
- Observations are paraphrased. No page content is reproduced at length.

## Access methods

| Method | Meaning |
| --- | --- |
| Integrated page view | Claude Desktop's built-in web page view (renders JavaScript). |
| Integrated fetch | Claude Desktop's built-in page retrieval and conversion. |

No terminal network commands, no clone, no fetch, no scraping, no downloads.

## Evidence status vocabulary

`Verified` · `Partially verified` · `Not found in reviewed official sources` ·
`Not applicable` · `Not verified due to access limitation`

---

## 1. IBM Carbon Design System

| Page title | URL | Source type | Method | Dimensions | Evidence status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Carbon Design System (home) | `https://carbondesignsystem.com/` | Official documentation | Integrated fetch | — | Not verified due to access limitation | Returned truncated content without a usable body. Superseded by the deeper pages below. Registered because it was opened. |
| What is Carbon? | `https://carbondesignsystem.com/all-about-carbon/what-is-carbon/` | Official documentation | Integrated page view | A, B, D, F, H, J, M | Verified | Integrated fetch returned truncated content; the integrated page view succeeded. States open-source status, inner-source model, maintained implementations vs community-maintained ones, Figma kits, pattern harvesting. |
| Accessibility — Overview | `https://carbondesignsystem.com/guidelines/accessibility/overview/` | Official documentation | Integrated page view | G | Verified | States alignment with an internal accessibility checklist based on WCAG AA, Section 508, and European standards. |
| Data visualization — Get started | `https://carbondesignsystem.com/data-visualization/getting-started/` | Official documentation | Integrated page view | L | Verified | Charting guidance and separate charts implementation across several frameworks. |
| carbon (repository) | `https://github.com/carbon-design-system/carbon` | Official repository | Integrated fetch | H, I, J, N | Verified | Apache-2.0 stated; monorepo package list; large release count; contribution guidance referenced. |

## 2. Microsoft Fluent 2

| Page title | URL | Source type | Method | Dimensions | Evidence status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Fluent 2 | `https://fluent2.microsoft.design/` | Official documentation | Integrated fetch | A, B, C, G, J | Verified | Multi-platform design/develop/components structure; design tooling and accessibility tooling referenced; legacy version linked. |
| fluentui (repository) | `https://github.com/microsoft/fluentui` | Official repository | Integrated fetch | I, J, N | Verified | MIT stated for repository files; assets (fonts/icons) under a separate licence agreement; parallel v8/v9/web-components lines; documented migration path. |

## 3. Google Material Design 3

| Page title | URL | Source type | Method | Dimensions | Evidence status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Foundations | `https://m3.material.io/foundations` | Official documentation | Integrated page view | B, C, E, G, K | Verified | Foundations include accessibility, content design, customization/brand expression, tokens, interaction states, layout. |
| Design tokens — Overview | `https://m3.material.io/foundations/design-tokens/overview` | Official documentation | Integrated fetch | — | Not verified due to access limitation | Returned title only; no usable body. Superseded by the sibling page below, read via the page view. Registered because it was opened. |
| Design tokens — How to use tokens | `https://m3.material.io/foundations/design-tokens/how-to-use-tokens` | Official documentation | Integrated page view | D, E, J | Verified | Token workflow described via a proprietary design-tool plugin; baseline theme downloadable as a package format; export targets named. |
| Material Design (home) | `https://m3.material.io/` | Official documentation | Integrated fetch | A | Not verified due to access limitation | Fetch returned title only; homepage content not retrievable by that method. Strategic position taken from Foundations instead. |

## 4. GitHub Primer

| Page title | URL | Source type | Method | Dimensions | Evidence status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Primer | `https://primer.style/` | Official documentation | Integrated fetch | A, B, C, L | Verified | Separates product UI from brand UI; shared foundations; icon set; tokens. |
| Accessibility at GitHub | `https://primer.style/guides/accessibility/accessibility-at-github` | Official documentation | Integrated fetch | G, M | Verified | States an aim for WCAG 2.2 AA conformance; references published conformance reports and Section 508. |
| Contributing (product) | `https://primer.style/product/getting-started/contributing/` | Official documentation | Integrated fetch | H | Not found in reviewed official sources | The retrieved page returned navigation only; no contribution process content was obtained via this route. |

## 5. Atlassian Design System

| Page title | URL | Source type | Method | Dimensions | Evidence status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Atlassian Design System | `https://atlassian.design/` | Official documentation | Integrated fetch | A, B, C | Verified | Foundations enumerated including tokens and accessibility; cohesion across the product family stated as the goal. |
| Design tokens | `https://atlassian.design/foundations/tokens/` | Official documentation | Integrated fetch | E | Partially verified | Purpose of tokens stated (single source of truth for design decisions) and a searchable token library referenced; layering and theming not described on this page. |

## 6. Adobe Spectrum and Spectrum 2

Treated as one evolution line, not two benchmark entries.

| Page title | URL | Source type | Method | Dimensions | Evidence status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Spectrum, Adobe's design system | `https://spectrum.adobe.com/` | Official documentation | Integrated page view | A, B, J | Verified | Purpose stated as team efficiency and cross-application cohesion; three open-source implementations named; downloadable resources referenced. |
| Spectrum 2 | `https://s2.spectrum.adobe.com/` | Official documentation | Integrated page view | A, G, I, K | Verified | Describes a major evolution of the system: cross-context adaptation, personalization for size/scale/colour/contrast, community-shaped direction. |

## 7. SAP Fiori Design System

| Page title | URL | Source type | Method | Dimensions | Evidence status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| (redirect source) | `https://experience.sap.com/fiori-design-web/` | Official documentation | Integrated fetch | — | Not applicable | **HTTP 301** permanent redirect to the SAP corporate domain. Recorded as a redirect, not used as an evidence page. |
| SAP Fiori for Web | `https://www.sap.com/design-system/fiori-design-web/` | Official documentation | Integrated page view | A, B, E, J, L | Verified | Redirect target. Integrated fetch returned **HTTP 403**; the integrated page view succeeded. States a modular multi-technology approach with centrally defined components that products may extend or modify; per-platform guidelines. |

## 8. Salesforce Lightning Design System 2

| Page title | URL | Source type | Method | Dimensions | Evidence status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Lightning Design System 2 | `https://www.lightningdesignsystem.com/` | Official documentation | Integrated page view | A, B, C, E, I | Verified | States a new architecture prioritizing CSS custom properties, theming, role-based transition guidance, and an explicit link to the predecessor system. Version label observed. Integrated fetch returned title only; page view succeeded. |

## 9. GOV.UK Design System

| Page title | URL | Source type | Method | Dimensions | Evidence status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| GOV.UK Design System | `https://design-system.service.gov.uk/` | Official documentation | Integrated fetch | A, B, C | Verified | Purpose stated as consistency with the wider platform and reuse of other teams' research. |
| Community | `https://design-system.service.gov.uk/community/` | Official documentation | Integrated fetch | H | Verified | Propose → develop → review against contribution criteria; community principles and code of conduct; open discussion per component. |
| Accessibility | `https://design-system.service.gov.uk/accessibility/` | Official documentation | Integrated fetch | G, M | Verified | States that using the system does not by itself make a service accessible; further team work required; compliance described as continuous. |
| govuk-design-system (repository) | `https://github.com/alphagov/govuk-design-system` | Official repository | Integrated fetch | H, N | Verified | MIT stated; website codebase separated from the frontend implementation repository; code of conduct; CI checks. |

## 10. U.S. Web Design System

| Page title | URL | Source type | Method | Dimensions | Evidence status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| About USWDS | `https://designsystem.digital.gov/about/` | Official documentation | Integrated fetch | A, B | Verified | Government maintainer named; audience and multi-agency adoption stated. |
| Component lifecycle | `https://designsystem.digital.gov/components/lifecycle/` | Official documentation | Integrated fetch | F, I, M | Verified | Four public lifecycle phases with named maturity states and stated criteria, including a minimum public comment period and accessibility-test expectations. |
| Component status | `https://designsystem.digital.gov/components/status/` | Official documentation | Integrated fetch | F, I | Verified | Per-component lifecycle status tracked publicly, including proposal-phase items. |
| Components overview | `https://designsystem.digital.gov/components/overview/` | Official documentation | Integrated fetch | F | Partially verified | Component list with short descriptions; maturity labels live on the lifecycle/status pages rather than here. |
| Components (index) | `https://designsystem.digital.gov/components/` | Official documentation | Integrated fetch | — | Not applicable | Returned a redirect notice without content. Recorded for traceability; superseded by the overview page. |
| uswds (repository) | `https://github.com/uswds/uswds` | Official repository | Integrated fetch | I, J, N | Verified | CC0 1.0 public-domain dedication stated, with exceptions noted in the licence file; package distribution and precompiled assets; release history. |

---

## Standards references

Not benchmark systems. Used only to frame accessibility and token
interoperability.

| Page title | URL | Source type | Method | Purpose | Evidence status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Web Content Accessibility Guidelines (WCAG) 2.2 | `https://www.w3.org/TR/WCAG22/` | Official standard | Integrated fetch | Accessibility framing | Verified | Published as a W3C Recommendation dated 2024-12-12. Defines conformance levels A, AA, AAA. States explicitly that even AAA-conformant content will not be accessible to people with every type, degree, or combination of disability. |
| Design Tokens Format Module | `https://www.designtokens.org/tr/drafts/format/` | Official specification draft | Integrated fetch | Token interoperability framing | Verified | Self-identifies as a **preview draft** and explicitly **not** a W3C Standard. The document instructs readers not to implement this version and not to reference it as authoritative. Published by a Community Group; unstandardized and subject to change. |

**Boundary:** No CDS conformance is claimed against WCAG 2.2. No token format is
selected for CDS. The token draft's own status warning is recorded above and
must not be read as a CDS specification decision.

---

## Coverage summary

Figures below were reconciled machine-readably against the tables in this
document on 2026-07-15.

| Metric | Count |
| --- | --- |
| Benchmark systems reviewed | 10 |
| Benchmark source URLs | 31 |
| Standards reference URLs | 2 |
| **Total opened official URLs** | **33** |
| Sources with usable evidence (`Verified` or `Partially verified`) | 27 |
| Sources without usable evidence | 6 |

### Per system

| System | URLs | With usable evidence |
| --- | --- | --- |
| IBM Carbon Design System | 5 | 4 |
| Microsoft Fluent 2 | 2 | 2 |
| Google Material Design 3 | 4 | 2 |
| GitHub Primer | 3 | 2 |
| Atlassian Design System | 2 | 2 |
| Adobe Spectrum and Spectrum 2 | 2 | 2 |
| SAP Fiori Design System | 2 | 1 |
| Salesforce Lightning Design System 2 | 1 | 1 |
| GOV.UK Design System | 4 | 4 |
| U.S. Web Design System | 6 | 5 |
| **Benchmark subtotal** | **31** | **25** |
| Standards references | 2 | 2 |
| **Total** | **33** | **27** |

### Access and content limitations

Two distinct things are counted separately, because conflating them was the
source of an earlier miscount.

**Sources without usable evidence — 6.** These yielded nothing and are excluded
from the evidence base:

| Classification | Count | Sources |
| --- | --- | --- |
| `Not applicable` — redirect or no content, not used as an evidence page | 2 | `experience.sap.com/fiori-design-web/` (301); `designsystem.digital.gov/components/` (redirect notice) |
| `Not verified due to access limitation` — opened, no retrievable body | 3 | `m3.material.io/`; `carbondesignsystem.com/`; `m3.material.io/foundations/design-tokens/overview` |
| `Not found in reviewed official sources` — page retrieved, content absent | 1 | `primer.style/product/getting-started/contributing/` |

**Access-limited but still usable — 4.** These refused the integrated fetch or
returned only a title, but were read successfully via the integrated page view.
They carry full evidence status and are **counted among the 27 usable**, not
among the 6:

- `carbondesignsystem.com/all-about-carbon/what-is-carbon/` (fetch truncated)
- `www.sap.com/design-system/fiori-design-web/` (HTTP 403 via fetch)
- `spectrum.adobe.com/` (title only via fetch)
- `www.lightningdesignsystem.com/` (title only via fetch)

A source is therefore *access-limited* (retrieval method failed, another
succeeded) or *without usable evidence* (no method yielded content) — never
both.

## Related documents

- [Design System Benchmark](DESIGN_SYSTEM_BENCHMARK.md)
- [Benchmark Evidence Matrix](BENCHMARK_EVIDENCE_MATRIX.md)
- [CDS Differentiation Hypotheses](CDS_DIFFERENTIATION_HYPOTHESES.md)
- [Research Limitations](RESEARCH_LIMITATIONS.md)
