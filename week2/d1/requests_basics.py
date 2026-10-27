import requests
url = "https://jsonplaceholder.typicode.com"


"""
Predictions
status code: 200
header: content-type: application/json
title: ""sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
"""
r = requests.get(url+"/posts/1", timeout=10)
print(f"status code: {r.status_code}\n")
print(f"header: {r.headers['Content-Type']}\n")
print(f"title: {r.json()['title']}\n\n")


"""
Predictions
url: url/posts?userId=1
length of json body: number of characters in dictionary
"""
r = requests.get(url+"/posts", params={"userId": 1}, timeout=10)
print(f"url: {r.url}\n")
print(f"length of json body: {len(r.json())}\n\n")


"""
Predictions
content-type: application/json
status code: 201
body: {"Tony": "LB"}
"""
r = requests.post(url+"/posts", json={"Tony": "LB"}, timeout=10)
print(f"content-type: {r.request.headers['Content-Type']}\n\n")
print(f"status code: {r.status_code}")
print(f"body: {r.json()}")


"""
status code: 404
prints error: 404
"""
r = requests.get(url+"/posts/9999", timeout=10)
print(f"status code: {r.status_code}")
try:
        r.raise_for_status()
except requests.HTTPError as e:
        print(f"error: {e}")
