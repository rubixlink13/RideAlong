import unittest
import auth
import api
from mount import Mount, Source, Achievement, Drop
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

class TestAchieveMount(unittest.TestCase):
    achieve_mount = Mount(364, "Icebound Frostbrood Vanquisher", 51955, "Reins of the Icebound Frostbrood Vanquisher", Achievement("Dungeons & Raids", 4603, "Glory of the Icecrown Raider (25 player)"))
    
    def test_mount_id(self):
        self.assertTrue(self.achieve_mount.get_mount_id() == 364)

    def test_mount_name(self):
        self.assertTrue(self.achieve_mount.get_mount_name() == "Icebound Frostbrood Vanquisher")

    def test_item_id(self):
        self.assertTrue(self.achieve_mount.get_item_id() == 51955)
    
    def test_item_name(self):
        self.assertTrue(self.achieve_mount.get_item_name() == "Reins of the Icebound Frostbrood Vanquisher")

    def test_source(self):
        self.assertTrue(type(self.achieve_mount.get_source()) == Achievement)

    def test_category(self):
        self.assertTrue(self.achieve_mount.get_source().get_category() == "Dungeons & Raids")

    def test_achieve_id(self):
        self.assertTrue(self.achieve_mount.get_source().get_achievement_id() == 4603)

    def test_achieve_name(self):
        self.assertTrue(self.achieve_mount.get_source().get_achievement_name() == "Glory of the Icecrown Raider (25 player)")


if __name__ == '__main__':
    unittest.main()