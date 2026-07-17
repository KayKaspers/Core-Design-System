# Token Reference, Resolution and Validation Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-011 — Machine-Readable Source and Token Format Decision
- **Date:** 2026-07-16
- **Status:** **Normative** for token reference, resolution, and validation,
  **pending Human-Maintainer commit** of ADR-0001. It defines rules and a validation
  contract; it implements **no validator** and creates no token.

## Purpose

Defines how token references resolve across the CDS source sets and what must be
validated, so the five-layer flow (DEC-S-024) and the fail-closed authority model
(DEC-S-023, DEC-S-034) hold in the machine-readable source. Format detail is in the
[CDS Token Format Profile](CDS_TOKEN_FORMAT_PROFILE.md).

## Reference syntax decision

CDS uses **two distinct, complementary reference mechanisms**, each for a different
purpose (DEC-S-078). They are not alternatives to one another.

- **Canonical token-to-token authoring — curly-brace `{group.token}`.** The DTCG
  2025.10 alias form is the canonical syntax for **token-to-token references**: it
  resolves to the referenced token's **`$value`** within the resolvable source-set
  graph. It is the only normative alias encoding for token-to-token references (no
  alternative alias encoding is normative for this purpose).
- **JSON Pointer / `$ref` — document, property, resolver, and source-set
  references.** DTCG 2025.10-conformant **`$ref`** references and **RFC 6901 (JSON
  Pointer)** paths are the reference form for: **document positions**,
  **property-level references**, **Resolver/Composition documents**, **Source-Set
  references**, **same-document resolver references**, and **controlled cross-file
  references**. `$ref`/JSON Pointer is a **supported and required** reference form for
  these cases — it is not undecided and not unsupported in the resolver.

**Open point (bounded):** only the concrete **provenance-pointer form** — how a
provenance or evidence record byte-precisely identifies a position for traceability —
remains open and is deferred to CDS-WP-012. This open point does **not** mean JSON
Pointer is generally undecided, that `$ref` is unsupported in the resolver, or that
curly-brace is the only DTCG reference form.

## Canonical authoring syntax

Normative sources are authored and stored as **strict JSON `.tokens.json`**
(DEC-S-075). **Token-to-token references** are authored in the DTCG `{group.token}`
form (no alternative alias encoding is normative for token-to-token references).
**Document, property, resolver, and source-set references** use DTCG-conformant
`$ref` / RFC 6901 JSON Pointer as above.

## DTCG resolver relationship

Multi-context composition (e.g. light/dark themes) uses the **DTCG Resolver Module
2025.10**: reusable **sets** combined by conditional **modifiers** in a **defined
order**. Resolver and Source-Set references within and across resolver documents use
DTCG-conformant **`$ref` / RFC 6901 JSON Pointer** references (not curly-brace
aliases). The resolver selects and layers **approved values** for a context; it
introduces no new value or meaning and does not invert the downward dependency
direction (DEC-S-079).

## Cross-file reference boundary

A cross-file reference (curly-brace token-to-token across files, or `$ref`/JSON
Pointer to another document/source set) is permitted **only** when it is:

- **declared** by the Source-Set Manifest or Resolver graph;
- pointing to a **known Source-Set identity**;
- **locally / offline resolvable** — no hidden network dependency;
- **revision- and provenance-bound** (DEC-S-080).

An **ad-hoc or undeclared cross-file reference fails closed**. A reference to a source
set not in the manifest, or outside the approved dependency set, fails closed (missing
source set). No reference reaches into a consumer-local artifact (class 7) or a
generated output (class 3).

## Resolution order

1. Load the Source-Set Manifest; establish the declared set graph and dependency
   set.
2. Resolve **Reference → Semantic → Component → Product Profile** strictly downward.
3. Apply the Resolver/Composition document's modifiers in their **defined order**
   for the requested context.
4. Produce a resolved value set for generation; generated outputs (class 3) are then
   derived read-only.

