# CDS-WP-014 — Semantic Status Foundation Contract and First Candidate Plan — Notes

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-014 (Completed; pending Human-Maintainer commit)
- **Date:** 2026-07-17
- **Executor:** Claude (scoped executor). This evidence is executor-produced; the
  readiness review is a self-assessment, not an independent review.

## Assignment

Define the first concrete CDS design foundation — the **Semantic Status
Foundation**: the channel-independent semantic contract for the five status axes,
a controlled vocabulary, combination/conflict rules, accessibility/content/
localization requirements, a value-neutral semantic token contract, a bounded
first Candidate plan, and its evidence/review model. Explicitly not: colours,
typography, spacing, icons, motion, themes, real token files, components, Product
Profiles, CoreOps implementation, Candidate/Stable status, claims.

## Preflight

- Repository `D:\Projects\Core-Design-System`, branch `main`, working tree
  **clean**, no merge/rebase/cherry-pick, origin correct.
- Last commit `a7f2691` ("feat(cds): implement offline token profile validator")
  — **CDS-WP-013 committed**.
- Registers verified by script: Decisions 104 (contiguous) · Risks 81
  (74 Monitored / 7 Mitigating: 040, 044, 066, 067, 068, 069, 071) · ADRs 3 ·
  CR-001…040 (40).
- Work packages: 001…013 Completed, 014 Next ✓.
- Architecture preconditions: 8 layers, 8 artifact classes, 5 token-flow levels,
  **5 status axes** (Evidence/Status-Semantics doc), **16 architecture
  invariants** — the five axes derive unambiguously; no source permits
  unknown/stale/unavailable/incomplete/unverified to read as healthy/successful.
- Validator: 71 unit tests passed, 15/15 expected/actual matches,
  `independentReviewState: pending` ✓ (not Candidate).
- Accessibility: WCAG 2.2 AA target, A11Y-BL-001 defined, every design artifact
  AE-0 ✓.
- Publication `Private Development`; no Candidate/Stable/claim; pilot inactive ✓.
- Skills: 38 directories, 39 files, **39/39 manifest SHA-256 matches** ✓.
- Fail-closed conditions: **none triggered.** No web research performed.

Read in full: the listed normative architecture/accessibility/governance sources
(EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS, DESIGN_SYSTEM_ARCHITECTURE
invariants, ACCESSIBILITY_REQUIREMENTS_BASELINE areas 7/8,
TOKEN_AND_THEME_ARCHITECTURE, CDS_TOKEN_FORMAT_PROFILE naming profile, and the
project-control files) plus the three newly authorized skills; the eight
remaining authorized skills were fully read earlier in this session and used
from context.

## Skills used (11; only the authorized set)

ndf-work-package-runner (WP frame) · ndf-architecture-blueprint-runner (contract
family structure) · ndf-accessibility-reviewer (communication contract review
posture; advisory, no certification) · ndf-ux-flow-reviewer (disclosure/summary
flow honesty) · ndf-content-tone-reviewer (unqualified-claim prohibitions,
DE/EN parity rules) · ndf-validation-evidence-reviewer (honest readiness grades,
executor-produced labeling) · ndf-existing-project-analysis-runner (preflight
structure) · ndf-feature-scope-runner (scope/non-scope sharpening) ·
ndf-adr-governance-review (no-new-ADR check: DEC-S-105…114 need no ADR; ADR
count stays 3) · ndf-context-pack-maintainer (context pack update) ·
ndf-compact-context-summary-runner (closing blocks). No further skills.

## Created artifacts

- **[SEMANTIC_STATUS_FOUNDATION_CONTRACT.md](../docs/foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)**
  — normative main source: purpose/authority, scope, non-scope, five-axis model,
  11-field complete object, **ten invariants**, target/evidence/claim boundary,
  channel + Product-Profile/Consumer-Extension boundaries, Experimental maturity,
  Elevated change control.
- **[STATUS_AXIS_VOCABULARY.md](../docs/foundations/STATUS_AXIS_VOCABULARY.md)**
  — 5 axes × 5 values = **25 values**, each with the seven mandated attributes;
  all mandatory meaning bounds implemented (nominal ≠ verified/current/available;
  none = no *known* impact; verified requires identified current evidence;
  current requires documented time; available ≠ correct; not-applicable requires
  rationale; unknown standalone, never a default). Counts + independent re-count
  at the end.
- **[STATUS_COMPOSITION_AND_CONFLICT_RULES.md](../docs/foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md)**
  — 11 object fields, independent composition, **6 review-required
  combinations** (exactly the mandated minimum), **8 fail-closed conditions**,
  rationale/provenance rules, 6-level disclosure priority, no-aggregate rule,
  abstract value-neutral examples.
