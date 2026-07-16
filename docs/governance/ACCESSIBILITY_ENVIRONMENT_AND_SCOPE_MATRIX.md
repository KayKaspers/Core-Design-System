# Accessibility Environment and Scope Matrix

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy
- **Baseline:** A11Y-BL-001
- **Date:** 2026-07-16
- **Status:** **Normative** for the environment entries of A11Y-BL-001, **pending
  Human-Maintainer commit**. Lists the environments future evidence targets. It is
  **not** evidence and asserts **no** support.

## How to read this matrix

Each row is one testable environment combination with a stable ID (`A11Y-ENV-###`,
contiguous, no gaps, no duplicates). Fields: Tier · OS family · Browser/renderer
family · Assistive-technology family · Input method · Language scope · Channel
scope · Intended evidence level · Requirement (**Required / Conditional /
Deferred**) · Trigger · Local execution availability · Known gap · Claim boundary ·
Selection rationale · Official sources.

**Requirement mapping to tiers:** Tier 1 → Required · Tier 2 → Conditional ·
Tier 3 → Deferred. "Conditional/Deferred" means *not mandatory until its trigger
fires* — never *supported*.

**Local execution availability is `Not asserted` for every row** — no local
hardware/software availability is invented (RISK-051). It must be established,
capacity-checked, before the intended evidence level can be produced.

## Register scope

- Environment ID range: **A11Y-ENV-001 … A11Y-ENV-014**
- Count: **14** — Required **6**, Conditional **4**, Deferred **4**.

---

## Tier 1 — Required (A11Y-ENV-001 … 006)

### A11Y-ENV-001 — Windows 11 · Chromium (Edge) · NVDA
- **Tier:** 1 · **Requirement:** Required
- **OS family:** Windows 11 (supported version) · **Browser:** Chromium (Edge; Chrome same engine) · **AT:** NVDA · **Input:** keyboard + pointer
- **Language scope:** DE, EN · **Channel:** Web Product UI, Web Documentation
- **Intended evidence level:** AE-2 + AE-3
- **Trigger:** always (interactive desktop-web scope)
- **Local execution availability:** Not asserted (Execution Gap until a slot exists)
- **Known gap:** none beyond availability
- **Claim boundary:** listing ≠ support; no claim until AE-3 evidence + approval
- **Selection rationale:** primary no-cost SR on the primary engine (S-04, S-02)
- **Sources:** S-02, S-04

### A11Y-ENV-002 — Windows 11 · Firefox (Gecko) · NVDA
- **Tier:** 1 · **Requirement:** Required
- **OS family:** Windows 11 · **Browser:** Firefox (release or ESR) · **AT:** NVDA · **Input:** keyboard + pointer
- **Language scope:** DE, EN · **Channel:** Web Product UI, Web Documentation
- **Intended evidence level:** AE-2 + AE-3
- **Trigger:** always
- **Local execution availability:** Not asserted (Execution Gap)
- **Known gap:** none beyond availability
- **Claim boundary:** listing ≠ support
- **Selection rationale:** second rendering engine catches single-engine quirks (S-06, S-04)
- **Sources:** S-06, S-04

### A11Y-ENV-003 — Windows 11 · Chromium (Edge) · Keyboard-only (no AT)
- **Tier:** 1 · **Requirement:** Required
- **OS family:** Windows 11 · **Browser:** Chromium (Edge) · **AT:** None (keyboard-only) · **Input:** keyboard only
- **Language scope:** DE, EN · **Channel:** Web Product UI, Web Documentation
- **Intended evidence level:** AE-2
- **Trigger:** always
- **Local execution availability:** Not asserted
- **Known gap:** none beyond availability
- **Claim boundary:** a keyboard check is a specific check, never conformance
- **Selection rationale:** keyboard operability, focus order/visibility, no trap (2.1.1, 2.1.2, 2.4.3, 2.4.7)
- **Sources:** S-02

### A11Y-ENV-004 — Windows 11 · Chromium (Edge) · Forced Colors / High Contrast
- **Tier:** 1 · **Requirement:** Required
- **OS family:** Windows 11 · **Browser:** Chromium (Edge) · **AT:** None (forced-colors condition) · **Input:** keyboard + pointer
- **Language scope:** DE, EN · **Channel:** Web Product UI, Web Documentation
- **Intended evidence level:** AE-2
- **Trigger:** always (platform offers forced colors)
- **Local execution availability:** Not asserted
- **Known gap:** non-Windows forced-colors behavior out of Required
- **Claim boundary:** listing ≠ support
- **Selection rationale:** non-colour meaning must survive forced colors (1.4.1; DEC-S-056); tied to Windows High Contrast (S-08)
- **Sources:** S-08, S-02

