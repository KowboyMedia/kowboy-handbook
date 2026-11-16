#!/usr/bin/env python3
"""The Kowboy package's automatic checks, one entry per platform event.

    kowboy.py session-start HANDBOOK.md | WORK.md
                              gives the session that page whole
    kowboy.py rules           repeats the ten rules at every message
    kowboy.py guard           holds a dangerous action for the operator's yes
    kowboy.py reply           sends back a reply without its state line, and has
                              the advisor check a reply that asks the operator

Each reads the event as JSON on stdin and answers as JSON on stdout. The pages
are read from this repository itself, so no copy of them exists.
"""

import json
import os
import re
import shlex
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def page(name):
    return (ROOT / name).read_text(encoding="utf-8")


def answer(event, **fields):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": event, **fields}}))


# --- session-start and rules ------------------------------------------------


# The platform cuts a hook's text at 10,000 characters to a 2,000-character preview.
LIMIT = 10_000

INTRO = {
    "HANDBOOK.md": (
        "The Kowboy package gives you the Kowboy handbook, binding: HANDBOOK.md here and "
        "WORK.md next. Follow them as you would a CLAUDE.md. The phases of PHASES.md are "
        "the package's skills. Name the handbook's version in the first line of your "
        "first reply.\n\n"
    ),
    "WORK.md": "The Kowboy handbook, its required second page:\n\n",
}


def page_text(name):
    text = INTRO[name] + page(name)
    if len(text) <= LIMIT:
        return text
    return (
        f"{INTRO[name]}{name} is too long to be given here: read {ROOT / name} whole with "
        "the Read tool before any work."
    )


def session_start(name):
    answer("SessionStart", additionalContext=page_text(name))


def ten_rules():
    text = page("HANDBOOK.md")
    match = re.search(r"^## The rules\n(.*?)(?=^## )", text, re.S | re.M)
    if not match:
        raise SystemExit("HANDBOOK.md has no '## The rules' section")
    return match.group(1).strip()


def rules(_event):
    answer(
        "UserPromptSubmit",
        additionalContext="The Kowboy rules, repeated at every message:\n\n" + ten_rules(),
    )


# --- guard ------------------------------------------------------------------

RULE = {
    1: "rule 1, never destroy anything you cannot bring back yourself",
    2: "rule 2, never change production",
    6: "rule 6, never change the rules agents work by",
    8: "rule 8, never change, send, spend or pay for anything outside the repository",
}

# (rule, what it is, pattern) checked against each simple command of a Bash call.
COMMANDS = [
    (1, "overwriting history on GitHub", r"^git\s+push\b.*(\s--force\b|\s--force-with-lease\b|\s-f\b|\s\+\S)"),
    (1, "deleting on GitHub", r"^git\s+push\b.*(\s--delete\b|\s-d\b|\s:\S)"),
    (1, "dropping or emptying a database", r"\b(drop\s+(table|database|schema)|truncate\s+(table\s+)?\w)"),
    (1, "deleting every row of a table", r"\bdelete\s+from\s+[\w.\"`]+\s*(;|$|\"|')"),
    (1, "deleting in a cloud account", r"^(aws|doctl|gcloud|az|heroku)\b.*\b(delete|destroy|terminate|rm|remove|rb)\b"),
    (1, "deleting with kubectl or terraform", r"^(kubectl\s+delete|terraform\s+destroy)\b"),
    (1, "deleting on GitHub", r"^gh\s+(repo|release)\s+delete\b"),
    (2, "logging in to a server", r"^(ssh|scp|sftp)\b"),
    (2, "copying to a server", r"^rsync\b.*\s[\w.@-]+:\S*"),
    (2, "deploying", r"^(vercel|netlify)\b.*--prod\b"),
    (2, "deploying", r"^(fly|flyctl|firebase|wrangler|serverless|sls|eb)\s+(deploy|publish)\b"),
    (2, "deploying", r"^(gcloud\s+app\s+deploy|kubectl\s+apply|terraform\s+apply|cap\s+\w+\s+deploy)\b"),
    (2, "merging on GitHub", r"^gh\s+(pr\s+merge|workflow\s+run|secret\s+(set|delete))\b"),
    (8, "sending mail", r"^(sendmail|mail|mailx)\b|^aws\s+sesv?2?\s+send"),
    (8, "starting an agent as a separate program", r"^(npx\s+(-y\s+)?@anthropic-ai/claude-code|claude)\b.*\s(-p|--print)\b"),
]

# Commands that only show text; nothing they name is acted on.
TEXT_ONLY = {"grep", "rg", "ag", "echo", "printf", "cat", "less", "head", "tail", "awk", "sed", "jq"}
TEMP_DIRS = {Path("/tmp").resolve(), Path(tempfile.gettempdir()).resolve()}
URLISH = re.compile(r"^(https?://|[\w-]+(\.[\w-]+)+(:\d+)?(/|$))")
LOCAL_HOSTS = re.compile(r"^(https?://)?(localhost|127\.0\.0\.1|0\.0\.0\.0|\[::1\])([:/]|$)")
WRITE_FLAGS = re.compile(r"^(-d|--data\S*|-F|--form\S*|-T|--upload-file|--json)$")
WRITE_METHOD = re.compile(r"^(-X|--request)(=?)(POST|PUT|PATCH|DELETE)?$", re.I)

