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
        self.assertTrue(type(api.get_mount_index(self.BEARER_TOKEN)) == dict)
        with self.assertRaises(requests.HTTPError):
            api.get_mount_index("wrong")

    def test_achieve_index(self):
        self.assertTrue(type(api.get_achieve_index(self.BEARER_TOKEN)) == dict)
        with self.assertRaises(requests.HTTPError):
            api.get_achieve_index("wrong")

    def test_encounter_index(self):
        self.assertTrue(type(api.get_encounter_index(self.BEARER_TOKEN)) == dict)
        with self.assertRaises(requests.HTTPError):
            api.get_encounter_index("wrong")

    def test_achieve_info(self):
        self.assertTrue(type(api.get_achieve_info(self.BEARER_TOKEN, 6)) == dict)
        with self.assertRaises(requests.HTTPError):
            api.get_achieve_info("wrong", 6)

    def test_item_info(self):
        self.assertTrue(type(api.get_item_info(self.BEARER_TOKEN, 51954)) == dict)
        with self.assertRaises(requests.HTTPError):
            api.get_item_info("wrong", 51954)

    def test_mount_search(self):
        self.assertTrue(type(api.get_mount_search(self.BEARER_TOKEN, "Voracious Gorger")) == dict)
        with self.assertRaises(requests.HTTPError):
            api.get_mount_search("wrong", "Voracious Gorger")

    def test_encounter_info(self):
        self.assertTrue(type(api.get_encounter_info(self.BEARER_TOKEN, 1636)) == dict)
        with self.assertRaises(requests.HTTPError):
            api.get_encounter_info("wrong", 1636)


if __name__ == '__main__':
    unittest.main()