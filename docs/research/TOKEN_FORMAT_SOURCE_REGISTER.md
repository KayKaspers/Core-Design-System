# Token Format Source Register

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-011 — Machine-Readable Source and Token Format Decision
- **Date:** 2026-07-16
- **Status:** **Research evidence — NON-normative.** A dated snapshot of the
  official sources opened for the format decision. Sources decay (RISK-012,
  RISK-055); re-verify before relying on any entry. Records **no** design value and
  **no** implementation.

## Method

Only official standards/specification sources were opened, via the integrated web
view. No third-party comparison sites, blogs, forums, or search snippets were used
as evidence; no software or file was downloaded; no tool was installed. Every opened
URL is registered below. **Stable and preview sources are separated explicitly.**

## Stable DTCG 2025.10 sources (candidate normative basis)

| # | Publisher | Title | URL | Type | Status / version | Access date | Used for | Usable | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S-01 | W3C Design Tokens CG | Design Tokens specification reaches first stable version | https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/ | Announcement | **Stable** 2025.10, published 2025-10-28; **CG report, not a W3C Standard** | 2026-07-16 | DTCG status / DEC-S-073 | Yes | — |
| S-02 | Design Tokens CG | Design Tokens 2025.10 (index) | https://www.designtokens.org/TR/2025.10/ | Technical report | **Final Community Group Report**, "considered stable", "intended for implementation"; not a W3C Standard | 2026-07-16 | External format basis | Yes | — |
| S-03 | Design Tokens CG | Format Module 2025.10 | https://www.designtokens.org/TR/2025.10/format/ | Technical report | Stable 2025.10 | 2026-07-16 | JSON format, `$value`/`$type`/`$description`/`$extensions`, groups, `{group.token}` alias, `$`-reserved | Yes | — |
| S-04 | Design Tokens CG | Color Module 2025.10 | https://www.designtokens.org/TR/2025.10/color/ | Technical report | Stable 2025.10 | 2026-07-16 | color token type: `colorSpace` + `components`, `alpha`, `hex` fallback; 14 color spaces | Yes | — |
| S-05 | Design Tokens CG | Resolver Module 2025.10 | https://www.designtokens.org/TR/2025.10/resolver/ | Technical report | Stable 2025.10 | 2026-07-16 | sets + modifiers, ordered resolution, multi-context (light/dark) | Yes | — |
| S-06 | Design Tokens CG | Technical Reports (index) | https://www.designtokens.org/technical-reports/ | Index | Lists 4 reports; **2025.10 Stable** vs 3 drafts + 1 experimental preview | 2026-07-16 | Stable/preview separation | Yes | — |
| S-07 | W3C Design Tokens CG | Design Tokens Community Group | https://www.w3.org/community/design-tokens/ | Group page | Produces **Community Group Reports, not W3C Standards** | 2026-07-16 | Standards-status boundary | Yes | — |

## Preview / draft sources (status only — NEVER normative)

| # | Publisher | Title | URL | Type | Status | Access date | Used for | Usable | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S-08 | Design Tokens CG | Preview drafts (index) | https://www.designtokens.org/TR/drafts/ | Draft | **Preview draft** — states "Do not refer to this document directly, and do not implement anything in this document"; not authoritative | 2026-07-16 | Preview boundary, future-change / drift risk (RISK-055, RISK-056) | Status only | **Must not be normative or implemented** |

## Supplementary official standards

| # | Publisher | Title | URL | Type | Status | Access date | Used for | Usable | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S-09 | IETF / RFC Editor | RFC 8259 — JSON | https://www.rfc-editor.org/info/rfc8259 | RFC | **Internet Standard, STD 90** | 2026-07-16 | Strict JSON canonical syntax (DEC-S-075) | Yes | — |
| S-10 | IETF / RFC Editor | RFC 6901 — JSON Pointer | https://www.rfc-editor.org/info/rfc6901 | RFC | **Standards Track** (Proposed Standard) | 2026-07-16 | Path/pointer identity option | Yes | — |
| S-11 | RFC Editor (Independent) | RFC 8785 — JSON Canonicalization Scheme (JCS) | https://www.rfc-editor.org/info/rfc8785 | RFC | **Informational — NOT Standards Track** (independent stream) | 2026-07-16 | Possible future canonicalization basis (evaluated, not selected) | Yes | Not a standard; deterministic-serialization decision deferred |
| S-12 | JSON Schema | JSON Schema draft 2020-12 | https://json-schema.org/draft/2020-12 | Specification | Current draft; split into Core + Validation; published June 2022 | 2026-07-16 | Profile-schema foundation (DEC-S-077) | Yes | A "draft" family, not an ISO/IETF standard |
| S-13 | JSON Schema | JSON Schema specification (index) | https://json-schema.org/specification | Index | Confirms **2020-12** is the current version (prev 2019-09) | 2026-07-16 | Schema-version confirmation | Yes | Release notes work-in-progress |

## Coverage summary

- **URLs opened: 13. Usable: 13.** Stable DTCG **7** · Preview/draft **1** (status
  only) · RFC **3** · JSON Schema **2**.
- **Stable vs preview:** the stable 2025.10 reports (S-02…S-05) and the preview
  drafts (S-08) are the same publisher but **different status**; only the stable
  reports are a candidate normative basis (DEC-S-073, DEC-S-074).

## Limitations

- DTCG 2025.10 is a **Community Group Report, not a W3C Standard**, and not on the
  W3C Recommendation Track (S-01, S-02, S-07). It is stable and implementation-ready
  but carries no formal standards-body guarantee; CDS remains responsible for its
  own profile.
- Version/status facts are **dated snapshots** (2026-07-16) and drift as the CG
  publishes (RISK-055). No third-party or popularity data was used.
- **RFC 8785 is Informational**, not a standard; its adoption is a deferred
  implementation-phase decision (DEC-S-080; canonicalization decision state = open).

## Related documents

- [Token Format Evaluation](TOKEN_FORMAT_EVALUATION.md)
- [ADR-0001 — Machine-Readable Token Source Format](../decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
- [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md)
