#!/bin/sh
# Kowboy: runs on every message the owner sends; adds the short reminder card.
while read -r _; do :; done
cat "${KOWBOY_CLAUDE_DIR:-$HOME/.claude}/kowboy/reminder.md" 2>/dev/null
exit 0
