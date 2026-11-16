# Open questions

Every question asked of the owner about the handbook, numbered for good. An answered question is
recorded in the handbook's history with the change it led to, and leaves this file.

Next number: 56

## 22 `[handbook]` Instruction: change your preferences and your environment's setup script so every session works from one copy of the handbook, the newest, and treats it as binding; then say "done".

Asked 2026-11-01. Replaces 17, 20 and 21. The steps and both texts are in
`docs/setup-new-account.md`, parts 0 and 1. The colleague gets the same steps on Slack when the
owner says so.

## 23 `[handbook]` Should the handbook say that your answer to a question goes back only to the thread that asked it, and is never passed to another thread unless that thread owns the subject?

Asked 2026-11-01. A coordinator in a project committed to this rule; the handbook has the thread
rule and the plain-words rule but not this one. Reply: yes or no.

## 40 `[handbook]` Instruction: protect the handbook's live copy on GitHub so that a change reaches it only after the owner's click; then say "protected".

Asked 2026-11-15, on the owner's yes to 39. Only the owner can change the repository's settings.
The steps are in the thread of 2026-11-15. Not known: whether the owner can approve a change an
agent prepared under his own account; the first change after the protection shows it.

## 43 `[handbook]` Which of the keys in the building environment reach live systems and are to be removed from it?

Asked 2026-11-15, on the owner's yes to 42. The list of key names with the agent's guess for each
is in the thread of that day and not here, because this repository is public. The owner corrects
the list, then approves the removal on a card. Reply: ok, or the names to keep.

## 55 `[handbook]` Instruction: look whether your plan lets you add our own package; then reply with what you see.

Asked 2026-11-16. The first step of item 9: nothing is built before the answer (question 25).
From the platform's documentation, read 2026-11-16: a package is added under Customize, Plugins,
Add, either as "Add marketplace" (it then updates from this repository by itself) or as "Upload
plugin" (each update uploaded again by each person); which plans may add their own is not
stated. Steps: open claude.ai, then Customize, then Plugins; click Add and look at the menu.
- a) **both**: "Add marketplace" and "Upload plugin" are there; the package is built and updates
  by itself.
- b) **upload only**: the package is built; every change means each person uploads it again.
- c) **none**: back to the operator before anything is built.
- Reply: a, b or c.
