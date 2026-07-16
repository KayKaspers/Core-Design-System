# Consumer Evidence Register

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract
- **Evidence date:** 2026-07-15
- **Status:** Research and validation evidence — **not normative**

## Purpose

This register lists every consumer repository source actually read during
CDS-WP-004, bound to a committed revision, so that each requirement in the
[Consumer Requirements Model](../governance/CONSUMER_REQUIREMENTS_MODEL.md) is
traceable to real committed content.

## Rules applied

- All consumer repositories were treated as **strictly read-only**. Nothing was
  written, created, or modified in any consumer repository.
- Evidence is bound to the **committed HEAD revision** (DEC-S-013). Uncommitted
  consumer content was never used as evidence.
- Only committed content from the permitted areas was read: `README.md`,
  `CLAUDE.md`, `CHANGELOG.md`, `project-system/**`, `project-brain/**`,
  `docs/**`.
- No secrets, environment files, certificates, keys, databases, logs, backups,
  user data, build output, dependencies, binaries, or images were read. No
  product source code outside the permitted documentation areas was read.
- Read-only Git only (`ls-tree`, `grep`, `show HEAD:<path>`). No network
  commands, no clone, no fetch.
- Only sources actually read are registered.

## Evidence strength vocabulary

`Explicit committed requirement` · `Repeated committed requirement` ·
`Documented implemented behavior` · `Documented planned capability` ·
`Inferred requirement requiring Human Maintainer validation` · `Context only` ·
`Not usable as requirement evidence`

## Evidence classes

`Primary Pilot Evidence` (CoreOps) · `Secondary Consumer Evidence` (SpeakCore,
CastCore) · `Context Only` · `Not Used`

---

## 1. CoreOps — Primary Pilot Evidence

| Property | Value |
| --- | --- |
| Project role | Primary pilot consumer (DEC-S-002) |
| Repository | KayKaspers/CoreOps |
| Local path | `D:\Projects\CoreOps` |
| Remote | `https://github.com/KayKaspers/CoreOps.git` — matches expected |
| Branch | `main` |
| HEAD commit | `399de21c2d76cf84279badfcde58dacbb9eec1a2` |
| Working tree | **Dirty — 2 uncommitted entries** |
| Merge / rebase / cherry-pick | None active |
| Verification status | **Verified** |

### Working-tree note

The CoreOps working tree carries two uncommitted entries at evidence time:

- modified: `project-system/LESSONS_LEARNED_REGISTER.md`
- untracked: `docs/governance/FOUNDATION_MILESTONE_REVIEW_CO_WP_021_026.md`

Both sit inside areas this work package is permitted to read. **Neither was used
as evidence.** All CoreOps content was read strictly from HEAD via
`git show HEAD:<path>`, never from the working tree (DEC-S-013). The dirty status
is recorded here rather than silently ignored.

### Sources read

| # | File | Section / focus | Evidence summary | Method | Strength |
| --- | --- | --- | --- | --- | --- |
| 1 | `README.md` | whole file | Empty at HEAD. No content. | `show HEAD:` | Not usable as requirement evidence |
| 2 | `docs/architecture/PROJECT_BRIEF.md` | Problem statement, vision, principles, accepted product requirements | Self-hosted, offline and air-gap capable operations control plane; no cloud requirement for core functions; DE/EN from foundation with German as possible default; read-only before write, preview before execute, plan before deployment, backup before dangerous change, verification after change; fail closed; auditability; missing data must not count as healthy. | `show HEAD:` | Explicit committed requirement |
| 3 | `docs/architecture/COREOPS_CONCEPT_V3.md` | Experience Plane, UI expectations, accepted product requirements table | Central dashboard, configurable widgets, global search; Simple and Expert Mode; clear risk tiers; clear capability display; understandable previews; no misleading success indication; accessibility baseline named without a conformance level; light/dark mode; DE/EN; responsive; reduced emergency interface (recovery mode); UI must not use privileged internal shortcuts unavailable to API consumers. | `show HEAD:` + `grep` | Explicit committed requirement |
| 4 | `docs/architecture/DEGRADED_MODE_AND_CAPABILITY_RESTRICTION_MODEL.md` | Section headings, non-goals, open questions | Operational modes, capability restriction matrix, read-only mode, restricted and guarded mode, degraded mode, containment, emergency stop, **Unknown Operational State**, failure and unknown state. Explicitly documentary; no implemented modes claimed. | `show HEAD:` | Documented planned capability |
| 5 | `docs/architecture/RESTRICTED_ISOLATED_AND_AIR_GAPPED_OPERATION_MODEL.md` | Section headings | Connectivity classes, offline identity, policy freshness, time and clock uncertainty, restricted operation, degraded modes, import boundary, evidence return, reconciliation, failure and unknown state. | `show HEAD:` | Documented planned capability |
| 6 | `docs/governance/COREOPS_LANGUAGE_STANDARD.md` | Artifact classes, canonical language, DE/EN product scope, translation status, semantic parity | English canonical for machine-facing artifacts; German and English as product-facing languages; translation parity claimable only when actually reviewed; translation-status metadata; semantic parity; explicit non-goal of UI localization in that work package. | `show HEAD:` | Explicit committed requirement |

