# Kowboy handbook: phase "Decide architecture"

Version 2026-11-16q.

## Decide architecture

When: before a choice later work builds on.

- Repeat the operator's aim back first; design only after the operator's yes.
- Design for the goal and scale the operator stated, never for today's data. Assumptions are written at the top, and one that changes the design is the operator's decision.
- A fresh agent checks the design against the operator's words before the operator sees it.
- Name the parts and the connections first. A part knows nothing beyond its connections.
- Boring and widely used, with as few moving parts as possible: nothing without a need that exists now.
- One shape and one owning part per piece of data; raw input is kept; changes add, never break.
- Between two workable options, the one that can be undone wins.
- Every design meets this: every entry point checks who is calling and every key has the least access; personal data only where needed and never in logs; backups exist and a restore was rehearsed before the first go-live; measure before making anything faster.
- Record the decision, the options rejected and the condition to revisit.

End of the phase.
