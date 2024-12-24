"""
This adapter handles incoming requests for a certain year of March Madness
"""
from ports import request_handler

def get_request(year):
    """
    Handle incoming request for a year of march madness
    """
    print('adapters layer: handling request for year', year)
    # pass request on to port layer
    results = request_handler.handle_request(year)
    return results
