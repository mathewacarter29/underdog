"""
Business logic for Underdog

Calculates profit given a default bet size on every underdog during a certain year
"""

def get_winnings(year):
    """
    Get the winnings from betting on an underdog every game of march madness
    """
    print('getting winnings for year', year)
    # 1. get odds for every game during march madness

    # 2. get winners of above games

    # 3. Given that you bet a default amount on each game, calculate winnings for each game
    # favorites denoted with minus sign, number shows how much you need to bet to win $100
    # ex) -188 = team is a favorite to win, bet $188 to win $100

    # underdogs denoted with plus sign, number shows how much you'd win if you bet $100
    # ex) +158 = team is an underdog, bet $100 to win $158

    # the team with the higher moneyline odds number is the underdog 
    # ex) -102 vs -118 means -102 is technically the underdog

    # 4. add up all winnings
    return None
