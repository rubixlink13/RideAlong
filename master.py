import api
import json
import requests
from mount import Mount, Source, Achievement, Drop

def generate(BEARER_TOKEN):
    master = []
    add_achievement_mounts(BEARER_TOKEN, master)
    save_json({"data" : [mount.to_dict() for mount in master]})
    add_encounter_mounts(BEARER_TOKEN, master)
    save_json({"data" : [mount.to_dict() for mount in master]})
    return master

def add_achievement_mounts(BEARER_TOKEN, master):
    """
    Adds achievement mounts to the master list using the following steps:
    1. Create achievement index
    2. For each achievement, check if there's an mount reward
    3. If there's a mount reward, get item ID
    4. Convert item ID to a Mount object
    5. Add Mount object to master list
    """

    index = api.get_achieve_index(BEARER_TOKEN)
    achieve_list = index.get("achievements")

    for achieve in achieve_list:
        achieve_id = achieve.get("id")
        
        achieve_info = api.get_achieve_info(BEARER_TOKEN, achieve_id)
        if achieve_info.get("reward_description") is not None and achieve_info.get("reward_description").startswith("Mount: "):
            if achieve_info.get("reward_item") is not None:
                item_id = achieve_info.get("reward_item").get("id")
                item_name = achieve_info.get("reward_item").get("name")
                try:
                    item_info = api.get_item_info(BEARER_TOKEN, item_id)
                except requests.HTTPError as e:
                    print(f"Item {item_id} not found")
                    continue
                if item_info.get("preview_item").get("spells") is not None:
                    mount_name = item_info.get("preview_item").get("spells")[0].get("spell").get("name")
                else:
                    continue
            else:
                mount_name = achieve_info.get("reward_description")[7:]
            mount_id = _get_mount_id(BEARER_TOKEN, mount_name)
            achieve_name = achieve_info.get("name")
            category = achieve_info.get("category").get("name")

            master.append(Mount(mount_id, mount_name, item_id, item_name, Achievement(category, achieve_id, achieve_name)))

def add_encounter_mounts(BEARER_TOKEN, master):
    """
    Adds encounter mounts to the master list using the following steps:
    1. Create encounter index
    2. For each encounter, get list of drops
    3. For each drop, check if drop is mount
    4. If mount, get item ID
    5. Convert item ID to Mount object
    6. Add Mount object to master list
    """

    index = api.get_encounter_index(BEARER_TOKEN)
    encounter_list = index.get("encounters")

    for encounter in encounter_list:
        encounter_info = api.get_encounter_info(BEARER_TOKEN, encounter.get("id"))
        drops_list = encounter_info.get("items")
        for drop in drops_list:
            try:
                item_info = api.get_item_info(BEARER_TOKEN, drop.get("item").get("id"))
            except requests.HTTPError as e:
                print(f"Item {drop.get("item").get("id")} not found")
                continue
            if item_info.get("item_class").get("id") == 15 and item_info.get("item_subclass").get("id") == 5:
                mount_name = item_info.get("preview_item").get("spells")[0].get("spell").get("name")
                mount_id = _get_mount_id(BEARER_TOKEN, mount_name)
                item_id = item_info.get("id")
                item_name = item_info.get("name")
                category = encounter_info.get("category").get("type")
                instance_id = encounter_info.get("instance").get("id")
                instance_name = encounter_info.get("instance").get("name")
                encounter_id = encounter_info.get("id")
                encounter_name = encounter_info.get("name")

                master.append(Mount(mount_id, mount_name, item_id, item_name, Drop(category, instance_id, instance_name, encounter_id, encounter_name)))


def save_json(master):
    with open("master.json", "w") as file:
        json.dump(master, file)
    print("Saved to json!")
        
def _get_mount_id(BEARER_TOKEN, mount_name):
    """
    Helper function that gets mount id from mount name
    """

    mount_search = api.get_mount_search(BEARER_TOKEN, mount_name)
    for result in mount_search.get("results"):
        if result.get("data").get("name").get("en_US") == mount_name:
            return result.get("data").get("id")


if __name__ == "__main__":
    import auth
    BEARER_TOKEN = auth.get_access_token()
    master = generate(BEARER_TOKEN)
    for mount in master:
        print(str(mount))