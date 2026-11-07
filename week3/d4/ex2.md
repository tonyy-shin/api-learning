# Query parameters

## GET /v1/coaches
### Filters
        - sport=
        - school_id=
### Sort fields allowed
        - name
        - avg_rating (add field)
### Default sort
        - id
### Pagination (default limit, max limit)
        - default limit 20
        - max limit 100

## GET /v1/coaches/{id}/reviews
### Filters
        - rating
### Sort fields allowed
        - rating
        - created_at
### Default sort
        - -created_at
### Pagination (default limit, max limit)
        - default limit 5
        - max limit 30
