import auth
import requests
from dotenv import load_dotenv

# Load environmental variables from .env
load_dotenv()


def get_mount_index(BEARER_TOKEN):
	"""
	Fetch Mount Index
	"""
	REQUEST_URL = "https://us.api.blizzard.com/data/wow/mount/index?namespace=static-us&locale=en_US"
	response = requests.get(
		REQUEST_URL,
		headers = {"Authorization" : f"Bearer {BEARER_TOKEN}"}
	)
	try:
		print("Requesting Mount Index...")
		response.raise_for_status()
		data = response.json()
		print("Success")
	except requests.HTTPError as e:
		print(f"HTTP Error: {e}")
		raise e
	except Exception as e:
		print(f"Unexpected Exception: {e}")
		raise e
	return data["mounts"]

def get_achieve_index(BEARER_TOKEN):
	"""
	Fetch Achievement Index
	"""
	REQUEST_URL = "https://us.api.blizzard.com/data/wow/achievement/index?namespace=static-us&locale=en_US"
	response = requests.get(
		REQUEST_URL,
		headers = {"Authorization" : f"Bearer {BEARER_TOKEN}"}
	)
	try:
		print("Requesting Achievement Index...")
		response.raise_for_status()
		data = response.json()
		print("Success")
	except requests.HTTPError as e:
		print(f"HTTP Error: {e}")
		raise e
	except Exception as e:
		print(f"Unexpected Exception: {e}")
		raise e
	return data["achievements"]

def get_encounter_index(BEARER_TOKEN):
	"""
	Fetch Encounter Index
	"""
	REQUEST_URL = "https://us.api.blizzard.com/data/wow/journal-encounter/index?namespace=static-us&locale=en_US"
	response = requests.get(
		REQUEST_URL,
		headers = {"Authorization" : f"Bearer {BEARER_TOKEN}"}
	)
	try:
		print("Requesting Encounter Index...")
		response.raise_for_status()
		data = response.json()
		print("Success")
	except requests.HTTPError as e:
		print(f"HTTP Error: {e}")
		raise e
	except Exception as e:
		print(f"Unexpected Exception: {e}")
		raise e
	
	print(len(data["encounters"]))
	return data["encounters"]

def get_achieve_reward(BEARER_TOKEN, achieve_id):
	"""
	Fetch Achievement Reward
	"""
	REQUEST_URL = f"https://us.api.blizzard.com/data/wow/achievement/{achieve_id}?namespace=static-us&locale=en_US"
	response = requests.get(
		REQUEST_URL,
		headers = {"Authorization" : f"Bearer {BEARER_TOKEN}"}
	)
	try:
		print(f"Requesting Achievement Reward from {achieve_id}...")
		response.raise_for_status()
		data = response.json()
	except requests.HTTPError as e:
		print(f"HTTP Error: {e}")
		raise e
	except Exception as e:
		print(f"Unexpected Exception: {e}")
		raise e
	
	if (data.get("reward_description") == None):
		return None
	elif (not data.get("reward_description").startswith("Mount: ")):
		return None
	else:
		return data.get("reward_item").get("id")
	
def check_item_is_mount(BEARER_TOKEN, item_id):
	"""
	Checks if item is mount
	"""
	REQUEST_URL = f"https://us.api.blizzard.com/data/wow/item/{item_id}?namespace=static-us&locale=en_US"
	response = requests.get(
		REQUEST_URL,
		headers = {"Authorization" : f"Bearer {BEARER_TOKEN}"}
	)
	try:
		print(f"Checking if item {item_id} is mount...")
		response.raise_for_status()
		data = response.json()
	except requests.HTTPError as e:
		print(f"HTTP Error: {e}")
		raise e
	except Exception as e:
		print(f"Unexpected Exception: {e}")
		raise e

	return (data.get("item_class").get("id") == 15 and data.get("item_subclass").get("id") == 5)

def get_mount_name(BEARER_TOKEN, item_id):
	"""
	Gets mount name from item id
	"""
	REQUEST_URL = f"https://us.api.blizzard.com/data/wow/item/{item_id}?namespace=static-us&locale=en_US"
	response = requests.get(
		REQUEST_URL,
		headers = {"Authorization" : f"Bearer {BEARER_TOKEN}"}
	)
	try:
		print(f"Getting mount name from item {item_id}...")
		response.raise_for_status()
		data = response.json()
	except requests.HTTPError as e:
		print(f"HTTP Error: {e}")
		raise e
	except Exception as e:
		print(f"Unexpected Exception: {e}")
		raise e
	return data.get("preview_item").get("spells")[0].get("spell").get("name")

def get_mount_id(BEARER_TOKEN, mount_name):
	"""
	Gets mount id from mount name
	"""
	REQUEST_URL = f"https://us.api.blizzard.com/data/wow/search/mount?namespace=static-us&name.en_US={mount_name.lower().replace(" ", "%20")}&orderby=id&_page=1"
	response = requests.get(
		REQUEST_URL,
		headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
	)
	try:
		print(f"Getting mount id from mount {mount_name}...")
		response.raise_for_status()
		data = response.json()
	except requests.HTTPERROR as e:
		print(f"HTTP Error: {e}")
		raise e
	except Exception as e:
		print(f"Unexpected Exception: {e}")
		raise e
	for i in data.get("results"):
		if i.get("data").get("name").get("en_US") == mount_name:
			return i.get("data").get("id")
		
def get_encounter_drops(BEARER_TOKEN, encounter_id):
	"""
	Gets list of encounter drops from encounter id
	"""
	REQUEST_URL = f"https://us.api.blizzard.com/data/wow/journal-encounter/{encounter_id}?namespace=static-us&locale=en_US"
	response = requests.get(
		REQUEST_URL,
		headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
	)
	try:
		print(f"Getting list of encounter drops from encounter {encounter_id}...")
		response.raise_for_status()
		data = response.json()
	except requests.HTTPError as e:
		print(f"HTTP Error: {e}")
		raise e
	except Exception as e:
		print(f"Unexpected Exception: {e}")
		raise e
	return data.get("items")

def get_encounter_info(BEARER_TOKEN, encounter_id):
	"""
	Gets dict with instance name, encounter name, and instance type from encounter id
	"""
	REQUEST_URL = f"https://us.api.blizzard.com/data/wow/journal-encounter/{encounter_id}?namespace=static-us&locale=en_US"
	response = requests.get(
		REQUEST_URL,
		headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
	)
	try:
		print(f"Getting dict of encounter info from encounter {encounter_id}...")
		response.raise_for_status()
		data = response.json()
	except requests.HTTPError as e:
		print(f"HTTP Error: {e}")
		raise e
	except Exception as e:
		print(f"Unexpected Exception: {e}")
		raise e
	return {"type" : data.get("category").get("type"), "name" : data.get("name"), "instance" : data.get("instance").get("name")}


if __name__ == '__main__':
	print(len(get_achieve_index(auth.get_access_token())))
	