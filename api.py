import auth
import requests
from dotenv import load_dotenv

# Load environmental variables from .env
load_dotenv()

def _api_request(REQUEST_URL, BEARER_TOKEN, msg):
	"""
	Helper function for generating an api request
	"""
	response = requests.get(
		REQUEST_URL,
		headers = {"Authorization" : f"Bearer {BEARER_TOKEN}"}
	)
	try:
		print(msg)
		response.raise_for_status()
		data = response.json()
		print("Success")
	except requests.HTTPError as e:
		print(f"HTTP Error: {e}")
		raise e
	except Exception as e:
		print(f"Unexpected Exception: {e}")
		raise e
	print(type(data))
	return data


def get_mount_index(BEARER_TOKEN):
	"""
	Fetch Mount Index
	"""
	REQUEST_URL = "https://us.api.blizzard.com/data/wow/mount/index?namespace=static-us&locale=en_US"
	
	return _api_request(REQUEST_URL, BEARER_TOKEN, "Requesting Mount Index...")

def get_achieve_index(BEARER_TOKEN):
	"""
	Fetch Achievement Index
	"""
	REQUEST_URL = "https://us.api.blizzard.com/data/wow/achievement/index?namespace=static-us&locale=en_US"
	
	return _api_request(REQUEST_URL, BEARER_TOKEN, "Requesting Achievement Index...")

def get_encounter_index(BEARER_TOKEN):
	"""
	Fetch Encounter Index
	"""
	REQUEST_URL = "https://us.api.blizzard.com/data/wow/journal-encounter/index?namespace=static-us&locale=en_US"
	
	return _api_request(REQUEST_URL, BEARER_TOKEN, "Requesting Encounter Index...")

def get_achieve_info(BEARER_TOKEN, achieve_id):
	"""
	Gets achievement info (dict) from achievement id
	"""
	REQUEST_URL = f"https://us.api.blizzard.com/data/wow/achievement/{achieve_id}?namespace=static-us&locale=en_US"

	return _api_request(REQUEST_URL, BEARER_TOKEN, f"Requesting Achievement Info from {achieve_id}...")


def get_item_info(BEARER_TOKEN, item_id):
	"""
	Gets item info (dict) from item id
	"""
	REQUEST_URL = f"https://us.api.blizzard.com/data/wow/item/{item_id}?namespace=static-us&locale=en_US"

	return _api_request(REQUEST_URL, BEARER_TOKEN, f"Requesting Item Info from {item_id}...")

def get_mount_search(BEARER_TOKEN, mount_name):
	"""
	Gets mount search (dict) from mount name
	"""
	REQUEST_URL = f"https://us.api.blizzard.com/data/wow/search/mount?namespace=static-us&name.en_US={mount_name.lower().replace(" ", "%20")}&orderby=id&_page=1"

	return _api_request(REQUEST_URL, BEARER_TOKEN, f"Requesting Mount Search for {mount_name}...")
		
def get_encounter_info(BEARER_TOKEN, encounter_id):
	"""
	Gets encounter info (dict) from encounter id
	"""
	REQUEST_URL = f"https://us.api.blizzard.com/data/wow/journal-encounter/{encounter_id}?namespace=static-us&locale=en_US"

	return _api_request(REQUEST_URL, BEARER_TOKEN, f"Requesting Encounter Info from {encounter_id}...")


if __name__ == '__main__':
	print(len(get_achieve_index(auth.get_access_token())))
	