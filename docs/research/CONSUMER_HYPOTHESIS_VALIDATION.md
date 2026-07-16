# Consumer Hypothesis Validation

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract
- **Evidence date:** 2026-07-15
- **Status:** Research and validation evidence — **not normative, not a decision**

## Purpose and authority

This document adds a **consumer-evidence layer** to the hypotheses assessed in
CDS-WP-003. It answers a different question than the benchmark did.

- **CDS-WP-003 asked:** do mature design systems publicly document this?
- **CDS-WP-004 asks:** do real Core consumers actually need this?

**The CDS-WP-003 research assessments are reproduced unchanged and were not
modified** — that document remains the authority for the research layer. See
[CDS Differentiation Hypotheses](CDS_DIFFERENTIATION_HYPOTHESES.md).

No hypothesis becomes an accepted decision here. All eight remain **research
hypotheses** (DEC-S-019).

### The critical distinction

Consumer evidence can show that a **need is real**. It cannot show that the
capability is **unique to CDS** (DEC-S-019). A confirmed consumer need and a
differentiation claim are different things, and this document never converts one
into the other.

## Consumer assessment vocabulary

`Confirmed consumer need` · `Partially supported by consumer evidence` ·
`Not supported by reviewed consumer evidence` · `Human validation required` ·
`Out of current pilot scope`

## Evidence base

Three consumers, committed revisions, 15 sources (14 usable), documentation only.
**Level 1 evidence** — see [Consumer Validation Plan](../governance/CONSUMER_VALIDATION_PLAN.md).
No user research took place (RISK-017).

---

## HYP-001 — Unified multi-channel foundation

| Layer | Assessment |
| --- | --- |
| Research (CDS-WP-003, unchanged) | Moderately supported differentiation opportunity · uniqueness risk **High** |
| **Consumer evidence (CDS-WP-004)** | **Partially supported by consumer evidence** |

- **CoreOps evidence:** documentation and report references exist; PDF, diagram,
  and presentation needs appear only incidentally. CR-028, CR-029 carry
  `Context only` strength.
- **Secondary evidence:** CastCore documents a *serious* documentation standard —
  DE/EN parity enforced by a check script in CI (CR-027, repeated across
  consumers). CoreOps documents a language standard covering artifact classes.
- **Counter- and limiting evidence:** the strongest multi-channel evidence is for
  **documentation**, not for PDF, presentations, or diagrams. CR-030
  presentations has **no consumer evidence at all**. So the channel the benchmark
  showed as a white space is *not* the channel consumers demonstrably need.
- **Human validation required:** do consumers produce enough reports,
  presentations, and diagrams to justify the scope, given RISK-001?
- **Consequence:** documentation standards (CR-027) are the credible near-term
  channel candidate. PDF, diagrams, and presentations remain deferred with weak
  evidence. → CDS-WP-005

---

## HYP-002 — Offline and self-hosted consumption

| Layer | Assessment |
| --- | --- |
| Research (CDS-WP-003, unchanged) | Moderately supported differentiation opportunity · uniqueness risk **Medium** |
| **Consumer evidence (CDS-WP-004)** | **Confirmed consumer need** |

- **CoreOps evidence:** the strongest confirmation in this work package.
  Self-hosted, offline- and air-gap-capable operation with no cloud requirement
  for core functions is an *accepted product requirement*, not an aspiration. A
  dedicated model covers connectivity classes, offline identity, policy
  freshness, clock uncertainty, and reconciliation (CR-031, CR-032).
- **Secondary evidence:** SpeakCore and CastCore both position as self-hosted.
  CastCore documents offline handling.
- **Counter- and limiting evidence:** consumers need *their products* to run
  offline. That they need **CDS artifacts** to be offline-capable is a reasonable
  inference, not a documented requirement — no consumer states a requirement
  addressed to CDS. Runtime dependencies were not tested (prohibited).
- **Human validation required:** confirm that CDS artifacts specifically must
  carry the offline constraint.
- **Consequence:** DEC-S-006 is confirmed by real consumer need. Offline must be
  an explicit architectural criterion. → CDS-WP-005

---

## HYP-003 — Operations-oriented experience patterns

| Layer | Assessment |
| --- | --- |
| Research (CDS-WP-003, unchanged) | **Not verifiable in this research** · uniqueness risk **High** |
| **Consumer evidence (CDS-WP-004)** | **Confirmed consumer need** |

- **CoreOps evidence:** dense operational need is thoroughly documented —
  operations overview, monitoring, inventory, health and severity semantics,
  degraded and restricted modes, unknown operational state, topology, audit,
  preview-before-execute, plan-before-deployment (CR-005 … CR-016, CR-032).
- **Secondary evidence:** decisive. **All three consumers independently document
  graded status semantics**, and **two independently document that unknown must
  not read as healthy** (CR-007). CastCore ships a health score with an explicit
  separate unknown state; CoreOps holds an accepted requirement that missing data
  must not count as healthy.
