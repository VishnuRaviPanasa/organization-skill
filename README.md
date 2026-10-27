# Panasa Claude skills

Panasa's shared Claude skills. This repo is the single source for them: the Claude app gets a ZIP built from it, and Claude Code installs it directly as a plugin marketplace.

## Skills

**project-documentation** writes Panasa's standard project documents as branded Word files:

| Code | Document |
|---|---|
| OVR | Project Overview |
| SRS | Software Requirements Specification |
| TDD | Technical Design Document |
| RHN | Release and Handover Note |

Claude picks the skill up whenever someone asks for project documentation, for example "Write an SRS for the Nirvana loans module from these workshop notes" or "Update the FieldPulse handover note for release 2.4". In Claude Code you can also run `/panasa-docs:project-documentation`.

`samples/` has a finished example: [FIELDPULSE_SRS_v0.2.md](samples/FIELDPULSE_SRS_v0.2.md) and the Word file built from it. The project and client are fictional.

## Layout

```
.claude-plugin/marketplace.json        Claude Code marketplace listing
plugins/panasa-docs/
  .claude-plugin/plugin.json           plugin name and version
  skills/project-documentation/        the skill (this folder is what the ZIP contains)
    SKILL.md                           instructions Claude follows
    templates/                         section structure for each document type
    reference/style-guide.md           writing rules
    scripts/build_docx.py              checks a Markdown source and builds the Word file
    scripts/docx_to_md.py              turns a Word file back into its source for updates
    assets/brand.json                  company name, colours, fonts, confidentiality notice
    assets/panasa-template.docx        Word styles, header and footer (generated)
tools/make_template.py                 regenerates the Word template from brand.json and the logo
tools/package_skill.py                 checks the skill and builds dist/project-documentation.zip
samples/                               worked example
```

## Changing the standard

1. Make the change:
   - section structure: `templates/*.md`
   - writing rules: `reference/style-guide.md`
   - workflow: `SKILL.md`
   - branding: `assets/brand.json`, plus the logo as `assets/logo.png` (PNG with a transparent background, about 600 px wide). Then run `python tools/make_template.py`.
2. Run `python tools/package_skill.py`. It checks the skill, test-builds every template and writes `dist/project-documentation.zip`.
3. Raise `version` in `plugins/panasa-docs/.claude-plugin/plugin.json`, then open a pull request.
4. After merging, an Owner uploads the new ZIP to the Claude app (see below). Claude Code users get the update automatically.

Renaming, reordering or adding a top-level section changes the standard for everyone, and the builder rejects documents that don't match it. Agree such changes before merging.

Needs Python 3.9 or later and `pip install python-docx`.

## Making it available to everyone

### Claude app (claude.ai and the desktop app)

Needs a Team or Enterprise plan and the Owner role.

1. Organization settings → Plugins & skills → Policy: turn on **Cloud code execution and file creation** and **Skills**.
2. Add → Upload a skill → choose `dist/project-documentation.zip`.

Every member gets the skill, switched on by default. To release an update, upload the new ZIP the same way.

### Claude Code

1. Push this repo to Panasa's Git host. Every developer needs read access to it.
2. An Owner adds this to claude.ai → Organization settings → Claude Code → Managed settings. Replace `your-org` with the real organisation:

   ```json
   {
     "extraKnownMarketplaces": {
       "panasa": {
         "source": { "source": "github", "repo": "your-org/panasa-claude-skills" },
         "autoUpdate": true
       }
     },
     "enabledPlugins": { "panasa-docs@panasa": true }
   }
   ```

### Try it locally first

```
claude plugin marketplace add C:\path\to\panasa-claude-skills
claude plugin install panasa-docs@panasa
```
