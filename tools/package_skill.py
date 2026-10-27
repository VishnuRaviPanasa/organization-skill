#!/usr/bin/env python3
"""Check the skill and package it as a ZIP for the Claude app.

    python tools/package_skill.py

Writes dist/project-documentation.zip. An Owner uploads it in Claude:
Organization settings > Plugins & skills > Add > Upload a skill.
"""

import json
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PLUGIN = REPO / "plugins" / "panasa-docs"
SKILL = PLUGIN / "skills" / "project-documentation"
DIST = REPO / "dist"
# The Claude app rejects any other front matter key; Claude Code accepts more, but the skill must work in both.
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
REQUIRED_FILES = [
    "SKILL.md", "reference/style-guide.md", "assets/brand.json", "assets/panasa-template.docx",
    "scripts/build_docx.py", "scripts/docx_to_md.py", "templates/overview.md", "templates/srs.md",
    "templates/technical-design.md", "templates/release-handover.md",
]
SKIP_PARTS = {"__pycache__", ".DS_Store"}


def read_front_matter(text, problems):
    lines = text.split("\n")
    if lines[0].strip() != "---" or "---" not in [line.strip() for line in lines[1:]]:
        problems.append("SKILL.md must start with front matter between '---' lines.")
        return {}, 0
    end = [line.strip() for line in lines].index("---", 1)
    block = "\n".join(lines[1:end])
    try:
        import yaml
        front = yaml.safe_load(block) or {}
    except ImportError:
        front = dict(line.split(":", 1) for line in lines[1:end] if ":" in line and not line.startswith(" "))
        front = {k.strip(): v.strip() for k, v in front.items()}
    except Exception as exc:  # the Claude app parses this as YAML, so a YAML error blocks the upload
        problems.append(f"SKILL.md front matter isn't valid YAML: {exc}")
        return {}, 0
    return front, len(lines) - end - 1


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    problems = []
    front, body_lines = read_front_matter((SKILL / "SKILL.md").read_text(encoding="utf-8"), problems)

    extra = set(front) - ALLOWED_KEYS
    if extra:
        problems.append(f"SKILL.md keys the Claude app won't accept: {', '.join(sorted(extra))}")
    name = str(front.get("name", ""))
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name) or "claude" in name or "anthropic" in name:
        problems.append("name must be up to 64 lowercase letters, digits or hyphens, without 'claude' or 'anthropic'.")
    if name != SKILL.name:
        problems.append(f"name '{name}' must match the folder name '{SKILL.name}'.")
    description = str(front.get("description", ""))
    if not description or len(description) > 1024 or re.search(r"[<>]", description):
        problems.append(f"description must be 1-1024 characters with no < or > (it is {len(description)}).")
    if body_lines > 500:
        print(f"Note: SKILL.md body is {body_lines} lines; keep it under 500.")

    for rel in REQUIRED_FILES:
        if not (SKILL / rel).is_file():
            problems.append(f"Missing {rel}" + (" (run tools/make_template.py)" if rel.endswith(".docx") else ""))

    plugin = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    market = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    if plugin.get("name") not in [p.get("name") for p in market.get("plugins", [])]:
        problems.append("plugin.json name isn't listed in .claude-plugin/marketplace.json.")

    if not problems:  # every template must build as a blank document
        with tempfile.TemporaryDirectory() as tmp:
            for template in sorted((SKILL / "templates").glob("*.md")):
                result = subprocess.run(
                    [sys.executable, str(SKILL / "scripts" / "build_docx.py"), str(template), "--blank", "--out", tmp],
                    capture_output=True, text=True, encoding="utf-8")
                if result.returncode:
                    problems.append(f"templates/{template.name} doesn't build:\n{result.stdout}{result.stderr}")

    if problems:
        print("Not packaged:")
        for p in problems:
            print(f"  - {p}")
        return 1

    DIST.mkdir(exist_ok=True)
    zip_path = DIST / f"{name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(SKILL.rglob("*")):
            if f.is_file() and not SKIP_PARTS.intersection(f.parts) and f.suffix != ".pyc":
                zf.write(f, Path(name) / f.relative_to(SKILL))
    print(f"Packaged {zip_path} ({zip_path.stat().st_size // 1024} KB), plugin version {plugin.get('version', '?')}.")
    print("Upload it in Claude: Organization settings > Plugins & skills > Add > Upload a skill.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
