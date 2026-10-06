"""Screen fictional companies using simple IB and credit-research metrics.

All figures in data/sample_companies.csv are fictional and in EUR millions.
The calculations are intentionally explicit so a reviewer can trace them.
"""

from __future__ import annotations

import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "sample_companies.csv"
OUTPUT_FILE = PROJECT_ROOT / "output" / "screening_results.csv"


def as_number(value: str) -> float:
    return float(value)


def credit_score(net_debt_to_ebitda: float, interest_coverage: float) -> str:
    """Classify leverage and debt-service capacity with disclosed thresholds."""
    if net_debt_to_ebitda <= 2.0 and interest_coverage >= 5.0:
        return "Strong"
    if net_debt_to_ebitda <= 3.5 and interest_coverage >= 2.5:
        return "Moderate"
    return "Higher risk"


def analyse_company(row: dict[str, str]) -> dict[str, str | float]:
    revenue = as_number(row["revenue_eur_m"])
    ebitda = as_number(row["ebitda_eur_m"])
    net_debt = as_number(row["net_debt_eur_m"])
    enterprise_value = as_number(row["enterprise_value_eur_m"])
    ebit = as_number(row["ebit_eur_m"])
    interest_expense = as_number(row["interest_expense_eur_m"])
    order_backlog = as_number(row["order_backlog_eur_m"])

    ebitda_margin = ebitda / revenue
    net_debt_to_ebitda = net_debt / ebitda
    ev_to_ebitda = enterprise_value / ebitda
    interest_coverage = ebit / interest_expense
    backlog_to_revenue = order_backlog / revenue

    return {
        "company": row["company"],
        "sector": row["sector"],
        "revenue_eur_m": revenue,
        "ebitda_margin_pct": round(ebitda_margin * 100, 1),
        "net_debt_to_ebitda_x": round(net_debt_to_ebitda, 2),
        "ev_to_ebitda_x": round(ev_to_ebitda, 2),
        "interest_coverage_x": round(interest_coverage, 2),
        "order_backlog_to_revenue_x": round(backlog_to_revenue, 2),
        "credit_score": credit_score(net_debt_to_ebitda, interest_coverage),
    }


def main() -> None:
    with INPUT_FILE.open(newline="", encoding="utf-8") as source:
        results = [analyse_company(row) for row in csv.DictReader(source)]

    results.sort(key=lambda result: float(result["net_debt_to_ebitda_x"]))
    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    fields = list(results[0].keys())
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as destination:
        writer = csv.DictWriter(destination, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    print("Deal & Credit Analyzer — fictional example data only\n")
    for result in results:
        print(
            f"{result['company']}: "
            f"{result['net_debt_to_ebitda_x']}x Net Debt/EBITDA | "
            f"{result['order_backlog_to_revenue_x']}x backlog/revenue | "
            f"{result['ev_to_ebitda_x']}x EV/EBITDA | "
            f"{result['credit_score']} credit profile"
        )
    print(f"\nSaved detailed output to: {OUTPUT_FILE.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
