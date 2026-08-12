# CDS-WP-016 — Contract Correction Notes

*Non-normative working notes for the CDS-WP-016 Contract Correction Run
(Candidate metadata validation and resolver digest-state reconciliation). This
run performs **no** Candidate promotion and **no** status advancement. It does
not change the main [PROJECT_BRAIN](PROJECT_BRAIN.md), any decision, risk, or
ADR, or any project-status file.*

## Why this run exists — two prior BLOCKED finalization runs

Two Candidate-finalization runs correctly ended as **BLOCKED** with a clean
working tree, each surfacing one contract-level root cause:

1. **Resolver digest-state (Blocker 1).** OBS-003 required a precise
   machine-readable statement that no resolver output digest was computed, but
   the committed resolver schema `digestState.status` enum allowed only
   `Not computed – validator implementation pending` (imprecise after the
   validator exists) and `Computed` (untrue). The precise wording was
   schema-invalid, and schema changes were out of scope in those runs.
2. **Candidate metadata validation (Blocker 2).** The committed validator
   `tools/cds_validator/semantic_status.py` rejected `maturityState = Candidate`,
   `maturityState = Stable`, and `approvalState = Approved` **unconditionally** on
   Semantic Status documents (two `CDS-V4-STATUS-IDENTITY` errors). Correct for
   the Experimental state, but it also blocks any legitimate Candidate
   finalization after review, gate, and Human-Maintainer authorization.

Nova confirmed both blockers and authorized this focused Contract Correction Run
(resolver schema + validator contract + tests + docs only). Candidate
finalization stays gated until this correction is committed.

## Correction 1 — Resolver digest-state schema (additive)

File: `schemas/cds-resolver-document.schema.json`.

- **Old enum:** `["Not computed – validator implementation pending", "Computed"]`.
- **New enum (additive):**
  1. `Not computed – validator implementation pending` — retained for backward
     compatibility with historical / not-yet-migrated Experimental artifacts.
  2. `Not computed – no resolution or generated-output step executed` — the
     precise value where no resolution/output-generation step exists.
  3. `Computed` — only when an actual output digest was computed.
- Unchanged: `$schema` (draft 2020-12), `$id`
  (`tag:github.com,2026:KayKaspers/Core-Design-System/schema/cds-resolver-document/1`),
  title, resolver-identity contract, ordering, source-set contract, local `$ref`,
  offline boundary. No new schema version. No free strings, no remote refs.
- The real resolver instance was **not** changed in this run.

## Correction 2 — Semantic Status maturity/approval state machine

File: `tools/cds_validator/semantic_status.py`.

- **Old behavior:** unconditional rejection of `maturityState ∈ {Candidate,
  Stable}` and `approvalState = Approved`.
- **New state machine** (emits the **existing** `CDS-V4-STATUS-IDENTITY`, Error;
  **no new diagnostic code**):
  - **Experimental source:** `Experimental` + `Unapproved` (or absent) → coherent.
  - **Candidate source:** `Candidate` **and** `Approved` **and** revision matching
    `^semantic-status-rev-[0-9]{4}-candidate$` **and** not a `testOnly`/
    `nonNormative` fixture → coherent.
  - **Stable:** blocked (later explicit gate + separate validator-contract change).
  - **Fail-closed combinations:** Candidate+Unapproved · Candidate+non-Approved ·
    Candidate+Approved without Candidate revision · Candidate/Approved on a
    `testOnly` fixture · Candidate/Approved on a `nonNormative` fixture ·
    Experimental+Approved · Stable+any · Approved without a coherent Candidate
    source.
- **Candidate revision pattern:** `^semantic-status-rev-[0-9]{4}-candidate$`
  (module constant `CANDIDATE_REVISION_PATTERN`).
