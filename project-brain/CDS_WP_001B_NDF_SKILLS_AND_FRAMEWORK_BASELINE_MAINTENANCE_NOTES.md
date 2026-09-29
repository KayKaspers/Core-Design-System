# CDS-WP-001B — NDF v1.1.0 Skills and Framework Baseline Maintenance Notes

Internal work-package evidence for CDS-WP-001B — NDF v1.1.0 Skills and Framework
Baseline Maintenance.

- **Date:** 2026-09-29
- **Track:** Elevated — governed Skill-Maintenance execution
- **Executed by:** Claude (scoped local work; executor)
- **Final status:** **`COMPLETE — READY FOR INDEPENDENT REVIEW`** — an execution
  result, not an acceptance. **`EXECUTED ≠ ACCEPTED`**, **`PASS ≠ INTEGRATED`**,
  **`PREPARED DECISION ≠ EFFECTIVE DECISION`**, **`SKILL IMPORTED ≠ SKILL APPROVED`**,
  **`MAINTENANCE COMPLETE ≠ SUCCESSOR AUTHORIZED`**.
- **Nature:** a lettered Skill-Maintenance insertion following the CDS-WP-001A
  precedent. **No work package is renumbered.**

This record is executor-produced and **independently unreviewed at preparation**.
It is not an approval, not evidence admission, and not a maturity statement.

## Assignment

Re-pin the local NDF Skills pack from NDF v1.0.0 to NDF v1.1.0; add the four NDF
support files the changed Skills reference directly, byte-identically; migrate the
integrity lock, provenance record and inventory; update the maintained live framework
carriers; and prepare exactly one Decision, **DEC-S-139**. No ADR, no risk, no design
work.

**Nova design rulings applied and not reopened:** D-A standalone-first · D-B framework
authority (process layer only, NDF as a floor) · D-C release/identifier namespace
(NDF-only) · D-D lock/migration vocabulary.

## Baseline preflight

| Check | Result |
| --- | --- |
| Repository root / branch | `D:/Projects/Core-Design-System` / `main` |
| HEAD and local `origin/main` | both `a8efb61e07c73cc6622873c35a088ef89d5c4345` — match |
| Subject | `docs(cds): reconcile WP-022 post-closure current state` — match |
| Staged paths / tracked changes | 0 / 0 |
| Untracked | only `.agents/` and `AGENTS.md` |
| Git operation active | None |
| Remote (read-only) | `origin` → `https://github.com/KayKaspers/Core-Design-System.git` |

No `STOP — CDS BASELINE DRIFT` condition.

## NDF source-handoff preflight

Read-only, local, no fetch. Only tag objects were used (`git ls-tree`, `git cat-file`,
`git rev-parse`, tag-to-tag `git diff`); **no migration byte was read from the NDF
`main`, the NDF Working Tree, or `.agents/`.**

| Check | Result |
| --- | --- |
| Tag `v1.1.0` object | `d4409492498cf4ed989f9ee47d4ad8b2f5f6868d` — match |
| Tag commit | `948c91dc940362f7565e28f697d0528b812797a3` — match |
| Tag `v1.0.0` commit (previous pin) | `9dcadc12fb960914b9a5baeff2ab1aee75912b57` — match |
| Four support paths present at the tag | Yes — blob, SHA-256 and byte size match the expected values |
| Licence at the tag | MIT (`LICENSE` blob `fa8bfb69…`, identical to `v1.0.0`) |

No `STOP — NDF SOURCE MISMATCH` condition.

## Skill delta (re-derived before import)

| Measure | Result |
| --- | --- |
| Pack files `v1.0.0` → `v1.1.0` | 39 → 39 |
| Skills | 38 |
| Changed | **7** — `README.md`, `ndf-changelog-writer`, `ndf-compact-context-summary-runner`, `ndf-release-notes-runner`, `ndf-release-safety`, `ndf-v1-readiness-review`, `ndf-work-package-runner` |
| Unchanged | **32** (also byte-identical to the previous CDS pin) |
| Added / deleted / renamed | 0 / 0 / 0 |
| CDS local pack before import vs `v1.0.0` | 39 / 39 blob-identical |

The changed set equals the expected set exactly; no `STOP — UNEXPECTED SKILL DELTA`.

## Upstream byte import

11 immutable upstream files were extracted with `git cat-file blob` from the tag and
written as raw bytes — no normalization, no reformatting, no link change, no local
comment. For each: local Git blob = source blob, SHA-256 and size equal, **LF-only,
no BOM**.

