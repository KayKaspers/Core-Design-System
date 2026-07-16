# CDS-WP-005 — Design System Architecture Notes

Internal work-package evidence for CDS-WP-005 — Design System Architecture.

- **Date:** 2026-07-16
- **Executed by:** Claude (scoped local work)
- **Final status:** Completed

## Assignment

Define the complete CDS logical architecture: system layers, authority and
source-of-truth model, artifact classes, token flow, product profiles and
extension points, existing-product reconciliation, channels and distribution,
consumer contracts, evidence and traceability, status and unknown semantics, and
the architecture boundaries to CDS-WP-006 and CDS-WP-007.

Concrete enough to steer later technical and design decisions; selecting no
technology and no visual solution.

## Preflight

| Check | Result |
| --- | --- |
| Repository root | `D:/Projects/Core-Design-System` — matches |
| Branch | `main` |
| Working tree | Clean |
| Last commit | `3c1acec docs(cds): define consumer requirements and CoreOps pilot` — contains CDS-WP-004 |
| Remote | `origin` → `https://github.com/KayKaspers/Core-Design-System.git` |
| Merge / rebase / cherry-pick | None active |
| WP status | 001, 001A, 002, 003, 004 Completed; 005 Next |
| Decisions | DEC-S-001 … DEC-S-020, exactly 20 |
| Risks | RISK-001 … RISK-019, exactly 19 |
| Consumer requirements | CR-001 … CR-040, exactly 40, contiguous |
| Requirement classification | 25 / 9 / 2 / 2 / 2 — matches expectation exactly |
| Pilot | Groups A–E (5), 9 scenarios |
| Hypotheses | HYP-001 … HYP-008, exactly 8 |
| Skills | 38 dirs, 39 files, 39/39 manifest match, commit `9dcadc12…` |

All fourteen preflight expectations matched. No fail-closed condition. All twenty
required normative documents were read before any change.

## Skills used

Nine authorized Skills. The six prohibited Skills — the five design-oriented ones
plus `ndf-implementation-review-runner` — were **not** loaded.

| Skill | Purpose | Section used |
| --- | --- | --- |
| `ndf-work-package-runner` | WP frame, guardrails, closing structure | Purpose, Allowed/Forbidden, Fail-closed |
| `ndf-architecture-blueprint-runner` | Blueprint structure: context, goals/non-goals, components, flows, deferred decisions | Expected outputs, Forbidden actions, Fail-closed, Output contract |
| `ndf-feature-scope-runner` | Scope sharpening; open questions instead of assumptions | Expected outputs, Fail-closed |
| `ndf-existing-project-analysis-runner` | Framing the reconciliation of existing consumer designs | Expected outputs, Forbidden actions |
| `ndf-accessibility-reviewer` | Accessibility as advisory constraint, never certification | Forbidden actions, Specific risk boundaries |
| `ndf-privacy-data-minimization-reviewer` | Privacy-aware readiness without compliance guarantees | Forbidden actions, Output contract |
| `ndf-validation-evidence-reviewer` | Rating evidence honestly; documenting limits | Expected outputs, Fail-closed |
| `ndf-context-pack-maintainer` | Context Pack update; references over repetition | Expected outputs, Forbidden actions |
| `ndf-compact-context-summary-runner` | Report and Compact Context Summary structure | Expected outputs, Output contract |

`ndf-architecture-blueprint-runner`'s fail-closed rule — *mark an unclear
requirement as an open question rather than assuming* — directly shaped the
deferred-decision sections. `ndf-accessibility-reviewer` shaped the decision to
keep accessibility a structural constraint rather than a threshold.

## Architecture objectives

Nine objectives, each traceable to prior evidence: unambiguous tool-independent
source of truth (DEC-S-004, RISK-004); convergence without forced merging
(RISK-005); controlled individuality (RISK-008); reconciliation rather than
overwrite (RISK-022); operations patterns without foundation capture (RISK-023);
architectural status truthfulness; offline as structure; universal traceability;
affordability for actual capacity (RISK-026).

## Layer model

