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
            raise RuntimeError(f"HTTP {self.status_code}")
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

if __name__ == "__main__":
    unittest.main()
