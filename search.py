
import sys
from time import time
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import numpy as np
import csv
from sklearn.cluster import KMeans
from scipy.spatial import distance
import lyricsgenius


scope = 'user-library-read'

sp = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
          client_id='8ea9544c774649e49a2c2e41feb74396',
          client_secret='9df779bfb7fb45649869fbd792e9ae47',
          redirect_uri='http://localhost/',    
          scope=scope, open_browser=False))

limit = 1

playlist = sp.search("funeral", limit=limit, offset=0, type='playlist', market=None)
# search(q, limit, offset, type, market)
## q is the search term or terms
## limit is the number of results requested
## offset moves the index of the first result returned
## type is the type of thing being search for
## market is used if you want to constrain to a particular countryt

limit_count = 0

out_columns = ['PlaylistName', 'PlaylistURL', 'PlaylistID', 'Owner', 'OwnerURL', 'Number of Tracks', 'Description', 'Collaborative', 'ImageURL']
out = pd.DataFrame(columns=out_columns)

while limit_count < limit:
  #print(playlist['playlists']['items'])

  #[{'collaborative': False, 'description': 'Ryuichi’s Last Playlist. We would like to share the playlist that Ryuichi had been privately compiling to be played at his own funeral to accompany his own passing. He truly was with music until the very end.', 'external_urls': {'spotify': 'https://open.spotify.com/playlist/31OIme0YdF4ORWvEdTyE6V'}, 'href': 'https://api.spotify.com/v1/playlists/31OIme0YdF4ORWvEdTyE6V', 'id': '31OIme0YdF4ORWvEdTyE6V', 'images': [{'height': None, 'url': 'https://images-ak.spotifycdn.com/image/ab67706c0000bebbe0a0dbec04a4ccd67b95e647', 'width': None}], 'name': 'funeral', 'owner': {'display_name': 'Ryuichi Sakamoto', 'external_urls': {'spotify': 'https://open.spotify.com/user/ryuichisakamoto'}, 'href': 'https://api.spotify.com/v1/users/ryuichisakamoto', 'id': 'ryuichisakamoto', 'type': 'user', 'uri': 'spotify:user:ryuichisakamoto'}, 'primary_color': None, 'public': None, 'snapshot_id': 'OTcsNTY3YWY4NDgzODdkYTJiOTAzYzJjMjQ2NTY3ZGQyN2FkOWM3MGE0OA==', 'tracks': {'href': 'https://api.spotify.com/v1/playlists/31OIme0YdF4ORWvEdTyE6V/tracks', 'total': 33}, 'type': 'playlist', 'uri': 'spotify:playlist:31OIme0YdF4ORWvEdTyE6V'}]

  playlist = playlist['playlists']['items'][limit_count]['name']
  owner = playlist['playlists']['items'][limit_count]['owner']['display_name']
  owner_url = playlist['playlists']['items'][limit_count]['owner']['external_urls']['spotify']
  num_tracks = playlist['playlists']['items'][limit_count]['tracks']['total']
  description = playlist['playlists']['items'][limit_count]['description']
  collaborative = playlist['playlists']['items'][limit_count]['collaborative']
  playlist_url = ['playlists']['items'][limit_count]['external_urls']['spotify']
  image_url = playlist['playlists']['items'][limit_count]['images'][0]['url']
  track_url = playlist['playlists']['items'][limit_count]['tracks']['href']
  print('*****************')

  playlist_id = playlist['playlists']['items'][limit_count]['id']

  playlist_info = [limit_count, playlist, playlist_url, playlist_id, owner, owner_url, num_tracks, description, collaborative, image_url]

  

  print(sp.playlist_items(playlist_id, limit=1))
  
  #print(playlist['playlists']['items'][limit_count]['name'])
  #print(playlist['playlists']['items'][limit_count]['description'])
  #print(playlist['playlists']['items'][limit_count]['external_urls']['spotify'])
  limit_count += 1
#out.to_csv('playlist-out1.csv')