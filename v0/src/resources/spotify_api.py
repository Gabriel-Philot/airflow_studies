import os
from dotenv import load_dotenv
import base64
from requests import post, get
import json
import re

load_dotenv()

# app.secret_key = '543de345-512a-4a6b-b9b6-12f50b29d491'


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# BASE URLS
TOKEN_BASE_URL = 'https://accounts.spotify.com/api/token'
ARTIST_BASE_URL = 'https://api.spotify.com/v1/search?'
TOP_SONGS_BASE_URL = 'https://api.spotify.com/v1/artists'


class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None

    def get_token(self):
        auth_string = f"{self.client_id}:{self.client_secret}"
        au_bytes = auth_string.encode('utf-8')
        auth_base64 = str(base64.b64encode(au_bytes), 'utf-8')

        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        result = post(TOKEN_BASE_URL, headers=headers, data=data)
        json_result = json.loads(result.content)
        self.token = json_result["access_token"]
        return self.token

    def get_aut_header(self):
        if not self.token:
            self.get_token()
        return {"Authorization": "Bearer " + self.token}

    def search_for_artist(self, artistname):
        headers = self.get_aut_header()
        query = f"q={artistname}&type=artist&tlimit=1"
        
        query_url = ARTIST_BASE_URL + query
        result = get(query_url, headers=headers)
        json_result = json.loads(result.content)['artists']['items']

        if len(json_result) == 0:
            print("No artist with this name exists...")
            return None
        return json_result[0]

    def get_songs_by_artist(self, artist_id, country):
        url = f"{TOP_SONGS_BASE_URL}/{artist_id}/top-tracks?country={country}"
        headers = self.get_aut_header()
        result = get(url, headers=headers)
        json_result = json.loads(result.content)['tracks']
        return json_result
    


