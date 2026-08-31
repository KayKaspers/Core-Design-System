# CDS-WP-020 — Reference and Semantic Token Foundation — Notes

**Executor-produced working notes. Not normative, not evidence, and not a
review.** They require an independent review by a reviewer who is not their
executor before any closure claim is made.

> **Additive supersession note (2026-08-27).** These notes are a **dated
> point-in-time record of the CDS-WP-020 execution** and are **not rewritten**.
> Where the body states that CDS-WP-020 is *not closed*, that was true when the
> notes were written. The reviewed CDS-WP-020 object has since been **integrated**
> by the Human-Maintainer commit `42a568d823de3388e45af62967546f13ad67eff6`, and a
> separately authorized **closure and routing pass** records the work package as
> **`Completed`** — closure effective only at that pass's Human-Maintainer
> integration commit. The value and machine-readable half is routed by **`FR-N-03`**
> to **`CDS-WP-020A`**, which is `Planned`, not active, and not authorized. See
> [CDS-WP-020 Closure and Authoring Routing — Notes](CDS_WP_020_CLOSURE_AND_AUTHORING_ROUTING_NOTES.md).
> **`DECISION_REQUIRED` remains the executed result of the work package**, and
> **OD-4 … OD-7 remain open.**

- **Work package:** CDS-WP-020
- **Date:** 2026-08-26
- **Executor:** Claude (scoped executor)
- **Baseline:** `main` at `e956560be2b5650cc1ce717931f3da39a2414a1b`, working tree
  clean, index clean, `origin/main` identical, ahead/behind `0 / 0`, 0 tags, no
  merge/rebase/cherry-pick in progress
- **Result:** **DECISION_REQUIRED** — the contract half of the work package is
  delivered; the value and machine-readable half is gated on **seven** normative
  choices that no committed CDS source has made and that this work package holds
  no authority to make.
- **Skills used:** `ndf-work-package-runner` (execution frame, guardrails, closing
  structure), `ndf-architecture-blueprint-runner` (blueprint shape: context,
  boundaries, obligations, open questions), `ndf-ui-style-system-runner`
  (structuring visual-foundation guidance neutrally, options over mandates),
  `ndf-accessibility-reviewer` (advisory accessibility framing with no
  certification claim), `ndf-adr-governance-review` (ADR-need assessment and next
  number derived from context, not invented), `ndf-docs-polish-runner`,
  `ndf-changelog-writer`, `ndf-context-pack-maintainer`,
  `ndf-compact-context-summary-runner`. Reported openly per the Skills-first
  operating mode. **No Skill granted authority, extended scope, or overrode the
  prompt or the normative sources.**

## Objective

Establish the first concrete Reference and Semantic visual token layer on top of
the architecture CDS-WP-019 completed — without producing a finished Core brand,
a Product Profile, a consumer brand, a component library, a complete theme
implementation, a pilot, consumer adoption, channel evidence, conformance
evidence, or Stable maturity.

## Baseline verification

Every element of the expected baseline was verified read-only before any file was
touched, and every element matched:

| Check | Expected | Observed |
| --- | --- | --- |
| Repository root | `D:\Projects\Core-Design-System` | matched |
| Branch | `main` | matched |
| HEAD | `e956560be2b5650cc1ce717931f3da39a2414a1b` | matched |
| `origin/main` | same commit | matched |
| Ahead / behind | `0 / 0` | matched |
| Working tree · index | clean · clean | matched |
| Tags | 0 | matched |
| Active merge / rebase / cherry-pick | none | none |

The negative-state sentinels were verified against the registers, not from memory:
**DEC-S-127** highest and **127** entries; **RISK-098** highest and **98**
entries; **ADR-0001 … ADR-0003** (3 files); Semantic Status at
`semantic-status-rev-0002-candidate`, `Candidate` / `Approved`.

