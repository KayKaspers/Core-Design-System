# Semantic Status Candidate Dossier

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-015 — Semantic Status Foundation Source Set and
  Candidate Evidence
- **Date:** 2026-07-18
- **Status: Draft – Candidate gate incomplete.** This dossier follows the
  [Elevated Change Dossier](ELEVATED_CHANGE_DOSSIER_TEMPLATE.md) discipline
  for the planned first Candidate. **A populated dossier is not an approval**
  (DEC-S-122): the Candidate decision requires independent evidence review,
  Nova review, and Human-Maintainer approval — all open.
  **Candidate Status = Not Candidate.**

## Target artifact

The **Semantic Status Foundation**: the normative contract family (CDS-WP-014)
plus the machine-readable Semantic Source Set **`semantic/status`**
(CDS-WP-015) — the first planned CDS design Candidate (DEC-S-113).

## Scope

Five axes · 25 axis values · ten invariants · combination/conflict rules ·
communication/accessibility contract · token role contract · DE/EN semantic
parity · the `semantic/status` source set with manifest and resolver.

## Exclusions

Visual values of any kind, UI components, CoreOps/consumer integration,
Product Profiles, mobile/non-web implementations, Stable status, and every
conformance/adoption/accessibility claim. Scope expansion is a NO-GO trigger
(RISK-089).

## Normative sources

[Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) ·
[Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) ·
[Composition Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) ·
[Communication Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md) ·
[Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md) ·
[Terminology DE/EN](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md)

## Machine-readable source set, manifest, and resolver

[semantic-status.tokens.json](../../tokens/semantic/status/semantic-status.tokens.json)
(25 tokens, 5 axes, Experimental, Unapproved) ·
[semantic-status.source-set.json](../../tokens/semantic/status/semantic-status.source-set.json) ·
[semantic-status.resolver.json](../../tokens/semantic/status/semantic-status.resolver.json)
— identity `semantic/status`, revision `semantic-status-rev-0001`, local-only,
no Product-Profile extension points.

## Validation evidence

- WP-013 clean re-execution on the committed WP-014 revision: 71/71 tests,
  **15/15 matches, worktree clean**
  ([review](../reviews/WP013_VALIDATOR_EVIDENCE_REEXECUTION_REVIEW.md)).
- Full 24-case harness: **24/24 expected/actual matches** (9 new status
  cases; [results](../../artifacts/validation/wp015-fixture-results.json)).
- Source-set execution: V1–V3 Pass, V4 objective status checks passed, exit 0
  ([review](../reviews/SEMANTIC_STATUS_SOURCE_SET_EXECUTION_REVIEW.md)).
- 103/103 unit tests; RFC 8785 + SHA-256 digests for source set (3) and
  fixtures (23).

## Accessibility and content evidence

