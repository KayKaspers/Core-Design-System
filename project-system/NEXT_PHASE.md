# Next Phase

- **Phase:** Foundation / Pre-Design
- **Completed work packages:** CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004
- **Next work package:** CDS-WP-005 — Design System Architecture

## Status of completed work packages

### CDS-WP-001 — Project Governance and NDF Bootstrap — Completed

Project charter, role and authority model, DEC-S-001 … DEC-S-006,
RISK-001 … RISK-005, the controlled roadmap, and the local Claude operating
instructions.

### CDS-WP-001A — NDF Skills Bootstrap — Completed

38 verified docs-only NDF v1.0.0 Skills, 39 files, pinned byte-identical to
commit `9dcadc12fb960914b9a5baeff2ab1aee75912b57`; Skills-first mode activated.

### CDS-WP-002 — Concept and Scope Registration — Completed

Six capability domains, ten cross-cutting concerns, current versus long-term
scope, twelve non-goals, three consumer classes, ownership boundaries, CoreOps
pilot boundary. Added DEC-S-007 … DEC-S-012 and RISK-006 … RISK-009.

### CDS-WP-003 — Benchmark and Differentiation Research — Completed

Ten design systems reviewed against 14 dimensions from official sources; eight
differentiation hypotheses assessed. Added RISK-010 … RISK-013. **Results remain
non-normative.**

### CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract — Completed

Three consumer repositories analyzed read-only at committed revisions; 40
requirements registered and traced; the bounded CoreOps pilot and its contract
defined; HYP-001 … HYP-008 assessed against consumer evidence. Added
DEC-S-013 … DEC-S-020 and RISK-014 … RISK-019.

**Requirements are input, not approval.** No requirement is an accepted CDS
standard (DEC-S-014), and the pilot contract is a proposal that is normative only
upon Human Maintainer commit following Nova approval. Entry criteria are unmet;
no pilot has started.

Documents:
[Consumer Requirements Model](../docs/governance/CONSUMER_REQUIREMENTS_MODEL.md) ·
[Traceability](../docs/governance/CONSUMER_REQUIREMENTS_TRACEABILITY.md) ·
[Pilot Scope and Scenarios](../docs/governance/COREOPS_PILOT_SCOPE_AND_SCENARIOS.md) ·
[Pilot Contract](../docs/governance/COREOPS_PILOT_CONTRACT.md) ·
[Validation Plan](../docs/governance/CONSUMER_VALIDATION_PLAN.md) ·
[Consumer Evidence Register](../docs/research/CONSUMER_EVIDENCE_REGISTER.md) ·
[Consumer Hypothesis Validation](../docs/research/CONSUMER_HYPOTHESIS_VALIDATION.md)

Completion is reported for Human Maintainer review. No Git write action was
performed, and no consumer repository was modified.

## Next work package: CDS-WP-005 — Design System Architecture

### Objective

Define the CDS architecture that can carry the registered scope and the
registered consumer requirements.

### Scope direction

- normative system layers,
- source-of-truth model,
- token flow **as architecture, without selecting a format**,
- artifact classes and the separation of normative sources from generated
  output,
- product profiles and their governed limits,
- distribution,
- consumer contracts,
- evidence flows.

### Input to carry forward

**From CDS-WP-004 (requirements — normative for classification):**

- 40 requirements CR-001 … CR-040; 25 Shared CDS Candidates; 28 pilot-relevant.
- The strongest multi-consumer signal is **status semantics** — all three
  consumers document graded status, and two independently require that *unknown
  must never read as healthy* (CR-006, CR-007).
- Consumers already hold **product-local design decisions and token sets**
  (CR-002, CR-037). CDS arrives after them; this is reconciliation, not a blank
  slate.
- Offline and self-hosted operation is a confirmed, accepted consumer
  requirement (CR-031, CR-032) — DEC-S-006 must be an explicit architectural
  criterion.
- The interface must not rely on privileged internal shortcuts unavailable to
  API consumers (CR-040) — an architectural constraint.
- Requirements are **Level 1 evidence** (documentation only). No user research
  took place (RISK-017).

**From CDS-WP-003 (research — non-normative):**

- Tool coupling in token workflows is common and rarely documented as a risk.
  DEC-S-004 must shape the source-of-truth model.
- The reviewed token interoperability draft is explicitly a preview that
  instructs readers not to implement it — **no token format may be selected on
  its basis**.
- Every reviewed system permits product variation; none published its limits.

### Open questions this work package must address

1. Where does the normative source actually live, if not in a design tool?
2. How much may a product profile vary before the system fragments — given
   consumers already shipped their own design decisions?
3. Which states are CDS-owned versus domain semantics, and how are combined
   states resolved (CR-015)?
4. How is "unknown" represented honestly and consistently (CR-007)?
5. Does CoreOps' operational shape generalize, or is CDS becoming an operations
   design system (RISK-016)?
6. What artifact distribution satisfies the offline constraint (CR-031)?

### Explicitly prohibited in CDS-WP-005

- final visual design of any kind,
- selecting colours, typography, icons, logos, or themes,
- selecting a design tool, component framework, or **token format**,
- implementing components or product code,
- licensing, publication, or support commitments,
- claiming adoption or conformance,
- promoting a hypothesis to a decision without evidence,
- treating CoreOps requirements as automatically normative (DEC-S-016),
- modifying Skill files or consumer repositories,
- extending the roadmap.

### Authorization note

CDS-WP-005 requires an explicit work-package prompt from Nova. Being listed as
**Next** identifies sequence, not authorization.

## Related documents

- [Work Packages](WORK_PACKAGES.md)
- [Project Profile](PROJECT_PROFILE.md)
- [Foundation Context Pack](CONTEXT_PACK_FOUNDATION.md)
- [Project Charter](../docs/governance/PROJECT_CHARTER.md)