**"No visual value exists in CDS" was verified by search, not assumed.** The
tracked repository contains no hexadecimal colour literal, no `colorSpace` or
`components` member, and no `px`, `rem`, `em`, or `pt` dimension literal in any
token source or schema. The only `$type` values present in a normative token
source are 25 occurrences of `string` in `semantic/status`; the synthetic
fixtures additionally carry `number` and one deliberately invalid preview type.

### The work-package-state divergence, and why it is not a baseline divergence

The prompt's expected WP state records CDS-WP-019 as `CLOSED` and CDS-WP-020 as
`ACTIVE / AUTHORIZED`. The repository text at HEAD still records CDS-WP-020 as
`Planned`, not active, and not authorized.

This is **not** a baseline divergence and did not trigger a stop. The Git baseline
matched exactly. The work-package text lags by construction: each work package's
own commit marks the previous one `Completed` and records its own activation, so
the repository always trails the authorization by one step. CDS-WP-019 recorded
exactly the same divergence and reached the same conclusion, and
`project-system/WORK_PACKAGES.md` states the rule directly — CDS-WP-019 *"left
`Planned` only when the Human Maintainer authorized it separately."* This prompt
is that separate authorization for CDS-WP-020.

## Discovery

Read in full before any file was touched: `CLAUDE.md`, `README.md`, the four
`project-system/` control files, `project-brain/PROJECT_BRAIN.md`, all eleven
CDS-WP-019 visual foundation documents, the CDS-WP-011 machine-readable source
documents (source model, format profile, metadata and provenance model, reference
and resolution model, validation contract), the Token and Theme Architecture, the
Decision Index scope and the specific decisions relied on, the Risk Register scope
and the specific risks relied on, and the forward roadmap.

Inspected directly rather than inferred: `tokens/**`, `schemas/**`, `tools/**`,
`tests/**`, `artifacts/validation/**`, and the CDS-WP-019 and DEC-S-127 commit
file sets.

### What the machinery actually supports

Four findings from reading the implementation rather than the documentation about
it:

1. **The committed token-document schema places no `$type` constraint.** It
   validates structure, the CDS `$extensions` payload, and segment naming. A
   visual token document would pass it unchanged.
2. **The offline validator's token-type set is a V2 coverage boundary, not a
   profile admission.** It is scoped by DEC-S-098 and exists to keep V2 honest;
   reading it as "the types CDS admits" is exactly RISK-074.
3. **The semantic-status V4 extension fires only on a document with a root group
   named `status`.** A visual token document would not trigger it and would be
   recorded `Not assessed` at V4 — which is correct, since V4 semantics for visual
   families are CDS-WP-024's.
4. **Therefore nothing in the tooling blocks a visual source set.** What blocks it
   is that authoring one requires normative choices nobody has made.

### The validator stack is not installed in this environment

`jsonschema`, `rfc8785`, and `pytest` are absent, and no
`cds-validator-venv` exists. Installing dependencies is prohibited without
explicit approval (`CLAUDE.md`, *Prohibited decisions*), so **no validator run and
no test execution was possible in this session**. This is recorded as a fact, not
as a reason: it independently reinforces the conclusion below, because the prompt
requires that any added implementation file be validated and regression-tested,
and neither was executable here.

## Decision-need assessment

The prompt's Decision Need Gate required that no new normative choice be
implemented where existing authority is insufficient. Each candidate area was
tested against the committed sources rather than assumed.

