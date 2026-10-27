#!/usr/bin/env python3
"""Turn a Word file made by build_docx.py back into its Markdown source, so it can be updated.

Usage:
    python docx_to_md.py FILE.docx [--out FILE.md] [--force]

Images are saved in a FILE_images folder next to the Markdown file. Changes made by hand
in Word come through as long as they use the document's own styles.
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_docx import COVER_FIELDS, DOC_TYPES  # noqa: E402  (also checks python-docx is installed)

from docx import Document  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.table import Table  # noqa: E402
from docx.text.paragraph import Paragraph  # noqa: E402

MONO_FONTS = {"Consolas", "Courier New"}
LABEL_TO_KEY = dict(COVER_FIELDS)
FRONT_KEYS = ("type", "title", "project", "project_code", "client", "version", "status", "date",
              "prepared_by", "reviewed_by", "approved_by", "classification")
BULLET_STYLES = {"List Bullet": 0, "List Bullet 2": 1, "List Bullet 3": 2}
NUMBER_STYLES = {"Numbered Item": 0, "Numbered Item 2": 1, "Numbered Item 3": 2}


def body_items(doc):
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, doc)
        elif child.tag == qn("w:tbl"):
            yield Table(child, doc)


def style_name(par):
    return par.style.name if par.style is not None else "Normal"


def wrap(text, bold, italic, mono):
    core = text.strip()
    if not core:
        return text
    if mono:
        core = f"`{core}`"
    if italic:
        core = f"*{core}*"
    if bold:
        core = f"**{core}**"
    return text[: len(text) - len(text.lstrip())] + core + text[len(text.rstrip()):]


def inline_md(par):
    pieces = []
    content = par.iter_inner_content() if hasattr(par, "iter_inner_content") else par.runs
    for item in content:
        if hasattr(item, "url"):  # a hyperlink (python-docx 1.0 and later)
            if item.text:
                pieces.append(("link", f"[{item.text}]({item.url})"))
        elif item.text:
            fmt = (bool(item.bold), bool(item.italic), (item.font.name or "") in MONO_FONTS)
            if pieces and pieces[-1][0] == fmt:
                pieces[-1] = (fmt, pieces[-1][1] + item.text)
            else:
                pieces.append((fmt, item.text))
    text = "".join(t if fmt == "link" else wrap(t, *fmt) for fmt, t in pieces)
    return text.replace("\n", "<br>")


def table_md(table):
    rows = []
    for i, row in enumerate(table.rows):
        cells = []
        for cell in row.cells:
            parts = [p.text.strip() if i == 0 else inline_md(p).strip() for p in cell.paragraphs]
            cells.append("<br>".join(x for x in parts if x).replace("\n", "<br>").replace("|", "\\|"))
        rows.append(cells)
    lines = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * len(rows[0])]
    return "\n".join(lines + ["| " + " | ".join(r) + " |" for r in rows[1:]])


def read_front(items):
    """Recover the front matter from the cover table, title and revision table."""
    meta, revisions, title, in_revisions = {}, [], None, False
    for it in items:
        if isinstance(it, Paragraph):
            name = style_name(it)
            if name == "Title":
                title = it.text.strip()
            elif name == "Front Heading":
                in_revisions = it.text.strip().lower() == "revision history"
        elif in_revisions:
            revisions = [[c.text.strip().replace("\n", " ") for c in r.cells] for r in it.rows][1:]
            in_revisions = False
        elif not meta:
            for r in it.rows:
                cells = [c.text.strip() for c in r.cells]
                if len(cells) >= 2 and cells[0] in LABEL_TO_KEY:
                    meta[LABEL_TO_KEY[cells[0]]] = cells[1].replace("\n", " ")
    m = re.search(r"\((\w+)\)\s*$", meta.pop("type_label", ""))
    if m:
        meta["type"] = m.group(1)
    if title and title != DOC_TYPES.get(meta.get("type"), ("",))[0]:
        meta["title"] = title
    return meta, [r for r in revisions if any(r)]


def convert(docx_path, md_path):
    doc = Document(str(docx_path))
    items = list(body_items(doc))
    start = next((i for i, it in enumerate(items)
                  if isinstance(it, Paragraph) and style_name(it) == "Heading 1"), len(items))
    meta, revisions = read_front(items[:start])

    img_dir = md_path.with_name(md_path.stem + "_images")
    out, figures, i, first = [], 0, start, True
    while i < len(items):
        it = items[i]
        i += 1
        if isinstance(it, Table):
            out.append(("block", table_md(it)))
            first = False
            continue
        name = style_name(it)
        if it.paragraph_format.page_break_before and not first:
            out.append(("block", "\\newpage"))
        first = False
        text = inline_md(it).strip()
        blips = it._p.xpath(".//a:blip/@r:embed")
        if blips:
            part = doc.part.related_parts[blips[0]]
            figures += 1
            img_dir.mkdir(exist_ok=True)
            img = img_dir / f"figure-{figures}{Path(str(part.partname)).suffix or '.png'}"
            img.write_bytes(part.blob)
            alt = ""
            if i < len(items) and isinstance(items[i], Paragraph) and style_name(items[i]) == "Caption":
                alt = re.sub(r"^Figure \d+:\s*", "", items[i].text.strip())
                i += 1
            out.append(("block", f"![{alt}]({img_dir.name}/{img.name})"))
        elif not text or name == "Spacer":
            continue
        elif name.startswith("Heading "):
            level = name.split()[1]
            out.append(("block", "#" * (min(int(level), 4) if level.isdigit() else 4) + " " + it.text.strip()))
        elif name in BULLET_STYLES:
            out.append(("list", "  " * BULLET_STYLES[name] + "- " + text))
        elif name in NUMBER_STYLES:
            m = re.match(r"(\d+)\.\s*(.*)", text, re.S)
            num, body = (m.group(1), m.group(2)) if m else ("1", text)
            out.append(("list", "  " * NUMBER_STYLES[name] + f"{num}. {body}"))
        elif name == "Checklist":
            out.append(("list", f"- [{'x' if text[0] in '☑☒' else ' '}] {text[1:].strip()}"))
        elif name == "Code Block":
            out.append(("block", "```\n" + it.text + "\n```"))
        elif name == "Note":
            out.append(("block", "> " + text))
        else:
            out.append(("block", text))

    lines = ["---"]
    if not meta.get("project"):
        lines.append("# This file wasn't made by the Panasa builder: fill in every field below.")
    for key in FRONT_KEYS:
        if key in meta or key != "title":
            lines.append(f"{key}: {meta.get(key) or '<' + key + '>'}")
    for r in revisions:
        lines.append("revision: " + " | ".join((r + [""] * 4)[:4]))
    lines += ["---", ""]
    prev_list = False
    for kind, text in out:
        if lines[-1] != "" and not (kind == "list" and prev_list):
            lines.append("")
        lines.append(text)
        prev_list = kind == "list"
    with open(md_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines).rstrip() + "\n")
    return figures, img_dir


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Convert a Panasa Word document back to its Markdown source.")
    ap.add_argument("docx", help="Word file made by build_docx.py")
    ap.add_argument("--out", help="Markdown file to write (default: next to the .docx)")
    ap.add_argument("--force", action="store_true", help="overwrite an existing Markdown file")
    args = ap.parse_args()

    src = Path(args.docx).resolve()
    if not src.is_file():
        print(f"ERROR: {src} not found.")
        return 1
    md = Path(args.out).resolve() if args.out else src.with_suffix(".md")
    if md.exists() and not args.force:
        print(f"ERROR: {md} already exists. If it is the document's source, edit it instead; "
              "otherwise pass --force to overwrite it.")
        return 1
    figures, img_dir = convert(src, md)
    print(f"Wrote {md}" + (f" and {figures} image(s) in {img_dir}" if figures else ""))
    print("Next: make the changes, raise the version, add a revision line, then run build_docx.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
