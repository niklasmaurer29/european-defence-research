"""Interactive FY2025 peer dashboard for the European defence research case.

Run from the project root with:
    python3 -m streamlit run src/dashboard.py

The dashboard intentionally reads only the versioned input CSV files. It is a
historical, definition-aware research screen and does not provide investment
advice or a company ranking.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FACT_BASE_INPUT = PROJECT_ROOT / "data" / "reported_fy2025_summary.csv"
VALUATION_INPUT = PROJECT_ROOT / "data" / "valuation_fy2025_inputs.csv"
CREDIT_INPUT = PROJECT_ROOT / "data" / "credit_fy2025_inputs.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


@st.cache_data
def load_dashboard_data() -> pd.DataFrame:
    """Merge the versioned fact-base, valuation and credit inputs by company."""
    facts = {row["company"]: row for row in read_csv(FACT_BASE_INPUT)}
    valuations = {row["company"]: row for row in read_csv(VALUATION_INPUT)}
    credit = {row["company"]: row for row in read_csv(CREDIT_INPUT)}

    companies = list(facts)
    if set(companies) != set(valuations) or set(companies) != set(credit):
        raise ValueError("The fact-base, valuation and credit files must contain the same companies.")

    rows: list[dict[str, float | str]] = []
    for company in companies:
        fact = facts[company]
        valuation = valuations[company]
        credit_row = credit[company]
        revenue = float(fact["revenue_eur_m"])
        backlog = float(fact["order_backlog_eur_m"])
        ebit = float(valuation["ebit_eur_m"])
        gross_interest = float(credit_row["gross_interest_expense_eur_m"])
        standardised_net_debt = float(valuation["standardised_net_debt_eur_m"])
        market_cap = float(valuation["market_cap_eur_m"])
        enterprise_value = market_cap + standardised_net_debt

        rows.append(
            {
                "Company": company,
                "Revenue (EUR m)": revenue,
                "Reported profitability measure": fact["reported_result_name"],
                "Reported result (EUR m)": float(fact["reported_result_eur_m"]),
                "Backlog (EUR m)": backlog,
                "Backlog / revenue (x)": round(backlog / revenue, 1),
                "Market cap (EUR m)": market_cap,
                "Standardised net debt (EUR m)": standardised_net_debt,
                "Enterprise value (EUR m)": enterprise_value,
                "IFRS EBIT (EUR m)": ebit,
                "EV / EBIT (x)": round(enterprise_value / ebit, 1),
                "EBIT / gross interest expense (x)": round(ebit / gross_interest, 1),
                "Credit definition": credit_row["coverage_definition"],
                "Comparability note": fact["comparability_note"],
                "Valuation note": valuation["definition_note"],
                "Credit source note": credit_row["source_note"],
            }
        )

    return pd.DataFrame(rows)


def eur_m(value: float, digits: int = 0) -> str:
    """Format a euro amount in millions, retaining the net-liquidity sign."""
    return f"EUR {value:,.{digits}f}m"


def main() -> None:
    st.set_page_config(page_title="European Defence FY2025", page_icon="📊", layout="wide")
    st.title("European Defence FY2025 Peer Screen")
    st.caption(
        "Rheinmetall, Hensoldt and RENK | Historical market-data date: 31 December 2025"
    )
    st.info(
        "Educational research only. This definition-aware screen is not investment advice "
        "and does not produce a buy, hold or sell recommendation."
    )

    data = load_dashboard_data()
    selected_company = st.selectbox("Select a company", data["Company"].tolist())
    selected = data.loc[data["Company"] == selected_company].iloc[0]

    st.subheader(f"{selected_company}: FY2025 snapshot")
    metrics = st.columns(4)
    metrics[0].metric("Revenue", eur_m(selected["Revenue (EUR m)"]))
    metrics[1].metric("Backlog / revenue", f"{selected['Backlog / revenue (x)']:.1f}x")
    metrics[2].metric("EV / EBIT", f"{selected['EV / EBIT (x)']:.1f}x")
    metrics[3].metric(
        "EBIT / gross interest expense",
        f"{selected['EBIT / gross interest expense (x)']:.1f}x",
    )

    st.subheader("Peer comparison")
    chart_metric = st.selectbox(
        "Metric",
        [
            "EV / EBIT (x)",
            "Backlog / revenue (x)",
            "EBIT / gross interest expense (x)",
            "Standardised net debt (EUR m)",
        ],
        help="Negative standardised net debt indicates net liquidity.",
    )
    chart_data = data.set_index("Company")[[chart_metric]]
    st.bar_chart(chart_data, width="stretch")

    st.subheader("Source-backed metrics")
    display_columns = [
        "Company",
        "Revenue (EUR m)",
        "Backlog (EUR m)",
        "Backlog / revenue (x)",
        "Standardised net debt (EUR m)",
        "EV / EBIT (x)",
        "EBIT / gross interest expense (x)",
    ]
    st.dataframe(
        data[display_columns],
        column_config={
            "Revenue (EUR m)": st.column_config.NumberColumn(format="EUR %.0f m"),
            "Backlog (EUR m)": st.column_config.NumberColumn(format="EUR %.0f m"),
            "Backlog / revenue (x)": st.column_config.NumberColumn(format="%.1fx"),
            "Standardised net debt (EUR m)": st.column_config.NumberColumn(format="EUR %.1f m"),
            "EV / EBIT (x)": st.column_config.NumberColumn(format="%.1fx"),
            "EBIT / gross interest expense (x)": st.column_config.NumberColumn(format="%.1fx"),
        },
        hide_index=True,
        width="stretch",
    )

    with st.expander("Methodology and comparability cautions"):
        st.markdown(
            "- Enterprise value equals market capitalisation plus standardised net debt. "
            "The date is fixed at 31 December 2025 for all three companies.\n"
            "- EV / EBIT is used instead of EV / EBITDA because the issuers' disclosed "
            "profitability measures are not yet fully harmonised.\n"
            "- Standardised net debt includes lease liabilities where the underlying inputs "
            "were available. Negative net debt denotes net liquidity.\n"
            "- Interest coverage is EBIT divided by gross interest expense. It is a screening "
            "diagnostic, not a covenant ratio or credit score."
        )

    with st.expander(f"{selected_company}: source and definition notes"):
        st.markdown(f"**Reported profitability measure:** {selected['Reported profitability measure']}")
        st.markdown(f"**Fact-base caution:** {selected['Comparability note']}")
        st.markdown(f"**Valuation note:** {selected['Valuation note']}")
        st.markdown(f"**Credit source:** {selected['Credit source note']}")

    st.caption(
        "Audit trail: research/source_register.csv, research/04_credit_evidence.md "
        "and research/05_valuation_method.md."
    )


if __name__ == "__main__":
    main()