| Area | Existing authority | Verdict |
| --- | --- | --- |
| Visual token family registry | VF-1 … VF-9 registered by CDS-WP-019 | **Sufficient** — applied, not created |
| Reference / semantic layer separation | DEC-S-024, DEC-S-079 | **Sufficient** |
| Alias semantics and fail-closed resolution | DEC-S-078, DEC-S-091 | **Sufficient** |
| Naming constraints (segment syntax, prohibited terms) | DEC-S-081, DEC-S-082, DEC-S-110, N-1 … N-8 | **Sufficient** |
| Role classes per family | The CDS-WP-019 family architectures | **Sufficient** — consolidated, not invented |
| Role obligations | CR-1 … CR-6, TR-1 … TR-6, SP-1 … SP-5, SH-1 … SH-5 | **Sufficient** — consolidated as SR-1 … SR-12 |
| Format, serialization, provenance, validation layers | ADR-0001, ADR-0002, DEC-S-073 … DEC-S-092 | **Sufficient** |
| Value-selection discipline | RISK-003 mitigation direction, DEC-S-033, accessibility policy | **Sufficient** |
| **Colour model / colour space** | *"not decided here — it is CDS-WP-020's"* | **Insufficient → OD-1** |
| **Visual `$type` vocabulary** | Deferred decision 2, *"not enumerated here"* | **Insufficient → OD-2** |
| **Source-set structure and topology** | Classes only; DEC-S-115 precedent; DEC-S-032 topology deferral | **Insufficient → OD-3** |
| **Naming grammar (concrete path shape)** | Explicitly non-normative illustration; DEC-S-117 precedent | **Insufficient → OD-4** |
| **Palette architecture and scale topology** | *Deferred decisions* in three family architectures | **Insufficient → OD-5** |
| **Concrete role vocabulary; family granularity** | Deferred decision 3; the lifecycle document's open capacity question | **Insufficient → OD-6** |
| **Mode / theme representation** | **CDS-WP-022's** | **Out of scope — and it gates value selection → OD-7** |
| **Breakpoint semantics** | **CDS-WP-021's** | **Out of scope; CR-004 unchanged** |
| **Typography value representation** | Structure derivable; typeface gated by FP-1 … FP-8 | **Sufficient for structure; typeface stays deferred** |
| **Density model** | Constraints only; levels explicitly undefined | **Folded into OD-5 and OD-6** |
| **Extension-point introduction** | **CDS-WP-032's**; the set is empty | **Out of scope — none created** |

### Why the gate produced DECISION_REQUIRED rather than implementation

The five work packages that made comparable first-of-their-kind normative choices
each registered a Decision block, and three of them an ADR: **CDS-WP-011**
(DEC-S-073 … DEC-S-082, ADR-0001), **CDS-WP-012** (DEC-S-083 … DEC-S-092, ADR-0002),
**CDS-WP-013** (DEC-S-093 … DEC-S-104, ADR-0003), **CDS-WP-014**
(DEC-S-105 … DEC-S-114), and **CDS-WP-015** (DEC-S-115 … DEC-S-124) — the *Decision
types* table of the Decision Index records each block against its work package.
**CDS-WP-019, by contrast, registered none — correctly, because it made no new
normative choice.**

CDS-WP-020 sits across that line. Its **contract** half makes no new normative
choice and was delivered. Its **value** half cannot be executed without making at
least seven, and Claude creates no Decision, ADR, or risk entry without separate
authorization. Writing a token file anyway would have settled OD-1 … OD-5 by
implication — **acquiring** authority rather than receiving it, which DEC-S-033
prohibits outright.

## Risk-need assessment

**No new risk is required, and none was registered.** The risk surface of
CDS-WP-020 as executed is already carried by: **RISK-003** (premature design
decisions — whose registered mitigation direction *is* the open-decision register
produced here), **RISK-021** (token and override proliferation), **RISK-026**
(architecture overdesign), **RISK-029** (single-maintainer bottleneck),
**RISK-031** (maturity inflation), **RISK-040** (ceremony without decision),
**RISK-061** (token identifier collision), **RISK-074** (partial DTCG coverage
overstated), **RISK-087** (visual-only status encoding), and **RISK-091**
(semantic status tokens mistaken for visual tokens).

Registering a duplicate would add ceremony that produces no decision — which
RISK-040 exists to prevent. **No risk was accepted, closed, or re-scored.**

