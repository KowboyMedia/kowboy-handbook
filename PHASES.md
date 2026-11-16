# Kowboy handbook: the phases

Version 2026-11-16j. Read a phase's section when that phase starts. It ends with "End of the
phases."

## Start a repository

When: a repository is new, or lacks the memory files.

- The four memory files.
- Each technology choice is the widely used one, with one clause why.

## Plan an item

When: a change is more than one sentence, or touches more than one part or a connection.

- Anything visible is agreed before it is built: a reference, a sketch or a staging page, and
  one question.

## Decide architecture

When: before a choice later work builds on.

- Repeat the operator's aim back first; design only after the operator's yes.
- Design for the goal and scale the operator stated, never for today's data.
- A fresh agent checks the design against the operator's words before the operator sees it.
- Boring and widely used, with as few moving parts as possible: nothing without a need that
  exists now.
- Between two workable options, the one that can be undone wins.
- Every key has the least access.

## Build

When: a planned item is built.

- No test is skipped.
- Before deleting a feature, list everything that belongs to it: code, tests, settings, what it
  wrote and what it stored. Delete what nothing else uses in the same change; stored data
  under rule 1.
- A text in the product says what happened, what it means for the reader and what to do, calls
  things by the names the reader knows, and links to them.

## Review

When: before anything is reported done.

A second agent with no part in the work. In this order:

1. Did an item or a decision ask for this change? If not: unasked for, take it back.
2. Does it do what the item says, and nothing more?
3. Is logic repeated that already existed?
4. Would the tests fail if the feature broke? Is anything skipped or edited to pass?
5. Is a data change breaking? Is there a field or a rule with no written source?
6. Bad input, a timeout, a half failure: what happens, and is it visible?
7. Are the documents and the memory files true?
8. Do the texts a person reads pass the check in Build?

## Release and operate

When: the operator says "release", a health check is red, or something is wrong in
production.

1. Every check is green on staging.
2. The operator says "release". Nothing goes live before.
3. The approved publish runs by itself, as "Keys and access" in `WORK.md` says. Watch the health
   check until it is green, keep the previous version ready and say in one line how it comes
   back.

When something is wrong in production: every action there is the operator's decision.

End of the phases.
