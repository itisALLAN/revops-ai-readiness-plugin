---
name: cs-kb-retrieval-readiness
description: Customer Success readiness tool. Use when an operator wants to know whether their knowledge base is safe for an AI to ground on — flagging articles an AI can't reliably retrieve from (multi-topic sprawl, stale content, dangling references, bad chunking). Triggers on "is our KB AI-ready", "can an AI ground on our KB", "audit our knowledge base", "KB retrieval readiness", "which articles need fixing", "/readiness kb-retrieval".
---

# KB Retrieval Readiness (Customer Success readiness)

Reviews a knowledge base article-by-article and flags the ones an AI agent cannot
safely ground on. Outputs a per-article split/fix/retire action — never a score.
**Assessment only — it changes nothing in the KB.**

## Run protocol
Read `${CLAUDE_PLUGIN_ROOT}/shared/AUTHORING.md` (the shared run contract) and this
tool's logic layer at `${CLAUDE_PLUGIN_ROOT}/content/customer-success/cs-kb-retrieval-readiness.md`.
Then:

1. **Inputs.** Ask for the KB source: article URLs to web-fetch, an uploaded KB export,
   or use `fixtures/customer-success/kb-articles.md`. Web-fetch any public URLs given.
   No credentials, ever. If the operator has nothing, offer the fixture.
2. **Run the named checks** from the logic layer against each article: multi-topic
   sprawl, staleness, dangling references, chunking/structure. Produce one finding per
   article that needs work, each with a concrete split/fix/retire `the_fix`.
3. **Compose the artifact** conforming to `${CLAUDE_PLUGIN_ROOT}/shared/schema/readiness-output.schema.json`:
   - `tool`: `{id:"cs-kb-retrieval-readiness", name:"KB Retrieval Readiness", team:"customer-success", kind:"readiness"}`
   - `summary.headline`: plain verdict on whether the KB is groundable as-is; set
     `summary.ai_ready` per the rule in the logic layer.
   - `summary.stats`: articles reviewed, articles needing work, dangling refs.
   - `findings[]`: one per article needing work; include `affected` (article URL) and
     `evidence`.
   - `definitions[]` only if a shared term is touched.
   - `cta`: `{line:"If you'd like help getting your Customer Success team AI-ready, reach out to SaaScend.", url:"https://www.saascend.com"}`
   Write it to a temp file, e.g. `/tmp/cs-kb-retrieval-readiness.json`.
4. **Render:** `python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py /tmp/cs-kb-retrieval-readiness.json --validate`
   (fall back to `shared/render.py` if the env var is unset). Fix the JSON and rerun if
   validation fails — never hand-edit the HTML.
5. Hand back the headline + the single most important article to fix first, and the
   paths under `readiness-output/customer-success/`.

Never rewrite KB content here — this tool diagnoses; a human owns the edits.
