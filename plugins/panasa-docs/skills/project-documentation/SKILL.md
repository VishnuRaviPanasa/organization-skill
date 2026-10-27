---
name: project-documentation
description: Creates and updates Panasa's standard project documents as branded Word (.docx) files - Project Overview (OVR), Software Requirements Specification (SRS), Technical Design Document (TDD) and Release and Handover Note (RHN). Use whenever someone asks to write, draft, update, version or review project documentation, including a project overview or summary, requirements (SRS, BRD, FRD), a technical or architecture design, release notes, deployment notes or a client handover document, and when they ask for a blank Panasa document template. Use it even if they don't mention the standard or name the document type.
---

# Panasa project documentation

Every Panasa project document follows one of four standard structures and is delivered as a branded Word file. Paths in this file are relative to the folder that contains this SKILL.md.

| Code | Document | Template | Covers |
|---|---|---|---|
| OVR | Project Overview | `templates/overview.md` | Purpose, people, scope, timeline, stack, environments, links, risks |
| SRS | Software Requirements Specification | `templates/srs.md` | What the system must do, as numbered, testable requirements. Also use for BRD and FRD requests |
| TDD | Technical Design Document | `templates/technical-design.md` | How it is built: architecture, modules, data, APIs, security, deployment, decisions |
| RHN | Release and Handover Note | `templates/release-handover.md` | One release: changes, deployment and rollback, configuration, tests, client handover |

A request for another kind of document (user manual, test plan, proposal) is outside the standard. Say so, and offer the closest type or a document without the standard.

## Writing a new document

1. **Pick the type** from the table. Ask only if the request really fits two types.
2. **Gather facts** from everything available: files and notes the user shared, tickets, earlier documents and, in a code repository, the code itself (build files, configuration, CI pipelines, README, API routes, database migrations). Then ask the user, in one message, only for essentials you could not find: project name and code, client, author, and facts whole sections depend on. Don't hold the document back for smaller gaps.
3. **Read** `reference/style-guide.md` and the template for the type.
4. **Write the source file.** Copy the template to `<PROJECTCODE>_<TYPE>_v<version>.md` (for example `NIRVANA_SRS_v0.1.md`) and fill it in:
   - Keep every top-level (`#`) section, with its number and title unchanged, in the template's order. If one doesn't apply, keep it and write one sentence saying why, such as "Not applicable: the app has no third-party integrations." Extra material goes in a `##` sub-section or at the end as `# Appendix A: <title>`.
   - The template's `##` sub-sections are the recommended layout. Add, remove or repeat them as the content needs.
   - Replace every `<placeholder>`, and delete example rows you don't use.
   - `<!-- comments -->` are guidance for you. They never appear in the Word file.
   - Never invent facts, names, dates, figures or URLs. Write `TBD (owner: <name or role>)` instead; the Word file highlights it.
   - Never write passwords, keys or tokens. Say where they are kept instead.
5. **Build** with `python scripts/build_docx.py <source>.md` (use `python3` where `python` isn't found). It checks the structure and metadata, flags placeholders, possible secrets and TBDs, and writes `<PROJECTCODE>_<TYPE>_v<version>.docx` next to the source. Use `--out <folder>` to write it elsewhere, such as the folder the user downloads files from. If it reports errors, nothing is written: fix the source and run it again. If python-docx is missing, run `pip install python-docx` first.
6. **Hand over** the .docx and tell the user:
   - every TBD item and its owner (the builder lists them);
   - any warning you couldn't resolve;
   - that Word asks to update fields when the file is first opened, and answering **Yes** fills in the table of contents.

   In a code repository, keep the `.md` source in `docs/` next to the .docx so the next update starts from it.

## Updating a document

1. Start from the `.md` source if there is one. Otherwise convert the latest .docx with `python scripts/docx_to_md.py <file>.docx`, which writes `<file>.md` and saves its images in a folder beside it.
2. Make the changes, then update the front matter: raise `version` (0.1 → 0.2 while in draft, 1.0 at approval, then 1.1, 1.2 and so on), set `date` and `status`, and add a `revision:` line saying what changed.
3. Build and hand over as above. Each version gets its own file; never overwrite the previous version's file.

## Status

`Draft` → `In review` → `Approved`. Set `Approved` only when the user confirms sign-off. An approved document needs version 1.0 or higher and a name in `approved_by`.

## Blank templates

If someone wants a blank template to fill in by hand in Word, build the template itself: `python scripts/build_docx.py templates/srs.md --blank --out <folder>`.

## Source format

The builder understands this Markdown and nothing more:

- Front matter between `---` lines: `key: value` lines, plus one `revision: version | date | author | changes` line per version, oldest first.
- Headings `#` to `####`.
- Paragraphs with `**bold**`, `*italic*`, `` `code` `` and `[link text](https://...)`.
- Bullets (`- `) and numbered items (`1. `), nested by indenting two spaces; checklists `- [ ]` and `- [x]`.
- Pipe tables with a header row; `<br>` makes a line break inside a cell.
- Fenced code blocks, notes (`> `), images `![Caption](path/to/image.png)` (PNG or JPG, numbered as figures automatically), and `\newpage` on its own line for a page break.
