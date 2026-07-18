# WP-016 Source and Contract Traceability Review

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Semantic Status Foundation Independent
  Evidence Review and Candidate Gate
- **Date:** 2026-07-18
- **Evidence class:** **Independent traceability review** by an Evidence
  Reviewer who is not the executor (DEC-S-121). Read-only against the source
  set and the contract. **Candidate: no.**

## Scope

Independent verification that the Experimental `semantic/status` source set is
1:1 traceable to the normative human-readable Semantic Status Foundation and
carries no prohibited role, no approval statement, and a consistent identity.
Sources reviewed at the committed HEAD:
[tokens](../../tokens/semantic/status/semantic-status.tokens.json) ·
[manifest](../../tokens/semantic/status/semantic-status.source-set.json) ·
[resolver](../../tokens/semantic/status/semantic-status.resolver.json) ·
[Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) ·
[Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md).

## Structural traceability (independently derived)

| Check | Expected | Independent result |
| --- | --- | --- |
| Axis groups | exactly 5 | **5** — `condition`, `severity`, `confidence`, `freshness`, `evidence` |
| Values per axis | exactly 5 | **5 / 5 / 5 / 5 / 5** |
| Status tokens | exactly 25 | **25** (each leaf carries `$value`) |
| `unknown` presence | one per axis | **5** — `unknown` explicit on every axis (DEC-S-107) |
| Token path shape | `status.<axis>.<value>` | **25 / 25** conform |
| `$type` | `string` | **25 / 25** |
| Path/value agreement | `$value` = leaf technical ID | **25 / 25** agree (DEC-S-117) |
| Vocabulary traceability | each token value 1:1 to a vocabulary value | **25 / 25** — token-leaf multiset equals the vocabulary value set |

The reviewer derived these counts directly from the JSON (not from executor
reports). The five `unknown` tokens are `condition.unknown`, `severity.unknown`,
`confidence.unknown`, `freshness.unknown`, `evidence.unknown`. The value
`unavailable` legitimately appears on two distinct axes (`condition`,
`evidence`); this is authorized per axis and is **not** a case-only collision
(collision checks are per-axis, casefold-based).

## Prohibited-role and approval-statement checks

- **No aggregate role.** No `health`, `overall`, `score`, `aggregate`, or
  `success` group or value exists; the only groups are the five authorized axes
  (DEC-S-108). Negative `VAL-CASE-022` exercises the rejection and was executed.
- **No appearance/visual role.** No `color`, `icon`, `shape`, `position`, or
  `motion` group or value exists; status meaning is non-visual (DEC-S-111).
  Negative `VAL-CASE-023` exercises the rejection and was executed.
- **No case-only collision** in the real source (DEC-S-117); negative
  `VAL-CASE-024` exercises the rejection.
- **No Candidate/approval statement embedded.** The `io.github.kaykaspers.cds`
  payload declares `maturityState: Experimental` and `approvalState:
  Unapproved`; the validator would flag `Candidate`/`Stable`/`Approved`
  (DEC-S-115, DEC-S-122, DEC-S-124) — none is present.

## Identity, provenance, and digest binding

| Field | Token payload | Manifest entry | Resolver |
| --- | --- | --- | --- |
| Source-set ID | `semantic/status` | `semantic/status` | `semantic/status` (ordered step) |
| Layer | `semantic` | `semantic` | — |
| Profile version | `1` | `1` (expected) | `1` |
| DTCG report | `2025.10` | `2025.10` (expected) | `2025.10` |
| Source revision | `semantic-status-rev-0001` | `semantic-status-rev-0001` | `semantic-status-rev-0001` |
| Maturity / approval | Experimental / Unapproved | Experimental / Unapproved | — |

- Manifest ID `semantic/status/manifest`; resolver ID
  `semantic/status/resolver`, `localOnly: true`, one ordered step; generated
  output declared `generated: true` and non-normative.
- **Product-Profile boundary:** `approvedExtensionPoints: []` — no Product
  Profile may reference or remap the vocabulary (DEC-S-112, DEC-S-124).
- **Content digests** recomputed independently and identical to committed
  WP-015 (`8d127cf…` token, `879933…` manifest, `61e64f…` resolver);
  see [wp016-independent-source-digests.json](../../artifacts/validation/wp016-independent-source-digests.json).

## Contract agreement

Each token `$description` matches the canonical meaning of the corresponding
value in the [Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md); the
token structure keeps every axis independently addressable and introduces no
26th meaning, consistent with the
[Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md) (roles only,
no visual/numeric value, no irreversible aggregation).

## Findings

No missing or extra axis, value, or role; no aggregate or appearance role; no
approval statement; identity and provenance consistent; digests reproduced.
No Blocking and no High traceability finding. One transparency observation on
the resolver `outputIdentity` wording is recorded in the
[Candidate Gate Recommendation](WP016_CANDIDATE_GATE_RECOMMENDATION.md)
(WP016-OBS-003); it does not affect traceability, outcomes, or the gate.

## Related documents

- [Independent Re-Execution Review](WP016_INDEPENDENT_REEXECUTION_REVIEW.md)
- [Terminology, Accessibility and Content Review](WP016_TERMINOLOGY_ACCESSIBILITY_CONTENT_REVIEW.md)
- [Candidate Gate Recommendation](WP016_CANDIDATE_GATE_RECOMMENDATION.md)
