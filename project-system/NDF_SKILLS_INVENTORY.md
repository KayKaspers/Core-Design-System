# NDF Skills Inventory

Inventory of the NDF Claude Skills held locally in this repository.

- **Source:** NDF v1.0.0 (`9dcadc12fb960914b9a5baeff2ab1aee75912b57`)
- **Target path:** `.claude/skills/`
- **Total skills: 38**
- **Total files:** 39 (38 × `SKILL.md` + the released pack index `README.md`)
- **Status:** All 38 skills Verified
- **Verification date:** 2026-07-15

Every skill directory contains exactly one main file, `SKILL.md`. All skills are
docs-only. Purpose descriptions below are condensed from each skill's own
declared description; they are summaries for orientation and are not normative.
The normative content is the skill file itself.

Provenance: [docs/governance/NDF_SKILLS_PROVENANCE.md](../docs/governance/NDF_SKILLS_PROVENANCE.md) ·
Hashes: [NDF_SKILLS_MANIFEST.json](NDF_SKILLS_MANIFEST.json)

## Skills

| # | Skill directory | Main file | Files | Status | Source | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `ndf-accessibility-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews docs, UI concepts, and flows for accessibility and understandability risks. Advisory; claims no certification. |
| 2 | `ndf-adr-governance-review` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews ADR-relevant changes for governance consistency. Fail-closed; never silently changes or finalizes an ADR. |
| 3 | `ndf-architecture-blueprint-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Produces architecture blueprints — context, goals/non-goals, components, data flows, ADR candidates. No implementation. |
| 4 | `ndf-behavioral-adoption-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews adoption and behavioral design ethically. No manipulation, dark patterns, or pressure design. |
| 5 | `ndf-branding-kit-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Creates or reviews branding kits — name, slogan, color world, logo ideas, asset list. Copies no third-party brands. |
| 6 | `ndf-changelog-writer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Helps write consistent, neutral, WP-referenced changelog entries. Never invents release status or triggers releases. |
| 7 | `ndf-compact-context-summary-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Produces the uniform Compact Context Summary and Report-to-Nova handover block. |
| 8 | `ndf-content-tone-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews language, tone, and communication consistency. Flags misleading claims. |
| 9 | `ndf-context-pack-maintainer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Keeps Context Packs consistent and short for lower-token handover. Does not invent status. |
| 10 | `ndf-creative-direction-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Develops creative direction — style, tonality, visual principles, differentiation, risks. Advisory. |
| 11 | `ndf-debugging-root-cause-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Structures debugging and root-cause analysis. Advisory; no risky actions. |
| 12 | `ndf-docs-polish-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Improves documentation clarity, structure, and consistency without changing governance substance. |
| 13 | `ndf-ethical-growth-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews growth, community, and support flows ethically. No pressure mechanics or paywalls. |
| 14 | `ndf-existing-project-analysis-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Structures a neutral analysis of an existing project for NDF onboarding. No network, secrets, or git actions. |
| 15 | `ndf-feature-scope-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Sharpens feature scope — problem, goal, non-goal, acceptance criteria, risks. Write actions only after human approval. |
| 16 | `ndf-feedback-triage-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Triages feedback and issues neutrally. Invents no feedback; documents no reviewer identities. |
| 17 | `ndf-implementation-review-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews an implementation for scope-fit, architecture-fit, security, tests, docs, risks. No automatic code changes. |
| 18 | `ndf-landing-page-concept-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Creates landing-page concepts with CTAs free of pressure mechanics. Advisory. |
| 19 | `ndf-naming-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Finds and assesses names — options, meaning, risk, differentiation. No trademark claim without a proper check. |
| 20 | `ndf-onboarding-friction-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Assesses onboarding friction — first run, setup steps, doc gaps, quickstart improvements. No dark patterns. |
| 21 | `ndf-privacy-data-minimization-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews artifacts for data minimization and private-data risks. Forbids secrets; gives no binding legal advice. |
| 22 | `ndf-product-discovery-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Supports product discovery — audience, problem, value proposition, MVP scope, non-goals. |
| 23 | `ndf-project-adapter-quality-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews project adapters for quality, neutrality, and reusability. No automatic migration. |
| 24 | `ndf-project-brief-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Produces neutral project briefs — goal, scope, non-goals, risks, next steps. |
| 25 | `ndf-public-neutrality-guard` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Guards public-neutrality rules; flags private names, domains, or secrets. A reminder, not a CI gate. |
| 26 | `ndf-public-release-body-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews public release bodies for status correctness and neutrality. Performs no GitHub action. |
| 27 | `ndf-readme-quality-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews a README for entry point, clarity, honest status, and neutrality. Flags false claims. |
| 28 | `ndf-release-notes-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Creates or reviews release notes. Never asserts publication or performs tag/release actions. |
| 29 | `ndf-release-safety` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Checks release-adjacent work for safety boundaries. Never performs autonomous tag/release actions. |
| 30 | `ndf-skill-quality-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews skill documents for quality, scope, compliance, neutrality, and fail-closed behavior. Never executes skills. |
| 31 | `ndf-skill-supply-chain-risk-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews risks from external skill sources, unclear licenses, and unsafe patterns. No network or install. |
| 32 | `ndf-skill-trigger-quality-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews skill names and descriptions to avoid over-, under-triggering, and sprawl. No rename/merge/delete without WP scope. |
| 33 | `ndf-test-strategy-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Plans a test strategy — check levels, CI hints, acceptance criteria, regression risks. |
| 34 | `ndf-ui-style-system-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Creates UI style principles — layout, component style, color system, typography and accessibility hints. Forces no concrete implementation. |
| 35 | `ndf-ux-flow-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews user flows for clarity and friction. No dark patterns. |
| 36 | `ndf-v1-readiness-review` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Supports v1.0/RC/final readiness reviews. Never invents v1.0 claims or performs release actions. |
| 37 | `ndf-validation-evidence-reviewer` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Reviews validation and evidence artifacts; classifies sources and documents limits honestly. Invents no evidence. |
| 38 | `ndf-work-package-runner` | `SKILL.md` | 1 | Verified | NDF v1.0.0 | Standardized NDF work-package execution — stable role, guardrails, self-check, closing structure. No git/release actions. |

## Additional released file

| Path | Files | Status | Source | Purpose |
| --- | --- | --- | --- | --- |
| `README.md` | 1 | Verified | NDF v1.0.0 | Pack index of the released `.claude/skills/` path, listing the 38 docs-only skills. Not a skill directory and not counted toward the skill total. |

## Note on the pack index

The released `README.md` contains relative links into NDF repository paths
outside `.claude/skills/` (for example `../../docs/...`). Those targets do not
exist in CDS, so the links do not resolve here. The file was adopted unchanged
because upstream content must not be modified (see the provenance record). This
is a known, accepted consequence of the pinned copy.
