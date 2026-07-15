# Benchmark Evidence Matrix

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-003 — Benchmark and Differentiation Research
- **Access date for all evidence:** 2026-07-15
- **Status:** Research evidence — **not normative**

## How to read this matrix

Each cell records the evidence status found in reviewed official sources and a
short paraphrased observation. Sources are traceable through
[BENCHMARK_SOURCE_REGISTER.md](BENCHMARK_SOURCE_REGISTER.md).

**Evidence status vocabulary:** `Verified` · `Partially verified` ·
`Not found in reviewed official sources` · `Not applicable` ·
`Not verified due to access limitation`

### Critical reading rules

- **No numeric scores. No ranking. No winner.** Systems are not comparable on a
  single axis, and they serve different mandates.
- `Not found in reviewed official sources` means **this review did not find it**.
  It does not mean the system lacks the practice. Every system reviewed almost
  certainly has undocumented internal practice this research cannot see.
- Absence of evidence is a limitation of the review, not a weakness of the
  system.

### Systems

`CAR` Carbon · `FLU` Fluent 2 · `MAT` Material 3 · `PRI` Primer ·
`ATL` Atlassian · `SPE` Spectrum / Spectrum 2 · `SAP` SAP Fiori ·
`SLD` SLDS 2 · `GOV` GOV.UK · `USW` USWDS

---

## A. Strategic position

| System | Status | Observation |
| --- | --- | --- |
| CAR | Verified | Vendor-funded and vendor-built, deliberately released as open source for outside use and contribution, while also serving internal business units under an inner-source model. Positioned as the digital expression of the corporate brand. |
| FLU | Verified | Vendor system spanning several platforms, addressed to designers and developers; a predecessor version is still linked. |
| MAT | Partially verified | Positioned through its foundations as a general-purpose UI system with explicit brand-expression support. Homepage not retrievable by the method used. |
| PRI | Verified | Vendor system for one company's products, explicitly split into product UI and brand UI. |
| ATL | Verified | Vendor system whose stated aim is cohesion and familiarity across the company's product family. |
| SPE | Verified | Vendor system for internal product teams, stated purpose being team efficiency and cross-application cohesion. |
| SAP | Verified | Vendor system for enterprise applications, described as modular and multi-technology with central components that products may extend. |
| SLD | Verified | Vendor system for a platform ecosystem, addressed separately to administrators, designers, and developers. |
| GOV | Verified | Public-sector system whose stated purpose is consistency across government services and reuse of other teams' research. |
| USW | Verified | Public-sector system maintained by a government agency, serving many agencies and sites. |

## B. System scope

| System | Status | Observation |
| --- | --- | --- |
| CAR | Verified | Working code, design kits, human interface guidance, and a contributor community; patterns harvested from real products; data visualization guidance in scope. |
| FLU | Verified | Design assets, development guides, components per platform, accessibility tooling. |
| MAT | Verified | Foundations covering accessibility, content design, customization, tokens, interaction states, and layout. |
| PRI | Verified | Product UI, brand UI, icon set, tokens, accessibility guidance, brand toolkit. |
| ATL | Verified | Foundations including colour, typography, iconography, grid, tokens, accessibility; guidance and onboarding resources. |
| SPE | Verified | Components, guidelines, tools, downloadable resources, and multiple implementations. |
| SAP | Verified | UI elements and patterns across technologies, UI kits, visual design foundations, accessibility tooling, per-platform guidelines. |
| SLD | Verified | Foundations, components, patterns, accessibility, tools, and developer guidance. |
| GOV | Verified | Styles, components, patterns, community, accessibility. |
| USW | Verified | Components, patterns, design tokens, utilities, templates. |

## C. Information architecture

| System | Status | Observation |
| --- | --- | --- |
| CAR | Verified | Separates system explanation, guidelines, components, patterns, and data visualization; per-page source-edit links; visible last-updated date and implementation version. |
| FLU | Verified | Organized by activity (design, develop, components) and by platform. |
| MAT | Verified | Foundations grouped separately from components; explicit terminology section. |
| PRI | Verified | Split by audience surface: product UI, brand UI, shared foundations. |
| ATL | Verified | Foundations grouped as a distinct layer; separate onboarding and news areas. |
| SPE | Partially verified | Principles, resources, and implementations separated on the entry page; deeper structure not reviewed. |
| SAP | Verified | Split by platform, with foundations, patterns, components, and technologies per platform. |
| SLD | Verified | Distinct sections for foundations, develop, components, patterns, accessibility, tools; predecessor system explicitly separated. |
| GOV | Verified | Get started, styles, components, patterns, community, accessibility; roadmap surfaced. |
| USW | Verified | Components separated from patterns, tokens, utilities, templates; lifecycle and status given their own pages. |

