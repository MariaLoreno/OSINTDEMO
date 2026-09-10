# report-scripts

> ⚠️ **DEMO / TEACHING REPOSITORY — NOT A REAL LEAK** ⚠️
>
> This repository is a **deliberately insecure example** built for an academic
> OSINT / cybersecurity awareness demonstration. Every name, account, password,
> and API key in this repo is **fake and invented**. None of them work, and none
> of them belong to any real person or system. Do not treat anything here as a
> real credential.

Small helper scripts for generating weekly enrollment reports.

Written by **Alex Dela Cruz** (fictional persona) — social media / reports.

## What this repo demonstrates

This repo is used in a classroom demo to show *why committing secrets to a
public repository is dangerous*. During the demo, the audience uses simple,
legal OSINT techniques to discover that a password was accidentally committed:

```bash
# Clone the repo
git clone <repo-url>
cd report-scripts

# Search the current files for secrets
grep -rniE "password|api_key|token|secret" .

# Search the git HISTORY — secrets stay in old commits even after "deleting" them
git log -p | grep -niE "password|api_key|token|secret"
```

## The lesson

Even though the developer wrote `# TODO remove before pushing`, the secret was
committed anyway — and once it is in git history, deleting the line in a later
commit does **not** remove it. A real attacker scanning public repos would find
it instantly.

## How to protect against this

- Never hardcode credentials. Use environment variables or a secrets manager.
- Add sensitive files to `.gitignore` **before** the first commit.
- Scan repos with tools like `gitleaks` or `trufflehog` before pushing.
- If a secret is ever committed, **rotate it immediately** — don't just delete the line.
- Enable secret-scanning alerts in your GitHub repository settings.
