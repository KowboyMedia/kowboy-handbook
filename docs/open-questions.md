# Open questions

Every question asked of the owner about the handbook, numbered for good. An answered question is
recorded in the handbook's history with the change it led to, and leaves this file.

Next number: 25

## 22 `[handbook]` Instruction: change your preferences and your environment's setup script so every session works from one copy of the handbook, the newest, and treats it as binding; then say "done".

Asked 2026-11-01. Replaces 17, 20 and 21. The steps and both texts are in
`docs/setup-new-account.md`, parts 0 and 1. The colleague gets the same steps on Slack when the
owner says so.

## 23 `[handbook]` Should the handbook say that your answer to a question goes back only to the thread that asked it, and is never passed to another thread unless that thread owns the subject?

Asked 2026-11-01. A coordinator in a project committed to this rule; the handbook has the thread
rule and the plain-words rule but not this one. Reply: yes or no.

## 24 `[handbook]` Should every cloud session, whatever its environment, fetch the newest handbook itself when it starts and get a short reminder of the reply shape with every message you send?

Asked 2026-11-08. Replaces 22 if answered a) or b). The owner reports that three of four sessions
today did not follow the handbook. Found in this session: the environment's copy was 2026-11-01a
while the live one is 2026-11-08a (the script has no date line, so the copy waits for a rebuild);
the "Default" environment has no setup script, so a session there has no handbook file at all and
depends on the preferences line alone; the personal preferences are still the older text with an
"Output shape" of their own, which competes with the reply protocol; the handbook is about 30,000
characters and nothing restates it during a long conversation. The platform itself fixes the same
drift for its Slack sessions with a reminder injected on every message.

Rejected without asking: a copy in each repository's `AGENTS.md` (decided against on 2026-10-31
and 2026-11-01; it would not load more strongly than the personal `CLAUDE.md` it already is, and a
client's repository gets none of the handbook).

- a) Fetch at start and a reminder on every message (recommended). Each environment's setup
  script becomes one line that runs a start file kept in this repository; the start file sets a
  session-start step that loads the live handbook (also after compaction) and a per-message step
  that adds a short card (reply blocks, ask-or-go) kept here too. One source, no lag, drift held
  in long conversations. Owner's cost: approve one card for this environment, paste one line into
  the two others, once. Not yet tested whether the platform caps what a start step may add; if it
  does, the handbook stays as the instruction file and only the card goes through the step.
- b) Fetch at start only. Removes the lag and the missing copy in "Default"; long conversations
  still drift. Same owner cost.
- c) As now. No cost; the failures go on.

Reply: a, b or c.

