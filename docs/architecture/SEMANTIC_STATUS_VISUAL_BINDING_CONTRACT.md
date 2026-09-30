# Semantic Status Visual Binding Contract

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-023 — Semantic Status Visual Binding Contract
- **Date:** 2026-09-30
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for what a binding between Semantic Status meaning and a
  visual representation must be, may never be, and must declare**, and for the
  binding states, fail-closed behaviour, and downstream preconditions that follow —
  **upon the Human-Maintainer exact-object integration commit of the reviewed
  CDS-WP-023 object, and not before.** That condition was met by the commit
  **`0ea15ff080c377d7494876efdb6197404fa3cf40`** (tree
  `89fcc3d3b946ef3d7c90a856e86cb4dd2b80b8bc`), which integrated the CDS-WP-023
  execution object: **this document is normative from that commit.** Before it, the
  document was uncommitted executor output prepared under the explicit
  Human-Maintainer authorization of CDS-WP-023 for **execution only**.
  **`EXECUTION INTEGRATED ≠ WP CLOSURE EFFECTIVE`**: a separate closure reconciliation
  object is prepared in the Working Tree, and the CDS-WP-023 closure becomes effective
  only at the later Human-Maintainer exact-object integration commit of that closure
  object. **Successor: NONE.** **`EXECUTED ≠ ACCEPTED`**, **`PASS ≠ INTEGRATED`**, and
  **`INTEGRATED ≠ CLOSED`**.
- **Rework:** a **limited rework** (2026-09-30), authorized by the Human Maintainer
  after the independent review and Nova's adjudication *NO-GO FOR INTEGRATION —
  LIMITED REWORK REQUIRED*, corrected the authority classification, the binding-state
  model, domain-based completeness, the scope of RD-1, the Area 7 quotation, and the
  `Not Applicable` terminology. **It widened no scope and decided nothing outside the
  CDS-WP-023 contract boundary.**
- **Maturity:** **`Proposed`** — this document promotes nothing and grants no
  maturity to any artifact (DEC-S-036, VF-I-14).
- **Contract only.** It **creates no** visual role, role identifier, role
  vocabulary, visual value, icon, motion value, Theme or context identifier, Source
  Set, `sourceRevision`, alias, resolver instance, binding instance, mapping,
  schema, validator rule, test, fixture, renderer, component, or evidence, and it
  changes **no byte of the Semantic Status source**. It registers **no** Decision,
  ADR, or risk.

> **`STATUS MEANING ≠ VISUAL ENCODING` · `CONTRACT REQUIREMENT ≠ IMPLEMENTATION` ·
> `SEMANTIC OBLIGATION ≠ ROLE VOCABULARY` · `BINDING CLASS ≠ CONCRETE VALUE`**
>
> **COLOUR ≠ STATUS · ICON ≠ STATUS · MOTION ≠ STATUS · ELEVATION ≠ STATUS**

## Purpose and boundary

