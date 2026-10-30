# Open questions

Every question asked of the owner about the handbook, numbered for good. An answered question is
recorded in the handbook's history with the change it led to, and leaves this file.

Next number: 14

## 5 `[handbook]` Should the handbook be restructured as the audit proposes, with no rule changed?

Asked 2026-10-30, from `docs/audit-2026-10-30.md` (findings A4, B1 to B5, C1 to C6). The two files
hold 124 rules and cost about 12,000 tokens (a token is the unit a model reads, roughly four
characters) before any work; history sits inside the rules; the handbook's own terms are
undefined; and the main file is growing about 800 characters a day, so the condense of 27 October
will be needed again by December.

- a) **yes, all of it** (recommended): a core of at most 24,000 characters, the procedure moved,
  no rule lost.
  - The core keeps every rule that must be in the agent's head: who decides, working with the
    owner, the reply protocol with an example of every block, memory, stop and ask, the anti-drift
    rules (simple beats clever, market-leading first, one code path, readable code, never invent a
    rule), session, units of work; it gains a glossary and the two lines that settle C1 and C2.
  - The procedure (the checklist for product texts, the deletion inventory, "Checks", "Definition
    of done", the index of phases; about 4,200 characters) moves into `PHASES.md`, where the
    Review phase enforces it; the history (about 2,500 characters) moves to a new
    `docs/decisions.md` here, one line per rule.
  - The arithmetic in the audit's step 1 lands at about 26,600, and the wording pass (one rule
    per line, imperative, no justification in the core, no abbreviations, examples kept) brings
    it to about 18,000 to 20,000. A fresh agent checks rule by rule that nothing was lost, and the
    owner reads the result before it is saved.
- b) **history out and glossary in only**: the file lands near 31,000 characters and keeps growing
  at the same rate.
- c) **leave it**: nothing changes.

Blocked: steps 2 to 5 of the strategy build on the core and the glossary. The smaller option is b).
Reply: a, b or c.

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

## 12 `[handbook]` Should one-way actions be refused by the platform's permission settings, not only by a rule?

Asked 2026-10-30 (audit finding F4; the owner: an agent deleted a complete database, no damage
done). A rule is guidance that the agent must remember hours into a session; the platform
documents that only its permission settings enforce. A refused command makes the agent stop and
ask by itself.

- a) **yes, through managed settings** (recommended): one deny list for both accounts, reaching
  every session, pasted once where question 11's core goes.
  - The list names the destructive commands: deleting data, databases, tables, environments,
    servers, apps or backups; forced overwrites of saved work; hosting and firewall changes. If
    the managed-settings page is not there, b) follows without another question.
- b) **yes, in each of our own repositories' settings**: the same list, kept in every repository
  we own; a client's repository gets it only with the client's word.
- c) **no**: the rule of 18 and 23 October stays the only guard.

Blocked: nothing today; the next one-way step rests on memory. The smaller option is b). Reply: a,
b or c.

## 13 `[handbook]` Should the ten rules on when to ask be replaced by one "Ask or go" test?

Asked 2026-10-30 (audit findings F1 to F3, F5; the owner: "too much noise and too little
autonomy"). The draft test is in the audit under "F. When to ask and when to go": three questions
in order (can the agent alone undo it; is it on the gate list; does more than one option meet the
requirements), three outcomes (Go, Default, Ask), and two lines that make a one-option question a
slip and the evaluation mandatory before any question.

- a) **yes** (recommended): the test replaces the ten rules and keeps their content; nothing
  becomes allowed that is not allowed today.
  - About 1,000 characters in place of about 5,000. Over-asking is corrected like acting without
    asking, so the agent's safe move is no longer to ask.
- b) **add the test, keep the rules**: the test on top; the file grows and the ten rules still
  compete with it.
- c) **no**: the ten rules stay as they are.

Blocked: step 1 of the strategy, which writes the test into the core. The smaller option is b).
Reply: a, b or c.
