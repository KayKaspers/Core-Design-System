# Changelog

All notable changes to the Core Design System project will be documented here.

The format will be refined before the first CDS release. No version has been
released and no release is announced.

## Unreleased

### Added

- Registered concept and scope as the normative scope source: problem
  statement, mission, vision, strategic objectives, six capability domains,
  cross-cutting concerns, current Foundation scope separated from long-term
  scope, twelve binding non-goals, ownership boundaries, CoreOps pilot
  boundary, assumptions, and deferred decisions. (CDS-WP-002)
- Consumer and Stakeholder Model with direct users, indirect beneficiaries,
  stakeholder roles, three consumer relationship classes, channel-consumer
  categories, and the limits of the classification. (CDS-WP-002)
- Scope Boundary Matrix registering the per-area split between CDS
  responsibility, consumer responsibility, and shared or contract-controlled
  responsibility. (CDS-WP-002)
- Foundation Context Pack as a compact, explicitly non-normative continuation
  summary. (CDS-WP-002)
- Strategic scope decisions DEC-S-007 … DEC-S-012. (CDS-WP-002)
- Risks RISK-006 … RISK-009. (CDS-WP-002)
- Work-package evidence notes for CDS-WP-002.
- Verified local adoption of the 38 docs-only NDF v1.0.0 Claude Skills under
  `.claude/skills/`, extracted byte-identically from the released NDF v1.0.0
  tag (commit `9dcadc12fb960914b9a5baeff2ab1aee75912b57`). Upstream contents
  unmodified. (CDS-WP-001A)
- NDF Skills provenance documentation recording source, tag, commit,
  verification method, verification result, and the update rule. (CDS-WP-001A)
- Machine-readable SHA-256 hash manifest of every adopted Skill file.
  (CDS-WP-001A)
- NDF Skills inventory covering all 38 Skills. (CDS-WP-001A)
- Work-package evidence notes for CDS-WP-001A.
- Project charter defining mission, vision, strategic purpose, scope
  categories, current phase boundary, non-goals, pilot relationship, and
  authority model. (CDS-WP-001)
- Decision index with the strategic foundation decisions DEC-S-001 …
  DEC-S-006. (CDS-WP-001)
- Risk register with the initial risks RISK-001 … RISK-005. (CDS-WP-001)
- Initial controlled work-package roadmap CDS-WP-001 … CDS-WP-008.
  (CDS-WP-001)
- Work-package evidence notes for CDS-WP-001.

### Changed

- Project charter consolidated with the registered scope: capability domains,
  consumer classes, pilot boundary, and Foundation status; it now references
  the normative scope source instead of carrying its own scope list.
  (CDS-WP-002)
- Decision index extended to DEC-S-001 … DEC-S-012 and now distinguishes
  strategic foundation decisions from strategic scope decisions.
  DEC-S-001 … DEC-S-006 unchanged. (CDS-WP-002)
- Risk register extended to RISK-001 … RISK-009 with an explicit note that the
  risk owner model is provisional until CDS-WP-006. RISK-002 gained a
  cross-reference to the CoreOps pilot boundary without changing its meaning.
  (CDS-WP-002)
- Work-package status advanced: CDS-WP-002 completed, CDS-WP-003 next.
  (CDS-WP-002)
- README, project profile, project brain, and next-phase definition updated
  with the registered scope, consumer classes, register ranges, and the
  CDS-WP-003 boundaries. (CDS-WP-002)
- Claude working instructions updated with the context-pack and normative scope
  references and the current work-package pointers. (CDS-WP-002)
- Skills-first operating mode activated in the Claude working instructions,
  including selection, context-economy, authority-boundary, fail-closed, and
  Skill-maintenance rules. (CDS-WP-001A)
- Work-package status advanced: CDS-WP-001 and CDS-WP-001A completed,
  CDS-WP-002 next. (CDS-WP-001A)
- Project profile extended with NDF Skills version, count, status, source
  commit, and Skills-first operating mode. (CDS-WP-001A)
- README and project brain extended with the Skills-first operating mode and
  links to provenance and inventory. (CDS-WP-001A)
- Project profile extended with work-package status, register scope, and the
  intentionally open decision areas. (CDS-WP-001)
- Project brain restructured as a compact long-term orientation document.
  (CDS-WP-001)
- README updated with project status, pilot role, operating model, registers,
  and governance links. (CDS-WP-001)
- Claude working instructions rewritten for Claude Desktop with a locally
  connected repository. (CDS-WP-001)

### Removed

- `.claude/skills/.gitkeep` placeholder, superseded by the verified Skills
  adoption. (CDS-WP-001A)
