# Token Metadata, Provenance and Identity Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-011 — Machine-Readable Source and Token Format Decision
- **Date:** 2026-07-16
- **Status:** **Normative** for token/source-set identity, metadata, and provenance,
  **pending Human-Maintainer commit** of ADR-0001. It defines required identity; it
  implements **no extension structure** and creates no token.

## Purpose

Defines the identity, governance metadata, and provenance every normative source
set and generated output must carry, so traceability (DEC-S-031), fail-closed
authority (DEC-S-023), and provenance (RISK-025, RISK-062) hold in the
machine-readable source. CDS metadata is represented **only** through the approved
`io.github.kaykaspers.cds` `$extensions` namespace (DEC-S-076) — no structure is
implemented here.

## Source-Set Identity

*(Normative — required per normative source set; via the Source-Set Manifest and
`io.github.kaykaspers.cds` extensions)*

- Source-Set ID
- CDS Profile Version
- DTCG Report Version (pinned 2025.10)
- Source Revision (immutable)
- Maturity State
- Approval State
- Owner Role
- Layer (Reference / Semantic / Component / Product Profile)
- Dependency Set
- Product Profile (if applicable)
- Channel Scope (if applicable)

An identity missing any required element **fails closed** at V3 (RISK-062).

## Token governance metadata

*(Normative where applicable — per token, via `io.github.kaykaspers.cds` extensions)*

- stable technical ID (separate from display label; DEC-S-081)
- description
- type (`$type`)
- lifecycle or deprecation state
- originating Decision or Requirement (traceability)
- accessibility relevance (e.g. non-colour meaning, status truth)
- approved extension point (for Product Profile overrides)
- compatibility impact
- migration reference (on rename/removal)

## Extension ownership

All CDS metadata lives inside DTCG `$extensions` under the
**`io.github.kaykaspers.cds`** namespace (DEC-S-076): centrally documented in the
[CDS Token Format Profile](CDS_TOKEN_FORMAT_PROFILE.md), a collision-resistant
reverse-DNS-style key derived from the project's repository identity, versioned via a
mandatory `profileVersion` field, tool-neutral, and **not** a claim of a registered
commercial domain or brand (publication/licensing undecided — DEC-S-046, DEC-S-047).
CDS never places metadata outside `$extensions` and never redefines reserved DTCG
properties. **Only** the CDS-owned namespace may claim CDS profile metadata;
**foreign/unknown `$extensions` from other tools are preserved but are not
automatically trusted or normative for CDS.** A namespace change requires
compatibility, migration, and a Human-Maintainer decision (DEC-S-082).

## Provenance chain

*(Normative; DEC-S-031, DEC-S-080)*

- **immutable Source Revision** for every normative source set
- **source file identity** (`.tokens.json` document identity)
- **transformation revision** for every generated output
- **generated-output identity** bound to its source and transformation revisions
- **validation evidence identity** bound to the source revision and profile version
- **`latest` is never a sufficient evidence identity**
- **no secrets or personal data** in any token source, metadata, or provenance
  record (privacy/data-minimization)

A break anywhere in the chain breaks traceability; distributing an output without
provenance is a defect (RISK-025, RISK-062).

## Source revision

Every normative source set is bound to an **immutable source revision**. Evidence,
generated outputs, and claims reference a specific revision — never a moving target.
A rebuild must not silently reuse an identifier with different content (DEC-S-038
applied to token sources).

## Profile and DTCG version

Every source set records both the **CDS Profile Version** and the **DTCG Report
Version** (2025.10) it conforms to. These are independent of a CDS release version.
A change to either binding is Elevated and governed (DEC-S-082).

## Transformation identity

Every generated output records the **transformation revision** that produced it, so
that same source revision + same transformation revision = same logical output
(DEC-S-080). A generated output is class-3 and never normative.

## Output identity

A generated output carries an identity binding it to its source revision(s),
transformation revision, resolver/context (if applicable), and channel scope. An
output whose origin cannot be established is treated as a defect, not a source
(RISK-025).

## Maturity and approval

Every normative source set carries a **maturity state** (per the
[Artifact Maturity Lifecycle](../governance/ARTIFACT_MATURITY_LIFECYCLE.md)) and an
**approval state**. **No source set is Candidate or Stable**, and none is approved,
by this work package — none exists. Maturity, release version, and publication state
remain separate axes (DEC-S-035).

## Compatibility and migration references

A source set records its **compatibility impact** and, on rename/removal/breaking
change, a **migration reference** (DEC-S-039, DEC-S-040 applied to token sources).
No format or profile upgrade is automatic (DEC-S-082).

## Privacy and secret exclusions

Token sources, metadata, provenance records, and generated outputs **must not
contain secrets or personal data**. Provenance identifies revisions and
transformations, not people or credentials.

## Deterministic-identity requirements

Identity is reproducible: the same source content at the same revision yields the
same logical identity; provenance and output identity are computable offline with no
external registry (DEC-S-030, DEC-S-080).

## Canonicalization decision state

- A **deterministic serialization / canonicalization** mechanism is required for
  reproducible hashing and output identity, but the concrete mechanism is
  **open**.
- **RFC 8785 (JSON Canonicalization Scheme)** is **evaluated as a possible future
  basis** and is **neither selected nor rejected** in CDS-WP-011; it is Informational,
  not a standard (Source Register S-11). The decision is deferred to CDS-WP-012.

## Related documents

- [Machine-Readable Source Model](MACHINE_READABLE_SOURCE_MODEL.md)
- [CDS Token Format Profile](CDS_TOKEN_FORMAT_PROFILE.md)
- [Token Reference, Resolution and Validation Model](TOKEN_REFERENCE_RESOLUTION_AND_VALIDATION_MODEL.md)
- [Evidence, Traceability and Status Semantics](EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md)
- [ADR-0001](../decisions/ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md)
