# CoreCloud Procurement v2.1 - Lead Capture Notes

This pass keeps the hardened v2 site stable and adds FormSubmit lead capture for live testing.

## Lead capture routing

- Form endpoint: `https://formsubmit.co/sales@corecloudza.com`
- CC: `mark@corecloudza.com`
- Template: table
- Captcha: enabled
- Thank-you redirect: `/thank-you.html`

## Submission subjects

Subjects are set dynamically before submit:

- `[Procurement] <Bundle Name>` for a single selected bundle
- `[Procurement] Multiple bundle quote request` for carts with multiple bundle types
- `[Custom Procurement] <Company>` for custom procurement requests with no cart items

## Metadata captured

Each submission includes:

- source: CoreCloud Procurement
- submission_type
- submission_date
- page_url
- bundle_summary
- deployment_summary
- cart_contents
- user_profile_json, when local profile data exists

## Important first-use note

FormSubmit normally requires email activation on first submission for the recipient address. Submit one test form and approve the activation email for `sales@corecloudza.com` before relying on live traffic.
