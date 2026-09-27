# Kowboy agents

The one source of how agents work in every Kowboy repository, and the starting kit for a new one.

- `AGENTS-shared.md`: the Kowboy-wide rules, and `PLAYBOOK.md` with its phase skills in `template/.claude/skills/`: the procedure per phase. Edit here only; the action below copies them out.
- `template/`: what a repository needs to run the setup. A new project copies the whole folder to
  its root and fills in `AGENTS.md`. This repository is marked as a GitHub template, so "Use this
  template" does the copy.
- `.github/sync.yml` and `.github/workflows/sync-shared.yml`: on every change to the shared file or
  the hooks, a change for approval is opened in every repository listed in `sync.yml`.

Setup, once: add a fine-grained token as the secret `SYNC_TOKEN` in this repository's settings
(repositories: the ones in `sync.yml`; permissions: Contents, Workflows and Pull requests read and
write, Metadata read). From then on a change saved here lands in every listed repository within a
minute, into its staging branch where one exists. Until the token exists, an agent copies the files
on request. Marking this repository as a template is optional: an agent copies `template/` anyway.

Why a copy and not a link: Claude Code reads instructions only from files inside the repository it
works in. Its `@import` takes a path in the repository or on the same machine, never a web address,
and the AGENTS.md standard has no import at all. A hook could fetch the rules over the network at
session start, but it could not deliver the skills and hooks as files, and a session's access is
bound to its own repository, so the copy is the only way that works everywhere.
