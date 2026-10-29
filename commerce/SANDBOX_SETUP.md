# RC11 — PayFast sandbox setup (NOT LIVE)

1. Register a **Company** account at https://registration.payfast.io/ using **CoreCloud Marketplace (Pty) Ltd**, registration **2015/405028/07**. Upload verification documents requested in the merchant dashboard. Do not share passwords, passphrases or merchant keys in chat or GitHub.
2. Create a separate sandbox account at https://sandbox.payfast.co.za/ and obtain sandbox merchant ID, merchant key and optional passphrase. The sample credentials in the code are public PayFast test credentials, never live credentials.
3. Deploy `commerce/sandbox_server.py` to a **private, persistent HTTPS service** (not GitHub Pages). Use a database volume. Set `MARKETPLACE_DB`, `MARKETPLACE_ADMIN_KEY`, `MARKETPLACE_ORIGIN` (exact GitHub Pages origin, e.g. `https://access-mark.github.io`), `MARKETPLACE_PUBLIC_API_URL`, `MARKETPLACE_PUBLIC_SITE_URL` (site directory ending in `/CoreCloud_Marketplace_RC11_PayFast_Sandbox`), `PAYFAST_SANDBOX_MERCHANT_ID`, `PAYFAST_SANDBOX_MERCHANT_KEY`, `PAYFAST_SANDBOX_PASSPHRASE`.
4. Configure the HTTPS API endpoint in `assets/js/sandbox-checkout.js` as `API_BASE`. Do not put secrets into JavaScript. The PayFast ITN endpoint is `<API>/api/payfast/itn` and must be publicly reachable from PayFast. Configure proxy to preserve a trustworthy client IP; never trust arbitrary `X-Forwarded-For`. Restrict origin, use HTTPS, and protect admin endpoints.
5. Publish **test** SKUs using the existing admin endpoint `/api/admin/product`. All existing products remain inactive/zero-price/zero-stock by design. Test products must be explicitly labelled as test inventory; do not imply real supplier stock.
6. Open `sandbox-checkout.html` to place a sandbox reservation and redirect to the PayFast sandbox wallet. A return-page visit never confirms payment; verified ITN is required to set `paid_sandbox`.
7. Run `python commerce/test_sandbox.py` locally for mocked tests. Real sandbox checkout and ITN delivery remain unverified until a hosted HTTPS API and sandbox account are connected.

## Production blockers
No live merchant activation, supplier stock sync, delivery rate calculations, refunds, order expiry/restock, VAT invoices, staff RBAC/MFA, POPIA controls, monitoring or live gateway tests. The existing quote basket remains separate. **Never switch sandbox endpoints to live by changing a URL alone.**
