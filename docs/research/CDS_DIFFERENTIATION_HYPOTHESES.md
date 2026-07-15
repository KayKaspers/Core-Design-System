# CDS Differentiation Hypotheses

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-003 — Benchmark and Differentiation Research
- **Evidence access date:** 2026-07-15
- **Status of every entry: Research hypothesis — not a decision**

## Authority

**Nothing in this document is a CDS principle, commitment, or decision.**

Each entry is a research hypothesis assessed against the evidence in
[BENCHMARK_EVIDENCE_MATRIX.md](BENCHMARK_EVIDENCE_MATRIX.md). No hypothesis was
promoted to a decision by CDS-WP-003. The decision range remains
DEC-S-001 … DEC-S-012 (12), unchanged.

Hypotheses HYP-001 … HYP-008 were fixed by the work-package prompt. No further
hypothesis IDs were created.

## Assessment vocabulary

- **Strongly supported differentiation opportunity**
- **Moderately supported differentiation opportunity**
- **Common industry practice, not differentiating alone**
- **Weakly supported**
- **Not verifiable in this research**

## The uniqueness trap

Every hypothesis below carries a uniqueness risk, because this research can only
see **public documentation**. Absence from public documentation is not absence
from practice. A claim that "no one else does this" is unsafe; a claim that "no
reviewed system *documented* this" is defensible. Every assessment here is
capped accordingly, per RISK-013.

---

## HYP-001 — Unified multi-channel foundation

> CDS may differentiate by governing product UI, GitHub presentation,
> documentation, PDF reports, presentations, diagrams, dashboards, and selected
> communication materials through one controlled foundation.

- **Current assessment:** **Moderately supported differentiation opportunity**
- **Status:** Research hypothesis

### Supporting evidence

In reviewed official sources, no system documented standards for PDF reports,
presentations, or diagrams. The reviewed systems are overwhelmingly
product-interface systems that touch brand at the edges. This was the most
consistent gap in the entire review, across all ten systems and both sectors.

### Counterevidence and limitations

- **Partial coverage exists.** Carbon documents data visualization with its own
  guidance and implementation. Primer explicitly separates product UI from brand
  UI with a brand toolkit. SAP documents multi-platform product UI with
  per-platform guidelines. The channels are not untouched — they are unevenly
  covered.
- **The gap may be a scope choice, not an oversight.** Mature systems may
  deliberately exclude document and presentation channels because those belong
  to separate brand or marketing functions that simply do not publish alongside
  the design system. Absence from a design-system site is not absence from the
  organization.
- **Review depth.** Marketing, brand, and template channels were not
  systematically searched on every system. This is a real limitation.
- **The gap may reflect cost, not opportunity.** Nobody documenting a channel is
  weak evidence that documenting it is valuable. It may simply be expensive and
  low-return.

### Uniqueness risk

**High.** This is the most tempting claim in the review and the least safe. The
defensible statement is narrow: *no reviewed system publicly documented these
channels in one governed foundation*. It is **not** established that CDS would
be the first to do so, nor that doing so is worthwhile.

### Potential CDS value

If real, this addresses a genuine problem already registered in the CDS problem
statement: cross-channel artifacts today have no shared standard at all. The
value is coherence across everything a product emits, not just its interface.

### Validation required

- Do CoreOps and other consumers actually produce enough documents, reports,
  presentations, and diagrams for a standard to pay for itself? → CDS-WP-004
- What would governing a non-interface channel concretely require? → CDS-WP-005
- Is the breadth affordable given RISK-001 (uncontrolled scope expansion)?

### Target follow-up

**CDS-WP-004** (consumer demand), then **CDS-WP-005** (feasibility).

---

## HYP-002 — Offline and self-hosted consumption

> CDS may differentiate through consumer artifacts that require no mandatory
> external runtime service.

- **Current assessment:** **Moderately supported differentiation opportunity**
- **Status:** Research hypothesis

### Supporting evidence

No reviewed system stated an explicit offline or self-hosted consumption
guarantee, and none was found treating mandatory external runtime services as a
documented constraint. Offline usability is essentially absent as a *stated
commitment* across all ten systems.

### Counterevidence and limitations

- **Capability is common; the commitment is not.** USWDS distributes precompiled
  assets and source files via a package registry and direct download. Carbon
  ships scoped packages. Spectrum offers three implementations. Most of these
  artifacts are very likely self-hostable already.
- **Therefore the differentiator is the promise, not the property.** CDS would
  not be uniquely *able* to run offline; it would be unusual in *committing* to
  it and governing against it.
- **Runtime dependencies were not tested.** No package was installed or
  inspected, per the work-package prohibitions. The claim rests on documentation
  only.
