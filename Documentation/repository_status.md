# Repository status and final publishing step

The assignment folder is a local Git repository with commit history included in this project archive. A remote GitHub repository has **not** been created by this environment: the connected GitHub integration refused repository creation due to its current permission scope. This means the GitHub-hosted deliverable is not yet complete.

## Publish to your own GitHub account

1. Sign in to GitHub and create a **blank** repository named `Week_2_FinTech_Domain_Software_Development_Fundamentals`. Do not initialize it with a README, license or `.gitignore`, because this folder already has commits.
2. Open a terminal at the extracted project root.
3. Configure your own commit identity if needed: `git config user.name "Your Name"` and `git config user.email "your-github-email@example.com"`.
4. Add the URL GitHub shows you and push: 

```bash
git remote add origin https://github.com/YOUR_USERNAME/Week_2_FinTech_Domain_Software_Development_Fundamentals.git
git push -u origin main
```

If `origin` already exists, inspect it with `git remote -v` before changing it. Check `git status` and `git log --oneline` before the first push. Never commit access tokens, passwords or confidential customer/internship data.