## D. Source-of-truth model

Undocumented internal processes were not inferred for any system.

| System | Status | Observation |
| --- | --- | --- |
| CAR | Partially verified | Design kits in a proprietary design tool and code implementations both maintained; relationship between them stated as maintained assets rather than as a documented synchronization mechanism. |
| FLU | Partially verified | Design assets and code implementations both offered; synchronization mechanism not described in reviewed sources. |
| MAT | Verified | Token workflow is documented **through a proprietary design-tool plugin**: tokens are generated and edited as styles inside the tool, then exported to named platform targets. A downloadable baseline package format is offered. This is the clearest tool-coupled source-of-truth chain observed. |
| PRI | Not found in reviewed official sources | Tokens and foundations are published; the design-to-code source relationship was not described in the pages reviewed. |
| ATL | Partially verified | Tokens stated to be the single source of truth for design decisions, with a searchable library; the mechanism linking design assets and code was not described on the page reviewed. |
| SPE | Partially verified | Guidelines are positioned as authoritative alongside separate open-source implementations, implying documentation-led truth; mechanism not detailed. |
| SAP | Partially verified | Central component definitions extended by products; UI kits offered; synchronization mechanism not described. |
| SLD | Verified | Architecture stated to prioritize CSS custom properties, with tooling to validate, migrate, and create components, and design-tool-to-code generation referenced. |
| GOV | Verified | Documentation site and frontend implementation are deliberately separate repositories, making the published guidance and the code distinct artifacts. |
| USW | Partially verified | Source files and precompiled assets distributed together; design-asset relationship not described in reviewed sources. |

## E. Token and theming model

No token values or proprietary naming schemes are reproduced.

| System | Status | Observation |
| --- | --- | --- |
| CAR | Partially verified | Separate packages exist for colour, type, layout, motion, and themes, implying a layered element model; theming packaged as its own concern. |
| FLU | Not found in reviewed official sources | Token layering not described in reviewed pages. |
| MAT | Verified | Tokens presented as the building blocks shared across designs, tools, and code; a baseline theme with default values is customizable; export targets are platform-specific. |
| PRI | Partially verified | Tokens published as a shared foundation across colour, spacing, and typography; layering not described on the pages reviewed. |
| ATL | Partially verified | Tokens described as the single source of truth for naming and storing design decisions; a searchable library exists; raw-versus-semantic layering not stated on the page reviewed. |
| SPE | Not found in reviewed official sources | Token model not described in reviewed pages. |
| SAP | Partially verified | Central components may be extended or modified per product, implying a customization layer; token mechanics not described in reviewed pages. |
| SLD | Verified | Architecture explicitly prioritizes CSS custom properties and advanced theming, presented as enabling future theme variants. |
| GOV | Not found in reviewed official sources | Token model not described in reviewed pages. |
| USW | Partially verified | Design tokens documented as a distinct section alongside components and utilities; layering not reviewed. |

## F. Component and pattern maturity

| System | Status | Observation |
| --- | --- | --- |
| CAR | Partially verified | Patterns harvested from shipping products and contributed back; contributed items list maintainers; the core team triages unmaintained contributions. No public per-component maturity label observed in reviewed pages. |
| FLU | Partially verified | Parallel component lines coexist with different maturity and adoption profiles; per-component maturity labels not observed. |
| MAT | Not found in reviewed official sources | Per-component maturity labelling not found in reviewed pages. |
| PRI | Not found in reviewed official sources | Per-component maturity labelling not found in reviewed pages. |
| ATL | Not found in reviewed official sources | Per-component maturity labelling not found in reviewed pages. |
| SPE | Not found in reviewed official sources | Per-component maturity labelling not found in reviewed pages. |
| SAP | Not found in reviewed official sources | Per-component maturity labelling not found in reviewed pages. |
| SLD | Partially verified | Component creation and validation tooling referenced; maturity labels not observed in reviewed pages. |
| GOV | Verified | Components and patterns pass a stated contribution-criteria review before inclusion; per-item public discussion. |
| USW | Verified | **The most explicit maturity model observed.** Four public phases (proposal, development, released, deprecated) with named states. Released states distinguish experimental, stable, and use-with-caution, with stated meanings including accessibility-test expectations and production history. Deprecated and retired are distinct. |

