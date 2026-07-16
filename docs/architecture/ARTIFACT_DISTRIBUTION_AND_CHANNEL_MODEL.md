# Artifact Distribution and Channel Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-005 — Design System Architecture
- **Date:** 2026-07-16
- **Status:** **Normative** for artifact families, channels, and distribution properties

## Purpose and boundary

This document defines **what CDS produces, how it reaches consumers, and what
must remain true of it** — without selecting a single technology.

**No format, package manager, repository topology, build system, or distribution
service is chosen here** (DEC-S-032).

Frame: [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md) — Layers 6
and 7.

## Logical artifact families

*(Normative)*

Families are **logical**. A family is not a file, package, or repository.

| Family | Contains | Authority class |
| --- | --- | --- |
| **Governance artifacts** | Intent, rules, boundaries, change control | 1 Normative human-readable |
| **Semantic source artifacts** | Approved values, relationships, metadata | 2 Normative machine-readable |
| **Contract artifacts** | Component and pattern contracts | 1, with 2 where values apply |
| **Derived artifacts** | Channel and platform outputs | 3 Generated |
| **Reference artifacts** | Reference implementations, examples | 4 and 8 |
| **Evidence artifacts** | Validation, accessibility, adoption, migration records | 6 |
| **Enablement artifacts** | Adoption, integration, migration guidance | 1 |

Authority classes: [Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md).

## Channel classes

*(Normative, DEC-S-029)*

| Channel | Consumes | Channel-specific reality |
| --- | --- | --- |
| **Product UI** | Foundations, components, patterns | Interactive, stateful, assistive-technology surface |
| **Repository presentation** | Brand, content standards | Constrained rendering; platform-controlled |
| **Documentation** | Content, brand, components | Long-form; needs DE/EN parity (CR-023, CR-027) |
| **PDF and reports** | Foundations, brand, data presentation | **Paginated, non-interactive, often printed** |
| **Presentations** | Brand, foundations | Projected; distance viewing |
| **Diagrams** | Foundations, semantics | Structural meaning; often exported |
| **Data visualization** | Foundations, status semantics | Dense; encoding-sensitive |
| **Release materials** | Brand, content, status semantics | Outward-facing; claim-sensitive |
| **Selected communication materials** | Brand, verbal identity | Outward-facing |

### The channel rule

**Channels share governed semantic foundations and retain their own
transformation, layout, interaction, and evidence requirements.**

**There is no assumption that product UI, PDF, presentation, and diagram render
identically.** A paginated report and an interactive dashboard have different
physics; forcing visual identity on them produces bad artifacts in both.

What may **not** differ is meaning (invariant 13). A status that means *unknown*
in the UI means *unknown* in the PDF. The presentation is free; the semantics are
not.

### Evidence honesty about channels

The benchmark found that **no reviewed system documented standards for PDF
reports, presentations, or diagrams** — and consumer evidence for those channels
is weak to absent (CR-028, CR-029 weak; **CR-030 has no consumer evidence at
all**). Registering these channel classes registers **structure**, not demand.
Nothing here asserts that CDS will build them, or that consumers need them.

## Transformation boundaries

*(Normative)*

A transformation turns a normative source into a derived artifact.

**A transformation may:** select, filter, reformat, restructure for a channel's
constraints, and encode for a platform.

**A transformation may not:**

- introduce a decision absent from the source,
- discard semantics the source carries,
- collapse separate status axes into one opaque value (DEC-S-028),
- make colour the sole carrier of meaning (CR-006),
- produce an output that cannot identify its source.

The last one turns a transformation into laundering: an artifact whose origin
nobody can establish is functionally normative because nobody can contradict it
(RISK-025).

## Offline and self-hosted requirements

*(Normative, DEC-S-030)*

| Requirement | Meaning |
| --- | --- |
| **No mandatory external runtime service** | Consuming a CDS artifact must not require calling a service CDS or a third party operates (invariant 12). |
| **Local availability** | Artifacts must be obtainable and usable locally. |
| **Local assets** | Assets an artifact depends on must be servable locally (CR-031). |
| **Air-gap tolerance** | A consumer with no external network must still be able to consume a pinned CDS revision. |
| **Optional services stay optional** | Convenience services may exist; nothing may depend on them. |

This is a **confirmed consumer need**, not a hypothesis: offline and air-gap
capable operation is an accepted product requirement of the pilot consumer, and
all three consumers position as self-hosted (CR-031, CR-032, HYP-002).

The benchmark found **no reviewed system stated an offline guarantee** — self-
containable distribution is common, but *committing* to it is not. CDS commits
architecturally. That is a commitment, not a claim of uniqueness (DEC-S-019).

## Provenance and pinning

*(Normative, DEC-S-031)*

Every derived artifact must carry:

| Identity | Answers |
| --- | --- |
| **Source revision** | Which normative source produced this |
| **Transformation revision** | Which transformation ran |
| **Output identity** | Which artifact this is |

Every consumer must be able to **pin to an identifiable CDS version or
revision**. "Latest" is not a pin, and a consumer that cannot name its CDS
revision cannot make an adoption claim (DEC-S-012, DEC-S-017).

## Reproducibility

*(Normative)*

Same source revision + same transformation revision = **same output**.

Reproducibility is what makes provenance meaningful: without it, a recorded
source revision is a claim rather than a fact.

Consequently: no unpinned inputs, no ambient state, no network dependency during
transformation, no non-determinism that changes semantics.

## Channel-specific constraints

Registered as structure. **None is designed here.**

- **Product UI** — interaction, focus, assistive technology, live state changes.
- **Documentation** — DE/EN parity and staleness control (CR-027).
- **PDF and reports** — pagination, print, no interaction; status must survive
  without hover, colour, or motion.
- **Presentations** — distance legibility.
- **Diagrams** — structural meaning must survive export.
- **Data visualization** — dense encoding; the non-colour rule bites hardest here.
- **Release materials** — claim discipline: no adoption or conformance claim
  without evidence (DEC-S-012, RISK-018).

## Distribution neutrality

*(Normative, DEC-S-030, DEC-S-032)*

The architecture is **neutral on distribution technology**. It constrains
properties, not mechanisms:

- must support local and offline consumption,
- must support revision pinning,
- must carry provenance,
- must be reproducible,
- must not require a mandatory external runtime.

Any mechanism satisfying these is architecturally acceptable. Any mechanism that
does not, is not — regardless of convenience.

## Deferred package and repository decisions

*(Deliberately open)*

Repository topology and split · package manager · package naming and granularity ·
distribution service or registry · build system · artifact formats per channel ·
metadata structure · versioning scheme (CDS-WP-006) · compatibility model
(CDS-WP-006) · which channels are actually built, and in what order.

**Open architectural question:** channels can drift into inconsistent semantic or
visual systems as they multiply (RISK-024). The shared semantic source constrains
this; it does not eliminate it. Governance of channel additions is CDS-WP-006's.

## Related documents

- [Design System Architecture](DESIGN_SYSTEM_ARCHITECTURE.md)
- [Source of Truth and Authority Model](SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)
- [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md)
- [Consumer Contract and Reconciliation Model](CONSUMER_CONTRACT_AND_RECONCILIATION_MODEL.md)
- [Evidence, Traceability and Status Semantics](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md)
