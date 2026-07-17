# Offline Validator Dependency Source Register

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-013 — Offline Token Profile Validator and Fixture Harness
- **Date:** 2026-07-17
- **Status:** Research evidence, **not a normative source**. Findings are dated
  snapshots that decay; re-verify a source before relying on it (`docs/research/`
  rule). `latest` is not an identity (DEC-S-093).

## Purpose

Records every official source actually opened for the validator dependency decision
(ADR-0003), and the exact versions selected. Only the authorized official sources
were used: docs.python.org, pypi.org, python-jsonschema.readthedocs.io, and the
repository linked from the rfc8785 PyPI page. No blogs, forums, Stack Overflow,
comparison portals, unlinked forks, or popularity arguments.

## Opened official URLs

| # | URL | Purpose | Date opened |
| --- | --- | --- | --- |
| 1 | https://pypi.org/project/jsonschema/ | Current stable version, Python support, license, Draft 2020-12 support | 2026-07-17 |
| 2 | https://pypi.org/project/rfc8785/ | Current stable version, API, dependencies, license, official repository link | 2026-07-17 |
| 3 | https://python-jsonschema.readthedocs.io/en/stable/referencing/ | Local/offline `$ref` resolution via `referencing.Registry`; unretrievable-reference behavior | 2026-07-17 |
| 4 | https://github.com/trailofbits/rfc8785.py | API surface, `CanonicalizationError` semantics, canonicalization limitations (repository linked from the PyPI page) | 2026-07-17 |

Four URLs were opened in total. No further web source was used; the DTCG/standards
evidence from CDS-WP-011 remains the format basis.

## Runtime

- **Requirement:** Python **3.11 or later** (ADR-0003).
- **Executed runtime for the CDS-WP-013 evidence:** Python **3.12.10**
  (CPython, win32) — recorded in
  [wp013-fixture-results.json](../../artifacts/validation/wp013-fixture-results.json).

## Selected exact versions

### Direct dependencies

| Package | Exact version | Purpose | License (informational) | Runtime network |
| --- | --- | --- | --- | --- |
| `jsonschema` | **4.26.0** | JSON Schema Draft 2020-12 execution (`Draft202012Validator`, `check_schema`, local `referencing.Registry`) | MIT | none |
| `rfc8785` | **0.1.4** | RFC 8785 (JCS) canonical JSON serialization (`dumps`, `CanonicalizationError`) | Apache-2.0 | none (pure Python, zero dependencies) |

### Transitive dependencies (of `jsonschema`)

| Package | Exact version | Role |
| --- | --- | --- |
| `attrs` | 26.1.0 | Class machinery used by jsonschema |
| `jsonschema-specifications` | 2025.9.1 | Bundled meta-schemas (offline Draft 2020-12 support) |
| `referencing` | 0.37.0 | Local registry / `$ref` resolution |
| `rpds-py` | 2026.6.3 | Persistent data structures for referencing |
| `typing_extensions` | 4.16.0 | Typing backports |

All seven packages are pinned exactly in
[requirements-validator.lock](../../requirements-validator.lock).

## Offline behavior

- `jsonschema` 4.26.0 resolves Draft 2020-12 meta-schemas from the bundled
  `jsonschema-specifications` package and resolves CDS schema `$id`s through a local
  `referencing.Registry` — no HTTP retrieval occurs; an unretrievable reference
  raises an exception (fail closed) instead of fetching.
- `rfc8785` 0.1.4 is a pure-Python, zero-dependency implementation; all APIs raise
  `CanonicalizationError` (or a subclass) on unsupported input.
- After installation into the temporary environment, the validator was executed with
  no network access requirement.

## Known limitations

- `rfc8785` does not transparently convert non-string dictionary keys; strict JSON
  input (the only CDS input) cannot produce them.
- `rfc8785` produces minimal encoding only — this matches the ADR-0002
  authoring-versus-canonicalization boundary (authoring files stay indented).
- `jsonschema` validates structure only; V2 semantic DTCG checks and V4 governance
  checks live in the CDS validator itself (DEC-S-083, DEC-S-098).
- License names above are informational metadata from the official pages, **not** a
  CDS licensing decision (publication state stays `Private Development`).

## Upgrade triggers

Re-verify these sources and re-run the full harness when: a security advisory affects
any pinned package; the Python runtime is upgraded; a DTCG or JSON Schema binding
changes (DEC-S-082); or an offline-boundary regression is suspected (RISK-079).
Upgrades change the lock file only through a governed change with re-run evidence.
