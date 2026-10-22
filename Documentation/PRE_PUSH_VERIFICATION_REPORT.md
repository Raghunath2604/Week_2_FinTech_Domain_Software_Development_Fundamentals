# Pre-Submission Verification & Quality Report: Week 2 FinTech Fundamentals

**Review Date:** 22 October 2026
**Prepared By:** RAGHUNATHAREDDY GR (FinTech Research Intern)
**Project Directory:** `Week_2_FinTech_Domain_Software_Development_Fundamentals/`
**Git Branch:** `main`
**Target Remote:** `https://github.com/Raghunath2604/Week_2_FinTech_Domain_Software_Development_Fundamentals.git`
**Review Status:** **VERIFIED PASS & READY FOR SUBMISSION**

---

## 1. Project Location and Required Structure Checklist

| Target Item | Expected Path | Found Status | Notes |
|---|---|---|---|
| Project Root | `Week_2_FinTech_Domain_Software_Development_Fundamentals/` | **PASS** | Valid local Git repository at inner directory |
| Git Config | `.gitattributes` & `.gitignore` | **PASS** | Strict LF normalization enforced; caches/envs ignored |
| Source Code | `Source Code/api_extract.py` | **PASS** | Live public REST API extraction; exports clean deduplicated JSON & CSV |
| Requirements | `Source Code/requirements.txt` | **PASS** | `requests`, `pandas`, `matplotlib`, `python-docx`, `python-pptx` |
| Unit Tests | `Source Code/test_api_extract.py` | **PASS** | **9/9 unit tests passing** (including HTTP 4xx, 5xx, & deduplication) |
| FX CSV | `Datasets/fx_rates_api.csv` | **PASS** | Live 4-row rate extract from Frankfurter (LF endings) |
| FX JSON | `Datasets/fx_rates_api.json` | **PASS** | Live formatted JSON (pure LF line endings) |
| FX JSON (alias) | `Datasets/fx_rates_api_response.json` | **PASS** | Synchronized JSON alias (pure LF line endings) |
| Stock Primer | `Documentation/stock_market_summary_one_page.docx` / `.md` | **PASS** | Verified **strictly 1 page** via Microsoft Word COM |
| Statement Analysis | `Documentation/infosys_financial_statement_analysis.docx` / `.md` | **PASS** | Audited Ind AS FY25 vs FY26 numbers |
| API Assignment | `Documentation/api_data_extraction_assignment.docx` / `.md` | **PASS** | Reconciled rates (USD/INR 94.51) and live HTTP 200 data |
| Git Guide | `Documentation/github_version_control_guide.docx` / `.md` | **PASS** | Branching, committing, and GitHub guide |
| Zerodha Report | `Documentation/fintech_research_report_zerodha.docx` / `.md` | **PASS** | Market plumbing, depositories, analytics cases |
| Architecture Diagram | `Documentation/software_architecture_data_flow.png` | **PASS** | 2532x1393 high-resolution data flow |
| Slide Deck | `PPT/Slides/Week_2_FinTech_Domain_Software_Development_Fundamentals.pptx` | **PASS** | 9 widescreen slides; boundary checks pass |
| Slide Montage | `PPT/Slides/slide_montage.png` | **PASS** | Re-rendered directly from PowerPoint COM |
| Distributable ZIP | `Week_2_FinTech_Domain_Software_Development_Fundamentals.zip` | **PASS** | Zero `__pycache__` / `.pyc` files; 100% LF normalized |

---

## 2. File Inventory and Deliverables Status

All required deliverables are present in the repository with zero missing files:

```text
Week_2_FinTech_Domain_Software_Development_Fundamentals/
├── .gitattributes
├── .gitignore
├── README.md
├── Datasets/
│   ├── api_extraction_metadata.json
│   ├── api_response_sample.json
│   ├── api_sample_data_note.txt
│   ├── fx_rates_api.csv
│   ├── fx_rates_api.json
│   ├── fx_rates_api_response.json
│   ├── fx_rates_sample.csv
│   └── infosys_financials_fy25_fy26.csv
├── Documentation/
│   ├── PRE_PUSH_VERIFICATION_REPORT.md
│   ├── api_data_extraction_assignment.docx
│   ├── api_data_extraction_assignment.md
│   ├── file_manifest.txt
│   ├── fintech_research_report_zerodha.docx
│   ├── fintech_research_report_zerodha.md
│   ├── github_version_control_guide.docx
│   ├── github_version_control_guide.md
│   ├── infosys_financial_statement_analysis.docx
│   ├── infosys_financial_statement_analysis.md
│   ├── infosys_financial_trend.png
│   ├── repository_status.md
│   ├── software_architecture_data_flow.png
│   ├── software_architecture_diagram_notes.md
│   ├── software_development_fundamentals.docx
│   ├── software_development_fundamentals.md
│   ├── sources_and_references.md
│   ├── stock_market_summary_one_page.docx
│   └── stock_market_summary_one_page.md
├── PPT/Slides/
│   ├── Week_2_FinTech_Domain_Software_Development_Fundamentals.pptx
│   └── slide_montage.png
└── Source Code/
    ├── api_extract.py
    ├── requirements.txt
    └── test_api_extract.py
```

