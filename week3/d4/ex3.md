# Exercise 3 - curl github repos

## Predictions
        - It will have 2 repos
        - We will have to look at the updated_at field to confirm the sorting



## Result
curl -s "https://api.github.com/users/tonyy-shin/repos?sort=updated&direction=desc&per_page=2" | grep -E '"name"|"updated_at"'

    "name": "api-learning",
    "updated_at": "2026-11-06T19:07:14Z",
    "name": "Smart-Sweat-Band-Project",
    "updated_at": "2026-11-05T21:51:10Z",


## Comparision
Github: sort=updated&direction=desc, per_page + page
Mine: sort=-avg_rating (minus means descending), limit + offset
