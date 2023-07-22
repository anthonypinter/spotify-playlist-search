
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

limit = 10

playlist = sp.search("funeral", limit=limit, offset=0, type='playlist', market=None)
# search(q, limit, offset, type, market)
## q is the search term or terms
## limit is the number of results requested
## offset moves the index of the first result returned
## type is the type of thing being search for
## market is used if you want to constrain to a particular country


limit_count = 0

while limit_count < limit:
  print(playlist['playlists']['items'][limit_count]['name'])
  print(playlist['playlists']['items'][limit_count]['description'])
  print(playlist['playlists']['items'][limit_count]['external_urls']['spotify'])
  limit_count += 1
#out.to_csv('playlist-out1.csv')