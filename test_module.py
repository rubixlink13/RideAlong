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

    def test_encounter_index(self):
        self.assertTrue(type(api.get_encounter_index(self.BEARER_TOKEN)) == list)
        with self.assertRaises(requests.HTTPError):
            api.get_encounter_index("wrong")

    def test_achieve_reward(self):
        self.assertTrue(api.get_achieve_reward(self.BEARER_TOKEN, 6) == None)
        self.assertTrue(api.get_achieve_reward(self.BEARER_TOKEN, 4602) == 51954)
        self.assertTrue(api.get_achieve_reward(self.BEARER_TOKEN, 19343) == None)

    def test_achieve_info(self):
        self.assertTrue(api.get_achieve_info(self.BEARER_TOKEN, 4602) == {"name" : "Glory of the Icecrown Raider (10 player)", "category" : "Dungeons & Raids"})

    def test_check_item_is_mount(self):
        self.assertFalse(api.check_item_is_mount(self.BEARER_TOKEN, 19019))
        self.assertTrue(api.check_item_is_mount(self.BEARER_TOKEN, 51954))

    def test_item_name(self):
        self.assertTrue(api.get_item_name(self.BEARER_TOKEN, 51954) == "Reins of the Bloodbathed Frostbrood Vanquisher")

    def test_mount_name(self):
        self.assertTrue(api.get_mount_name(self.BEARER_TOKEN, 51954) == "Bloodbathed Frostbrood Vanquisher")
        self.assertTrue(api.get_mount_name(self.BEARER_TOKEN, 184183) == "Voracious Gorger")

    def test_mount_id(self):
        self.assertTrue(api.get_mount_id(self.BEARER_TOKEN, "Voracious Gorger") == 1443)
        self.assertTrue(api.get_mount_id(self.BEARER_TOKEN, "Bloodbathed Frostbrood Vanquisher") == 365)

    def test_encounter_drops(self):
        self.assertTrue(type(api.get_encounter_drops(self.BEARER_TOKEN, 1636)) == list)
        self.assertTrue(type(api.get_encounter_drops(self.BEARER_TOKEN, 2519)) == list)

    def test_encounter_info(self):
        self.assertTrue(api.get_encounter_info(self.BEARER_TOKEN, 1636) == {"type": "RAID", "name": "The Lich King", "instance": "Icecrown Citadel"}) 
        self.assertTrue(api.get_encounter_info(self.BEARER_TOKEN, 2519) == {"type": "RAID", "name": "Fyrakk the Blazing", "instance": "Amirdrassil, the Dream's Hope"}) 
        self.assertTrue(api.get_encounter_info(self.BEARER_TOKEN, 2396) == {"type": "DUNGEON", "name": "Nalthor the Rimebinder", "instance": "The Necrotic Wake"})

if __name__ == '__main__':
    unittest.main()