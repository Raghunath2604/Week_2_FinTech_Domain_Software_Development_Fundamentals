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
│   ├── fx_rates_api_response.json
│   ├── api_extraction_metadata.json
│   └── api_sample_data_note.txt
├── Documentation/
│   ├── stock_market_summary_one_page.docx / .md
│   ├── infosys_financial_statement_analysis.docx / .md
│   ├── api_data_extraction_assignment.docx / .md
│   ├── github_version_control_guide.docx / .md
│   ├── software_development_fundamentals.docx / .md
│   ├── fintech_research_report_zerodha.docx / .md
│   ├── sources_and_references.md
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

The code fetches public currency reference rates from Frankfurter and writes JSON and CSV output to `Datasets/`. The package includes a filtered live response capture retrieved on 22 October 2026 (USD quotes EUR, GBP, INR and JPY), plus the raw-format JSON and a metadata note. The current execution shell could not independently call the endpoint through Python because outbound DNS was unavailable; rerun the script on an internet-connected laptop to independently refresh the output. API documentation: https://frankfurter.dev/.

## Key assumptions and caveats

- The stock-market primer is educational, not investment advice.
- Financial statement figures are from published Infosys consolidated FY2025-26 statements; units are INR crore except EPS. The report identifies statement basis explicitly.
- Financial analysis is historical, not a stock recommendation.
- Zerodha case-study metrics are analyst suggestions inferred from public engineering posts, not claims about private/internal KPIs.
- The Git/GitHub guide shows how to publish to your account. A remote GitHub repository has not been created from this environment because the connected GitHub integration denied repository-creation permission; the local history and push instructions are included. Create a blank repository under your own account, then set `origin` and push.

See `Documentation/sources_and_references.md` for primary references and as-of date.


## GitHub publication (final account step)

This folder has local Git history. To publish, create an empty repository in your GitHub account, then run from this folder:

```bash
git remote add origin https://github.com/YOUR_USERNAME/Week_2_FinTech_Domain_Software_Development_Fundamentals.git
git push -u origin main
```

If you use a newly created blank repository, check `git status` and `git log --oneline` before pushing. If Git asks for author identity, set your own name/email with `git config user.name` and `git config user.email`. Never add tokens or passwords to the repository.

See `Documentation/repository_status.md` for the final account step required to publish this local Git repository to GitHub.
