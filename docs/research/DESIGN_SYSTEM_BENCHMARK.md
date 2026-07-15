# Design System Benchmark

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-003 — Benchmark and Differentiation Research
- **Access date for all evidence:** 2026-07-15
- **Status:** Research evidence — **not normative**

## Purpose

This document records what ten established design systems publicly document,
what recurring structures emerge across them, and what CDS can reasonably learn.
It exists to make later architecture and governance work evidence-based rather
than assumed.

## Authority and non-normative status

**This document decides nothing.**

It is research evidence. It is not a normative source, not a decision, not a
design brief, and not a technology recommendation. It creates no CDS commitment
of any kind.

Normative scope remains
[Concept and Scope](../governance/CONCEPT_AND_SCOPE.md). Decisions remain the
[Decision Index](../decisions/DECISION_INDEX.md). Nothing here changes either.
No decision was added or altered by CDS-WP-003; the decision range stays
DEC-S-001 … DEC-S-012.

No system reviewed here is a model for CDS to copy. Naming a system is source
attribution, not endorsement.

## Methodology

1. Ten systems were fixed in advance by the work-package prompt. None were added
   or substituted.
2. Each system was examined against the same 14 dimensions (A–N).
3. Only official publisher documentation and official publisher repositories
   were opened.
4. Every observation is paraphrased and tied to a registered URL with an access
   date in [BENCHMARK_SOURCE_REGISTER.md](BENCHMARK_SOURCE_REGISTER.md).
5. Where a property could not be verified, it is recorded with an explicit
   evidence status. Nothing was filled in from memory.
6. Undocumented internal practice was never inferred.

### Source-selection rules

Permitted: official design-system documentation, official standards pages,
official public repositories of the publisher, official release and migration
documentation.

Excluded: encyclopedias, blog platforms, private and agency blogs, comparison
portals, social media, search snippets, AI-generated summaries, unofficial
mirrors, third-party archives.

### Evaluation rules

No numeric scores. No overall ranking. No winner. A weakness is stated only when
evidence supports it; otherwise it is recorded as a trade-off, a limitation of
the reviewed evidence, or a CDS-specific mismatch.

---

## System profiles

Each profile is deliberately short. Detail lives in the
[Evidence Matrix](BENCHMARK_EVIDENCE_MATRIX.md).

### 1. IBM Carbon Design System

Vendor-funded and vendor-built, deliberately open-sourced for outside use and
contribution while also serving internal business units under an inner-source
model. Positioned as the digital expression of the corporate brand. Patterns are
harvested from products actually built with the system and contributed back.

- **Notable strength:** An explicit, honest maintenance model. Contributed
  components and patterns carry named maintainers, and the core team triages
  what has none. Framework bindings are openly labelled first-party or
  community-maintained, so consumers can see support reality before adopting.
- **Trade-off:** Serving an open community and internal business units
  simultaneously means two audiences with different needs share one system.
- **Evidence gap:** No public per-component maturity label found; testing regime
  not detailed in reviewed pages.
- **CDS lesson:** Publish who maintains what. Support asymmetry that is visible
  is manageable; support asymmetry that is hidden becomes a broken promise.

### 2. Microsoft Fluent 2

Vendor system spanning web and native platforms, addressed to designers and
developers, with a predecessor generation still linked and maintained.

- **Notable strength:** Parallel major lines are allowed to coexist for
  different consumer generations, with a documented migration path — a realistic
  answer to consumers who cannot all migrate at once.
- **Trade-off:** Parallel lines multiply maintenance surface and force consumers
  to choose a generation before they understand the difference.
- **Notable observation:** Code and brand assets are on deliberately different
  terms — a permissive licence for repository files, a separate assets licence
  agreement for fonts and icons.
- **CDS lesson:** Code and brand assets are different legal objects. Any future
  CDS licensing thinking must treat them separately — routed to CDS-WP-006.

### 3. Google Material Design 3

General-purpose UI system with explicit brand-expression support, structured
around foundations that include accessibility, content design, customization,
tokens, interaction states, and layout.

