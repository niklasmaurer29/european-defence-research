"""Prevent a credit ranking until comparable source-backed inputs exist."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_REGISTER = PROJECT_ROOT / "research" / "source_register.csv"
# Issuers may use either label. The source register preserves the label used in
# the report instead of forcing a false standardisation at data-entry stage.
REQUIRED_EVIDENCE = {
    "net debt evidence": {"net debt", "net financial debt", "standardised net debt"},
    "interest expense": {"interest expense"},
}


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
        missing = sorted(
            evidence
            for evidence, accepted_labels in REQUIRED_EVIDENCE.items()
            if not metrics_by_company[company].intersection(accepted_labels)
        )
        if missing:
            ready = False
            print(f"{company}: INCOMPLETE — missing {', '.join(missing)}")
        else:
            print(f"{company}: SOURCE INPUTS CAPTURED — check definition before peer comparison")

    if not ready:
        print("\nNo peer credit ranking generated. Complete the audited source register first.")
    else:
        print("\nNo automatic peer credit ranking generated. Review the qualitative definition notes before any conclusion.")


if __name__ == "__main__":
    main()
