# CDS-WP-006 — Governance, Versioning and Contribution Notes

Internal work-package evidence for CDS-WP-006 — Governance, Versioning,
Contribution, Risk and Publication Model.

- **Date:** 2026-07-16
- **Executed by:** Claude (scoped local work)
- **Final status:** Completed

## Assignment

Define binding governance for roles and decision authority, conflicts between
normative sources, artifact maturity, versioning, compatibility, deprecation and
removal, contributions and acceptance, exceptions, Product Profiles, adoption and
conformance claims, risk ownership and control, release and change control, and
licensing and publication decisions.

Operationalize the CDS-WP-005 architecture without selecting technology or
design. Enterprise-grade, but runnable by a small maintainer circle.

## Preflight

| Check | Result |
| --- | --- |
| Repository root | `D:/Projects/Core-Design-System` — matches |
| Branch | `main` |
| Working tree | Clean |
| Last commit | `c40bf4d docs(cds): define logical design system architecture` — contains CDS-WP-005 |
| Remote | `origin` → `https://github.com/KayKaspers/Core-Design-System.git` |
| Merge / rebase / cherry-pick | None active |
| WP status | 001, 001A, 002, 003, 004, 005 Completed; 006 Next |
| Decisions | DEC-S-001 … DEC-S-032, exactly 32 |
| Risks | RISK-001 … RISK-028, exactly 28 |
| Requirements | CR-001 … CR-040, exactly 40 |
| Architecture | 8 layers · 8 artifact classes · 5 token levels · 5 status axes · 5 consumer contracts · 16 invariants |
| Skills | 38 dirs, 39 files, 39/39 manifest match |

All twelve preflight expectations matched. No fail-closed condition. All 24
required normative documents were read before any change.

## Skills used

Nine authorized Skills. The five prohibited Skills — the three design-oriented
ones plus `ndf-implementation-review-runner` and
`ndf-public-release-body-reviewer` — were **not** loaded.

| Skill | Purpose | Section used |
| --- | --- | --- |
| `ndf-work-package-runner` | WP frame, guardrails, closing structure | Purpose, Allowed/Forbidden, Fail-closed |
| `ndf-adr-governance-review` | Decision-record structure; never mark a decision Accepted autonomously | Allowed/Forbidden actions, Human-maintainer boundaries |
| `ndf-release-safety` | Release steps as human-maintainer instructions only; NO-GO over GO | Forbidden actions, Fail-closed, Release limitations |
| `ndf-feature-scope-runner` | Scope sharpening; open questions instead of assumptions | Expected outputs, Fail-closed |
| `ndf-validation-evidence-reviewer` | Rate evidence honestly; document limits | Expected outputs, Fail-closed |
| `ndf-ethical-growth-reviewer` | Voluntary adoption, transparency, no pressure mechanics | Ethical-use boundaries, Forbidden actions |
| `ndf-public-neutrality-guard` | Neutrality check of produced text | Public-neutrality requirements |
| `ndf-context-pack-maintainer` | Context Pack update; references over repetition | Expected outputs, Forbidden actions |
| `ndf-compact-context-summary-runner` | Report and Compact Context Summary structure | Expected outputs, Output contract |

Two skills shaped substance directly. `ndf-release-safety`'s rule —
*recommend NO-GO rather than GO when readiness is unclear, and never assert
publication* — became the Release Authority section and the publication gate's
fail-closed posture. `ndf-ethical-growth-reviewer`'s framing produced the
publication-honesty section: no pressure to adopt, no implied endorsement, and an
explicit statement of what CDS does **not** offer.

## Governance roles

Six (DEC-S-033): Human Maintainer · Nova · Claude · Consumer Maintainer ·
Contributor · Evidence Reviewer. Roles are functions, not people; separation of
duties applies even when one person holds several.

The governing principle: **authority is granted, never acquired.** Creating,
implementing, or frequently using an artifact confers nothing.

## Tracks

Two: Standard and Elevated. The load-bearing rule is that **proportional
governance scales ceremony, never obligation** — authority, traceability,
evidence, human approval, and fail-closed hold in both. A change that looks
Standard but touches an Elevated trigger is Elevated.

This exists to answer RISK-029 without answering it by bypassing gates.

## Conflict resolution

