# Decisions

One line per rule or structural decision about the handbook: date, the decision, who decided.
Append only; a changed decision is a new line that says what it supersedes. The lines up to
2026-10-30 are the history that sat inside the rules until the restructure of 2026-10-31.

- 2026-09-19 and 2026-09-20 · Write for the product owner: plain words, no git words, every term
  explained; a rule, not a preference · the owner.
- 2026-09-20 · Tooling inside the work is the agent's call, never asked · the owner.
- 2026-09-20 · Market-leading solutions and patterns first: a production strategy, not a
  preference · the owner.
- 2026-09-20 · A library or framework added, dropped or swapped, or a departure from an approved
  proposal: pause, propose with the net value, wait · the owner.
- 2026-09-20 and 2026-09-21 · The reply protocol of labelled blocks: questions had to be searched
  for in a page of prose · the owner.
- 2026-09-23 · An ask that only describes a situation cannot be answered; it belongs in Notes with
  a question after it · the owner.
- 2026-09-27 · "I feel I am guiding you instead of you figuring out these things": the agent is
  the architect and product lead; the owner only makes decisions · the owner.
- 2026-09-27 · A Default: silence is the answer; asked before the work · the owner.
- 2026-09-27 · At most three questions per reply, five only when all five block today · the owner.
- 2026-09-27 · Done lines carry the undo word; the agent keeps the means to undo · the owner.
- 2026-09-27 · Twice is a rule · the owner.
- 2026-09-27 · A fresh pair of eyes before the owner's (definition of done) · the owner.
- 2026-09-29 · A question gets an answer, not a change · the owner.
- 2026-09-29 · Bullets, not paragraphs · the owner.
- 2026-09-29 · Questions are labelled with their register number, never a list position: "1."
  and "2." read as the numbers while they were 113 and 114 · the owner.
- 2026-09-29 · One decision per question, no options or reasoning in it; the agent's recommended
  option comes first, as a) · the owner.
- 2026-09-29 · Each repository's files hold only what is about that repository · the owner.
- 2026-09-29 · A change to how agents work, or beyond the repository worked on, is a gate · the
  owner.
- 2026-10-06 · A deletion is a complete clean-up · the owner.
- 2026-10-06 · Every text in the product is written for the person who reads it · the owner.
- 2026-10-07 · A clear winner is noted, not raised; picking the simplest option at hand "does not
  condone the agent to try to actively find a better solution": the agent looks for better · the
  owner.
- 2026-10-15 · A live site is read-only for an agent · the owner.
- 2026-10-18 · No deleting stored data that is kept nowhere else without the owner's explicit yes,
  even when it follows from an asked-for change · the owner.
- 2026-10-19 · Options in rising letter order from the top; questions in rising number order;
  blocks only when they hold something; discussion mode: plain answers, Questions block only · the
  owner.
- 2026-10-19 · Decide architecture: repeat the aim back first (a search was designed twice on a
  misreading of its aim); design for the stated goal, never today's data ("like me asking you to
  design a car, and you design a tractor"); a fresh check against the owner's words · the owner.
- 2026-10-21 · One question round, then execution: "If there are options with critical
  differences, ask the questions first. Then execute without asking more questions" · the owner.
- 2026-10-23 · A clear winner is done, not offered; being doable by the agent alone is one input
  to "best", never the deciding one (editing the existing document kept the link the owner already
  had); one-way decisions need an explicit yes and a backup plan · the owner.
- 2026-10-24 · A finished thread's last reply says it can be closed · the owner.
- 2026-10-27 · Never go quiet on a promise; every reply names the session's state ("almost every
  session feels abandoned mid work. I don't know if you are working, idle or waiting for me and
  for what"); every request to the owner is a Questions bullet ("you seem to have requested three
  things they should be requested on the agreed format with bullets"); the handbook's reply
  protocol comes before the preferences' "Output shape"; every session reads all of it; the phases
  move to `PHASES.md` · the owner.
- 2026-10-28 · Every `decisions.md` line names who decided; writing a choice down is never the
  owner's approval · the owner.
- 2026-10-28 · Anything new that a person sees is asked before it is built, after the owner found
  features nobody had asked him about · the owner.
- 2026-10-28 · A number is the question's only once it is saved, after sessions working side by
  side kept taking the same numbers · the owner.
- 2026-10-29 · New feature, new thread · the owner.
- 2026-10-30 · Cold pickup · the owner.

- 2026-10-31 · The handbook is restructured with no rule changed: a core under 24,000 characters,
  aiming for 20,000, with every anti-drift rule in it and the ask-or-go test; the procedure moves
  to `PHASES.md` and the history to this file; a glossary and the two settling lines are added;
  the wording pass follows the rules in the audit; a fresh agent checks rule by rule that nothing
  was lost, and the owner reads the result before it is saved. Every version stays in the history
  and can be restored whole or file by file · the owner, question 5 a), 2026-10-31, "assuming the
  entire repo can be rolled back entirely or in part, if it does not turn out well".
- 2026-10-31 · The ten rules on when to ask are replaced by one "Ask or go" test
  (`docs/audit-2026-10-30.md`, section F) that keeps their content; a question with one option
  that meets the requirements is a slip; the options are scored before any question · the owner,
  question 13 a), 2026-10-31.
