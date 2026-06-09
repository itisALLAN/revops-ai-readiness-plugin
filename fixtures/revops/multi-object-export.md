# Sample multi-object export (synthetic)

Stand-in for the multi-object CSV exports an operator gives the RevOps data-architecture
and handoff-integrity tool. Foreign keys link the objects. Deliberately seeded with:
an orphaned opportunity (no account), a broken lead→opportunity seam, a case on a
non-existent account, a duplicate account key, and a contact with no account.

## Accounts
| account_id | name | duplicate_of |
|---|---|---|
| ACC-01 | Northwind | |
| ACC-02 | Globex | |
| ACC-03 | Initech | |
| ACC-03b | Initech Inc | ACC-03 (duplicate key — same company, two records) |
| ACC-06 | Stark | |

## Contacts
| contact_id | name | account_id |
|---|---|---|
| CON-01 | Jordan Pike | ACC-01 |
| CON-02 | Sam Ortiz | ACC-01 |
| CON-03 | Lee Park | ACC-99 (account does not exist — broken FK) |
| CON-04 | Dana Liu | (blank — orphan contact, no account) |

## Leads (pre-conversion)
| lead_id | email | converted_opp_id |
|---|---|---|
| LD-4001 | a@northwind.test | OPP-2001 |
| LD-4003 | c@initech.test | OPP-9999 (points to an opportunity that does not exist — broken seam) |
| LD-4005 | e@soylent.test | (blank — MQL never converted, no opp, stuck 90+ days) |

## Opportunities
| opp_id | name | account_id | source_lead_id |
|---|---|---|---|
| OPP-2001 | Northwind - Platform | ACC-01 | LD-4001 |
| OPP-2003 | Initech - Renewal | ACC-03 | |
| OPP-2050 | Mystery Deal | (blank — orphan opp, no account) | |

## Cases
| case_id | subject | account_id |
|---|---|---|
| CS-1001 | Password reset | ACC-01 |
| CS-1011 | GDPR question | ACC-06 |
| CS-1099 | Unknown account case | ACC-77 (account does not exist — broken FK) |
