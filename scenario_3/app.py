"""Executive Lens — Scenario 3: The Headcount Request"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app_engine import run_app

SCENARIO = {
    "title": "The Headcount Request",
    "situation": (
        "You're an engineering manager leading a team of 6 at a mid-size tech company. "
        "For two consecutive quarters your team has missed delivery targets by 15–20%. "
        "Two of your senior engineers have privately told you they're burning out, "
        "and one has already started interviewing elsewhere. "
        "You've calculated your team is running at roughly 130% capacity. "
        "You need one additional senior engineer — budgeted at $160K fully loaded annually. "
        "Your VP and CFO have both signaled that headcount is frozen unless there's a compelling business case."
    ),
    "ask": (
        "Build a business case to get one senior engineering hire approved despite a headcount freeze. "
        "Your audience is your VP and CFO."
    ),
}

if __name__ == "__main__":
    run_app(SCENARIO, scenario_number=3)
