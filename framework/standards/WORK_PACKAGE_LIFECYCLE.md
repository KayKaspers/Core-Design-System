# NDF Standard – Work Package Lifecycle

> Sprachstatus / Language status: EN mit deutscher Einleitung. / English with German introduction.

DE: Dieser Standard beschreibt den Lebenszyklus jedes Work Package — von der Aufnahme über Klassifizierung, Prompt, Umsetzung durch den Implementation Agent und Rückmeldung an Nova (ChatGPT-Review-Rolle, siehe [NOVA_CHATGPT_ROLE.md](../../docs/workflow/NOVA_CHATGPT_ROLE.md)) bis zu Review, Maintainer-Commit, CI-Prüfung und Follow-up.

## Lifecycle

```text
Intake -> Classification -> Blueprint/Prompt -> Execution -> Rückmeldung -> Nova Review -> Maintainer Commit -> CI/Validation -> Follow-up
```

## 1. Intake

Capture the need: bug, feature, risk, security finding, documentation gap, release need or CI failure.

## 2. Classification

Assign one primary Work Package type.

Examples:

- Security review -> `security-baseline`
- Security fix -> `security-code-fix`
- Health score change -> `health-score-update`
- Delete feature planning -> `destructive-blueprint`
- Delete feature implementation -> `destructive-implementation`

## 3. Blueprint / Prompt

Nova writes the Claude prompt with type, scope, allowed files, forbidden files, tests and Rückmeldung.

Execution prompts carry the execution header (`SESSION`, `SESSION REASON`, `STATUS`) and form one complete, self-contained active contract per the [Execution Contract](../prompts/blocks/BLOCK_EXECUTION_CONTRACT.md) — complete, not verbose.

## 4. Execution

Claude executes only within the scope and does not commit or push.

## 5. Rückmeldung

Claude reports summary, changed files, tests, risks and recommendation.

## 6. Nova Review

Nova decides: GO, GO WITH NOTES, REWORK, SPLIT or STOP. This is the review verdict: it does not itself accept governed changes, change scope, accept ADRs, or trigger any Git/release action — normative acceptance and all irreversible actions stay with the Human Maintainer (section 7; `NOVA_REVIEW != HUMAN_ACCEPTANCE`). After REWORK, the corrected prompt is a `COMPLETE REPLACEMENT` (see section 13).

## 7. Maintainer Commit

The human maintainer controls staging, commit, push and release.

## 8. CI / Validation

After push, CI is checked and failures are classified.

## 9. Follow-up

If project posture changes, update Health Score, Project Brain, risks or create next WP.

## 10. Source-Handoff Preflight (before Execution)

Work packages that rely on chat-provided documents, uploaded files, local external files, documents from another repository, exported reports, handed-over specifications or source packs must run a source-handoff preflight **before any change**:

```text
Source available in execution environment
Source identity verified
Expected document or artifact confirmed
Completeness checked
Truncation or partial-content risk checked
Version/date/revision recorded when relevant
Provenance recorded when relevant
Scope-relevant sections readable
```

A present source is **not** an automatic trust grant: deeper provenance, hash, public-neutrality, security or license/usage checks belong to the work package designated for them.

## 11. Fail-closed Transition to `blocked`

If a required source is missing, not uniquely identifiable, only partially available, visibly truncated, mismatched against the expected version, or not fully readable, the work package transitions fail-closed to `blocked`:

1. change no repository file;
2. invent no content; treat no indirect memory as a replacement source;
3. report status `blocked`;
4. name the exact missing source and the unblock condition.

The same fail-closed transition applies to any unmet preflight prerequisite (e.g., an unclean working tree).

## 12. Blocked Report (structured, no-change)

A fail-closed stop **before any change** is itself a complete, review-ready result. The blocked report must contain at least:

```text
Work Package ID
Status: blocked
Blocker
Preflight results
Reason for fail-closed stop
Files changed: none
Git write performed: no
Tests run
Tests not run and why
Exact unblock condition
Recommended next step
Compact Context Summary
```

### No-Change Rule

A blocked work package with no repository changes does **not** require an artificial intermediate commit. The implementation agent must not create an empty/unnecessary file, perform a status-only mutation without authorization, demand an artificial intermediate commit, or report the blocker as `completed`.

### Human-Maintainer Gate

The human maintainer may make a separate documentation/correction commit only when actually authorized repository changes exist. The commit itself is not an automatic status mutation: the intended status must already be correct in the repository documents before staging and commit.

## 13. Resume / New Work Package after Unblock

Once the unblock condition is met, the work package is resumed (or a new work package is started) from the documented resume point. A resume does not widen the original scope or allowed files.

When the executable contract changes — resolution of `blocked`, REWORK, a scope or authority correction, a review-driven correction, or changed commands — the next instruction is a `COMPLETE REPLACEMENT` with `SUPERSEDES`, never a delta. The only exception is a pure Human-Maintainer selection among options already fully defined in the active instruction, and only while scope, authority, files, operations, commands, acceptance criteria and STOP conditions stay unchanged ([Execution Contract](../prompts/blocks/BLOCK_EXECUTION_CONTRACT.md), Rule 3).
