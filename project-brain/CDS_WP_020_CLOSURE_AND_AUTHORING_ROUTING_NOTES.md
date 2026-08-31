# CDS-WP-020 — Closure and Authoring Routing — Notes

**Executor-produced working notes. Not normative, not evidence, and not a review.**
They require an independent review by a reviewer who is not their executor before
any closure claim is treated as settled.

- **Pass:** CDS-WP-020 Closure and `FR-N-03` Routing — a bounded closure and
  roadmap-routing pass, **not** a new work package and **not** a hygiene work
  package
- **Date:** 2026-08-27
- **Executor:** Claude (scoped executor)
- **Baseline:** `main` at `42a568d823de3388e45af62967546f13ad67eff6`, working tree
  clean, index clean, `origin/main` identical, ahead/behind `0 / 0`, 0 tags, no
  merge, rebase, cherry-pick, or revert in progress
- **Reviewed CDS-WP-020 object reproduced:** manifest SHA-256
  `831eff8c5f981d7c7c250d87f0a0ded773480216fda722ddace013ea087da0ee`, **3501**
  bytes, **22** paths — reproduced exactly against the working tree
- **Result:** **COMPLETE WITH NOTES**
- **Git writes:** **none**

## What this pass did

1. Recorded **CDS-WP-020** as **`Completed`** in the current-state carriers, with
   closure **proposed in this working object** and effective only at the
   Human-Maintainer integration commit of that object.
2. Recorded **`FR-N-03`** as **RESOLVED BY EXPLICIT AUTHORING-WP DESTINATION**, and
   registered that destination as **`CDS-WP-020A` — Visual Token Source Authoring
   and Source Set Realization**, `Planned`, not active, not authorized.
3. Made the **AUTHOR is not VALIDATE** responsibility boundary explicit as a
   standing gate in the forward roadmap.
4. Recorded three findings — **`F-020C-01`**, **`F-020C-02`**, **`F-020C-03`** — and
   routed all but one without repair.

## `FR-N-03` — the adjudication and how it was implemented

Nova adjudicated `FR-N-03` with Human-Maintainer approval and selected **Option 2**:

> **SOURCE / VALUE AUTHORING is not VALIDATION.** The concrete machine-readable
> Visual Token Source and Value Authoring work must receive its own explicit
> work-package destination, and must not be silently absorbed into **CDS-WP-024**.

**`FR-N-03` existed nowhere in the tracked repository before this pass.** A
repository-wide search for `FR-N-` returned zero hits. The identifier appears here
only because this routing was written, and — exactly as the CDS-WP-017 routing note
already says of its own identifiers — **an identifier in a routing table is not the
finding.** Only `FR-N-03` was supplied; `FR-N-01`, `FR-N-02`, and any other findings
from that review are separately governed, their text was not provided, and this pass
**neither reconstructs nor disposes of them.**

### Why no existing planned work package was the right destination

Every planned work package was checked against the authoring responsibility. **None
matched.**

| Candidate | Established purpose | Verdict |
| --- | --- | --- |
| CDS-WP-021 | Adaptive Layout and Responsive Foundation | Responsive strategy, not source authoring |
| CDS-WP-022 | Theme and Environmental Presentation Model | The theme mechanism; CDS-WP-020 deliberately kept it free |
| CDS-WP-023 | Semantic Status Visual Binding Contract | Binds status to visual roles; needs authored roles, does not create them |
| CDS-WP-024 | Semantic Validation and Render-Gate Architecture | **Validation and the render gate** — the very absorption `FR-N-03` forbids |
| CDS-WP-025 | Semantic Validation Negative-Fixture Expansion | Negative-fixture coverage; validation-side |
| CDS-WP-026 … CDS-WP-053 | Components, evidence, profiles, experience, multimodal, brand, distribution, Stable | None is a Layer-3 visual token **source authoring** work package |

The gap is real and pre-existing: **Phase V holds architecture (CDS-WP-019),
contract (CDS-WP-020), responsive (CDS-WP-021) and theme (CDS-WP-022) — and no work
package that actually authors the machine-readable visual token sources.**
`F-020-07` already anticipated *"a future implementation work package"* without
naming one.

### Why the identifier is `CDS-WP-020A`

The identifier was **derived from the repository, not invented**.

- **Preference 1 — reuse an existing planned work package: rejected.** No planned
  work package's authoritative purpose matches authoring, as the table above shows.
