"""
generate_report.py — builds a weekly enrollment summary.

DEMO FILE for an OSINT classroom demonstration. Does not connect to anything real.
"""

import csv
import datetime
import config


def load_enrollments(path):
    """Read a CSV of enrollments into a list of dicts."""
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def summarize(rows):
    """Count enrollments per program."""
    totals = {}
    for row in rows:
        program = row.get("program", "unknown")
        totals[program] = totals.get(program, 0) + 1
    return totals


def main():
    print(f"Connecting to {config.DB_USER}@{config.DB_HOST}/{config.DB_NAME} ...")
    print("(demo only — no real connection is made)")

    rows = load_enrollments("sample_enrollments.csv")
    totals = summarize(rows)

    today = datetime.date.today().isoformat()
    print(f"\nEnrollment report — {today}")
    print("-" * 32)
    for program, count in sorted(totals.items()):
        print(f"{program:<20} {count:>3}")


if __name__ == "__main__":
    main()
