# Week 2 - FinTech Domain & Software Development Fundamentals

Prepared for the Bluestock FinTech prerequisite assignment. This learning package contains a stock market primer, Infosys FY2025-26 financial statement analysis, a public REST API extraction exercise, Git/GitHub instructions, a software data-flow diagram, a Zerodha analytics research report, and a slide deck.

## Required folder structure

```text
Week_2_FinTech_Domain_Software_Development_Fundamentals/
├── Source Code/
│   ├── api_extract.py
│   ├── test_api_extract.py
│   └── requirements.txt
├── Datasets/
│   ├── infosys_financials_fy25_fy26.csv
│   ├── fx_rates_sample.csv
│   ├── api_response_sample.json
│   ├── fx_rates_api.csv
│   ├── fx_rates_api.json
│   ├── fx_rates_api_response.json
│   ├── api_extraction_metadata.json
│   └── api_sample_data_note.txt
├── Documentation/
│   ├── PRE_PUSH_VERIFICATION_REPORT.md
│   ├── stock_market_summary_one_page.docx / .md
│   ├── infosys_financial_statement_analysis.docx / .md
│   ├── api_data_extraction_assignment.docx / .md
│   ├── github_version_control_guide.docx / .md
│   ├── software_development_fundamentals.docx / .md
│   ├── fintech_research_report_zerodha.docx / .md
│   ├── sources_and_references.md
│   ├── repository_status.md
│   ├── file_manifest.txt
│   ├── infosys_financial_trend.png
│   └── software_architecture_data_flow.png
└── PPT/Slides/
    ├── Week_2_FinTech_Domain_Software_Development_Fundamentals.pptx
    └── slide_montage.png
```

## Run the API exercise

```bash
pip install -r "Source Code/requirements.txt"
python "Source Code/api_extract.py"
```

The script fetches public currency reference rates from Frankfurter and exports JSON and CSV outputs to `Datasets/` (`fx_rates_api.json`, `fx_rates_api_response.json`, and `fx_rates_api.csv`). Live execution has been verified via Python on 22 October 2026 (base USD quotes EUR, GBP, INR, and JPY) with HTTP 200 OK. Unit tests can be run with:

```bash
python -m unittest discover -s "Source Code" -p "test_*.py" -v
```

API documentation: https://frankfurter.dev/.

## Key assumptions and caveats

- The stock-market primer is educational, not investment advice.
- Financial statement figures are from published Infosys consolidated FY2025-26 statements; units are INR crore except EPS. The report identifies statement basis explicitly.
- Financial analysis is historical, not a stock recommendation.
- Zerodha case-study metrics are analyst suggestions inferred from public engineering posts, not claims about private/internal KPIs.
- The Git/GitHub guide shows how to publish to your account.

See `Documentation/sources_and_references.md` for primary references and as-of date.

## GitHub publication

The configured remote for this repository is:

```bash
https://github.com/Raghunath2604/Week_2_FinTech_Domain_Software_Development_Fundamentals.git
```

To configure and publish to GitHub:

```bash
git remote add origin https://github.com/Raghunath2604/Week_2_FinTech_Domain_Software_Development_Fundamentals.git
git push -u origin main
```

Before pushing:
1. Review `git status` and `git log --oneline`.
2. Ensure your author identity is set: `git config user.name "Raghunath2604"` and `git config user.email "your_email@example.com"`.
3. Never add access tokens or passwords to the repository.

See `Documentation/PRE_PUSH_VERIFICATION_REPORT.md` for the complete pre-push audit report.