- **Preference 2 — an existing repository-supported insert mechanism: applied.**
  **`CDS-WP-001A`** already exists in the controlled register: a suffixed identifier
  inserted between two numbered work packages, carried in the roadmap table with its
  own `Depends on` entry and its own description block, and mirrored in every
  current-state carrier. `CDS-WP-020A` applies that same mechanism. **It is a
  precedent rather than a written rule**, which is recorded here openly and flagged
  for Nova.
- **Renumbering: not done.** No existing planned work package was renumbered, and
  the numeric sequence CDS-WP-017 … CDS-WP-053 is **unchanged**. A suffix occupies
  no number, so no gap and no duplicate was created.
- **Why `020` and not `022` or `024`.** The authoring work realizes exactly the
  contract CDS-WP-020 defined — RP-1 … RP-10, SR-1 … SR-12, AL-1 … AL-8,
  VP-1 … VP-7. It **is** the value and machine-readable half that CDS-WP-020
  returned as `DECISION_REQUIRED`. Binding it to `020` states that coupling; binding
  it to `022` would have decided **OD-7**, and binding it to `024` would have been
  the absorption `FR-N-03` forbids.
- **Why not `CDS-WP-054`.** Appending after **CDS-WP-053 — Stable Gate and
  Distribution Readiness** would place a foundational authoring work package after
  the Stable gate, which is semantically false.

**The authority to register it is explicit.** [Next Phase](../project-system/NEXT_PHASE.md)
lists among the still-prohibited actions *"creating a new work-package ID beyond the
recorded CDS-WP-017 … CDS-WP-053 planning sequence **without Human-Maintainer
approval**"*, and [Work Packages](../project-system/WORK_PACKAGES.md) permits
controlled roadmap extension through *"Nova planning and Human Maintainer
approval"*. Both conditions are met by the Human-Maintainer-approved Nova
adjudication of `FR-N-03`. **The gate is satisfied, not bypassed.**

**Its table position is registration, not sequencing.** Listing `CDS-WP-020A` before
CDS-WP-021 does not decide that it runs first. **OD-7 is open**, and this pass
neither accepts nor rejects its recommendation that CDS-WP-022 be considered before
any value-selection work package.

## The AUTHOR is not VALIDATE invariant

**AUTHOR is not VALIDATE. SOURCE CREATION is not CONFORMANCE DETERMINATION.**

| Responsibility | Owner | Never acquires |
| --- | --- | --- |
| Visual source sets, machine-readable source authoring at token-flow layers 1 and 2, source-set identity and revision, provenance, family × layer topology, and — once gated — identifier realization and concrete normative values | **`CDS-WP-020A`** | Validator implementation, validation authority, conformance determination, evidence admission, maturity promotion, Product Profile activation, pilot activation, release authority, `Stable` declaration, runtime renderer implementation, unrelated schema/tool/test expansion |
| Semantic validation, the render gate, negative-fixture coverage | **CDS-WP-024** · **CDS-WP-025** | Source authoring, value selection, identifier creation, source-set identity, or any power to originate the sources it validates |

**The invariant is derived, not created.** It applies decisions already in force —
**DEC-S-022** (authority by artifact class), **DEC-S-031** and **DEC-S-079**
(generated artifacts are never normative and never stand against their source),
**DEC-S-053** (an automated check is never sufficient), and **DEC-S-126** (evidence
admission and maturity promotion are Human-Maintainer acts). The roadmap's existing
*generated-output authority boundary* already states the same rule from the other
side: **a renderer is not a governance authority.** By the same reasoning, **a
validator is not a source.**

## Decision and ADR determination

**No `DEC-S-132` was created, and none is required.**

The governing precedent is **CDS-WP-017**, which registered **CDS-WP-018 …
CDS-WP-053** as `Planned` — thirty-six work packages, twelve arcs, twelve
milestones, the standing gates, and the **CDS-WP-024 validation boundary itself** —
and **added no ADR and no Decision.** **CDS-WP-018** likewise added none. Registering
one further planned work package and stating its responsibility boundary is the same
class of act.

The Decision Index states that decisions *"define purpose, boundaries, scope, and
authority"* and that they *"do not select tools, formats, frameworks, repository
structures"*. Roadmap routing is neither. Nothing new is decided here: the
authoring/validation boundary is an application of DEC-S-022, DEC-S-031, DEC-S-053,
DEC-S-079, and DEC-S-126, and the roadmap is explicitly **non-normative**.

