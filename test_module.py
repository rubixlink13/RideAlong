import unittest
import auth
import requests

class TestAPI(unittest.TestCase):
    def test_access_token(self):
        with self.assertRaises(requests.HTTPError):
            auth.get_access_token()

if __name__ == '__main__':
    unittest.main()