# Semantic Status Terminology DE/EN

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-015 — Semantic Status Foundation Source Set and
  Candidate Evidence
- **Date:** 2026-07-18
- **Status:** **Normative terminology mapping** for the 25 status values,
  pending Human-Maintainer commit. Experimental; no Candidate status.
  **Labels are display terminology, never technical identifiers** (DEC-S-110,
  DEC-S-119); technical IDs stay language-neutral and unchanged. This document
  fixes meaning parity — **no final UI microcopy, no layout rule, no visual
  value**. All labels tolerate localization-driven length variation; no
  meaning-bearing abbreviation is permitted. Review state of every entry:
  **executor-drafted, independent review pending**.

## Reading the tables

Per entry: value technical ID · canonical EN label · canonical DE label ·
short EN meaning · short DE meaning · prohibited translation shortening
(what a localization must never do) · flexibility note. The axis technical ID
heads each table. Review State for all 25 entries: *executor-drafted,
independent review pending* (stated once here, valid per row).

## Axis `condition` — Operational Condition

| Value ID | EN label | DE label | EN meaning | DE meaning | Prohibited shortening | Flexibility |
| --- | --- | --- | --- | --- | --- | --- |
| `nominal` | Nominal | Normalbetrieb | Operates within declared normal parameters | Arbeitet innerhalb der deklarierten Normalparameter | Never render as "healthy/verified/current" — condition only | Longer DE compound acceptable; no abbreviation |
| `degraded` | Degraded | Beeinträchtigt | Operates with reduced capability or quality | Arbeitet mit verminderter Leistung oder Qualität | Never soften into a nominal-like state or merge with `disrupted` | Label may wrap; keep distinct from „gestört" |
| `disrupted` | Disrupted | Gestört | One or more declared functions do not operate | Eine oder mehrere deklarierte Funktionen arbeiten nicht | Never equate with total unavailability | Keep distinct from „nicht verfügbar" |
| `unavailable` | Unavailable | Nicht verfügbar | The declared function is not provided | Die deklarierte Funktion wird nicht erbracht | Never soften into „eingeschränkt" (degraded-like) | Two-word DE label intended; no abbreviation |
| `unknown` | Unknown | Unbekannt | The condition cannot currently be stated | Der Zustand kann derzeit nicht angegeben werden | **Never** render as neutral success, „OK" or empty display | Must remain explicit text, never blank |

## Axis `severity` — Severity and Impact

| Value ID | EN label | DE label | EN meaning | DE meaning | Prohibited shortening | Flexibility |
| --- | --- | --- | --- | --- | --- | --- |
| `none` | None known | Keine bekannte Auswirkung | No known impact in the declared scope | Keine bekannte Auswirkung im deklarierten Scope | Never shorten to "no impact"/„keine Auswirkung" — the *known* qualifier is meaning-bearing | The longer DE/EN forms are intentional |
| `minor` | Minor | Gering | Impact does not materially impair the purpose | Auswirkung beeinträchtigt den Zweck nicht wesentlich | Never render as „keine" | Single word acceptable |
| `major` | Major | Erheblich | Impact materially impairs the purpose | Auswirkung beeinträchtigt den Zweck wesentlich | Never soften toward „gering" | Single word acceptable |
| `critical` | Critical | Kritisch | Impact endangers the declared purpose | Auswirkung gefährdet den deklarierten Zweck | Never inflate routinely (meaning erosion) or soften | Single word acceptable |
| `unknown` | Unknown | Unbekannt | The impact cannot currently be assessed | Die Auswirkung kann derzeit nicht bewertet werden | **Never** render as `none`/„keine" | Explicit text, never blank |

## Axis `confidence` — Knowledge Confidence

