# Status Axis Vocabulary

- **Project:** Core Design System (CDS)
- **Registered by:** CDS-WP-014 — Semantic Status Foundation Contract and First
  Candidate Plan
- **Date:** 2026-07-17
- **Status:** **Normative** vocabulary of the
  [Semantic Status Foundation Contract](SEMANTIC_STATUS_FOUNDATION_CONTRACT.md),
  pending Human-Maintainer commit. Experimental; no Candidate status.
- **Update (CDS-WP-015):** every one of the 25 values now has exactly one
  non-visual token in the Experimental
  [`semantic/status` source set](../../tokens/semantic/status/semantic-status.tokens.json)
  (`status.<axis>.<value>`, 1:1 machine-verified traceability, DEC-S-117) and a
  DE/EN entry in the [terminology mapping](SEMANTIC_STATUS_TERMINOLOGY_DE_EN.md).
  The Candidate gate remains open.

## Reading this vocabulary

Exactly **five axes** with exactly **five values each** — **25 axis values**
(DEC-S-105, DEC-S-106). Technical IDs are stable, language-neutral, and follow
the CDS naming profile (`^[a-z][a-z0-9-]*$` per segment, DEC-S-081); display
labels are localized separately and must preserve these meanings (DEC-S-110).
For every value this vocabulary fixes: canonical meaning · allowed use ·
prohibited inference · minimum required context · communication obligation ·
Candidate evidence requirement. **`unknown` is a first-class value on every
axis and never an omitted default** (DEC-S-107).

The recurring Candidate evidence requirement — "covered by positive and
negative fixtures and executed validation" — refers to the planned Candidate
gates ([Candidate Plan](../roadmap/FIRST_SEMANTIC_STATUS_CANDIDATE_PLAN.md));
**no such evidence exists in CDS-WP-014**.

---

## Axis 1 — Operational Condition (`condition`)

Answers: *what state is the subject in, within the declared scope?* This axis
describes the subject, never our knowledge of it (that is `confidence`), its
importance (`severity`), its currency (`freshness`), or its proof (`evidence`).

### `condition: nominal`

- **Canonical meaning:** the subject operates within its declared normal
  parameters in the declared scope.
- **Allowed use:** only when an observation or assessment supports normal
  operation for the declared scope and time.
- **Prohibited inference:** does **not** imply `verified`, `current`,
  `available` evidence, or `severity: none`. A nominal condition with stale
  freshness or unverified confidence remains exactly that.
- **Minimum required context:** subject identity, declared scope, and the
  observed-or-assessed time.
- **Communication obligation:** must not be summarized as "healthy"/"good"
  when any other axis carries a material qualifier (`stale`, `unverified`,
  `partial`, `unknown` …) — the qualifier travels with it (invariant 6).
- **Candidate evidence requirement:** covered by positive and negative
  fixtures and executed validation, including at least one case where
  `nominal` coexists with a non-positive value on another axis.

### `condition: degraded`

- **Canonical meaning:** the subject operates, but outside declared normal
  parameters — reduced capability, performance, or quality.
- **Allowed use:** when operation continues with an identified reduction.
- **Prohibited inference:** does not imply how severe the reduction is
  (`severity` states that); does not imply the subject will fail; is not a
  softer synonym for `disrupted`.
- **Minimum required context:** what is reduced, relative to which declared
  normal.
- **Communication obligation:** degraded and unavailable must stay
  distinguishable in every representation (status rule 4).
- **Candidate evidence requirement:** fixture coverage distinguishing
  `degraded` from `disrupted` and `unavailable`.

### `condition: disrupted`

- **Canonical meaning:** one or more declared functions of the subject do not
  operate; the subject as a whole is not fully out of service.
- **Allowed use:** when specific functions are identified as non-operating.
- **Prohibited inference:** does not imply total unavailability, a cause, or
  permanence.
- **Minimum required context:** which declared function(s) are affected.
- **Communication obligation:** the affected functions must be nameable;
  "disrupted" without an affected scope is incomplete.
- **Candidate evidence requirement:** fixture coverage distinguishing
  `disrupted` from `degraded` (partial quality loss) and `unavailable` (no
  service).

### `condition: unavailable`

- **Canonical meaning:** the subject does not provide its declared function in
  the declared scope.
- **Allowed use:** when the declared function is absent — regardless of cause.
- **Prohibited inference:** does not imply the cause is known, the outage is
  total across other scopes, or that evidence exists (`evidence` states that).
- **Minimum required context:** the declared scope in which the function is
  absent.
