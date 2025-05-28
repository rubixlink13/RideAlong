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
		print("Requesting Achievement Reward...")
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

if __name__ == '__main__':
	print(len(get_achieve_index(auth.get_access_token())))
	