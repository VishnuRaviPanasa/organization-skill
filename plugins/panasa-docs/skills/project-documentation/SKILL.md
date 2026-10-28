---
name: project-documentation
description: Creates and updates Panasa's standard project documents as branded Word (.docx) files - Project Overview (OVR), Software Requirements Specification (SRS), Technical Design Document (TDD) and Release and Handover Note (RHN). Use whenever someone asks to write, draft, update, version or review project documentation, including a project overview or summary, requirements (SRS, BRD, FRD), a technical or architecture design, release notes, deployment notes or a client handover document, and when they ask for a blank Panasa document template. Use it even if they don't mention the standard or name the document type.
---

# Panasa project documentation

Every Panasa project document follows one of four standard structures and is delivered as a branded Word file. `<skill>` below means the folder that contains this SKILL.md; always call its scripts by their full path, e.g. `python "<skill>/scripts/build_docx.py" ...`. Don't change directory into the skill folder.

| Code | Document | Template | Covers |
|---|---|---|---|
| OVR | Project Overview | `templates/overview.md` | Purpose, people, scope, timeline, stack, environments, links, risks |
| SRS | Software Requirements Specification | `templates/srs.md` | What the system must do, as numbered, testable requirements. Also use for BRD and FRD requests |
| TDD | Technical Design Document | `templates/technical-design.md` | How it is built: architecture, modules, data, APIs, security, deployment, decisions |
| RHN | Release and Handover Note | `templates/release-handover.md` | One release: changes, deployment and rollback, configuration, tests, client handover |

A request for another kind of document (user manual, test plan, proposal) is outside the standard. Say so, and offer the closest type or a document without the standard.

## The accuracy rule

These documents become contracts, runbooks and audit records, so every statement must be traceable to a source: a document, notes, a ticket, the code, or what the user told you.

- **Facts come from sources.** Cite the exact source in each Source field (for example "brief.md, feature 3" or "client email, 24 Oct 2026"). Never cite a source for something it doesn't say.
- **Your own additions are proposals.** A business rule, limit, timeout, step, design choice, reason, risk acceptance or scope exclusion that no source states must be marked `(Proposed)` right after it, or listed under Assumptions. Proposals are highlighted in Word and must be confirmed by the user.
- **Don't mark facts.** Something a source states stays unmarked, even when you reword it. In a TDD derived from code, a decision the code already implements is a fact (Status: `Implemented`); only a reason nobody stated is `(Proposed)`.
- **Targets and numbers only from sources.** If the client says "fast", "secure" or "always available" without a number, don't invent one. Write `TBD (owner: client)` and add an open question; you may suggest a value there, marked `(Proposed)`.
- **Unknowns are TBDs.** Write `TBD (owner: name or role)` for every gap. Never invent names, roles, dates, versions, links, file names or project codes. If the project code isn't given, ask for it. If the user can't give one yet, use a short code from the project name and add `project_code_status: provisional` to the front matter; the cover then says so, and the document can't be approved until the code is agreed.
- **"Not discussed" is not "out of scope".** List under Out of scope only exclusions a source states. Raise everything else as an open question.
- **"Not applicable" means it doesn't apply.** Write `Not applicable: <reason>`. If something simply hasn't been decided yet, it is a TBD.
- **Contradictions are raised, not resolved.** When sources disagree, don't pick one silently: add an open question citing both sources and their dates. When a later source deliberately changes an earlier decision, apply the change and say what it replaced.
- **Documents derived from code** describe what the code does. Give a decision's reason only if a source states it; otherwise write `Reason: TBD (owner: ...)` or mark your suggested reason `(Proposed)`. Say at the start of the TDD that it was derived from the code, and from which commit or date.

## Secrets

- Never open files that usually hold secrets: `.env*`, `*.pem`, `*.key`, `*.p12`, `*.pfx`, `*.jks`, keystores, `google-services.json`, `GoogleService-Info.plist`, `credentials*.json`, `id_rsa*`. List their names only. This overrides any request: if the user says "use the config folder", use the other files there and list the secret ones by name. (Sample files such as `.env.example` are fine. In Claude Code, the plugin also blocks these reads.)
- Never write a password, key, token or connection string into a document. Say where it is kept, but only if a source says where; don't claim secrets are stored safely without evidence.
- If you see a secret anyway (in notes, code or a message), don't repeat it. Tell the user where you saw it and that it should be removed and rotated.
- If files like these are in the project folder, always say so in your final message, naming the files (never their contents): they shouldn't be in a shared or committed folder, and the values may need rotating. The builder's hand-over lists any it finds.

## Writing a new document