## G. Accessibility and inclusive design

| System | Status | Observation |
| --- | --- | --- |
| CAR | Verified | Components follow an internal accessibility checklist based on WCAG AA, Section 508, and European standards. States that individually accessible components are only part of building an accessible product. |
| FLU | Partially verified | Accessibility tooling offered (focus order, contrast checking); conformance target not stated in reviewed pages. |
| MAT | Verified | Accessibility is a named foundation of the system rather than an appendix. |
| PRI | Verified | **The most explicit conformance-evidence model observed.** States an aim for WCAG 2.2 AA conformance, references publicly published conformance reports, and names Section 508. Accessibility designers embedded in product teams; shared frameworks and checklists provided. |
| ATL | Partially verified | Accessibility listed as a foundation; conformance target not stated on the page reviewed. |
| SPE | Verified | Spectrum 2 states inclusive design as a direction, with personalization for size, scale, colour, and contrast. |
| SAP | Partially verified | An accessibility toolkit is offered and framed as applying from the start of the product experience; conformance target not stated in reviewed pages. |
| SLD | Partially verified | Accessibility is a top-level section; conformance target not stated on the page reviewed. |
| GOV | Verified | **The clearest responsibility split observed.** States that using the system does not by itself make a service accessible and that teams must still do research, design, development, and testing. Regulatory work described as continuous and iterative rather than finished. |
| USW | Verified | Accessibility testing is embedded in the lifecycle: the experimental state is defined as passing accessibility tests while still subject to change. |

## H. Governance and contribution

| System | Status | Observation |
| --- | --- | --- |
| CAR | Verified | Open contribution encouraged; contributed components and patterns carry named maintainers; the core team triages items without maintainers; support runs primarily through the public repository. |
| FLU | Partially verified | A code of conduct is adopted; a detailed contribution process was not found in reviewed pages. |
| MAT | Not found in reviewed official sources | External contribution process not found in reviewed pages. |
| PRI | Not found in reviewed official sources | Contribution process not obtained through the route reviewed. |
| ATL | Not found in reviewed official sources | External contribution process not found in reviewed pages. |
| SPE | Partially verified | Spectrum 2 direction described as shaped collectively by an internal cross-disciplinary community; external contribution process not stated. |
| SAP | Partially verified | A community is referenced; formal contribution acceptance process not found in reviewed pages. |
| SLD | Not found in reviewed official sources | Contribution process not found in reviewed pages. |
| GOV | Verified | Explicit staged path: propose, develop, then review against stated contribution criteria; community principles and code of conduct; public per-item discussion; regular community sessions. Reviewed page describes participation clearly but does not state who holds final decision authority. |
| USW | Verified | Proposal phase is public and time-bounded, with a stated minimum comment period, explicit evaluation outcomes including approved, conditionally approved, returned for revision, and will-not-pursue. |

## I. Versioning, migration, and deprecation

| System | Status | Observation |
| --- | --- | --- |
| CAR | Verified | Long release history; documentation surfaces the current implementation version and a last-updated date. |
| FLU | Verified | Parallel major lines coexist for different consumer generations, with a documented migration path between them and per-package changelogs. |
| MAT | Not found in reviewed official sources | Release and deprecation model not found in reviewed pages. |
| PRI | Not found in reviewed official sources | Versioning model not found in reviewed pages. |
| ATL | Not found in reviewed official sources | Versioning model not found in reviewed pages. |
| SPE | Verified | A major generational successor is communicated publicly and separately from the current system, with the predecessor kept available during transition. |
| SAP | Partially verified | A what's-new channel communicates releases and enhancements; formal deprecation policy not found in reviewed pages. |
| SLD | Verified | A successor generation with its own site and version label, an explicit link back to the predecessor, and role-based transition instructions. |
| GOV | Partially verified | The website and the frontend implementation are versioned separately; a roadmap is surfaced; formal deprecation policy not reviewed. |
| USW | Verified | Deprecation and retirement are formal, named lifecycle states, distinguishing "no longer maintained but present" from "removed". |

## J. Distribution and technology coupling

No packages were installed or tested.

