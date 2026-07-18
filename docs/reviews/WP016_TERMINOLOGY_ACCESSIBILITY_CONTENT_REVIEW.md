# WP-016 Terminology, Accessibility and Content Review

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Semantic Status Foundation Independent
  Evidence Review and Candidate Gate
- **Date:** 2026-07-18
- **Evidence class:** **Independent contract review** by an Evidence Reviewer
  who is not the executor (DEC-S-121). No user research, no assistive-technology
  execution, no WCAG testing, and **no WCAG or conformance claim** — every
  artifact remains **AE-0**. **Candidate: no.**

## Terminology review

Reviewed: [Terminology DE/EN](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md),
independently re-counted against the tables.

| Check | Independent result |
| --- | --- |
| Mapping rows | **25** (5 axes × 5) |
| English labels | **25** |
| German labels | **25** |
| Missing parity rows | **0** |
| Technical IDs unchanged / language-neutral | **25 / 25** — multiset equals the token leaves exactly (`unavailable` ×2 across axes, `unknown` ×5) |
| Labels used as IDs | none — labels are display terminology only (DEC-S-110, DEC-S-119) |

Semantic-integrity spot checks (all pass):

- **`supported` not upgraded** — renders as EN "Supported" / DE "Gestützt",
  explicitly **not** „verifiziert"/„geprüft" (DEC-S-119); `verified` is
  reserved to its own value; `unverified` keeps its negation.
- **`unknown` not weakened** — all five `unknown` rows prohibit neutral-success,
  „OK", or blank rendering in both languages; must remain explicit text.
- **`none` stays scope-bound** — "None known / Keine bekannte Auswirkung"; the
  *known* qualifier is meaning-bearing and may not be shortened to "no impact".
- **`not-applicable` keeps its rationale requirement** in every locale.
- **Freshness/evidence limitations remain visible** — `stale` ≠ „aktuell",
  `expired` not merged with „veraltet", `partial` never rounded up to
  „verfügbar".
- **No meaning-bearing abbreviations**; every row carries a flexibility note;
  multi-word labels are declared intentional; no fixed length is assumed.
- **No final UI microcopy claimed** — the mapping fixes meaning parity, not
  wording, layout, or visual value.

## Accessibility and content review

Reviewed: [Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md),
the token `$description`s, and the terminology.

| Aspect | Independent assessment (as contract) |
| --- | --- |
| Text-first meaning | **Met** — every value has a textual canonical meaning, a source-set `$description`, and EN/DE meaning texts; no meaning rests on a visual channel |
| No single-channel encoding | **Met** — colour/icon/shape/position/motion may accompany but never carry alone; the validator rejects visual roles (executed `VAL-CASE-023`) |
| Unknown / limitation language | **Met** — `unknown` explicit on every axis; limitation language (`partial`, `unavailable`, `stale`, `expired`, `unverified`) required and plain |
| No unqualified healthy/success language | **Met** — "healthy/good/current/verified/all systems normal" prohibited when axes do not carry them; no aggregate/score token exists (executed `VAL-CASE-022`) |
| No normative aggregation | **Met** — summaries must carry every material qualifier and offer full five-axis disclosure; axes stay individually recoverable |
| DE/EN parity | **Met** — semantic parity now, wording later; no contradictory translation |
| Screenreader / keyboard obligations | **Met as contract / Gap as evidence** — stated as obligations on future interactive artifacts; nothing interactive exists, so no AT behaviour is (or can be) evidenced |
| Reduced-motion boundary | **Met** — motion is redundant-only; removing motion never removes meaning; no motion value defined |
| Scope / evidence boundary | **Honest** — obligations, not met criteria; comprehension and cultural suitability unvalidated (RISK-095) |

## Explicit accessibility confirmations

- **No user research** was performed or is claimed.
- **No assistive-technology execution** took place.
- **No WCAG level, certification, or conformance** is stated or implied.
- **AE-0 remains** across every artifact (DEC-S-050, Accessibility Evidence and
  Claims Model); a target is not a claim.

## Findings

25/25 terminology parity with no prohibited upgrade or weakening; the
accessibility and content contracts are internally consistent and honest. No
Blocking and no High finding. Residual limitations (self-authored contract
review, no user validation) are the same honestly-recorded boundaries the
governance already names and are visible in the dossier.

## Related documents

- [Independent Re-Execution Review](WP016_INDEPENDENT_REEXECUTION_REVIEW.md)
- [Source and Contract Traceability Review](WP016_SOURCE_CONTRACT_TRACEABILITY_REVIEW.md)
- [Candidate Gate Recommendation](WP016_CANDIDATE_GATE_RECOMMENDATION.md)
