import requests

url = "https://postman-echo.com/headers"
my_headers = {
    "User-Agent": "api-learning/0.1",
    "X-Tony-Test": "hello",
}

# TODO 1: send a GET to url with my_headers attached (hint: headers=...)
r = requests.get(url, headers=my_headers)

# TODO 2: print what the server says it received (the JSON body)
print(r.json())

# TODO 3: print the response's Content-Type header
print(r.headers['Content-Type'])

# TODO 4: print it again using all-lowercase "content-type"
print(r.headers['content-type'])



"""
Predictions
1. it will appear as is.
2. the id will be set
3. 4 will not raise an error since everything is turned into lower case.
"""
