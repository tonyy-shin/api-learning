from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

coaches = [
    {"id": 1, "name": "Ava", "sport": "soccer"},
    {"id": 2, "name": "Ben", "sport": "basketball"},
]

reviews = []
next_review_id = 1


# TODO 1: fill in the ReviewCreate model (replace "pass")
#   rating: an int from 1 to 5  ->  use Field(ge=..., le=...)
#   text: a str
class ReviewCreate(BaseModel):
        rating: int = Field(ge=1, le=5, description="review rating")
        text: str


@app.post("/v1/coaches/{coach_id}/reviews", status_code=201)
def create_review(coach_id: int, review: ReviewCreate):
        global next_review_id
        ids = [c["id"] for c in coaches]

        if coach_id not in ids:
                raise HTTPException(status_code=404, detail="coach not found")

        new_review = {"id": next_review_id, "coach_id": coach_id, "rating": review.rating, "text": review.text}

        next_review_id += 1
        reviews.append(new_review)
        return new_review



"""
Predictions
a) POST /v1/coaches/1/reviews with {"rating": 4, "text": "Great coach"}
        - 201: the request body with the id and coach_id

b) the same request with "rating": 9
        - 422: error message

c) {"rating": 4} with no text
        - 422: missing field

d) POST /v1/coaches/99/reviews with a valid body
        - 404: coach not found error message

e) {"rating": "4", "text": "ok"}, where rating is a string. 
   Does Pydantic reject it or accept it? And why might it decide that way?
        - pydantic rejects it since we declared that rating is a int type
"""
