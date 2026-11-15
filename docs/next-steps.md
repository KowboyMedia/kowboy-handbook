# Next steps

The order of work on the handbook. "Resume next steps" means: read this, do the first item that is
not done, keep it current.

## Where to pick up

Item 8 (the three layers) is in progress in a thread of 2026-11-15: sorted and checked in that
thread's working copy, layer 1 rewritten as ten rules from their principles; waiting for the owner's yes
(question 31) before it is live. Still to do in item 8: the small preferences of layer 3 cut
down to their principles.
Item 9 (the Kowboy package) is next and takes a new thread on this repository with "resume next
steps", once item 8 is live. Items 1, 2 and 7 are done; 5 is dropped; 3 and 6 are taken over by
item 9; item 4 follows item 9. The audit behind items 1 to 7 is `docs/audit-2026-10-30.md`.

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
   environment's setup script are replaced once, which closes 22. One to a few sessions. Ready
   when item 8 is live.
10. `[handbook]` Keys to live systems out of the sessions that build (question 26, the owner
    2026-11-15): find out which keys can be limited or moved to a setting used only for a
    release, and come back with the steps only the owner can take. One session. After item 9.

## Later

- `[handbook]` A session budget (time, helper agents, cost) before a session stops and reports
  (audit E2).
- `[handbook]` One line saying that the language of product texts belongs in each repository's
  `AGENTS.md` (audit E3).
