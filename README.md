# Kowboy handbook

`HANDBOOK.md` is how agents work with us, for every session someone at Kowboy starts, on any
repository: ten rules and the shape of a reply, kept under 4,000 characters. `WORK.md` is its
required second page: what each rule covers, when to ask and when to go, the question log and
the repository's memory, code, security and done; a session reads it before any work in a
repository. `PHASES.md` holds the steps of each phase, read when that phase starts. The history
of every rule, with the owner's words, is in `docs/decisions.md`; open questions about the
handbook are in `docs/open-questions.md`, the order of work in `docs/next-steps.md`, and the
quiz that is run after every change in `tests/`. All of it lives only here. Nothing is copied
into a repository, and nothing in this repository reaches another repository on its own.

**This repository is public.** It holds how we work and nothing else: never a client's name, a
credential, a token, an address, a price, a person's data or anything from a project. Anything of
that kind belongs in the project's own repository, which is private.

## How it reaches a session

Through the Kowboy package, a Claude Code plugin kept in this repository (`.claude-plugin/`,
`hooks/`, `skills/`, `agents/`). Each person adds it once to their claude.ai account, and it then
updates by itself from this repository. In every session it:

- gives `HANDBOOK.md` and `WORK.md` whole at the start and after the session's memory is
  compacted;
- repeats the ten rules at every message;
- holds a dangerous action on the platform's permission prompt, naming the rule, until the
  operator allows it: deleting outside the working folder, overwriting or deleting on GitHub,
  dropping a database, logging in to a server or deploying, writing to a server or through a
  connected service, sending mail, starting agents as separate programs, editing agents' rule
  files, and here the handbook and the package themselves;
- sends a reply back once when it lacks its state line, or waits for the operator without a
  numbered question, and has the advisor (`agents/advisor.md`) check a reply's questions first;
- loads each phase of `PHASES.md` as a skill when that phase starts.

The hold is a net, not a wall: it reads commands as text and can miss one, such as a deletion
inside a script. It needs `python3` on the machine. Its tests: `python3 -m unittest discover
tests/package`. In the terminal, if `/plugin` does not list it, add it there with:

```
/plugin marketplace add KowboyMedia/kowboy-handbook
/plugin install kowboy@kowboy
```

How each person sets it up is in `docs/setup-new-account.md`.

## Changing it

Only here, in a session on this repository, when the owner asks for the change in plain words:
never implicitly and never as an agent's choice (rule 8 of the handbook).
Save it, and the next session anywhere has it. Each change gets a line in `docs/decisions.md` with
the date and the owner's words; the rule itself stays short. A rule that holds in one repository
only goes into that repository's `AGENTS.md`, not here. A question about the handbook that must
wait is recorded here, in `docs/open-questions.md`, never in another repository's register, and
names no client.
