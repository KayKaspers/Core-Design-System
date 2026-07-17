# CDS-WP-011 — Machine-Readable Source and Token Format Decision — Work Package Notes

- **Project:** Core Design System (CDS)
- **Work package:** CDS-WP-011 — Machine-Readable Source and Token Format Decision
- **Date:** 2026-07-16
- **Status:** Work-package evidence — **non-normative**.

## Assignment

Make the binding architecture decision for the normative machine-readable CDS source
and the design-token format: the external format basis, the CDS profile, file
format/extension, naming, source-set/layer structure, reference/resolver rules,
metadata/provenance, validation boundaries, interoperability, upgrade governance, and
offline/tool-neutrality — and prepare the implementation work package. Create no
token, schema, validator, transformer, tool selection, or design value.

## Preflight

- Root `D:/Projects/Core-Design-System`; branch `main`; working tree clean; no
  merge/rebase; `origin` correct. Last commit `abe84b6` (CDS-WP-010).
- Foundation Closed with Notes; Phase Pre-Candidate Operating Enablement.
- Registers re-derived and counted: Decisions 72 (DEC-S-001…072); Risks 54 (52
  Monitored, RISK-040 + RISK-044 Mitigating); Requirements 40; Skills 39 files /
  manifest 38·39; **no existing ADR**. Token flow (Reference→Semantic→Component→
  Product Profile→Channel Output) and the 8 artifact classes confirmed. Publication
  `Private Development`; no Candidate/Stable; no claim; pilot inactive.
- Fail-closed conditions: none triggered.

## Skills used (9, only the authorized set)

ndf-work-package-runner (frame) · ndf-architecture-blueprint-runner (source-set/format
blueprint) · ndf-adr-governance-review (ADR-need + ADR-0001 number derived, not
invented) · ndf-existing-project-analysis-runner (structured format analysis) ·
ndf-feature-scope-runner (scope/non-goals) · ndf-validation-evidence-reviewer (honest
evidence strength; schema-not-correctness) · ndf-release-safety (no release/claim;
NO-GO on unclear readiness) · ndf-context-pack-maintainer (Context Pack update) ·
ndf-compact-context-summary-runner (closing blocks). No other skill was used.

## Web research

Authorized official-source research via the integrated web view only; no
curl/wget/CLI, no downloads, no installs, no third-party/comparison/snippet evidence.
**13 URLs opened; all 13 usable.** Stable DTCG **7** · preview/draft **1** (status
only) · RFC **3** · JSON Schema **2**. Full register:
[Token Format Source Register](../docs/research/TOKEN_FORMAT_SOURCE_REGISTER.md).

## Stable / preview separation

Stable: DTCG **2025.10** (index, Format, Color, Resolver) — a **Final Community Group
Report, "considered stable", "intended for implementation", not a W3C Standard** (S-01,
S-02, S-06, S-07). Preview: the DTCG **drafts** index explicitly states "do not
implement … do not reference as authoritative" (S-08) — used for status/future-change
awareness only, never normative.

## Options A…G

A DTCG 2025.10 Strict JSON Profile (**selected**) · B custom CDS JSON (rejected —
isolation/cost) · C YAML (rejected — non-determinism) · D JSONC/JSON5 (rejected — not
strict JSON) · E design-tool-native (rejected — lock-in) · F generated/CSS (rejected —
authority inversion) · G preview draft (rejected — unstable). Qualitative, no numeric
score:
[Token Format Evaluation](../docs/research/TOKEN_FORMAT_EVALUATION.md).

## Format decision

