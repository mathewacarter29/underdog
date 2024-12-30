"""
Underdog - calculates the odds of whether it was beneficial to bet on the underdog
during March Madness in a given year

This project uses hexagonal architecture
"""

import decimal
import logging
from adapters.get_request import get_underdog_request

YEAR = 2021
BET = 100
BEST_WINS = 3
VERBOSE = False

logger = logging.getLogger(__name__)

def main():
    """
    main method
    """
    if VERBOSE:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)
    print("starting Underdog...")
    result, top_picks = get_underdog_request(YEAR, BET, BEST_WINS)
    if result is None:
        logger.warning("There was a problem getting data, check logs for further information")
    else:
        print()
        print("Winnings for", YEAR)
        print_winnings(result)
        print()
        print("Best bets for", YEAR)
        print_top_wins(top_picks)

def print_top_wins(top_picks: list[(int, str)]):
    """
    Print out the top winners of March Madness
    """
    for pick in top_picks:
        print(pick[1])

def print_winnings(winnings: list[decimal.Decimal]):
    """
    Helper function to print the winnings from each round of the tournament
    """
    for i, r in enumerate(winnings):
        print(f"Net profit after Round {i + 1}: ${r}")


if __name__ == "__main__":
    main()
