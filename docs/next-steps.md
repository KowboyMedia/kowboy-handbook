# Next steps

The order of work on the handbook. "Resume next steps" means: read this, do the first item that is
not done, keep it current.

## Where to pick up

Item 9, the Kowboy package, is released (2026-11-16), installs from GitHub and is added to the
operator's account (57). The fresh-session check (2026-11-16, second thread): the handbook arrived
at the start and the rules at every message; the hold for `ssh -V` reached the operator as a permission
prompt in auto mode (59); a reply without its state was sent back; the handbook download is out
of "Worksuite 2.0" too (60). The installed copy is version 2026-11-16h, synced 14:38:58 UTC, 30 seconds before
2026-11-16i reached main: until it updates, sessions still get the removed second-correction rule.
Version 2026-11-16j is live (2026-11-16): agent-made and doubtful rules removed, nine rules,
the new reply format. Next: a fresh thread with "resume next steps" checks the version
the package delivers at its start (becomes a question if still h); if it is current, item 9 is
done. The
preferences stay as they are for now. The benchmark in `tests/bench/` is not run until the
operator says so (2026-11-16). The key clean-up (question 43) is booked with the product lead
for 2026-11-20. After item 9: item 11 (the one-page map of each repository), then item 4.

## Items

1. `[handbook]` Restructure: a core under 24,000 characters with every anti-drift rule in it,
   the ask-or-go test with the advisor line and the over-asking slip, the procedure into
   `PHASES.md`, the history into `docs/decisions.md`, a glossary, the two settling lines, the
   wording pass. One session. Done 2026-10-31 in this thread, checked rule by rule by a fresh
   agent, combined into the shared copy on the owner's word.
2. `[handbook]` Delivery: the handbook as the personal `CLAUDE.md` of every cloud environment
   (setup script) and every developer machine (download plus session-start hook); the texts are
   in the README. Done 2026-10-31 in this thread; waits for the owner's steps 16 and 17. The
   replacement preference text (question 6) follows once the placed copy is seen to survive a
   long session.
3. `[handbook]` The deny list for one-way actions, drafted as a reference file here, for
   `~/.claude/settings.json` on each machine and `.claude/settings.json` in each of our own
   repositories; project threads apply neither. Taken over by item 9 (question 25 a),
   2026-11-15): the package carries the blocks.
4. `[handbook]` Automatic checks on every save, a date-with-letter version, a `CHANGELOG.md`, a
   checklist for each change. One session. Ready (agent's choice, 2026-10-31).
5. `[handbook]` Dropped (question 8 c, 2026-10-31): no corrections lists, no monthly session.
6. `[handbook]` Twelve scripted prompts on reply shape, drift and ask-or-go, run in a fresh
   session after each handbook change. Taken over by item 9 (question 25 a), 2026-11-15): the
   package carries the test prompts.
7. `[handbook]` Done 2026-10-31: the connected-services rule is in the core (question 9 a).

8. `[handbook]` Three layers (question 24, the owner 2026-11-15). In progress 2026-11-15.
   - What changes: `HANDBOOK.md` is sorted into layer 1 (twelve absolute rules), layer 2 (the
     work, required) and layer 3 (preferences); every rule is moved as it stands; `PHASES.md`
     is untouched; one file still, so today's delivery keeps working.
   - What proves it: a word-for-word comparison with the live text, and a second agent with no
     part in the work comparing the two rule by rule.
   - Decides: 27 (what may change the preferences layer) and 28 (the owner reads layer 1 before
     it is live).
   - Not in it: shortening the wording of the moved rules, and the delivery (item 9).
9. `[handbook]` The Kowboy package (question 25 a), the owner 2026-11-15): one package each
   person adds once to their account, kept in this repository. It repeats layer 1 at every
   message, stops the dangerous actions by itself, sends back a reply that lacks its state or
   its questions, carries the phases to be loaded when a phase starts, and updates centrally.
   First step: the owner looks whether his plan offers adding a package (Customize, Plugins,
   Add); if not, back to the owner before anything is built. Then the preferences text and the
   environment's setup script are replaced once, which closes 22. One to a few sessions. In
   progress 2026-11-16; built 2026-11-16; waits for questions 56 and 57.
   - The one part: the package, kept at the root of this repository, so it reads `HANDBOOK.md`,
     `WORK.md` and `PHASES.md` themselves and no copy of them exists.
   - What changes for the product: every session on an account with the package:
     1. is given `HANDBOOK.md` and `WORK.md` whole when it starts and again after its memory is
        compacted, so neither the preferences download nor the environment's copy is needed;
     2. is given the ten rules again at every message, read from `HANDBOOK.md`;
     3. is held for the operator's yes, on the platform's own permission prompt naming the rule,
        before: deleting outside the working folder, overwriting history on GitHub, dropping or
        emptying a database, deploying or logging in to a server, writing through a connected
        service (mail, chat, calendar, files, tasks), paid generation, starting agents as
        separate programs, editing agents' rule files (`CLAUDE.md`, `AGENTS.md`, settings,
        hooks). A prompt, never a hard block, because the operator's word lifts a rule
        (question 53);
     4. has a reply sent back once when its first line lacks the state, or when it waits for the
        operator without a numbered question;
     5. loads a phase's steps from `PHASES.md` when that phase starts;
     6. has the advisor run by itself (question 33) only when a reply asks the operator new
        questions: the reply is sent back once until the agent has called the advisor
        (`agents/advisor.md`), which answers Go or Ask for each question against "Ask or go",
        says Ask for any step under one of the ten rules and when unsure; the agent follows it
        or keeps the question. Repeated questions and "status" replies are not sent back;
     7. updates when this repository changes.
   - What proves it: a script test for each check (a reply without its state is sent back, a
     held action is held, a harmless one passes), run on every change; then the package added
     to the account and seen working in a fresh cloud session. The benchmark waits for the
     operator's word.
   - Unknowns, each tried first: whether the permission prompt still reaches the operator in
     auto mode (the documentation does not say; if not, back to the operator); a held action in
     a session nobody watches waits until someone answers.
   - Not in it: a repository's `AGENTS.md` read at the start (item 11); removing keys (43).
10. `[handbook]` Keys to live systems out of the sessions that build (question 26, the owner
    2026-11-15): find out which keys can be limited or moved to a setting used only for a
    release, and come back with the steps only the owner can take. One session. After item 9.

11. `[handbook]` A one-page map of each repository's parts (question 29, the owner 2026-11-15):
    the parts, how they connect and what must not change without the owner, on one short page
    read at the start of every session, moved out of the plan document and not copied; settles
    also how a session comes to read a repository's `AGENTS.md`. Changes `PHASES.md`. One
    session. After item 9.

## Later

- `[handbook]` A session budget (time, helper agents, cost) before a session stops and reports
  (audit E2).
- `[handbook]` One line saying that the language of product texts belongs in each repository's
  `AGENTS.md` (audit E3).
