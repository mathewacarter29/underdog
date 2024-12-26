"""
Underdog - calculates the odds of whether it was beneficial to bet on the underdog
during March Madness in a given year

This project uses hexagonal architecture
"""

from adapters.get_request import get_underdog_request

YEAR = 2023
BET = 100


def main():
    """
    main method
    """
    print("starting Underdog...")
    result = get_underdog_request(YEAR, BET)
    if result is None:
        print("there was a problem getting data, check logs for further information")


if __name__ == "__main__":
    main()
