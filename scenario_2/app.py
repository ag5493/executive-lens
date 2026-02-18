"""Executive Lens — Scenario 2: The Product Feature That Keeps Getting Deprioritized"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app_engine import run_app

SCENARIO = {
    "title": "The Feature That Keeps Getting Bumped",
    "situation": (
        "You're a product manager at a B2B SaaS company with 800 enterprise customers "
        "and $40M in annual recurring revenue. Over the past three quarters, your support team "
        "has logged 340 tickets requesting the same feature — a bulk data export function. "
        "Your NPS surveys show it's the number one requested improvement. "
        "The engineering team says it's a 6-week build. "
        "It keeps getting bumped from the roadmap in favor of new customer acquisition features. "
        "You're heading into quarterly planning."
    ),
    "ask": (
        "Build a business case to get the bulk export feature prioritized in next quarter's roadmap. "
        "Your audience is the CPO and CFO."
    ),
}

if __name__ == "__main__":
    run_app(SCENARIO, scenario_number=2)
