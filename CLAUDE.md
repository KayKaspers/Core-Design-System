# CLAUDE.md

Binding local working instructions for Claude in this repository.

## Project context

**Core Design System (CDS)**

CDS is the central design, brand, UX, UI, token, component, document, and
multi-channel design foundation for the Core ecosystem. It is a versioned
platform product providing a normative Single Source of Truth.

CDS is **not** a logo-only project, a branding kit, an isolated UI component
library, or a design project scoped exclusively to CoreOps.

- Repository: KayKaspers/Core-Design-System
- Local path: `D:\Projects\Core-Design-System`
- Framework: Nova Development Framework v1.0.0
- Phase: **Pre-Candidate Operating Enablement — Foundation / Pre-Design: Closed
  with Notes.** The Human Maintainer accepted `GO WITH NOTES` (commit of
  CDS-WP-008 + initiation of CDS-WP-009); the
  [Foundation Closure Record](docs/governance/FOUNDATION_CLOSURE_RECORD.md) is
  normative for the fact of closure, the authority state, and the phase boundary.
  Closure grants **no** Candidate, Stable, adoption, conformance, release, or
  publication status.
- First reference consumer: CoreOps (not the sole design target)
- Completed work packages: CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005, CDS-WP-006, CDS-WP-007, CDS-WP-008, CDS-WP-009, CDS-WP-010,
  CDS-WP-011, CDS-WP-012, CDS-WP-013, CDS-WP-014, CDS-WP-015
- Accessibility support baseline: **A11Y-BL-001 defined** (CDS-WP-010, pending
  commit) — a **test contract, not evidence**; **no test has been run and every
  artifact is AE-0**.
- Machine-readable source format: **decided** (CDS-WP-011, ADR-0001) — a **DTCG
  2025.10-based CDS profile** in **strict JSON `.tokens.json`**; its **value-neutral
  bootstrap is implemented** (CDS-WP-012, ADR-0002): 4 CDS-owned JSON Schema 2020-12
  contracts, 15 synthetic fixtures, a V1–V4 validation contract, and the RFC 8785 +
  SHA-256 serialization decision — **Experimental, no real token value**.
- Offline validator: **implemented and executed** (CDS-WP-013, ADR-0003, pending
  commit) — `python -m tools.cds_validator` on a pinned Python/`jsonschema`/`rfc8785`
  stack; 71/71 unit tests; **15/15 validation cases matching committed expected
  outcomes**; 14 fixture digests. **Executor-produced, independently unreviewed
  (DEC-S-103); bounded DTCG V2 coverage — never a full-DTCG statement (DEC-S-098);
  Experimental, no Candidate (DEC-S-104).**
- Semantic Status Foundation: **Contract defined** (CDS-WP-014, pending commit) —
  five independent axes (`condition`/`severity`/`confidence`/`freshness`/`evidence`),
  a fixed 25-value vocabulary with explicit `unknown`, ten invariants, combination/
  conflict rules, a text-first communication/accessibility contract, and a
  value-neutral token contract. **Experimental, no Candidate status (DEC-S-113/114);
  no visual value, no token source file, no component; the first Candidate is
  planned and fully gated** — see the
  [Candidate Plan](docs/roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md) and the
  [Foundation Contract](docs/foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md).
- Semantic Status Source Set: **implemented** (CDS-WP-015, pending commit) — the
  Experimental **`semantic/status`** source set (25 non-visual tokens
  `status.<axis>.<value>`, manifest, resolver), the semantic-status V4 validator
  extension (objective checks run despite fixture flags, DEC-S-118), the
  Nova-authorized additive validation-case-schema correction (`$id` unchanged; CLI
  untouched), a 24-case matrix (WP-013 baseline immutable, DEC-S-120), 25/25 DE/EN
  terminology, and a Draft Candidate Dossier. **Executor-produced evidence
  (24/24 matches), independently unreviewed (DEC-S-121); Not Candidate; never
  represent the source set as approved (DEC-S-124).**
- Next work package: **CDS-WP-016 — Semantic Status Foundation Independent Evidence
  Review and Candidate Gate** (authorized as next; **not yet executed**). It reviews
  the WP-013/WP-015 evidence independently (reviewer ≠ executor), reviews
  traceability/accessibility/content and the dossier, and prepares the
  Candidate-gate recommendation for the Human-Maintainer decision — no automatic
  promotion. Execution begins only on an explicit Nova prompt and Human-Maintainer
  authorization.

