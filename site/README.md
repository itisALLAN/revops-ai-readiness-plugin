# Landing site — RevOps AI Readiness Suite

Two static, self-contained pages that collect email opt-ins and hand new users a clean
install path. Built on the SaaScend design system (same brand tokens as the plugin's
deliverables).

```
site/
├── index.html        Landing page + email opt-in form
├── thank-you.html    Post-opt-in: install steps + where to begin
├── styles.css        Shared brand + layout (Montserrat + Open Sans via Google Fonts)
└── assets/           SaaScend logos
```

## Deploy

It's plain static HTML — host it anywhere:

- **Drag-and-drop:** drop the `site/` folder onto Netlify Drop / Vercel / Cloudflare Pages.
- **GitHub Pages:** serve this folder (or copy it to `/docs`) and enable Pages.
- **Local preview:** `python3 -m http.server -d site 8000` → http://localhost:8000

The flow is `index.html` → submit → `thank-you.html`.

## Wire up the email capture (one change)

The form works out of the box in **demo mode**: until you configure a real endpoint, a small
script on the landing page simply routes submissions to `thank-you.html` so you can click
through the whole flow. **No emails are stored in demo mode.**

To actually capture opt-ins, point the form at any form provider that accepts an HTML POST
(Formspree, Buttondown, ConvertKit, Mailchimp embedded, HubSpot forms, etc.). For example,
with Formspree:

1. Create a form and copy its endpoint.
2. In `index.html`, replace the form `action`:
   ```html
   action="https://formspree.io/f/REPLACE_WITH_YOUR_FORM_ID"
   ```
   with your real endpoint. The hidden `_next` field already redirects successful
   submissions to `thank-you.html`; the demo-mode script disables itself automatically once
   the placeholder id is gone.
3. Keep the `consent` checkbox — it records explicit opt-in, which matters for CAN-SPAM / GDPR.

No backend, OAuth, or API keys live in this repo — the provider owns storage and delivery.

## Notes

- Brand tokens mirror `../shared/brand/colors_and_type.css` (the source of truth). If the brand
  changes there, update `styles.css` to match.
- Install commands on the thank-you page must match the plugin's `.claude-plugin/marketplace.json`
  (`name: "saascend"`) and `plugin.json` (`name: "revops-ai-readiness-suite"`). If either name
  changes, update `thank-you.html`.
