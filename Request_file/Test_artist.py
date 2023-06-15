from requests_file import get_artist, get_play_list, put_play_list, get_top_tracks, get_available_markets, get_play_lists
import unittest

class TestArtist(unittest.TestCase):
    def test_artist_check_status(self):
        response = get_artist("0GoJXmDr5UBG8ValCZe4om")
        assert response.status_code == 200, f'Error status code 200, but got {response.status_code}'

    def test_top_track_artist(self):
        response = get_top_tracks("0GoJXmDr5UBG8ValCZe4om","RO")
        assert response.status_code == 200, f'Error avalaible code 200, but got {response.avalaible_code}'
        assert len(response.json()["tracks"]) >= 10

        track_list = response.json()["tracks"]
        tracks_playable = True
        for i in range(len(track_list)):
            if track_list[i]["album"]["is_playable"] == False:
                tracks_playable = False
        assert tracks_playable == True, "Error, tracks for this artist should be playable"

    def test_avalaible_markets(self):
        response = get_available_markets("IT")
        assert response.status_code == 200, f'Error avalaible markets code 200, but got {response.status_code}'

    def test_get_play_lists(self):
        response = get_play_lists("37i9dQZF1E3585oSSAOUUK")
        assert response.status_code == 200, f'Error avalaible markets code 200, but got {response.status_code}'
        assert len(response.json()["tracks"]) >=3
        playlist = response.json()["tracks"]
        playlist_playable = True
        for i in range(len(playlist)):
            if playlist[i]["traks"] is False:
                playlist_playable = False
        assert playlist_playable == True, "Error, tracks for this artist should be playable"

    def test_play_list(self):
        response = get_play_list("37i9dQZF1E3585oSSAOUUK","RO")
        assert response.status_code == 200, f'Error status code 200, but got {response.status_code}'


    def test_playlists_check_number_of_results(self):
        response = get_play_list("37i9dQZF1E3585oSSAOUUK","RO")
        assert response.status_code == 200, f'Error avalaible code 200, but got {response.status_code}'
        assert len(response.json()["tracks"]) >= 5
        playlist = response.json()["tracks"]
        for i in range (len(playlist)):
            playlist == True
        assert playlist [i]['playlist'] == playlist, f"Error, playlist does not extist"

