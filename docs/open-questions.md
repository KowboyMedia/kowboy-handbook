# Open questions

- 5: Should the Status bullet name the phase the agent is in, so a skipped phase file shows? This changes the output format (rule 5).
- 6: Should this repository get an automatic check that runs `tests/kowboy-handbook-sync.test.sh` on every pull request? This adds a merge gate (rule 5).
- 7: Merge `claude/handbook-restructure` into `main`? Every project with the sync workflow then picks it up within a day.
- 8: Protect `main` here so a merge needs a review? Whoever can merge into `main` decides what every project's agents obey and what the sync script does.