- **[STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md](../docs/foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md)**
  — text-first meaning, multi-modal contract, screenreader/keyboard boundary
  (obligations, not evidence), understandable unknown/limitation language,
  reduced-motion boundary, DE/EN parity, flexible labels, channel preservation,
  no visual values, no final UI copy.
- **[SEMANTIC_STATUS_TOKEN_CONTRACT.md](../docs/foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md)**
  — role boundary, axis relationship (no irreversible aggregation), planned
  source set (Semantic layer, DTCG 2025.10, CDS profile v1, Experimental, not in
  WP-014), component/Product-Profile/generated-output boundaries, no-current-
  token and no-value statements, planned validation requirements.
- **[FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md](../docs/roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md)**
  — target artifact, scope, exclusions, **8-element Candidate package**, **10
  cumulative prerequisites (none met/waived)**, four-class evidence plan,
  independent-review requirement, known blockers, Human-Maintainer decisions,
  no-promotion statement, CDS-WP-015 as next.
- **[SEMANTIC_STATUS_FOUNDATION_READINESS_REVIEW.md](../docs/reviews/SEMANTIC_STATUS_FOUNDATION_READINESS_REVIEW.md)**
  — 9 criteria: 0 Met · 5 Met with notes · 2 Partially met · 1 Not met
  (Candidate readiness, by design) · 1 Not applicable (consumer evidence); no
  numeric score; executor-produced.

## Registers

- **DEC-S-105…114** added exactly (10); total **114**, contiguous; DEC-S-001…104
  textually unchanged; **no new ADR** (ADR count stays 3).
- **RISK-082…089** added exactly (8); total **89**, contiguous; all Monitored
  with the finalized role model; **no existing risk status changed** (Mitigating
  set unchanged: 040, 044, 066, 067, 068, 069, 071); no acceptance/closure.

## Status files updated

WORK_PACKAGES (014 Completed, 015 Next, no further ID) · NEXT_PHASE (fully
oriented to CDS-WP-015) · PROJECT_PROFILE (current/previous WP, foundation
section with 5/25/10 counts, register spans 114/89, ADR 3, links) ·
CONTEXT_PACK_FOUNDATION (WP row, source map, decision/risk tables and spans,
tail) · PROJECT_BRAIN (header, WP-014 section, next step, links) · README
(status paragraph, foundation section with links, WP list) · CLAUDE.md (status
lines, foundation boundary, next WP) · CHANGELOG (Unreleased WP-014 block).

## Corrections to pre-existing content (logged per the allowed-files rule)

`PROJECT_PROFILE.md` carried four stale statements contradicting the WP-013
sections of the same file (a current-state document, so recency-conflicts fail
closed rather than stand): "no validator" in the schema-foundation line, "no
validator implemented" in the source-status boundary, "Schema execution: Not
assessed", and "no canonicalizer implemented; digests Not computed". All four
were corrected to the post-WP-013 truth with explicit executor-produced/
independently-unreviewed labeling. No other pre-existing normative content was
altered.

## Quantitative validation

All figures derived from the created artifacts and independently re-counted by
script (axes/values via `### \`axis: value\`` heading count and per-axis
distribution; invariants via table rows; object fields, review combinations,
fail-closed rows, disclosure levels via table/list counts; package elements and
prerequisites via numbered lists; registers via regex ID scans; results in the
report to Nova). **Counting errors found and corrected: none** in this WP's
artifacts (the register scans matched first derivations).

## Deviations

1. Eight of the eleven authorized skills were not re-opened from disk in this
   work package; they were fully read earlier in this same session and applied
   from context. The three newly authorized skills (accessibility-, ux-flow-,
   content-tone-reviewer) were read from disk.
2. Four stale `PROJECT_PROFILE.md` lines corrected (see above) — a consistency
   correction inside an Allowed File, fully logged here.
3. None otherwise: no visual value, no token file, no promotion, no claim, no
   web research, no Git write action.

## Open items

- Independent review of WP-013 validator evidence remains **pending** (Candidate
  prerequisite 2).
- DE/EN terminology mapping, machine-readable source set, fixtures, and all
  Candidate evidence are CDS-WP-015 and later.
- The CDS/consumer semantic boundary (CR-035) remains an explicitly open
  question.

## Completion status

**PASS** against the Definition of Done. The Semantic Status Foundation is
**Contract defined — Experimental, no Candidate status**. No Git write action
was performed.
