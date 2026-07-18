# Semantic Status Localization Parity Review

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-015 — Semantic Status Foundation Source Set and
  Candidate Evidence
- **Date:** 2026-07-18
- **Evidence class:** **Executor-produced parity review** of the
  [DE/EN Terminology Mapping](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md).
  Independent review: **pending**. No comprehension, usability, or cultural
  validation took place (RISK-095).

## Checks over all 25 mapping rows

| # | Check | Result |
| --- | --- | --- |
| 1 | **ID parity** — every row carries the unchanged language-neutral technical ID; no label is used as an ID | **25/25 pass** |
| 2 | **Meaning parity** — DE and EN meaning texts state the same normative content as the canonical vocabulary meaning | **25/25 pass** (executor assessment) |
| 3 | **No confidence upgrade** — `supported` renders as „Gestützt", explicitly not „verifiziert"/„geprüft"; `verified` reserved; `unverified` keeps its negation | **Pass** |
| 4 | **No unknown weakening** — all five `unknown` rows prohibit neutral-success or blank renderings in both languages | **Pass** |
| 5 | **No freshness/evidence obscuring** — `stale`≠„aktuell", `expired`≠„veraltet"-merge, `partial` never rounds up to „verfügbar", `not-applicable` keeps its rationale requirement in every locale | **Pass** |
| 6 | **DE entries** | **25/25** |
| 7 | **EN entries** | **25/25** |
| 8 | **Missing entries** | **0** |

## Counting basis

Independent re-count against the mapping document: 5 tables × 5 data rows =
25 rows; each row contains both label columns and both meaning columns; the
five `unknown` rows appear exactly once per axis. Counts agree with the
mapping document's own closing counts.

## Limitations and review state

The parity assessment of meaning (check 2) is a judgment by the same executor
who authored both sides — exactly the self-confirmation risk the governance
names (RISK-078, RISK-095). A complete mapping is **not** validated
comprehension. **Independent review: pending** (DEC-S-121); terminology
approval rests with the Human Maintainer. No Candidate effect.
