# Resources

## coaches
Fields: id, school_id, name, sport
Belongs to: each coach belongs to a school
Has many: one coach has many review

## schools
Fields: id, name 
Belongs to: None
Has many: one school has many coaches

## reviews
Fields: id, coach_id, rating, text
Belongs to: each review belongs to a coach
Has many: None


# Decisions

## Who sets each field?
Server sets: id for schools, coaches, and reviews
Client sends: other fields except for id

## Coach moves
If coach 42 changes from school 1 to school 2, what field changes?
Do the coach's reviews need to change?
- reviews do not change. The only thing that changes is the coach's school_id

## Review URL
Choice: /reviews/7 for one review, /coaches/42/reviews for a coach's reviews
Reason: A review's ID is already unique, so getting one review doesn't need its school or coach. Leaving them out also means the URL doesn't change when a coach moves schools.
