# Semantic Status Token Contract

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-014 — Semantic Status Foundation Contract and First
  Candidate Plan
- **Date:** 2026-07-17
- **Status:** **Normative** role contract for the future machine-readable
  Semantic Status source set, pending Human-Maintainer commit. Experimental; no
  Candidate status. **No token source file, no token name as a shipped
  identifier, and no token value exists or is created here.**

## Semantic role boundary

*(Normative — Token and Theme Architecture, layer 2; DEC-S-024)*

Semantic status tokens represent **roles and meanings** — never concrete
colours, icons, or other appearance values:

- A semantic status token expresses *which status meaning a representation
  binds to*, not *how it looks*.
- **Appearance-derived names are prohibited** where a semantic role is meant
  (naming profile, DEC-S-081; prohibited shortcut 4): no colour word, icon
  name, or visual metaphor may serve as the semantic identity of a status.
- Raw values live only in the Reference layer; a semantic status token never
  carries a raw value of its own and a consumer never binds to a reference
  token directly (prohibited shortcuts 1–2).

## Relationship to the five axes

*(Normative — DEC-S-105, DEC-S-112)*

- Every axis remains **distinguishable** in the token contract: the future
  token structure must let a representation bind `condition`, `severity`,
  `confidence`, `freshness`, and `evidence` meanings independently.
- **A token must not irreversibly aggregate multiple axes.** A convenience
  binding that composes axes may exist only if the constituent axis meanings
  remain individually addressable and recoverable (invariants 1–2).
- The 25 axis values of the
  [Status Axis Vocabulary](STATUS_AXIS_VOCABULARY.md) are the complete initial
  semantic value space; a token may not introduce a 26th status meaning.
- Unknown-, stale-, unverified-, and evidence-limitation semantics must
  survive every token mapping (DEC-S-107, invariant 9).

## Planned source set

*(A plan, not an implementation — no file, no topology, no token is created.)*

| Property | Planned value |
| --- | --- |
| Layer | **Semantic** (source-set layer `semantic`) |
| Purpose | Status meaning contracts (roles for the five axes and their 25 values) |
| DTCG binding | **2025.10** (pinned; Format/Color/Resolver per ADR-0001) |
| CDS profile | **Version 1** (strict JSON `.tokens.json`, `io.github.kaykaspers.cds` payload) |
| Maturity at creation | **Experimental** |
| Candidate | **Not in CDS-WP-014** — per the [Candidate Plan](../roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md) gates |

Technical token identifiers will follow the CDS naming profile
(`^[a-z][a-z0-9-]*$` segments, no case-only collisions, technical IDs separate
from display labels — DEC-S-081, DEC-S-110). **No concrete token name is
reserved or shipped by this contract**; names are created only inside the
future source set under validator coverage.

## Component reference boundary

- Component tokens **may reference** semantic status tokens (layer 3 binds
  layer 2 — DEC-S-024).
- Component tokens **must not redefine** status meaning: a component token
  introducing a status meaning absent from the semantic layer is a defect
  (prohibited shortcut 3).
- Components must not bypass the semantic layer into reference values for
  status purposes (layer-direction rules; validator-enforced later).

## Product Profile boundary

Product Profiles adjust **approved extension points only** (DEC-S-025,
DEC-S-043): they may vary *presentation bindings* at named extension points but
must never rename, merge, remap, reweight, or suppress a status meaning, never
weaken an accessibility obligation, and never distort truth (invariant 10;
RISK-088). An override standing in for a missing semantic status role is a gap
in the core, to be raised — not profiled around (prohibited shortcut 6).

## Generated-output boundary

Channel and platform outputs generated from the future source set are
**class-3 generated artifacts** — never normative, never hand-edited, always
provenance-carrying (DEC-S-031, DEC-S-079). Unknown-, stale-, unverified-, and
evidence-limitations must be preserved in **all** generated outputs; a
transformation that collapses axes or drops qualifiers fails closed
(DEC-S-112).

## DTCG / CDS profile binding

The future source set is a normative machine-readable source under the
[CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md):
strict JSON `.tokens.json`, DTCG 2025.10 pinned, the
`io.github.kaykaspers.cds` extension payload (profileVersion, sourceSetId,
layer `semantic`, revision, manifest binding), curly-brace token-to-token
references, `$ref`/RFC-6901 for document/manifest/resolver references, and
fail-closed reference rules (DEC-S-073…082, DEC-S-091).

## No current token

**Update (CDS-WP-015):** the planned source set is now implemented as
[`semantic/status`](../../tokens/semantic/status/semantic-status.tokens.json)
(Experimental, Unapproved; 5 axis groups, 25 non-visual tokens, manifest and
resolver; DEC-S-115…116). Everything below documents the CDS-WP-014 state it
constrained and remains the binding contract for that source set; **the tokens
carry identity values only — still no visual value, and no Candidate status.**

**As of CDS-WP-014 no semantic status token exists.** No `.tokens.json` source,
no token name, no token value, no manifest entry, and no resolver step for
status semantics has been created. This contract constrains what the future
source set must be; it is not that source set.

## No value

This contract binds **no visual or numeric value** to any status meaning — no
colour, icon, typography, spacing, size, duration, easing, or theme. Value
decisions require a later, explicitly authorized design work package and are
excluded from the first Candidate scope.

## Planned validation requirements

The future source set must pass the committed validation contract before any
maturity step (DEC-S-114):

- **V1–V4** via the offline validator (`python -m tools.cds_validator`),
  including schema execution, manifest/resolver binding, and layer rules;
- **positive fixtures** for representative axis-role bindings and **negative
  fixtures** for at least: axis aggregation, unknown-as-default mapping,
  appearance-derived naming, undeclared cross-references, and
  meaning-losing remappings;
- validation-case coverage with committed expected outcomes and
  machine-readable execution evidence (RFC 8785 + SHA-256 digests);
- independent Evidence Review of the results (executor ≠ reviewer,
  DEC-S-103).

## Related documents

- [Semantic Status Foundation Contract](SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
- [Status Axis Vocabulary](STATUS_AXIS_VOCABULARY.md)
- [Token and Theme Architecture](../architecture/TOKEN_AND_THEME_ARCHITECTURE.md)
- [CDS Token Format Profile](../architecture/CDS_TOKEN_FORMAT_PROFILE.md)
- [Machine-Readable Validation Contract](../architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)
- [First Semantic Status Candidate Plan](../roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md)
