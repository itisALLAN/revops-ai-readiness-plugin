"""Reusable HTML fragment builders for SaaScend-branded deliverables.

Every fragment uses only classes defined in deliverable.css + the brand
tokens in colors_and_type.css. No inline colors, no new design values.
All user/model-supplied text is HTML-escaped here so render.py never has
to think about escaping.
"""
from html import escape as _esc
import re


def esc(value) -> str:
    return _esc(str(value if value is not None else ""))


def _inline_md(text: str) -> str:
    """Minimal, safe inline markdown: **bold**, *italic*, `code`. Escapes first."""
    out = esc(text)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", out)
    out = re.sub(r"`(.+?)`", r"<code>\1</code>", out)
    return out


def eyebrow(text: str, cls: str = "ss-eyebrow hero__eyebrow") -> str:
    return f'<div class="{cls}">{esc(text)}</div>'


def section(title: str, body: str, intro: str = "") -> str:
    intro_html = f'<p class="ss-p section__intro">{_inline_md(intro)}</p>' if intro else ""
    return (
        '<section class="section"><div class="wrap pad">'
        f'<div class="section__head"><h2 class="ss-h2">{esc(title)}</h2>{intro_html}</div>'
        f"{body}"
        "</div></section>"
    )


def stat_band(stats) -> str:
    if not stats:
        return ""
    cells = []
    for s in stats:
        tone = s.get("tone", "neutral")
        cells.append(
            f'<div class="stat stat--{esc(tone)}">'
            f'<div class="stat__value">{esc(s.get("value",""))}</div>'
            f'<div class="stat__label">{esc(s.get("label",""))}</div>'
            "</div>"
        )
    return (
        '<section class="section"><div class="wrap pad">'
        f'<div class="stats">{"".join(cells)}</div>'
        "</div></section>"
    )


_SEV_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def finding_card(f) -> str:
    sev = f.get("severity", "medium")
    cat = f'<div class="finding__cat">{esc(f["category"])}</div>' if f.get("category") else ""
    parts = [
        '<div class="card finding">',
        '<div class="finding__top">',
        f'<div style="flex:1">{cat}<h3 class="finding__title">{esc(f.get("title",""))}</h3></div>',
        f'<span class="pill pill--{esc(sev)}">{esc(sev)}</span>',
        "</div>",
    ]
    if f.get("what_we_found"):
        parts.append(f'<div class="kv"><div class="kv__k">What we found</div><div class="kv__v ss-p">{_inline_md(f["what_we_found"])}</div></div>')
    if f.get("why_it_blocks_ai"):
        parts.append(f'<div class="kv"><div class="kv__k">Why it blocks a safe AI step</div><div class="kv__v ss-p">{_inline_md(f["why_it_blocks_ai"])}</div></div>')
    fixes = f.get("the_fix") or []
    if fixes:
        items = "".join(f"<li class=\"ss-p\">{_inline_md(x)}</li>" for x in fixes)
        parts.append(f'<div class="kv"><div class="kv__k">The fix</div><ol class="fixlist">{items}</ol></div>')
    if f.get("evidence"):
        parts.append(f'<div class="kv"><div class="kv__k">Evidence</div><div class="kv__v ss-p ss-muted">{_inline_md(f["evidence"])}</div></div>')
    meta = []
    if f.get("owner_role"):
        meta.append(f'<span class="tag">owner: {esc(f["owner_role"])}</span>')
    for a in (f.get("affected") or [])[:12]:
        meta.append(f'<span class="tag">{esc(a)}</span>')
    if meta:
        parts.append(f'<div class="tags">{"".join(meta)}</div>')
    parts.append("</div>")
    return "".join(parts)


def findings_section(findings, title="What to fix", intro=""):
    if not findings:
        return ""
    ordered = sorted(findings, key=lambda f: _SEV_ORDER.get(f.get("severity", "medium"), 2))
    body = "".join(finding_card(f) for f in ordered)
    return section(title, body, intro)


def definitions_section(definitions, title="Definitions in play", intro=""):
    if not definitions:
        return ""
    rows = "".join(
        "<tr>"
        f'<td><b>{esc(d.get("term",""))}</b></td>'
        f'<td>{_inline_md(d.get("definition",""))}</td>'
        f'<td>{esc(d.get("source_team",""))}</td>'
        f'<td class="ss-muted">{esc(d.get("derived_from",""))}</td>'
        "</tr>"
        for d in definitions
    )
    table = (
        '<div class="card"><table class="deftable">'
        "<thead><tr><th>Term</th><th>Definition</th><th>Team</th><th>Derived from</th></tr></thead>"
        f"<tbody>{rows}</tbody></table></div>"
    )
    return section(title, table, intro)


