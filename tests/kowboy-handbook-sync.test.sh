#!/usr/bin/env bash
# Proof for docs/strategy.md: one test per acceptance criterion.
# Run from anywhere: bash tests/kowboy-handbook-sync.test.sh
set -uo pipefail

repo=$(cd "$(dirname "$0")/.." && pwd -P)
sync="$repo/kowboy-handbook-sync.sh"
start='<!-- kowboy-handbook:start -->'
end='<!-- kowboy-handbook:end -->'
failed=0
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT
mktemp() { command mktemp -p "$scratch" "$@"; }

pass() { echo "ok   $1"; }
fail() { echo "FAIL $1: $2"; failed=1; }

# A fresh copy of the handbook, so a test can change it without touching the repository.
handbook_copy() {
  local d; d=$(mktemp -d)
  cp "$repo"/kowboy-handbook-*.md "$d/"
  cp -R "$repo/kowboy-handbook-phases" "$d/"
  echo "$d"
}

test_1_new_project_gets_agents_md() {
  local hb p; hb=$(handbook_copy); p=$(mktemp -d)
  bash "$sync" "$hb" "$p" >/dev/null || { fail 1 "sync exited non-zero"; return; }
  local a="$p/AGENTS.md"
  grep -qxF "$start" "$a" && grep -qxF "$end" "$a" \
    && grep -qF '# Kowboy handbook: the rules' "$a" \
    && grep -qF '# Kowboy handbook: output format' "$a" \
    && grep -qF '# Kowboy handbook: the phases' "$a" \
    && diff -r "$hb/kowboy-handbook-phases" "$p/kowboy-handbook-phases" >/dev/null \
    && pass "1 new project gets AGENTS.md with rules, output, phase index and phase files" \
    || fail 1 "AGENTS.md block or phase files missing"
}

test_2_existing_agents_md_is_kept() {
  local hb p; hb=$(handbook_copy); p=$(mktemp -d)
  printf '# My project\n\nDesign: none\n' > "$p/AGENTS.md"
  bash "$sync" "$hb" "$p" >/dev/null || { fail 2 "sync exited non-zero"; return; }
  [ "$(head -n1 "$p/AGENTS.md")" = "$start" ] \
    && [ "$(tail -n3 "$p/AGENTS.md")" = "$(printf '# My project\n\nDesign: none')" ] \
    && pass "2 existing AGENTS.md keeps its text; the block goes on top" \
    || fail 2 "project text lost or block not on top"
}

test_3_second_run_changes_nothing() {
  local hb p before; hb=$(handbook_copy); p=$(mktemp -d)
  printf 'Project notes\n' > "$p/AGENTS.md"
  bash "$sync" "$hb" "$p" >/dev/null
  before=$(cd "$p" && find . -type f -exec sha256sum {} + | sort)
  bash "$sync" "$hb" "$p" >/dev/null || { fail 3 "sync exited non-zero"; return; }
  [ "$before" = "$(cd "$p" && find . -type f -exec sha256sum {} + | sort)" ] \
    && pass "3 a second run changes nothing" \
    || fail 3 "files changed on the second run"
}

test_4_handbook_change_replaces_only_the_block() {
  local hb p; hb=$(handbook_copy); p=$(mktemp -d)
  printf 'Project notes\n' > "$p/AGENTS.md"
  bash "$sync" "$hb" "$p" >/dev/null
  printf 'Text after the block\n' >> "$p/AGENTS.md"
  awk '{ sub(/^Version .*\.$/, "Version TEST-NEW."); print }' "$hb/kowboy-handbook-rules.md" > "$hb/x" \
    && mv "$hb/x" "$hb/kowboy-handbook-rules.md"
  bash "$sync" "$hb" "$p" >/dev/null || { fail 4 "sync exited non-zero"; return; }
  grep -qF 'Version TEST-NEW.' "$p/AGENTS.md" \
    && [ "$(grep -cxF "$start" "$p/AGENTS.md")" = 1 ] \
    && grep -qxF 'Project notes' "$p/AGENTS.md" \
    && grep -qxF 'Text after the block' "$p/AGENTS.md" \
    && pass "4 a handbook change replaces the block and only the block" \
    || fail 4 "block not replaced, duplicated, or project text lost"
}

test_5_removed_phase_file_is_removed() {
  local hb p; hb=$(handbook_copy); p=$(mktemp -d)
  bash "$sync" "$hb" "$p" >/dev/null
  rm "$hb/kowboy-handbook-phases/kowboy-handbook-phase-design.md"
  bash "$sync" "$hb" "$p" >/dev/null || { fail 5 "sync exited non-zero"; return; }
  [ ! -e "$p/kowboy-handbook-phases/kowboy-handbook-phase-design.md" ] \
    && pass "5 a phase file removed from the handbook is removed from the project" \
    || fail 5 "stale phase file left in the project"
}

