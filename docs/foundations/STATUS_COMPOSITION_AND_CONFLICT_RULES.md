# Status Composition and Conflict Rules

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-014 — Semantic Status Foundation Contract and First
  Candidate Plan
- **Date:** 2026-07-17
- **Status:** **Normative** composition rules of the
  [Semantic Status Foundation Contract](SEMANTIC_STATUS_FOUNDATION_CONTRACT.md),
  pending Human-Maintainer commit. Experimental; no Candidate status.

## The complete status object

*(Normative — a CDS-conformant status statement carries all eleven fields.)*

| # | Field | Content | Absence means |
| --- | --- | --- | --- |
| 1 | **Subject identity** | What the status is about (stable identifier) | The statement is unattributable — fail closed |
| 2 | **Declared scope** | The boundary within which the statement holds | Every value is unbounded and unreviewable — fail closed |
| 3 | **`condition`** | One of the five condition values | No implicit value — fail closed |
| 4 | **`severity`** | One of the five severity values | No implicit value — fail closed |
| 5 | **`confidence`** | One of the five confidence values | No implicit value — fail closed |
| 6 | **`freshness`** | One of the five freshness values | No implicit value — fail closed |
| 7 | **`evidence`** | One of the five evidence values | No implicit value — fail closed |
| 8 | **Observed-or-assessed time** | When the statement was grounded | `freshness: current` becomes review-required; undated ⇒ `freshness: unknown` |
| 9 | **Source or evidence identity** | Resolvable origin of the statement (DEC-S-031, DEC-S-080) | Provenance-unknown — review-required; `verified`/`available` become untenable |
| 10 | **Known limitations** | What the statement does not cover | Silence about limitations is treated as an omission, not as absence of limitations |
| 11 | **Rationale where required** | For `not-applicable`, review-required combinations, and consumer remappings | The requiring value/combination fails closed |

**A missing mandatory axis is never an implicit positive value** — it is a
fail-closed state (invariant 3 applied to omission).

## Independent composition

*(Normative — DEC-S-105, DEC-S-109)*

Every combination of the 25 axis values is **representable**: the axes are
orthogonal statements about different questions, and unusual combinations are
often precisely the truthful ones (a nominally operating subject with stale,
unverified knowledge is the classic honest state). Therefore:

- No axis value constrains another axis's value **mechanically**.
- No transformation, token mapping, channel output, or summary may merge two
  axes into one value (invariant 1, 2).
- Combinations divide into: **freely representable**, **review-required**
  (below), and **fail-closed** (below). Review-required combinations are not
  presumed impossible — they demand an explicit check and rationale
  (DEC-S-109).

## Review-required combinations

*(Normative — each requires an explicit review and a recorded rationale before
being asserted as intended. They are representable; unexplained they fail the
later V4 governance layer.)*

| # | Combination | Why review is required |
| --- | --- | --- |
| 1 | `condition: nominal` + `severity: major` or `critical` | Normal operation with material or existential impact is possible (risk exposure) but must be explained, not glossed |
| 2 | `confidence: verified` + `evidence: unavailable` or `unknown` | Verification without accessible or known evidence contradicts the verification meaning unless explained (e.g. evidence access restrictions — which are then a limitation) |
| 3 | `freshness: current` without a resolvable observed-or-assessed time | "Current" is a claim about time; without a time it is unsupported |
| 4 | `evidence: not-applicable` without a rationale | The rationale is a mandatory part of the value; absence fails closed |
| 5 | `condition: unavailable` + `severity: none` | A non-functioning subject with no known impact is legitimate (e.g. an idle redundant instance) but must say why |
| 6 | `unknown` on any axis + an unqualified positive summary | A summary that says "all good" while an axis says "we don't know" is a truthfulness defect unless the summary carries the qualifier |

The six rows are the mandatory minimum; a future Candidate review may add
review-required combinations through governed change, never remove these.

## Fail-closed conditions

*(Normative — these states block assertion, transformation, and distribution;
no automatic repair, DEC-S-023, DEC-S-109.)*

| # | Condition |
| --- | --- |
| 1 | A mandatory axis is missing from the status object |
| 2 | An unknown axis or value identifier is used (outside the 25 normative values) |
| 3 | `unknown` is applied as a positive default (mapped to nominal/none/verified/current/available anywhere) |
| 4 | `stale` or `expired` is represented as `current` |
| 5 | `unverified` is represented as `verified` |
| 6 | `not-applicable` is asserted without a rationale |
| 7 | The source or evidence identity is unresolvable where the values require it (`verified`, `available`) |
| 8 | A Product-Profile or consumer remapping loses, merges, renames, or reweights axis meaning (RISK-088) |

## Rationale requirements

A rationale is mandatory for: every review-required combination asserted as
intended; every `evidence: not-applicable`; every consumer-visible deviation
from a CDS axis meaning (which is a deviation record, not a local fix). A
rationale states *why the combination or value is truthful here* — it never
weakens the underlying invariants.

## Provenance requirements

Status statements inherit the CDS provenance discipline (DEC-S-031, DEC-S-080):
the source or evidence identity must be resolvable and revision-bound where the
values claim backing; `latest` is not an identity; a statement whose provenance
cannot be established may not carry `verified` confidence or `available`
evidence. Deviation records follow the architecture's deviation flow.

## Disclosure priority

*(Normative — an ordering for **attention**, never a semantic override; every
material qualifier stays visible regardless of position, DEC-S-108.)*

1. `severity: critical`
2. `condition: unavailable` or `disrupted`
3. `freshness: expired` or `stale`
4. `confidence: unverified` or `unknown`
5. `evidence: partial`, `unavailable`, or `unknown`
6. The remaining state

Rules: a nominal condition never hides stale, unverified, or missing evidence;
summaries carry material qualifiers; detail levels must be able to disclose all
five axes ([Communication Contract](STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md)).

## No aggregate score

There is **no normative aggregated health score, badge, traffic light, or
percentage** that replaces or hides the five axes (DEC-S-108, invariant 2).
A consumer may build prioritized *views*; a view is a disclosure ordering over
truthful axes, never a substitute value.

## Abstract examples

*(Illustrative only — value-neutral, no visual encoding, no product names.)*

- **Honest nominal:** subject `example-subject-a`, scope "declared scope A":
  `nominal · none · supported · current(T1) · available(E1)` — representable
  without review; summary may be positive, qualifiers minimal.
- **The classic honest middle:** `nominal · none · unverified · stale ·
  unavailable` — representable; any summary must carry "not verified, not
  current, no accessible evidence"; an unqualified "healthy" here violates
  invariant 6 and fails review.
- **Review case:** `nominal · critical · supported · current(T2) ·
  available(E2)` — representable only with a recorded rationale (row 1), e.g.
  an identified risk exposure while operation continues.
- **Fail-closed case:** `condition` omitted, or `severity: fine` (unknown
  identifier), or `evidence: not-applicable` without rationale — blocked, no
  repair.

## Related documents

- [Semantic Status Foundation Contract](SEMANTIC_STATUS_FOUNDATION_CONTRACT.md)
- [Status Axis Vocabulary](STATUS_AXIS_VOCABULARY.md)
- [Status Communication and Accessibility Contract](STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md)
- [Evidence, Traceability and Status Semantics](../architecture/EVIDENCE_TRACEABILITY_AND_STATUS_SEMANTICS.md)
