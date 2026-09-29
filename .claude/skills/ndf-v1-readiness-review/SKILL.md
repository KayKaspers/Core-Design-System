---
name: ndf-v1-readiness-review
description: Historical / specialist skill for the completed v1.0.0 readiness path (RC vs final, G-13, final criteria). USE WHEN reviewing or citing historical v1.0 readiness evidence. DO NOT USE for readiness, release prep, or post-release work after v1.0.0 — use ndf-release-safety instead. Docs-only, fail-closed; never invents claims, re-opens v1.0, or performs release actions.
---

# ndf-v1-readiness-review

## Title

NDF v1.0 Readiness Review — historical / specialist (docs-only, ADR-0032-compliant).

## Status

**Historical / specialist.** The v1.0 readiness path this skill supported is complete: `v1.0.0` is the final release, and the ADR-0031 v1.x compatibility promise is active since `v1.0.0`. The skill stays available under its name for compatibility and is **not** deprecated; any formal deprecation would follow the ADR-0031 deprecation process in a later, separately authorised decision. **For readiness work after `v1.0.0`, use `ndf-release-safety`.**

## Purpose

Support honest reviews of the historical v1.0 readiness evidence (RC vs final, G-13, final criteria) without re-opening or re-deciding the completed v1.0 release.

## When to use

- **USE WHEN** reviewing, citing, or reconciling historical v1.0 RC/final readiness evidence.
- **DO NOT USE** for readiness, release-prep, or post-release work after `v1.0.0` → **use `ndf-release-safety` instead** (release notes → `ndf-release-notes-runner`).

## Required inputs

- The historical v1.0 release criteria (RC vs final), the gap/evidence reviews, and the recorded v1.0 outcome.

## Expected outputs

- An honest historical assessment: RC-vs-final distinction; G-13 and final-criteria status as recorded (met / met with notes / gap / accepted boundary); pointers to the authoritative v1.0 records.
- A redirect to `ndf-release-safety` for any current readiness question.

## Allowed actions

- Read the historical criteria, status, and records; structure the historical check honestly.

## Forbidden actions

- Invent or re-decide v1.0 claims; re-open the completed v1.0 release.
- Present `v1.0.0` as not yet released or the v1.x promise as awaiting activation.
- Use its RC/final process as the general readiness process for later versions.
- Perform any release/tag action; run scripts; access the network; read/document secrets.

## Fail-closed behavior

If a historical outcome is unclear, cite the authoritative record or mark it unverified — never claim it; route any current readiness question to `ndf-release-safety`. Anything not explicitly allowed is forbidden.

## Public-neutrality requirements

No private names, real domains, secret values, private search patterns, reviewer identities, org-internal names, or personal data. The secret name `NDF_PUBLIC_NEUTRALITY_DENYLIST` may be named; its value never. Role phrasing — DE: "Nova (ChatGPT) – die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle."; EN: "Nova (ChatGPT) – the ChatGPT-based planning, architecture and review role."

## ADR-0032 safety boundaries

Docs-only, fail-closed; no scripts; no network; no secrets; no private data; no autonomous git/release/tag actions.

## Human-maintainer-only boundaries

Release decisions stay with the Human Maintainer; this skill decides nothing.

## Output contract

An advisory historical assessment — never a release, an activation, or a current readiness verdict.

## Interaction with existing NDF skills

Post-v1.0 readiness successor: `ndf-release-safety`; frame via `ndf-work-package-runner`; evidence depth via `ndf-validation-evidence-reviewer`; results via `ndf-compact-context-summary-runner`.

## Release/governance limitations

Historical record: the v1.x compatibility promise is active since `v1.0.0` (ADR-0031; not retroactive for Foundation `v0.x` releases or the RC `v1.0.0-rc.1`); the RC was a candidate, not final; G-13 was reconciled for final via path C (path B accepted boundary, path A a future improvement). This skill neither re-activates nor changes any of it.
