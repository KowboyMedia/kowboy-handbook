# Kowboy handbook: phase "Setup"

Version 2026-11-16q.

## Start a repository

When: a repository is new, or lacks a strategy, acceptance criteria or the memory files and has no code yet. A repository with code follows "Bring up an existing repository".

- `AGENTS.md` with only what is true there: the parts of the product and their tags, the commands an agent cannot guess, the repository's own rules and checks, and "Design: none" or `DESIGN.md`. The four memory files.
- What the operator has (a concept, reference sites, data, old documents) goes under `docs/inputs/`, unchanged.
- Discover, then write `docs/strategy.md` from the answers: the features; the purpose in three sentences; the parts and the connections between them; the data and which part owns each piece; the technology, each choice the widely used one with one clause why; the hosting and how a change reaches staging and live; the acceptance criteria, numbered, each testable without a person; what is out of scope.
- The operator approves the strategy, as at most five decisions.
- Then the skeleton: one folder per part; automatic checks (build, types, tests with none skipped, no secrets); staging published from the shared copy; every acceptance criterion mapped to a named test.

## Bring up an existing repository

When: a repository that already has code starts working this way.

- Change no code yet. Read the code, its history and what the operator gives; run the build and the tests to see what works.
- `AGENTS.md` and the four memory files as in "Start a repository", from what is true today.
- `docs/strategy.md` with the same sections as in "Start a repository", describing the product as it is, not as it should be. The acceptance criteria are what it does today, numbered. What looks wrong goes into `docs/known-bugs.md` and what is unclear into `docs/open-questions.md`; neither is fixed now.
- The operator confirms only what the code could not tell, as at most five decisions.
- First item: the automatic checks that can run on what exists, and a staging if there is none. If the product is live, check what the first go-live asks for in "Release and operate"; each gap becomes an item.
- From then on, a part is brought up when an item first touches it: first the tests that pin what it does today, then the change. Nothing is restructured, renamed or upgraded unless an item asks for it.

End of the phase.
