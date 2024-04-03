
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
import requests
from PIL import Image
from io import BytesIO

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

y = sp.playlist_items('https://open.spotify.com/playlist/5zTUX59PIGj24TuLWBxnQC?si=4b8d0255c22c4fa4', offset=99)

x = 100

for item in y['items']:
    url = item['track']['album']['images'][0]['url']
    response = requests.get(url)
    if response.status_code == 200:
      # Use PIL to open the image from the bytes content
      image = Image.open(BytesIO(response.content))
      path = str(x) + ".jpg"
      # Save the image to the specified path
      image.save(path)
      x+=1
    

#playlist_songs = []

#for x in y['items']:
#    #print(x['track']['uri'])
#    playlist_songs.append(x['track']['uri'])

#print(playlist_songs)
#print(len(playlist_songs))
