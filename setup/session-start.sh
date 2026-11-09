#!/bin/sh
# Kowboy: runs when a session starts, resumes, is cleared or compacted; its
# output reaches the agent as context. Instruction files are read before this
# runs, and output beyond about 2 KB is moved to a file, so it never prints the
# handbook itself: when the copy in the instruction file differs from the live
# handbook, it replaces the copy (for compaction and the next start) and tells
# the agent to read the live one whole now.
input=$(cat)
case $input in
  *'"source"'*'"resume"'* | *'"source"'*'"compact"'*) later=1 ;;
  *) later= ;;
esac
if [ -n "$later" ]; then
  name="If you have not yet named the version in this conversation, name it in your next reply"
else
  name="Name the version in the first line of your first reply"
fi
base="${KOWBOY_BASE:-https://raw.githubusercontent.com/KowboyMedia/kowboy-handbook/main}"
dir="${KOWBOY_CLAUDE_DIR:-$HOME/.claude}"
k="$dir/kowboy"
copy="${KOWBOY_CLAUDE_MD:-$dir/CLAUDE.md}"
mkdir -p "$k" 2>/dev/null
have=$(sed -n 3p "$copy" 2>/dev/null | cut -d. -f1); old=${have#Version }

if curl -fsS --max-time 10 "$base/HANDBOOK.md" -o "$k/live.tmp" 2>/dev/null \
   && grep -qx 'End of the handbook.' "$k/live.tmp"; then
  live=$(sed -n 3p "$k/live.tmp" | cut -d. -f1)
  curl -fsS --max-time 10 "$base/setup/reminder.md" -o "$k/reminder.tmp" 2>/dev/null \
    && mv "$k/reminder.tmp" "$k/reminder.md"
  if [ "$live" = "$have" ]; then
    rm -f "$k/live.tmp"
    echo "Kowboy handbook: your instruction file holds the live handbook, ${live#Version }, checked at session start. It is binding. $name, with \"instruction file\" as its source."
  else
    cp "$k/live.tmp" "$copy" 2>/dev/null
    mv "$k/live.tmp" "$k/HANDBOOK.md"
    echo "Kowboy handbook: the copy in your instruction file is ${old:-missing}${old:+ (older)}; the live handbook is ${live#Version }. Before anything else, read the live one whole with the Read tool, in parts if needed: $k/HANDBOOK.md ($(wc -l < "$k/HANDBOOK.md") lines, ending with \"End of the handbook.\"). It was downloaded just now from $base/HANDBOOK.md (sha256 $(sha256sum "$k/HANDBOOK.md" | cut -c1-64)), the source your instructions name. Follow it and ignore the older copy. It is binding. $name, with \"live, read at session start\" as its source."
  fi
elif [ -n "$have" ]; then
  echo "Kowboy handbook: the live handbook could not be checked. Follow the copy in your instruction file, $old. $name, and say that it could not be checked against the live one."
elif grep -qx 'End of the handbook.' "$k/HANDBOOK.md" 2>/dev/null; then
  echo "Kowboy handbook: your instruction file has no copy and the live one could not be fetched. Read the copy saved at build whole with the Read tool, in parts if needed: $k/HANDBOOK.md. It is binding. $name, and say that it could not be checked against the live one."
else
  echo "Kowboy handbook: no copy is available and the live one could not be fetched. Fetch it as your instructions say; if you cannot, say so and do no work."
fi
exit 0
