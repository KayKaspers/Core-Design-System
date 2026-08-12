# Accessibility Channel Profiles

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-007
- **Date:** 2026-07-16
- **Status:** **Normative** for per-channel accessibility

## Purpose

WCAG 2.2 is written for **web content**. CDS scope includes non-web channels.

A web target therefore cannot simply be asserted across all of them: applying web
success criteria to a paginated print artifact is a category error in some cases
and undefined in others.

**Each channel requires an explicit accessibility profile before its artifacts
may become Candidate or Stable** (DEC-S-058).

Frame: [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md).

## The six profiles

| # | Channel | Target | WCAG applies? |
| --- | --- | --- | --- |
| 1 | Web Product UI | **WCAG 2.2 AA** | Yes |
| 2 | Web Documentation and Repository Presentation | **WCAG 2.2 AA** for web-rendered content | Yes, where applicable |
| 3 | PDF and Reports | **Undefined — profile required** | No |
| 4 | Presentations | **Undefined — profile required** | No |
| 5 | Diagrams and Data Visualization | Mixed — web-embedded inherits; exported does not | Partly |
| 6 | Brand and Communication Materials | **Undefined — usage rules required** | No |

**Only profiles 1 and 2 have a target today.** The rest are registered as
structure, not as commitments.

---

## 1. Web Product UI

| | |
| --- | --- |
| **Scope** | Web-based product interfaces built on CDS artifacts, in a declared scope |
| **Target** | **WCAG 2.2 Level AA** |
| **Owner** | CDS for artifacts and contracts; **Consumer for composition, content, process, runtime** |
| **Minimum future evidence** | AE-1 + AE-2 + **AE-3** against a declared baseline; **AE-4** for a product claim |
| **Current gap** | **Nearly everything.** No artifact exists; no evidence exists. AE-0. The support baseline **A11Y-BL-001 is declared and committed** (CDS-WP-010) — a test contract, not evidence. |
| **Candidate boundary** | Candidate accessibility gate |
| **Stable boundary** | Stable gate incl. AE-3 — **currently unreachable** |
| **Deferred** | Test tooling; status taxonomy; concrete values (the support baseline is no longer deferred — A11Y-BL-001 is committed) |

The primary channel. The pilot's declared web scope sits here.

## 2. Web Documentation and Repository Presentation

| | |
| --- | --- |
| **Scope** | Web-rendered CDS documentation and repository-facing presentation |
| **Target** | **WCAG 2.2 Level AA** for web-rendered content, where applicable |
| **Owner** | CDS |
| **Minimum future evidence** | AE-1 + AE-2; AE-3 where interactive |
| **Current gap** | No evidence. AE-0. Existing CDS documentation is **untested**. |
| **Candidate boundary** | Candidate gate |
| **Stable boundary** | Stable gate |
| **Deferred** | Documentation platform; rendering environment; DE/EN parity mechanism |

Additional requirements: semantic headings · understandable link text ·
alternative text · structured tables · **accessible code and diagram
explanations**.

**Constraint worth stating:** repository-hosted rendering is **platform-controlled**.
CDS cannot guarantee a host's rendering, so this profile covers what CDS
authors — not what a platform does with it.

## 3. PDF and Reports

| | |
| --- | --- |
| **Scope** | Paginated documents and exported reports |
| **Target** | **Undefined.** An accessible-document profile is required before Candidate or Stable. |
| **Owner** | CDS for templates and standards; Consumer for content and data |
| **Minimum future evidence** | Defined by the future profile |
| **Current gap** | **No profile, no standard, no evidence.** |
| **Candidate boundary** | **Blocked** — no profile exists |
| **Stable boundary** | **Blocked** |
| **Deferred** | **The PDF/document accessibility standard itself — not selected here** |

The physics differ: no hover, no live update, no focus, possibly greyscale print.
A status that depends on colour, interaction, or refresh **fails here** — which is
why the non-colour rule is architectural rather than a courtesy.

Consumer evidence for this channel is **weak** (CR-028).

