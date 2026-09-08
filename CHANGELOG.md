# Changelog

## 0.2.0 — 2026-09-09

- Update xena-client, xena-order, xena-finance and xena-subscription to 0.2.0. Other domain packages remain at 0.1.0.
- Add six OrderTaskBudgetPost operations, OrderTaskLine/DeleteLines and ResourcePost/Totals to xena-order.
- Add PaymentExportDraft/{contextId}/ByPaymentIds to xena-finance.
- Add optional exclude_article_groups_without_number to LedgerAccount GET and is_active to Subscription GET. New arguments follow all existing positional arguments.
- Preserve existing method names and Document/Inbox.query_string for compatibility; the latter is absent from current Swagger but its runtime support is unverified.
- Track the public Swagger snapshot used for this update under specs/. Source: https://my.xena.biz/api/swagger/docs/v1. SHA-256: 948a617516198ce453cb5e4a00326ea3d6837d22c1ea6a7ab70dc9e19964c9c6.

This update aligns endpoint and parameter coverage. It does not assert that all historical JSON schemas or server behavior are unchanged. HTTPS remains the default.
