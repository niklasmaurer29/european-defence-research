# European Defence: Valuation, Order-Book Growth & Credit Analysis

A reproducible equity-, valuation- and credit-research case study on the
European defence sector. The peer universe is Rheinmetall, Hensoldt and Renk.

## What it does

For each company, the analysis will calculate:

- EBITDA margin
- Net debt / EBITDA
- Enterprise value / EBITDA
- Interest coverage
- A simple, transparent credit score

It produces a ranked screening table and supports a short investment / deal
summary. The current `sample_companies.csv` is a technical demonstration only;
it will be replaced by source-checked reported data.

## Why this project

This is a learning portfolio project for Corporate Finance, Investment Banking,
Credit Research and Capital Markets applications. The final project will cite
the relevant annual reports and record the exact reporting period for each
input. It is educational work, not investment advice.

## Run locally

You only need Python 3:

```bash
python3 src/analyze.py
```

The result is written to `output/screening_results.csv`.

## Project workflow

1. Collect financial data from official annual reports into a source register.
2. Standardise financial metrics and make each calculation auditable.
3. Build a comparable-company table and a valuation range.
4. Write a two-page investment memo with a clear thesis, catalysts and risks.
5. Add charts and a small Streamlit dashboard only after the analysis works.

See `research/01_project_brief.md` for the exact research question and
`research/investment_memo_template.md` for the final written deliverable.
