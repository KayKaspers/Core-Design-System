# CDS-WP-016 — A11Y-BL-001 Baseline Freshness Review (Trigger 1)

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Accessibility Gate Remediation
- **Review date:** 2026-08-17
- **Baseline under review:** **A11Y-BL-001**
  ([Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md)),
  declared 2026-07-16 and committed with CDS-WP-010
  (`abe84b6b7267b8b9c5f96609e7c9d1ad1e68bc0a`)
- **Governing policy:**
  [Accessibility Baseline Maintenance Policy](../governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md)
  (DEC-S-070)
- **CDS revision at review:** `7ac8a9e7be021a05e517adda64751920a5eff247`
- **Status:** **Review record — NOT evidence, NOT a support claim, NOT a
  conformance statement.**

## Trigger

Maintenance-policy review trigger **1**: *before the first Candidate with an
accessibility obligation*. The Semantic Status Foundation is the first planned
CDS Candidate and is accessibility-relevant, so the baseline must be reviewed
before its Candidate accessibility gate can be assessed.

Triggers 2 (before Stable), 3 (before pilot evidence), and 4 (before a claim) do
**not** apply: no Stable transition, no pilot, and no claim exists or is
proposed.

## What this review is and is not

- It determines **one freshness state** for A11Y-BL-001 and records the primary
  sources it was determined from.
- It **produces no accessibility evidence**, tests nothing, installs nothing,
  and selects no tool.
- It **creates no support claim.** Confirming that a product family is still
  supported by its vendor is not a statement that CDS works in it. **Every CDS
  artifact remains AE-0.**
- It changes **no** baseline composition, tier, or declared scope. Such a change
  would be Elevated and requires Nova review and Human-Maintainer approval.

## Method

Each Required (Tier-1) product family named by A11Y-BL-001, and the accessibility
standard the target rests on, was re-verified against its **official primary
source** on the review date and compared with the facts recorded in the
[Accessibility Baseline Source Register](../research/ACCESSIBILITY_BASELINE_SOURCE_REGISTER.md)
on 2026-07-16.

Only official standards bodies and vendor lifecycle/product pages were consulted.
No benchmark material, no design-system comparison, no third-party aggregator,
and no community source was used for a determination. Sources are named so the
review is independently repeatable.

## Primary-source verification

| Register ref | Family / standard | Recorded 2026-07-16 | Verified 2026-08-17 (official source) | Drift |
| --- | --- | --- | --- | --- |
| — | **WCAG 2.2** (the accessibility target, DEC-S-049) | W3C Recommendation, 2024-12-12 | **W3C Recommendation, 12 December 2024**; no superseding Recommendation; previous version WCAG 2.1 — `https://www.w3.org/TR/WCAG22/` | **None** |
| S-03 | **Windows 11** (Tier-1 desktop OS) | Modern Lifecycle; in support 24H2, 25H2, 26H1; 23H2 ended | **Modern Lifecycle; in support: 26H1 (to 2028-03-15 PT), 25H2 (to 2027-10-13 PT), 24H2 (to 2026-10-14 PT); 23H2 ended 2025-11-12 PT** — `https://learn.microsoft.com/en-us/lifecycle/products/windows-11-home-and-pro` | **None** (see observation OBS-BFR-001) |
| S-02 | **Microsoft Edge** (Tier-1 Chromium family) | Stable major cadence moving to 2 weeks from v152; Extended Stable 8 weeks; trigger = equivalent Chromium release; stable ≈ v150–151 | **Identical**: 2-week Stable cadence from v152, Extended Stable on an 8-week cycle; latest released Stable **151.0.4129.59 (2026-07-31)**; v152 Stable planned for the week of 2026-08-27 — `https://learn.microsoft.com/en-us/deployedge/microsoft-edge-release-schedule` | **None** |
| S-09 | **Chrome** (Chromium corroboration) | Stable major every 4 weeks; Extended Stable every 8 weeks | Chromium-family cadence unchanged; Edge remains the officially-sourced Tier-1 representative and shares the engine | **None** |
| S-06 | **Firefox / Firefox ESR** (Tier-1 Gecko family) | Rapid release every 4 weeks; ESR annual major releases with regular security updates | **Identical**: "stable releases every four weeks"; ESR "long-term stability, regular security updates, and annual major releases" — `https://www.firefox.com/en-US/browsers/enterprise/` | **None** |
| S-04 | **NVDA** (Tier-1 no-cost screen reader) | Free, open source; 64-bit Windows 10 / Windows 11 and Windows Server 2016+ | **Identical**: 100% free, open source; 64-bit Windows 10, Windows 11 and Server 2016+; ARM64 on Windows 11 only; recommended Windows 11 / Server 2022–2025 — `https://www.nvaccess.org/about-nvda/` | **None for the CDS baseline** (see observation OBS-BFR-002) |

Tier-2 and Tier-3 entries were **not** re-verified: they are not Required for
this Candidate scope, and the previously recorded gaps stand unchanged —
Safari/VoiceOver and JAWS remain unverified, and the JAWS official requirements
were **not retrievable** (S-12/S-13, RISK-051). Nothing in this review makes them
available, and no Tier-2/Tier-3 environment is represented as supported.

## Trigger-by-trigger assessment