- **Notable strength:** Accessibility and content design are named foundations
  rather than appendices. Brand expression is treated as a first-class,
  supported customization rather than a deviation.
- **Trade-off — and the most instructive finding of this review:** the
  documented token workflow runs **through a proprietary design tool and its
  plugin**. Tokens are generated and edited as styles inside the tool, then
  exported to platform targets. The design tool is positioned in the middle of
  the token chain.
- **CDS mismatch:** This is precisely the arrangement DEC-S-004 exists to
  prevent and RISK-004 exists to monitor. Documented here as evidence, not as
  criticism — the arrangement is coherent for its publisher and its consumers.
- **CDS lesson:** Tool-centred token workflows are convenient and are common
  practice at scale. They are still a source-of-truth dependency. CDS should
  learn the ergonomics without adopting the dependency.

### 4. GitHub Primer

Vendor system for one company's products, explicitly split into product UI and
brand UI, with shared foundations across both.

- **Notable strength:** The clearest accessibility **evidence** model observed.
  A stated conformance aim (WCAG 2.2 AA), publicly published conformance
  reports, a named regulatory standard, embedded accessibility designers, and
  shared checklists. The claim is externally checkable rather than asserted.
- **Notable strength:** Product UI and brand UI are separated as first-class
  surfaces sharing foundations — the clearest channel split observed.
- **Evidence gap:** Contribution process and versioning model were not obtained
  through the routes reviewed.
- **CDS lesson:** This is the strongest available support for DEC-S-012.
  "We aim for a stated level, and here is the published report" is a defensible
  claim. "We are accessible" is not.

### 5. Atlassian Design System

Vendor system whose stated aim is cohesion and familiarity across a product
family — the closest mandate to the CDS product-family situation.

- **Notable strength:** Tokens are stated to be the single source of truth for
  naming and storing design decisions, with a searchable library — a
  documentation-led rather than tool-led framing.
- **Evidence gap:** Token layering, theming, contribution process, and
  versioning were not described on the pages reviewed. This is a depth-of-review
  limitation.
- **CDS lesson:** The product-family cohesion mandate is real and is pursued by
  serious systems. CDS is not unusual in wanting it; it will be unusual only in
  how it governs it.

### 6. Adobe Spectrum and Spectrum 2

Vendor system for internal product teams, reviewed as one evolution line.
Spectrum is the current design language; Spectrum 2 is a publicly communicated
major successor.

- **Notable strength:** A generational successor is communicated openly and
  separately, with the predecessor kept available during transition, and the
  direction described as shaped by a broad internal cross-disciplinary
  community.
- **Notable strength:** Spectrum 2 frames inclusive design around
  personalization — size, scale, colour, contrast — rather than a single
  compliance threshold.
- **Trade-off:** A long, publicly visible transition creates an extended period
  where two generations coexist and consumers must decide when to move.
- **CDS lesson:** Major evolution is survivable if it is communicated as its own
  artifact rather than silently replacing the old one.

### 7. SAP Fiori Design System

Enterprise system described as modular and multi-technology, with centrally
defined components that products may extend or modify to fit specific needs, and
distinct per-platform guideline sets.

- **Notable strength:** The central-plus-extension model is stated explicitly —
  the closest observed analogue to a governed product-profile mechanism, and
  directly relevant to HYP-005.
- **Trade-off:** "Extend or modify to fit specific needs" is exactly where
  fragmentation risk lives (RISK-008). The reviewed sources did not state what
  constrains that extension.
- **Access note:** The historical documentation domain now issues a permanent
  redirect to the corporate domain; the redirect target refused the fetch method
  and was read via the page view.
- **CDS lesson:** Permitting product extension without publishing its limits is
  the failure mode CDS must avoid. The mechanism is worth learning; the missing
  constraint is worth not copying.

### 8. Salesforce Lightning Design System 2

Platform-ecosystem system addressed separately to administrators, designers, and
developers, presented as a successor generation with its own site.

