"""
This adapter handles incoming requests for a certain year of March Madness
"""
from ports.request_handler import handle_request

def get_underdog_request(year, bet):
    """
    Handle incoming request for a year of march madness
    """
    # pass request on to port layer
    return handle_request(year, bet)
