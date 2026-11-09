#!/bin/sh
# Kowboy: run by a cloud environment's setup script when a container is built,
# with this one line (it never stops a session from starting):
#   curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/setup/environment.sh | sh || true
# It places the handbook as the personal CLAUDE.md, the reminder card and the
# two session steps, and registers the steps in ~/.claude/settings.json.
base="${KOWBOY_BASE:-https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main}"
dir="${KOWBOY_CLAUDE_DIR:-$HOME/.claude}"
k="$dir/kowboy"
mkdir -p "$k" || exit 0

get() { curl -fsS --max-time 20 "$base/$1" -o "$2.tmp" && mv "$2.tmp" "$2"; }

get HANDBOOK.md "$k/HANDBOOK.md" && grep -qx 'End of the handbook.' "$k/HANDBOOK.md" \
  && cp "$k/HANDBOOK.md" "$dir/CLAUDE.md"
get setup/session-start.sh "$k/session-start.sh"
get setup/reminder.sh "$k/reminder.sh"
get setup/reminder.md "$k/reminder.md"
chmod +x "$k/session-start.sh" "$k/reminder.sh" 2>/dev/null

# Register the steps, keeping anything already in settings.json.
python3 - "$dir/settings.json" "$k" <<'PY' || true
import json, os, sys
path, k = sys.argv[1], sys.argv[2]
try:
    s = json.load(open(path))
except Exception:
    s = {}
hooks = s.setdefault("hooks", {})
def put(event, cmd):
    lst = [h for h in hooks.get(event, []) if "kowboy/" not in json.dumps(h)]
    lst.append({"matcher": "", "hooks": [{"type": "command", "command": cmd}]})
    hooks[event] = lst
put("SessionStart", os.path.join(k, "session-start.sh"))
put("UserPromptSubmit", os.path.join(k, "reminder.sh"))
allow = s.setdefault("permissions", {}).setdefault("allow", [])
rule = "Read(/" + k.rstrip("/") + "/**)"
if rule not in allow:
    allow.append(rule)
json.dump(s, open(path, "w"), indent=2)
PY
exit 0
