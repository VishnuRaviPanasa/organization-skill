---
# Panasa Technical Design Document. Replace every <placeholder>; SKILL.md has the rules.
type: TDD
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
# Optional: logo: <company logo file the user uploaded>   client_logo: <client logo file the user uploaded>
# Optional: approval_ref: <where approval is recorded; only when Approved>
# Optional: project_code_status: provisional   (only when the client hasn't agreed the project code yet)
revision: 0.1 | <DD Mon YYYY> | <Author name> | First draft
---

# 1. Overview and goals

## 1.1 Purpose

<!-- If this design was derived from existing code rather than agreed in advance, add a sentence such as: "Derived from the code at commit <hash> on <date>; anything not yet confirmed is marked (Proposed)." -->

This document describes the design of <project name>. It implements the requirements in <SRS file name>.

## 1.2 Design goals

<!-- 3-6 goals that shaped the design, such as "works offline for up to 7 days". Refer to requirement IDs where they apply. -->

- <Goal>

## 1.3 Related documents

| Document | Version | Location |
|---|---|---|
| Software Requirements Specification | <Version> | <File name or URL> |

# 2. Architecture

## 2.1 Architecture diagram

<!-- A PNG showing the main components and how they communicate. If you can draw one (for example with Python and matplotlib, or Graphviz), embed it as below; a diagram you draw yourself is a proposal, so end its caption with "(Proposed)" until the tech lead confirms it. Otherwise delete the image line, describe the components in 2.2, and write "TBD (owner: tech lead)" here. -->

![<What the diagram shows>](<path/to/diagram.png>)

## 2.2 Components

| Component | Responsibility | Technology | Owner |
|---|---|---|---|
| <Component> | <What it does> | <Technology> | <Team or person> |

# 3. Module design

<!-- One sub-section per module or feature area. -->

## 3.1 <Module name>

- **Purpose:** <What it does>
- **Main parts:** <Key classes, packages or files>
- **Key flow:** <The main path, step by step>
- **Implements:** <FR-001, FR-002>

# 4. Data model

## 4.1 Entities

| Entity | Key fields | Relationships | Notes |
|---|---|---|---|
| <Entity> | <Fields> | <e.g. one customer has many accounts> | |

## 4.2 Storage

<!-- Databases, on-device storage, caches and files: where each runs and how it is backed up. -->

<Description>

# 5. APIs and integrations

| Method | Endpoint | Purpose | Authentication | Implements |
|---|---|---|---|---|
| <GET> | <e.g. /api/v1/accounts> | <Purpose> | <e.g. JWT> | <FR-001> |

# 6. Security

## 6.1 Authentication

<How users and services prove who they are>

## 6.2 Authorisation

<How permissions are enforced for each role>

## 6.3 Data protection

<!-- Encryption in transit and at rest, handling of personal data, what must never be logged. -->

<Description>

## 6.4 Secrets management

<!-- Where keys and passwords are kept and who can reach them, as stated by a source. Never the values, and never claim they are stored safely without evidence: write TBD (owner: ...) instead. -->

<Description>

# 7. Infrastructure and deployment

## 7.1 Environments

| Environment | Hosting | URL | Notes |
|---|---|---|---|
| <Environment> | <e.g. AWS ap-south-1> | <URL> | |

## 7.2 CI/CD pipeline

<!-- Every step from commit to production: build, tests, signing, approvals, release. -->

1. <Step>

## 7.3 Monitoring and logging

<Tools, alerts and who receives them>

# 8. Key design decisions

<!-- Decisions a newcomer would question. DEC IDs are never reused.
Record options and reasons only as a source states them. For a decision you can only see in the code, write the options and reason as TBD (owner: tech lead), or mark your suggestion (Proposed). Status is "Confirmed by <name>, <date>", "Implemented" (the code already does it) or "Proposed". An implemented decision is a fact; only an unstated reason for it is Proposed. -->

| ID | Decision | Options considered | Reason | Status | Date |
|---|---|---|---|---|---|
| DEC-001 | <Decision> | <Options from a source> | <Reason from a source> | <Confirmed by name, Implemented, or Proposed> | <DD Mon YYYY> |

# 9. Testing approach

| Level | Scope | Tools | Owner |
|---|---|---|---|
| Unit | <Scope> | <Tools> | <Owner> |
| Integration | <Scope> | <Tools> | <Owner> |
| UI and end-to-end | <Scope> | <Tools> | <Owner> |
| Performance | <Scope> | <Tools> | <Owner> |
| Security | <Scope> | <Tools> | <Owner> |
| User acceptance (UAT) | <Scope> | <Tools> | <Client name> |

# 10. Risks and trade-offs

| ID | Risk or trade-off | Impact | Mitigation |
|---|---|---|---|
| RSK-001 | <Description> | <High / Medium / Low> | <Mitigation> |
