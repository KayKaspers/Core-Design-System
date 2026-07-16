# Accessibility Source Register

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-007 — Accessibility and Inclusive Design Policy
- **Access date for all entries:** 2026-07-16
- **Status:** Research evidence — **not normative**

## Purpose

Lists every official standards source **actually opened** during CDS-WP-007, so
that every accessibility statement in the policy can be traced to a concrete URL
and its correct normative status.

## Rules applied

- Only official publisher sources: W3C, WAI, ETSI.
- **Every opened URL is registered** — including where the content was
  unusable, access was restricted, or only a status was obtained.
- Normative requirements are derived **only** from the WCAG 2.2 Recommendation.
  Understanding, Techniques, APG, and supplemental guidance are informative.
- No third-party sources, blogs, summaries, or search snippets.
- No standards PDF was downloaded.
- Observations are paraphrased. No normative criterion text is reproduced.

## Access methods

| Method | Meaning |
| --- | --- |
| Integrated fetch | Claude Desktop's built-in page retrieval. |
| Integrated page view | Claude Desktop's built-in page view (renders JavaScript). |

No terminal network commands, no downloads, no scraping.

---

## W3C — Normative specifications

| # | Title | URL | Type | Status | Access | Used for | Usability | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Web Content Accessibility Guidelines (WCAG) 2.2 | `https://www.w3.org/TR/WCAG22/` | Standard | **Normative** — W3C Recommendation, published **2024-12-12** | Integrated page view + fetch | The complete Level A and AA success criteria set; the normative basis of the CDS target | **Full** | Contains 4.1.1 Parsing marked *Obsolete and removed*. Even AAA conformance will not serve every disability — stated by the standard itself. |
| 2 | Accessible Rich Internet Applications (WAI-ARIA) 1.2 | `https://www.w3.org/TR/wai-aria-1.2/` | Standard | **Normative** — W3C Recommendation, published **2023-06-06** | Integrated fetch | Semantics model; roles, states, properties as normative | **Status and scope only** | Roles, characteristics, states, properties and their markup use are normative. No ARIA implementation was designed here. |

## W3C / WAI — Informative supporting material

| # | Title | URL | Type | Status | Access | Used for | Usability | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | Understanding WCAG 2.2 | `https://www.w3.org/WAI/WCAG22/Understanding/` | Supporting document | **Informative** — explicitly not part of the normative standard | Integrated fetch | Confirming informative status | Status only | Cannot create or alter a requirement. |
| 4 | Techniques for WCAG 2.2 | `https://www.w3.org/WAI/WCAG22/Techniques/` | Supporting document | **Informative** — explicitly **not required** to meet WCAG | Integrated fetch | Confirming informative status | Status only | Content may satisfy WCAG without using any documented technique. A technique is an example, never an obligation. |
| 5 | ARIA Authoring Practices Guide — Introduction | `https://www.w3.org/WAI/ARIA/apg/about/introduction/` | Guidance | **Informative** — the APG states it is an informative resource; WCAG and ARIA are the normative standards | Integrated fetch | Establishing the APG boundary | **Full** | States its objectives **do not include** providing a comprehensive design system or production-ready code; examples are for learning accessibility concepts, not production templates. |
| 6 | APG — Read Me First | `https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/` | Guidance | **Informative** | Integrated fetch | Native-semantics-first principle | **Full** | States *No ARIA is better than Bad ARIA*; ARIA can cloak native semantics; browser and AT support for ARIA 1.2 is incomplete; testing with real assistive technologies is essential before production use. |
| 7 | APG — Developing a Keyboard Interface | `https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/` | Guidance | **Informative** | Integrated fetch | Keyboard and focus policy direction | **Full** | Guidance only. Focus visibility, predictable movement aligned to reading order, DOM-order tab sequence, one tab stop per composite widget, discoverability without documentation. |
| 8 | Conformance Evaluation of Web Sites for Accessibility | `https://www.w3.org/WAI/test-evaluate/conformance/` | Guidance | **Informative** | Integrated fetch | Evaluation framing; limits of tooling | **Full** | States that the report tool does not do the checking; evaluation needs expertise across standards, design, AT, and how people with disabilities use the web; recommends involving real users with disabilities. |
| 9 | WCAG 2 Supplemental Guidance | `https://www.w3.org/WAI/WCAG2/supplemental/` | Guidance | **Informative** — explicitly **not required** for WCAG conformance | Integrated fetch | Cognitive and inclusive-design direction | **Full** | Additional ways to improve accessibility beyond WCAG. **Creates no additional conformance level.** |
| 10 | Authoring HTML: Language declarations and direction | `https://www.w3.org/International/techniques/authoring-html` | Guidance | **Informative** | Integrated fetch | Localization and internationalization policy direction | **Full** | Covers page and in-document language declaration per BCP 47, RTL direction, and bidirectional content handling. Guidance only; no implementation chosen. |

