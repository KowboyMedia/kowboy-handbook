# Kowboy handbook - the phases

Version 2026-10-31. The second part of the Kowboy handbook: what each phase reads, produces and
must make true, and the build procedure (Checks, the deletion inventory, the checks for product
texts). `HANDBOOK.md`, next to this file, says when each phase starts, and its rules hold all the
time. Read the phase's section in full when it starts. Every phase ends with the memory current.

**Make sure your copy is whole.** This file ends with the line "End of the phases." If your copy
does not, or a tool shortened it anywhere, it was cut off: save it to a file with
`curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/PHASES.md -o /tmp/PHASES.md`
and read that file whole with the Read tool, in parts if needed.

## Start a repository

From the first session on, every later session finds the same things in the same places, and the
first thing the owner decides is the plan, not a detail.

1. **The files.** `AGENTS.md` with only what is true here: the components and their tags, the
   commands an agent cannot guess, the hard blocks, the repository's own stop-and-ask items and
   definition of done, and "Design: none" or `DESIGN.md`. The four memory files under `docs/`.
2. **The inputs.** What the owner has (a concept, a spec, reference sites, existing data, old
   documents) goes under `docs/inputs/`, unchanged.
3. **Discover** (below): the feature map, the decision list with a recommendation each, the risks,
   and the guided rounds. The strategy is written from the answers, never before them.
4. **The strategy**, `docs/strategy.md`, in this order: the features; the purpose in three
   sentences; the components and the named interfaces between them; the data at rest (its shapes,
   which component owns each); the technology, each choice the market-leading option with one
   clause why; hosting and how a change reaches staging and live; the phases, each with a gate;
   the acceptance criteria, numbered `AC n`, each testable without a person; what is out of scope.
   The strategy names which document wins when the inputs disagree.
5. **Gate 1 is the owner approving the strategy**, presented as at most five Decides with one
   clause of consequence each; the approval is a line in `docs/decisions.md`.
