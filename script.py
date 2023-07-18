import requests
import base64
from decouple import config

CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')

encoded = base64.b64encode(
    (CLIENT_ID + ":" + CLIENT_SECRET).encode("ascii")).decode("ascii")

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic " + encoded
}

payload = {
    "grant_type": "client_credentials"
}

auth_res = requests.post(
    "https://accounts.spotify.com/api/token", data=payload, headers=headers)

token = auth_res.json()['access_token']

authed_headers = {
    "Authorization": "Bearer " + token
}

tracks_to_add = {
    "uris": [
        "spotify:track:0dK4cAHHNAlFf7FIel2njT"
    ]
}

playlist_res = requests.post(
    "https://api.spotify.com/v1/playlists/23tDXTZVZo0Mz936JKSM7j/tracks", data=tracks_to_add, headers=authed_headers)

print(auth_res)
print(auth_res.text)
print(playlist_res.text)
