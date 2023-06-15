import unittest

from requests_file.requests_file import get_play_list

class TestArtist(unittest.TestCase):
		def test_get_play_list(self):
				response = get_play_list("37i9dQZF1E3585oSSAOUUK")
				assert response.status_code == 200, f'Error avalaible markets code 200, but got {response.status_code}'
				assert len(response.json()["tracks"]) >= 3
				track_list = response.json()["tracks"]
				playlist_playable = True
				for i in range(len(track_list)):
						if track_list[i]["album"]["is_playable"] == False:
								playlist_playable = False
				assert playlist_playable == True, "Error, tracks for this artist should be playable"

