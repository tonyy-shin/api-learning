# Write the exact JSON body your API sends back in each of these 3 cases. 
# Use the fields from your week3/d2/ex1.md and ex2.md.


## a) GET /v1/coaches/7 → 200
One coach as a single JSON object.
        - {"id": 7, "school_id": 1, "name": "Bill", "sport": "soccer"}


## b) GET /v1/coaches/7/reviews?limit=2 → 200
A list of reviews. Wrap it like this, using your own review fields inside data:

Prediction: before you write (b), answer one question. 
Why wrap the list in {"data": [...]} instead of sending back a bare array [...]?
        - makes room for metadata.

json
{
  "data": [{"id": 1, "coach_id": 7, "rating": 2, "text": "poor"}, {"id": 4, "coach_id": 7, "rating": 5, "text": "great"}],
  "count": 38,
  "next": "/v1/coaches/7/reviews?offset=2&limit=2",
  "previous": null
}


## c) POST /v1/coaches/7/reviews → 201
Write the request body the client sends, then the response body. 
Two sessions ago you learned what a 201 response should contain, so use that.


Request Body
- {"rating": 2, "text": "poor"}

Response Body
- {"id": 1, "coach_id": 7, "rating": 2, "text": "poor"}
