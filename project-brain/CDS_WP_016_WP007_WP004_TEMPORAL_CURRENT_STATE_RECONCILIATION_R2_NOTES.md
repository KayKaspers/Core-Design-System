# CDS-WP-016 — WP-007 / WP-004 Governance-Control Temporal Reconciliation R2 — Notes

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-016 — Temporal Current-State Reconciliation, Round 2
  (Governance and Active-Control Surface Tranche)
- **Date:** 2026-08-12
- **Status:** **Operational evidence — NON-normative.** These notes record how the
  reconciliation was derived and bounded. They decide nothing, approve nothing,
  and are not a policy source.

## Baseline

| Item | Value |
| --- | --- |
| Starting HEAD | `c7e1c151be8e4e707dbbe22ba4b439fb5fc57b6a` |
| Starting tree | `3c8fee102e0a4a64afef6bc905b499452077b118` |
| Parent | `bb38b0ce771aabac4c599883be8caa177bd9b59f` |
| Branch | `main`; HEAD == `origin/main` (read-only `git ls-remote`) |
| Working tree / index before | CLEAN / CLEAN |
| Merge · rebase · cherry-pick | none active |

### Source work-package ancestry

| WP | Commit | Subject | Ancestry |
| --- | --- | --- | --- |
| CDS-WP-004 | `3c1acecd198d94f3f0189216e51e631eee29e521` | docs(cds): define consumer requirements and CoreOps pilot | **PASS** (exit 0) |
| CDS-WP-007 | `7b716522b6dc9b8b43801419550b47233712e613` | docs(cds): define accessibility and inclusive design policy | **PASS** (exit 0) |

Both work packages are committed repository history. Every current statement that
made their effect conditional on a *future* Human-Maintainer commit was therefore
stale.

## R1 result carried forward

R1 (`…TEMPORAL_CURRENT_STATE_RECONCILIATION_R1`) ended **BLOCKED —
TEMPORAL_RECON_SCOPE_INCOMPLETE** with **0 modified · 0 added · 0 deleted** and no
Git write of any kind. R1 blocked because fresh discovery proved the authorized
scope incomplete: current WP-007 drift existed in normative governance files that
the R1 scope did not cover. R2 was authorized with an expanded 12-file scope and a
deliberate tranche split.

## Skills

Verified **38 skill directories · 39 skill files · 39/39 manifest SHA-256
matches**. Used exactly the eleven skills named in the prompt:
`ndf-work-package-runner`, `ndf-accessibility-reviewer`,
`ndf-validation-evidence-reviewer`, `ndf-implementation-review-runner`,
`ndf-adr-governance-review`, `ndf-release-safety`,
`ndf-existing-project-analysis-runner`, `ndf-feature-scope-runner`,
`ndf-content-tone-reviewer`, `ndf-context-pack-maintainer`,
`ndf-compact-context-summary-runner`. No additional skills. No skill widened
authority.

## Dual-method discovery

**Method A — line-oriented.** Repository-wide regular-expression search over all
non-`.git` paths for the WP-007 and WP-004 temporal families and for the
architecture dependency phrase `no maturity model exists`.

**Method B — whitespace-normalized whole-file semantic search.** Helper script
held **outside** the repository. Strict UTF-8 whole-file reads; consecutive
whitespace collapsed to a single space; case-insensitive matching; eighteen
semantic patterns. Every normalized match is mapped back to its true starting
line through a character-offset index, so occurrences wrapped across Markdown
line breaks report correctly. Method B found sites invisible to line-oriented
search (DEC-S-060, the release-policy clause, the architecture clause).

**Reading in context was decisive.** Two current WP-007 occurrences matched no
pattern and were found only by reading candidate regions in full:
`CONTEXT_PACK_FOUNDATION.md` (`the accessibility target (CR-024) are all
missing`) and `PROJECT_BRAIN.md` (`the undefined accessibility target`). Pattern
search alone would have left the tranche incomplete.

