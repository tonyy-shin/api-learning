from fastapi import FastAPI, Query

app = FastAPI()

# Fake data for now. Postgres replaces this in Week 5.
COACHES = [
    {"id": 1, "name": "Ava Kim", "sport": "soccer", "school_id": 3},
    {"id": 2, "name": "Ben Ortiz", "sport": "basketball", "school_id": 3},
    {"id": 3, "name": "Cara Lee", "sport": "soccer", "school_id": 5},
    {"id": 4, "name": "Dan Park", "sport": "hockey", "school_id": 5},
]


@app.get("/v1/health")
def read_health():
    return {"status": "ok"}


# TODO 1: GET /v1/coaches/{coach_id}
# - coach_id is a PATH parameter, type int
# - loop through COACHES and return the coach whose "id" matches
# - if none match, just return {"error": "not found"} for now
#   (proper 404s with HTTPException come later this week)
@app.get("/v1/coaches/{coach_id}")
def read_coach(coach_id: int):
        for c in COACHES:
                if c["id"] == coach_id:
                        return c
        return {"error": "not found"}



# TODO 2: GET /v1/coaches
# - QUERY parameters: sport (optional, default None),
#   limit (int, default 20), offset (int, default 0)
# - if sport is given, keep only coaches with that sport
# - then slice the list with offset and limit
# - return {"data": <the list>}
@app.get("/v1/coaches")
def get_coaches(sport: str | None = None, limit: int = Query(default=20, ge=1, le=100), offset: int = 0):
        if sport is None:
                return {"data": COACHES[offset:offset+limit]}

        coaches = list()
        for c in COACHES:
                if c["sport"] == sport:
                        coaches.append(c)
        return {"data": coaches[offset:offset+limit]}


"""
Predictions
a.	/v1/coaches/2
        - 200: "id": 2, "name": "Ben Ortiz", "sport": "basketball", "school_id": 3}
b	/v1/coaches/abc
        - 400: not found
c	/v1/coaches?sport=soccer
        - 200: {"data": [{"id": 1, "name": "Ava Kim", "sport": "soccer", "school_id": 3, {"id": 3, "name": "Cara Lee", "sport": "soccer", "school_id": 5}]}
d	/v1/coaches?limit=1&offset=1
        - 200: {"data": [{"id": 1, "name": "Ava Kim", "sport": "soccer", "school_id": 3}]}
e	/v1/coaches?limit=500
        - 200: {"data": [{"id": 1, "name": "Ava Kim", "sport": "soccer", "school_id": 3},
               {"id": 2, "name": "Ben Ortiz", "sport": "basketball", "school_id": 3},
               {"id": 3, "name": "Cara Lee", "sport": "soccer", "school_id": 5},
               {"id": 4, "name": "Dan Park", "sport": "hockey", "school_id": 5}]
"""