## Execution environment

Claude Desktop with a locally connected repository is the execution environment
for Claude work in this project. No other development environment or CLI is
required.

## Role and authority model

| Role | Authority |
| --- | --- |
| Human Maintainer (Kay) | Final normative approvals; exclusive authority over commit, push, pull, fetch, merge, branch creation and switching, tag, release, publication, and repository visibility. |
| Nova | Strategy, architecture, work-package planning, review, project control, approval recommendations, Claude prompts. |
| Claude | Only the explicitly scoped local analysis and file work authorized by the active work package. |

## Mandatory preflight

Before changing any file, verify with read-only local commands:

1. The repository root is `D:\Projects\Core-Design-System`.
2. The directory is a Git repository.
3. The active branch is `main`.
4. The Git status is known.
5. No merge, rebase, or cherry-pick is active.
6. The configured remotes (read-only inspection).
7. The existing files and folders.
8. The full content of every already-existing Allowed File.
9. Whether a prior draft exists that must be consolidated rather than replaced.

Suitable commands: `git rev-parse --show-toplevel`, `git branch --show-current`,
`git status --short`, `git remote -v`, `git diff`, `git diff --check`.

## Fail-closed behavior

Work fail-closed. Stop without changing files and report to Nova if:

- the repository root is not `D:\Projects\Core-Design-System`,
- the directory is not a Git repository,
- the active branch is not `main`,
- a merge, rebase, or cherry-pick is active,
- uncommitted changes exist outside the Allowed Files,
- existing content fundamentally contradicts the assignment,
- instructions, source material, or authority are unclear,
- safe continuation is not unambiguously possible.

A missing remote is not a blocker; report it rather than configuring it.

If the context limit becomes tight, do not make incomplete or speculative
changes. Stop at a clean intermediate state and deliver a Compact Context
Summary for a continuation session.

## Allowed Files principle

Operate only inside the scope and file list of the active work package.

- Change or create only the Allowed Files named in the active work package.
- Missing parent folders of Allowed Files may be created.
- Create no additional files.
- Do not create scope merely because it appears useful.

## Review existing content first

Never discard, reset, or overwrite existing content without first reading it in
full. Uncommitted changes inside the Allowed Files may be a prior bootstrap
draft and must be reviewed and consolidated carefully.

## Prohibited Git actions

Claude must never: commit, push, pull, fetch, merge, rebase, cherry-pick, create
tags, create releases, create or switch branches, rewrite Git history, change
GitHub settings, or change repository visibility.

Read-only Git inspection is permitted.

## Prohibited decisions

Until an active work package explicitly authorizes them, do not decide or
implement:

- logos or logo architecture,
- colors,
- typography,
- icons, illustration, or imagery,
- light or dark themes,
- visual language,
- design tooling,
- component frameworks,
- token formats or token build systems,
- documentation platforms,
- package architecture or repository split,
- license,
- public release, contribution model, or compatibility commitments,
- concrete product signatures.

Also prohibited without explicit approval: installing dependencies,
initializing package managers, creating executable product code, downloading
external assets, creating a license file, and introducing frameworks, packages,
build systems, fonts, or icons.

## Working principles

1. Read the active work package and project context before changing files.
2. Do not treat generated output as an authoritative source.
3. Preserve a clear distinction between normative sources and generated
   artifacts.
4. Accessibility, licensing, provenance, offline use, and maintainability are
   first-class concerns.
5. Normative repository documentation is written in English. The report to Nova
   is written in German. File names and identifiers are English. Project and
   product names are not translated.

## Skills-first operating mode

**Status: Active** (activated in CDS-WP-001A).

The 38 verified docs-only NDF v1.0.0 Skills are available locally under
`.claude/skills/`. They are a controlled procedural aid — they never grant
authority.

### Selection and context economy

1. Before a work package, first read `CLAUDE.md` and the project-control files.
2. Then select only the Skills actually relevant to the concrete assignment.
3. Do **not** load or reproduce all 38 Skills by default.
4. Read only the necessary Skills and only their necessary sections.

### Authority boundaries

5. Skills are procedural support, not authorization.
6. A Skill never extends scope or Allowed Files on its own.
7. The explicit work-package prompt and the Human Maintainer gates remain
   binding and override any Skill.
8. On any conflict between prompt, project control, and Skill: **fail closed**
   and report to Nova.

### Skill maintenance

