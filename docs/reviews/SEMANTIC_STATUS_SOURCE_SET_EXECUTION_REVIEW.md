# Semantic Status Source Set Execution Review

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-015 — Semantic Status Foundation Source Set and
  Candidate Evidence
- **Date:** 2026-07-18
- **Evidence class:** **Executor-produced, revision- and content-bound,
  independently unreviewed** (DEC-S-121). **Candidate: no** (DEC-S-115).

## Source-set identity

- Source-Set ID: **`semantic/status`** · Layer: **semantic** · CDS profile
  **1** · DTCG **2025.10** · Source revision: **`semantic-status-rev-0001`** ·
  Maturity: **Experimental** · Approval: **Unapproved** · Extension root:
  `io.github.kaykaspers.cds` · Manifest reference: local relative
  (`semantic-status.source-set.json`).
- Manifest identity: `semantic/status/manifest`, registering exactly one
  source set with zero dependencies, an empty `approvedExtensionPoints` list
  (no Product-Profile boundary), provenance `Bound`, digest state `Computed`
  (RFC 8785 / SHA-256; digest values live in the evidence artifacts).
- Resolver identity: `semantic/status/resolver`, `localOnly: true`, exactly
  one ordered step over `semantic/status`, generated non-normative output
  placeholder.

## Token, axis, and value counts

- **Axis groups: 5** (`condition` · `severity` · `confidence` · `freshness` ·
  `evidence`) · **Values per axis: 5** · **Status tokens: 25**, path pattern
  `status.<axis>.<value>`, DTCG type `string`, each `$value` equal to its
  stable technical value identifier; `unknown` present on every axis.
- One-to-one traceability to the
  [Status Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) is
  machine-verified by a dedicated unit test (axes, values, `$value`
  agreement).

## Validator result

`validate-file` on the token document **with manifest and resolver in scope**:

| Layer | Result |
| --- | --- |
| V1 | **Pass** |
| V2 | **Pass** |
| V3 | **Pass** |
| V4 | **Not assessed** (scope aggregate — see below) |

Exit code **0** (Pass level); blocking layer `none`; **not Fail, not
Blocked**. The V4 scope aggregate is `Not assessed` because manifest and
resolver carry only non-objective generic V4 residue; the **token document's
objective semantic-status V4 checks executed and passed** (14 mandated
checks; per-document diagnostics in the report show no error and the honest
`CDS-V4-NOT-ASSESSED` informational residue).

## Diagnostics and digests

- Errors: **0** across all layers for the source-set scope.
- Digests: **3** (`sha256:` RFC 8785/SHA-256) — token document, manifest,
  resolver — recorded with revision and worktree identity in
  [wp015-semantic-status-source-digests.json](../../artifacts/validation/wp015-semantic-status-source-digests.json);
  results in
  [wp015-semantic-status-source-results.json](../../artifacts/validation/wp015-semantic-status-source-results.json).

## Structural evidence and semantic validator coverage

The status-specific V4 extension enforces: the exact axis set, the exact
per-axis value sets, explicit `unknown` everywhere, the 25-token count,
path/value agreement, case-only collision rejection (value-level in the
harness; key-level directly unit-tested — the token-document schema already
blocks uppercase keys at V3), prohibition of aggregate roles (`health`,
`overall`, `score`, `aggregate`, `success`) and appearance roles (`color`,
`icon`, `shape`, `position`, `motion`), no Candidate/approval statement, and
source/manifest identity agreement (DEC-S-118). All eight negative harness
cases (VAL-CASE-017…024) fail exactly at V4 with their primary status
category; the positive case (VAL-CASE-016) passes V4.

## Known limitations

- The extension validates the **fixed vocabulary shape**, not meaning quality,
  summary honesty in consuming UIs, localization drift, or channel-level
  truthfulness (RISK-093); fixture coverage may miss unrepresented invalid
  states (RISK-094).
- Single environment, same executor as the implementation (RISK-075,
  RISK-078).
- Non-objective V4 aspects remain `Not assessed` by design.

## Review state

**Independent review: pending** (DEC-S-121); reviewer must not be the
executor. **No Candidate**: implementation and green execution confer no
maturity, consumer, or claim status (DEC-S-115, DEC-S-124).
