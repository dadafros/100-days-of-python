import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import os
from datetime import date

date_to_travel = input("Welcome to Spotify Time Machine. Which date do you want travel to? (YYYY-MM-DD) ")

print("Searching Billboard's hot 100 songs for that date...")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date_to_travel)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
chart = soup.find("div", class_="chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max")
top100 = chart.find_all("h3", id="title-of-a-story")
artists = chart.select(selector="li ul li span")
artists = [artist.getText().strip() for artist in artists]
artists = [artist for artist in artists if not artist.isnumeric() and artist != "-"]
top100 = [music.getText().strip() for music in top100]
top100 = [music for music in top100 if music[-1] != ":"]
try:
    top100.remove("Gains in Weekly Performance")
    top100.remove("Additional Awards")
except ValueError:
    pass
print("Search successful")

print("Spotify authorizing...")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="d283f658debf4cd49702a58898a68fd3",
                                               client_secret=os.environ.get("SPOTIFY_SECRET"),
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))
print("Searching songs on Spotify...")
uris = []
year = date_to_travel.split('-')[0]
if len(top100) != len(artists):
    print("Scraping artists and songs are out of sync. Keeping only song names, results may be poor.")
    artists = [""] * len(top100)

for index, music in enumerate(top100):
    result = sp.search(q=f"track: {music} year: {year} artist: {artists[index]}", type="track")
    try:
        uris.append(result["tracks"]["items"][0]['uri'])
    except IndexError:
        print(f"Not found: {music} {artists[index]}")

print("Creating playlist...")
playlist = sp.user_playlist_create(user=sp.current_user()["id"],
                                   name=f"Spotify Time Machine - {date.fromisoformat(date_to_travel).strftime('%B %Y')}",
                                   description=f"Revive the trending songs from {date_to_travel} according to Billboard Hot 100",
                                   public=False)
sp.playlist_add_items(playlist["id"], uris)
print(f"Here is your playlist {playlist['external_urls']['spotify']}")