DEC-S-034: neither normative source wins automatically. Intent without values is
unimplementable; values without intent are meaningless — so a blanket precedence
rule would discard half the truth.

Five conflict states; `Suspected` already blocks. Eight-step fail-closed
procedure. Eight prohibited automatic precedence rules, headed by **recency
wins** — the silent default of nearly every tool.

Only three of the eight conflict types are true conflicts; the other five already
have determinate answers and must not be escalated as if undecidable, or the
process becomes unusable.

## Maturity lifecycle

Seven states (DEC-S-035), three independent axes (maturity, release version,
publication state). Candidate mandatory before Stable (DEC-S-036). Ten-requirement
Candidate gate, seven-requirement Stable gate.

**No existing artifact is declared Candidate or Stable.** Defining a lifecycle
does not populate it — including for the governance documents themselves.

## Versioning and compatibility

MAJOR.MINOR.PATCH (DEC-S-037). Pre-1.0 removes the *promise*, not the duty to
document breaking changes, migrations, revisions, and deprecations.

Ten release identity elements (DEC-S-038); `latest` is not an identity. Eight
compatibility axes with six statements (DEC-S-039); `Not yet assessed` must
survive into the record rather than be rounded up.

**No cadence was invented** — CDS has no evidence for what it could sustain.

## Deprecation and removal

Nine-field deprecation record (DEC-S-040). **A deprecation without a viable
migration path is a removal with extra steps** — if no migration exists, the
artifact is not ready to be deprecated.

Emergency removal is bounded to four causes and defers evidence rather than
waiving it. "Emergency" describes the timeline, not the standard.

## Contributions

Ten-step flow, eleven required inputs, five outcomes (DEC-S-041). Steps 3–5 exist
to reach a cheap *no*.

**`Keep Consumer-local` is a first-class success**, not a soft rejection — CDS
absorbing everything is Non-goal 11.

**External contributions are not yet possible**: they need an approved
publication state and a contribution licensing model, neither of which exists.
No `CONTRIBUTING.md` was created.

## Exceptions

Thirteen fields, six statuses (DEC-S-042). `Expired` is an **uncovered
deviation**, not a grandfathered permission. Recurring exceptions trigger a CDS
gap review.

**Accessibility weakening is not approvable through a normal exception** — which
currently protects a requirement whose value is unknown. Awkward and correct.

## Product Profiles

Twelve required elements (DEC-S-043). The central rule: **a Product Profile is
not retrospective legitimation of an existing consumer design.** SpeakCore and
CastCore hold their own decisions; those stay consumer-local until reconciled and
accepted.

**No profile can be approved today** — accessibility evidence is unobtainable.

## Claims

Four graded types with eight mandatory fields each (DEC-S-044). `CDS certified`
**prohibited** — no programme exists, so the word is unavailable rather than
discouraged.

**No claim is currently valid, by anyone, including CDS itself.**

## Risk governance

The owner model was **provisional since CDS-WP-001** and deferred by every work
package since. Now finalized (DEC-S-045): four roles per risk, with accountability
uniformly on the Human Maintainer and control uniformly on Nova.

Separating them matters: a controller who could accept the risks they assess is
not a control.

All 28 existing risks were updated to the model. **No description, assessment, or
status was changed** — no evidence justified a change.

The anti-ceremonial rule is the point: **documentation is not mitigation**, and
this work package added twelve risks while treating none — recorded rather than
obscured (RISK-040).

## Publication states

Five (DEC-S-046), current state **`Private Development`**, unchanged. Fifteen-point
gate. **Repository visibility is not a publication state** — otherwise a checkbox
performs a publication decision nobody made (RISK-039).

## Licensing model

Ten artifact classes, eleven-field rights matrix each (DEC-S-047). **No licence
selected for any class. No `LICENSE` file created.**

Fonts and brand assets are where naive licensing breaks: fonts are frequently not
redistributable; logos are trademarks whose purpose is to not be freely usable.

Unknown or conflicting rights **block publication absolutely**.

## Release control

Twelve release candidate requirements, six change classes (DEC-S-048). No
automatic publication from `main`; no tag without a Human Maintainer action;
**Claude never releases**. A green build is evidence, not consent.

## New decisions

