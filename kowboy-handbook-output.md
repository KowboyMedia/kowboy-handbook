# Kowboy handbook: output format

Version 2026-11-18a.

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
   - Before asking, look for the answer in the handbook, `docs/` and the code. Ask only when a
     wrong guess would be costly: it changes what gets built, cannot be undone, or is the
     operator's alone under the rules. Decide everything else, list it under Done, and never ask
     what does not block the goal.
   - Ask every question you have in one round, before the work. A question is written in full
     once, when it is asked; while it waits, later replies name only its number in Status.
4. **Done**: what changed and how to undo it, at most three bullets.
5. **Notes**: only what changes a decision the operator has to make now, and whatever was skipped
   or left unfinished, at most three bullets. Most replies have none.

A person may change how replies look for themselves, by saying so explicitly.

## Language

When: always, for all you write to people and to helpers: replies, questions, reports, the memory
files in `docs/`, commit messages, pull request text and prompts. Not for product text, code or
quotations.

Write in ASD-STE100 Simplified Technical English (STE). These are its core rules. If a rule and
the reply shape above disagree, the reply shape wins. Its fixed labels, such as "Working", stay as
they are.

- Use common words. Give each word one meaning, and use the same word for the same thing every
  time.
- Use a technical name or a technical verb only when no common word does the job.
- Write one idea in each sentence. An instruction has at most 20 words, a description at most 25.
- Write an instruction as a command: "Merge the branch." Put a condition before it: "If the test
  fails, stop."
- Use the active voice as much as possible: say who or what does the action.
- Use only the simple present, past and future tenses. Do not use the "-ing" form of a verb,
  except in a technical name such as "staging".
- Use a verb, not a noun made from a verb: "approve", not "give approval".
- Do not leave out "a", "the" or "this" to make a sentence shorter.
- Do not put more than three nouns in a row.
- Write one topic in each paragraph, in at most six sentences.

## Status

When: the operator says "status".

Read-only. The reply shape, without its limits on length, and nothing else: the first line is the session's state and "Where to pick up" from `docs/next-steps.md`; Questions, every open entry of `docs/open-questions.md`, one line each; Done, what is in staging and not yet live, one line each; Notes, every entry of `docs/known-bugs.md`, one line each.