- **Notable strength:** An architecture stated to prioritize CSS custom
  properties, which lowers framework coupling at the styling layer, plus tooling
  to validate, migrate, and create components. Role-based transition instructions
  acknowledge that migration is a different job for different people.
- **Trade-off:** The successor is tied to platform-specific adoption steps, and
  the reviewed page foregrounds generative-AI direction alongside the design
  system itself.
- **CDS lesson:** Migration guidance segmented by role is a better model than one
  generic upgrade note. Consumers do not migrate as a single abstract actor.

### 9. GOV.UK Design System

Public-sector system whose stated purpose is consistency across government
services and reuse of other teams' research.

- **Notable strength:** The clearest **responsibility split** observed anywhere
  in this review. The system states plainly that using it does not by itself
  make a service accessible, and that teams must still do their own research,
  design, development, and testing. Regulatory work is described as continuous
  and iterative rather than achieved.
- **Notable strength:** An explicit staged contribution path — propose, develop,
  review against stated criteria — with public per-item discussion and user
  research as a first-class, templated community input.
- **Notable strength:** Documentation site and frontend implementation are
  deliberately separate repositories.
- **Evidence gap:** The reviewed page describes how to participate but does not
  state who holds final decision authority.
- **CDS lesson:** This is the strongest model found for DEC-S-008 and RISK-006.
  Stating what the system does *not* do is what makes the boundary real. CDS
  should copy this honesty, not by imitation but by principle.

### 10. U.S. Web Design System

Government-maintained system serving many agencies and sites.

- **Notable strength:** **The most explicit maturity model observed.** Four
  public lifecycle phases — proposal, development, released, deprecated — with
  named states. Released distinguishes experimental, stable, and
  use-with-caution, each with a stated meaning. Deprecated and retired are
  separated, distinguishing "unmaintained but present" from "removed". Per
  component status is published, including proposal-phase items.
- **Notable strength:** Accessibility testing is a **gating condition inside the
  lifecycle**, not a separate claim: the experimental state is defined partly by
  passing accessibility tests while still being subject to change.
- **Notable strength:** The most permissive publication model observed — a
  public-domain dedication with documented exceptions, consistent with a
  government mandate.
- **Trade-off:** A public proposal process with a stated minimum comment period
  is transparent but slow. That cost buys legitimacy; a small team should not
  assume it can afford the same process unchanged.
- **CDS lesson:** This is the strongest available support for DEC-S-009 and
  DEC-S-012. A published maturity state is what makes "registered but not
  available" an honest, machine-readable statement rather than a disclaimer.

---

## Cross-system findings

Findings are classified: **[Source-backed]** directly evidenced;
**[Synthesis]** a pattern across several systems; **[CDS inference]** our
reasoning about implications for CDS.

### Structures widely common across mature systems

**[Synthesis]** All ten separate foundations from components, and most separate
patterns from components again. Foundations-then-components-then-patterns is
effectively the industry's settled information architecture. Tokens appear as a
named concern in most systems. Accessibility appears as a named section in all
ten.

**[CDS inference]** This layering is not a differentiator. CDS should adopt the
convention because consumers already expect it, and spend its originality
elsewhere.

### Practices that appear especially effective

**[Source-backed]** Four practices stood out, each from a different system:

1. **Published maturity states per component** (USWDS) — makes availability
   honest and checkable.
2. **Published conformance reports** (Primer) — makes an accessibility claim
   externally verifiable.
3. **Explicitly stating what the system does not guarantee** (GOV.UK) — makes
   the ownership boundary real.
4. **Naming who maintains each contributed part** (Carbon) — makes support
   asymmetry visible before adoption.

**[CDS inference]** All four are governance practices, not design practices. All
four are cheap to state and expensive to fake. All four map onto decisions CDS
has already taken (DEC-S-008, DEC-S-009, DEC-S-012).

### Recurring governance weaknesses and trade-offs

**[Synthesis]** Contribution governance is the most consistently thin area in
reviewed public documentation. Six of ten systems yielded no external
contribution process in the pages reviewed. Even the most explicit process found
(GOV.UK) describes participation clearly while not stating who holds final
decision authority.

