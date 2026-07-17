# ADR-0001 — Machine-Readable Token Source Format

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-011 — Machine-Readable Source and Token Format Decision
- **Status:** **Accepted upon Human-Maintainer commit following Nova approval.**
  Until commit, this ADR is a proposal. It creates no implementation, no token, no
  schema, and no Candidate maturity.
- **Date:** 2026-07-16
- **ADR number:** 0001 (first ADR; number derived from the empty ADR set, not
  invented)

## Context

The [Token and Theme Architecture](../architecture/TOKEN_AND_THEME_ARCHITECTURE.md)
defined a five-layer token flow but deliberately left the **machine-readable format
undecided** (DEC-S-024, DEC-S-032; open question 1). The
[Source of Truth and Authority Model](../architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)
established that normative machine-readable sources are **artifact class 2**
(approved values), distinct from class-1 meaning and class-3 generated artifacts.
No concrete format could be chosen earlier because the reviewed token
interoperability draft was an unimplementable preview. As of 2025-10-28, the Design
Tokens Community Group published its **first stable version, 2025.10** (S-01, S-02),
which makes a controlled decision possible.

## Decision drivers

Interoperability without tool lock-in (DEC-S-004, RISK-004) · human reviewability of
intent · offline and deterministic processing (DEC-S-006, DEC-S-030, DEC-S-031) ·
reference/alias support for the five-layer flow · metadata extensibility without
redefining shared semantics · machine-checkable validation · versioned provenance ·
small-team capacity (RISK-026, RISK-029).

## Considered options

A — DTCG 2025.10 Strict JSON Profile (**selected**) · B — fully custom CDS JSON ·
C — YAML source · D — JSONC/JSON5 source · E — design-tool-native format · F —
generated code/CSS as source · G — current DTCG preview draft. Full comparison:
[Token Format Evaluation](../research/TOKEN_FORMAT_EVALUATION.md). No numeric score.

## Decision

CDS adopts **Option A**: the **Design Tokens Community Group Technical Reports
2025.10** as the external normative basis of the CDS Token Format Profile, expressed
in **strict JSON**, constrained by a CDS-owned profile.

### Stable DTCG version and module binding

- **Pinned version: DTCG 2025.10** (S-02).
- **Modules:** **Format Module 2025.10**, **Color Module 2025.10**, and **Resolver
  Module 2025.10** where applicable (S-03, S-04, S-05).
- **Status recorded (normative facts):** DTCG 2025.10 is a **Final Community Group
  Report**, published stable and intended for implementation; it is **not a W3C
  Standard** and **not on the W3C Recommendation Track**. CDS remains responsible
  for its own profile. **DTCG conformance is not a CDS quality, semantic, or
  accessibility statement** (DEC-S-073).
- **Preview boundary:** only the pinned 2025.10 reports are authoritative. Preview,
  draft, editor, or future reports are research inputs until a controlled
  compatibility and migration decision accepts them (DEC-S-074). The preview drafts
  themselves state "do not implement" (S-08).

### Strict JSON and `.tokens.json`

- Normative CDS token source documents use **strict JSON per RFC 8259** (S-09) and
  the file extension **`.tokens.json`** (DEC-S-075).
- **Not normative sources:** YAML, JSONC, JSON5, JavaScript/TypeScript modules,
  design-tool export formats, CSS custom properties, Sass variables, generated
  platform formats. These may later be **authoring input** or **generated output**,
  never a normative source without controlled reconciliation (DEC-S-026).

### JSON Schema 2020-12 profile-validation decision

- CDS uses **JSON Schema draft 2020-12** (S-12, S-13) as the structural-schema
  foundation for a **future CDS-owned** profile validator (DEC-S-077).
- **CDS-WP-011 creates no schema.** The schema will be CDS-owned, will validate the
  CDS profile, and is **not** an official DTCG schema. **Schema success alone proves
  neither full DTCG conformance nor semantic, visual, accessibility, or governance
  correctness** (RISK-058).

### Source-Set model

Normative machine-readable sources are separated into **Reference, Semantic,
Component, and Product Profile** layers; **Channel/Platform outputs are generated
artifacts and are not independently normative** (DEC-S-079). Full model:
[Machine-Readable Source Model](../architecture/MACHINE_READABLE_SOURCE_MODEL.md).

### Reference and resolver model

CDS uses **two complementary reference mechanisms**:

- **Curly-brace `{group.token}`** is the **canonical token-to-token authoring**
  syntax, resolving the referenced token's `$value` within the resolvable source-set
  graph.
- **DTCG-conformant `$ref` / RFC 6901 JSON Pointer** references are the **required**
  form for document positions, property-level references, Resolver/Composition
  documents, Source-Set references, same-document resolver references, and controlled
  cross-file references — `$ref`/JSON Pointer is supported and required for these
  cases, not undecided and not unsupported in the resolver.

