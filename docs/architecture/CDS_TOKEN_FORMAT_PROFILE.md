# CDS Token Format Profile

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-011 — Machine-Readable Source and Token Format Decision
- **Date:** 2026-07-16
- **Status:** **Normative** for the CDS token format profile, **pending
  Human-Maintainer commit** of ADR-0001. It constrains a format; it defines **no
  token value, name, colour, typography, spacing, or size**.

## Profile identity

- **Profile:** CDS Token Format Profile
- **Profile version:** `1` (initial; versioned independently of a CDS release)
- **External basis:** DTCG 2025.10 (Final Community Group Report; **not** a W3C
  Standard) — DEC-S-073
- **Authority:** a class-2 normative machine-readable constraint over DTCG; meaning
  stays in class-1 sources (DEC-S-022)

## Pinned DTCG version and modules

- **Pinned:** DTCG **2025.10** — the only authoritative version for this profile
  (DEC-S-074).
- **Applicable modules:** Format Module 2025.10; Color Module 2025.10; Resolver
  Module 2025.10 (where applicable).
- **Preview boundary:** preview/draft/editor/future reports are **not** part of this
  profile and must not be implemented or documented as if they were (DEC-S-074,
  RISK-056).

## Strict JSON and file extension

- Normative source documents are **strict JSON per RFC 8259** (DEC-S-075).
- **File extension:** `.tokens.json` for normative token documents; a Source-Set
  Manifest and a Resolver/Composition document are also strict JSON with a
  CDS-documented extension to be fixed at implementation (not selected here).
- **Prohibited as normative sources:** YAML, JSONC, JSON5, JS/TS modules,
  design-tool exports, CSS custom properties, Sass variables, generated platform
  formats. These are at most **authoring input** or **generated output**, reconciled
  to strict JSON before they could ever be normative (DEC-S-026).

## Naming and identifier profile

*(Machine-validatable; DEC-S-081. No real token name is created.)*

- **Technical identifiers** (stable, machine-facing) are **separate** from
  **display labels** (human-facing, in `$description` / a CDS extension).
- **Segment syntax:** a technical identifier is a **dot-free** segment within a DTCG
  group hierarchy; the full path is the ordered group chain plus the token segment.
  Each segment: `^[a-z][a-z0-9-]*$` (lower-case start, lower-case alphanumerics and
  single hyphens), machine-checkable.
- **Prohibited:** names differing only by case (case-only collisions); leading or
  trailing whitespace; empty path segments; reserved DTCG characters (`{`, `}`, `.`
  inside a segment, `$`-prefix); tool- or platform-specific prefixes in shared
  semantics; an appearance/colour or product-implementation name where a semantic
  role is meant (semantic-first, DEC-S-024).
- **Renames** are a migration event with a migration reference (DEC-S-082); an
  identifier is not silently repurposed.

## Group and token restrictions

- Tokens and groups follow the DTCG Format Module: a token is an object with a
  required `$value`; groups nest tokens hierarchically.
- **`$type`** is required on every CDS token (explicit typing; no reliance on
  inheritance-only typing) at the profile level.
- Semantic-first: a component source set **binds** semantic tokens and introduces no
  new meaning or raw value; a component token referencing a reference token directly
  is a profile violation (Token Architecture, prohibited shortcut).

## Allowed DTCG properties

The reserved DTCG `$`-properties are used **as defined**, never redefined
(DEC-S-076): `$value`, `$type`, `$description`, and `$extensions`. Color tokens use
the Color Module's `colorSpace` + `components` (+ optional `alpha`, `hex`) as
defined — CDS selects **no** colour value here.

## CDS `$extensions` boundary

*(Normative)*

- All CDS-specific metadata and governance data live **only** inside DTCG
  `$extensions`, under the CDS namespace (below). CDS never introduces unknown
  top-level or token-level properties outside `$extensions` (DEC-S-076).
- CDS extensions are **additive**: a DTCG-only tool that ignores them still reads a
  valid token. CDS validation (V3/V4) enforces what a generic tool cannot
  (RISK-057).

## Selected extension namespace

- **Namespace root:** **`io.github.kaykaspers.cds`** — the single stable, reserved
  root key for CDS-specific DTCG `$extensions`.
- **Collision resistance:** the reverse-DNS-style key is derived from the project's
  repository identity (`github.com/kaykaspers/…`), making it collision-resistant
  without asserting a **commercial** domain of CDS's own; it does not claim ownership
  of a registrable brand or product domain, and publication/licensing remain undecided
  (DEC-S-046, DEC-S-047).
- **Usage bounds:** used **only** inside DTCG `$extensions`; project- and
  repository-scoped; **not tool-bound**; it must **not** redefine a reserved DTCG
  property and must **not** replace token meaning that DTCG fields already express.
- **Versioning:** the namespace **key stays stable**; the later extension structure
  must carry a mandatory **`profileVersion`** field. The full payload structure,
  concrete JSON examples, real metadata values, token files, and schema definitions
  are **not** defined or implemented here.
- **Foreign extensions:** unknown/foreign `$extensions` from other tools **must be
  preserved**; they are **not** automatically trusted or normative for CDS. **Only**
  the CDS-owned `io.github.kaykaspers.cds` namespace may claim CDS profile metadata.
- **Change control:** a namespace change requires a compatibility, migration, and
  Human-Maintainer decision (DEC-S-082).

## Type handling

- Every CDS token declares an explicit `$type` from the DTCG-defined types
  applicable to CDS scope; unknown or CDS-unsupported types **fail closed** at V3.
- Type compatibility across references is enforced (a reference must resolve to a
  compatible type) — detail in the
  [Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md).

## Source-Set layer metadata

Every normative source set declares its **layer** (Reference / Semantic / Component
/ Product Profile) and its **dependency set** via CDS `$extensions` and the
Source-Set Manifest, so the downward-dependency rule (DEC-S-079) is machine-checkable.

## Product Profile constraints

A Product Profile Source Set overrides **only named, approved extension points**
(DEC-S-025, DEC-S-043); it may not redefine shared semantics, weaken accessibility
(invariant 10), distort status truth, or break contracts. A profile needing a
prohibited change is a **fork**, named as one.

## Unsupported and prohibited features

- Preview/draft DTCG features (DEC-S-074).
- Redefinition of reserved DTCG semantics (DEC-S-076).
- Unknown properties outside `$extensions`.
- Non-strict-JSON source encodings (DEC-S-075).
- Generated output treated as a normative source (DEC-S-079).
- Colour as sole meaning carrier at any layer (CR-006).
- Design tool as the token source of truth (DEC-S-004).

## Profile versioning

The CDS profile version is independent of a CDS release version and of the DTCG
report version. A change to the profile, the DTCG binding, the naming rule, the
extension model, or the validation contract is **Elevated** and requires
compatibility, migration, evidence, Nova review, and Human-Maintainer approval
(DEC-S-082). No upgrade is automatic.

## No current token

**This profile defines no token, no group instance, no colour, no typography, no
spacing, and no size.** No `.tokens.json` source exists. It is a format constraint,
awaiting an authorized implementation work package (CDS-WP-012). No artifact is
Candidate or Stable.

## Related documents

- [Machine-Readable Source Model](MACHINE_READABLE_SOURCE_MODEL.md)
- [Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
- [Token Metadata, Provenance and Identity Model](TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md)
- [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md)
- [ADR-0001](../decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