**[Limitation of reviewed evidence]** This is partly a review-depth artifact and
partly real: governance often lives in internal process that public
documentation does not expose.

**[Synthesis]** Public, time-bounded proposal processes (USWDS) buy legitimacy
at the cost of speed. Vendor systems mostly do not attempt them.

**[CDS inference]** CDS cannot copy a large public governance process with its
maintainer capacity, and should not pretend otherwise. The applicable lesson is
that decision authority must be *stated*, which costs nothing. CDS has already
done this (DEC-S-005).

### Accessibility responsibility patterns

**[Source-backed]** Three distinct patterns appeared:

- **Standard-referencing** (Carbon): components follow an internal checklist
  derived from named external standards.
- **Evidence-publishing** (Primer): a stated conformance aim plus published
  conformance reports.
- **Boundary-stating** (GOV.UK): explicit that the system does not make a
  consumer's service accessible, and that teams retain testing obligations.
- **Lifecycle-gating** (USWDS): accessibility tests as a condition of a maturity
  state.

**[Source-backed]** WCAG 2.2 is a W3C Recommendation (2024-12-12) defining
levels A, AA, AAA, and it states explicitly that even AAA-conformant content
will not be accessible to people with every type, degree, or combination of
disability.

**[CDS inference]** The standard itself refuses to promise total accessibility.
That is decisive for CDS: any future CDS accessibility statement must be a
stated target plus evidence plus an explicit consumer obligation — never a
conformance claim. This is advisory input to CDS-WP-007 and certifies nothing
today.

### Component and pattern acceptance models

**[Source-backed]** Two credible models observed: **harvesting** proven patterns
out of shipping products and contributing them back (Carbon), and a **staged
public proposal** with explicit evaluation outcomes (USWDS, GOV.UK).

**[CDS inference]** Harvesting matches the CDS pilot situation directly.
DEC-S-011 already requires generalization plus explicit acceptance before a
CoreOps solution becomes normative — which is a harvesting model with a
governance gate. The benchmark supports that this is a real, working pattern,
not an invention.

### Design-tool and code-source relationships

**[Source-backed]** The strongest single finding of this review. Material
documents a token workflow that runs through a proprietary design tool and its
plugin, with export to platform targets. Carbon and Fluent maintain design kits
and code implementations in parallel without describing a synchronization
mechanism in reviewed pages. Atlassian frames tokens as the documented single
source of truth. GOV.UK separates the documentation site from the implementation
repository. SLDS centres the architecture on CSS custom properties.

**[Synthesis]** Tool coupling is common, largely undocumented, and rarely
presented as a risk by the systems themselves.

**[CDS inference]** DEC-S-004 and RISK-004 are validated by evidence, not just
by intuition. The systems most coupled to a design tool are not failing — they
are trading portability for ergonomics with an owner large enough to absorb the
consequence. CDS does not have that owner. **[Synthesis]** Notably, none of the
reviewed systems documented tool-independence as an explicit design goal, which
suggests the concern is under-served rather than solved.

### Product-family customization approaches

**[Source-backed]** SAP documents central components that products extend or
modify. Material treats brand expression as a supported customization. SLDS
offers advanced theming via CSS custom properties. Spectrum 2 frames
personalization as a direction.

**[Synthesis]** Every mature system permits product-level variation. None of the
reviewed sources stated the *limits* of that variation.

**[CDS inference]** The mechanism is common practice; the **governed limit** is
where the open question sits. This directly sharpens the open boundary question
already registered in the
[Scope Boundary Matrix](../governance/SCOPE_BOUNDARY_MATRIX.md): how much
individuality may a product profile express before it fragments the system?
Unresolved — routed to CDS-WP-005 and CDS-WP-006.

### Adoption and maturity approaches

**[Source-backed]** USWDS publishes per-component lifecycle status including
proposal-phase items. Fluent runs parallel generations with a migration path.
Spectrum and SLDS communicate generational succession publicly with the
predecessor retained. Carbon surfaces the current implementation version and a
last-updated date in the documentation.