## What was produced

| Artifact | Class | What it does |
| --- | --- | --- |
| [Visual Reference Token Foundation](../docs/architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md) | 1 — normative | Defines token-flow layer 1 for the visual families: RP-1 … RP-10, ST-1 … ST-7, RN-1 … RN-9, RV-1 … RV-5, RB-1 … RB-5, the machine-readable disposition, and ten validation requirements handed to CDS-WP-024 |
| [Visual Semantic Token Foundation](../docs/architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) | 1 — normative | Defines token-flow layer 2: SR-1 … SR-12, the alias model AL-1 … AL-8, SN-1 … SN-9, PN-1 … PN-5, TC-1 … TC-7, SS-1 … SS-8, IS-1 … IS-5, the focus role set, and fifteen validation requirements |
| [Visual Token Value Selection Rules](../docs/governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md) | 1 — normative | The discipline any future value must satisfy: VP-1 … VP-7 prerequisites, the VE-1 … VE-12 evaluation, IG-1 … IG-10 inadmissible grounds, the VD-1 … VD-8 record, VA-1 … VA-10 accessibility constraints, VS-1 … VS-6 validation strategy, and the lifecycle disposition |
| [Visual Token Foundation Open Decisions](../docs/roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md) | 8 — **non-normative** | OD-1 … OD-7 with proposition, alternatives, recommendation, affected files, and track; the items that are *not* open decisions; and the recommended instruments |

## The seven open decisions, in one line each

| # | Proposition | Recommendation |
| --- | --- | --- |
| **OD-1** | The colour space CDS authors in, and its encoding | A standard gamma-encoded RGB space as the sole authored space; every other representation generated |
| **OD-2** | The admitted `$type` set for visual families | Minimal scalar set now; composites only on demonstrated need |
| **OD-3** | Visual source-set identity, granularity, and topology | Per family, per token-flow layer — the only shape that preserves AF-1 and AF-3 |
| **OD-4** | The concrete identifier grammar | Family-rooted with a declared modifier position; layer stays in manifest metadata |
| **OD-5** | Scale topology for the dimensional families | One declared base unit; per-family step sets derived by a declared rule |
| **OD-6** | The role vocabulary, and how many families CDS matures separately | Minimal vocabulary bound to the six registered Layer-3 consumer anchors; mature VF-1 and VF-2 separately, group VF-3 / VF-5 / VF-6 |
| **OD-7** | Whether a role may carry a binding before CDS-WP-022 fixes the theme mechanism | Reorder — authorize CDS-WP-022 before value selection; hold "no binding" until then |

## Findings

*(Recorded 2026-08-26. **Historical for its date and not rewritten.** For current
state see *Decision Integration Pass — 2026-08-27* below: DEC-S-128 … DEC-S-131
and ADR-0004 were later prepared under a separate Human-Maintainer
authorization, and are **effective** at the Human-Maintainer integration commit
`42a568d823de3388e45af62967546f13ad67eff6`.)*

