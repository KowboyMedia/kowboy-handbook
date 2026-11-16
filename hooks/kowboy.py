#!/usr/bin/env python3
"""The Kowboy package's automatic checks, one entry per platform event.

    kowboy.py session-start HANDBOOK.md | WORK.md
                              gives the session that page whole
    kowboy.py rules           repeats the rules at every message
    kowboy.py guard           holds a dangerous action for the operator's yes
    kowboy.py reply           sends back a reply without its status line, or one
                              that waits for the operator without a numbered question

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
        "the package's skills.\n\n"
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


def the_rules():
    text = page("HANDBOOK.md")
    match = re.search(r"^## The rules\n(.*?)(?=^## )", text, re.S | re.M)
    if not match:
        raise SystemExit("HANDBOOK.md has no '## The rules' section")
    return match.group(1).strip()


def rules(_event):
    answer(
        "UserPromptSubmit",
        additionalContext="The Kowboy rules, repeated at every message:\n\n" + the_rules(),
    )


# --- guard ------------------------------------------------------------------

RULE = {
    1: "rule 1, never destroy anything you cannot bring back yourself",
    2: "rule 2, never change production",
    5: "rule 5, never change the rules agents work by",
    7: "rule 7, never change, send, spend or pay for anything outside the repository",
}

# (rule, what it is, pattern) checked against each simple command, from its first word.
COMMANDS = [
    (1, "overwriting history on GitHub", r"^git\s+push\b.*(\s--force\b|\s--force-with-lease\b|\s-f\b|\s\+\S)"),
    (1, "deleting on GitHub", r"^git\s+push\b.*(\s--delete\b|\s-d\b|\s:\S)"),
    (1, "deleting on GitHub", r"^gh\s+(repo|release)\s+delete\b"),
    (1, "dropping or emptying a database", r"^(dropdb|mysqladmin\s.*\bdrop)\b"),
    (1, "dropping or emptying a database", r"^redis-cli\b.*\bflush(all|db)\b"),
    (1, "dropping or emptying a database", r"^(rails|rake|bin/rails)\s+db:(drop|reset|purge)\b"),
    (1, "dropping or emptying a database", r"^(prisma\s+migrate\s+reset|wp\s+db\s+(drop|reset|clean))\b"),
    (1, "deleting in a cloud account", r"^(aws|doctl|gcloud|az|heroku)\b.*([\s:-](delete|destroy|rm|rb)(\s|$)|(delete|terminate|remove|destroy)-\S+)"),
    (1, "deleting with kubectl or terraform", r"^(kubectl\s+delete|terraform\s+destroy)\b"),
    (2, "logging in to a server", r"^(ssh|scp|sftp)(\s|$)"),
    (2, "copying to a server", r"^rsync\b.*\s[\w.@-]+:\S*"),
    (2, "deploying", r"^(vercel|netlify)\b.*\s--prod\b"),
    (2, "deploying", r"^(fly|flyctl|firebase|serverless|sls|eb)\s+deploy\b"),
    (2, "deploying", r"^wrangler\s+(pages\s+)?(deploy|publish)\b"),
    (2, "deploying", r"^gcloud\s+(app|run|functions)\s+deploy\b"),
    (2, "deploying", r"^(kubectl\s+apply|terraform\s+apply|helm\s+(install|upgrade)|cap\s+\S+\s+deploy)\b"),
    (7, "sending mail", r"^(sendmail|mail|mailx)(\s|$)|^aws\s+sesv?2?\s+send"),
    (7, "starting an agent as a separate program", r"^(claude|@anthropic-ai/claude-code)\b.*\s(-p|--print)(\s|$)"),
]

# Database clients: their arguments are read as database statements.
DB_CLIENTS = {"psql", "mysql", "mariadb", "sqlite3", "mongosh", "mongo", "sqlcmd", "clickhouse-client"}
SQL = [
    (r"\b(drop\s+(table|database|schema|collection)|truncate\s+(table\s+)?\w)", "dropping or emptying a database"),
    (r"\bdelete\s+from\s+[\w.\"`]+\s*(;|$)", "deleting every row of a table"),
    (r"\.drop(database)?\(", "dropping or emptying a database"),
]

# Commands that only show text; nothing they name is acted on.
TEXT_ONLY = {"grep", "rg", "ag", "echo", "printf", "cat", "less", "head", "tail", "awk", "jq", "sed", "which", "type"}
SHELLS = {"bash", "sh", "zsh", "dash"}
PREFIXES = {"sudo", "env", "time", "nohup", "exec", "command", "npx", "bunx"}
TWO_WORD_PREFIXES = {("pnpm", "dlx"), ("yarn", "dlx"), ("npm", "exec")}
SEPARATORS = re.compile(r"^[;&|()`\n]+$")
REDIRECTS = {">", ">>", ">|", "&>", "&>>"}
TEMP_DIRS = {Path("/tmp").resolve(), Path(tempfile.gettempdir()).resolve()}
URLISH = re.compile(r"^(https?://|[\w-]+(\.[\w-]+)+(:\d+)?(/|$))")
LOCAL_HOSTS = re.compile(r"^(https?://)?(localhost|127\.0\.0\.1|0\.0\.0\.0|\[::1\])([:/]|$)")
WRITE_FLAGS = re.compile(r"^(-d|--data\S*|-F|--form\S*|-T|--upload-file|--json)$")
WRITE_METHOD = re.compile(r"^(-X|--request)(=?)(POST|PUT|PATCH|DELETE)?$", re.I)
HEREDOC = re.compile(r"^([^\n]*?)<<-?\s*(['\"]?)([\w-]+)\2([^\n]*)\n(.*?)\n?^[ \t]*\3[ \t]*$", re.S | re.M)

RULE_FILES = {"CLAUDE.md", "CLAUDE.local.md", "AGENTS.md"}
CLAUDE_DIR_RULES = re.compile(r"^(settings[^/]*\.json|(hooks|agents|skills|commands|rules)/.*)$")
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
# Writes the platform already asks about every time, or that are the session's own work.
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
# GitHub is where the repository's own work is saved; only writes beyond it are held.
GITHUB_HOLD_TOOLS = {"mcp__github__create_repository", "mcp__github__fork_repository"}


def unfold_heredoc(match):
    """A heredoc's text runs as commands for a shell, as statements for a database
    client, and is only text for anything else."""
    line = match.group(1) + match.group(4)
    names = {Path(w).name for w in line.split()}
    if names & SHELLS:
        return line + "\n" + match.group(5)
    if names & DB_CLIENTS:
        return line + " " + shlex.quote(match.group(5))
    return line


def simple_commands(command):
    """Split a shell command line into its simple commands, as lists of words."""
    command = HEREDOC.sub(unfold_heredoc, command)
    lexer = shlex.shlex(command, posix=True, punctuation_chars=";&|()<>`\n")
    lexer.whitespace = " \t\r"
    lexer.whitespace_split = True
    words = []
    for token in list(lexer) + [";"]:
        if SEPARATORS.match(token) and token not in REDIRECTS:
            words = strip_prefixes(words)
            if words:
                yield words
            words = []
        elif token != "$":
            words.append(token)


def strip_prefixes(words):
    while words:
        if words[0] == "command" and words[1:2] in (["-v"], ["-V"]):
            return ["which", *words[2:]]
        if re.match(r"^\w+=", words[0]):
            words = words[1:]
        elif words[0] in PREFIXES:
            words = words[1:]
            while words and words[0].startswith("-"):
                takes_value = words[0] in ("-u", "-g", "-C", "-p")
                words = words[2:] if takes_value else words[1:]
        elif tuple(words[:2]) in TWO_WORD_PREFIXES:
            words = words[2:]
            while words and words[0].startswith("-"):
                words = words[1:]
        else:
            return words
    return words


def inside(path, folder):
    try:
        path.relative_to(folder)
        return True
    except ValueError:
        return False


def resolve(target, current):
    if target.startswith("~") or "$" in target:
        return Path.home()
    return (current / target).resolve()


def hold_rm(args, current, cwd):
    flags = "".join(w[1:] for w in args[1:] if w.startswith("-") and not w.startswith("--"))
    if "r" not in flags.lower() and "--recursive" not in args:
        return None
    for target in (w for w in args[1:] if not w.startswith("-")):
        if target.startswith("~") or "$" in target:
            return "deleting outside the working folder"
        path = resolve(target, current)
        in_temp = any(inside(path, folder) and path != folder for folder in TEMP_DIRS)
        if not in_temp and (path == cwd or not inside(path, cwd)):
            return "deleting the working folder or something outside it"
    return None


def hold_web_write(args):
    if args[0] not in ("curl", "wget", "http", "https", "xh"):
        return None
    urls = [w for w in args[1:] if URLISH.match(w) or LOCAL_HOSTS.match(w)]
    if urls and all(LOCAL_HOSTS.match(u) for u in urls):
        return None
    for i, word in enumerate(args[1:], 1):
        method = WRITE_METHOD.match(word)
        if method:
            value = method.group(3) or (args[i + 1] if i + 1 < len(args) else "")
            if value.upper() in ("POST", "PUT", "PATCH", "DELETE"):
                return "sending or changing data on a server"
        if WRITE_FLAGS.match(word) or word.startswith("--post-"):
            return "sending or changing data on a server"
        if args[0] in ("http", "https", "xh") and word.upper() in ("POST", "PUT", "PATCH", "DELETE"):
            return "sending or changing data on a server"
    return None


def rule_file_reason(target, current):
    if not isinstance(target, str):
        raise TypeError("the file path is not text")
    path = Path(os.path.expandvars(target)).expanduser()
    path = (path if path.is_absolute() else current / path).resolve()
    if path.name in RULE_FILES:
        return "editing agents' rule files"
    parts = path.parts
    if ".claude" in parts:
        below = "/".join(parts[len(parts) - parts[::-1].index(".claude"):])
        if CLAUDE_DIR_RULES.match(below):
            return "editing agents' rule files"
    for folder in [path.parent, *path.parent.parents]:
        if (folder / ".claude-plugin" / "plugin.json").is_file():
            relative = path.relative_to(folder).as_posix()
            if relative in HANDBOOK_FILES or relative.startswith(PACKAGE_DIRS):
                return "editing the handbook or the Kowboy package"
            break
    return None


def written_files(words):
    """The files a simple command writes to, as far as its words show."""
    files = [words[i + 1] for i, w in enumerate(words[:-1]) if w in REDIRECTS]
    name = Path(words[0]).name
    args = [w for w in words[1:] if not w.startswith("-")]
    if name == "tee":
        files += args
    elif name == "sed" and any(w.startswith("-i") or w == "--in-place" for w in words[1:]):
        files += args[1:]
    elif name in ("cp", "mv", "ln", "install") and args:
        files.append(args[-1])
    elif name in ("curl", "wget"):
        for i, w in enumerate(words):
            if re.match(r"^-[a-zA-Z]*[oO]$|^--output(-document)?$", w) and i + 1 < len(words):
                files.append(words[i + 1])
            elif w.startswith(("--output=", "--output-document=")):
                files.append(w.split("=", 1)[1])
    return files


def bash_reason(command, cwd):
    if not isinstance(command, str):
        raise TypeError("the command is not text")
    current = cwd
    for words in simple_commands(command):
        name = Path(words[0]).name
        for target in written_files(words):
            if rule_file_reason(target, current):
                return 5, rule_file_reason(target, current)
        if name in ("cd", "pushd"):
            current = resolve(words[1], current) if len(words) > 1 else Path.home()
            continue
        if name in TEXT_ONLY:
            continue
        args = [w for i, w in enumerate(words) if w not in REDIRECTS and (i == 0 or words[i - 1] not in REDIRECTS)]
        line = " ".join(args)
        for rule, what, pattern in COMMANDS:
            if re.search(pattern, line, re.I):
                return rule, what
        if {Path(w).name for w in args} & DB_CLIENTS:
            for pattern, what in SQL:
                if re.search(pattern, line, re.I):
                    return 1, what
        if name == "rm":
            what = hold_rm(args, current, cwd)
            if what:
                return 1, what
        what = hold_web_write(args)
        if what:
            return 7, what
    return None


def mcp_reason(tool):
    if tool in PASS_TOOLS or tool.startswith("mcp__github__") and tool not in GITHUB_HOLD_TOOLS:
        return None
    words = set(re.split(r"[_\-]", tool.split("__", 2)[-1].lower()))
    if tool in GITHUB_HOLD_TOOLS or words & WRITE_WORDS or not words & READ_WORDS:
        return 7, "writing through a connected service"
    return None


def guard_reason(event):
    if "unreadable" in event:
        raise ValueError("the platform's message was not readable")
    tool = event.get("tool_name", "")
    data = event.get("tool_input") or {}
    if not isinstance(data, dict) or not isinstance(tool, str):
        raise TypeError("the action's details are not readable")
    cwd = Path(event.get("cwd") or os.getcwd()).resolve()
    if tool == "Bash":
        return bash_reason(data.get("command", ""), cwd)
    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        what = rule_file_reason(data.get("file_path") or data.get("notebook_path") or "", cwd)
        return (5, what) if what else None
    if tool.startswith("mcp__"):
        return mcp_reason(tool)
    return None


def guard(event):
    try:
        found = guard_reason(event)
        if not found:
            return
        rule, what = found
        why = f"{what} ({RULE[rule]})"
    except Exception as error:  # an unreadable action is asked about, never let through
        why = f"it could not read this action ({error})"
    answer(
        "PreToolUse",
        permissionDecision="ask",
        permissionDecisionReason=f"Kowboy package: {why}. Allow only if you asked for exactly this step.",
    )


# --- reply ------------------------------------------------------------------

STATES = ("Working", "Waiting for you", "Waiting for something else", "Done")


def first_line(text):
    for line in text.splitlines():
        line = re.sub(r"^[\s#>*_\-]+", "", line).replace("**", "").replace("__", "").strip()
        if line:
            return line
    return ""


def status(text):
    """The state after 'Status:' on the first line, or None."""
    line = first_line(text)
    match = re.match(r"Status:\s*(.*)", line)
    rest = match.group(1) if match else line
    return next((s for s in sorted(STATES, key=len, reverse=True) if rest.startswith(s)), None)


def numbers(text):
    """Question numbers: a line that starts with a number and a colon, as '64: Merge?'."""
    return set(re.findall(r"(?m)^[\s>*_\-]*(?:\*\*)?(\d+)(?:\*\*)?:", text))


def reply(event):
    if not isinstance(event, dict) or event.get("stop_hook_active"):
        return
    text = event.get("last_assistant_message")
    if not isinstance(text, str) or not text.strip():
        return
    state = status(text)
    if state is None:
        reason = (
            "Start the reply with the status line: 'Status: Working', 'Status: Waiting for "
            "you', 'Status: Waiting for something else' or 'Status: Done' (HANDBOOK.md, How to "
            "reply)."
        )
    elif state == "Waiting for you" and not numbers(text):
        reason = (
            "A reply that waits for the operator asks numbered questions, each written with "
            "its number from the question log and a colon, as '64: Merge into main?'."
        )
    else:
        return
    print(json.dumps({"decision": "block", "reason": "Kowboy package: " + reason}))


if __name__ == "__main__":
    raw = sys.stdin.read()
    try:
        incoming = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        incoming = {"unreadable": raw}
    if not isinstance(incoming, dict):
        incoming = {"unreadable": incoming}
    entry = sys.argv[1]
    if entry == "session-start":
        session_start(sys.argv[2])
    else:
        {"rules": rules, "guard": guard, "reply": reply}[entry](incoming)