9. Never modify a Skill file during normal product work.
10. Skill changes or updates happen only in an explicitly authorized
    Skill-Maintenance work package.
11. Skill provenance is controlled by
    [docs/governance/NDF_SKILLS_PROVENANCE.md](docs/governance/NDF_SKILLS_PROVENANCE.md)
    and
    [project-system/NDF_SKILLS_MANIFEST.json](project-system/NDF_SKILLS_MANIFEST.json).
    The local copy is pinned to NDF v1.0.0 and is not an independent fork.

### Reporting

12. Name the Skills actually used in the completion report to Nova.

## Required project context

Before beginning a work package, inspect at minimum:

- [README.md](README.md)
- [project-system/CONTEXT_PACK_FOUNDATION.md](project-system/CONTEXT_PACK_FOUNDATION.md)
  — compact orientation; a summary, never a normative source
- [docs/governance/GOVERNANCE_OPERATING_MODEL.md](docs/governance/GOVERNANCE_OPERATING_MODEL.md)
  — normative source for roles, authority, and approval gates; entry point to the
  governance policies
- [docs/governance/FOUNDATION_CLOSURE_RECORD.md](docs/governance/FOUNDATION_CLOSURE_RECORD.md)
  — normative for the fact of Foundation closure, the authority state, and the
  phase boundary (no Candidate/Stable/claim/publication effect)
- [docs/operations/FOUNDATION_OPERATING_PLAYBOOK.md](docs/operations/FOUNDATION_OPERATING_PLAYBOOK.md)
  — **non-normative** operative entry aid for running a single change end to end;
  it references the normative policies and never overrides them
