---
name: ndf-release-safety
description: Version-neutral NDF release governance — readiness, prep and post-release checks for pre-release or final releases and major/minor/patch bumps, v1.x compatibility under ADR-0031 (active since v1.0.0), and Human-Maintainer tag/release command guidance per the Execution Contract. USE WHEN a WP does release readiness, release prep, or post-release review for any version. DO NOT USE for WPs without release impact. Docs-only, fail-closed; never performs tag/release actions.
---

# ndf-release-safety

## Title

NDF Release Safety — version-neutral release governance (docs-only, ADR-0032-compliant).

## Purpose

Check release-adjacent work against safety boundaries and structure readiness, release-prep, and post-release documentation for any NDF version — without triggering any release. Since `v1.0.0` it is also the readiness entry point that `ndf-v1-readiness-review` points to.

## When to use

- **USE WHEN** a WP does release readiness, release prep, or post-release review — pre-release or final; major, minor, or patch.
- **DO NOT USE** for WPs without release impact.
- **USE ALONGSIDE / INSTEAD** `ndf-release-notes-runner` for the release-notes text; `ndf-changelog-writer` for CHANGELOG sections (only when in scope); `ndf-v1-readiness-review` only for historical v1.0 evidence.

## Required inputs

- The current release scope and its readiness criteria — taken from the current release-scope documents, not hard-coded.
- Target version, release type (pre-release / final), and version bump (major / minor / patch).
- The authoritative current status, compatibility-relevant changes, and known notes.

## Expected outputs

- **Release type:** pre-release vs final kept distinct; "latest" is a Human-Maintainer decision.
- **Version bump check:** major / minor / patch consistent with the actual changes.
- **Compatibility check** (ADR-0031; the v1.x promise is active since `v1.0.0`): minor and patch releases must not silently break covered v1.x behavior; deprecations name a successor where applicable; migration notes wherever covered behavior changes; breaking changes only via the major-version path and Human-Maintainer governance.
- **Readiness assessment** against the current release scope's criteria (met / met with notes / gap / blocker) with a go / no-go recommendation and notes.
- **Human-Maintainer command guidance** for tag / release steps (below) and documentary rollback / correction notes.

## Human-Maintainer command guidance

Any tag / release command sequence drafted with this skill is guidance for the Human Maintainer and follows the [Execution Contract](../../../framework/prompts/blocks/BLOCK_EXECUTION_CONTRACT.md) (Rules 2 and 3): execution header where applicable; target shell; working directory; preconditions / required baseline (branch, revision, clean tree, gate result); the complete ordered command sequence for the authorised gate; expected result; verification; STOP conditions. A correction is reissued as a complete block marked `COMPLETE REPLACEMENT` — never as a delta. The skill itself performs no git write.

## Allowed actions

- Structure release checklists, readiness reviews, and post-release reconciliation.
- Draft Human-Maintainer command guidance as above.
- Repeat "only the Human Maintainer tags/releases".

## Forbidden actions

- Create/push/move/delete a tag; create or edit a GitHub release; set release flags; assert publication without authoritative evidence.
- Declare readiness, release type, or "latest" on the Human Maintainer's behalf.
- Activate, extend, narrow, or withdraw the v1.x compatibility promise; relax ADR-0031.
- Reuse an earlier release's criteria as current readiness criteria.
- Run scripts; access the network; read/document secrets.

## Fail-closed behavior

If readiness, release type, version bump, or a compatibility claim is unclear, recommend NO-GO/notes rather than GO; anything not explicitly allowed is forbidden.

## Public-neutrality requirements

No private names, real domains, secret values, private search patterns, reviewer identities, org-internal names, or personal data. The secret name `NDF_PUBLIC_NEUTRALITY_DENYLIST` may be named; its value never. Role phrasing — DE: "Nova (ChatGPT) – die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle."; EN: "Nova (ChatGPT) – the ChatGPT-based planning, architecture and review role."

## ADR-0032 safety boundaries

Docs-only, fail-closed; no scripts; no network; no secrets; no private data; no autonomous git/release/tag actions.

## Human-maintainer-only boundaries

Tag, release, publication, and release-flag decisions stay with the Human Maintainer.

## Output contract

Checklists, assessments, and documented Human-Maintainer command guidance only — never an executed tag/release.

## Interaction with existing NDF skills

Selected by `ndf-work-package-runner` for release/readiness WPs; pairs with `ndf-release-notes-runner` and, when the CHANGELOG is in scope, `ndf-changelog-writer`; `ndf-public-release-body-reviewer` for a release body; historical v1.0 context via `ndf-v1-readiness-review`; results via `ndf-compact-context-summary-runner`.

## Release/governance limitations

Never sets a release "latest"; the v1.x compatibility promise is active since `v1.0.0` (ADR-0031, not retroactive) — this skill checks releases against it and never activates, re-activates, or changes it; breaking changes to covered behavior need the major-version path; rollback/correction is documented only and decided by the Human Maintainer.
