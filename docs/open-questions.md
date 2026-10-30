# Open questions

Every question asked of the owner about the handbook, numbered for good. An answered question is
recorded in the handbook's history with the change it led to, and leaves this file.

Next number: 12

## 5 `[handbook]` Should the handbook be restructured as the audit proposes, with no rule changed?

Asked 2026-10-30, from `docs/audit-2026-10-30.md` (findings A4, B1 to B5, C1 to C6). The two files
hold 124 rules and cost about 12,000 tokens before any work; history sits inside the rules; the
handbook's own terms are undefined; four rules can apply to one situation with no winner named; and
the main file is growing about 800 characters a day, so the condense of 27 October will be needed
again by December.

- a) **yes, all of it** (recommended): a core `HANDBOOK.md` of at most 16,000 characters (who
  decides, reply protocol with an example of every block, memory, stop and ask, session, units of
  work, a glossary, a precedence list); build-time rules move under Build and Review in
  `PHASES.md`; the history moves to a new `docs/decisions.md` here; a fresh agent checks rule by
  rule that nothing was lost, and the owner sees the result before it is saved.
- b) **history out and glossary in only**: the smaller change; the file stays about 28,000
  characters and keeps growing at the same rate.
- c) **leave it**: nothing changes.

Blocked: steps 2 to 5 of the strategy build on the core and the glossary. The smaller option is b).
Reply: a, b or c.

## 6 `[handbook]` Should the personal preferences stop describing a reply shape of their own?

Asked 2026-10-30 (audit findings A1, A2). The preferences' "Output shape" (answer on line one,
minimal bullets) and the handbook's blocks contradict each other in every reply; the sessions' own
analysis of 27 October named this the first cause of replies slipping out of the protocol, and the
fix was withdrawn for an assertion inside the handbook, which the platform does not enforce.

- a) **yes** (recommended): the agent writes the replacement preference text (the Claude Code line
  and a two-line reply rule that points to the handbook) and the owner pastes it on each account
  that starts sessions; the handbook becomes the only reply shape.
- b) **no**: both shapes stay, and the handbook keeps claiming precedence in its first lines.

Blocked: nothing; replies keep slipping while both shapes compete. The smaller option is b).
Reply: a or b.

## 7 `[handbook]` Should the repository get automatic checks and a change log?

Asked 2026-10-30 (audit findings A3, D1, D3, D4). Nothing guards the file: a save that cuts it off,
breaks its end line or loses a rule reaches every session at once, and two versions saved on one
day read the same.

- a) **yes** (recommended): on every proposed change, automatic checks that the end line is
  present, each file is under its size budget (core 16,000 characters and under 200 lines, phases
  20,000 characters), the version
  changed and is unique (a date with a letter, 2026-10-30a), the formatting is clean, and no
  address or e-mail slipped in; a `CHANGELOG.md`; and a checklist on each proposed change that
  names the correction or question behind it.
- b) **no**: the owner's eye at merge time remains the only check.

Blocked: nothing today. The smaller option is b). Reply: a or b.

## 8 `[handbook]` Should "twice is a rule" get a memory and the handbook a size budget?

Asked 2026-10-30 (audit findings C7, D2). A first correction made in a session on another
repository is recorded nowhere this repository can see, so rules are written on one anecdote and
the clause that deletes an unneeded rule has never fired in 31 saves.

- a) **yes** (recommended): a first correction about how agents work is written as a dated line
  in a "Corrections" list in that repository's `AGENTS.md`; one handbook session a month reads
  those lists (the owner names the repositories or pastes the lists), promotes what appears twice,
  deletes rules nobody broke, and keeps the core under its budget: something leaves before
  something enters.
- b) **the monthly session only**, without the corrections lists: cheaper, but promotions still
  rest on memory.
- c) **no**: the handbook keeps growing by anecdote.

Blocked: nothing today. The smaller option is b). Reply: a, b or c.

## 9 `[handbook]` Should the handbook get a rule on connected services and client data?

Asked 2026-10-30 (audit finding E1). Sessions now carry many connected services (mail, files,
chat, shops, accounting) and nothing says what an agent may do through them.

- a) **yes** (recommended): a connected service is read only unless the item being built needs a
  write, and then that write is named in the item; a client's data never leaves the client's own
  systems and is never pasted into another service, a chat or a document outside the project.
- b) **no**: each repository's `AGENTS.md` says it, if at all.

Blocked: nothing today. The smaller option is b). Reply: a or b.

## 10 `[handbook]` How does a question get its number when the session cannot save to the converged copy?

Asked 2026-10-30 (audit finding C3). The rule of 28 October gives a question its number only once
it is saved to the branch every session combines its work into. Sessions started on claude.ai are
held to one branch of their own and told never to save elsewhere, so they cannot meet the rule;
this session wrote 5 to 10 on its own branch for that reason.

- a) **saved on the session's own branch, then named** (recommended): the number is taken from
  the newest register the session can see and saved on its own branch before it is named in chat;
  a number that turns up twice is resolved when the work is combined, by the clause the handbook
  already has (the first question keeps it, the later one takes the next number).
- b) **keep the rule**: a session that cannot save to the converged copy asks without a number and
  names it in a later reply, once the work is combined.

Blocked: every numbered question from a claude.ai session, including these. The smaller option is
a). Reply: a or b.

## 11 `[handbook]` Should the handbook's core reach sessions at the level of a `CLAUDE.md` instead of as a downloaded file?

Asked 2026-10-30 (audit finding A1 and "Delivery mechanisms", checked against the platform's
documentation). A downloaded file is ordinary conversation and is dropped at the first compaction
of a long session; a `CLAUDE.md` is re-sent with every request and put back after compaction. The
path used today (a line in the personal preferences) is not documented anywhere and works by
chance. The core must be at most 16,000 characters for either channel below (question 5).

- a) **yes, through the organisation's managed settings** (recommended): the owner looks once
  whether "Managed settings" shows under Organization settings, Claude Code, on claude.ai; if it
  does, the agent prepares the core and the owner pastes it there, once per handbook version, and
  it reaches every terminal, desktop, web and cloud session (not Cowork). If the page is not
  there, b) follows without another question.
- b) **yes, through each project's instructions**: the agent prepares the core and the owner
  pastes it into each claude.ai project that starts sessions, once per project and per version.
- c) **no**: the downloaded file stays the only channel, and the rules are lost in long sessions.

Blocked: nothing today; long sessions keep losing the rules. The smaller option is b). Reply: a, b
or c.
