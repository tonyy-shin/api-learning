import os
import requests
from dotenv import load_dotenv

# TODO 1: load the .env file
load_dotenv()

# TODO 2: read NASA_API_KEY into api_key
api_key = os.getenv("NASA_API_KEY")

url = "https://api.nasa.gov/planetary/apod"
# TODO 3: send the key as a query param named api_key
r = requests.get(url, params={"api_key": api_key})


print(r.status_code)
print(r.json()["title"])

# TODO 4: print how many requests you have left (look in r.headers for a RateLimit header)
print(r.headers["X-RateLimit-Remaining"])
