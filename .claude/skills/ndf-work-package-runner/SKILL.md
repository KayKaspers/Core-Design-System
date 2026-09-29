---
name: ndf-work-package-runner
description: Primary docs-only execution router for NDF work packages. USE WHEN starting or executing an NDF WP prompt — reads the execution header (SESSION, STATUS, SUPERSEDES), applies the Execution Contract, keeps the declared profile/budget, scope, STOP conditions and Human-Maintainer gate visible, and selects 0–3 relevant support skills instead of the whole pack. DO NOT USE for closing or handover content alone (use ndf-compact-context-summary-runner). Fail-closed; no git/release actions; no runtime.
---

# ndf-work-package-runner

## Title

NDF Work Package Runner — primary docs-only execution router (ADR-0032-compliant).

## Purpose

Route the start and execution of an NDF work package so the WP prompt carries only WP-specific content, while the stable frame (role, hard limits, gates, closing content) is referenced instead of repeated. The runner reads the execution contract, keeps the declared profile and budget, keeps scope and gates visible, and selects only the support skills the WP needs. It is a documentation-only routing aid: no runtime, no state, no decisions.

## When to use

- **USE WHEN** starting or executing an NDF work package in any prompt mode (Full / Standard / Short) or WP-152 profile (Lean / Handoff / Review-only / Fix).
- **DO NOT USE** for the closing or handover content alone → `ndf-compact-context-summary-runner`; for Context Pack upkeep alone → `ndf-context-pack-maintainer`.
- Short Prompt Mode only within its allowances: a current Context Pack exists and the case is not Short-forbidden (security policy, ADR, scope lock, release readiness, release prep, destructive / git-write / tag actions, unclear requirements).

## Required inputs

- The active authorised WP prompt, including its execution header.
- Public repository content only (ADR-0032). A clause for private consumer projects is reserved for a separate ADR decision and is **not** active in this skill.

## Execution start

Apply in order. The rules are referenced, not copied: [Execution Contract](../../../framework/prompts/blocks/BLOCK_EXECUTION_CONTRACT.md) (NDF-WP-153) and [Token Efficiency & Context Budget Baseline](../../../docs/guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md) (NDF-WP-152).

1. **Execution header.** Read `SESSION` (`SAME_SESSION_ALLOWED` / `SAME_SESSION_RECOMMENDED` / `NEW_SESSION_RECOMMENDED` / `NEW_SESSION_REQUIRED`), `SESSION REASON`, `STATUS` (`COMPLETE` / `COMPLETE REPLACEMENT`) and `SUPERSEDES`. Session continuity is never implicit. A newly authored prompt without a declaration is a prompt defect → REWORK and a `COMPLETE REPLACEMENT`; a legacy prompt runs as `NEW_SESSION_RECOMMENDED`, reported as `SESSION_DECLARATION_MISSING_LEGACY`.
2. **Completeness.** Execute only one complete, self-contained contract. A `COMPLETE REPLACEMENT` supersedes the named instruction entirely; never merge instruction versions. Delta-only or incomplete instructions (e.g. "reuse the previous block, change step 4") and conflicting instruction states → STOP / `BLOCKED` and request a `COMPLETE REPLACEMENT`. Only a pure Human-Maintainer selection among fully defined options needs none (Rule 3).
3. **Profile and budget.** Recognise the declared mode, profile, and budget (B0–B4). Never lower a declared profile or budget. Escalate only when a fail-closed trigger applies (guide §16), by the step the trigger requires (normally one level, guide §7) and within the prompt's declared maximum; beyond it → STOP and report — continuing needs a `COMPLETE REPLACEMENT`. Full and B3 only where the actual risk requires them (release, scope lock, ADR, security policy, v1.x compatibility, destructive actions, complex review); B4 only with explicit justification, never as a default. Handoff does not implement; Review-only starts no implementation; Fix does not widen scope.
4. **Preflight.** Run or verify the prompt's read-only preflight (branch, revision, working tree, index, no in-progress git operation; source-handoff preflight where relevant). A material deviation → `BLOCKED`, no change ([lifecycle §10–§12](../../../framework/standards/WORK_PACKAGE_LIFECYCLE.md)).
5. **Visible frame.** Keep visible throughout: WP-ID, goal, allowed / forbidden files and operations, STOP conditions, acceptance criteria, Human-Maintainer gate. A needed path or operation outside the authorised scope → STOP; scope expansion is a Human-Maintainer decision.
6. **Support skills.** Select as below — never the whole pack.

## Support-skill selection

Prefer 0–3 support skills, chosen by the WP's actual content and within the per-budget totals of guide §14. The core candidates (`ndf-compact-context-summary-runner`, `ndf-public-neutrality-guard`, `ndf-context-pack-maintainer`) are selected per task, not forced blindly.

