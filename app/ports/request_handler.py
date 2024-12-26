"""
Port layer for incoming underdog request
"""

import decimal
from domains.winnings_logic import get_winnings

def handle_request(year, bet) -> decimal.Decimal:
    """
    Passes on the year from this request to the business logic and returns the response
    """
    print("port layer: asking business logic...")
    winnings = get_winnings(year, bet)
    return winnings
