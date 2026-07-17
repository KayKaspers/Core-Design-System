# ADR-0003 — Offline Token Validator Implementation Stack

- **Status:** **Accepted upon Human-Maintainer commit following Nova approval.** Until
  that commit, this ADR is a decision record pending final human approval; no earlier
  wording confers acceptance.
- **Date:** 2026-07-17
- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-013 — Offline Token Profile Validator and Fixture Harness
- **Related:** [ADR-0001](ADR-0001-MACHINE_READABLE_TOKEN_SOURCE_FORMAT.md) ·
  [ADR-0002](ADR-0002-DETERMINISTIC_JSON_SERIALIZATION.md) ·
  DEC-S-093 … DEC-S-104

## Context

CDS-WP-012 committed four CDS-owned JSON Schema Draft 2020-12 contracts, fifteen
synthetic fixtures, a fifteen-case expected-outcome matrix, and the V1–V4
[Machine-Readable Validation Contract](../architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)
— all unexecuted (`Not assessed`). Executing them requires a concrete runtime and, for
two already-decided standards, tested implementations: JSON Schema Draft 2020-12
execution (DEC-S-077) and RFC 8785 canonicalization (DEC-S-090, ADR-0002). The
validator must run fully offline, reject duplicate keys at parse time (DEC-S-088), and
produce machine-readable, revision-bound evidence.

## Decision drivers

- Offline, deterministic, reproducible execution (DEC-S-080, DEC-S-030).
- Minimal, auditable supply-chain surface (RISK-073).
- Standards fidelity: no self-written JSON-Schema or JCS implementation.
- Duplicate-key rejection at the parser level (DEC-S-088).
- Evidence quality: exact runtime/dependency identity in every report.
- No tool becomes a source of truth (DEC-S-004, RISK-063).

## Considered alternatives

1. **Pure standard library only (no third-party packages).** Zero supply-chain risk,
   but requires re-implementing JSON Schema 2020-12 and RFC 8785 — untested standards
   code is a larger correctness risk than two pinned, focused dependencies. Rejected.
2. **Node.js/ajv stack.** Capable, but introduces a second runtime, a much larger
   transitive dependency tree, and no rfc8785 pairing advantage. Rejected.
3. **A design-token toolchain (e.g. a token build framework).** Prohibited direction:
   a productive transformer/build decision is out of scope and couples validation to a
   tool (DEC-S-004); far more surface than needed. Rejected.
4. **Python + pinned `jsonschema` + pinned `rfc8785` (chosen).** Both packages
   implement exactly the two already-decided standards; `rfc8785` is pure-Python with
   zero dependencies; `jsonschema` brings a small, pinnable transitive set and native
   Draft 2020-12 + local-registry (`referencing`) support.
5. **Python + jsonschema, digests from raw source bytes (no rfc8785).** Contradicts
   ADR-0002: raw-byte digests break under formatting-only changes. Rejected.

## Decision

The initial CDS offline token validator uses:

- **Python 3.11 or later** (executed: see the evidence report for the exact version);
- **standard library first**: `argparse`, `dataclasses`, `enum`, `hashlib`, `json`
  (with `object_pairs_hook` duplicate-key rejection), `pathlib`, `re`, `typing`,
  `unittest`;
- **`jsonschema` (pinned)** for JSON Schema Draft 2020-12 execution with a local
  `referencing.Registry`;
- **`rfc8785` (pinned)** for RFC 8785 canonical JSON;
- **`unittest`** as the only test framework;
- entry point **`python -m tools.cds_validator`** with the `version`,
  `validate-file`, `validate-cases`, and `digest` commands (DEC-S-094);
- **exact dependency pins** — direct and transitive — in
  [requirements-validator.lock](../../requirements-validator.lock);
- **no runtime network dependency** of any kind.

## Dependency boundary

Only `jsonschema` and `rfc8785` are direct dependencies; their transitive closure is
pinned in the lock file. No further runtime dependency may be added without a BLOCKED
status and a Nova decision (DEC-S-093). Dependencies are never vendored into the
repository; installation targets a temporary environment outside the repository.
License metadata is recorded in the
[Stack Evaluation](../research/OFFLINE_VALIDATOR_STACK_EVALUATION.md) as information
only — it is not a CDS licensing decision (publication state stays
`Private Development`).

## Offline boundary

After installation the validator performs no network access: schema resolution is a
committed local registry (DEC-S-096), all references are local paths, network
references fail V1, and there is no telemetry. An offline-boundary regression is a
defect (RISK-079).

## CLI boundary

The CLI contract (commands and exit codes 0/1/2/3) is the operational interface
(DEC-S-094). Exit codes report contract outcomes — they are never a Human-Maintainer
approval, a maturity state, or a claim (DEC-S-053 applied).

## Test strategy

`unittest` covers the controlled loader, schema registry, graph rules,
canonicalization invariance, layered validation against the committed fixtures,
reporting contract, CLI exit codes, and the full fixture harness with
expected-versus-actual comparison. Tests run offline. Test success is
executor-produced evidence, not review (DEC-S-103).

## Security and privacy

No secrets, no personal data, no telemetry, no network. Digests are integrity aids,
never authenticity (DEC-S-100, RISK-072). Supply-chain exposure is tracked as
RISK-073 with exact pins and a governed upgrade path.

## Trade-offs

- Two third-party packages add supply-chain surface (accepted; mitigated by pinning,
  provenance records, and offline execution) in exchange for tested standards
  fidelity.
- Python version drift across environments can change behavior (RISK-075); reports
  therefore bind the exact executed runtime.
- The bounded V2 subset (DEC-S-098) trades breadth for honesty: unsupported DTCG
  areas are limitations, never silent passes.

## Determinism consequence

Same inputs + same pinned stack + same contract ⇒ same layered outcomes and digests.
Any observed divergence across environments is a defect, not noise (RISK-075).

## Implementation deferral

This ADR selects the validator stack only. It selects no productive transformer,
build system, package, design-token toolchain, publication pipeline, or any design
value. Semantic status foundations and Candidate planning are CDS-WP-014.

## Follow-up work package

**CDS-WP-014 — Semantic Status Foundation Contract and First Candidate Plan** builds
on the executed harness; independent Evidence Review of this WP's results remains
open (DEC-S-103, DEC-S-104).

## Authority boundary

This ADR grants no Candidate, Stable, claim, release, or publication status. Nova
reviews; only the Human Maintainer accepts this ADR (by commit), approves maturity
transitions, and performs any Git or release action.