**CoreOps sources read: 6 · usable: 5 · not usable: 1**

### Limitations

- Accessibility appears in only **one** substantive CoreOps document, as a named
  "accessibility baseline" with **no stated conformance level and no evidence
  method**. This is thin.
- The frontend technology names appearing in the concept document are **CoreOps
  product statements**, not CDS decisions, and are not treated as such here.
- CoreOps documentation is architecture- and governance-heavy. There is no
  dedicated UI, interaction, or design-system document to read.
- `README.md` is empty at HEAD, so the usual entry-point evidence is absent.

---

## 2. SpeakCore — Secondary Consumer Evidence

| Property | Value |
| --- | --- |
| Project role | Secondary consumer (DEC-S-018) |
| Repository | KayKaspers/SpeakCore |
| Local path | `D:\Projects\SpeakCore` |
| Remote | `https://github.com/KayKaspers/SpeakCore.git` — matches expected |
| Branch | `main` |
| HEAD commit | `a5e697715c1c7077bc6c53400b3e6411730720ba` |
| Working tree | **Clean** |
| Merge / rebase / cherry-pick | None active |
| Verification status | **Verified** |

### Sources read

| # | File | Section / focus | Evidence summary | Method | Strength |
| --- | --- | --- | --- | --- | --- |
| 7 | `docs/branding/ui-principles.md` | Principles | Trust before effect; calm surfaces, clear hierarchy, restrained animation; **status colours only semantic, always with text or icon**; Simple versus Expert mode with risk options hidden in Simple; safety made visible, destructive actions require deliberate confirmation; panel and card layout; **sufficient contrast, visible focus states, no colour-only coding**; consistency through design tokens rather than one-off values. | `show HEAD:` | Explicit committed requirement |
| 8 | `project-brain/BRANDING.md` | Style direction, brand values, palette | A product-local corporate design with its own stated style direction, brand-value-to-visual mapping, and an explicitly preliminary token-based palette. Documents that authoritative tokens live in a product-local token directory. | `show HEAD:` | Explicit committed requirement |
| 9 | `docs/README.md` | Preflight advisor reference | A preflight and capacity advisor evaluates the environment automatically using a traffic-light system. | `grep` | Context only |

**SpeakCore sources read: 3 · usable: 3**

### Limitations

- SpeakCore's authoritative design tokens live under a `branding/` path that is
  **outside the permitted read areas** for this work package. They were **not**
  read. Evidence about tokens is limited to what the permitted documents state
  *about* them.
- Concrete palette values appear in the permitted documents. They are recorded
  here only as *the existence of a product-local palette*. **No values are
  carried into CDS** — doing so would be an unauthorized visual decision and
  product-local contamination (RISK-016).
- The documents are product-local design decisions, not requirements addressed
  to CDS. Reading them as CDS requirements would be an inference.

---

## 3. CastCore — Secondary Consumer Evidence

| Property | Value |
| --- | --- |
| Project role | Secondary consumer (DEC-S-018) |
| Repository | KayKaspers/CastCore |
| Local path | `D:\Projects\CastCore` |
| Remote | `https://github.com/kaykaspers/castcore.git` — matches expected repository (host-normalized casing) |
| Branch | `main` |
| HEAD commit | `6c7614e3192a11479ae1c7431195daa042d38250` |
| Working tree | **Dirty — 1 untracked entry** |
| Merge / rebase / cherry-pick | None active |
| Verification status | **Verified** |

### Working-tree note

One untracked directory (`Nova-Development-Framework/`) is present — an
unrelated nested copy. It was **not read and not used**. All CastCore content
was read from HEAD.

### Sources read

