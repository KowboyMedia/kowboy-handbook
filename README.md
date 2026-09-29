# Kowboy handbook

How agents work at Kowboy, in one place: the rules that hold in every session
(`plugins/kowboy-handbook/KOWBOY-HANDBOOK.md`), the playbook of phases (`PLAYBOOK.md` and one
skill per phase), the hooks that enforce them, and the starting kit for a repository's own files
(`template/`). Edit here only.

## Two ways it reaches a session

1. **As a plugin on your Claude account (recommended).** Once, in claude.ai: open Customize,
   then Plugins, choose to add a marketplace from GitHub and paste `KowboyMedia/kowboy-handbook`
   (this repository is private, so the account's GitHub connection must include it; if the add is
   refused, grant the Claude GitHub app access to this repository under Settings, Connectors,
   GitHub, and add again). Then install the plugin named `kowboy-handbook` from that marketplace.
   From then on every session you start, in the browser, in Cowork or in the terminal, on any
   repository including a customer's, carries the handbook, the playbook, the skills and the
   hooks; nothing is copied into the repository. An organization Owner can set it to "Installed by
   default" or "Required" for every member, which makes it the team's way of working.
   A repository still gets its own files once: open a session on it and say "set up this repo".
   The `start` skill copies `CLAUDE.md`, `AGENTS.md`, the four memory files under `docs/`,
   `.claude/settings.json`, `.github/CODEOWNERS` and the register check from the plugin's
   `template/` folder, fills `AGENTS.md` with what is true in that repository, and goes on to the
   discovery round.
2. **As a copy in the repository.** For a repository read by agents other than Claude, or where
   the plugin is not on, `.github/sync.yml` lists the repositories that receive a copy of the
   handbook, the playbook, the skills and the hooks whenever they change here; the copy is
   versioned with the code and imported by the repository's `CLAUDE.md`. The plugin steps aside in a
   repository that carries a copy, so nothing loads twice.

Setup for the copy, once: add a fine-grained token as the secret `SYNC_TOKEN` in this repository's
settings (repositories: the ones in `sync.yml`; permissions: Contents read and write, Metadata
read). Until it exists, an agent copies the files on request.

Why a copy and not a link: Claude Code reads instructions only from files in the repository it
works in, from the plugins on the account, or from server-managed settings. Its `@import` takes a
path in the repository, never a web address, and the AGENTS.md standard has no import at all.

## Layout

```
.claude-plugin/marketplace.json     lists the plugin, so the repository can be added as a marketplace
plugins/kowboy-handbook/            the plugin
  .claude-plugin/plugin.json        its manifest
  KOWBOY-HANDBOOK.md                the rules that hold all the time
  PLAYBOOK.md                       the phases and when each applies
  skills/<phase>/SKILL.md           one skill per phase
  hooks/                            session start (handbook + memory), one line per turn, format after every write, no turn ends with unsent saved work
  template/                         the starting kit for a repository: CLAUDE.md, AGENTS.md skeleton, docs/ memory files, settings.json, CODEOWNERS, register check
.github/sync.yml                    the copy path: which repositories receive which files
```
