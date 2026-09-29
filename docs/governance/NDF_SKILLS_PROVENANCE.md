# NDF Skills Provenance

Provenance record for the NDF Claude Skills and the NDF support snapshot held
locally in this repository.

- **Current pin:** NDF **v1.1.0** — adopted by **CDS-WP-001B** (Elevated
  Skill-Maintenance package, a lettered insertion following the CDS-WP-001A
  precedent) under **DEC-S-139**.
- **Effectivity:** this pin, **DEC-S-139** and the lock state `lock-enforced` became
  effective at the Human-Maintainer exact-object integration commit of CDS-WP-001B,
  `daa5f114c1b9c02afcfc0205149ca00dc4801d8d`; before that commit the object was `migration-pending`
  (historical). **`EXECUTED ≠ ACCEPTED`, `PASS ≠ INTEGRATED`,
  `PREPARED DECISION ≠ EFFECTIVE DECISION`, and `SKILL IMPORTED ≠ SKILL APPROVED`.**
- **Previous pin:** NDF v1.0.0 (source commit
  `9dcadc12fb960914b9a5baeff2ab1aee75912b57`), adopted by CDS-WP-001A on
  2026-07-15. That record is historical and is superseded as the live pin only.

## Purpose of the local copy

CDS holds a local, verified copy of the released NDF Claude Skills, plus four NDF
support files that the pinned Skills reference directly, so that CDS work
packages can use the Skills-first operating mode **offline, reproducibly and
byte-verifiably**, without network access, without an external NDF checkout, and
without depending on an external runtime service.

The copy exists for controlled consumption only. It is **not** an independent fork
and carries no local modifications.

## Authoritative source

| Property | Value |
| --- | --- |
| Source repository | KayKaspers/Nova-Development-Framework |
| Source remote | `https://github.com/KayKaspers/Nova-Development-Framework.git` |
| Released tag | `v1.1.0` (annotated) |
| Tag object | `d4409492498cf4ed989f9ee47d4ad8b2f5f6868d` |
| Tag commit (source commit) | `948c91dc940362f7565e28f697d0528b812797a3` |
| Tag date (informational) | 2026-09-23 |
| Source paths | `.claude/skills/` and the four support paths listed below |
| Source licence | MIT (`LICENSE` at tag `v1.1.0`, blob `fa8bfb69cdf3cdf59c35c421c708ebf76ca3a2b0`, identical to the blob at `v1.0.0`) |

The source licence is the licence of the NDF project. **It selects no licence for
CDS**: no licence is selected for any CDS artifact class.

**No absolute workstation source path is recorded here or in the lock.** Sources
are identified by repository identity, tag, tag object, commit, and relative paths
only.

## Target

| Property | Value |
| --- | --- |
| Target repository | KayKaspers/Core-Design-System |
| Pack target path | `.claude/skills/` |
| Skill count | 38 |
| Pack file count | 39 (38 × `SKILL.md` + the pack index `README.md`) |
| Support-snapshot file count | 4 |
| Total locked files | 43 |
| Verification date | 2026-09-29 |

## Verification method

1. The NDF repository identity and `origin` remote were confirmed read-only.
2. The tag `v1.1.0` was resolved locally, without fetch, to its tag object and
   commit, and both matched the expected identities recorded above.
3. **Source handoff.** The released tree was read **only from the tag's Git
   objects** (`git ls-tree`, `git cat-file`, tag-to-tag `git diff`) — **never from
   the NDF `main`, the NDF Working Tree, or any `.agents/` content.**
4. Every imported file was extracted byte-for-byte from the tag's blob via
   `git cat-file blob`, which returns raw content without smudge filters,
   formatting, or line-ending normalization. No manual recreation occurred.
5. For all 43 files the Git blob identity, the SHA-256 and the byte size of the
   source blob were compared with the target file, and the files were checked for
   LF-only line endings and the absence of a byte-order mark.
6. The target file set was compared against the tag file set.
7. The tag-to-tag delta against `v1.0.0` was re-derived before import.
8. No network access, clone, fetch, or pull was performed at any point.

## Verification result

| Check | Result |
| --- | --- |
| Source-handoff preflight (tag object, tag commit, required paths) | **PASS** — all match |
| Files verified against the tag | **43 / 43** |
| SHA-256 matches | 43 |
| SHA-256 mismatches | 0 |
| Git blob identity matches | 43 |
| Byte identity with tag `v1.1.0` | Confirmed for all 43 files |
| Extra files in the pack target | None |
| Missing files in the pack target | None |
| Skill directories | 38 — exact |
| Symlinks / submodules / executables | None — all 43 files are regular mode-100644 Markdown |
| LF-only / no BOM (all 43) | Confirmed |

