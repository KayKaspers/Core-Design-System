# Semantic Status Candidate — Accessibility Limitations

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Accessibility Gate Remediation
- **Date:** 2026-08-17
- **Scope:** the **Semantic Status Candidate source and contract family**
- **Status:** **Limitation record — NOT normative, NOT evidence, NOT a waiver.**
  The normative source is the
  [Accessibility Limitations and Exception Policy](ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md).

## The three sentences that govern this document

> **A limitation is not a passed test.**
> **A limitation is never grounds for promotion.**
> **Neither a limitation nor an exception can waive an accessibility
> requirement** (DEC-S-059).

Recording a barrier does not remove it. This document exists to make the cost of
the current state visible to whoever must decide — not to make the state
acceptable.

## Fields held in common

Requirement 6 of the [Candidate accessibility gate](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md#candidate-accessibility-gate)
requires the normative 15-field limitation record. Three fields are identical for
all sixteen entries and are stated **once here**, holding **per entry**:

| # | Field | Value for every entry below |
| --- | --- | --- |
| 4 | **CDS version or revision** | `7ac8a9e7be021a05e517adda64751920a5eff247`, plus the CDS-WP-016 working-tree changes; source revision `semantic-status-rev-0001` |
| 10 | **Owner** | CDS — Human Maintainer is the only role that may approve a limitation with normative effect (DEC-S-045) |
| 15 | **Approval state** | **Unapproved.** No limitation here has been approved by the Human Maintainer, and none may be treated as accepted. |

The remaining twelve fields — ID, affected artifact, scope, affected user needs,
affected requirements or success criteria, impact, cause, available alternative
or mitigation, evidence, review trigger, expiry or re-assessment point, and claim
effect — are stated per entry.

## The user-impact boundary — read this before the entries

Field 5 (**affected user needs**) and field 7 (**impact**) are the fields that
keep a limitation record honest. Both require care here, and the reasoning is
stated openly so a reviewer can test it rather than infer it:

**The Semantic Status Candidate ships no user-facing artifact.** It is four
contract documents, a terminology mapping, and a 25-token JSON source. There is
no interface, no page, no process, and no user path. Consequently:

- The **actual user impact of every entry below is `Unknown / not directly
  evaluated at source-only scope`.** Nothing has been evaluated with users
  because there is nothing for a user to use.
- **This is not a claim that the impact is zero.** "Not evaluated" and "no
  impact" are different statements, and conflating them is exactly the failure
  this policy exists to prevent.
- Field 9 (**available alternative or mitigation**) reads *not applicable at
  source-only scope* rather than **None** for most entries. Under the policy,
  `None` means *a blocked user has no equivalent path*, which makes an artifact
  ineligible for Candidate. **No user is currently blocked, because no user-facing
  path exists to be blocked.** The mitigation that does exist is the maturity and
  claim restriction itself: nothing may be adopted, consumed, or claimed.
- **Consequence, stated plainly: no downstream user-facing claim is permitted on
  the basis of anything in this document.**

**This reasoning is the single most reviewable judgement in this remediation.**
It is the difference between "0 Critical limitations" and "16 unassessed
barriers", and it rests entirely on the premise that no user-facing
representation exists. The fresh independent reviewer should test that premise
first; if it fails, every severity below is wrong.

## Classification

| Class | Meaning |
| --- | --- |
| **Evidence gap** | Something that must eventually be evidenced has not been. It constrains maturity and claims. |
| **Scope exclusion** | Something deliberately outside this Candidate's scope. Not a barrier; recorded so it cannot later be mistaken for coverage. |
| **Claim boundary** | A restriction on what may be said, rather than a gap in what exists. |

**Severity** uses the normative three-value scale: **Critical** (a user group
cannot complete a process, no alternative — blocks Candidate *and* Stable) ·
**Significant** (degraded, alternative exists — blocks Stable; Candidate possible
if documented) · **Minor** (narrow, documented, alternative exists).

---

## SSC-LIM-001 — No user research

- **Affected artifact:** the whole Semantic Status Candidate family
- **Scope:** all 25 values, all contract documents, DE and EN
- **Affected user needs:** everyone who would have to *understand* a status
  statement — in particular people relying on plain language, people with
  cognitive or reading-related needs, and non-native readers of either language
- **Affected requirements:** WCAG 3.3.x and content/cognitive accessibility
  expectations generally; **AE-4** in the evidence model
- **Impact:** `Unknown / not directly evaluated at source-only scope`. It is not
  known whether any of the 25 canonical meanings, or their DE/EN labels, are
  actually understood as intended by anyone outside this project.
- **Cause:** no user research has been conducted; committed documentation
  evidences stated intent, never that an experience works for real people
  (RISK-017)
- **Alternative / mitigation:** not applicable at source-only scope — no user
  path exists. Mitigation is the claim restriction: no understandability claim
  may be made.
- **Evidence:** none. Executor-produced content review and the independent
  WP-016 terminology/accessibility/content review are **contract** reviews, not
  user evidence.
- **Review trigger:** the first user-facing representation; any change to the
  25 canonical meanings; any added language
- **Expiry / re-assessment:** re-assess at the first representation, and in any
  case at the next Candidate-gate review
- **Claim effect:** **blocks every claim about understandability, usability, or
  user outcome.** Class: **Evidence gap** · Severity: **Significant**

## SSC-LIM-002 — No assistive-technology execution

- **Affected artifact:** the whole family
- **Scope:** all Tier-1 baseline pairings (A11Y-ENV-001, A11Y-ENV-002)
- **Affected user needs:** screen-reader users; anyone depending on
  programmatic exposure of status and status changes
- **Affected requirements:** WCAG 4.1.2, 4.1.3; A11Y-BL-001 Tier-1 entries 5, 6,
  12; **AE-3**
- **Impact:** `Unknown / not directly evaluated at source-only scope`. No status
  representation has ever been exposed to an assistive technology.
- **Cause:** there is nothing to expose — no rendered artifact exists — and no
  execution environment is available (RISK-051)
- **Alternative / mitigation:** not applicable at source-only scope. The
  source-level mitigation is structural: `unknown` is a first-class value and
  textual meaning exists for all 25 values, so a future representation *can* be
  exposed truthfully.
- **Evidence:** none
- **Review trigger:** the first rendered representation (regression trigger T-13)
- **Expiry / re-assessment:** at the first representation; mandatory before any
  Stable consideration
- **Claim effect:** **AE-3 is unreachable; Stable is unreachable; no
  assistive-technology support claim may be made.** Class: **Evidence gap** ·
  Severity: **Significant**

## SSC-LIM-003 — No interactive or rendered representation

- **Affected artifact:** the whole family
- **Scope:** all channels
- **Affected user needs:** none directly — there is nothing to interact with
- **Affected requirements:** the **30 representation-triggered** WCAG criteria in
  the [applicability mapping](SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md)
- **Impact:** `Unknown / not directly evaluated at source-only scope`. This is
  the structural reason 30 of 55 criteria are not assessable.
- **Cause:** deliberate. The first CDS Candidate is a **meaning** foundation, not
  a visual one (DEC-S-113).
- **Alternative / mitigation:** not applicable — this is a scope decision, not a
  barrier
- **Evidence:** not applicable
- **Review trigger:** regression trigger T-13 (first visual binding)
- **Expiry / re-assessment:** at the first representation
- **Claim effect:** **no claim about rendered or interactive behaviour is
  possible.** Class: **Scope exclusion** · Severity: **Minor**

## SSC-LIM-004 — No consumer composition evidence

- **Affected artifact:** the whole family
- **Scope:** all consumers
- **Affected user needs:** all users of any future product that would display CDS
  status — composition, content, and process are where accessibility is usually
  lost
- **Affected requirements:** the **20 consumer-owned** WCAG criteria; **AE-4**
- **Impact:** `Unknown / not directly evaluated at source-only scope`
- **Cause:** **no consumer of the Semantic Status source exists and none is
  authorized** (DEC-S-124, RISK-097); the CoreOps pilot is inactive
- **Alternative / mitigation:** not applicable at source-only scope
- **Evidence:** none. **Accessible artifacts do not compose into an accessible
  product** (DEC-S-052).
- **Review trigger:** the first authorized consumer integration or pilot start
- **Expiry / re-assessment:** at the first consumer integration
- **Claim effect:** **no product, adoption, or conformance claim is possible.**
  Class: **Evidence gap** · Severity: **Significant**

## SSC-LIM-005 — No Product Profile

- **Affected artifact:** the whole family
- **Scope:** Product-Profile extension points
- **Affected user needs:** none directly today
- **Affected requirements:** invariant 10; DEC-S-112, DEC-S-124
- **Impact:** `Unknown / not directly evaluated at source-only scope`. No profile
  has ever remapped the vocabulary, so no profile-induced meaning loss has been
  observed — or ruled out.
- **Cause:** deliberate. `approvedExtensionPoints` is empty; no Product Profile
  may reference or remap the status vocabulary.
- **Alternative / mitigation:** not applicable — an empty extension surface is
  the safest state, not a gap
- **Evidence:** the fail-closed remapping check (FC-8) exists but has been
  exercised only against synthetic cases
- **Review trigger:** the first proposed Product Profile touching status
- **Expiry / re-assessment:** at the first proposed profile
- **Claim effect:** **no profile-related claim is possible.** Class: **Scope
  exclusion** · Severity: **Minor**

## SSC-LIM-006 — No visual binding

- **Affected artifact:** the whole family
- **Scope:** colour, icon, shape, position, motion
- **Affected user needs:** none directly today; protective for colour-vision and
  low-vision users in the sense that no colour-only encoding *can* exist yet
- **Affected requirements:** WCAG 1.4.1, 1.4.3, 1.4.11, 1.3.3; invariant 7
- **Impact:** `Unknown / not directly evaluated at source-only scope`
- **Cause:** deliberate. No visual value of any kind is authorized or created.
- **Alternative / mitigation:** not applicable — the absence *is* the current
  safeguard
- **Evidence:** the appearance-oriented-role check
  (`CDS-V4-STATUS-VISUAL-LEAKAGE`) fails closed on any visual role in the source
- **Review trigger:** regression trigger T-09 (first non-textual meaning carrier)
- **Expiry / re-assessment:** at the first visual binding, when AE-2 and AE-3
  become required
- **Claim effect:** **no visual-accessibility claim, including contrast, is
  possible.** Class: **Scope exclusion** · Severity: **Minor**

## SSC-LIM-007 — No complete-process validation

- **Affected artifact:** the whole family
- **Scope:** end-to-end processes in any product
- **Affected user needs:** every user who must complete a task in which a status
  is shown — a single unmet criterion can make a whole process unusable
- **Affected requirements:** **AE-4**; the process-level WCAG criteria (3.3.4,
  3.3.7, 3.3.8, 2.4.1, 3.2.3)
- **Impact:** `Unknown / not directly evaluated at source-only scope`
- **Cause:** no process exists; complete-process evaluation is consumer-owned
- **Alternative / mitigation:** not applicable at source-only scope
- **Evidence:** none
- **Review trigger:** the first authorized pilot or consumer process
- **Expiry / re-assessment:** at the first consumer process
- **Claim effect:** **only AE-4 can support a conformance claim; none exists, so
  no conformance claim is possible.** Class: **Evidence gap** · Severity:
  **Significant**

## SSC-LIM-008 — No conformance claim exists or is valid

- **Affected artifact:** the whole family, and CDS generally
- **Scope:** all claim types
- **Affected user needs:** anyone who would rely on a CDS accessibility statement
  to make a procurement or adoption decision
- **Affected requirements:** the eight claim elements; DEC-S-044, DEC-S-050
- **Impact:** `Unknown / not directly evaluated at source-only scope`. Nobody may
  rely on a CDS accessibility statement, because none exists.
- **Cause:** no evidence at any level supports a claim, and **`CDS certified` is
  prohibited outright** — no certification programme exists
- **Alternative / mitigation:** not applicable — the honest absence of a claim is
  the correct state, not a gap to be closed by wording
- **Evidence:** not applicable
- **Review trigger:** any proposed claim of any of the four graded types
- **Expiry / re-assessment:** whenever a claim is proposed
- **Claim effect:** **absolute. No accessibility claim of any level is valid
  today, for anyone, including CDS.** Class: **Claim boundary** · Severity:
  **Minor** as a limitation record; **absolute** as a claim effect.

## SSC-LIM-009 — AE-3 absent

- **Affected artifact:** the whole family
- **Scope:** the declared support baseline A11Y-BL-001
- **Affected user needs:** assistive-technology users on every baseline
  environment
- **Affected requirements:** the Stable accessibility gate, requirement 3
- **Impact:** `Unknown / not directly evaluated at source-only scope`
- **Cause:** AE-3 requires a rendered artifact **and** an execution environment;
  neither exists
- **Alternative / mitigation:** not applicable at source-only scope. **AE-1 may
  never be substituted where AE-3 is required** (DEC-S-059, prohibited waiver 6).
- **Evidence:** none
- **Review trigger:** the first rendered representation; any A11Y-BL-001 change
- **Expiry / re-assessment:** before any Stable consideration
- **Claim effect:** **Stable is structurally unreachable.** Class: **Evidence
  gap** · Severity: **Significant**

## SSC-LIM-010 — AE-4 absent

- **Affected artifact:** the whole family
- **Scope:** any consumer product scope
- **Affected user needs:** all users of any future consuming product
- **Affected requirements:** conformance claims; the Stable gate, requirement 4
- **Impact:** `Unknown / not directly evaluated at source-only scope`
- **Cause:** AE-4 is the **consumer's** evidence for the consumer's declared
  scope and revision; no consumer exists
- **Alternative / mitigation:** not applicable at source-only scope
- **Evidence:** none
- **Review trigger:** the first authorized consumer integration
- **Expiry / re-assessment:** at the first consumer integration
- **Claim effect:** **only AE-4 supports a conformance claim; none is
  possible.** Class: **Evidence gap** · Severity: **Significant**

## SSC-LIM-011 — DE/EN comprehension and cultural suitability unvalidated

- **Affected artifact:** the DE/EN terminology mapping; all 25 values
- **Scope:** German and English display terminology
- **Affected user needs:** German-language and English-language readers,
  particularly where a softened or upgraded label would make an untrue statement
  read as true — the `supported → verifiziert` upgrade is the archetype
- **Affected requirements:** DEC-S-110, DEC-S-119; the DE/EN parity obligation;
  WCAG 3.1.2 material
- **Impact:** `Unknown / not directly evaluated at source-only scope`. Structural
  parity is machine-verified at **25/25**; **semantic equivalence and cultural
  suitability are not.**
- **Cause:** meaning equivalence is a human judgement. **Machine-checkable
  structure is not machine-checkable meaning**, and no automated semantic
  language comprehension was invented for this remediation.
- **Alternative / mitigation:** partial — the existing executor-produced
  localization parity review and the independent WP-016
  terminology/accessibility/content review cover meaning by human reading. Their
  cost: neither is user validation, and both are reviews of a contract rather
  than of a rendered label.
- **Evidence:** provisional AE-1 structural coverage (25 identifiers, 25 EN
  labels, 25 DE labels, 0 duplicates, 0 unauthorized, 0 missing); human reviews
  as above
- **Review trigger:** regression triggers T-04, T-05, T-11
- **Expiry / re-assessment:** at any terminology or localization change, and at
  the next Candidate-gate review
- **Claim effect:** **no claim that the DE and EN wordings are understood as
  intended.** Class: **Evidence gap** · Severity: **Significant**

## SSC-LIM-012 — Machine validation does not prove meaning quality or channel truthfulness

- **Affected artifact:** the validator's V4 status checks; the CDS-WP-016
  evidence runner
- **Scope:** all automated status evidence
- **Affected user needs:** everyone who would receive a status statement that is
  formally valid but substantively misleading
- **Affected requirements:** invariants 2, 6, 9; DEC-S-053 (an automated check is
  never sufficient); RISK-093
- **Impact:** `Unknown / not directly evaluated at source-only scope`. The checks
  prove the vocabulary's **shape** and the **enumerated** combinations, not that a
  real statement is truthful. A concrete instance: **hiding partiality is
  invariant 6, and the six normative review-required combinations do not
  enumerate it on its own** — the evidence case reaches it only because an axis
  also carries `unknown` (RR-6). A summary that hides `partial` evidence with no
  `unknown` axis present is **not detected** by the current machine rules.
- **Cause:** the rules are a faithful transcription of the six review-required
  combinations and eight fail-closed conditions. **No seventh combination and no
  ninth condition was invented** to close this, because inventing normative rules
  in an evidence runner would be a worse defect than the gap.
- **Alternative / mitigation:** human review of every review-required assertion
  and of every summary; the rationale requirement; the disclosure-priority rules
- **Evidence:** the coverage sentinels (6/6, 8/8) and their explicit boundary
  statements in the results artifact
- **Review trigger:** regression triggers T-06, T-07, T-08, T-15
- **Expiry / re-assessment:** at any change to the composition rules or the
  communication contract
- **Claim effect:** **no automated result may be presented as an accessibility or
  truthfulness pass.** Class: **Evidence gap** · Severity: **Significant**

## SSC-LIM-013 — Fixture coverage may miss unrepresented invalid states

- **Affected artifact:** the test-only statement fixture; the semantic-status
  token fixtures
- **Scope:** all negative coverage
- **Affected user needs:** everyone exposed to an invalid state nobody thought to
  model
- **Affected requirements:** the fail-closed discipline; RISK-094 (semantic
  fixture overfitting)
- **Impact:** `Unknown / not directly evaluated at source-only scope`. Passing
  cases prove the modelled invalid states are caught. They prove nothing about
  invalid states that were never modelled.
- **Cause:** fixtures are authored, and an author cannot enumerate what they did
  not think of. Executor-authored fixtures compound this (see SSC-LIM-015).
- **Alternative / mitigation:** partial — independent review of the case set is
  the counterweight, and it is exactly what is still pending
- **Evidence:** 32 statement cases, 6/6 review-required, 8/8 fail-closed, plus
  1 positive and 9 negative token fixtures
- **Review trigger:** any new invalid state discovered in review or in use;
  regression triggers T-06, T-07
- **Expiry / re-assessment:** at the fresh independent review, and at every
  composition-rule change
- **Claim effect:** **coverage may not be described as complete.** Class:
  **Evidence gap** · Severity: **Significant**

## SSC-LIM-014 — Single-environment technical validation

- **Affected artifact:** all machine evidence
- **Scope:** the execution environment of the evidence run
- **Affected user needs:** none directly
- **Affected requirements:** reproducibility; RISK-075
- **Impact:** `Unknown / not directly evaluated at source-only scope`. All
  evidence was produced on **one** platform (Windows 11, Python 3.13.15, the
  pinned `requirements-validator.lock` stack) in **one** session.
- **Cause:** no second execution environment was authorized or available
- **Alternative / mitigation:** strong — the runner is deterministic (verified
  byte-identical across two runs), dependencies are exactly pinned, digests are
  recorded, and the whole run is offline and re-executable by a reviewer
- **Evidence:** the results and digest artifacts; the deterministic double
  execution
- **Review trigger:** any dependency, Python, or platform change
- **Expiry / re-assessment:** at the fresh independent review, which should
  re-execute on its own environment
- **Claim effect:** **results are bound to the recorded environment.** Class:
  **Evidence gap** · Severity: **Minor**

## SSC-LIM-015 — Executor self-confirmation partially mitigated, not erased

- **Affected artifact:** the whole CDS-WP-016 remediation package
- **Scope:** implementation, fixtures, expectations, and evidence
- **Affected user needs:** everyone who would rely on evidence that was never
  genuinely checked by anyone else
- **Affected requirements:** DEC-S-045, DEC-S-103, DEC-S-121; evidence rule 10 —
  **evidence reviewed only by its own executor has not been reviewed**;
  RISK-078
- **Impact:** `Unknown / not directly evaluated at source-only scope`. **The same
  executor wrote the validator rule, the fixtures, the expected classifications,
  the runner, and the tests that check them.** Agreement between them is
  therefore weaker evidence than it looks.
- **Cause:** a single-executor work package
- **Alternative / mitigation:** partial. Mitigating factors: the rules are
  transcribed from documents the executor did not write and may not change; the
  WP-013/WP-015 baseline harness (24 cases) was left untouched as an independent
  regression sentinel; all 112 pre-existing test IDs still exist and pass;
  determinism and digests make the run externally reproducible. **None of this
  substitutes for an independent reviewer**, and one is required.
- **Evidence:** the preserved baseline sentinels; the deterministic re-execution
- **Review trigger:** immediately — this limitation is the reason the package is
  offered for review rather than for approval
- **Expiry / re-assessment:** **on completion of the fresh independent review**
- **Claim effect:** **the AE-1 evidence produced here is `provisional` and is not
  admitted AE-1.** Class: **Evidence gap** · Severity: **Significant**

## SSC-LIM-016 — Local execution availability not asserted for any baseline environment

- **Affected artifact:** the whole family; A11Y-BL-001
- **Scope:** every Required Tier-1 environment
- **Affected user needs:** all users who would be protected by AE-2 and AE-3
  evidence that cannot currently be produced
- **Affected requirements:** A11Y-BL-001 Tier-1 entries 1–12; RISK-051
- **Impact:** `Unknown / not directly evaluated at source-only scope`. No
  capacity-checked execution slot exists for Windows 11 × Edge × NVDA or
  Windows 11 × Firefox × NVDA, and **JAWS official requirements remain
  unretrievable** (S-12/S-13).
- **Cause:** no environment has been provisioned, no test tool has been selected,
  and none may be without explicit authorization
- **Alternative / mitigation:** none available today. **Missing capacity is a
  planning limit, never a conformance justification** (the policy is explicit).
  The honest response is a lower maturity, not a weaker standard.
- **Evidence:** recorded as an Execution Gap in the environment matrix
- **Review trigger:** any provisioning of a baseline environment; any
  A11Y-BL-001 change; regression trigger T-14
- **Expiry / re-assessment:** before any AE-2 or AE-3 attempt
- **Claim effect:** **no environment may be represented as supported.** Class:
  **Evidence gap** · Severity: **Significant**

---

## Summary

| Metric | Count |
| --- | --- |
| **Total limitations recorded** | **16** |
| **Critical** | **0** |
| **Significant** | **11** (001, 002, 004, 007, 009, 010, 011, 012, 013, 015, 016) |
| **Minor** | **5** (003, 005, 006, 008, 014) |
| Evidence gaps | **12** (001, 002, 004, 007, 009, 010, 011, 012, 013, 014, 015, 016) |
| Scope exclusions | **3** (003, 005, 006) |
| Claim boundaries | **1** (008) |
| Entries with an actual, evaluated user impact | **0** — all are `Unknown / not directly evaluated at source-only scope` |
| **Candidate-blocking under the normative severity rules** | **0** |
| **Stable-blocking** | **11** (every Significant entry) |
| Entries with **no** available alternative where a user-facing requirement is currently applicable | **0** — because **no user-facing requirement is currently applicable** to this artifact |

## Why Critical is zero — and what would change it

Under the normative scale, **Critical** means *a user group cannot complete a
process and no alternative exists*. That requires a process. This Candidate has
none: no interface, no page, no task, no user path.

**Zero Critical is therefore a statement about the artifact's scope, not a
statement about its quality.** It would change immediately if any of the
following became true, and each is a recorded regression trigger:

| # | Change | Effect |
| --- | --- | --- |
| 1 | A rendered or interactive representation exists (T-13) | 30 WCAG criteria become live and assessable; AE-2 and AE-3 become required; Critical limitations become possible for the first time. |
| 2 | A non-textual meaning carrier is introduced (T-09) | Colour-only and icon-only encoding become possible; 1.4.1 and 1.3.3 move from structurally prevented to must-be-tested. |
| 3 | A consumer integration begins | Composition, content, and process enter scope, and AE-4 obligations attach. |
| 4 | The premise that no user-facing artifact exists turns out to be wrong | **Every severity in this document is wrong** and must be re-derived. |

## What this document does not do

- It **grants no waiver.** Accessibility requirements for Stable or
  CDS-conformant scope **cannot** be waived through an ordinary exception
  (DEC-S-059).
- It **promotes nothing.** Candidate remains **No**, maturity **Experimental**,
  approval **Unapproved**, admitted evidence level **AE-0**.
- It **approves nothing.** Only the Human Maintainer may approve a limitation
  with normative effect, and none of these sixteen is approved.
- It **is not a passed test**, and no entry may be netted against a strength.

## Related documents

- [Accessibility Limitations and Exception Policy](ACCESSIBILITY_LIMITATIONS_AND_EXCEPTION_POLICY.md) — normative
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md) — normative
- [Semantic Status Candidate WCAG Applicability Mapping](SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md)
- [Semantic Status Candidate Accessibility Regression Plan](SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md)
- [Semantic Status Candidate AE-1 Evidence Record](../operations/SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md)
- [Semantic Status Candidate Evidence Requirements Matrix](../operations/SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md)