- Static distribution is the industry norm for CSS and component libraries, so
  the baseline is already fairly offline-friendly.

### Uniqueness risk

**Medium.** Overstating this as "CDS works offline, others don't" would be
false. The honest framing is that CDS treats offline and self-hosted use as a
governed requirement (DEC-S-006) where reviewed systems leave it unstated.

### Potential CDS value

Real for consumers deploying without dependable or permitted external network
access — an existing CDS assumption. Turns an implicit property into a
verifiable constraint.

### Validation required

- Do consumers actually have offline or air-gapped deployment needs? →
  CDS-WP-004
- What distribution forms satisfy the constraint? → CDS-WP-005
- How is the constraint tested rather than asserted? → CDS-WP-006

### Target follow-up

**CDS-WP-004** (need), **CDS-WP-005** (architecture).

---

## HYP-003 — Operations-oriented experience patterns

> CDS may develop unusually strong guidance for dense operational dashboards,
> monitoring, inventory, topology, maintenance, deployments, degraded
> operation, dangerous actions, and auditability — generalizable beyond CoreOps.

- **Current assessment:** **Not verifiable in this research**
- **Status:** Research hypothesis

### Supporting evidence

Carbon documents data visualization as a distinct concern with its own guidance
and implementation, establishing that data-dense presentation is treated
seriously by at least one mature system. SAP addresses enterprise applications.
Beyond that, this review found no evidence either way.

### Counterevidence and limitations

- **The dimensions reviewed do not reach this depth.** Pattern libraries were
  not opened per system. A claim that operational patterns are weak across the
  industry would be unsupported by anything actually reviewed.
- **The enterprise systems reviewed are the most likely counterexamples.** SAP
  and SLDS serve enterprise operational software, and their pattern libraries
  were not examined. It is quite plausible they cover this ground well.
- Carbon's data-visualization coverage is direct evidence that at least part of
  this space is already occupied.

### Uniqueness risk

**High and currently unquantifiable.** This hypothesis was neither supported nor
refuted. Claiming differentiation here today would be pure assertion.

### Potential CDS value

Potentially high if real — this is the area closest to the pilot consumer's
actual domain. It is also the area where the CoreOps-overfitting risk
(RISK-002) is most acute: strength in operational patterns is exactly what a
single operational pilot would produce, and DEC-S-011 exists to stop that
becoming normative without generalization.

### Validation required

- Targeted review of the enterprise systems' pattern libraries (SAP, SLDS,
  Carbon) before any differentiation claim.
- Do multiple consumers need these patterns, or only CoreOps? → CDS-WP-004
- Can the patterns be generalized beyond one operational product at all? →
  DEC-S-011 conditions.

### Target follow-up

**CDS-WP-004** (multi-consumer need and generalizability). A deeper pattern
review would require its own explicit authorization; **Claude does not extend
the roadmap**.

---

## HYP-004 — Design-code-documentation convergence

> CDS may treat normative sources, generated artifacts, documentation,
> implementation, and validation evidence as one governed lifecycle.

- **Current assessment:** **Moderately supported differentiation opportunity**
- **Status:** Research hypothesis

### Supporting evidence

This is the strongest evidence area in the review. Material documents a token
workflow running through a proprietary design tool and its plugin, with export
to platform targets — the design tool sits in the middle of the chain. Carbon
and Fluent maintain design kits and code implementations in parallel without
describing a synchronization mechanism in reviewed pages. Tool coupling is
common, largely undocumented, and not presented as a risk by the systems
themselves. No reviewed system documented tool-independence as an explicit goal.

### Counterevidence and limitations

- **Partial convergence already exists.** Atlassian frames tokens as the
  documented single source of truth. GOV.UK separates documentation from
  implementation as distinct artifacts. USWDS binds validation evidence into the
  component lifecycle — arguably the closest thing to a governed lifecycle
  observed. SLDS provides validate/migrate/create tooling.
- **Undocumented ≠ absent.** These organizations very likely have internal
  synchronization processes; public docs simply do not describe them. This
  review explicitly does not infer internal practice.
- **The coupled systems are not failing.** Material's arrangement is coherent
  for a publisher large enough to absorb the portability cost. Tool coupling is
  a trade-off, not an error.

### Uniqueness risk

**Medium.** The individual pieces exist across several systems. The unclaimed
space is treating them as *one governed lifecycle* with tool-independence as an
explicit, stated goal.

### Potential CDS value

High. This is where the benchmark most directly validates existing CDS
decisions: DEC-S-004 (tool independence) and RISK-004 (tool lock-in) address a
real, evidenced, under-served gap — and RISK-005 (drift) is what convergence
prevents.

### Validation required

- Where does the normative source actually live, concretely? → CDS-WP-005
- Can convergence be maintained with limited maintainer capacity, or is it a
  large-organization luxury?