### A11Y-ENV-005 — Windows 11 · Chromium (Edge) · Reduced Motion
- **Tier:** 1 · **Requirement:** Required
- **OS family:** Windows 11 · **Browser:** Chromium (Edge) · **AT:** None (reduced-motion condition) · **Input:** keyboard + pointer
- **Language scope:** DE, EN · **Channel:** Web Product UI, Web Documentation
- **Intended evidence level:** AE-2
- **Trigger:** always
- **Local execution availability:** Not asserted
- **Known gap:** none beyond availability
- **Claim boundary:** listing ≠ support
- **Selection rationale:** motion honours the OS reduced-motion setting (S-07)
- **Sources:** S-07, S-02

### A11Y-ENV-006 — Windows 11 · Chromium (Edge) · Zoom 400 % / Reflow / Text spacing
- **Tier:** 1 · **Requirement:** Required
- **OS family:** Windows 11 · **Browser:** Chromium (Edge) · **AT:** None (magnification/reflow condition) · **Input:** keyboard + pointer
- **Language scope:** DE, EN · **Channel:** Web Product UI, Web Documentation
- **Intended evidence level:** AE-2
- **Trigger:** always
- **Local execution availability:** Not asserted
- **Known gap:** none beyond availability
- **Claim boundary:** listing ≠ support
- **Selection rationale:** reflow at 400 %, text spacing, flexible text length (1.4.10, 1.4.12, 1.4.4)
- **Sources:** S-02

---

## Tier 2 — Conditional (A11Y-ENV-007 … 010)

### A11Y-ENV-007 — macOS · Safari (WebKit) · VoiceOver
- **Tier:** 2 · **Requirement:** Conditional
- **OS family:** macOS (current) · **Browser:** Safari (WebKit) · **AT:** VoiceOver · **Input:** keyboard + pointer
- **Language scope:** DE, EN · **Channel:** Web Product UI, Web Documentation
- **Intended evidence level:** AE-2 + AE-3
- **Trigger:** declared scope/claim includes Apple platforms; or evidence/risk shows a WebKit gap
- **Local execution availability:** Not asserted
- **Known gap:** WebKit engine untested in Required (RISK-049)
- **Claim boundary:** no Apple-platform claim without this evidence
- **Selection rationale:** third engine + built-in SR (S-05)
- **Sources:** S-05

### A11Y-ENV-008 — Windows 11 · Chromium (Edge) · JAWS
- **Tier:** 2 · **Requirement:** Conditional
- **OS family:** Windows 11 · **Browser:** Chromium (Edge) · **AT:** JAWS (commercial) · **Input:** keyboard + pointer
- **Language scope:** DE, EN · **Channel:** Web Product UI, Web Documentation
- **Intended evidence level:** AE-2 + AE-3
- **Trigger:** scope/consumer/risk requires the most common commercial SR
- **Local execution availability:** Not asserted; **licence required**
- **Known gap:** **official system requirements NOT retrievable (S-12/S-13, HTTP 403)** — must be verified before this becomes Required or claimed (RISK-051)
- **Claim boundary:** no JAWS-support claim without verified requirements + evidence
- **Selection rationale:** widely used commercial SR; verification pending
- **Sources:** S-12 (403), S-13 (403)

### A11Y-ENV-009 — Windows 11 · Chromium (Edge) · Narrator
- **Tier:** 2 · **Requirement:** Conditional
- **OS family:** Windows 11 · **Browser:** Chromium (Edge) · **AT:** Narrator (Windows built-in) · **Input:** keyboard + pointer
- **Language scope:** DE, EN · **Channel:** Web Product UI, Web Documentation
- **Intended evidence level:** AE-2 + AE-3
- **Trigger:** platform SR coverage beyond NVDA required by scope/risk
- **Local execution availability:** Not asserted
- **Known gap:** kept out of Required to hold the pairing count small
- **Claim boundary:** listing ≠ support
- **Selection rationale:** built-in Windows SR; complementary breadth
- **Sources:** S-03 (platform)

### A11Y-ENV-010 — Windows 11 · Chromium (Edge) · Alternative input (voice / switch)
- **Tier:** 2 · **Requirement:** Conditional
- **OS family:** Windows 11 · **Browser:** Chromium (Edge) · **AT:** speech/switch input · **Input:** voice / switch
- **Language scope:** DE, EN · **Channel:** Web Product UI
- **Intended evidence level:** AE-2 + AE-3
- **Trigger:** declared scope or consumer includes alternative input
- **Local execution availability:** Not asserted
- **Known gap:** alternative-input behavior untested in Required
- **Claim boundary:** listing ≠ support
- **Selection rationale:** operability beyond keyboard/pointer
- **Sources:** S-03 (platform)

---

