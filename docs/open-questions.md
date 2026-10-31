# Open questions

Every question asked of the owner about the handbook, numbered for good. An answered question is
recorded in the handbook's history with the change it led to, and leaves this file.

Next number: 16

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
