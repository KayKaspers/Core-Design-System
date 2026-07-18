# First Semantic Status Candidate Plan

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-014 — Semantic Status Foundation Contract and First
  Candidate Plan
- **Date:** 2026-07-17
- **Status:** **A plan, not a promotion.** Pending Human-Maintainer commit.
  **Nothing is Candidate today** (DEC-S-113, DEC-S-114); this document defines
  what the first Candidate would be and what must be true first.

## Target artifact

The first planned CDS design Candidate is the **Semantic Status Foundation
Contract** together with its future **machine-readable Semantic Source Set**
(DEC-S-113) — a meaning foundation, deliberately not a visual one: the first
thing CDS commits to at Candidate maturity is *truthful status semantics*, the
area with the strongest multi-consumer evidence (CR-006, CR-007).

## Candidate scope

Included:

- the **five axes** and their **25 axis values**
  ([Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md));
- the **ten invariants**
  ([Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md));
- the **combination and conflict rules** including review-required
  combinations and fail-closed states
  ([Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md));
- the **communication contract** (textual meaning, multi-modal, qualifiers,
  channel preservation —
  [Communication Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md));
- the **token role contract**
  ([Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md));
- **DE/EN semantic parity** of status meaning.

## Exclusions

Not part of the first Candidate: visual values of any kind (colour,
typography, icons, spacing, motion, themes); UI components; CoreOps or any
consumer integration; Product Profiles; mobile/non-web implementations; any
Stable status; any conformance, adoption, or accessibility claim. Scope
expansion into these areas before the contract and evidence are ready is a
registered risk (RISK-089) and a NO-GO trigger, not a stretch goal.

## Candidate Package

*(The reviewable bundle the promotion decision will be made on — 8 elements.)*

| # | Element | State in CDS-WP-014 |
| --- | --- | --- |
| 1 | Normative human-readable Status Contract (the four foundations documents) | Drafted (Experimental) |
| 2 | Machine-readable Semantic Source Set (`.tokens.json`, CDS profile v1, DTCG 2025.10) | **Implemented (CDS-WP-015)** — [`semantic/status`](../../tokens/semantic/status/semantic-status.tokens.json), Experimental |
| 3 | Localization and terminology mapping DE/EN | **Created (CDS-WP-015)** — [25/25 mapping](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md), executor-drafted |
| 4 | Positive and negative validation fixtures for status semantics | **Created (CDS-WP-015)** — 1 positive + 8 negative under `tests/fixtures/semantic-status/` |
| 5 | Validation execution evidence (offline validator, machine-readable results, digests) | **Produced (CDS-WP-015)** — 24/24 harness + source-set run, executor-produced, independently unreviewed |
| 6 | Accessibility and content review evidence (non-visual meaning, DE/EN parity, understandability) | **Drafted (CDS-WP-015)** — executor-produced contract reviews; no user research, AE-0 |
| 7 | Known limitations register for the Candidate | **Recorded (CDS-WP-015)** — inside the [dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md) |
| 8 | Candidate dossier (Elevated change dossier binding 1–7) | **Draft (CDS-WP-015)** — gate incomplete (DEC-S-122) |

## Candidate prerequisites

*(All gates, cumulative — none is met or waived by CDS-WP-014.)*

1. **CDS-WP-014 committed** by the Human Maintainer.
2. **WP-013 validator evidence independently reviewed** — or re-executed and
   then independently reviewed (executor ≠ reviewer, DEC-S-103; currently
   `independentReviewState: pending`).
3. **Evidence Reviewer authorized** (Nova or a separately authorized reviewer,
   DEC-S-045).
4. **Machine-readable Semantic Source Set implemented** under the CDS Token
   Format Profile.
5. **Validator harness passed for that source set** (V1–V4 with committed
   expected outcomes; machine-readable, revision-bound evidence).
6. **No Blocking or High defects** open against the contract or source set
   (accessibility defect model applies).
