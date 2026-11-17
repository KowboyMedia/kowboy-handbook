# Kowboy handbook: phase "Release and operate"

Version 2026-11-16q.

## Release and operate

When: the operator says "release", a health check is red, or something is wrong in production.

1. Every check is green on staging.
2. Say what changes for the people who use it, in their words.
3. The operator says "release". Nothing goes live before.
4. The approved publish runs by itself, as "Keys and access" in `WORK.md` says. Watch the health check until it is green, keep the previous version ready and say in one line how it comes back.
5. Write the release into `docs/decisions.md`.

The first go-live adds: the address and its certificates answer; backups run and a restore was rehearsed; the alerts were seen firing once; the undo is known; personal data and keys are only where the design says; who is told, and in which words, is written beforehand.

When something is wrong in production: every action there is the operator's decision. First make it safe, then find the cause, then fix it through staging. The cause goes into `docs/known-bugs.md`. Libraries are updated once a month, as one item, with every test green.

End of the phase.
