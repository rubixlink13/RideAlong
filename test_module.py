import unittest
import auth
import api
import requests

class TestAPI(unittest.TestCase):
    # def test_access_token(self):
    #     with self.assertRaises(requests.HTTPError):
    #         auth.get_access_token()
    BEARER_TOKEN = auth.get_access_token()
    
    def test_mount_index(self):
        self.assertTrue(type(api.get_mount_index(self.BEARER_TOKEN)) == list)
        with self.assertRaises(requests.HTTPError):
            api.get_mount_index("wrong")

    def test_achieve_index(self):
        self.assertTrue(type(api.get_achieve_index(self.BEARER_TOKEN)) == list)
        with self.assertRaises(requests.HTTPError):
            api.get_achieve_index("wrong")

    def test_achieve_reward(self):
        self.assertTrue(api.get_achieve_reward(self.BEARER_TOKEN, 6) == None)
        self.assertTrue(api.get_achieve_reward(self.BEARER_TOKEN, 4602) == 51954)
        self.assertTrue(api.get_achieve_reward(self.BEARER_TOKEN, 19343) == None)

    def test_check_item_is_mount(self):
        self.assertFalse(api.check_item_is_mount(self.BEARER_TOKEN, 19019))
        self.assertTrue(api.check_item_is_mount(self.BEARER_TOKEN, 51954))

    def test_mount_name(self):
        self.assertTrue(api.get_mount_name(self.BEARER_TOKEN, 51954) == "Bloodbathed Frostbrood Vanquisher")
        self.assertTrue(api.get_mount_name(self.BEARER_TOKEN, 184183) == "Voracious Gorger")

if __name__ == '__main__':
    unittest.main()