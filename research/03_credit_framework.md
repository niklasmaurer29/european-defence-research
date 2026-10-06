# Credit framework — definition before ranking

## Purpose

The goal is to assess debt capacity across Rheinmetall, Hensoldt and Renk
without treating different company disclosures as if they were identical.

## Required measures

| Measure | Formula | Why it matters |
|---|---|---|
| Reported net debt | Use each issuer's disclosed definition first; record whether it includes lease and other financial liabilities. | Shows the issuer-reported net debt burden without silently changing its definition. |
| Standardised net debt | Financial debt + lease liabilities - cash and cash equivalents, when all three inputs are source-backed. | Enables a like-for-like peer comparison, separately from reported net debt. |
| Net leverage | Net debt / adjusted EBITDA | Relates debt to recurring earnings capacity. |
| Interest coverage | EBIT / net interest expense | Indicates how easily operating profit covers financing costs. |
| Free-cash-flow conversion | Free cash flow / reported earnings measure | Tests whether reported profitability converts into cash. |

## Current evidence status

| Company | Current evidence | What remains before peer ranking |
|---|---|---|
| Rheinmetall | Audited net liquidity of EUR 369m, lease liabilities of EUR 306m, and net interest expense of EUR 112m. | Its financial-debt total includes leasing, unlike Hensoldt's reported net-debt table. No peer ranking yet. |
| Hensoldt | Audited net debt of **EUR -297m** (net cash) and gross interest expense of EUR 106m; management also reports net leverage of 1.6x. | Lease liabilities are excluded from its reported net-debt table, and the covenant definition behind the 1.6x metric remains company-specific. No peer ranking yet. |
| Renk | Audited financial liabilities of EUR 535.3m, cash of EUR 187.1m, lease liabilities of EUR 18.5m and interest expense of EUR 33.8m. | No separately reported interest-income line; use gross interest expense for the interim coverage diagnostic. |

## Analytical rule

No company receives a "best credit profile" label until all three have a
source-backed, comparable net-debt and interest-coverage measure. A missing
value stays `INCOMPLETE`; it is never interpreted as zero debt or low risk.

## Hensoldt definition check

Hensoldt's FY2025 annual report defines net debt as current and non-current
financing liabilities plus other financial liabilities, less cash and cash
equivalents. It explicitly excludes lease liabilities from that net-debt table.
The resulting reported value is EUR -297m, i.e. net cash, at 31 December 2025.

This should not be confused with the separately disclosed 1.6x net-leverage
ratio. That ratio is linked to a syndicated-loan covenant using "consolidated
EBITDA" as defined in the loan agreement. The project retains both disclosures
but does not use either as a cross-company ranking input until the equivalent
definitions for Rheinmetall and Renk have been collected.

## Rheinmetall definition check

Rheinmetall reports EUR 1,281m of financial debts and EUR 1,650m of cash and
cash equivalents at 31 December 2025, which it presents as **EUR 369m net
liquidity**. Its financial-debt note includes EUR 306m of leasing. This means
that Rheinmetall's reported measure is not like-for-like with Hensoldt's
reported net-debt table, which excludes lease liabilities.

Rheinmetall reported EBIT of EUR 1,684m, interest expense of EUR 116m and
interest income of EUR 4m. Its EUR 112m net interest expense therefore gives a
standalone EBIT / net-interest-expense calculation of 15.0x. This is retained
as issuer-specific evidence, not as a relative credit ranking.

## RENK definition check

RENK reports total financial liabilities of EUR 535.3m, including EUR 18.5m of
lease liabilities, and cash and cash equivalents of EUR 187.1m at 31 December
2025. The project therefore calculates **EUR 348.2m standardised net debt** as
financial liabilities less cash. This is a transparent project calculation, not
an issuer-reported net-debt line.

RENK's income statement reports operating profit of EUR 169.4m and interest
expense of EUR 33.8m, but no separately reported interest-income line. The
interim coverage diagnostic therefore uses gross interest expense: 5.0x. RENK
also reports a 1.7x consolidated net-leverage covenant ratio, which remains
issuer-specific.

## What this lets me say in an interview

> I began with operational fundamentals, but I did not turn incomplete or
> differently defined debt disclosures into a simplistic credit ranking. I
> documented the definitions first, then completed leverage and interest
> coverage on a comparable basis before drawing a conclusion.
