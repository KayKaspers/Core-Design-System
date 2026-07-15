# NDF Skills Provenance

Provenance record for the NDF Claude Skills held locally in this repository.

## Purpose of the local skills copy

CDS holds a local, verified copy of the released NDF Claude Skills so that CDS
work packages can use the Skills-first operating mode offline, without network
access and without depending on an external runtime service.

The copy exists for controlled consumption only. It is **not** an independent
fork of the skill contents and carries no local modifications.

## Authoritative source

| Property | Value |
| --- | --- |
| Source repository | KayKaspers/Nova-Development-Framework |
| Source remote | `https://github.com/KayKaspers/Nova-Development-Framework.git` |
| Released tag | `v1.0.0` |
| Expected commit prefix | `9dcadc1` |
| Confirmed commit prefix | `9dcadc1` — match |
| Full source commit | `9dcadc12fb960914b9a5baeff2ab1aee75912b57` |
| Released source path | `.claude/skills/` |
| Locally verified source path | `D:\Projects\Nova-Development-Framework` |

## Target

| Property | Value |
| --- | --- |
| Target repository | KayKaspers/Core-Design-System |
| Target path | `.claude/skills/` |
| Skill count | 38 |
| File count | 39 |
| Verification date | 2026-07-15 |

The file count is 39 because the released source path contains the 38 skill
directories — each holding exactly one `SKILL.md` — plus the pack index file
`.claude/skills/README.md` that ships as part of the released path. The index
file was adopted unchanged together with the skills.

## Verification method

1. The local source repository was identified and its `origin` remote confirmed
   against the expected repository. Read-only Git inspection only.
2. The tag `v1.0.0` was resolved locally to its full commit hash and matched
   against the expected prefix `9dcadc1`.
3. The released file tree was read directly from the Git object tree of the tag
   (`git ls-tree -r v1.0.0 -- .claude/skills`), not from the source working
   tree.
4. Every file was extracted byte-for-byte from the tag's Git objects via
   `git cat-file blob <sha>`, which returns raw blob content without smudge
   filters, formatting, or line-ending normalization.
5. For every file, the SHA-256 of the source blob read from the tag and the
   SHA-256 of the written target file were computed and compared.
6. The target file set was compared against the tag file set to detect extra or
   missing files.
7. Modes were checked for symlinks, submodules, binaries, and executables.

No network access, clone, fetch, or pull was performed at any point.

## Verification result

| Check | Result |
| --- | --- |
| Files compared | 39 |
| SHA-256 matches | 39 |
| SHA-256 mismatches | 0 |
| Byte identity with tag `v1.0.0` | Confirmed for all files |
| Extra files in target | None |
| Missing files in target | None |
| Skill directories | 38 — exact |
| Symlinks | None |
| Submodules | None |
| Binary or executable files | None — all 39 files are regular mode-100644 Markdown |

The upstream contents were **not modified**. No skill was reformulated, merged,
split, reformatted, or adapted to CDS. Line endings were not normalized.

A machine-readable hash manifest of every file is maintained at
[project-system/NDF_SKILLS_MANIFEST.json](../../project-system/NDF_SKILLS_MANIFEST.json).
A human-readable inventory is maintained at
[project-system/NDF_SKILLS_INVENTORY.md](../../project-system/NDF_SKILLS_INVENTORY.md).

## Relationship to upstream

- The authoritative source of the skill contents remains the NDF repository at
  the released tag.
- The local copy is a consumption copy pinned to `v1.0.0`.
- The local copy must never diverge from the pinned upstream revision.
- CDS does not maintain, extend, or govern the skill contents.

## Update rule

Future NDF skill versions may only be adopted under the following rules:

1. Updates require a **separate, explicitly authorized Skill-Maintenance work
   package**. They are never performed as a side effect of product work.
2. Skill files must never be changed during normal CDS work.
3. An update must pin a new released NDF tag, resolve its full commit, and
   verify the expected commit against that tag.
4. An update must re-run the byte-exact extraction and full SHA-256
   verification described above.
5. An update must regenerate the manifest and inventory and refresh this
   provenance record, including tag, commit, counts, and verification date.
6. Local modifications of skill contents remain prohibited. If CDS ever needs
   different behavior, that requires an upstream change or an explicit,
   separately governed decision — not a local edit.
7. Any verification failure is fail-closed: the update is reported to Nova and
   not adopted.