Cross-file references are permitted **only** when declared by the Source-Set Manifest
or Resolver graph, pointing to a known Source-Set identity, locally/offline
resolvable, and revision-/provenance-bound; an **undeclared or ad-hoc cross-file
reference fails closed**. Cycles, dangling/unresolvable references, type conflicts,
missing source sets, invalid layer dependencies, and unresolved overrides also **fail
closed** (DEC-S-078). Only the concrete **provenance-pointer form** remains open
(deferred to CDS-WP-012) — this does not mean JSON Pointer is generally undecided or
`$ref` unsupported. Full model:
[Token Reference, Resolution and Validation Model](../architecture/TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md).

### Extension boundary and namespace

CDS-specific metadata and governance data live **only** inside DTCG `$extensions`
under a CDS-reserved namespace; CDS must **not** redefine reserved DTCG semantics
(DEC-S-076). **Selected namespace root: `io.github.kaykaspers.cds`** — a stable,
single, reserved `$extensions` root key. **Rationale:** it is a collision-resistant
reverse-DNS-style key derived from the project's **repository identity**
(`github.com/kaykaspers/…`), so it is unique enough to avoid clashes **without**
asserting a registered commercial domain or brand of CDS's own (publication and
licensing remain undecided — DEC-S-046, DEC-S-047). It is used only inside
`$extensions`, project-/repository-scoped, tool-neutral, and must not replace token
meaning that DTCG fields already express. **Versioning:** the namespace key stays
stable; the later extension structure must carry a mandatory **`profileVersion`**
field. **Foreign extensions:** unknown/foreign `$extensions` from other tools are
**preserved** and are **not** automatically trusted or normative for CDS; only the
CDS-owned namespace may claim CDS profile metadata. **No extension payload, structure,
JSON example, metadata value, token file, or schema is defined or implemented here.**
A namespace change requires compatibility, migration, and a Human-Maintainer decision
(DEC-S-082).

### Validation layers

Four separate layers: **V1 Syntax** (RFC 8259) · **V2 DTCG 2025.10** · **V3 CDS
Profile** · **V4 Semantic and Governance**. A V1 pass proves no higher layer; a
schema pass is not complete correctness; a tool result is not human approval; no
numeric score; an unrun layer is `Not assessed`. Full model in the Reference,
Resolution and Validation Model.

### Determinism and offline boundary

Reproducible processing (same source revision + same transformation revision =
same logical output), no hidden network calls, no mandatory external registry, local
validatability, and pinnable spec/profile versions (DEC-S-080). **Canonicalization
decision state: open** — **RFC 8785 (JCS)** is *evaluated as a possible future
canonicalization basis* and **neither selected nor rejected** in this work package;
it is Informational, not a standard (S-11). No canonicalization is implemented.

## Consequences

### Positive

- Interoperable, tool-neutral, offline, human-reviewable, deterministic source
  format aligned with the five-layer flow and the class-1/class-2 authority split.
- A stable, implementation-ready external basis, with CDS governance retained.
- CDS metadata is expressible without polluting shared semantics.

### Trade-offs

- DTCG is a **CG report, not a W3C Standard**, and may evolve (RISK-055); pinning +
  upgrade governance manage this.
- The CDS profile and a future schema are ongoing maintenance for a small team
  (RISK-057, RISK-026).
- Some correctness (semantics, accessibility, governance) is **beyond schema reach**
  and needs V4 review (RISK-058).
- The `io.github.kaykaspers.cds` namespace is repository-identity-derived, not a
  registered commercial domain (deliberate; migratable under DEC-S-082).

### Rejected alternatives

B custom JSON (isolation/cost) · C YAML (non-determinism) · D JSONC/JSON5 (not
strict JSON) · E design-tool-native (lock-in) · F generated/CSS (authority
inversion) · G preview draft (unstable, "do not implement").

## Migration and upgrade boundary

No format upgrade is automatic. A change to the DTCG version binding, the profile,
the reference model, the extension model, or the validation contract is **Elevated**
and requires compatibility assessment, migration information, evidence, Nova review,
and explicit Human-Maintainer approval (DEC-S-082). Adopting a later DTCG report or
a preview feature is a controlled decision, never a silent one (DEC-S-074).

## Risks

RISK-055 … RISK-063 (version drift, preview contamination, profile divergence,
schema false assurance, reference-resolution failure, cross-layer violation,
identifier collision, provenance incompleteness, transformation-tool lock-in).
Registered in the [Risk Register](../risks/RISK_REGISTER.md).

## Follow-up implementation work package

**CDS-WP-012 — Machine-Readable Source Bootstrap and Validation Contract**: a
CDS profile JSON Schema, a source-set manifest schema, value-neutral fixtures,
positive/negative validation fixtures, reference/cycle tests, the layer-dependency
validation contract, an offline-validation boundary, a deterministic-serialization
decision, and provenance evidence — **still no real design values**. Prepared in the
[Machine-Readable Source Implementation Plan](../roadmap/MACHINE_READABLE_SOURCE_IMPLEMENTATION_PLAN.md).

## Authority and approval boundary

This ADR is a **proposal**. Nova reviews; the **Human Maintainer** accepts it by
commit. Claude selects no transformation, design, or build tool, creates no token
value or schema, promotes no artifact to Candidate or Stable, starts no pilot, makes
no claim, selects no licence, and performs no Git write. A clean diff is not
approval (DEC-S-048).
