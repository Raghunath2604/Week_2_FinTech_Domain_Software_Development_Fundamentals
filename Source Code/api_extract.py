#!/usr/bin/env python3
"""Fetch currency reference rates from Frankfurter API and export JSON + CSV.

Default endpoint: https://api.frankfurter.dev/v2/rates?base=USD&quotes=INR,EUR,GBP,JPY
No API key is required. This is a learning example for reference-rate analytics,
not a trading feed. Requires internet access and the requests package.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from typing import Any
import requests
import pandas as pd

API_BASE = "https://api.frankfurter.dev/v2/rates"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "Datasets"


def fetch_rates(base: str, quotes: list[str], date_from: str | None = None,
                date_to: str | None = None) -> list[dict[str, Any]]:
    """Call the public endpoint, validate the status, and normalize rows."""
    params: dict[str, str] = {"base": base.upper(), "quotes": ",".join(q.upper() for q in quotes)}
    # Date filters make a timeseries request. If no date is supplied, API returns latest available quotes.
    if date_from:
        params["from"] = date_from
    if date_to:
        params["to"] = date_to

    try:
        response = requests.get(API_BASE, params=params, timeout=30,
                                headers={"Accept": "application/json", "User-Agent": "Week2-Analytics-Learning/1.0"})
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"API request failed: {exc}. Check your internet connection and endpoint.") from exc

    try:
        payload = response.json()
    except ValueError as exc:
        raise RuntimeError("The API response was not valid JSON.") from exc

    # The v2 rates endpoint is expected to return a list of rate objects.
    if isinstance(payload, dict) and "message" in payload:
        raise RuntimeError(f"API returned an error: {payload.get('message')}")
    if isinstance(payload, dict) and "rates" in payload:
        payload = payload["rates"]
    if not isinstance(payload, list):
        raise RuntimeError(f"Unexpected response shape: expected a JSON array, got {type(payload).__name__}.")

    rows: list[dict[str, Any]] = []
    required = {"date", "base", "quote", "rate"}
    for record in payload:
        if not isinstance(record, dict) or not required.issubset(record):
            continue
        rows.append({
            "date": str(record["date"]),
            "base": str(record["base"]).upper(),
            "quote": str(record["quote"]).upper(),
            "rate": float(record["rate"]),
        })
    if not rows:
        raise RuntimeError("No usable rate rows were returned. Check the requested currencies/dates.")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="USD", help="Base currency code, e.g. USD (default: USD)")
    parser.add_argument("--quotes", nargs="+", default=["INR", "EUR", "GBP", "JPY"],
                        help="Quote currency codes (default: INR EUR GBP JPY)")
    parser.add_argument("--from-date", dest="date_from", help="Optional start date YYYY-MM-DD for a time series")
    parser.add_argument("--to-date", dest="date_to", help="Optional end date YYYY-MM-DD for a time series")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUTPUT_DIR,
                        help="Output directory (default: project Datasets folder)")
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    try:
        rows = fetch_rates(args.base, args.quotes, args.date_from, args.date_to)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    df = pd.DataFrame(rows).drop_duplicates(subset=["date", "base", "quote"]).sort_values(["date", "quote"])
    json_path = args.out_dir / "fx_rates_api_response.json"
    csv_path = args.out_dir / "fx_rates_api.csv"
    json_path.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    df.to_csv(csv_path, index=False)

    print(f"HTTP request successful. Rows exported: {len(df)}")
    print(f"JSON: {json_path}")
    print(f"CSV:  {csv_path}")
    print("Preview:")
    print(df.head(10).to_string(index=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
