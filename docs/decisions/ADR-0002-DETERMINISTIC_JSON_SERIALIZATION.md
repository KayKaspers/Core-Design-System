# ADR-0002 — Deterministic JSON Serialization

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-012 — Machine-Readable Source Bootstrap and Validation Contract
- **Status:** **Accepted upon Human-Maintainer commit following Nova approval.** Until
  commit, this ADR is a proposal. It creates no canonicalizer, computes no digest, and
  confers no Candidate or Stable status.
- **Date:** 2026-07-17
- **ADR number:** 0002 (number derived from the existing ADR set — ADR-0001 exists;
  0002 is the next free number, not invented)

## Context

CDS-WP-011 decided the machine-readable source format (DTCG 2025.10, strict JSON,
`.tokens.json`; ADR-0001) and required deterministic processing (DEC-S-031, DEC-S-080)
but deliberately left the **canonicalization / content-digest method open**. CDS-WP-012
implements the value-neutral schema and fixture bootstrap and must fix that method so a
future offline validator (CDS-WP-013) can compute reproducible content identity. RFC
8785 (JCS) was previously evaluated and neither selected nor rejected.

## Decision drivers

Reproducible content identity across implementations (RISK-067); offline, registry-free
computation (DEC-S-006, DEC-S-030); human-reviewable authoring preserved; a clear
boundary between an integrity digest and authenticity/approval (RISK-072); tool
neutrality (RISK-063).

## Considered alternatives

- **Raw source bytes only** — digest the authoring bytes. Rejected: whitespace/key-order
  differences would change identity for logically identical content; brittle and
  review-hostile.
- **Ad-hoc sorted JSON** — a home-grown sort/serialize. Rejected: unspecified,
  implementation-divergent, reinvents a solved problem.
- **RFC 8785 (JCS)** — **selected**. A specified canonicalization (I-JSON subset,
  ECMAScript number serialization, deterministic property sorting) with independent
  implementations; interoperable and offline.
- **Tool-specific serialization** — a design/build tool's serializer. Rejected: tool
  lock-in (DEC-S-004, RISK-063); a tool would become the identity authority.
- **No canonical digest** — rely on source revision only. Rejected: leaves content
  integrity/reproducibility unverifiable across copies (RISK-067).

## Decision

CDS adopts **RFC 8785 (JSON Canonicalization Scheme)** with **SHA-256** for canonical
content digests of CDS machine-readable JSON artifacts. Digest representation:
lowercase hexadecimal with the prefix **`sha256:`** (DEC-S-090). RFC 8785 is
Informational, adopted by explicit CDS decision, not as a standards mandate.

## Authoring versus canonicalization boundary

RFC 8785 governs the **canonical digest input**, computed from the parsed content —
**not** human authoring formatting. Authoring files stay indented, ordered, and
reviewable; a canonical digest is derived separately, so logically identical content
yields the same digest regardless of authoring whitespace or key order.

## Identity model

A complete future identity record binds: immutable source revision · source-set ID ·
CDS profile version · DTCG report version · canonicalization method (RFC 8785) · digest
algorithm (SHA-256) · content digest. See the
[Deterministic Serialization and Digest Model](../architecture/DETERMINISTIC_SERIALIZATION_AND_DIGEST_MODEL.md).

## Security and authenticity boundary

A content digest is an **integrity/reproducibility** aid only. It is **not** a digital
signature and proves **no** authorship, approval, trust, security posture, or release
legitimacy (RISK-072), and it **never** replaces the immutable source revision, approval,
or provenance evidence (DEC-S-080, DEC-S-090).

## Determinism consequence

Same source revision + same transformation revision ⇒ same canonical bytes ⇒ same
digest, computed identically by any conforming implementation.

## Offline consequence

Canonicalization and digest computation run locally, offline, with no external registry
or network call (DEC-S-030).

## Implementation deferral

CDS-WP-012 **decides the method only**. No productive canonicalizer is implemented, no
digest is computed or claimed as validated evidence, and no release manifest is produced.
Artifact digests are carried as `Not computed – validator implementation pending`.

## Risks

RISK-067 (canonicalization/digest mismatch), RISK-072 (digest mistaken for authenticity).

## Follow-up work package

**CDS-WP-013 — Offline Token Profile Validator and Fixture Harness**: implements the
offline validator (with duplicate-key detection), executes the validation cases,
implements RFC 8785 canonicalization and SHA-256 digest generation, and produces
machine-readable validation results under independent evidence review.

## Authority and approval boundary

This ADR is a **proposal**. Nova reviews; the **Human Maintainer** accepts it by commit.
Claude implements no canonicalizer or validator, computes no digest, selects no build/
transformation tool, creates no design value, promotes no artifact to Candidate or
Stable, makes no claim, and performs no Git write. A clean diff is not approval
(DEC-S-048).