Eight layers (DEC-S-021), dependencies **downward only**. Eight prohibited
dependency directions registered, the load-bearing ones being: no upward
dependency, no component-specific foundation, no channel-specific semantics, no
domain family in the universal foundation, no tool-driven authority.

Sixteen architecture invariants registered and validated.

## Authority model

Eight artifact classes (DEC-S-022) with a six-column authority matrix. Only
classes 1 and 2 are normative, and only through change control.

The central rule is DEC-S-023: **conflicts fail closed, and recency confers no
authority.** This was made explicit because recency-wins is the silent default of
nearly every tool and merge strategy — a system resolving design conflicts by
timestamp has a race condition, not an authority model.

Nine conflict scenarios registered, including the two that cannot auto-resolve:
human-readable versus machine-readable source (RISK-020), and evidence versus
normative source.

## Token flow

Five layers (DEC-S-024), strictly downward. Semantic-first: appearance-derived
names in meaning-carrying positions are defects; a component binding a reference
token directly is the most tempting and most damaging shortcut.

No format selected — the reviewed interoperability draft explicitly instructs
readers not to implement it or cite it as authoritative. Nine validation
requirements registered as capabilities, no tool chosen. RISK-021 records
honestly that the architecture constrains *direction* but not *volume*.

## Product Profile model

Five constructs: Core Foundation, Product Profile, Consumer Extension, Domain
Pattern Family, Local Exception.

Four absolute prohibitions on profiles (DEC-S-025) — no redefining shared
semantics, no weakening accessibility, no distorting status truth, no breaking
contracts. A profile needing any of them is a fork and must be named as one.

Domain Pattern Family (DEC-S-027) exists for a specific evidenced reason:
HYP-003 is a *Confirmed consumer need* whose generalizability is entirely
untested, because all three reviewed consumers are infrastructure products.

## Reconciliation

Eight-step flow (DEC-S-026). Semantic mapping is the load-bearing step: the
question is what a decision *meant*, never whether a value is right.

Registered as fact without inspecting values: SpeakCore and CastCore hold their
own style direction, palette, and token sets; their authoritative sources were
outside the permitted read areas in CDS-WP-004 and were **not read**. The
architecture knows *that* they exist, not *what they contain*.

Consumer-local retention is a **valid final outcome**, not a failure.

## Channel and distribution model

Nine channel classes; DEC-S-029 permits differing rendering but forbids differing
meaning. The non-interactive channels are the hard case — no hover, no live
update, possibly greyscale print — which makes the non-colour rule an
architectural necessity rather than a courtesy.

DEC-S-030: offline, no mandatory external runtime, reproducibility, pinning.
Registered honestly: the benchmark found no reviewed system stating an offline
guarantee, and CDS commits architecturally — a commitment, not a uniqueness claim
(DEC-S-019).

## Consumer contracts

Five contracts plus nine CDS obligations — the other half of the boundary, since
a contract stating only consumer duties is not a contract.

## Status semantics

Five separated axes (DEC-S-028) and the Unknown invariant. Placed in the
architecture rather than in convention because a convention can be forgotten under
deadline while a structural separation cannot be quietly ignored.

Rests on the strongest multi-consumer evidence CDS holds: all three consumers
document graded status; two independently require unknown ≠ healthy.

## Requirement traceability

CR-001 … CR-040 fully mapped. The matrix was **generated from the requirement
register**, so IDs cannot drift.

- Addressed by architecture **8**
- Partially addressed – later design decision required **24**
- Deferred to CDS-WP-007 **3**
- Deferred to CDS-WP-006 **1**
- Consumer-owned **2**
- Out of CDS scope **2**

Layers: L1 4 · L2 2 · L3 6 · L4 4 · L5 10 · L6 6 · L7 1 · L8 5 · n/a 2.

**Only 8 of 40 fully addressed is the expected result.** An architecture claiming
to resolve most requirements would be doing design work it is not authorized to
do. The 8 cluster in status truthfulness, offline capability, and reconciliation —
precisely where the architecture *itself* is the answer.

