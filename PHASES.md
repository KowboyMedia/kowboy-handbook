# Kowboy handbook: the phases

Version 2026-11-16g. Read a phase's section when that phase starts. It ends with "End of the
phases."

## Start a repository

When: a repository is new, or lacks a strategy, acceptance criteria or the memory files.

- `AGENTS.md` with only what is true there: the parts of the product and their tags, the
  commands an agent cannot guess, the repository's own rules and checks, and "Design: none" or
  `DESIGN.md`. The four memory files.
- What the operator has (a concept, reference sites, data, old documents) goes under
  `docs/inputs/`, unchanged.
- Discover, then write `docs/strategy.md` from the answers: the features; the purpose in three
  sentences; the parts and the connections between them; the data and which part owns each
  piece; the technology, each choice the widely used one with one clause why; the hosting and
  how a change reaches staging and live; the acceptance criteria, numbered, each testable
  without a person; what is out of scope.
- The operator approves the strategy, as at most five decisions.
- Then the skeleton: one folder per part; automatic checks (build, types, tests with none
  skipped, no secrets); staging published from the shared copy; every acceptance criterion
  mapped to a named test.

## Discover

When: a project starts, a feature is larger than one item, or the operator describes a wish.

- Read everything given. Ask nothing yet.
- List the features: each in one sentence of value to the user, marked now or later, and what
  is out.
- List the decisions the features need: each a question in plain words with at most three
  options, whether it can be undone, and a recommendation.
- Name the risks and unknowns and the cheapest way to find out. Unknowns go first.
- Bring the decisions in rounds of at most five, the most binding first; record each answer as
  it comes.
- Write the plan from the answers. The first item is the riskiest unknown or the thinnest
  slice that proves the design.

## Plan an item

When: a change is more than one sentence, or touches more than one part or a connection.

- Read the item, the strategy parts it touches, the decisions and the acceptance criteria.
- Bring the decisions this item and the next two need, now.
- Anything visible is agreed before it is built: a reference, a sketch or a staging page, and
  one question.
- Write the plan into the item: the one part it changes; what changes for the product, in one
  sentence; the test that proves it; the connection it touches (none, added to, or broken, and
  then widen, move, narrow as separate releases); the unknowns, each with a short trial first;
  what it does not do.
- Size it to one session and mark it "in progress" with the date.

## Design

When: something people look at is created or restyled. Never in a repository whose `AGENTS.md`
says "Design: none".

- Size first. None (existing patterns): build, one picture on desktop and one on mobile,
  compare with a neighbouring page. Light (inside a pattern, adding something): build against
  `DESIGN.md` and check yourself once. Full (a new page or look): the loop.
- `DESIGN.md`, once per repository, written by an agent from references the operator names:
  colours, type, spacing, rules for components, tone, and what to avoid. Real content from the
  start.
- The loop: build one section at a time; a second agent looks at desktop and mobile and scores
  order, contrast, spacing, every state and keyboard use; at most three passes. For a new look,
  two or three finished candidates side by side, and the operator picks.

## Decide architecture

When: before a choice later work builds on.

- Repeat the operator's aim back first; design only after the operator's yes.
- Design for the goal and scale the operator stated, never for today's data. Assumptions are
  written at the top, and one that changes the design is the operator's decision.
- A fresh agent checks the design against the operator's words before the operator sees it.
- Name the parts and the connections first. A part knows nothing beyond its connections.
- Boring and widely used, with as few moving parts as possible: nothing without a need that
  exists now.
- One shape and one operator per piece of data; raw input is kept; changes add, never break.
- Between two workable options, the one that can be undone wins.
- Every design meets this: every entry point checks who is calling and every key has the least
  access; personal data only where needed and never in logs; backups exist and a restore was
  rehearsed before the first go-live; measure before making anything faster.
- Record the decision, the options rejected and the condition to revisit.

## Build

When: a planned item is built.

- Order: the connection (types, schema), the failing test, the code, the documents; all in the
  same change.
- One part. Touching another is a new item.
- Settings come from the environment and are checked at start with a message that says what is
  wrong. Anything that runs unattended writes what it did, with an id that connects it.
- Tests give the same result every time, do not depend on each other, and run against the real
  local services, not imitations. None is skipped.
- The repository's `AGENTS.md` lists the checks that block; everything else is a warning.
- Before deleting a feature, list everything that belongs to it: code, tests, settings, what it
  wrote and what it stored. Delete what nothing else uses in the same change; stored data
  under rule 1.
- A text in the product says what happened, what it means for the reader and what to do, calls
  things by the names the reader knows, links to them, and is read once with real data by
  someone who does not know the code.

## Review

When: before anything is reported done.

A second agent with no part in the work. Report only failures, each with its fix, in at most ten
lines. In this order:

1. Did an item or a decision ask for this change? If not: unasked for, take it back.
2. Does it do what the item says, and nothing more?
3. Does a part know something beyond its connections?
4. Is logic repeated that already existed?
5. Would the tests fail if the feature broke? Is anything skipped or edited to pass?
6. Is a data change breaking? Is there a field or a rule with no written source?
7. Secrets, unchecked input, an entry point that does not check the caller, personal data in
   logs.
8. Bad input, a timeout, a half failure: what happens, and is it visible?
9. Are the documents and the memory files true?
10. Do the texts a person reads pass the check in Build?

## Release and operate

When: the operator says "release", a health check is red, or something is wrong in
production.

1. Every check is green on staging.
2. Say what changes for the people who use it, in their words.
3. The operator says "release". Nothing goes live before.
4. The approved publish runs by itself, as "Security" says. Watch the health check until it is
   green, keep the previous version ready and say in one line how it comes back.
5. Write the release into `docs/decisions.md`.

The first go-live adds: the address and its certificates answer; backups run and a restore was
rehearsed; the alerts were seen firing once; the undo is known; personal data and keys are only
where the design says; who is told, and in which words, is written beforehand.

When something is wrong in production: every action there is the operator's decision. First make
it safe, then find the cause, then fix it through staging. The cause goes into
`docs/known-bugs.md`. Libraries are updated once a month, as one item, with every test green.

## Status

When: the operator says "status".

Read-only. The reply shape, without its limits on length, and nothing else: the first line is the session's state and "Where to
pick up" from `docs/next-steps.md`; **Questions**, every open entry of `docs/open-questions.md`,
one line each; **Done**, what is in staging and not yet live, one line each; **Notes**, every
entry of `docs/known-bugs.md`, one line each.

End of the phases.