**[Synthesis]** Mature systems converge on: version the artifact, state its
maturity, keep the predecessor available, document migration.

**[CDS inference]** Strong support for DEC-S-009 and DEC-S-012. Advisory input
to CDS-WP-006; no versioning or maturity model is selected here.

### Multi-channel coverage gaps

**[Source-backed]** In reviewed official sources, **no system documented
standards for PDF reports, presentations, or diagrams**. Data visualization was
documented by one system (Carbon), with its own guidance and implementation. An
explicit product-UI/brand-UI split was documented by one system (Primer). SAP
documents multi-platform product UI. Several systems reference brand
relationships without documenting non-product channel standards.

**[Synthesis]** Reviewed design systems are overwhelmingly **product-interface**
systems that touch brand at the edges. The document, report, presentation, and
diagram channels are essentially absent from their public scope.

**[CDS inference]** This is the largest apparent white space for CDS — and the
place where overstatement is most tempting. See HYP-001, which is explicitly
capped by this review's depth limits.

### Offline and self-hosted implications

**[Source-backed]** USWDS distributes precompiled assets and source files via a
package registry and direct downloads. Carbon distributes scoped packages.
Spectrum offers three implementations. GOV.UK separates implementation from
documentation.

**[Source-backed]** **No reviewed system stated an explicit offline or
self-hosted consumption guarantee**, and none was found treating mandatory
external runtime services as a documented constraint.

**[CDS inference]** Self-containable distribution is common; *stating* offline
and self-hosted usability as a governed requirement is not. DEC-S-006 therefore
addresses a real and under-documented gap. But absence of a documented
guarantee is not the same as inability — most of these artifacts are probably
self-hostable in practice. The honest claim is narrow: CDS may differentiate by
*committing* to it, not by being uniquely capable of it.

### Licensing and publication observations

For CDS-WP-006. **No licence is recommended, selected, or legally assessed
here.**

**[Source-backed]** Observed models span a wide range:

- Public-domain dedication with documented exceptions (USWDS) — the most
  permissive, aligned with a government mandate.
- Permissive open-source licences for code repositories (Carbon, Fluent,
  GOV.UK).
- **Code and brand assets deliberately separated** (Fluent): permissive licence
  for repository files, separate assets licence agreement for fonts and icons.
- Open-source implementations alongside downloadable fonts and icons under
  unreviewed terms (Spectrum).
- Open source coexisting with an internal inner-source model (Carbon).
- General all-rights-reserved and trademark notice on the documentation site
  (SLDS).

**[Synthesis]** Licensing is not one decision. Documentation, code, fonts,
icons, and brand assets routinely sit on different terms — and brand assets are
the most restricted category almost everywhere.

**[CDS inference]** Any future CDS licensing work must treat these as separate
objects rather than picking one licence for "CDS". This is an observation for
CDS-WP-006, not a recommendation. Publication, licensing, and contribution
rights remain undecided.

### Practices CDS should not copy

**[CDS inference]** Stated as CDS-specific mismatches, not as criticism. Each is
coherent for its publisher.

1. **Tool-centred token chains** (as documented by Material). Efficient at
   scale, but it places a proprietary tool in the source-of-truth path —
   contrary to DEC-S-004.
2. **Permitting product extension without publishing its limits** (as observed
   at SAP). The mechanism is valuable; the missing constraint is the
   fragmentation risk in RISK-008.
3. **Large public proposal processes with fixed comment periods** (USWDS).
   Excellent legitimacy, wrong cost structure for current CDS capacity.
4. **Parallel major generations maintained indefinitely** (as observed at
   Fluent). A rational answer to a huge installed base; unaffordable for a
   system with no installed base yet.
5. **Serving an open community and internal consumers from one system without
   distinguishing them** (a tension visible at Carbon). CDS has already chosen
   the opposite via the three consumer classes (DEC-S-010).
6. **Adopting any reviewed system's visual identity, taxonomy, component
   structure, or wording.** CDS must synthesize, never imitate (RISK-010).

---

