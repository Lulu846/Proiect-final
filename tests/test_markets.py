import unittest

from requests_file.requests_file import get_available_markets

class TestMarkets(unittest.TestCase):
		def test_available_markets(self):
				response = get_available_markets("IT")
				assert response.status_code == 200, f'Error avalaible markets code 200, but got {response.status_code}'