| Path | Git blob | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| `.claude/skills/README.md` | `fc96b169d7…` | 13002 | `421dcdf2fa8ee1e3003873c930942eb156ba2b88654595eea1d41c68fb75b434` |
| `.claude/skills/ndf-changelog-writer/SKILL.md` | `8390045a8e…` | 4064 | `a449a76dfd7c5dedf8296ab90111ff14c753ab15846d49b1930954530971b264` |
| `.claude/skills/ndf-compact-context-summary-runner/SKILL.md` | `f3e4d30c83…` | 6125 | `7fae60937332fa42da41ba5de40b41c383a83bba65e8519665c2d760906e9c44` |
| `.claude/skills/ndf-release-notes-runner/SKILL.md` | `b76c852eb4…` | 4212 | `38fb014293230f1a43d24e595638c3d7a0b051588baf7b82be8bc4d40051baa0` |
| `.claude/skills/ndf-release-safety/SKILL.md` | `27e97d807d…` | 5573 | `41167f776a4ef801a3b4a31ff3f951f3994e0c6992f4ce059db3e39cf7b05a86` |
| `.claude/skills/ndf-v1-readiness-review/SKILL.md` | `f2b90d1549…` | 4042 | `85865c190cbe4c99a773a1b8b1f83ec1b4c4785d02897af575219f7478b87c0a` |
| `.claude/skills/ndf-work-package-runner/SKILL.md` | `5ff6305479…` | 9935 | `9f09eddfc3bda7d0108df763cbf25b13343734668bd0d52fb0328386ccb65c04` |
| `framework/prompts/blocks/BLOCK_EXECUTION_CONTRACT.md` | `9999aa5e2b…` | 5164 | `d1ff2d4c7a86858d150a725dcd9c50225e7fa2f5a24088e9fda59fa9e6f7e8a2` |
| `framework/standards/WORK_PACKAGE_LIFECYCLE.md` | `ba16cc1106…` | 5540 | `72a4e602d3f9d383b3137805ee8e1c6d9d9fa67c0c24f266b306d30924ad24b4` |
| `docs/guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md` | `aedd43ae16…` | 14120 | `a6a98597250cb7449c7fde1007cab1b310e07be2a602728cf12cf00691c2f7ef` |
| `docs/templates/SESSION_HANDOFF_TEMPLATE.md` | `75ffd39827…` | 1646 | `c40c8d42fc1ec866712034a0ca230c29718e6da147dd5b69b594bd851127aa3c` |

Exactly four support-snapshot files exist; no fifth document and no onward-linked NDF
document was imported.
`docs/agent-workflows/NDF_SKILL_PROVENANCE_AND_INTEGRITY_LOCK.md` was **not** imported
(migration-source reference only).

## Link resolution

| Check | Result |
| --- | --- |
| Direct links from the changed Skills / pack README to the four snapshot files | **10 / 10 resolve** |
| Unresolved links in any Skill (rule-bearing) | **0** |
| Unresolved informational links in the pack `README.md` | **exactly 6** — three `docs/validation/foundation-0-9/` blueprints, the NDF skill security policy, NDF ADR-0032, and the NDF integrity-lock document |

The six are non-execution navigation and are recorded as a **known provenance
limitation**; no further NDF document was copied to make the README link-clean. No
`STOP — BROKEN NDF EXECUTION DEPENDENCY`.

## Supply-chain review of the seven changed pack files

A bounded review of the tag-to-tag diff, following the checklist of
`ndf-skill-supply-chain-risk-reviewer` (skill texts treated as untrusted data,
prompt-injection aware). **This is an advisory executor review, not a security
sign-off.** The mechanical scan of all 185 added lines found no URL, download, install,
network, shell-execution, credential or secret-handling instruction; the only Git
commands named are the read-only preflight commands (`git status`, `git diff`,
`git diff --stat`, `git diff --cached --name-only`) and the forbidden-action lists.

