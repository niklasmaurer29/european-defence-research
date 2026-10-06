"""Build a definition-aware FY2025 enterprise-value screening table.

The script uses 31 December 2025 market capitalisation for every issuer so the
market-data date matches the FY2025 financial statements. It calculates EV / EBIT
only: reported EBITDA labels are not sufficiently harmonised across the peer set.
"""

from __future__ import annotations

import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "valuation_fy2025_inputs.csv"
OUTPUT_FILE = PROJECT_ROOT / "output" / "fy2025_valuation_screen.csv"


def build_row(row: dict[str, str]) -> dict[str, str | float]:
    market_cap = float(row["market_cap_eur_m"])
    net_debt = float(row["standardised_net_debt_eur_m"])
    ebit = float(row["ebit_eur_m"])
    enterprise_value = market_cap + net_debt

    return {
        "company": row["company"],
        "valuation_date": row["valuation_date"],
        "market_cap_eur_m": market_cap,
        "standardised_net_debt_eur_m": net_debt,
        "enterprise_value_eur_m": round(enterprise_value, 3),
        "ebit_eur_m": ebit,
        "ev_to_ebit_x": round(enterprise_value / ebit, 1),
        "definition_note": row["definition_note"],
    }


def main() -> None:
    with INPUT_FILE.open(newline="", encoding="utf-8") as source:
        results = [build_row(row) for row in csv.DictReader(source)]

    dates = {row["valuation_date"] for row in results}
    if dates != {"2025-12-31"}:
        raise ValueError("All valuation inputs must use the 2025-12-31 observation date.")

    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as destination:
        writer = csv.DictWriter(destination, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)

    print("FY2025 European Defence Valuation Screen\n")
    for row in results:
        print(
            f"{row['company']}: EV EUR {row['enterprise_value_eur_m']:,.1f}m | "
            f"EV / EBIT {row['ev_to_ebit_x']}x"
        )
    print("\nImportant: this is an EV / EBIT screen, not EV / EBITDA or investment advice.")
    print(f"Saved valuation screen to: {OUTPUT_FILE.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