- **Communication obligation:** must never be visually or textually softened
  into a degraded-like state; `unavailable + severity: none` is a
  review-required combination.
- **Candidate evidence requirement:** fixture coverage including the
  `unavailable`-with-low-severity review case.

### `condition: unknown`

- **Canonical meaning:** the operational condition cannot currently be stated
  for the declared scope.
- **Allowed use:** whenever no supportable condition statement exists — this is
  the honest default of an unobserved subject.
- **Prohibited inference:** is **never** a shorthand for `nominal` (invariant
  7 of the architecture) and never an error state of the status system itself;
  it is a truthful statement about knowledge of condition.
- **Minimum required context:** why the condition is unknown, when knowledge
  was last available (if ever), and what would resolve it — where these are
  themselves known.
- **Communication obligation:** explicitly perceivable, non-visually included
  (requirement 7.4); never rendered as neutral silence, an empty cell, or a
  positive default.
- **Candidate evidence requirement:** negative fixtures proving that an
  omitted or unknown condition never validates as a positive one.

---

## Axis 2 — Severity and Impact (`severity`)

Answers: *how much does the current state matter, in the declared scope?*
Severity qualifies impact; it does not restate condition.

### `severity: none`

- **Canonical meaning:** no known impact in the declared scope.
- **Allowed use:** when impact has been considered and none is known.
- **Prohibited inference:** does **not** imply `condition: nominal` (an
  unavailable test system may correctly carry `none`), and "no known impact"
  is not "no impact" — the difference is carried by `confidence` and
  `evidence`.
- **Minimum required context:** the declared scope against which impact was
  assessed.
- **Communication obligation:** where confidence is `uncertain`/`unverified`/
  `unknown`, "no known impact" phrasing (or equivalent) is mandatory — not
  "no impact".
- **Candidate evidence requirement:** fixture coverage of `none` combined
  with non-nominal conditions.

### `severity: minor`

- **Canonical meaning:** impact exists but does not materially impair the
  declared purpose.
- **Allowed use:** identified, bounded impact below the major threshold of the
  declared scope.
- **Prohibited inference:** not a statement that attention is unnecessary;
  not a trend statement.
- **Minimum required context:** what is impacted and why it is bounded.
- **Communication obligation:** must remain visible in summaries when
  combined with worsening freshness or confidence.
- **Candidate evidence requirement:** boundary fixtures between `minor` and
  `major`.

### `severity: major`

- **Canonical meaning:** impact materially impairs the declared purpose.
- **Allowed use:** identified material impairment.
- **Prohibited inference:** does not imply `critical` urgency or a
  particular cause.
- **Minimum required context:** the impaired purpose and the affected scope.
- **Communication obligation:** high disclosure priority; may not be
  aggregated away (invariant 2).
- **Candidate evidence requirement:** review-combination fixture
  `nominal + major` (valid only with explicit rationale).

### `severity: critical`

- **Canonical meaning:** impact endangers the declared purpose as a whole or
  creates an unacceptable risk in the declared scope.
- **Allowed use:** the strongest impact statement; reserved for endangerment
  of the declared purpose.
- **Prohibited inference:** does not imply the subject is `unavailable`; a
  nominally operating subject can carry a critical risk exposure — that exact
  combination is review-required.
- **Minimum required context:** what is endangered and the basis of the
  assessment.
- **Communication obligation:** first in disclosure priority; never hidden
  behind a positive condition (Communication Contract).
- **Candidate evidence requirement:** fixtures for `critical` with each
  non-unknown condition value, including the review-required pairs.

### `severity: unknown`

- **Canonical meaning:** the impact cannot currently be assessed for the
  declared scope.
- **Allowed use:** when no supportable impact assessment exists.
- **Prohibited inference:** never treated as `none`; an unassessed impact is
  not an absent impact.
- **Minimum required context:** why assessment is not possible, where known.
- **Communication obligation:** must be disclosed in any summary that makes a
  positive statement about the subject.
- **Candidate evidence requirement:** negative fixtures proving
  `severity: unknown` never validates as `none`.

---

## Axis 3 — Knowledge Confidence (`confidence`)

Answers: *how sure are we of the status statement?* Confidence qualifies the
statement, not the subject.

### `confidence: verified`

- **Canonical meaning:** the statement is backed by identified, current
  verification evidence appropriate to the declared scope.
- **Allowed use:** **only** with identified and current verification evidence
  — evidence identity must be resolvable and freshness must support it.
- **Prohibited inference:** verification of one scope does not verify a wider
  scope; `verified` does not imply the state will persist.