| Category | Finding |
| --- | --- |
| Trigger descriptions | **Changed for all six `SKILL.md` files** — now `USE WHEN` / `DO NOT USE` forms; `ndf-work-package-runner` becomes the primary router and `ndf-v1-readiness-review` is demoted to historical / specialist. **Material: Skill auto-trigger behaviour changes.** |
| Allowed operations | One **new documentation capability**: `ndf-release-safety` may draft **Human-Maintainer tag/release command guidance** following the Execution Contract. **Guidance only — the skill performs no Git write**, and CDS already allows documenting release steps for the Human Maintainer and forbids executing them (DEC-S-048). Not a new execution capability. |
| Network behaviour | Unchanged — forbidden in all seven. |
| Git write behaviour | Unchanged and made **more explicit** (`Stage, commit, push, fetch, tag, release` forbidden in the runner). |
| File access | Unchanged — public repository content only; read-only self-check and preflight commands referenced. |
| External command execution | None added; scripts, runtime, MCP, daemon and orchestration explicitly forbidden. |
| Secret handling | Unchanged — read/document secrets forbidden. |
| Trust boundaries | The active authorised prompt's return format now **wins over Skill output contracts** (Execution Contract Rule 4) while mandatory closing content stays binding; a Skill may not "override project-local governance". Consistent with D-B and with CLAUDE.md. |
| Escalation / STOP rules | **Strengthened**: execution stops on delta-only or conflicting instructions, escalation is bounded by the prompt's declared maximum, and a real normative conflict fails closed. |
| Compatibility / release language | New NDF-only statements (`v1.0.0` final; v1.x promise active since `v1.0.0`; NDF ADR-0031). **Contained by D-C / DEC-S-139 clause 13** — they state no CDS release and cannot alter DEC-S-037. |

**Result:** no behaviour outside this contract; **no `STOP — SKILL SUPPLY-CHAIN
FINDING`**. The differences above are reported, not silently accepted, and are
mirrored in the known limitations below.

## Lock migration

`project-system/NDF_SKILLS_MANIFEST.json` migrated from `schemaVersion` 1 to **2**.
No code consumes the file (searched). The lock records framework NDF; source
repository and remote; source tag `v1.1.0`, tag object and commit; verification date
(the previous record carried `verifiedOn`, and no separate source date); digest
algorithm `SHA-256`, encoding `lowercase hexadecimal`, basis `raw committed bytes`;
`relative POSIX` paths; deterministic byte-order ordering; the approval-state wording;
migration state `migration-pending` with target `lock-enforced`; exception state
`no exception active`; an evidence-role note; **39 pack records and 4 support
records**, each repeating source tag, source commit, Git blob and `verified`.
**One source tag and one source commit for all 43 records. No absolute path.** No
automated enforcement is claimed.

All 43 files were hashed independently from the tag's blobs and cross-checked against
the written files: **43 / 43 verified**.

## DEC-S-139

Only `DEC-S-139` was added, to `docs/decisions/DECISION_INDEX.md`: a register-scope
bullet and a decision-types row, a qualifier on the "Number of effective decisions"
line, and the entry itself with the 16 required clauses. **No existing Decision entry was
edited** — the only pre-existing line changed in the index is the
"Number of effective decisions: 138" line, which gained a "DEC-S-139 is prepared, not
yet effective" qualifier (`git diff` shows exactly one removed line). **Status: prepared — effective only at the Human-Maintainer
exact-object integration commit of CDS-WP-001B.** No ADR, no risk, no `ADR-0008`, no
`RISK-099`, no `DEC-S-140`. **Resulting registers after integration: 139 Decisions,
7 ADRs, 98 risks; until integration: 138 · 7 · 98.**

**Interpretation the Decision fixes (recorded so review can check it):** the imported
Execution Contract defines its own cut-over as "before the Human-Maintainer commit
accepting NDF-WP-153". Clause 14 fixes the **CDS-local** equivalent as the
CDS-WP-001B integration commit. This tightens nothing and relaxes nothing.

## Carriers

