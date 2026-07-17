# Token Format Evaluation

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-011 — Machine-Readable Source and Token Format Decision
- **Date:** 2026-07-16
- **Status:** **Research evidence — NON-normative.** Explains *why* the format
  decision is what it is. The binding decision lives in
  [ADR-0001](../decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) and the
  normative profile, and takes effect only on Human-Maintainer commit. **No numeric
  score is used** (a single disqualifying property outweighs many minor advantages).

## Methodology

1. Read the committed token and authority architecture
   ([Token and Theme Architecture](../architecture/TOKEN_AND_THEME_ARCHITECTURE.md),
   [Source of Truth and Authority Model](../architecture/SOURCE_OF_TRUTH_AND_AUTHORITY_MODEL.md)).
2. Opened only official standards/specification sources
   ([Source Register](TOKEN_FORMAT_SOURCE_REGISTER.md)); separated stable (DTCG
   2025.10) from preview drafts.
3. Derived CDS requirements from architecture, governance, and consumer needs.
4. Compared seven options qualitatively against fourteen criteria; selected one.
5. Chose no design value, no naming instance, no transformation tool, and no build
   tool.

## CDS requirements the format must satisfy

- **Interoperability** with external tools without becoming their captive
  (DEC-S-004, RISK-004).
- **Human reviewability** — meaning arguable in a diff without a proprietary tool
  (Source of Truth, class 1/2 split).
- **Tool neutrality and offline use** — no mandatory external runtime or registry
  (DEC-S-006, DEC-S-030).
- **Deterministic processing** — same source + same transformation = same output
  (DEC-S-031, invariant on generated artifacts).
- **Reference/alias support** honoring the five-layer downward flow (DEC-S-024).
- **Metadata extensibility** for CDS governance without redefining shared semantics
  (DEC-S-022, DEC-S-025).
- **Machine-checkable validation** — cycles, orphans, layer/override violations,
  provenance (Token Architecture validation table).
- **Provenance and versioned identity** — no `latest` as identity (DEC-S-031).
- **Capacity fit** — runnable and reviewable by a very small team (RISK-026,
  RISK-029).

## Evaluation criteria

Interoperability · Standards Stability · Tool Neutrality · Human Reviewability ·
Deterministic Processing · Offline Use · Validation · Reference Resolution ·
Metadata Extensibility · Migration Cost · Lock-in Risk · Maintainer Capacity ·
Provenance · Alignment with CDS Architecture.

## Options

### Option A — DTCG 2025.10 Strict JSON Profile — **selected**

Adopt the stable DTCG 2025.10 reports (Format, Color, Resolver) as the external
format basis, expressed in strict RFC 8259 JSON, constrained by a CDS profile.

- **Advantages:** vendor-neutral, tool-supported interchange; a **stable** Final
  Community Group Report intended for implementation; built-in groups, `$type`,
  `{group.token}` references, and `$extensions` for CDS metadata; plain JSON is
  human-reviewable, diffable, deterministic, and offline-validatable; aligns
  directly with the five-layer flow and the class-1/class-2 authority split.
- **Disadvantages:** DTCG is a **CG report, not a W3C Standard** (S-02), so it
  carries no formal standards-body guarantee and may evolve (RISK-055); CDS must
  own its profile and a schema; some semantic rules exceed what a schema can check
  (RISK-058).
- **Interoperability:** high. **Validation:** JSON + schema + CDS + governance
  layers. **Offline/Tool-neutral:** yes. **Migration/Capacity:** low migration
  (nothing built yet); moderate ongoing profile maintenance.
- **Result:** selected — best alignment with architecture, interoperability, and
  reviewability at acceptable, visible cost.

### Option B — Fully custom CDS JSON format — rejected

- **Advantages:** total control; exact fit to CDS architecture.
- **Disadvantages:** zero external interoperability; reinvents groups, references,
  color, theming; high build and maintenance cost for a tiny team (RISK-026); no
  ecosystem tooling; **lock-in to a bespoke format** with no migration path in.
- **Result:** rejected — control does not justify isolation and cost.

### Option C — YAML as the normative source — rejected

- **Advantages:** concise, comment-friendly authoring.
- **Disadvantages:** YAML's implicit typing and multiple representations undermine
  **deterministic processing** and safe parsing; weaker interoperability with DTCG
  tooling; harder to validate canonically; not the DTCG interchange form.
- **Result:** rejected — non-normative authoring input at most, never the source.

