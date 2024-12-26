"""
port layer for sending API request
"""
from adapters.games_request import send_games_request

def get_games() -> dict[str, any]:
    """
    get api response from games API
    """
    response = send_games_request()
    return response