## Implications for CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract

1. The harvesting model (Carbon) plus a governance gate is real, working
   practice. It supports the DEC-S-011 acceptance conditions. CDS-WP-004 should
   test those conditions against actual CoreOps needs.
2. GOV.UK's boundary-stating shows the pilot contract should state what CDS does
   **not** do for CoreOps as explicitly as what it does.
3. The product-extension question (SAP) must be put to real consumers: what do
   they actually need to vary, and why?
4. Operational-domain guidance (HYP-003) is unverified across the benchmark and
   must be tested against real CoreOps requirements rather than assumed.
5. Consumer classes (DEC-S-010) should be validated against the observation that
   every reviewed vendor system serves a narrower consumer set than CDS intends.

## Implications for CDS-WP-005 — Design System Architecture

1. Adopt the conventional foundations/components/patterns layering; it is settled
   expectation, not differentiation.
2. Treat the tool-coupling evidence as the central architectural constraint.
   Under DEC-S-004, the normative source must sit outside any proprietary tool,
   and the architecture must say where it does sit.
3. The token-format question stays open. The interoperability draft reviewed is
   explicitly a preview that instructs readers not to implement it or cite it as
   authoritative — so no format may be selected on its basis today.
4. The product-profile limit is the unresolved architectural question. Every
   system permits variation; none reviewed published its bounds.
5. Separating documentation from implementation (GOV.UK) is a proven,
   low-cost structural choice worth evaluating.
6. Offline and self-hosted use (DEC-S-006) must be an explicit architectural
   criterion, since the benchmark shows it is not something consumers can assume.

## Implications for CDS-WP-006 — Governance, Versioning, and Contribution

1. Published per-component maturity states (USWDS) are the most effective
   mechanism found for making DEC-S-009 operational.
2. Published conformance evidence (Primer) is the most effective mechanism found
   for making DEC-S-012 operational.
3. Licensing is multiple decisions across documentation, code, fonts, icons, and
   brand assets — never one.
4. Decision authority must be stated explicitly; the benchmark shows this is
   commonly left implicit even in otherwise strong governance.
5. Deprecation needs distinct states ("unmaintained but present" versus
   "removed"), per USWDS.
6. Migration guidance segmented by role (SLDS) beats a single generic upgrade
   note.

## Implications for CDS-WP-007 — Accessibility Policy

WCAG 2.2's own statement that even AAA conformance will not serve every
disability means CDS's future policy should be a stated target plus published
evidence plus an explicit consumer obligation — following the pattern of
GOV.UK's boundary statement and Primer's published reports, and USWDS's
lifecycle gating. **No conformance level is chosen here and nothing is
certified.**

---

## Unresolved questions

Carried forward. None is answered by this research.

1. What exactly is the normative source of truth for CDS, if not a design tool?
   → CDS-WP-005
2. How much may a product profile vary before the system fragments? → CDS-WP-005,
   CDS-WP-006
3. Which token interoperability approach is viable while the reviewed draft
   remains an unstandardized preview? → CDS-WP-005
4. Is multi-channel coverage (HYP-001) genuinely absent from mature systems, or
   absent from their *public documentation* and from this review's depth?
5. Do real consumers need operational-domain patterns (HYP-003) enough to
   justify the investment? → CDS-WP-004
6. What accessibility target can CDS actually evidence with its capacity? →
   CDS-WP-007
7. What maturity vocabulary fits CDS without importing another system's
   taxonomy? → CDS-WP-006
8. How should CDS license documentation, code, and brand assets differently? →
   CDS-WP-006

## Related documents

- [Benchmark Source Register](BENCHMARK_SOURCE_REGISTER.md)
- [Benchmark Evidence Matrix](BENCHMARK_EVIDENCE_MATRIX.md)
- [CDS Differentiation Hypotheses](CDS_DIFFERENTIATION_HYPOTHESES.md)
- [Research Limitations](RESEARCH_LIMITATIONS.md)
- [Concept and Scope](../governance/CONCEPT_AND_SCOPE.md) — normative scope source