The [Semantic Status Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
defines **what status means**. The
[Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md) and the
[Visual Semantic Token Foundation](VISUAL_SEMANTIC_TOKEN_FOUNDATION.md) define **what a
visual role is**. Both deliberately leave one question open and route it here
(*Relationship to the Semantic Status Foundation*, **SS-7**, **CB-5**): **how a visual
role may be associated with a status meaning without becoming, replacing, or
distorting it.**

This document answers that question **as a contract** — at the level of **role
classes**, **semantic obligations**, **binding rules**, **redundancy requirements**,
**fail-closed constraints**, and **validation and rendering preconditions** — the
boundary fixed for CDS-WP-023 in the
[Post-Candidate Development Roadmap](../roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md),
*Phase S*.

It sits in **architecture Layer 3** and is consumed at **Layer 4**, where a component
contract applies a binding to a concrete representation (roadmap mapping *3 → 4*). It
introduces **no layer** (VF-I-1) and **no token-flow layer** (DEC-S-024).

### What this document is not

- **Not a mapping.** It binds **no** status value to **any** role, class instance,
  value, icon, or motion. Every statement below is a **requirement on a future
  binding**, never a binding.
- **Not a vocabulary.** It admits, reserves, recommends, and counts **no** role. The
  concrete Core visual-role vocabulary is **Route C**'s — a separately authorized
  role-vocabulary Decision Pass under **DEC-S-134** and **DEC-S-140** — and this
  document supplies **requirements** to it, never an answer (see *Requirements on
  the Route C vocabulary decision*).
- **Not validation or rendering.** It states what **CDS-WP-024** must be able to
  detect and which invalid-state categories **CDS-WP-025** must cover. It implements
  **no** check, authors **no** fixture, and defines **no** renderer behaviour.
- **Not a change to status meaning.** The five axes, their value vocabulary as it
  stands in the authoritative Semantic Status source revision *(25 values in all in
  the current revision — an informative count, not an invariant of this contract)*,
  the eleven-field status object, the ten invariants, the review-required combinations, the
  fail-closed conditions, and the disclosure priority are **unchanged** and are
  **applied** here.

## Authority basis — derived requirements and contract determinations

*(Normative. **This document registers no new Decision, ADR, or risk.** Its binding
statements are of **two kinds**, and the kind of each rule is stated below.)*

- **Derived requirement (D).** A requirement **directly compelled** by
  already-effective repository authority. The table *Derived requirements* names that
  authority; this document restates and applies it and adds nothing to it.
- **Contract determination (CD).** A normative choice this contract **makes itself**,
  inside the boundary CDS-WP-023 is authorized to fix — **role classes, semantic
  obligations, binding rules, redundancy requirements, fail-closed constraints, and
  validation and rendering preconditions** (roadmap *Phase S*, *CDS-WP-023
  boundary*). It is **not pre-decided** by an earlier Decision: the authority cited
  beside it **motivates** it and is **consistent** with it, but does not compel it. A
  contract determination binds **only as part of this contract**, from the
  effectivity of this contract, and changing it is an **Elevated** change (*Change
  classification*).

**`DERIVED ≠ DETERMINED`.** **DEC-S-023 is a conflict rule** — it governs how a
conflict between sources is handled. It is cited here **only where a source conflict
exists**, and **no contract determination is justified as a "conservative reading"
of DEC-S-023** where no conflict exists.

### Rule provenance

| Kind | Rules |
| --- | --- |
| **Derived requirement** | BM-2 … BM-6, BM-9, BM-10; BO-1 … BO-11; the **Excluded by existing authority** role-class rows; BE-4, BE-6; BR-1, BR-8 … BR-14; RD-1 … RD-3, RD-5 … RD-11; TI-2, TI-3, TI-5 … TI-10; BF-3, BF-6, BF-7, BF-9; VQ-1 … VQ-4, VQ-6 … VQ-9 |
| **Contract determination** | BM-1, BM-7, BM-8 (the revision-identification requirement; the non-transfer of evidence is derived); the **Bindable**, **Data** and **Not bindable under this contract** role-class categories; BE-1, BE-2, BE-3 (the placement of the change on the Elevated track is derived, DEC-S-033), BE-5 (as a binding rule; the *sole carrier* prohibition is derived); BR-2 … BR-7 (BR-3's prohibition on reading an omitted disposition as `no visual encoding` is derived, DEC-S-106); RD-4; TI-1, TI-4; the **binding-state model** and its fail-closed assignments BF-1, BF-2, BF-4, BF-5, BF-8, BF-10, BF-11; BP-1 … BP-8 as a precondition set; VQ-5, VQ-10; and the *Inputs to CDS-WP-024* and *Inputs to CDS-WP-025*, which follow from the rules they cite |

A rule marked **CD** may contain derived elements; the marker says that **the rule as
a whole is not compelled by earlier authority**. A rule marked **D** that this
document words more precisely than its source is **not** thereby a determination:
**where wording and source differ, the source wins** (DEC-S-022).

### Derived requirements

| This document's derived statements | Derive from |
| --- | --- |
| Status meaning is owned by the status contract; the visual foundation defines none | DEC-S-105, DEC-S-106, SS-1, VF-I-6 |
| Status meaning is textual and accessible first; every other modality is redundant | DEC-S-111, invariant 7, Communication Contract *Multi-modal contract*, SS-4, NC-1 … NC-3 |
| Degraded knowledge is never represented as success | DEC-S-107, invariants 3 … 6, SS-3 |
| No aggregate score, badge, traffic light, or percentage | DEC-S-108, invariant 2, Composition Rules *No aggregate score* |
| Downstream artifacts preserve axis distinction and truthfulness | DEC-S-112, invariant 9, TB-2, TB-3 |
| A visual role is a presentation role and never a status | VF-I-6, VF-I-7, NC-4, SS-2, SS-5, IC-2, SU-3 |
| A status name is never a visual role name | N-4, SN-2 |
| A semantic role never aliases another semantic role | **AL-2** |
| Semantic status tokens carry no appearance value | Semantic Status Token Contract *Semantic role boundary*, RISK-091 |
| The role classification is closed; the vocabulary is open; declaration is not materialization | **DEC-S-134** (RA-1 … RA-5), **DEC-S-140** |
| A theme re-binds and never redefines; a context difference is never a status difference | T-1, T-2, T-5, TC-1 … TC-7, CB-5 |
| Theme resolution mechanism, context evidence inputs, supported contexts, no default, fail closed, Theme `Not Applicable` | **DEC-S-137** (TM-1 … TM-12), **DEC-S-138** parts A … G, CF-1 … CF-11 |
| Forced colours is an environmental accessibility condition that binds independently of the Theme | **DEC-S-138** part B, baseline 3.5 |
| Channels may differ in form, never in meaning; limitations are declared | DEC-S-029, VF-I-11, PN-3, *The declaration obligation* |
| Contrast is a property of a pair, evaluated under WCAG 2.2 at full precision; no threshold is restated | DEC-S-129, CR-2, CR-3, SR-3, SR-4 |
| Motion and icon constraints | Motion boundary 1 … 6, IC-1 … IC-9, baseline 4.1, 4.5 |
| Evidence is revision-bound and never transfers | DEC-S-126, DEC-S-131, TM-7 … TM-10, SS-8 |
| Maturity is granted by a gate, never by a document | DEC-S-035, DEC-S-036, VF-I-14 |
| Conflicts fail closed; no automatic repair; recency never resolves | DEC-S-023, DEC-S-034 |
| An automated check is never sufficient accessibility evidence | DEC-S-053, EV-4 |

## Terms

*(Normative. A term not defined here keeps the meaning its source document gives it.)*

| Term | Meaning |
| --- | --- |
| **Status representation** | Any rendering, output, or artifact that asserts a status statement — some or all of the eleven fields of the complete status object — in any channel. |
| **Primary carriers** | The **text form** of every asserted axis value and its material qualifiers, and the **accessible-semantics form** (name / role / state or channel equivalent), both required by the *Multi-modal contract* of the [Status Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md). |
| **Visual status encoding** | Any visual modality — colour, shape, icon, motion, or other appearance — whose presentation **differs according to a status axis value**. It is always **redundant** to the primary carriers. |
| **Status Visual Binding** (*binding*) | A normative, revision-bound declaration that associates **status axis values** with **visual semantic roles** for the purpose of a visual status encoding. A binding is a **relation between two meanings owned elsewhere**; it owns neither. |
| **Binding entry** | One element of a binding: **exactly one** status axis value, identified by its technical identifier (`<axis>` and `<value>`, DEC-S-110), together with its **binding disposition**. |
| **Binding disposition** | What a binding entry declares for its axis value: **either** one or more **bound roles**, **or** the explicit disposition **`no visual encoding`**. An omitted disposition is **not** a disposition. |
| **Encoded axis** | An axis for which a binding contains at least one entry. A binding need not encode every axis. |
| **Encoding slot** | A position in a representation to which a bound role is applied — for example the ground, the boundary, or the foreground of a region. **Slots are defined by component contracts (Layer 4)**; this document names none and requires only that each slot be driven by one axis. |
| **Authoritative value domain** | For one axis, **the set of values that axis has in the Semantic Status source revision a binding is bound to** (BM-8). It is read from that revision, never restated here: **in the current authoritative vocabulary each axis has five values** — the *fixed initial five-value vocabulary* of **DEC-S-106**, whose change is a governed, Elevated change. **No rule in this document depends on that count.** |
| **Affirmative value** | The value invariant 3 names, for each axis, as never to be implied by `unknown`: **`condition: nominal`**, **`severity: none`**, **`confidence: verified`**, **`freshness: current`**, **`evidence: available`** — one per axis. |
| **Degraded-knowledge value** | Every **`unknown`**; **`freshness: stale`** and **`expired`**; **`confidence: unverified`**; **`evidence: partial`** and **`unavailable`** — the values DEC-S-107 and invariants 3 … 6 forbid to be represented as success. |
| **Material qualifier** | As listed in the Communication Contract *Status-summary qualifiers*: stale / expired freshness, unverified / unknown confidence, partial / unavailable / unknown evidence, and any `unknown` axis. |
| **Supported context** | A supported Core Theme Resolution Context under **DEC-S-138** part A — today `Light` and `Dark`, as human-readable architectural names only. **This document presupposes no count** (TC-6). |
| **Theme `Not Applicable`** | The **DEC-S-138** part G disposition that **Theme resolution does not apply** to a representation. It concerns **Theme resolution only**. It is **unrelated to** the Semantic Status axis value **`evidence: not-applicable`**, which is one value of the `evidence` axis's authoritative value domain, carries its own status meaning, and is subject to BR-3 like every other value. **The two are never equated, mapped to each other, or substituted for each other**, and neither implies anything about the other. |
| **Setting** | One evaluation setting of a bound element: **one Theme-resolution input, one channel, and one environmental condition**. The **Theme-resolution input** is **exactly one** of: (a) an **explicitly selected supported context**; (b) **no selected context** (*missing context*); (c) a requested context that is not a supported context (*non-supported context request*); (d) selection inputs in **unresolved equal-authority conflict**; or (e) **Theme `Not Applicable`**. (b), (c) and (d) arise only where Theme resolution applies, and (e) only where it genuinely does not (TI-8). **This domain is closed**: every evaluation of a bound element has exactly one setting. A setting is **not** a supported context: (b), (c) and (d) are settings in which resolution **Fails in setting** (BF-6). **A non-supported context request is never the setting-applicability outcome *Unsupported***, which is reserved for a **declared channel or environmental limitation** (BF-10); whether the channel and environmental condition can render the element decides between *Holds* and *Unsupported*, never whether the setting exists. |

These are **terms**, not identifiers. **No term above is a token path, a role name, a
Source Set, or a machine-readable key.**

## The binding model

*(Normative)*

| # | Rule |
| --- | --- |
| **BM-1** | **A binding is a relation, not a meaning.** It declares that, where a status representation chooses to carry a visual status encoding, a given axis value is encoded through given roles. It adds **no** status meaning, **no** visual meaning, and **no** Semantic Status value: it neither creates a value nor expands the **authoritative value domain** of any axis (*Terms*). **Values come only from the authoritative Semantic Status source revision** the binding is bound to (BM-8). |
| **BM-2** | **A binding is optional; the primary carriers are not.** A status representation is **complete as to status meaning** without any binding. **Removing every binding must remove no meaning** (SS-4, NC-2). |
| **BM-3** | **`BINDING ≠ ALIAS`.** A binding is **not** a token-to-token reference between a status token and a visual role, in either direction. A semantic status token aliasing a visual role, or a visual role aliasing a status token, is a **role-to-role alias** and is prohibited (**AL-2**). |
| **BM-4** | **A binding is never written into the Semantic Status source.** The `semantic/status` Source Set carries identity and meaning only, never an appearance value (Semantic Status Token Contract; RISK-091). A binding that required a change to a status source byte would require a **new status source revision**, with every consequence DEC-S-126 attaches — and is outside this contract. |
| **BM-5** | **A binding is never expressed through a role name.** No role acquires a status meaning by being named after an axis or a value, and no binding may be inferred from a name (N-4, SN-2). **The binding is the only place the association exists.** |
| **BM-6** | **A binding is keyed by technical identity.** Each entry names its axis and value by their stable, language-neutral technical identifiers (DEC-S-110) — never by a display label, a translation, or a visual description. |
| **BM-7** | **A binding is context-independent in identity and content.** The same entries and the same bound roles hold in **every** supported context; only the primitive a bound role resolves to may differ per context. See *Theme invariants*, **TI-1**. *(Contract determination, motivated by T-1, TC-1 and TC-2.)* |
| **BM-8** | **A binding is revision-bound.** It identifies the Semantic Status source revision whose values it binds and the Visual Source Set revisions whose roles it references. **Evidence about a bound representation never transfers across a change to any of them** (DEC-S-126, DEC-S-131, TM-9, TM-10). |
| **BM-9** | **A binding carries no maturity of its own and inherits none.** It registers **no** artifact family and **no** maturity unit. Whatever artifact carries a binding carries that artifact's maturity; the Semantic Status family's `Candidate` state and `AE1-CDS-WP016-SEMSTATUS-004` **do not transfer** to it (SS-8, AF-2), and **a construct that draws on several families matures no faster than its weakest constituent** (AF-4). |
| **BM-10** | **A binding covers the five status axes only.** A validation outcome, an interaction state, a selection state, a focus state, a risk tier, or a consumer domain state is **not** a status axis value and is **not** bindable under this contract (VF-I-7, IS-3, IS-4, CR-035). |

**The representation and ownership of a binding artifact are not decided here.** Where
a binding lives machine-readably — and which work package authors it — is an **open
question** (see *Open questions*, question 1), registered as the planning finding
**`F-023-01`** in the
[Post-Candidate Development Roadmap](../roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md).
**Every rule in this document binds whichever representation is later chosen.**

## Semantic obligations of a status representation

*(Normative. These are **not new** — they restate, as obligations a binding may never
defeat, what the status contract already requires of every representation.)*

| # | Every status representation that carries a visual status encoding must still | Source |
| --- | --- | --- |
| **BO-1** | Carry the **text form** of every asserted axis value and every material qualifier | DEC-S-111, Communication Contract |
| **BO-2** | Carry the **accessible-semantics form** of the status, and expose its changes to assistive technology | DEC-S-111, baseline 7.1, 7.6 |
| **BO-3** | Keep the **five axes independent** — no axis inferred from, merged with, or substituted for another | DEC-S-105, invariant 1 |
| **BO-4** | Never represent a **degraded-knowledge value** as an affirmative value | DEC-S-107, invariants 3 … 6 |
| **BO-5** | Never replace the axes with an **aggregate** signal | DEC-S-108, invariant 2 |
| **BO-6** | Keep `unknown` **explicit** — never an omitted default, never silence | DEC-S-106, Communication Contract |
| **BO-7** | Keep every **material qualifier** disclosed; a nominal condition never hides stale, unverified, or missing evidence | Composition Rules *Disclosure priority*, DEC-S-108 |
| **BO-8** | Offer a **path to the full five-axis disclosure** | Communication Contract *Status-summary qualifiers* |
| **BO-9** | Preserve **DE/EN semantic parity**; no visual encoding narrows, widens, softens, or upgrades the textual meaning | DEC-S-110, Communication Contract *DE/EN parity* |
| **BO-10** | Honour **reduced-motion** preferences without losing meaning | DEC-S-111, baseline 4.1, 4.5 |
| **BO-11** | Preserve meaning in **every channel**, declaring a limitation rather than dropping a distinction | DEC-S-029, invariant 9, VF-I-11 |

The [Visual Foundation Accessibility Mapping](../governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md),
*Area 7*, states:

> **"The visual foundation cannot make status honest. It can only fail to make it
> dishonest."**

*Applied here (a derived summary, not a quotation):* a visual status encoding cannot
make a status representation honest; it can only fail to make it dishonest. Every rule
that follows exists to prevent that failure.

## Role classes a binding may draw on

*(Normative as a **classification of the registered classes**. **No class is added**
(RA-4, DEC-S-134 clause 6), **no role is created**, and **no class is populated.**
The **Excluded by existing authority** rows are **derived requirements**; the
**Bindable**, **Data** and **Not bindable under this contract** categories are
**contract determinations** — the classification is this contract's, made within its
authorized boundary (*role classes*), and is motivated by, not compelled by, the
authority cited beside each row.)*

The registered semantic role classes are those consolidated in
[*Role classes by family*](VISUAL_SEMANTIC_TOKEN_FOUNDATION.md#role-classes-by-family).
Each falls into exactly one binding category:

| Category | Registered classes | Why |
| --- | --- | --- |
| **Bindable** | **VF-1 Feedback** | The only registered class whose **purpose** is *"presentation roles for outcomes and conditions communicated to a person"* — contrast-sensitive and **never the sole carrier** ([Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md), *Semantic colour role classes*). It remains a **presentation** class: it carries **no** axis meaning (NC-4, SS-5). |
| **Bindable in the data-visualization channel only — once its authority exists** | **VF-1 Data** | Registered for data-visualization encoding and **never the sole encoding channel**. **Data-visualization encoding is owned by CDS-WP-039** ([Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md), *Data-visualization colour*). **Until the required Data / data-visualization binding authority exists, no Data-class binding element is authorized**: a binding that contains one requires authority that does not exist and is **Invalid** (*Binding states*, binding validity). **This is missing design authority, not an unsupported channel or environment**, and it is never classified as **Unsupported**. This contract neither authorizes CDS-WP-039 nor performs any of its work. |
| **Excluded by existing authority** | **VF-1 Interaction**, **VF-1 Focus**, **VF-1 Emphasis**; the **focus role set**; the **component-independent state set** | An interaction, selection, pointer-emphasis, or focus state **is not a semantic status**, and conflating them *"destroys both"* (VF-I-7, SS-6, IS-1 … IS-5). The focus indicator has **no permitted mechanism of repurposing or removal** (F-1 … F-8). |
| **Excluded by existing authority** | **VF-6 Elevation role**, **VF-6 Surface hierarchy** | *"Depth is not status, not severity, and not priority"* (**SU-3**); **ELEVATION ≠ STATUS**. |
| **Not bindable under this contract** | **VF-1 Surface**, **Content**, **Boundary**; **VF-2** Heading, Body, UI, Editorial and document, Code and monospace, Numeric and data, Supporting, font-family role, weight role; **VF-3** Spacing role, Size role, Density model; **VF-5** Radius role, Border role, Separator role; **VF-6** Surface role, Overlay and scrim role | No registering architecture gives these classes a purpose of communicating conditions or outcomes. Several may *participate in meaning* where they declare a non-visual carrier (SR-5, SH-3, SP-2) — but **no effective authority makes them a status carrier**, and treating them as one would register scope by implication. **This is a contract determination**, following the CDS-WP-019 *positioned, not registered* precedent. **No source conflict exists here, so DEC-S-023 is not invoked.** Being **not bindable** is about **binding roles**: it does not by itself prohibit an independently authorized redundant perceptual modality, and it permits **no** status-dependent selection or variation of these roles (BE-2). |

| # | Rule |
| --- | --- |
| **BE-1** | **A bound role belongs to a Bindable class.** A binding entry that names a role of any other class is **Invalid**. |
| **BE-2** | **A non-bindable role is never a Semantic Status binding carrier, and is never varied by status value.** A role of any class outside the Bindable category **must not acquire Semantic Status meaning**, **must not be treated as an authorized Semantic Status binding carrier** — no binding names it (BE-1), and nothing declares, documents, or uses it as carrying a status value — and **must not be selected or varied according to a Semantic Status value merely to encode status meaning**. It may render the primary carriers and the representation's structure. **`BINDING ROLE ≠ REDUNDANT PERCEPTUAL MODALITY`** and **`REDUNDANT MODALITY ≠ UNGOVERNED SECOND BINDING`**: (a) a modality such as shape, pattern, border, or weight may participate in redundant perception **only where its status-dependent use is independently authorized by existing authority** — invariant 7, NC-1 … NC-3, RD-2 and RD-3 **permit** redundant modalities and constrain them, but authorize no particular realization; (b) **where a modality can be realized only through a non-bindable CDS role** — as border and weight are today, through the non-bindable **Border role** and **weight role** — **using that role as a status-dependent encoding requires separate, explicit authority**, which this contract does not grant and which no effective authority grants today; (c) a modality so authorized is never the sole carrier, acquires no status meaning, and **is not a binding and not a second status-to-role mapping mechanism** — **the Binding Contract remains the only CDS mechanism that associates a status value with a visual role** (BM-5). This contract **creates no mapping** from any status value to any modality and makes **no** modality, role, or class bindable (BE-3). *(Contract determination, motivated by SS-2, SS-5, NC-4 and VF-I-6.)* |
| **BE-3** | **Widening the Bindable category is an Elevated change** requiring Human-Maintainer approval (DEC-S-033). **CDS-WP-023 cannot widen it**, and neither can a vocabulary decision, a component contract, a Product Profile, or a consumer. |
| **BE-4** | **Icon and motion have no registered semantic role class.** The status contract permits them as redundant modalities (invariant 7), but **no construct exists to bind**: iconography is **CDS-WP-037**'s and the Motion System is **CDS-WP-035**'s. **Until the owning work package registers a construct, a binding may contain no icon or motion element** — an entry that names one references something that does not exist and is **Invalid** (*Binding states*). |
| **BE-5** | **Position and location are never the sole carrier, and not a binding role.** *Derived:* position or location **must not be the sole carrier** of Semantic Status meaning (baseline 3.7, WCAG 1.3.3), and a spatial context carries no meaning (**CX-4**, DEC-S-136). *Contract determination:* position **must not become a Semantic Status binding role** without separate authority — no registered role class represents it. **Existing authorized layout and location behaviour is not globally prohibited** by this rule, including the disclosure priority, which orders **attention** through composition at Layers 4 and 5 and is **not** a binding. **This contract introduces no positional status encoding.** |
| **BE-6** | **A Theme Resolution Context and an environmental condition are never a binding modality.** Nothing may be communicated by which context is active (T-5, TC-5, CE-2). |

**Being Bindable is not being demanded.** Whether any Feedback or Data role exists at
all is decided **only** by an effective Route C vocabulary decision under **RA-1**
(*Requirements on the Route C vocabulary decision*). **If none is admitted, no
binding can exist — and every status remains fully representable through its
primary carriers.**

## Binding rules

*(Normative — each rule applies to **every** binding, in **every** channel and
**every** supported context.)*

| # | Rule |
| --- | --- |
| **BR-1** | **One entry, one axis value.** A binding entry binds **exactly one** axis value. An entry keyed on a combination of axis values is an **aggregate** and is **Invalid** (DEC-S-108, invariant 2). |
| **BR-2** | **One slot, one axis.** The presentation of any encoding slot may depend on **at most one** axis. A slot whose presentation is a function of two or more axes fuses them into one signal and is **Invalid**. *(Contract determination, motivated by BO-3, BO-5 and TB-3, which forbid merging axes and aggregate signals but do not themselves fix a per-slot rule.)* |
| **BR-3** | **An encoded axis is encoded completely.** For every encoded axis, **every value in that axis's authoritative value domain** — as it stands in the Semantic Status source revision the binding is bound to (BM-8) — carries an explicit binding disposition: a bound role, or **`no visual encoding`**. **Completeness is measured against that domain, never against a count**; the current authoritative vocabulary has five values per axis (DEC-S-106, *initial*), and a later governed vocabulary revision changes the domain the rule reads, not the rule. **A missing disposition is never read as `no visual encoding`**: that reading would give `unknown` an implicit default, which **DEC-S-106** forbids *(derived)*. *(The completeness requirement itself is a contract determination.)* |
| **BR-4** | **An affirmative disposition is exclusive.** Within an encoded axis, the disposition of the **affirmative value** may be shared with **no** other value of that axis — including the disposition `no visual encoding`. Otherwise the other value is visually represented **as** the affirmative value (BO-4). *(Contract determination, motivated by DEC-S-107 and invariants 3 … 6, which forbid representing degraded knowledge as affirmative; this contract determines that sharing an affirmative presentation is such a representation. No source conflict exists, and DEC-S-023 is not invoked.)* |
| **BR-5** | **Degraded knowledge never shares affirmative presentation.** As a direct consequence of BR-4, no **degraded-knowledge value** may share a disposition with the affirmative value of its axis. This is stated separately because it is the failure CR-006 and CR-007 exist to prevent. |
| **BR-6** | **Other shared dispositions are declared.** Two non-affirmative values of the same axis may share a disposition only if the binding **declares** that its visual encoding does not distinguish them. The primary carriers still do. *(Contract determination, motivated by the declaration obligation, VF-I-11.)* |
| **BR-7** | **Qualifier interaction is declared.** For every bound role applied to an **affirmative value**, the binding declares how the representation behaves when **another axis carries a material qualifier**. A success-reading presentation must never imply `verified`, `current`, or `nominal` where those axes do not carry it (Colour Architecture, *Interaction, feedback and state colour*; review-required combination 6). **An undeclared qualifier interaction makes the binding Incomplete.** This contract selects **no** behaviour; it requires one to be declared and to satisfy BO-4 and BO-7. *(The prohibition on implying `verified`, `current` or `nominal` is derived — SS-5, NC-4; the declaration requirement is a contract determination.)* |
| **BR-8** | **Every bound role declares its obligations.** A role may be bound only if it carries, in full, the declarations **SR-1 … SR-12** (RA-3, DEC-S-140) — in particular **SR-3** and **SR-4** (its contrast obligation and pairing set, evaluated under **WCAG 2.2** at full precision, DEC-S-129), **SR-5** (it participates in meaning, and its non-visual carrier is the status **primary carriers**), **SR-6** (reduced-colour behaviour, including forced colours), and **SR-9** (channel availability and degradation). |
| **BR-9** | **Bound roles are referenced, never embedded.** A binding names roles; it holds **no** raw value, primitive, or literal (AL-1, VF-I-3). |
| **BR-10** | **No interaction, focus, or selection reuse.** A binding never binds a role that also serves an Interaction, Focus, or Emphasis purpose, and never alters a focus indicator (BE-1, F-4 … F-7). |
| **BR-11** | **No rank by encoding.** A binding asserts **no** ranking, priority, or importance through visual salience; the **disclosure priority** remains the only normative attention ordering and is **never a semantic override** (Composition Rules, N-7, SN-7). |
| **BR-12** | **No contradiction.** A visual status encoding never contradicts, extends, or reinterprets the text form it accompanies. **Redundancy is additive; contradiction is a defect** (Communication Contract *Multi-modal contract*). |
| **BR-13** | **No Product Profile or consumer re-binding.** A Product Profile may vary a **value** at a named, approved extension point and may never rename, merge, remap, or reweight a status meaning (DEC-S-025, DEC-S-112, invariant 10). **No extension point is named today** (SR-10), so **no binding can be varied by a profile today**. A consumer re-binding outside that route is a consumer-local artifact and is **not** a CDS binding (PN-5). |
| **BR-14** | **Review-required combinations stay review-required.** A binding cannot convert a review-required combination into a freely representable one, and cannot render a fail-closed status statement as though it were valid. **A status that cannot be validated must not be rendered as though it were** (SS-7). |

## Redundancy and accessibility rules

*(Normative. **No rule mandates every modality for every status.** The minimum is the
primary carriers; everything else is optional, redundant, and constrained.)*

| # | Rule | Source |
| --- | --- | --- |
| **RD-1** | **The primary carriers are mandatory, and sufficient for status meaning only.** Every status representation carries the text form and the accessible-semantics form of every asserted value and qualifier, **with or without** a binding. Where **no optional visual binding** is present, text plus accessible semantics **may be sufficient to communicate the Semantic Status meaning**. **`SUFFICIENT FOR STATUS MEANING ≠ SUFFICIENT FOR EVERY OBLIGATION`**: this sufficiency **never** reads as satisfying the disclosure obligations (**BO-7**, **BO-8**), interaction and keyboard obligations, component-specific requirements, or any other existing consumer, component, interaction, or accessibility obligation — each continues to bind under its own authority. | DEC-S-111, BO-1, BO-2 |
| **RD-2** | **Visual encoding is never the sole carrier**, in any channel, including greyscale print, exported diagrams, and presentations at distance. | invariant 7, VF-I-5, NC-1, NC-5 |
| **RD-3** | **Non-text carriers do not satisfy each other.** Colour plus icon, colour plus shape, or any combination of sensory modalities **without** the text form is still sensory-only encoding, and the representation **fails closed** (BF-3). | NC-3, DEC-S-111, 1.3.3 |
| **RD-4** | **Hue-only differentiation is declared.** Where a binding distinguishes values of an axis by hue alone, it declares that its visual encoding does not distinguish them under colour-vision differences, greyscale, and monochrome print. The primary carriers carry the distinction. *(Contract determination.)* | Motivated by Colour Architecture *reduced-colour conditions*, SR-6, CR-6 |
| **RD-5** | **Forced colours are honoured, not fought.** A binding **must not depend** on its colour encoding surviving forced colours or platform high contrast. It declares its behaviour under that condition, which **binds independently of the selected Theme** and is **outside Theme precedence**. | **DEC-S-138** parts B and D, baseline 3.5, SR-6 |
| **RD-6** | **Reduced motion removes no meaning** — and today no motion element is bindable at all (BE-4). | BO-10, Motion boundary 1 and 2 |
| **RD-7** | **Nothing flashes.** No visual status encoding may flash above threshold. | 2.3.1 (CDS-alone), Motion boundary 3 |
| **RD-8** | **Changes are not visible-only.** A status change carried by a visual status encoding is also carried by the primary carriers and exposed to assistive technology. | baseline 7.6, BO-2 |
| **RD-9** | **Loss of a visual channel is declared.** Where a channel cannot render a bound role, the limitation is **declared in that channel's record**, the meaning stays with the primary carriers, and the output is **not** shipped as though the encoding were present. | VF-I-11, *The declaration obligation* |
| **RD-10** | **Contrast is a property of a declared pair in a context.** A bound role's contrast obligation is evaluated against its declared pairings, under WCAG 2.2, in every supported context. **CDS restates no threshold and invents none.** | DEC-S-129, CR-2, CR-3, TC-3 |
| **RD-11** | **Distinguishability is two statements, not one.** *Structurally distinct* — resolved presentations are not identical — is checkable from sources. *Perceptibly distinct* — a person can tell them apart — requires rendering and assistive-technology evidence. **`STRUCTURALLY DISTINCT ≠ PERCEPTIBLY DISTINCT`**, and only the second can support any accessibility statement. | DEC-S-053, EV-4, CDS-WP-031 |

## Theme invariants

*(Normative — applying **T-1 … T-10**, **TC-1 … TC-7**, **DEC-S-137** and **DEC-S-138**.
**No Theme, context identifier, or context-specific value is created.**)*

| # | Invariant |
| --- | --- |
| **TI-1** | **Invariant across every supported context:** the binding's entries, its dispositions, its bound roles, its declared obligations and declarations, the primary carriers, and the status meaning. **A binding that differs by context is Invalid** — a context-specific binding is a different binding. *(Contract determination, motivated by **T-1**, **TC-1** and **TC-2** — a context re-binds a role's primitive and never its identity or meaning — and by **T-5** and **TC-5** — no status difference is expressed by a context difference. Those rules govern roles and contexts; they do not themselves address bindings, so this invariant is determined here.)* |
| **TI-2** | **May vary across supported contexts:** only the **reference primitive** each bound role resolves to, through the Resolver / Composition architecture (**TM-1**), subject to TI-3 … TI-5. |
| **TI-3** | **Obligations hold in every supported context.** Every declared contrast obligation and pairing of a bound role holds in every supported context (**T-3**, **TC-3**); a context in which one does not is a **contract break**, not a context difference, and **fails closed in that context** (CF-3; *Binding states*, setting applicability). |
| **TI-4** | **Affirmative exclusivity holds after resolution.** In every supported context, the resolved presentation of an affirmative value's disposition is **not identical** to the resolved presentation of any other value's disposition on the same axis. A context in which they collapse violates BR-4 **in that context** — a **setting failure**, not a binding-validity outcome (*Binding states*). *(Contract determination, extending BR-4 to resolved presentations.)* |
| **TI-5** | **Recognisability is carried by the text, not by the colour.** When the visual implementation changes between contexts, the status remains recognisable **because the primary carriers do not change**. A binding must not depend on a person recognising a status by the same appearance across contexts. |
| **TI-6** | **No context difference is a status difference.** No status, state, or severity is expressed by which context is active (**T-5**, **TC-5**, **CB-5**). |
| **TI-7** | **No default, no fallback, no substitution.** A Theme-applicable resolution of a bound role requires an **explicitly selected supported context**; a missing context, a non-supported context request, or a conflicting context (*Terms*, **Setting**) **fails closed** (**CF-1**, **CF-9**, **CF-11**), with **no silent substitution** to `Light`, `Dark`, or anything else (**DEC-S-138** parts E and F). |
| **TI-8** | **Theme `Not Applicable` is honest inapplicability only.** Where Theme resolution genuinely does not apply to a representation, Theme `Not Applicable` is recorded — a Theme-resolution disposition, **never** the status value `evidence: not-applicable` (*Terms*); it is **never** a hidden Theme, a fallback, or a way to avoid a fail-closed condition that does apply (**DEC-S-138** part G). |
| **TI-9** | **The binding presupposes no context count.** It must remain valid whether CDS supports two contexts or more, including a future dedicated High-Contrast Theme should one ever be separately authorized (**TC-6**, **CA-13**, **DEC-S-138** part B clause 11). |
| **TI-10** | **Theme and spatial context stay orthogonal.** No spatial context selects, modifies, or feeds a binding's Theme resolution (**TM-11**, **CB-2**). Joint Theme × Spatial evaluation of a bound representation stays **deferred** (**TM-12**). |

## Binding states

*(Normative. **Contract determination** — the evaluation model is this contract's,
made within its authorized boundary (*fail-closed constraints*); the fail-closed
behaviour it applies is derived from DEC-S-023, DEC-S-034, DEC-S-107, DEC-S-138 and
CF-1 … CF-11. **Four different subjects are classified, each on its own
classification.** An outcome of one classification is **never** an outcome of
another, and **no outcome substitutes for another**.)*

| Subject | Classification | Outcomes |
| --- | --- | --- |
| **A binding** — evaluated from sources, **once**, independent of any context, channel, or representation | **Binding validity** | **Valid** · **Incomplete** · **Invalid** |
| **One axis of a status representation** — whether a Valid binding encodes it | **Axis disposition** | **Bound** · **Missing** |
| **One bound element of a Valid binding in one setting** (*Terms*) — one Theme-resolution input, one channel, and one environmental condition | **Setting applicability** | **Holds** · **Unsupported** · **Fails in setting** |
| **One consumer or renderer output** of a status representation | **Output deviation** | **Implementation error** — or none |

**Evaluation is deterministic, in this order:**

1. **Binding validity** is evaluated for every binding a representation applies. **A
   binding that meets any Invalid condition is Invalid**, even if it also meets an
   Incomplete condition; a binding that meets an Incomplete condition and no Invalid
   condition is **Incomplete**; a binding that meets neither is **Valid**.
2. **Axis disposition** is assigned **only** where the representation applies **no**
   binding to the axis (**Missing**), or applies a **Valid** binding — which then
   encodes the axis (**Bound**) or does not (**Missing**). **Where the representation
   applies an Incomplete or Invalid binding, the axis receives no disposition: the
   visual-binding use fails closed** (BF-2, BF-4). A representation *applies* a
   binding when it — or the component contract it realizes — declares that binding as
   the source of its visual status encoding.
3. **Setting applicability** is evaluated **only** for the elements of a **Valid**
   binding on a **Bound** axis, once per setting (*Terms*, **Setting**).
4. **Output deviation** is evaluated for any output, whatever the outcomes above.

**Evaluation is per applied binding.** Where a representation applies more than one
binding, **binding validity is evaluated separately for each applied binding**, and
**each binding contributes axis disposition only for the axis or axes it governs** —
the axes to which the representation applies it. **A Valid binding keeps its
otherwise-valid disposition** for the axes it governs even where a **separate** binding
applied to another axis is Incomplete or Invalid. **An Incomplete or Invalid binding
contributes no axis disposition** for the axes it governs, and its visual-binding use
fails closed (step 2). **The representation still obeys every fail-closed consequence
of that binding**: an Invalid or Incomplete binding blocks every **visual output
resolved from that binding**, according to the fail-closed rules (*Binding validity*,
BF-2, BF-4), and a Valid binding applied to another axis neither overrides nor relaxes
that consequence. **That blocking is a consequence for the visual outputs resolved from
the failing binding; it is not a judgement on any other binding.** A separate Valid
binding for another axis **does not become Invalid** because another binding is Invalid
or Incomplete, and **the blocking weakens no rule in BF-1 … BF-11** — in particular,
BF-4 is unchanged. **No representation-level aggregate** of binding validity, axis
disposition, or setting applicability **exists or may be derived** — the axes stay
independent, and no aggregate status signal is created (BO-3, BO-5).

### Binding validity

| Outcome | Definition | Effect |
| --- | --- | --- |
| **Valid** | A binding that satisfies every rule in this document and references only admitted and materialized roles of a Bindable class. **Validity is structural and context-independent**; whether the binding can be satisfied in a given setting is **setting applicability**, never validity. | May be used **once the realization preconditions are met** (*Realization and rendering preconditions*), in each setting where it **Holds**. Being Valid is **not** evidence and grants **no** accessibility statement. |
| **Incomplete** | A binding that omits a required disposition (BR-3), a required declaration (BR-6, BR-7, BR-8, RD-4, RD-5), or a required revision binding (BM-8, BF-11). | **Fails closed.** Not distributable, not renderable as a CDS binding. **No automatic completion** — in particular, an omitted disposition is **never** filled with `no visual encoding` — and **no degradation to Missing** (*Axis disposition*). |
| **Invalid** | A binding that contradicts semantic authority or this contract: aggregation (BR-1, BR-2); a shared affirmative disposition (BR-4, BR-5); a non-Bindable class (BE-1); a non-bindable role treated as a binding carrier (BE-2); an unregistered construct (BE-4); **a Data-class element before the required data-visualization binding authority exists** (*Role classes*, Data); context variance (TI-1); contradiction (BR-12); an interaction or focus reuse (BR-10); a non-status state (BM-10); a profile or consumer re-binding (BR-13); or an unknown, unadmitted, or unmaterialized reference (BF-7, BF-9). | **Fails closed — in every setting**, because the defect is structural and independent of context. Blocks distribution of the binding and rendering of every visual output resolved from that binding. **No automatic repair, no nearest match, no substitution, and no degradation to Missing**; the defect is recorded and escalated. A conflict between a class-1 meaning source and a class-2 value source **invalidates the affected artifact state** (DEC-S-034, CF-10), and recency never resolves it (DEC-S-023). |

### Axis disposition

| Outcome | Definition | Effect |
| --- | --- | --- |
| **Bound** | The representation applies a **Valid** binding that encodes the axis. | The axis carries a visual status encoding **in addition to** its primary carriers, subject to **setting applicability** in each setting. |
| **Missing** | The representation applies **no** binding to the axis — none exists, none is applied, or the applied **Valid** binding does not encode that axis. *(An encoded axis with an omitted value makes the binding **Incomplete** — BR-3 — and never produces Missing.)* | The status is represented through its **primary carriers only**, with **no** visual status encoding — **the status contract's own form, complete as to status meaning** (BM-2, RD-1), where existing authority permits it. **No encoding is invented, and no other role or binding is substituted.** It is **not** an error of the status statement. |

**`MISSING ≠ FALLBACK`.** **Missing is never a fallback from an Invalid or Incomplete
binding.** An **Invalid** binding **must not degrade** to Missing or to a
primary-carriers-only presentation as automatic repair, and neither may an
**Incomplete** one: **their visual-binding use fails closed**, with **no fallback
value, no role substitution, and no implicit repair**. Missing arises **only** where no
binding is applied, or a Valid binding does not encode the axis. **A failure never
produces it**; a representation reaches Missing for a previously bound axis only by a
separate, deliberate authoring change that stops applying the binding — reviewed like
any other change — never as a consequence of the failure.

### Setting applicability

| Outcome | Definition | Effect |
| --- | --- | --- |
| **Holds** | In that setting the bound element resolves under an explicitly selected supported context (or Theme resolution does not apply), its declared obligations and pairings hold (TI-3), affirmative exclusivity holds after resolution (TI-4), and the channel and environmental condition can render it. | May be rendered in that setting, **once the realization preconditions are met**. |
| **Unsupported** | A **channel or environmental condition** cannot render the bound element — for example colour in greyscale print, or a colour encoding under forced colours (RD-5) — **and the limitation is declared** in that channel's own record. | **A declared limitation, not a failure**: the primary carriers remain, and the output is **not** shipped as though the encoding were present (RD-9, VF-I-11). **An undeclared drop is an Implementation error**, never Unsupported. **Unsupported never describes missing design authority**: a binding element that requires authority which does not exist makes the binding **Invalid** (*Binding validity*). |
| **Fails in setting** | In that setting the binding **cannot be satisfied**: a bound role cannot resolve (CF-2), a declared obligation or pairing breaks (TI-3, CF-3), or affirmative exclusivity collapses after resolution (TI-4); or, where Theme resolution applies, the setting's Theme-resolution input is a **missing context**, a **non-supported context request**, or selection inputs in **unresolved conflict** (*Terms*, **Setting** (b) … (d); TI-7, CF-1, CF-9, CF-11). | **Fails closed for that bound element's use in that setting**, and the failure is **declared**, never silent (**CF-2**, **CF-3**). **No other context is substituted**, no context-specific alternative binding is created, and the declaration does not make the resolution succeed. **It does not by itself invalidate the binding or its use in any other setting** in which the binding Holds — no effective authority requires global invalidation for a context-specific failure — **but** it is raised as a defect against the binding or the role: *"if a role only works in one context, the role is wrong"* (**T-10**). Where the failure is a **class-1 / class-2 source conflict**, DEC-S-034 governs instead and invalidates the affected artifact state (CF-10). |

### Output deviation

| Outcome | Definition | Effect |
| --- | --- | --- |
| **Implementation error** | A consumer or renderer output that deviates from a Valid binding or from the primary-carrier obligations — a different role; a dropped primary carrier (BF-3); a substituted context; a non-bindable role used as a status binding carrier, or selected or varied according to a status value without separate, explicit authority (BE-2); a bound element dropped in a channel **without** a declared limitation (BF-10); or an Invalid or Incomplete binding rendered as though it were Missing. | **Not a binding outcome.** It is a property of the **output**, never inferred from the binding, and the binding's validity is unchanged. The deviating output is **not** a CDS-sanctioned representation, supports **no** claim, and is handled as a consumer defect under the [Accessibility Defect and Regression Model](../governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md) and the consumer contract. |

### Fail-closed rules

*(Normative)*

| # | When | Then |
| --- | --- | --- |
| **BF-1** | **No binding is applied to an axis**, or the applied Valid binding does not encode it | Axis disposition **Missing**. Primary carriers only; no invented, borrowed, or default encoding. **BF-1 never applies to an axis whose applied binding is Incomplete or Invalid** (BF-2, BF-4). |
| **BF-2** | **A binding is incomplete** | Binding validity **Incomplete** — fail closed; no automatic completion; **no degradation to Missing**, no fallback value, no role substitution. |
| **BF-3** | **A required primary carrier is missing** from a representation that carries a visual status encoding | **Implementation error** of the output, and the **representation** fails closed: it may not ship as a status representation. **No binding compensates for a missing text or accessible-semantics form** (RD-1, RD-3). |
| **BF-4** | **A binding contradicts semantic authority or this contract** | Binding validity **Invalid** — fail closed in every setting and escalate; **no degradation to Missing**, no fallback value, no role substitution; recency never resolves a source conflict (DEC-S-023, DEC-S-034). |
| **BF-5** | **A supported context cannot satisfy a Valid binding** (TI-3, TI-4, CF-2) | Setting applicability **Fails in setting** — **for that bound element's use in that context only**, declared, never silent (**CF-2**, **CF-3**). **No other context is substituted, no context-specific alternative binding is created, and the declaration does not make the resolution succeed.** Uses in other supported contexts where the binding Holds are **not** invalidated by it; the failure is raised as a defect against the binding or role (**T-10**). |
| **BF-6** | **The setting's Theme-resolution input is a missing context, a non-supported context request, or an unresolved conflict** where Theme resolution applies (*Terms*, **Setting** (b) … (d)) | Setting applicability **Fails in setting** under **CF-1**, **CF-9**, **CF-11** — never *Unsupported*; no default, no fallback. |
| **BF-7** | **A downstream consumer encounters an unknown axis, value, role, class, or construct** in a binding | Fail closed. **Not interpreted, not approximated, not mapped to a nearest match, not defaulted.** An unknown status value is already fail-closed condition 2 of the Composition Rules. |
| **BF-8** | **A role admitted by a future vocabulary decision has no authorized binding** | It is **not** a status encoding. A binding that names it without the vocabulary decision recording it as intended to be bindable (VQ-10) is **Invalid**; an output that varies it by status value without an authorized binding is an **Implementation error**. The axis disposition stays **Missing** (BF-1). |
| **BF-9** | **A binding references a role not admitted by an effective vocabulary decision, or not materialized in an authorized Source Set revision** | Binding validity **Invalid** — fail closed (**DEC-S-140** clause 12, AL-4). |
| **BF-10** | **A channel or environmental condition cannot render a bound element** | Setting applicability **Unsupported** if and only if declared (RD-9); an undeclared drop is an **Implementation error** of the output. |
| **BF-11** | **The Semantic Status source revision or a referenced Visual Source Set revision changes** | The binding must be **re-bound** to the new revisions — including the authoritative value domain of each encoded axis (BR-3) — and **re-evaluated**; evidence about the previous binding **does not transfer** (BM-8, DEC-S-126, TM-9). Until then the binding is **Incomplete** for the new revision. |

**`FAIL CLOSED ≠ DEGRADED OUTPUT`.** Failing closed never produces a partially bound,
nearest-match, or best-effort visual encoding, **and never produces Missing**. **The
Missing disposition is not a degradation of a binding** — it is the absence of one,
and the status contract's primary carriers are complete **as to status meaning** on
their own (RD-1).

## Realization and rendering preconditions

*(Normative. **Answers the question *"may implementation proceed?"*
deterministically — and today the answer is **no**.**)*

A concrete binding instance may be **authored**, and a bound representation may be
**rendered as a CDS visual status encoding**, **only when every precondition below
holds**. Each is independent; satisfying one satisfies none of the others.

| # | Precondition | State today |
| --- | --- | --- |
| **BP-1** | This contract is **effective** at a Human-Maintainer exact-object integration commit | **Met** — the CDS-WP-023 execution object, including this contract, was integrated at the Human-Maintainer exact-object commit `0ea15ff080c377d7494876efdb6197404fa3cf40`. **`EXECUTION INTEGRATED ≠ WP CLOSURE EFFECTIVE`** — BP-1 does not depend on the closure, and meeting it satisfies no other precondition |
| **BP-2** | Every bound role is **admitted by an effective Route C vocabulary decision**, in a Bindable class, satisfying *Requirements on the Route C vocabulary decision* | **Not met** — no vocabulary decision exists; **VP-6 is `UNSATISFIED`** |
| **BP-3** | Every bound role is **materialized** in an authorized Visual Source Set revision with **SR-1 … SR-12** in full, and every value it resolves to satisfies **VP-1 … VP-7** | **Not met** — visual Source Sets **0**, visual values **0**; **VP-3, VP-5, VP-6, VP-7 `UNSATISFIED`** |
| **BP-4** | **Context-conditional realization is representable** — **`F-022-01` / Route D** resolved under its own authorization | **Not met** — routed, undecided (DEC-S-140 clause 12) |
| **BP-5** | The **representation and ownership of a binding artifact** are decided by a separately authorized act | **Not met** — open and unresolved (*Open questions*, question 1; roadmap finding **`F-023-01`**) |
| **BP-6** | **CDS-WP-024** defines the render gate and implements the detections in *Inputs to CDS-WP-024* applicable to the binding; **an unrun check is `Not assessed`, never assumed passed** | **Not met** — CDS-WP-024 `Planned`, not authorized |
| **BP-7** | **CDS-WP-025** covers the invalid-state categories in *Inputs to CDS-WP-025* with negative fixtures | **Not met** — CDS-WP-025 `Planned`, not authorized |
| **BP-8** | The work package that authors the binding is **separately authorized** by the Human Maintainer | **Not met** — none is authorized |

**`CONTRACT READY ≠ BINDING AUTHORIZED`**, **`VALID ≠ RENDERABLE`**, and
**`RENDER GATE PASSED ≠ ACCESSIBLE`**. Meeting BP-1 … BP-8 permits a binding to be
authored and rendered; it supports **no** accessibility statement, which requires
rendering and assistive-technology evidence (**CDS-WP-031**) that does not exist.

**Channels bound further.** Meeting BP-1 … BP-8 lifts no channel gate: in a channel
whose accessibility profile is undefined — PDF and reports, presentations, release
materials, selected communication materials, and exported diagrams and
visualizations — a bound output **cannot reach Candidate or Stable** until that
channel's profile exists (DEC-S-058, [Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md)).

## Requirements on the Route C vocabulary decision

*(Normative **requirements**, supplied to the separately authorized role-vocabulary
Decision Pass (**Route C**) under **DEC-S-134** and **DEC-S-140**. **They choose
nothing.** They do not admit, reserve, recommend, name, or count any role, and
**Route C may conclude that no bindable role is admitted.**)*

| # | Requirement |
| --- | --- |
| **VQ-1** | **RA-1 is unchanged.** This contract is **not** evidence of cross-consumer need for any role. **CR-006** is evidence that status must never be colour-only — **not** a demand for visual roles (DEC-S-134 rationale) — and **`WCAG OBLIGATION ≠ CROSS-CONSUMER EVIDENCE`** (DEC-S-140 clause 9). **`BINDING CONTRACT ≠ ROLE DEMAND`.** |
| **VQ-2** | A role intended to be bound under this contract belongs to a **Bindable class** (BE-1). Admitting a role of another class **for a binding purpose** requires the Elevated change BE-3 first. |
| **VQ-3** | Its **purpose** (SR-2) is a **presentation purpose**, never a status meaning (SS-5, NC-4). |
| **VQ-4** | Its **name** reuses no axis or value name and implies no equivalence with one (N-4, SN-2), and states a purpose, not a rank (N-7, SN-7). |
| **VQ-5** | **The vocabulary does not mirror the status vocabulary.** A role set structured as a one-to-one counterpart of the axis values would be an alternative status vocabulary in visual form, which **IC-2**'s principle, **SS-2** and **BM-5** exclude. A role's justification is its presentation purpose under RA-1, never the existence of a status value. *(Contract determination, motivated by SS-2, BM-5 and IC-2's principle.)* |
| **VQ-6** | Its **SR-5** declaration states that it participates in conveying meaning and names the status **primary carriers** as its non-visual carrier. |
| **VQ-7** | Its **SR-3**, **SR-4**, **SR-6** and **SR-9** declarations are complete — including its pairings, its behaviour under greyscale, monochrome print and forced colours, and its channel availability — **from admission** (RA-3, DEC-S-140 clause 8). |
| **VQ-8** | Its identity and meaning are **context-independent**, and its obligations are declared to hold in **every** supported context without presupposing their count (TC-1, TC-2, TC-6). |
| **VQ-9** | It is **distinct from** every Interaction, Focus and Emphasis role and serves none of their purposes (BR-10, VF-I-7). The **IS-5** disposition of `selected`, `active` and `current` is **unchanged** by this contract. |
| **VQ-10** | Route C records, for each role it admits, **whether it is intended to be bindable** under this contract. **An admitted role is not bindable by default** (BF-8). *(Contract determination — a requirement this contract supplies to Route C; it decides nothing for Route C.)* |

**A requirement is not a vocabulary.** If Route C cannot satisfy these requirements
for any role, the correct result is **no bindable role** — not a relaxed requirement.
Relaxing any requirement here is an Elevated change to this contract.

## Inputs to CDS-WP-024

*(Stated as **requirements on CDS-WP-024**, which is `Planned`, not active, and not
authorized. **No validator, schema, rule, diagnostic, test, or fixture is created or
changed here.**)*

A later semantic validation and render gate must be able to **detect**, structurally:

| # | Must detect | Derived from |
| --- | --- | --- |
| 1 | A binding entry keyed on **more than one** axis value | BR-1 |
| 2 | An encoding slot whose presentation depends on **more than one axis** | BR-2 |
| 3 | An encoded axis **lacking an explicit disposition for any value of its authoritative value domain** in the bound Semantic Status source revision | BR-3 |
| 4 | An **affirmative disposition shared** with any other value of its axis | BR-4, BR-5 |
| 5 | A **shared non-affirmative disposition** without its declaration | BR-6 |
| 6 | An affirmative disposition with **no declared qualifier interaction** | BR-7 |
| 7 | A bound role **missing any of SR-1 … SR-12** | BR-8, RA-3, DEC-S-140 |
| 8 | A bound role of a **non-Bindable class** | BE-1 |
| 9 | A binding element in a **modality with no registered construct** (icon, motion), or a **Data-class element before the required data-visualization binding authority exists** | BE-4, *Role classes* (Data) |
| 10 | A **non-bindable role declared, documented, or used as a Semantic Status binding carrier**; declared as carrying a status meaning; or **declared as selected or varied according to a Semantic Status value** without citing the separate, explicit authority BE-2 (b) requires | BE-2 |
| 11 | A binding **referencing an unknown axis, value, role, class, or construct** | BF-7 |
| 12 | A binding referencing a role **not admitted** or **not materialized** | BF-9, DEC-S-140 |
| 13 | A binding expressed as a **token alias** between a status token and a visual role | BM-3, AL-2 |
| 14 | **Any appearance value** inside the Semantic Status source | BM-4 |
| 15 | A role name **reusing an axis or value name** | BM-5, SN-2 |
| 16 | A binding **keyed by display label** instead of technical identifier | BM-6 |
| 17 | A binding that **differs between supported contexts** | TI-1 |
| 18 | A supported context in which an affirmative disposition's **resolved presentation is identical** to another value's | TI-4 |
| 19 | A supported context in which a bound role's **declared pairing or contrast obligation** does not hold | TI-3, CF-3 |
| 20 | A bound resolution with **no explicitly selected supported context**, a default, a fallback, or a substitution | TI-7, CF-1, CF-9, CF-11 |
| 21 | A binding **without revision binding** to the status source revision and each Visual Source Set revision, or bound to a superseded revision | BM-8, BF-11 |
| 22 | A binding asserting **its own maturity or approval**, or claiming the status family's | BM-9 |
| 23 | A binding of a **non-status state** — validation outcome, interaction, selection, focus, risk tier | BM-10 |
| 24 | A binding that uses a role also serving an **Interaction, Focus or Emphasis** purpose | BR-10 |
| 25 | A **profile override** of a binding outside a named extension point | BR-13 |
| 26 | A channel output that **drops a bound element without a declared limitation** | RD-9, BF-10 |
| 27 | A Theme `Not Applicable` declaration **standing in for an applicable fail-closed condition** | TI-8 |

**Evidence-record input constraint — not a detection.** *(Reclassified in the limited
rework: it was listed above as detection 28.)* Any future evidence record about a bound
representation carries, as **exact evidence inputs**, the Semantic Status source
revision, the Visual Source Set revisions, the Resolver / Composition revision, the
Theme Resolution Context (or Theme `Not Applicable`), and the channel (BM-8, **TM-7**).
**That is a requirement on evidence records, not something a semantic validator of
binding sources must detect**: it is stated here as an **input constraint** that
CDS-WP-024 may consume, not as a CDS-WP-024 detection. **This contract does not design
the evidence model**, assigns it to no work package, and creates no evidence record.

**What a validator cannot do here is the more important half.** Whether a bound
encoding is **perceptibly** distinct, whether a pairing is **perceivable**, whether
the primary carriers **actually reach** a person through assistive technology, and
whether a qualifier interaction **reads truthfully** all require rendering,
interaction and assistive-technology evidence (**CDS-WP-031**), which **does not
exist**. **An automated check is never sufficient accessibility evidence**
(DEC-S-053), and **absence of a failure is not evidence of success** (EV-4).

## Inputs to CDS-WP-025

*(Invalid-state **categories** that the negative-fixture expansion must cover. **No
fixture, example value, role name, or file is authored here**, and CDS-WP-025 is
`Planned`, not active, and not authorized. Fixtures remain synthetic, test-only, and
non-normative (DEC-S-087).)*

| # | Invalid-state category | Expected state |
| --- | --- | --- |
| **IV-1** | Multi-axis binding entry; multi-axis encoding slot | Invalid |
| **IV-2** | Encoded axis lacking a disposition for any value of its authoritative value domain, including an omitted `unknown` | Incomplete |
| **IV-3** | Omitted disposition treated as `no visual encoding`; an Invalid or Incomplete binding degraded to Missing or to primary-carriers-only as automatic repair | Incomplete or Invalid as the binding is, and the degraded output an Implementation error — **the repair itself is the defect**, never Missing |
| **IV-4** | Affirmative disposition shared with a degraded-knowledge value | Invalid |
| **IV-5** | Affirmative disposition shared with any other value, including through `no visual encoding` | Invalid |
| **IV-6** | Missing qualifier-interaction, hue-only, forced-colours, or shared-disposition declaration | Incomplete |
| **IV-7** | Bound role of a non-Bindable class; non-bindable role declared or used as a Semantic Status binding carrier; non-bindable role declared as selected or varied according to a Semantic Status value without the separate, explicit authority BE-2 (b) requires | Invalid — an output that so varies a non-bindable role is an Implementation error |
| **IV-8** | Icon or motion element with no registered construct; Data-class element before the required data-visualization binding authority exists | Invalid — never Unsupported |
| **IV-9** | Unknown axis, value, role, class, or construct reference; unadmitted or unmaterialized role | Invalid — fail closed, no nearest match |
| **IV-10** | Status-to-role alias in either direction; appearance value inside the status source | Invalid |
| **IV-11** | Role named after an axis or value; binding keyed by display label | Invalid |
| **IV-12** | Binding differing between supported contexts | Invalid |
| **IV-13** | Resolved affirmative presentation identical to another value's in one supported context | Fails in setting — that context only, declared |
| **IV-14** | Broken pairing or contrast obligation in one supported context | Fails in setting — that context only, declared |
| **IV-15** | Default, fallback, or substituted context; Theme `Not Applicable` masking an applicable failure | Fails in setting |
| **IV-16** | Representation with visual status encoding and no text form, or no accessible-semantics form | Implementation error — representation fails closed |
| **IV-17** | Sensory-only encoding: colour, icon, shape, or motion — alone or combined — without the text form | Implementation error — representation fails closed |
| **IV-18** | Binding of a validation outcome, interaction, selection, focus, or risk-tier state | Invalid |
| **IV-19** | Binding without revision binding, or bound to a superseded revision | Incomplete |
| **IV-20** | Binding asserting its own maturity, or inheriting the status family's | Invalid |
| **IV-21** | Profile or consumer re-binding outside a named extension point | Invalid |
| **IV-22** | Channel output silently dropping a bound element | Implementation error — not Unsupported |

**Every category also needs its positive counterpart** — a representation that
applies **no** binding and carries its primary carriers is **correct** (axis
disposition **Missing**, no Implementation error), and a fixture set that treats it as
a failure would encode the wrong rule. **The converse holds too**: a fixture that
accepts an Invalid or Incomplete binding degraded to Missing would encode the wrong
rule (IV-3).

## Review determinations

*(Normative. How a reviewer answers each question **deterministically** against this
contract. A question that cannot be answered from sources is answered **"not
assessable"**, never **"yes"**.)*

| Question | Determined by | "Yes" requires |
| --- | --- | --- |
| **Is this binding permitted?** | BM-1 … BM-10, BE-1 … BE-6, BR-9 … BR-13 | Every bound role in a Bindable class, admitted and materialized; no prohibited form |
| **Is it complete?** | BR-3, BR-6, BR-7, BR-8, RD-4, RD-5, BM-8 | Every encoded axis has an explicit disposition for every value of its authoritative value domain in the bound status source revision; every required declaration and revision binding present |
| **Is it sufficiently redundant?** | RD-1 … RD-3, BO-1, BO-2 | Primary carriers present in every representation; no single-sensory or visual-only encoding. **Sufficiency for status meaning only** — every other obligation is assessed under its own authority (RD-1) |
| **Is it theme-safe?** | TI-1 … TI-10 | Identical binding in every supported context; in each supported context the setting applicability of every bound element **Holds**, or is a declared **Unsupported** |
| **Does it preserve semantic meaning?** | BO-3 … BO-9, BR-1, BR-2, BR-4, BR-5, BR-12, BR-14 | No aggregation, no affirmative sharing, no contradiction, no conversion of review-required or fail-closed states |
| **Is it accessible according to existing CDS authority?** | RD-1 … RD-11 structurally; **CDS-WP-031** evidence for anything perceptual | **Structurally conformant to this contract — which is not an accessibility statement.** Any accessibility statement requires admitted evidence; **none exists**, and **every visual artifact is AE-0** |
| **Is the failure state defined?** | *Binding states*, BF-1 … BF-11 | For each subject — binding, axis, setting, output — exactly one outcome of its own classification applies wherever the tabled evaluation order assigns one, and its effect is the one tabled; an axis whose applied binding is Incomplete or Invalid receives **no** disposition, and its visual-binding use fails closed |
| **Is implementation allowed to proceed?** | BP-1 … BP-8 | **Every** precondition met — **today BP-1 is met and BP-2 … BP-8 are not** |

## Evidence and claim boundary

- **This contract is a target and a rule set — not evidence, and not a claim**
  (DEC-S-050). No binding exists, so nothing has been bound, rendered, resolved,
  measured, or tested in any environment.
- **Every visual artifact is AE-0.** `AE1-CDS-WP016-SEMSTATUS-004` covers the
  channel-independent Semantic Status source/contract family **only** and **does not
  transfer** to any binding, role, context, channel, or representation (SS-8, TM-10).
- **No accessibility claim of any level is valid**, by anyone, including CDS itself,
  and **no conformance of any kind is stated**.
- **The Semantic Status family is unchanged**: source revision
  `semantic-status-rev-0002-candidate`, `Candidate` / `Approved`, **Stable: No**.
- **Visual values: 0 · visual Source Sets: 0 · visual Candidate families: 0.**
  Publication remains **`Private Development`**; there is no release and no tag.

## Open questions

*(Recorded so they are not decided by implication. **Recording one defers it; it does
not decide, schedule, route by authority, or authorize it.**)*

| # | Open question | Why this contract does not answer it | Blocks |
| --- | --- | --- | --- |
| 1 | **Representation and ownership of a binding artifact** — where a binding lives machine-readably and which work package or artifact authors it. **Unresolved.** **No owner is chosen, routed, or implied** — not `CDS-WP-020A`, CDS-WP-024, CDS-WP-026, CDS-WP-027, or a new artifact. Registered as the planning finding **`F-023-01`** in the [Post-Candidate Development Roadmap](../roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md). **It is not Route D / `F-022-01`**: Route D concerns the representation of **context-conditional semantic realization** in resolver / composition sources; only a binding's **resolver-specific** aspect overlaps it and stays with Route D. | Choosing would decide an architecture and an ownership assignment no effective authority makes. **BM-3**, **BM-4** and **BM-5** exclude three representations; the rest are open. **The contract does not depend on the answer**; implementation and reification of any binding depend on later, separate authority. | **BP-5** — realization only; not this contract |
| 2 | **The concrete Core visual-role vocabulary**, including whether any Bindable role exists | **Route C**'s (DEC-S-134, DEC-S-140) | **BP-2** |
| 3 | **Context-conditional realization** of a bound role | **Route D** / **`F-022-01`** | **BP-4** |
| 4 | **Icon and motion constructs** a binding could draw on | **CDS-WP-037**, **CDS-WP-035** | BE-4 |
| 5 | **Data-visualization status encoding** | **CDS-WP-039** | Every Data-class binding element — **Invalid** until that authority exists (missing authority, never Unsupported) |
| 6 | **Whether another registered class may become Bindable** | Requires the Elevated change **BE-3** | — |
| 7 | **Perceptual distinguishability and qualifier-interaction truthfulness in practice** | Rendering and assistive-technology evidence, **CDS-WP-031** | Any accessibility statement |
| 8 | **Where CDS status semantics end and consumer domain semantics begin** | **CR-035**, unchanged | Consumer-local states stay unbindable (BM-10) |

## What CDS-WP-023 does not do

It selects **no** colour, typography, spacing, shape, surface, icon, or motion value;
creates **no** role, role identifier, role name, role count, vocabulary entry,
primitive, alias, binding instance, mapping, Theme, context identifier, Source Set,
`sourceSetId`, `sourceRevision`, manifest, resolver instance, schema, validator rule,
test, fixture, renderer, component, or evidence; changes **no** byte of the Semantic
Status source; admits **no** evidence; changes **no** maturity; makes **no** claim;
determines **no** conformance; adds **no** Decision, ADR, or risk; decides **no**
Route A, B, C or D, **no** `WP021-D2`, **no** `F-022-01`, **no** `F-022-04`, **no**
`F-023-01` — which it registers as an unresolved planning finding and assigns to no
owner — and **no** Layer-2 ecosystem question; and **authorizes no work package** — **CDS-WP-024,
CDS-WP-025, `CDS-WP-020A` and every later identifier remain `Planned`, not active, and
not authorized.**

## Change classification

*(Normative — an application of DEC-S-033)*

| Change | Track |
| --- | --- |
| Clarifying a rule's wording without changing what it permits or requires | **Standard** |
| **Adding, removing, or relaxing any BM, BO, BE, BR, RD, TI, BF, BP, or VQ rule** | **Elevated** — it touches shared semantics and accessibility obligations |
| **Widening the Bindable category** | **Elevated** (BE-3) |
| **Changing an outcome, its subject, the evaluation order, or an effect in *Binding states*** | **Elevated** |
| **Reclassifying a contract determination as a derived requirement, or the reverse** | **Elevated** — it changes the authority a rule rests on |

> **A change that looks Standard but touches an Elevated trigger is Elevated.**

## Related documents

- [Semantic Status Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
- [Status Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md)
- [Status Composition and Conflict Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md)
- [Status Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md)
- [Semantic Status Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md)
- [Visual Foundation Architecture](VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Semantic Token Foundation](VISUAL_SEMANTIC_TOKEN_FOUNDATION.md)
- [Visual Foundation Colour Architecture](VISUAL_FOUNDATION_COLOR_ARCHITECTURE.md)
- [Visual Foundation Shape and Surface Architecture](VISUAL_FOUNDATION_SHAPE_AND_SURFACE_ARCHITECTURE.md)
- [Visual Foundation Iconography and Imagery Architecture](VISUAL_FOUNDATION_ICONOGRAPHY_AND_IMAGERY_ARCHITECTURE.md)
- [Visual Foundation Theme Architecture](VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
- [Visual Foundation Accessibility Mapping](../governance/VISUAL_FOUNDATION_ACCESSIBILITY_MAPPING.md)
- [Visual Foundation Channel Mapping](../governance/VISUAL_FOUNDATION_CHANNEL_MAPPING.md)
- [Visual Token Value Selection Rules](../governance/VISUAL_TOKEN_VALUE_SELECTION_RULES.md)
- [Decision Index](../decisions/DECISION_INDEX.md) — DEC-S-105 … DEC-S-112, DEC-S-134, DEC-S-137, DEC-S-138, DEC-S-140
- [Post-Candidate Development Roadmap](../roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md) — *Phase S*, *Prerequisite decision routes*
