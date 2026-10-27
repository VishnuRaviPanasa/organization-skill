---
# Panasa Release and Handover Note. Replace every <placeholder>; SKILL.md has the rules.
type: RHN
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

# 1. Release summary

| Item | Detail |
|---|---|
| Release version | <e.g. 2.3.0> |
| Release date | <DD Mon YYYY> |
| Environment | <Production / Staging / UAT> |
| Platforms | <e.g. Android, iOS, Web> |
| Build or commit | <Build number or commit hash> |
| Release type | <Major / Minor / Patch / Hotfix> |

<!-- 2-3 sentences: what this release delivers and why it matters to the client. -->

<Summary paragraph>

# 2. Changes

<!-- Link every item to a ticket. If a sub-section has no items, write "None in this release." -->

## 2.1 New features

| Ticket | Description | Requirement |
|---|---|---|
| <Ticket ID> | <What users can now do> | <FR-001> |

## 2.2 Improvements

| Ticket | Description |
|---|---|
| <Ticket ID> | <What changed> |

## 2.3 Bug fixes

| Ticket | Description |
|---|---|
| <Ticket ID> | <What was wrong and is now fixed> |

# 3. Known issues and limitations

| ID | Issue | Impact | Workaround | Planned fix |
|---|---|---|---|---|
| KI-001 | <Issue> | <High / Medium / Low> | <Workaround, or None> | <Version or date> |

# 4. Deployment steps and rollback plan

## 4.1 Before deployment

- [ ] <Check, e.g. production database backed up>

## 4.2 Deployment steps

1. <Step>

## 4.3 Rollback plan

<!-- The exact steps to restore the previous version, and who decides to roll back. -->

1. <Step>

# 5. Configuration changes

## 5.1 Environment variables and settings

<!-- Names only. For secret values, say where they are stored. -->

| Name | Environment | Change | Notes |
|---|---|---|---|
| <VARIABLE_NAME> | <Environment> | <Added / Changed / Removed> | |

## 5.2 Database migrations

<Migrations to run, in order, or "None">

## 5.3 Third-party services

<Changes to external accounts, keys, quotas or webhooks, or "None">

# 6. Test summary

| Test type | Executed | Passed | Failed | Notes |
|---|---|---|---|---|
| <e.g. Regression> | <Number> | <Number> | <Number> | |

Full test report: <File name or URL>

# 7. Handover checklist

<!-- Tick only what is actually done. Delete lines that don't apply and add anything the contract requires. -->

- [ ] Source code delivered and repository access transferred
- [ ] Project Overview, SRS and Technical Design delivered at their latest versions
- [ ] Admin and store accounts transferred (e.g. Google Play Console, App Store Connect, cloud console)
- [ ] Credentials handed over through a secure channel, never by email or chat
- [ ] Signing keys handed over, or their custody agreed in writing
- [ ] Client team trained
- [ ] Support contacts shared

# 8. Support period and contacts

| Item | Detail |
|---|---|
| Support period | <DD Mon YYYY> to <DD Mon YYYY> |
| Response time | <e.g. Critical: 4 hours; others: 2 working days> |
| How to raise an issue | <Email, portal or tracker> |
| Panasa contact | <Name, role, email> |
| Client contact | <Name, role, email> |

# 9. Client acceptance sign-off

By signing below, the client confirms that release <release version> meets the agreed acceptance criteria.

| Name | Organisation | Role | Signature | Date |
|---|---|---|---|---|
| <Name> | <Client name> | <Role> | | |
| <Name> | Panasa | <Role> | | |