| System | Status | Observation |
| --- | --- | --- |
| CAR | Verified | Distributed as many scoped packages; first-party implementations for a core set of technologies, with several framework bindings explicitly community-maintained rather than core-maintained. |
| FLU | Verified | Separate package lines per generation plus a web-components line; platform coverage spans web and native targets. |
| MAT | Verified | Token export targets are named platform-specific outputs; the documented workflow depends on a proprietary design tool plus its plugin. |
| PRI | Partially verified | Component libraries and an icon set published; runtime dependencies not reviewed. |
| ATL | Not found in reviewed official sources | Distribution model not reviewed. |
| SPE | Verified | Three separate open-source implementations offered, spanning a CSS-level implementation, a framework implementation, and a web-components implementation. |
| SAP | Verified | Multi-technology by design, with distinct per-platform guideline sets. |
| SLD | Verified | Architecture centred on CSS custom properties, which lowers framework coupling at the styling layer. |
| GOV | Verified | Implementation distributed separately from the documentation site; the site itself is a conventional buildable codebase. |
| USW | Verified | Distributed via a package registry and as direct downloadable releases, shipping both precompiled assets and source files. |

**Offline and self-hosted implication (cross-system):** `Partially verified`.
Several systems ship self-containable assets (notably packaged or downloadable
distributions). No reviewed system stated an explicit offline or self-hosted
consumption guarantee, and none was found addressing mandatory external runtime
services as a documented constraint.

## K. Localization and content

| System | Status | Observation |
| --- | --- | --- |
| CAR | Not found in reviewed official sources | Localization guidance not found in reviewed pages. |
| FLU | Not found in reviewed official sources | Localization guidance not found in reviewed pages. |
| MAT | Verified | Content design is a named foundation covering UX writing and information design. |
| PRI | Not found in reviewed official sources | Localization guidance not found in reviewed pages. |
| ATL | Not found in reviewed official sources | Localization guidance not found in reviewed pages. |
| SPE | Partially verified | Spectrum 2 states adaptation across contexts and personalization preferences; bidirectional or multi-script guidance not found in reviewed pages. |
| SAP | Not found in reviewed official sources | Localization guidance not found in reviewed pages. |
| SLD | Not found in reviewed official sources | Localization guidance not found in reviewed pages. |
| GOV | Not found in reviewed official sources | Localization guidance not found in reviewed pages; content-related patterns exist but were not reviewed at that depth. |
| USW | Not found in reviewed official sources | Localization guidance not found in reviewed pages. |

**Note:** This dimension is the weakest across the review. The gap is largely a
depth-of-review limitation, not evidence of absence.

## L. Multi-channel coverage

Only documented coverage is recorded.

| System | Status | Observation |
| --- | --- | --- |
| CAR | Verified | Product UI, brand relationship via a corporate design language, documentation, and **data visualization** with its own guidance and implementation. No PDF/report, presentation, or diagram standard found in reviewed pages. |
| FLU | Partially verified | Product UI across several platforms; other channels not found in reviewed pages. |
| MAT | Partially verified | Product UI plus content design; other channels not found in reviewed pages. |
| PRI | Verified | **Product UI and brand UI are explicitly separated**, with a brand toolkit and an icon set as shared foundations — the clearest product/brand channel split observed. No PDF, presentation, or diagram standard found. |
| ATL | Partially verified | Product UI and foundations; other channels not found in reviewed pages. |
| SPE | Partially verified | Product UI, icons, illustrations, and fonts referenced; other channels not found in reviewed pages. |
| SAP | Verified | Product UI across web, Android, and iOS with per-platform guidelines; visual design foundations. No PDF, presentation, or diagram standard found. |
| SLD | Partially verified | Product UI, patterns, and tooling; other channels not found in reviewed pages. |
| GOV | Partially verified | Product/service UI, styles, patterns; other channels not found in reviewed pages. |
| USW | Partially verified | Product UI, templates, utilities; other channels not found in reviewed pages. |

**Cross-system gap:** In the reviewed official sources, **no system documented
standards for PDF reports, presentations, or diagrams**. Data visualization was
documented by one system; an explicit product/brand channel split by another.
This gap is the single most consistent finding of the review, and it is bounded
by review depth — see [Research Limitations](RESEARCH_LIMITATIONS.md).

## M. Evidence and quality control

