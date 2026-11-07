# Exercise 1 - writing URLs

## Part A. Write a URL for each:
a. All soccer coaches
        - /v1/coaches?sport=soccer
b. Soccer coaches, highest rating first, 10 per page
        - /v1/coaches?sport=soccer&sort=-rating&limit=10
c. Page 3 of (b)
        - /v1/coaches?sport=soccer&sort=-rating&offset=20&limit=10
d. Reviews for coach 7, newest first
        - /v1/coaches/7/reviews?sort=-created_at
e. Coaches at school 3, sorted by name A to Z
        - /v1/schools/3/coaches?sort=name


## Part B. Predict the status code for each of these:
f. GET /v1/coaches?sport=curling (your site has no curling coaches)
        - 200 with empty list
g. GET /v1/coaches?sort=-salary (salary isn’t a field you allow sorting by)
        - 422
h. GET /v1/coaches?limit=500 (you have two options: quietly cap it at 100, or reject it with 422. Pick one and write why.)
        - 422: quietly capping it at one is not detailed enough for the users
