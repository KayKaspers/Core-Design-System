# CDS-WP-016 — Contract Correction Independent Review R2 Notes

*Non-normative reviewer working notes for the R2 independent review of the committed
Contract Correction. Reviewer-produced, independent from the correction executor, and
bound to revision `c93cd660ba6a8fe9ee9e54ec1e165d3f1ad1d5ed`. This run reviewed only —
it implemented nothing, promoted nothing, and changed no implementation, schema, test,
fixture, source, or governance artifact. It does not modify the main
[PROJECT_BRAIN](PROJECT_BRAIN.md).*

**Result: REWORK REQUIRED · Recommendation: NO-GO · Candidate: No.**

The full record is the
[Contract Correction Independent Review](../docs/reviews/WP016_CONTRACT_CORRECTION_INDEPENDENT_REVIEW.md).

## Independence

Fresh reviewer session. It did not execute the correction and did not edit the
validator, the resolver schema, the correction tests, or the correction notes. Its
inputs were the committed repository state, the committed diff, the committed
correction notes, and the authorized normative artifacts — review sources, not
executor session memory. **Gate: PASS.**

## What was verified independently

Every sentinel was re-derived rather than accepted from the executor's record.

- **Baseline** — root, branch `main`, HEAD `c93cd660…`, parent `3619b1a…`, subject,
  clean tree and index before and after, no merge/rebase/cherry-pick, `origin`
  present with `origin/main == HEAD`, 0 tags.
- **Delta** — exactly 8 paths, 7 modified, 1 added, 0 deleted; no ninth file.
- **Skills** — 38 directories, 39 files, 39/39 manifest digest matches against the
  pinned NDF v1.0.0 manifest; the ten authorized skills read, no others.
- **Resolver schema** — enum 2→3 strictly additive, `$id`/`$schema`/Draft unchanged,
  unknown values rejected (including lowercase and ASCII-hyphen near-misses), the
  committed resolver valid under both parent and corrected schema, 5/5 schemas
  `check_schema`, 51 `$ref` all local and resolvable, no remote resolution even under
  a fetch-refusing registry, and the schema byte-identical outside the `status`
  subschema.
- **State machine** — confirmed from the committed code, not from tests alone.
- **Runtime** — fresh venv outside the repository, 7 exact lock pins, no runtime
  network, bytecode writing disabled so the tree stayed pristine.
- **Execution** — 38/38 targeted, **111/111** full regression, **24/24** harness
  matches, 0 failures, 0 errors, 0 skips, 0 mismatches, 0 internal errors —
  reproduced identically on Python 3.12.10 and 3.13.14.
- **Probes** — all **8/8** direct metadata probes matched expectations, run both with
  and without the committed manifest.
- **Regression boundary** — CLI, validation, diagnostics, fixtures, cases, source
  set, lock, decisions, risks, ADRs, dossier, project-system, brain, README, CLAUDE,
  and CHANGELOG all unchanged.
- **Governance** — Candidate No, `semantic-status-rev-0001`, Experimental,
  Unapproved, dossier Draft, 124 decisions, 97 risks, 3 ADRs, WP-016 open, WP-017 not
  activated, Private Development, no claims, pilot inactive.

## Why NO-GO despite a clean technical result

The correction is sound and well-scoped. The single blocker is documentary.

`docs/architecture/MACHINE_READABLE_VALIDATION_CONTRACT.md` — a **normative, Elevated**
source — now contains both rules at once. Line 77 still lists the superseded
unconditional prohibition ("no Candidate/approval statement") in the CDS-WP-015 rule
set, while the new CDS-WP-016 section describes the conditional state machine that
permits a coherent Candidate/Approved source.

This matters because the CDS conflict rule forbids resolving a conflict by recency, so
a reviewer cannot simply let the newer section win. The conservative reading —
line 77 — prohibits exactly the Candidate metadata the correction was authorized to
enable, which would leave the finalization run citing a self-contradicting contract.

The same stale wording survives in the `semantic_status.py` module docstring.

Importantly, the contradiction does **not** extend to the Decision layer: DEC-S-115
constrains the source set's actual state, which remains Experimental and untouched, not
the validator's capacity to evaluate a future Candidate document. Authority statements
are consistent across all five artifacts. **There is no authority conflict** — the
defect is a rule description left unreconciled.

## Findings

| ID | Severity | Subject |
| --- | --- | --- |
| CDS-WP016-CCR-R2-F-001 | **High** | Normative contract states both the superseded prohibition and the new state machine |
| CDS-WP016-CCR-R2-F-002 | Medium | `semantic_status.py` module docstring still asserts the superseded rule |
| CDS-WP016-CCR-R2-F-003 | Medium | No enum on `maturityState`/`approvalState`; mis-cased `candidate`/`stable` passes silently (pre-existing) |
| CDS-WP016-CCR-R2-F-004 | Low | `CANDIDATE_REVISION_PATTERN.match` + `$` accepts a trailing newline |
| CDS-WP016-CCR-R2-F-005 | Observation | `__pycache__` not gitignored; a naive run dirties the tree |
| CDS-WP016-CCR-R2-F-006 | Observation | En-dash enum values are typo-prone for operators |

**Blocking 0 · High 1 · Medium 2 · Low 1 · Observation 2.**

F-003 is pre-existing — the parent behaved identically — and belongs in a separate,
explicitly scoped hardening change, not in the finalization run. F-004 is the only
defect introduced by this correction's own new code.

## Notable positives worth carrying forward

- The **manifest identity check is an independent second gate**: a Candidate document
  whose revision disagrees with the manifest still fails closed, so a Candidate
  finalization cannot be completed in the token document alone.
- The correction added the precise resolver digest value but deliberately did **not**
  apply it to the committed resolver instance — correct scope discipline.
- The two pre-existing Candidate/approval tests still pass and remain meaningful
  under the new state machine rather than having been weakened.
- Backward compatibility is total: the committed resolver validates under both the
  parent and the corrected schema.

## Recommended next step

A minimal follow-up correction, Nova-reviewed and Human-Maintainer-authorized,
touching two files only: reconcile line 77 of the validation contract and the
`semantic_status.py` docstring, optionally with the one-word `fullmatch` fix for
F-004. Re-run the R2 gate afterwards. The Candidate finalization resume run stays
gated until then; F-003 is queued separately.

## Boundaries

No commit, push, pull, fetch, merge, rebase, cherry-pick, reset, restore, clean,
branch change, tag, release, or history change was performed. No risk was accepted or
closed, no decision or ADR added, no maturity granted. Candidate remains **No**.

## Related

- [Contract Correction Independent Review](../docs/reviews/WP016_CONTRACT_CORRECTION_INDEPENDENT_REVIEW.md)
- [Contract Correction Notes](CDS_WP_016_CONTRACT_CORRECTION_NOTES.md)
- [Independent Evidence Review Notes](CDS_WP_016_INDEPENDENT_EVIDENCE_REVIEW_NOTES.md)
- [Candidate Gate Recommendation](../docs/reviews/WP016_CANDIDATE_GATE_RECOMMENDATION.md)
