# Accessibility Architecture Alignment

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-007
- **Date:** 2026-07-16
- **Status:** **Normative** for how accessibility binds to the architecture

## Purpose

Maps accessibility onto the existing CDS architecture, so that it is **carried by
the structure** rather than sitting beside it as a policy nobody's artifact
references.

**No technology is selected** (DEC-S-032).

Frame: [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) ·
[Accessibility and Inclusive Design Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md).

## The eight architecture layers

| Layer | Accessibility responsibility |
| --- | --- |
| **1 Strategy and Governance** | Holds the target (WCAG 2.2 AA), the policy, the target-versus-claim boundary, and the claim rules. Accessibility governance lives here — not in a review step. |
| **2 Brand and Identity** | Brand expression may not defeat accessibility. Brand approval is **never** an accessibility claim. Product identity operates within the profile limits. |
| **3 Foundations and Tokens** | **Semantic status foundations**; colour roles must permit conforming contrast (1.4.3, 1.4.11); motion foundations carry reduced-motion (CR-022); focus visibility (2.4.7); flexible text (CR-023). **Colour is never the sole carrier** (1.4.1). |
| **4 Components** | **Accessibility behavior is part of the component contract** — names, roles, values, states (4.1.2); keyboard operability (2.1.1); no trap (2.1.2); focus order (2.4.3). A contract without accessibility semantics is **incomplete**. |
| **5 Patterns and Experiences** | Flow-level accessibility: navigation and bypass (2.4.1); safe actions (3.3.4); setup; help (3.2.6); Simple/Expert without hiding status; error recovery. Composition risks live here. |
| **6 Channels and Communication** | **Channel profiles** (DEC-S-058). Semantics constant, presentation per channel (DEC-S-029). Non-web channels are not WCAG-assessable without a profile. |
| **7 Distribution and Enablement** | Accessibility documentation ships with artifacts. Offline consumption must not degrade accessibility — a help system unreachable offline is a barrier (CR-031). |
| **8 Evidence and Quality** | **AE-0 … AE-4**, support baseline, regression gates, limitations, deviations. Evidence is revision-bound and never transfers across scope or channel. |

### Dependency direction holds

Accessibility does **not** invert the layer rules. A component may not push an
accessibility requirement down into Layer 3 to satisfy itself; that would create
a component-specific foundation. Foundations carry accessibility **because
semantics require it**, not because a component asked.

## The eight artifact classes

| Class | Accessibility authority |
| --- | --- |
| **1 Normative human-readable source** | **Defines** accessibility intent, requirements, and boundaries. The policy lives here. |
| **2 Normative machine-readable source** | Carries approved values that must permit conformance (contrast-capable roles). Holds no meaning. |
| **3 Generated artifact** | **Inherits** accessibility properties; proves nothing. A generated output is **not** accessibility evidence. |
| **4 Reference implementation** | **Demonstrates** an accessible contract; does not define it. May not extend accessibility semantics on its own authority. |
| **5 Authoring / design-tool representation** | **Never** an accessibility source of truth. A tool's accessibility panel is not evidence. |
| **6 Evidence artifact** | **Records** accessibility evidence (AE-1…AE-4). Does not change a source; triggers a decision. |
| **7 Consumer-local artifact** | Consumer-owned. Its accessibility is the consumer's. **CDS does not certify it** (DEC-S-026). |
| **8 Research / example artifact** | **Never normative.** **APG examples live here** — the APG states its objectives exclude production-ready code. |

Class 8 carries the sharpest rule of this work package: **an APG pattern is a
learning example, not an accessible component**. Treating it as production-ready
because it comes from W3C is exactly the shortcut the APG itself warns against
(DEC-S-054).

## The five token-flow levels

| Level | Accessibility role |
| --- | --- |
| **1 Reference tokens** | Raw values. **No accessibility semantics.** A consumer binding here loses the meaning that made a value conforming. |
| **2 Semantic tokens** | **Where accessibility meaning lives.** Status roles must be expressible non-visually; colour roles must permit conforming contrast. |
| **3 Component tokens** | Bind semantic accessibility decisions to contracts. May not invent meaning. |
| **4 Product Profile overrides** | **May never weaken accessibility** (invariant 10, DEC-S-025). Cannot remove focus visibility, reduce a contrast role below target, or make colour sole carrier. |
| **5 Channel / platform outputs** | Must not collapse accessible semantics during transformation. |

