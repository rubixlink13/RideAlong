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

if __name__ == '__main__':
	print(len(get_achieve_index(auth.get_access_token())))
	