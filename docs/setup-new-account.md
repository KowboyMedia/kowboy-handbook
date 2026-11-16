# Setting up the handbook on an account

Once per person. The Kowboy package then gives every Claude Code session the newest handbook,
on claude.ai and in the terminal, and keeps it current by itself.

## 1. Add the package (claude.ai)

1. Open claude.ai, then Customize, then Plugins.
2. Click Add, then Add marketplace, enter `KowboyMedia/kowboy-handbook` and confirm.
3. Turn on "Sync automatically" for that marketplace.
4. Install the plugin "kowboy" from it and make sure it is enabled.

## 2. Replace the Claude Code part of your preferences (claude.ai)

1. Open claude.ai, then Settings, then Profile, then the personal preferences field.
2. Delete every paragraph that starts "Claude Code-only instructions", down to the paragraph that
   starts "For every chat"; keep that one.
3. Paste this in their place and save:

```
Claude Code-only instructions, don't use in normal chat:
The Kowboy handbook is binding in every Claude Code session and comes before any default about
reply length, tone or format. The Kowboy package gives it to every session at the start. If it
is not in your context, download
https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/HANDBOOK.md and WORK.md from
the same address, read both whole, follow them, and say in your first line that the package is
missing. If you cannot get the handbook at all, say so in that line and do no work.
```

## 3. The cloud environment

Its setup script no longer needs to place the handbook. Once the package works in a fresh
session, that session offers to remove those lines on an approval card; any other environment
whose setup script downloads `HANDBOOK.md` gets the same from a session in it.

## 4. Your Mac (terminal)

1. Open the file `~/.claude/CLAUDE.md` and delete the line `@~/.claude/kowboy-handbook.md`, if it
   is there; then delete the file `~/.claude/kowboy-handbook.md`.
2. Start Claude Code and type `/plugin`. If "kowboy" is not listed, type these two lines:

```
/plugin marketplace add KowboyMedia/kowboy-handbook
/plugin install kowboy@kowboy
```

Done. Tell the product lead "installed".
