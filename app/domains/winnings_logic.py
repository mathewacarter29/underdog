"""
Business logic for Underdog

Calculates profit given a default bet size on every underdog during a certain year
"""

import json
import decimal
from ports.api_service import get_games

BEST_WINS = 3


def get_winnings(year, bet):
    """
    Get the winnings from betting on an underdog every game of march madness
    """
    api_response = get_games()
    if api_response is None:
        return None
    winnings = 0
    tournament_round = 0
    top_picks = [(0, "")] * BEST_WINS
    for game in api_response["games"]:
        # only get games for the requested year
        if game["year"] == year:
            continue
        # print a winnings update every round
        if game["round"] != tournament_round:
            tournament_round = game["round"]
            print(
                f"\nWinnings at beginning of round ${tournament_round}: ${winnings}\n"
            )

        winner_name, loser_name = (
            (game["awayTeamName"], game["homeTeamName"])
            if game["awayTeamScore"] > game["homeTeamScore"]
            else (game["homeTeamName"], game["awayTeamName"])
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
            print("+ Underdog won the game -", winner_name, "wins")
            profit = calculate_winnings(bet, moneyline)
            winnings += profit
            top_picks = check_for_best_win_list(
                top_picks,
                profit,
                winner_name,
                loser_name,
                game["round"]
            )
            assert len(top_picks) == BEST_WINS
        # there is not an underdog? would be weird
        elif game["awayTeamMoneyline"] == game["homeTeamMoneyline"]:
            print(
                f'{game["homeTeamName"]} vs. {game["awayTeamName"]} the same moneyline: {game["homeTeamMoneyline"]}' # pylint: disable=line-too-long
            )
            print("this should not happen, investigate further")
            winnings += 0
        # the underdog did not win
        else:
            print("- Favorite won the game -", winner_name, "wins")
            winnings -= bet
    print_top_wins(top_picks)
    return winnings

####################
# HELPER FUNCTIONS #
####################

def print_top_wins(top_picks: list[(int, str)]):
    """
    Print out the top winners of March Madness
    """
    print()
    for pick in top_picks:
        print(pick[1])
    print()

def check_for_best_win_list(top_picks: list[(int, str)], profit, winner, loser, tourn_round):
    """
    Check to see if this game is one of the most profitable games
    """
    # if the profit is greater than the 3rd element in the list, add it
    if profit > top_picks[-1][0]:
        label = f"{winner} beats {loser} to win ${profit} in Round {tourn_round}"
        top_picks.append((profit, label))
        sorted_list = sorted(top_picks, key=lambda tup: tup[0], reverse=True)
        sorted_list = sorted_list[:-1]
        return sorted_list
    return top_picks

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
