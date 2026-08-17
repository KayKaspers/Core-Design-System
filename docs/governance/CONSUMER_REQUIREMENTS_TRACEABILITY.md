# Consumer Requirements Traceability

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-004 — Consumer Requirements and CoreOps Pilot Contract
- **Evidence date:** 2026-07-15
- **Status:** Normative for **traceability**; not an approval of any requirement

## Purpose

Every requirement in the
[Consumer Requirements Model](CONSUMER_REQUIREMENTS_MODEL.md) is traced here to
the committed consumer revision it came from, so that no requirement rests on
memory, assumption, or an uncommitted working tree (DEC-S-013).

This matrix was generated from the requirement register rather than written by
hand, so requirement IDs cannot drift between the two documents.

## Source revisions

| Consumer | Code | Repository | HEAD commit |
| --- | --- | --- | --- |
| CoreOps | `CO` | KayKaspers/CoreOps | `399de21c2d76cf84279badfcde58dacbb9eec1a2` |
| SpeakCore | `SP` | KayKaspers/SpeakCore | `a5e697715c1c7077bc6c53400b3e6411730720ba` |
| CastCore | `CC` | KayKaspers/CastCore | `6c7614e3192a11479ae1c7431195daa042d38250` |

Commit column below shows the short form of each cited consumer's HEAD.

## Reading the matrix

- **Pilot group** `—` means the requirement is pilot-relevant but not bound to a
  single group (for example an artifact-level or governance constraint).
  `Not in pilot` means it is outside the bounded pilot entirely.
- **Follow-up** names where the requirement is next handled. It is not a
  schedule.
- A traceability entry records **provenance**, never approval.

## Traceability matrix

