# Logic layer — Account & ICP Readiness (readiness)

**Purpose.** Assess whether account data, buying-committee/hierarchy coverage, and ICP /
MQL-SQL definitions are solid enough for an AI to route or prioritise accounts. Missing
committee data and an undefined ICP mean an AI would route on vibes. **Assessment only.**

**Minimum inputs.** An accounts export with at least: `account_id`, `name`, `industry`,
`employees`, `arr`, `buying_committee_contacts`, `icp_tier`, `parent_account`.

## Named checks
1. **NO_BUYING_COMMITTEE** — an account with `buying_committee_contacts = 0`. Severity
   **high**; **critical** if it has an open opportunity. The AI cannot reason about who
   to engage. List the named accounts (e.g. Hooli, Wayne).
2. **MISSING_ICP_DEFINITION** — no field/source encodes what ICP membership *means*;
   `icp_tier` is present but its A/B/C criteria are not documented anywhere. Severity
   **high**. The tiering is an opinion, not a rule an AI can apply.
3. **HIERARCHY_GAP** — accounts that should roll up to a parent (e.g. same group) but
   have a blank `parent_account`. Severity **medium**. Cross-sell/whitespace reasoning
   breaks without the hierarchy.
4. **DATA_HYGIENE_GAP** — implausible or zero values in `arr`/`employees` that an AI
   would treat as fact. Severity **medium**. Flag for review, do not assume meaning.

## Definitions emitted
- term **"ICP"**, `source_team:"sales"`, e.g. *"ICP = B2B software accounts, 250–5,000
  employees, with a named economic buyer and a budgeted RevOps initiative"*. Emit so the
  semantic-reconciler can reconcile it with marketing's ICP/MQL framing.

## Fix patterns
- Require at least one buying-committee contact (ideally an economic buyer) before an
  account is AI-routable.
- Document ICP tier criteria explicitly and encode them as rules, not just a label.
- Set parent_account on accounts in the same corporate group to restore hierarchy.
- Validate ARR/employee data before an AI prioritises on it.
