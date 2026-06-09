---
description: Run an activation tool that drafts a human-owned artifact (kb-reply | deal-update | brand-codex | content)
argument-hint: <tool> [inputs]
---

The operator wants to run an activation tool — these draft a real, usable artifact a human then owns. They never send, publish, or write to any system.

**Requested:** `$ARGUMENTS`

Activation tools:
- `kb-reply` → **cs-kb-reply-drafter** — customer question + KB URLs → cited, grounded draft reply (flags what the KB can't answer).
- `deal-update` → **sales-transcript-deal-update** — call transcript → drafted CRM update text (next steps, stage rationale, qualification signals).
- `brand-codex` → **mkt-brand-codex-builder** — content/blog URLs → a machine-usable brand codex (JSON consumed by other marketing tools).
- `content` → **mkt-onbrand-content-drafter** — a brief + the brand codex → a first on-brand draft, auto-checked against the claims list and distinctiveness guard.

Do this:

1. Map the first argument to the tool above (accept the long skill id too). If absent or ambiguous, list the four and ask.
2. Ask for that tool's inputs (uploads / Google Drive / public URLs). For `content` and `distinctiveness` work, look for an existing `readiness-output/marketing/mkt-brand-codex-builder.json` codex and offer to use it; if none exists, offer to run the codex builder first.
3. Invoke the skill. It produces the draft inside a schema-valid JSON `drafts[]` entry and renders the branded HTML.
4. Hand the draft back clearly labelled **draft only — not sent**, with its grounding citations and any caveats. Remind the operator a human owns the send/publish.
