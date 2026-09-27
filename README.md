# Kowboy agents

The one source of how agents work in every Kowboy repository, and the starting kit for a new one.

- `AGENTS-shared.md`: the Kowboy-wide rules, and `PLAYBOOK.md` with its phase skills in `template/.claude/skills/`: the procedure per phase. Edit here only; the action below copies them out.
- `template/`: what a repository needs to run the setup. A new project copies the whole folder to
  its root and fills in `AGENTS.md`. This repository is marked as a GitHub template, so "Use this
  template" does the copy.
- `.github/sync.yml` and `.github/workflows/sync-shared.yml`: on every change to the shared file or
  the hooks, a change for approval is opened in every repository listed in `sync.yml`.

Setup, once: create this repository from these files, mark it as a template in its settings, add a
fine-grained token as the secret `SYNC_TOKEN` (repositories: the ones in `sync.yml`; permissions:
Contents, Workflows and Pull requests read and write, Metadata read), and list the repositories.
