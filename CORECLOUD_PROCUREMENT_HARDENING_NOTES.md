# CoreCloud Procurement v2 Hardening Notes

Stabilisation pass completed before linking from CoreCloudZA.

## Changes
- Fixed 404 page stale Dell/product references and missing logo asset references.
- Removed stale CNAME for GitHub project-page deployment testing.
- Updated canonical, Open Graph, JSON-LD, robots.txt and sitemap.xml to the current GitHub Pages deployment path.
- Removed missing legacy sitemap URLs for deleted product/accessory/MSP pages.
- Preserved existing quote cart and bundle detail flow.
- Hardened the custom procurement CTA so `cart.html?custom=1` can submit a quote request even when no standard bundle is in the cart, provided the custom requirements field is used.
- Added custom request focus behaviour on the quote page.
- Revalidated JSON data and internal asset/link references.
- Removed stale public admin generator page and duplicate unreferenced logo directory from the deployable package.

## No-regression boundary
No new bundle categories, pricing logic, checkout provider changes or visual redesign were introduced in this pass.
