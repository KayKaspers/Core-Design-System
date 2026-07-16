# CDS-WP-004 — Consumer Requirements and CoreOps Pilot Notes

Internal work-package evidence for CDS-WP-004 — Consumer Requirements and
CoreOps Pilot Contract.

- **Date:** 2026-07-15
- **Executed by:** Claude (scoped local work; read-only consumer analysis)
- **Final status:** Completed

## Assignment

Capture requirements from committed CoreOps content, evaluate supplementary
evidence from SpeakCore and CastCore, separate shared from product-specific
requirements, respect permanent non-goals, assess consumer need for
HYP-001 … HYP-008, define a bounded CoreOps pilot with scenarios and a contract,
and deliver architecture inputs for CDS-WP-005.

No visual design, components, tokens, product code, technology selection, or
public conformance claim.

## CDS preflight

| Check | Result |
| --- | --- |
| Repository root | `D:/Projects/Core-Design-System` — matches |
| Branch | `main` |
| Working tree | Clean |
| Last commit | `05ec59d docs(cds): complete benchmark and differentiation research` — contains CDS-WP-003 |
| Remote | `origin` → `https://github.com/KayKaspers/Core-Design-System.git` |
| Merge / rebase / cherry-pick | None active |
| WP status at start | 001, 001A, 002, 003 Completed; 004 Next |
| Decisions at start | DEC-S-001 … DEC-S-012, exactly 12 |
| Risks at start | RISK-001 … RISK-013, exactly 13 |
| Hypotheses at start | HYP-001 … HYP-008, exactly 8 |
| Research metrics | 31 benchmark + 2 standards = 33 opened, 27 usable; 140 matrix cells (68 / 37 / 35) — **all verified against the artifacts** |
| Skills | 38 dirs, 39 files, 39/39 manifest match, commit `9dcadc12…` confirmed |

All twelve preflight expectations matched. No fail-closed condition. All sixteen
required normative documents were read before any change.

## Skills used

Nine authorized Skills. The five prohibited design-oriented Skills were **not**
loaded.

| Skill | Purpose | Section used |
| --- | --- | --- |
| `ndf-work-package-runner` | WP frame, guardrails, closing structure | Purpose, Allowed/Forbidden, Fail-closed |
| `ndf-existing-project-analysis-runner` | Structure for neutral read-only analysis of existing repos | Expected outputs, Forbidden actions, Fail-closed |
| `ndf-product-discovery-runner` | Audience, problem, value framing for requirements | Expected outputs, Ethical-use boundaries |
| `ndf-feature-scope-runner` | Scope sharpening; open questions instead of assumptions | Expected outputs, Fail-closed |
| `ndf-ux-flow-reviewer` | Scenario framing — entry, states, errors, help, barriers | Expected outputs, Ethical-use boundaries |
| `ndf-accessibility-reviewer` | Accessibility findings as advisory, never certification | Forbidden actions, Specific risk boundaries |
| `ndf-validation-evidence-reviewer` | Classify evidence sources, rate strength honestly, document limits | Expected outputs, Fail-closed, Output contract |
| `ndf-context-pack-maintainer` | Context Pack update; references over repetition | Expected outputs, Forbidden actions |
| `ndf-compact-context-summary-runner` | Report and Compact Context Summary structure | Expected outputs, Output contract |

`ndf-validation-evidence-reviewer` directly shaped the evidence-level model:
rate honestly as limited rather than overstate. `ndf-accessibility-reviewer`
directly shaped CR-024 and HYP-007 — advisory, never a conformance claim.

## Consumer repository preflights

All three verified. **All treated as strictly read-only. Nothing was written,
created, or modified in any consumer repository.**

| Consumer | Path | Remote | Branch | HEAD | Tree | Status |
| --- | --- | --- | --- | --- | --- | --- |
| CoreOps | `D:\Projects\CoreOps` | KayKaspers/CoreOps ✓ | `main` | `399de21c2d76cf84279badfcde58dacbb9eec1a2` | **Dirty — 2 entries** | Verified |
| SpeakCore | `D:\Projects\SpeakCore` | KayKaspers/SpeakCore ✓ | `main` | `a5e697715c1c7077bc6c53400b3e6411730720ba` | Clean | Verified |
| CastCore | `D:\Projects\CastCore` | kaykaspers/castcore ✓ | `main` | `6c7614e3192a11479ae1c7431195daa042d38250` | **Dirty — 1 untracked** | Verified |

No merge, rebase, or cherry-pick active anywhere.

**CoreOps dirty tree — significant.** Its two uncommitted entries
(`project-system/LESSONS_LEARNED_REGISTER.md` modified, and an untracked
governance milestone review) sit **inside the areas this work package may read**.
Under DEC-S-013 neither was used. All CoreOps content was read via
`git show HEAD:<path>`, never from the working tree. Had local files been read
naively, uncommitted content would have entered the evidence base.

**CastCore dirty tree:** one untracked nested directory, not read, not used.

## Analysed commits and files read