- **Minimum required context:** the evidence identity and verification time.
- **Communication obligation:** the word "verified" (or a localized
  equivalent) may only appear when this value legitimately holds
  (invariant 5).
- **Candidate evidence requirement:** negative fixtures where `verified` with
  `evidence: unavailable`/`unknown` fails review; positive fixtures with
  resolvable evidence identity.

### `confidence: supported`

- **Canonical meaning:** the statement rests on relevant but not fully
  verifying evidence or observation.
- **Allowed use:** when evidence supports, but does not verify, the
  statement.
- **Prohibited inference:** not a rounding-up path to `verified`; not a
  statement that contradicting evidence is absent.
- **Minimum required context:** what supports the statement.
- **Communication obligation:** must not be collapsed into "verified" in any
  summary or translation.
- **Candidate evidence requirement:** DE/EN parity checks that no localized
  label upgrades `supported` toward verified.

### `confidence: uncertain`

- **Canonical meaning:** relevant indications exist, but they are incomplete
  or partially conflicting.
- **Allowed use:** honest middle state; indications exist, sureness does not.
- **Prohibited inference:** not an error, not an implicit negative; does not
  justify hiding the status.
- **Minimum required context:** the nature of the uncertainty (incomplete vs.
  conflicting), where known.
- **Communication obligation:** the uncertainty is part of the message;
  dropping it is a truthfulness defect.
- **Candidate evidence requirement:** content-review evidence that uncertain
  language stays understandable (Content and Cognitive Accessibility, area 5).

### `confidence: unverified`

- **Canonical meaning:** the statement has not been verified; no verification
  has taken place or its result is not usable.
- **Allowed use:** default for stated-but-unverified information — including
  documentation-derived statements (evidence honesty: documentation evidences
  stated intent, not that anything works, RISK-017).
- **Prohibited inference:** never displayed or summarized as `verified`
  (invariant 5); not a claim that the statement is wrong.
- **Minimum required context:** the origin of the unverified statement.
- **Communication obligation:** "not verified"/"not tested" must remain
  available and used — absence of a failure is not evidence of success.
- **Candidate evidence requirement:** negative fixtures proving
  `unverified → verified` renaming or remapping fails closed.

### `confidence: unknown`

- **Canonical meaning:** the confidence of the statement itself cannot be
  stated — it is unknown whether, or how well, the statement is backed.
- **Allowed use:** when the provenance of a statement is itself unclear.
- **Prohibited inference:** never treated as any positive confidence; a
  statement of unknown confidence cannot carry an unqualified summary.
- **Minimum required context:** why confidence cannot be assessed.
- **Communication obligation:** discloses itself in any summary
  (review-required combination with positive summaries).
- **Candidate evidence requirement:** fixtures where `confidence: unknown`
  blocks unqualified positive summaries.

---

## Axis 4 — Freshness (`freshness`)

Answers: *how current is the observation or assessment?* Freshness qualifies
the time-validity of the statement, never its correctness.

### `freshness: current`

- **Canonical meaning:** the observation or assessment is recent enough for
  the declared scope's decision needs, with a documented observation or
  assessment time.
- **Allowed use:** **only** with a documented observed-or-assessed time within
  the declared currency window.
- **Prohibited inference:** current does not imply verified or nominal; a
  current observation of an unavailable subject is `current`.
- **Minimum required context:** the observation/assessment time and the
  declared currency window it satisfies.
- **Communication obligation:** "current" without an observable time is a
  review-required combination — the time must exist and be resolvable.
- **Candidate evidence requirement:** negative fixture: `current` without a
  documented time fails review.

### `freshness: aging`

- **Canonical meaning:** the observation is beyond its ideal currency but not
  yet stale for the declared scope.
- **Allowed use:** a declared early-warning band between current and stale.
- **Prohibited inference:** not silently equal to current; not yet stale —
  the band boundaries belong to the declared scope, not to this vocabulary.
- **Minimum required context:** the observation time and the declared bands.
- **Communication obligation:** must be distinguishable from `current` where
  the distinction is material to the consumer's decision.
- **Candidate evidence requirement:** band-boundary fixtures
  (current/aging/stale) with declared windows.

### `freshness: stale`

- **Canonical meaning:** the observation is too old to support current
  decisions in the declared scope.
- **Allowed use:** when the declared staleness threshold is passed.
- **Prohibited inference:** **never communicated as current** (invariant 4);
  staleness does not invalidate the historical observation itself.
- **Minimum required context:** the observation time and the passed
  threshold.
- **Communication obligation:** the staleness qualifier travels into every
  summary that uses the underlying observation.
