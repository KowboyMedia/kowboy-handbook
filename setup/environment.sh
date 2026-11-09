#!/bin/sh
# Kowboy: run by a cloud environment's setup script when a container is built,
# with these two lines (they never stop a session from starting):
#   # Kowboy handbook: the newest handbook, the reminder and the session steps, from the handbook repository
#   curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/setup/environment.sh -o /tmp/kowboy.sh && sh /tmp/kowboy.sh || { mkdir -p ~/.claude; curl -fsSL https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main/HANDBOOK.md -o ~/.claude/CLAUDE.md; } || true
# It places the handbook as the personal CLAUDE.md, the reminder card and the
# two session steps, and registers the steps in ~/.claude/settings.json,
# keeping everything else there.
base="${KOWBOY_BASE:-https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main}"
dir="${KOWBOY_CLAUDE_DIR:-$HOME/.claude}"
k="$dir/kowboy"
mkdir -p "$k" || exit 0

get() { curl -fsS --max-time 20 "$base/$1" -o "$2.tmp" && mv "$2.tmp" "$2"; }

get HANDBOOK.md "$k/HANDBOOK.md" && grep -qx 'End of the handbook.' "$k/HANDBOOK.md" \
  && cp "$k/HANDBOOK.md" "$dir/CLAUDE.md"
get setup/session-start.sh "$k/session-start.sh" && chmod +x "$k/session-start.sh"
get setup/reminder.sh "$k/reminder.sh" && chmod +x "$k/reminder.sh"
get setup/reminder.md "$k/reminder.md"

start=; [ -x "$k/session-start.sh" ] && start="$k/session-start.sh"
remind=; [ -x "$k/reminder.sh" ] && remind="$k/reminder.sh"
[ -n "$start$remind" ] || { echo "Kowboy: session steps not downloaded; the handbook copy alone is in place."; exit 0; }

if command -v python3 >/dev/null 2>&1; then
  python3 - "$dir/settings.json" "$k" "$start" "$remind" <<'PY' || echo "Kowboy: settings.json left as it was; session steps not registered."
import json, os, sys
path, k, start, remind = sys.argv[1:5]
if os.path.exists(path):
    try:
        s = json.load(open(path))
    except Exception:
        sys.exit("settings.json does not parse")
else:
    s = {}
if not isinstance(s, dict) or not isinstance(s.get("hooks", {}), dict):
    sys.exit("settings.json has an unexpected shape")
hooks = s.setdefault("hooks", {})
def put(event, cmd):
    lst = [h for h in hooks.get(event, []) if "/kowboy/" not in json.dumps(h)]
    if cmd:
        lst.append({"matcher": "", "hooks": [{"type": "command", "command": cmd}]})
    hooks[event] = lst
put("SessionStart", start)
put("UserPromptSubmit", remind)
perms = s.setdefault("permissions", {})
allow = perms.setdefault("allow", []) if isinstance(perms, dict) else None
rule = "Read(/" + k.rstrip("/") + "/**)"
if isinstance(allow, list) and rule not in allow:
    allow.append(rule)
tmp = path + ".kowboy.tmp"
json.dump(s, open(tmp, "w"), indent=2)
os.replace(tmp, path)
PY
elif [ ! -e "$dir/settings.json" ]; then
  {
    printf '{\n  "hooks": {\n'
    [ -n "$start" ] && printf '    "SessionStart": [{"matcher": "", "hooks": [{"type": "command", "command": "%s"}]}]%s\n' "$start" "${remind:+,}"
    [ -n "$remind" ] && printf '    "UserPromptSubmit": [{"matcher": "", "hooks": [{"type": "command", "command": "%s"}]}]\n' "$remind"
    printf '  },\n  "permissions": {"allow": ["Read(/%s/**)"]}\n}\n' "$k"
  } > "$dir/settings.json"
else
  echo "Kowboy: no python3 and settings.json exists; session steps not registered."
fi
exit 0