test_6_index_matches_phase_files() {
  local named on_disk
  named=$(grep -o 'kowboy-handbook-phase-[a-z-]*\.md' "$repo/kowboy-handbook-phases.md" | sort -u)
  on_disk=$(cd "$repo/kowboy-handbook-phases" && ls | sort)
  local ok=1 f
  [ "$named" = "$on_disk" ] || ok=0
  for f in "$repo"/kowboy-handbook-phases/*.md; do
    [ "$(tail -n1 "$f")" = 'End of the phase.' ] || ok=0
  done
  [ "$ok" = 1 ] \
    && pass "6 every phase file is named in the index, exists, and ends with its end line" \
    || fail 6 "index and phase files differ, or a file lacks 'End of the phase.'"
}

test_7_claude_md_loads_agents_md() {
  local hb p q; hb=$(handbook_copy); p=$(mktemp -d); q=$(mktemp -d)
  printf 'Own Claude notes\n' > "$q/CLAUDE.md"
  bash "$sync" "$hb" "$p" >/dev/null && bash "$sync" "$hb" "$q" >/dev/null \
    || { fail 7 "sync exited non-zero"; return; }
  bash "$sync" "$hb" "$q" >/dev/null
  [ "$(cat "$p/CLAUDE.md")" = '@AGENTS.md' ] \
    && [ "$(head -n1 "$q/CLAUDE.md")" = '@AGENTS.md' ] \
    && [ "$(grep -cxF '@AGENTS.md' "$q/CLAUDE.md")" = 1 ] \
    && grep -qxF 'Own Claude notes' "$q/CLAUDE.md" \
    && pass "7 CLAUDE.md loads AGENTS.md, once, keeping its own text" \
    || fail 7 "CLAUDE.md missing the import, duplicated it, or lost text"
}

test_8_missing_handbook_file_stops_and_changes_nothing() {
  local hb p before out; hb=$(handbook_copy); p=$(mktemp -d)
  printf 'Project notes\n' > "$p/AGENTS.md"
  rm "$hb/kowboy-handbook-output.md"
  before=$(cd "$p" && find . -type f -exec sha256sum {} + | sort)
  if out=$(bash "$sync" "$hb" "$p" 2>&1); then fail 8 "sync succeeded without a handbook file"; return; fi
  echo "$out" | grep -qF 'kowboy-handbook-output.md' \
    && [ "$before" = "$(cd "$p" && find . -type f -exec sha256sum {} + | sort)" ] \
    && pass "8 a missing handbook file stops the sync, names the file, changes nothing" \
    || fail 8 "message does not name the file, or the project changed"
}

test_9_this_repository_is_current() {
  local p; p=$(mktemp -d)
  cp "$repo/AGENTS.md" "$repo/CLAUDE.md" "$p/"
  bash "$sync" "$repo" "$p" >/dev/null || { fail 9 "sync exited non-zero"; return; }
  diff -q "$repo/AGENTS.md" "$p/AGENTS.md" >/dev/null && diff -q "$repo/CLAUDE.md" "$p/CLAUDE.md" >/dev/null \
    && pass "9 this repository's AGENTS.md block matches the handbook text" \
    || fail 9 "run: bash kowboy-handbook-sync.sh . ."
}

snapshot() { (cd "$1" && find . -type f -exec sha256sum {} + | sort); }

test_10_start_without_end_stops_and_changes_nothing() {
  local hb p before; hb=$(handbook_copy); p=$(mktemp -d)
  printf '%s\nhalf a block\n' "$start" > "$p/AGENTS.md"
  before=$(snapshot "$p")
  if bash "$sync" "$hb" "$p" >/dev/null 2>&1; then fail 10 "sync succeeded with a broken block"; return; fi
  [ "$before" = "$(snapshot "$p")" ] \
    && pass "10 a start marker without an end marker stops the sync and changes nothing" \
    || fail 10 "project changed"
}

test_11_marker_in_later_text_is_kept() {
  local hb p; hb=$(handbook_copy); p=$(mktemp -d)
  bash "$sync" "$hb" "$p" >/dev/null
  printf 'Notes\n%s\nquoted marker above, keep me\n' "$start" >> "$p/AGENTS.md"
  bash "$sync" "$hb" "$p" >/dev/null || { fail 11 "sync exited non-zero"; return; }
  grep -qxF 'quoted marker above, keep me' "$p/AGENTS.md" \
    && pass "11 a marker quoted in the project's own text later on is kept, with the text after it" \
    || fail 11 "project text after a quoted marker was lost"
}

test_12_windows_line_ends_replace_the_block() {
  local hb p; hb=$(handbook_copy); p=$(mktemp -d)
  printf 'Project notes\n' > "$p/AGENTS.md"
  bash "$sync" "$hb" "$p" >/dev/null
  awk '{ printf "%s\r\n", $0 }' "$p/AGENTS.md" > "$p/x" && mv "$p/x" "$p/AGENTS.md"
  bash "$sync" "$hb" "$p" >/dev/null || { fail 12 "sync exited non-zero"; return; }
  [ "$(grep -c 'kowboy-handbook:start' "$p/AGENTS.md")" = 1 ] \
    && grep -q '^Project notes' "$p/AGENTS.md" \
    && pass "12 AGENTS.md with Windows line ends gets its block replaced, not a second one" \
    || fail 12 "block duplicated or project text lost"
}

test_13_claude_md_linked_to_agents_md() {
  local hb p; hb=$(handbook_copy); p=$(mktemp -d)
  printf 'Project notes\n' > "$p/AGENTS.md"
  ln -s AGENTS.md "$p/CLAUDE.md"
  bash "$sync" "$hb" "$p" >/dev/null || { fail 13 "sync exited non-zero"; return; }
  [ -L "$p/CLAUDE.md" ] && ! grep -qxF '@AGENTS.md' "$p/AGENTS.md" \
    && pass "13 CLAUDE.md linked to AGENTS.md is left alone and AGENTS.md gets no import line" \
    || fail 13 "link replaced or '@AGENTS.md' written into AGENTS.md"
}

test_14_no_trailing_newline_is_stable() {
  local hb p before; hb=$(handbook_copy); p=$(mktemp -d)
  printf 'Project notes without newline' > "$p/AGENTS.md"
  bash "$sync" "$hb" "$p" >/dev/null
  before=$(snapshot "$p")
  bash "$sync" "$hb" "$p" >/dev/null || { fail 14 "sync exited non-zero"; return; }
  [ "$before" = "$(snapshot "$p")" ] \
    && pass "14 AGENTS.md without a final newline is stable from the first run" \
    || fail 14 "second run changed files"
}

test_15_handbook_synced_onto_itself_keeps_phases() {
  local hb; hb=$(handbook_copy)
  bash "$sync" "$hb" "$hb" >/dev/null || { fail 15 "sync exited non-zero"; return; }
  diff -r "$repo/kowboy-handbook-phases" "$hb/kowboy-handbook-phases" >/dev/null \
    && pass "15 syncing the handbook onto itself keeps its phase files" \
    || fail 15 "phase files changed or deleted"
}

test_16_marker_with_trailing_spaces_is_found() {
  local hb p; hb=$(handbook_copy); p=$(mktemp -d)
  printf 'Project notes\n' > "$p/AGENTS.md"
  bash "$sync" "$hb" "$p" >/dev/null
  awk '{ if (index($0, "kowboy-handbook:")) $0 = $0 "  "; print }' "$p/AGENTS.md" > "$p/x" && mv "$p/x" "$p/AGENTS.md"
  bash "$sync" "$hb" "$p" >/dev/null || { fail 16 "sync exited non-zero"; return; }
  [ "$(grep -c 'kowboy-handbook:start' "$p/AGENTS.md")" = 1 ] \
    && pass "16 markers with trailing spaces are still found, so no second block is added" \
    || fail 16 "a second block was added"
}

test_17_other_project_files_are_untouched() {
  local hb p before; hb=$(handbook_copy); p=$(mktemp -d)
  mkdir -p "$p/src" "$p/docs"
  printf 'readme\n' > "$p/README.md"; printf 'code\n' > "$p/src/app.js"; printf 'notes\n' > "$p/docs/agents.md"
  before=$(cd "$p" && find . -type f ! -name AGENTS.md ! -name CLAUDE.md ! -path './kowboy-handbook-phases/*' -exec sha256sum {} + | sort)
  bash "$sync" "$hb" "$p" >/dev/null || { fail 17 "sync exited non-zero"; return; }
  [ "$before" = "$(cd "$p" && find . -type f ! -name AGENTS.md ! -name CLAUDE.md ! -path './kowboy-handbook-phases/*' -exec sha256sum {} + | sort)" ] \
    && pass "17 files other than AGENTS.md, CLAUDE.md and kowboy-handbook-phases/ are untouched" \
    || fail 17 "another project file changed"
}

test_1_new_project_gets_agents_md
test_2_existing_agents_md_is_kept
test_3_second_run_changes_nothing
test_4_handbook_change_replaces_only_the_block
test_5_removed_phase_file_is_removed
test_6_index_matches_phase_files
test_7_claude_md_loads_agents_md
test_8_missing_handbook_file_stops_and_changes_nothing
test_9_this_repository_is_current
test_10_start_without_end_stops_and_changes_nothing
test_11_marker_in_later_text_is_kept
test_12_windows_line_ends_replace_the_block
test_13_claude_md_linked_to_agents_md
test_14_no_trailing_newline_is_stable
test_15_handbook_synced_onto_itself_keeps_phases
test_16_marker_with_trailing_spaces_is_found
test_17_other_project_files_are_untouched

[ "$failed" = 0 ] && echo "all passed" || { echo "some failed"; exit 1; }