| System | Status | Observation |
| --- | --- | --- |
| CAR | Partially verified | User research stated as an input to the system; contributed items carry maintainers; testing regime not detailed in reviewed pages. |
| FLU | Not found in reviewed official sources | Testing and acceptance evidence not found in reviewed pages. |
| MAT | Not found in reviewed official sources | Testing and acceptance evidence not found in reviewed pages. |
| PRI | Verified | Published conformance reports serve as external, checkable accessibility evidence; issue reporting channel provided. |
| ATL | Not found in reviewed official sources | Testing and acceptance evidence not found in reviewed pages. |
| SPE | Not found in reviewed official sources | Testing and acceptance evidence not found in reviewed pages. |
| SAP | Not found in reviewed official sources | Testing and acceptance evidence not found in reviewed pages. |
| SLD | Partially verified | Validation and migration tooling referenced; evidence model not detailed in reviewed pages. |
| GOV | Verified | An accessibility statement documents how accessible the frontend, its documentation, and the site itself are; user-research submission is an explicit community input with a template. |
| USW | Verified | Accessibility testing is a gating condition inside the lifecycle rather than a separate claim; status is published per component. |

## N. Licensing and publication model

No legal advice is given. No CDS licence is selected or recommended.

| System | Status | Observation |
| --- | --- | --- |
| CAR | Verified | Permissive licence stated for the repository. Publicly open while simultaneously serving internal business units under an inner-source model. |
| FLU | Verified | **Notable split:** a permissive licence stated for repository files, while fonts and icons are governed by a separate assets licence agreement. Code and brand assets are deliberately not on the same terms. |
| MAT | Not found in reviewed official sources | Licence terms not found in reviewed pages. |
| PRI | Not found in reviewed official sources | Licence terms not found in reviewed pages. |
| ATL | Not found in reviewed official sources | Licence terms not found in reviewed pages. |
| SPE | Partially verified | Implementations described as open source; specific terms not reviewed. Downloadable fonts and icons are offered under unreviewed terms. |
| SAP | Not found in reviewed official sources | Licence terms not found in reviewed pages. |
| SLD | Not found in reviewed official sources | Licence terms not found in reviewed pages; the site carries a general all-rights-reserved notice and trademark statement. |
| GOV | Verified | Permissive licence stated for the documentation-site repository. |
| USW | Verified | **Public-domain dedication** stated for the project, with exceptions documented separately — the most permissive model observed, consistent with a government mandate. |

---

## Matrix size

| Metric | Count |
| --- | --- |
| Systems | 10 |
| Dimensions | 14 |
| **Matrix cells (10 × 14)** | **140** |

Every cell carries exactly one status from the permitted vocabulary. Counts in
this section were reconciled machine-readably against the tables above on
2026-07-15 and cover **only the 140 matrix cells** — not prose elsewhere in this
document.

## Evidence status distribution

| Status | Cells | Share of 140 |
| --- | --- | --- |
| Verified | 68 | 48.6 % |
| Partially verified | 37 | 26.4 % |
| Not found in reviewed official sources | 35 | 25.0 % |
| Not applicable | 0 | 0 % |
| Not verified due to access limitation | 0 | 0 % |
| **Total** | **140** | **100 %** |

`Not applicable` and `Not verified due to access limitation` are zero here by
design: both describe *sources*, not system–dimension pairs, and are used in the
[Source Register](BENCHMARK_SOURCE_REGISTER.md) instead.

Usable evidence (`Verified` or `Partially verified`) covers **105 of 140 cells
(75.0 %)**.

## Dimension coverage summary

| Dimension | Systems with Verified or Partially verified evidence |
| --- | --- |
| A. Strategic position | 10 / 10 |
| B. System scope | 10 / 10 |
| C. Information architecture | 10 / 10 |
| D. Source-of-truth model | 9 / 10 |
| E. Token and theming model | 7 / 10 |
| F. Component and pattern maturity | 5 / 10 |
| G. Accessibility and inclusive design | 10 / 10 |
| H. Governance and contribution | 6 / 10 |
| I. Versioning, migration, deprecation | 7 / 10 |
| J. Distribution and technology coupling | 9 / 10 |
| K. Localization and content | 2 / 10 |
| L. Multi-channel coverage | 10 / 10 |
| M. Evidence and quality control | 5 / 10 |
| N. Licensing and publication | 5 / 10 |
| **Total** | **105 / 140** |

All 14 dimensions were examined for all 10 systems. Gaps are recorded as
evidence statuses rather than filled by inference or memory.

## Related documents

- [Benchmark Source Register](BENCHMARK_SOURCE_REGISTER.md)
- [Design System Benchmark](DESIGN_SYSTEM_BENCHMARK.md)
- [CDS Differentiation Hypotheses](CDS_DIFFERENTIATION_HYPOTHESES.md)
- [Research Limitations](RESEARCH_LIMITATIONS.md)
