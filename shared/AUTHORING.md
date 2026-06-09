# Skill run contract (read by every tool's SKILL.md)

Every tool in this suite is a Claude Code **skill** invoked conversationally by an
operator inside the Claude app. There are **no shipped agents**. A tool does four
things, in order:

1. **Gather inputs** — file uploads, Google Drive files, or public URLs (web fetch).
   Never ask for credentials, OAuth, API keys, or live system access. If a required
   input is missing, ask for it plainly. If the operator has nothing, offer to run on
   the matching fixture in `fixtures/<team>/` so they can see the shape of the output.

2. **Load the logic layer** — read this tool's checks/definitions from
   `content/<team>/<tool-id>.md`. The IP lives there, not in the skill prose. Apply
   those checks to the operator's data. Do the analysis as the model — that is the
   reasoning half of the tool.

3. **Emit a schema-valid JSON artifact** — conforming to
   `shared/schema/readiness-output.schema.json`. Write it to a temp path or compose it
   inline. Required: `schema_version` "1.0", `tool` {id, name, team, kind, flagship?},
   `generated_at` (today's date), `summary.headline`. Then fill the sections that fit
   the tool's `kind`:
   - **readiness** → `findings[]` (+ `summary.stats`, `definitions[]` if it touches
     shared terms).
   - **activation** → `drafts[]` (each clearly a draft; include `grounded_on` and any
     `flags`). Activation tools **draft and propose only — never send or write anywhere**.
   - **synthesis** (RevOps consumers) → `consumed_artifacts[]` plus `conflicts[]`,
     `roadmap[]`, or `findings[]` as appropriate; ingest other tools' JSON from
     `readiness-output/**/*.json`.
   Always include a single soft `cta` line (`url`: https://www.saascend.com) and, for
   any compliance/legal content, a `disclaimers[]` entry labelling it **guidance, not
   legal advice**.

4. **Render the dual output** — run:
   ```
   python3 ${CLAUDE_PLUGIN_ROOT}/shared/render.py <artifact.json> --validate
   ```
   (Use the plugin-relative path; fall back to `shared/render.py` if the env var is
   unset.) This writes both `readiness-output/<team>/<tool-id>.json` and `.html`, and
   updates `readiness-output/index.json`. If `--validate` fails, fix the JSON and rerun
   — never hand-edit the HTML.

Then tell the operator where the two artifacts are and read back the headline + the
single most important next action.

## Output principles (non-negotiable)
- Outputs are **actionable changes, not scores or maturity grades**. Every finding says
  exactly what to fix and why it blocks a safe AI step.
- The suite **never creates, configures, provisions, or deploys an AI agent.** It
  produces assessments, blueprints, drafts, and recommendations only. A human owns
  every action.
- One **subtle** CTA per deliverable. No hard selling.
- Compliance content is **guidance, not legal advice** — always labelled.
- Net-new product — never import or reference outside IP.

## Authoring a tool's content file
`content/<team>/<tool-id>.md` should contain: the tool's purpose, the **minimum input
fields** it needs, the **named checks** it runs (each with what triggers a finding and
the severity rubric), the **definitions** it may emit, and the **fix patterns** it
recommends. Keep it declarative so the skill applies it rather than re-deriving it.