| # | Finding | Disposition |
| --- | --- | --- |
| **F-020-01** | The value half of CDS-WP-020 is gated on **seven** normative choices no committed source has made. | **DECISION_REQUIRED.** Recorded as OD-1 … OD-7. **DEC-S-128 and ADR-0004 recommended; neither created.** |
| **F-020-02** | **AF-1 / AF-3 versus source-set metadata:** a source-set payload carries **one** `maturityState`, but the lifecycle model requires per-family maturity that is never inherited. A shared visual source set cannot express both. | Recorded as **OD-3**, coupled to **OD-6**. Not resolved here. |
| **F-020-03** | **T-2 is vacuously satisfiable today.** *"Every semantic role must resolve in every supported context"* is trivially true when **zero** contexts are supported, so it cannot guide whether a default binding is legitimate. | Recorded as **OD-7**. The semantic foundation adds **TC-6** so the gap is at least stated. |
| **F-020-04** | **The validator's bounded `$type` set is routinely readable as a CDS profile admission.** It is a DEC-S-098 V2 coverage boundary. | Stated explicitly in the reference foundation's machine-readable disposition and in **OD-2**, citing **RISK-074**. |
| **F-020-05** | **`docs/architecture/TOKEN_AND_THEME_ARCHITECTURE.md` question 4 (*"How are aliases represented?"*) is stale** in the same way F-019-04 records questions 1, 2, and 7 to be: the CDS Token Format Profile and DEC-S-078 settled alias representation. F-019-04 does not currently name question 4. | **Deferred, not repaired.** Routed to the same destination as **F-019-04** — a bounded, separately authorized reconciliation. CDS-WP-020 edited no CDS-WP-005 document. |
| **F-020-06** | **No registered consumer requirement asks for a palette, a type scale, a spacing scale, a radius scale, an elevation model, an icon library, or illustration**, and VF-3, VF-5, VF-6, VF-7 carry no consumer demand evidence at all. Building a full role vocabulary now would be unevidenced structure. | Carried into **OD-6** as the argument for a minimal, anchor-bound vocabulary. |
| **F-020-07** | **The pinned validator stack is not installed** in this execution environment, and installing dependencies is prohibited without approval. No validator run and no test execution was possible. | Recorded. **No implementation file was added**, so no regression run was owed. Nothing was weakened to compensate. |
| **F-020-08** | The governance-capacity question CDS-WP-019 routed to CDS-WP-020 (**F-019-07**: nine artifact families, one Human Maintainer, Consumer Maintainer unstaffed) is **answerable only together with the role vocabulary**. | Answered as a **recommendation** inside **OD-6** — reduce the number of families matured separately. **No family register was changed.** |

## What was deliberately not done

*(Recorded 2026-08-26. **Historical for its date and not rewritten.** For current
state see *Decision Integration Pass — 2026-08-27* below: DEC-S-128 … DEC-S-131
and ADR-0004 were later prepared under a separate Human-Maintainer
authorization, and are **effective** at the Human-Maintainer integration commit
`42a568d823de3388e45af62967546f13ad67eff6`.)*

- **No token source file, manifest, or resolver** was created. `tokens/` is
  untouched.
- **No schema was added or changed.** `schemas/` is untouched.
- **No validator rule, diagnostic, or test** was added or changed. `tools/` and
  `tests/` are untouched. **No test expectation was weakened and no fixture was
  rewritten.**
- **No visual value of any kind** was selected — no colour, colour space, palette,
  typeface, font stack, weight, size, line height, tracking, spacing step, radius,
  stroke, shadow, opacity level, elevation step, icon dimension, motion value, or
  breakpoint.
- **No identifier** was created, adopted, reserved, or recommended for adoption.
- **No Decision, ADR, or risk entry** was created; `docs/decisions/DECISION_INDEX.md`
  and `docs/risks/RISK_REGISTER.md` are untouched. The registers stay at **127**
  and **98**, and the ADR range stays **ADR-0001 … ADR-0003**.
- **No Semantic Status artifact** was touched. `tokens/semantic/status/**`, its
  source revision, maturity, approval, and evidence are unchanged, and
  `AE1-CDS-WP016-SEMSTATUS-004` was **not** transferred to anything.
- **No maturity was promoted.** VF-1 … VF-9 remain `Proposed`; visual Candidate
  families remain **0**; Stable remains **0**.
- **No theme, no Product Profile, no named extension point, no pilot, no consumer
  activation, no claim, no release, no tag, and no publication change.**
- **No capability domain** was registered — audio, haptics, multimodal feedback,
  and AI/agent interaction remain outside registered scope, and **F-017-03**
  remains open.
- **No CDS-WP-021 work** was begun, and **CR-004's registered Layer-5 mapping was
  not altered.**
