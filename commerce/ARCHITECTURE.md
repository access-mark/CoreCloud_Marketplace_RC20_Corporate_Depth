# RC3 architecture

Existing business procurement pages are retained. New `shop.html` is the personal storefront; `assets/js/commerce-rc3.js` calls the standalone Python `commerce/server.py` API. SQLite stores stock and reservations. Admin endpoints are staging-only. Orders are reserved pending manual review; there is no online payment or customer authentication.

Production recommendation: move to managed PostgreSQL, authenticated staff dashboard with MFA/RBAC, payment service adapter with PayFast IPN verification and reconciliation, Sage integration, supplier stock import and operational notifications. GitHub Pages cannot run the Python backend. Configure a same-origin reverse proxy or explicit API base and appropriate CORS/security controls before production.