---

## 3. Financial Source & Calculation Verification

### Source Authority
- **Company:** Infosys Limited (NSE/BSE: INFY)
- **Reporting Framework:** Consolidated Ind AS Audited Statements
- **Periods:** Year ended March 31, 2025 (FY2024-25) vs Year ended March 31, 2026 (FY2025-26)
- **Units:** ₹ crore (except Basic EPS in ₹/share)

### Recalculation Results

$$\text{Revenue Growth} = \frac{178,650 - 162,990}{162,990} \times 100 = 9.61\% \quad (\text{Reported: } +9.6\%)$$

$$\text{Profit for the Year Growth} = \frac{29,474 - 26,750}{26,750} \times 100 = 10.18\% \quad (\text{Reported: } +10.2\%)$$

$$\text{Basic EPS Growth} = \frac{71.58 - 64.50}{64.50} \times 100 = 10.98\% \quad (\text{Reported: } +11.0\%)$$

$$\text{Current Ratio (FY25)} = \frac{97,099}{42,850} = 2.266\text{x} \approx 2.27\text{x} \quad (\text{Reported: } 2.27\text{x})$$

$$\text{Current Ratio (FY26)} = \frac{103,489}{52,322} = 1.978\text{x} \approx 1.98\text{x} \quad (\text{Reported: } 1.98\text{x})$$

$$\text{Net Profit Margin (FY25)} = \frac{26,750}{162,990} \times 100 = 16.41\% \quad (\text{Reported: } 16.41\%)$$

$$\text{Net Profit Margin (FY26)} = \frac{29,474}{178,650} \times 100 = 16.50\% \quad (\text{Reported: } 16.50\%)$$

$$\text{Simple Free Cash Flow (FY25)} = 35,694 - 2,237 = ₹33,457\text{ cr}$$

$$\text{Simple Free Cash Flow (FY26)} = 33,986 - 2,727 = ₹31,259\text{ cr} \quad (-6.57\%, \text{Reported: } -6.6\%)$$

**Audit Result:** All financial calculations match official source figures with 100% precision. Narrative conclusions accurately reflect the verified data.

---

## 4. API Extraction Pipeline & Dataset Parity

### Captured Reference Data & Parity Evidence
- **Endpoint:** `https://api.frankfurter.dev/v2/rates?base=USD&quotes=INR,EUR,GBP,JPY`
- **Captured Reference Date:** 22 October 2026
- **HTTP Payload:** Status `200 OK`, `Content-Type: application/json`
- **Total Records:** 4 currency pairs (USD base against EUR, GBP, INR, JPY)
- **Offline Test Coverage:** 9/9 unit tests validating network mocking, deduplication, and HTTP 4xx/5xx handling

### Reconciled Currency Reference Rates

| Date | Base | Quote | Rate |
|---|---|---|---:|
| 2026-10-22 | USD | EUR | 0.88966 |
| 2026-10-22 | USD | GBP | 0.74667 |
| 2026-10-22 | USD | INR | 94.51000 |
| 2026-10-22 | USD | JPY | 157.94000 |

### Parity, Line Endings, and Execution Note
1. **JSON & CSV Parity:** Both `fx_rates_api.json` and `fx_rates_api.csv` are exported from the exact same deduplicated DataFrame records (`clean_records = df.to_dict(orient="records")`). Zero discrepancies exist.
2. **Line Ending Normalization:** Both `fx_rates_api.json` and `fx_rates_api_response.json` are written using strict binary LF bytes (`formatted_json.encode('utf-8')`). Python byte checks confirm `CRLF: 0`, eliminating cross-platform Git line-ending churn.
3. **Document Reconcilement:** The rate examples across `api_data_extraction_assignment.docx`, `api_data_extraction_assignment.md`, and `README.md` match the dataset rate of `94.51` for USD/INR.
4. **Environment Execution Note:** The included dataset represents the validated reference response captured on 22 October 2026. In environments where outbound network or DNS requests are restricted, the 9 offline unit tests verify the script's normalization, error handling, and deduplication logic without network dependency. Executing `python "Source Code/api_extract.py"` on an internet-connected machine pulls live updates.

---

## 5. Comprehensive Unit Test Suite (9 Tests Passing)

The test suite in [`Source Code/test_api_extract.py`](Source%20Code/test_api_extract.py) was expanded to 9 tests covering normal responses, error codes, and deduplication logic:

```bash
python -m unittest discover -s "Source Code" -p "test_*.py" -v
```

### Execution Log