**Creating a decision merely to advance the count would be ceremony that produces no
decision — which RISK-040 exists to prevent.**

**No `ADR-0005` was created, and none is required.** An ADR records an
**architecture** decision. This pass records **no** architecture: no layer, no
representation, no identity model, no format, and no structural change. CDS-WP-017
performed far more roadmap structuring and added none. The
`ndf-adr-governance-review` skill is also explicit that **accepting, superseding, or
finalizing an ADR stays with the Human Maintainer**, and that autonomously marking an
ADR `Accepted` is forbidden.

**No risk was added, accepted, closed, or re-scored.** The register stays at **98**;
`RISK-099` remains not required.

## Findings

Local finding IDs, prefixed `F-020C-` for the CDS-WP-020 **c**losure pass, matching
the repository's existing `F-<wp>-<n>` convention.

| ID | Class | Observation | Disposition |
| --- | --- | --- | --- |
| **`F-020C-01`** | **STALE CURRENT-STATE CARRIER** | **74** live assertions across **21** files (measured at baseline `42a568d8…`) still qualify **DEC-S-128 … DEC-S-131** and **ADR-0004** as `PROPOSED / AUTHORIZED FOR INTEGRATION` and **NOT YET EFFECTIVE** *"until the Human-Maintainer exact-byte integration commit"*, and state the effective registers as **DEC-S-127** and **ADR-0003**. That commit has occurred — `42a568d823de3388e45af62967546f13ad67eff6` — so the stated condition is met. Carriers include the **normative** Decision Index *Register scope* section and the ADR-0004 status line. | **Routed → a separately authorized effectivity reconciliation pass.** **Not repaired here.** Three reasons: the volume is a material scope expansion beyond a bounded closure and routing pass; **marking an ADR `Accepted` is a Human-Maintainer act** the executor may not perform; and the repository already has the pattern — the **CDS-WP-016 Post-Promotion Current-State Reconciliation** was its own separately authorized pass after the Promotion Commit, with closure following it. **This pass asserts no effectivity state and changed no effectivity wording anywhere.** The decision and ADR **counts** — **131** and **4** — are already correct in the register; only the qualification is stale. |
| **`F-020C-02`** | **NO CHANGE REQUIRED — routed** | **M2 — Visual Foundation Ready** is *"reached after CDS-WP-022"*. Registering `CDS-WP-020A` in Phase V leaves it unstated whether M2 should also depend on it. | **Routed → Nova and Human-Maintainer disposition once OD-4 … OD-7 are decided.** **M2 is unchanged.** Re-deriving it now would decide sequencing while **OD-7 is open**. |
| **`F-020C-03`** | **STALE CURRENT-STATE CARRIER — repaired** | The *Completed work packages* list in [Project Profile](../project-system/PROJECT_PROFILE.md) ended at **CDS-WP-018** and omitted **CDS-WP-019**, although the same file already recorded CDS-WP-019 as `Completed` and closed by `538fbccbf6f554de3b872e9fb75a70d13318feb6`. | **Repaired**, because the same line had to be edited to add CDS-WP-020 and leaving the gap would have produced a new false list. **CDS-WP-019 and CDS-WP-020 were both added.** This is the same recurrence `R1-F-01` and `F-019-09` describe. |

**Recording a finding repairs nothing and authorizes nothing.**

## Historical records deliberately not rewritten

| Artifact class | Treatment |
| --- | --- |
| The **dated current-state paragraphs** in the forward roadmap (`CDS-WP-018 (2026-08-25)`, `CDS-WP-019 (2026-08-26)`, `CDS-WP-020 (2026-08-26)`) | **HISTORICAL RECORD — not rewritten.** A new dated paragraph was appended, exactly as each earlier pass did. Only one false-live clause was qualified as *"as at that date"*. |
| [CDS-WP-020 Reference and Semantic Token Foundation Notes](CDS_WP_020_REFERENCE_AND_SEMANTIC_TOKEN_FOUNDATION_NOTES.md) | **POINT-IN-TIME EVIDENCE — body untouched.** An **additive supersession note** was added at the head; no statement in the body was altered. |
| The `F-020-01` finding disposition | **DECISION-TIME TEXT — additively superseded.** Its original text stands, marked *"stated as at 2026-08-27, before integration"*, with the supersession appended. |
| The earlier CDS-WP-020 changelog entry | **HISTORICAL RECORD.** Its recorded facts are unaltered; only the opening was prefixed *"previously recorded"* so the two entries are not read as competing current state. |
| `docs/reviews/**`, `docs/foundations/**`, `docs/risks/**`, evidence, admission, and approval artifacts | **UNTOUCHED.** No evidence-bound or review-bound artifact was modified. |
| `tokens/**`, `schemas/**`, `tools/**`, `tests/**`, `artifacts/**`, `requirements-validator.lock`, `.claude/**` | **UNTOUCHED.** |
| `docs/decisions/**` | **UNTOUCHED.** No Decision Index entry, no ADR, and no effectivity qualification was changed — see `F-020C-01`. |

