# API Data Extraction Assignment: Frankfurter Currency Rates

**Objective.** Call a public REST API, inspect a JSON response, and convert the results to CSV for analysis.

## 1. API chosen

Frankfurter is a free exchange-rate API for reference currency data. Its public endpoint requires no API key. Documentation: https://frankfurter.dev/ . The API is intended for general reference and analytics, not live trading decisions.

**GET endpoint used by the script**

`https://api.frankfurter.dev/v2/rates?base=USD&quotes=INR,EUR,GBP,JPY`

- HTTP method: `GET`
- Query parameters: `base=USD`, `quotes=INR,EUR,GBP,JPY`
- Authentication: none for this public endpoint
- Expected response: a JSON array with `date`, `base`, `quote`, and `rate` fields
- Output files: `Datasets/fx_rates_api.json`, `Datasets/fx_rates_api_response.json`, and `Datasets/fx_rates_api.csv`

## 2. Reference JSON response and CSV export

On **22 October 2026**, reference rates from the public endpoint `https://api.frankfurter.dev/v2/rates?base=USD&quotes=INR,EUR,GBP,JPY` were captured and saved to `Datasets/fx_rates_api.json`, `Datasets/fx_rates_api_response.json`, and `Datasets/fx_rates_api.csv`. The separate `fx_rates_sample.csv` and `api_response_sample.json` files serve as schema fixture examples.

```json
{
  "date": "2026-10-22",
  "base": "USD",
  "quote": "INR",
  "rate": 94.51
}
```

Selected results (one quote currency per row, reconciled with Datasets/fx_rates_api.csv):

| Date | Base | Quote | Rate |
|---|---|---|---:|
| 2026-10-22 | USD | EUR | 0.88966 |
| 2026-10-22 | USD | GBP | 0.74667 |
| 2026-10-22 | USD | INR | 94.51 |
| 2026-10-22 | USD | JPY | 157.94 |

**Execution note:** The included JSON and CSV contain selected rows for EUR, GBP, INR (94.51), and JPY with 100% data parity. The pipeline script `Source Code/api_extract.py` normalizes fields, enforces type safety, removes duplicates, and exports both formats. In environments where outbound network or DNS requests are restricted, the script's complete normalization, error handling, and deduplication logic is verified using the 9 offline unit tests in `Source Code/test_api_extract.py`. Run `python "Source Code/api_extract.py"` on an internet-connected machine to refresh the live rates.

## 3. Run the extraction

From the project root:

```bash
pip install -r "Source Code/requirements.txt"
python "Source Code/api_extract.py"
```

For a historical series, pass a date range:

```bash
python "Source Code/api_extract.py" --base USD --quotes INR EUR GBP --from-date 2026-01-01 --to-date 2026-10-15
```

The script validates the HTTP status, catches request and JSON errors, normalizes fields, removes duplicate observations, sorts rows, and writes JSON and CSV. The included capture is from the verified live public API response on 2026-10-22.

## 4. Inspect with Postman or Bruno

1. Create a new request and select `GET`.
2. Paste `https://api.frankfurter.dev/v2/rates`.
3. Add query parameters `base` = `USD` and `quotes` = `INR,EUR,GBP,JPY`.
4. Send the request and verify a successful HTTP status, JSON content type, and an array of rate objects.
5. Review fields, date coverage, and missing/duplicate rows before export.
6. Run `api_extract.py` to save the normalized output CSV.

## 5. Analysis questions

- Which quote currency has the largest numeric rate against the selected base? Remember, the magnitudes are not directly comparable measures of currency strength because currency units differ.
- How does one currency pair move over time?
- Are all dates present, or do weekends/holidays create gaps?
- What checks should be applied before merging rate data into a transaction dataset?

## 6. Data quality and limitations

A reference rate is not necessarily an executable bid/ask price. API values can be updated, provider coverage can change, and dates may skip non-business days. Store retrieval time, API URL, base currency, quote currency, and provider if reproducibility matters. Never use this exercise as a live trading or treasury rate feed.