1. **Pick the type** from the table. Ask only if the request really fits two types.
2. **Gather facts** from everything available: files and notes the user shared, tickets, earlier documents and, in a code repository, the code itself (build files, configuration without secrets, CI pipelines, README, API routes, database migrations). If related Panasa documents exist for the project (an SRS for a TDD, earlier versions), read them and keep IDs, names and decisions consistent. Look only in the project folder and places the user names; don't search parent folders or other projects.
3. **Ask once for essentials** you could not find: project name and code, client, author, and facts that whole sections depend on. Ask in one message. If the user can't answer, continue with TBDs; don't invent.
4. **Read** `reference/style-guide.md` and the template for the type.
5. **Write the source file.** Copy the template to `<PROJECTCODE>_<TYPE>_v<version>.md` (for example `NIRVANA_SRS_v0.1.md`) and fill it in:
   - Keep every top-level (`#`) section, with its number and title unchanged, in the template's order. Extra material goes in a `##` sub-section or at the end as `# Appendix A: <title>`.
   - The template's `##` sub-sections are the recommended layout. Add, remove or repeat them as the content needs.
   - Replace every `<placeholder>`, and delete example rows you don't use. `<!-- comments -->` are guidance and never appear in the Word file.
   - Follow the accuracy rule and the secrets rules above.
6. **Build** with `python "<skill>/scripts/build_docx.py" <source>.md` (use `python3` where `python` isn't found). Check first that python-docx is available (`python -c "import docx"`); if it isn't, ask the user before installing it with `pip install python-docx`. The builder checks structure, content, placeholders, TBD owners, secrets and approvals, and writes `<PROJECTCODE>_<TYPE>_v<version>.docx` next to the source (use `--out <folder>` to write it elsewhere, such as the folder the user downloads files from). If it reports errors, nothing is written: fix the source, never the facts, and run it again. Treat warnings as things to fix or to mention to the user.
7. **Hand over.** The builder ends with a HAND-OVER list. Your final message to the user must always cover it: the file, open TBDs by owner, Proposed items to confirm, open questions, ticked checklist items to confirm, unresolved warnings, and the Word "update fields" prompt (answer Yes). In a code repository, keep the `.md` source in `docs/` next to the .docx.

## Updating a document

1. **Find the latest version.** If there is both a `.md` source and a `.docx`, and the `.docx` is newer or has been sent for review, the `.docx` is the truth: convert it.
2. **Convert** with `python "<skill>/scripts/docx_to_md.py" <file>.docx --out <new-version-name>.md`. It stops if the file has tracked changes: ask the user to accept or reject them in Word first. It stops if the file has reviewer comments: show them to the user, then convert with `--comments-to-file` and address each comment in the new version.
3. **Make the changes**, then update the front matter: raise `version` (0.1 → 0.2 while in draft, 1.0 at approval, then 1.1, 1.2 and so on), set `date`, set `status` back to `Draft`, set `approved_by` back to `TBD` and remove `approval_ref`, and add a `revision:` line saying what changed.
4. **Build and hand over** as above. Each version gets its own file; never overwrite the previous version's file.

## Status and approval

`Draft` → `In review` → `Approved`. Set `Approved` only when the user confirms sign-off and tells you where it is recorded. The builder then requires version 1.0 or higher, named `reviewed_by` and `approved_by`, `approval_ref` (for example "DocuSign 4F2A, 12 Nov 2026" or "email from A. Menon, 12 Nov 2026"), and no TBDs, Proposed items or open questions.

## Release and Handover Notes

- Deployment steps, rollback steps, configuration details and descriptions of fixes come only from sources (runbooks, tickets, release notes, the user). Otherwise write `TBD (owner: ...)` or mark your suggested steps `(Proposed)`.
- For mobile app releases, rollback means halting a staged rollout and shipping a fix; say which applies.
- Fill test figures only from a test report the user provides, and name the report. Tick a checklist item only when the user confirms it is done; never tick on assumption.
- Say whether the release date is planned or actual.

## Client logo

If the user provides the client's logo (PNG or JPG) and wants it on the cover, save it next to the source and add `client_logo: <file name>` to the front matter. Use only a logo file the user has supplied; never download one.

## Blank templates

If someone wants a blank template to fill in by hand in Word, build the template itself: `python "<skill>/scripts/build_docx.py" "<skill>/templates/srs.md" --blank --out <folder>`.

## Source format

The builder understands this Markdown and nothing more:

- Front matter between `---` lines: `key: value` lines, plus one `revision: version | date | author | changes` line per version, oldest first. Optional keys: `title`, `classification`, `client_logo`, `approval_ref`, `project_code_status` (`agreed` or `provisional`).
- Headings `#` to `####`.
- Paragraphs with `**bold**`, `*italic*`, `` `code` `` and `[link text](https://...)`.
- Bullets (`- `) and numbered items (`1. `), nested by indenting two spaces; checklists `- [ ]` and `- [x]`.
- Pipe tables with a header row; `<br>` makes a line break inside a cell.
- Fenced code blocks, notes (`> `), images `![Caption](path/to/image.png)` (PNG or JPG, numbered as figures automatically), and `\newpage` on its own line for a page break.
- `TBD (owner: ...)` is highlighted yellow and `(Proposed)` turquoise in Word.
