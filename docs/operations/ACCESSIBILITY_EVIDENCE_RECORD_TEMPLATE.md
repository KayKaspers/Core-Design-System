# Accessibility Evidence Record — Template

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy
- **Baseline:** A11Y-BL-001
- **Date:** 2026-07-16
- **Status:** **Operational template — NOT normative, NOT evidence.** A blank
  reusable record. Copying it creates **no** evidence and **no** claim, and grants
  **no** approval. The evidence-level meanings are owned by the
  [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md).

## How to use

Copy this template into a per-run record for a single artifact/consumer in a single
environment. Bind **exact** versions (DEC-S-071, RISK-052); `current`/`latest` is
not an identity. A single `Pass` is one environment at one revision — it creates
**no global claim** (DEC-S-044, DEC-S-052). `Not tested` and `Not applicable with
rationale` are first-class and must be used honestly.

## Mandatory fields

- **Evidence ID**
- **Evidence level** — AE-1 · AE-2 · AE-3 · AE-4
- **Artifact or consumer**
- **Declared scope**
- **CDS version or revision**
- **Artifact or consumer revision**
- **Baseline version** — A11Y-BL-001 revision + freshness state
- **Operating-system family and exact version**
- **Browser or renderer and exact version**
- **Assistive technology and exact version**
- **Input methods**
- **Language**
- **Channel**
- **Test date**
- **Reviewer** — never the executor, never the artifact (DEC-S-045)
- **Executor**
- **Test cases**
- **Expected result**
- **Actual result**
- **Result status** — see below
- **Defects** — references into the [Defect and Regression Model](../governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md)
- **Known limitations**
- **Deviations**
- **Source references**
- **Approval state** — Human-Maintainer approval is separate and later
- **Freshness state** — Current · Review due · Stale · Superseded · Unknown
- **Next review trigger**

## Result status values

`Pass` · `Pass with limitations` · `Fail` · `Blocked` · `Not tested` ·
`Not applicable with rationale`

- A `Pass` is bound to this record's artifact, revision, environment, and channel.
- **No numeric or percentage score** is produced (a single unmet criterion can make
  a process unusable).
- **`Not tested` is never read as `Passed`.**

## AE-1 for non-rendered source or contract artifacts

*(Additive, CDS-WP-016. This adds the minimum rule needed to make AE-1 usable for
an artifact that has no rendered surface. **No mandatory field is removed,
optional, or relaxed.**)*

An **AE-1** run on a non-rendered source or contract artifact — a machine-readable
source set, a semantic contract, a terminology mapping — genuinely does not
exercise an operating system, a browser or renderer, an assistive technology, or
an input method, because there is nothing to render or operate.

For such a run, and **only** for such a run, those environment fields are recorded
as:

> `Not applicable with rationale` — plus the rationale itself, stating *why* the
> field is not exercised by this artifact at this scope.

They may **never** be:

| # | Prohibited handling |
| --- | --- |
| 1 | **Omitted.** A missing field is an incomplete record, not an absent obligation. |
| 2 | **Filled with a plausible-looking OS, browser, renderer, or assistive-technology version** that was not exercised. Inventing an environment identity is fabricating evidence. |
| 3 | **Treated as passed.** `Not applicable with rationale` is not `Pass`, exactly as `Not tested` is not `Passed`. |
| 4 | **Silently inherited** from another record, artifact, revision, scope, or channel (DEC-S-052). |
| 5 | Used to make an artifact that *does* have a rendered surface look non-rendered in order to skip AE-2/AE-3. |

The record must still bind **all** of the following, exactly as for any other
evidence level:

artifact or consumer · declared scope · **CDS version or revision** · artifact or
consumer revision · **baseline version (A11Y-BL-001 revision) and its freshness
state** · language · channel · test date · executor · reviewer state · test cases
· expected result · actual result · result status · known limitations · deviations
· source references · approval state · **next review trigger**.

**Channel field.** For a **channel-independent** Layer-3 semantic source or
contract, the channel is recorded as *not applicable with rationale*, citing
DEC-S-125 — not as a chosen channel and not as blank. The moment such a source
gains a rendered representation, that representation is a **separate** artifact
with its own Channel Accessibility Profile, its own evidence, and no inheritance
from this record.

**What this section does not do.** It does not make AE-1 sufficient for anything
AE-1 was not already sufficient for: AE-1 alone still supports no conformance
claim (DEC-S-053), still does not substitute for AE-2 or AE-3, and a filled AE-1
record is still evidence only for its own artifact, revision, and scope. It also
does not make this template evidence.

## Rules for this record

- **Not normative and not evidence-by-existence** — a filled record is evidence
  *for its exact environment identity only*; a blank template is neither.
- **No automatic approval** — Nova review and Human-Maintainer approval are separate
  acts; an automated result is input to review, never the review (DEC-S-053).
- **No transfer** — evidence never transfers across artifact, revision, environment,
  channel, scope, or consumer (DEC-S-052).
- **Freshness-bound** — `Unknown`/`Stale` evidence is not current and passes no gate.

## Related documents

- [Accessibility Evidence Strategy](../governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md)
- [Accessibility Evidence and Claims Model](../governance/ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Environment and Scope Matrix](../governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
- [Accessibility Defect and Regression Model](../governance/ACCESSIBILITY_DEFECT_AND_REGRESSION_MODEL.md)
