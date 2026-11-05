# Endpoints

## Schools
List all schools: GET /schools
Get one school: GET /schools/1
Create a school: POST /schools with body {school fields}

## Coaches
List all coaches: GET /coaches
List only soccer coaches: GET /coaches?sport=soccer
List one school's coaches: GET /schools/1/coaches
Get one coach: GET /coaches/42
Create a coach at a school: POST /schools/1/coaches with body {coaches fields}
Move a coach to another school: PATCH /coaches/42 with body {"school_id": 2}
Delete a coach: DELETE /coaches/42

## Reviews
List one coach's reviews: GET /coaches/42/reviews
Get one review: GET /reviews/7
Create a review for a coach: POST /coaches/42/reviews with body {review fields} 
Change only a review's rating: PATCH /reviews/7 with body {"rating": 3}
Delete a review: DELETE /reviews/7