- **No Git write of any kind.**

## Authority statement

CDS-WP-020 as executed **creates no design value, admits no evidence, changes no
maturity, accepts or closes no risk, adds no Decision or ADR, renames no phase,
registers no capability, makes no claim, and activates no Product Profile, pilot,
consumer integration, release, tag, publication, or later work package.**

The four documents it produced are **proposals** until the Human Maintainer
integrates them. Three are normative-on-commit for **structure and obligations
only**; the fourth is explicitly **non-normative**. None of them grants maturity
to anything, and **an architecture document is not the artifact** (AF-5).

## R1-F-03 micro-rework

*(Bounded correction — recorded here because it changed a normative document
after the Fresh Independent CDS-WP-020 Review R1 had read it.)*

- The Independent Review reproduced **one dangling normative cross-reference**.
- **The citation used the `VR-` prefix with index 7, which exists nowhere in
  CDS.** `VR-` is the validation-rule series in the Visual Foundation Governance
  and Lifecycle document, and it ends at **VR-5** — there is no sixth and no
  seventh member.
- The intended existing rule is **`VD-7`** — *its known limitations, stated
  honestly, including what has not been evaluated* — defined in the value
  selection record table that the defective sentence directly follows.
- **The cross-reference was corrected only:** the series prefix was changed to
  `VD-`, index **7** unchanged — a single byte. The surrounding sentence was not
  rewritten, and the file's byte length is unchanged.
- **No normative semantics changed.** No rule was added, removed, renumbered,
  restated, or reordered, and no other CDS-WP-020 content was touched.
- **No P1 / P2 / P3 decision was made**, and no Decision, ADR, or risk entry was
  created.
- **CDS-WP-020 remains `DECISION_REQUIRED` and not closed.** OD-1 … OD-7 stay
  open.
- Integration still requires a **Fresh Independent R2 Delta Review** and Nova
  adjudication.
- The defective token is deliberately **not reproduced literally** in this note,
  so that the repository-wide dangling-reference check stays clean.

## Decision Integration Pass — 2026-08-27

*(Additive section. **Date: 2026-08-27.** The file header date above is
**2026-08-26** and records when the original execution happened; it is historical
and is **not** rewritten.)*

**Executor-produced working notes. Not normative, not evidence, and not a review.**

### What was authorized, and what it is not

The Human Maintainer authorized a bounded **Decision Integration Pass** on
2026-08-27, after Nova adjudicated OD-1 … OD-7. It prepared **four Decisions and
one ADR** in the working tree:

| Instrument | Substance |
| --- | --- |
| **DEC-S-128** | One canonical normative visual colour representation — the pinned DTCG 2025.10 colour space keyed `srgb`. OKLCH is a derivation and design-analysis space only: not a source space, not a second canonical representation, not authority, not evidence. Delivery quantization belongs to the channel boundary. Out-of-model source values fail closed. `alpha` stays part of the colour value; **no standalone opacity family**; `hex` gains **no** new authority and **no** new prohibition. |
| **DEC-S-129** | **WCAG 2.2** as the contrast evaluation authority — **not** `WCAG 2.x`, **not** `latest`. The method is the one the cited criteria themselves require; **no threshold is restated or invented**. Comparison at full precision, **no rounding before comparison**. APCA and other methods may be **calculated and recorded as informational only** — calculation is not adoption. An automated calculation is **not** evidence and grants **no** AE level. |
| **DEC-S-130** | An explicit, minimal, **closed** `$type` admission profile: `color`, `dimension`, `number`. **DTCG-defined is not CDS-admitted.** Explicit own typing required; group and root typing are not typing authority; no composites; font-family and font-weight identity **not** admitted prematurely. `$type` carries **value-type semantics only**. `$type` is identity- and digest-affecting, and **evidence never transfers over that revision change**. **`profileVersion` stays `1`.** |
| **DEC-S-131** | The **Source Set** is the canonical independently evaluable unit; one per Family × Token-Flow-Layer; maturity binds to (`sourceSetId`, `sourceRevision`); **one manifest may aggregate many source sets**; manifest maturity describes only the manifest; **AGGREGATED is not MATURE**; a rename is an identity event, a file move is not. |
| **ADR-0004** | Architecture rationale for **DEC-S-128, DEC-S-130 and DEC-S-131**. **DEC-S-129 is deliberately not an architecture dependency of it** — it is an accessibility-methodology decision, and the exclusion is recorded rather than left implicit. |