## New decisions

DEC-S-021 … DEC-S-032 added (12), all Accepted, dated 2026-07-16, typed as
logical architecture decisions. DEC-S-001 … DEC-S-020 unchanged — only the index
header and type table were touched. No ADR. Range now DEC-S-001 … DEC-S-032,
count 32.

## New risks

RISK-020 … RISK-028 added (9), all Monitored, qualitative only, owner roles
provisional until CDS-WP-006. Existing risks not redefined. Range now
RISK-001 … RISK-028, count 28.

RISK-026 (architecture overdesign) and RISK-028 (deferred accessibility debt) are
the two the architecture creates about itself rather than inheriting.

## Files created and changed

**Created (9):** eight architecture documents under `docs/architecture/` plus
this evidence document.

**Changed (10):** `docs/decisions/DECISION_INDEX.md` ·
`docs/risks/RISK_REGISTER.md` · `project-system/CONTEXT_PACK_FOUNDATION.md` ·
`project-system/PROJECT_PROFILE.md` · `project-system/NEXT_PHASE.md` ·
`project-system/WORK_PACKAGES.md` · `project-brain/PROJECT_BRAIN.md` ·
`README.md` · `CLAUDE.md` · `CHANGELOG.md`.

## Quantitative validation

All counts derived from artifacts by script and independently re-counted — never
asserted from working memory, per the rule established in the CDS-WP-003
correction run.

| Metric | Artifact | Value | Re-counted |
| --- | --- | --- | --- |
| Architecture layers | DESIGN_SYSTEM_ARCHITECTURE.md | 8 | Yes |
| Architecture documents | `docs/architecture/*.md` | 8 | Yes |
| Traceability entries | ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md | 40 | Yes |
| Status distribution | same | 8/24/3/1/2/2 = 40 | Yes |
| Layer distribution | same | 4/2/6/4/10/6/1/5/2 = 40 | Yes |
| Decisions | DECISION_INDEX.md | 32 | Yes |
| Risks | RISK_REGISTER.md | 28 | Yes |

The traceability generator verified that no requirement was missing from the map
and no mapped ID lacked a requirement. **No counting errors were found in this
work package** — the generate-then-count approach prevented the class of error
that occurred in CDS-WP-003 and CDS-WP-004.

## Deviations

None. Executed within the defined scope, Allowed Files, and authorized skills.

## Open architecture questions

1. **What is the normative machine-readable format?** Undecided; the reviewed
   draft is explicitly not implementable.
2. **How much may a Product Profile vary** before it fragments the system?
   Approved extension points are named as a construct but not enumerated
   (CDS-WP-006).
3. **Does the operational shape generalize**, or is CDS becoming an operations
   design system? Unanswerable from the current consumer sample (RISK-023).
4. **What is the concrete status taxonomy**, and how are combined states resolved?
5. **Where does CDS status semantics end and consumer domain semantics begin?**
   Carried from CDS-WP-002 and CDS-WP-004; still open.
6. **Is the architecture affordable?** Eight layers, eight artifact classes, five
   token levels, five axes, five contracts — none yet met an implementation
   (RISK-026).
7. **What accessibility target constrains it?** Undefined (CR-024, RISK-028).
8. Is a setup wizard a CDS pattern at all, given all three consumers built their
   own?

## Open notes

- **The architecture is unvalidated by implementation.** Its first real test is
  the bounded CoreOps pilot, whose entry criteria remain unmet.
- **CR-024 blocks more than policy:** it blocks a pilot entry criterion and
  Pilot Group E evidence. Accessibility is weak in **both** evidence layers.
  Advancing CDS-WP-007 is worth Nova's consideration; Claude does not reorder the
  roadmap.
- The risk owner model is **provisional across all 28 risks** and must be settled
  in CDS-WP-006.
- Licensing and publication finally have an assigned work package (CDS-WP-006).
- All changes are uncommitted. Commit authority rests with the Human Maintainer.

## Completion status

CDS-WP-005 is Completed against its Definition of Done and reported for Human
Maintainer review.
