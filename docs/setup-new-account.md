# Setting up the handbook on a new account

Two parts: cloud sessions on claude.ai, and your Mac. Keep your current "Instructions for Claude"
in claude.ai exactly as they are, including the Claude Code line that downloads and reads the
handbook: that line still brings the newest text at every session start. The steps below only
make the handbook survive long sessions, by placing it as your personal instruction file.

## 1. Cloud Claude Code (claude.ai)

1. Open claude.ai, then Claude Code, then Environments. Open the environment you use, or create
   one.
2. In its setup script, paste these two lines and save:

```
mkdir -p ~/.claude
curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/HANDBOOK.md -o ~/.claude/CLAUDE.md
```

3. In every project you start threads from: Project settings, Environment, choose that
   environment.

Done. From the next session on, the handbook is also loaded as your personal instruction file.

## 2. Your Mac (terminal)

1. Open Terminal, paste this line, press Enter. It saves the handbook as its own file:

```bash
mkdir -p ~/.claude && curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/HANDBOOK.md -o ~/.claude/kowboy-handbook.md
```

2. Open the file `~/.claude/CLAUDE.md` (create it if it does not exist) and add this line at the
   end; everything already in the file stays:

```
@~/.claude/kowboy-handbook.md
```

That is all. The saved file is the copy that survives long sessions; the Claude Code line in your
instructions still brings the newest text at every session start. When Patric says the handbook
changed, run the line in step 1 again.

One limit: Cowork on the Mac skips included files, so there the handbook comes only from the
Claude Code line in your instructions, as before.

Done. Tell Patric "installed".