## 4. Presentations

| | |
| --- | --- |
| **Scope** | Presentation artifacts and templates |
| **Target** | **Undefined — profile required** |
| **Owner** | CDS for template rules; Consumer for content |
| **Minimum future evidence** | Defined by the future profile |
| **Current gap** | **No profile, no evidence — and no consumer evidence at all** (CR-030) |
| **Candidate boundary** | **Blocked** |
| **Stable boundary** | **Blocked** |
| **Deferred** | Presentation format and accessibility standard |

Later needs: accessible template rules · reading order · alternative text ·
contrast · understandable slide titles · **no information conveyed visually
only**.

**No presentation template is created here.** This channel has **no consumer
demand evidence whatsoever** — it is registered to close the multi-channel set,
not because anyone asked for it.

## 5. Diagrams and Data Visualization

| | |
| --- | --- |
| **Scope** | Diagrams, charts, topology and relationship views |
| **Target** | Web-embedded inherits the web target; **exported requires a profile** |
| **Owner** | CDS for standards; Consumer for domain semantics and data |
| **Minimum future evidence** | AE-1 + AE-2 web-embedded; profile-defined when exported |
| **Current gap** | **No standard, no evidence** |
| **Candidate boundary** | Web-embedded: Candidate gate. Exported: **blocked** |
| **Stable boundary** | Exported: **blocked** |
| **Deferred** | Diagram format; alternative-representation mechanism |

Requirements: **textual explanation or an alternative data representation** ·
semantic legend · meaning without colour · **status and confidence
differentiation** · accessible framing of complex relationships.

**The hardest channel.** Dense encoding tempts every shortcut the policy forbids,
and structural meaning must survive export. It also carries the Unknown invariant
into a visual medium: a chart must distinguish *no data* from *zero*.

## 6. Brand and Communication Materials

| | |
| --- | --- |
| **Scope** | Brand assets, release and communication materials |
| **Target** | **Undefined — usage rules required** |
| **Owner** | CDS for usage rules; Consumer for deployment |
| **Minimum future evidence** | Profile-defined |
| **Current gap** | **No rules, no evidence** |
| **Candidate boundary** | **Blocked** |
| **Stable boundary** | **Blocked** |
| **Deferred** | Brand rules; asset formats; licensing (undecided per DEC-S-047) |

Needs: contrast and legibility usage rules · alternative-text and context rules ·
channel-appropriate limitations.

**Brand approval is never an accessibility claim.** The two are unrelated
authorities, and a brand sign-off says nothing about whether an asset is
perceivable.

**No design is created here.**

---

## Summary

| Metric | Count |
| --- | --- |
| **Channel profiles defined** | **6** |
| With a defined target | 2 |
| Target undefined pending profile | 4 |
| Candidate-eligible today | **0** |
| Stable-eligible today | **0** |

**Not one channel can produce a Candidate or Stable artifact today** — profiles 1
and 2 lack evidence and a support baseline; profiles 3–6 lack a profile entirely.

## Cross-cutting rules

*(Normative)*

1. **Non-web channels are never presented as WCAG-conformant.** WCAG is a web
   standard; asserting it elsewhere is a status error (DEC-S-058).
2. **Semantics stay constant across channels; presentation may differ**
   (DEC-S-029). A status that means *unknown* in the UI means *unknown* in the
   PDF.
3. **Evidence never transfers between channels** (DEC-S-052).
4. Each profile requires its own target, evidence, and known limitations.
5. A channel without a profile **cannot reach Candidate or Stable**.
6. **Meaning without colour applies to every channel**, including print.

## Related documents

- [Accessibility and Inclusive Design Policy](ACCESSIBILITY_AND_INCLUSIVE_DESIGN_POLICY.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
- [Accessibility Requirements Baseline](ACCESSIBILITY_REQUIREMENTS_BASELINE.md)
- [Artifact Distribution and Channel Model](../architecture/ARTIFACT_DISTRIBUTION_AND_CHANNEL_MODEL.md)
