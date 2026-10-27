---
# Panasa Software Requirements Specification. Replace every <placeholder>; SKILL.md has the rules.
type: SRS
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
revision: 0.1 | <DD Mon YYYY> | <Author name> | First draft
---

# 1. Introduction

## 1.1 Purpose

This document specifies the requirements for <project name> for <client name>. It is the agreed basis for design, development, testing and acceptance.

## 1.2 Scope

<!-- The product in 3-5 sentences: what it does, for whom, and on which platforms. -->

<Scope paragraph>

## 1.3 Definitions and abbreviations

| Term | Meaning |
|---|---|
| <Term> | <Meaning> |

## 1.4 References

| Document | Version | Location |
|---|---|---|
| <e.g. Project Overview> | <Version> | <File name or URL> |

# 2. Overall description

## 2.1 Product context

<!-- Where the product fits: whether it is new or replaces something, which systems it talks to, and how users reach it. -->

<Context paragraph>

## 2.2 User roles

| Role | Description | What they can do |
|---|---|---|
| <Role> | <Who they are> | <Main permissions> |

## 2.3 Assumptions

- <Assumption the requirements rely on>

## 2.4 Constraints

<!-- Fixed limits: platforms, regulations, deadlines, budget, mandated technology. -->

- <Constraint>

## 2.5 Dependencies

- <External system, team or decision the project depends on>

# 3. Functional requirements

<!-- Group requirements by module: 3.1, 3.2 and so on. Each requirement gets a level-3 heading "FR-001: <short title>".
IDs run through the whole document and are never reused or renumbered; a dropped requirement keeps its ID with "(Withdrawn)" after the title.
Write "The system shall ...". One behaviour per requirement. Priority is Must, Should or Could. -->

## 3.1 <Module name>

### FR-001: <Short title>

- **Priority:** <Must / Should / Could>
- **Description:** The system shall <behaviour>.
- **Acceptance criteria:**
  1. Given <context>, when <action>, then <expected result>.
- **Source:** <Workshop, ticket or person the requirement came from>

# 4. Non-functional requirements

<!-- Each one measurable. Categories: Performance, Security, Availability, Scalability, Usability, Accessibility, Compatibility, Compliance, Maintainability. -->

| ID | Category | Requirement | Target or measure |
|---|---|---|---|
| NFR-001 | <Category> | <The system shall ...> | <e.g. 95% of API calls answered within 500 ms> |

# 5. External interfaces

## 5.1 User interfaces

<!-- Platforms, screen sizes, languages, accessibility level, and where the designs are. -->

<Description>

## 5.2 APIs

| API | Direction | Purpose | Format and authentication |
|---|---|---|---|
| <API name> | <Inbound / Outbound> | <Purpose> | <e.g. REST and JSON, OAuth 2.0> |

## 5.3 Third-party integrations

| System | Purpose | Owned by | Notes |
|---|---|---|---|
| <e.g. Payment gateway> | <Purpose> | <Organisation> | |

# 6. Data requirements

<!-- The main business data, not database tables. Mark personal data, because it drives security and compliance work. -->

| Data | Description | Personal data | Retention |
|---|---|---|---|
| <e.g. Customer profile> | <What it holds> | <Yes / No> | <How long it is kept> |

# 7. Out of scope

<!-- Features someone might expect that this release will not deliver. -->

- <Item>

# 8. Open questions

| ID | Question | Raised by | Owner | Due date | Status |
|---|---|---|---|---|---|
| OQ-001 | <Question> | <Name> | <Name> | <DD Mon YYYY> | <Open / Answered> |

# 9. Sign-off

<!-- Leave Signature and Date empty; they are completed on paper or in an e-signature tool. -->

By signing below, the parties agree that this document describes the requirements for <project name>.

| Name | Organisation | Role | Signature | Date |
|---|---|---|---|---|
| <Name> | <Client name> | <Role> | | |
| <Name> | Panasa | <Role> | | |