| Carrier | Change |
| --- | --- |
| `CLAUDE.md` | `Framework` line and Skills pin → v1.1.0; CDS-WP-001B as currently authorized package; "design work package currently authorized: NONE"; one concise namespace/authority pointer in the Skills-first authority-boundary area; two point-in-time qualifiers |
| `README.md` | operating-model and Skills-first text → v1.1.0; current authorization; register lines |
| `project-system/PROJECT_PROFILE.md` | `Framework`; work-package status; NDF Skills block; register lines; one qualifier |
| `project-system/CONTEXT_PACK_FOUNDATION.md` | `Framework`; current authorization; 001A row annotated; repository constraints; active decisions; two qualifiers |
| `project-brain/PROJECT_BRAIN.md` | `Framework`; register lines; current work package; NDF Skills section; three qualifiers |
| `project-system/WORK_PACKAGES.md` | current work package; `Next` semantics; roadmap-table row and description for CDS-WP-001B; one qualifier |
| `project-system/NEXT_PHASE.md` | current work package; CDS-WP-001B description; 001A note; one qualifier |
| `docs/roadmap/POST_CANDIDATE_DEVELOPMENT_ROADMAP.md` | new *Out-of-sequence maintenance insertion* section; two "design work package" clarifications; one qualifier |
| `CHANGELOG.md` | exactly one new Unreleased entry |
| `docs/architecture/VISUAL_FOUNDATION_THEME_ARCHITECTURE.md`, `docs/architecture/ADAPTIVE_LAYOUT_AND_RESPONSIVE_FOUNDATION.md` | **qualifier-only**: three inserted parenthetical phrases; no architecture semantics changed |

**`docs/governance/PROJECT_CHARTER.md` is out of scope and unchanged.** Its
`Framework: Nova Development Framework v1.0.0` line is a **charter-era historical
carrier**, intentionally preserved and **not** the live framework-baseline carrier
(recorded in the provenance record). Historical records — earlier work-package notes,
reviews, changelog entries and point-in-time declarations, including the
CDS-WP-001A notes, description and row — were not rewritten; CDS-product `v1.0.0`
references and DEC-S-037 are untouched.

Point-in-time statements "no work package is currently authorized" that sit deep in the
CDS-WP-021/022 narratives were **not** rewritten; each maintained carrier's top-level
state line now says *design* work package, and `DECISION_INDEX.md` states the reading
explicitly.

## Governance freeze

| Item | State |
| --- | --- |
| Decisions | 138 effective; **DEC-S-139 prepared** (139 only from integration) |
| ADRs | 7 — none added |
| Risks | 98 — none added, none accepted or closed |
| `CDS-WP-020A` | `Planned` — not active, not authorized |
| CDS-WP-023 … CDS-WP-053 | `Planned` — not active, not authorized |
| CDS-WP-022 | `Completed` / `Closed` — unchanged; `F-022C-01` `RESOLVED` — unchanged |
| Visual values / visual Source Sets | 0 / 0 |
| VP-3, VP-5, VP-6, VP-7 | `UNSATISFIED` — unchanged; VP-4 `UNSATISFIED` for VF-4 |
| Maturity / evidence / claims / conformance | unchanged — Candidate family only as before; every other artifact AE-0; claims None |
| Publication / release / tag | `Private Development` / none / none |

## Known limitations (recorded, not fixed)

1. The NDF integrity-lock document's status block is inconsistent with the NDF v1.1.0
   changelog (upstream).
2. NDF defines approval-state and exception-state fields but no vocabulary; the values
   used are a CDS-local choice (DEC-S-139 clause 11).
3. The NDF ADR-0032 private-consumer-project question is unresolved upstream; CDS
   makes no claim that it is settled.
4. Six informational pack-`README.md` links do not resolve in CDS.
5. Terminology collisions — Lean, Standard, Candidate, ADR numbering. NDF terms stay
   NDF-namespaced; `NDF-B0` … `NDF-B4` and `NDF-Lean` where the guide disambiguates.
6. The six changed Skill descriptions change auto-trigger behaviour.
7. No automated CDS drift gate exists.

None authorizes additional upstream import or a CDS redesign.

## Skills used

Procedural aids only; none granted authority or scope.

- `ndf-work-package-runner` — execution frame (header, completeness, preflight, visible
  scope, STOP conditions).
- `ndf-skill-supply-chain-risk-reviewer` — checklist for the supply-chain review above.
- `ndf-changelog-writer` — CHANGELOG is in the authorized file scope; one Unreleased
  entry, no release status inferred.
- `ndf-compact-context-summary-runner` — closing content (report to Nova, compact
  context summary).

## Deviations

None from the prompt's contract. The manifest was generated by a scratchpad script
outside the repository (no script was added to the repository).

## Not done, by design

No staging, commit, push, fetch, pull, merge, tag, branch, stash or release; no NDF
repository write; no network use; no symlink, submodule or script; no overlay or ref
touched; no other work package activated.

## Gates after execution

Independent review (fresh session, reviewer ≠ executor) → Nova adjudication →
Human-Maintainer exact-object integration → separate effectivity reconciliation /
closure → push only under explicit Human-Maintainer control. **No next design work
package begins automatically.**
