"""
Port layer for incoming underdog request
"""

def handle_request(year):
    """
    Passes on the year from this request to the business logic and returns the response
    """
    print("port layer: asking business logic...")
    return year
