"""
This adapter handles incoming requests for a certain year of March Madness
"""
from ports.request_handler import handle_request #pylint: disable=import-error

def get_request(year):
    """
    Handle incoming request for a year of march madness
    """
    print('adapters layer: handling request for year', year)
    # pass request on to port layer
    return handle_request(year)