RULE_FILES = {"CLAUDE.md", "CLAUDE.local.md", "AGENTS.md"}
HANDBOOK_FILES = {"HANDBOOK.md", "WORK.md", "PHASES.md"}
PACKAGE_DIRS = ("hooks/", "skills/", "agents/", ".claude-plugin/")

READ_WORDS = {
    "get", "list", "search", "read", "find", "query", "fetch", "show", "describe",
    "download", "explore", "scan", "whoami", "view", "count", "check", "status",
    "wait", "summarize", "suggest", "export", "me", "guide", "balance",
}
WRITE_WORDS = {
    "send", "reply", "forward", "create", "update", "delete", "trash", "remove",
    "move", "share", "merge", "publish", "deploy", "generate", "upload", "add",
    "set", "complete", "schedule", "post", "edit", "write", "archive", "label",
    "mark", "start", "stop", "cancel", "rent", "exec", "import", "copy", "attach",
    "react", "batch", "execute", "fork", "push", "rename", "respond", "link",
    "unlink", "resolve", "invoke", "clone", "confirm", "register", "fire", "pin",
    "unarchive", "uncomplete", "untrash", "unmark", "unlabel", "pause", "resume",
    "enable", "disable", "subscribe", "unsubscribe", "trigger", "run", "restore",
    "duplicate", "split", "participate", "request", "save", "apply",
}
# Writes the platform already asks about every time, or that are the repository's own work.
PASS_TOOLS = {
    "mcp__claude-code-remote__create_environment",
    "mcp__claude-code-remote__update_environment",
    "mcp__claude-code-remote__switch_environment",
    "mcp__claude-code-remote__request_credential",
    "mcp__claude-code-remote__request_computer_folder",
    "mcp__claude-code-remote__confirm_repository_trust",
    "mcp__claude-code-remote__send_later",
    "mcp__claude-code-remote__subscribe_pr_activity",
    "mcp__claude-code-remote__unsubscribe_pr_activity",
    "mcp__claude-code-remote__register_repo_root",
    "mcp__claude-code-remote__add_repo",
    "mcp__claude-code-remote__report_preview_port",
}
GITHUB_HOLD = {"merge", "delete", "fork", "enable", "trigger"}
GITHUB_HOLD_TOOLS = {"mcp__github__create_repository", "mcp__github__actions_run_trigger"}


def simple_commands(command):
    """Split a shell command line into its simple commands, as lists of words."""
    pieces = re.split(r"&&|\|\||;|\||\n|\$\(|`|\(|\)", command)
    for piece in pieces:
        try:
            words = shlex.split(piece, posix=True)
        except ValueError:
            words = piece.split()
        while words and re.match(r"^\w+=", words[0]):
            words = words[1:]
        while words and words[0] in ("sudo", "env", "time", "nohup", "exec", "command"):
            words = words[1:]
        if words:
            yield words


def inside(path, folder):
    try:
        path.relative_to(folder)
        return True
    except ValueError:
        return False


def hold_rm(words, cwd):
    flags = "".join(w[1:] for w in words[1:] if w.startswith("-") and not w.startswith("--"))
    long_flags = {w for w in words[1:] if w.startswith("--")}
    if "r" not in flags.lower() and "--recursive" not in long_flags:
        return None
    for target in (w for w in words[1:] if not w.startswith("-")):
        if target.startswith("~") or "$" in target:
            return "deleting outside the working folder"
        resolved = (cwd / target).resolve()
        in_temp = any(inside(resolved, folder) and resolved != folder for folder in TEMP_DIRS)
        if not in_temp and (resolved == cwd or not inside(resolved, cwd)):
            return "deleting the working folder or something outside it"
    return None


def hold_web_write(words):
    if words[0] not in ("curl", "wget", "http", "https", "xh"):
        return None
    urls = [w for w in words[1:] if URLISH.match(w) or LOCAL_HOSTS.match(w)]
    if urls and all(LOCAL_HOSTS.match(u) for u in urls):
        return None
    for i, word in enumerate(words[1:], 1):
        method = WRITE_METHOD.match(word)
        if method:
            value = method.group(3) or (words[i + 1] if i + 1 < len(words) else "")
            if value.upper() in ("POST", "PUT", "PATCH", "DELETE"):
                return "sending or changing data on a server"
        if WRITE_FLAGS.match(word) or word.startswith("--post-"):
            return "sending or changing data on a server"
        if words[0] in ("http", "https", "xh") and word.upper() in ("POST", "PUT", "PATCH", "DELETE"):
            return "sending or changing data on a server"
    return None


def rule_file_reason(path, cwd):
    path = (cwd / path).resolve() if not Path(path).is_absolute() else Path(path)
    if path.name in RULE_FILES or ".claude" in path.parts:
        return "editing agents' rule files"
    for folder in [path.parent, *path.parent.parents]:
        if (folder / ".claude-plugin" / "plugin.json").is_file():
            relative = path.relative_to(folder).as_posix()
            if relative in HANDBOOK_FILES or relative.startswith(PACKAGE_DIRS):
                return "editing the handbook or the Kowboy package"
            break
    return None


