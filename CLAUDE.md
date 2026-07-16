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
- Phase: Foundation / Pre-Design
- First reference consumer: CoreOps (not the sole design target)
- Completed work packages: CDS-WP-001, CDS-WP-001A, CDS-WP-002, CDS-WP-003,
  CDS-WP-004, CDS-WP-005, CDS-WP-006
- Next work package: CDS-WP-007 — Accessibility and Inclusive Design Policy

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
- [docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md](docs/architecture/DESIGN_SYSTEM_ARCHITECTURE.md)
  — normative source for the logical architecture; entry point to the
  architecture documents
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