| Requirement | Consumer source | Source commit | Source file and section | CDS domain | Classification | Pilot group | Validation target | Follow-up | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR-001 | CO, SP, CC | 399de21c · a5e69771 · 6c7614e3 | CO `docs/architecture/PROJECT_BRIEF.md` §4 | Brand | Shared CDS Candidate | A | Human Maintainer decision on family expression | CDS-WP-005 | Open |
| CR-002 | SP, CC | a5e69771 · 6c7614e3 | SP `project-brain/BRANDING.md` §1–3; CC `docs/ARCHITECTURE.md` UI | Foundations | Shared CDS Candidate | — | Reconciliation review against product-local token sets | CDS-WP-005 | Open |
| CR-003 | CO | 399de21c | CO `docs/architecture/COREOPS_CONCEPT_V3.md` §11 | Experience | CoreOps Pilot Requirement | A | Pilot Group A scenario evidence | CDS-WP-005 | Open |
| CR-004 | CO, CC | 399de21c · 6c7614e3 | CO `…/COREOPS_CONCEPT_V3.md` Frontend; CC `docs/ARCHITECTURE.md` UI | Experience | Shared CDS Candidate | A | Pilot Group A scenario evidence | CDS-WP-005 | Open |
| CR-005 | CO, SP, CC | 399de21c · a5e69771 · 6c7614e3 | CO `…/COREOPS_CONCEPT_V3.md` §11; SP `docs/branding/ui-principles.md`; CC `docs/de/user-guide/monitoring.md` | Experience | Shared CDS Candidate | B | Pilot Group B scenario evidence | CDS-WP-005 | Open |
| CR-006 | CO, SP, CC | 399de21c · a5e69771 · 6c7614e3 | SP `docs/branding/ui-principles.md` P2/P6; CC `docs/de/user-guide/monitoring.md`; CO `…/COREOPS_CONCEPT_V3.md` | Foundations | Shared CDS Candidate | B, D | Pilot Group B and D evidence; non-colour check | CDS-WP-005 | Open |
| CR-007 | CO, CC | 399de21c · 6c7614e3 | CO `docs/architecture/PROJECT_BRIEF.md` §8 APC-07; CC `docs/de/user-guide/monitoring.md` | Experience | Shared CDS Candidate | B, D | Pilot Group B and D state coverage | CDS-WP-005 | Open |
| CR-008 | CO, SP, CC | 399de21c · a5e69771 · 6c7614e3 | CO `…/COREOPS_CONCEPT_V3.md` §11; CC `docs/ARCHITECTURE.md` UI | Components | Shared CDS Candidate | C | Pilot Group C scenario evidence | CDS-WP-005 | Open |
| CR-009 | CO | 399de21c | CO `docs/architecture/TOPOLOGY_GRAPH_AND_RELATIONSHIP_MODEL.md` | Experience | Deferred Requirement | Not in pilot | Deferred; needs multi-consumer demand | CDS-WP-005 | Deferred |
| CR-010 | CO, SP | 399de21c · a5e69771 | CO `…/COREOPS_CONCEPT_V3.md`; SP `docs/branding/ui-principles.md` P4 | Components | Shared CDS Candidate | D | Pilot Group D scenario evidence | CDS-WP-005 | Open |
| CR-011 | CO, CC | 399de21c · 6c7614e3 | CO `docs/architecture/PROJECT_BRIEF.md` §7; CC `docs/ARCHITECTURE.md` UI | Experience | Shared CDS Candidate | D | Pilot Group D scenario evidence | CDS-WP-005 | Open |
| CR-012 | CO, SP, CC | 399de21c · a5e69771 · 6c7614e3 | SP `docs/branding/ui-principles.md` P4; CC `docs/ARCHITECTURE.md` UI; CO `PROJECT_BRIEF.md` §7 | Components | Shared CDS Candidate | D | Pilot Group D scenario evidence | CDS-WP-005 | Open |
| CR-013 | CO, CC | 399de21c · 6c7614e3 | CO `…/COREOPS_CONCEPT_V3.md`; CC `README.md` | Experience | Shared CDS Candidate | D | Pilot Group D state coverage | CDS-WP-005 | Open |
| CR-014 | CO | 399de21c | CO `docs/architecture/PROJECT_BRIEF.md` §6 | Experience | CoreOps Pilot Requirement | D | Pilot Group D evidence; generalizability review | CDS-WP-004 follow-up | Open |
| CR-015 | CO, SP, CC | 399de21c · a5e69771 · 6c7614e3 | CO `…/DEGRADED_MODE_AND_CAPABILITY_RESTRICTION_MODEL.md` §6–16; SP `docs/branding/ui-principles.md`; CC `docs/de/user-guide/monitoring.md` | Components | Shared CDS Candidate | D | Pilot Group D full state coverage | CDS-WP-005 | Open |
| CR-016 | CO, CC | 399de21c · 6c7614e3 | CO `…/DEGRADED_MODE_AND_CAPABILITY_RESTRICTION_MODEL.md` §8; CC `docs/ARCHITECTURE.md` | Experience | Shared CDS Candidate | D | Pilot Group D scenario evidence | CDS-WP-005 | Open |
| CR-017 | CO, SP, CC | 399de21c · a5e69771 · 6c7614e3 | CO `docs/architecture/PROJECT_BRIEF.md`; SP `docs/README.md`; CC `docs/de/getting-started/first-setup.md` | Experience | Shared CDS Candidate | E | Pilot Group E scenario evidence | CDS-WP-005 | Open |
| CR-018 | CO, SP, CC | 399de21c · a5e69771 · 6c7614e3 | CO `…/COREOPS_CONCEPT_V3.md`; SP `docs/branding/ui-principles.md` P3; CC `docs/ARCHITECTURE.md` | Experience | Shared CDS Candidate | A, E | Pilot Group A and E evidence | CDS-WP-005 | Open |
| CR-019 | CO, CC | 399de21c · 6c7614e3 | CO `…/COREOPS_CONCEPT_V3.md`; CC `docs/ARCHITECTURE.md` UI | Channels | Shared CDS Candidate | E | Pilot Group E scenario evidence | CDS-WP-005 | Open |
| CR-020 | CO, CC | 399de21c · 6c7614e3 | CO `…/COREOPS_CONCEPT_V3.md`; CC `README.md` + `docs/ARCHITECTURE.md` | Experience | Shared CDS Candidate | D, E | Pilot Group D and E evidence | CDS-WP-005 | Open |
| CR-021 | SP | a5e69771 | SP `docs/branding/ui-principles.md` P6 | Foundations | Shared CDS Candidate | E | Pilot Group E keyboard and focus check | CDS-WP-008 | Open |
| CR-022 | SP | a5e69771 | SP `docs/branding/ui-principles.md` P1/P6 | Foundations | Shared CDS Candidate | E | Pilot Group E reduced-motion check | CDS-WP-008 | Open |
| CR-023 | CO, CC | 399de21c · 6c7614e3 | CO `docs/governance/COREOPS_LANGUAGE_STANDARD.md` §7; CC `docs/ROADMAP.md` | Foundations | Shared CDS Candidate | E | Pilot Group E text-length and DE/EN check | CDS-WP-005 | Open |
| CR-024 | CO, SP | 399de21c · a5e69771 | CO `…/COREOPS_CONCEPT_V3.md` baseline; SP `docs/branding/ui-principles.md` | Governance | Deferred Requirement | — | **Resolved at policy level by CDS-WP-007 — WCAG 2.2 AA target (DEC-S-060), committed and in effect; evidence still absent, no conformance claim** | CDS-WP-008 | Open |
| CR-025 | CO, SP | 399de21c · a5e69771 | CO `…/COREOPS_CONCEPT_V3.md` Frontend; SP `project-brain/BRANDING.md` §1 | Foundations | Shared CDS Candidate | — | Deferred to foundations work | CDS-WP-005 | Open |
| CR-026 | CC | 6c7614e3 | CC `README.md` | Channels | Deferred Requirement | Not in pilot | Deferred; needs multi-consumer demand | CDS-WP-005 | Deferred |
| CR-027 | CO, CC | 399de21c · 6c7614e3 | CO `docs/governance/COREOPS_LANGUAGE_STANDARD.md`; CC `docs/de/developer-guide/documentation-rules.md` | Channels | Deferred Requirement | Not in pilot | Deferred; strong evidence but outside pilot | CDS-WP-005 | Deferred |
| CR-028 | CO | 399de21c | CO `docs/architecture/*` report references | Channels | Deferred Requirement | Not in pilot | Deferred; demand unproven | CDS-WP-005 | Deferred |
| CR-029 | CO | 399de21c | CO `docs/architecture/*` diagram references | Channels | Deferred Requirement | Not in pilot | Deferred; demand unproven | CDS-WP-005 | Deferred |
| CR-030 | — | — | — no consumer evidence found | Channels | Deferred Requirement | Not in pilot | **No consumer evidence found.** Registered only to close the multi-channel set | CDS-WP-005 | Deferred |
| CR-031 | CO, SP, CC | 399de21c · a5e69771 · 6c7614e3 | CO `docs/architecture/PROJECT_BRIEF.md` §8; SP `docs/README.md`; CC `README.md` | Foundations | Shared CDS Candidate | — | Pilot artifact review against offline constraint | CDS-WP-005 | Open |
| CR-032 | CO, CC | 399de21c · 6c7614e3 | CO `…/RESTRICTED_ISOLATED_AND_AIR_GAPPED_OPERATION_MODEL.md`; CC `README.md` | Experience | Shared CDS Candidate | D | Pilot Group D state coverage | CDS-WP-005 | Open |
| CR-033 | CO | 399de21c | CO `docs/governance/COREOPS_LANGUAGE_STANDARD.md` §5 | Governance | Shared CDS Candidate | — | Terminology review across pilot artifacts | CDS-WP-005 | Open |
| CR-034 | CO | 399de21c | CO `docs/architecture/PROJECT_BRIEF.md` header | Governance | Shared CDS Candidate | — | Version-bound traceability in pilot evidence | CDS-WP-006 | Open |
| CR-035 | CO, SP, CC | 399de21c · a5e69771 · 6c7614e3 | CO `…/COREOPS_CONCEPT_V3.md`; SP `project-brain/`; CC `docs/DATA_MODEL.md` | — | Out of CDS Scope | Not in pilot | None — permanent non-goal | — | Closed |
| CR-036 | CO, SP, CC | 399de21c · a5e69771 · 6c7614e3 | CO `docs/security/*`; SP `project-brain/ARCHITECTURE.md`; CC `docs/ARCHITECTURE.md` | — | Out of CDS Scope | Not in pilot | None — permanent non-goal | — | Closed |
| CR-037 | SP, CC | a5e69771 · 6c7614e3 | SP `project-brain/BRANDING.md` §3; CC `docs/ARCHITECTURE.md` UI | Brand | Product-local Requirement | Not in pilot | Product-local; reconcile only via CR-002 | CDS-WP-005 | Open |
| CR-038 | SP, CC | a5e69771 · 6c7614e3 | SP `docs/README.md`; CC `docs/de/user-guide/monitoring.md` | — | Product-local Requirement | Not in pilot | Product-local unless generalized under DEC-S-016 | — | Open |
| CR-039 | CO | 399de21c | CO `…/COREOPS_CONCEPT_V3.md` §43 | Experience | Deferred Requirement | Not in pilot | Deferred; single-consumer need | CDS-WP-005 | Deferred |
| CR-040 | CO | 399de21c | CO `…/COREOPS_CONCEPT_V3.md` §9 | Governance | Deferred Requirement | Not in pilot | Deferred; architectural constraint for CDS-WP-005 | CDS-WP-005 | Deferred |