### Delta from v1.0.0

| Measure | Value |
| --- | --- |
| Pack files at `v1.0.0` → `v1.1.0` | 39 → 39 |
| Skills | 38 → 38 |
| Changed | **7** — the pack index `README.md` and six `SKILL.md` files (`ndf-changelog-writer`, `ndf-compact-context-summary-runner`, `ndf-release-notes-runner`, `ndf-release-safety`, `ndf-v1-readiness-review`, `ndf-work-package-runner`) |
| Unchanged (byte-identical to both tags) | **32** |
| Added / deleted / renamed | 0 / 0 / 0 |

The upstream contents were **not modified**. No skill was reformulated, merged,
split, reformatted, or adapted to CDS. Line endings were not normalized. The six
changed Skills carry new **trigger descriptions**, so **Skill auto-trigger
behaviour changes** with this pin.

## Support snapshot

Exactly **four** NDF support files are held byte-identically from the same source
release. They exist so that the direct rule/document references of the pinned
Skills resolve offline, at the repository-relative paths the unmodified Skills
expect.

| Path | Git blob | Bytes |
| --- | --- | --- |
| `docs/guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md` | `aedd43ae166346392490830e739def35b9d9c0f2` | 14120 |
| `docs/templates/SESSION_HANDOFF_TEMPLATE.md` | `75ffd39827c178d592ab86b8bc32d399d3d69028` | 1646 |
| `framework/prompts/blocks/BLOCK_EXECUTION_CONTRACT.md` | `9999aa5e2b84368b0e76f242f03e97513ea744a8` | 5164 |
| `framework/standards/WORK_PACKAGE_LIFECYCLE.md` | `ba16cc1106b4a4ef01932e7d3a796e92826cf9d9` | 5540 |

**Classification.** The support snapshot is **NDF process material under NDF
authority**, held by CDS as a byte-verified consumption copy. It is **not** a
fork, **not** independent CDS policy, **not** CDS architecture, and **not** counted
as Skills. **Mixed-tag Skill/support content is forbidden**: the pack and the
snapshot are bound to one source release and one source commit. No fifth support
document and no onward-linked NDF document is imported.
`docs/agent-workflows/NDF_SKILL_PROVENANCE_AND_INTEGRITY_LOCK.md` — the NDF
governance reference for integrity locks — is a **migration-source reference
only** and is deliberately **not** imported.

## Integrity lock

The machine-readable lock is
[project-system/NDF_SKILLS_MANIFEST.json](../../project-system/NDF_SKILLS_MANIFEST.json)
(`schemaVersion` 2). A human-readable inventory is
[project-system/NDF_SKILLS_INVENTORY.md](../../project-system/NDF_SKILLS_INVENTORY.md).

| Lock property | Value |
| --- | --- |
| Digest algorithm | `SHA-256` |
| Digest encoding | lowercase hexadecimal |
| Digest basis | raw committed bytes |
| Path representation | relative POSIX |
| Ordering | deterministic, byte-order by path within each record set |
| Records | 39 pack + 4 support snapshot = 43, **one** source tag and **one** source commit |
| Verification status | `verified` |
| Approval state | Human-Maintainer approval became effective at the exact-object integration commit `daa5f114c1b9c02afcfc0205149ca00dc4801d8d` |
| Migration state | **`lock-enforced`** — effective from the Human-Maintainer exact-object integration commit `daa5f114c1b9c02afcfc0205149ca00dc4801d8d` (`migration-pending` was the pre-integration state of the candidate object) |
| Exception state | no exception active |

Every record repeats its source tag and source commit, so **mixed-tag content is
structurally detectable by inspection. No automated enforcement or drift gate
exists**; a lock is an integrity aid, **not authenticity, not approval, and not a
release statement** (the same boundary DEC-S-090 sets for digests).

## NDF release/version namespace vs CDS release state

Release, version and compatibility statements inside the pinned NDF Skills and the
NDF support-snapshot documents describe **the NDF project and the NDF release
family only.** Statements such as *"`v1.0.0` is final"* or *"the v1.x compatibility
promise is active since `v1.0.0`"* are **NDF statements**. They **do not state,
imply or activate** a CDS `v1.0.0`, a CDS release, a CDS maturity transition, or a
CDS compatibility commitment, and they **cannot satisfy or alter DEC-S-037**.