- **Fixture boundary:** Candidate/Approved may never be embedded in a fixture.
- **Authority boundary (documented in code and contracts):** a validator pass on a
  coherent Candidate/Approved source proves metadata coherence and an allowed
  revision form only. It does **not** prove governance authorization,
  Human-Maintainer approval, promotion, Stable, conformance, or publication. Real
  Candidate authority comes only from the Candidate Approval Record, the Nova
  finalization review, and the Human-Maintainer commit (DEC-S-115, DEC-S-122,
  DEC-S-124).
- **Unchanged checks:** axis / value / unknown / count / path-value / collision /
  aggregate / visual-leakage / manifest-source-identity; diagnostic code set.

## Tests

File: `tests/validator/test_semantic_status.py` (new class
`SemanticStatusMaturityApprovalTests`, 8 focused tests; no existing test removed
or weakened; no fixture or case file touched):

1. Experimental+Unapproved passes · 2. Candidate+Approved+valid revision passes ·
3. Candidate+Unapproved fails · 4. Candidate+Approved+invalid revision fails ·
5. Experimental+Approved fails · 6. Candidate+Approved+testOnly fails ·
7. Candidate+Approved+nonNormative fails · 8. Stable stays blocked.

## Validation results (Python 3.12.10, pinned deps, offline)

Runtime: fresh venv outside the repository, `requirements-validator.lock` exact
pins (jsonschema 4.26.0, rfc8785 0.1.4 + transitive), no runtime network.

- **Schema regression:** `check_schema` passes for the resolver and all five
  schemas; `$schema`/`$id` unchanged; old, new, and `Computed` values valid;
  unknown value invalid; committed resolver still valid; no local `$ref` broken;
  no remote resolution.
- **Validator state machine:** all eight combinations behave as specified; the
  real Experimental source still produces zero identity errors.
- **Unit tests:** **111/111 passed** (103 committed + 8 new), 0 failures, 0 errors.
- **Fixture harness:** **24/24 cases executed, 24/24 expected/actual matches,**
  0 mismatches, 0 internal errors (`VAL-CASE-001…024`).
- **Diagnostic codes:** unchanged (30 total; `CDS-V4-STATUS-IDENTITY` reused; no
  new code).

## Explicitly NOT done in this run

No Candidate/Stable metadata on the real source set, manifest, or resolver
instance; no Candidate Approval Record; the Candidate Dossier stays
`Draft – Candidate gate incomplete`; no project-status advancement; no new
Decision, Risk, or ADR; no risk-status change; publication stays Private
Development; claims none; pilot inactive.

## Changed files (8 Allowed Files)

1. `schemas/cds-resolver-document.schema.json` — additive enum + description.
2. `tools/cds_validator/semantic_status.py` — maturity/approval state machine.
3. `tests/validator/test_semantic_status.py` — 8 focused tests.
4. `docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md` — contract boundary.
5. `docs/architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md` — state machine.
6. `docs/operations/OFFLINE_TOKEN_VALIDATOR_USAGE.md` — operator boundary.
7. `docs/foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md` — maturity/authority.
8. `project-brain/CDS_WP_016_CONTRACT_CORRECTION_NOTES.md` — this file.

## Next step

After Human-Maintainer commit of this correction, the Candidate finalization
resume run becomes executable: apply the resolver instance digest-state wording
and the governance-only Candidate delta (revision → `-0002-candidate`, maturity
→ Candidate, approval → Approved) on a validator that now accepts a coherent
Candidate source.

## Related

- [Candidate Gate Recommendation](../docs/reviews/WP016_CANDIDATE_GATE_RECOMMENDATION.md)
- [Independent Evidence Review Notes](CDS_WP_016_INDEPENDENT_EVIDENCE_REVIEW_NOTES.md)
- [Machine-Readable Validation Contract](../docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md)
- [Offline Token Validator Architecture](../docs/architecture/OFFLINE_TOKEN_VALIDATOR_ARCHITECTURE.md)
- [Semantic Status Token Contract](../docs/foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md)
