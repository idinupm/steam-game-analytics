import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("STEAM_API_KEY")
STEAM_ID = os.getenv("STEAM_ID")

def get_owned_games():
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    params = {
        "key": API_KEY,
        "steamid": STEAM_ID,
        "format": "json",
        "include_appinfo": True,
        "include_played_free_games": True
    }

    r = requests.get(url, params=params)
    data = r.json()
    return data["response"]["games"]
