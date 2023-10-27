
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

# x = sp.artist('https://open.spotify.com/artist/3pTE9iaJTkWns3mxpNQlJV?si=ffWB8L8uTGaQxTLl5VfNGA')
# print(x)
# print(x['genres'])

#y = sp.playlist_items('https://open.spotify.com/playlist/5zTUX59PIGj24TuLWBxnQC?si=434565dc34e94139', offset=99)
#print(y)

#playlist_songs = []

#for x in y['items']:
#    #print(x['track']['uri'])
#    playlist_songs.append(x['track']['uri'])

#print(playlist_songs)
#print(len(playlist_songs))

x = 100
track_index = []
while x <= 271:
    track_index.append(x)
    x += 1


print(len(track_index))
print(track_index)