6. **The skeleton.** One folder per component; CI with the enforced checks (build, typecheck,
   tests with no skips, no secrets, plus the repository's own); staging deployed from the
   converged branch; `acceptance/criteria.json` mapping every `AC n` to a named test and a script
   that writes `acceptance/report.md` from a real run. The order of work goes into
   `docs/next-steps.md` with "Where to pick up" on top.
7. **Cold pickup.** Every project must be safe to patch and deploy by someone who has only
   Claude Code and access to its repository. Anything the work depends on (deploy steps, server
   and app names, safety limits, "never do this" rules, scripts, the names of required secrets)
   lives in the repository, never only in a personal project, agent memory, chat history or a
   shared folder. Secret values stay in the platform's secret store and are never written down.
   When a working note becomes something the next person needs, move it into the repository in
   the same session. General rules belong in the handbook, not copied into repositories; a
   repository may assume the handbook is available but must not need it to be patched and
   deployed safely.

Done when a new session told only "resume next steps" starts on the right item, a red check
blocks, and the acceptance report lists every criterion with its test or "no test yet".

## Discover

The owner describes what they want in their words; the agent turns it into the decisions that
must be made, brings them one round at a time with a recommendation, and writes the plan from the
answers.

1. **Read everything given**: the concept, the spec, the reference sites or systems, the data, and
   for a feature the strategy and the decisions that bind it. Ask nothing yet.
2. **Write the feature map** into `docs/strategy.md` ("Features"): each feature in one sentence of
   user value, marked now (the smallest useful version) or later, with the acceptance criteria it
   will need. What is explicitly out stands in its own list.
3. **Write the decision list**: every product and architecture decision the map needs. For each:
   the question in plain words; at most three options, one clause of consequence each; whether it
   can be undone later; the recommended answer and why in one clause.
4. **Name the risks and unknowns**, and the cheapest way to find out (a time-boxed spike, a
   question to a third party, a look at real data). Unknowns go first in the order of work.
5. **Guide the rounds**: at most five decisions per round, the most binding first (boundaries and
   data before technology, technology before details), each a Decide with its register number;
   "ok" takes every recommendation. Record each answer in `docs/decisions.md` as it comes and
   revise the list between rounds.
6. **Write the plan from the answers**: the strategy sections the answers settle, the acceptance
   criteria numbered, the order of work in `docs/next-steps.md`, sized in sessions (one, a few,
   many). The first item is the riskiest unknown or the thinnest slice that proves the design.

Done when every decision the first phase needs has a line in `docs/decisions.md` and the first
item of `docs/next-steps.md` can be built without a question.

## Plan an item

Thinking happens in the plan; building executes a plan the owner could have read, and a fresh
session must be able to build from it alone.

1. **Read first**: the item, the strategy sections it touches, every `docs/decisions.md` line for
   its component, the acceptance criteria it serves, open questions on it. A feature larger than
   one item goes through discover first.
2. **Look two items ahead** and bring the decisions this item and the next two need, now.
3. **Anything visible is agreed before it is built**: a reference page, a sketch or a staging page
   the owner can look at, and one Decide: "build it like this? yes or no". A new page, section
   type, component, layout or look goes through design; a change inside an existing pattern does
   not.
4. **Write the plan into the item** in `docs/next-steps.md`: the component (one; two means two
   items in dependency order); what changes for the product, one sentence in the owner's words;
   the test that proves it, named; the interface touched (none, additive, or breaking, and then
   expand, migrate, contract as separate releases); the unknowns, each with a time-boxed spike
   first; the Decides it needs and the Defaults it takes; what it does not do, and where a request
   outside it went; its size in sessions.
5. **Order the work** unknowns first, then the smallest vertical slice verifiable end to end, then
   widen. **Size to one session**: split what will not finish, take the first unblocked part.
6. **Mark it** "in progress" with the date, so no other session takes it.

Done when the plan names the test that will prove the item, a fresh session could build from it,
and every Decide in it is in the register.

## Design

Taste lives in assets built once and in a review loop, never in the owner's time. A visible change
either follows the repository's design exactly or goes through the loop, and the owner only ever
picks between finished candidates by looking.

- **The size of the change, first.** None: existing components and patterns as they are (text, a
  field in a known form, a bug fix): build, one screenshot desktop and one mobile, compare with a
  neighbouring page, done. Light: inside an existing pattern but adding something: build against
  `DESIGN.md`, screenshots, the self-check once, done. Full: a new page, section type, component,
  layout or look: the loop. A repository whose `AGENTS.md` says "Design: none" (an API, a job, an
  internal tool) never enters this phase.
- **The assets, once per repository.** `DESIGN.md` at the root, a protected path: the palette (4
  to 6 named colours), the type (1 or 2 typefaces and a scale), spacing and radius, component
  rules, layout patterns, 3 to 5 tone words, an anti-defaults list, and 2 or 3 reference
  screenshots or links. It is derived by an agent from references the owner names ("which 2 or 3
  sites or screenshots should this look like?"), never written by the owner. Real content from
  the start; placeholders make every layout look cheap. The usual AI tells are on the
  anti-defaults list: identical rounded cards with the same soft shadow, all-caps eyebrow labels
  over every heading, one accented word per headline, fade-up animations on every section, arrows
  on buttons, the same two or three palettes everywhere.
- **The loop, for a full change.** Plan the tokens and components from `DESIGN.md` and check the
  plan for genericness. Build one section at a time with real content. Review with fresh eyes: a
  second agent screenshots desktop and mobile, scores hierarchy, contrast, spacing rhythm, the
  anti-defaults, real content, every state (empty, loading, error, long text), keyboard and
  screen-reader basics, and returns ordered fixes; at most three passes. For a new look, run the
  loop two or three times in different directions and show the owner the finished candidates side
  by side on staging with one question: "a, b or c?".
- **Self-check** (light and full): against `DESIGN.md`, no raw colour or size outside the tokens,
  nothing from the anti-defaults list, both screenshots taken and compared with a neighbouring page.

Done when the screenshots exist and match the reference, the reviewer's last pass has no findings
above "taste", and for a new look the owner has picked a candidate.

## Decide architecture

Few, boring, explicit decisions that outlive the session that made them, each undoable where it
can be.

- **The aim, repeated back first.** Before designing a core feature, the agent repeats back in a
  few lines what the owner means, in the owner's terms and at the scale the owner stated, and
  designs only after the owner's yes.
- **Designed for the stated goal, never for today's data.** A design starts from the scale and
  openness its goal states, not from the size of today's data or what today's code makes easy. An
  assumption on volume, scope or limits is written at the top of the design, and one that changes
  the architecture is a Decide. Today's size may decide what is built first, never what the design
  can do.
- **Checked against the owner's words before the owner sees it.** A fresh agent given only the
  owner's words and the design checks that it delivers what was asked, at the scale asked, and
  names the assumption that would break it; what it finds is fixed before the design is shown.
- **Boundaries first.** Name the components and the interface between each pair; a component knows
  nothing beyond its interfaces; each interface is a protected path.
- **Market-leading and boring**, the way the documentation says; a deviation is written down with
  its reason. **Least moving parts**: no queue, cache, service, worker or layer without a need that
  exists now and is named.
- **Data.** One shape and one owner per datum; raw input is kept so everything derived can be
  recomputed; changes are additive; a breaking change is expand, migrate, contract in separate
  releases.
- **Reversible first.** Between two workable options, the one that can be undone wins; a choice
  that cannot be undone is a Decide however small. At most three options, one clause of
  consequence each, the smaller recommended.
- **The baseline every design meets**: every endpoint authenticated and every token given the
  least it needs; personal data kept only where needed and never in logs; backups exist and a
  restore has been rehearsed before the first go-live; performance is measured against a criterion
  before anything is optimised.

Recorded as a `docs/decisions.md` line: date · the decision · the options rejected and why · the
condition to revisit · the reference. A decision on boundaries, data or the stack also gets its
section in `docs/strategy.md`, and every `docs/next-steps.md` item that depended on it is updated.

## Build

The smallest change that makes the named test pass, in the shape a reader of this codebase
expects, leaving the repository cleaner than it was found.

- **Order**: interface (types, schema), the failing test or golden master, the implementation, the
  docs, all in the same change.
- **One component.** Touching another is a new item, or the plan was wrong: go back to the plan.
- **Search before writing**; one code path per concern; the framework's way, no wrappers, no
  home-made layers, no flags for cases that do not exist.
- **Configuration** comes from the environment, is validated at startup with a message that says
  what is wrong; secrets are never in code, logs or chat. **Errors fail loudly** with their cause.
  **Anything that runs unattended writes events** with an id that connects them.
- **Tests** are deterministic, independent, fast, and run against the real local services the
  session has rather than mocks; a transformation has golden masters; expected output is never
  edited to pass; nothing is skipped.
- **Save often**, with a message that says what changed for the product. **Two failed fixes end
  the attempt.**
- **Checks.** The repository's `AGENTS.md` lists the checks that block merge or deploy; they are
  the only ones, and adding one needs approval. Everything else is a warning: reported, never
  blocking. Leave every file you touch free of warnings, formatted the way the repository formats.
- **A deletion is a complete clean-up.** Before a function or a feature is deleted, take an
  inventory of everything that belongs to it: the code, the tests, the settings, the events it
  wrote, and the data it stored (tables, columns, files). Everything in it that nothing else uses
  is deleted in the same change; what stays is named with the thing that still uses it.
- **Every text in the product is written for the person who reads it.** A text is anything the
  product shows a person: a page, a label, a button, a status, a health check, an alert, a mail,
  an error. Text that code puts together (from a template, a check or an event) is held to the
  same rule and read whole, with real data, before it ships. Every text passes these checks:
  - **What happened, what it means, what to do.** It says what happened, what that means for the
    reader's business (its customers, its websites, its visitors) and what to do next, in that
    order. When there is nothing to do, it says so.
  - **Things by the names the reader knows.** It names a customer by its name, a website by its
    address and an office or a person by name, and calls each thing by the same word everywhere.
    Never a code name, a key, an internal id, a table, a function, an event type or a check's
    name. When the reader needs an id, it follows the name and says whose id it is ("the Harbour
    office, the CRM's id 3011").
  - **A link to every thing named.** Each thing that has a page in the product links to that
    page, and a problem links to the page where it is fixed.
  - **Whole sentences in the reader's words.** A number agrees with its sentence ("one site has",
    "three sites have"), never "site(s)". No arrows, slashes, dashes or brackets standing in for
    words, and no term the reader would have to ask about.
  - **The cold reader test.** A person who knows the business but not the code reads the text
    once, understands what happened and knows what to do next without asking anyone.

Done when the named test passes, the enforced checks are green, touched files have no warnings,
the README and every text a user reads tell the truth, the item says what remains, and each
structural choice has its `docs/decisions.md` line.

## Review

Only correct, minimal work reaches the owner. The reviewer reports what changes correctness or a
requirement, never taste. Check, in this order, reporting only failures, each with its fix:

1. **Authorised**: which item or decision asked for this change? None means the finding is
   "unasked for, revert", whatever its quality.
2. **Does it do what the item and its acceptance criterion say, and nothing more?** Where visible,
   compare with the reference side by side.
3. **Boundaries**: a component knowing something beyond its interface; a protected path changed
   without a Decide.
4. **Duplication**: logic that already existed; a second code path for one concern.
5. **Tests**: would they fail if the feature broke; behaviour, not implementation; anything
   skipped, flaky, timed or edited to pass.
6. **Data and contract**: a breaking change outside expand, migrate, contract; a field or rule
   with no written source.
7. **Security**: secrets, injection, an endpoint without authentication, personal data in logs.
8. **Failure modes**: bad input, timeout, partial failure: what happens, and is it visible.
9. **Truth**: README, user-facing text, `docs/next-steps.md` and `docs/decisions.md` updated.
10. **Plain words**: every new or changed text a user reads, read whole with real data, passes
    the checks of "Every text in the product is written for the person who reads it" (Build).
11. **Proportion**: a fix for a rare and harmless problem, or new infrastructure to prevent one,
    is "disproportionate, accept as debt in `docs/known-bugs.md`", whatever its quality.

Output: at most ten lines, each `[component] what is wrong · why it matters · the fix`. "No
findings" is a complete answer.

## Release and operate

Live changes only on the owner's word, and every release can be taken back in one step.

1. Every check is green on staging and the acceptance report is current.
2. The impact preview: what data and behaviour change for users, in product words.
3. The release note is the Done block: one line per change, how each was verified.
4. The owner says "release". Nothing goes live before.
5. Promote staging to live; watch the health check until green; keep the previous version ready
   and say in one line how it comes back ("say 'undo the release'").
6. A `docs/decisions.md` line "Release <date>", and "Where to pick up" updated.

**First go-live** adds: the domain and certificates answer; backups run and a restore was
rehearsed on staging; health checks and alerts are in place and were seen firing once; the undo is
known; who is told, and in which words, is written before the switch; personal data and
credentials were checked to be only where the design says.

**Operate.** Health checks explain themselves in plain words and counts; an alert goes where a
person sees it; events carry ids that connect them; logs hold ids, never personal data.
**Maintain.** Dependencies are updated in one item a month with every test green; dead code and
rules nobody would break without them are removed as they are found. **Incident.** Any action on
production is a Decide. First make it safe (take back the last release if it is the cause), then
find the cause, then fix it forward through staging. The cause gets a `docs/known-bugs.md` entry
until fixed, and a rule or decision if it can happen again. A symptom is never fixed silently.

## Status

Read-only. Four blocks, nothing else: **Questions**, every open entry of `docs/open-questions.md`,
one line each, Decide or Default marked, with its tag; **Done**, what is in staging and not yet
live, in product words, one line each; **Notes**, every entry of `docs/known-bugs.md`, one line
each; **Next**, the session's state first, then "Where to pick up" from `docs/next-steps.md`, in
two lines.

End of the phases.
