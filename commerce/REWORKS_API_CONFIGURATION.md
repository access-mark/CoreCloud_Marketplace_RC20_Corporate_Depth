# RC12 — ReWorks API integration (disabled by default)

**No ReWorks API specification or credentials have been provided or verified.** The adapter is a configurable integration boundary, not an authenticated live connection.

## Configuration (backend only)
Set `REWORKS_API_ENABLED=false` until a supplier-issued specification and sandbox are verified. The following values must come from ReWorks; do not guess endpoint names or authentication mechanisms:

- `REWORKS_API_BASE_URL` (HTTPS only)
- `REWORKS_API_KEY` (server secret; never place in GitHub Pages)
- `REWORKS_CATALOGUE_PATH`
- `REWORKS_AVAILABILITY_PATH`
- `REWORKS_RESERVE_PATH`
- `REWORKS_ORDERS_PATH`
- `REWORKS_STATUS_PATH`

Current adapter **assumes Bearer authorization, JSON payloads, and an `order_reference` response** as a provisional contract. Replace these mappings only after ReWorks confirms its actual API. Supplier stock, prices, reservations, taxes, delivery fields and status mappings are NOT integrated yet.

## Submission safeguards
`POST /api/admin/reworks/submit` requires `X-Admin-Key`, an order in `paid_sandbox` state and JSON `{"order_id":"CCM-...","approved":true}`. It never auto-submits from a payment notification. Supplier submission is recorded once per CoreCloud order; ambiguous failures require reconciliation and are **not automatically retried** to avoid duplicate purchase orders. This is sandbox orchestration, not a production fulfilment system.

## Before live supplier testing
Obtain ReWorks technical contact, sandbox base URL, authentication and scopes, SKU mapping, stock/reservation semantics, price and VAT basis, delivery schema, create-order idempotency, order confirmation, webhook or polling details, returns process, and agreed supplier account terms. Verify API behaviour with supplier test credentials.

## Known blockers
- No confirmed supplier API, access, contract or supplier test environment.
- No shipping address schema or real courier integration in RC11 checkout.
- No verified supplier reservations or stock synchronisation.
- No production-ready background worker, reconciliation UI, or authentication hardening.
- Do not deploy this as unattended live fulfilment.