[Accessibility and Content Review](../reviews/SEMANTIC_STATUS_ACCESSIBILITY_AND_CONTENT_REVIEW.md)
— executor-produced **contract** review; no user research, no AT execution,
no WCAG claim. *(At the time of that review every artifact was AE-0. The
source/contract family has since reached admitted **AE-1** — see the additive
section [AE-1 Admission and Post-Review Gate Reconciliation](#ae-1-admission-and-post-review-gate-reconciliation-additive-2026-08-17).)*

## Localization evidence

[Localization Parity Review](../reviews/SEMANTIC_STATUS_LOCALIZATION_PARITY_REVIEW.md)
— 25/25 DE, 25/25 EN, 0 missing rows; executor-produced; comprehension
unvalidated.

## Known limitations

Bounded DTCG V2 coverage (DEC-S-098) · V4 validates the vocabulary shape, not
meaning quality or channel truthfulness (RISK-093) · fixture coverage may miss
unrepresented invalid states (RISK-094) · single-environment execution
(RISK-075) · executor self-confirmation across implementation, fixtures, and
reviews (RISK-078) · no consumer evidence yet.

## Defects

None known and open against the contract family or the source set at dossier
time. Any Blocking/High defect found in review re-opens this dossier.

## Compatibility

First introduction of the `semantic/status` source set — no consumer depends
on it; no compatibility promise exists (pre-1.0, Experimental). The 25 value
IDs and the `status.<axis>.<value>` paths become compatibility-relevant only
at Candidate; renames are migration events (DEC-S-082, RISK-092).

## Migration

Not applicable (first introduction; nothing migrates). Future path/ID changes
require migration references per DEC-S-082.

## Product-Profile boundary

No approved extension points exist (`approvedExtensionPoints: []`); no
Product Profile may reference or remap the status vocabulary (DEC-S-112,
DEC-S-124).

## Consumer boundary

No consumer integration exists or is authorized; the Experimental source set
must not be consumed, distributed, or represented as approved before the
Candidate gate (RISK-097, DEC-S-124). CoreOps pilot inactive.

## Evidence Reviewer

**Open — not yet authorized.** Must be Nova or a separately authorized
reviewer; never the executor (DEC-S-045, DEC-S-121).

## Nova review

**Open** — Candidate-gate review pending.

## Human-Maintainer approval

**Open** — final maturity authority (DEC-S-036).

## Candidate decision

### Gate state after CDS-WP-015

Present: WP-014 committed · machine-readable source set implemented ·
validator harness executed (24/24) · executor-produced structural evidence ·
executor-produced accessibility/content review · executor-produced DE/EN
parity review.

Open: independent review of the WP-013 and WP-015 evidence · authorized
independent Evidence Reviewer · Nova Candidate-gate review · Human-Maintainer
Candidate approval.

### Decision

**Not Candidate.** The decision field stays empty until every open gate
closes; unclear readiness resolves as NO-GO (DEC-S-048).

## CDS-WP-016 Independent Evidence Review (additive)

*(Added by CDS-WP-016. This section is additive; the dossier status remains
**Draft – Candidate gate incomplete** and **Candidate = No**. The reviewer
awards nothing.)*

### Evidence Reviewer identity

Claude Opus 4.8 (`claude-opus-4-8`), a fresh session with no inherited executor
context, authorized by the Human Maintainer as a **separate** Evidence Reviewer
(reviewer ≠ executor; DEC-S-045, DEC-S-103, DEC-S-121).

### Review scope and revision

Independent review of the committed WP-013 validator evidence and WP-015
semantic-status evidence: clean-tree re-execution, digest comparison,
source/contract traceability, terminology parity, and accessibility/content
contract review. **Review revision:** the committed HEAD containing CDS-WP-015,
reviewed on a **clean** working tree.

### Independent re-execution

Fresh venv outside the repository, exact `requirements-validator.lock` pins
(7/7), Python 3.12.10, offline after install:

- **103/103** unit tests; **24/24** cases with **24/24** expected/actual
  matches; **0** mismatches, **0** execution errors; result-schema validation
  passed.
- Source set: V1–V3 Pass, V4 Not assessed (objective status checks passed, 0
  status errors), block `none` — not Fail, not Blocked.
- **23** fixture content digests + **1** undigestible, and **3** source content
  digests — **all identical** to the committed WP-015 evidence.
- Schema `$id` unchanged; case-schema change additive; CLI unchanged;
  `VAL-CASE-001…015` byte-identical; `VAL-CASE-016…024` schema-valid; no gate
  evasion.

Evidence: [wp016-independent-fixture-results.json](../../artifacts/validation/wp016-independent-fixture-results.json) ·
[wp016-independent-fixture-digests.json](../../artifacts/validation/wp016-independent-fixture-digests.json) ·
[wp016-independent-source-results.json](../../artifacts/validation/wp016-independent-source-results.json) ·
[wp016-independent-source-digests.json](../../artifacts/validation/wp016-independent-source-digests.json).
Reviews: [Re-Execution](../reviews/WP016_INDEPENDENT_REEXECUTION_REVIEW.md) ·
[Traceability](../reviews/WP016_SOURCE_CONTRACT_TRACEABILITY_REVIEW.md) ·
[Terminology/Accessibility/Content](../reviews/WP016_TERMINOLOGY_ACCESSIBILITY_CONTENT_REVIEW.md).

### Findings

**0 Blocking · 0 High · 0 Medium · 0 Low · 3 Observations** — provenance stamp
of the source-set evidence is pre-commit (WP016-OBS-001), source-set V4 label
is "Not assessed" vs the "Pass with limitations" prose (WP016-OBS-002), and the
resolver `outputIdentity` wording is imprecise (WP016-OBS-003). None weakens the
Candidate scope or threatens truth, accessibility, or evidence identity. Detail:
[Candidate Gate Recommendation](../reviews/WP016_CANDIDATE_GATE_RECOMMENDATION.md).

### Independent review outcome and Candidate recommendation

Independent review **PASS**; **Candidate Recommendation: GO** in the strict
review sense — the independent review is clean and Nova may open its
Candidate-gate review. GO is **not** a Candidate award and asserts no
Candidate, Stable, approved, promoted, or conformant status.

### Still-open gates

- **Evidence Reviewer:** authorized and complete for this run (supersedes the
  "Open" note above for the WP-016 review only).
- **Nova review:** **open** — Candidate-gate review and promotion recommendation.
- **Human-Maintainer approval:** **open** — final maturity authority (DEC-S-036).

**Candidate Status = Not Candidate.** The decision field stays empty until the
Nova and Human-Maintainer gates close.

## Candidate Accessibility Gate Remediation (additive, CDS-WP-016, 2026-08-17)

*(Added by the CDS-WP-016 Candidate Accessibility Gate Remediation — internal
rework of CDS-WP-016, **not** a new work package. This section is additive; the
dossier status remains **Draft – Candidate gate incomplete** and **Candidate =
No**. The executor awards nothing.)*

### What changed since the section above

The independent evidence review recorded above returned **PASS / GO** in its
declared narrow sense, and that finding **stands and is not revoked**. Nova then
opened its **Candidate Maturity Review** and returned **NO-GO**: the normative
**Candidate accessibility gate** was unmet. A read-only gap assessment confirmed
it — **9 / 9 requirements not demonstrated as satisfied** — and the Human
Maintainer authorized this remediation on 2026-08-17.

Detail: [Candidate Accessibility Gate Addendum](../reviews/WP016_CANDIDATE_ACCESSIBILITY_GATE_ADDENDUM.md).

### Gate table

| # | Gate requirement | Pre-remediation state | Remediation artifact | Executor state | Independent-review state | Authority state | Satisfied for Candidate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **WCAG applicability mapping** | Absent (GAP-B-05) — only the global CDS matrix existed, unscoped to this artifact | [Candidate WCAG Applicability Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md) — 56 rows: 5 direct, 30 representation-triggered, 20 consumer-owned, 1 historical not-applicable | Complete | **Pending** | Executor-produced; no authority | **PENDING** |
| 2 | **Responsibility mapping** | Absent (GAP-B-05) | [Candidate Accessibility Responsibility Mapping](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_RESPONSIBILITY_MAPPING.md) — 13 subjects: 5 CDS, 8 Shared, 0 Consumer-only | Complete | **Pending** | Executor-produced; no authority | **PENDING** |
| 3 | **Known accessibility requirements** | Partially absent (GAP-H-02) — 25 per-value Candidate evidence requirements unmapped | [Candidate Evidence Requirements Matrix](SEMANTIC_STATUS_CANDIDATE_EVIDENCE_REQUIREMENTS_MATRIX.md) — **25/25 mapped, 0 UNMAPPED**, 22 `COVERED` + 3 `COVERED_WITH_LIMITATION` | Complete | **Pending** | Executor-produced; no authority. `COVERED_WITH_LIMITATION` is **not automatically Candidate-compatible** — the reviewer judges that. | **PENDING** |
| 4 | **AE-1** | Absent (GAP-B-02) — no AE-1 and no instantiated evidence record | [Provisional AE-1 Evidence Record](SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md) · [results](../../artifacts/validation/wp016-candidate-accessibility-remediation-results.json) · [digests](../../artifacts/validation/wp016-candidate-accessibility-remediation-digests.json) | Complete — machine result `Pass with limitations`; 25/25 descriptions, 25/25 DE/EN, 25/25 value requirements, 6/6 review-required, 8/8 fail-closed, 0 execution errors | **PENDING INDEPENDENT REVIEW** | **Provisional AE-1 candidate only. NOT admitted AE-1. Admitted level remains AE-0.** | **PENDING INDEPENDENT REVIEW** |
| 5 | **AE-2, or a reasoned evidence plan** | Absent (GAP-B-06) | [Candidate AE-2 Evidence Plan](../governance/SEMANTIC_STATUS_CANDIDATE_AE2_EVIDENCE_PLAN.md) — the gate's "reasoned plan" alternative; AE-2 execution is not meaningful against an artifact with no interactive surface and was **not** fabricated | Complete | **Pending** | Executor-produced; a plan is not evidence | **PENDING** |
| 6 | **Known limitations** | Insufficient (GAP-M-04) — dossier limitations did not meet the limitation discipline | [Candidate Accessibility Limitations](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md) — 16 entries with the normative 15 fields: **0 Critical · 11 Significant · 5 Minor** | Complete | **Pending** | Executor-produced; **only the Human Maintainer may approve a limitation with normative effect** — none is approved | **PENDING** |
| 7 | **Support baseline plan** | Absent (GAP-B-03) — no plan, Trigger-1 freshness review never run | [Candidate Support Baseline Plan](../governance/SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md) + [A11Y Baseline Freshness Review](../reviews/WP016_A11Y_BASELINE_FRESHNESS_REVIEW.md) — freshness **`Current`** (2026-08-17, official primary sources); 1 Tier-1 entry applicable now, 12 representation-triggered, 0 not applicable | Complete | **Pending** | Executor-produced; **a baseline is not evidence** | **PENDING** |
| 8 | **Regression plan** | Absent (GAP-B-04) | [Candidate Accessibility Regression Plan](../governance/SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md) — 15 triggers (13 assessed, 2 traceable splits, 0 losses) | Complete | **Pending** | Executor-produced; **documentation is not mitigation** | **PENDING** |
| 9 | **Human-Maintainer approval after Nova review** | Open | — none possible — | **Not addressable by an executor** | Not applicable | **Nova review OPEN · Human-Maintainer approval OPEN** | **NO / OPEN** |

### Gate arithmetic

| Outcome | Count |
| --- | --- |
| Requirements with a remediation artifact | **8 of 9** |
| Requirements **satisfied for Candidate** | **0 of 9** |
| `PENDING` (artifact exists, independent review outstanding) | **8** |
| **`NO / OPEN`** | **1** (requirement 9) |

**The dossier therefore remains incomplete, by construction.** Eight requirements
wait on a review that has not happened; the ninth waits on an authority the
executor does not hold and cannot simulate.

### Supporting decisions and boundaries

- **DEC-S-125** clarifies that Channel Accessibility Profiles gate **channel
  artifacts**, not channel-independent Layer-3 semantic sources (GAP-B-07,
  resolved by Nova and accepted by the Human Maintainer). It **grants no
  Candidate status and waives no accessibility requirement**; DEC-S-058 and
  DEC-S-029 remain in force, and **evidence transfers in neither direction**.
- **Text-first structural validation** is now operational at the source:
  `CDS-V4-STATUS-DESCRIPTION` fails closed on a missing, whitespace-only, or
  non-string `$description` (GAP-M-01, DEC-S-111). It proves a textual
  description **exists** — never comprehension, UI accessibility,
  assistive-technology behaviour, channel accessibility, or conformance.
- **DE/EN structural coverage** is machine-verified at **25/25** (GAP-M-02).
  **Machine-checkable structure is not machine-checkable meaning**; semantic
  equivalence remains a human judgement (SSC-LIM-011).
- The **WP-013/WP-015 24-case harness is unchanged** and still returns
  **24/24/0/0, exit 0** — retained as an independent regression sentinel
  (DEC-S-120). All **112** pre-existing validator test IDs and all **39**
  pre-existing targeted test IDs still exist and pass.
- The three WP-016 observations (**WP016-OBS-001, -002, -003**) are **preserved
  and unresolved**, as is the low-severity channel-profiles wording
  inconsistency (**GAP-L-01**), which is deliberately **not** repaired here.

### Candidate decision after remediation

> **Not Candidate.**
>
> Candidate = **No** · Maturity = **Experimental** · Approval = **Unapproved** ·
> Admitted accessibility evidence level = **AE-0** · Claims = **none** · Pilot =
> **inactive** · Publication = **Private Development** · CDS-WP-017 = **not
> activated**.
>
> The remediation makes the package **reviewable**. It does not make it
> **approved**. The decision field stays empty until the fresh independent
> review, the Nova gate, and the Human-Maintainer gate all close, and unclear
> readiness resolves as **NO-GO**, never "go with notes" (DEC-S-048).

*The block above records the state **at the close of the remediation**, before the
fresh independent reviews and before the AE-1 admission. For the current state, see
the additive section below; it supersedes the `AE-0` line above for present-day
reading. Candidate is unchanged at **No**.*

## AE-1 Admission and Post-Review Gate Reconciliation (additive, 2026-08-17)

*Additive current-state section. Every section above is preserved as written and
remains the record of what was true when it was written.*

### What closed since the remediation

| Step | Result |
| --- | --- |
| Fresh independent **remediation implementation** review | **PASS WITH NOTES** |
| Fresh independent **clean-HEAD Evidence 002** review | **PASS** |
| Evidence 002 (`AE1-CDS-WP016-SEMSTATUS-002`) | **integrated** at `43a512892e148fc53a5f5bee522ef6c30d848f19` |
| F-003 — revision binding and independent evidence review | **SATISFIED** |
| GAP-H-02 | **CLOSED BY EVIDENCE** |
| Nova AE-1 admission recommendation | **GO** |
| **Human-Maintainer AE-1 admission** | **APPROVED / ADMITTED**, 2026-08-17 |

Provenance for the two reviews:
[Review Provenance Record](../reviews/WP016_ACCESSIBILITY_REMEDIATION_REVIEW_PROVENANCE.md).
Admission authority and scope:
[Semantic Status AE-1 Admission Record](../governance/SEMANTIC_STATUS_AE1_ADMISSION_RECORD.md).

### Current evidence state

| Item | Value |
| --- | --- |
| Admitted evidence level | **AE-1** |
| Admitted evidence ID | `AE1-CDS-WP016-SEMSTATUS-002` |
| Evidence type | Structural and Automated Evidence |
| Evidence scope | **channel-independent source/contract only** |
| Source revision | `semantic-status-rev-0001` |
| Evidenced implementation revision | `e6cb6fae63b1548ce4dabb7f5548116e4c61d622` |
| Evidence result | Pass with limitations |
| AE-2 / AE-3 / AE-4 | **none** |

### Current Candidate accessibility gate state

| # | Requirement | Current state |
| --- | --- | --- |
| 1 | WCAG applicability mapping | **SATISFIED for the declared source scope** |
| 2 | Responsibility mapping | **SATISFIED** |
| 3 | Known accessibility requirements | **SATISFIED** — 25/25 mapped; GAP-H-02 closed |
| 4 | AE-1 | **SATISFIED** — `AE1-CDS-WP016-SEMSTATUS-002` **admitted** |
| 5 | Relevant AE-2 evidence **or** a reasoned plan | **SATISFIED BY REASONED PLAN** — no AE-2 execution fabricated |
| 6 | Known limitations | **SATISFIED as a documentation requirement** — 16 recorded: 0 Critical · 11 Significant · 5 Minor; none approved as an exception; no waiver |
| 7 | Support baseline plan | **SATISFIED** — A11Y-BL-001, freshness `Current` at review |
| 8 | Regression plan | **SATISFIED** — 15 triggers |
| 9 | **Human-Maintainer Candidate approval after Nova review** | **OPEN** |

**Arithmetic: 8 / 9 currently supported or satisfied · 1 / 9 authority gate open.**

This dossier does **not** make the final Candidate judgement. The next authority step
is the **Nova post-admission Candidate Maturity Re-Review**; only if that returns GO
does a separate Human-Maintainer Candidate decision follow.

### Candidate decision after admission

> **Still not Candidate.**
>
> Candidate = **No** · Maturity = **Experimental** · Approval = **Unapproved** ·
> Admitted accessibility evidence level = **AE-1, source scope only** · Claims =
> **none** · Pilot = **inactive** · Publication = **Private Development** ·
> CDS-WP-017 = **not activated**.
>
> An AE-1 admission is not a Candidate award. Evidence is not authority.

## Candidate Finalization Governance Rework (additive, CDS-WP-016, 2026-08-18)

*Additive current-state section. Every section above is preserved as written and
remains the record of what was true when it was written.*

A read-only Candidate Finalization Bootstrap Assessment found that the remaining
gate — element 9 — could not be reached without resolving a circular dependency:
a Candidate revision must declare `Candidate`/`Approved` metadata and a **new**
source revision, but that new revision invalidates the AE-1 admitted for
`semantic-status-rev-0001`. On Human-Maintainer authorization, **DEC-S-126** now
defines the transition. **Nothing in this dossier is thereby satisfied, and no
gate state above changes.**

### What DEC-S-126 changes for this Candidate

| Item | State |
| --- | --- |
| Proposed Candidate Revision | A named, **non-authoritative** state. Target metadata in its bytes grants nothing. |
| Reserved Candidate source revision | `semantic-status-rev-0002-candidate` — **authorized and reserved, not created**. |
| Current authoritative source revision | **`semantic-status-rev-0001`** — unchanged. |
| Admitted `AE1-CDS-WP016-SEMSTATUS-002` | Bound to `semantic-status-rev-0001`. It **does not transfer** to the future Candidate revision. |
| Evidence for the Candidate revision | A **fresh** execution, a **fresh** independent review, and a **fresh** Human-Maintainer AE-1 admission are required — regression trigger **T-12 is not waived**. |
| Pre-commit evidence | Permitted only under **exact-byte binding**; any byte drift in the evidenced scope invalidates it, with no "small fix" exemption. |
| Candidate approval instrument | An instance of the [Candidate Approval Record Template](CANDIDATE_APPROVAL_RECORD_TEMPLATE.md). **No instance exists.** |
| Effectivity | The **Human-Maintainer exact-byte Promotion Commit**, not the approval and not a validator pass. |

### Gate state after the rework

**Unchanged: 8 / 9 currently supported or satisfied · 1 / 9 authority gate open.**

Element 4 (AE-1) remains satisfied **for `semantic-status-rev-0001` only**.
Element 9 remains **OPEN**. The rework produced no evidence, admitted no evidence,
and granted no approval; it defined only the sequence by which the remaining gate
may later be closed.

### Candidate decision after the governance rework

> **Still not Candidate.**
>
> Candidate = **No** · Maturity = **Experimental** · Approval = **Unapproved** ·
> Source revision = **`semantic-status-rev-0001`** · Admitted accessibility
> evidence level = **AE-1, source scope only** · Claims = **none** · Pilot =
> **inactive** · Publication = **Private Development** · CDS-WP-017 = **not
> activated**.
>
> A governance transition model is not a transition. Preparing the route to a
> gate is not passing it.
