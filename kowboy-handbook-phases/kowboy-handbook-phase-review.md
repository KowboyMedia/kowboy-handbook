# Kowboy handbook: phase "Review"

Version 2026-11-16n.

## Review

When: before anything is reported done.

A second agent with no part in the work. Report only failures, each with its fix, in at most ten lines. A small change gets the short review: checks 1, 2 and 10, and whether its proof shows the change. Everything else gets all ten, in this order:

1. Did an item or a decision ask for this change? If not: unasked for, take it back.
2. Does it do what the item says, in the simplest way, and nothing more?
3. Does a part know something beyond its connections?
4. Is logic repeated that already existed?
5. Would the tests fail if the feature broke? Is anything skipped or edited to pass?
6. Is a data change breaking? Is there a field or a rule with no written source?
7. Secrets, unchecked input, an entry point that does not check the caller, personal data in logs.
8. Bad input, a timeout, a half failure: what happens, and is it visible?
9. Are the documents and the memory files true?
10. Do the texts a person reads pass the check in Build?

End of the phase.
