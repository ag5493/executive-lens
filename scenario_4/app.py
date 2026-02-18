"""Executive Lens — Scenario 4: The Infrastructure Upgrade"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app_engine import run_app

SCENARIO = {
    "title": "The Infrastructure Upgrade",
    "situation": (
        "You're a senior infrastructure engineer at an e-commerce company generating $2M in revenue "
        "on an average day. Your platform experiences an average of 5 hours of unplanned downtime "
        "per month across 2–3 incidents. Each hour of downtime costs approximately $80K in lost "
        "transactions plus customer support overhead. The root cause is aging infrastructure your "
        "team has been patching rather than replacing. A full upgrade would cost $200K upfront, "
        "take 3 months to implement, reduce unplanned downtime by an estimated 90%, "
        "and cut monthly maintenance costs by $15K."
    ),
    "ask": (
        "Build a business case for the $200K infrastructure upgrade. "
        "Your audience is your CTO and CFO."
    ),
}

if __name__ == "__main__":
    run_app(SCENARIO, scenario_number=4)