| # | Maintenance-policy trigger | Fired? | Assessment |
| --- | --- | --- | --- |
| 1 | Before the first Candidate with an accessibility obligation | **Yes** | This review is that re-verification. It is complete, not pending. |
| 2 | Before Stable | No | No Stable transition exists or is proposed; Stable stays structurally unreachable. |
| 3 | Before pilot evidence | No | The CoreOps pilot is inactive and unauthorized. |
| 4 | Before an accessibility or conformance claim | No | No claim exists, is proposed, or would be valid. |
| 5 | Major version release of a baseline OS, browser, renderer, or AT | **Yes** | Edge Stable 151 (2026-07-31) and Firefox 153 (2026-07-21) are major releases after the baseline date. A11Y-BL-001 uses a **rolling family policy**, which the maintenance policy explicitly permits; the family entries ("a currently supported Windows 11 version", "Chromium stable", "Firefox release or ESR") still resolve. The policy sets **affected evidence** to `Review due` — and **the affected evidence set is empty**, because no accessibility evidence exists at any level (every artifact is AE-0). Nothing was carried forward and nothing was revalidated, because nothing exists to revalidate. |
| 6 | Support-end or lifecycle change of a baseline product | **No** | No baseline product left vendor support between 2026-07-16 and 2026-08-17. Windows 11 24H2, 25H2, and 26H1 are all still in support. The Edge move to a 2-week Stable cadence was **already recorded on 2026-07-16** (S-02) and is therefore not a change since the baseline. |
| 7 | Critical or High accessibility regression, or a compatibility warning | No | No accessibility evidence and no accessibility defect exists, so no regression can have occurred. |
| 8 | Declared-scope or Product-Profile change altering environments | No | The declared scope (Web Product UI, Web Documentation; interactive desktop web; DE and EN) is unchanged. No Product Profile exists. |
| 9 | At least every six months since the last baseline review | **No** | Last baseline review 2026-07-16; this review 2026-08-17 — **32 days**, well inside the six-month maximum review gap. |

## Freshness determination

Applying the five normative freshness states:

- **`Stale`** would require the maximum review gap to have been passed, or a
  Major-version/support-end change to have occurred **without re-verification**.
  The gap is 32 days, and the Major-version releases have now been re-verified.
  Not `Stale`.
- **`Review due`** would mean a trigger has fired and **re-verification is
  pending**. Triggers 1 and 5 fired; this review *is* the re-verification and it
  is complete. Not `Review due`.
- **`Superseded`** would require a newer A11Y-BL revision. None exists.
- **`Unknown`** would mean freshness cannot be established. Every Required family
  and the standard itself were verified against official primary sources on the
  review date. Not `Unknown`.
- **`Current`** — "reviewed against the present environment reality; within the
  review window" — is what actually happened.

> ## **A11Y-BL-001 freshness state: `Current`** (as of 2026-08-17)

This determination is bound to **this date** and **these sources**. It decays: it
must be re-determined at the next trigger, and in any case within six months
(by **2027-02-17**).

## Observations

*(Non-blocking. Neither is a defect in A11Y-BL-001, and neither changes the
freshness determination.)*

- **OBS-BFR-001 — end-date rendering convention.** The source register renders
  the Windows 11 servicing end dates one calendar day earlier than the vendor
  page's Pacific-Time retirement timestamps (register: 24H2 "to 2026-10-13";
  vendor: retirement 2026-10-14 06:59:59 PT). This is a display-convention
  difference about the same lifecycle boundary, **not** a lifecycle change and
  **not** a support-end event. The source register is a read-only research file
  outside this work package's Allowed Files and is deliberately **not** edited
  here; the observation is preserved for a later authorized documentation pass.
- **OBS-BFR-002 — NVDA platform-support note.** The NVDA page now states that
  Windows 10 and Windows Server versions older than 2022 are no longer under
  active support. **No CDS Required entry is affected:** the Tier-1 CDS desktop
  OS is Windows 11 only, and no Windows Server environment is in any CDS tier.
  Recorded so a reviewer can confirm the assessment rather than infer it.

## Forward-looking review trigger

**Windows 11 version 24H2 reaches its servicing end on 2026-10-14 (PT).** That is
a trigger-6 event on a Required Tier-1 family. When it occurs, the family entry
rolls to a currently supported version and this freshness determination must be
re-made. Recording the date is **not** a change to A11Y-BL-001 and creates no
obligation on the vendor's schedule.

## What did not change

- No baseline composition, tier, family, or declared-scope change was made or
  proposed. Such a change is **Elevated** and needs Nova review and
  Human-Maintainer approval.
- No environment is claimed as supported. **A listed environment is not a
  supported environment.**
- The execution-availability gap stands: **no local execution availability is
  asserted for any listed environment** (RISK-051). A `Current` baseline does not
  create an execution slot, and AE-2/AE-3 remain unproducible until real,
  capacity-checked environments exist.
- **A baseline is not evidence** (DEC-S-065). `Current` means the test contract
  is up to date, never that anything passed. **Every CDS artifact remains AE-0.**

## Related documents

- [Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Baseline Maintenance Policy](../governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md)
- [Accessibility Environment and Scope Matrix](../governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
- [Semantic Status Candidate Support Baseline Plan](../governance/SEMANTIC_STATUS_CANDIDATE_SUPPORT_BASELINE_PLAN.md)
- [Semantic Status Candidate AE-1 Evidence Record](../operations/SEMANTIC_STATUS_CANDIDATE_AE1_EVIDENCE_RECORD.md)
- [Accessibility Baseline Source Register](../research/ACCESSIBILITY_BASELINE_SOURCE_REGISTER.md) — research, non-normative
