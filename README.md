# Kowboy handbook

`HANDBOOK.md` is how agents work with us, for every session someone at Kowboy starts, on any
repository, ours or a client's. `PHASES.md` is its second part: what each phase of the work
(starting a repository, discovering, planning, designing, deciding architecture, building,
reviewing, releasing, status) reads and produces, read when that phase starts. Both live only here.
They are never copied into a repository, and nothing in this repository reaches another repository
on its own.

**This repository is public.** It holds how we work and nothing else: never a client's name, a
credential, a token, an address, a price, a person's data or anything from a project. Anything of
that kind belongs in the project's own repository, which is private.

## How it reaches a session

One line in the personal preferences of each Claude account (claude.ai: Settings, Profile, the
personal preferences field). Every session that account starts, in the browser, in Cowork or in
the terminal, on one repository or several, then fetches the current file before doing anything:

```
Before anything else in every session, run
curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/HANDBOOK.md
and follow that handbook as you would a CLAUDE.md. Say its version in the first line of your
first reply; if the fetch fails, say so in that line instead and carry on.
```

In the terminal the same line can go into `~/.claude/CLAUDE.md` instead of the preferences.

A session whose tool cuts off a long download still ends up with the whole file: the handbook's
first lines say that it ends with the line "End of the handbook.", and that a copy without that
line is to be saved to a file and read whole. The same lines put the handbook's reply rules ahead
of the platform's defaults on reply length, tone and format, and of the general "Output shape" in
the personal preferences.

## Changing it

Only here, in a session on this repository, when the owner asks for the change in plain words.
Save it, and the next session anywhere has it. A rule that holds in one repository only goes into
that repository's `AGENTS.md`, not here. A question about the handbook that must wait is recorded
here, in `docs/open-questions.md`, never in another repository's register, and names no client.