## W3C — Evaluation methodology

| # | Title | URL | Type | Status | Access | Used for | Usability | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | Website Accessibility Conformance Evaluation Methodology (WCAG-EM) 2.0 | `https://www.w3.org/TR/wcag-em-2/` | Methodology | **Non-normative — W3C Group Note *Draft*, 2026-02-05** | Integrated fetch | Determining current status before any adoption | **Status only — deliberately** | **The document states it is a draft that may be updated, replaced, or obsoleted at any time, and that it is inappropriate to cite it as other than a work in progress.** It adds nothing to and changes nothing in the normative WCAG 2 standard. **Not adopted as the CDS conformance method** (see the standard-status document). |

## ETSI — European reference

| # | Title | URL | Type | Status | Access | Used for | Usability | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | ETSI TC HF (Human Factors) — committee page | `https://www.etsi.org/technical-groups/hf/` | Publisher status listing | Publisher page | Integrated page view (**integrated fetch returned HTTP 403**) | Establishing the current EN 301 549 version status | **Full for status** | States **ETSI EN 301 549 V4.1.0 (2026-06) — "On Approval"**, that is **not final**. Related published deliverables listed separately. |

### Not opened — deliberately

| Source | Reason |
| --- | --- |
| `https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf` (EN 301 549 V3.2.1) | **Downloading standards PDFs is prohibited by this work package.** The V3.2.1 deliverable was therefore **not opened and its status not independently verified here**. Only the ETSI committee listing was used, which reports V4.1.0 as On Approval. |

---

## Coverage summary

Counts derived from the tables above and independently re-counted.

| Metric | Count |
| --- | --- |
| **Official URLs opened and registered** | **12** |
| Normative specifications | 2 |
| Informative supporting material | 8 |
| Evaluation methodology (draft) | 1 |
| Publisher status listing | 1 |
| Sources with full usable content | 8 |
| Sources used for status only | 4 |
| Access failures recorded | 1 (ETSI via fetch → HTTP 403; page view succeeded) |
| Sources deliberately not opened | 1 (EN 301 549 V3.2.1 PDF) |

### By publisher

| Publisher | URLs |
| --- | --- |
| W3C / WAI | 11 |
| ETSI | 1 |
| **Total** | **12** |

### By normative status

| Status | Count |
| --- | --- |
| Normative | 2 |
| Informative | 8 |
| Non-normative draft | 1 |
| Publisher listing | 1 |
| **Total** | **12** |

## Normative basis statement

**All normative CDS accessibility requirements derive solely from source 1, the
WCAG 2.2 Recommendation.** Sources 3–11 are informative and may inform policy
direction; they cannot create, weaken, or alter a requirement. Source 2
(WAI-ARIA 1.2) is normative for semantics where ARIA is used. Source 12
establishes a European standards-watch status only and creates no CDS obligation.

**No third-party source, blog, summary, or search snippet was used as evidence.**

## Related documents

- [Accessibility Standard Status and Limitations](ACCESSIBILITY_STANDARD_STATUS_AND_LIMITATIONS.md)
- [WCAG 2.2 AA Applicability Matrix](../governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md)
- [Accessibility and Inclusive Design Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
