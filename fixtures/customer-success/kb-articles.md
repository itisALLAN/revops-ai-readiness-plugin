# Sample KB corpus (synthetic)

Stand-in for the KB article URLs an operator would supply. Each block is one
"article". Deliberately seeded with retrieval problems: a multi-topic sprawl page,
a stale article, a dangling cross-reference, and gaps (no billing-dispute or
API-rate-limit article).

---

## https://kb.example.com/getting-started
title: Getting Started (Everything You Need)
last_updated: 2024-03-02
body: Welcome! This guide covers initial setup, inviting your team, configuring SSO,
connecting billing, and using the API. To set up SSO see the section below. For billing
questions, contact your account owner. To invite teammates, go to Settings > Members.
The API section explains authentication. (NOTE: ~4,100 words spanning four unrelated topics.)

---

## https://kb.example.com/sso-setup
title: Single Sign-On Setup
last_updated: 2023-08-14
body: Configure SAML by uploading your IdP metadata. See the certificate steps in
"SSO Advanced" for cert rotation. (Cross-references an article that no longer exists.)

---

## https://kb.example.com/invite-team
title: Invite Your Team
last_updated: 2026-02-01
body: Admins can invite members from Settings > Members > Invite. Roles: Admin, Member,
Viewer. Single, well-scoped, current.

---

## https://kb.example.com/password-reset
title: Reset Your Password
last_updated: 2026-01-10
body: Use the "Forgot password" link on the sign-in page. A reset email arrives within
five minutes. Single-topic, current. Good grounding source.

---

## https://kb.example.com/data-exports
title: Exporting Your Data
last_updated: 2025-11-20
body: Exports run as background jobs and are stored for 30 days. Large datasets may take
several minutes. Single-topic, reasonably current.

---

## https://kb.example.com/salesforce-integration
title: Connecting Salesforce
last_updated: 2023-05-01
body: Install the managed package v1.2 and map fields. (References a package version that
is three major versions out of date. Stale.)

# Known gaps (no article exists): billing disputes / refunds, API rate limits,
# API key rotation, GDPR / data residency, webhook troubleshooting.
