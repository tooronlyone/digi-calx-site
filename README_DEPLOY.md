# Digi_CalX public website

Production URL: https://digi-calx.d-hag.com/

## Contents

- `index.html` — homepage and SEO metadata
- `styles.css` — monochrome D-HAG/Digi_TransX visual family
- `script.js` — navigation + reveal behavior
- `robots.txt` — crawler access + sitemap reference
- `sitemap.xml` — canonical public URL
- `404.html` — branded noindex 404
- `site.webmanifest` — basic web manifest
- `assets/png/digi-calx-social-card.png` — Open Graph/Twitter card
- `assets/svg/favicon.svg` — favicon
- `wrangler.jsonc` — Cloudflare Workers Static Assets config

## Cloudflare Workers Static Assets

From the project root:

```bash
npx wrangler dev
npx wrangler deploy
```

The Wrangler config already declares `digi-calx.d-hag.com` as the Worker custom domain. The deploying Cloudflare account must have permission to attach that subdomain.

## Post-deploy checks

1. Open `https://digi-calx.d-hag.com/`.
2. Open `/robots.txt` and `/sitemap.xml`.
3. Test a missing route and confirm the branded 404 page.
4. View page source and confirm the canonical URL is `https://digi-calx.d-hag.com/`.
5. Confirm the social image loads from `/assets/png/digi-calx-social-card.png`.
6. Submit the sitemap in Google Search Console after the domain is serving the final site.

## Current positioning boundary

The site intentionally says Digi_CalX is in pre-development validation and not publicly launched. Do not replace that with “live”, “available”, “ISO certified”, or “under active development” until the underlying status actually changes.
