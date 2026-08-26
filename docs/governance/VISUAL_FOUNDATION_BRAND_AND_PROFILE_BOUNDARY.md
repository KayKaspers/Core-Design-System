# Visual Foundation Brand and Product Profile Boundary

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-019 — Core Visual Foundation Architecture
- **Date:** 2026-08-26
- **Artifact class:** **1 — Normative human-readable source** (DEC-S-022)
- **Status:** **Normative for the boundary between the visual foundation, brand,
  and Product Profiles.** It **activates no Product Profile** and **creates no
  brand**.
- **Maturity:** **`Proposed`** — this document promotes nothing.

## Purpose and boundary

This document answers one question precisely: **who owns which visual decision,
and how much may a product differ?**

**It creates no brand.** No Core identity, no product identity, no logo, no mark,
no palette, no signature, and no visual language.

**It activates no Product Profile**, names **no extension point**, and approves
**nothing**.

Frame: [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md) ·
[Product Profile and Extension Model](../architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) ·
[Exception and Product Profile Governance](EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md).

## The four authorities

*(Normative — they are routinely conflated, and conflating them is how a design
system loses its boundary)*

| Authority | Architecture layer | Owns | Does not own |
| --- | --- | --- | --- |
| **Core brand and identity** | **2 — Brand and Identity** | Masterbrand rules, product-family relationship, brand roles, verbal identity, logos and brand assets | Foundation roles; accessibility guarantees |
| **Visual foundation** | **3 — Foundations and Tokens** | Visual roles, their obligations, and the primitives behind them | Brand marks; product identity; component contracts |
| **Product Profile** | **1 → 2 governance, applied at token-flow layer 4** | Approved, bounded, version-bound product variation at **named extension points** | Roles, shared semantics, accessibility, status truth |
| **Consumer** | Outside CDS | Its own product, its extensions, its local artifacts, its own claims | Any CDS approval authority |

**Layer 2 may not depend on Layer 3.** The visual foundation may depend on brand;
brand may not depend on the foundation. A brand decision that requires a foundation
change is a **request**, routed through governance — never a direct edit.

## Roles are mandatory; values are variable