def conflicts_section(conflicts, title="Cross-team definition conflicts", intro=""):
    if not conflicts:
        return ""
    cards = []
    for c in conflicts:
        positions = "".join(
            f'<div class="pos ss-p"><b>{esc(p.get("team",""))}:</b> {_inline_md(p.get("definition",""))}</div>'
            for p in c.get("positions", [])
        )
        impact = f'<div class="kv"><div class="kv__k">Impact on an AI agent</div><div class="kv__v ss-p">{_inline_md(c["impact"])}</div></div>' if c.get("impact") else ""
        canon = f'<div class="kv"><div class="kv__k">Recommended canonical definition</div><div class="kv__v ss-p">{_inline_md(c["recommended_canonical"])}</div></div>' if c.get("recommended_canonical") else ""
        cards.append(
            '<div class="card conflict">'
            f'<h3 class="finding__title">“{esc(c.get("term",""))}” means different things</h3>'
            f"{positions}{impact}{canon}</div>"
        )
    return section(title, "".join(cards), intro)


def drafts_section(drafts, title="Drafted for you — human owns the send", intro=""):
    if not drafts:
        return ""
    cards = []
    for d in drafts:
        grounded = ""
        if d.get("grounded_on"):
            tags = "".join(f'<span class="tag">{esc(g)}</span>' for g in d["grounded_on"])
            grounded = f'<div class="draft__meta"><b>Grounded on:</b></div><div class="tags">{tags}</div>'
        flags = "".join(f'<div class="draft__flag">⚑ {_inline_md(x)}</div>' for x in (d.get("flags") or []))
        cards.append(
            '<div class="card">'
            f'<span class="draft__label">{esc(d.get("kind","draft"))} · draft only — not sent</span>'
            f'<h3 class="finding__title" style="margin-bottom:var(--space-4)">{esc(d.get("title",""))}</h3>'
            f'<div class="draft__body">{esc(d.get("content",""))}</div>'
            f"{grounded}{flags}</div>"
        )
    return section(title, "".join(cards), intro)


def roadmap_section(items, title="Prioritised roadmap", intro=""):
    if not items:
        return ""
    cards = []
    for it in sorted(items, key=lambda x: x.get("rank", 99)):
        symptoms = ""
        if it.get("symptoms"):
            tags = "".join(f'<span class="tag">{esc(s)}</span>' for s in it["symptoms"])
            symptoms = f'<div class="kv"><div class="kv__k">Resolves these symptoms</div><div class="tags">{tags}</div></div>'
        meta_bits = []
        if it.get("teams"):
            meta_bits.append("· ".join(esc(t) for t in it["teams"]))
        if it.get("effort"):
            meta_bits.append(f'effort {esc(it["effort"])}')
        meta = f'<div class="draft__meta">{" &nbsp;·&nbsp; ".join(meta_bits)}</div>' if meta_bits else ""
        cards.append(
            '<div class="card"><div class="road">'
            f'<div class="road__rank">{esc(it.get("rank",""))}</div>'
            "<div style=\"flex:1\">"
            f'<div class="road__seq">{esc(it.get("sequence","now"))}</div>'
            f'<h3 class="finding__title">{esc(it.get("action",""))}</h3>'
            f'<div class="kv"><div class="kv__k">Root cause (RevOps level)</div><div class="kv__v ss-p">{_inline_md(it.get("root_cause",""))}</div></div>'
            f"{symptoms}{meta}"
            "</div></div></div>"
        )
    return section(title, "".join(cards), intro)


def cta_band(cta) -> str:
    if not cta:
        return ""
    return (
        '<div class="wrap pad"><div class="cta">'
        f'<p>{_inline_md(cta.get("line",""))}</p>'
        f'<a class="btn" href="{esc(cta.get("url","#"))}">Talk to SaaScend</a>'
        "</div></div>"
    )


def disclaimers_block(disclaimers) -> str:
    if not disclaimers:
        return ""
    lines = "".join(f'<div class="disclaimer">{_inline_md(x)}</div>' for x in disclaimers)
    return f'<div class="wrap pad">{lines}</div>'
