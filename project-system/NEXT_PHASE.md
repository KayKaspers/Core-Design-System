# Next Phase

- **Phase:** Foundation / Pre-Design
- **Completed work packages:** CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003
- **Next work package:** CDS-WP-004 — Consumer Requirements and CoreOps Pilot
  Contract

## Status of completed work packages

### CDS-WP-001 — Project Governance and NDF Bootstrap — Completed

Established the project charter, the role and authority model, the strategic
foundation decisions DEC-S-001 … DEC-S-006, the initial risks
RISK-001 … RISK-005, the controlled work-package roadmap, and the local Claude
operating instructions.

### CDS-WP-001A — NDF Skills Bootstrap — Completed

Adopted the released NDF v1.0.0 Claude Skills into `.claude/skills/` — 38
verified docs-only Skills, 39 files, pinned to commit
`9dcadc12fb960914b9a5baeff2ab1aee75912b57`, byte-identical to the released tag
— and activated the Skills-first operating mode.

### CDS-WP-002 — Concept and Scope Registration — Completed

Registered the binding project concept: six capability domains, ten
cross-cutting concerns, current Foundation scope separated from long-term scope,
twelve non-goals, direct users and indirect beneficiaries, three consumer
relationship classes, ownership boundaries, and the CoreOps pilot boundary.
Added DEC-S-007 … DEC-S-012 and RISK-006 … RISK-009.

### CDS-WP-003 — Benchmark and Differentiation Research — Completed

Reviewed ten established design systems against 14 dimensions using official
publisher sources only, and assessed the eight differentiation hypotheses
HYP-001 … HYP-008. Added RISK-010 … RISK-013. No decision was added or changed.

**The research results are explicitly non-normative.** They are research
evidence and differentiation hypotheses — not decisions, not principles, not a
design brief, and not a technology recommendation. No hypothesis reached
"Strongly supported"; the strongest candidates rest on what mature systems do
not *publicly document*, which is weaker evidence than what they do.

Research documents:
[Design System Benchmark](../docs/research/DESIGN_SYSTEM_BENCHMARK.md) ·
[Evidence Matrix](../docs/research/BENCHMARK_EVIDENCE_MATRIX.md) ·
[Source Register](../docs/research/BENCHMARK_SOURCE_REGISTER.md) ·
[Differentiation Hypotheses](../docs/research/CDS_DIFFERENTIATION_HYPOTHESES.md) ·
[Research Limitations](../docs/research/RESEARCH_LIMITATIONS.md)

Completion is reported for Human Maintainer review. No Git write action was
performed.

## Next work package: CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract

### Objective

Capture requirements from CoreOps and the further consumer classes, separate
shared from product-specific requirements, define the pilot scope and validation
contract, and test the differentiation hypotheses against real consumer needs.

### Scope direction

- collect requirements from CoreOps and from further consumer classes,
- separate shared requirements from product-specific requirements,
- define the pilot scope and the validation contract,
- test HYP-001 … HYP-008 against real consumer requirements rather than against
  absence of public documentation,
- state what CDS does **not** do for the pilot as explicitly as what it does,
- apply the DEC-S-011 acceptance conditions to any candidate generalization,
- validate the six assumptions registered in
  [Concept and Scope](../docs/governance/CONCEPT_AND_SCOPE.md).

### Research input to carry forward

- The benchmark evidence is **not normative** and must not be cited as a
  decision or a requirement.
- Findings are a dated snapshot (2026-07-15) and decay; re-verify a source
  before relying on it (RISK-012).
- The reviewed sample consists only of large technology companies and national
  governments, and cannot represent smaller or community systems (RISK-011).
- Hypotheses stay hypotheses until validated against real consumer needs
  (RISK-013).
- Do not import any reviewed system's identity, taxonomy, structure, or wording
  (RISK-010).

### Explicitly prohibited in CDS-WP-004

- concrete visual design of any kind,
- technology, tool, framework, or token-format selection,
- selecting colours, typography, icons, logos, or themes,
- licensing, publication, or support commitments,
- promoting a differentiation hypothesis to a decision without evidence,
- treating CoreOps requirements as automatically normative (DEC-S-011),
- modifying Skill files,
- extending the roadmap.

### Authorization note

CDS-WP-004 requires an explicit work-package prompt from Nova before execution
begins. Being listed as **Next** identifies the sequence; it does not by itself
authorize the work.

## Related documents

- [Work Packages](WORK_PACKAGES.md)
- [Project Profile](PROJECT_PROFILE.md)
- [Foundation Context Pack](CONTEXT_PACK_FOUNDATION.md)
- [Project Charter](../docs/governance/PROJECT_CHARTER.md)
