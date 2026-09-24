# Instructor / Presenter Guide

A 4-minute live segment on "why secrets in git are dangerous." Everything is fake.

## Setup (once)
Push this folder to a GitHub repo on your own account (steps in the message).
Make it **public** so the demo is realistic, but keep the DEMO warnings intact.

## Live script

**1. "Here's an employee's public repo we found via sherlock."**
```bash
git clone https://github.com/<your-username>/report-scripts
cd report-scripts
```

**2. "First, a quick grep of the current files."**
```bash
grep -rniE "password|api_key|token|secret" --include="*.py" .
```
Audience sees the password is only *commented out*. Ask: "Are we safe? The dev removed it."

**3. "Now let's look at the history — this is the real lesson."**
```bash
git log --oneline
git log -p -- config.py | grep -niE 'db_pass'
```
Reveal: the password `Biscuit2021!` was **live** in commit `Add database config`.
Deleting it later did NOT remove it from history.

**4. The correlation payoff (ties to the persona demo).**
Note the password contains "Biscuit" — the pet name from Alex's (fictional) Instagram
bio. Separate public clues combine into a real risk.

**5. Flip to defense.** Walk through the "How to protect against this" list in README.md:
environment variables, .gitignore before first commit, secret scanning, and — most
important — **rotate any secret that was ever committed.**

## Key line to say out loud
> "Git never forgets. Once a secret is committed, treating it as compromised and
> rotating it is the only safe move — deleting the line is not enough."
