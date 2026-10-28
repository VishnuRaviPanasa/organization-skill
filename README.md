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

Every project gets its own details (name, code, client, version, author) on the cover, in the header and in the file name. Panasa's branding is the same everywhere. If the client hasn't agreed a project code yet, Claude uses a provisional one: the cover says so, and the document can't be approved until the code is agreed. There is no fixed logo: when Claude starts a document it asks whether you want logos on the cover. Upload your company's logo (shown on the cover and in the page header) and/or the client's logo (cover), as PNG or JPG, or skip it and the company name is shown instead. Updated versions keep the same logos.

In the Word file, open items are highlighted: `TBD (owner: ...)` in yellow, and anything Claude suggested that no source states, marked `(Proposed)`, in turquoise. Both must be resolved before a document can be marked Approved.

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
4. After merging, an Owner uploads the new ZIP to the Claude app (see below), which replaces the old version for everyone. If the console won't accept a skill with the same name, remove the old one first. Claude Code users get the update automatically because the version number went up.

Documents already produced aren't affected by an update. Each .docx records "Built with the Panasa project-documentation skill" in its properties.

Renaming, reordering or adding a top-level section changes the standard for everyone, and the builder rejects documents that don't match it. Agree such changes before merging.

Needs Python 3.9 or later and `pip install python-docx`.

## Making it available to everyone

### Claude app (claude.ai and the desktop app)

Needs a Team or Enterprise plan and the Owner role.

1. Organization settings → Plugins & skills → Policy: turn on **Cloud code execution and file creation** and **Skills**.
2. Add → Upload a skill → choose `dist/project-documentation.zip`.

Every member gets the skill, switched on by default. To release an update, upload the new ZIP the same way.

### Claude Code

1. The repo is `github.com/VishnuRaviPanasa/organization-skill` (public, so no access set-up is needed). Every developer needs Python 3 with `pip install python-docx` on their machine (the Claude app runs the scripts in its own environment). If the repo is made private later, every developer will also need read access and a GitHub sign-in through git.
2. An Owner adds this to claude.ai → Organization settings → Claude Code → Managed settings:

   ```json
   {
     "extraKnownMarketplaces": {
       "panasa": {
         "source": { "source": "github", "repo": "VishnuRaviPanasa/organization-skill" },
         "autoUpdate": true
       }
     },
     "enabledPlugins": { "panasa-docs@panasa": true }
   }
   ```

### Secret-file protection in Claude Code

The plugin includes a hook (`plugins/panasa-docs/hooks/`) that stops Claude from opening files that usually hold secrets: `.env*`, private keys (`*.pem`, `*.key`), keystores, `google-services.json`, `credentials*.json` and SSH keys. It blocks the Read and Grep tools and shell commands that print those files. Listing their names is allowed, and so are sample files such as `.env.example`.

The hook applies to **all** Claude Code work while the plugin is installed, not only documentation. That is deliberate Panasa policy. Developers who need Claude to read a real secrets file in a specific case must open it themselves. The hook needs Python 3; if Python isn't available, the hook does nothing.

### Try it locally first

```
claude plugin marketplace add C:\path\to\panasa-claude-skills
claude plugin install panasa-docs@panasa
```
