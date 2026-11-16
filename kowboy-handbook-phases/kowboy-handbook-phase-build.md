# Kowboy handbook: phase "Build"

Version 2026-11-16n.

## Make a small change

When: the change fits in one sentence, stays inside one part, and touches no connection, stored data, access check or anything that cannot be undone. If one of these turns out wrong along the way, stop and plan it as an item.

- No plan. One question only if the request can be read two ways.
- Build as in "Build", with one difference: prove it the cheapest real way. A failing test first when behaviour changes; otherwise show the result once, as a picture on desktop and mobile or the output with real data. No test that only repeats the code.
- It gets the short review in "Review", then waits on staging and goes live with the next release.

## Plan an item

When: a change is more than one sentence, or touches more than one part or a connection.

- Read the item, the strategy parts it touches, the decisions and the acceptance criteria.
- Bring the decisions this item and the next two need, now.
- Anything visible is agreed before it is built: a reference, a sketch or a staging page, and one question.
- Write the plan into the item: the one part it changes; what changes for the product, in one sentence; the test that proves it; the connection it touches (none, added to, or broken, and then widen, move, narrow as separate releases); the unknowns, each with a short trial first; what it does not do.
- Size it to one session and mark it "in progress" with the date.

## Build

When: a planned item is built.

- Order: the connection (types, schema), the failing test, the code, the documents; all in the same change.
- One part. Touching another is a new item.
- The simplest code that does what the item says: no option, layer, library or case for a need that does not exist now.
- Every changed line serves the item. Anything else noticed on the way becomes a new item in `docs/next-steps.md`, not part of this change.
- A refactor changes no behaviour. If the part has no test for what it does today, write that test first; then the tests pass unchanged before and after, and none is edited.
- Settings come from the environment and are checked at start with a message that says what is wrong. Anything that runs unattended writes what it did, with an id that connects it.
- Tests give the same result every time, do not depend on each other, and run against the real local services, not imitations. An outside service with no local version is tested against its real responses, recorded. None is skipped.
- The repository's `AGENTS.md` lists the checks that block; everything else is a warning.
- Before deleting a feature, list everything that belongs to it: code, tests, settings, what it wrote and what it stored. Delete what nothing else uses in the same change; stored data under rule 1.
- A text in the product says what happened, what it means for the reader and what to do, calls things by the names the reader knows, links to them, and is read once with real data by someone who does not know the code.

End of the phase.
