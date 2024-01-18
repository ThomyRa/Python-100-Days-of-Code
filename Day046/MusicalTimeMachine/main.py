import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from prettyprinter import pprint

# date = input("Insert a date you want to search Billboard songs (YYYY-MM-DD): ")
#
# URL = f"https://www.billboard.com/charts/hot-100/{date}"
#
# response = requests.get(url=URL)
# soup = BeautifulSoup(response.text, "html.parser")
#
# song_info = soup.select("div .o-chart-results-list-row-container li .o-chart-results-list__item .a-no-trucate")
# artists_list = [artist.getText().strip() for artist in song_info if song_info.index(artist) % 2 != 0]
# print(artists_list)
#
# songs_list = [artist.getText().strip() for artist in song_info if song_info.index(artist) % 2 == 0]
# print(songs_list)

load_dotenv()

spotify = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
                client_id=os.getenv("CLIENT_ID"),
                client_secret=os.getenv("CLIENT_SECRET"),
                scope="playlist-modify-private",
                redirect_uri="https://example.org/callback",
                show_dialog=True,
                cache_path="token.txt",
                username="Thomy"
        )
)

user_id = spotify.current_user()["id"]
print(user_id)
