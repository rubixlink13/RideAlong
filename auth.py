import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()

# Caches
_cached_access_token = ''
_access_token_expiry = 0

def get_access_token():

    TOKEN_URL = "https://oauth.battle.net/token"
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    global _cached_access_token, _access_token_expiry
    now = time.time()
    if _cached_access_token and now < _access_token_expiry:
        return _cached_access_token
    
    response = requests.post(
        TOKEN_URL,
        data = {"grant_type": "client_credentials"},
        auth = (CLIENT_ID, CLIENT_SECRET)
    )

    try:
        print("Sending Client Credentials...")
        response.raise_for_status()
        data = response.json()
        _cached_access_token = data["access_token"]
        _access_token_expiry = now + data.get("expires_in", 1800) - 60
        print("Success")
    except requests.HTTPError as e:
        print(f"HTTP Error: {e}")
        raise e
    except Exception as e:
        print(f"Unexpected Exception: {e}")
        raise e
    
    return _cached_access_token

if __name__ == "__main__":
    print(get_access_token())