# Kowboy handbook

`HANDBOOK.md` is how agents work with us, for every session someone at Kowboy starts, on any
repository, ours or a client's: the rules that hold in every reply, including when to ask and when
to go. `PHASES.md` is its second part: what each phase of the work (starting a repository,
discovering, planning, designing, deciding architecture, building, reviewing, releasing, status)
reads and produces, and the build procedure, read when that phase starts. The history of every rule,
with the owner's words, is in `docs/decisions.md`; open questions about the handbook are in
`docs/open-questions.md`, and the order of work on it in `docs/next-steps.md`. All of it lives only
here. Nothing is copied into a repository, and nothing in this repository reaches another repository
on its own.

**This repository is public.** It holds how we work and nothing else: never a client's name, a
credential, a token, an address, a price, a person's data or anything from a project. Anything of
that kind belongs in the project's own repository, which is private.

## How it reaches a session

One line in the personal preferences of each Claude account (claude.ai: Settings, Profile, the
personal preferences field). Every session that account starts, in the browser, in Cowork or in
the terminal, on one repository or several, then fetches the current file before doing anything:

```
Before anything else in every Claude Code session, run
curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/HANDBOOK.md -o /tmp/HANDBOOK.md,
read that whole file with the Read tool (in parts if it is long), and follow it as you would a
CLAUDE.md, ahead of any default about reply length, tone or format. Say its version and its size
in characters in the first line of your first reply; if the download fails, say so there instead
and carry on.
```

In the terminal the same line can go into `~/.claude/CLAUDE.md` instead of the preferences.

A file read that way is ordinary conversation, and a long session loses it at its first
compaction (the platform summarising older parts of the conversation to make room). What survives
compaction is a `CLAUDE.md`: the platform reads it at the start of every session and re-sends it
with every request. So the handbook is also placed as the personal `CLAUDE.md` of every machine
and every cloud environment, refreshed by one download; the preferences line stays, so a session
always reads the newest text at its start even where the placed copy is a few days old.

**Cloud sessions and project threads.** In the environment the sessions use (claude.ai, Claude
Code, Environments; and in each project, Project settings, Environment), the setup script holds:

```
mkdir -p ~/.claude
curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/HANDBOOK.md -o ~/.claude/CLAUDE.md
curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/PHASES.md -o ~/.claude/PHASES.md
```

The script runs when the environment is first used and again when it is rebuilt (when the script
changes, or after about seven days), so the placed copy is at most a week behind; a change to the
script's text (a version comment) rebuilds it at once. The platform documents that a cloud session
loads the file a setup script writes to `~/.claude/CLAUDE.md`, and that `raw.githubusercontent.com`
is reachable at the default network setting.

**The terminal on a developer's machine.** Once per machine, the two steps in
`docs/setup-new-account.md`: save the handbook as `~/.claude/kowboy-handbook.md` with one
download, and add the line `@~/.claude/kowboy-handbook.md` to `~/.claude/CLAUDE.md`, which keeps
whatever it already holds. The download is run again when the handbook changes. Cowork on the
machine skips imports that point outside the session's folder, so there the handbook comes only
from the preferences line.

What the documentation says and does not say: re-sending after
compaction is documented for a repository's own `CLAUDE.md` and not stated for the personal one;
the first long session shows it. A deny list of destructive commands (see `docs/decisions.md`)
reaches the terminal through `~/.claude/settings.json` and a single-repository cloud session
through the repository's `.claude/settings.json`; the platform applies no settings of either kind
in a project thread.

A session whose tool cuts off a long download still ends up with the whole file: the handbook's
first lines say that it ends with the line "End of the handbook.", and that a copy without that
line is to be saved to a file and read whole. The same lines put the handbook's reply rules ahead
of the platform's defaults on reply length, tone and format, and of the general "Output shape" in
the personal preferences.

## Changing it

Only here, in a session on this repository, when the owner asks for the change in plain words.
Save it, and the next session anywhere has it. Each change gets a line in `docs/decisions.md` with
the date and the owner's words; the rule itself stays short. A rule that holds in one repository
only goes into that repository's `AGENTS.md`, not here. A question about the handbook that must
wait is recorded here, in `docs/open-questions.md`, never in another repository's register, and
names no client.