15 evidence sources across three repositories, all bound to HEAD. Full detail in
the [Consumer Evidence Register](../docs/research/CONSUMER_EVIDENCE_REGISTER.md).

- **CoreOps (6 read, 5 usable):** `README.md` (empty at HEAD → not usable),
  `docs/architecture/PROJECT_BRIEF.md`, `docs/architecture/COREOPS_CONCEPT_V3.md`,
  `docs/architecture/DEGRADED_MODE_AND_CAPABILITY_RESTRICTION_MODEL.md`,
  `docs/architecture/RESTRICTED_ISOLATED_AND_AIR_GAPPED_OPERATION_MODEL.md`,
  `docs/governance/COREOPS_LANGUAGE_STANDARD.md`.
- **SpeakCore (3 read, 3 usable):** `docs/branding/ui-principles.md`,
  `project-brain/BRANDING.md`, `docs/README.md`.
- **CastCore (6 read, 6 usable):** `README.md`, `docs/ARCHITECTURE.md`,
  `docs/de/getting-started/first-setup.md`, `docs/de/user-guide/monitoring.md`,
  `docs/de/developer-guide/documentation-rules.md`, `docs/ROADMAP.md`.

No secrets, environment files, logs, databases, user data, build output, or
product source outside the permitted documentation areas were read.

## Evidence figures

| Metric | Value |
| --- | --- |
| Repositories analyzed | 3 |
| Evidence sources read | 15 |
| Usable as requirement evidence | 14 |
| Not usable | 1 (CoreOps `README.md`, empty at HEAD) |
| Evidence level reached | **Level 1 — documentation only** |

Strength distribution: Explicit committed requirement 6 · Documented implemented
behavior 5 · Documented planned capability 2 · Context only 1 · Not usable 1
(total 15).

## Requirement figures

Derived from the register and independently re-counted by script.

| Metric | Value |
| --- | --- |
| Range | CR-001 … CR-040 |
| Total | 40 |
| Traceability entries | 40 |

**By classification:** Shared CDS Candidate 25 · Deferred Requirement 9 ·
CoreOps Pilot Requirement 2 · Product-local Requirement 2 · Out of CDS Scope 2.

**By evidence status:** Repeated across consumers 21 · Confirmed by committed
evidence 9 · Deferred – insufficient evidence 6 · Inferred – Human validation
required 2 · Rejected as CDS requirement 2.

**By pilot priority:** Must 16 · Should 11 · Could 1 · Not in pilot 12.
Pilot-relevant 28.

**By consumer (overlapping, does not sum to 40):** CoreOps 33 · CastCore 25 ·
SpeakCore 19 · no consumer evidence 1.

## Pilot groups and scenarios

Five groups, nine scenarios — every group has at least one.

| Group | Focus | Scenarios |
| --- | --- | --- |
| A | Application Foundation | 2 |
| B | Operations Overview | 2 |
| C | Inventory and Dense Data | 1 |
| D | State and Safety Patterns | 2 |
| E | Help, Accessibility, Localization | 2 |

Scenarios describe **what must be expressible and safe**, never a UI solution.

## Hypothesis validation

Consumer layer added; CDS-WP-003 research assessments **unchanged**.

Confirmed consumer need: HYP-002 offline/self-hosted, HYP-003 operations
patterns, HYP-005 governed family flexibility. Human validation required:
HYP-007. Partially supported: HYP-001, HYP-004, HYP-006, HYP-008.

The sharpest result: **HYP-003 was "Not verifiable" in the research layer and is
"Confirmed consumer need" in the consumer layer.** CDS should build it because
consumers demonstrably need it — while knowing nothing about whether it
differentiates CDS at all (DEC-S-019).

## New decisions

DEC-S-013 … DEC-S-020 added, all Accepted, dated 2026-07-15, typed as consumer
and pilot scope decisions. DEC-S-001 … DEC-S-012 unchanged — only the index
header and type table were touched. No ADR. Range now DEC-S-001 … DEC-S-020,
count 20.

## New risks

RISK-014 … RISK-019 added, all Monitored, qualitative only, owner roles
provisional until CDS-WP-006. Existing risks not redefined; RISK-013 gained one
cross-reference to DEC-S-019 without changing meaning. Range now
RISK-001 … RISK-019, count 19.

## Files created and changed

**Created (7):** `docs/governance/CONSUMER_REQUIREMENTS_MODEL.md` ·
`docs/governance/CONSUMER_REQUIREMENTS_TRACEABILITY.md` ·
`docs/governance/COREOPS_PILOT_SCOPE_AND_SCENARIOS.md` ·
`docs/governance/COREOPS_PILOT_CONTRACT.md` ·
`docs/governance/CONSUMER_VALIDATION_PLAN.md` ·
`docs/research/CONSUMER_EVIDENCE_REGISTER.md` ·
`docs/research/CONSUMER_HYPOTHESIS_VALIDATION.md` · plus this evidence document.

