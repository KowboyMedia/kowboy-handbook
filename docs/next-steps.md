# Next steps

## Where things stand (2026-11-16)

- The restructured handbook, the sync and the tests are on `main`. The tests ran green on the pull request and on `main`.
- `main` is not protected yet; the agent could not set it.
- The sync workflow has not yet run in a project on GitHub.

## Where to pick up

1. The operator protects `main` (decision 8a): Settings → Branches → add a rule for `main` with "Require a pull request before merging" (1 approval) and "Require status checks to pass" with `kowboy-handbook-tests`.
2. The operator answers question 9 in `docs/open-questions.md`.
3. Add `kowboy-handbook-sync.yml` to one project as in `README.md`, run it once from the Actions tab, and check its commit.