def bash_reason(command, cwd):
    for words in simple_commands(command):
        if Path(words[0]).name in TEXT_ONLY:
            continue
        line = " ".join(words)
        for rule, what, pattern in COMMANDS:
            if re.search(pattern, line, re.I):
                return rule, what
        if words[0] == "rm":
            what = hold_rm(words, cwd)
            if what:
                return 1, what
        what = hold_web_write(words)
        if what:
            return 8, what
    redirect = re.search(r"(>>?|\btee\b(\s+-a)?)\s*([^\s;&|]+)", command)
    if redirect and rule_file_reason(redirect.group(3), cwd):
        return 6, "editing agents' rule files"
    sed = re.search(r"\bsed\s+(-\w*i\w*|--in-place)\b.*?(\S*(CLAUDE|AGENTS)\.md|\S*\.claude/\S+)", command)
    if sed:
        return 6, "editing agents' rule files"
    return None


def mcp_reason(tool):
    if tool in PASS_TOOLS:
        return None
    if tool in GITHUB_HOLD_TOOLS:
        return 8, "changing GitHub outside this work"
    action = tool.split("__", 2)[-1]
    words = set(re.split(r"[_\-]", action.lower()))
    if tool.startswith("mcp__github__"):
        if words & GITHUB_HOLD:
            return 2, "merging, deleting or running on GitHub"
        return None
    if words & WRITE_WORDS or not words & READ_WORDS:
        return 8, "writing through a connected service"
    return None


def guard(event):
    tool = event.get("tool_name", "")
    data = event.get("tool_input") or {}
    cwd = Path(event.get("cwd") or os.getcwd()).resolve()
    found = None
    if tool == "Bash":
        found = bash_reason(data.get("command", ""), cwd)
    elif tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        what = rule_file_reason(data.get("file_path") or data.get("notebook_path") or "", cwd)
        if what:
            found = 6, what
    elif tool.startswith("mcp__"):
        found = mcp_reason(tool)
    if not found:
        return
    rule, what = found
    answer(
        "PreToolUse",
        permissionDecision="ask",
        permissionDecisionReason=(
            f"Kowboy package: {what} ({RULE[rule]}). Allow only if the operator asked for "
            "exactly this step."
        ),
    )


# --- reply ------------------------------------------------------------------

STATES = ("Working:", "Waiting for you:", "Waiting for something else:", "Done:")


def first_line(text):
    for line in text.splitlines():
        line = re.sub(r"^[\s#>*_\-]+", "", line).replace("**", "").replace("__", "").strip()
        if line:
            return line
    return ""


def asks_operator(text):
    return bool(re.search(r"^\s*(\*\*|#+\s*)?Questions\b", text, re.M))


def advisor_ran(transcript_path):
    """True when the advisor was called since the operator's last message."""
    try:
        lines = Path(transcript_path).read_text(encoding="utf-8").splitlines()
    except (OSError, TypeError):
        return False
    for line in reversed(lines):
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = (entry.get("message") or {}).get("content")
        if entry.get("type") == "user" and (
            isinstance(content, str)
            or isinstance(content, list)
            and not any(part.get("type") == "tool_result" for part in content)
        ):
            return False
        if entry.get("type") == "assistant" and isinstance(content, list):
            for part in content:
                if part.get("type") == "tool_use" and str(
                    (part.get("input") or {}).get("subagent_type", "")
                ).endswith("advisor"):
                    return True
    return False


def reply(event):
    if event.get("stop_hook_active"):
        return
    text = event.get("last_assistant_message") or ""
    if not text.strip():
        return
    reasons = []
    if not first_line(text).startswith(STATES):
        reasons.append(
            "Start the reply with the state line: 'Working:', 'Waiting for you:', "
            "'Waiting for something else:' or 'Done:' (HANDBOOK.md, How to reply)."
        )
    elif first_line(text).startswith("Waiting for you:") and not re.search(r"\*\*\d+\*\*", text):
        reasons.append(
            "A reply that waits for the operator asks numbered questions: give each its "
            "number from the question log, in bold."
        )
    if asks_operator(text) and not advisor_ran(event.get("transcript_path")):
        reasons.append(
            "Before you ask the operator, have the advisor check your questions: call the "
            "agent 'kowboy:advisor' with each question, the operator's words for the item, "
            f"and the path {ROOT / 'WORK.md'}. Follow its answer or keep the question."
        )
    if reasons:
        print(json.dumps({"decision": "block", "reason": "Kowboy package: " + " ".join(reasons)}))


ENTRIES = {"rules": rules, "guard": guard, "reply": reply}

if __name__ == "__main__":
    raw = sys.stdin.read()
    if sys.argv[1] == "session-start":
        session_start(sys.argv[2])
    else:
        ENTRIES[sys.argv[1]](json.loads(raw) if raw.strip() else {})