- **Candidate evidence requirement:** negative fixtures proving stale-as-
  current representations fail closed.

### `freshness: expired`

- **Canonical meaning:** the observation has passed a declared hard validity
  limit and must not be used as a basis for current statements in the
  declared scope.
- **Allowed use:** where a hard expiry is declared and passed.
- **Prohibited inference:** never a current basis; distinct from `stale`
  (advisory ageing vs. hard limit).
- **Minimum required context:** the expiry rule and when it was passed.
- **Communication obligation:** an expired basis must be disclosed as such
  wherever the subject's status is still shown.
- **Candidate evidence requirement:** fixtures distinguishing `stale` from
  `expired` semantics.

### `freshness: unknown`

- **Canonical meaning:** the observation/assessment time — and therefore
  currency — cannot be stated (including: the clock itself is uncertain).
- **Allowed use:** honest state for undated or unreliable-clock information;
  this answers the architecture's open question 5.
- **Prohibited inference:** never treated as `current`; undated information
  is not fresh by default.
- **Minimum required context:** why the time is unknown or unreliable.
- **Communication obligation:** disclosed wherever a decision could assume
  currency.
- **Candidate evidence requirement:** fixtures with missing/uncertain time
  metadata validating only as `unknown`.

---

## Axis 5 — Evidence Availability (`evidence`)

Answers: *is the statement backed by accessible evidence?* Availability
qualifies access to evidence, never its quality (that is `confidence`).

### `evidence: available`

- **Canonical meaning:** evidence for the statement exists and is accessible
  via a resolvable evidence identity.
- **Allowed use:** only with a resolvable evidence identity.
- **Prohibited inference:** **availability is not correctness or
  sufficiency** — available evidence may still be weak (see `confidence`).
- **Minimum required context:** the evidence identity.
- **Communication obligation:** must not be presented as proof of quality;
  "backed by evidence" language must not overstate.
- **Candidate evidence requirement:** fixtures with resolvable vs.
  unresolvable evidence identities.

### `evidence: partial`

- **Canonical meaning:** some, but not all, evidence relevant to the declared
  scope is accessible.
- **Allowed use:** when identified parts of the evidence are missing or
  inaccessible.
- **Prohibited inference:** not rounded up to `available`; the gap is part of
  the status.
- **Minimum required context:** which part is available and which is missing.
- **Communication obligation:** the partiality must remain visible
  (invariant 6).
- **Candidate evidence requirement:** fixtures where hiding partiality fails
  review.

### `evidence: unavailable`

- **Canonical meaning:** no evidence for the statement is currently
  accessible.
- **Allowed use:** honest state for claims without accessible backing.
- **Prohibited inference:** does not automatically falsify the statement; it
  removes its backing — combined with `verified` it is review-required
  (verification without accessible evidence must be explained).
- **Minimum required context:** whether evidence never existed, is lost, or
  is inaccessible — where known.
- **Communication obligation:** any positive statement carrying
  `unavailable` evidence must disclose that.
- **Candidate evidence requirement:** the `verified + unavailable`
  review-combination fixture.

### `evidence: not-applicable`

- **Canonical meaning:** evidence is not meaningfully applicable to this
  statement in the declared scope — **with an explicit rationale**.
- **Allowed use:** only with a recorded rationale; without one it fails
  closed.
- **Prohibited inference:** not an escape hatch from evidence obligations; a
  missing rationale turns it into a fail-closed state, not `unknown`.
- **Minimum required context:** the rationale itself.
- **Communication obligation:** the rationale must be reachable from the
  representation.
- **Candidate evidence requirement:** negative fixture: `not-applicable`
  without rationale fails.

### `evidence: unknown`

- **Canonical meaning:** whether evidence exists or is accessible cannot
  currently be stated.
- **Allowed use:** when the evidence situation itself is unassessed.
- **Prohibited inference:** never treated as `available`; also not as
  `not-applicable` (which requires a rationale).
- **Minimum required context:** why the evidence situation is unassessed.
- **Communication obligation:** disclosed in any summary that leans on the
  statement.
- **Candidate evidence requirement:** fixtures proving `unknown` evidence
  blocks "evidence-backed" phrasing.

---

## Counts

- **Axis count: 5** (`condition`, `severity`, `confidence`, `freshness`,
  `evidence`)
- **Value count: 25** (5 per axis)
- **Independent re-count:** headings of the form `### \`axis: value\`` in this
  document: 5 + 5 + 5 + 5 + 5 = **25**; `unknown` appears exactly once per
  axis = **5**. Any future mismatch between these counts and the headings is a
  defect in this document and fails closed.