- **Counter- and limiting evidence:** this is where CoreOps overfitting is most
  acute (RISK-002). The need is real; that it **generalizes** beyond operational
  products is not established. SpeakCore and CastCore are *also* infrastructure
  products — the sample cannot distinguish "operational products need this" from
  "all products need this". The benchmark could not assess this either, so both
  layers are silent on generalizability.
- **Human validation required:** does this generalize beyond operations-shaped
  products, or is CDS becoming an operations design system?
- **Consequence:** the research layer could not verify this; the consumer layer
  confirms the **need** strongly. The gap between them is the most important
  finding of CDS-WP-004. → CDS-WP-005, and DEC-S-016 for generalization.

---

## HYP-004 — Design-code-documentation convergence

| Layer | Assessment |
| --- | --- |
| Research (CDS-WP-003, unchanged) | Moderately supported differentiation opportunity · uniqueness risk **Medium** |
| **Consumer evidence (CDS-WP-004)** | **Partially supported by consumer evidence** |

- **CoreOps evidence:** a language standard governing terminology across artifact
  classes, with translation-status metadata and semantic parity (CR-033); the NDF
  version pinned by tag and commit in document headers (CR-034); the requirement
  that the UI must not use privileged internal shortcuts unavailable to API
  consumers (CR-040).
- **Secondary evidence:** CastCore enforces DE/EN documentation synchronicity via
  a check script in CI — an actual, working convergence mechanism. SpeakCore
  states that consistency comes from tokens rather than one-off values.
- **Counter- and limiting evidence:** consumers converge *their own* artifacts.
  None documents a requirement that **CDS** provide convergence. SpeakCore's own
  authoritative tokens sit outside the readable area, so the design-to-code link
  could not be inspected.
- **Human validation required:** is convergence a CDS deliverable, or something
  each consumer maintains for itself?
- **Consequence:** the mechanisms exist and work in consumers. CDS's role is
  unproven. → CDS-WP-005, CDS-WP-006

---

## HYP-005 — Governed product-family flexibility

| Layer | Assessment |
| --- | --- |
| Research (CDS-WP-003, unchanged) | Moderately supported differentiation opportunity · uniqueness risk **Medium-high** |
| **Consumer evidence (CDS-WP-004)** | **Confirmed consumer need** |

- **CoreOps evidence:** targets Core products as first-party integrations while
  explicitly being neither Core-exclusive nor Core-centred — a product family
  that must cohere without collapsing into one product (CR-001).
- **Secondary evidence:** the decisive finding. **SpeakCore and CastCore already
  hold their own product-local design decisions** — a stated style direction,
  brand-value mapping, a token-based palette, and their own brand assets (CR-002,
  CR-037). This is not hypothetical future divergence; it exists today.
- **Counter- and limiting evidence:** the need for governed flexibility is
  confirmed, but the **limit** is undocumented everywhere — exactly as the
  benchmark found for mature systems. No consumer states how much variation is
  acceptable. CDS also arrives *after* these decisions, so this is reconciliation,
  not greenfield governance.
- **Human validation required:** how much individuality is permitted, and what
  happens to design decisions consumers already shipped?
- **Consequence:** CDS cannot assume a blank slate. RISK-008 and RISK-016 are
  live. → CDS-WP-005 (mechanism), CDS-WP-006 (governance)

---

## HYP-006 — Evidence-based adoption

| Layer | Assessment |
| --- | --- |
| Research (CDS-WP-003, unchanged) | **Common industry practice, not differentiating alone** · uniqueness risk **Low** |
| **Consumer evidence (CDS-WP-004)** | **Partially supported by consumer evidence** |

- **CoreOps evidence:** version pinning by tag and commit in document headers;
  documents carry explicit status markers and decision classifications; evidence,
  provenance, and auditability are product principles (CR-034, CR-014).