### Fresh counts

| Category | Occurrences | Files |
| --- | --- | --- |
| **A — current WP-007 governance/control drift** | **13** | **10** |
| **B — current WP-004 governance/control drift** | **6** | **6** |
| **H — architecture separate temporal dependency drift** | **1** | **1** |

The R2 prompt's informational expectation was 11 / 9 for Category A. The two
additional occurrences are the context-found sites above; both lie inside files
already authorized, so the scope gate was unaffected.

### Category A paths (all inside the authorized scope)

| # | Path | Line |
| --- | --- | --- |
| 1 | `docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md` | 33 |
| 2 | `docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md` | 147 |
| 3 | `docs/governance/COREOPS_PILOT_ACCESSIBILITY_CRITERION.md` | 162 |
| 4 | `docs/governance/COREOPS_PILOT_CONTRACT.md` | 68 |
| 5 | `docs/decisions/DECISION_INDEX.md` | 2128–2130 (DEC-S-060) |
| 6 | `docs/governance/CONSUMER_REQUIREMENTS_TRACEABILITY.md` | 64 |
| 7 | `docs/governance/CONSUMER_REQUIREMENTS_MODEL.md` | 154 |
| 8 | `docs/governance/GOVERNANCE_OPERATING_MODEL.md` | 246–263 |
| 9 | `docs/governance/RELEASE_AND_CHANGE_CONTROL_POLICY.md` | 130–133 |
| 10 | `project-system/PROJECT_PROFILE.md` | 265–266 |
| 11 | `project-brain/PROJECT_BRAIN.md` | 577 |
| 12 | `project-system/CONTEXT_PACK_FOUNDATION.md` | 616 |
| 13 | `project-brain/PROJECT_BRAIN.md` | 391–392 |

### Category B paths (all inside the authorized scope)

`docs/governance/COREOPS_PILOT_CONTRACT.md:9` · `README.md:198` ·
`project-system/PROJECT_PROFILE.md:356` ·
`project-system/CONTEXT_PACK_FOUNDATION.md:614` ·
`project-brain/PROJECT_BRAIN.md:490` · `docs/risks/RISK_REGISTER.md:615`

### Scope gate

**PASS.** Every Category A and Category B occurrence lies within the twelve
authorized files. The single occurrence outside them is the architecture path,
classified H and deliberately excluded.

## Status-only changes

All edits replace a temporal/status qualifier. No requirement, gate, obligation,
role, authority, evidence level, or maturity state was changed.

| File | Prior meaning | Corrected meaning |
| --- | --- | --- |
| `COREOPS_PILOT_ACCESSIBILITY_CRITERION.md:33` | policy becomes a normative basis after a future commit | the policy is committed and serves as a normative basis |
| `COREOPS_PILOT_ACCESSIBILITY_CRITERION.md:147` | criterion satisfiable upon a future WP-007 commit | criterion met by the WP-007 commit |
| `COREOPS_PILOT_ACCESSIBILITY_CRITERION.md:162` | `Satisfiable on commit` | `Met — committed with CDS-WP-007` |
| `COREOPS_PILOT_CONTRACT.md:9` | normative upon a future commit; a proposal until then | normative — committed with CDS-WP-004; not an active pilot |
| `COREOPS_PILOT_CONTRACT.md:68` | criterion 8 satisfiable upon a future WP-007 commit | criterion 8 met by the WP-007 commit |
| `DECISION_INDEX.md` DEC-S-060 | criterion satisfiable upon a future WP-007 commit | criterion met by the WP-007 commit |
| `CONSUMER_REQUIREMENTS_TRACEABILITY.md:64` | `activates on Human Maintainer commit` | `committed and in effect` |
| `CONSUMER_REQUIREMENTS_MODEL.md:154` | `activates on commit` | `committed and in effect` |
| `GOVERNANCE_OPERATING_MODEL.md` | target and evidence method do not yet exist; deferred to WP-007 | both exist and are committed; no evidence produced, every artifact AE-0 |
| `RELEASE_AND_CHANGE_CONTROL_POLICY.md` | Stable blocked because the target is undefined | Stable blocked because no accessibility evidence exists (AE-0) |
| `PROJECT_PROFILE.md:266` | entry criterion satisfiable on commit | entry criterion met with the WP-007 commit |
| `PROJECT_PROFILE.md:356` | pilot contract is a proposal | pilot contract is committed |
| `CONTEXT_PACK_FOUNDATION.md:613–617` | contract normative only upon commit; target missing | contract committed; target decided, evidence absent |
| `PROJECT_BRAIN.md:391–392` | blockers trace to the undefined target | blockers trace to absent evidence (AE-0) |
| `PROJECT_BRAIN.md:490` | contract normative only upon commit | contract committed and normative |
| `PROJECT_BRAIN.md:577` | entry criterion satisfiable on commit | entry criterion met with the WP-007 commit |
| `RISK_REGISTER.md:615` | contract normative only upon commit | contract committed and normative |

