import requests

url = "https://postman-echo.com/"

"""
1. status code: 404
2. status: False
"""
r = requests.get(url+"status/404", timeout=5)
print(f"status code: {r.status_code}")
print(f"status: {r.ok}\n")


"""
Catches the 404 error
"""
try:
        r.raise_for_status()
except requests.HTTPError as e:
        print(f"Error: {e}\n")



"""
gives no answer because the response gives back in 3 seconds but I only give it a second to respond.
"""
try:
        r = requests.get(url + "delay/3", timeout = 1)
except requests.Timeout as e:
        print(type(e).__name__, e)


"""
The connection does not exist.
So it raises an exception of no connection
"""
try:
        r = requests.get("https://does-not-exist-xyz123.com",timeout=5)
except requests.ConnectionError as e:
        print(type(e).__name__, e)


"""
Server answers 503 error.
Does not print anything since 503 errors give a response back.
So, it doesn't raise an error.
The client should retry when server is ready.
A 503 error mostly indicates that the server is not ready to handle the request (server maintenence).
"""
try:
        r = requests.get(url + "status/503", timeout=5)
except requests.HTTPError as e:
        print(f"Error: {e}")
