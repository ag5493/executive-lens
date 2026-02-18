"""Executive Lens — Scenario 1: The AI Tool Nobody Approved"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app_engine import run_app

SCENARIO = {
    "title": "The AI Tool Nobody Approved",
    "situation": (
        "You're a senior analyst at a 2,000-person financial services company. "
        "Your team of 3 analysts spends every Monday producing a weekly performance report — "
        "pulling data from five systems, formatting it, and distributing it to 12 senior leaders. "
        "Each person spends roughly 4 hours on this task every week. "
        "You've piloted an AI reporting tool for 30 days that automates 80% of the work. "
        "It costs $15,000 annually. Your CFO has already pushed back once, saying "
        "'we don't have budget for new tools right now.'"
    ),
    "ask": (
        "Build a business case to get your CFO to approve the $15,000 annual spend."
    ),
}

if __name__ == "__main__":
    run_app(SCENARIO, scenario_number=1)