**Option A.** DTCG 2025.10 (Format, Color, Resolver) as external basis; strict JSON
(RFC 8259) `.tokens.json`; CDS profile over DTCG; JSON Schema 2020-12 profile-schema
foundation; `io.github.kaykaspers.cds` `$extensions` namespace. Recorded in
[ADR-0001](../docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
(accepted upon Human-Maintainer commit following Nova approval).

## DTCG modules

Format Module 2025.10 (JSON, `$value`/`$type`/`$description`/`$extensions`, groups,
`{group.token}` alias, `$`-reserved) · Color Module 2025.10 (`colorSpace` +
`components`, 14 spaces) · Resolver Module 2025.10 (sets + modifiers, ordered
resolution, multi-context). CDS selects no colour value.

## JSON and schema decision

Strict JSON per RFC 8259 (S-09); `.tokens.json`. JSON Schema draft 2020-12 (S-12/S-13)
as the future CDS-owned profile-schema foundation — **no schema created**; a schema
pass proves no semantic/accessibility/governance correctness (RISK-058).

## Extension namespace

Selected root **`io.github.kaykaspers.cds`** (single stable reserved `$extensions`
key). *(Corrected in the CDS-WP-011 correction run from the initially proposed `cds`,
which was insufficiently collision-resistant.)* Rationale: a collision-resistant
reverse-DNS-style key derived from the project's **repository identity**
(`github.com/kaykaspers/…`), unique enough to avoid clashes without asserting a
registered commercial domain/brand (publication/licensing undecided — DEC-S-046/047).
Used only inside `$extensions`, project-/repository-scoped, tool-neutral; must not
replace DTCG-expressible meaning. The key stays stable; the later extension structure
must carry a mandatory `profileVersion` field. **Foreign/unknown `$extensions` are
preserved and not automatically trusted or normative for CDS; only the CDS-owned
namespace may claim CDS profile metadata.** A namespace change requires compatibility/
migration/Human-Maintainer decision (DEC-S-082). No
extension value implemented.

## Source-set model

Eight source-set classes; class-2 normative: Reference, Semantic, Component, Product
Profile, Source-Set Manifest, Resolver/Composition; class-3 generated: Channel Output;
class-6 evidence: Validation/Evidence. Strictly downward dependency (Reference →
Semantic → Component → Product Profile → Generated Output); upward/cyclic dependencies
fail closed. [Machine-Readable Source Model](../docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md).

## Naming profile

Technical IDs separate from display labels; per-segment `^[a-z][a-z0-9-]*$`; no
case-only collisions, no reserved characters, no empty segments, no tool-specific
shared-semantics prefixes, no appearance/colour name in a semantic role; renames are
migration events (DEC-S-081). No real name created.

## Reference and resolver model

*(Reconciled in the CDS-WP-011 correction run.)* **Two complementary reference
mechanisms:** curly-brace `{group.token}` for **canonical token-to-token authoring**
(resolves `$value`); DTCG-conformant **`$ref` / RFC 6901 JSON Pointer** (required, not
undecided) for **document/property/resolver/source-set and controlled cross-file
references**. Cross-file references are permitted only via the declared Source-Set
Manifest/Resolver graph, to a known source-set identity, offline-resolvable, and
revision-/provenance-bound; **undeclared/ad-hoc cross-file references fail closed**.
Only the concrete **provenance-pointer form** stays open (CDS-WP-012). DTCG Resolver
for multi-context; declared source-set graph; deterministic ordered resolution;
type-compatible alias chains; **cycles, dangling references, missing source sets, type
conflicts, layer violations, unresolved overrides, undeclared cross-file references
fail closed; no automatic repair** (DEC-S-078).
[Reference, Resolution and Validation Model](../docs/architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md).

## Validation layers

Exactly four: **V1 Syntax** (RFC 8259) · **V2 DTCG 2025.10** · **V3 CDS Profile** ·
**V4 Semantic/Governance**. A V1 pass proves no higher layer; schema ≠ full
correctness; a tool result is not approval; no numeric score; an unrun layer is `Not
assessed`. **No validator implemented.**

## Metadata and provenance

Source-Set Identity (ID, CDS profile version, DTCG report version, immutable source
revision, maturity, approval, owner role, layer, dependency set, profile/channel
scope); token governance metadata; provenance chain (immutable source revision,
source/transformation/output/evidence identity, **no `latest`**, no secrets/personal
data). [Metadata, Provenance and Identity Model](../docs/architecture/TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md).

## Determinism

Reproducible processing (same source + transformation = same output); no hidden
network calls; no mandatory registry; local validatability; pinnable versions.
**Canonicalization decision state: open** — **RFC 8785 (JCS)** evaluated (Informational,
not a standard — S-11), **neither selected nor rejected**; deferred to CDS-WP-012. No
canonicalization implemented.

## ADR-0001

First ADR; title "Machine-Readable Token Source Format"; status "Accepted upon
Human-Maintainer commit following Nova approval"; options A…G; decision (DTCG 2025.10 +
strict JSON + `.tokens.json` + JSON Schema 2020-12 + source-set model + reference/
resolver + `io.github.kaykaspers.cds` extension + four validation layers +
determinism/offline); positive
consequences; trade-offs; rejected alternatives; migration/upgrade boundary; risks;
follow-up (CDS-WP-012); authority boundary.

