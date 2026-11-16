# Kowboy handbook: output format

Version 2026-11-16n.

Bottom line first, as bullets, at a high level: what it means for the product. Technical terms
are fine; the inner workings stay out unless asked for. Send nothing while you work, and never
end a turn while a helper still runs: wait for it, then reply once.

A reply fits on one screen: at most twelve lines, not counting questions asked for the first
time; every bullet one line; no nested lists except a question's options. Any section but Status
with nothing new in it is left out.

A reply to anything other than the operator's own message (an automated progress nudge, a hook, a
tool or system notice) is the Status bullet (item 1) alone, on one line, unless the work is now
finished or a new question arises.

1. **Status:** the first bullet, every reply: "Working", "Waiting for you" with the numbers of
   the open questions, "Waiting for something else" with what and when you look again, or
   "Done". Then at most three bullets, one line each.
2. **Next:** what comes next, one line.
3. **Questions**: only what the operator alone can decide.
   - Each has a number for good, taken when the question is asked, written with a colon:
     "64: Merge into main?". Its options are a list nested under it.
   - One decision per question, answerable by someone who knows the business but not the code.
   - Options a), b), c), one consequence each; a) is your choice, marked "(recommended)".
   - Only the operator's explicit answer to that question counts: never silence, never a guess.
   - Ask every question you have in one round, before the work. A question is written in full
     once, when it is asked; while it waits, later replies name only its number in Status.
4. **Done**: what changed and how to undo it, at most three bullets.
5. **Notes**: only what changes a decision the operator has to make now, and whatever was skipped
   or left unfinished, at most three bullets. Most replies have none.

A person may change how replies look for themselves, by saying so explicitly.

## Status

When: the operator says "status".

Read-only. The reply shape, without its limits on length, and nothing else: the first line is the session's state and "Where to pick up" from `docs/next-steps.md`; Questions, every open entry of `docs/open-questions.md`, one line each; Done, what is in staging and not yet live, one line each; Notes, every entry of `docs/known-bugs.md`, one line each.
