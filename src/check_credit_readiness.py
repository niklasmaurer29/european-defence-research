"""Prevent a credit ranking until comparable source-backed inputs exist."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_REGISTER = PROJECT_ROOT / "research" / "source_register.csv"
REQUIRED_METRICS = {"net financial debt", "interest expense"}


def main() -> None:
    with SOURCE_REGISTER.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))

    metrics_by_company: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        if row["verified"] == "yes" and row["reported_value"].strip():
            metrics_by_company[row["company"]].add(row["metric"])

    print("Credit ranking readiness\n")
    ready = True
    for company in sorted(metrics_by_company):
        missing = sorted(REQUIRED_METRICS - metrics_by_company[company])
        if missing:
            ready = False
            print(f"{company}: INCOMPLETE — missing {', '.join(missing)}")
        else:
            print(f"{company}: READY")

    if not ready:
        print("\nNo credit ranking generated. Complete the audited source register first.")


if __name__ == "__main__":
    main()
