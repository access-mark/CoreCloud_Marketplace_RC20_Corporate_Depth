# CoreCloud Marketplace RC2 — source upgrade and launch gates

## Implemented
- Responsive shell / header widths across existing pages; personal purchasing redesigned with filtered product catalogue, session quote basket, individual enquiry form, and employee referral landing page.
- No unverified stock, pricing, discount, warranty, delivery or bank endorsement claims.
- FormSubmit is used for the personal enquiry. Business procurement, Sage and PayFast integration code is retained without claiming it is operational.

## Critical blockers before calling this a fully transactional portal
1. GitHub Pages hosts static files only: `/api` Node serverless handlers do not execute on GitHub Pages. Deploy APIs to a supported backend with environment secrets, authentication, logging, rate limits and payment webhook validation.
2. Live supplier stock and individual unit pricing feed, SKU inventory reservation, order persistence, VAT invoices, courier integration and returns workflow are not implemented.
3. PayFast merchant verification, signed server-side payment initiation, idempotent webhooks and reconciliation need live sandbox tests. Do not accept card payments via static HTML.
4. Sage credentials, contact/quote/invoice workflows, and business cart regression tests need secure environment validation.
5. FormSubmit destination activation and real delivery must be verified. Consumer terms/POPIA/privacy/CPA and warranty policies need legal review.
6. Cross-browser and mobile visual QA is pending; source-level syntax checks only.

## Staging entry points
- `employee-purchase.html`: individual product selection and quote basket
- `employee-programme.html`: non-branded employer referral entry page
- `index.html`: existing business procurement homepage, with personal purchasing link

## Important
This is a significantly expanded **quote-first frontend**, not a completed live transactional backend. Do not publish as an operational checkout until all launch gates pass.
