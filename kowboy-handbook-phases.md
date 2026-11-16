# Kowboy handbook: the phases

Version 2026-11-16m. A workflow to follow with judgement, not rules: the nine rules are the only rules. "Run a session" is below and applies always. Every other phase is in its own file in `kowboy-handbook-phases/`: when a phase starts, read its file before you act. Each file ends with "End of the phase."

- `kowboy-handbook-phase-setup.md`: "Start a repository" when a repository is new, or lacks a strategy, acceptance criteria or the memory files and has no code yet; "Bring up an existing repository" when a repository that already has code starts working this way.
- `kowboy-handbook-phase-discover.md`: "Discover" when a project starts, a feature is larger than one item, or the operator describes a wish.
- `kowboy-handbook-phase-architecture.md`: "Decide architecture" before a choice later work builds on.
- `kowboy-handbook-phase-design.md`: "Design" when something people look at is created or restyled. Never in a repository whose `AGENTS.md` says "Design: none".
- `kowboy-handbook-phase-build.md`: "Make a small change" when the change fits in one sentence, stays inside one part, and touches no connection, stored data, access check or anything that cannot be undone; "Plan an item" when a change is more than one sentence, or touches more than one part or a connection; "Build" when a planned item is built.
- `kowboy-handbook-phase-review.md`: "Review" before anything is reported done.
- `kowboy-handbook-phase-release.md`: "Release and operate" when the operator says "release", a health check is red, or something is wrong in production.
- "Status" when the operator says "status": in the output format (`kowboy-handbook-output.md`).

## Run a session

When: every session, from the first message to the last.

- Start from `docs/next-steps.md`: say the goal of the session and what done means for it, one sentence each.
- Work until the goal is done or only the operator can move it. Never stop to ask whether to go on when the next step is known and needs nothing from the operator.
- Never ask what `docs/inputs/`, the strategy or `docs/decisions.md` already answer. Decide details that do not change what gets built yourself, and list them in the report so the operator can change them.
- What only the operator can give (a decision, access, an approval) goes into `docs/open-questions.md` at once, and the work goes on with the next thing that does not depend on it.
- If the plan stops serving the goal, or a clearly cheaper way to it shows up, bring that as a decision with a recommendation before going on.
- Done means the proof for the goal passes and the review found nothing left to fix. Report against the goal: done, or what is left and what it waits for.
- End by writing where things stand and where to pick up into `docs/next-steps.md`.
