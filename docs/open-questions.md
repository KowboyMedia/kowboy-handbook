# Open questions

Every question asked of the owner about the handbook, numbered for good. An answered question is
recorded in the handbook's history with the change it led to, and leaves this file.

Next number: 27

## 22 `[handbook]` Instruction: change your preferences and your environment's setup script so every session works from one copy of the handbook, the newest, and treats it as binding; then say "done".

Asked 2026-11-01. Replaces 17, 20 and 21. The steps and both texts are in
`docs/setup-new-account.md`, parts 0 and 1. The colleague gets the same steps on Slack when the
owner says so.

## 23 `[handbook]` Should the handbook say that your answer to a question goes back only to the thread that asked it, and is never passed to another thread unless that thread owns the subject?

Asked 2026-11-01. A coordinator in a project committed to this rule; the handbook has the thread
rule and the plain-words rule but not this one. Reply: yes or no.

## 24 `[handbook]` How should the handbook be reorganised so that agents obey it?

Asked 2026-11-15. Blocks all work on the handbook's text. The owner, 2026-11-15: agents act on
their own decisions and drift apps, code bases and the handbook itself; the hard rules must be
short, "like commandments", and kept apart from the preferences for how agents talk to the owner.
Measured on version 2026-11-08a: 30,116 characters and 77 bold rules of equal weight; the rules
that stop damage are two sentences of 573 and 1,002 characters inside "Ask or go"; 31% of the
text is about how replies look and 14% about when to stop; each stop depends on the agent first
judging its own step, next to rules that tell it to go; 13 lines of `docs/decisions.md` are an
agent's own choice about the handbook, 8 of them not confirmed by the owner; the text grew from
25,606 to 30,116 characters in nine days.

- a) **three layers** (recommended): a one-screen list of absolute rules that beat everything
  else, then how agents talk to the owner, then how the work is done; every rule kept and placed
  in one layer.
- b) **tidy in place**: the same single document, the absolute rules moved to the top, the
  wording shortened.
- c) **rewrite from the owner's decisions**: a new, shortest text written only from the
  decisions the owner made; the rules agents added on their own go.

Scored (obedience gained · risk of losing a rule · the owner's time): a) high · low, checked
rule by rule by a second agent · one screen to read; b) low · lowest · none; c) highest · high ·
the whole text to re-read. The smaller option: b). Reply: a, b or c.

## 25 `[handbook]` How should the rules reach every session and be enforced?

Asked 2026-11-15. Blocks the delivery work; follows 24. Today every rule is text, and three
things were found: the handbook arrives twice in a session (the instruction file and the
download the preferences demand); the preferences still carry their own competing rules and an
older text than the README's (22 is open); and only an environment whose setup script was edited
by hand carries the handbook.
Checked 2026-11-15. Proven in a session: a package (plugin) enabled on the account reaches a
cloud session, and its automatic checks ran before an action there. From the platform's
documentation: a personal settings file is not read in cloud sessions; a repository's settings
do not load in project threads; an instruction file is "context, not enforced configuration";
central admin settings need a Team or Enterprise plan. Not known: whether an individual plan can
add our own package to the account; that is the first step of a), before anything is built.

- a) **one Kowboy package** (recommended): each person installs it once on the account; it puts
  the absolute rules in front of the agent at every message, stops the dangerous actions by
  itself, sends back a reply that lacks its state or its questions, and updates from this
  repository for everyone.
- b) **today's way, in three texts**: the same download, now of the three layers; nothing to
  install, still only text.
- c) **a Team plan**: the platform's own central rule control for every account; a monthly cost
  and both accounts moved.

Scored (enforced, not only remembered · central for several people, nothing per project · the
owner's time and cost): a) yes · yes · one install per person, if the plan allows it; b) no ·
yes · none; c) yes · yes · a recurring cost and a move. The smaller option: b). Reply: a, b or c.

## 26 `[handbook]` Should I plan, as its own item after 24 and 25, that sessions which build no longer hold the keys to live sites and servers?

Asked 2026-11-15. A risk seen during the review: "a live site is read-only for an agent" is a
sentence, while a session that only builds, or only edits this handbook, can hold keys that
change or delete live systems. A key a session does not hold cannot be misused. The item would
find out which keys can be limited or moved to a separate setting used only for a release, and
come back with the steps only the owner can take. Reply: yes or no.
