# Next Phase

- **Phase:** Foundation / Pre-Design
- **Completed work packages:** CDS-WP-001, CDS-WP-001A
- **Next work package:** CDS-WP-002 — Concept and Scope Registration

## Status of CDS-WP-001

CDS-WP-001 — Project Governance and NDF Bootstrap is **Completed**.

It established the project charter, the role and authority model, six strategic
foundation decisions (DEC-S-001 … DEC-S-006), five initial risks
(RISK-001 … RISK-005), the controlled work-package roadmap, and the local
Claude operating instructions.

## Status of CDS-WP-001A

CDS-WP-001A — NDF Skills Bootstrap is **Completed**.

It adopted the released NDF v1.0.0 Claude Skills into `.claude/skills/`,
verified byte-identity against the released tag, and activated the Skills-first
operating mode:

- 38 verified docs-only Skills, 39 files,
- pinned to NDF v1.0.0, commit `9dcadc12fb960914b9a5baeff2ab1aee75912b57`,
- all SHA-256 comparisons matched; upstream contents unmodified,
- provenance, hash manifest, and inventory established.

See [NDF Skills Provenance](../docs/governance/NDF_SKILLS_PROVENANCE.md),
[NDF Skills Manifest](NDF_SKILLS_MANIFEST.json), and
[NDF Skills Inventory](NDF_SKILLS_INVENTORY.md).

Completion is reported for Human Maintainer review. No Git write action was
performed.

## Next work package: CDS-WP-002 — Concept and Scope Registration

### Objective

Formal registration of the CDS concept and its boundaries.

### Scope direction

- register the concrete CDS concept,
- register the authorized scope,
- register the non-goals,
- register the target audiences,
- register the consumer classes,
- register the project boundaries,
- keep long-term scope and currently authorized scope clearly separated.

### Explicitly prohibited in CDS-WP-002

No concrete visual or technical design decisions may be made. In particular:

- selecting colors,
- creating or selecting logos or logo architecture,
- selecting typography,
- selecting icon systems, illustration, or imagery,
- defining light or dark themes,
- selecting design tools, component frameworks, or token tooling,
- selecting a token format or documentation platform,
- deciding package architecture or repository split,
- deciding license, public release, or compatibility commitments.

Skill files must not be modified. Skills support the procedure; they do not
extend scope.

### Authorization note

CDS-WP-002 requires an explicit work-package prompt from Nova before execution
begins. Being listed as **Next** identifies the sequence; it does not by itself
authorize the work.

## Related documents

- [Work Packages](WORK_PACKAGES.md)
- [Project Profile](PROJECT_PROFILE.md)
- [Project Charter](../docs/governance/PROJECT_CHARTER.md)
