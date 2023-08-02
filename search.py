
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

limit_count = 0


###################
# IMPORTANT VARIABLES 
limit = 2 # this controls how many results you get; min is 1, max is 50, default is 10
search_term = 'funeral'
###################

playlist = sp.search(search_term, limit=limit, offset=0, type='playlist', market=None)
# search(q, limit, offset, type, market)
## q is the search term or terms
## limit is the number of results requested
## offset moves the index of the first result returned
## type is the type of thing being search for
## market is used if you want to constrain to a particular countryt

out_columns = ['PlaylistName', 'PlaylistURL', 'PlaylistID', 'Number','Owner', 'OwnerURL', 'Number of Tracks', 'Description', 'Collaborative', 'ImageURL']
out = pd.DataFrame(columns=out_columns)

while limit_count < limit:
  #print(playlist['playlists']['items'])

  #[{'collaborative': False, 'description': 'Ryuichi’s Last Playlist. We would like to share the playlist that Ryuichi had been privately compiling to be played at his own funeral to accompany his own passing. He truly was with music until the very end.', 'external_urls': {'spotify': 'https://open.spotify.com/playlist/31OIme0YdF4ORWvEdTyE6V'}, 'href': 'https://api.spotify.com/v1/playlists/31OIme0YdF4ORWvEdTyE6V', 'id': '31OIme0YdF4ORWvEdTyE6V', 'images': [{'height': None, 'url': 'https://images-ak.spotifycdn.com/image/ab67706c0000bebbe0a0dbec04a4ccd67b95e647', 'width': None}], 'name': 'funeral', 'owner': {'display_name': 'Ryuichi Sakamoto', 'external_urls': {'spotify': 'https://open.spotify.com/user/ryuichisakamoto'}, 'href': 'https://api.spotify.com/v1/users/ryuichisakamoto', 'id': 'ryuichisakamoto', 'type': 'user', 'uri': 'spotify:user:ryuichisakamoto'}, 'primary_color': None, 'public': None, 'snapshot_id': 'OTcsNTY3YWY4NDgzODdkYTJiOTAzYzJjMjQ2NTY3ZGQyN2FkOWM3MGE0OA==', 'tracks': {'href': 'https://api.spotify.com/v1/playlists/31OIme0YdF4ORWvEdTyE6V/tracks', 'total': 33}, 'type': 'playlist', 'uri': 'spotify:playlist:31OIme0YdF4ORWvEdTyE6V'}]

  playlist_name = playlist['playlists']['items'][limit_count]['name']
  owner = playlist['playlists']['items'][limit_count]['owner']['display_name']
  owner_url = playlist['playlists']['items'][limit_count]['owner']['external_urls']['spotify']
  num_tracks = playlist['playlists']['items'][limit_count]['tracks']['total']
  description = playlist['playlists']['items'][limit_count]['description']
  collaborative = playlist['playlists']['items'][limit_count]['collaborative']
  playlist_url = playlist['playlists']['items'][limit_count]['external_urls']['spotify']
  image_url = playlist['playlists']['items'][limit_count]['images'][0]['url']
  track_url = playlist['playlists']['items'][limit_count]['tracks']['href']
  #print('*****************')

  playlist_id = playlist['playlists']['items'][limit_count]['id']

  number = playlist['playlists']['items'][limit_count]['tracks']['total']

  playlist_info = [playlist_name, playlist_url, playlist_id, number, owner, owner_url, num_tracks, description, collaborative, image_url]

  out.loc[len(out.index)] = playlist_info
  #print(out)
  out.to_csv('out.csv')
  out.to_json('out.json')
  #print(sp.playlist_items(playlist_id, limit=1))

  
  #print(playlist['playlists']['items'][limit_count]['name'])
  #print(playlist['playlists']['items'][limit_count]['description'])
  #print(playlist['playlists']['items'][limit_count]['external_urls']['spotify'])
  limit_count += 1


#then, we'll cycle through the out and use the playlist ID value to get the tracks from each playlist.

song_columns = ['PlaylistID', 'Song', 'SongURI', 'PreviewLink', 'Album', 'Artist', 'BigAlbumArt', 'SmallAlbumArt', 'Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo', 'Duration', 'TimeSignature']
song_df = pd.DataFrame(columns=song_columns)

for index, row in out.iterrows():
  pid = out['PlaylistID'].loc[out.index[index]]
  size = out['Number'].loc[out.index[index]] ## this will be a problem if the number is greater than 100
  
  y = 0

  while y < size:
    x = (sp.playlist_items(pid, limit=100))
    song_id = x['items'][y]['track']['id']

    y +=1

    results = sp.track(song_id)
        
    artist_name = results['album']['artists'][0]['name']
    album_name = results['album']['name']
    big_album_art = results['album']['images'][1]['url']
    small_album_art = results['album']['images'][2]['url']
    song_name = results['name']
    song_uri = results['uri']
    preview_link = results['preview_url']

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


    ## Leaving this here for now... just in case.
    # ------------------------- GENIUS LYRIC PULL

    #artist = genius.search_artist("Say Anything", max_songs=5)
    #song = artist.song("Alive With the Glory of Love")
    #artist = genius.search_artist("Say Anything", max_songs=5)
    #try:
            #song = genius.search_song(song_name, artist_name)
            #lyrics_new_line_breaks = song.lyrics
            #lyrics = lyrics_new_line_breaks.replace("\n", " ")
    #except:
            #lyrics = "NO LYRICS"
    #print(lyrics_new_line_breaks)

    
    #print(lyrics)

    #song.save_lyrics()  

    # ------------------------- OUT DF COMPOSITION

    song_array = [pid, song_name, song_uri, preview_link, album_name, artist_name, big_album_art, small_album_art, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time_signature]

    song_df.loc[len(song_df.index)] = song_array

song_df.to_csv('songdf.csv')
song_df.to_json('songdf.json')
    
