import api
from mount import Mount, Source, Achievement, Drop

def generate(BEARER_TOKEN):
    master = []
    add_achievement_mounts(BEARER_TOKEN, master)
    add_encounter_mounts(BEARER_TOKEN, master)
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
            item_id = achieve_info.get("reward_item").get("id")
            item_name = achieve_info.get("reward_item").get("name")
            item_info = api.get_item_info(BEARER_TOKEN, item_id)
            mount_name = item_info.get("preview_item").get("name")
            mount_id = _get_mount_id(BEARER_TOKEN, mount_name)
            achieve_name = achieve_info.get("name")
            category = achieve_info.get("category").get("name")

            master.append(Mount(mount_id, mount_name, item_id, item_name, Achievement(category, achieve_id, achieve_name)))


def add_encounter_mounts(BEARER_TOKEN, master):
    pass


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
    print(master)