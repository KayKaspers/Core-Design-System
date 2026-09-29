# Prompt Block – Execution Contract

> NDF-WP-153 — Prompt Execution Contract Baseline. Docs-only governance rule: no runtime, tooling, or enforcement machinery.
> Sprachstatus: EN mit deutscher Kernaussage. / English with a German key statement.

**Kernaussage:** Jede Ausführungsanweisung ist ein vollständiger, eigenständiger aktiver Vertrag — nach jeder Korrektur vollständig neu ausgegeben, nie als Delta.

**Scope:** framework-wide, for every execution instruction in every prompt mode and profile — AI/agent prompts and Human-Maintainer command sequences (PowerShell, Bash/sh, CMD, Git, Docker/Docker Compose, infrastructure CLI, other executable command blocks).

## Execution header

```text
SESSION:         SAME_SESSION_ALLOWED | SAME_SESSION_RECOMMENDED | NEW_SESSION_RECOMMENDED | NEW_SESSION_REQUIRED
SESSION REASON:  one concise line (required for every value except SAME_SESSION_ALLOWED)
STATUS:          COMPLETE | COMPLETE REPLACEMENT
SUPERSEDES:      <instruction ID / WP revision>                          (COMPLETE REPLACEMENT only)
RULE:            Do not merge this instruction with earlier versions.   (COMPLETE REPLACEMENT only)
```

No further metadata is required.

## Rule 1 – Session Declaration

- **Cut-over:** "legacy" means an execution instruction authored before the Human-Maintainer commit accepting NDF-WP-153; an instruction authored under the accepted baseline after that commit is new. No commit hash is embedded here.
- Every new execution instruction declares exactly one `SESSION` value; session continuity is never implicit.
- A missing declaration in a new instruction is a prompt defect → `REWORK` and a `COMPLETE REPLACEMENT`.
- **Legacy fallback (non-breaking):** a legacy instruction is not blocked solely because the declaration is missing; treat it as `NEW_SESSION_RECOMMENDED` and report `SESSION_DECLARATION_MISSING_LEGACY`.

## Rule 2 – Complete Execution Instruction

- One self-contained active contract: neither the executor nor the Human Maintainer has to merge earlier messages to know what to execute.
- Contains, where relevant: goal · scope · authoritative sources · authority · task-specific invariants · allowed/forbidden files · allowed/forbidden operations · task · acceptance criteria · STOP conditions · Human-Maintainer gate · return/output requirements.
- Stable NDF rules are referenced, not copied.
- **Human-Maintainer command sequences** additionally name, where applicable: target shell · working directory · required baseline/preconditions · complete ordered command sequence for the authorised gate · expected result · verification · STOP condition.

```text
COMPLETE != VERBOSE
COMPLETE WITHIN AUTHORIZED SCOPE != REPEAT THE WHOLE PROJECT WORKFLOW
```

## Rule 3 – Complete Replacement

- Triggers: prompt defect · command defect · `REWORK` · resolution of `BLOCKED` · scope correction · authority clarification · review-driven correction · changed allowed/forbidden scope · changed executable instruction.
- The successor is regenerated in full as `STATUS: COMPLETE REPLACEMENT` with `SUPERSEDES`; it reuses the compact current contract, not the conversation history.
- Delta-only executable corrections are invalid — e.g. "use the previous PowerShell block, but replace command 4". Valid: a complete corrected block marked `COMPLETE REPLACEMENT`.
- **Option-selection exception:** a Human-Maintainer selection among options already fully defined in the active instruction needs no replacement — only if it changes none of: scope · authority · allowed/forbidden files · allowed/forbidden operations · executable commands · acceptance criteria · STOP conditions. Otherwise → `COMPLETE REPLACEMENT`.

## Rule 4 – Prompt-over-Skill Output Precedence

- If a generic Skill output contract conflicts with the explicit return format of the active authorised prompt, the prompt's format wins.
- Mandatory minimum reporting content required by higher NDF authority (e.g. Report to Nova, Compact Context Summary, Human-Maintainer gates) stays binding and is fitted into the prompt's structure.
- A Skill never silently replaces or weakens the active execution contract; a real normative conflict is reported and fails closed.

## Authority and fail-closed

- `DERIVE != DECLARE` · `VERIFY != APPROVE` · `EVIDENCE != AUTHORITY` · `EXECUTED != ACCEPTED` · `AGENT_COMPLETE != HUMAN_APPROVED` · `NOVA_REVIEW != HUMAN_ACCEPTANCE`.
- Nova (ChatGPT) – the ChatGPT-based planning, architecture and review role – issues review verdicts (GO / GO WITH NOTES / REWORK / STOP / BLOCKED). A verdict is an evaluation: it does not itself accept governed changes, expand scope, accept ADRs, or perform any Git/release action.
- The Human Maintainer remains the final owner: normative acceptance of governed changes, scope changes, ADR acceptance, and staging, commit, push, tag, and release. This block grants no new authority to any agent or Skill; no AI role stages, commits, pushes, tags, or releases.
- Missing, ambiguous, or conflicting instruction state → STOP / `BLOCKED` with a report; never guess, never merge instruction versions.
