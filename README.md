# Kowboy handbook

How AI agents work at Kowboy Media: nine rules, the reply format, and the phases of the work.

| File | What it is | When an agent reads it |
|---|---|---|
| [`kowboy-handbook-rules.md`](kowboy-handbook-rules.md) | The nine rules | Always |
| [`kowboy-handbook-output.md`](kowboy-handbook-output.md) | How replies look | Always |
| [`kowboy-handbook-phases.md`](kowboy-handbook-phases.md) | "Run a session" and the index of phases | Always |
| [`kowboy-handbook-phases/`](kowboy-handbook-phases) | One file per phase | Only when that phase starts |

The three always-read files are copied into a block at the top of each project's `AGENTS.md`. The phase files are copied into the project's `kowboy-handbook-phases/` folder.

## Add the handbook to a project

1. Copy [`kowboy-handbook-sync.yml`](kowboy-handbook-sync.yml) to `.github/workflows/kowboy-handbook-sync.yml` in the project.
2. In the project's Actions tab, run "kowboy-handbook-sync" once.

From then on, the project picks up every change to `main` here once a day, at 04:17 UTC.

- The workflow commits straight to the project's default branch. If that branch requires pull requests or passing checks, the push fails and the run shows it in red.
- The workflow file itself is not synced: GitHub does not let a workflow change workflow files. When `kowboy-handbook-sync.yml` changes here, copy it into each project again.

## Change the handbook

Change the files on a branch, run `bash kowboy-handbook-sync.sh . .`, and open a pull request. The tests run on it; a merge into `main` needs them green and one review. Every project then picks the change up within a day, without further review.

## What the sync changes in a project

- `AGENTS.md`: only the text between `<!-- kowboy-handbook:start -->` and `<!-- kowboy-handbook:end -->`. The first time, that block is added on top. Everything else in the file is kept.
- `CLAUDE.md`: adds the line `@AGENTS.md` on top if it is missing. Everything else is kept.
- `kowboy-handbook-phases/`: replaced as a whole. Do not keep your own files in it.
- Nothing else.