Resolution is **deterministic**: same source revisions + same resolver + same
context = same resolved result (DEC-S-080).

## Alias chains

Alias chains (a semantic token referencing a reference token referencing …) are
permitted **only downward** and **only within** the declared dependency set. Every
link must resolve to a **type-compatible** target. A chain that leaves the declared
graph, rises a layer, or forms a cycle fails closed.

## Type compatibility

A reference must resolve to a value of a **compatible `$type`**. A component token
referencing a semantic token of an incompatible type is a **type conflict** and
fails closed (V2/V3).

## Cycle and dangling-reference handling

- **Cycle** (a reference path returning to its origin at any layer): **fail closed**.
- **Dangling reference** (a reference whose target does not exist): **fail closed**.
- **Missing source set** (a referenced set absent from the manifest): **fail
  closed**.
- **No automatic repair** — a failing state blocks transformation and distribution
  until corrected at the source (DEC-S-078, DEC-S-023).

## Layer validation

The downward dependency direction (DEC-S-079) is machine-checkable from the declared
layer and dependency-set metadata: any **upward dependency**, any
**component→reference bypass** of semantics, any **profile→core redefinition**, and
any **output→output** chain is a layer violation and fails closed.

## Validation layers

*(Normative — exactly four; DEC-S-078. No validator is implemented here.)*

### V1 — Syntax Validation
Strict JSON per RFC 8259; encoding; duplicate-key handling; file extension and file
identity (`.tokens.json`).

### V2 — DTCG 2025.10 Validation
Format Module (tokens, groups, `$value`/`$type`/`$description`/`$extensions`,
`{…}` references); Color Module (`colorSpace`/`components`); Resolver Module (sets,
modifiers, resolution) where applicable; DTCG token types and resolver semantics.

### V3 — CDS Profile Validation
Naming/identifier profile; source-set layer metadata; required governance metadata;
declared dependencies; Product-Profile bounds; maturity and approval state; the
`io.github.kaykaspers.cds` extension namespace boundary.

### V4 — Semantic and Governance Validation
Semantic layer direction; accessibility relevance (e.g. non-colour meaning,
invariant 10); status truth; compatibility; provenance completeness; Decision and
Requirement traceability; approved overrides only.

## Fail-closed conditions

Any of the following **blocks transformation and distribution** (DEC-S-023,
DEC-S-078); no automatic repair:

- invalid or malformed JSON;
- DTCG profile violation;
- missing mandatory metadata;
- unresolvable or dangling reference;
- reference cycle;
- backward (upward) layer dependency;
- illegal override (unapproved extension point);
- incompatible type (type mismatch);
- unknown source revision;
- conflicting source-set identity;
- missing source set;
- **undeclared or ad-hoc cross-file reference**;
- use of a non-approved draft/preview feature.

## Validation result vocabulary

`Pass` · `Pass with limitations` · `Fail` · `Blocked` · `Not assessed` ·
`Not applicable with rationale`.

Rules: a **V1 pass proves no V2/V3/V4 pass**; **JSON Schema does not cover all
semantic rules** (RISK-058); a **tool result is not human approval** (DEC-S-053
applied to format validation); **no numeric or aggregate score**; **an unrun layer
is `Not assessed`**, never assumed passed.

## No validator yet

**CDS-WP-011 implements no validator, no schema, and no resolver.** This document is
the contract those future artifacts must satisfy (CDS-WP-012). No token source exists
to validate; every future validation result is bound to an exact source revision and
profile version (DEC-S-080).

## Related documents

- [CDS Token Format Profile](CDS_TOKEN_FORMAT_PROFILE.md)
- [Machine-Readable Source Model](MACHINE_READABLE_SOURCE_MODEL.md)
- [Token Metadata, Provenance and Identity Model](TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md)
- [Token and Theme Architecture](TOKEN_AND_THEME_ARCHITECTURE.md)
- [ADR-0001](../decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
