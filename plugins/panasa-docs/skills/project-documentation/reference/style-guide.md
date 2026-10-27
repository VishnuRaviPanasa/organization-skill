# Panasa documentation style guide

## Language

- Plain, direct English in short sentences and the active voice: "The app sends a reminder", not "A reminder is sent by the app".
- British spelling: organisation, colour, licence (noun), authorise.
- Write for someone who joins the project tomorrow. Spell out an abbreviation the first time it appears, and add it to the glossary (SRS section 1.3).
- No marketing language such as "seamless", "cutting-edge" or "robust".
- Headings in sentence case: "Data requirements", not "Data Requirements".
- Write product, company and people's names exactly as the client writes them.
- Put code, file names, commands and environment variable names in `code` format.

## Requirements (SRS)

- "shall" means mandatory, "should" means recommended, "may" means optional. Don't use "will" or "must" in requirements.
- One behaviour per requirement. If a requirement needs "and", consider splitting it.
- Every requirement has acceptance criteria a tester can check. Prefer "Given … when … then …".
- Replace vague words (fast, user-friendly, secure, scalable) with a number or a standard: "loads in under 2 seconds on a 4G connection".

## IDs

| Prefix | Used for | Document |
|---|---|---|
| FR-001 | Functional requirement | SRS |
| NFR-001 | Non-functional requirement | SRS |
| OQ-001 | Open question | SRS |
| DEC-001 | Design decision | TDD |
| RSK-001 | Risk | OVR, TDD |
| KI-001 | Known issue | RHN |

IDs have three digits and are never reused or renumbered, because other documents and tickets refer to them. A dropped requirement keeps its ID and gets "(Withdrawn)" after its title.

## Formatting

- Dates: 27 Oct 2026. Times with a time zone: 14:30 IST.
- Measurements in digits with a space before the unit: 500 ms, 2 GB.
- Money with the currency code first: INR 1,50,000 or USD 2,000.
- Tables for three or more comparable items, bullets for short lists, numbered lists only for steps that happen in order.
- Diagrams as PNG images, readable when printed at A4 width, each with a caption saying what it shows.

## Unknowns and gaps

- Unknown facts: `TBD (owner: name or role)`. Never guess.
- A section that doesn't apply stays in the document with one sentence explaining why.

## Confidentiality and security

- Never include passwords, API keys, tokens, private keys, signing keystores or one-time codes. Say where they are kept and who grants access.
- Personal data: only people's names, project roles and work email addresses. No personal phone numbers or identity numbers unless the client has agreed.
- Hide real customer data in screenshots.
- The classification is Confidential unless the front matter sets `classification:` to something else, such as Internal.

## Files and versions

- File name: `<PROJECTCODE>_<TYPE>_v<version>.docx`, for example `NIRVANA_SRS_v1.0.docx`. The project code is 2 to 12 capital letters or digits, agreed at project start, and the same in every document for that project.
- Versions: 0.1, 0.2 and so on for drafts; 1.0 when approved; 1.1, 1.2 and so on for changes after approval; 2.0 for a major rewrite.
- Status: Draft, then In review, then Approved.
- Every new version adds a revision line that says, in a few words, what changed.
