import requests

url = "https://httpbin.org/anything"
payload = {"coach": "Smith", "rating": 4}

for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        body = payload if method in {"POST", "PUT", "PATCH"} else None
        r = requests.request(method, url, json=body, timeout=10)
        data = r.json()
        print(f"{method:7} {r.status_code}  server saw: {data['method']:7} body: {data['json']}")
