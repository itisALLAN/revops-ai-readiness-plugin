#!/usr/bin/env python3
"""RevOps AI Readiness Suite — dual-output renderer.

Turns a schema-valid JSON artifact into:
  1. a SaaScend-branded, fully self-contained HTML deliverable (inline CSS +
     base64 fonts + base64 logo — opens from file:// or any static host), and
  2. the JSON itself, written to the conventional output path.

Skills call this after producing their analysis JSON. The model does the
reasoning; this script owns consistent branded rendering. Stdlib only.

Usage:
    python3 shared/render.py <artifact.json> [--out-root readiness-output] [--validate]
    python3 shared/render.py -            # read JSON from stdin
    cat artifact.json | python3 shared/render.py -

Writes:
    <out-root>/<team>/<tool-id>.json
    <out-root>/<team>/<tool-id>.html
    <out-root>/index.json          (rolling manifest of all artifacts)

Exit codes: 0 ok · 2 invalid input · 3 schema validation failed.
"""
import argparse
import base64
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "template"))
import components as C  # noqa: E402

BRAND = HERE / "brand"
SCHEMA_PATH = HERE / "schema" / "readiness-output.schema.json"


# --------------------------------------------------------------------------- assets
def _read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def _brand_css() -> str:
    """colors_and_type.css with its @import line stripped (fonts are inlined separately)."""
    css = _read(BRAND / "colors_and_type.css")
    return "\n".join(l for l in css.splitlines() if "@import" not in l)


def _fonts_css() -> str:
    f = BRAND / "fonts_inline.css"
    if not f.exists():
        raise SystemExit("fonts_inline.css missing — run shared/brand/_build_fonts_inline.py first")
    return _read(f)


def _logo_data_uri(name: str) -> str:
    b = (BRAND / "assets" / name).read_bytes()
    return "data:image/png;base64," + base64.b64encode(b).decode("ascii")


# --------------------------------------------------------------------------- validation
def _validate(obj: dict) -> list:
    """Best-effort validation. Uses jsonschema if available, else a structural fallback."""
    try:
        import jsonschema  # type: ignore
        schema = json.loads(_read(SCHEMA_PATH))
        v = jsonschema.Draft7Validator(schema)
        return [f"{'/'.join(map(str, e.path)) or '(root)'}: {e.message}" for e in v.iter_errors(obj)]
    except ImportError:
        pass
    errs = []
    if obj.get("schema_version") != "1.0":
        errs.append("schema_version must be '1.0'")
    tool = obj.get("tool") or {}
    for k in ("id", "name", "team", "kind"):
        if not tool.get(k):
            errs.append(f"tool.{k} is required")
    if tool.get("team") not in {"customer-success", "sales", "marketing", "revops"}:
        errs.append("tool.team invalid")
    if tool.get("kind") not in {"readiness", "activation", "synthesis"}:
        errs.append("tool.kind invalid")
    if not obj.get("generated_at"):
        errs.append("generated_at is required")
    if not (obj.get("summary") or {}).get("headline"):
        errs.append("summary.headline is required")
    return errs


# --------------------------------------------------------------------------- html
TEAM_LABEL = {
    "customer-success": "Customer Success",
    "sales": "Sales",
    "marketing": "Marketing",
    "revops": "RevOps",
}


