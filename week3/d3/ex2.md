# Ex2: Error shapes

## Error format
{"error": {"code": "...", "message": "..."}}


## 1) GET /v1/coaches/999 (coach doesn't exist)
Status: 404
Body: {"error": {"code": "not_found", "message": "Coach 999 does not exist"}}


## 2) POST /v1/coaches/7/reviews with {"rating": 9, "text": "ok"}
Status: 422
Body: {"error": {"code": "validation_error", "message": "rating must be between 1 and 5"}}


## 3) POST /v1/coaches/7/reviews with {"text": "ok"}
Status: 422
Body: {"error": {"code": "validation_error", "message": "rating is required"}}


## 4) PATCH /v1/reviews/4 (not logged in)
Status: 401
Body: {"error": {"code": "unauthorized", "message": "You must be logged in to edit a review"}}


## Bonus: should 2 and 3 share the same code?
Answer: Yes, both use "validation_error"
Why: The client handles both the same way, by showing the user what's wrong with the input. 
The message says which rule failed.
