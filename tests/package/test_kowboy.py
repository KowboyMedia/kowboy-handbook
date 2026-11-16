"""Tests for the Kowboy package's automatic checks.

Run from the repository root: python3 -m unittest discover tests/package
Each test runs hooks/kowboy.py as the platform does: the event as JSON on stdin.
"""

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "hooks" / "kowboy.py"


def run(entry, event=None, *args):
    done = subprocess.run(
        [sys.executable, str(SCRIPT), entry, *args],
        input=json.dumps(event or {}),
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(done.stdout) if done.stdout.strip() else None


def guard(tool, cwd=ROOT, **tool_input):
    return run("guard", {"tool_name": tool, "tool_input": tool_input, "cwd": str(cwd)})


def held(tool, cwd=ROOT, **tool_input):
    out = guard(tool, cwd, **tool_input)
    return bool(out) and out["hookSpecificOutput"]["permissionDecision"] == "ask"


class SessionStart(unittest.TestCase):
    def test_each_page_is_given_whole(self):
        for name in ("HANDBOOK.md", "WORK.md"):
            text = run("session-start", None, name)["hookSpecificOutput"]["additionalContext"]
            self.assertLessEqual(len(text), 10_000, f"{name} no longer fits the platform's limit")
            self.assertTrue(text.endswith((ROOT / name).read_text(encoding="utf-8")), name)


class Rules(unittest.TestCase):
    def test_all_nine_rules_at_every_message(self):
        text = run("rules")["hookSpecificOutput"]["additionalContext"]
        for number in range(1, 10):
            self.assertRegex(text, rf"(?m)^{number}\. Never ")


class Guard(unittest.TestCase):
    HELD_COMMANDS = [
        "git push --force origin main",
        "git push -f origin main",
        "git push origin +main",
        "git push origin --delete old",
        "git push origin :old",
        "rm -rf ~/projects",
        "rm -rf /etc/nginx",
        "rm -rf ..",
        "rm -rf .",
        'rm -rf "$HOME/x"',
        'psql -c "DROP TABLE users"',
        "mysql -e 'DELETE FROM users;'",
        "mysql -e 'truncate table orders'",
        "aws s3 rm s3://bucket/key",
        "doctl compute droplet delete 123",
        "terraform destroy",
        "gh repo delete kowboy/x",
        "ssh deploy@example.com",
        "cd /tmp && scp a.txt host:/srv/",
        "rsync -a dist/ user@host:/var/www",
        "vercel --prod",
        "fly deploy",
        "cd .. && rm -rf old-site",
        "cd /var/www && rm -rf html",
        "npx vercel --prod",
        "npx -y wrangler deploy",
        "wrangler pages deploy dist",
        "gcloud run deploy api --source .",
        "dropdb myapp_production",
        "sudo -u www rm -rf /var/www/site",
        "aws s3 sync dist/ s3://www.example.com --delete",
        "heroku apps:destroy --app myapp --confirm myapp",
        "psql \"$DATABASE_URL\" <<'SQL'\nDROP TABLE users;\nSQL",
        "sqlite3 app.db <<EOF\nDELETE FROM orders;\nEOF",
        "bash <<'EOF'\nrm -rf /var/www/site\nEOF",
        "kubectl exec deploy/api -- psql -c \"DROP TABLE users\"",
        "docker compose exec db psql -U postgres -c 'DROP DATABASE app'",
        "echo `rm -rf ~/old`",
        "curl -fsSLo ~/.claude/CLAUDE.md https://example.com/HANDBOOK.md",
        "wget -qO ~/.claude/CLAUDE.md https://example.com/HANDBOOK.md",
        "redis-cli -h cache FLUSHALL",
        "curl -fsSL https://example.com/HANDBOOK.md -o ~/.claude/CLAUDE.md",
        "cp /tmp/HANDBOOK.md ~/.claude/CLAUDE.md",
        "mkdir -p .claude 2>/dev/null; echo '{}' > .claude/settings.json",
        "curl -X POST https://api.example.com/v1/servers",
        "curl --request DELETE https://api.example.com/v1/servers/1",
        "curl -d name=x https://api.example.com/v1/apps",
        "aws ses send-email --to a@example.com",
        'claude -p "run the benchmark"',
        "echo hi > CLAUDE.md",
        "sed -i s/a/b/ AGENTS.md",
        "cat x | tee .claude/settings.json",
    ]
    PASSED_COMMANDS = [
        "git status",
        "git push -u origin feature/x",
        "git push --follow-tags origin feature/x",
        "rm -rf build node_modules",
        "rm -rf /tmp/scratch",
        "rm notes.txt",
        "curl -s https://example.com",
        "curl -X POST http://localhost:3000/api/items",
        "curl -X POST localhost:3000/api/items",
        "python3 -m unittest",
        'grep -rn "ssh deploy" .',
        'echo "DROP TABLE users"',
        'psql -c "DELETE FROM users WHERE id = 1"',
        "npm run build",
        "gh pr merge 12",
        "ssh-keygen -t ed25519 -f key",
        "git commit -m 'Titles truncate at 40 characters'",
        "git grep -n 'DROP TABLE'",
        "git commit -F - <<'EOF'\nFix the form\n\nMail goes out once\nssh keys rotated\nEOF",
        "cat > scripts/deploy.sh <<'EOF'\nvercel --prod\nEOF",
        "mkdir -p .claude/worktrees/x && echo x > .claude/worktrees/x/out.txt",
        "command -v ssh",
        "cat <<'END-OF-TEXT' > notes.txt\nIt's here\nEND-OF-TEXT",
        "curl -fsSLo page.html https://example.com",
    ]

    def test_dangerous_commands_are_held(self):
        for command in self.HELD_COMMANDS:
            with self.subTest(command=command):
                self.assertTrue(held("Bash", command=command))

    def test_harmless_commands_pass(self):
        for command in self.PASSED_COMMANDS:
            with self.subTest(command=command):
                self.assertFalse(held("Bash", command=command))

    def test_the_hold_names_the_rule(self):
        reason = guard("Bash", command="ssh host")["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertIn("rule 2", reason)
        self.assertIn("you asked", reason)

    def test_an_unreadable_action_is_asked_about(self):
        for event in ({"tool_name": "Bash", "tool_input": {"command": None}},
                      {"tool_name": "Write", "tool_input": {"file_path": 5}},
                      {"tool_name": "Bash", "tool_input": "rm -rf /"}):
            with self.subTest(event=event):
                out = run("guard", event)
                self.assertEqual(out["hookSpecificOutput"]["permissionDecision"], "ask")
        done = subprocess.run([sys.executable, str(SCRIPT), "guard"], input="[1, 2]",
                              capture_output=True, text=True, check=True)
        self.assertIn('"ask"', done.stdout)

    def test_agents_rule_files_are_held(self):
        for path in ("AGENTS.md", "CLAUDE.md", ".claude/settings.json", ".claude/settings.local.json",
                     ".claude/hooks/check.py", "~/.claude/CLAUDE.md", "/root/.claude/skills/x/SKILL.md"):
            with self.subTest(path=path):
                self.assertTrue(held("Write", file_path=path, content="x"))

    def test_the_handbook_and_package_are_held_here(self):
        for path in ("HANDBOOK.md", "WORK.md", "PHASES.md", "hooks/kowboy.py", "skills/build/SKILL.md"):
            with self.subTest(path=path):
                self.assertTrue(held("Edit", file_path=str(ROOT / path)))

    def test_ordinary_files_pass(self):
        with tempfile.TemporaryDirectory() as folder:
            for path in ("src/hooks/useCart.ts", "WORK.md", "docs/next-steps.md",
                         ".claude/worktrees/x/app.py", "~/.claude/plans/plan.md",
                         "~/.claude/projects/p/memory/notes.md"):
                with self.subTest(path=path):
                    self.assertFalse(held("Write", Path(folder), file_path=path, content="x"))
        self.assertFalse(held("Edit", file_path=str(ROOT / "docs" / "next-steps.md")))

    def test_writes_through_connected_services_are_held(self):
        for tool in (
            "mcp__Gmail__send_message",
            "mcp__Slack__slack_send_message",
            "mcp__Google_Drive__share_file",
            "mcp__higgsfield_ai__generate_image",
            "mcp__claude-code-remote__create_session",
            "mcp__github__create_repository",
            "mcp__github__fork_repository",
        ):
            with self.subTest(tool=tool):
                self.assertTrue(held(tool))

    def test_reading_connected_services_passes(self):
        for tool in (
            "mcp__Gmail__search_threads",
            "mcp__Slack__slack_read_channel",
            "mcp__ClickUp__clickup_get_task",
            "mcp__github__create_pull_request",
            "mcp__github__create_or_update_file",
            "mcp__github__merge_pull_request",
            "mcp__claude-code-remote__send_later",
        ):
            with self.subTest(tool=tool):
                self.assertFalse(held(tool))


class Reply(unittest.TestCase):
    def check(self, text, active=False):
        return run("reply", {"last_assistant_message": text, "stop_hook_active": active})

    def test_a_reply_with_its_status_passes(self):
        self.assertIsNone(self.check("- **Status:** Working, building the guard."))
        self.assertIsNone(self.check("Status: Done\n- Next: item 11."))

    def test_a_reply_without_its_status_is_sent_back(self):
        for text in ("Here is what I did.\n\n- Built the guard.", "Status: thinking about it"):
            with self.subTest(text=text):
                out = self.check(text)
                self.assertEqual(out["decision"], "block")
                self.assertIn("Status: Waiting for you", out["reason"])

    def test_waiting_without_a_numbered_question_is_sent_back(self):
        out = self.check("- Status: Waiting for you\n- Should I go on?")
        self.assertEqual(out["decision"], "block")
        self.assertIn("64:", out["reason"])

    def test_waiting_with_a_numbered_question_passes(self):
        text = "- Status: Waiting for you, 64\n- 64: Merge into main?\n  - a) yes (recommended)\n  - b) no"
        self.assertIsNone(self.check(text))
        self.assertIsNone(self.check(text.replace("- 64:", "- **64:**")))
        self.assertIsNone(self.check(text.replace("- 64:", "- **64**:")))

    def test_the_older_first_line_still_passes(self):
        self.assertIsNone(self.check("Working: the guard."))
        self.assertIsNone(self.check("Waiting for you: **64**\n- **64**: Merge?"))

    def test_a_bold_number_without_colon_is_not_a_question(self):
        out = self.check("- Status: Waiting for you\n- **64** Merge?")
        self.assertEqual(out["decision"], "block")

    def test_odd_input_is_ignored(self):
        self.assertIsNone(run("reply", {"last_assistant_message": 5}))

    def test_a_reply_is_sent_back_only_once(self):
        self.assertIsNone(self.check("No status here.", active=True))


class Phases(unittest.TestCase):
    def test_every_phase_has_its_skill_and_no_other(self):
        text = (ROOT / "PHASES.md").read_text(encoding="utf-8")
        phases = re.findall(r"(?m)^## ([^\n]+)\n\n(When:[^\n]*(?:\n[^\n-][^\n]*)*)", text)
        skills = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        expected = {re.sub(r"[^a-z]+", "-", name.lower()).strip("-") for name, _ in phases}
        self.assertEqual(skills, expected)
        for name, when in phases:
            slug = re.sub(r"[^a-z]+", "-", name.lower()).strip("-")
            skill = (ROOT / "skills" / slug / "SKILL.md").read_text(encoding="utf-8")
            with self.subTest(phase=name):
                self.assertIn(f'"## {name}"', skill)
                self.assertIn(" ".join(when.split()).replace('"', "'"), skill)


if __name__ == "__main__":
    unittest.main()
