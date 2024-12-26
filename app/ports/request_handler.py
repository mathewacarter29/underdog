"""
Port layer for incoming underdog request
"""

import decimal
from domains.winnings_logic import get_winnings

def handle_request(year: int, bet: float, best_wins: int) -> tuple[list[decimal.Decimal], list[(int, str)]]:
    """
    Passes on the year from this request to the business logic and returns the response

    The ports layer is supposed to basically act an an interface between domains and adapters,
    so that is why these function definitions are typed
    """
    winnings, top_picks = get_winnings(year, bet, best_wins)
    return winnings, top_picks