### CR-024 requirement tables

Only the temporal activation clause changed in each table. Requirement ID,
classification (`Deferred Requirement`), priority, ownership, the
`evidence absent` statement, the no-conformance boundary, the follow-up
(`CDS-WP-008`), and the row status (`Open`) are unchanged in both files. The
requirement-statement row `CONSUMER_REQUIREMENTS_MODEL.md:109` and the deferred-
requirement narrative at line 247 were left untouched: they record the original
CDS-WP-004 evidence verdict, not current CDS status.

### Governance Operating Model

The section heading `Open accessibility dependency` is retained because the
dependency is still open — what changed is *why*. The premise moved from "the
target and evidence method do not yet exist" to "both exist and are committed; no
evidence has been produced." All four consequence bullets are retained. The claim
prohibition and the Stable-gate constraint are unchanged and unweakened. The
exception bullet keeps DEC-S-059 and RISK-028 intact, restated from "value is
unknown" to "conformance is unverified" — the target value is now known, the
measurement is not. The pilot bullet was narrowed to the accessibility-specific
truth (Group E cannot be evidenced) rather than asserting anything about the
other entry criteria. The closing invitation to advance CDS-WP-007 was removed as
spent.

### Release and Change Control

The nine release-readiness requirements are unchanged. The unresolved
licensing/publication blocker (requirement 7) is unchanged. Only the stale factual
reason was replaced. The replacement — no accessibility evidence exists, every
artifact is AE-0 — is derived from existing current normative state
(DEC-S-036 Stable gate; the AE-0 fact recorded across the accessibility suite) and
mirrors the wording already present in `CONTEXT_PACK_FOUNDATION.md`
("the remaining obstacles are the **absent accessibility evidence**"). No new
release gate was invented, and **`No CDS release is possible today` is retained
verbatim**.

## Decision and Risk authority

- **DEC-S-060** — future-commit wording repaired. Decision ID, status, date, work
  package, rationale and all six consequences unchanged, including
  "This closes a policy gap, not an evidence gap."
- **DEC-S-036** — **PRESERVED UNCHANGED.** Its consequence still reads "the
  accessibility target does not exist". Classified as a historical CDS-WP-006
  Decision consequence.
- **DEC-S-046** — **PRESERVED UNCHANGED**, same class.
- **Decision count: 124 before · 124 after.** No decision created, deleted,
  renumbered, retitled, or re-argued.
- **Risk Register** — one mitigation-direction sentence in RISK-018 changed, and
  only its WP-004 contract commit-state clause. RISK-028 was initially preserved
  in full here, including "the accessibility target is undefined", on a
  historical-framing classification. **That classification was wrong and was
  corrected in the Nova rework recorded below.**
  **97 risks · 90 Monitored · 7 Mitigating · 0 Accepted · 0 Closed** — unchanged.