DEC-S-033 … DEC-S-048 added (16), all Accepted, dated 2026-07-16, typed as
governance, lifecycle and publication decisions. DEC-S-001 … DEC-S-032 unchanged —
only the index header and type table were touched. No ADR. Range now
DEC-S-001 … DEC-S-048, count 48.

## New risks

RISK-029 … RISK-040 added (12), all Monitored, qualitative only, on the finalized
four-role model. Existing risks preserved. Range now RISK-001 … RISK-040,
count 40.

## Files created and changed

**Created (11):** ten governance documents under `docs/governance/` plus this
evidence document.

**Changed (10):** `docs/decisions/DECISION_INDEX.md` ·
`docs/risks/RISK_REGISTER.md` · `project-system/CONTEXT_PACK_FOUNDATION.md` ·
`project-system/PROJECT_PROFILE.md` · `project-system/NEXT_PHASE.md` ·
`project-system/WORK_PACKAGES.md` · `project-brain/PROJECT_BRAIN.md` ·
`README.md` · `CLAUDE.md` · `CHANGELOG.md`.

## Quantitative validation

All counts derived from artifacts by script and independently re-counted.

| Metric | Artifact | Value | Re-counted |
| --- | --- | --- | --- |
| Governance roles | GOVERNANCE_OPERATING_MODEL.md | 6 | Yes |
| Governance tracks | same | 2 | Yes |
| Maturity states | ARTIFACT_MATURITY_LIFECYCLE.md | 7 | Yes |
| Publication states | LICENSING_AND_PUBLICATION_DECISION_MODEL.md | 5 | Yes |
| Claim types | ADOPTION_CONFORMANCE_AND_CLAIMS_POLICY.md | 4 (+1 prohibited) | Yes |
| Artifact licence classes | LICENSING_AND_PUBLICATION_DECISION_MODEL.md | 10 | Yes |
| Change classes | RELEASE_AND_CHANGE_CONTROL_POLICY.md | 6 | Yes |
| Compatibility axes | VERSIONING_… | 8 | Yes |
| Exception statuses | EXCEPTION_AND_PRODUCT_PROFILE_GOVERNANCE.md | 6 | Yes |
| Risk statuses | RISK_REGISTER.md | 5 | Yes |
| Decisions | DECISION_INDEX.md | 48, contiguous | Yes |
| Risks | RISK_REGISTER.md | 40, contiguous | Yes |
| Risk role fields | RISK_REGISTER.md | 40/40 finalized, 0 provisional | Yes |

**One defect found and corrected during validation:** replacing the owner field
left a **duplicate, contradicting "Status values" section** in the risk register —
the old vocabulary (`Open`, `Mitigated`) alongside the new five-status model. The
recount detected two `Status values` headings; the stale section was removed.

No other counting errors. The generate-then-count approach continues to prevent
the error class from CDS-WP-003 and CDS-WP-004.

## Deviations

None. Executed within the defined scope, Allowed Files, and authorized skills.

## Open governance questions

1. **What accessibility target?** (CR-024) — now blocks four gates.
2. **Which licence, per each of the ten artifact classes?** All open.
3. **Is CDS published at all**, and in which state?
4. **Which extension points are approved** for Product Profiles?
5. **What cadence can one maintainer sustain?** Deliberately not invented.
6. **Is the governance affordable?** 48 decisions, 40 risks, 10 policies, one
   maintainer (RISK-026, RISK-029, RISK-040).
7. **When does external contribution open**, and under what rights framework?
8. **What evidence can CDS actually produce** at its capacity?

## Open notes

- **CDS-WP-006 made the accessibility gap load-bearing.** CR-024 now blocks the
  Stable gate, Product Profile approval, the publication gate, and a CoreOps
  pilot entry criterion. Consequently **no artifact can reach Stable and no
  release is possible.** This is a genuine finding of this work package, not a
  side note.
- **Licensing finally has a decision model** — the gap flagged since CDS-WP-002.
  It remains entirely undecided.
- The governance is **untested**. Ten policies exist; none has governed anything.
- **This work package added twelve risks and treated none** — precisely what
  RISK-040 warns about. Recorded honestly.
- All changes are uncommitted. Commit authority rests with the Human Maintainer.

## Completion status

CDS-WP-006 is Completed against its Definition of Done and reported for Human
Maintainer review.
