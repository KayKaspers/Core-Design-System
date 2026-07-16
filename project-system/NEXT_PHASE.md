# Next Phase

- **Phase:** Foundation / Pre-Design
- **Completed work packages:** CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005, CDS-WP-006, CDS-WP-007
- **Next work package:** CDS-WP-008 — Foundation Milestone Review

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

### CDS-WP-007 — Accessibility and Inclusive Design Policy — Completed

Defined the normative CDS accessibility and inclusive-design policy:

- **Target** — **WCAG 2.2 Level AA** for the applicable web-based scope
  (DEC-S-049), resolving **CR-024** at policy level (DEC-S-060). No AAA
  commitment. **A target is not a conformance claim** (DEC-S-050).
- **Applicability matrix** — all Level A and AA success criteria: **56 listed**
  (32 A · 24 AA), **55 applicable** (31 A · 24 AA), excluding the obsolete 4.1.1.
  No pass/fail statement.
- **Responsibility** — shared by contract; **49 of 55 applicable criteria require
  both CDS and the consumer** (DEC-S-051, DEC-S-052).
- **Evidence** — five levels AE-0 … AE-4 (Evidence and Claims Model); automated-
  only is never sufficient (DEC-S-053). Every artifact is **AE-0**; no support
  baseline exists.
- **Channels** — six profiles; only two have a target; **none is Candidate- or
  Stable-eligible** (DEC-S-058).
- **Limits** — accessibility cannot be waived by an ordinary exception
  (DEC-S-059); no legal or certification statement (policy boundary, standard-
  status doc); native semantics first and APG examples are informative only
  (DEC-S-054).
- **Pilot** — CR-024 resolved at policy level; entry criterion satisfiable on
  Human Maintainer commit; **the pilot has not started and cannot start.**

Reconciled CR-021, CR-022, CR-024, and CR-034 traceability. Added
DEC-S-049 … DEC-S-060 and RISK-041 … RISK-048.

**No artifact was promoted, no claim, tag, or release created, and every artifact
remains AE-0.** Publication state remains `Private Development`. No Git write
action was performed.

Documents:
[Accessibility and Inclusive Design Policy](../docs/governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md) ·
[WCAG 2.2 AA Applicability Matrix](../docs/governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md) ·
[Evidence and Claims Model](../docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) ·
[Channel Profiles](../docs/governance/ACCESSIBILITY_CHANNEL_PROFILES.md) ·
[CoreOps Pilot Accessibility Criterion](../docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md)

## Next work package: CDS-WP-008 — Foundation Milestone Review

### Why this is now the next step

The Foundation phase is materially complete: concept and scope, benchmark
research, consumer requirements, logical architecture, governance, and the
accessibility policy are all defined. **No policy work package remains** — the
two `Deferred to CDS-WP-006/007` states in the traceability are retired.

What is missing is not more policy. It is a **review** that decides whether the
foundation is coherent and affordable enough to authorize concrete design and
implementation.

### Objective

Review the completed Foundation phase and recommend whether — and how — to enter
the design and implementation phase. **CDS-WP-008 starts no implementation.**

### Review goals

- **Foundation completeness** — every registered concern has a home.
- **Decision and risk consistency** — DEC-S-001 … DEC-S-060 and
  RISK-001 … RISK-048 internally coherent; no contradictions.
- **Architecture and governance coherence** — the eight layers, artifact classes,
  and governance tracks hold together.
- **Accessibility-policy completeness** — target, matrix, evidence model, channel
  profiles, and pilot criterion form a usable whole; the AE-0 reality is visible.
- **Consumer-requirement coverage** — CR-001 … CR-040 mapped and reconciled.
- **Unresolved blockers** — no support baseline (RISK-044), no licence
  (DEC-S-047), no artifact at Candidate.
- **Governance affordability** — whether the evidence and ceremony burden is
  sustainable at actual maintainer capacity (RISK-040, RISK-048).
- **Candidate-readiness assessment** — what the first artifact to attempt
  Candidate would need.
- **CoreOps pilot entry readiness** — which entry criteria remain structurally
  unmet.
- **Next-phase roadmap recommendation** — what CDS-WP-009 onward should be.

### Input to carry forward

- **Nothing is tested.** Every artifact is AE-0; no accessibility, no
  implementation, and no user evidence exists (RISK-017, RISK-041).
- **No release is possible** — licence review is unsatisfiable (DEC-S-047) and no
  artifact can reach Stable.
- The **evidence-burden-versus-capacity** question (RISK-048) is the most likely
  thing to break the foundation, and it is unresolved.
- Publication state remains `Private Development`; no claim of any kind is valid.

### Explicitly prohibited in CDS-WP-008

- concrete visual design of any kind,
- selecting colours, typography, icons, logos, or themes,
- selecting a design tool, component framework, or token format,
- implementing components or product code,
- selecting a licence or approving publication,
- claiming conformance, accessibility, or certification,
- promoting any artifact to Candidate or Stable,
- starting the CoreOps pilot,
- modifying Skill files or consumer repositories,
- extending the roadmap without Human Maintainer approval.

### Authorization note

CDS-WP-008 requires an explicit work-package prompt from Nova. Being listed as
**Next** identifies sequence, not authorization.

## Related documents

- [Work Packages](WORK_PACKAGES.md)
- [Project Profile](PROJECT_PROFILE.md)
- [Foundation Context Pack](CONTEXT_PACK_FOUNDATION.md)
- [Governance Operating Model](../docs/governance/GOVERNANCE_OPERATING_MODEL.md)
