import unittest

from requests_file.requests_file import get_artist, get_top_tracks


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
