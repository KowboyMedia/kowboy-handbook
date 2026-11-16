# Kowboy handbook: the phases

Version 2026-11-16j. Read a phase's section when that phase starts. It ends with "End of the
phases."

## Start a repository

When: a repository is new, or lacks the memory files.

- The four memory files.

## Plan an item

When: a change is more than one sentence, or touches more than one part or a connection.

- Anything visible is agreed before it is built: a reference, a sketch or a staging page, and
  one question.

## Decide architecture

When: before a choice later work builds on.

- Repeat the operator's aim back first; design only after the operator's yes.
- Design for the goal and scale the operator stated, never for today's data.
- A fresh agent checks the design against the operator's words before the operator sees it.
- Between two workable options, the one that can be undone wins.
- Every key has the least access.

## Review

When: before anything is reported done.

In this order:

1. Did an item or a decision ask for this change? If not: unasked for, take it back.
2. Is logic repeated that already existed?
3. Would the tests fail if the feature broke? Is anything skipped or edited to pass?
4. Is a data change breaking? Is there a field or a rule with no written source?
5. Bad input, a timeout, a half failure: what happens, and is it visible?
6. Are the documents and the memory files true?

## Release and operate

When: the operator says "release", or a health check is red.

1. Every check is green on staging.
2. The approved publish runs by itself, as "Keys and access" in `WORK.md` says. Watch the health
   check until it is green, keep the previous version ready and say in one line how it comes
   back.

End of the phases.