**Changed (8):** `docs/decisions/DECISION_INDEX.md` (DEC-S-013…020) ·
`docs/risks/RISK_REGISTER.md` (RISK-014…019) ·
`project-system/CONTEXT_PACK_FOUNDATION.md` ·
`project-system/PROJECT_PROFILE.md` · `project-system/NEXT_PHASE.md` ·
`project-system/WORK_PACKAGES.md` · `project-brain/PROJECT_BRAIN.md` ·
`README.md` · `CLAUDE.md` · `CHANGELOG.md`.

## Quantitative validation

Counts were derived from the artifacts by script and independently re-counted —
never asserted from working memory, per the lesson recorded in the CDS-WP-003
correction run.

**The independent count caught three errors in my own first draft** before any
downstream document consumed them:

| Figure | Asserted | Actual | Fixed |
| --- | --- | --- | --- |
| Evidence status: Repeated across consumers | 20 | **21** | Yes |
| Evidence status: Confirmed by committed evidence | 10 | **9** | Yes |
| Requirements citing CoreOps / SpeakCore / CastCore | 32 / 17 / 20 | **33 / 19 / 25** | Yes |
| Evidence strength: Explicit committed requirement | 5 | **6** | Yes |

The fourth error was caught by the final recount: the evidence-strength column
summed to 14 against a stated total of 15. Actual distribution is 6 / 5 / 2 / 1 / 1.

Classification (25/2/2/9/2) and pilot priority (16/11/1/12) were correct on the
first pass. All totals resolve to 40 (requirements) and 15 (evidence sources).
The traceability matrix was **generated from the register** rather than written
by hand, so requirement IDs cannot drift between the two documents.

## Validations performed

All 45 required checks were executed. Summary: only Allowed Files changed in
CDS; **no consumer repository modified** (re-verified after the work); full diff
reviewed; `git diff --check` clean; internal links resolve; CoreOps verified as
primary evidence; SpeakCore and CastCore verified; only committed evidence used;
no secrets, logs, databases, or product sources read; CR IDs unique, contiguous
CR-001…CR-040, each with source, classification, priority, ownership, and
validation method; sums derived and re-counted; every requirement traced and no
orphan traces; Pilot Groups A–E complete with ≥1 scenario each; entry, exit,
evidence, and out-of-scope complete; HYP-001…008 exactly eight with research
assessments unchanged and a consumer assessment each; none presented as an
accepted decision; DEC-S-013…020 added, total 20, DEC-S-001…012 unchanged, no
ADR; RISK-014…019 added, total 19; no visual, technology, or token decision; no
implementation; no adoption or conformance claim; Context Pack still
non-normative; skills 39/39 unchanged; only the nine authorized skills used; WP
status consistent; no Git write action.

## Deviations

None. The work package was executed within the defined scope, Allowed Files,
authorized skills, and authorized consumer repositories.

## Open Human-validation questions

1. **What accessibility level does CDS commit to, and how is it evidenced?**
   (CR-024) CoreOps names a baseline with no level; CastCore documentation has no
   accessibility evidence at all. This blocks Group E evidence. → CDS-WP-007
2. **How much product individuality is permitted?** SpeakCore and CastCore
   already shipped their own style direction, palette, and tokens. CDS is
   reconciling, not starting fresh. (CR-001, CR-002, CR-037) → CDS-WP-005
3. **Are CR-003 and CR-014 generalizable** beyond CoreOps? Both single-consumer
   today. → DEC-S-016 review
4. **Does the operational shape generalize?** All three consumers are
   infrastructure products — the sample cannot distinguish "operational products
   need this" from "all products need this". (RISK-016, RISK-019)
5. **Do consumers need the deferred channels** — PDF, diagrams, presentations?
   CR-028 and CR-029 are weak; CR-030 has no evidence at all.
6. **Is documentation evidence sufficient**, or is real validation required
   before Must requirements are accepted? (RISK-017)
7. **Should AirCore and further projects be reviewed** before foundations
   freeze? Not authorized here. → Nova decision

## Open notes

- **Evidence is Level 1 only.** No interviews, observation, usability testing, or
  accessibility testing took place, and none is claimed.
- **Accessibility is the weakest area in both layers** — thin in the benchmark,
  thin in the consumers, and CDS treats it as first-class. Uncomfortable and
  worth Nova's attention.
- Concrete palette, typography, and stack values appear in consumer
  documentation. They were recorded only as *the existence of product-local
  decisions*; **no value was carried into CDS** (DEC-S-020, RISK-016).
- SpeakCore's and CastCore's authoritative design tokens and brand assets live
  under `branding/` paths **outside** the permitted read areas and were not read.
- CoreOps `README.md` is empty at HEAD — the usual entry-point evidence is
  absent.
- Licensing and publication still carry no assigned work package. → Nova
  decision; Claude does not extend the roadmap.
- All CDS changes are uncommitted. Commit authority rests with the Human
  Maintainer.

## Completion status

CDS-WP-004 is Completed against its Definition of Done and reported for Human
Maintainer review.
