import requests


def get_players(url):
    try:
        response = requests.request("GET", url)
        return response.json()
    except Exception as e:
        print(f"Error {e}")