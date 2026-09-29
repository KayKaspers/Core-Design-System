---
name: ndf-release-notes-runner
description: Create or review NDF release notes for any version — pre-release vs final label, compatibility statement and migration notes where relevant, visible known notes and accepted limitations, changelog consistency, and release-body checks (flags, known notes, compatibility claims, neutrality). USE WHEN drafting or checking release notes in authorised release prep or post-release reconciliation. Docs-only, fail-closed; never asserts publication or performs tag/release actions.
---

# ndf-release-notes-runner

## Title

NDF Release Notes Runner (docs-only, ADR-0032-compliant).

## Purpose

Create or review release notes in the NDF style for any version — labelling pre-release vs final correctly and stating compatibility honestly — without asserting publication or triggering a release.

## When to use

- **USE WHEN** drafting or reviewing release notes during authorised release prep or post-release reconciliation.
- **DO NOT USE** for readiness decisions → `ndf-release-safety`; for CHANGELOG entries → `ndf-changelog-writer`.
- `ndf-public-release-body-reviewer` stays available for a dedicated release-body review.

## Required inputs

- Target version and release type (pre-release / final).
- The WP results, known notes and accepted limitations, the changelog, and compatibility-relevant changes — from authoritative records.

## Expected outputs

- Release notes with the correct release-type label (pre-release vs final).
- A compatibility statement where relevant (ADR-0031; the v1.x promise is active since `v1.0.0`): non-breaking changes, deprecations with a named successor, breaking changes only on the major-version path.
- Migration notes wherever covered behavior changes.
- Known notes and accepted limitations kept visible.
- Changelog-consistent phrasing.
- Release-body review points: flags (pre-release / latest) match the release type; known notes visible; compatibility claims accurate; public neutrality.

## Allowed actions

- Draft/structure release notes; keep known notes and limitations visible; check changelog consistency and compatibility claims.

## Forbidden actions

- Claim a release is published, tagged, or live without authoritative evidence; perform tag/release actions; set release flags.
- Activate, extend, or withdraw a compatibility promise; overstate compatibility.
- Drop known notes or accepted limitations.
- Run scripts; access the network; read/document secrets.

## Fail-closed behavior

If publication status is uncertain, phrase as "prepared / pending Human-Maintainer release" rather than "published"; mark unproven compatibility or migration claims as notes instead of asserting them; anything not explicitly allowed is forbidden.

## Public-neutrality requirements

No private names, real domains, secret values, private search patterns, reviewer identities, org-internal names, or personal data. The secret name `NDF_PUBLIC_NEUTRALITY_DENYLIST` may be named; its value never. Role phrasing — DE: "Nova (ChatGPT) – die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle."; EN: "Nova (ChatGPT) – the ChatGPT-based planning, architecture and review role."

## ADR-0032 safety boundaries

Docs-only, fail-closed; no scripts; no network; no secrets; no private data; no autonomous git/release/tag actions.

## Human-maintainer-only boundaries

Publishing the release and setting its flags stay with the Human Maintainer.

## Output contract

A release-notes draft/review — never a publication or a tag/release.

## Interaction with existing NDF skills

Pairs with `ndf-release-safety` (readiness, command guidance) and, when the CHANGELOG is in scope, `ndf-changelog-writer`; `ndf-public-release-body-reviewer` remains the dedicated release-body reviewer; frame via `ndf-work-package-runner`; neutrality via `ndf-public-neutrality-guard`.

## Release/governance limitations

Never claims a release occurred unless authoritative evidence (e.g. a Human-Maintainer-confirmed tag and release) says so; a pre-release is labelled as a pre-release, never as final; release notes describe the v1.x compatibility promise (active since `v1.0.0`, ADR-0031) and never activate or change it.