**None of them is effective.** All five are **`PROPOSED / AUTHORIZED FOR
INTEGRATION`**, and effectivity occurs **only** at the Human-Maintainer exact-byte
integration commit, after a Fresh Independent Review and Nova integration
adjudication. The **effective** registers remain **DEC-S-127** and **ADR-0003**
until then; the **prepared** object holds **131** decisions and **4** ADRs.

> **Additive supersession note.** The paragraph above is **point-in-time, written
> before integration, and not rewritten.** That integration commit has since
> occurred — `42a568d823de3388e45af62967546f13ad67eff6` — so **DEC-S-128 …
> DEC-S-131 are effective and ADR-0004 is `Accepted`**, and the **effective**
> registers are **DEC-S-131** and **ADR-0004**, holding **131** decisions and **4**
> ADRs. **The counts did not change; only the effectivity qualification did.**

### External authority verification

The three type literals and the colour-space key were verified **directly against
the final published DTCG 2025.10 technical reports**, not inferred from CDS tooling:

| Item | Literal | Report |
| --- | --- | --- |
| Token type | `color` | **Format Module 2025.10**, Final Community Group Report, 28 October 2025 |
| Token type | `dimension` | **Format Module 2025.10**, Final Community Group Report, 28 October 2025 |
| Token type | `number` | **Format Module 2025.10**, Final Community Group Report, 28 October 2025 |
| sRGB `colorSpace` key | `srgb` | **Color Module 2025.10**, Final Community Group Report, 28 October 2025 |
| sRGB components | Red, Green, Blue, each 0 – 1 | **Color Module 2025.10**, Final Community Group Report, 28 October 2025 |

The committed validator's V2 token-`$type` set was consulted **as corroboration
only** and was **not** treated as authority. **A tool accepting a type is not the
profile admitting it** — that reading is RISK-074, and closing it is part of what
DEC-S-130 does.

### `F-020-02` — precise correction

**The conclusion of `F-020-02` stands.** A source-set payload carries **one**
`maturityState`, so a shared visual source set spanning several families cannot
express the per-family, never-inherited maturity AF-1 and AF-3 require.

**Its artifact-count mechanism was imprecise.** The finding, and OD-3 option (b)
which carried it, implied that per-family, per-layer source sets multiply manifests
and resolvers at the same rate — recorded as *"ten sets, plus manifests and a
resolver"*. Reading the committed manifest contract rather than reasoning about it
shows otherwise: it carries a **`sourceSets` array**, and each entry independently
carries `sourceSetId`, `path`, `layer`, `dependencies`, `sourceRevision`,
`maturityState` and `approvalState`. **One manifest may therefore aggregate many
source sets without collapsing any of them**, and the governance cost of preserving
AF-1 and AF-3 is smaller than the finding assumed.

The correction matters because it removed the cost basis of the argument for
collapsing independent maturities into one shared artifact. **A source set is not a
manifest**, and **AGGREGATED is not MATURE**.

### Open items that stayed open

