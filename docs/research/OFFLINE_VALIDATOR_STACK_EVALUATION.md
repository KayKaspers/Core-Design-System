# Offline Validator Stack Evaluation

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-013 — Offline Token Profile Validator and Fixture Harness
- **Date:** 2026-07-17
- **Status:** Research evidence, **not a normative source**. The binding decision is
  [ADR-0003](../decisions/ADR-0003-OFFLINE_TOKEN_VALIDATOR_IMPLEMENTATION_STACK.md).

## Question

Which minimal, offline-capable, auditable stack executes the committed CDS validation
contracts (JSON Schema Draft 2020-12, RFC 8785 + SHA-256, V1–V4) without selecting a
productive transformer, build system, or design-token toolchain?

## Constraints applied

- Only already-decided standards get third-party implementations (DEC-S-077,
  DEC-S-090); everything else is standard library.
- No runtime network access; no dynamic registry; no telemetry (DEC-S-093, RISK-079).
- Exact pins; `latest` is not an identity; no vendoring.
- Duplicate-key rejection must live at the parser (DEC-S-088, DEC-S-095).
- No tool becomes a source of truth (DEC-S-004, RISK-063).

## Evaluation

| Option | Standards fidelity | Supply-chain surface | Offline | Verdict |
| --- | --- | --- | --- | --- |
| Pure stdlib (re-implement JSON Schema + JCS) | Low (untested standards code) | None | Yes | Rejected — correctness risk exceeds dependency risk |
| Python + pinned `jsonschema` + pinned `rfc8785` | High (dedicated, focused implementations) | 2 direct + 5 transitive, all pinned | Yes (verified) | **Selected (ADR-0003)** |
| Node.js/ajv | High for schema; no JCS pairing | Large transitive tree; second runtime | Yes | Rejected |
| Design-token toolchain | Indirect | Large; couples validation to a tool | Varies | Rejected — prohibited direction (DEC-S-004) |
| jsonschema + raw-byte digests (no rfc8785) | Violates ADR-0002 | Smaller | Yes | Rejected |

## Selected stack (summary)

- Python ≥ 3.11 (executed: 3.12.10) · `jsonschema==4.26.0` · `rfc8785==0.1.4` ·
  `unittest` · entry point `python -m tools.cds_validator`.
- Full provenance and transitive pins: see the
  [Dependency Source Register](OFFLINE_VALIDATOR_DEPENDENCY_SOURCE_REGISTER.md) and
  [requirements-validator.lock](../../requirements-validator.lock).

## License metadata (informational only)

MIT (`jsonschema`, `attrs`, `referencing`, `rpds-py` — per their official pages) and
Apache-2.0 (`rfc8785`). This is dependency metadata for provenance, **not** a CDS
licensing or publication decision; no CDS artifact license is selected and the
publication state remains `Private Development` (DEC-S-046 ff.).

## Known limitations of the selected stack

- `jsonschema` proves structure only; a schema pass is not correctness (DEC-S-083).
- The CDS V2 layer implements a bounded DTCG subset (DEC-S-098); the stack does not
  provide DTCG semantics out of the box.
- `rfc8785` rejects non-JSON-serializable input with `CanonicalizationError` — the
  controlled failure the digest contract requires (DEC-S-100).
- Reproducibility across environments is contract-bound, not guaranteed by the stack
  (RISK-075): reports bind exact runtime/dependency identities.

## Upgrade governance

Any version change re-runs the full unit-test suite and 15-case harness, re-verifies
the offline boundary, and updates the lock and the source register — as a governed
change with Nova review (DEC-S-082, ADR-0003). No `latest`, no floating ranges.
