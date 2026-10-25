import json

text = '{"name": "Kim", "active": true, "school": {"name": "RIT"}, "ratings": [4, 5, 3]}'

coach = json.loads(text)
print(type(text))
print(type(coach))
print(coach["school"]["name"])
print(sum(coach["ratings"]) / len(coach["ratings"]))
print(coach["active"])

back = json.dumps(coach)
print(type(back))
print(back)
