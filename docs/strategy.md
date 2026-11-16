# Strategy

## Features

- Now: every agent in every Kowboy project holds the nine rules and the output format in every session.
- Now: an agent reads a phase only when that phase starts, so the text it must always hold stays small.
- Now: a change merged into `main` reaches every project within a day, with no one copying files.
- Now: people read the handbook online, on GitHub.
- Out: enforcing the rules with hooks or branch protection; review of synced changes before they land (decision 4).

## Purpose

Kowboy Media's agents follow one shared handbook. The rules must be obeyed reliably, so the text an agent always holds is kept small and the phases are read only when needed. The handbook lives in one public repository so people can read it online and every project stays in sync.

## Parts and connections

- **Handbook text:** `kowboy-handbook-rules.md`, `kowboy-handbook-output.md`, `kowboy-handbook-phases.md` and `kowboy-handbook-phases/`.
- **Sync:** `kowboy-handbook-sync.sh`, run by `kowboy-handbook-sync.yml` inside each project.
- **Connections:** the sync reads the handbook text by its file names. In a project it owns three things: the block between `<!-- kowboy-handbook:start -->` and `<!-- kowboy-handbook:end -->` in `AGENTS.md`, the folder `kowboy-handbook-phases/`, and the line `@AGENTS.md` in `CLAUDE.md`. The phase index names phase files by their file names.

## Data

- The handbook text is owned by this repository. Copies in projects are generated; edits to them are overwritten.
- Everything else in a project's `AGENTS.md` and `CLAUDE.md` is owned by the project and kept.
- The text as the operator first gave it is kept unchanged in `docs/inputs/`.

## Technology

- Markdown: every agent reads it and GitHub shows it.
- Bash and awk: present on every GitHub runner and developer machine, nothing to install.
- A scheduled GitHub Actions workflow in each project: it runs with that project's own token, so no shared secret is needed.

## Hosting and how a change goes live

Public on GitHub. A change is made on a working branch, which is staging. It goes live when merged into `main`; each project's workflow then commits it to that project's default branch at its next daily run, or at once through "Run workflow".

## Acceptance criteria

Each is a test in `tests/kowboy-handbook-sync.test.sh` with the same number.

1. A project without `AGENTS.md` gets one holding the rules, the output format and the phase index, plus the phase files.
2. A project's own `AGENTS.md` text is kept, with the block on top.
3. A second run changes nothing.
4. A change to the handbook text replaces the block, and only the block.
5. A phase file removed from the handbook is removed from the project.
6. Every phase file is named in the index, every name in the index exists, and each file ends with "End of the phase."
7. `CLAUDE.md` loads `AGENTS.md`, once, and keeps its own text.
8. A missing handbook file stops the sync with a message naming it, and the project is left unchanged.
9. This repository's own `AGENTS.md` block matches the handbook text.

## Out of scope

- Hooks, branch protection and repository settings in projects: set by the operator.
- An automatic check in this repository that runs the tests on every change: proposed, not made (rule 5).
- Agents that cannot read files from the repository.
