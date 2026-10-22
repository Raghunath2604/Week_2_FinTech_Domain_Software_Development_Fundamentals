# Git and GitHub: Assignment Submission Guide

This deliverable prepares the project for version control. A local project folder is not the same as a hosted GitHub repository; the commands below create commits locally and publish the files only after you sign into your own GitHub account.

## Core concepts

- **Repository:** project files plus version history.
- **Clone:** copy an existing remote repository locally.
- **Commit:** save a named snapshot to local history.
- **Push:** send local commits to the remote repository.
- **Pull:** fetch and integrate remote changes.
- **Branch:** independent line of work.
- **Pull request:** ask to review/merge changes from one branch into another.

## Option A: Publish this folder with GitHub CLI (recommended)

1. Install Git and GitHub CLI (`gh`) if not already installed.
2. Open a terminal in the extracted project root.
3. Sign in: `gh auth login`.
4. Initialize and commit:

```bash
git init
git branch -M main
git add .
git commit -m "Add Week 2 FinTech fundamentals assignments"
```

5. Create the remote repo and push:

```bash
gh repo create week-2-fintech-fundamentals --public --source=. --remote=origin --push
```

Choose `--private` instead of `--public` if your mentor allows a private repo and you do not want the project public. Check company/internship policy before publishing. Never commit API tokens, passwords, personal data or confidential documents.

## Standard update workflow

```bash
git status
git checkout -b docs/fintech-research
# edit files
git add Documentation/fintech_research_report_zerodha.md
git commit -m "Add Zerodha analytics research report"
git push -u origin docs/fintech-research
```

Then create a pull request on GitHub, review the diff, and merge when ready. To update the main branch locally, use `git checkout main` and `git pull`.

## Suggested repository hygiene

- Keep `README.md`, `requirements.txt`, folder names and source links current.
- Use descriptive commit messages and small logical commits.
- Do not include environment secrets. Review `.gitignore` before every push.
- Include sources and as-of dates for financial facts.
- If sharing the project, state that the mock API CSV is an example row and the API script should be run online for current values.

## Submission verification

After pushing, open the repository in a browser and confirm the expected folders and files appear. Include the remote URL in your internship submission note. This package does not create or publish a GitHub repository automatically; these steps intentionally keep control of public posting with you.