## Pilot state

The CoreOps Pilot Contract is now described as committed repository governance.
**The pilot remains inactive.** Entry criteria 2, 4, 5, 6 and 7 remain
Pending/Unmet in both the contract and the criterion document; "The pilot cannot
start" and "no pilot has started" are retained everywhere. Criterion 8 is recorded
as met **as a decision**, which is what CDS-WP-007 resolved — not as evidence.
`contract committed` and `pilot inactive` coexist by design and are not a
contradiction.

## Accessibility boundaries preserved

Target exists (**WCAG 2.2 Level AA**) — evidence does not. Evidence *method*
exists — evidence *produced* does not. Every CDS artifact remains **AE-0**. No
AE-1, AE-2, AE-3 or AE-4 was created. A11Y-BL-001 remains a committed baseline and
is not evidence. No conformance claim of any level was created or implied.
Candidate remains **No**.

## Excluded architecture residual

**`docs/architecture/CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md` line 186** —
"Entry criteria remain unmet: the architecture needs approval, no maturity model
exists, and the accessibility target is undefined (CR-024)."

- Blob before: `0605bcbb9523db218d149243725b25d8a9f06e0b`
- Blob after: `0605bcbb9523db218d149243725b25d8a9f06e0b` — **byte-identical**
- Classification: **ARCHITECTURE_SEPARATE_DRIFT**
- Mutation: **none**

The sentence carries two independently stale dependency assertions — a WP-006
maturity-lifecycle claim and a WP-007 accessibility-target claim. Repairing only
the accessibility half would leave a half-true sentence in a normative
architecture source. Disposition:
**SEPARATE ARCHITECTURE TEMPORAL DEPENDENCY RECONCILIATION REQUIRED.** This is a
known residual, not an R2 tranche failure.

A materially similar mixed pair exists at
`project-system/CONTEXT_PACK_FOUNDATION.md:614–617`, where the same sentence named
both a missing maturity model and a missing accessibility target. There the
WP-007 half was inside the authorized active-control scope and was corrected,
while **the maturity-model assertion was left verbatim** for the same separate
reconciliation. That residual is registered as a finding.

## Post-mutation discovery

Both methods were re-run against the mutated tree.

- **WP-007 governance/control tranche drift: 0**
- **WP-004 governance/control tranche drift: 0**
- Same-file contradictions in modified files: **0**

Ten live occurrences remain repository-wide, every one deliberately out of
tranche: `CHANGELOG.md` (2, historical release record) ·
`docs/architecture/CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md` (1, Category H) ·
`DECISION_INDEX.md` DEC-S-036 and DEC-S-046 (2, preserved by instruction) ·
`LICENSING_AND_PUBLICATION_DECISION_MODEL.md` (1, already current and true) ·
`RISK_REGISTER.md` RISK-028 (2 — **subsequently reassessed in the Nova rework
below; no longer present**) · `project-system/NEXT_PHASE.md` (1,
historical "CDS-WP-007 — Completed" summary). Twenty-one further occurrences sit
in R2/R3 and AE-1 reconciliation evidence files, which are historical records.

**This run does not claim whole-repository WP-007 temporal zero-drift.** It claims
tranche zero-drift for the governance and active-control surface only.

## Preserved boundaries

- **WP-011 … WP-015 and ADR pending-commit drift: untouched.** The 24-path class
  and its unresolved occurrence-count disagreement (R3 notes 52 · independent
  review 54) were neither resolved nor normalised.
- **AE-1 Future Mirror Inventory: 33 — unchanged.** Ambiguous set: **1 —
  unchanged.**
- **WP-010 / A11Y-BL-001 reconciliation: untouched.**
- Independent-review and AE-1 correction evidence: untouched.

## Encoding note

