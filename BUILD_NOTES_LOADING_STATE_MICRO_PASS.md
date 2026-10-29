# CoreCloud Marketplace - Loading State Micro Pass

Date: 29 June 2026

## Purpose
Final homepage polish pass after the production performance pass.

## Changes
- Removed the visible homepage "Loading... / Pulling bundle details..." state.
- Added a static highlighted bundle fallback for the Sales Team Deployment Bundle.
- Added static bundle cards into the initial HTML so the page has meaningful content before JavaScript fetches JSON.
- Preserved the existing dynamic JSON-driven rendering once bundle data loads.
- Changed JSON fetch failure behaviour so it preserves the static fallback cards instead of replacing the section with an error state.
- Fixed a duplicate JavaScript `const top` declaration in the homepage render function.

## Expected impact
- Better first impression on GitHub Pages and slower connections.
- Lower perceived layout shift around the highlighted bundle and featured bundle grid.
- Safer rendering if `bundles.by_promotion.json` is delayed or unavailable.

## Design impact
No visual redesign. This is a stability and production-polish pass only.
