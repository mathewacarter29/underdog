"""
Business logic for Underdog

Calculates profit given a default bet size on every underdog during a certain year
"""

import json
import decimal
from ports.api_service import get_games


def get_winnings(year, bet):
    """
    Get the winnings from betting on an underdog every game of march madness
    """
    # 1. get odds for every game during march madness
    api_response = get_games()
    if api_response is None:
        return None
    winnings = 0
    tournament_round = 0
    for game in api_response["games"]:
        if game["year"] == year:
            continue
        if game["round"] != tournament_round:
            tournament_round = game["round"]
            print(f"Winnings at beginning of round ${tournament_round}: ${winnings}")

        winner_name = (
            game["awayTeamName"]
            if game["awayTeamScore"] > game["homeTeamScore"]
            else game["homeTeamName"]
        )
        # if underdog wins, then add to winnings
        # check if home team is underdog and if they win OR
        # check if away team is underdog and if they win
        if (
            game["homeTeamMoneyline"] > game["awayTeamMoneyline"]
            and game["homeTeamScore"] > game["awayTeamScore"]
        ) or (
            game["awayTeamMoneyline"] > game["homeTeamMoneyline"]
            and game["awayTeamScore"] > game["homeTeamScore"]
        ):
            moneyline = (
                game["homeTeamMoneyline"]
                if winner_name == game["homeTeamName"]
                else game["awayTeamMoneyline"]
            )
            print("+ Underdog home team won the game -", winner_name, "wins")
            winnings += calculate_winnings(bet, moneyline)
        # there is not an underdog? would be weird
        elif game["awayTeamMoneyline"] == game["homeTeamMoneyline"]:
            print(f'{game["homeTeamName"]} vs. {game["awayTeamName"]} the same moneyline: {game["homeTeamMoneyline"]}') #pylint: disable=line-too-long
            print("this should not happen, investigate further")
            winnings += 0
        # the underdog did not win
        else:
            print("- Favorite won the game -", winner_name, "- lost the bet")
            winnings -= bet
    return winnings


def calculate_winnings(bet: int, odds: float) -> decimal.Decimal:
    """
    Calculate winning total based on the bet and the following formulas

    favorites denoted with minus sign, number shows how much you need to bet to win $100
    ex) -188 = team is a favorite to win, bet $188 to win $100

    underdogs denoted with plus sign, number shows how much you'd win if you bet $100
    ex) +158 = team is an underdog, bet $100 to win $158

    the team with the higher moneyline odds number is the underdog
    ex) -102 vs -118 means -102 is technically the underdog

    Determine the sign before the odd: + or -.
    For an underdog (+):
    Divide the wager by 100.
    Multiply the result by the moneyline odd to calculate the profit.

    For a favorite (-):
    Divide 100 by the odds.
    Multiply the result by the bet — that's the payout.
    """
    result = 0
    if odds >= 0:
        result = decimal.Decimal((bet / 100.0)) * odds
    else:
        result = decimal.Decimal((100 / odds)) * bet * -1
    return round(result, 2)


def indent_dictionary(obj):
    """
    Helper function to print out dictionary in an easier to read format
    """
    return json.dumps(obj, indent=4)
