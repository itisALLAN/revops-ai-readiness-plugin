# Logic layer — Data Architecture & Handoff Readiness (RevOps readiness)

**Purpose.** An AI agent that routes work — qualifying a lead, advancing an opportunity,
opening a case — has to trust the object graph. If the lead→opportunity→case spine has
orphans, dangling foreign keys, broken seams, or duplicate keys, the agent routes to the
wrong place or to nothing at all. This tool inspects multi-object exports and reports every
integrity defect with a concrete repair, so the graph is trustworthy before any AI touches it.

**Inputs (minimum).** Multi-object CRM exports with foreign keys intact:
- **Accounts** (account_id, name)
- **Contacts** (contact_id, account_id FK)
- **Leads** (lead_id, converted_opp_id FK)
- **Opportunities** (opp_id, account_id FK, source_lead_id FK)
- **Cases** (case_id, account_id FK)

No new system access. No credentials. Works on uploaded exports or the fixture.

## Named checks
- **FK-INTEGRITY** — For every foreign key, confirm the referenced parent record exists in
  the supplied parent object. A dangling FK (child points at a parent id not present) is a
  finding. Severity high — the AI follows a pointer to nothing.
- **ORPHAN-RECORD** — A child record with a blank/absent required parent FK (a contact with
  no account, an opportunity with no account). Severity high for opportunities (unroutable
  revenue), medium for contacts.
- **SEAM-INTEGRITY** — Trace the lead→opportunity→case handoff spine. A broken seam is a lead
  whose `converted_opp_id` points at an opportunity that does not exist (the conversion seam
  is severed). Severity high — the agent cannot follow the handoff a human believes happened.
- **DUPLICATE-KEY** — Two account (or other parent) records that represent the same real-world
  entity (same company, near-identical name, or an explicit `duplicate_of` marker). Severity
  high — the AI splits one customer across two identities and reasons over half the picture.

## What it emits (reflecting the seeded fixture)
- **OPP-2050** — orphaned opportunity, no account (ORPHAN-RECORD).
- **LD-4003 → OPP-9999** — broken lead→opportunity seam; the converted opportunity does not
  exist (SEAM-INTEGRITY).
- **ACC-03 / ACC-03b "Initech" vs "Initech Inc"** — duplicate account keys (DUPLICATE-KEY).
- **CON-03 → ACC-99** and **CS-1099 → ACC-77** — broken foreign keys to non-existent accounts
  (FK-INTEGRITY).
- **CON-04** — orphan contact, no account (ORPHAN-RECORD).

`summary.stats`: objects checked, broken FKs, orphans, duplicates. `summary.ai_ready` is
false when any critical/high integrity defect is present.

## Recommendation patterns (the_fix)
- **Dangling FK:** either reparent the child to the correct existing record, or, if the parent
  truly should exist, create it and backfill; never leave the pointer dangling.
- **Orphan record:** assign the missing parent (look up by domain/email/company), or quarantine
  the record out of the AI's routable set until a parent is assigned.
- **Broken seam:** re-link the lead to its real converted opportunity, or mark the conversion
  failed and re-run conversion so the seam is rebuilt.
- **Duplicate key:** merge on the surviving master record, repoint all children, and add a
  dedup rule so the AI sees one customer identity.

**Acceptance:** every defect in the supplied export is reported once, with the implicated
record ids in `affected` and a concrete repair in `the_fix`.
