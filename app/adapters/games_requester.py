"""
send API request to get March Madness data
"""
import requests

def send_games_request():
    """
    send API request to local games API
    """
    url = 'http://localhost:8000/games'
    try:
        resp = requests.get(url=url)
        data = resp.json() #this returns a dictionary
        return data
    except requests.exceptions.ConnectionError:
        print('error when sending API request - connection failed')
        return None
    