| WP content | Support skill |
|---|---|
| `CHANGELOG.md` in the authorised file scope | `ndf-changelog-writer` |
| release, readiness, release notes | `ndf-release-safety`, `ndf-release-notes-runner` |
| ADR question | `ndf-adr-governance-review` |
| skill modification | `ndf-skill-quality-reviewer`, `ndf-skill-trigger-quality-reviewer` |
| evidence-strength review | `ndf-validation-evidence-reviewer` |
| feedback | `ndf-feedback-triage-runner` |
| privacy / personal data | `ndf-privacy-data-minimization-reviewer` |
| code review / tests / debugging | `ndf-implementation-review-runner` / `ndf-test-strategy-runner` / `ndf-debugging-root-cause-reviewer` |
| product / UX / creative | the matching advisory skill — only when explicitly relevant |

Any other skill only when the prompt names it. A selected skill never replaces a gate, a review, or the Public Quality Gate.

## Expected outputs

- An internal execution scaffold — header status, completeness, declared mode / profile / budget, preflight result, visible frame, and the selected support skills with a one-line reason each — surfaced only as far as the prompt's return format allows.
- The WP-specific steps and the affected-file identification.
- The closing content via `ndf-compact-context-summary-runner`, in the prompt's format.

## Allowed actions

- Structure WP steps and identify relevant public files within the authorised scope.
- Reference the NDF role model, hard limits, and gates instead of copying them.
- Recommend a prompt mode, profile, budget, or escalation (the prompt and the Human Maintainer decide).
- Recommend documentary status / roadmap / context-pack updates in the repository style, within scope.
- Reference the read-only self-check and preflight commands (`git status`, `git diff --stat`, `git diff`, `git diff --cached --name-only`) as self-check instructions.

## Forbidden actions

- Replace concrete WP goals, invent file paths, widen scope, or activate optional WPs.
- Write normative authority, approve scope changes, or stand in for a Nova verdict or a Human-Maintainer decision.
- Stage, commit, push, fetch, tag, release, or perform any other git write action.
- Act as runtime: no runtime or persistent state, no central state store, no daemon, no MCP server, no network service, no tool orchestration.
- Override project-local governance.
- Bypass the Public Quality Gate, human review, or any release / readiness gate.
- Run scripts, access the network, read or document secrets, embed private data, or document chain-of-thought.

## Output precedence

The active authorised prompt's return format wins over this skill's generic output (Execution Contract, Rule 4). The skill only ensures that the mandatory minimum NDF content — honest result, changed files, validation, Human-Maintainer gate, Report-to-Nova and Compact-Context-Summary content or their prompt-defined equivalents — is present, fitted into the prompt's structure and never added as an extra parallel block. A real normative conflict is reported and fails closed.

## Fail-closed behavior

Missing, ambiguous, or conflicting context is made visible, never guessed: escalate within the declared maximum, report STOP / `BLOCKED`, or trigger the Human-Maintainer gate — whichever the fail-closed rules require. Unclear context alone is no reason to demand Full. No execution on a delta-only or incomplete instruction. Anything not explicitly allowed is forbidden.

## Public-neutrality requirements

No private project names, real private domains, secret values, private search patterns, real reviewer identities, org-internal names, or personal data. The secret name `NDF_PUBLIC_NEUTRALITY_DENYLIST` may be named; its value never. Allowed role phrasing — DE: "Nova (ChatGPT) – die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle."; EN: "Nova (ChatGPT) – the ChatGPT-based planning, architecture and review role."

## ADR-0032 safety boundaries

Docs-only, fail-closed; no scripts; no network; no secrets; no private data; no autonomous git/release/tag actions; Public Quality Gate and Public Neutrality mandatory.

## Human-maintainer-only boundaries

Nova (ChatGPT) issues review verdicts (GO / GO WITH NOTES / REWORK / STOP / BLOCKED) — evaluations, not acceptance. The Human Maintainer alone accepts governed changes and scope changes, accepts ADRs, and performs staging, commit, push, tag, and release. This skill produces suggestions only; it makes no irreversible decision.

## Output contract

A routing scaffold and suggestions — never an executed git/release action, never a decision. The final return follows the active prompt's format (see Output precedence) and always contains the mandatory closing content.

## Compact Context Summary / Report-to-Nova requirements

Every WP handled with this skill closes with the mandatory closing content — Report-to-Nova and Compact-Context-Summary content, or the prompt's named equivalents (e.g. a `SESSION_HANDOFF` section) — via `ndf-compact-context-summary-runner`. It is never dropped for compression; its shape follows the active prompt.
