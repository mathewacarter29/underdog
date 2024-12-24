"""
Underdog - calculates the odds of whether it was beneficial to bet on the underdog
during March Madness in a given year

This project uses hexagonal architecture
"""
from adapters.get_request import get_request

YEAR = 2023

def main():
    """
    main method
    """
    print('starting Underdog...')
    result = get_request(YEAR)
    print(result)

if __name__ == '__main__':
    main()
