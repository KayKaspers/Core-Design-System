# CDS-WP-019 — Core Visual Foundation Architecture — Notes

**Executor-produced working notes. Not normative, not evidence, and not a
review.** They require an independent review by a reviewer who is not their
executor before any closure claim is made.

- **Work package:** CDS-WP-019
- **Date:** 2026-08-26
- **Executor:** Claude (scoped executor)
- **Baseline:** `main` at `e5d5d492619071655ba956713980d1ee261d9213`, working tree
  clean, index clean, `origin/main` identical, ahead/behind `0 / 0`, 0 tags, no
  merge/rebase/cherry-pick in progress
- **Skills used:** `ndf-work-package-runner` (execution frame and closing
  structure), `ndf-architecture-blueprint-runner` (blueprint shape: context,
  goals/non-goals, components, boundaries, open questions), `ndf-ui-style-system-runner`
  (structuring visual-style guidance neutrally, options over mandates),
  `ndf-accessibility-reviewer` (advisory accessibility framing without any
  certification claim), `ndf-docs-polish-runner`, `ndf-changelog-writer`,
  `ndf-context-pack-maintainer`, `ndf-compact-context-summary-runner`. Reported
  openly per the Skills-first operating mode. **No Skill granted authority, extended
  scope, or overrode the prompt or the normative sources.**

## Objective

Define the architecture of the CDS visual foundation — **how** visual foundations
are structured, governed, represented, extended, validated, and consumed — without
producing a finished Core brand, activating a Product Profile, implementing a
component system, or authorizing a consumer rollout.

## Baseline verification

Every element of the expected baseline was verified read-only before any file was
touched, and every element matched:

| Check | Expected | Observed |
| --- | --- | --- |
| Repository root | `D:\Projects\Core-Design-System` | matched |
| Branch | `main` | matched |
| HEAD | `e5d5d492619071655ba956713980d1ee261d9213` | matched |
| `origin/main` | same commit | matched |
| Ahead / behind | `0 / 0` | matched |
| Working tree · index | clean · clean | matched |
| Tags | 0 | matched |
| Active merge / rebase / cherry-pick | none | none |

The negative-state sentinels were verified against the registers, not from memory:
**DEC-S-126** highest and 126 entries; **RISK-098** highest and 98 entries;
**ADR-0001 … ADR-0003**; Semantic Status at `semantic-status-rev-0002-candidate`,
`Candidate` / `Approved`, `AE1-CDS-WP016-SEMSTATUS-004` at AE-1.

### The work-package-state divergence, and why it is not a baseline divergence

The prompt's expected **WP state** records CDS-WP-018 as `CLOSED` and CDS-WP-019 as
`ACTIVE`. The repository text at HEAD still recorded CDS-WP-018 as `Next` and
CDS-WP-019 as `Planned`.

This is **not** a baseline divergence and did not trigger a stop. The Git baseline
matched exactly. The work-package text lags by construction: each work package's own
commit marks the **previous** one `Completed` and itself `Next`, so the repository
always trails the authorization by one step — the same pattern CDS-WP-018 applied to
CDS-WP-017 in commit `e5d5d492…`. Reconciling that text is part of this work
package's job, and it was done.

## Discovery

Read in full before any edit: `README.md`, `CLAUDE.md`, all four `project-system/`
documents, `project-brain/PROJECT_BRAIN.md`, all sixteen `docs/architecture/`
documents relevant to Layer 3 and the token flow, the governance policies
(concept and scope, governance operating model, maturity lifecycle, versioning,
exception and Product Profile governance, all seven accessibility documents), the
Semantic Status contract and communication contract, the Decision Index register
scope, the Risk Register index, and the forward roadmap.

### The verified starting point

A search for concrete visual values across `docs/`, `project-system/`,
`project-brain/`, `tokens/`, `schemas/`, `README.md`, and `CLAUDE.md` returned
**zero** hits for hex colours, `px`/`rem` dimensions, and font names.

> **No visual value existed at the baseline. This was verified, not assumed.**

### Existing visual authority found

