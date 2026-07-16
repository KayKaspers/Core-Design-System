# Foundation Reference Integrity Review

- **Project:** Core Design System (CDS)
- **Produced by:** CDS-WP-009 — Operating Enablement and Pre-Candidate Readiness
- **Reviewed revision:** `6ceda35` (repository HEAD; CDS-WP-001 … CDS-WP-008
  committed)
- **Date:** 2026-07-16
- **Status:** **Review evidence — not a normative source.** This review records an
  assessment of reference integrity across the committed document inventory. It
  changes no normative source and corrects nothing on its own authority.

## Purpose and method

The review checks the committed, text-based project files for internal reference
integrity as a closure obligation (Foundation Closure Record, note 7). It verifies
that internal links and local file references resolve, and that stale status,
deferral, or register-span statements do not contradict the committed state.

**Correction rule.** This work package does not modify a normative source solely
because a broken reference is found. A defect found in a file **outside the
CDS-WP-009 Allowed Files** is **recorded as a finding** with a blocking-effect
assessment and a targeted correction recommendation — it is **not** corrected
here. A Foundation-closure-relevant normative contradiction would force a
fail-closed result; **none was found.**

**No web research.** External URLs are checked for syntactic plausibility and
obvious breakage only; they are never fetched.

## Scope

Committed text files under: repository root (`README.md`, `CLAUDE.md`,
`CHANGELOG.md`), `docs/**`, `project-system/**`, `project-brain/**`, and
`.claude/skills/**`.

| Area | Files in scope |
| --- | --- |
| Root (`README`, `CLAUDE`, `CHANGELOG`) | 3 |
| `docs/**` (markdown) | 54 |
| `project-system/**` (markdown) | 5 |
| `project-system/**` (JSON manifest) | 1 |
| `project-brain/**` (markdown) | 10 |
| `.claude/skills/**` (markdown) | 39 |
| **Total text files in scope** | **112** |

*(Counts re-derived from `git ls-files` and independently re-counted:
54 + 5 + 10 + 39 + 3 = 111 markdown + 1 JSON = 112.)*

## What was checked

- relative Markdown links `[text](path)`;
- local file references in backticks;
- referenced document paths and `Next` pointers;
- work-package status statements;
- `Deferred to CDS-WP-006` and `Deferred to CDS-WP-007` markers;
- stale current-work-package statements;
- non-existent target paths, case mismatch, and backslash/slash issues;
- stale Decision / Risk / CR / HYP / Finding spans;
- competing Foundation-status statements.

## Quantitative results

| Metric | Value |
| --- | --- |
| Text files in scope | 112 |
| Relative Markdown links checked | 829 |
| External URLs (syntactic check only, not fetched) | 56 |
| Broken Markdown links | **5** (all in the vendored `.claude/skills/README.md`) |
| Broken Markdown links in CDS-authored docs | **0** |
| Backtick path-like references examined | 170 |
| Genuine CDS-internal broken backtick references | **0** |
| Stale **active** WP-006 / WP-007 deferrals | **0** |
| Competing Foundation-status contradictions (normative) | **0** |