### Option D — JSONC or JSON5 as the normative source — rejected

- **Advantages:** comments and trailing commas ease authoring.
- **Disadvantages:** not strict JSON (RFC 8259); non-interoperable with standard
  JSON/DTCG tooling; ambiguous canonicalization; comments invite out-of-band
  meaning that escapes governance.
- **Result:** rejected — not a normative source; possible authoring convenience
  only, reconciled to strict JSON.

### Option E — Design-tool-native format — rejected

- **Advantages:** direct authoring in a design tool.
- **Disadvantages:** violates DEC-S-004 and invariant 4 (a tool must not be the
  sole truth); proprietary, non-portable, non-diffable; **maximum lock-in** and
  provenance loss (RISK-004, RISK-063).
- **Result:** rejected — a class-5 authoring representation, never normative.

### Option F — Generated code or CSS as the normative source — rejected

- **Advantages:** immediately consumable by products.
- **Disadvantages:** inverts the authority model — a **generated artifact (class 3)
  would become the source**, which is prohibited (Source of Truth, invariant 1);
  strips meaning; unreviewable as intent; no provenance to a real source.
- **Result:** rejected — outputs are derived, never normative.

### Option G — Current DTCG preview draft — rejected

- **Advantages:** newest features.
- **Disadvantages:** the preview drafts explicitly state **"do not implement … do
  not reference as authoritative"** (S-08); adopting them would contaminate the
  stable basis (RISK-056) and pin CDS to shifting, unstable behavior.
- **Result:** rejected as a basis; retained **only** for future-change awareness
  and migration planning (DEC-S-074).

## Selected option and rationale

**Option A.** DTCG 2025.10 (Format, Color, Resolver) as the external normative
basis, in strict JSON, under a CDS profile, is the only option that is
simultaneously interoperable, stable, tool-neutral, offline-validatable,
human-reviewable, and architecturally aligned — while keeping meaning in class-1
sources and values in class-2 sources. Its principal cost (a CG report that may
evolve, and semantic rules beyond schema reach) is **managed**, not eliminated, by
pinning 2025.10 (DEC-S-074), a four-layer validation contract, and upgrade
governance (DEC-S-082).

## Rejected alternatives (summary)

B (isolation/cost) · C (non-determinism) · D (not strict JSON) · E (tool lock-in) ·
F (authority inversion) · G (unstable preview).

## Interoperability limits

DTCG conformance is **not** a CDS quality, semantic, or accessibility statement.
Interoperability is bounded by each external tool's own DTCG support, by the CDS
profile's added constraints (which a generic DTCG tool will not enforce —
RISK-057), and by the fact that CDS `$extensions` are ignored by tools that do not
understand them.

## Maintainer-capacity effects

Adopting a supported external format **reduces** build cost versus a bespoke format
(Option B) and keeps sources reviewable in plain diffs. Ongoing cost is the CDS
profile, a future schema, and version-drift watch (RISK-055) — bounded and
deferred to implementation.

## Profile risks

RISK-055 (version drift) · RISK-056 (preview contamination) · RISK-057 (profile
divergence from DTCG) · RISK-058 (schema false assurance) · RISK-059 (reference
resolution failure) · RISK-060 (cross-layer violation) · RISK-061 (identifier
collision) · RISK-062 (provenance incompleteness) · RISK-063 (transformation-tool
lock-in).

## Preview and future-spec boundary

Only the pinned 2025.10 reports are authoritative (DEC-S-074). Preview/draft and
future reports are research inputs until a controlled compatibility and migration
decision accepts them (DEC-S-082). No preview feature may be implemented or
documented as part of the stable profile (RISK-056).

## Unresolved implementation questions

- Exact CDS profile JSON Schema shape and the source-set manifest schema.
- Concrete reference/pointer identity form (DTCG `{…}` alias vs RFC 6901 pointer for
  cross-artifact provenance).
- Whether RFC 8785 (JCS) is adopted for canonical serialization, or another
  deterministic scheme — deliberately left open here (DEC-S-080).
- Repository topology and file layout for source sets (not selected — DEC-S-032).
- Which validations run in which pipeline and what blocks (implementation phase).

## Related documents

- [Token Format Source Register](TOKEN_FORMAT_SOURCE_REGISTER.md)
- [ADR-0001 — Machine-Readable Token Source Format](../decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
- [Machine-Readable Source Model](../architecture/MACHINE_READABLE_SOURCE_MODEL.md)
- [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md)
