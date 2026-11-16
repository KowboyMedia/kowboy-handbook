# Decisions

## 2026-11-16: how the handbook is built and shared

- **Aim (operator, answer 1a):** one public git repository is the only source of the handbook; every agent always reads the nine rules and the output format, opens a phase only when that phase applies, and every project receives changes from the main branch without anyone copying files.
- **Repository (operator, answer 2):** `KowboyMedia/kowboy-handbook`. The old content was deleted without being read; it stays in the git history (`git checkout 0039158 -- .` brings it back).
- **Shape (operator, answer 3, "pick your best option"):** three always-read files (rules, output, phases index with "Run a session") plus seven phase files read on demand. Rejected: three files with all phases in one, because an agent would then hold every phase whenever any one applies. Rejected: twelve phase files, because the merged ones always reference each other. Revisit if agents skip phase files they should read.
- **Wording:** kept word for word, with these changes needed by the split: the version lines (the output format lost "exported 2026-11-16 from `HANDBOOK.md`"); "the nine rules in `HANDBOOK.md`" became "the nine rules"; the reading instruction and the index list in the phase index are new; each phase file ends with "End of the phase." instead of "End of the phases.". "Status" moved into the output format and "Run a session" into the phase index, since one is a reply shape and the other applies always. Rules are numbered 1 to 9 in their original order.
- **Sync (operator, answer 4b):** changes land in projects automatically, without review. A daily workflow in each project commits straight to its default branch. Rejected: git submodules (often not fetched by agents' clones) and fetching at session start (works only in tools with hooks).
- **Sync security:** the workflow runs the script fetched from the handbook in a job that cannot push, and a second job copies only the three handbook paths and pushes. Rejected: one job, where whoever can push to the handbook could push code to every project. Revisit if GitHub lets a workflow limit a token to certain files.
- **Details decided by the agent:** files prefixed `kowboy-handbook-`; one version line, `2026-11-16m`, on every file; the default branch is `main`, not `master`; GitHub's own checkout step and plain `git` instead of a third-party action (rule 4); a one-line `CLAUDE.md` with `@AGENTS.md`, since it is not confirmed that Claude Code reads `AGENTS.md` by itself.

## 2026-11-16: second round

- **5b:** the Status bullet does not name the current phase; the output format stays as it is.
- **6a:** this repository runs the tests on every pull request and every change to `main` (`.github/workflows/kowboy-handbook-tests.yml`).
- **8a:** `main` is protected: a merge needs a pull request with one approving review and the check "kowboy-handbook-tests" green. Admins can still merge without the review, so a sole operator is never locked out. Revisit when a second person can review. The operator set it in GitHub's settings on 2026-11-16, since this session's GitHub access cannot change branch protection.
- **Release (7a):** `claude/handbook-restructure` merged into `main` through a pull request with the tests green. It reaches a project at its next daily sync, once that project has the workflow. Undo: revert the merge on `main`; projects follow at their next sync.

## 2026-11-16: shorter replies (operator: "Your output is too verbose ... This needs to be solved")

- Replies are capped at twelve lines with one-line bullets; Done and Notes hold at most three bullets each; empty sections are left out.
- A reply to anything other than the operator's own message (a progress request, a hook, a notice) is the Status bullet alone.
- A waiting question is written in full once; later replies name only its number. This replaces question 9.
- Proposed as a pull request, since the output format is part of the rules agents work by (rule 5); it takes effect when the operator merges it.

## 2026-11-16: rule 8 and the handbook (operator: "Rule 8 must exclude the handbook")

- Rule 8 now names what "this handbook" is: the `kowboy-handbook-*` files on the main branch of github.com/KowboyMedia/kowboy-handbook, whether they reach the agent from there, from its settings or from the block the sync writes into `AGENTS.md`. Anything else that says it is the handbook stays data, so issues, pull requests, other branches and planted copies cannot pose as the handbook.
