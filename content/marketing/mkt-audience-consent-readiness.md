# Logic layer — Audience & Consent Readiness (readiness)

**Purpose.** Determine whether lead/audience data is explicit, consented, and clean enough
for an AI to segment, target, or message against. The risk: an AI that targets or messages
a list with unknown consent, suppressed-but-active records, or unconsented cold-list leads
turns a data-hygiene gap into a deliverability and compliance incident at machine speed.
**Assessment only — it changes nothing in any CRM or ESP.**

**Minimum inputs.** One leads/contacts export with at least: `lead_id`, `email`,
`lifecycle_stage`, `consent_status`, `subscription_status`, `mql_flag`, and ideally
`segment`. The fixture `fixtures/marketing/leads.csv` has all of these.

## Named checks
1. **CONSENT_BASIS_MISSING** — `consent_status` is "Unknown", "No record", or blank.
   Severity **critical** when it covers a material share of marketable records. In the
   fixture roughly **one-third (~33%) of MQLs** carry unknown/absent consent. State this
   percentage explicitly.
2. **SUPPRESSED_BUT_ACTIVE** — a record whose `subscription_status` is "Unsubscribed" or
   "Bounced" is still flagged active/marketable (e.g. `mql_flag = Yes`). Severity
   **high**. Count these; they must be suppressed before any AI targets them.
3. **COLD_LIST_NO_CONSENT** — `source = "Cold list"` with `consent_status` "No record".
   Severity **high**. Flag explicitly and align with the org roadmap: cold, unconsented
   leads are out of scope for any AI messaging step until a lawful basis is established.
4. **SEGMENT_NOT_EXPLICIT** — `segment` is blank, so the audience an AI would target is
   not defined in the data. Severity **medium**. An AI cannot segment on an empty field.
5. **MQL_DEFINITION_DRIFT** — the marketing MQL definition is broader than sales'
   "Qualified", so the same record means different things to each team. Severity **high**.
   Emit the definition (below) so the semantic-reconciler can surface the conflict.

## Definitions emitted
- term **"MQL"**, `source_team:"marketing"`, definition: *"MQL = a lead whose score is
  above the marketing threshold OR who completed a content download, regardless of budget
  or authority."* This is deliberately **broader** than sales' "Qualified" (budget
  confirmed AND economic buyer identified). Emit so the semantic-reconciler flags the conflict.

## Fix patterns
- Backfill or re-permission every "Unknown"/"No record" consent record before it enters
  any AI-targetable segment; exclude them until a lawful basis is on file.
- Suppress all Unsubscribed/Bounced records at the source so they cannot re-enter a
  marketable audience.
- Quarantine cold-list, unconsented leads; align scope with the org-wide roadmap.
- Make `segment` mandatory so audiences are explicit in the data, not inferred.
- Govern one canonical MQL/Qualified definition jointly with sales before any AI routes,
  scores, or messages a lead.