| Source | What it already establishes |
| --- | --- |
| **DEC-S-021** (eight-layer model) | Layer 3 registers *"Colour, typography, space and size, grid and layout, shape, elevation, motion, iconography, design tokens, theme mechanisms, semantic status foundations"* |
| **DEC-S-024** (token flow) | **Exactly five** layers, semantic-first, prohibited shortcuts, validation requirements |
| **DEC-S-025 / DEC-S-043** | Product Profile bounds; twelve mandatory profile elements |
| **DEC-S-029 / invariant 13** | Presentation may differ across channels; meaning may not |
| **DEC-S-032** | Concrete visual values deliberately open |
| **DEC-S-049 … DEC-S-060** | Accessibility target, target-versus-claim, responsibility, channel profiles, exception limit |
| **DEC-S-073 … DEC-S-092** · ADR-0001/0002 | Format, profile, naming, references, metadata, validation, determinism |
| **DEC-S-105 … DEC-S-112** | The five status axes and their invariants |
| **DEC-S-125 / DEC-S-126** | Channel-profile applicability boundary; Candidate route and evidence non-transfer |
| **CR-002, CR-006, CR-021, CR-022, CR-023, CR-025** | The six Layer-3 consumer requirements |
| **WCAG 2.2 AA Applicability Matrix** | 14 criteria mapped to Layer 3; 5 classified `Normative CDS requirement` |
| **Accessibility Requirements Baseline** | 69 requirements across 10 areas; **all seven of area 3 (Visual Access)** are visual foundation requirements |

### Classification of the discovery

| State | Areas |
| --- | --- |
| **Already decided** | Layer model · token flow · authority classes · profile bounds · channel rule · format and profile · validation contract · accessibility target and evidence model · status semantics · maturity and versioning |
| **Partially defined** | Theme *mechanism* (open question 5 of the token architecture) · responsive model · component token granularity |
| **Open** | Every visual value · admitted `$type` set · concrete vocabulary · extension points · status-to-visual binding |
| **Historical** | The CDS-WP-005 *"Layer responsibilities in this work package"* statements; the CDS-WP-009 Pre-Candidate plan's forward references |
| **Non-normative** | `docs/research/**` · benchmark material · PB001 |
| **Prohibited** | Selecting values · registering audio, haptic, multimodal, or AI/agent scope · activating a Product Profile |

## Decision-need assessment

The prompt required a determination, not an automatic `DEC-S-127`.

**Determination: no new Decision is required, and none was created.**

The reasoning, recorded so a reviewer can check it rather than take it:

1. CDS change control requires a Decision Index entry **where a registered decision
   changes**. No registered decision changes.
2. An **authorized work package plus Human-Maintainer approval** is the route by
   which a document becomes normative; a Decision is additionally required only for
   a new or changed normative choice.
3. Every binding statement in the CDS-WP-019 documents was traced to a decision
   already in force. That derivation is recorded **in the artifact itself** — the
   *Authority basis* section of the Visual Foundation Architecture — so it is
   reviewable rather than asserted here.

### The four statements that were stress-tested hardest

Each looked like it might be a new normative choice. Each turned out to be an
application or a deliberate non-choice:

| Statement | Verdict |
| --- | --- |
| *"Opacity is an attribute of colour and surface, not a family."* | **Positioning within registered scope.** It registers **less** than the alternative, which is the conservative reading DEC-S-023 requires on unclear authority. |
| *"Illustration and imagery are Layer 2."* | **Layer assignment**, which is what an architecture work package does. DEC-S-021 registers *iconography* at Layer 3 and *"logos and brand assets"* at Layer 2; illustration and imagery are registered as CDS deferred decision areas, so they are in scope with Layer 2 as their home. |
| *"A theme is a resolution context, not a layer."* | **Derived** from DEC-S-024's *"exactly five layers"*. |
| *"Print is a channel, not a theme."* | **Derived** from DEC-S-029 and the registered channel set. |

### What was deliberately not decided

The theme **mechanism** was the strongest candidate for a new Decision, and it was
**left open on purpose**. Selecting between a resolver-modifier context, a separate
context source set, or a combination would have been a genuinely new normative
choice. Instead the architecture fixes ten constraints (**T-1 … T-10**) that any
mechanism must satisfy, and routes the selection to **CDS-WP-022**.

> **If a proposed mechanism cannot satisfy T-1 … T-10, the mechanism is wrong — not
> the constraints.**

The same treatment was applied to the responsive model (CDS-WP-021), the
status-to-visual binding (CDS-WP-023), the admitted `$type` set and the concrete
vocabulary (CDS-WP-020), and the extension-point set (CDS-WP-032).

## Risk-need assessment

**Determination: no new risk requires registration, and none was created.**

Each candidate was checked against the existing register rather than assumed novel:

| Candidate concern | Covered by |
| --- | --- |
| Nine families defined without consumer demand | **RISK-026** (architecture overdesign), **RISK-003** (premature design decisions), **RISK-017** (documentation is not user validation) |
| Illustrative naming examples hardening into decisions | **RISK-003**, architecture invariant 3, artifact class 8, **VF-I-13** |
| Nine families multiplying beyond governable capacity | **RISK-021**, **RISK-026**, **RISK-029**, **RISK-040** |
| Visual encoding displacing status meaning | **RISK-087**, **RISK-091**, **RISK-082** |
| Channel divergence across nine channels | **RISK-024**, **RISK-046** |
| Profile and override proliferation | **RISK-021**, **RISK-027**, **RISK-035** |
| Identifier collision in a large vocabulary | **RISK-061** |
| Cross-layer dependency violation | **RISK-060** |

