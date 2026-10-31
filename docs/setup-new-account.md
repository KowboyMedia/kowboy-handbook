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

## 2. Your Mac (terminal and Cowork)

Open Terminal, paste this whole block, press Enter:

```bash
mkdir -p ~/.claude && curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/HANDBOOK.md -o ~/.claude/CLAUDE.md && python3 - <<'PY'
import json, os
p = os.path.expanduser("~/.claude/settings.json")
d = json.load(open(p)) if os.path.exists(p) else {}
hook = {"hooks": [{"type": "command", "command": "curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/HANDBOOK.md -o ~/.claude/CLAUDE.md"}]}
d.setdefault("hooks", {}).setdefault("SessionStart", [])
if not any("kowboy-handbook" in json.dumps(h) for h in d["hooks"]["SessionStart"]):
    d["hooks"]["SessionStart"].append(hook)
json.dump(d, open(p, "w"), indent=2)
print("done")
PY
```

It downloads the handbook as your personal instruction file and adds a refresh at the start of
every terminal session. If the Mac asks to install "command line developer tools", accept and run
the block again. It replaces `~/.claude/CLAUDE.md` if you had one; personal notes of your own go
into `~/.claude/rules/` instead.

Done. Tell Patric "installed".
