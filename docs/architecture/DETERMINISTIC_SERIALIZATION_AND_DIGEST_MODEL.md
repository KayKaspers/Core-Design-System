# Deterministic Serialization and Digest Model

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-012 — Machine-Readable Source Bootstrap and Validation Contract
- **Date:** 2026-07-17
- **Status:** **Normative** for the canonicalization and content-digest method,
  **pending Human-Maintainer commit** of CDS-WP-012 and ADR-0002. It decides a
  *method*; it **implements no canonicalizer** and computes no digest. Full decision
  record: [ADR-0002](../decisions/ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md).

## Purpose

Determinism was left open by CDS-WP-011 (DEC-S-080). CDS needs reproducible content
identity so that the same logical JSON content yields the same identity across
implementations, offline, without ambiguity (RISK-067). This model fixes the method.

## Decision

- **Canonicalization:** **RFC 8785 — JSON Canonicalization Scheme (JCS)** is the basis
  for canonical content digests of CDS machine-readable JSON artifacts (DEC-S-090).
- **Digest algorithm:** **SHA-256**.
- **Digest representation:** lowercase hexadecimal, prefixed **`sha256:`**.

RFC 8785 is an Informational RFC (not a Standards-Track standard); it is adopted here
as CDS's deterministic-serialization method by explicit decision, not as a standards
mandate.

## Authoring versus canonicalization boundary

- **RFC 8785 does not govern human authoring formatting.** Authoring `.tokens.json`,
  `.source-set.json`, and `.resolver.json` files remain indented, reviewable, and
  sensibly ordered for humans and diffs.
- The **canonical digest is computed separately from the parsed content**, not from
  the authoring bytes. Two authoring files that differ only in whitespace or key order
  but parse to the same logical content have the **same** canonical digest.

## Identity model

A complete (future) identity record for a machine-readable artifact contains:

- immutable **Source Revision**;
- **Source-Set ID**;
- **Profile Version** (CDS profile);
- **DTCG Report Version** (2025.10);
- **Canonicalization Method** (RFC 8785 / JCS);
- **Digest Algorithm** (SHA-256);
- **Content Digest** (`sha256:` + lowercase hex).

## Digest boundary

The content digest:

- **does not replace** the immutable Source Revision (DEC-S-080);
- **is not a digital signature** and proves no authorship;
- **proves no approval, trust, security, or release legitimacy** (RISK-072);
- **proves no semantic, accessibility, or governance correctness**;
- **creates no Candidate, Stable, or claim status**.

It is a reproducibility and integrity aid — same logical content ⇒ same digest —
nothing more.

## Offline and determinism consequences

Canonicalization and digest computation must run **locally, offline, with no external
registry or network call** (DEC-S-006, DEC-S-030). Same source revision + same
transformation revision ⇒ same canonical bytes ⇒ same digest.

## WP-012 boundary

In CDS-WP-012 the **method is decided**; **no productive canonicalizer is
implemented**, **no digest is claimed as validated evidence**, and **no release
manifest is produced**. Fixture and artifact digests are therefore carried as:

> **`Not computed – validator implementation pending`**

Implementing the canonicalizer, computing digests, and producing digest evidence are
**CDS-WP-013**.

## Risks

RISK-067 (canonicalization/digest mismatch across implementations) and RISK-072
(digest mistaken for authenticity), registered in the
[Risk Register](../risks/RISK_REGISTER.md).

## Change control

Elevated; a change to the canonicalization method or digest algorithm requires
compatibility, migration, evidence, Nova review, and Human-Maintainer approval
(DEC-S-082, DEC-S-090).

## Related documents

- [ADR-0002 — Deterministic JSON Serialization](../decisions/ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md)
- [Token Metadata, Provenance and Identity Model](TOKEN_METADATA_PROVENANCE_AND_IDENTITY_MODEL.md)
- [Machine-Readable Validation Contract](MACHINE_READABLE_VALIDATION_CONTRACT.md)
- [Machine-Readable Source Model](MACHINE_READABLE_SOURCE_MODEL.md)
