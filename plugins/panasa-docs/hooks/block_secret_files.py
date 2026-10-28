#!/usr/bin/env python3
"""Claude Code PreToolUse hook for the panasa-docs plugin: never open files that usually hold secrets.

Denies Read and Grep on .env files, private keys, keystores and credential files, and shell commands that read
them. Listing file names is allowed, and so are sample files (.env.example, *.sample, *.template, *.dist).
Reads the hook event as JSON on stdin; prints a deny decision on stdout, or nothing to let the call proceed.
"""

import json
import re
import sys
from pathlib import PurePath

SECRET = re.compile(r"(?i)^(\.env(\.[\w.-]+)?|[\w.-]+\.(pem|key|p12|pfx|jks|keystore)|google-services\.json|"
                    r"googleservice-info\.plist|credentials[\w.-]*\.json|id_rsa[\w.-]*|id_ed25519[\w.-]*)$")
SAMPLE = re.compile(r"(?i)\.(example|sample|template|dist)$")
# Shell commands that would print or load a file's contents.
READERS = re.compile(r"(?i)(^|[\s;&|(])(cat|type|head|tail|less|more|grep|rg|sed|awk|strings|xxd|od|nl|cut|sort|bat|"
                     r"get-content|gc|select-string|source|python[\d.]*|py|node|perl|ruby)\b|open\(|<\s*\S")
# A name right after these flags is a search or exclude pattern (e.g. grep -v ".env"), not a file being read.
PATTERN_FLAGS = {"-v", "-e", "-E", "-F", "-name", "-iname", "-path", "-ipath", "-regex", "-not", "--exclude",
                 "--include", "--glob", "-g", "-notmatch", "-match", "-like", "-notlike", "-exclude", "-include", "-filter"}


def is_secret(path):
    name = PurePath(str(path).replace("\\", "/")).name
    return bool(SECRET.match(name)) and not SAMPLE.search(name)


def deny(what):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": (f"Blocked by Panasa policy: {what} usually holds secrets and must not be opened. "
                                     "Refer to it by name only, and tell the user it shouldn't be in a shared or "
                                     "committed folder and may need rotating."),
    }}))
    sys.exit(0)


def main():
    try:
        event = json.load(sys.stdin)
    except ValueError:
        sys.exit(0)
    tool, args = event.get("tool_name", ""), event.get("tool_input") or {}
    if tool == "Read" and is_secret(args.get("file_path", "")):
        deny(args["file_path"])
    if tool == "Grep":
        for key in ("path", "glob"):
            if args.get(key) and is_secret(args[key]):
                deny(args[key])
    if tool in ("Bash", "PowerShell"):
        command = args.get("command", "")
        tokens = re.findall(r"[^\s'\"|;&<>()]+", command)
        hits = [t for i, t in enumerate(tokens) if is_secret(t)
                and not re.fullmatch(r"\\+\.[\w.-]+", t)  # a regex pattern such as \.env, not a path
                and not (i and tokens[i - 1].lower() in {f.lower() for f in PATTERN_FLAGS})]
        if hits and READERS.search(command):
            deny(hits[0])
    sys.exit(0)


if __name__ == "__main__":
    main()
