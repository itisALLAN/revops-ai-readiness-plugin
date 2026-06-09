# RevOps AI Readiness Suite

A Claude Code plugin by **SaaScend** that helps a go-to-market org's four teams —
**Customer Success, Sales, Marketing, and RevOps** — get ready for AI and take a first
*safe* step into using it.

It is operated by a technical RevOps person or a SaaScend consultant **inside the Claude
app — no terminal required.** The four GTM teams are the beneficiaries, not the hands-on
users.

> **The suite never creates, configures, provisions, or deploys an AI agent.** Every tool
> produces an **assessment, blueprint, draft, or recommendation** — and a human owns every
> action. Activation tools draft and propose; they never send or write to any system.

## Install

Inside Claude Code, add the SaaScend marketplace, then install the suite:

```
/plugin marketplace add itisALLAN/revops-ai-readiness-plugin
/plugin install revops-ai-readiness-suite@saascend
```

That's it — the 25 skills and the `/readiness`, `/activate`, and `/roadmap` commands are now
available. (Prefer a menu? Run `/plugin`, open **Discover**, and install
*RevOps AI Readiness Suite* from there.)

**Requirements:** Claude Code with plugins enabled, and `python3` on your PATH (the renderer
uses only the standard library). No CRM/MAP credentials, OAuth, or API keys — inputs are file
uploads, Google Drive, and public URLs via native Claude connectors.

**Where to begin:** run `/readiness` and pick a team, or `/activate brand-codex` to produce a
quick first artifact. Once a few team tools have run, `/roadmap` synthesizes everything into one
org-wide plan.

## What you get from every tool

Two artifacts, from one source of truth (so they can't drift):

1. A **SaaScend-branded, fully self-contained HTML deliverable** (inline CSS, base64 fonts
   + logo — opens from `file://` or any static host).
2. A **schema-valid JSON** written to a predictable path, so downstream RevOps tools can
   consume it.

Outputs are **actionable changes, not scores or maturity grades** — they tell you exactly
what to fix to get AI-ready.

## How it's operated

Inside the Claude app, either invoke a tool by name conversationally ("build me a brand
codex from these URLs") or use the operator slash-commands:

| Command | What it does |
|---|---|
| `/readiness <team>` | Run a team's readiness tools (`customer-success` \| `sales` \| `marketing` \| `revops`). |
| `/activate <tool>` | Run an activation tool (`kb-reply`, `deal-update`, `brand-codex`, `content`). |
| `/roadmap` | Synthesize every team's JSON into one org-wide AI-readiness roadmap. |

Inputs are **file uploads, Google Drive, and public URLs** only — no live CRM/MAP
connections, no OAuth, no API keys, no custom MCP. The suite uses native Claude connectors.

## Tool catalog (25 tools · ★ = flagship)

**Customer Success** — kb-retrieval-readiness · intent-scope-mapper · deployment-guardrails ·
case-testset-observability · **kb-reply-drafter ★**

**Sales** — stage-qualification-readiness · pipeline-reality-check · capture-coverage ·
account-icp-readiness · trust-integrity-signals · deployment-guardrails ·
**transcript-deal-update ★**

**Marketing** — **brand-codex-builder ★** · claims-compliance-guardrails ·
audience-consent-readiness · measurement-attribution-readiness · deployment-guardrails ·
distinctiveness-guard · onbrand-content-drafter

**RevOps (keystone — consumes the other teams' JSON)** — **semantic-reconciler ★** ·
data-architecture-handoff · control-plane-blueprint · eval-deployment-framework ·
practitioner-maturity · **org-wide-roadmap ★**

## Architecture

```
.claude-plugin/plugin.json     Plugin manifest
commands/                      Operator slash-commands (sugar; tools also work by name)
skills/<tool-id>/SKILL.md      One skill per tool — no shipped agents
content/<team>/<tool-id>.md    The product IP: each tool's readiness checks & definitions
shared/
  AUTHORING.md                 The run contract every skill follows
  schema/readiness-output.schema.json   The dual-output JSON contract
  brand/                       Brand tokens, fonts, logos (from the SaaScend design system)
  template/                    deliverable.css + components.py (reusable branded HTML)
  render.py                    JSON → branded self-contained HTML + JSON (stdlib only)
fixtures/                      Synthetic sample data so every tool runs without real data
examples-src/                  Hand-authored sample artifacts (one per tool, schema-valid)
```

**Division of labor:** a skill (driven by its `content/` logic layer) does the *analysis*
of the operator's data and emits a schema-valid JSON artifact; `shared/render.py`
deterministically turns that JSON into the branded HTML. Reasoning to the model, consistent
branding to code. The JSON schema is the contract between the two halves **and** between
tools — Customer Success / Sales / Marketing tools emit JSON that the RevOps Semantic
Reconciler, Control-Plane Blueprint, and Org-Wide Roadmap consume.

### Output convention

```
readiness-output/<team>/<tool-id>.json
readiness-output/<team>/<tool-id>.html
readiness-output/index.json        # rolling manifest the RevOps synthesizers ingest
```

## Try it without the plugin runtime

The `examples-src/` directory holds one schema-valid sample artifact per tool, built from
the synthetic `fixtures/`. Render them all to branded HTML:

```bash
bash shared/build-examples.sh        # → examples/<team>/<tool>.html  (+ examples/index.json)
```

Validate any artifact against the schema, or render a single one:

```bash
python3 shared/render.py examples-src/revops-org-wide-roadmap.json --validate
```

(`render.py` uses only the Python standard library. If `jsonschema` is installed it is used
for full Draft-07 validation; otherwise a structural fallback runs.)

## Maintainer notes

- Brand tokens are the source of truth in `shared/brand/colors_and_type.css` — never invent
  color or type values; deliverables use only those tokens.
- The inline-font CSS (`shared/brand/fonts_inline.css`) is generated. Regenerate after
  changing the curated weight list: `python3 shared/brand/_build_fonts_inline.py`.
- Compliance and guardrail content is **guidance, not legal advice** and is labelled as such
  in every deliverable that contains it.

---

*Net-new product. The summit metaphor, voice, and brand are SaaScend's own. If you'd like
help getting your teams AI-ready, reach out to [SaaScend](https://www.saascend.com).*