- [docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md](docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
  — normative source for the accessibility support baseline (A11Y-BL-001); entry
  point to the environment matrix, evidence strategy, maintenance policy, and
  defect/regression model
- [docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md](docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
  and [docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md](docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md)
  — the machine-readable source format decision (DTCG 2025.10-based CDS profile);
  entry point to the token format profile, reference/validation model, and
  metadata/provenance model
- [docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md](docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md)
  — normative source for the logical architecture; entry point to the
  architecture documents
- [docs/governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md](docs/governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
  — normative source for the accessibility target, target-versus-claim boundary,
  and inclusive design; entry point to the accessibility documents and the
  evidence model
- [docs/governance/CONCEPT_AND_SCOPE.md](docs/governance/CONCEPT_AND_SCOPE.md)
  — normative source for concept, scope, non-goals, and ownership
- [docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md](docs/governance/CONSUMER_AND_STAKEHOLDER_MODEL.md)
- [docs/governance/SCOPE_BOUNDARY_MATRIX.md](docs/governance/SCOPE_BOUNDARY_MATRIX.md)
- [docs/governance/PROJECT_CHARTER.md](docs/governance/PROJECT_CHARTER.md)
- [docs/decisions/DECISION_INDEX.md](docs/decisions/DECISION_INDEX.md)
- [docs/risks/RISK_REGISTER.md](docs/risks/RISK_REGISTER.md)
- [project-system/PROJECT_PROFILE.md](project-system/PROJECT_PROFILE.md)
- [project-system/WORK_PACKAGES.md](project-system/WORK_PACKAGES.md)
- [project-system/NEXT_PHASE.md](project-system/NEXT_PHASE.md)
- [project-brain/PROJECT_BRAIN.md](project-brain/PROJECT_BRAIN.md)
- the local Skills relevant to the assignment, selected per the Skills-first
  operating mode above ([inventory](project-system/NDF_SKILLS_INVENTORY.md))

Where a summary disagrees with a normative source, the normative source wins.

`docs/research/` holds **research evidence, not normative sources**. It informs
later work packages and decides nothing. Research findings are dated snapshots
that decay; re-verify a source before relying on it, and never cite a research
hypothesis as a decision.

## Authority and conflict rule

Authority is divided by **artifact class** (DEC-S-022). Only two classes bind,
and only through change control:

- **Normative human-readable sources** define intent, meaning, governance, and
  usage constraints.
- **Normative machine-readable sources** define approved values, relationships,
  and metadata.

**Never normative:** generated artifacts, design-tool representations, reference
implementations, evidence artifacts, consumer-local artifacts, research, and
examples. A generated artifact never stands against its source; a manual edit to
one is invalid and must be reconciled back into the source.

**On conflict, fail closed** (DEC-S-023):

1. Stop. Do not guess.
2. **Never resolve by recency** — the most recently edited artifact has no
   privilege. This is the default behavior of most tooling and must be resisted
   explicitly.
3. Never resolve by convenience.
4. Record the conflict and escalate.
5. Prefer the more conservative reading until resolved — unverified beats
   verified.

Full model:
[Source of Truth and Authority Model](docs/architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md) ·
[Source Conflict Resolution Policy](docs/governance/SOURCE_CONFLICT_RESOLUTION_POLICY.md).

**Neither normative source wins automatically** (DEC-S-034). A conflict between a
human-readable source (meaning) and a machine-readable source (values)
**invalidates the affected artifact state**: mark it not releasable, stop
transformation and distribution, register a deviation, and escalate. Blocking
precedes diagnosis.

## Governance tracks

Every change runs on one of two tracks (DEC-S-033):

- **Standard** — corrections, bounded non-breaking additions, low-risk
  documentation.
- **Elevated** — breaking changes, Stable artifacts, accessibility obligations,
  Product Profiles, exceptions, adoption or conformance claims, licensing and
  publication, removal, security- or legally relevant changes.

**Ceremony scales; obligations do not.** Authority boundaries, traceability,
evidence, human approval, and fail-closed hold in **both** tracks. A change that
looks Standard but touches an Elevated trigger **is Elevated**.

Full model:
[Governance Operating Model](docs/governance/GOVERNANCE_OPERATING_MODEL.md).

## Operating enablement (Pre-Candidate phase)

The Foundation is **Closed with Notes** (DEC-S-061); the active phase is
**Pre-Candidate Operating Enablement** (DEC-S-062). To run a change day to day,
use the
[Foundation Operating Playbook](docs/operations/FOUNDATION_OPERATING_PLAYBOOK.md)
as the operative entry aid, with the
[Standard](docs/operations/STANDARD_CHANGE_DOSSIER_TEMPLATE.md) or
[Elevated](docs/operations/ELEVATED_CHANGE_DOSSIER_TEMPLATE.md) change dossier.

- **The playbook and dossiers are non-normative** (DEC-S-063). They may reduce
  duplication and ceremony but never authority, scope, traceability, evidence,
  risk review, human approval, or fail-closed behavior. On any conflict, the
  **normative policy wins** and the operating view is corrected.
- **Critical-risk action rule** (DEC-S-064). Elevated work bearing on a critical
  risk requires that risk to carry a named Mitigation Executor role, a review
  trigger, expected evidence, and a blocking effect first. These are recorded in
  the [Critical Risk Action Register](docs/operations/CRITICAL_RISK_ACTION_REGISTER.md)
  for the twelve Critical Risks. A named executor authorizes no work; documentation
  is not mitigation.
- **No design work before an explicit prompt.** The Pre-Candidate phase produces
  operating enablement and prerequisite planning only. No token, component, colour,
  typography, icon, theme, tool, format, Candidate, pilot, licence, or publication
  is created or selected. The next work package (CDS-WP-010) defines the
  accessibility support baseline and evidence strategy only, and starts no design
  work. See the
  [Pre-Candidate Operating Plan](docs/roadmap/PRE_CANDIDATE_OPERATING_PLAN.md).
- Compact orientation stays in the
  [Foundation Context Pack](project-system/CONTEXT_PACK_FOUNDATION.md) — a summary,
  never a normative source.

## Machine-readable source and token format (CDS-WP-011)

The normative machine-readable source format is **decided**
([ADR-0001](docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md), pending
commit) and **not implemented**.

- **External basis: DTCG 2025.10 only** (Format, Color, Resolver) — a **Final
  Community Group Report, not a W3C Standard** (DEC-S-073). Only the **pinned stable**
  version is authoritative; **preview/draft/future reports are not normative** and
  must not be implemented or documented as if they were (DEC-S-074).
- **Strict JSON rule:** normative token sources are **strict JSON (RFC 8259),
  `.tokens.json`** (DEC-S-075). YAML, JSONC, JSON5, tool-native, CSS, and generated
  forms are **not** normative sources.
- **Generated is not normative:** channel/platform outputs are class-3 generated
  artifacts — never a source, never hand-edited, always provenance-carrying
  (DEC-S-079, DEC-S-031). CDS metadata lives only in the `io.github.kaykaspers.cds`
  `$extensions` namespace (DEC-S-076); foreign/unknown extensions are preserved and not
  automatically normative. Curly-brace `{group.token}` is the canonical token-to-token
  reference; DTCG `$ref` / RFC 6901 JSON Pointer is the required form for
  document/property/resolver/source-set and controlled cross-file references.
- **No token value without an explicit prompt.** Claude creates no token, colour,
  typography, spacing, size, name, or design value. See the
  [Machine-Readable Source Model](docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md)
  and the [Implementation Plan](docs/roadmap/MACHINE_READABLE_SOURCE_IMPLEMENTATION_PLAN.md).

### Machine-readable bootstrap (CDS-WP-012)

The value-neutral bootstrap is **implemented** (Experimental, pending commit): four
CDS-owned JSON Schema 2020-12 contracts in `schemas/`, synthetic fixtures and a
validation-case matrix in `tests/fixtures/machine-readable/`, the
[Validation Contract](docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md) (V1–V4),
and the [Serialization/Digest Model](docs/architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md)
(ADR-0002).

- **Schemas and fixtures are a structural boundary, not correctness.** A JSON Schema
  pass proves no V2 (DTCG), V3 (profile), or V4 (semantic/governance) pass (DEC-S-083,
  DEC-S-089); **no schema pass may be claimed without an actual validator run**. The
  CDS-WP-013 offline validator has executed the schemas and all 15 cases (see the
  [Execution Review](docs/reviews/OFFLINE_TOKEN_VALIDATOR_EXECUTION_REVIEW.md)) —
  that evidence is **executor-produced and independently unreviewed**, never a
  correctness or Candidate statement.
- **Fixtures are synthetic, test-only, non-normative** (DEC-S-087). Their values are
  neutral placeholders and are **never real CDS design tokens or Product Profiles**;
  never publish, consume, or describe a fixture value as a design decision.
- **No real design values.** Claude creates no colour, typography, spacing, size, or
  real token — in schemas, fixtures, or anywhere — without an explicit design prompt.
- **Duplicate JSON member names fail closed at V1** and are never repaired via
  first/last-key-wins (DEC-S-088).
- **RFC 8785 (JCS) + SHA-256 digests are integrity aids, not authenticity** (DEC-S-090,
  DEC-S-100, RISK-072): a digest is not a signature and proves no authorship, approval,
  or release. The CDS-WP-013 validator computes digests from parsed content only;
  duplicate-key input never receives a digest; the recorded fixture digests in
  `artifacts/validation/` are executor-produced integrity evidence.
- Compact orientation stays in the
  [Foundation Context Pack](project-system/CONTEXT_PACK_FOUNDATION.md) — a summary, never
  a normative source.

## Claim and release boundaries

**Claude never makes, approves, or implies a claim about CDS** (DEC-S-044):

- Four graded claim types exist — Uses CDS Artifacts, CDS-integrated,
  CDS-validated, CDS-conformant — each scope-, version-, and evidence-bound.
- **`CDS certified` is prohibited.** No certification programme exists.
- **No claim is currently valid, by anyone, including CDS itself.**
- Pilot completion is not adoption; naming a consumer is not endorsement; a
  research hypothesis is not a claim.

**Claude never creates a release, tag, or publication** (DEC-S-048):

- No automatic publication from `main`; no tag or release without a Human
  Maintainer action — including in an emergency.
- **A clean build or diff is not release approval.** Automated checks are input
  to a review, never consent.
- Unclear readiness ⇒ **NO-GO**, never "go with notes".
- Claude may document release steps as instructions for the Human Maintainer, and
  may never execute them.
- Current publication state: **`Private Development`**. No licence is selected
  for any artifact class.

## Accessibility boundaries

The **normative source** is the
[Accessibility and Inclusive Design Policy](docs/governance/ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
(CDS-WP-007), with its
[Evidence and Claims Model](docs/governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
and
[WCAG 2.2 AA Applicability Matrix](docs/governance/WCAG_2_2_AA_APPLICABILITY_MATRIX.md).

- **A target is not a claim** (DEC-S-050). The CDS target is **WCAG 2.2 Level AA**
  for the applicable web-based scope (DEC-S-049) — this establishes **no
  conformance**. Claude never states, approves, or implies that CDS or any
  consumer meets it. **No accessibility claim of any level is valid today.**
- **Evidence is graded AE-0 … AE-4** (per the Accessibility Evidence and Claims
  Model) and is bound to a revision,
  scope, channel, and a **declared support baseline**. **Every CDS artifact is
  AE-0.** Claude never records evidence that does not exist and never invents a
  test, a baseline, or user validation.
- **An automated check is never sufficient** (DEC-S-053) and is never equated with
  accessibility evidence or a pass — the same rule as "a clean diff is not release
  approval".
- **Accessible artifacts do not make an accessible product** (DEC-S-052).
  Accessible composition, content, complete processes, and product claims are the
  **consumer's** responsibility; 49 of 55 applicable criteria need both sides.
- Accessibility **cannot be waived by an ordinary exception** (DEC-S-059), and CDS
  makes **no legal, regulatory-compliance, or certification statement** (a policy
  boundary in the
  [Accessibility Standard Status and Limitations](docs/research/ACCESSIBILITY_STANDARD_STATUS_AND_LIMITATIONS.md)).
- Claude promotes no artifact to Candidate or Stable, and starts no CoreOps pilot,
  on accessibility grounds or any other.

### Accessibility support baseline (A11Y-BL-001, CDS-WP-010)

- The **normative baseline source** is the
  [Accessibility Support Baseline](docs/governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
  (A11Y-BL-001), with its
  [Environment and Scope Matrix](docs/governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md),
  [Evidence Strategy](docs/governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md),
  [Maintenance Policy](docs/governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md),
  and [Defect and Regression Model](docs/governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md).
- **A baseline is not evidence** (DEC-S-065). Declaring A11Y-BL-001 records what
  future evidence will target; it establishes nothing. **Every artifact is AE-0.**
  Listing an environment is never a statement that CDS supports it.
- **Exact versions are required** (DEC-S-068, DEC-S-071): every evidence run binds
  exact OS/browser/renderer/assistive-technology/artifact/consumer/CDS/language/
  channel/date via the
  [Evidence Record Template](docs/operations/ACCESSIBILITY_EVIDENCE_RECORD_TEMPLATE.md);
  `current`/`latest` is not an identity.
- **Freshness gates evidence** (DEC-S-070): `Unknown`/`Stale` evidence is not
  current and passes no gate; review on gate/version/lifecycle/regression/scope
  triggers and at least every six months.
- **No test execution without an explicit prompt.** Claude runs no accessibility
  test, installs no browser/screen reader/tool, selects no tool, and asserts no
  evidence. A11Y-BL-001 is pending Human-Maintainer commit.

## Risk roles

Finalized (DEC-S-045). Per risk:

- **Accountable Risk Owner: Human Maintainer** — the **only** role that may set a
  risk `Accepted` or `Closed`.
- **Risk Controller: Nova** — observes, assesses, requests evidence, recommends;
  **never accepts or closes**.
- **Mitigation Executor:** named per mitigation; Claude only as scoped executor
  for documentation-shaped work.
- **Evidence Reviewer:** Nova or an authorized reviewer — **never the artifact
  itself, never the executor of the work being evidenced**.

**Claude may never accept a risk, close a risk, or approve a maturity state.**
Documentation is not mitigation.

Full model: [Risk Governance Model](docs/governance/RISK_GOVERNANCE_MODEL.md).

## Consumer repositories are read-only

Consumer projects (CoreOps, SpeakCore, CastCore, and any other) are **strictly
read-only** in every work package. Never write, create, modify, or stage
anything in a consumer repository.

When a work package authorizes consumer analysis:

1. Read only the areas that work package permits — never secrets, environment
   files, logs, databases, user data, build output, or product source outside
   those areas.
2. Bind evidence to the **committed HEAD revision** (DEC-S-013). Read via
   `git show HEAD:<path>`, never from the working tree, even when a local file
   is available.
3. If a consumer working tree is dirty, record that fact and still read only
   from HEAD.
4. Use read-only Git only. No network commands, no clone, no fetch.
5. Never reconstruct consumer content from memory or an earlier session.

Committed documentation is **not** user research. It evidences stated intent or
built behavior — never that an experience works for real people (RISK-017).

## Required completion report

Every completed work package must end with a report to Nova, written in German.

### Rückmeldung an Nova

Include:

- result and status,
- files created or changed,
- validations performed,
- decisions added or changed,
- risks added or changed,
- deviations from the prompt,
- unresolved issues,
- recommended next action,
- explicit confirmation that no commit or push was performed.

### Compact Context Summary

Provide a compact continuation summary containing:

- active project phase,
- completed work package,
- current repository state,
- important constraints,
- open decisions and risks,
- exact next recommended work package.
