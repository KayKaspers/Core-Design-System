# Semantic Status Accessibility and Content Review

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-015 — Semantic Status Foundation Source Set and
  Candidate Evidence
- **Date:** 2026-07-18
- **Evidence class:** **Executor-produced contract review** of the committed
  status contracts, the source set, and the terminology mapping. It involved
  **no user research, no assistive-technology execution, and no WCAG testing,
  and makes no WCAG or conformance claim** — every artifact remains **AE-0**.
  Independent review: **pending**.

## Result vocabulary

`Met (as contract)` — the reviewed artifacts satisfy the obligation *on
paper*; nothing is evidenced against real usage. `Gap` — an obligation is not
yet covered by any artifact.

## Findings

| # | Aspect | Assessment | Basis |
| --- | --- | --- | --- |
| 1 | **Text-first meaning** | Met (as contract) | Every one of the 25 values carries a canonical textual meaning (vocabulary), a `$description` in the source set, and EN/DE meaning texts; no meaning depends on a visual channel |
| 2 | **Unknown and limitation language** | Met (as contract) | `unknown` is an explicit token on every axis; terminology prohibits neutral-success renderings and blank displays; `none` is "None known / Keine bekannte Auswirkung", preserving the known-qualifier |
| 3 | **No visual-only meaning** | Met (as contract) | The source set contains zero visual roles; the validator rejects appearance segments (VAL-CASE-023 executed); DEC-S-111 enforced machine-side |
| 4 | **No health-score language** | Met (as contract) | No aggregate token exists; the validator rejects aggregate roles (VAL-CASE-022 executed); terminology contains no score/badge wording |
| 5 | **DE/EN understandability** | Met (as contract) | 25/25 parity rows with plain-language meanings in both languages; no meaning-bearing abbreviation; deliberate longer forms where meaning requires them |
| 6 | **Flexible labels** | Met (as contract) | Every terminology row carries a flexibility note; multi-word labels are declared intentional; no fixed-length assumption is introduced |
| 7 | **Screenreader/keyboard boundary** | Met (as contract) / **Gap (evidence)** | The obligations exist in the Communication Contract and remain binding on future interactive artifacts; nothing interactive exists, so no AT behavior was or could be evidenced |
| 8 | **Reduced-motion boundary** | Met (as contract) | No motion value exists; motion remains a redundant-only future modality per the Communication Contract |
| 9 | **Evidence limitations** | Honestly recorded | This is a contract review by the artifact author; comprehension, usability, and cultural suitability are unvalidated (RISK-095); AE-0 everywhere |

## Boundaries

This review evidences **stated contract properties**, not that any status
communication works for real people (RISK-017 applied). It is
executor-produced (the reviewer authored the reviewed artifacts — RISK-078)
and must be independently re-assessed before the Candidate gate (DEC-S-121).
No WCAG level, certification, or conformance statement is made or implied.
