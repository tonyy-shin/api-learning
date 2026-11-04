GET /getCoach?id=42
1. GET /coaches/42
getCoach should just be a noun. GET provides the verbs.

POST /coaches/42/delete
2. DELETE /coaches/42
delete should be the HTTP method since you want to delete.

GET /coaches/42/addReview?rating=5&text=Great
3. POST /coaches/42/reviews
POST should be the HTTP method since you want to add.

POST /updateReview/7 (changes only the rating)
4. PATCH /coaches/reviews/7
{"rating": 4}
since you are only updating a certain field, you use PUT method.

GET /reviewsForCoach/42
5. GET /coaches/42/reviews
should use correct path.

POST /coach (creates a coach)
6. POST /coaches
creates coach with id=43
