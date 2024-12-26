"""
Port layer for incoming underdog request
"""

from domains.winnings_logic import get_winnings

def handle_request(year, bet) -> float:
    """
    Passes on the year from this request to the business logic and returns the response
    """
    print("port layer: asking business logic...")
    return get_winnings(year, bet)
