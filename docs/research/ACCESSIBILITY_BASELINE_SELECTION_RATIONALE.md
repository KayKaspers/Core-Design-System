# Accessibility Baseline Selection Rationale

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-010 — Accessibility Support Baseline and Evidence Strategy
- **Date:** 2026-07-16
- **Status:** **Research evidence — NON-normative.** Explains *why* the initial
  baseline (A11Y-BL-001) is composed as it is. It decides nothing; the normative
  choice lives in the [Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
  and takes effect only on Human-Maintainer commit.

## Methodology

1. Read the committed accessibility policy suite (evidence levels, responsibility
   model, channel profiles, pilot criterion, requirements baseline).
2. Opened only official standards/vendor/product sources
   ([Source Register](ACCESSIBILITY_BASELINE_SOURCE_REGISTER.md)); recorded every
   URL, including failures.
3. Derived a **small, capacity-aware** Required baseline for the interactive
   **desktop-web** scope, and assigned everything else to Complementary or
   Scope-triggered tiers.
4. Ran no tests, installed nothing, and invented no local availability.

## Selection criteria

- **Official-source-verifiable** current support/lifecycle status only.
- **Two rendering engines** so single-engine quirks are caught (Chromium + Gecko).
- **At least one no-cost desktop screen reader**, so the Required baseline is
  executable without a commercial licence.
- **Small**: Required holds **two** screen-reader/browser pairings (the policy cap
  is three), plus keyboard-only and the platform display conditions.
- **Capacity honesty**: anything the maintainers cannot currently, verifiably run
  is a **Deferred** or **Conditional** entry with an Execution Gap — never a
  Required entry propped up by assumed availability.

## Evaluated environment families (official sources)

| Family | Official finding (dated 2026-07-16) | Source |
| --- | --- | --- |
| Windows 11 desktop OS | Modern Lifecycle; supported 24H2 / 25H2 / 26H1 | S-03 |
| Chromium browser (Edge / Chrome) | Rapid release (Edge 2-week from v152; Chrome 4-week; both 8-week Extended Stable); shared Chromium engine | S-02, S-09 |
| Firefox (Gecko) | Rapid release 4-week + ESR annual with security updates | S-06 |
| NVDA (screen reader) | Free / open source; Windows 10/11 64-bit | S-04 |
| VoiceOver (screen reader) | Built into macOS / iOS / iPadOS | S-05 |
| JAWS (screen reader) | Official requirements **not retrievable** (HTTP 403) | S-12, S-13 |
| Forced colors / High Contrast | `forced-colors` tied to Windows High Contrast / Contrast Themes | S-08 |
| Reduced motion | `prefers-reduced-motion` tied to OS setting | S-07 |
| Automated tooling role | Tools *assist*, do not *determine* accessibility | S-01 |

## Selected Tier-1 (Required Core) baseline

- **OS family:** Windows 11 (a currently supported version).
- **Browsers:** one Chromium-based family (Edge as the officially-sourced
  representative; Chrome is the same engine) **and** Firefox (Gecko).
- **Screen reader:** NVDA (no-cost), paired with each browser → **2 pairings**.
- **Non-AT conditions:** keyboard-only; forced-colors/high-contrast; reduced
  motion; zoom 400 % + reflow + text spacing.
- **Languages:** DE and EN. **Channels:** Web Product UI; Web Documentation.

**Why this set:** it exercises two engines and a real screen reader on a supported
OS, covers the WCAG-relevant display conditions that the CDS status/contract areas
depend on (non-colour meaning under forced colors, motion, magnification), and is
runnable with **only free software** — so capacity does not force a shortcut
(RISK-048, DEC-S-059).

## Tier-2 (Complementary) assessment

- **Safari + VoiceOver (macOS):** the second engine family (WebKit) and a built-in
  screen reader; becomes mandatory when the declared scope or a claim includes
  Apple platforms.
- **JAWS (Windows):** the most widely used commercial screen reader in enterprise
  contexts, but its official requirements were **not retrievable** (S-12, S-13);
  kept Conditional with an explicit source limitation.
- **Narrator (Windows built-in)** and **alternative input** (voice/switch): kept
  Conditional to hold Required small.

## Tier-3 (Scope-triggered) assessment

Mobile web (iOS Safari + VoiceOver; Android Chrome + TalkBack), additional
languages, and enterprise/procurement or air-gapped environments are **Deferred**:
none is in the declared initial desktop-web scope, and adding them to Required now
would exceed capacity and mis-state coverage (RISK-049, RISK-051).

## Capacity trade-offs

- A small Required set means **narrower** coverage, made **visible** rather than
  hidden (RISK-049): Apple/WebKit, JAWS, and mobile are out of Required by design.
- Free-software-only Required keeps AE-2/AE-3 executable without procurement, but
  **JAWS-specific behavior is unproven** until Tier-2 runs.
- The honest response to more demand is **more scope declared and evidenced**, or
  **lower maturity** — never a weaker standard (DEC-S-059).

## Coverage gaps (carried forward)

1. **WebKit/Safari untested** until Tier-2 (RISK-049).
2. **JAWS behavior unknown** and its requirements unverified (RISK-051; S-12/S-13).
3. **Mobile/touch untested** (Tier-3, RISK-049).
4. **No local execution availability is asserted** for any environment; each
   Required entry still needs a real, capacity-checked execution slot before AE-2/
   AE-3 can be produced (RISK-051).
5. **Languages beyond DE/EN** are out of scope until declared.

## Rejected or deferred combinations

- Market-share-driven "top browsers" selection — **rejected**: no market-share or
  popularity source is permitted (RISK-011), and popularity is not fitness.
- A JAWS-Required baseline — **deferred**: cannot be justified without verifiable
  official requirements.
- A mobile-inclusive Required baseline — **deferred**: outside the declared scope
  and over capacity.

## Explicit non-claims

- **No market-share or popularity claim** is made or implied.
- **No support claim**: listing an environment is a *plan to evidence it later*,
  not a statement that it works or is supported.
- **No accessibility evidence** exists; every CDS artifact remains **AE-0**.

## Future review needs

Re-verify vendor lifecycle/version facts before each Candidate, Stable, pilot, or
claim gate and on any major version, support-end, regression, or scope change, and
at least every six months (per the
[Baseline Maintenance Policy](../governance/ACCESSIBILITY_BASELINE_MAINTENANCE_POLICY.md)).
Verify JAWS official requirements before it becomes a Required or claimed pairing.

## Related documents

- [Accessibility Baseline Source Register](ACCESSIBILITY_BASELINE_SOURCE_REGISTER.md)
- [Accessibility Support Baseline](../governance/ACCESSIBILITY_SUPPORT_BASELINE.md)
- [Accessibility Environment and Scope Matrix](../governance/ACCESSIBILITY_ENVIRONMENT_AND_SCOPE_MATRIX.md)
- [Accessibility Evidence Strategy](../governance/ACCESSIBILITY_EVIDENCE_STRATEGY.md)
