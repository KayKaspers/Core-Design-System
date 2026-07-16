# Next Phase

- **Phase:** Foundation / Pre-Design
- **Completed work packages:** CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005, CDS-WP-006
- **Next work package:** CDS-WP-007 — Accessibility and Inclusive Design Policy

## Status of completed work packages

### CDS-WP-001 — Project Governance and NDF Bootstrap — Completed

Charter, role and authority model, DEC-S-001 … DEC-S-006, RISK-001 … RISK-005,
controlled roadmap.

### CDS-WP-001A — NDF Skills Bootstrap — Completed

38 verified docs-only NDF v1.0.0 Skills pinned to commit
`9dcadc12fb960914b9a5baeff2ab1aee75912b57`; Skills-first mode active.

### CDS-WP-002 — Concept and Scope Registration — Completed

Six capability domains, ten cross-cutting concerns, twelve non-goals, three
consumer classes, ownership boundaries. DEC-S-007 … DEC-S-012,
RISK-006 … RISK-009.

### CDS-WP-003 — Benchmark and Differentiation Research — Completed

Ten design systems reviewed from official sources; HYP-001 … HYP-008 assessed.
RISK-010 … RISK-013. **Non-normative.**

### CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract — Completed

Three consumers analyzed at committed revisions; CR-001 … CR-040 registered and
traced; bounded CoreOps pilot and contract. DEC-S-013 … DEC-S-020,
RISK-014 … RISK-019.

### CDS-WP-005 — Design System Architecture — Completed

Eight-layer logical architecture, authority model, token flow, profiles and
reconciliation, channels and distribution, consumer contracts, status semantics.
DEC-S-021 … DEC-S-032, RISK-020 … RISK-028. **No technology or design selected.**

### CDS-WP-006 — Governance, Versioning, Contribution, Risk and Publication Model — Completed

Operationalized the architecture into governance:

- **Governance operating model** — six roles, Standard and Elevated tracks, an
  authority matrix, and the rule that ceremony scales but obligation does not
  (DEC-S-033).
- **Source conflict resolution** — neither normative source wins automatically; a
  conflict invalidates the affected state (DEC-S-034).
- **Seven-state maturity lifecycle** — Proposed → Exploratory → Experimental →
  Candidate → Stable → Deprecated → Removed, on an axis separate from release
  version and publication state (DEC-S-035, DEC-S-036).
- **Versioning and compatibility** — MAJOR.MINOR.PATCH, an honest pre-1.0
  policy, immutable release identity, and compatibility declared across eight
  axes (DEC-S-037 … DEC-S-039).
- **Deprecation and removal** — deprecation before removal, bounded emergency
  removal (DEC-S-040).
- **Contribution and acceptance** — a ten-step flow with five outcomes
  (DEC-S-041).
- **Exceptions and Product Profiles** — bounded, expiring, and never
  retrospective legitimation (DEC-S-042, DEC-S-043).
- **Adoption claims** — four graded types; `CDS certified` prohibited
  (DEC-S-044).
- **Risk ownership finalized** — Human Maintainer accountable, Nova controller
  (DEC-S-045).
- **Publication and licensing** — five states with a gate; licensing decided per
  ten artifact classes (DEC-S-046, DEC-S-047).
- **Release control** — no automated approval or publication (DEC-S-048).

Added DEC-S-033 … DEC-S-048 and RISK-029 … RISK-040.

**No licence was selected, no publication approved, no technology or design
chosen, and no accessibility level set.** The current publication state remains
`Private Development`.

Documents:
[Governance Operating Model](../docs/governance/GOVERNANCE_OPERATING_MODEL.md) ·
[Source Conflict Resolution](../docs/governance/SOURCE_CONFLICT_RESOLUTION_POLICY.md) ·
[Artifact Maturity Lifecycle](../docs/governance/ARTIFACT_MATURITY_LIFECYCLE.md) ·
[Versioning, Compatibility and Deprecation](../docs/governance/VERSIONING_COMPATIBILITY_AND_DEPRECATION_POLICY.md) ·
[Contribution and Acceptance](../docs/governance/CONTRIBUTION_AND_ACCEPTANCE_MODEL.md) ·
[Exception and Product Profile Governance](../docs/governance/EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md) ·
[Adoption, Conformance and Claims](../docs/governance/ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md) ·
[Risk Governance Model](../docs/governance/RISK_GOVERNANCE_MODEL.md) ·
[Licensing and Publication](../docs/governance/LICENSING_AND_PUBLICATION_DECISION_MODEL.md) ·
[Release and Change Control](../docs/governance/RELEASE_AND_CHANGE_CONTROL_POLICY.md)