7. **Accessibility and content review completed** (multi-modal meaning,
   unknown/limitation language, understandability).
8. **DE/EN parity reviewed** (semantic parity, no contradictory translations).
9. **Nova review** with a promotion recommendation.
10. **Human-Maintainer approval** of the maturity transition (Experimental →
    Candidate; DEC-S-036 — Candidate is mandatory before Stable and is itself
    gated).

## Evidence plan

- **Structural evidence:** completeness of axes/values (5/25), ID uniqueness
  and naming-profile conformance, absence of prohibited aggregations,
  source-set and profile validation (schemas + V1–V3), reference and
  provenance integrity (manifest/resolver binding, revision-bound identities).
- **Semantic evidence:** meaning review of all 25 values; combination and
  conflict coverage (all six review-required combinations exercised; all
  eight fail-closed states provoked by negative fixtures); the
  unknown/stale/evidence invariants demonstrated end-to-end; no contradictory
  inferences derivable.
- **Accessibility and content evidence:** non-visual expressibility of every
  value; DE/EN parity; clear unknown- and limitation-communication; label
  flexibility; applicability to future interactive use (keyboard/screenreader
  obligations stated and reviewable).
- **Consumer evidence:** **none exists in CDS-WP-014.** Later at minimum: a
  bounded CoreOps reconciliation against concrete tasks and states (read-only,
  revision-bound, DEC-S-013), without activating the pilot before its entry
  criteria (RISK-018). Consumer evidence informs the Candidate review; it is
  not a pilot start.

## Gate state after CDS-WP-015

Prerequisite 1 (WP-014 committed) is met; 4 and parts of 5 are implemented but
their evidence is executor-produced and **independently unreviewed**;
prerequisites 2–3 and 6–10 remain open. **Candidate Status: Not Candidate.**
Detail: [Candidate Dossier](../operations/SEMANTIC_STATUS_CANDIDATE_DOSSIER.md).

## Known blockers

1. WP-013 evidence is executor-produced and **independently unreviewed**
   (RISK-078) — prerequisite 2 is open.
2. No machine-readable source set exists (prerequisites 4–5 open).
3. No accessibility/content/parity review evidence exists (prerequisites 6–8
   open; every artifact is AE-0).
4. Licensing/publication state unchanged (`Private Development`) — publication
   is out of scope for the Candidate and remains blocked separately.

## Human-Maintainer decisions required

Commit of CDS-WP-014 · authorization of the independent Evidence Review ·
authorization of CDS-WP-015 · the eventual maturity transition itself. None of
these is made, implied, or scheduled by this plan.

## No-promotion statement

**CDS-WP-014 promotes nothing.** The Semantic Status Foundation remains
**Experimental**; the WP-013 harness result is a bounded, executor-produced
observation and **no Candidate evidence** (DEC-S-104). Unclear readiness at any
future gate resolves as NO-GO, never as "go with notes" (DEC-S-048).

## Next work package

**CDS-WP-015 — Semantic Status Foundation Source Set and Candidate Evidence**
(registered as Next; not executed): the machine-readable Semantic Source Set
(value-neutral roles and identifiers), positive/negative status fixtures,
validator execution with committed expected outcomes, accessibility/content
evidence preparation, and Candidate-dossier preparation — still without visual
values and without a Candidate award. Execution requires an explicit Nova
prompt and Human-Maintainer authorization.

## Related documents

- [Semantic Status Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
- [Semantic Status Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md)
- [Readiness Review](../reviews/SEMANTIC_STATUS_FOUNDATION_READINESS_REVIEW.md)
- [Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md)
- [Pre-Candidate Operating Plan](PRE_CANDIDATE_OPERATING_PLAN.md)
- [Offline Token Validator Execution Review](../reviews/OFFLINE_TOKEN_VALIDATOR_EXECUTION_REVIEW.md)