## Coverage

| Metric | Count |
| --- | --- |
| Requirements in register | 40 |
| Traceability entries | 40 |
| Requirements without a traceability entry | 0 |
| Traceability entries without a requirement | 0 |
| Entries citing at least one committed consumer revision | 39 |
| Entries with no consumer evidence | 1 (CR-030) |

Every requirement has exactly one traceability entry, and every entry maps to a
registered requirement. Counts were derived from the register and independently
re-counted.

**CR-030 carries no consumer source.** It is registered only to close the
multi-channel set and is explicitly marked as having no consumer evidence rather
than being quietly dropped.

## Limitations

- Provenance is to a **committed document**, not to user research. A traced
  requirement is evidenced as *documented intent or behavior* only (RISK-017).
- Consumer repositories evolve. These commits are a dated snapshot and decay
  (RISK-014). Re-verify before relying on a trace in a later decision.
- Section references point at headings and numbered sections as they exist at
  the cited commit; they will move as consumers edit their documents.

## Related documents

- [Consumer Requirements Model](CONSUMER_REQUIREMENTS_MODEL.md)
- [Consumer Evidence Register](../research/CONSUMER_EVIDENCE_REGISTER.md)
- [CoreOps Pilot Scope and Scenarios](COREOPS_PILOT_SCOPE_AND_SCENARIOS.md)