| Value ID | EN label | DE label | EN meaning | DE meaning | Prohibited shortening | Flexibility |
| --- | --- | --- | --- | --- | --- | --- |
| `verified` | Verified | Verifiziert | Backed by identified, current verification evidence | Durch identifizierte, aktuelle Verifikationsevidenz gestützt | Reserved strictly for this value — no other value may borrow it | Loanword „verifiziert" intended, not „geprüft" generally |
| `supported` | Supported | Gestützt | Backed by relevant but not verifying evidence | Durch relevante, aber nicht verifizierende Evidenz gestützt | **Never upgrade in DE to „verifiziert" or „geprüft"** (DEC-S-119) | „Gestützt" is deliberate; no upgrade synonym |
| `uncertain` | Uncertain | Unsicher | Indications are incomplete or partially conflicting | Hinweise sind unvollständig oder teilweise widersprüchlich | Never hide the uncertainty in summaries | Single word acceptable |
| `unverified` | Unverified | Nicht verifiziert | Not verified; no usable verification exists | Nicht verifiziert; keine verwertbare Verifikation vorhanden | **Never** render as „verifiziert"; never drop the negation | Negated two-word DE form intended |
| `unknown` | Unknown | Unbekannt | The confidence itself cannot be stated | Die Verlässlichkeit selbst kann nicht angegeben werden | Never treated as any positive confidence | Explicit text, never blank |

## Axis `freshness` — Freshness

| Value ID | EN label | DE label | EN meaning | DE meaning | Prohibited shortening | Flexibility |
| --- | --- | --- | --- | --- | --- | --- |
| `current` | Current | Aktuell | Recent enough, with a documented observation time | Aktuell genug, mit dokumentiertem Beobachtungszeitpunkt | Never claim without a resolvable time | Single word acceptable |
| `aging` | Aging | Alternd | Beyond ideal currency, not yet stale | Über der idealen Aktualität, noch nicht veraltet | Never collapse into „aktuell" | Distinct middle band must stay visible |
| `stale` | Stale | Veraltet | Too old to support current decisions | Zu alt, um aktuelle Entscheidungen zu tragen | **Never** render as „aktuell" (invariant 4) | Single word acceptable |
| `expired` | Expired | Abgelaufen | Past a declared hard validity limit | Über eine deklarierte harte Gültigkeitsgrenze hinaus | Never merge with „veraltet" — the hard limit is meaning-bearing | Keep distinct from `stale` |
| `unknown` | Unknown | Unbekannt | The observation time cannot be stated | Der Beobachtungszeitpunkt kann nicht angegeben werden | Never treated as current; undated is not fresh | Explicit text, never blank |

## Axis `evidence` — Evidence Availability

| Value ID | EN label | DE label | EN meaning | DE meaning | Prohibited shortening | Flexibility |
| --- | --- | --- | --- | --- | --- | --- |
| `available` | Available | Verfügbar | Evidence is accessible via a resolvable identity | Evidenz ist über eine auflösbare Identität zugänglich | Never imply correctness or sufficiency („belegt korrekt") | Single word acceptable |
| `partial` | Partial | Teilweise verfügbar | Some relevant evidence is accessible, some is not | Ein Teil der relevanten Evidenz ist zugänglich, ein Teil nicht | Never round up to „verfügbar"; the gap stays visible | Two-word DE label intended |
| `unavailable` | Unavailable | Nicht verfügbar | No evidence is currently accessible | Derzeit ist keine Evidenz zugänglich | Never imply the statement is false — only unbacked | Negated form intended |
| `not-applicable` | Not applicable | Nicht anwendbar | Evidence is not meaningfully applicable — rationale required | Evidenz ist nicht sinnvoll anwendbar — Begründung erforderlich | **Never drop the rationale requirement in any locale** | Localized label must keep the rationale reachable |
| `unknown` | Unknown | Unbekannt | Whether evidence exists cannot be stated | Ob Evidenz existiert, kann nicht angegeben werden | Never render as „verfügbar" or as `not-applicable` | Explicit text, never blank |

## Counts

- **Entries: 25/25** · **English labels: 25** · **German labels: 25** ·
  **Missing parity rows: 0**
- **Independent re-count:** table data rows above: 5 + 5 + 5 + 5 + 5 = **25**;
  every row carries both an EN and a DE label and both meaning columns; the
  five `unknown` rows appear exactly once per axis. A future mismatch between
  these counts and the tables is a defect and fails closed.