- 2026-10-31 · One-way actions are guarded by the rule and by a deny list in the platform's
  permission settings: through managed settings where the owner's plan offers them, otherwise in
  each of our own repositories' settings, never in a client's repository without the client's
  word. The list is configuration, not handbook text · the owner, question 12, 2026-10-31,
  "rulebook and permissions if possible, but that's outside of the scope of the handbook". Where
  the list is kept so that both accounts paste the same one (a reference file in this repository,
  next to the audit): agent's choice, not confirmed by the owner; asked as Default 15, 2026-10-31.
- 2026-10-31 · Over-asking is a slip, corrected like acting without asking; a question with one
  option that meets the requirements is not asked, and tooling is never asked. Provenance: the
  agent asked question 14 (one viable option) and Default 15 (where a configuration file lives)
  right after drafting the test · the owner, 2026-10-31: "you are currently asking me a question
  of the kind we are trying to eliminate" and "i dont even know what this means, pick the best
  option". This is the second correction of over-asking (the first, 2026-10-30: "too much noise
  and too little autonomy"), so it is a rule and goes into the core with the test.
- 2026-10-31 · A second agent advises on ask-or-go at three moments: before a one-way step, at a
  close call, and in the question round before the work; one line in the test · agent's choice on
  the recommendation of question 14, on the owner's correction above; not separately confirmed.
- 2026-10-31 · The deny list for one-way actions is kept as a reference file in this repository
  next to the audit, so both accounts and every repository we own paste the same one · agent's
  choice (Default 15), the owner: "pick the best option".
- 2026-10-31 · Questions 6 and 11 are taken on their recommendation: the personal preferences
  stop describing a reply shape of their own, and the core is delivered through the
  organisation's managed settings if the page exists, otherwise through each project's
  instructions. Both need only steps the owner alone can take, so they come back as one
  instruction with the texts ready, in item 2, not as questions · agent's choice on the owner's
  correction above; not separately confirmed.
- 2026-10-31 · A fix is proportional to its problem: a rare and harmless problem is accepted as
  debt in `docs/known-bugs.md` with its frequency and the condition to revisit, and new
  infrastructure to prevent it is never proposed · the owner, 2026-10-31: "Sometimes I get a
  suggestion to add a solution to an issue which can happen maybe once or twice over the course of
  a year and have no real consequence, and the agent wants to add a database to keep track of a
  state to prevent it."
- 2026-10-31 · The restructure is done: the core holds every always-on rule and the ask-or-go
  test; the procedure (Checks, the deletion inventory, the checks for product texts) is in Build
  in `PHASES.md`; the history is in this file; terms are explained under "Words used here" · item
  1, decided by question 5 a).
- 2026-10-31 · A question's number exists only once its entry is saved in the shared copy's
  register, and that save is made when the question is asked, never when it is answered: the
  entry alone goes straight to the shared copy, with the repository's own command or the
  platform's file-change tool given the file's current version, so a stale save is refused and
  the session takes the next number; a session that cannot save there asks without a number.
  Supersedes question 10's recommendation (a number saved on the session's own copy), which
  reserves nothing for other sessions · the owner, 2026-10-31: "Multiple threads working on a
  project repeatedly ask questions with the same numbers before I have time to reply ... Make sure
  they write down the question with number somewhere as they are asked, not as they are answered."
- 2026-10-31 · The Review phase gets check 11, "Proportion": a fix for a rare and harmless problem
  is reported as disproportionate, whatever its quality · agent's choice, the enforcement half of
  the proportional-fix rule; not confirmed by the owner.
- 2026-10-31 · The restructured core landed at 26,534 characters, above the 24,000 named for
  question 5 a): the test, the advisor, the proportional-fix rule, the numbering rule, the glossary
  and the examples added about 5,000 characters of new content after that figure was set, and no
  rule was cut to meet it. The budget going forward is question 8's to set · agent's choice, not
  confirmed by the owner.
- 2026-10-31 · The core reaches sessions as the personal `CLAUDE.md` of every machine and cloud
  environment, written by one download: a three-line setup script on the owner's cloud
  environment (selected in each project), and on each developer's machine a one-time download
  plus a session-start hook that refreshes it. The preferences line stays. Supersedes the
  managed-settings channel (question 11 a), which needs an organisation; the account is a Max plan
  without one · the owner, 2026-10-31: "There is no organization, I use max 20 and it does not
  exist in team configuration. Find another solution." Channel chosen on the platform's
  documentation (cloud-environments: a setup script that writes `~/.claude/CLAUDE.md` is loaded as
  user instructions; memory: user-scope files load in the terminal; Cowork skips outside imports,
  so the copy is the whole file) · agent's choice on the facts, not separately confirmed.
- 2026-10-31 · Not covered by any documented channel: a project thread applies no settings from a
  repository or a machine, so the deny list for one-way actions (question 12) reaches the terminal
  and single-repository cloud sessions only; in project threads the rule and the advisor are the
  guard · agent's finding, from the platform's documentation.