| # | File | Section / focus | Evidence summary | Method | Strength |
| --- | --- | --- | --- | --- | --- |
| 10 | `README.md` | Positioning, status | Self-hosted streaming operations suite; explicitly early beta and not production-hardened; states that it explains failures in plain language and offers fallbacks; role-based access (three roles). | `show HEAD:` | Documented implemented behavior |
| 11 | `docs/ARCHITECTURE.md` | UI section | A mandatory page set including login, setup wizard, dashboard and further pages; required UX explicitly lists a DE/EN switcher, status badges, health score, live logs, **command preview**, **expert mode**, form validation, help texts, warnings, test buttons, secret masking, and **plain-language errors alongside technical logs**. | `show HEAD:` + `grep` | Documented implemented behavior |
| 12 | `docs/de/getting-started/first-setup.md` | Setup wizard | Setup wizard with language choice (DE/EN), then a **system check** verifying dependencies, write permissions and free space, with the result shown as a traffic light. | `grep` | Documented implemented behavior |
| 13 | `docs/de/user-guide/monitoring.md` | Stream health panel | Health score per job with traffic-light status distinguishing healthy, warning, critical **and a separate unknown state for "not running"**; clicking opens a diagnosis assistant rather than only showing a red score. | `grep` | Documented implemented behavior |
| 14 | `docs/de/developer-guide/documentation-rules.md` | DE/EN synchronisation | Every German page must have an English counterpart; a documentation status file and check script verify structure, DE/EN synchronicity, empty pages, and stale review entries; enforced in CI. | `grep` | Explicit committed requirement |
| 15 | `docs/ROADMAP.md` | Delivered items | DE/EN i18n foundation (frontend resource files, backend error codes); setup wizard with language, deployment detection, dependency check, directories and storage; role model. Definition-of-done includes translated UI texts and updated DE and EN user documentation. | `grep` | Documented implemented behavior |

**CastCore sources read: 6 · usable: 6**

### Limitations

- **Accessibility does not appear at all** in the reviewed CastCore
  documentation. No accessibility, WCAG, or keyboard evidence was found in the
  permitted areas.
- CastCore's logo and brand assets live under a `branding/` path outside the
  permitted read areas and were **not** read.
- Evidence is largely *implemented behavior* rather than *stated requirement*.
  Behavior is good evidence that a need is real, but it describes what CastCore
  built for itself, not what it asks of CDS.
- The concrete UI stack and accent colours named in the architecture document
  are CastCore product decisions and are **not** treated as CDS input.

---

## 4. Not analyzed

| Project | Reason |
| --- | --- |
| AirCore | Not authorized for analysis in CDS-WP-004. Registered as an open validation question. |
| SC-OrgaBase, OrgaCore, and further projects | Not authorized for analysis in CDS-WP-004. |

No substitute source was used for any missing or unauthorized consumer.

---

## Coverage summary

Counts derived from the tables above and independently re-counted.

| Metric | Count |
| --- | --- |
| Consumer repositories verified | 3 |
| Repositories with clean working tree | 1 (SpeakCore) |
| Repositories with dirty working tree, read from HEAD only | 2 (CoreOps, CastCore) |
| **Evidence sources read** | **15** |
| Usable as requirement evidence | 14 |
| Not usable as requirement evidence | 1 |

### Per repository

| Repository | Class | Sources read | Usable |
| --- | --- | --- | --- |
| CoreOps | Primary Pilot Evidence | 6 | 5 |
| SpeakCore | Secondary Consumer Evidence | 3 | 3 |
| CastCore | Secondary Consumer Evidence | 6 | 6 |
| **Total** | — | **15** | **14** |

### Evidence strength distribution

| Strength | Count |
| --- | --- |
| Explicit committed requirement | 6 |
| Documented implemented behavior | 5 |
| Documented planned capability | 2 |
| Context only | 1 |
| Not usable as requirement evidence | 1 |
| Repeated committed requirement | 0 |
| Inferred requirement requiring Human Maintainer validation | 0 |
| **Total** | **15** |

Usable evidence (all strengths except `Not usable as requirement evidence`):
**14**. The six `Explicit committed requirement` sources are CoreOps 3
(project brief, concept, language standard), SpeakCore 2 (UI principles,
branding), CastCore 1 (documentation rules).

`Repeated committed requirement` is zero at source level by design: repetition
is a property of a *requirement across consumers*, not of a single file, and is
recorded in the
[Consumer Requirements Model](../governance/CONSUMER_REQUIREMENTS_MODEL.md)
instead. `Inferred requirement requiring Human Maintainer validation` is
likewise a requirement-level judgement and is recorded there.

## Committed-revision binding

Confirmed. Every source above is bound to the HEAD commit stated for its
repository:

- CoreOps `399de21c2d76cf84279badfcde58dacbb9eec1a2`
- SpeakCore `a5e697715c1c7077bc6c53400b3e6411730720ba`
- CastCore `6c7614e3192a11479ae1c7431195daa042d38250`

No uncommitted content was used. No content was reconstructed from memory or
from earlier sessions (DEC-S-013).

## Related documents

- [Consumer Requirements Model](../governance/CONSUMER_REQUIREMENTS_MODEL.md)
- [Consumer Requirements Traceability](../governance/CONSUMER_REQUIREMENTS_TRACEABILITY.md)
- [Consumer Hypothesis Validation](CONSUMER_HYPOTHESIS_VALIDATION.md)
- [CoreOps Pilot Contract](../governance/COREOPS_PILOT_CONTRACT.md)