**The semantic-first principle is an accessibility mechanism**, not only a naming
convention: a token named for appearance cannot express "unknown", and therefore
cannot be made perceivable non-visually.

## Product Profiles

*(DEC-S-025, DEC-S-043, DEC-S-059)*

- A profile **may never weaken accessibility** — absolute.
- A profile requires **scope-appropriate accessibility evidence** before approval.
  **This cannot be produced today** → **no profile can be approved.**
- **An ordinary exception cannot waive accessibility** for Stable or conformant
  scope.
- Anti-fragmentation review must ask whether a profile request would degrade
  accessibility.

## Consumer contracts

| Contract | Accessibility content |
| --- | --- |
| **Source** | Which normative sources define accessibility requirements |
| **Transformation** | Must not strip accessible semantics |
| **Distribution** | Accessibility documentation ships with the artifact |
| **Integration** | **Consumer must preserve accessibility requirements** and not suppress them via overrides |
| **Adoption Evidence** | AE levels, baseline, scope, limitations required before any claim |

The Integration Contract is where DEC-S-052 becomes enforceable: the consumer
owes accessible **composition**, and no CDS contract can supply it.

## The five status axes

*(DEC-S-028, DEC-S-056 — the strongest binding)*

| Axis | Accessibility requirement |
| --- | --- |
| **Operational condition** | Perceivable non-visually |
| **Severity** | Not conveyed by colour alone (1.4.1) |
| **Knowledge confidence** | **"Unknown" must reach assistive technology** |
| **Freshness** | Staleness perceivable, not implied visually |
| **Evidence availability** | Distinguishable from a verified state |

The architecture invariant becomes an accessibility invariant:

> **Unknown ≠ Healthy · Stale ≠ Current · Unverified ≠ Verified — for every
> user, through every modality.**

Merging condition and confidence leaves "unknown" nowhere to live; conveying it
only visually leaves it nowhere to live *for a screen-reader user*. Both are the
same failure, and 4.1.2 and 4.1.3 are where it is caught.

## Channel architecture

Semantics constant, presentation per channel (DEC-S-029). Each channel needs an
accessibility profile before Candidate or Stable (DEC-S-058).

The non-interactive channels are the hard case: no hover, no focus, no live
update, possibly greyscale print. **A status depending on colour, interaction, or
refresh fails there** — which is why the non-colour rule is architectural rather
than a web courtesy.

## Evidence flow

Accessibility evidence rides the existing traceability chain:

```
Requirement / Decision → Normative source → Transformation → Generated artifact
   → Reference or consumer implementation → Accessibility evidence (AE-1…AE-4)
      → Consumer feedback → Controlled change decision ↺
```

Every accessibility evidence artifact carries: source revision · transformation
revision · output identity · consumer revision · evidence identity · **support
baseline** · deviation record · approval state.

**Accessibility evidence without a declared baseline is unverifiable** — it does
not say what it was tested against.

## Maturity and publication gates

| Gate | Accessibility requirement | Satisfiable today? |
| --- | --- | --- |
| **Candidate** | Mapping, responsibility, AE-1, AE-2 or plan, limitations, baseline plan, regression plan | **No** — for the Semantic Status source/contract family the evidence elements are now supported (admitted **AE-1**), but Human-Maintainer approval after Nova review is still open; for every other artifact no evidence exists |
| **Stable** | AE-2 complete + **AE-3** against baseline + consumer evidence + no critical deviations | **No** — the baseline exists (A11Y-BL-001, committed), but **no AE-2, AE-3, or consumer evidence exists anywhere** |
| **Product Profile** | Scope-appropriate accessibility evidence | **No** |
| **Publication** | Accessibility statement per this policy | **Now definable** — the statement is *what the policy says*, and it says nothing is tested |
| **Release** | Depends on Stable artifacts | **No** |

### What CDS-WP-007 changed

The accessibility **target** was the missing input to all of these. It now exists.

**None of the gates opened.** The blocker moved from *"no target"* to *"no
evidence"* — which is progress in kind, not in state: the question changed from
"against what?" to "show it".

## Related documents

- [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md)
- [Accessibility and Inclusive Design Policy](../governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Evidence, Traceability and Status Semantics](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md)
- [Product Profile and Extension Model](PRODUCT_PROFILE_AND_EXTENSION_MODEL.md)
