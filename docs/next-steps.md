# Next steps

## Where things stand (2026-11-16)

- The handbook is split into three always-read files and seven phase files on branch `claude/handbook-restructure`. The old content is deleted there and kept in the git history at `0039158`.
- The sync script and the project workflow are built. All 16 acceptance tests pass, and both workflow jobs were simulated locally. Three independent reviews ran; every failure they found is fixed. The workflow has not yet run on GitHub.

## Where to pick up

1. The operator answers questions 5 to 8 in `docs/open-questions.md`.
2. After the merge into `main`: add `kowboy-handbook-sync.yml` to one project as in `README.md`, run it once from the Actions tab, and check its commit.
