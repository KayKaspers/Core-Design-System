---
name: ndf-changelog-writer
description: Write consistent, honest, WP-referenced NDF CHANGELOG entries. USE WHEN CHANGELOG.md is in the authorised file scope of a work package or release section. DO NOT USE when CHANGELOG is not in the authorised file scope. Docs-only, fail-closed; never infers or declares release/tag/version status, never activates a compatibility promise, never triggers git/release actions.
---

# ndf-changelog-writer

## Title

NDF Changelog Writer (docs-only, ADR-0032-compliant).

## Purpose

Support consistent changelog entries for NDF work packages and release sections — honest, neutral, WP-referenced, in the NDF style (Keep-a-Changelog-like) — as a suggestion that never asserts or triggers a release.

## When to use

- **USE WHEN** `CHANGELOG.md` is in the authorised file scope: a WP entry under `[Unreleased]`, or consolidating entries into a release section during authorised release prep.
- **DO NOT USE** when the CHANGELOG is not in the authorised file scope — record changes only where the prompt allows (e.g. WP notes or the return format).
- **USE INSTEAD** `ndf-release-notes-runner` for release notes and `ndf-compact-context-summary-runner` for the WP report.

## Required inputs

- The WP result, affected artifacts, and WP-ID.
- The existing changelog format and known notes.
- Release and compatibility status from authoritative repository records only (released CHANGELOG sections, release notes, Human-Maintainer-confirmed tags).

## Expected outputs

- A neutral, consistent entry suggestion: under `[Unreleased]` unless an authoritative release record says otherwise; WP reference; honest status; preserved known notes; the compatibility class where relevant (clarification / behavioral non-breaking / additive / breaking, per ADR-0031).
- Status wording consistent with the records: `v1.0.0` is final and the ADR-0031 v1.x compatibility promise is active since `v1.0.0` — an entry neither denies nor re-activates it.

## Allowed actions

- Check the changelog format and structure the entry within the existing conventions.
- Summarize WP results accurately and preserve known notes.

## Forbidden actions

- Infer or declare a release/tag/version status, or move entries out of `[Unreleased]` without an authoritative release record.
- Activate, extend, or withdraw a compatibility promise, or misstate its status.
- Trigger commit/tag/release or any git write action.
- Redesign the changelog conventions.
- Insert private content, secret values, or reviewer identities.
- Document chain-of-thought.

## Fail-closed behavior

No invented release/version status; if status or compatibility class is uncertain, phrase neutrally, mark the uncertainty, and defer to the Human Maintainer. CHANGELOG outside the authorised scope → no entry. Anything not explicitly allowed is forbidden.

## Public-neutrality requirements

No private project names, real private domains, secret values, private search patterns, real reviewer identities, org-internal names, or personal data. The secret name `NDF_PUBLIC_NEUTRALITY_DENYLIST` may be named; its value never. Allowed role phrasing — DE: "Nova (ChatGPT) – die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle."; EN: "Nova (ChatGPT) – the ChatGPT-based planning, architecture and review role."

## ADR-0032 safety boundaries

Docs-only, fail-closed; no scripts; no network; no secrets; no private data; no autonomous git/release/tag actions; Public Quality Gate and Public Neutrality mandatory.

## Human-maintainer-only boundaries

Version, tag, and release stay with the Human Maintainer, who performs commit/push/tag/release.

## Output contract

A single changelog entry suggestion — never a commit, tag, or release.

## Interaction with existing NDF skills

Selected by `ndf-work-package-runner` only when the CHANGELOG is in scope; the entry aligns with the WP result (`ndf-compact-context-summary-runner`); pairs with `ndf-release-notes-runner` and `ndf-release-safety` in release prep; neutrality via `ndf-public-neutrality-guard`.
