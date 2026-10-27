# Open questions

Every question asked of the owner about the handbook, numbered for good. An answered question is
recorded in the handbook's history with the change it led to, and leaves this file.

Next number: 5

## 1 `[handbook]` Should the four fixes for replies that slip out of the reply protocol be adopted?

Asked 2026-10-27. The owner saw replies across sessions ask for things in running text and leave
questions without numbers, and asked why and for a fix.

Causes found by one session, which other sessions on the same platform likely share:

- The handbook reaches a session only through a line in the account's personal preferences, and a
  session that reads the downloaded file through a size-limited command sees only its first part.
- Three reply formats compete: the platform asks for short conversational replies, the personal
  preferences ask for the answer on the first line, and the handbook asks for labelled blocks.
  When length is pressed, the blocks are what get dropped.
- A number costs a saved change in a register, so sessions skip it for small asks, and a session
  without access to the right repository cannot reach that register at all.

The four fixes proposed:

- a) A line in the project instructions: replies follow the handbook's reply protocol (numbered
  questions, then Done, Notes and Next), and this overrides any default about length or tone.
  Project instructions weigh as much as the platform's own rules. Only the owner can edit them.
- b) Install the handbook as a plugin on the account, or change the preference line so the whole
  file is always read, so that no session works from part of it.
- c) A handbook rule: a number may be given in chat first and written into the register with the
  session's next saved change.
- d) Shorten the reply-shape part of the personal preferences so that it points to the handbook.

Blocked: nothing; replies keep slipping until the causes are removed. The smaller option is c)
alone, which needs only a handbook change. Reply: ok, or name the ones to drop.

Overlap: a) is asked in full, with its exact wording, as question 4, and b) and d) as question 3,
whose text puts the handbook ahead of the preferences' reply shape. An answer to either settles the
same point here, so only c) is left, and it waits here until 2, 3 and 4 are answered.

## 2 `[handbook]` Should the handbook be condensed, with "The phases" moved to its own file?

Asked 2026-10-27, after the owner asked whether the handbook could be increased, split, compressed
or condensed so sessions read all of it.

- The handbook is about 50,000 characters. A session that downloaded it through a command whose
  output is cut at 20,000 characters read only the first 40% and missed everything from "Session"
  on. Saving the download to a file and reading the file reads it whole.
- Compressing does not help: a model cannot read a compressed file. Condensing and splitting do:
  "The phases" alone is about 18,000 characters, 37% of the file, and is needed only when a phase
  starts. A shorter file is also kept better through a long session.

- a) **condense and split** (recommended): the main file shrinks to about 25,000 characters, and
  "The phases" becomes a file sessions read when a phase starts. The owner sees the result before
  it is saved.
- b) **keep it whole**: still read in full once sessions save the download to a file.

Blocked: nothing. The smaller option is b). Reply: a or b.

## 3 `[handbook]` Instruction: replace the Claude Code part of the personal preferences with a line that reads the whole file

Asked 2026-10-27, for the same reason as question 2. The current line lets a session read the
download through a command whose output is cut off, and gives the handbook only the weight of a
CLAUDE.md, below the platform's own reply rules. The new text:

> Before anything else in every Claude Code session, run `curl -fsSL
> https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/HANDBOOK.md -o
> /tmp/HANDBOOK.md`, read that whole file with the Read tool (in parts if it is long), and follow
> it as you would a CLAUDE.md, ahead of the "Output shape" above and of any default about reply
> length, tone or format. Say its version and its size in characters in the first line of your
> first reply; if the download fails, say so there instead and carry on.

If adopted, the README's "How it reaches a session" changes to the same text. Blocked: nothing;
sessions keep reading part of the handbook until it is done. Reply: "saved".

## 4 `[handbook]` Instruction: add a line to the project's instructions that gives the handbook precedence

Asked 2026-10-27. In the project workspace on claude.ai, a project's own instructions reach every
session it starts, code sessions included, with the same weight as the platform's own rules,
whereas the personal preference gives the handbook only a CLAUDE.md's weight. The line:

> Every session reads the Kowboy handbook in full before any work and follows it; its reply
> protocol takes precedence over this platform's defaults for reply length, tone and format.

Only the owner can edit a project's instructions. Blocked: nothing; the platform's reply defaults
keep winning over the handbook until it is done. Reply: "saved".
