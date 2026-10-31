# Open questions

Every question asked of the owner about the handbook, numbered for good. An answered question is
recorded in the handbook's history with the change it led to, and leaves this file.

Next number: 15

## 6 `[handbook]` Should the personal preferences stop describing a reply shape of their own?

Asked 2026-10-30 (audit findings A1, A2). The preferences' "Output shape" (answer on line one,
minimal bullets) and the handbook's blocks contradict each other in every reply; the sessions' own
analysis of 27 October named this the first cause of replies slipping out of the protocol, and the
fix was withdrawn for an assertion inside the handbook, which the platform does not enforce.

- a) **yes** (recommended): the handbook becomes the only reply shape.
  - The agent writes the replacement preference text: the Claude Code line, and a two-line reply
    rule that points to the handbook. The owner pastes it on each account that starts sessions.
- b) **no**: both shapes stay, and the handbook keeps claiming precedence in its first lines.

Blocked: nothing; replies keep slipping while both shapes compete. The smaller option is b).
Reply: a or b.

## 7 `[handbook]` Should the repository get automatic checks and a change log?

Asked 2026-10-30 (audit findings A3, D1, D3, D4). Nothing checks a save: one that cuts the file
off, breaks its end line or loses a rule reaches every session at once, and two versions saved on
one day are told apart only by a suffix typed by hand.

- a) **yes** (recommended): every proposed change is checked before it is combined, and the
  history is readable.
  - The checks: the end line is present; the core and the phases are each under 24,000
    characters; the version changed and is unique (a date with a letter,
    2026-10-30a); the formatting is clean; no address or e-mail slipped in.
  - A `CHANGELOG.md`, and a short checklist on each proposed change naming the correction or
    question behind it and, for a condense, the "no rule lost" check.
- b) **no**: nothing checks a save.

Blocked: nothing today. The smaller option is b). Reply: a or b.

## 8 `[handbook]` Should "twice is a rule" get a memory and the handbook a size budget?

Asked 2026-10-30 (audit findings C7, D2). A first correction made in a session on another
repository is recorded nowhere this repository can see, so rules are written on one anecdote and
the clause that deletes an unneeded rule has never fired in 31 saves.

- a) **yes** (recommended): first corrections are written down where the session is, and one
  session a month tends the handbook.
  - A first correction about how agents work becomes a dated line in a "Corrections" list in that
    repository's `AGENTS.md`.
  - The monthly session reads those lists (the owner names the repositories or pastes the lists),
    promotes what appears twice, deletes rules nobody broke, and keeps the core under its budget:
    something leaves before something enters.
- b) **the monthly session only**: cheaper, but promotions still rest on memory.
- c) **no**: the handbook keeps growing by anecdote.

Blocked: nothing today. The smaller option is b). Reply: a, b or c.

## 9 `[handbook]` Should the handbook get a rule on connected services and client data?

Asked 2026-10-30 (audit finding E1). Sessions now carry many connected services (mail, files,
chat, shops, accounting) and nothing says what an agent may do through them.

- a) **yes** (recommended): a connected service is read-only unless the item being built needs a
  write, and a client's data never leaves the client's own systems.
  - A write through a connected service is named in the item before it happens. A client's data
    is never pasted into another service, a chat or a document outside the project.
- b) **no**: each repository's `AGENTS.md` says it, if at all.

Blocked: nothing today. The smaller option is b). Reply: a or b.

## 10 `[handbook]` How does a question get its number when the session cannot save to the shared copy?

Asked 2026-10-30 (audit finding C3). The rule of 28 October gives a question its number only once
it is saved to the shared copy that every session's work is combined into. A session started on
claude.ai works in a copy of its own, combined into the shared copy later, and is told never to
save anywhere else, so it cannot meet the rule; this session wrote 5 to 11 in its own copy for
that reason.

- a) **saved in the session's own copy, then named** (recommended): a duplicate is resolved when
  the work is combined, by the clause the handbook already has.
  - The session takes the number from the newest register it can see and saves the entry in its
    own copy before naming the number in chat. When two sessions took the same number, the first
    question keeps it and the later one takes the next, as the handbook already says.
- b) **keep the rule**: a session that cannot save to the shared copy asks without a number and
  names it in a later reply, once its work is combined.

Blocked: every numbered question from a claude.ai session, including these. The smaller option is
a). Reply: a or b.

## 11 `[handbook]` Should the handbook's core reach sessions at the level of a `CLAUDE.md` instead of as a downloaded file?

Asked 2026-10-30 (audit finding A1 and "Delivery mechanisms", checked against the platform's
documentation). A downloaded file is ordinary conversation and is dropped at the first compaction
of a long session (the platform summarising older parts of the conversation to make room); a
`CLAUDE.md` is re-sent with every request and put back after compaction. The path used today, a
line in the personal preferences, is documented nowhere and works by chance.

- a) **yes, through the organisation's managed settings** (recommended): one paste by the owner
  per handbook version reaches every terminal, desktop, web and cloud session (not Cowork).
  - The owner looks once whether "Managed settings" shows under Organization settings, Claude
    Code, on claude.ai. If it does, the agent prepares the core and the owner pastes it there. If
    the page is not there, b) follows without another question.
- b) **yes, through each project's instructions**: one paste per claude.ai project and per
  version, and the core must first be cut to 16,000 characters, which cuts rules.
- c) **no**: the downloaded file stays the only channel, and the rules are lost in long sessions.

Blocked: nothing today; long sessions keep losing the rules. The smaller option is b). Reply: a, b
or c.

## 14 `[handbook]` Should a second agent advise on ask-or-go at the close calls?

Asked 2026-10-31, from the owner's idea. An agent asked to evaluate its options can pick, where
the same agent in the middle of the work cannot (the owner, 2026-10-30). A second agent with no
memory of the work would get only the owner's words for the item, the step or the options, the
test and the decisions file, and answer Go, Default or Ask with one line why. The gain comes from
the fresh context and from evaluating instead of acting; a stronger model than the session's
helps only where the session runs on a smaller one.

- a) **yes, at three moments** (recommended): before any one-way step, when the test lands on
  "close", and in the question round before the work, to strike options that do not meet the
  requirements.
  - One line in the test. The strongest model the account offers; a few thousand tokens a call.
    It cuts noise and catches boldness at planning time; it cannot refuse a command, which stays
    the deny list's job.
- b) **yes, before every question only**: cheaper; one-way steps rest on the test and the deny
  list.
- c) **no**: the agent applies the test alone.

Blocked: nothing; item 1 writes the test either way and adds the line if a) or b) is chosen. The
smaller option is b). Reply: a, b or c.