The register stays at **RISK-098**, and **no risk was accepted, closed, or
reclassified**.

## The architectural work — what was actually decided within existing authority

### The reconciliation that mattered most

The prompt offered a conceptual **A / B / C / D** layer reading (primitive →
semantic → context → brand). Adopting it literally would have created a **second,
competing layer model** alongside the normative five-layer token flow.

It was therefore mapped onto the existing constructs rather than adopted, and two
things were recorded explicitly:

- **C (context) is not a layer.** Treating it as one would make a presentation
  context capable of holding a decision.
- **The Component layer is absent from the A–D reading and must not be dropped.**
  Omitting it is precisely how a component silently binds a reference token and
  strips meaning.

### The nine families and the three positionings

Nine families were registered (VF-1 … VF-9), each traced to DEC-S-021 Layer 3 or
capability domain 3, each with its consumer anchor stated — **including where there
is none**.

Three subjects were **positioned rather than registered**, in each case choosing the
option that registers less scope: **opacity**, **illustration and imagery**, and
**focus indication**.

### The boundaries that later work inherits

- **COLOUR ≠ STATUS · ICON ≠ STATUS · MOTION ≠ STATUS · ELEVATION ≠ STATUS.**
- **An interaction state is not a semantic status.**
- **Roles are mandatory; values vary only at named extension points — and that set
  is empty.** This is the answer to *"must a Core product inherit every Core visual
  value?"*: it inherits every **role**, not every **value**.
- **Every semantic colour role declares its contrast obligation and its pairings**
  (VF-I-8) — the check that stops a theme or a profile from silently breaking
  conformance capability.
- **Focus visibility has no permitted mechanism of removal.** Every other visual
  decision has a legitimate route to being overridden, themed, or profiled. This one
  does not.

### The accessibility finding

Derived by re-counting the WCAG matrix programmatically, not from memory: **14**
criteria map to Layer 3, and **all five** rows classified `Normative CDS
requirement` are among them — **1.3.3, 1.4.1, 1.4.5, 2.3.1, 2.4.7**.

> **Every criterion CDS owns alone is a visual foundation criterion.**

This is the sharpest structural argument for why the visual foundation cannot be
treated as styling: it is the only place in CDS where an accessibility obligation
has no consumer to share it with.

## Findings

Recorded in the forward roadmap's deferred-finding section. **Each is recorded and
not repaired** — CDS-WP-019 is an architecture work package, not a hygiene pass —
and **none blocked it**.

| ID | Summary | Destination |
| --- | --- | --- |
| **F-019-01** | `CONCEPT_AND_SCOPE.md` still lists four already-decided areas as open — the same drift as `F-017-01`/`F-017-02`, but that file was not in CDS-WP-018's list | Bounded, separately authorized governance reconciliation |
| **F-019-02** | DEC-S-021 Layer 3 registers *iconography*; capability domain 3 does not name it, and neither domain names illustration or imagery | Same reconciliation, or CDS-WP-037 / CDS-WP-045 at authorization |
| **F-019-03** | CR-004 is mapped to **Layer 5** in the normative traceability; the roadmap plans CDS-WP-021 at **Layer 3** | **CDS-WP-021 must confirm the split before defining any responsive foundation** |
| **F-019-04** | `TOKEN_AND_THEME_ARCHITECTURE.md` still presents questions 1, 2, and 7 as open, and its preamble still describes the token interoperability source as a non-implementable preview | Bounded reconciliation, or CDS-WP-020 |
| **F-019-05** | `DESIGN_SYSTEM_ARCHITECTURE.md` still lists six decided areas under *Deferred technical decisions* | Same reconciliation |
| **F-019-06** | **No consumer requirement asks for a palette, type scale, spacing scale, radius scale, elevation model, icon library, or illustration**; VF-3, VF-5, VF-6, VF-7 have no demand evidence at all | Recorded as honesty; RISK-026, RISK-003 |
| **F-019-07** | Nine artifact families added to a model run by one Human Maintainer, with the Consumer Maintainer role unstaffed (FM-F-006) | Open capacity question for CDS-WP-020; RISK-021, RISK-026, RISK-029, RISK-040 |
| **F-019-08** | The DEC-S-062 phase label stays coherent for CDS-WP-019 but will be strained by CDS-WP-020 | **`PHASE_TRANSITION_RECOMMENDED`** raised; resolve before CDS-WP-020 is authorized; tied to F-017-04 |
| **F-019-09** | `R1-F-01` recurs by construction: the Candidate Dossier's *"Current state"* header still reads `CDS-WP-018 active` | **Not repaired** — `docs/operations/**` is outside this work package's file scope. Bounded separate repair; **removal** of the work-package-status row is the structural fix |

