# CoreCloud Marketplace - Performance Hardening Pass v2
Date: 29 Jun 2026

Source build: CoreCloud-Marketplace.com-main (1).zip

## Changes applied

- Optimised `assets/images/corecloud-neon-logo.png` from ~1.56 MB to ~48 KB.
- Added explicit `width="256"` and `height="256"` attributes to every logo image instance.
- Added `decoding="async"` to logo images.
- Removed cache-busting/no-store fetches for `bundles.by_promotion.json` so the static JSON can be browser-cached.
- Removed no-cache meta directives from the cart page.
- Added layout reservations for dynamic bundle, hero, related bundle, cart and summary regions to reduce CLS.
- Added aspect-ratio rules for the logo.
- Added reduced-motion fallback.
- Preserved current visual design and content structure.

## Expected Lighthouse impact

Primary target is CLS reduction. The previous marketplace report showed very fast FCP/LCP/TBT but high CLS. This pass targets the causes Lighthouse flagged: missing image dimensions, large logo transfer, and dynamic content insertion after first paint.

## Deployment note

Deploy the contents of this ZIP as the new root for `corecloud-marketplace.com`, then rerun Lighthouse against:

- `https://www.corecloud-marketplace.com/`
- deployed GitHub Pages preview URL
