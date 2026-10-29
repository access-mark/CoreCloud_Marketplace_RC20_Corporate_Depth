# RC3 commerce service

Run `MARKETPLACE_ADMIN_KEY=<long-random-secret> MARKETPLACE_ORIGIN=https://your-site.example python commerce/server.py`. Local default is 127.0.0.1:8787. Set `MARKETPLACE_DB` to persistent private disk storage.

**Not production ready:** This is an order reservation and administration backend. There is NO payment processing, automatic invoicing, customer login, email dispatch, or live supplier stock sync. Product records are seeded **inactive**, zero-price, zero-stock; publish only verified inventory and VAT-inclusive pricing via the authenticated admin endpoint.

Never deploy this service to GitHub Pages. Deploy behind HTTPS reverse proxy with rate limits, request logs, backups, secret manager, access controls, CSRF/origin restrictions, and operational monitoring. Admin API uses one shared secret for staging only; replace with individual RBAC and MFA before production. Orders hold personal information; implement POPIA retention and deletion policy. Never mark paid based on a client request or unverified gateway webhook. Existing legacy PayFast webhook is **unsafe** (does not validate IPN) and must not be deployed.
