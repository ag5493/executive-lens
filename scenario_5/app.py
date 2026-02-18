"""Executive Lens — Scenario 5: The New Market Opportunity"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app_engine import run_app

SCENARIO = {
    "title": "The New Market Opportunity",
    "situation": (
        "You're a senior product strategist at a $50M ARR enterprise software company. "
        "Your product currently serves only companies with 1,000+ employees. "
        "Through customer conversations and market research you've identified a mid-market segment — "
        "companies with 100–999 employees — that is underserved by competitors and growing fast. "
        "Entering this segment would require 6 months of product adaptation, "
        "a dedicated sales team of 3 people, and approximately $800K in first-year investment. "
        "Your market analysis suggests the mid-market segment could represent "
        "$15M in additional ARR within 3 years."
    ),
    "ask": (
        "Build a business case for entering the mid-market segment. "
        "Your audience is your CEO and board."
    ),
}

if __name__ == "__main__":
    run_app(SCENARIO, scenario_number=5)