- What evidence proves convergence rather than asserting it? → CDS-WP-006

### Target follow-up

**CDS-WP-005** (architecture), **CDS-WP-006** (evidence and governance).

---

## HYP-005 — Governed product-family flexibility

> CDS may support controlled product profiles without allowing independent,
> incompatible design systems to emerge.

- **Current assessment:** **Moderately supported differentiation opportunity**
- **Status:** Research hypothesis

### Supporting evidence

Every mature system reviewed permits product-level variation — SAP documents
central components that products extend or modify, Material treats brand
expression as supported customization, SLDS offers advanced theming, Spectrum 2
frames personalization as a direction. **None of the reviewed sources stated the
limits of that variation.** The mechanism is universal; the published constraint
is absent.

### Counterevidence and limitations

- **The mechanism itself is emphatically common practice** — offering profiles or
  theming is not differentiating in the slightest.
- **The limit may be governed internally** and simply not published. Vendor
  systems govern their own products directly and may not need a public rule.
- **CDS's situation differs structurally.** Atlassian pursues cohesion across
  one company's product family with unified ownership. CDS must govern products
  plus associated projects plus potential external consumers (DEC-S-010) —
  harder, and without the unified authority those vendors have.
- **The differentiator is the published limit, not the flexibility.** That is a
  narrow claim.

### Uniqueness risk

**Medium-high.** "We support product profiles" is not differentiating. "We
publish and enforce their limits" might be — but is unproven and hard.

### Potential CDS value

Directly addresses RISK-008 (consumer fragmentation) and Non-goal 11 (CDS must
not become a collection of product-specific special solutions). This is the
mechanism by which controlled individuality either works or fails.

### Validation required

- What do consumers actually need to vary? → CDS-WP-004
- What is the profile mechanism? → CDS-WP-005
- What constrains it, and who enforces that? → CDS-WP-006
- This maps to an open boundary question already registered in the
  [Scope Boundary Matrix](../governance/SCOPE_BOUNDARY_MATRIX.md).

### Target follow-up

**CDS-WP-005** (mechanism), **CDS-WP-006** (governance).

---

## HYP-006 — Evidence-based adoption

> CDS may require version-bound adoption and conformance evidence instead of
> informal claims.

- **Current assessment:** **Common industry practice, not differentiating alone**
- **Status:** Research hypothesis

### Supporting evidence

The practice is proven and effective where it exists. USWDS publishes
per-component lifecycle status across four phases with named maturity states,
with accessibility testing as a gating condition. Primer states a conformance
aim and references publicly published conformance reports. Carbon surfaces the
current implementation version and a last-updated date. Fluent documents
migration between generations.

### Counterevidence and limitations

- **This is the hypothesis the benchmark most clearly shows CDS would be
  *following*, not leading.** Mature systems already converge on: version the
  artifact, state its maturity, keep the predecessor, document migration.
- USWDS's model is more developed than anything CDS has planned, and it is public
  and operating today.
- The practice carries real cost. USWDS's public proposal process with a stated
  minimum comment period buys legitimacy at the price of speed — a cost a small
  team may not afford.

### Uniqueness risk

**Low, because no uniqueness is claimed.** Assessed deliberately as common
practice. Presenting it as a CDS differentiator would be a textbook RISK-013
overstatement.

### Potential CDS value

**High value, low differentiation** — and that combination is fine. It validates
DEC-S-009 and DEC-S-012 as sound, mainstream governance rather than invention.
CDS should adopt it because it works, not because it distinguishes.

### Validation required

- What maturity vocabulary fits CDS without importing another taxonomy
  (RISK-010)?
- What evidence can CDS actually produce with its capacity? → CDS-WP-006
- What does version-bound adoption mean for the pilot? → CDS-WP-004

### Target follow-up

**CDS-WP-006** (policy), **CDS-WP-004** (pilot application).

---

## HYP-007 — Accessibility, localization, privacy, and security awareness

> CDS may integrate these concerns across foundations, components, patterns,
> content, and evidence rather than treating them as isolated appendices.

- **Current assessment:** **Weakly supported** (as a differentiator)
- **Status:** Research hypothesis

### Supporting evidence

The *integrated* half is partly supported. Localization guidance was found in
only 2 of 10 systems in reviewed pages, and privacy-aware and security-aware
interaction design were not found as documented cross-cutting concerns anywhere
in the review. If real, that is an unclaimed space.

### Counterevidence and limitations

- **Accessibility is emphatically not differentiating.** It is a named section in
  all ten systems. Four distinct mature patterns were observed
  (standard-referencing, evidence-publishing, boundary-stating,
  lifecycle-gating). Material names accessibility a foundation; USWDS gates
  releases on it. CDS would be joining a crowded, well-developed field.