`F-019-01`, `F-019-04`, and `F-019-05` are the same class as `NF-R4-OBS-001`. They
were **not** repaired because each lives in a **normative source** whose change
control requires a work package that names it, and CDS-WP-019 does not.

## PB001

The roadmap routes the *Visual Foundation Gap* topic to CDS-WP-019 and CDS-WP-020.

**Nothing was imported.** PB001 is not held in this repository, its finding text
remains outside it, and CDS-WP-019 obtained no PB001 material, cited none, and used
none as an input. The architecture was derived **entirely** from the committed
normative CDS sources and the registered consumer requirements. PB001 remains
Experimental Evidence at **AE-0**, non-normative, and the routing to CDS-WP-020
stands.

## What was deliberately not done

- **No visual value.** No colour, palette, typeface, font stack, weight, size,
  spacing, radius, stroke, shadow, opacity value, icon, illustration, motion value,
  breakpoint, or theme instance.
- **No implementation.** No token source file, schema, validator rule, diagnostic,
  fixture, digest, component, channel adapter, template, or asset. Nothing under
  `tokens/`, `schemas/`, `tools/`, `tests/`, `artifacts/`, or
  `requirements-validator.lock` was touched.
- **No Semantic Status change.** No source, revision, maturity, approval, or
  evidence package. `docs/foundations/**` is byte-unchanged.
- **No Decision, ADR, or risk.** `DECISION_INDEX.md`, the ADRs, and
  `RISK_REGISTER.md` are unchanged.
- **No named extension point, no Product Profile, no brand, no identity.**
- **No phase rename**, and no Decision superseding DEC-S-062.
- **No capability registration** for audio/sonic, haptic, multimodal, AI/agent, or
  safety subject matter. The architecture was checked only for **not foreclosing**
  a future multimodal extension; it prepares none.
- **No consumer read.** No consumer repository was opened, and no consumer visual
  decision was evaluated or reconciled.
- **No hygiene sweep.** `F-019-01`, `F-019-04`, and `F-019-05` were left as found.
- **One additive edit to an existing normative architecture document**: a single
  *Related documents* row in `DESIGN_SYSTEM_ARCHITECTURE.md`, so the new family is
  reachable from the architecture entry point. Its *Deferred technical decisions*
  list and every other section were left untouched.

## Authority statement

CDS-WP-019 **proposes**. It approves nothing.

No Git write of any kind was performed — no `add`, `commit`, `push`, `pull`,
`fetch`, `merge`, `rebase`, `cherry-pick`, `tag`, `reset`, `restore`, `checkout`,
`stash`, or branch operation. Only read-only inspection was used.

No maturity was granted, no evidence produced or admitted, no risk accepted or
closed, no claim made, no artifact promoted, no Product Profile or pilot activated,
no release or tag created, and no publication state changed. Publication remains
**`Private Development`**.

**Closure is not the executor's to make.** It requires a fresh independent review by
a reviewer who is not the executor, Nova adjudication, and a Human-Maintainer
integration commit. Uncommitted executor output changes no authoritative
work-package status, and a review PASS is not a commit.

## Related documents

- [Visual Foundation Architecture](../docs/architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Colour Architecture](../docs/architecture/VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
- [Visual Foundation Typography Architecture](../docs/architecture/VISUAL_FOUNDATION_TYPOGRAPHY_ARCHITECTURE.md)
- [Visual Foundation Spatial Architecture](../docs/architecture/VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md)
- [Visual Foundation Shape and Surface Architecture](../docs/architecture/VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md)
- [Visual Foundation Iconography and Imagery Architecture](../docs/architecture/VISUAL_FOUNDATION_ICONOGRAPHY_AND_IMAGERY_ARCHITECTURE.md)
- [Visual Foundation Theme Architecture](../docs/architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
- [Visual Foundation Accessibility Mapping](../docs/governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md)
- [Visual Foundation Channel Mapping](../docs/governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Visual Foundation Brand and Product Profile Boundary](../docs/governance/VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md)
- [Visual Foundation Governance and Lifecycle](../docs/governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
- [Post-Candidate Development Roadmap](../docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md)
- [Work Packages](../project-system/WORK_PACKAGES.md)
- [CDS-WP-018 Deferred Governance Hygiene Notes](CDS_WP_018_DEFERRED_GOVERNANCE_HYGIENE_NOTES.md)