def render_html(obj: dict) -> str:
    tool = obj["tool"]
    summary = obj["summary"]
    team = tool.get("team", "revops")

    style = f"<style>\n{_fonts_css()}\n{_brand_css()}\n{_read(HERE / 'template' / 'deliverable.css')}\n</style>"

    # hero meta
    meta_bits = [f'<span><b>{C.esc(TEAM_LABEL.get(team, team))}</b> · AI Readiness Suite</span>']
    if obj.get("generated_at"):
        meta_bits.append(f'<span>Generated {C.esc(obj["generated_at"])}</span>')
    inputs = obj.get("inputs") or []
    if inputs:
        ins = ", ".join(C.esc(i.get("description") or i.get("ref")) for i in inputs[:4])
        meta_bits.append(f"<span>Inputs: {ins}</span>")

    hero = (
        '<header class="hero"><div class="wrap pad">'
        f'<img class="hero__logo" alt="SaaScend" src="{_logo_data_uri("SaaScend_FullLogo_white_text.png")}"/>'
        f'{C.eyebrow(tool.get("name", "AI Readiness"))}'
        f'<h1 class="hero__title">{C.esc(summary.get("headline",""))}</h1>'
        + (f'<p class="hero__headline">{C._inline_md(summary["narrative"])}</p>' if summary.get("narrative") else "")
        + f'<div class="hero__meta">{"".join(meta_bits)}</div>'
        "</div></header>"
    )

    body = [C.stat_band(summary.get("stats"))]
    # synthesis-specific sections first when present
    body.append(C.conflicts_section(obj.get("conflicts")))
    body.append(C.roadmap_section(obj.get("roadmap")))
    body.append(C.findings_section(obj.get("findings")))
    body.append(C.definitions_section(obj.get("definitions")))
    body.append(C.drafts_section(obj.get("drafts")))
    body.append(C.disclaimers_block(obj.get("disclaimers")))
    body.append(C.cta_band(obj.get("cta")))

    foot = (
        '<footer class="foot"><div class="wrap pad">'
        f'<img alt="SaaScend" src="{_logo_data_uri("SaaScend_FullLogo.png")}"/>'
        "Produced by the SaaScend RevOps AI Readiness Suite. "
        "Findings are recommendations a human reviews and owns — this tool changes nothing in your systems."
        "</div></footer>"
    )

    return (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/>"
        '<meta name="viewport" content="width=device-width, initial-scale=1"/>'
        f"<title>{C.esc(tool.get('name',''))} — SaaScend AI Readiness</title>"
        f"{style}</head><body>{hero}<main>{''.join(b for b in body if b)}</main>{foot}</body></html>"
    )


# --------------------------------------------------------------------------- io
def write_outputs(obj: dict, out_root: pathlib.Path) -> dict:
    tool = obj["tool"]
    team_dir = out_root / tool["team"]
    team_dir.mkdir(parents=True, exist_ok=True)
    base = tool["id"]
    json_path = team_dir / f"{base}.json"
    html_path = team_dir / f"{base}.html"
    json_path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")
    html_path.write_text(render_html(obj), encoding="utf-8")
    _update_index(out_root, obj, json_path, html_path)
    return {"json": str(json_path), "html": str(html_path)}


def _update_index(out_root: pathlib.Path, obj: dict, json_path, html_path) -> None:
    idx_path = out_root / "index.json"
    idx = {"schema_version": "1.0", "artifacts": []}
    if idx_path.exists():
        try:
            idx = json.loads(idx_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    tool = obj["tool"]
    entry = {
        "tool_id": tool["id"],
        "team": tool["team"],
        "kind": tool["kind"],
        "name": tool.get("name"),
        "generated_at": obj.get("generated_at"),
        "json": str(pathlib.Path(json_path).relative_to(out_root)),
        "html": str(pathlib.Path(html_path).relative_to(out_root)),
        "blocking_count": obj.get("summary", {}).get("blocking_count"),
    }
    idx["artifacts"] = [a for a in idx.get("artifacts", []) if a.get("tool_id") != tool["id"]]
    idx["artifacts"].append(entry)
    idx["artifacts"].sort(key=lambda a: (a.get("team", ""), a.get("tool_id", "")))
    idx_path.write_text(json.dumps(idx, indent=2, ensure_ascii=False), encoding="utf-8")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Render a RevOps AI Readiness artifact to branded HTML + JSON.")
    ap.add_argument("artifact", help="Path to artifact JSON, or '-' for stdin")
    ap.add_argument("--out-root", default="readiness-output", help="Output root directory (default: readiness-output)")
    ap.add_argument("--validate", action="store_true", help="Validate against the schema and fail on errors")
    ap.add_argument("--html-only", action="store_true", help="Print HTML to stdout, write nothing")
    args = ap.parse_args(argv)

    raw = sys.stdin.read() if args.artifact == "-" else _read(pathlib.Path(args.artifact))
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}", file=sys.stderr)
        return 2

    errs = _validate(obj)
    if errs:
        msg = "Schema validation errors:\n  - " + "\n  - ".join(errs)
        if args.validate:
            print(msg, file=sys.stderr)
            return 3
        print(f"[warn] {msg}", file=sys.stderr)

    if args.html_only:
        sys.stdout.write(render_html(obj))
        return 0

    paths = write_outputs(obj, pathlib.Path(args.out_root))
    print(f"Wrote:\n  {paths['json']}\n  {paths['html']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
