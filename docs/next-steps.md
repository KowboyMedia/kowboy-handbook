# Next steps

## Where things stand (2026-11-16)

- The handbook is split into three always-read files and seven phase files, on branch `claude/handbook-restructure`; the old content is deleted there and kept in the git history.
- The sync script and the project workflow are built; all nine acceptance tests pass, and the workflow's steps were run once locally against a throwaway project. They have not yet run on GitHub.

## Where to pick up

1. The operator answers questions 5 to 7 in `docs/open-questions.md`.
2. After the merge into `main`: add `kowboy-handbook-sync.yml` to one project as in `README.md`, run it once from the Actions tab, and check its commit.
