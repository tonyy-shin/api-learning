import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=100"
names = []
requests_sent = 0

while url is not None:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    requests_sent += 1

    data = r.json()
    for p in data["results"]:
        names.append(p["name"])
    url = data["next"]
    print(f"page {requests_sent}: got {len(data['results'])}, total so far {len(names)}")

print(f"Done. {requests_sent} requests, {len(names)} names")
print(f"First: {names[0]}, last: {names[-1]}")



"""
Predictions

1. Goes up to 14 requests: Gets 100 pokemon each call with 100 incremented to the total (adds 51 at the end).
2. When done, 14 requests will be sent(1351 pokemon) and there will be 1351 pokemon names stored.
3. first name will be bulbasaur, and last name will be the last pokemon in the data list of dicts.
"""
