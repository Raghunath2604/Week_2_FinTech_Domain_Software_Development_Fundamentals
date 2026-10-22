"""Offline unit test for the JSON normalization logic in api_extract.py.

This test mocks the HTTP response, so it can run without internet access.
Run: python -m unittest discover -s "Source Code" -p "test_*.py"
"""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

script_path = Path(__file__).with_name("api_extract.py")
spec = importlib.util.spec_from_file_location("api_extract", script_path)
api_extract = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(api_extract)

class FakeResponse:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code
        self.url = "https://api.frankfurter.dev/v2/rates?base=USD&quotes=INR"
    def raise_for_status(self):
        if self.status_code >= 400:
            import requests
            raise requests.exceptions.HTTPError(f"HTTP {self.status_code} Error", response=self)
    def json(self):
        return self._payload

class FetchRatesTests(unittest.TestCase):
    @patch.object(api_extract.requests, "get")
    def test_fetch_rates_normalizes_rows(self, mock_get):
        mock_get.return_value = FakeResponse([
            {"date": "2026-10-15", "base": "USD", "quote": "INR", "rate": 88.1},
            {"date": "2026-10-15", "base": "USD", "quote": "EUR", "rate": 0.86},
        ])
        rows = api_extract.fetch_rates("usd", ["inr", "eur"])
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["base"], "USD")
        self.assertEqual(rows[0]["quote"], "INR")
        self.assertIsInstance(rows[0]["rate"], float)
        self.assertEqual(mock_get.call_args.kwargs["params"]["base"], "USD")

    @patch.object(api_extract.requests, "get")
    def test_empty_payload_raises_clear_error(self, mock_get):
        mock_get.return_value = FakeResponse([])
        with self.assertRaisesRegex(RuntimeError, "No usable rate rows"):
            api_extract.fetch_rates("USD", ["INR"])

    @patch.object(api_extract.requests, "get")
    def test_invalid_json_raises_runtime_error(self, mock_get):
        class InvalidJsonResponse(FakeResponse):
            def json(self):
                raise ValueError("Expecting value: line 1 column 1 (char 0)")
        mock_get.return_value = InvalidJsonResponse(None)
        with self.assertRaisesRegex(RuntimeError, "The API response was not valid JSON"):
            api_extract.fetch_rates("USD", ["INR"])

    @patch.object(api_extract.requests, "get")
    def test_http_request_exception_handled(self, mock_get):
        import requests
        mock_get.side_effect = requests.RequestException("Connection timeout")
        with self.assertRaisesRegex(RuntimeError, "API request failed"):
            api_extract.fetch_rates("USD", ["INR"])

    @patch.object(api_extract.requests, "get")
    def test_http_4xx_client_error_handled(self, mock_get):
        mock_get.return_value = FakeResponse({"message": "Not Found"}, status_code=404)
        with self.assertRaisesRegex(RuntimeError, "API request failed: HTTP 404 Error"):
            api_extract.fetch_rates("USD", ["XYZ"])

    @patch.object(api_extract.requests, "get")
    def test_http_5xx_server_error_handled(self, mock_get):
        mock_get.return_value = FakeResponse({"message": "Server Error"}, status_code=500)
        with self.assertRaisesRegex(RuntimeError, "API request failed: HTTP 500 Error"):
            api_extract.fetch_rates("USD", ["INR"])

    @patch.object(api_extract.requests, "get")
    def test_api_error_message_payload(self, mock_get):
        mock_get.return_value = FakeResponse({"message": "Invalid base currency"})
        with self.assertRaisesRegex(RuntimeError, "API returned an error: Invalid base currency"):
            api_extract.fetch_rates("INVALID", ["INR"])

    @patch.object(api_extract.requests, "get")
    def test_skips_malformed_records(self, mock_get):
        mock_get.return_value = FakeResponse([
            {"date": "2026-10-22", "base": "USD"},  # Missing quote and rate
            {"date": "2026-10-22", "base": "USD", "quote": "INR", "rate": 94.51},
        ])
        rows = api_extract.fetch_rates("USD", ["INR"])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["quote"], "INR")
        self.assertEqual(rows[0]["rate"], 94.51)

    def test_deduplication_parity_records(self):
        import pandas as pd
        raw_rows = [
            {"date": "2026-10-22", "base": "USD", "quote": "INR", "rate": 94.51},
            {"date": "2026-10-22", "base": "USD", "quote": "INR", "rate": 94.51}, # duplicate
            {"date": "2026-10-22", "base": "USD", "quote": "EUR", "rate": 0.88964},
        ]
        df = pd.DataFrame(raw_rows).drop_duplicates(subset=["date", "base", "quote"]).sort_values(["date", "quote"])
        clean_records = df.to_dict(orient="records")
        self.assertEqual(len(clean_records), 2)
        self.assertEqual(len(df), 2)
        self.assertEqual(clean_records[0]["quote"], "EUR")
        self.assertEqual(clean_records[1]["quote"], "INR")

if __name__ == "__main__":
    unittest.main()
