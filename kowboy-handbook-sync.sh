#!/usr/bin/env bash
# Brings a project's copy of the Kowboy handbook up to date.
#
#   bash kowboy-handbook-sync.sh HANDBOOK_DIR PROJECT_DIR
#
# Writes into PROJECT_DIR:
#   AGENTS.md                 rules, output format and phase index between the kowboy-handbook
#                             markers; text outside the markers is kept
#   kowboy-handbook-phases/   the phase files, replaced as a whole
#   CLAUDE.md                 first line "@AGENTS.md", so Claude Code loads AGENTS.md
set -euo pipefail

say() { echo "kowboy-handbook-sync: $*"; }
stop() { echo "kowboy-handbook-sync: $*" >&2; exit 1; }

[ $# -eq 2 ] || stop "usage: kowboy-handbook-sync.sh HANDBOOK_DIR PROJECT_DIR"
hb=$1
proj=$2
start='<!-- kowboy-handbook:start -->'
end='<!-- kowboy-handbook:end -->'

# Check everything before writing anything, so a failed run leaves the project as it was.
[ -d "$proj" ] || stop "project folder $proj does not exist"
for f in kowboy-handbook-rules.md kowboy-handbook-output.md kowboy-handbook-phases.md; do
  [ -s "$hb/$f" ] || stop "handbook file $hb/$f is missing or empty; nothing was changed"
done
ls "$hb"/kowboy-handbook-phases/kowboy-handbook-phase-*.md >/dev/null 2>&1 \
  || stop "no phase files in $hb/kowboy-handbook-phases; nothing was changed"
agents="$proj/AGENTS.md"
if [ -f "$agents" ] && grep -qxF "$start" "$agents" && ! grep -qxF "$end" "$agents"; then
  stop "$agents has the start marker but not the end marker; fix it by hand, nothing was changed"
fi

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

{
  echo "$start"
  echo '<!-- Synced from github.com/KowboyMedia/kowboy-handbook. Edits inside this block are overwritten. -->'
  for f in rules output phases; do
    echo
    cat "$hb/kowboy-handbook-$f.md"
  done
  echo
  echo "$end"
} > "$tmp/block"

# AGENTS.md: replace the block, or put it on top. Writing with cat keeps the file's permissions.
if [ -f "$agents" ] && grep -qxF "$start" "$agents"; then
  awk -v s="$start" -v e="$end" -v b="$tmp/block" '
    $0 == s { while ((getline line < b) > 0) print line; skip = 1; next }
    skip && $0 == e { skip = 0; next }
    !skip { print }' "$agents" > "$tmp/agents"
  how="block replaced"
elif [ -f "$agents" ]; then
  { cat "$tmp/block"; echo; cat "$agents"; } > "$tmp/agents"
  how="block added on top"
else
  cp "$tmp/block" "$tmp/agents"
  how="created"
fi
if [ -f "$agents" ] && cmp -s "$tmp/agents" "$agents"; then
  say "AGENTS.md already current"
else
  cat "$tmp/agents" > "$agents"
  say "AGENTS.md $how"
fi

# Phase files. Skipped when the project is the handbook repository itself.
if [ "$(cd "$hb" && pwd -P)" = "$(cd "$proj" && pwd -P)" ]; then
  say "phase files left as they are (project is the handbook itself)"
else
  rm -rf "$proj/kowboy-handbook-phases"
  cp -R "$hb/kowboy-handbook-phases" "$proj/kowboy-handbook-phases"
  say "phase files copied"
fi

# CLAUDE.md
claude="$proj/CLAUDE.md"
if [ ! -f "$claude" ]; then
  echo '@AGENTS.md' > "$claude"
  say "CLAUDE.md created"
elif ! grep -qxF '@AGENTS.md' "$claude"; then
  { echo '@AGENTS.md'; echo; cat "$claude"; } > "$tmp/claude"
  cat "$tmp/claude" > "$claude"
  say "CLAUDE.md now loads AGENTS.md"
else
  say "CLAUDE.md already loads AGENTS.md"
fi