**Historical truth remains historical truth.** Nothing was rewritten merely because
its old current state is no longer current.

## What this pass explicitly did not do

- **No successor work package was activated.** `CDS-WP-020A`, CDS-WP-021,
  CDS-WP-022, CDS-WP-024, and every entry through CDS-WP-053 are **`Planned`, not
  active, not authorized**. **Routing is not activation; planning is not
  authorization; a dependency is not authority.**
- **No visual value, identifier, token source file, manifest, resolver, schema,
  validator rule, diagnostic, test, fixture, component, channel adapter, brand,
  identity, or Product Profile** was created. Visual values **0**, visual source
  sets **0**, visual Candidate families **0**, VF-1 … VF-9 **`Proposed`**.
- **No Decision, ADR, or risk** was added, accepted, closed, or re-scored — the
  registers stay at **131**, **4**, and **98**.
- **No evidence** was produced or admitted; **no maturity** changed. Candidate stays
  **YES** for the channel-independent Semantic Status Layer-3 source/contract family
  only; **`Stable: No`**; every other artifact stays **AE-0**;
  **`AE1-CDS-WP016-SEMSTATUS-004`** was transferred to nothing.
- **No claim, no conformance, no capability registration, no phase rename.** The
  phase stays **Post-Candidate Foundation & Design-System Enablement** (DEC-S-127).
- **No Product Profile, pilot, consumer activation, release, tag, or publication
  change.** Publication stays **`Private Development`**; tags stay **0**.
- **No Semantic Status source, revision, maturity, approval, or evidence package**
  was touched.
- **No Git write of any kind.** No `add`, `commit`, `push`, `tag`, `reset`,
  `restore`, `checkout`, `stash`, `merge`, `rebase`, `cherry-pick`, `revert`,
  `clean`, or `switch`; nothing was staged.
- **No network access**, and no dependency was installed.

## Effective versus proposed

**Editing a file changes no repository history.** The closure recorded here is
**proposed in the working object**. It becomes **effective** only after:

1. an independent review by a reviewer who is not the executor,
2. Nova adjudication of that review,
3. the **Human-Maintainer exact-byte integration commit** of this object.

**A review PASS is not a commit, and a Nova recommendation is not an approval.**

## Skills used in this pass

`ndf-work-package-runner` (execution frame and guardrails),
`ndf-adr-governance-review` (ADR-need determination and the binding rule that
accepting an ADR stays with the Human Maintainer), `ndf-changelog-writer` (changelog
entry shape and the no-invented-release-status rule), `ndf-feedback-triage-runner`
(finding classification), `ndf-context-pack-maintainer`,
`ndf-compact-context-summary-runner`. Reported openly per the Skills-first operating
mode. **A Skill grants no authority and extended no scope.**

## Related documents

- [Work Packages](../project-system/WORK_PACKAGES.md) — the controlled register; `CDS-WP-020A` scope and exclusions
- [Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md) — `FR-N-03`, `F-020C-01`, `F-020C-02`, the authoring and validation separation gate
- [CDS-WP-020 Reference and Semantic Token Foundation Notes](CDS_WP_020_REFERENCE_AND_SEMANTIC_TOKEN_FOUNDATION_NOTES.md) — the execution record this pass closes
- [Visual Token Foundation Open Decisions](../docs/roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md) — **OD-1 … OD-7**, non-normative
- [Visual Token Value Selection Rules](../docs/governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md) — **VP-1 … VP-7**
- [Next Phase](../project-system/NEXT_PHASE.md)
- [Project Brain](PROJECT_BRAIN.md)
