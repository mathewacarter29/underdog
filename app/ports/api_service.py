"""
port layer for sending API request
"""
from adapters.games_requester import send_games_request

def get_games(year: int) -> dict[str, any]:
    """
    get api response from games API
    """
    response = send_games_request(year)
    return response
