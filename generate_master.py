import os
import json
import requests
import unittest
from dotenv import load_dotenv

# Load environmental variables from .env
load_dotenv()

if __name__ == '__main__':
  print(os.getenv("CLIENT_ID"))