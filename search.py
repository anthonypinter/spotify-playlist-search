
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




###################
# IMPORTANT VARIABLES 
limit = 50 # this controls how many results you get; min is 1, max is 50, default is 10
offsets = [50] # offset is the index of the first item to return (e.g., 0, 50, 100, so on)
#for i in range(0,1000,50):
#  offsets.append(i)
search_term = 'funeral'
###################

'''
Can you give us 1000 playlists that have the term "funeral"? <-- DONE
Can you give us 1000 playlists that have the term "memorial"? <-- DONE
Can you give us 1000 playlists that have the term "grief"? <-- DONE
Can you give us 1000 playlists that have the term "mourning"?
'''

out_columns = ['PlaylistName', 'PlaylistURL', 'PlaylistID', 'Followers', 'NumberTracks', 'Duration', 'Owner', 'OwnerURL', 'Number of Tracks', 'Description', 'Collaborative', 'ImageURL']
out = pd.DataFrame(columns=out_columns)

song_columns = ['PlaylistID', 'Song', 'SongURI', 'PreviewLink', 'Album', 'Artist', 'Genres', 'BigAlbumArt', 'SmallAlbumArt', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo', 'Duration', 'TimeSignature']
song_df = pd.DataFrame(columns=song_columns)

for offset in offsets:

  limit_count = 0

  playlist = sp.search(search_term, limit=limit, offset=offset, type='playlist', market=None)
  print(playlist)
  # search(q, limit, offset, type, market)
  ## q is the search term or terms
  ## limit is the number of results requested
  ## offset moves the index of the first result returned
  ## type is the type of thing being search for
  ## market is used if you want to constrain to a particular countryt

  while limit_count < len(playlist['playlists']['items']):
    #print(playlist['playlists']['items'])

    #[{'collaborative': False, 'description': 'Ryuichi’s Last Playlist. We would like to share the playlist that Ryuichi had been privately compiling to be played at his own funeral to accompany his own passing. He truly was with music until the very end.', 'external_urls': {'spotify': 'https://open.spotify.com/playlist/31OIme0YdF4ORWvEdTyE6V'}, 'href': 'https://api.spotify.com/v1/playlists/31OIme0YdF4ORWvEdTyE6V', 'id': '31OIme0YdF4ORWvEdTyE6V', 'images': [{'height': None, 'url': 'https://images-ak.spotifycdn.com/image/ab67706c0000bebbe0a0dbec04a4ccd67b95e647', 'width': None}], 'name': 'funeral', 'owner': {'display_name': 'Ryuichi Sakamoto', 'external_urls': {'spotify': 'https://open.spotify.com/user/ryuichisakamoto'}, 'href': 'https://api.spotify.com/v1/users/ryuichisakamoto', 'id': 'ryuichisakamoto', 'type': 'user', 'uri': 'spotify:user:ryuichisakamoto'}, 'primary_color': None, 'public': None, 'snapshot_id': 'OTcsNTY3YWY4NDgzODdkYTJiOTAzYzJjMjQ2NTY3ZGQyN2FkOWM3MGE0OA==', 'tracks': {'href': 'https://api.spotify.com/v1/playlists/31OIme0YdF4ORWvEdTyE6V/tracks', 'total': 33}, 'type': 'playlist', 'uri': 'spotify:playlist:31OIme0YdF4ORWvEdTyE6V'}]
    
    try:
      playlist_name = playlist['playlists']['items'][limit_count]['name']
    except:
      playlist_name = ' '

    try:
      owner = playlist['playlists']['items'][limit_count]['owner']['display_name']
    except:
      owner = ' '
    
    try:
      owner_url = playlist['playlists']['items'][limit_count]['owner']['external_urls']['spotify']
    except:
      owner_url = ' '

    try:
      num_tracks = playlist['playlists']['items'][limit_count]['tracks']['total']
    except:
      num_tracks = ' '

    try:  
      description = playlist['playlists']['items'][limit_count]['description']
    except:
      description = ' '

    try:  
      collaborative = playlist['playlists']['items'][limit_count]['collaborative']
    except:
      collaborative = ' '
    
    try:
      playlist_url = playlist['playlists']['items'][limit_count]['external_urls']['spotify']
    except:
      playlist_url = ' '

    try:  
      image_url = playlist['playlists']['items'][limit_count]['images'][0]['url']
    except:
      image_url = ''

    try:   
      track_url = playlist['playlists']['items'][limit_count]['tracks']['href']
    except: 
      track_url = ' '
    
    try:
      playlist_id = playlist['playlists']['items'][limit_count]['id']
    except:
      playlist_id = ' '

    try:
      playlist_data = sp.playlist(playlist_id)
    except:
      playlist_data = ' '

    try:
      followers = playlist_data['followers']['total']
    except:
      followers = ' '

    try:
      number = playlist['playlists']['items'][limit_count]['tracks']['total']
    except:
      number = ' '
    
    #print(playlist['playlists']['items'][limit_count]['name'])
    #print(playlist['playlists']['items'][limit_count]['description'])
    #print(playlist['playlists']['items'][limit_count]['external_urls']['spotify'])

    total_duration = 0

    #size = out['Number'].loc[out.index[index]] ## this will be a problem if the number is greater than 100

    y = 0

    while y < number:
      x = (sp.playlist_items(playlist_id, limit=100))
      try:
        song_id = x['items'][y]['track']['id']
        y += 1
      except:
        y += 1
        continue
      

      results = sp.track(song_id)
      #print(results['duration_ms'])
      total_duration = total_duration + results['duration_ms']
      album = sp.album(results['album']['external_urls']['spotify']) 

      
      #print(album['genres'])
      try:
        artist_name = results['album']['artists'][0]['name']
      except:
        artist_name = ' '


      album_name = results['album']['name']
      big_album_art = results['album']['images'][1]['url']
      small_album_art = results['album']['images'][2]['url']
      song_name = results['name']
      song_uri = results['uri']
      duration = results['duration_ms']
      preview_link = results['preview_url']
      genre = album['genres']

      #audio_analysis = sp.audio_analysis(song_uri)
      # probably don't need this ^

      audio_features = sp.audio_features(song_uri)

      danceability = audio_features[0]['danceability']
      energy = audio_features[0]['energy']
      key = audio_features[0]['key']
      loudness = audio_features[0]['loudness']
      mode = audio_features[0]['mode']
      speechiness = audio_features[0]['speechiness']
      acousticness = audio_features[0]['acousticness']
      instrumentalness = audio_features[0]['instrumentalness']
      liveness = audio_features[0]['liveness']
      valence = audio_features[0]['valence']
      tempo = audio_features[0]['tempo']
      duration = audio_features[0]['duration_ms']
      time_signature = audio_features[0]['time_signature']

      song_array = [playlist_id, song_name, song_uri, preview_link, album_name, artist_name, genre, big_album_art, small_album_art, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature]

      song_df.loc[len(song_df.index)] = song_array

      song_df.to_csv('songdf.csv')
      song_df.to_json('songdf.json')


    playlist_info = [playlist_name, playlist_url, playlist_id, followers, number, total_duration, owner, owner_url, num_tracks, description, collaborative, image_url]

    out.loc[len(out.index)] = playlist_info
    #print(out)
    out.to_csv(search_term + str(offset) + '.csv')
    out.to_json(search_term + str(offset) + '.json')
    #print(sp.playlist_items(playlist_id, limit=1))

    limit_count += 1



#print(sp.playlist('https://open.spotify.com/playlist/37i9dQZF1EJLSui5aWyVII?si=f7531b1d341e46b1'))

'''

Info about playlist creation and creator -- 
We can get (what I think) is a proxy for algorithm or not (is it created by an account or by Spotify)
We can get collaborative or not (and/or proxies for collaborative or not, like who added each song to the playlist)
There are ways to identify if it is a blend or not (but I don't think we'll get any of those in our search -- they have very specific naming conventions)
'''