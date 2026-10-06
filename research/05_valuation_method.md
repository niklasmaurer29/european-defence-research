# Valuation screen - a common market-data date

## Date and scope

This screen uses **31 December 2025** as the valuation date for every company.
That aligns market capitalisation with the FY2025 audited financial statements
already used in the fact base. It is a historical research snapshot, not a
live-price recommendation.

## Formula

```text
Enterprise value = market capitalisation + standardised net debt
EV / EBIT = enterprise value / IFRS EBIT
```

For this project, standardised net debt includes lease liabilities where the
underlying inputs are available. Negative net debt denotes net liquidity.

## Source-backed result

| Company | Market cap | Standardised net debt | Enterprise value | IFRS EBIT | EV / EBIT |
|---|---:|---:|---:|---:|---:|
| Rheinmetall | EUR 71,810m | EUR -369m | EUR 71,441m | EUR 1,684m | 42.4x |
| Hensoldt | EUR 8,478m | EUR 748m | EUR 9,226m | EUR 221m | 41.7x |
| RENK | EUR 5,362m | EUR 348.2m | EUR 5,710.2m | EUR 169.4m | 33.7x |

## Market-data evidence

- **Rheinmetall:** official investor-relations table reports EUR 71.81bn stock
  market value at the end of 2025.
- **Hensoldt:** Annual Report 2025, p. 14, reports a EUR 73.40 Xetra closing
  price and EUR 8.478bn market capitalisation at 31 December 2025.
- **RENK:** official historical-price lookup reports a EUR 53.62 2025 Xetra
  annual close. Annual Report 2025, p. 188, confirms 100.0m shares, resulting
  in EUR 5.362bn market capitalisation.

## What the screen does and does not say

This screen makes the peer-set valuation visible on a single, auditable date.
It does **not** claim that the lowest multiple is automatically the most
attractive company. Backlog definitions, growth, capital intensity, the mix of
defence exposure and the precise meaning of each company's EBIT must be tested
before writing an investment conclusion.

EV / EBITDA is intentionally excluded. The existing source set contains
operating result, adjusted EBITDA and adjusted EBIT disclosures that are not
yet aligned. Using a common IFRS EBIT denominator is the more defensible first
screen.

## How to explain this in an interview

> I fixed the valuation date at the FY2025 year-end, used issuer or exchange
> sources for equity value, reconciled cash, debt and leases into enterprise
> value, and used EV / EBIT rather than forcing unlike EBITDA definitions into
> a multiple. The output is a screening tool; the investment conclusion comes
> only after analysing growth, backlog conversion and risks.
