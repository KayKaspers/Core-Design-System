# Next Phase

- **Phase:** Foundation / Pre-Design
- **Completed work packages:** CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005
- **Next work package:** CDS-WP-006 — Governance, Versioning, and Contribution
  Model

## Status of completed work packages

### CDS-WP-001 — Project Governance and NDF Bootstrap — Completed

Charter, role and authority model, DEC-S-001 … DEC-S-006, RISK-001 … RISK-005,
controlled roadmap, local Claude operating instructions.

### CDS-WP-001A — NDF Skills Bootstrap — Completed

38 verified docs-only NDF v1.0.0 Skills, 39 files, pinned byte-identical to
commit `9dcadc12fb960914b9a5baeff2ab1aee75912b57`; Skills-first mode active.

### CDS-WP-002 — Concept and Scope Registration — Completed

Six capability domains, ten cross-cutting concerns, current versus long-term
scope, twelve non-goals, three consumer classes, ownership boundaries, CoreOps
pilot boundary. DEC-S-007 … DEC-S-012, RISK-006 … RISK-009.

### CDS-WP-003 — Benchmark and Differentiation Research — Completed

Ten design systems reviewed against 14 dimensions from official sources;
HYP-001 … HYP-008 assessed. RISK-010 … RISK-013. **Non-normative.**

### CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract — Completed

Three consumers analyzed read-only at committed revisions; CR-001 … CR-040
registered and traced; bounded CoreOps pilot (Groups A–E, 9 scenarios) and its
contract; HYP consumer layer. DEC-S-013 … DEC-S-020, RISK-014 … RISK-019.

### CDS-WP-005 — Design System Architecture — Completed

Defined the CDS logical architecture:

- **eight architecture layers** (DEC-S-021),
- **source-of-truth and authority model** with eight artifact classes and an
  authority matrix (DEC-S-022, DEC-S-023),
- **five-level conceptual token flow** (DEC-S-024),
- **product profile and extension model** with the existing-product
  reconciliation flow (DEC-S-025, DEC-S-026),
- **operations patterns as a domain family**, not the universal foundation
  (DEC-S-027),
- **status semantics with five separated axes** and the Unknown invariant
  (DEC-S-028),
- **channel and distribution model** with offline and provenance requirements
  (DEC-S-029, DEC-S-030, DEC-S-031),
- **five consumer contracts**,
- **CR-001 … CR-040 mapped** to the architecture.

Added DEC-S-021 … DEC-S-032 and RISK-020 … RISK-028.

**The architecture selects no technology and no design** (DEC-S-032). It is
structure awaiting policy and implementation evidence.

Documents:
[Architecture](../docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md) ·
[Authority](../docs/architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md) ·
[Tokens](../docs/architecture/TOKEN_AND_THEME_ARCHITECTURE.md) ·
[Profiles](../docs/architecture/PRODUCT_PROFILE_AND_EXTENSION_MODEL.md) ·
[Channels](../docs/architecture/ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md) ·
[Contracts](../docs/architecture/CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md) ·
[Evidence & Status](../docs/architecture/EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md) ·
[Requirement Coverage](../docs/architecture/ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md)

Completion is reported for Human Maintainer review. No Git write action was
performed.

## Next work package: CDS-WP-006 — Governance, Versioning, and Contribution Model

### Objective

Supply the policy the architecture deliberately deferred. The architecture
defines structure; CDS-WP-006 defines the rules that operate it.

### Scope direction

- **Governance roles** — who decides what, and the escalation path.
- **Risk ownership** — the risk owner model is currently **provisional** across
  all 28 risks and must be settled here.
- **Maturity states** — what makes a foundation Candidate or Stable.
- **Versioning** — the scheme that gives "revision" a concrete meaning.
- **Compatibility** — what makes pinning safe.
- **Deprecation** — distinct states for unmaintained-but-present versus removed.
- **Contribution** — proposal, review, and acceptance process.
- **Exception governance** — recording, review, and expiry of Local Exceptions.
- **Product Profile governance** — which extension points are approved, who
  approves, and how a profile is revoked.
- **Conformance and adoption claims** — the criteria and evidence model behind
  DEC-S-012 and DEC-S-017.
- **Licensing and publication decision model** — still with no assigned work
  package until now.

### Input to carry forward

**Architecture dependencies explicitly deferred to CDS-WP-006:**

- the detailed conflict-resolution authority behind DEC-S-023,
- the change-control process that turns an escalation into a decision,
- how a deviation is formally recorded, reviewed, and expired,
- which token extension points are approved (DEC-S-025),
- profile and exception limits (RISK-021, RISK-027),
- the versioning scheme underpinning DEC-S-031 and CR-034,
- the evidence model behind the Adoption Evidence Contract.

**From the benchmark (non-normative):** published per-component maturity states
and published conformance evidence were the two most effective practices found —
but they come from publishers with dedicated teams (RISK-011). Governance rigour
must be sized to actual capacity (RISK-026).

**From consumers:** consumers are already **more mature at version-bound evidence
than CDS is** — CDS has no version, no maturity model, and no evidence model
(HYP-006). Licensing is never one decision: documentation, code, fonts, icons,
and brand assets routinely sit on different terms.

### Explicitly prohibited in CDS-WP-006

- final visual design of any kind,
- selecting colours, typography, icons, logos, or themes,
- selecting a design tool, component framework, or token format,
- selecting a build system, package manager, or repository topology,
- implementing components or product code,
- claiming adoption or conformance,
- starting the CoreOps pilot,
- modifying Skill files or consumer repositories,
- extending the roadmap.

### Authorization note

CDS-WP-006 requires an explicit work-package prompt from Nova. Being listed as
**Next** identifies sequence, not authorization.

## Open question for Nova

**CR-024 — the accessibility target — remains undefined**, and it now blocks
more than a policy gap: it blocks a CoreOps pilot entry criterion and prevents
Pilot Group E from being evidenced. Accessibility is weak in **both** the
benchmark and the consumer evidence layers.

RISK-028 records the resulting architecture debt. Nova may wish to consider
advancing CDS-WP-007, or deciding the target earlier than the roadmap implies.
**Claude does not reorder the roadmap.**

## Related documents

- [Work Packages](WORK_PACKAGES.md)
- [Project Profile](PROJECT_PROFILE.md)
- [Foundation Context Pack](CONTEXT_PACK_FOUNDATION.md)
- [Design System Architecture](../docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md)