## Tier 3 — Deferred (A11Y-ENV-011 … 014)

### A11Y-ENV-011 — iOS · Safari (WebKit) · VoiceOver · touch
- **Tier:** 3 · **Requirement:** Deferred
- **OS family:** iOS (current) · **Browser:** Safari (WebKit) · **AT:** VoiceOver · **Input:** touch
- **Language scope:** DE, EN · **Channel:** Web Product UI
- **Intended evidence level:** AE-2 + AE-3 (when triggered)
- **Trigger:** declared mobile-web scope / Consumer Contract / Product Profile
- **Local execution availability:** Not asserted
- **Known gap:** mobile/touch untested (RISK-049)
- **Claim boundary:** undeclared mobile is never presented as supported (DEC-S-069)
- **Selection rationale:** mobile web with built-in SR (S-05)
- **Sources:** S-05

### A11Y-ENV-012 — Android · Chrome (Chromium) · TalkBack · touch
- **Tier:** 3 · **Requirement:** Deferred
- **OS family:** Android (current) · **Browser:** Chrome (Chromium) · **AT:** TalkBack · **Input:** touch
- **Language scope:** DE, EN · **Channel:** Web Product UI
- **Intended evidence level:** AE-2 + AE-3 (when triggered)
- **Trigger:** declared mobile-web scope / Consumer Contract
- **Local execution availability:** Not asserted
- **Known gap:** Android/TalkBack untested; TalkBack official requirements not yet researched
- **Claim boundary:** undeclared mobile is never presented as supported
- **Selection rationale:** second mobile platform
- **Sources:** S-09 (Chromium)

### A11Y-ENV-013 — Additional languages beyond DE/EN
- **Tier:** 3 · **Requirement:** Deferred
- **OS family:** any Required/Conditional · **Browser:** any · **AT:** any · **Input:** any
- **Language scope:** languages beyond DE/EN · **Channel:** Web Product UI, Web Documentation
- **Intended evidence level:** AE-2 (when triggered)
- **Trigger:** declared additional-language scope / Consumer Contract
- **Local execution availability:** Not asserted
- **Known gap:** only DE/EN in Required
- **Claim boundary:** no multilingual claim without declared scope + evidence
- **Selection rationale:** DE/EN is the declared initial language scope (CR-023)
- **Sources:** — (policy scope)

### A11Y-ENV-014 — Enterprise / procurement / air-gapped environments
- **Tier:** 3 · **Requirement:** Deferred
- **OS family:** consumer-declared · **Browser:** consumer-declared · **AT:** consumer-declared · **Input:** consumer-declared
- **Language scope:** consumer-declared · **Channel:** consumer-declared
- **Intended evidence level:** AE-4 (consumer)
- **Trigger:** Consumer Contract / procurement requirement / air-gapped deployment (CR-031, CR-032)
- **Local execution availability:** Not asserted
- **Known gap:** consumer-owned environments not represented in CDS Required
- **Claim boundary:** consumer evidence does not transfer to CDS (DEC-S-052)
- **Selection rationale:** offline/self-hosted is a confirmed consumer need (DEC-S-030)
- **Sources:** — (policy scope)

---

## Derived counts

*(Re-derived from the entries above; independently re-counted)*

| Metric | Value | Entries |
| --- | --- | --- |
| Total environment entries | **14** | ENV-001 … 014 |
| Required (Tier 1) | **6** | 001–006 |
| Conditional (Tier 2) | **4** | 007–010 |
| Deferred (Tier 3) | **4** | 011–014 |
| Required browser/screen-reader pairings | **2** | 001, 002 |
| Total browser/screen-reader pairings (all tiers) | **7** | 001, 002, 007, 008, 009, 011, 012 |
| OS families | **4** | Windows 11, macOS, iOS, Android |
| Browser/renderer families | **3** | Chromium, Gecko, WebKit |
| Assistive-technology families | **5** | NVDA, JAWS, Narrator, VoiceOver, TalkBack |
| Declared languages | **2** | DE, EN |
| Declared channels | **2** | Web Product UI, Web Documentation |

## Open coverage gaps

- WebKit/Safari untested until Tier 2 (RISK-049).
- JAWS requirements unverified (S-12/S-13, RISK-051).
- Mobile/touch and Android/TalkBack untested (Tier 3).
- No local execution availability asserted for any row (RISK-051).
- Languages beyond DE/EN out of Required.

## Related documents

- [Accessibility Support Baseline](ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Baseline Maintenance Policy](ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md)
- [Accessibility Evidence Strategy](ACCESSIBILITY_EVIDENCE_STRATEGY.md)
- [Accessibility Baseline Source Register](../research/ACCESSIBILITY_BASELINE_SOURCE_REGISTER.md)
