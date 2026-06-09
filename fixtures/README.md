# Fixtures — synthetic sample data

Net-new, fictional data so every tool runs end-to-end without real client data. No
outside IP. Company names are obvious placeholders. Each tool's SKILL.md offers to run
on the matching fixture when the operator has nothing to upload.

| Team | File | Used by |
|---|---|---|
| Customer Success | `customer-success/cases.csv` | intent-scope-mapper, case-testset-observability, deployment-guardrails-cs |
| Customer Success | `customer-success/kb-articles.md` | kb-retrieval-readiness, intent-scope-mapper, kb-reply-drafter |
| Sales | `sales/opportunities.csv` | stage-qualification, pipeline-reality-check, trust-integrity-signals |
| Sales | `sales/activities.csv` | pipeline-reality-check, capture-coverage |
| Sales | `sales/accounts.csv` | account-icp-readiness |
| Sales | `sales/call-transcript.txt` | capture-coverage, transcript-deal-update |
| Marketing | `marketing/content-corpus.md` | brand-codex-builder, claims-compliance, distinctiveness-guard, content-drafter |
| Marketing | `marketing/leads.csv` | audience-consent-readiness |
| Marketing | `marketing/campaign-reporting.csv` | measurement-attribution-readiness |
| RevOps | `revops/multi-object-export.md` | data-architecture-handoff |
| RevOps | (other tools' JSON in `readiness-output/`) | semantic-reconciler, control-plane-blueprint, org-wide-roadmap |

The seeded problems are intentional — they let each tool produce a non-trivial, realistic
deliverable (coverage gaps, stale pipeline, consent holes, broken FKs, definition conflicts,
brand drift, risky claims).