- **The localization gap is mostly a review artifact.** Content and localization
  pages were not opened per system. The 2-of-10 figure reflects review depth far
  more than industry practice, and should not be cited as an industry finding.
- Material documents content design as a named foundation — the concern is
  already treated as foundational by at least one system.
- Bundling four different concerns into one hypothesis makes it hard to assess;
  they have genuinely different evidence profiles.

### Uniqueness risk

**High.** Claiming differentiation on accessibility would be indefensible and
would also risk implying a conformance status CDS does not have. WCAG 2.2 itself
states that even AAA conformance will not serve every disability.

### Potential CDS value

Value is in **rigor and honesty**, not novelty. The cross-cutting concerns are
already registered (DEC-S-007) as quality requirements explicitly not
conformance claims — which the benchmark shows is the correct framing.

### Validation required

- Separate the four concerns; assess individually.
- Deeper localization review before any claim → would need explicit
  authorization.
- What accessibility target can CDS evidence? → CDS-WP-007

### Target follow-up

**CDS-WP-007** (accessibility and inclusive design policy).

---

## HYP-008 — Small-team and enterprise applicability

> CDS may combine enterprise-grade governance with a workflow usable by small
> self-hosted projects without dedicated design departments.

- **Current assessment:** **Weakly supported**
- **Status:** Research hypothesis

### Supporting evidence

The reviewed systems cluster at two poles: large vendor systems built by
dedicated teams for their own product families, and government systems built for
many agencies with substantial public process. No reviewed system documented a
deliberately scaled-down adoption path for a small team without design staffing.
SLDS's role-based transition instructions are the closest observed
acknowledgement that adopters differ.

### Counterevidence and limitations

- **This is a research-and-source-bias artifact as much as a finding.** The ten
  systems were fixed in advance and are all published by large technology
  companies or national governments (RISK-011). A benchmark of only large
  publishers cannot show whether small-team-friendly systems exist. They very
  likely do — the sample simply cannot see them.
- **The two halves may be in tension.** Enterprise-grade governance is expensive
  precisely because it is thorough. USWDS's rigor costs a public comment period.
  Combining rigor with small-team usability may be a trade-off rather than a
  synthesis.
- Nothing in the review demonstrates the combination is achievable.
- CDS itself has limited maintainer capacity — the hypothesis may describe an
  aspiration rather than a capability.

### Uniqueness risk

**High, and structurally unmeasurable from this sample.** The benchmark set
cannot support a claim about small-team systems either way.

### Potential CDS value

Aligns with an existing CDS assumption (roles are functions, not positions; no
organizational size or design department assumed) and with DEC-S-006. If
achievable, it matters for the self-hosted consumer base.

### Validation required

- Establish whether the combination is achievable at all, not just desirable.
- What does adoption cost a small team concretely? → CDS-WP-004
- Can governance rigor scale down without becoming ceremony? → CDS-WP-006
- Any comparison against smaller or community design systems would require a
  separately authorized research scope; **Claude does not extend the roadmap**.

### Target follow-up

**CDS-WP-004** (real adopter cost), **CDS-WP-006** (scalable governance).

---

## Summary

| ID | Hypothesis | Assessment | Uniqueness risk |
| --- | --- | --- | --- |
| HYP-001 | Unified multi-channel foundation | Moderately supported | High |
| HYP-002 | Offline and self-hosted consumption | Moderately supported | Medium |
| HYP-003 | Operations-oriented experience patterns | Not verifiable in this research | High |
| HYP-004 | Design-code-documentation convergence | Moderately supported | Medium |
| HYP-005 | Governed product-family flexibility | Moderately supported | Medium-high |
| HYP-006 | Evidence-based adoption | Common industry practice, not differentiating alone | Low |
| HYP-007 | Accessibility, localization, privacy, security | Weakly supported | High |
| HYP-008 | Small-team and enterprise applicability | Weakly supported | High |

**No hypothesis reached "Strongly supported."** That result is itself the most
useful finding: the evidence does not currently justify a confident
differentiation claim in any single area. The strongest candidates (HYP-001,
HYP-002, HYP-004) are all capped by the same limitation — they rest on what
mature systems do **not publicly document**, which is weaker evidence than what
they do.

**Every entry above remains a research hypothesis.** None is a decision, a
principle, or a commitment.

## Related documents

- [Design System Benchmark](DESIGN_SYSTEM_BENCHMARK.md)
- [Benchmark Evidence Matrix](BENCHMARK_EVIDENCE_MATRIX.md)
- [Benchmark Source Register](BENCHMARK_SOURCE_REGISTER.md)
- [Research Limitations](RESEARCH_LIMITATIONS.md)
