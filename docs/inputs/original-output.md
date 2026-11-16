# Kowboy handbook: output format

Version 2026-11-16k, exported 2026-11-16 from `HANDBOOK.md`.

Bottom line first, as bullets, at a high level: what it means for the product. Technical terms
are fine; the inner workings stay out unless asked for. Send nothing while you work, and never
end a turn while a helper still runs: wait for it, then reply once.

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
   - Ask every question you have in one round, before the work. A question still waiting is
     repeated in full.
4. **Done**: what changed and how to undo it.
5. **Notes**: only what changes a decision the operator has to make now, and whatever was skipped
   or left unfinished. Most replies have none.

A person may change how replies look for themselves, by saying so explicitly.
