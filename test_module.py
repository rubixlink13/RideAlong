import unittest
import auth
import api
import requests

class TestAPI(unittest.TestCase):
    # def test_access_token(self):
    #     with self.assertRaises(requests.HTTPError):
    #         auth.get_access_token()
    
    def test_mount_index(self):
        self.assertTrue(type(api.get_mount_index(auth.get_access_token())) == dict)
        with self.assertRaises(requests.HTTPError):
            api.get_mount_index("wrong")

if __name__ == '__main__':
    unittest.main()