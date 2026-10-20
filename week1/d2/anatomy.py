from urllib.parse import urlsplit, parse_qs
import requests

url = "https://httpbin.org/anything/coaches/42?sport=soccer&sort=-rating"

parts = urlsplit(url)
print("scheme: ", parts.scheme)
print("host: ", parts.netloc)
print("path: ", parts.path)
print("query: ", parse_qs(parts.query))

r = requests.post(
        url,
        headers={"X-Study-Session": "day2"},
        json={"coach_id": 42, "rating": 5},
        timeout=10,
)

print("\n--- request as sent ---")
print(r.request.method, r.request.url)
for k, v in r.request.headers.items():
        print(f"{k}: {v}")
print("body: ", r.request.body)

echo = r.json()
print("\n--- server saw ---")
print("method:", echo["method"])
print("args:  ", echo["args"])
print("json:  ", echo["json"])
