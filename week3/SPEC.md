# RateMyCoach API — v1 Spec

All paths start with `/v1`. All bodies are JSON (`Content-Type: application/json`).

## Resources and fields

### Coach
| Field      | Type           | Set by | Notes                                   |
|------------|----------------|--------|-----------------------------------------|
| id         | integer        | server |                                         |
| name       | string         | client | required                                |
| sport      | string         | client | required, e.g. "soccer"                 |
| school_id  | integer        | client | required, must be an existing school    |
| avg_rating | number or null | server | read-only, average of this coach's reviews; null if none |

### School
| Field | Type    | Set by | Notes    |
|-------|---------|--------|----------|
| id    | integer | server |          |
| name  | string  | client | required |

### Review
| Field      | Type     | Set by | Notes                      |
|------------|----------|--------|----------------------------|
| id         | integer  | server |                            |
| coach_id   | integer  | server | taken from the URL path    |
| rating     | integer  | client | required, 1–5              |
| text       | string   | client | required                   |
| created_at | datetime | server | ISO 8601, e.g. "2026-11-10T16:41:00Z" |

## Shared shapes

### List response
```json
{
  "data": [ ...items... ],
  "next": "/v1/coaches?sport=soccer&offset=20&limit=20"
}
```
- `next` keeps the current filters and sort, and is `null` on the last page.

### Error response
```json
{
  "error": {
    "code": "invalid_rating",
    "message": "rating must be between 1 and 5"
  }
}
```
- The status goes in the status line, not the body.
- `code` is snake_case and stable, so clients branch on it.
- `message` is for humans and names the field.

Error codes used:
| Code               | Status | When                                      |
|--------------------|--------|-------------------------------------------|
| invalid_json       | 400    | body can't be parsed                      |
| missing_field      | 422    | a required field is absent                |
| invalid_rating     | 422    | rating not an integer 1–5                 |
| invalid_query      | 422    | bad sort, filter, or limit value          |
| coach_not_found    | 404    | no coach with that id                     |
| school_not_found   | 404    | no school with that id                    |
| review_not_found   | 404    | no review with that id                    |

## Endpoints

| Method | Path                               | Request body                          | Success response        | Error statuses |
|--------|------------------------------------|---------------------------------------|-------------------------|----------------|
| GET    | /v1/coaches                        | none                                  | 200, List of Coach      | 422            |
| GET    | /v1/coaches/{coach_id}             | none                                  | 200, Coach              | 404            |
| POST   | /v1/coaches                        | {name, sport, school_id}              | 201, Coach              | 400, 404, 422  |
| PATCH  | /v1/coaches/{coach_id}             | any of {name, sport, school_id}       | 200, Coach              | 400, 404, 422  |
| DELETE | /v1/coaches/{coach_id}             | none                                  | 204, no body            | 404            |
| GET    | /v1/schools                        | none                                  | 200, List of School     | 422            |
| GET    | /v1/schools/{school_id}            | none                                  | 200, School             | 404            |
| GET    | /v1/schools/{school_id}/coaches    | none                                  | 200, List of Coach      | 404, 422       |
| GET    | /v1/coaches/{coach_id}/reviews     | none                                  | 200, List of Review     | 404, 422       |
| POST   | /v1/coaches/{coach_id}/reviews     | {rating, text}                        | 201, Review             | 400, 404, 422  |
| GET    | /v1/reviews/{review_id}            | none                                  | 200, Review             | 404            |
| PATCH  | /v1/reviews/{review_id}            | any of {rating, text}                 | 200, Review             | 400, 404, 422  |
| DELETE | /v1/reviews/{review_id}            | none                                  | 204, no body            | 404            |

Notes:
- POST /v1/coaches returns 404 `school_not_found` if `school_id` doesn't exist.
- Creating, editing, or deleting a review changes that coach's `avg_rating`.
- Server-set fields (`id`, `coach_id`, `avg_rating`, `created_at`) sent by a client are ignored.

## Query parameters

### GET /v1/coaches (also /v1/schools/{school_id}/coaches)
| Param     | Values                                      | Default |
|-----------|---------------------------------------------|---------|
| sport     | string                                      | none    |
| school_id | integer (only on /v1/coaches)               | none    |
| sort      | name, -name, avg_rating, -avg_rating        | id      |
| limit     | 1–100                                       | 20      |
| offset    | 0 or more                                   | 0       |

### GET /v1/coaches/{coach_id}/reviews
| Param  | Values                                       | Default     |
|--------|----------------------------------------------|-------------|
| rating | 1–5                                          | none        |
| sort   | rating, -rating, created_at, -created_at     | -created_at |
| limit  | 1–30                                         | 5           |
| offset | 0 or more                                    | 0           |

Any value outside these ranges → 422 `invalid_query` (no silent capping).