An editing-tool artifact converted
`docs/governance/CONSUMER_REQUIREMENTS_TRACEABILITY.md` wholesale to CRLF. This
was detected by `git diff --check`, verified against the committed blob (114 LF,
0 CRLF) and repaired in place. All twelve modified files are strict UTF-8, LF-only
and BOM-free; `git diff --check` passes. The repair is recorded here because it
was a real regression, caught and corrected rather than silently carried.

## Technical regression

Fresh virtual environment outside the repository; `PYTHONDONTWRITEBYTECODE=1`;
exactly the seven pins of `requirements-validator.lock`; no runtime network. No
`__pycache__` was written into the repository.

| Run | Expected | Actual |
| --- | --- | --- |
| `python -B -m unittest tests.validator.test_semantic_status -v` | 39 | **39 passed · 0 failed · 0 errors · 0 skipped** |
| `python -B -m unittest discover -s tests/validator -p "test_*.py" -v` | 112 | **112 passed · 0 failed · 0 errors · 0 skipped** |
| `python -B -m tools.cds_validator validate-cases …/VALIDATION_CASES.json` | 24 | **24 cases · 24 matches · 0 mismatches · 0 internal errors · exit 0** |

These runs produce **no accessibility evidence** and no Candidate status.

## Governance state after R2

Candidate **No** · Revision `semantic-status-rev-0001` · Maturity **Experimental**
· Approval **Unapproved** · Dossier **Draft – Candidate gate incomplete** ·
Semantic Status **AE-0** · A11Y-BL-001 committed baseline · AE-1/2/3/4 **NONE** ·
Decisions **124** · Risks **97** (90 / 7 / 0 / 0) · ADRs **3** · CDS-WP-016 open ·
CDS-WP-017 not activated · Publication **Private Development** · Claims **None** ·
Pilot **inactive** · AE-1 mirror count **33** · Ambiguous count **1**.

## Git state

No Git write action of any kind. No add, commit, push, pull, fetch, merge, rebase,
cherry-pick, reset, restore, clean, branch change, tag, release, or history
change. HEAD and index are unchanged; all edits are uncommitted working-tree
changes awaiting Human-Maintainer review. Commit authority rests solely with the
Human Maintainer.

## Nova review and RISK-028 rework

### Nova review

| Item | Value |
| --- | --- |
| Original R2 executor result | `CDS_WP_016_WP007_WP004_GOVERNANCE_CONTROL_TEMPORAL_RECONCILIATION_R2_COMPLETE` |
| Nova decision | **REWORK REQUIRED** |
| Reason | `RISK-028 CURRENT-RISK TEMPORAL STATE NOT RECONCILED OR EXPLICITLY ACCOUNTED FOR` |

The finding is **reproduced and accepted**. R2 classified RISK-028 alongside the
DEC-S-036 / DEC-S-046 Decision consequences as a historical, revision-bound
record and preserved it unchanged. That classification was wrong.

### Why RISK-028 is not an immutable Decision record

A Decision record fixes what was decided at a point in time; its consequences are
historical by construction. A risk entry is a **living instrument**. The
[Risk Governance Model](../docs/governance/RISK_GOVERNANCE_MODEL.md) states that a
risk is re-assessed when, among other triggers, **a related work package
completes** or **a related decision changes**. Both fired: CDS-WP-007 completed
and was committed, and DEC-S-049 / DEC-S-060 were added. RISK-028 therefore owed a
reassessment, and carrying "the accessibility target is undefined" forward as a
current `Monitored` risk statement was a genuine current-state defect — not a
preserved historical artefact.

### Exact change

**Description — before**

> Architecture decisions made before CDS-WP-007 may inadvertently constrain future
> accessibility requirements or make them costly to adopt.

**Description — after**

> Architecture decisions taken before CDS-WP-007 may have constrained the
> now-defined accessibility requirements, or made them costly to adopt.

**Impact — before (opening and closing clauses)**

> The architecture is being decided while the accessibility target is undefined
> (CR-024). … A CoreOps pilot entry criterion is also blocked until the target
> exists.

