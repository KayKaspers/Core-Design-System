# Changelog

All notable changes to the Core Design System project will be documented here.

The format will be refined before the first CDS release. No version has been
released and no release is announced.

## Unreleased

### Added

- **CDS-WP-022 effectivity — `DEC-S-137` and `DEC-S-138` effective, `ADR-0007`
  `Accepted` and effective; CDS-WP-022 integrated, NOT closed.** The condition the
  CDS-WP-022 decision package stated for itself — the Human-Maintainer exact-object
  integration commit of the exact reviewed CDS-WP-022 object — was met on
  **2026-09-12** by commit `23914ecc48c1fb3cba5e3dab97a505589e821b6b` (parent
  `01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`), which followed a Fresh Independent
  Review, a bounded corrective rework, a confirmatory independent review, and Nova
  final integration adjudication. At that commit **`DEC-S-137` and `DEC-S-138` became
  effective** and **`ADR-0007` became `Accepted` and effective**, advancing the
  effective registers from **136 decisions and 6 ADRs** to **138 decisions and
  7 ADRs** with **the risk register unchanged at 98** — **no `RISK-099`, no
  `DEC-S-139`, no `ADR-0008`** — and the supported Core Theme Resolution Contexts
  from **0** to **2**, **`Light` and `Dark`, with no default**. **This records
  completed Human-Maintainer acts and performs none.** The live current-state
  carriers were then reconciled by the already-integrated reconciliation commits
  `6f5408b1a6863e52560d8884fb9202f1cdfb85c9` (post-integration effectivity),
  `61ee2f3c67d5dd2da4443f782c56d770eaa80074` (pre-closure current state) and
  `4714f892a2780afd6425885ccc28a75533fca3df` (final residual current state), none of
  which closed CDS-WP-022. **Point-in-time records are preserved**: the event-time
  CDS-WP-022 execution and bounded-decision-rework entries below truthfully recorded
  the decision package as prepared and not effective at their own time, and remain
  as written. **The effectivity created 0 visual values and 0 visual Source Sets**;
  it **did not close CDS-WP-022**, **authorized neither `CDS-WP-020A` nor
  CDS-WP-023 … CDS-WP-053**, **authorized no successor**, **granted no maturity**,
  and **admitted no evidence** — **`EFFECTIVE ≠ CLOSED`**: **CDS-WP-022 remains
  `AUTHORIZED` / `ACTIVE FOR EXECUTION`, integrated, and not closed**, and closure is
  a separate Human-Maintainer act that has not occurred. **VP-3, VP-5, VP-6 and VP-7
  stay `UNSATISFIED`**, **VP-4 stays `UNSATISFIED` for VF-4**, **`WP021-D2` stays
  DEFERRED**, and **`DEC-S-135` is unchanged** — its theme-mechanism sequencing
  condition is satisfied from that commit, and **`THEME GATE SATISFIED ≠ VALUE
  SELECTION AUTHORIZED`**.
  (CDS-WP-022 final pre-closure reconciliation)
