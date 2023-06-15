import requests
from environment import token
def get_artist(id="",albums=""):
    response = ""
    header = {'Authorization': token}
    if id =="" and albums == "":
        response = requests.get(f'https://api.spotify.com/v1/artists',headers = header)
    elif id != "" and albums == "":
        response = requests.get(f'https://api.spotify.com/v1/artists/{id}',headers = header)
    elif id == "" and albums != "":
        response = requests.get(f'https://api.spotify.com/v1/artists/albums={albums}', headers = header)

    return response
def get_top_tracks(artist_id,country):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={country}', headers = header)
    return response

def get_available_markets(country):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/markets?markets={country}', headers = header)
    return response

def get_play_lists(playlist_id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/playlists?playlist_id={playlist_id}', headers = header)
    return response

def get_play_list(playlist_id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}', headers = header)
    return response

def put_play_list(playlist=""):
    header = {'Authorization': token}
    response = requests.put(f'https://api.spotify.com/v1/playlists/t   racks', headers = header)
    return response