| Item | State |
| --- | --- |
| **OD-4** — identifier grammar below the root segment | **OPEN** |
| **OD-5** — scale topology | **OPEN** |
| **OD-6** — role vocabulary and family granularity | **OPEN**, and **not pre-answered** by DEC-S-131 |
| **OD-7** — theme and context sequencing against CDS-WP-022 | **OPEN** |
| **VP-3** — scale topology decided | **UNSATISFIED for every family** |
| **VP-4** — identifier grammar decided | **UNSATISFIED for every family** |
| **VP-5** — source-set identity and topology decided, with an immutable revision | **UNSATISFIED for every family** — the rule exists, the instance does not |
| Residual under **OD-1** | The CDS-specific disposition of the optional DTCG `hex` member |
| Residual under **OD-2** | Font-family and font-weight identity representation; composite-type admission |
| Residual under **OD-3** | The concrete visual source-set root identifiers, coupled to OD-4 |

**VP-2 became satisfied** for the families expressible in `color`, `dimension` and
`number`, and for colour representation — **and that changes nothing about whether
a value may be selected.** It may not. **Four Decisions do not complete the value
system**, and claiming otherwise would be exactly the overstatement this project
keeps having to refuse.

### What was deliberately not done in this pass

- **No visual value of any kind**, and **no identifier** — created, adopted,
  reserved, or recommended.
- **No token source file, manifest, or resolver.** `tokens/` untouched.
- **No schema, validator, test, or fixture change.** `schemas/`, `tools/`, `tests/`,
  `fixtures/`, `artifacts/` and `docs/foundations/` untouched.
- **No `profileVersion` bump** — it stays `1` everywhere.
- **No Semantic Status change.** No source byte, revision, maturity, approval, or
  evidence; `AE1-CDS-WP016-SEMSTATUS-004` transferred to nothing.
- **`RISK-099` not created.** It was explicitly assessed and is **not required**:
  the normative OKLCH-to-sRGB accessibility-path conversion architecture that would
  have created the exposure was **rejected** by DEC-S-128. The register stays at
  **98**, and **no risk was accepted, closed, or re-scored**.
- **No evidence admitted, no maturity promoted.** VF-1 … VF-9 stay `Proposed`;
  visual source sets stay **0**; visual Candidate families stay **0**; Stable stays
  **No**.
- **No CDS-WP-021 or CDS-WP-022 activation**, and **no roadmap reordering** —
  **OD-7 stays open**.
- **No Product Profile, pilot, consumer activation, claim, release, tag, or
  publication change.** Publication stays **`Private Development`**.
- **No Git write of any kind.**
- **CDS-WP-020 not closed.** It remains **`DECISION_REQUIRED`**, and closure is a
  separate Human-Maintainer act.

### Skills used in this pass

`ndf-work-package-runner` (execution frame and guardrails),
`ndf-adr-governance-review` (ADR need and next number derived from context, not
invented), `ndf-changelog-writer`, `ndf-docs-polish-runner`,
`ndf-context-pack-maintainer`, `ndf-compact-context-summary-runner`. **No Skill
granted authority, extended scope, or overrode the prompt or the normative
sources.**

## Related documents

- [Visual Reference Token Foundation](../docs/architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md)
- [Visual Semantic Token Foundation](../docs/architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
- [Visual Token Value Selection Rules](../docs/governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
- [Visual Token Foundation Open Decisions](../docs/roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md)
- [Visual Foundation Architecture](../docs/architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Governance and Lifecycle](../docs/governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
- [Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md)
- [Work Packages](../project-system/WORK_PACKAGES.md)
- [CDS-WP-019 Notes](CDS_WP_019_CORE_VISUAL_FOUNDATION_ARCHITECTURE_NOTES.md)
- [Decision Index](../docs/decisions/DECISION_INDEX.md) — DEC-S-128 … DEC-S-131, **effective at commit `42a568d8…`**
- [ADR-0004 — Visual Token Representation and Source Identity Architecture](../docs/decisions/ADR-0004-VISUAL_TOKEN_REPRESENTATION_AND_SOURCE_IDENTITY_ARCHITECTURE.md) — **`Accepted`, effective at commit `42a568d8…`**
