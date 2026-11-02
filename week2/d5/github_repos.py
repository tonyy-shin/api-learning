import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

url = "https://api.github.com/users/tonyy-shin/repos"
params = {"per_page": 10}
headers = {"Authorization": f"Bearer {token}"}

# predict (no token): limit = 60
r = requests.get(url, params=params, timeout=10)
print("No token:", r.status_code, r.headers["X-RateLimit-Limit"])

# predict (with token): limit = 5000
r = requests.get(url, params=params, headers=headers, timeout=10)
print("With token:", r.status_code, r.headers["X-RateLimit-limit"])


# predict: how many repos will print? (at most 10 (comes from params))
if (r.status_code == 200):
        body = r.json()
        for b in body:
                name = b["name"]
                print(f"name: {name}\n")