- **CDS-WP-022 — Theme and Environmental Presentation Model: separately authorized
  by the Human Maintainer, executed with result `DECISION_REQUIRED`.** The Human
  Maintainer **separately and explicitly authorized CDS-WP-022** after the CDS-WP-021
  closure became effective at `01145b8a0ad2a68c4c2743205f96ec34f3c2ed15`, and it is
  **`AUTHORIZED` / `ACTIVE FOR EXECUTION`** — **the current authorized work
  package**. **The authorization is a Human-Maintainer act and nothing else:** it was
  the Nova-recommended and `DEC-S-135`-sequenced Step-10 candidate, and **`SEQUENCED
  NEXT ≠ AUTHORIZED`**, **`CLOSED ≠ SUCCESSOR AUTHORIZED`** and **`DEPENDENCY
  SATISFIED ≠ AUTHORITY GRANTED`** all continue to hold. **CDS-WP-021 remains
  `Completed` / `Closed`** with its execution result unchanged at **`COMPLETE WITH
  NOTES`**; **`CDS-WP-020A` and CDS-WP-023 … CDS-WP-053 remain `Planned`, not active,
  and not authorized**, and **no roadmap row was reordered**.
  **Contract only, and deliberately incomplete.** The
  [Visual Foundation Theme Architecture](docs/architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
  now carries the derived Layer-3 contract for **VF-9**: the **Theme Resolution
  Context** term and the *environmental presentation* category; the **context
  admission contract** (**CA-1 … CA-13**); **context identity** (**CI-1 … CI-6**);
  **context selection and resolution entry** (**CS-1 … CS-8**); the
  **environmental-input boundary** (**CE-1 … CE-5**); the **fail-closed conditions**
  (**CF-1 … CF-10**); and the **composition boundaries** against channel, Spatial
  Context, Product Profile, semantic role identity, Semantic Status, Source Set and
  the five token-flow layers (**CB-1 … CB-7**). It also records a derived
  **machine-readable boundary** and the reconciled *context set*, *open
  mechanism*, *Validation requirements*, *Evidence and claim boundary* and *Deferred
  decisions* sections, and it answers **neutral / document** by existing normative
  authority — **channel scope, no new Decision required**.
  **Five normative choices are escalated, not invented** — **`WP022-D1`** the Theme
  and Context Mechanism, **`WP022-D2`** the initial supported Core context set,
  **`WP022-D3`** the forced-colours / high-contrast disposition, **`WP022-D4`**
  context selection and environmental precedence, and **`WP022-D5`** default,
  fallback and missing-context semantics. **`DERIVE ≠ DECLARE`** and **`AUTHORIZED
  WORK PACKAGE ≠ EXECUTOR AUTHORIZED TO INVENT NORMATIVE CHOICES`**; the
  **`WP022-D*` keys are execution-local report keys, not Decisions, ADRs, risks,
  requirements, or stable governance identifiers.** *(**Superseded as live current
  state by the bounded decision rework below and by the effectivity entry above**:
  the Human Maintainer decided all five on 2026-09-12, the execution result is now
  **`COMPLETE WITH NOTES`**, **`DEC-S-137`** and **`DEC-S-138`** are **effective**
  and **`ADR-0007`** is **`Accepted` and effective** from the Human-Maintainer
  exact-object integration commit `23914ecc48c1fb3cba5e3dab97a505589e821b6b`, the
  current registers hold **138 decisions, 7 ADRs and 98 risks**, and **CDS-WP-022 is
  `AUTHORIZED` / `ACTIVE FOR EXECUTION`, integrated, and not closed**. The statements
  above remain accurate for the initial execution.)*
  **No theme, no context, and no value.** **Supported Theme Resolution Contexts: 0 at
  this milestone.**
  It created **no** theme, context, context identifier, default alias, colour,
  typography, spacing, shape, surface or breakpoint value, semantic role, reference
  primitive, alias, token identifier, source set, `sourceSetId`, `sourceRevision`,
  manifest, resolver instance, schema, validator rule, test, fixture, generated
  output, Product Profile, extension point, Candidate package, release artifact, or
  tag; produced and admitted **no** evidence; changed **no** maturity — **VF-1 … VF-9
  stay `Proposed`** and **visual Candidate families stay 0**; made **no** claim;
  determined **no** conformance; renamed **no** phase; registered **no** capability;
  and activated **no** work package. **The registers are unchanged: 136 effective
  decisions, 6 effective ADRs, 98 risks** — **no `DEC-S-137`, no `ADR-0007`, no
  `RISK-099`**, and **no ADR was marked `Accepted`**, which is a Human-Maintainer act.
  **`DEC-S-135` is untouched and its gate was not cleared at this milestone**, so
  **`TS-1` still binds — no semantic visual role carries a default alias** and
  **context-sensitive value selection remains unauthorized**; **`DEC-S-136` is untouched** and
  **`SPATIAL CONTEXT ≠ THEME RESOLUTION CONTEXT`** stands with **no composition
  declared**; **`WP021-D2` stays DEFERRED** with **no VF-4 technical root and no VF-4
  Source Set identity**; and **VP-3, VP-5, VP-6 and VP-7 stay `UNSATISFIED`**, with
  **VP-4 still `UNSATISFIED` for VF-4** — the
  [Visual Token Value Selection Rules](docs/governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
  carry one **additive** VP-7 current-state note correcting only the justification.
  **The Semantic Status Candidate family is untouched** and
  **`AE1-CDS-WP016-SEMSTATUS-004` was transferred to nothing**; **publication stays
  `Private Development`** with **no release and no tag**. `tokens/**`, `schemas/**`,
  `tools/**`, `tests/**`, `artifacts/**`, `docs/foundations/**` and `docs/risks/**`
  are **untouched**, and **no existing Decision entry, proposition, status, or
  effectivity commit was edited** — only the Decision Index's maintained current
  carrier advanced. **Seven findings are recorded and routed** as **`F-022-01` …
  `F-022-07`**, including the derived gap that the **committed resolver schema cannot
  express a context condition** (a **declared DEC-S-098 coverage boundary, not a
  DEC-S-034 conflict**), routed to **`CDS-WP-020A`** and **CDS-WP-024**. **The object
  is prepared and uncommitted**, awaiting a **fresh independent review** (reviewer ≠
  executor), **Nova adjudication**, a **Human-Maintainer exact-object integration
  commit**, and — separately — **closure**: **`EXECUTION ≠ CLOSURE`**, **`REVIEW PASS
  ≠ INTEGRATION`**, and **`INTEGRATION ≠ CLOSURE`**.
- **CDS-WP-022 bounded decision rework — Human Maintainer approved
  `WP022-D1` … `WP022-D5`; `DEC-S-137`, `DEC-S-138` and `ADR-0007` prepared, NOT
  effective.** The Human Maintainer **decided all five escalations on 2026-09-12** and
  authorized a bounded rework to apply them to the existing uncommitted CDS-WP-022
  object. **CDS-WP-022's execution result is now `COMPLETE WITH NOTES`**; the initial
  **`DECISION_REQUIRED`** is **execution history and is not rewritten**, and the
  **lifecycle status and the execution result remain separate axes**. **CDS-WP-022
  stays `AUTHORIZED` / `ACTIVE FOR EXECUTION` and is NOT closed.**
  **`WP022-D1` — APPROVED: a Resolver-Modifier Context over the existing Source-Set
  graph.** Theme- and context-sensitive binding is represented through the existing
  normative **Resolver / Composition** architecture; **no per-context Source Set is
  introduced**; **no context or theme segment enters token-path or Source-Set
  identity**; the **Source Set remains the sole independently evaluable maturity
  unit**; **context-specific evidence stays bound to (`sourceSetId`,
  `sourceRevision`)** and additionally records the **Resolver / Composition revision**
  and the **Theme Resolution Context** as **exact evidence inputs**; a **Resolver /
  Composition document never becomes a maturity carrier** — **`EVIDENCE INPUT ≠
  MATURITY CARRIER`**; **any evidence-relevant change to a source revision, a resolver
  revision, or the context invalidates or supersedes the affected evidence**; **no
  evidence transfers automatically**; **Theme Resolution Context and Spatial Context
  stay orthogonal**, with **joint Theme × Spatial rendering and evidence evaluation
  deferred** to separately authorized scope. Recorded as **`DEC-S-137` — Theme
  Resolution and Context-Evidence Architecture** with
  **[ADR-0007](docs/decisions/ADR-0007-THEME-RESOLUTION-AND-CONTEXT-EVIDENCE-ARCHITECTURE.md)**,
  which covers **`DEC-S-137` only** — **`DEC-S-138` is deliberately not an
  architecture dependency of it.**
  **`WP022-D2` … `WP022-D5` — APPROVED and recorded as `DEC-S-138` — Core Theme
  Context, Environmental Selection and Fail-Closed Policy**, which has **no ADR**:
  **`Light` and `Dark`** as the **initial supported Core Theme Resolution Contexts**,
  **equal peers**, **neither the default**, with **no machine-readable identifier
  authored** — they are **human-readable architectural names**; **forced colours and
  platform high contrast** as an **environmental accessibility condition and NOT a
  Core Theme Resolution Context**, which supported consumers and outputs **must
  honour independently of the selected Theme**, as an **architecture obligation and
  never evidence, conformance, a claim, or an AE level** — **a future dedicated CDS
  High-Contrast Theme requires separate authorization**; an **abstract Core selection
  contract** in which **an explicit viewer choice takes precedence over an inferred
  environment preference**, with **mandatory platform accessibility conditions outside
  Theme precedence and always binding**, the **consumer or runtime owning sensing,
  persistence and transport**, **no CDS normative token artifact storing viewer or
  environment state**, and **no dependency on CSS, the DOM, a browser or OS API,
  JavaScript, a framework, a design tool, or a product runtime**; and **no Core
  default Theme, no resolver-level default Theme, and no semantic default reference
  alias**, with **missing, unsupported and unresolved equal-authority selection
  conflict all failing closed**, **no silent substitution**, and **`Not Applicable`**
  where Theme resolution genuinely does not apply — **never a hidden, fallback, or
  default Theme.**
  **Effectivity.** **`DEC-S-137`, `DEC-S-138` and `ADR-0007` are `PREPARED /
  HUMAN-MAINTAINER APPROVED / NOT EFFECTIVE` until, and effective from, the
  Human-Maintainer exact-object integration commit of the exact reviewed Working Tree
  object of CDS-WP-022**, which requires a **Fresh Independent Review** (reviewer ≠
  executor) and **Nova integration adjudication** first. **`APPROVED PROPOSITION ≠
  EFFECTIVE REPOSITORY DECISION`**, **a review PASS is not a commit**, and **a Nova
  recommendation is not an approval**. **The effective registers hold 136 decisions and
  6 ADRs until that commit and 138 decisions and 7 ADRs from it; the risk register
  stays at 98 throughout** — **no `RISK-099`, no `DEC-S-139`, no `ADR-0008`**, and
  **no ADR was marked `Accepted`**, which is a Human-Maintainer act. **Supported Theme
  Resolution Contexts: 0 before that commit and 2 — `Light` and `Dark`, with no
  default — from it.**
  **What the rework did not do.** It created **no** theme instance, machine-readable
  context identifier, default alias, colour, typography, spacing, shape, surface or
  breakpoint value, semantic role, reference primitive, token identifier, Source Set,
  `sourceSetId`, `sourceRevision`, manifest, resolver instance, schema, validator
  rule, test, fixture, generated output, Product Profile, extension point, Candidate
  package, release artifact, or tag; produced and admitted **no** evidence —
  admitting two contexts adds **two evidence obligations and zero evidence**, and
  every theme artifact stays **AE-0**; changed **no** maturity — **VF-1 … VF-9 stay
  `Proposed`** and visual Candidate families stay **0**; made **no** claim; determined
  **no** conformance; renamed **no** phase; registered **no** capability; and
  activated **no** work package. **`DEC-S-131`, `DEC-S-132`, `DEC-S-135` and
  `DEC-S-136` are unchanged in byte and in substance** — **no Decision entry,
  proposition, status, or effectivity commit was edited**, and only the Decision
  Index's **maintained current carrier** advanced. **`TS-1` still binds**: `DEC-S-138`
  part E creates **no** default reference alias, so TS-1 is **satisfied by compliance,
  not by exemption**. From the effectivity of the two new Decisions the **`DEC-S-135`
  theme-mechanism sequencing condition is satisfied** — and **`THEME GATE SATISFIED ≠
  VALUE SELECTION AUTHORIZED`**, **`THEME GATE SATISFIED ≠ CDS-WP-020A AUTHORIZED`**,
  **`ONE PREREQUISITE SATISFIED ≠ ALL PREREQUISITES SATISFIED`** and **`ALL
  PREREQUISITES SATISFIED ≠ WORK PACKAGE AUTHORIZED`**: **`CDS-WP-020A` and
  CDS-WP-023 … CDS-WP-053 remain `Planned`, not active, and not authorized**, and
  **VP-3, VP-5, VP-6 and VP-7 stay `UNSATISFIED`** with **VP-4 still `UNSATISFIED` for
  VF-4**. **`WP021-D2` stays DEFERRED** with **no VF-4 technical root and no VF-4
  Source Set identity** — **the prepared `DEC-S-137` and `ADR-0007` record `WP022-D1`
  and are unrelated to it**, and **no relation exists between approving `WP022-D1` and
  resolving `WP021-D2`**. **`F-022-01` stays routed and unresolved** — **`MECHANISM
  DECIDED ≠ REPRESENTATION AVAILABLE`** — and `tokens/**`, `schemas/**`, `tools/**`,
  `tests/**`, `artifacts/**`, `docs/foundations/**` and `docs/risks/**` are
  **untouched**. **The Semantic Status Candidate family is untouched** and
  **`AE1-CDS-WP016-SEMSTATUS-004` was transferred to nothing**; **publication stays
  `Private Development`** with **no release and no tag**. **The object is prepared and
  uncommitted**: **`EXECUTION ≠ CLOSURE`**, **`REVIEW PASS ≠ INTEGRATION`**, and
  **`INTEGRATION ≠ CLOSURE`**.
- **CDS-WP-021 bounded closure — Step 18 separately authorized by the Human
  Maintainer; closure object prepared, NOT effective.** Step 18 of the
  next-allowed-authority sequence — **the closure of CDS-WP-021** — is a **separate**
  Human-Maintainer act that neither the exact-object integration commit
  `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9` nor the effectivity of `DEC-S-136` and
  `ADR-0006` implied. The Human Maintainer has now authorized it, and this object
  records the resulting lifecycle state in the live current-authority carriers only.
  **The closure target is `CDS-WP-021` → `Completed` / `Closed`.** **The execution
  result remains `COMPLETE WITH NOTES`** — the lifecycle status and the execution
  result are **separate axes**, and the result is **not** rewritten to `COMPLETE`;
  the initial **`DECISION_REQUIRED`** execution history stands. **The integration
  commits remain historical facts**: `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9`
  (CDS-WP-021 object, 2026-09-11) and
  `1174228bf046a75af095e585d165c330cf194f47` (post-integration effectivity
  reconciliation), and **the closure commit is neither of them** — it is **not** the
  `DEC-S-136` effectivity commit and **not** the `ADR-0006` acceptance commit, both
  of which stay bound to `a6bd7bf0…`. **`WP021-D2` remains DEFERRED**: the **VF-4
  technical root and Source Set identity stay OPEN**, `sourceSetId` and
  `sourceRevision` remain **NONE**, and **`DEFERRED OPEN QUESTION ≠ INCOMPLETE WORK
  PACKAGE`** — closure records that the **authorized scope** was executed, reviewed,
  integrated and reconciled, never that every VF-4 design question is answered.
  **No successor is authorized**: **`CLOSED ≠ SUCCESSOR AUTHORIZED`**, **`DEPENDENCY
  SATISFIED ≠ AUTHORITY GRANTED`**, and **`SEQUENCED NEXT ≠ AUTHORIZED`**;
  **`CDS-WP-020A`, CDS-WP-022, CDS-WP-023, CDS-WP-024 and every other identifier
  remain `Planned`, not active, and not authorized**, no roadmap row was reordered,
  **`DEC-S-135` is untouched**, and **no work package is currently authorized.**
  **Closure becomes effective only at the Human-Maintainer exact-object integration
  commit of this independently reviewed closure object**, after a **fresh
  independent review** (reviewer ≠ executor) and **Nova final adjudication** —
  **`CLOSURE OBJECT PREPARED ≠ CLOSURE EFFECTIVE`**, and an uncommitted working tree
  closes no work package. **No Decision, ADR, risk, work package, evidence package,
  or evidence identifier was created or changed** — the registers stay at **136**,
  **6** and **98**; **no `DEC-S-137`, no `ADR-0007`, no `RISK-099`**;
  `docs/architecture/**`, `docs/governance/**` and `docs/risks/**` are untouched,
  and within `docs/decisions/**` **only the maintained Register Scope
  current-state carrier in `DECISION_INDEX.md` changed** — **no individual
  Decision entry, proposition, status, range or count changed, and `ADR-0006` is
  unchanged**. **No maturity changed**, **no claim was made**,
  **no conformance was stated**, publication stays **`Private Development`**, and
  **visual values and visual Source Sets stay 0** with **VF-1 … VF-9 `Proposed`**
  and **VP-3, VP-5, VP-6 and VP-7 unsatisfied** (**VP-4 unsatisfied for VF-4**).
  (CDS-WP-021 Step-18 bounded closure preparation)
- **`DEC-S-136` and `ADR-0006` reconciled to their effective state.**
  The condition those entries themselves stated — the Human-Maintainer exact
  integration commit of the exact reviewed CDS-WP-021 Working Tree object,
  following a Fresh Independent Review and Nova integration adjudication — was met
  on **2026-09-11** by commit `a6bd7bf0c290886bbe2695c0f9cf70efbef3f1e9` (parent
  `2d1561807e5d2a8bb673603e3f36511546631205`), which committed **16 / 16** blobs
  exact against the reviewed object. That review returned **`REWORK REQUIRED`**
  (**F-R21-01** material, **F-R21-02** minor); a **bounded two-file rework**
  resolved both, the **confirmatory independent review returned `PASS`** with **0**
  blocking and **0** unresolved material findings, and Nova adjudicated
  **`GO — EXACT-OBJECT INTEGRATION AUTHORIZED`**. The repository's live
  current-state carriers therefore no longer qualify them as
  `PROPOSED / AUTHORIZED FOR INTEGRATION` or `NOT YET EFFECTIVE`, and no longer
  name **DEC-S-135** and **ADR-0005** as the highest effective entries.
  **DEC-S-136 is effective and ADR-0006 is `Accepted`**; the effective registers
  are **DEC-S-001 … DEC-S-136 (136)** and **ADR-0001 … ADR-0006 (6)**.
  **This records a completed Human-Maintainer act and performs none** — an ADR is
  accepted by the Human-Maintainer commit its own status text bound acceptance to,
  never by an executor. **Point-in-time records were preserved**, not rewritten:
  dated review, execution, decision-time, and changelog statements that were true
  before integration remain as written, including the CDS-WP-021 preparation entry
  below and its `DECISION_REQUIRED` execution history. **No Decision, ADR, or risk
  was added, changed in substance, or removed** — the registers stay at **136**,
  **6**, and **98**; **no `DEC-S-137`, no `ADR-0007`, no `RISK-099`.** **No ADR
  rationale, alternative, consequence, or Decision scope was altered**; no visual
  value, identifier, responsive-range name, range count, threshold, VF-4 technical
  root, `sourceSetId`, `sourceRevision`, Source Set, token source, schema,
  validator rule, test, or fixture was created; **no** evidence was admitted,
  **no** maturity changed, **no** claim was made, and **no** work package was
  activated. **`EFFECTIVE ≠ CLOSED`: CDS-WP-021 remains `AUTHORIZED / ACTIVE FOR
  EXECUTION`, executed with result `COMPLETE WITH NOTES`, integrated, and NOT
  closed** — closure is a separate Human-Maintainer act that has not occurred.
  **`WP021-D2` stays DEFERRED**, with the **VF-4 technical root and Source Set
  identity OPEN** and no Decision and no ADR for it. **`DEC-S-136` decides an
  architecture, not a topology or a vocabulary**: **VP-3, VP-5, VP-6 and VP-7 stay
  unsatisfied, VP-4 stays unsatisfied for VF-4, VF-1 … VF-9 stay `Proposed`, and
  visual values and visual source sets stay 0.** **`CDS-WP-020A` and CDS-WP-022 …
  CDS-WP-053 remain `Planned`, not active, and not authorized.**
  (CDS-WP-021 post-integration effectivity reconciliation)
- **CDS-WP-021 — Adaptive Layout and Responsive Foundation. Executed with result
  `COMPLETE WITH NOTES`. Prepared and uncommitted; NOT closed.** Authorized separately
  and explicitly by the Human Maintainer as the next work package, at **step 10** of
  the next-allowed-authority sequence — **not** by the roadmap, and **not** by the
  `DEC-S-135` sequencing recommendation, which named **CDS-WP-022**. **A
  recommendation is not an authorization.** The work package adds the normative
  [Adaptive Layout and Responsive Foundation](docs/architecture/ADAPTIVE_LAYOUT_AND_RESPONSIVE_FOUNDATION.md)
  — the technology-neutral **Layer-3** adaptive-layout and responsive foundation of
  **VF-4 Layout and Grid**.
  **The Layer 3 / Layer 5 / Layer 6 split is CONFIRMED** (LO-1 … LO-8), discharging
  the obligation the Spatial Architecture placed on this work package by name and
  answering the deferred finding **`F-019-03`**: **Layer 3 owns the spatial
  vocabulary and the structural context model · Layer 5 owns the response · Layer 6
  owns channel-imposed geometry.** **`RANGE ≠ BEHAVIOUR` · `CONTEXT ≠ PATTERN` ·
  `FOUNDATION ≠ COMPOSITION`.** **`CR-004` remains registered at Layer 5**, its row
  is not edited, and **no count changes** — an additive clarifying note was added
  below the traceability matrix and **re-owns nothing**.
  It records the **spatial-context model** (CX-1 … CX-9), reconciling **RR-6** with
  the channel table — **the reference frame generalizes, the range construct does
  not**, and **continuity decides whether a range applies at all**; the
  **responsive-range obligations** (AR-1 … AR-12), applying **RR-1 … RR-6
  unchanged**; the **grid, container and content-width contracts** (GC-1 … GC-9);
  and the **density and adaptation interaction** (DA-1 … DA-6), where **obligations
  do not weaken under composition**. Accessibility is incorporated **structurally
  and claimed nowhere** — **`TARGET ≠ CLAIM` · `STRUCTURAL CONTRACT ≠ RENDERING
  EVIDENCE`** — with every rendering-dependent obligation routed to **CDS-WP-031**.
  **It first returned `DECISION_REQUIRED`, correctly**, escalating two normative
  choices existing authority could not derive; **that result is execution history and
  is not rewritten.** **The Human Maintainer answered both on 2026-09-06**, and a
  **bounded decision rework** applied them.
  **`WP021-D1` is APPROVED — the Container-Relative Named-Range Foundation**: the
  primary adaptive reference frame is a **declared Adaptation Container**, a
  technology-neutral spatial reference boundary that is **never a CSS container
  query, DOM construct, framework component, device class, viewport identity,
  product, screen type, or Layer-5 pattern**, and that a **root or application
  context may serve** without making **`viewport`, `desktop`, `tablet`, `mobile`,
  `phone` or `monitor`** Core responsive identifiers. The **Core Layer-3 response
  vocabulary is named discrete available-space ranges**, preserving **`RANGE ≠
  BEHAVIOUR`**. **Continuous transformation remains permitted downstream** where
  separately authorized — **`CORE RANGE IDENTITY ≠ DOWNSTREAM RESPONSE BEHAVIOUR`**
  — and it **requires no new `$type` and alters `DEC-S-130` in no way**: the closed
  `color`/`dimension`/`number` profile is **not** the reason, and a governed,
  extendable profile boundary is never a permanent architectural verdict.
  **Fixed-geometry channels — PDF, reports, print, presentations — use their own
  channel geometry** rather than forced responsive-range semantics. And **`SPATIAL
  CONTEXT ≠ THEME RESOLUTION CONTEXT`**, with any composition reserved to
  **CDS-WP-022**, which retains full authority over it.
  It is prepared as **`DEC-S-136` — Adaptive Spatial Context and Named-Range
  Architecture** with
  **[ADR-0006](docs/decisions/ADR-0006-ADAPTIVE_SPATIAL_CONTEXT_AND_NAMED_RANGE_ARCHITECTURE.md)**,
  covering **DEC-S-136 only**. **Both are `PROPOSED / AUTHORIZED FOR INTEGRATION` —
  NOT YET EFFECTIVE**, are **uncommitted executor output**, and become `Accepted`
  and effective **only** at the Human-Maintainer exact integration commit following
  a Fresh Independent Review and Nova adjudication. **`APPROVED PROPOSITION ≠
  EFFECTIVE REPOSITORY DECISION`**, and **`PREPARED ≠ EFFECTIVE`**: the **effective
  registers stay at DEC-S-001 … DEC-S-135 (135) and ADR-0001 … ADR-0005 (5)**, with
  a **prepared target of 136 and 6**.
  **`WP021-D2` is DEFERRED by the Human Maintainer — not rejected**, and it approves
  **no** concrete VF-4 identity: the **VF-4 technical root and Source Set identity
  stay OPEN**, **`sourceSetId` and `sourceRevision` are NONE**, concrete VF-4 range
  identifiers are **0**, and **no Decision and no ADR was created for it** — **no
  `DEC-S-137`, no `ADR-0007`**. **`DEC-S-132`'s root vocabulary stays closed at
  VF-1, VF-2, VF-3, VF-5 and VF-6**, and extending it by implication remains
  prohibited — **silence is recorded as silence.** **VF-4 already exists as an
  artifact family**; a future root decision would **extend machine-readable identity
  coverage to an existing family, never create a sixth one.**
  **No value prerequisite moved.** **VP-3, VP-5, VP-6 and VP-7 remain `UNSATISFIED`
  for every visual family**, **VP-4 remains `UNSATISFIED` for VF-4**, and the
  **Step-9 VP-4 state for VF-1, VF-2, VF-3, VF-5 and VF-6 is unchanged**.
  **`DEC-S-136` decides an architecture, not a topology or a vocabulary.** The live
  **VP-7 justification** was corrected additively — **CDS-WP-021 is authorized but
  is not authorized to select visual values**, so **no work package currently
  authorized to select visual values exists** — while **the VP-7 verdict, the
  normative VP-1 … VP-7 prerequisites, and the dated 2026-08-27 and 2026-09-05
  prerequisite tables are unchanged.** The live **`OD-7` stale assertion** in
  [Work Packages](project-system/WORK_PACKAGES.md) was likewise corrected: **`OD-7`
  is ANSWERED by the effective `DEC-S-135`**, and **CDS-WP-022 remains NOT
  AUTHORIZED**. **`WP021-D1` and `WP021-D2` were execution-report escalation keys,
  not governance identifiers.**
  **It created no visual value, no identifier, no responsive-range name, no VF-4
  technical root, no `sourceSetId`, no `sourceRevision`, no source set, and no token
  source file, manifest, resolver, schema, validator rule, test, fixture, component,
  brand, or Product Profile**; produced and admitted **no** evidence; changed **no**
  maturity; accepted or closed **no** risk; renamed **no** phase; registered **no**
  capability; made **no** claim; and **activated no work package** — **`CDS-WP-020A`
  and CDS-WP-022 … CDS-WP-053 remain `Planned`, not active, and not authorized**,
  and **`DEC-S-135` is unchanged.** **No risk was added** — the risk register stays
  at **98**, with **no `RISK-099`**; **no `DEC-S-137` and no `ADR-0007` exists.** **Visual values 0 · visual source sets 0 · visual Candidate families
  0 · VF-1 … VF-9 `Proposed` · Stable No · claims None · conformance None ·
  publication `Private Development`.** **Point-in-time records were preserved**, not
  rewritten: dated review, decision-entry, ADR-boundary, execution-note and
  event-time changelog statements remain as written. Six findings were recorded in
  the
  [Post-Candidate Development Roadmap](docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md)
  (`F-021-01` … `F-021-06`); the bounded rework **resolved `F-021-01` and the live
  half of `F-021-05`**, **preserved the dated non-normative half of `F-021-05`**,
  and left **`F-021-02`, `F-021-03`, `F-021-04` and `F-021-06` unchanged**. **No new
  finding and no new risk was created.**
  **`EXECUTION COMPLETE ≠ WORK PACKAGE CLOSED` · `REVIEW PASS ≠ INTEGRATION` ·
  `INTEGRATION ≠ CLOSURE`** — the object is **prepared and uncommitted**, becomes
  normative only at the Human-Maintainer exact integration commit, and **closure is
  a separate Human-Maintainer act that has not occurred.**
  (CDS-WP-021)
- **`DEC-S-132 … DEC-S-135` and `ADR-0005` reconciled to their effective state.**
  The condition those entries themselves stated — the Human-Maintainer exact
  integration commit of the exact reviewed Step-9 Working Tree object, following a
  Fresh Independent Review and Nova integration adjudication — was met by commit
  `2cb244e889c1a6b5a278afb233995a0379b5d9ef` (parent
  `6fcf6e4041508ff7c641ed89ec45a0684d4152f4`), so the repository's live
  current-state carriers no longer qualify them as
  `PROPOSED / AUTHORIZED FOR INTEGRATION` or `NOT YET EFFECTIVE`, and no longer
  name **DEC-S-131** and **ADR-0004** as the highest effective entries.
  **DEC-S-132 … DEC-S-135 are effective and ADR-0005 is `Accepted`**; the effective
  registers are **DEC-S-001 … DEC-S-135 (135)** and **ADR-0001 … ADR-0005 (5)**.
  **This records a completed Human-Maintainer act and performs none** — an ADR is
  accepted by the Human-Maintainer commit its own status text bound acceptance to,
  never by an executor. **Point-in-time records were preserved**, not rewritten:
  dated review, evidence, decision-time, and changelog statements that were true
  before integration remain as written, including the Step-9 preparation entry
  below. **No Decision, ADR, or risk was added, changed in substance, or removed** —
  the registers stay at **135**, **5**, and **98**; **no `DEC-S-136`, no
  `ADR-0006`, no `RISK-099`.** **No ADR rationale, alternative, consequence, or
  Decision scope was altered**; no visual value, identifier, role, Source Set,
  token source, schema, validator rule, test, or fixture was created; **no**
  evidence was admitted, **no** maturity changed, **no** claim was made, and **no**
  work package was activated. **OD-5 and OD-6A residuals, VF-1 tonal topology, and
  the concrete role vocabulary stay open; VP-3, VP-5, VP-6 and VP-7 stay
  unsatisfied; visual values and visual source sets stay 0.** **CDS-WP-022 remains
  the recommended and sequenced Step-10 candidate and is not authorized; no work
  package is currently authorized.**
  (CDS Step-9 post-integration effectivity reconciliation)
- **CDS Step-9 Decision Integration Pass — `DEC-S-132 … DEC-S-135` and `ADR-0005`,
  PREPARED and NOT YET EFFECTIVE.** Authorized separately by the Human Maintainer on
  **2026-09-05** after Nova adjudicated the CDS Step-9 R1/R2 decision package. All
  five are prepared as **`PROPOSED / AUTHORIZED FOR INTEGRATION`** and become
  effective **only** at the Human-Maintainer exact integration commit of the exact
  reviewed Working Tree object, following a Fresh Independent Review and Nova
  integration adjudication. **The committed registers remain `DEC-S-131` and
  `ADR-0004` — 131 decisions and 4 ADRs; the prepared target is 135 and 5.**
  **A review PASS is not a commit, and a Nova recommendation is not an approval.**
  (CDS Step-9 Decision Integration Pass)
- **`DEC-S-132` — visual identifier grammar and the two identity spaces.** Visual
  token paths are **family-rooted**: `<family>.<primitive-group>.<step>[.<qualifier>]`
  at Reference and `<family>.<role>[.<qualifier>]` at Semantic. The slot is
  **`qualifier`, not `modifier`** — *conditional modifier* is already bound to
  Resolver / Theme composition semantics, and **N-6** and **T-8** forbid a theme term
  inside a path — and **no concrete qualifier is created**. **The token-flow layer is
  never a path segment**; it stays the schema-validated `layer` field.
  **Token-path identity and Source Set identity are two separate spaces**, and a
  `sourceSetId` is **declared, never derived**. The source-set form is the flat
  **`<layer>/<family>`**, with **no** `visual`, `foundation`, `brand`, `product`,
  `channel`, `context` or `theme` segment. Technical roots: **`color`,
  `typography`, `space`, `shape`, `surface`** — **one per registered family**, so a
  compound display name produces one root and the `<primitive-group>` position
  differentiates internal constructs. The ten identities `reference/color` …
  `semantic/surface` are fixed as **identifier authority only**: **no Source Set
  instance, no `sourceRevision`, no manifest, no resolver, no token, and no file is
  created.** **AL-2 is unchanged**, and **any migration or deprecation compatibility
  mechanism outside the normative Semantic alias graph stays OPEN**. **The OD-3
  concrete-root residual is resolved and OD-4 is answered.**
  (CDS Step-9 Decision Integration Pass)
- **`ADR-0005` — Visual Identifier Grammar and Identity Spaces.** Architecture
  rationale for **DEC-S-132 only**; **DEC-S-133, DEC-S-134 and DEC-S-135 are
  deliberately not architecture dependencies of it**, on the ADR-0004 / DEC-S-129
  precedent. It records why layer-rooted paths, a mechanically derived
  `sourceSetId`, a `visual` namespace prefix, and multiple roots per compound family
  were each rejected. **It is `PROPOSED / AUTHORIZED FOR INTEGRATION` and confers no
  acceptance until the Human-Maintainer integration commit.**
  (CDS Step-9 Decision Integration Pass)
- **`DEC-S-133` — per-scale topology under the common scale contract.** **There is
  no universal cross-family scale base** — **ST-5 is per-scale**, and a shared base
  would create the coupling **AF-3** exists to prevent. **Each ordered primitive set
  independently owns** its anchor declaration, ordering, progression-rule kind,
  step count, extension behaviour, and exclusions, under the **unchanged**
  ST-1 … ST-7 contract. It records **`SCALE TOPOLOGY ≠ SCALE VALUES`** and fixes
  **VP-3's "base" as the anchor declaration, not a numeric magnitude** — under the
  magnitude reading VP-3 would be circular and unsatisfiable. Scope: **VF-2, VF-3,
  VF-5, VF-6**; **opacity remains an attribute** of VF-1 and VF-6 with **no
  standalone opacity family**; **VF-1 tonal topology, VF-4, VF-7, VF-8 and VF-9 are
  excluded**. **It selects no base, ratio, step, or value.** **OD-5 is only
  PARTIALLY answered**: the per-family topology parameters are **not** decided,
  **VF-1 tonal topology is a separate open residual**, and **VP-3 remains
  UNSATISFIED for every family and fails closed.**
  (CDS Step-9 Decision Integration Pass)
- **`DEC-S-134` — visual role admission rule.** **Model B:** an admission rule is
  decided and **the concrete role vocabulary is not**. A role enters CDS Core only
  on demonstrated **cross-consumer** need, classified before design, satisfying
  **SR-1 … SR-12 from the moment it exists**; the **role classification is closed**
  and a future vocabulary populates it and adds none. **`CDS-WP-020A` may not
  invent, adopt, reserve, or recommend a Core role identifier.** **`selected`,
  `active` and `current` are not CDS Core roles today** — answering **IS-5** — which
  is **not a permanent prohibition** and removes no protection, because IS-1 and
  IS-5 already bind whatever a consumer builds. **It creates no role, no role
  identifier, no binding, no extension point, and no value.** **OD-6A is POLICY
  ANSWERED with the concrete vocabulary OPEN, and VP-6 stays UNSATISFIED.**
  (CDS Step-9 Decision Integration Pass)
- **`DEC-S-135` — theme sequencing before context-sensitive value selection.** **No
  semantic visual role carries a default alias to a reference primitive before
  CDS-WP-022 decides the Theme and Context Mechanism**, and **CDS-WP-022 precedes
  context-sensitive value selection**. It gates **values and bindings, not
  structure**: identifier grammar, scale ownership and topology rules, role
  admission policy, family maturity governance, and **source-set structural
  identity** are context-independent by **TC-1**, **TC-2**, **T-8**, **N-6** and
  **RB-1**, and are not blocked — **`CDS-WP-022 BEFORE VALUE SELECTION` does not
  mean `CDS-WP-022 BEFORE EVERY SOURCE-STRUCTURE OR IDENTITY ACTIVITY`.** A theme
  remains a **Resolution Context, not a sixth token-flow layer**, and **A THEME
  RE-BINDS; IT NEVER REDEFINES.** **It authorizes no work package**: CDS-WP-022 is
  the recommended and sequenced Step-10 candidate only, and **SEQUENCED NEXT ≠
  AUTHORIZED**. **OD-7 is answered.**
  (CDS Step-9 Decision Integration Pass)
- **`OD-6B` dispositioned — answered by existing normative authority, with no new
  Decision.** **VF-1 … VF-9 remain separate artifact families**, each with **its own
  maturity, evidence, gate, and compatibility statement**, under **AF-1**, **AF-3**
  and **AF-4**. Administrative batching may occur, but **BATCHED REVIEW ≠ SHARED
  MATURITY** and **BATCHED GATE PREPARATION ≠ MATURITY INHERITANCE**; **one family
  passing grants nothing to another.** **No maturity group, cluster maturity,
  roll-up maturity, inherited maturity, or aggregate gate exists or may be
  created**, and creating a Decision for a rule that already binds would be ceremony
  that produces no decision (**RISK-040**). `F-019-07` and `F-020-08` close with this
  disposition. (CDS Step-9 Decision Integration Pass)
- **`CDS-WP-020A` — Visual Token Source Authoring and Source Set Realization,
  registered as `Planned`, not active, not authorized.** The explicit destination
  for the concrete machine-readable **Visual Token Source and Value Authoring** work
  that CDS-WP-020 returned as `DECISION_REQUIRED`. It resolves **`FR-N-03`**, which
  Nova adjudicated with Human-Maintainer approval — **Option 2: source and value
  authoring is a responsibility separate from validation**, and must not be absorbed
  into **CDS-WP-024**. **An inserted identifier on the existing `CDS-WP-001A`
  precedent: no work package was renumbered**, and the numeric sequence
  CDS-WP-017 … CDS-WP-053 is unchanged. It owns visual source sets, machine-readable
  source authoring at token-flow layers 1 and 2, source-set identity, revision,
  provenance, and family × layer topology — and, only once **OD-4** and **OD-5** are
  decided and **VP-1 … VP-7** are satisfied, identifier realization and concrete
  normative values. It **never** acquires validator implementation, validation
  authority, conformance determination, evidence admission, maturity promotion,
  Product Profile activation, pilot activation, release authority, `Stable`
  declaration, or runtime renderer implementation. **Registration is not
  activation**, and **no visual value, identifier, token source, schema, validator
  rule, test, or fixture was created.** (CDS-WP-020 closure and routing)
- **An *authoring and validation separation* standing gate in the forward roadmap.**
  **AUTHOR is not VALIDATE; SOURCE CREATION is not CONFORMANCE DETERMINATION.** A
  work package that authors machine-readable sources gains **no** validation
  authority because validators read what it wrote, and **CDS-WP-024** gains **no**
  authoring authority because it validates what someone else wrote. This is a
  responsibility boundary, not a runtime-dependency mandate; it derives from
  DEC-S-022, DEC-S-031, DEC-S-053, DEC-S-079, and DEC-S-126 and **registers no new
  Decision and no new ADR.** (CDS-WP-020 closure and routing)
- **Two findings recorded and routed, not repaired.** **`F-020C-01`** — **74**
  live assertions across **21** files still qualify **DEC-S-128 … DEC-S-131**
  and **ADR-0004** as `NOT YET EFFECTIVE` *"until the Human-Maintainer exact-byte
  integration commit"*, a condition met by commit
  `42a568d823de3388e45af62967546f13ad67eff6`; deferred to a **separately authorized
  effectivity reconciliation pass**, on the CDS-WP-016 post-promotion precedent,
  because the volume exceeds a bounded closure pass and **marking an ADR `Accepted`
  is a Human-Maintainer act**. **`F-020C-01` has since been resolved** by that
  separately authorized pass; **`F-020C-02` remains deferred.** **`F-020C-02`** — the **M2** milestone mapping was
  **not** re-derived, because doing so would decide sequencing while **OD-7** is
  open. (CDS-WP-020 closure and routing)
- **CDS-WP-020 Decision Integration Pass — `DEC-S-128 … DEC-S-131` and `ADR-0004`.**
  Separately authorized by the Human Maintainer on **2026-08-27** after Nova
  adjudicated **OD-1 … OD-7**. All five were prepared as
  **`PROPOSED / AUTHORIZED FOR INTEGRATION`** and became effective **only** at the
  Human-Maintainer exact-byte integration commit
  `42a568d823de3388e45af62967546f13ad67eff6`, which followed a Fresh Independent
  Review and Nova integration adjudication. The **effective** registers are
  therefore **DEC-S-131** and **ADR-0004**, holding **131** decisions and **4**
  ADRs. **A review PASS is not a commit, and a Nova recommendation is not an
  approval.** (CDS-WP-020)
- **`DEC-S-128` — exactly one canonical normative visual colour representation.**
  The pinned DTCG 2025.10 colour space keyed **`srgb`**, with components as that
  report defines them — **no 8-bit-only or `n/255` restriction**. **OKLCH is a
  derivation and design-analysis space only**: not a source space, not a second
  canonical representation, not authority for a value, and not an evidence carrier;
  a derivation result is recorded as the canonical value with the derivation kept as
  **provenance**. Delivery quantization belongs to the channel and generated-output
  boundary and **never rewrites a source value**; an out-of-model source value
  **fails closed**. `alpha` remains part of the colour value, **no standalone opacity
  family** is introduced, and **`hex` gains no new authority and no new
  prohibition** — it may never become a second source of truth, and its CDS-specific
  disposition stays deferred. **No colour value, palette, hue, or scale is
  selected.** (CDS-WP-020)
- **`DEC-S-129` — WCAG 2.2 is the contrast evaluation authority, and precision is
  not negotiable.** **Not `WCAG 2.x`, not `latest`** — a floating version is not an
  identity. The method is the one the cited criteria themselves require; **CDS
  restates no threshold and invents none.** Pass and fail are compared at **full
  available precision with no rounding before comparison**, and presentation
  rounding cannot alter the outcome. **APCA and other methods may be calculated and
  recorded as informational or experimental analysis only** — **calculation is not
  adoption**, and such a method satisfies no CDS obligation and supports no claim
  merely by being computed. **An automated contrast calculation is not accessibility
  evidence and grants no AE level**, and **no contrast was evaluated** — there is
  nothing to evaluate. (CDS-WP-020)
- **`DEC-S-130` — an explicit, minimal, closed `$type` admission profile.** Exactly
  **`color`**, **`dimension`** and **`number`**, each verified **directly against the
  final DTCG 2025.10 Format Module** (Final Community Group Report, 28 October 2025).
  **DTCG-defined is not CDS-admitted.** Every normative visual token carries its
  **own** explicit `$type`; **group and root typing are not typing authority** (a CDS
  profile restriction that does **not** redefine DTCG); **no composite type is
  admitted**, and font-family / font-weight identity is **not** admitted prematurely.
  **`$type` carries value-type semantics only** — never maturity, evidence, approval,
  lifecycle, authority, publication, or conformance. It is identity- and
  digest-affecting, and **evidence never transfers over that revision change**.
  **`profileVersion` stays `1`**, and **no schema, validator, test, or fixture was
  changed** — the validator's bounded V2 type set remains a **DEC-S-098 coverage
  boundary, not an admission** (RISK-074). (CDS-WP-020)
- **`DEC-S-131` — the Source Set is the independently evaluable unit, and
  aggregation confers nothing.** One source set per **Family × Token-Flow-Layer**,
  each carrying its own `sourceSetId`, `sourceRevision`, `layer`, dependencies,
  `maturityState` and `approvalState`. **Maturity binds to
  (`sourceSetId`, `sourceRevision`)** and to nothing else; a new revision inherits
  **no** evidence. **One manifest may aggregate many source sets** — **a source set
  is not a manifest** — and a manifest's own maturity describes **only the manifest
  artifact**: not a roll-up, not a maximum, not a minimum, not inherited.
  **AGGREGATED is not MATURE.** A rename is a migration and identity event; **a file
  move is not**; a `sourceSetId` change **invalidates admitted evidence**.
  (CDS-WP-020)
- **`ADR-0004` — Visual Token Representation and Source Identity Architecture.**
  Records why `srgb` is canonical (the contrast obligation stays computable from the
  source with **no conversion inside the normative path**, and the registered print,
  export and greyscale channels are served without gamut mapping), why OKLCH is
  derivational (a second canonical representation would manufacture the
  normative-source conflict DEC-S-034 resolves by **invalidating the artifact
  state**), why the admitted type set is closed and minimal (a composite cannot
  carry a **per-part** obligation under SR-3 … SR-5), why **`profileVersion` stays
  `1`**, why source sets rather than manifests carry independent maturity, and why
  aggregation confers no maturity — plus alternatives, consequences, compatibility,
  and four implementation obligations handed to **CDS-WP-024**. **DEC-S-129 is
  deliberately not an architecture dependency of it.** (CDS-WP-020)
- **`F-020-02` corrected precisely — conclusion upheld, mechanism corrected.** A
  source-set payload does carry **one** `maturityState`, so a shared visual source
  set cannot express the per-family, never-inherited maturity **AF-1** and **AF-3**
  require; that conclusion stands. Its **artifact-count mechanism was imprecise**:
  it implied that per-family, per-layer source sets multiply manifests and resolvers
  at the same rate. The committed manifest contract carries a **`sourceSets`
  array**, so **one manifest may aggregate many source sets**, each retaining its own
  maturity — the governance cost of preserving AF-1 and AF-3 is smaller than the
  finding assumed, and the argument for collapsing independent maturities loses its
  cost basis. (CDS-WP-020)
- **`OD-1`, `OD-2` and `OD-3` answered; `OD-4` … `OD-7` deliberately left open**,
  with three residuals recorded rather than silently deferred: the CDS-specific
  disposition of the optional DTCG **`hex`** member, the representation of
  **font-family and font-weight identity** (with composite-type admission), and the
  **concrete visual source-set root identifiers**. **VP-2 is now satisfied** for the
  families expressible in `color`, `dimension` and `number`; **VP-3, VP-4 and VP-5
  remain unsatisfied for every family**, so **no visual value may be selected.**
  **Four Decisions do not complete the value system.** (CDS-WP-020)
- **CDS-WP-020 — Reference and Semantic Token Foundation: the contract for
  token-flow layers 1 and 2 of the visual foundation.** Three normative documents —
  the [Visual Reference Token Foundation](docs/architecture/VISUAL_REFERENCE_TOKEN_FOUNDATION.md),
  the [Visual Semantic Token Foundation](docs/architecture/VISUAL_SEMANTIC_TOKEN_FOUNDATION.md),
  and the [Visual Token Value Selection Rules](docs/governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
  — plus one **non-normative**
  [open-decision register](docs/roadmap/VISUAL_TOKEN_FOUNDATION_OPEN_DECISIONS.md).
  **They select no value and create no identifier.** (CDS-WP-020)
- **The Reference layer, defined as a restriction.** *A reference token is a value
  without a purpose.* Ten obligations (RP-1 … RP-10), seven requirements on any
  future scale (ST-1 … ST-7), nine reference naming rules (RN-1 … RN-9), five
  provenance and lifecycle rules (RV-1 … RV-5), five theme and Product Profile
  boundary rules (RB-1 … RB-5), and ten validation requirements handed to
  CDS-WP-024. Five families hold reference constructs (VF-1, VF-2, VF-3, VF-5,
  VF-6); **VF-4, VF-7, VF-8, and VF-9 deliberately hold none**, and the exclusion is
  stated so absence is not read as oversight. (CDS-WP-020)
- **A reference token cannot be accessible — stated normatively.** Accessibility is
  a property of a **pair, a composition, and a context**, none of which exists at
  token-flow layer 1. A colour primitive has no contrast ratio. Recording an
  obligation on a primitive would put it where nothing can check it and where a
  theme could silently move it — the failure **VF-I-8** exists to prevent.
  (CDS-WP-020)
- **The Semantic layer, and the twelve obligations that bind every role.**
  *A semantic role is a named purpose that resolves to a value it does not own.*
  SR-1 … SR-12 consolidate the CDS-WP-019 family obligations (CR-1 … CR-6,
  TR-1 … TR-6, SP-1 … SP-5, SH-1 … SH-5) without adding one. **A role that does not
  declare its contrast obligation and its pairings must not exist**, and declaring
  *"this role conveys nothing"* is a real answer where a blank is not. Adds the
  semantic naming rules (SN-1 … SN-9), channel and product neutrality
  (PN-1 … PN-5), the Semantic Status boundary (SS-1 … SS-8), the **focus role set**,
  component-independent state constraints (IS-1 … IS-5), and fifteen validation
  requirements. (CDS-WP-020)
- **The alias model (AL-1 … AL-8), and the rule that keeps the layers honest.**
  **An alias transports a value, never an obligation** (AL-7): a role's contrast
  obligation, pairing set, and non-visual carrier are properties of the **role**,
  never inherited from or delegated to the primitive it resolves to — otherwise a
  theme could satisfy an accessibility obligation by re-binding. A role never holds
  a raw literal (AL-1), never aliases another role (AL-2), and an unresolved alias
  **fails closed** (AL-4). (CDS-WP-020)
- **Seven theme-compatibility requirements (TC-1 … TC-7) that keep CDS-WP-022
  free.** Including **TC-6**: the semantic layer presupposes no context count and no
  context set — *a role model that only works if exactly two contexts exist has
  decided CDS-WP-022's question by implication.* (CDS-WP-020)
- **The value-selection discipline.** *No visual value enters CDS without a
  recorded reason that someone else can disagree with.* Seven prerequisites
  (VP-1 … VP-7 — **none of VP-2 … VP-5 held for any family at that milestone**;
  VP-2 was satisfied later, by DEC-S-128 and DEC-S-130), a
  twelve-criterion evaluation (VE-1 … VE-12), **ten inadmissible grounds**
  (IG-1 … IG-10: taste, imitation, a consumer asking, a tool default, a generated
  artifact, an example or fixture, a validator pass, prior existence, schedule
  pressure, and making a failing check pass), the eight-field value record
  (VD-1 … VD-8), ten accessibility constraints (VA-1 … VA-10), and the validation
  strategy (VS-1 … VS-6). (CDS-WP-020)
- **`OD-1 … OD-7` — the open decisions that gate every visual value**, recorded
  **non-normatively** with proposition, alternatives, recommendation, affected
  files, and governance track: the **colour space and encoding**, the **admitted
  DTCG `$type` set**, the **visual source-set identity, granularity and topology**,
  the **concrete identifier grammar**, **scale topology** for the dimensional
  families, the **role vocabulary and how many families CDS matures separately**,
  and the **sequencing against CDS-WP-022**. The register also records the items
  that are deliberately *not* open decisions — the typeface (already governed by
  FP-1 … FP-8 and deferred), the theme mechanism, the responsive model, the
  status-to-visual binding, extension points, motion, icons, data visualization, and
  the transformation tool. (CDS-WP-020)
- **Eight CDS-WP-020 findings recorded in the forward roadmap** (`F-020-01` …
  `F-020-08`), including the **AF-1 / AF-3 versus source-set-metadata tension**
  (one `maturityState` per source set against per-family maturity that is never
  inherited), the observation that **T-2 is vacuously satisfiable** while zero
  contexts are supported, and that **`F-019-04` is incomplete** — question 4 of the
  Token and Theme Architecture is stale in the same way questions 1, 2, and 7 are.
  **Recording a finding repairs nothing and authorizes nothing.** (CDS-WP-020)
- **DEC-S-127 — the project phase becomes `Post-Candidate Foundation &
  Design-System Enablement`.** The phase established by **DEC-S-062** completed its
  intended operating purpose: its four prerequisites are committed, and the first
  Candidate transition completed on 2026-08-19. DEC-S-127 supersedes it **for
  current and future state only** and takes effect at its **Human-Maintainer
  integration commit**. **DEC-S-062 is not deleted, withdrawn, or retroactively
  invalidated** — it keeps `Status: Accepted` and remains correct for the period it
  governed. The register moves to **127 decisions, highest `DEC-S-127`**; **no risk
  and no ADR was added** — **RISK-098** and **ADR-0003** are unchanged.
  (CDS Phase Transition Governance Package)
- **The new phase is defined narrowly, and bounded explicitly.** It covers the
  period in which CDS develops and validates the shared design-system foundation
  **after the first Candidate family exists** — admitting work classes such as
  concrete visual foundation development, visual token architecture, semantic-visual
  binding, foundation maturity progression, component and pattern preparation, and
  accessibility evidence preparation. It is explicitly **not** Stable, release,
  publication, production rollout, consumer adoption, Product Profile activation,
  full component maturity, or ecosystem deployment. **No successor phase is named**
  — that would require its own Decision, and it is deferred.
  (CDS Phase Transition Governance Package)

### Changed

- **The Open Decisions register, the value-prerequisite state, and the live
  current-state carriers reconciled to the prepared Step-9 decisions.** The
  **non-normative** register now records **OD-4** and **OD-7** as answered, **OD-5**
  as **partially** answered, **OD-6A** as policy-answered with the vocabulary open,
  and **OD-6B** as answered by existing normative authority — each **conditional on
  the Human-Maintainer integration commit** — together with a **residual register**
  carrying nine entries, one of them new. The
  [Visual Token Value Selection Rules](docs/governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
  gain a **second, additive** prerequisite-state subsection: **VP-4 satisfied for
  VF-1, VF-2, VF-3, VF-5 and VF-6**, **VP-3, VP-5, VP-6 and VP-7 UNSATISFIED**, VP-2
  unchanged. **VP-3 fails closed and is not reported as satisfied** — the ownership
  model is decided, the per-family topology parameters are not. **The 2026-08-27
  prerequisite table is preserved**, not rewritten, as the record of the period it
  governed, and **VP-1 … VP-7 themselves are unchanged**. **Point-in-time records
  were preserved**: dated decision entries, execution notes, preparation records,
  and event-time changelog statements remain as written, including the OD-5
  recommendation that was **rejected** and the OD-6B family-count recommendation
  that was **rejected**. **N-6's principle is unchanged** — only the slot term is
  reconciled from *modifier* to **`qualifier`**. **No maturity changed, no evidence
  was admitted, no risk was added, no value was selected, no identifier instance or
  Source Set was created, and no work package was activated.**
  (CDS Step-9 Decision Integration Pass)
- **CDS-WP-020 closure recorded as effective — `F-020C-04` resolved.** The condition
  the closure and routing pass stated — a separate Human-Maintainer integration
  commit of its working object — was met by commit
  `3f37ecfe54dad82f8064aaff521ff9e3aec65fd7` (parent
  `42a568d823de3388e45af62967546f13ad67eff6`), whose exact object passed the
  **CDS-WP-020 EXACT-OBJECT CLOSURE INTEGRATION GATE R4**. The live current-state
  carriers no longer describe that closure as *proposed*, *pending*, or *not yet
  effective*: **CDS-WP-020 is `Closed`, effective at that commit**, and **no work
  package is currently authorized**. **This records a completed Human-Maintainer act
  and performs none.** **Point-in-time records were preserved**, not rewritten:
  dated review, execution, decision-time, and event-time changelog statements that
  were true before that commit remain as written. **`DECISION_REQUIRED` stands as
  the executed result** — closure answers **no** open decision, satisfies **no**
  value prerequisite, and selects **no** value. **No work package was activated** —
  **`CDS-WP-020A`** and **CDS-WP-021 … CDS-WP-053** all remain `Planned`, not
  active, not authorized. **OD-4, OD-5, OD-6 and OD-7 stay open**; **VP-3, VP-4 and
  VP-5 stay unsatisfied**; visual values **0**, visual source sets **0**, visual
  Candidate families **0**, VF-1 … VF-9 **`Proposed`**. **No Decision, ADR, or risk
  was added, changed, or removed** — the registers stay at **131**, **4**, and
  **98**; **no `DEC-S-132`, no `ADR-0005`, no `RISK-099`.** **No evidence was
  admitted, no maturity changed, no claim was made, no capability was registered, no
  phase was renamed, and no release, tag, or publication occurred.**
  (CDS-WP-020 post-closure current-state reconciliation)
- **`DEC-S-128 … DEC-S-131` and `ADR-0004` reconciled to their effective state, and
  `F-020C-01` resolved.** The condition those entries themselves stated — the
  Human-Maintainer exact-byte integration commit of the CDS-WP-020 Decision
  Integration Pass — was met by commit
  `42a568d823de3388e45af62967546f13ad67eff6`, so the repository's live current-state
  carriers no longer qualify them as `PROPOSED / AUTHORIZED FOR INTEGRATION` or
  `NOT YET EFFECTIVE`, and no longer name **DEC-S-127** and **ADR-0003** as the
  highest effective entries. **DEC-S-128 … DEC-S-131 are effective and ADR-0004 is
  `Accepted`**; the effective registers are **DEC-S-001 … DEC-S-131 (131)** and
  **ADR-0001 … ADR-0004 (4)**. **This records a completed Human-Maintainer act and
  performs none** — an ADR is accepted by the Human-Maintainer commit its own status
  text bound acceptance to, never by an executor. **Point-in-time records were
  preserved**, not rewritten: dated review, evidence, decision-time, and changelog
  statements that were true before integration remain as written. **No Decision,
  ADR, or risk was added, changed in substance, or removed** — the registers stay at
  **131**, **4**, and **98**; **no `DEC-S-132`, no `ADR-0005`, no `RISK-099`.** **No
  ADR rationale, alternative, consequence, or Decision scope was altered**; no
  visual value, identifier, token source, schema, validator rule, test, or fixture
  was created; **no** evidence was admitted, **no** maturity changed, **no** claim
  was made, and **no** work package was activated. **CDS-WP-020 closure remains
  proposed and not yet effective** — a separate Human-Maintainer integration commit.
  (CDS-WP-020 post-integration effectiveness reconciliation)
- **CDS-WP-020 recorded as `Completed` — executed with result `DECISION_REQUIRED`,
  integrated, closure proposed.** Its reviewed object — **22 paths** — was
  integrated by the Human-Maintainer commit
  `42a568d823de3388e45af62967546f13ad67eff6`. `project-system/WORK_PACKAGES.md`,
  `project-system/NEXT_PHASE.md`, `project-system/PROJECT_PROFILE.md`,
  `project-system/CONTEXT_PACK_FOUNDATION.md`, `project-brain/PROJECT_BRAIN.md`,
  `README.md`, `CLAUDE.md`, and the forward roadmap now record it as closed.
  **Closure is recorded in the working object of the closure and routing pass and
  becomes effective only at that object's Human-Maintainer integration commit** — an
  uncommitted edit changes no repository history. **`DECISION_REQUIRED` stands as
  the executed result**: closure answers **no** open decision, satisfies **no**
  value prerequisite, and selects **no** value. **OD-4, OD-5, OD-6 and OD-7 stay
  open**; **VP-3, VP-4 and VP-5 stay unsatisfied**; visual values **0**, visual
  source sets **0**, visual Candidate families **0**, VF-1 … VF-9 **`Proposed`**.
  **No successor work package was activated** — **`CDS-WP-020A`** and
  **CDS-WP-021 … CDS-WP-053** all remain `Planned`, not active, not authorized.
  **No Decision, ADR, or risk was added**; the registers stay at **131**, **4**, and
  **98**. **No evidence was admitted, no maturity changed, no claim was made, no
  capability was registered, no phase was renamed, and no release, tag, or
  publication occurred.** (CDS-WP-020 closure and routing)
- **CDS-WP-020 previously recorded as the current authorized work package —
  executed, `DECISION_REQUIRED`, not closed.** `project-system/WORK_PACKAGES.md`,
  `project-system/NEXT_PHASE.md`, `project-system/PROJECT_PROFILE.md`,
  `project-system/CONTEXT_PACK_FOUNDATION.md`, `project-brain/PROJECT_BRAIN.md`,
  `README.md`, `CLAUDE.md`, and the forward roadmap now record it, and
  **CDS-WP-021 … CDS-WP-053** as `Planned`, not active, not authorized. Its
  authorization came from a **separate Human-Maintainer decision** on 2026-08-26,
  **not** from its roadmap position — and **not** from the DEC-S-127 phase
  transition, which granted no authority. **Closure is a separate Human-Maintainer
  act and has not occurred.** (CDS-WP-020)
- **Two stale current-state statements corrected.** `WORK_PACKAGES.md` still
  described CDS-WP-019 as *"Next — the current authorized work package"* and
  `PROJECT_BRAIN.md` still carried `CDS-WP-019: Active`, although both files' own
  headers and tables already recorded it as `Completed` and closed by commit
  `538fbccbf6f554de3b872e9fb75a70d13318feb6`. This is the recurrence `R1-F-01` and
  `F-019-09` describe: a work-package-status row goes stale at the next activation.
  (CDS-WP-020)
- **The Visual Foundation Architecture gained four *Related documents* rows** —
  additive only. **No other CDS-WP-019 document was modified**, and no CDS-WP-005
  document was touched: `F-020-05` (the stale alias question in the Token and Theme
  Architecture) is **routed, not repaired**. (CDS-WP-020)
- **Nothing else changed, and the negative state is the point.** CDS-WP-020 touched
  no `tokens/**`, `schemas/**`, `tools/**`, `tests/**`, `artifacts/**`,
  `docs/foundations/**`, `docs/decisions/**`, or `docs/risks/**`. **No visual value,
  no identifier, no token source file, manifest, resolver, schema, validator rule,
  diagnostic, test, or fixture** was created; **no test expectation was weakened and
  no fixture rewritten**; **no evidence** was produced or admitted; **no maturity**
  changed — all nine visual families stay `Proposed`, visual source sets stay **0**,
  visual Candidate families stay **0**, Stable stays **0**; **no risk** was accepted,
  closed, or re-scored; **no phase** was renamed; **no capability** was registered;
  **no claim, Product Profile, extension point, pilot, consumer integration,
  release, tag, or publication** was created or activated; **CR-004's registered
  Layer-5 mapping is unchanged**; and **no Semantic Status source, revision,
  maturity, approval, or evidence package** was touched —
  **`AE1-CDS-WP016-SEMSTATUS-004` was not transferred to anything.** At that
  milestone the Decision register stayed at **127**, the ADR range at
  **ADR-0001 … ADR-0003**, and the Risk Register at **98**: **DEC-S-128 and ADR-0004
  were recommended and not created**, and a new risk entry was **not** recommended.
  *(Superseded for current state by the 2026-08-27 Decision Integration Pass above,
  which prepared DEC-S-128 … DEC-S-131 and ADR-0004 under a separate Human-Maintainer
  authorization. **The Risk Register stays at 98** — `RISK-099` was assessed and is
  not required.)* **No Git write was performed.** (CDS-WP-020)
- **Phase carriers reconciled, historical carriers preserved.** The maintained
  current-phase statements in `README.md`, `CLAUDE.md`,
  `project-system/PROJECT_PROFILE.md`, `project-system/NEXT_PHASE.md`,
  `project-system/WORK_PACKAGES.md`, `project-system/CONTEXT_PACK_FOUNDATION.md`,
  `project-brain/PROJECT_BRAIN.md`, the `docs/risks/RISK_REGISTER.md` scope header,
  and the forward roadmap now read the new label. **Dated records were not
  rewritten** — the [Foundation Closure Record](docs/governance/FOUNDATION_CLOSURE_RECORD.md),
  the historical CDS-WP-009 [Pre-Candidate Operating Plan](docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md),
  prior review reports, prior work-package notes, DEC-S-062 itself, and historical
  changelog entries still name `Pre-Candidate Operating Enablement` and are
  **correct as written**. **Historical state is not current state.**
  (CDS Phase Transition Governance Package)
- **CDS-WP-019 recorded as `Completed`.** Its closure became effective with the
  Human-Maintainer commit `538fbccbf6f554de3b872e9fb75a70d13318feb6`, which
  integrated the eleven normative visual foundation documents — the repository's own
  rule that closure "becomes committed and effective" at the integration commit.
  **No numbered work package is currently active**, and **CDS-WP-020 … CDS-WP-053
  remain `Planned`, not active, and not authorized**.
  (CDS Phase Transition Governance Package)
- **`F-017-04` phase-label governance portion CLOSED, and `F-019-08`
  (`PHASE_TRANSITION_RECOMMENDED`) CLOSED / SATISFIED** by DEC-S-127, recorded as
  **additive dated status notes** in the forward roadmap. The dated CDS-WP-017 and
  CDS-WP-019 findings tables were **not rewritten**, and `F-017-03` remains open as
  a future **Elevated** scope / capability-registration gate.
  (CDS Phase Transition Governance Package)
- **The transition changed governance state only.** **No** maturity changed: the
  `semantic/status` family stays at `semantic-status-rev-0002-candidate`,
  **`Candidate`**, **`Approved`**, with **`AE1-CDS-WP016-SEMSTATUS-004`** at
  **AE-1** for the channel-independent source/contract family only, and the nine
  visual foundation families **VF-1 … VF-9 stay `Proposed`** with **zero** Candidate
  visual families. **No** evidence was produced, admitted, altered, or transferred —
  **evidence does not transfer because of a phase change**. Nothing under `tokens/`,
  `schemas/`, `tools/`, `tests/`, `artifacts/`, or `docs/foundations/` was touched,
  and the eleven CDS-WP-019 visual foundation documents are **unchanged**. **No**
  capability was registered, **no** claim was made, **no** artifact reached
  `Stable`, **no** Product Profile or pilot was activated, publication remains
  **`Private Development`**, there are **0 tags and no release**, and **no Git write
  was performed**. (CDS Phase Transition Governance Package)

### Added

- **Core Visual Foundation Architecture — the Layer-3 visual foundation now has a
  structure, and still no values.** Eleven new normative documents establish **how**
  visual foundations are structured, governed, represented, extended, validated, and
  consumed. **No colour, typeface, size, spacing, radius, stroke, shadow, opacity
  value, icon, illustration, motion value, breakpoint, or theme instance is
  selected**, and no token source file, schema, validator rule, component, brand, or
  Product Profile is created. (CDS-WP-019)
  - [Visual Foundation Architecture](docs/architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
    — the entry point: position in the eight-layer model and the five-layer token
    flow, a register of **nine visual foundation families** (VF-1 … VF-9),
    **fourteen invariants** (VF-I-1 … VF-I-14), the naming model, the
    machine-readable representation boundary, the motion boundary, the Semantic
    Status relationship, and the deferred decisions.
  - Six specialised architectures:
    [Colour](docs/architecture/VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md),
    [Typography](docs/architecture/VISUAL_FOUNDATION_TYPOGRAPHY_ARCHITECTURE.md),
    [Spatial](docs/architecture/VISUAL_FOUNDATION_SPATIAL_ARCHITECTURE.md),
    [Shape and Surface](docs/architecture/VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md),
    [Iconography and Imagery](docs/architecture/VISUAL_FOUNDATION_ICONOGRAPHY_AND_IMAGERY_ARCHITECTURE.md),
    and [Theme](docs/architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md).
  - Four governance documents:
    [Accessibility Mapping](docs/governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md),
    [Channel Mapping](docs/governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md),
    [Brand and Product Profile Boundary](docs/governance/VISUAL_FOUNDATION_BRAND_AND_PROFILE_BOUNDARY.md),
    and [Governance and Lifecycle](docs/governance/VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md).
- **The visual foundation introduces no layer.** Visual constructs occupy positions
  in the existing eight-layer model (DEC-S-021) and the existing five-layer token
  flow (DEC-S-024). A **theme is a resolution context, not a layer**; a Product
  Profile enters at token-flow layer 4 only; and the **Component layer is never
  dropped** from the flow. (CDS-WP-019)
- **Three subjects positioned rather than registered as new scope** — the
  conservative reading in each case: **opacity** is an attribute of Colour (alpha)
  and Surface (overlay, scrim); **illustration and imagery** are **Layer 2 Brand and
  Identity**, consumed through a declared interface; and **focus indication** is a
  **cross-family role set**, so no single family's change can weaken it unnoticed.
  (CDS-WP-019)
- **The status boundary made explicit for visual work:** **COLOUR ≠ STATUS · ICON ≠
  STATUS · MOTION ≠ STATUS · ELEVATION ≠ STATUS**, and **an interaction state is not
  a semantic status**. Status meaning stays with the Semantic Status Foundation;
  visual encoding is redundant to it, never a substitute. The binding itself is
  **CDS-WP-023's**, gated by CDS-WP-024 and CDS-WP-025. **No status-to-visual mapping
  is defined or proposed.** (CDS-WP-019)
- **The accessibility finding, derived by re-counting the WCAG matrix:** **14**
  WCAG 2.2 A/AA criteria map to Layer 3, and **all five** criteria the matrix
  classifies as `Normative CDS requirement` — the ones CDS owns **without** the
  consumer — are among them (**1.3.3, 1.4.1, 1.4.5, 2.3.1, 2.4.7**). **Every
  criterion CDS owns alone is a visual foundation criterion.** Every visual artifact
  is **AE-0**; nothing has been evaluated; **no accessibility claim of any level is
  valid**; `AE1-CDS-WP016-SEMSTATUS-004` does **not** transfer. (CDS-WP-019)
- **The consumer-evidence honesty record.** **No registered consumer requirement
  asks for a colour palette, a typographic scale, a spacing scale, a radius scale, an
  elevation model, an icon library, or illustration.** Six requirements anchor
  Layer 3 (CR-002, CR-006, CR-021, CR-022, CR-023, CR-025), and four families
  (**VF-3, VF-5, VF-6, VF-7**) carry **no consumer demand evidence at all** —
  recorded, in the same way CDS-WP-005 recorded CR-030. (CDS-WP-019)
- **Work-package notes for CDS-WP-019**
  (`project-brain/CDS_WP_019_CORE_VISUAL_FOUNDATION_ARCHITECTURE_NOTES.md`) — the
  discovery record, the decision-need assessment, the positioning rationale, the
  findings **F-019-01 … F-019-09**, and what was explicitly not done. (CDS-WP-019)
- **Python repository hygiene added to `.gitignore`** — `__pycache__/` and `*.pyc`,
  so an offline validator or `unittest` run cannot leave untracked bytecode in a
  working tree whose cleanliness the DEC-S-126 exact-byte evidence workflow depends
  on. No runtime, build, or validation semantics change. (CDS-WP-018)
- **Additive, dated work-package status notes** added to the
  [Candidate Promotion Effectivity Record](docs/governance/SEMANTIC_STATUS_CANDIDATE_PROMOTION_EFFECTIVITY_RECORD.md)
  and the [Candidate Dossier](docs/operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md),
  recording that the `CDS-WP-017: INACTIVE` row each of them carries is historical
  and that work-package status is carried by
  [Work Packages](project-system/WORK_PACKAGES.md), not by a maturity-boundary
  table. **Neither dated table was rewritten**, and neither note is evidence, an
  admission, an approval, or a promotion. (CDS-WP-018, finding `R1-F-01`)
- **Work-package notes for CDS-WP-018**
  (`project-brain/CDS_WP_018_DEFERRED_GOVERNANCE_HYGIENE_NOTES.md`) — the finding
  classification, the repairs performed, and the items explicitly not repaired.
  (CDS-WP-018)

### Fixed

- **Stale `pending Human-Maintainer commit` current-state statements corrected**
  for artifacts the repository history shows as committed: the six
  `docs/architecture/**` machine-readable status headers (ADR-0001 `a81772c`,
  ADR-0002 `1ad9787`), the `CLAUDE.md` project-context bullets, the
  `project-system/PROJECT_PROFILE.md` ADR-0001/0002/0003 status lines, and two
  research status headers. **Per-work-package history sections and tables keep the
  `(pending commit)` convention** — they record each work package's state as of its
  own completion and are historical by construction. (CDS-WP-018, finding
  `NF-R4-OBS-001`)
- **`PROJECT_BRAIN.md` risk-status mirror synchronized** with the normative
  [Risk Register](docs/risks/RISK_REGISTER.md): RISK-066, RISK-067, RISK-068,
  RISK-069, and RISK-071 now read `Mitigating` in the mirror, matching the register
  and the narrative directly beneath the table. **No risk was accepted, closed, or
  reclassified** — only the mirror was corrected. (CDS-WP-018, finding
  `NF-R3-OBS-001`)
- **Validator maturity/approval wording made current-state precise** in the
  [Offline Token Validator Architecture](docs/architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md):
  `Experimental` / `Unapproved` is the default for an **unpromoted** source, not
  "the committed default", since `semantic/status` has declared
  `Candidate` / `Approved` since the Promotion Commit. **No state-machine arm and no
  validator behaviour changed.** (CDS-WP-018, finding `NF-R5R-OBS-001`)
- **Already-decided areas removed from the "intentionally open decision areas"
  lists** in `README.md`, `project-system/PROJECT_PROFILE.md`,
  `project-system/CONTEXT_PACK_FOUNDATION.md`, and `project-brain/PROJECT_BRAIN.md`:
  **token format** (CDS-WP-011, ADR-0001), **versioning and maturity model**
  (DEC-S-035…040), **conformance and adoption policy** (DEC-S-044), and **Product
  Profile and override governance** (DEC-S-042, DEC-S-043). Each is recorded with
  the decision and normative source that closed it. **A decided model is not an
  applied one** — no Product Profile is activated, no claim is valid, no artifact is
  `Stable`, and no version has been released. The **token build system** stays open.
  (CDS-WP-018, findings `F-017-01`, `F-017-02`)
- **Research baseline status wording corrected** in
  [Accessibility Baseline Selection Rationale](docs/research/ACCESSIBILITY_BASELINE_SELECTION_RATIONALE.md)
  — A11Y-BL-001 is committed (`abe84b6`), not awaiting commit — with the
  baseline-is-not-evidence and source-decay boundaries restated. The
  [Source Register](docs/research/ACCESSIBILITY_BASELINE_SOURCE_REGISTER.md) needed
  **no change**: its dated snapshots and decay markers were already correct. **No
  research evidence became normative and no accessibility claim was made.**
  (CDS-WP-018, finding `R3R-003`)
- **UTF-8 BOM removed** from `.gitattributes` and `.gitignore` — the only two
  BOM-carrying tracked files in the repository. Byte-verified: three bytes removed
  from each file and no other content change; the LF-only line-ending policy is
  preserved. (CDS-WP-018, findings `NF-R4-OBS-002`, `NF-R5R-OBS-003`)
- **Self-referentially imprecise deferred-finding wording corrected** in the
  [Post-Candidate Development Roadmap](docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md)
  and this changelog: the identifiers had no **pre-existing** repository occurrence,
  the routing itself is why they appear here, and the finding text is still held
  outside the repository. **Routing is not repair.** (CDS-WP-018, finding `R2-N-01`)
- **The `F-017-04` disclosure completed** with the stale forward "next work package"
  references it governs — `CLAUDE.md` naming CDS-WP-010, the historical
  Pre-Candidate Operating Plan naming CDS-WP-011, and the Foundation Closure Record
  naming CDS-WP-010. The dependent `CLAUDE.md` operating text was reconciled and the
  historical carriers were framed as historical. **The phase label set by DEC-S-062
  was not renamed, no superseding Decision was created, and `DECISION_INDEX.md` was
  not modified.** (CDS-WP-018, finding `R2-N-02`)

### Changed

- **CDS-WP-018 recorded as `Completed`** and **CDS-WP-019 recorded as the active
  work package** across the current-state surfaces (`README.md`, `CLAUDE.md`,
  `project-system/WORK_PACKAGES.md`, `project-system/NEXT_PHASE.md`,
  `project-system/PROJECT_PROFILE.md`,
  `project-system/CONTEXT_PACK_FOUNDATION.md`, `project-brain/PROJECT_BRAIN.md`,
  and the forward roadmap). CDS-WP-018 closure became effective with the
  Human-Maintainer commit `e5d5d492619071655ba956713980d1ee261d9213`.
  **CDS-WP-020 … CDS-WP-053 remain `Planned`, not active, and not authorized**, and
  CDS-WP-019's own authorization came from a separate explicit Human-Maintainer
  decision, never from its roadmap position. (CDS-WP-019)
- **One additive row added to
  [Design System Architecture](docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md)** —
  a *Related documents* pointer to the visual foundation architecture, so the new
  family is reachable from the architecture entry point. **Nothing else in that
  document was touched**, including its *Deferred technical decisions* list.
  (CDS-WP-019)
- **`PHASE_TRANSITION_RECOMMENDED` raised, and nothing renamed.** The phase label
  set by **DEC-S-062** stays coherent for CDS-WP-019, which creates no visual value,
  but will be materially strained by **CDS-WP-020**, the first work package that
  would create real visual values. Recorded as a forward-looking recommendation to
  be resolved **before CDS-WP-020 is authorized**, tied to the still-open
  **F-017-04**. A relabel requires a **new Decision superseding DEC-S-062** and is a
  Human-Maintainer decision. (CDS-WP-019)
- **Nine findings recorded and explicitly not repaired** (`F-019-01` … `F-019-09`)
  in the forward roadmap's deferred-finding section: the `CONCEPT_AND_SCOPE.md`
  open-decision drift that CDS-WP-018's file list did not cover (`F-019-01`), the
  capability-domain enumeration asymmetry for iconography, illustration, and imagery
  (`F-019-02`), the CR-004 Layer 5 versus CDS-WP-021 Layer 3 mapping tension
  (`F-019-03`), the stale *unresolved format and tooling questions* in
  `TOKEN_AND_THEME_ARCHITECTURE.md` (`F-019-04`) and the stale *deferred technical
  decisions* in `DESIGN_SYSTEM_ARCHITECTURE.md` (`F-019-05`), the absent consumer
  demand evidence for four families (`F-019-06`), the nine-family governance
  capacity question (`F-019-07`), the phase-transition item (`F-019-08`), and the
  by-construction recurrence of `R1-F-01` in the Candidate Dossier's
  work-package-status row (`F-019-09`, outside this work package's file scope).
  **Routing is not repair**, and none of them blocked CDS-WP-019. (CDS-WP-019)
- **PB001 disposition updated — nothing imported.** The *Visual Foundation Gap*
  topic routed to CDS-WP-019 and CDS-WP-020 reached its first destination.
  **CDS-WP-019 obtained no PB001 material, cited none, and used none as an input**;
  PB001 is not held in this repository and its finding text remains outside it. The
  visual foundation architecture was derived entirely from the committed normative
  CDS sources and the registered consumer requirements. **PB001 remains Experimental
  Evidence at AE-0, non-normative**, and the routing to CDS-WP-020 stands.
  (CDS-WP-019)

**Boundaries of the CDS-WP-019 entries above.** **No visual value was created** —
no colour, typeface, size, spacing, radius, stroke, shadow, opacity value, icon,
illustration, motion value, breakpoint, or theme instance — and **no visual value
exists in CDS**, verified by search. All nine visual foundation families are
**`Proposed`**; **none is Candidate**. No maturity changed: the Semantic Status
Foundation stays `Candidate` / `Approved` at `semantic-status-rev-0002-candidate`
with `AE1-CDS-WP016-SEMSTATUS-004` at **AE-1**, source/contract scope only, and
**no Semantic Status source, revision, maturity, or evidence package was touched**.
**No evidence was produced, admitted, altered, or transferred.** Everything under
`tokens/`, `schemas/`, `tools/`, `tests/`, `artifacts/`, `docs/foundations/`, and
`requirements-validator.lock` is **unchanged**, as are `DECISION_INDEX.md`, the
ADRs, and `RISK_REGISTER.md`. **No Decision and no ADR was added** — the register
stays at **DEC-S-126** and **ADR-0003**; **no risk was added, accepted, or closed**
— the register stays at **RISK-098**. No extension point was named, no Product
Profile or brand was created or activated, no pilot was started, no consumer
repository was read or written, no claim was made, no artifact reached `Stable`,
publication remains **`Private Development`**, there are **0 tags and no release**,
and **no Git write was performed**.

- **CDS-WP-017 recorded as `Completed`** and **CDS-WP-018 recorded as the active
  work package** across the current-state surfaces (`README.md`, `CLAUDE.md`,
  `project-system/WORK_PACKAGES.md`, `project-system/NEXT_PHASE.md`,
  `project-system/PROJECT_PROFILE.md`,
  `project-system/CONTEXT_PACK_FOUNDATION.md`, `project-brain/PROJECT_BRAIN.md`,
  and the forward roadmap). CDS-WP-017 closure became effective with the
  Human-Maintainer commit `df9b8f21ff3bde4607b1c9ff7fdcbe3144366040`.
  **CDS-WP-019 … CDS-WP-053 remain `Planned`, not active, and not authorized**, and
  CDS-WP-018's own authorization came from a separate explicit Human-Maintainer
  decision, never from its roadmap position. (CDS-WP-018)

**Boundaries of the CDS-WP-018 entries above.** No maturity changed; the Semantic
Status Foundation stays `Candidate` / `Approved` at
`semantic-status-rev-0002-candidate` with `AE1-CDS-WP016-SEMSTATUS-004` at **AE-1**,
source/contract scope only. **No evidence was produced, admitted, altered, or
transferred**; the five evidence-bound Foundation documents, the ADRs,
`DECISION_INDEX.md`, and every artifact under `tokens/`, `schemas/`, `tools/`,
`tests/`, and `artifacts/` are **unchanged**. No Decision and no ADR was added — the
register stays at **DEC-S-126** and **ADR-0003**; no risk was added, accepted, or
closed — the register stays at **RISK-098**. No phase was renamed, no capability was
registered, no claim was made, no artifact reached `Stable`, no Product Profile or
pilot was activated, publication remains **`Private Development`**, there are **0
tags and no release**, and **no Git write was performed**.

### Added

- **Post-Candidate Development Roadmap** added
  (`docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md`) — the **single active
  forward roadmap**: twelve development arcs from Reconciliation through Stable
  Evaluation, **CDS-WP-017 … CDS-WP-053** as a contiguous gap-free sequence,
  milestones **M1 … M12**, a per-work-package mapping to the normative eight-layer
  architecture, the standing gates (Product Profile · real consumer ·
  generated-output authority · semantic validation priority · multimodal and AI
  scope registration · Stable), and an eleven-way requirement classification model
  in which **Consumer-local** and **Reject** are valid outcomes. It is a **planning
  view — not normative, not an authorization, and not evidence**. (CDS-WP-017)
- **Forward work-package sequence registered as `Planned`** in
  `project-system/WORK_PACKAGES.md`: **CDS-WP-018 … CDS-WP-053**, none of them
  active and none authorized for execution. **`Planned` is not `Active`**, and
  recording the sequence activates nothing — each work package requires its own
  explicit Nova prompt and Human-Maintainer authorization. (CDS-WP-017)
- **PB001 disposition recorded.** PB001 is **not held in this repository** and
  remains **Experimental Evidence at AE-0, non-normative**, with no conformance
  evidence, no Product Profile authority, and no universal-core authority by
  itself. Its finding topics are routed to destination work packages **by topic
  only**; **no PB001 evidence is imported and none is upgraded**. (CDS-WP-017)
- **Deferred finding routing recorded.** `R3R-003`, `NF-R3-OBS-001`,
  `NF-R4-OBS-001`, `NF-R4-OBS-002`, `NF-R5R-OBS-001`, and `NF-R5R-OBS-003` are
  routed to **CDS-WP-018**; `NF-R5R-OBS-002` stays **informational — a historical
  evidence limitation requiring no repair**. None of these identifiers had any
  **pre-existing** occurrence in this repository — the routing itself is the only
  reason they appear here — and their finding text is still held outside it, so
  routing is by identifier only and CDS-WP-018 must reconstruct each finding's
  content from its original source. **Routing is not repair**, and CDS-WP-017
  repaired none of them. (CDS-WP-017)

- **Semantic Status Foundation promoted to `Candidate`** (CDS-WP-016). The
  Human-Maintainer exact-byte **Promotion Commit
  `22fa0710e2b75df22e7b420c2f9d86bbe67b2777`** (parent
  `8d1374fa4c61cc1eed214823681ee1209a2d91f7`, 2026-08-19) integrated the approved
  Proposed Candidate bytes unchanged. The `semantic/status` source set now declares
  source revision **`semantic-status-rev-0002-candidate`**, `maturityState`
  **`Candidate`**, and `approvalState` **`Approved`**. The **exact-byte Promotion
  Gate passed**: committed blob identity **15/15 exact**, post-commit regression
  **47/47 · 64/64 · 184/184 · 24/24/0/0**, remote fast-forward **PASS**.
  (CDS-WP-016)
- **`AE1-CDS-WP016-SEMSTATUS-004` admitted at AE-1** by the Human Maintainer
  (2026-08-19), bound to `semantic-status-rev-0002-candidate`, for the
  channel-independent Semantic Status Layer-3 source/contract family **only** —
  after a fresh independent evidence review (**PASS WITH NOTES**) by a reviewer who
  was not its executor. `AE1-CDS-WP016-SEMSTATUS-002` remains a historical
  `semantic-status-rev-0001` admission only; `AE1-CDS-WP016-SEMSTATUS-003` is **not
  admitted** (`SUPERSEDED_FOR_ADMISSION_BY_EVIDENCE_INPUT_CHANGE`). **Evidence never
  transfers across a source revision.** (CDS-WP-016)
- **Human-Maintainer Candidate approval recorded** as
  `AUTHORIZED_PENDING_EXACT_BYTE_INTEGRATION` in the Candidate Approval Record
  `CAR-CDS-WP016-SEMSTATUS-001` — the first instance of the Candidate Approval
  Record Template — following the Nova Candidate Finalization Review
  (**GO WITH NOTES**, a recommendation only). (CDS-WP-016)
- **Candidate Promotion Effectivity Record** added
  (`docs/governance/SEMANTIC_STATUS_CANDIDATE_PROMOTION_EFFECTIVITY_RECORD.md`) — a
  governance lifecycle effectivity record for the already completed promotion. It is
  **not evidence**, **not a Promotion Commit**, **not a Decision**, and **not a
  source-precedence policy**. (CDS-WP-016)

**Boundaries, unchanged by all of the above:** **Stable is not reached** and no
artifact is Stable. **No claim of any level** and **no conformance of any kind** is
established; there is no WCAG conformance, no AE-2, AE-3, or AE-4, no channel
evidence, and no consumer evidence. No Product Profile authority, no CoreOps pilot
activation, **no release, no tag, and no publication transition** — publication
remains `Private Development`. Candidate is bounded validation only and is never
normative. CDS-WP-017 is **inactive, not authorized, and not defined**.

- Semantic Status Source Set implemented (CDS-WP-015): the Experimental
  `semantic/status` source set (5 axis groups, 25 non-visual status tokens
  `status.<axis>.<value>` with technical-identifier values, manifest, resolver,
  revision `semantic-status-rev-0001`); no visual value, no Candidate.
  (CDS-WP-015)
- Validation-case schema additively corrected (Nova-authorized after a correctly
  BLOCKED first run): fixture-path pattern widened to admit
  `tests/fixtures/semantic-status/` token fixtures alongside the existing
  machine-readable families, and nine `semantic-status-*` diagnostic categories
  added; schema `$id`, draft, and all existing constraints unchanged; the CLI
  schema gate untouched and fail closed; regression-tested. (CDS-WP-015)
- Semantic-status V4 validator extension added (`tools/cds_validator/
  semantic_status.py`; nine stable `CDS-V4-STATUS-*` diagnostics): authorized
  axis/value sets, explicit `unknown`, 25-token count, path/value agreement,
  case-only collision rejection, aggregate- and appearance-role prohibition,
  approval-statement and manifest-identity checks; objective checks execute even
  for testOnly/nonNormative fixtures. (CDS-WP-015)
- Nine semantic-status fixtures (1 positive, 8 negative) and VAL-CASE-016…024
  added; the 24-case harness executed with **24/24 expected/actual matches**
  (VAL-CASE-001…015 byte-identical, immutable baseline); 103/103 unit tests;
  revision-clean WP-013 re-execution recorded (71/71 tests, 15/15 matches on the
  committed CDS-WP-014 revision, worktree clean). (CDS-WP-015)
- Semantic Status source-set validation executed (V1–V3 Pass, exit 0) with
  RFC 8785 + SHA-256 digests for the token document, manifest, and resolver;
  DE/EN terminology mapping created (25/25 entries, 0 missing); four
  executor-produced evidence reviews and the Draft Semantic Status Candidate
  Dossier created (Candidate gate incomplete — Not Candidate). (CDS-WP-015)
- DEC-S-115 … DEC-S-124 added (source-set identity, 25-token contract, path/value
  traceability, fail-closed status validation, terminology separation, immutable
  baseline cases, executor-produced evidence class, Draft-dossier rule,
  identity/digest alignment, no-premature-consumption). (CDS-WP-015)
- RISK-090 … RISK-097 added (source/contract drift, visual misuse, path migration,
  validator blind spot, fixture overfitting, localization false assurance, dossier
  completeness illusion, premature consumption); no existing risk status changed.
  (CDS-WP-015)
- CDS-WP-016 — Semantic Status Foundation Independent Evidence Review and
  Candidate Gate activated as the next work package. (CDS-WP-015)

- Semantic Status Foundation Contract defined (CDS-WP-014): five independent status
  axes (`condition`, `severity`, `confidence`, `freshness`, `evidence`) with a fixed
  25-value vocabulary and explicit `unknown` on every axis; ten invariants including
  no-aggregate-health-score and degraded-knowledge-never-as-success; the 11-field
  complete status object with 6 review-required combinations, 8 fail-closed states,
  and a 6-level disclosure priority. (CDS-WP-014)
- Status communication, accessibility, and localization contract created: text-first
  accessible meaning, no colour-/icon-/position-/shape-/motion-only encoding, DE/EN
  semantic parity, language-neutral technical IDs with separately localized labels,
  reduced-motion boundary. No final UI copy and no visual value. (CDS-WP-014)
- Semantic Status Token Contract created (value-neutral roles for a future Semantic
  source set under the CDS Token Format Profile; no token source file, no token
  name, no value). (CDS-WP-014)
- First Semantic Status Candidate Plan created: 8-element Candidate package, fixed
  scope and exclusions, 10 cumulative prerequisites (none met), evidence plan, and
  an executor-produced readiness review — no artifact promoted. (CDS-WP-014)
- DEC-S-105 … DEC-S-114 added (five-axis model, fixed vocabulary, truthfulness
  rules, no aggregate score, combination rules, localization boundaries, text-first
  accessibility, downstream preservation, first Candidate definition and gates).
  (CDS-WP-014)
- RISK-082 … RISK-089 added (axis conflation, unknown-state optimism, aggregate
  masking, combination ambiguity, localization drift, visual-only encoding,
  consumer remapping divergence, first-candidate scope expansion); no existing risk
  status changed. (CDS-WP-014)
- CDS-WP-015 — Semantic Status Foundation Source Set and Candidate Evidence
  activated as the next work package. (CDS-WP-014)
- Offline token profile validator implemented (CDS-WP-013): entry point
  `python -m tools.cds_validator` with `version`, `validate-file`, `validate-cases`,
  and `digest` commands and a stable exit-code contract; Python 3.11+ with exactly
  pinned `jsonschema==4.26.0` and `rfc8785==0.1.4` (`requirements-validator.lock`);
  no runtime network access. (CDS-WP-013)
- Single duplicate-key-rejecting JSON loader and a local five-schema registry
  implemented; unknown or network schema resolution fails closed. (CDS-WP-013)
- CDS validation-result schema created
  (`schemas/cds-validation-result.schema.json`) binding runtime, dependency, schema,
  case, source-revision, digest, and review-state identities; no numeric score.
  (CDS-WP-013)
- Layered V1–V4 validation executed against all fixtures: the fixture harness ran
  **15/15 validation cases with 15/15 expected/actual matches** (71/71 unit tests);
  machine-readable evidence recorded in `artifacts/validation/` and reviewed in the
  Offline Token Validator Execution Review — executor-produced, independently
  unreviewed. (CDS-WP-013)
- RFC 8785 + SHA-256 content digests computed for the 14 V1-parsable fixtures; the
  duplicate-key fixture received no digest. (CDS-WP-013)
- ADR-0003 created (Offline Token Validator Implementation Stack); dependency
  provenance recorded in the Offline Validator Dependency Source Register and Stack
  Evaluation; validator architecture and usage documented. (CDS-WP-013)
- DEC-S-093 … DEC-S-104 added (validator stack, CLI contract, controlled loader,
  local registry, layered states, bounded DTCG coverage, graph enforcement, digest
  boundary, result contract, harness semantics, evidence class, Candidate gate).
  (CDS-WP-013)
- RISK-073 … RISK-081 added; RISK-066, RISK-067, RISK-068, RISK-069, and RISK-071
  moved `Monitored → Mitigating` on executed harness evidence (executor-produced,
  independently unreviewed); no risk accepted or closed. (CDS-WP-013)
- CDS-WP-014 — Semantic Status Foundation Contract and First Candidate Plan
  activated as the next work package. (CDS-WP-013)
- Four CDS-owned JSON Schema Draft 2020-12 contracts created (CDS-WP-012): token
  document, source-set manifest, resolver document, and validation case — each with a
  stable `tag:` `$id`, same-document local `$ref`, and no remote dependency
  (`schemas/`). (CDS-WP-012)
- CDS extension payload contract implemented under `io.github.kaykaspers.cds`
  (requiring `profileVersion` and source-set identity; foreign extensions preserved and
  not automatically normative). (CDS-WP-012)
- Source-Set Manifest schema and Resolver schema created — explicit local declaration of
  identity, layer, path, dependency graph, and ordered composition; no implicit or
  network-discovered sets. (CDS-WP-012)
- Validation Case schema created; a 15-case validation-case matrix
  (`tests/fixtures/machine-readable/VALIDATION_CASES.json`) binds every fixture to
  expected V1–V4 outcomes with contiguous `VAL-CASE-###` IDs. (CDS-WP-012)
- Six synthetic positive fixtures and nine synthetic negative fixtures created (test-only,
  non-normative; `fixture/` IDs). (CDS-WP-012)
- V1–V4 Validation Contract created; the duplicate-key policy operationalized (duplicate
  object member names fail V1; no first/last-key-wins repair; a duplicate-key-aware parser
  is required). (CDS-WP-012)
- RFC 8785 (JSON Canonicalization Scheme) and SHA-256 digest model decided
  ([Deterministic Serialization and Digest Model](docs/architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md));
  a content digest is an integrity aid, not authenticity, and no canonicalizer is
  implemented. (CDS-WP-012)
- **ADR-0002 — Deterministic JSON Serialization** created (the second ADR; accepted upon
  Human-Maintainer commit following Nova approval). (CDS-WP-012)
- Work-package evidence notes for CDS-WP-012. (CDS-WP-012)
- Machine-readable source model defined (CDS-WP-011): the normative machine-readable
  CDS source (artifact class 2) with eight source-set classes, a strictly downward
  dependency model, and the boundary to generated artifacts and human-readable sources
  ([Machine-Readable Source Model](docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md)).
  (CDS-WP-011)
- **DTCG 2025.10 selected** as the external normative format basis (Format, Color,
  Resolver modules) — a Final Community Group Report, **not** a W3C Standard; only the
  pinned stable version is authoritative, previews are inputs only. Chosen from a
  seven-option evaluation using authorized official research (13 DTCG/W3C/RFC/
  JSON-Schema URLs). (CDS-WP-011)
- CDS Token Format Profile defined over DTCG with an `io.github.kaykaspers.cds`
  `$extensions` namespace (a collision-resistant, repository-identity-derived reserved
  root; foreign extensions preserved, not automatically normative), a
  machine-validatable naming/identifier profile, and Product-Profile bounds
  ([CDS Token Format Profile](docs/architecture/CDS_TOKEN_FORMAT_PROFILE.md)).
  (CDS-WP-011)
- **Strict JSON (RFC 8259) and `.tokens.json`** selected as the normative source form;
  YAML/JSONC/JSON5/tool-native/CSS/generated forms are not normative sources.
  (CDS-WP-011)
- **JSON Schema 2020-12** selected as the foundation for a future CDS-owned profile
  validator (no schema created; a schema pass is not full correctness). (CDS-WP-011)
- Token reference, resolution, and validation model defined: curly-brace
  `{group.token}` for canonical token-to-token references and DTCG `$ref` / RFC 6901
  JSON Pointer for document/property/resolver/source-set and controlled cross-file
  references; the resolver relationship; fail-closed cycle/dangling/type/layer/
  missing-set/undeclared-cross-file handling; and **four validation layers** (V1 Syntax
  · V2 DTCG · V3 CDS Profile · V4 Semantic/Governance)
  ([model](docs/architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)).
  (CDS-WP-011)
- Token metadata, provenance, and identity model defined: source-set identity,
  governance metadata, versioned non-`latest` provenance, and an open
  canonicalization decision state (RFC 8785 evaluated, not selected)
  ([model](docs/architecture/TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md)).
  (CDS-WP-011)
- **ADR-0001 — Machine-Readable Token Source Format** created (the first ADR; accepted
  upon Human-Maintainer commit following Nova approval)
  ([ADR-0001](docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)).
  (CDS-WP-011)
- Token format source register and evaluation created (non-normative research
  evidence); machine-readable source implementation plan created (roadmap for
  CDS-WP-012). (CDS-WP-011)
- Work-package evidence notes for CDS-WP-011. (CDS-WP-011)
- Initial accessibility support baseline defined (CDS-WP-010): **A11Y-BL-001**
  ([Accessibility Support Baseline](docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md)),
  pending Human-Maintainer commit — a **test contract, not evidence**; it declares
  the environments future evidence will target and asserts no support and no
  conformance. Composed from authorized official standards/vendor research only
  (13 URLs opened, 9 usable). (CDS-WP-010)
- Three-tier baseline model created — Required Core, Complementary, Scope-triggered
  (DEC-S-066). (CDS-WP-010)
- Accessibility environment and scope matrix created — 14 entries
  (A11Y-ENV-001…014): Required 6, Conditional 4, Deferred 4; 2 Required
  browser/screen-reader pairings. (CDS-WP-010)
- Accessibility evidence strategy created — operationalizes AE-0…AE-4, required
  evidence by maturity, manual/AT/consumer/pilot strategy, review independence, and
  a capacity-aware execution rule; **no evidence executed**. (CDS-WP-010)
- Accessibility evidence record template created — a non-normative operational form
  binding exact environment identity; **not evidence**. (CDS-WP-010)
- Accessibility baseline maintenance policy created — five freshness states, nine
  review triggers, and a six-month maximum review gap; no automatic claim renewal.
  (CDS-WP-010)
- Accessibility defect and regression model created — four impact levels, six defect
  statuses, and the rule that Blocking/High regressions block Stable and claims for
  the affected scope; **no defect registered (AE-0)**. (CDS-WP-010)
- Accessibility baseline source register and selection rationale created
  (non-normative research evidence), recording every opened official URL and the
  capacity-aware selection with its coverage gaps. (CDS-WP-010)
- Work-package evidence notes for CDS-WP-010. (CDS-WP-010)
- Foundation closure recorded (CDS-WP-009): the
  [Foundation Closure Record](docs/governance/FOUNDATION_CLOSURE_RECORD.md)
  registers the Foundation / Pre-Design milestone as **Closed with Notes** after
  CDS-WP-008, Nova review, and Human-Maintainer acceptance (commit of CDS-WP-008 +
  initiation of CDS-WP-009). It is normative for the fact of closure, the authority
  state, and the phase boundary; it grants no Candidate, Stable, claim, licence, or
  publication status. (CDS-WP-009)
- Pre-Candidate Operating Enablement phase activated; the
  [Pre-Candidate Operating Plan](docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md)
  records the phase entry state, prerequisites, Candidate entry conditions, and
  exit criteria. (CDS-WP-009)
- Foundation Operating Playbook created — a **non-normative** operational view that
  makes the committed governance runnable (intake and classification, Standard and
  Elevated tracks, stop conditions, decision/risk/evidence checks, approval gates,
  post-commit reconciliation, and the lean operating rule). (CDS-WP-009)
- Standard and Elevated change-dossier templates created — non-normative,
  reference-oriented per-change records (19 Standard fields; 36 Elevated fields,
  scalable via `Not applicable with rationale`). (CDS-WP-009)
- Critical Risk Action Register created — the twelve Critical Risks (RISK-017,
  020, 021, 023, 026, 028, 029, 031, 038, 040, 044, 048) each made actionable with
  a named Mitigation Executor role, review trigger, expected evidence, and blocking
  effect. (CDS-WP-009)
- Full repository reference-integrity review completed (CDS-WP-009): 112 text files
  in scope, 829 markdown links checked, **0 CDS-authored broken links**; the five
  broken links are confined to the vendored, pinned `.claude/skills/README.md` and
  are non-blocking; **PASS**. (CDS-WP-009)
- Work-package evidence notes for CDS-WP-009. (CDS-WP-009)
- Foundation Milestone Review completed (CDS-WP-008): a close-out review of the
  Foundation / Pre-Design phase across twelve dimensions, three governance dry
  runs, four-axis Candidate readiness, an eight-criterion CoreOps pilot entry
  matrix, and all 48 risks. Review evidence only — normative, no source changed.
  (CDS-WP-008)
- Foundation completeness matrix: 55 criteria (44 Met · 4 Met-with-notes · 3
  Partially met · 4 Not met), **0 Foundation blockers**. (CDS-WP-008)
- Governance affordability and operating-readiness review with three dry runs
  (Editorial → Operational; Additive Candidate → Operational with simplification
  notes; Elevated/accessibility → High burden). (CDS-WP-008)
- Foundation Candidate and CoreOps pilot entry readiness assessed; pilot remains
  inactive and no conformance is demonstrated; no artifact promoted. (CDS-WP-008)
- Open gaps and dependencies classified as twelve review findings
  (FM-F-001 … FM-F-012); none is a Foundation blocker. (CDS-WP-008)
- Next-phase recommendation created (advisory; no phase activated, no work-package
  ID assigned). (CDS-WP-008)
- Work-package evidence notes for CDS-WP-008. (CDS-WP-008)

### Changed

- **CDS-WP-016 recorded as `Completed`** across the current-state surfaces
  (`README.md`, `CLAUDE.md`, `project-system/WORK_PACKAGES.md`,
  `project-system/NEXT_PHASE.md`, `project-system/PROJECT_PROFILE.md`,
  `project-system/CONTEXT_PACK_FOUNDATION.md`, `project-brain/PROJECT_BRAIN.md`,
  and the two affected roadmap plans). Closure became effective with the
  Human-Maintainer commit `1fc53ae5afa40807e1950171ab700b0860ee581e`; the
  superseded two-stage closure statement, which predated that commit, is retired.
  **CDS-WP-017 is recorded as the active work package.** (CDS-WP-017)

**Boundaries of the CDS-WP-017 entries above.** No maturity changed; the Semantic
Status Foundation stays `Candidate` at `semantic-status-rev-0002-candidate` and
**nothing is Stable**. **No evidence was produced and none was admitted**; every
artifact other than the one admitted source-level AE-1 family remains **AE-0**. No
risk was accepted or closed, no ADR and no Decision was added, and no Semantic
Status source byte, schema, validator, fixture, or evidence artifact was touched.
**No claim, no conformance, no Product Profile, no pilot, no consumer integration,
no release, no tag, and no publication transition** — publication remains
`Private Development`. **CDS-WP-018 … CDS-WP-053 are inactive.**

- **Post-promotion lifecycle reconciliation** across the current-state, governance,
  authority, roadmap, risk, and project mirrors (CDS-WP-016). The five
  `AE1-CDS-WP016-SEMSTATUS-004`-bound normative Foundation documents, the promoted
  Candidate source, all evidence packages, the review provenance, the bound test
  input, the runner, the validator, the fixtures, the schemas, and
  `requirements-validator.lock` were left **exact-byte unchanged**. No accepted
  Decision text was altered, no ADR was added, and no evidence artifact was
  modified. (CDS-WP-016)
- **RISK-031 (maturity inflation): `Monitored` → `Mitigating`** by
  Human-Maintainer decision (2026-08-19) — the first Candidate transition completed
  under active, exact-byte, evidence-bound gate control. No other risk status
  changed and no new risk identifier was created. (CDS-WP-016)
- Decision index extended to DEC-S-001 … DEC-S-092 with a tenth decision type for
  machine-readable bootstrap and validation decisions (DEC-S-083 … DEC-S-092);
  DEC-S-001 … DEC-S-082 unchanged. **ADR range is now ADR-0001 … ADR-0002 (2 ADRs).**
  (CDS-WP-012)
- Risk register extended to RISK-001 … RISK-072: added **RISK-064 … RISK-072** (CDS schema
  contract incompleteness, synthetic fixtures mistaken for design tokens, schema/validator
  divergence, canonicalization/digest mismatch, duplicate-key ambiguity, manifest/resolver
  graph inconsistency, validation fixture coverage gap, validation expectation drift,
  digest mistaken for authenticity), all `Monitored`; no existing risk changed; no risk
  accepted or closed. RISK-040 and RISK-044 remain `Mitigating`. (CDS-WP-012)
- Work-package status advanced: CDS-WP-012 completed; **CDS-WP-013 — Offline Token Profile
  Validator and Fixture Harness** activated as the next work package (not yet executed).
  Foundation Context Pack, project profile, project brain, README, work packages, next
  phase, implementation plan, and Claude working instructions updated. Publication state
  remains `Private Development`; no real token/design value; no productive validator or
  canonicalizer; formal schema execution not assessed; the bootstrap is Experimental, not
  Candidate; pilot inactive. (CDS-WP-012)
- Decision index extended to DEC-S-001 … DEC-S-082 with a ninth decision type for
  machine-readable source and token format decisions (DEC-S-073 … DEC-S-082);
  DEC-S-001 … DEC-S-072 unchanged. **ADR-0001 is the first ADR**; the decision-record
  format note now covers ADR files. (CDS-WP-011)
- Risk register extended to RISK-001 … RISK-063: added **RISK-055 … RISK-063** (token
  specification version drift, preview contamination, profile divergence,
  schema-validation false assurance, reference-resolution failure, cross-layer
  dependency violation, token identifier collision, provenance incompleteness,
  transformation-tool lock-in), all `Monitored`; no existing risk changed; no risk
  accepted or closed. RISK-040 and RISK-044 remain `Mitigating`. (CDS-WP-011)
- Work-package status advanced: CDS-WP-011 completed; **CDS-WP-012 — Machine-Readable
  Source Bootstrap and Validation Contract** activated as the next work package (not
  yet executed). Foundation Context Pack, project profile, project brain, README, work
  packages, next phase, and Claude working instructions updated; "token format" removed
  from the intentionally-open-decisions list. Publication state remains `Private
  Development`; no token/schema/validator/design value; no Candidate/Stable; pilot
  inactive. (CDS-WP-011)
- Decision index extended to DEC-S-001 … DEC-S-072 with an eighth decision type for
  accessibility support baseline and evidence decisions (DEC-S-065 … DEC-S-072);
  DEC-S-001 … DEC-S-064 unchanged; no ADR. (CDS-WP-010)
- Risk register extended to RISK-001 … RISK-054: added **RISK-049 … RISK-054**
  (accessibility baseline representativeness, universal-support misreading,
  environment-availability mismatch, evidence-identity incompleteness,
  regression-coverage gap, defect normalization), all `Monitored`; moved **RISK-044
  `Monitored → Mitigating`** on the strength of the defined baseline; no existing
  risk description/likelihood/severity changed; no risk accepted or closed.
  (CDS-WP-010)
- Accessibility Evidence and Claims Model, CoreOps Pilot Accessibility Criterion, and
  Consumer Validation Plan reconciled to reference A11Y-BL-001 (product-family vs
  execution identity, freshness, regression, complete-process evidence, claim
  boundary); the AE-0…AE-4 meanings are unchanged. (CDS-WP-010)
- Critical Risk Action Register updated: RISK-044 expected evidence delivered and set
  to `Mitigating`; RISK-048 capacity-aware tiering recorded as partial mitigation;
  RISK-040 first follow-evidence noted. RISK-049…054 not auto-added to the Critical
  group. (CDS-WP-010)
- Work-package status advanced: CDS-WP-010 completed; **CDS-WP-011 — Machine-Readable
  Source and Token Format Decision** activated as the next work package (not yet
  executed). Foundation Context Pack, project profile, project brain, README, work
  packages, next phase, Pre-Candidate Operating Plan, and Claude working instructions
  updated. Publication state remains `Private Development`; every artifact remains
  AE-0; no environment claimed supported; pilot inactive. (CDS-WP-010)
- Foundation status: **Closed with Notes** — the Human Maintainer accepted the
  `GO WITH NOTES` outcome; the Pre-Candidate Operating Enablement phase is active.
  No version, Candidate, Stable, claim, release, or publication status is asserted;
  publication state remains `Private Development`. (CDS-WP-009)
- Decision index extended to DEC-S-001 … DEC-S-064 with a seventh decision type for
  operating enablement and pre-candidate decisions (DEC-S-061 … DEC-S-064);
  DEC-S-001 … DEC-S-060 unchanged; no ADR. (CDS-WP-009)
- Risk register: **RISK-040 moved `Monitored → Mitigating`** on the strength of the
  Critical Risk Action Register (DEC-S-064) — the only risk status change; no
  description, likelihood, or severity changed; no risk accepted or closed; range
  remains RISK-001 … RISK-048 (48). (CDS-WP-009)
- Work-package status advanced: CDS-WP-009 completed; **CDS-WP-010 — Accessibility
  Support Baseline and Evidence Strategy** activated as the next work package (not
  yet executed). (CDS-WP-009)
- Foundation Context Pack, project profile, project brain, README, work packages,
  next phase, and Claude working instructions updated for Foundation closure,
  operating enablement, the non-normative operating views, the critical-risk action
  rule, and the CDS-WP-010 pointer. (CDS-WP-009)
- Recommended milestone outcome: **GO WITH NOTES** — Foundation closable with
  mandatory next-phase notes, pending Nova review and Human-Maintainer approval.
  (CDS-WP-008)
- Work-package status: CDS-WP-008 completed; **no next work package authorized**;
  next-phase roadmap pending decision. No new Decision or Risk IDs; no ADR; no new
  work-package ID. Publication state remains `Private Development`. (CDS-WP-008)

- Accessibility and inclusive-design policy defined as the normative
  accessibility source: purpose and authority, the target-versus-claim boundary,
  principles, shared responsibility, architecture integration, maturity
  relationship, inclusive-design scope, source hierarchy, and change control.
  (CDS-WP-007)
- **WCAG 2.2 Level AA** target defined for the applicable web-based scope,
  resolving CR-024 at policy level. A target, not a conformance claim. (CDS-WP-007)
- Accessibility responsibility model: CDS, consumer, and shared/contract-
  controlled responsibilities, a RACI-style matrix, the component-to-product and
  Product Profile boundaries, claim responsibility, and escalation. (CDS-WP-007)
- Accessibility requirements baseline across ten areas, separating normative,
  implementation-dependent, consumer-scope, channel-specific, and deferred
  requirements. (CDS-WP-007)
- WCAG 2.2 Level A and AA applicability matrix: 56 displayed rows — 31 current
  Level A, 24 Level AA, and 1 historical removed reference row (4.1.1, obsolete
  and removed by the standard) — for 55 currently applicable criteria, with
  per-criterion
  responsibility, policy status, architecture layers, and required evidence — no
  pass/fail statement. (CDS-WP-007)
- Five-level accessibility evidence model AE-0 … AE-4 with Candidate and Stable
  gates, a support-baseline process, the automated-only insufficiency rule, the
  component/product evidence boundaries, claim boundaries, and no numeric score.
  (CDS-WP-007)
- Six accessibility channel profiles, each with scope, target, owner, minimum
  future evidence, current gap, and Candidate/Stable boundaries; only web UI and
  web documentation carry a target; none is Candidate- or Stable-eligible.
  (CDS-WP-007)
- Accessibility limitation and exception policy: a fifteen-field limitation
  record, impact and mitigation rules, maturity and claim effects, the exception
  boundary and prohibited waivers, and the capacity-is-not-a-rationale rule.
  (CDS-WP-007)
- CoreOps pilot accessibility criterion operationalizing CR-024, with the entry
  criterion `Accessibility target defined` satisfiable on Human Maintainer commit,
  Pilot Group E minimum evidence, and confirmation that the pilot has not started.
  (CDS-WP-007)
- Accessibility source register (13 opened official W3C/WAI/ETSI URLs) and a
  standard-status and limitations record (WCAG 2.2, WAI-ARIA, APG, WCAG-EM 2.0
  draft, EN 301 549 on-approval), with no legal-advice statement. (CDS-WP-007)
- Accessibility architecture alignment mapping accessibility onto the eight
  layers, eight artifact classes, five token-flow levels, profiles, contracts,
  status axes, channels, evidence flow, and maturity gates. (CDS-WP-007)
- Accessibility and inclusive-design decisions DEC-S-049 … DEC-S-060. (CDS-WP-007)
- Risks RISK-041 … RISK-048 covering target-mistaken-for-conformance,
  automated-testing substitution, the component-to-product responsibility gap,
  accessibility support-baseline drift, accessibility regression, the non-web
  channel gap, inclusive-design undercoverage, and the accessibility evidence
  burden. (CDS-WP-007)
- Work-package evidence notes for CDS-WP-007.

### Changed

- CR-021, CR-022, CR-024, and CR-034 traceability reconciled: no requirement is
  deferred to a policy work package any longer; the architecture status
  distribution is 9 addressed, 27 partially addressed, 2 consumer-owned, 2 out of
  scope. CR-024 is addressed because the target and policy exist — not because
  anything was tested. (CDS-WP-007)
- Artifact maturity lifecycle, exception and Product Profile governance, adoption
  and claims policy, licensing and publication model, CoreOps pilot contract, and
  consumer validation plan reconciled to reference the accessibility policy and
  evidence model. No artifact was promoted; publication state remains
  `Private Development`. (CDS-WP-007)
- Work-package status advanced: CDS-WP-007 completed, CDS-WP-008 — Foundation
  Milestone Review activated as the next work package. (CDS-WP-007)
- Decision index extended to DEC-S-001 … DEC-S-060 with a sixth decision type for
  accessibility and inclusive design; DEC-S-001 … DEC-S-048 unchanged; no ADR.
  (CDS-WP-007)
- Risk register extended to RISK-001 … RISK-048; existing risks unchanged; the
  finalized four-role model applied. (CDS-WP-007)

- Governance operating model defined as the normative governance source: six
  roles, an authority matrix, Standard and Elevated tracks, approval gates,
  separation of review and approval, the consumer governance boundary, and
  escalation. (CDS-WP-006)
- Normative source conflict policy: neither source wins automatically, five
  conflict states, an eight-step fail-closed procedure, and prohibited automatic
  precedence rules. (CDS-WP-006)
- Seven-state artifact maturity lifecycle with entry and exit criteria, a full
  transition matrix, Candidate and Stable gates, and maturity kept separate from
  release version and publication state. (CDS-WP-006)
- Semantic versioning and compatibility policy: MAJOR.MINOR.PATCH, a pre-1.0
  policy, ten release identity elements, eight compatibility axes, and six
  permitted compatibility statements. (CDS-WP-006)
- Deprecation and removal policy with nine required deprecation fields and
  narrowly bounded emergency removal. (CDS-WP-006)
- Contribution and acceptance model: a ten-step flow, eleven required inputs,
  five outcomes, and prohibited shortcuts. (CDS-WP-006)
- Exception and Product Profile governance: thirteen exception fields, six
  exception statuses, twelve Product Profile elements, and an anti-fragmentation
  review. (CDS-WP-006)
- Adoption and conformance claims policy: four graded claim types, eight
  mandatory claim fields, eight re-assessment triggers, and a prohibited
  certification claim. (CDS-WP-006)
- Risk governance model finalizing the risk owner model across all risks:
  Accountable Risk Owner, Risk Controller, Mitigation Executor, and Evidence
  Reviewer, with five risk statuses and an anti-ceremonial rule. (CDS-WP-006)
- Licensing and publication decision model: ten artifact classes with an
  eleven-field rights matrix, five publication states, and a fifteen-point
  publication gate. (CDS-WP-006)
- Release and change control policy: twelve release candidate requirements, six
  change classes, and release authority reserved to the Human Maintainer.
  (CDS-WP-006)
- Governance, lifecycle and publication decisions DEC-S-033 … DEC-S-048.
  (CDS-WP-006)
- Risks RISK-029 … RISK-040 covering governance bottleneck, role ambiguity,
  maturity inflation, compatibility ambiguity, deprecation without migration,
  contribution gate bypass, exception debt, Product Profile governance bypass,
  misleading claims, licensing fragmentation, premature publication, and
  ceremonial risk governance. (CDS-WP-006)
- Work-package evidence notes for CDS-WP-006.
- Logical design-system architecture defined as the normative architecture
  source, with architecture objectives, quality attributes, allowed and
  prohibited dependency directions, and sixteen architecture invariants.
  (CDS-WP-005)
- Eight architecture layers registered: Strategy and Governance, Brand and
  Identity, Foundations and Tokens, Components, Patterns and Experiences,
  Channels and Communication, Distribution and Enablement, Evidence and Quality.
  (CDS-WP-005)
- Source-of-Truth and Authority Model with eight artifact classes, an authority
  matrix, nine conflict scenarios, and fail-closed behavior. (CDS-WP-005)
- Conceptual Token and Theme Architecture with five token layers, the
  semantic-first principle, alias and dependency direction, validation
  requirements, and prohibited shortcuts. No values, names, format, or tooling
  selected. (CDS-WP-005)
- Product Profile and Extension Model with Core Foundation, Product Profile,
  Consumer Extension, Domain Pattern Family, and Local Exception; permitted and
  forbidden override categories; anti-fragmentation rules; and the
  existing-product reconciliation flow. (CDS-WP-005)
- Artifact Distribution and Channel Model with logical artifact families, nine
  channel classes, transformation boundaries, offline and self-hosted
  requirements, provenance and pinning, and distribution neutrality.
  (CDS-WP-005)
- Consumer Contract and Reconciliation Model with the Source, Transformation,
  Distribution, Integration, and Adoption Evidence contracts, plus CDS
  obligations and the reconciliation flow. (CDS-WP-005)
- Evidence, Traceability and Status Semantics architecture with the traceability
  flow, required logical identities, deviation and feedback flows, five separated
  status axes, and the Unknown invariant. (CDS-WP-005)
- CR-001 … CR-040 mapped to the architecture with per-requirement layer,
  response, remaining decision, follow-up, and status. (CDS-WP-005)
- Logical architecture decisions DEC-S-021 … DEC-S-032. (CDS-WP-005)
- Risks RISK-020 … RISK-028 covering authority ambiguity, token proliferation,
  reconciliation failure, domain-pattern leakage, channel divergence, provenance
  loss, architecture overdesign, profile fragmentation, and deferred
  accessibility debt. (CDS-WP-005)
- Work-package evidence notes for CDS-WP-005.
- Consumer evidence registered from three consumer repositories analyzed
  read-only at committed revisions — CoreOps as primary pilot consumer,
  SpeakCore and CastCore as secondary evidence. 15 sources, 14 usable, each
  bound to a committed HEAD revision. (CDS-WP-004)
- Consumer requirements model registering CR-001 … CR-040 with classification,
  evidence status and strength, pilot priority, ownership boundary, and
  validation method. (CDS-WP-004)
- Consumer requirements traceability matrix mapping every requirement to its
  committed consumer source. (CDS-WP-004)
- CoreOps pilot scope and scenarios: five pilot groups (A–E) with nine
  scenarios, an explicit out-of-scope list, and open design questions.
  (CDS-WP-004)
- CoreOps pilot contract with purpose, parties, entry criteria, evidence
  requirements, exit criteria, success categories, and change control. Normative
  only upon Human Maintainer commit following Nova approval; not active.
  (CDS-WP-004)
- Consumer validation plan defining evidence levels, the deviation model, the
  exit review, and the explicit absence of any conformance promise.
  (CDS-WP-004)
- Consumer hypothesis validation layer assessing HYP-001 … HYP-008 against
  consumer evidence, leaving the CDS-WP-003 research assessments unchanged.
  (CDS-WP-004)
- Consumer and pilot scope decisions DEC-S-013 … DEC-S-020. (CDS-WP-004)
- Risks RISK-014 … RISK-019 covering consumer evidence staleness, pilot scope
  inflation, product-specific contamination, document evidence mistaken for user
  validation, pilot mistaken for adoption, and secondary consumer
  underrepresentation. (CDS-WP-004)
- Work-package evidence notes for CDS-WP-004.
- Official-source benchmark of ten established design systems against 14
  dimensions, reviewed on 2026-07-15. Findings are research evidence and are
  explicitly **non-normative**. (CDS-WP-003)
- Benchmark source register recording every official URL opened, with access
  date, evidence status, redirects, and access failures. (CDS-WP-003)
- Benchmark evidence matrix covering all ten systems across all 14 dimensions,
  using a fixed evidence-status vocabulary and no numeric scores or rankings.
  (CDS-WP-003)
- Assessment of the eight CDS differentiation hypotheses HYP-001 … HYP-008, each
  with supporting evidence, counterevidence, and an explicit uniqueness risk. No
  hypothesis reached "Strongly supported"; all remain research hypotheses.
  (CDS-WP-003)
- Research limitations documenting source, access, depth, language, version, and
  copyright boundaries, and the difference between public documentation and
  unknown internal practice. (CDS-WP-003)
- Risks RISK-010 … RISK-013 covering benchmark imitation, research and source
  bias, source volatility, and differentiation overstatement. (CDS-WP-003)
- Work-package evidence notes for CDS-WP-003.
- Registered concept and scope as the normative scope source: problem
  statement, mission, vision, strategic objectives, six capability domains,
  cross-cutting concerns, current Foundation scope separated from long-term
  scope, twelve binding non-goals, ownership boundaries, CoreOps pilot
  boundary, assumptions, and deferred decisions. (CDS-WP-002)
- Consumer and Stakeholder Model with direct users, indirect beneficiaries,
  stakeholder roles, three consumer relationship classes, channel-consumer
  categories, and the limits of the classification. (CDS-WP-002)
- Scope Boundary Matrix registering the per-area split between CDS
  responsibility, consumer responsibility, and shared or contract-controlled
  responsibility. (CDS-WP-002)
- Foundation Context Pack as a compact, explicitly non-normative continuation
  summary. (CDS-WP-002)
- Strategic scope decisions DEC-S-007 … DEC-S-012. (CDS-WP-002)
- Risks RISK-006 … RISK-009. (CDS-WP-002)
- Work-package evidence notes for CDS-WP-002.
- Verified local adoption of the 38 docs-only NDF v1.0.0 Claude Skills under
  `.claude/skills/`, extracted byte-identically from the released NDF v1.0.0
  tag (commit `9dcadc12fb960914b9a5baeff2ab1aee75912b57`). Upstream contents
  unmodified. (CDS-WP-001A)
- NDF Skills provenance documentation recording source, tag, commit,
  verification method, verification result, and the update rule. (CDS-WP-001A)
- Machine-readable SHA-256 hash manifest of every adopted Skill file.
  (CDS-WP-001A)
- NDF Skills inventory covering all 38 Skills. (CDS-WP-001A)
- Work-package evidence notes for CDS-WP-001A.
- Project charter defining mission, vision, strategic purpose, scope
  categories, current phase boundary, non-goals, pilot relationship, and
  authority model. (CDS-WP-001)
- Decision index with the strategic foundation decisions DEC-S-001 …
  DEC-S-006. (CDS-WP-001)
- Risk register with the initial risks RISK-001 … RISK-005. (CDS-WP-001)
- Initial controlled work-package roadmap CDS-WP-001 … CDS-WP-008.
  (CDS-WP-001)
- Work-package evidence notes for CDS-WP-001.

### Changed

- Work-package status advanced: CDS-WP-006 completed, CDS-WP-007 activated as
  the next work package. (CDS-WP-006)
- Decision index extended to DEC-S-001 … DEC-S-048 with a fifth decision type for
  governance, lifecycle and publication. DEC-S-001 … DEC-S-032 unchanged.
  (CDS-WP-006)
- Risk register extended to RISK-001 … RISK-040. **The provisional owner model
  was replaced by the finalized four-role model across all existing risks**; no
  existing description, assessment, or status was changed. (CDS-WP-006)
- Foundation Context Pack, project profile, project brain, and README extended
  with the governance roles, tracks, maturity states, claim types, risk
  ownership, publication state, and licensing model. (CDS-WP-006)
- Claude working instructions extended with the governance entry point, the
  Standard and Elevated track rule, the source conflict rule, claim and release
  boundaries, and the finalized risk roles. (CDS-WP-006)
- Work-package status advanced: CDS-WP-005 completed, CDS-WP-006 activated as
  the next work package. (CDS-WP-005)
- Decision index extended to DEC-S-001 … DEC-S-032 with a fourth decision type
  for logical architecture. DEC-S-001 … DEC-S-020 unchanged. (CDS-WP-005)
- Risk register extended to RISK-001 … RISK-028. The provisional owner model is
  unchanged. (CDS-WP-005)
- Foundation Context Pack, project profile, project brain, and README extended
  with the architecture layers, authority model, token flow, status invariants,
  and requirement coverage. (CDS-WP-005)
- Claude working instructions extended with the architecture entry point and a
  binding authority and conflict rule. (CDS-WP-005)
- Work-package status advanced: CDS-WP-004 completed, CDS-WP-005 activated as
  the next work package. (CDS-WP-004)
- Decision index extended to DEC-S-001 … DEC-S-020 with a third decision type
  for consumer and pilot scope. DEC-S-001 … DEC-S-012 unchanged. (CDS-WP-004)
- Risk register extended to RISK-001 … RISK-019. The provisional owner model is
  unchanged. (CDS-WP-004)
- Foundation Context Pack, project profile, project brain, and README extended
  with consumer evidence sources, requirement counts, pilot groups, and the
  hypothesis consumer layer. (CDS-WP-004)
- Claude working instructions extended with a binding consumer-repository
  read-only rule and the committed-evidence requirement. (CDS-WP-004)
- Work-package status advanced: CDS-WP-003 completed, CDS-WP-004 activated as
  the next work package. (CDS-WP-003)
- Risk register extended to RISK-001 … RISK-013. The provisional owner model is
  unchanged. (CDS-WP-003)
- Foundation Context Pack, project profile, project brain, and README extended
  with the benchmark scope, hypotheses, and the non-normative status of
  research. (CDS-WP-003)
- Claude working instructions note that `docs/research/` is evidence rather than
  a normative source. (CDS-WP-003)
- Project charter consolidated with the registered scope: capability domains,
  consumer classes, pilot boundary, and Foundation status; it now references
  the normative scope source instead of carrying its own scope list.
  (CDS-WP-002)
- Decision index extended to DEC-S-001 … DEC-S-012 and now distinguishes
  strategic foundation decisions from strategic scope decisions.
  DEC-S-001 … DEC-S-006 unchanged. (CDS-WP-002)
- Risk register extended to RISK-001 … RISK-009 with an explicit note that the
  risk owner model is provisional until CDS-WP-006. RISK-002 gained a
  cross-reference to the CoreOps pilot boundary without changing its meaning.
  (CDS-WP-002)
- Work-package status advanced: CDS-WP-002 completed, CDS-WP-003 next.
  (CDS-WP-002)
- README, project profile, project brain, and next-phase definition updated
  with the registered scope, consumer classes, register ranges, and the
  CDS-WP-003 boundaries. (CDS-WP-002)
- Claude working instructions updated with the context-pack and normative scope
  references and the current work-package pointers. (CDS-WP-002)
- Skills-first operating mode activated in the Claude working instructions,
  including selection, context-economy, authority-boundary, fail-closed, and
  Skill-maintenance rules. (CDS-WP-001A)
- Work-package status advanced: CDS-WP-001 and CDS-WP-001A completed,
  CDS-WP-002 next. (CDS-WP-001A)
- Project profile extended with NDF Skills version, count, status, source
  commit, and Skills-first operating mode. (CDS-WP-001A)
- README and project brain extended with the Skills-first operating mode and
  links to provenance and inventory. (CDS-WP-001A)
- Project profile extended with work-package status, register scope, and the
  intentionally open decision areas. (CDS-WP-001)
- Project brain restructured as a compact long-term orientation document.
  (CDS-WP-001)
- README updated with project status, pilot role, operating model, registers,
  and governance links. (CDS-WP-001)
- Claude working instructions rewritten for Claude Desktop with a locally
  connected repository. (CDS-WP-001)

### Removed

- `.claude/skills/.gitkeep` placeholder, superseded by the verified Skills
  adoption. (CDS-WP-001A)