- **Secondary evidence:** CastCore states honest maturity ("early beta … not yet
  production-hardened") and runs automated documentation-status checking — real
  evidence discipline.
- **Counter- and limiting evidence:** consumers apply version-bound evidence to
  *themselves*. None requests it from CDS. The consumers are already more mature
  at this than CDS is — CDS has no version, no maturity model, and no evidence
  model yet.
- **Human validation required:** what evidence can CDS actually produce at its
  capacity?
- **Consequence:** both layers agree this is sound practice rather than
  differentiation. It validates DEC-S-009 and DEC-S-012 as mainstream.
  → CDS-WP-006

---

## HYP-007 — Accessibility, localization, privacy, and security awareness

| Layer | Assessment |
| --- | --- |
| Research (CDS-WP-003, unchanged) | **Weakly supported** · uniqueness risk **High** |
| **Consumer evidence (CDS-WP-004)** | **Human validation required** |

The four bundled concerns have sharply different evidence, so bundling them
obscures the picture:

- **Localization — Confirmed.** The strongest evidence of the four. DE/EN is an
  accepted CoreOps product requirement with a full language standard; CastCore
  enforces DE/EN parity in CI; both treat German as first-class (CR-023, CR-027).
- **Accessibility — Not supported.** CoreOps names an "accessibility baseline"
  **with no conformance level and no evidence method**, in one document.
  CastCore documentation contains **no accessibility evidence at all**. Only
  SpeakCore documents concrete practice — contrast, visible focus, no colour-only
  coding (CR-021, CR-022, CR-006). This is thin for something CDS treats as a
  first-class quality area.
- **Security-aware interaction design — Confirmed.** Strongly. Read-only before
  write, preview before execute, plan before deployment, backup before dangerous
  change, verification after change, risk tiers, fail-closed (CR-010 … CR-013).
- **Privacy-aware interaction design — Partially.** CoreOps documents privacy by
  design with data classes, redaction, and retention, but as architecture rather
  than interaction design.

- **Counter- and limiting evidence:** accessibility is the weakest link in an
  area CDS claims as foundational — and no consumer asks CDS for it.
- **Human validation required:** **CR-024 — what accessibility level does CDS
  commit to, and how is it evidenced?** This is the single most important open
  question from this work package.
- **Consequence:** split the bundle. Localization and security-aware design are
  confirmed needs; accessibility needs a decision before it can be evidenced.
  → CDS-WP-007

---

## HYP-008 — Small-team and enterprise applicability

| Layer | Assessment |
| --- | --- |
| Research (CDS-WP-003, unchanged) | **Weakly supported** · uniqueness risk **High** |
| **Consumer evidence (CDS-WP-004)** | **Partially supported by consumer evidence** |

- **CoreOps evidence:** target groups explicitly span homelabs, self-hosters,
  clubs, small and medium businesses, education, developers, and IT departments,
  later MSPs and data centres — the small-team-to-enterprise span in one product.
  Simple and Expert modes are the documented mechanism (CR-018).
- **Secondary evidence:** all three consumers document Simple/Expert modes and
  guided setup with environment checks (CR-017, CR-018) — the clearest shared
  mechanism for serving both ends.
- **Counter- and limiting evidence:** the consumers are all self-hosted
  infrastructure products with similar audiences, so this sample cannot test the
  span. All three are maintained by the same small maintainer base — it cannot
  show whether CDS works for a small team *other than this one*. The research
  layer had the mirror-image bias (only large publishers, RISK-011).
- **Human validation required:** can CDS's governance rigour scale down without
  becoming ceremony?
- **Consequence:** Simple/Expert and guided setup are strong shared candidates
  regardless of the differentiation question. → CDS-WP-004 follow-up, CDS-WP-006

---

## Summary

| ID | Research layer (unchanged) | Consumer layer |
| --- | --- | --- |
| HYP-001 Multi-channel | Moderately supported | Partially supported by consumer evidence |
| HYP-002 Offline / self-hosted | Moderately supported | **Confirmed consumer need** |
| HYP-003 Operations patterns | Not verifiable in this research | **Confirmed consumer need** |
| HYP-004 Design-code-doc convergence | Moderately supported | Partially supported by consumer evidence |
| HYP-005 Governed family flexibility | Moderately supported | **Confirmed consumer need** |
| HYP-006 Evidence-based adoption | Common industry practice | Partially supported by consumer evidence |
| HYP-007 Accessibility et al. | Weakly supported | **Human validation required** |
| HYP-008 Small-team + enterprise | Weakly supported | Partially supported by consumer evidence |

**Count: 8 hypotheses — HYP-001 … HYP-008. No IDs added or removed.**

### What the two layers together say

Three hypotheses reach **Confirmed consumer need**: offline/self-hosted (002),
operations patterns (003), and governed family flexibility (005). Each is a real,
documented need in real products.

**None of them becomes a differentiation claim.** A confirmed need means CDS
should probably do it — not that CDS would be unique in doing it (DEC-S-019,
RISK-013). Notably, HYP-003 is the sharpest case: the benchmark **could not
verify** it and the consumers **strongly confirm** it. That combination means
CDS should build it because consumers need it, while knowing nothing about
whether it distinguishes CDS at all.

The inverse also holds: HYP-007's accessibility strand is weak in **both**
layers, which is uncomfortable for a concern CDS registered as first-class.

**No hypothesis is an accepted decision.** All remain research hypotheses.

## Related documents

- [CDS Differentiation Hypotheses](CDS_DIFFERENTIATION_HYPOTHESES.md) — research layer, unchanged
- [Consumer Requirements Model](../governance/CONSUMER_REQUIREMENTS_MODEL.md)
- [Consumer Evidence Register](CONSUMER_EVIDENCE_REGISTER.md)
- [Research Limitations](RESEARCH_LIMITATIONS.md)
