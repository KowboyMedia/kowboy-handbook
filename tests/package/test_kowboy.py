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
    def test_all_ten_rules_at_every_message(self):
        text = run("rules")["hookSpecificOutput"]["additionalContext"]
        for number in range(1, 11):
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
        "gh pr merge 12",
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
        self.assertIn("operator", reason)

    def test_agents_rule_files_are_held(self):
        for path in ("AGENTS.md", "CLAUDE.md", ".claude/settings.json", "/root/.claude/CLAUDE.md"):
            with self.subTest(path=path):
                self.assertTrue(held("Write", file_path=path, content="x"))

    def test_the_handbook_and_package_are_held_here(self):
        for path in ("HANDBOOK.md", "WORK.md", "PHASES.md", "hooks/kowboy.py", "skills/build/SKILL.md"):
            with self.subTest(path=path):
                self.assertTrue(held("Edit", file_path=str(ROOT / path)))

    def test_ordinary_files_pass(self):
        with tempfile.TemporaryDirectory() as folder:
            for path in ("src/hooks/useCart.ts", "WORK.md", "docs/next-steps.md"):
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
            "mcp__github__merge_pull_request",
            "mcp__github__create_repository",
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
            "mcp__claude-code-remote__send_later",
        ):
            with self.subTest(tool=tool):
                self.assertFalse(held(tool))


class Reply(unittest.TestCase):
    def check(self, text, transcript=None, active=False):
        event = {"last_assistant_message": text, "stop_hook_active": active}
        if transcript is not None:
            event["transcript_path"] = transcript
        return run("reply", event)

    def test_a_reply_with_its_state_passes(self):
        self.assertIsNone(self.check("**Working:** building the guard; next message by 14:30."))
        self.assertIsNone(self.check("Done: nothing left here."))

    def test_a_reply_without_its_state_is_sent_back(self):
        out = self.check("Here is what I did.\n\n- Built the guard.")
        self.assertEqual(out["decision"], "block")
        self.assertIn("Waiting for you:", out["reason"])

    def test_waiting_without_a_numbered_question_is_sent_back(self):
        out = self.check("Waiting for you: should I go on?")
        self.assertEqual(out["decision"], "block")
        self.assertIn("number", out["reason"])

    def test_questions_go_to_the_advisor_first(self):
        text = "**Waiting for you:** question 56.\n\n**Questions**\n- **56** Which?\n  - Reply: a or b."
        out = self.check(text)
        self.assertIn("kowboy:advisor", out["reason"])

    def test_questions_pass_once_the_advisor_ran(self):
        text = "**Waiting for you:** question 56.\n\n**Questions**\n- **56** Which?\n  - Reply: a or b."
        call = {"type": "tool_use", "name": "Agent", "input": {"subagent_type": "kowboy:advisor"}}
        lines = [
            {"type": "user", "message": {"content": "go on"}},
            {"type": "assistant", "message": {"content": [call]}},
            {"type": "user", "message": {"content": [{"type": "tool_result", "content": "Go"}]}},
        ]
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            f.write("\n".join(json.dumps(line) for line in lines))
        self.assertIsNone(self.check(text, f.name))
        Path(f.name).unlink()

    def test_a_reply_is_sent_back_only_once(self):
        self.assertIsNone(self.check("No state here.", active=True))


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