*(Figures derived by a link-resolution pass over the committed tree and
independently re-counted; path resolution done with `realpath -m` relative to each
file's directory.)*

## Findings

### FRI-F-001 — Five broken links inside the vendored NDF skills README (non-blocking)

`.claude/skills/README.md` contains five relative links to NDF upstream paths that
were **not** copied into CDS:

- `../../docs/validation/foundation-0-9/SKILLS_MVP_IMPLEMENTATION_BLUEPRINT.md`
- `../../docs/validation/foundation-0-9/EXTENDED_SKILLS_PACK_BLUEPRINT.md`
- `../../docs/validation/foundation-0-9/EXTERNAL_SKILLS_LANDSCAPE_AND_PRIORITIZATION.md`
- `../../docs/agent-workflows/NDF_SKILL_SECURITY_POLICY.md`
- `../../docs/adr/ADR-0032-skill-security-policy.md`

- **Location:** `.claude/skills/README.md` — **outside the CDS-WP-009 Allowed
  Files** and outside every normal-work Allowed-Files set (the skills tree is
  provenance-controlled and pinned byte-identical to NDF v1.0.0).
- **Cause:** the README is a vendored upstream file; its links target NDF-internal
  documents that are intentionally not part of the CDS repository.
- **Blocking effect:** **None.** These are upstream-relative references inside a
  pinned third-party file, not CDS-authored navigation. They do not affect any
  CDS normative source, register, or Foundation-closure statement.
- **Correction:** **Not performed and not recommended within a product work
  package.** Editing the file would break the byte-identical pinning recorded in
  the [NDF Skills Provenance](../governance/NDF_SKILLS_PROVENANCE.md) and the
  manifest. Any change belongs solely to an authorized **Skill-Maintenance** work
  package, and even there the correct posture is to preserve upstream fidelity.

### FRI-F-002 — WP-006 / WP-007 deferral mentions are historical, not active (non-blocking)

Occurrences of `Deferred to CDS-WP-006` / `Deferred to CDS-WP-007` appear in
`docs/architecture/**` (the CDS-WP-005 architecture documents and the requirements
traceability) and in `project-brain/CDS_WP_005_...NOTES.md`.

- **Assessment:** every occurrence is either (a) a **count reconciled to 0** with
  an explicit reconciliation note, (b) explicitly marked **"Retired by"** a later
  work package, or (c) a description of what CDS-WP-005 deferred **at the time it
  was written** (historical evidence of a completed work package). The normative
  requirement-coverage source
  ([Architecture Requirements Traceability](../architecture/ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md))
  shows **0 requirements deferred** to a policy work package.
- **Location:** `docs/architecture/**` and `project-brain/**` — **outside the
  CDS-WP-009 Allowed Files.**
- **Blocking effect:** **None.** No **active** unmet deferral remains; the mentions
  are historical/descriptive and do not contradict the reconciled coverage.
- **Correction:** **Not performed.** Optionally, a future editorial Standard-Track
  change could annotate the historical mentions as "delivered by CDS-WP-006/007";
  this is a non-blocking readability improvement, not a defect.

### FRI-F-003 — Backtick references to consumer-repository source paths are external by design (non-blocking)

`docs/governance/CONSUMER_REQUIREMENTS_TRACEABILITY.md`,
`docs/research/CONSUMER_EVIDENCE_REGISTER.md`, and
`project-brain/CDS_WP_004_...NOTES.md` cite paths such as
`docs/architecture/COREOPS_CONCEPT_V3.md`, `docs/branding/ui-principles.md`, and
`project-brain/BRANDING.md`.

- **Assessment:** these are **consumer-repository** source paths (CoreOps,
  SpeakCore, CastCore), cited as committed-revision **provenance** under DEC-S-013.
  They are deliberately **not** CDS-repository files and correctly do not resolve
  inside CDS. A generic glob (`docs/architecture/*.md`) and an ellipsis token
  (`…/COREOPS_CONCEPT_V3.md`) are formatting, not paths.
- **Blocking effect:** **None.** These are correct external evidence citations, not
  broken internal links.
- **Correction:** **None required.**

### FRI-F-004 — Pre-closure status language in the CDS-WP-008 review documents (expected)

The `docs/reviews/**` documents produced by CDS-WP-008 state "closure pending
approval", "no next work package authorized", and "GO WITH NOTES (recommendation)".

- **Assessment:** these documents are **dated review evidence bound to reviewed
  revision `7b71652`**; their pre-closure language correctly describes the state at
  review time. They are **outside the CDS-WP-009 Allowed Files** (only this
  integrity review is new; the other review documents are not modified).
- **Blocking effect:** **None.** The [Foundation Closure Record](../governance/FOUNDATION_CLOSURE_RECORD.md)
  is now the authority on the current closure status; the review documents remain
  historical evidence and are not competing normative status statements.
- **Correction:** **Not performed** — historical evidence is preserved as written.

## Register-span consistency at closure

- **Decisions:** the live status files are updated by CDS-WP-009 to
  DEC-S-001 … DEC-S-064 (64). Historical work-package evidence notes correctly
  retain the span as of their own work package (e.g. "DEC-S-001 … DEC-S-060") and
  are **not** rewritten.
- **Risks:** RISK-001 … RISK-048 (48), unchanged in count; RISK-040 status updated
  to `Mitigating` per the Critical Risk Action Register gate.
- **CR / HYP / Finding spans:** CR-001 … CR-040, HYP-001 … HYP-008, and
  FM-F-001 … FM-F-012 remain internally consistent; no stale or duplicated span
  was found.

## Result

**PASS.** CDS-authored documents have **zero** broken internal references and
**zero** competing Foundation-status contradictions. All defects found are
confined to a vendored, pinned upstream file (FRI-F-001) or are correct-by-design
external/historical references (FRI-F-002…004), each **non-blocking** and each
**outside the CDS-WP-009 Allowed Files**. No normative source required correction,
and no Foundation-closure-relevant contradiction exists.

## Related documents

- [Foundation Closure Record](../governance/FOUNDATION_CLOSURE_RECORD.md)
- [NDF Skills Provenance](../governance/NDF_SKILLS_PROVENANCE.md)
- [Architecture Requirements Traceability](../architecture/ARCHITECTURE_REQUIREMENTS_TRACEABILITY.md)
- [Foundation Milestone Review](FOUNDATION_MILESTONE_REVIEW.md)
