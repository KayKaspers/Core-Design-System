# Accessibility Baseline Source Register

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy
- **Date:** 2026-07-16
- **Status:** **Research evidence — NON-normative.** A dated snapshot of official
  sources opened for the baseline. Sources decay (RISK-012, RISK-044); re-verify
  before relying on any entry. Records **no** accessibility evidence and **no**
  support claim.

## Method

Only official standards/vendor/product pages were opened, via the integrated web
view. No third-party comparison sites, blogs, forums, market-share pages, or
search snippets were used as evidence. No software was downloaded and no tests
were run. Every opened URL is registered below, including those that failed to
load.

## Registered sources

| # | Publisher | Product / standard | Title | URL | Type | Current status / version noted | Access date | Used for | Usable | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S-01 | W3C / WAI | Web accessibility evaluation | Selecting Web Accessibility Evaluation Tools | https://www.w3.org/WAI/test-evaluate/tools/selecting/ | Standard guidance | "tools can not **determine** accessibility, they can only **assist**"; human judgement required | 2026-07-16 | AE-1 / automated-not-sufficient rationale (DEC-S-053) | Yes | — |
| S-02 | Microsoft | Microsoft Edge | Microsoft Edge release schedule | https://learn.microsoft.com/en-us/deployedge/microsoft-edge-release-schedule | Release/lifecycle | Stable major cadence moving to **2 weeks** from v152; **Extended Stable 8 weeks**; trigger = equivalent Chromium release; stable ≈ v150–151 (Jul 2026) | 2026-07-16 | Chromium browser family cadence; version policy | Yes | Approximate dates per page note |
| S-03 | Microsoft | Windows 11 | Windows 11 Home and Pro — Microsoft Lifecycle | https://learn.microsoft.com/en-us/lifecycle/products/windows-11-home-and-pro | Lifecycle | Modern Lifecycle; in support: **24H2** (to 2026-10-13), **25H2** (to 2027-10-12), **26H1** (to 2028-03-14); 23H2 ended 2025-11-11 | 2026-07-16 | Tier-1 desktop OS family and version window | Yes | — |
| S-04 | NV Access | NVDA | About NVDA | https://www.nvaccess.org/about-nvda/ | Product | **Free, open source**; 64-bit **Windows 10 / Windows 11** and Windows Server 2016+; in-built add-on store; portable option | 2026-07-16 | Tier-1 no-cost desktop screen reader | Yes | — |
| S-05 | Apple | VoiceOver | VoiceOver User Guide for Mac | https://support.apple.com/guide/voiceover/welcome/mac | Product | VoiceOver is the screen reader **built into macOS**; also iOS/iPadOS | 2026-07-16 | Tier-2 (Safari+VoiceOver) and Tier-3 (iOS) | Yes | — |
| S-06 | Mozilla / Firefox | Firefox ESR | Firefox for Enterprise | https://www.firefox.com/en-US/browsers/enterprise/ | Product | ESR: **annual major releases**, regular **security updates** between; rapid release every **4 weeks** | 2026-07-16 | Tier-1 second engine (Gecko); version policy | Yes | Reached via redirect from mozilla.org (S-10) |
| S-07 | Mozilla (MDN) | prefers-reduced-motion | prefers-reduced-motion — CSS media feature | https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion | Product docs | Detects OS "Reduce motion" (macOS/iOS), "Show animations" (Windows), "Remove animations" (Android) | 2026-07-16 | Tier-1 reduced-motion category | Yes | — |
| S-08 | Mozilla (MDN) | forced-colors | forced-colors — CSS media feature | https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors | Product docs | Detects forced-colors mode, tied to **Windows High Contrast / Contrast Themes** | 2026-07-16 | Tier-1 forced-colors / high-contrast category | Yes | — |
| S-09 | Google | Chrome | Chrome browser release channels | https://support.google.com/chrome/a/answer/9027636 | Release/lifecycle | Stable major every **4 weeks**; **Extended Stable every 8 weeks**; Stable fully tested | 2026-07-16 | Chromium browser family corroboration | Yes | — |
| S-10 | Mozilla | Firefox | Firefox for organizations (redirect) | https://www.mozilla.org/en-US/firefox/organizations/ | Product | 301 redirect to firefox.com enterprise (S-06) | 2026-07-16 | ESR (followed to S-06) | Redirect | Cross-host 301; followed to S-06 |
| S-11 | Mozilla | Firefox ESR | Switch to Firefox ESR (support KB) | https://support.mozilla.org/en-US/kb/switch-to-firefox-extended-support-release-esr | Product docs | Page returned a load-error placeholder; no content | 2026-07-16 | ESR (superseded by S-06) | **No** | Not usable; content did not load |
| S-12 | Freedom Scientific | JAWS | JAWS product (support) | https://support.freedomscientific.com/products/blindness/jaws | Product | Not retrieved | 2026-07-16 | JAWS Tier-2 requirements | **No** | **HTTP 403** via web view |
| S-13 | Freedom Scientific | JAWS | JAWS software product page | https://www.freedomscientific.com/products/software/jaws/ | Product | Not retrieved | 2026-07-16 | JAWS Tier-2 requirements | **No** | **HTTP 403** via web view |

## Coverage summary

- **URLs opened:** 13. **Usable:** 9. **Not usable / redirect:** 4 (S-10 redirect,
  S-11 load error, S-12/S-13 HTTP 403).
- **By publisher:** W3C/WAI 1 · Microsoft 2 · Mozilla (incl. MDN) 5 · NV Access 1 ·
  Apple 1 · Google 1 · Freedom Scientific 2.

## Limitations

- **JAWS system requirements were not retrievable** via the authorized web view
  (S-12, S-13 both HTTP 403). JAWS therefore appears **only** as a Tier-2
  conditional environment and **must not** become a Required or claimed pairing
  until its official current system requirements are verified.
- The Firefox ESR support KB (S-11) did not load; the ESR facts are taken from the
  official Firefox enterprise page (S-06) instead.
- Version and lifecycle facts are **dated snapshots** as of 2026-07-16 and drift as
  vendors release (RISK-044, RISK-012). No market-share or popularity data was
  collected or used (RISK-011). An official product page proves a product exists —
  **not** that CDS has been tested against it (every artifact remains AE-0).

## Related documents

- [Accessibility Baseline Selection Rationale](ACCESSIBILITY_BASELINE_SELECTION_RATIONALE.md)
- [Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Environment and Scope Matrix](../governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
