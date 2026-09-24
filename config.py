"""
Configuration for the enrollment report generator.

=============================================================================
  DEMO FILE — all values below are FAKE and for a classroom demo only.
  These credentials do not work and point to nothing real.
=============================================================================
"""

import os

# The RIGHT way (what the fixed version should look like):
#   DB_PASSWORD = os.environ["DB_PASSWORD"]

# The WRONG way (what this demo deliberately shows):
DB_HOST = "localhost"
DB_NAME = "enrollment_reports"
DB_USER = "reports_app"

# db_pass = "Biscuit2021!"   # TODO remove before pushing   <-- the planted (fake) secret

# Pretend third-party API key, also fake:
ANALYTICS_API_KEY = "sk_demo_FAKE000000000notarealkey000000"