## New decisions

DEC-S-073…082 (DTCG basis; pinned-stable-only; strict JSON `.tokens.json`; profile via
extensions; JSON Schema 2020-12; fail-closed references; layered sources; versioned
identity; naming profile; governed upgrades). Range DEC-S-001…082 (82); DEC-S-001…072
unchanged. ADRs: 1.

## New risks

RISK-055…063 (spec version drift; preview contamination; profile divergence; schema
false assurance; reference-resolution failure; cross-layer violation; identifier
collision; provenance incompleteness; transformation-tool lock-in), all Monitored.
Range RISK-001…063 (63): 61 Monitored, 2 Mitigating (RISK-040, RISK-044). No existing
status changed; no acceptance/closure.

## Changed or created files

Created (9): `docs/architecture/MACHINE_READABLE_SOURCE_MODEL.md`,
`CDS_TOKEN_FORMAT_PROFILE.md`, `TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md`,
`TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md`,
`docs/research/TOKEN_FORMAT_SOURCE_REGISTER.md`, `TOKEN_FORMAT_EVALUATION.md`,
`docs/decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md`,
`docs/roadmap/MACHINE_READABLE_SOURCE_IMPLEMENTATION_PLAN.md`, and this notes file.
Changed (10): `docs/decisions/DECISION_INDEX.md`, `docs/risks/RISK_REGISTER.md`,
`project-system/CONTEXT_PACK_FOUNDATION.md`, `PROJECT_PROFILE.md`, `NEXT_PHASE.md`,
`WORK_PACKAGES.md`, `project-brain/PROJECT_BRAIN.md`, `README.md`, `CLAUDE.md`,
`CHANGELOG.md`.

## Quantitative validation

See the Report to Nova (§14). Key figures: 13 URLs (7 stable DTCG / 1 preview / 3 RFC /
2 JSON Schema) · 7 options · 3 DTCG modules · 8 source-set classes · 5 token-flow
layers · 4 validation layers · 11 fail-closed conditions · 82 decisions · 1 ADR · 63
risks (61/2) · 12 work-package IDs · 9 skills.

## Deviations

None from the prompt. All work confined to the 19 Allowed Files. No token, schema,
validator, transformer, tool selection, or design value created. No Git write.

## Open implementation questions

- Concrete CDS profile JSON Schema and source-set manifest schema shape (CDS-WP-012).
- Concrete provenance-pointer form (which RFC 6901 JSON Pointer / `$ref` shape a
  provenance record uses) — the only open reference point; token-to-token curly-brace
  and `$ref`/JSON-Pointer roles are decided.
- Deterministic-serialization / canonicalization mechanism (RFC 8785 vs alternative) —
  open (DEC-S-080).
- Repository topology and file layout for source sets (not selected — DEC-S-032).
- Which validations run in which pipeline and what blocks (CDS-WP-012).
- Evidence Reviewer role remains unstaffed (FM-F-006).

## Correction runs (within CDS-WP-011, pre-commit)

1. **Extension Namespace and Reference-Syntax Reconciliation:** the `$extensions`
   namespace was changed from the initially proposed `cds` to
   **`io.github.kaykaspers.cds`** (collision-resistant, repository-identity-derived),
   and the reference model was reconciled — curly-brace `{group.token}` for canonical
   token-to-token authoring, DTCG `$ref` / RFC 6901 JSON Pointer as the required form
   for document/property/resolver/source-set and controlled cross-file references,
   with only the concrete provenance-pointer form left open.
2. **Final Micro-Correction (Work-Package Summary Namespace Reconciliation):** the one
   remaining stale active WP-011 summary — `project-system/WORK_PACKAGES.md` — was
   updated from `cds` to `io.github.kaykaspers.cds`. The namespace is now consistent
   across **all active WP-011 status and summary artifacts**; the only remaining `cds`
   mention is the clearly labelled historical "corrected from `cds`" note in this
   evidence file. **No further commit blocker remains.**

## Completion status

**PASS.** All Definition-of-Done items met; the two pre-commit correction runs are
closed; only Allowed Files changed; no Git write action performed.
