# Semantic Status Candidate — Accessibility Responsibility Mapping

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-016 — Candidate Accessibility Gate Remediation
- **Date:** 2026-08-17
- **Scope:** the **Semantic Status Candidate source and contract family** — five
  axes, 25 values, ten invariants, combination and conflict rules, the
  communication and accessibility contract, the DE/EN terminology mapping, and
  the `semantic/status` source set with manifest and resolver.
- **Status:** **Scope-bound responsibility mapping — NOT normative, NOT
  evidence.** The normative source remains the
  [Accessibility Responsibility Model](ACCESSIBILITY_RESPONSIBILITY_MODEL.md),
  which this document derives from and does not change.

## What this document is

Requirement 2 of the [Candidate accessibility gate](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md#candidate-accessibility-gate):
a responsibility mapping for the artifact actually being proposed. It answers, per
accessibility-relevant subject: **who is responsible, why, under which authority,
who owns the evidence, and what changes downstream.**

## What this document is not

- It is **not** an assignment of blame and **not** a transfer of obligation. A
  `Consumer` row does not release CDS from the contract that makes the consumer's
  work possible; a `CDS` row does not make the consumer's product accessible.
- It **names no consumer.** **No consumer of the Semantic Status source exists
  and none is authorized** (DEC-S-124, RISK-097). Every `Consumer` row below is a
  statement about *a future consumer's* obligations, not about anyone's current
  behaviour, and no consumer evidence exists or is implied.
- It is **not evidence** and creates **no claim**.

## Responsibility values

| Value | Meaning |
| --- | --- |
| `CDS` | CDS owns it at the source/contract layer and can be held to it today. |
| `Consumer` | A future Consumer Maintainer owns it; CDS cannot satisfy it, however good the contract. |
| `Shared` | Both must act. CDS supplies a contract, a role, or a mechanism; the consumer composes, populates, or renders it. **Neither side alone is sufficient.** |
| `Not applicable with rationale` | Genuinely does not apply to this artifact family, with a stated reason that is not "nothing exists yet". |

## Mapping

*(13 subjects. `Evidence owner` names who must produce the evidence, never who
has produced it — see the "Evidence state today" column for what actually
exists.)*

### 1 — The five axes

| Field | Value |
| --- | --- |
| **Responsibility** | `CDS` |
| **Why** | Axis independence is the mechanism that keeps a truthful status expressible at all. If CDS lets one axis stand in for another, no downstream representation can recover the distinction. |
| **Source authority** | [Semantic Status Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) (DEC-S-105), invariant 1 |
| **Evidence owner** | CDS |
| **Evidence state today** | Provisional AE-1: axis completeness machine-verified (5/5, no unauthorized axis, no missing axis). |
| **Future downstream responsibility** | Every representation and every Product Profile must keep the five axes separable; merging them is a fail-closed remapping (FC-8). |

### 2 — The 25 values as a governed family

| Field | Value |
| --- | --- |
| **Responsibility** | `CDS` |
| **Why** | The value set is the shared vocabulary. Adding, removing, or renaming a value is a governed, migration-bearing change (DEC-S-082), not an authoring convenience. |
| **Source authority** | [Status Axis Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) (DEC-S-106), [Token Contract](../foundations/SEMANTIC_STATUS_TOKEN_CONTRACT.md) |
| **Evidence owner** | CDS |
| **Evidence state today** | Provisional AE-1: 25/25 values present, 1:1 path/value agreement, no case-only collisions, no aggregate and no visual role. |
| **Future downstream responsibility** | A Consumer Extension may add product-local *domain* states outside CDS semantics but must not repurpose a CDS value or map a CDS value onto a positive local state (DEC-S-112). |

### 3 — The ten invariants

| Field | Value |
| --- | --- |
| **Responsibility** | `Shared` |
| **Why** | CDS states and enforces the invariants at the source; only a representation can actually break invariants 6, 7, and 9 in front of a user. Both sides are required for any of them to hold end to end. |
| **Source authority** | [Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md), the ten invariants |
| **Evidence owner** | CDS for the source-level part; the consumer for the composed product part (AE-4). |
| **Evidence state today** | Provisional AE-1 for the source-level part only. **No product-level evidence exists**, because no product uses the source. |
| **Future downstream responsibility** | Each invariant must be re-evidenced at the representation layer under its Channel Accessibility Profile; source evidence does not transfer (DEC-S-125, DEC-S-052). |

### 4 — Textual descriptions of every value

| Field | Value |
| --- | --- |
| **Responsibility** | `CDS` |
| **Why** | Text-first is the whole accessibility strategy of this Foundation (DEC-S-111). A value without a textual meaning cannot be given a correct text alternative by anyone downstream. |
| **Source authority** | [Status Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md), "Textual meaning first" |
| **Evidence owner** | CDS |
| **Evidence state today** | Provisional AE-1: **25/25** non-empty `$description` at the source, now fail-closed under `CDS-V4-STATUS-DESCRIPTION`. |
| **Future downstream responsibility** | A representation must render or expose the textual meaning; supplying final UI microcopy is the consumer's, and it must not narrow the canonical meaning. |

### 5 — `unknown` preservation

| Field | Value |
| --- | --- |
| **Responsibility** | `Shared` |
| **Why** | CDS makes `unknown` a first-class value on all five axes and forbids the positive-default mapping. A consumer or a rendering can still silently drop it — as an empty cell, a neutral colour, or a blank. |
| **Source authority** | Invariant 3 (DEC-S-107); fail-closed condition FC-3; [Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) per-axis `unknown` entries |
| **Evidence owner** | CDS for the source; consumer for the rendered and composed state. |
| **Evidence state today** | Provisional AE-1: `unknown → positive default` fails closed for condition, severity, and evidence in the machine cases; omission fails closed (FC-1). |
| **Future downstream responsibility** | `unknown` must be **explicitly perceivable, visually and non-visually**; never neutral silence and never a positive default. This is not waivable by an ordinary exception (DEC-S-059). |

### 6 — `stale` and `expired` preservation

| Field | Value |
| --- | --- |
| **Responsibility** | `Shared` |
| **Why** | CDS forbids representing `stale` or `expired` as `current` (invariant 4, FC-4). Whether a real display honours that is a representation property. |
| **Source authority** | Invariant 4; [Composition Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) fail-closed row 4 |
| **Evidence owner** | CDS for the source; consumer for the product. |
| **Evidence state today** | Provisional AE-1: stale-as-current fails closed; `stale` and `expired` are distinguished by their minimum required context. |
| **Future downstream responsibility** | The staleness qualifier must travel into every summary that uses the underlying observation, in every channel including print and greyscale. |

### 7 — `unverified` preservation

| Field | Value |
| --- | --- |
| **Responsibility** | `Shared` |
| **Why** | CDS reserves the word "verified" for the value that legitimately holds it (invariant 5, FC-5) and forbids remappings that rename it (FC-8). A localization or a product label can still erode it. |
| **Source authority** | Invariant 5; [Terminology DE/EN](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md) prohibited-shortening column |
| **Evidence owner** | CDS for the source and the terminology; consumer for product wording. |
| **Evidence state today** | Provisional AE-1: both the representation route (FC-5) and the remapping route (FC-8) fail closed. |
| **Future downstream responsibility** | No locale, label, or profile may upgrade `unverified` or `supported` toward `verified`. |

### 8 — Evidence availability semantics

| Field | Value |
| --- | --- |
| **Responsibility** | `Shared` |
| **Why** | CDS defines what `available`, `partial`, `unavailable`, `not-applicable`, and `unknown` mean and requires a resolvable evidence identity where the value claims backing (FC-7). Supplying the actual evidence identity is the asserting party's job. |
| **Source authority** | [Vocabulary](../foundations/STATUS_AXIS_VOCABULARY.md) axis 5; [Composition Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) provenance requirements |
| **Evidence owner** | CDS for the semantics; the asserting party for each concrete evidence identity. |
| **Evidence state today** | Provisional AE-1: resolvable/unresolvable identity pair covered; `not-applicable` without a rationale fails closed. |
| **Future downstream responsibility** | Partiality must remain visible; "backed by evidence" phrasing must not overstate; `unknown` evidence must not become `available`. |

### 9 — DE/EN terminology

| Field | Value |
| --- | --- |
| **Responsibility** | `CDS` |
| **Why** | Semantic parity between DE and EN is a CDS obligation: technical IDs stay language-neutral and both languages must express identical semantic content (DEC-S-110, DEC-S-119). |
| **Source authority** | [Terminology DE/EN](../foundations/SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md); [Communication Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md) "DE/EN parity" |
| **Evidence owner** | CDS |
| **Evidence state today** | Provisional AE-1 for **structure only**: 25/25 identifiers with a DE and an EN label, no duplicate, no unauthorized, no missing row. **Meaning equivalence is not machine-checked** and rests on human review; comprehension and cultural suitability are unvalidated. |
| **Future downstream responsibility** | A consumer adding a further language inherits the same prohibition on narrowing, widening, softening, or upgrading a canonical meaning. Further languages are outside the declared scope and are **not supported by omission** (DEC-S-069). |

### 10 — Combination and conflict rules

| Field | Value |
| --- | --- |
| **Responsibility** | `CDS` |
| **Why** | The six review-required combinations and eight fail-closed conditions are what stop a formally valid status object from being a dishonest one. They are contract-level rules, not product policy. |
| **Source authority** | [Status Composition and Conflict Rules](../foundations/STATUS_COMPOSITION_AND_CONFLICT_RULES.md) (DEC-S-109) |
| **Evidence owner** | CDS |
| **Evidence state today** | Provisional AE-1: **6/6** review-required combinations and **8/8** fail-closed conditions exercised with expected/actual agreement. |
| **Future downstream responsibility** | A consumer may not relax a rule locally. Asserting a review-required combination as intended requires a recorded rationale wherever it is asserted. |

### 11 — Communication obligations

| Field | Value |
| --- | --- |
| **Responsibility** | `Shared` |
| **Why** | CDS fixes the obligations — material qualifiers travel with summaries, prohibited unqualified claims, a path to the full five-axis disclosure. The consumer writes the actual sentences a person reads. |
| **Source authority** | [Communication and Accessibility Contract](../foundations/STATUS_COMMUNICATION_AND_ACCESSIBILITY_CONTRACT.md) (DEC-S-108, DEC-S-111) |
| **Evidence owner** | CDS for the contract; consumer for product copy and for AE-4. |
| **Evidence state today** | Provisional AE-1 for the machine-checkable part (unqualified positive summary over an `unknown` axis is caught as RR-6). **Whether real wording is understandable is a human judgement**, supported only by executor-produced and independent contract reviews — **no user research exists**. |
| **Future downstream responsibility** | Plain, non-blaming, actionable language for `unknown`, limitations, and fail-closed states; no unqualified "healthy", "good", "current", "verified", or "all systems normal" in any language. |

### 12 — Preservation of meaning in future representations

| Field | Value |
| --- | --- |
| **Responsibility** | `Shared` |
| **Why** | CDS states that meaning is constant across channels while presentation is not (DEC-S-029, invariant 9), and that a channel unable to preserve a distinction must **declare the limitation rather than drop it silently**. Only the party building the representation can honour that. |
| **Source authority** | [Foundation Contract](../foundations/SEMANTIC_STATUS_FOUNDATION_CONTRACT.md) "Channel boundary"; [Accessibility Channel Profiles](ACCESSIBILITY_CHANNEL_PROFILES.md) cross-cutting rule 2 |
| **Evidence owner** | Whoever builds the representation — CDS for a CDS artifact, the consumer for a consumer artifact. |
| **Evidence state today** | **None.** No representation exists, so nothing has been preserved or lost. This is `not assessable`, not `passed`. |
| **Future downstream responsibility** | Redundant modalities (colour, icon, position, motion) may accompany but never carry or contradict textual meaning. Data visualization gets no exemption. |

### 13 — Future channel evidence

| Field | Value |
| --- | --- |
| **Responsibility** | `Shared` |
| **Why** | Per DEC-S-125 the channel-independent source is assessed at source level, **and** every later channel representation needs its own Channel Accessibility Profile and its own revision-bound evidence before Candidate or Stable. Neither obligation substitutes for the other. |
| **Source authority** | DEC-S-125, DEC-S-058, DEC-S-052; [Accessibility Channel Profiles](ACCESSIBILITY_CHANNEL_PROFILES.md) |
| **Evidence owner** | The producer of each channel artifact, reviewed by an Evidence Reviewer who is never its executor (DEC-S-045). |
| **Evidence state today** | **None.** No channel representation of the Semantic Status Foundation exists, is authorized, or is planned in this work package. |
| **Future downstream responsibility** | **Source evidence never becomes channel evidence and channel evidence never becomes source evidence.** Profiles 3–6 (PDF, presentations, exported diagrams, brand) remain blocked entirely until their profiles exist. |

## Counts

| Responsibility | Subjects |
| --- | --- |
| `CDS` | **5** (subjects 1, 2, 4, 9, 10) |
| `Shared` | **8** (subjects 3, 5, 6, 7, 8, 11, 12, 13) |
| `Consumer` | **0** |
| `Not applicable with rationale` | **0** |
| **Total** | **13** |
| Subjects with **no** evidence today | **2** (subjects 12, 13) |
| Subjects with a **provisional AE-1** source-level part | **11** |
| Subjects with any **consumer** evidence | **0** |

## Unresolved

- **`Consumer` count is zero — deliberately.** Every consumer-facing obligation
  in this artifact family is `Shared`, because CDS always carries at least the
  contract half. Nothing here is purely a consumer's to own **at the source
  scope**. The genuinely consumer-owned criteria live in the
  [WCAG applicability mapping](SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md),
  Group C, where 20 criteria are consumer-owned.
- **Where CDS status semantics end and consumer domain semantics begin remains an
  open boundary question** (CR-035, recorded in the Foundation Contract). It is an
  open point, not a licence to blur, and it is **not resolved here**.
- **No shared responsibility has been exercised**, because no consumer exists. A
  `Shared` row is an obligation on both sides, not a report that either side has
  acted.

## Related documents

- [Accessibility Responsibility Model](ACCESSIBILITY_RESPONSIBILITY_MODEL.md) — normative source
- [Semantic Status Candidate WCAG Applicability Mapping](SEMANTIC_STATUS_CANDIDATE_WCAG_APPLICABILITY_MAPPING.md)
- [Semantic Status Candidate Accessibility Limitations](SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_LIMITATIONS.md)
- [Semantic Status Candidate Accessibility Regression Plan](SEMANTIC_STATUS_CANDIDATE_ACCESSIBILITY_REGRESSION_PLAN.md)
- [Accessibility Evidence and Claims Model](ACCESSIBILITY_EVIDENCE_AND_CLAIMS_MODEL.md)