*(Normative — the statement that resolves "must a Core product inherit every Core
visual value?")*

The **Core Foundation** is *"the shared, mandatory basis"*, and *"a consumer does
not opt out of the Core Foundation"*. That is unchanged. But it does not mean a
product inherits every Core **value**, and the distinction is precise:

| Layer of the answer | Binding? | Why |
| --- | --- | --- |
| **The role exists** | **Mandatory** | Roles are the shared vocabulary that makes CDS a system. Removing one is a fork. |
| **The role's meaning** | **Mandatory** | Redefining shared semantics destroys the common meaning (DEC-S-025). |
| **The role's declared obligations** — contrast, pairing, non-colour carrier, focus visibility | **Mandatory** | Weakening accessibility is prohibited absolutely (invariant 10, DEC-S-059). |
| **The value bound to the role** | **Variable — but only at a named, approved extension point** | This is exactly what a Product Profile is for (DEC-S-025, layer 4). |

> **A Core product inherits every Core visual *role*. It does not automatically
> inherit every Core visual *value*.**
>
> **And it varies a value only where CDS has named that value as an extension
> point.**

## The extension-point set is empty

*(Normative — the operative constraint today)*

| Item | State |
| --- | --- |
| Named, approved visual extension points | **Zero** |
| Product Profiles in existence | **Zero** |
| Product Profiles approvable today | **Zero** |
| Work package that may name extension points | **CDS-WP-032** — `Planned`, not active, not authorized |

**Anything not named is not an extension point.** With an empty set, **no visual
override of any kind is currently possible**, and any override that appeared would
be an unrecorded deviation — that is, a fork.

### Why no Product Profile can be approved today

A Product Profile requires **twelve** mandatory elements (DEC-S-043). At least three
cannot be supplied:

| Element | State |
| --- | --- |
| **4 — Named extension points** | **None exist.** A profile that cannot name the points it touches is not scoped. |
| **7 — Scope-appropriate accessibility evidence** | **Cannot be produced.** Every visual artifact is **AE-0**; the one admitted AE-1 package covers the Semantic Status source scope and is **not** scope-appropriate evidence for any profile. |
| **10 — Consumer validation** | No consumer validation exists; the CoreOps pilot is **inactive**. |

Additionally, the **Consumer Maintainer** role a Product Profile requires is
currently **unstaffed** (FM-F-006).

**This is recorded, not worked around.**

## Criteria an extension point must satisfy

*(Normative as **criteria**. This names **no** extension point and creates **no**
candidate. Naming them is CDS-WP-032's and requires Human-Maintainer approval.)*

A future extension point may be proposed only where all of the following hold:

| # | Criterion |
| --- | --- |
| **EP-1** | It is a **value binding**, never a role, a meaning, or an obligation |
| **EP-2** | Its **variation range is bounded** and stated |
| **EP-3** | Every **declared obligation of the role survives** every admissible value in that range — contrast, pairing, non-colour carrier, focus visibility |
| **EP-4** | It is **machine-checkable**, so an out-of-bounds override fails closed |
| **EP-5** | It has a **stated purpose** — which legitimate product difference it exists to express |
| **EP-6** | It is **not filling a core gap.** If several products need the same override, the **core is wrong** — fix the core |
| **EP-7** | An **additive extension would not serve better.** Additive beats overriding |
| **EP-8** | Its **cumulative load is accounted for** — profiles and exceptions multiply faster than they can be governed (RISK-021, RISK-027) |

**EP-6 is the important one.** Repeated profile requests for the same thing mean
the foundation is wrong, and the correct response is to change the foundation, not
to grant more profiles.

## What a Product Profile may never do with visual foundations

*(Normative — absolute; the last five are not negotiable at any ceremony level)*

| Prohibition | Why |
| --- | --- |
| Add, remove, rename, merge, or repurpose a **role** | Destroys the shared vocabulary |
| Change what a role **means** | Redefines shared semantics (DEC-S-025) |
| **Weaken or remove a contrast obligation or a declared pairing** | Weakens accessibility — invariant 10 |
| **Remove, weaken, or obscure the focus indicator** | 2.4.7 is a CDS-alone obligation with **no permitted mechanism of removal** |
| **Make colour, icon, shape, position, or motion the sole carrier of meaning** | VF-I-5, CR-006 |
| **Distort status truth** | `unknown` must never read as healthy (DEC-S-028) |
| Reach past a named extension point into the core | Inverts the dependency direction |
| Use a **theme as a back door** around the extension-point boundary | The same violation with an extra step |

> **A profile that needs any of these is not a profile. It is a fork, and naming it
> honestly is the correct outcome** — an honest fork is manageable; a profile
> pretending not to be one is not (RISK-027).

## Consumer and customer branding

*(Normative)*

| Case | Classification | Rule |
| --- | --- | --- |
| **A consumer's existing visual decisions and token sets** | **Consumer-local artifact** (class 7) | Not CDS, not an override, **not a defect**. Enters CDS only through reconciliation (DEC-S-026) — never by being read as an override |
| **A consumer-built visual extension** | **Consumer Extension** | Consumer-owned unless explicitly accepted (DEC-S-016). **Most product-specific work should live here permanently** |
| **A customer's brand applied to a consumer's product** | **Consumer-owned**, entirely | Outside CDS authority. CDS neither governs nor certifies it |
| **A bounded, expiring deviation from a CDS contract** | **Local Exception** | Recorded, owned, expiring — and **may never weaken accessibility** (DEC-S-059) |

### No retrospective legitimation

*(Normative — the rule that matters most here)*

**A Product Profile is not retrospective legitimation of an existing consumer
design.**

SpeakCore and CastCore already hold their own style direction, palette values, and
typography choices (CR-002, CR-037). Those are **Consumer-local Artifacts**. Their
authoritative sources were **outside the permitted read areas** in CDS-WP-004 and
**were not read** — CDS knows *that* they exist, not *what they contain*.

- **No automatic adoption.** A consumer decision does not become CDS by existing.
- **No automatic overwrite.** CDS does not replace a shipped decision by appearing
  (invariant 14).
- **No retrospective conformance.** Existing consumer designs are not certified
  after the fact.
- **Consumer-local retention is a valid, final outcome** — not a failure to
  converge.
- **Labelling existing consumer work a "Product Profile" to make it look governed
  is prohibited** (RISK-036).

**CDS-WP-019 reads no consumer value, evaluates no consumer design, and reconciles
nothing.**

## Reconciliation flow for visual decisions

*(Normative — DEC-S-026, applied to the visual foundation. **Not executed here.**)*

```text
Inventory
  → Semantic Mapping      ← the load-bearing step
     → Conflict Identification
        → Classification
           ├→ Product Profile Candidate
           ├→ Consumer-local Retention   ← a valid, final outcome
           └→ Migration Candidate
              → Evidence and Review
```

**Step 2 is load-bearing and it is semantic, not value-level.** The question is
*"what did this visual decision mean?"* — **never** *"is this value right?"*.
Judging a consumer's colours is not reconciliation; it is a category error, and it
is prohibited.

## Core identity and product identity

*(Normative as a boundary; **no identity is created**)*

| Question | Answer today |
| --- | --- |
| Does a Core master visual identity exist? | **No.** None is created, and CDS-WP-045 (Advanced Brand Identity Model) is `Planned`, not active |
| Does any product identity exist? | **No** |
| May the visual foundation express brand? | It may **consume** Layer 2 decisions. It may not **make** them |
| May brand override an accessibility obligation? | **Never.** Brand approval is **never an accessibility claim** — the two are unrelated authorities |
| Is family recognition a foundation concern? | **No.** CR-001 (product-family recognition) is mapped to **Layer 2**, and remains a **Human-Maintainer decision** |

## What CDS-WP-019 explicitly does not do

- Activates **no** Product Profile and approves **none**.
- Names **no** extension point and proposes **no** candidate.
- Creates **no** brand, identity, mark, logo, palette, or signature.
- Reads, evaluates, or reconciles **no** consumer visual decision.
- Starts **no** pilot and integrates **no** consumer.
- Grants **no** maturity, admits **no** evidence, and makes **no** claim.

## Deferred decisions

The Core master visual identity · product identities · the named extension-point
set · Product Profile approval criteria specific to visual families · brand
governance for visual expression · customer-branding guidance · the reconciliation
of existing consumer visual decisions.

**Each requires its own explicitly authorized work package.** Product Profile and
brand extension governance is **CDS-WP-032**; the advanced brand identity model is
**CDS-WP-045**. Both are `Planned`, not active, and not authorized.

## Related documents

- [Visual Foundation Architecture](../architecture/VISUAL_FOUNDATION_ARCHITECTURE.md)
- [Visual Foundation Theme Architecture](../architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md)
- [Visual Foundation Iconography and Imagery Architecture](../architecture/VISUAL_FOUNDATION_ICONOGRAPHY_AND_IMAGERY_ARCHITECTURE.md)
- [Visual Foundation Governance and Lifecycle](VISUAL_FOUNDATION_GOVERNANCE_AND_LIFECYCLE.md)
- [Product Profile and Extension Model](../architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md)
- [Exception and Product Profile Governance](EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md)
- [Consumer Contract and Reconciliation Model](../architecture/CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md)
- [Accessibility Limitations and Exception Policy](ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md)
- [Consumer and Stakeholder Model](CONSUMER_AND_STAKEHOLDER_MODEL.md)
