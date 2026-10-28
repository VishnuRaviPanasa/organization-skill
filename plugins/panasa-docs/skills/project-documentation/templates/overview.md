---
# Panasa Project Overview. Replace every <placeholder>; SKILL.md has the rules.
type: OVR
project: <Project name>
project_code: <PROJECTCODE>
client: <Client name>
version: 0.1
status: Draft
date: <DD Mon YYYY>
prepared_by: <Author name>
reviewed_by: TBD
approved_by: TBD
classification: Confidential
# Optional: client_logo: <logo file supplied by the client>   approval_ref: <where approval is recorded; only when Approved>
# Optional: project_code_status: provisional   (only when the client hasn't agreed the project code yet)
revision: 0.1 | <DD Mon YYYY> | <Author name> | First draft
---

# 1. Summary

<!-- 3-5 sentences for a reader who knows nothing about the project: what is being built, for whom, the business problem it solves, and the current phase. No technical detail. -->

<Summary paragraph>

# 2. Client and stakeholders

<!-- Everyone who decides, approves or is consulted, on both sides. Work email addresses only. -->

| Name | Organisation | Role | Responsibility | Email |
|---|---|---|---|---|
| <Name> | <Client name> | <Role, e.g. Product owner> | <What they decide or approve> | <Email> |
| <Name> | Panasa | Project manager | <Responsibility> | <Email> |
| <Name> | Panasa | Tech lead | <Responsibility> | <Email> |

# 3. Objectives and scope

## 3.1 Objectives

<!-- 3-6 measurable outcomes. "Cut loan approval time from 3 days to 1" beats "improve efficiency". -->

- <Objective>

## 3.2 In scope

- <Feature, platform or deliverable>

## 3.3 Out of scope

<!-- Anything a reader might assume is included but isn't, as agreed with the client or stated in a source. This prevents disputes later. Items that simply weren't discussed go to section 8 as open issues, not here. -->

- <Item>

# 4. Timeline and milestones

| Milestone | Target date | Status |
|---|---|---|
| <Milestone, e.g. UAT start> | <DD Mon YYYY> | <Planned / In progress / Done / At risk> |

# 5. Technology stack

<!-- Only what the project actually uses. Delete rows that don't apply. If the stack isn't decided yet, write TBD (owner: tech lead): "Not applicable" means it will never apply. -->

| Layer | Technology | Version | Notes |
|---|---|---|---|
| Mobile app | <e.g. Kotlin, Jetpack Compose> | <Version> | |
| Web front end | <Technology> | <Version> | |
| Back end | <Technology> | <Version> | |
| Database | <Technology> | <Version> | |
| Hosting | <e.g. AWS, Azure> | | |
| CI/CD | <Tool> | | |

# 6. Environments and access

## 6.1 Environments

| Environment | URL or location | Purpose | Access granted by |
|---|---|---|---|
| Development | <URL> | <Purpose> | <Name or role> |
| Staging | <URL> | <Purpose> | <Name or role> |
| Production | <URL> | <Purpose> | <Name or role> |

## 6.2 Source code

| Repository | URL | Main branch | Notes |
|---|---|---|---|
| <Repository name> | <URL> | <Branch> | |

## 6.3 Credentials

<!-- Where secrets are kept and who grants access. Never the secrets themselves. -->

Credentials are stored in <password manager or vault>. Request access from <name or role>.

# 7. Key links

| Item | Link |
|---|---|
| Task tracker | <URL> |
| Designs | <URL> |
| Requirements (SRS) | <File name or URL> |
| Technical design (TDD) | <File name or URL> |

# 8. Risks and open issues

<!-- Anything that could delay or derail the project. RSK IDs are never reused. -->

| ID | Risk or issue | Impact | Owner | Mitigation or next step |
|---|---|---|---|---|
| RSK-001 | <Description> | <High / Medium / Low> | <Name> | <Action> |
