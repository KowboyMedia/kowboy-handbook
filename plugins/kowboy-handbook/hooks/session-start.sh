#!/bin/bash
# The plugin's session start: prints the handbook and the playbook index into the session, then the
# project's memory (where to pick up, open questions, known bugs, credentials, distance from
# staging). A repository that carries its own copy of the handbook (KOWBOY-HANDBOOK.md imported by
# its CLAUDE.md) gets only the memory part, so nothing is loaded twice. Never fails the session.
set -uo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
project="${CLAUDE_PROJECT_DIR:-.}"
echo "Kowboy handbook plugin root: $root (its template/ folder holds the starting kit for a repository)"
echo
if [ ! -f "$project/KOWBOY-HANDBOOK.md" ]; then
  cat "$root/KOWBOY-HANDBOOK.md"
  echo
  cat "$root/PLAYBOOK.md"
  echo
fi
if [ ! -x "$project/.claude/hooks/context.sh" ]; then
  exec bash "$root/hooks/context.sh"
fi
exit 0