Completion is reported for Human Maintainer review. No Git write action was
performed.

## Next work package: CDS-WP-007 — Accessibility and Inclusive Design Policy

### Why this is now the critical path

CDS-WP-006 made the accessibility gap **load-bearing**. The undefined
accessibility target (CR-024) now blocks four separate gates:

| Blocked | Because |
| --- | --- |
| **Stable gate** | Requires accessibility evidence — so **no artifact can reach Stable** |
| **Product Profile approval** | Requires accessibility evidence — so **no profile can be approved** |
| **Publication gate** | Requires an accessibility statement — so **no publication-state change is possible** |
| **CoreOps pilot entry** | An entry criterion; Pilot Group E cannot be evidenced |

Consequently **no CDS release is currently possible**, and a conformance claim
is unreachable by construction. This is recorded as RISK-028 and was not worked
around.

### Objective

Define the binding accessibility and inclusive-design policy and its verification
approach.

### Scope direction

- **Accessibility target level** — the decision CR-024 has been waiting for.
- **Inclusive design principles.**
- **Role and responsibility boundaries** — what CDS guarantees versus what the
  consumer must still do. The benchmark's clearest lesson: the strongest systems
  state plainly that using them does not make a consumer's product accessible.
- **Component and pattern requirements.**
- **Keyboard and focus** (CR-021).
- **Motion** (CR-022).
- **Contrast and non-colour semantics** (CR-006) — already an architectural
  invariant; the policy sets the threshold.
- **Localization and language** (CR-023).
- **Evidence model** — what substantiates the target, and who reviews it.
- **Consumer responsibilities.**
- **CoreOps pilot entry criterion CR-024.**

### Input to carry forward

- Accessibility is currently **weak in both evidence layers**: the benchmark found
  it named everywhere but evidenced rarely, and consumer evidence is thin —
  CoreOps names a baseline with no level, CastCore documentation contains none at
  all, and only SpeakCore documents concrete practice (contrast, visible focus,
  no colour-only coding).
- The architecture already holds the constraints that are safe regardless of
  level: colour never the sole meaning carrier, component contracts carry
  accessibility behavior, profiles may not weaken guarantees (invariant 10).
- **A normal exception may never weaken accessibility** (DEC-S-042) — a
  prohibition currently protecting a requirement whose value is unknown.
- The claim discipline applies: a stated target plus published evidence plus an
  explicit consumer obligation — **never** "CDS is accessible" (DEC-S-044).
- WCAG 2.2 itself states that even AAA conformance will not serve every
  disability. Whatever target is chosen, it is a target — not a guarantee of
  accessibility.
- The target must be **evidenceable at actual maintainer capacity** (RISK-029,
  RISK-040). A level CDS cannot substantiate is worse than a lower one it can.

### Explicitly prohibited in CDS-WP-007

- concrete visual design of any kind,
- selecting colours, typography, icons, logos, or themes,
- selecting a design tool, component framework, or token format,
- implementing components or product code,
- selecting a licence or approving publication,
- claiming conformance or certification,
- starting the CoreOps pilot,
- declaring any existing artifact accessible,
- modifying Skill files or consumer repositories,
- extending the roadmap.

### Authorization note

CDS-WP-007 requires an explicit work-package prompt from Nova. Being listed as
**Next** identifies sequence, not authorization.

## Related documents

- [Work Packages](WORK_PACKAGES.md)
- [Project Profile](PROJECT_PROFILE.md)
- [Foundation Context Pack](CONTEXT_PACK_FOUNDATION.md)
- [Governance Operating Model](../docs/governance/GOVERNANCE_OPERATING_MODEL.md)
