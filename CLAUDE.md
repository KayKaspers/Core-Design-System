# CLAUDE.md

## Project

Core Design System (CDS)

CDS is the central design, brand, UX, UI, token, component, document, and
multi-channel design foundation for the Core ecosystem.

CDS is not merely a logo project, branding kit, or UI component library.

## Operating model

This repository follows the Nova Development Framework v1.0.0.

Roles:

- Nova owns strategy, architecture, work-package planning, review, and approval recommendations.
- Claude performs only explicitly scoped analysis or implementation work.
- Cursor is the primary development environment.
- The Human Maintainer owns commit, push, tag, release, merge, and publication actions.

## Mandatory working rules

1. Read the active work package and project context before changing files.
2. Operate only inside the explicitly allowed scope and allowed files.
3. Work fail-closed when instructions, source material, or authority are unclear.
4. Do not create additional scope merely because it appears useful.
5. Do not make final visual or technological design decisions unless the active work package explicitly authorizes them.
6. Do not introduce frameworks, packages, build systems, fonts, icons, licenses, or external assets without explicit approval.
7. Do not commit, push, merge, tag, release, publish, or rewrite Git history.
8. Do not treat generated output as an authoritative source.
9. Preserve a clear distinction between normative sources and generated artifacts.
10. Accessibility, licensing, provenance, offline use, and maintainability are first-class concerns.

## Current restrictions

Until explicitly authorized, do not decide or implement:

- final logos,
- final colors,
- final typography,
- final iconography,
- final visual language,
- concrete design tooling,
- concrete component frameworks,
- token build tooling,
- package architecture,
- public compatibility commitments.

## Required project context

Before beginning a work package, inspect at minimum:

- `README.md`
- `project-system/PROJECT_PROFILE.md`
- `project-system/NEXT_PHASE.md`
- `project-brain/PROJECT_BRAIN.md`
- relevant governance and decision documents
- applicable local Claude Skills after the Skills Bootstrap has been completed

## Required completion report

Every completed work package must end with:

### Rückmeldung an Nova

Include:

- result and status,
- files created or changed,
- validations performed,
- decisions added or changed,
- risks added or changed,
- deviations from the prompt,
- unresolved issues,
- recommended next action,
- explicit confirmation that no commit or push was performed.

### Compact Context Summary

Provide a compact continuation summary containing:

- active project phase,
- completed work package,
- current repository state,
- important constraints,
- open decisions and risks,
- exact next recommended work package.
