"""Build an auditable FY2025 defence-sector fact base from reported figures.

This script deliberately does not calculate a valuation or a common credit
score. Rheinmetall, Hensoldt and Renk disclose different profitability and
backlog definitions. The output preserves these labels and marks where a
comparison needs further reconciliation.
"""

from __future__ import annotations

import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "reported_fy2025_summary.csv"
OUTPUT_FILE = PROJECT_ROOT / "output" / "fy2025_fact_base.csv"


def number(value: str) -> float | None:
    return float(value) if value.strip() else None


def build_row(row: dict[str, str]) -> dict[str, str | float]:
    revenue = float(row["revenue_eur_m"])
    reported_result = float(row["reported_result_eur_m"])
    reported_margin = float(row["reported_result_margin_pct"])
    backlog = float(row["order_backlog_eur_m"])
    net_leverage = number(row["reported_net_leverage_x"])

    return {
        "company": row["company"],
        "fiscal_year": row["fiscal_year"],
        "revenue_eur_m": revenue,
        "reported_result_name": row["reported_result_name"],
        "reported_result_eur_m": reported_result,
        "reported_result_margin_pct": reported_margin,
        "order_backlog_eur_m": backlog,
        "backlog_to_revenue_x": round(backlog / revenue, 1),
        "reported_net_leverage_x": "" if net_leverage is None else net_leverage,
        "comparability_note": row["comparability_note"],
    }


def main() -> None:
    with INPUT_FILE.open(newline="", encoding="utf-8") as source:
        results = [build_row(row) for row in csv.DictReader(source)]

    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as destination:
        writer = csv.DictWriter(destination, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)

    print("FY2025 European Defence Fact Base\n")
    for result in results:
        print(
            f"{result['company']}: "
            f"{result['reported_result_margin_pct']}% "
            f"{result['reported_result_name']} margin | "
            f"{result['backlog_to_revenue_x']}x backlog/revenue"
        )
    print("\nImportant: reported result and backlog definitions are retained as disclosed.")
    print("Do not treat them as fully comparable until the source definitions are reconciled.")
    print(f"\nSaved fact base to: {OUTPUT_FILE.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
