---
name: cs-kb-reply-drafter
description: ★ Flagship Customer Success activation tool. Use when an operator wants a cited, KB-grounded draft reply to a customer question — and wants the gaps where the KB can't answer flagged. Triggers on "draft a reply", "answer this customer question from our KB", "KB grounded reply", "can our KB answer this", "/activate kb-reply". Drafts only — never sends.
---

# KB-Grounded Reply Drafter (★ Customer Success flagship)

Drafts a cited, grounded reply to a customer question from the KB, and explicitly flags
anything the current KB can't safely answer. **Assist only — it sends nothing.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` (the shared run contract) and this
tool's logic layer at `${CLAUDE_PLUGIN_ROOT}/content/customer-success/cs-kb-reply-drafter.md`.
Then:

1. **Inputs.** Ask for the customer question and the KB source (article URLs to fetch, an
   uploaded KB export, or use `fixtures/customer-success/kb-articles.md`). Web-fetch any
   public URLs given. No credentials, ever.
2. **Draft** following the logic layer: retrieve-don't-invent, cite every claim, flag every
   gap, keep sensitive classes (billing dispute / account security / legal) to a safe
   acknowledge-and-escalate draft.
3. **Compose the artifact** conforming to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"cs-kb-reply-drafter", name:"KB-Grounded Reply Drafter", team:"customer-success", kind:"activation", flagship:true}`
   - `summary.headline`: whether the KB fully grounded the answer; `summary.ai_ready` per the rule.
   - one `drafts[]` entry (`kind:"kb-grounded-reply"`, `content`, `grounded_on`, `flags`).
   - `cta`: `{line:"If you'd like help getting your Customer Success team AI-ready, reach out to SaaScend.", url:"https://www.saascend.com"}`
   Write it to a temp file, e.g. `/tmp/cs-kb-reply-drafter.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/cs-kb-reply-drafter.json --validate`
5. Hand back the draft **labelled draft-only**, with its citations and gap flags, and the
   paths under `readiness-output/customer-success/`.

Never invent policy, pricing, or promises. A human owns the send.
