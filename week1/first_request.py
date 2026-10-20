import requests

resp = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)
print("Status: ", resp.status_code)
print("Content-Type: ", resp.headers["Content-Type"])
print("Name: ", resp.json()["name"])
print("username: ", resp.json()["username"])
print("phone: ", resp.json()["phone"])
print("company name: ", resp.json()["company"]["name"])