**Impact — after (opening and closing clauses)**

> Much of the architecture was decided before the accessibility target existed
> (CR-024). The target is now defined — **WCAG 2.2 Level AA** (DEC-S-049,
> DEC-S-060), committed with CDS-WP-007 — but **no accessibility evidence has been
> produced, and every CDS artifact is AE-0**. Whether the existing structure is
> compatible with the committed policy is therefore neither demonstrated nor
> refuted; the missing evidence is what keeps this risk open, not a missing
> target. … Pilot Group E still cannot be evidenced.

The middle of the Impact paragraph — the load-bearing-cost argument and the
benchmark/consumer evidence-weakness observation — is retained verbatim.

**Mitigation direction — before (closing clause)**

> … Consider advancing CDS-WP-007 or deciding the target earlier than the roadmap
> implies, since the architecture cannot fully validate Pilot Group E without it.

**Mitigation direction — after (closing clause)**

> … Make **no conformance claim of any kind** meanwhile: the committed policy is
> not evidence, and documentation is not mitigation. Validate the existing
> architecture against the committed policy once an authorized scope exists for
> that work; the architecture's own stale dependency state belongs to the separate
> architecture temporal-dependency reconciliation, not here.

The structural-constraint guidance is retained; only "constraints survive a later
policy" became "constraints survive policy revision", because the policy now
exists and the principle applies to its future revision.

### What did not change

Risk heading and identity · ID `RISK-028` · **Status `Monitored`** · Accountable
Risk Owner, Risk Controller, Mitigation Executor and Evidence Reviewer roles ·
**Initial likelihood `Medium`** · **Initial severity `High`**. No renumbering, no
deletion, no new risk. Risk totals remain **97 · 90 Monitored · 7 Mitigating ·
0 Accepted · 0 Closed**.

**No closure and no acceptance.** Only the Human Maintainer may set a risk
`Accepted` or `Closed`; Claude may never do either, and Nova may not accept a
risk. Nothing here is a treatment: the model is explicit that **documentation is
not mitigation — a policy addressing a risk is a first step, not a treatment.**
CDS-WP-007 delivered policy, not architectural validation.

**The risk meaning is preserved.** The subject remains that architecture
established before the accessibility policy was finalised may carry accessibility
debt. What changed is only the temporal premise: the open question is no longer
"against what target?" but "is the existing structure compatible with the
committed target?" — unanswerable while every artifact is AE-0. The absence of
evidence prevents the reassuring conclusion just as firmly as it prevents the
alarming one, so the risk stays open at unchanged likelihood and severity.

**The architecture residual stays separate.** RISK-028 now points at the
architecture validation question but performs none of it.
`docs/architecture/CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md` and the retained
maturity assertion in `CONTEXT_PACK_FOUNDATION.md:614` are untouched by this
rework.

### Post-rework classification

RISK-028 is no longer carried as "historical preserved". It is a
**current monitored risk — temporally reassessed**, current-state-true as of the
committed CDS-WP-007 while remaining fully open on the evidence question.

### Rework scope

Modified by this rework: `docs/risks/RISK_REGISTER.md` and this notes file only.
No file added, none deleted. The twelve pre-existing R2 working-tree changes were
verified intact and unaltered, HEAD is unchanged, and the index remained CLEAN
throughout.

## Required next steps

1. **Fresh independent review** of this reconciliation by a reviewer who is not
   its executor — these notes are executor-produced evidence.
2. **Human-Maintainer decision and commit.**
3. **Separate Architecture Temporal Dependency Reconciliation** covering
   `docs/architecture/CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md` and the
   retained maturity-model assertion in `CONTEXT_PACK_FOUNDATION.md`.
4. Unchanged and still open: the WP-011 … WP-015 / ADR class, and the Decision-
   record supersession question for DEC-S-036, DEC-S-043 and DEC-S-046.