**NDF identifiers remain NDF-namespaced** — for example NDF ADR-0031 and ADR-0032,
NDF work-package identifiers, `G-13`, and the NDF budget and profile names. Where
the NDF guide specifies disambiguated forms, CDS uses `NDF-B0` … `NDF-B4` and
`NDF-Lean`. **No NDF identifier is a CDS Decision, ADR, risk, work-package
identifier, maturity level, or profile.** CDS publication remains `Private
Development`.

## Authority boundary

`Framework: NDF v1.1.0` binds the **development-process layer only** (execution
contracts, work-package execution, process verification and evidence, session and
handoff rules, Skill routing, Human-Maintainer gates). NDF gains **no** authority
over CDS architecture, Decisions, ADRs, risks, design-system semantics, visual
values, Source Sets, maturity, CDS evidence admission or AE grading, CDS V1–V4
validation, conformance, claims, publication, or CDS release/version state. Inside
the process layer NDF normative requirements are a **floor**; a CDS rule may be
stricter and **never silently relaxes** one; a conflict fails closed and is
escalated to the Human Maintainer. Full rule: **DEC-S-139**.

## Known provenance limitations

Recorded, **not fixed**; none authorizes additional upstream import or a CDS
redesign.

1. The NDF integrity-lock document's status block is inconsistent with the NDF
   v1.1.0 changelog (upstream).
2. NDF defines approval-state and exception-state fields but no vocabulary; the
   values used in the lock are a CDS-local choice (**DEC-S-139**) and are not an NDF
   normative vocabulary.
3. The NDF ADR-0032 private-consumer-project question remains **unresolved
   upstream**; CDS makes no claim that it is settled.
4. **Six informational links in the pack `README.md` do not resolve in CDS**
   (three `docs/validation/foundation-0-9/` blueprints; the NDF skill security
   policy; NDF ADR-0032; the NDF integrity-lock document). They are
   non-execution navigation. The ten direct links from the changed Skills and the
   pack `README.md` to the four snapshot files all resolve.
5. Terminology collides with CDS terms — *Lean*, *Standard*, *Candidate*, and ADR
   numbering. NDF terms stay NDF-namespaced (see the namespace section above).
6. The six changed Skill descriptions change Skill **auto-trigger behaviour**.
7. **No automated CDS drift gate exists**; verification is by documented manual
   procedure.
8. **Seven onward links inside the support-snapshot documents themselves do not
   resolve in CDS** (six in `TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md`, one in
   `WORK_PACKAGE_LIFECYCLE.md`). They are informational and non-rule-bearing for the
   directly adopted Skill execution path; **no onward NDF document was imported**, and
   this does not weaken the 10/10 direct-dependency result.

## Historical carriers

`docs/governance/PROJECT_CHARTER.md` still states `Framework: Nova Development
Framework v1.0.0`. That wording is a **charter-era historical carrier**; it is
intentionally **preserved unchanged** and is **not** the live framework-baseline
carrier. The live carriers are this record, the lock, the inventory, and the
maintained project-control documents. Historical records — previous work-package
records, reviews, changelog entries and point-in-time framework declarations —
stay historical and are not rewritten.

## Relationship to upstream

- The authoritative source of the pinned content remains the NDF repository at the
  released tag. **The snapshot is not a fork.**
- The local copy must never diverge from the pinned upstream revision.
- CDS does not maintain, extend, or govern the skill contents.

## Update rule

Future NDF skill or support-snapshot versions may only be adopted under the
following rules:

1. Updating the pack **or** the support snapshot requires a **separate, explicitly
   authorized Skill-Maintenance work package**, a byte-exact import, full
   re-verification, independent review, and Human-Maintainer integration. It is
   never performed as a side effect of product work.
2. Skill and support-snapshot files must never be changed during normal CDS work.
3. An update must pin a new released NDF tag, resolve its tag object and full
   commit, and verify them against the expected identities.
4. An update must re-run the tag-source extraction and the full SHA-256 and blob
   verification described above, for **all** locked files, from **one** tag.
5. An update must regenerate the lock and inventory and refresh this provenance
   record, including tag, tag object, commit, counts, and verification date.
6. Local modifications remain prohibited. If CDS needs different behavior, that
   requires an upstream change or an explicit, separately governed decision — not a
   local edit.
7. Any verification failure is fail-closed: the update is reported to Nova and not
   adopted.