```text
test_api_error_message_payload (test_api_extract.FetchRatesTests.test_api_error_message_payload) ... ok
test_deduplication_parity_records (test_api_extract.FetchRatesTests.test_deduplication_parity_records) ... ok
test_empty_payload_raises_clear_error (test_api_extract.FetchRatesTests.test_empty_payload_raises_clear_error) ... ok
test_fetch_rates_normalizes_rows (test_api_extract.FetchRatesTests.test_fetch_rates_normalizes_rows) ... ok
test_http_4xx_client_error_handled (test_api_extract.FetchRatesTests.test_http_4xx_client_error_handled) ... ok
test_http_5xx_server_error_handled (test_api_extract.FetchRatesTests.test_http_5xx_server_error_handled) ... ok
test_http_request_exception_handled (test_api_extract.FetchRatesTests.test_http_request_exception_handled) ... ok
test_invalid_json_raises_runtime_error (test_api_extract.FetchRatesTests.test_invalid_json_raises_runtime_error) ... ok
test_skips_malformed_records (test_api_extract.FetchRatesTests.test_skips_malformed_records) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.077s

OK
```

---

## 6. Distributable ZIP Verification

The project archive `Week_2_FinTech_Domain_Software_Development_Fundamentals.zip` was completely cleaned and repackaged:
- **Pycache Excluded:** 0 `.pyc` files, 0 `__pycache__` directories in the archive.
- **Line Endings:** All code, JSON, and CSV files normalized to LF line endings (`CRLF: 0`).
- **Archive File Count:** Exactly 34 clean project deliverable files.

---

## 7. Documentation and PowerPoint Inspection Results

1. **Stock Market Primer (`stock_market_summary_one_page.docx`):**
   - Populated valuation terms (Market Cap, EPS, P/E, P/B, Dividends, Bonus shares, Stock splits, Trading volume).
   - Fixed encoding (`India's`).
   - Verified **strictly 1 page** via Microsoft Word COM (`doc.ComputeStatistics(2) = 1`).
2. **Software Architecture Diagram (`software_architecture_data_flow.png`):**
   - High-resolution (2532x1393) diagram detailing end-to-end user-to-dashboard financial data flow.
3. **FinTech Case Study (`fintech_research_report_zerodha.docx`):**
   - Correctly analyzes market plumbing, depositories (NSDL/CDSL), SEBI, and realistic brokerage analytics use cases.
4. **PowerPoint Presentation (`PPT/Slides/Week_2_FinTech_Domain_Software_Development_Fundamentals.pptx`):**
   - 9 widescreen slides; zero bounding box clipping; montage refreshed via PowerPoint COM.
5. **README Badges:**
   - Replaced all local `file:///` URLs with repository-relative paths for clean GitHub rendering.

---

## 8. Summary of All Repaired Issues

| Issue ID | Severity | Category | Description & Fix Applied |
|---|---|---|---|
| **ISS-01** | `HIGH` | Documentation | Empty paragraph 6 in `stock_market_summary_one_page.docx` populated; verified 1-page fit via Word COM. |
| **ISS-02** | `HIGH` | Documentation | Character encoding artifact (`Indias`) corrected to `India's`. |
| **ISS-03** | `HIGH` | Datasets | Target structure required `Datasets/fx_rates_api.json`. Updated `api_extract.py` to write both JSON variants with LF endings. |
| **ISS-04** | `HIGH` | Datasets | Reconciled INR rate (`94.51`) across datasets, Word document, markdown, and README. |
| **ISS-05** | `HIGH` | Code Quality | Deduplicated records before JSON export, guaranteeing CSV/JSON parity on duplicate inputs. |
| **ISS-06** | `HIGH` | Testing | Expanded unit tests from 6 to 9 tests covering HTTP 4xx, HTTP 5xx, and deduplication parity. |
| **ISS-07** | `MEDIUM` | Distribution | Cleaned `Source Code/__pycache__/` and rebuilt distributable ZIP with zero pycache files and pure LF endings. |
| **ISS-08** | `MEDIUM` | Documentation | Replaced broken `file:///` badge links in `README.md` with repository-relative paths. |
| **ISS-09** | `LOW` | Git Config | Added `.gitattributes` to enforce LF line endings across repository; `git diff --check` passes cleanly. |

---

## 9. Final Checklist Summary

- [x] All 6 module assignments present and complete
- [x] One-page stock market primer verified in Microsoft Word
- [x] Infosys financial calculations cross-verified against official reports
- [x] REST API reference dataset extraction verified with 100% CSV/JSON parity
- [x] 9 offline unit tests passing
- [x] System architecture diagram and notes verified
- [x] Zerodha FinTech business analytics case study complete
- [x] PowerPoint presentation verified without visual clipping
- [x] Zero sensitive data, API keys, or personal credentials
- [x] Clean Git working tree and remote synchronization with GitHub
