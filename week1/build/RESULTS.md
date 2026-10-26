# Week 1 Build — curl only (JSONPlaceholder)

| # | Method + path | Actual | What I learned |
|---|---------------|--------|----------------|
| 1 | GET /posts/1 | 200, full post JSON (userId, id, title, body) | Posts 1–100 already exist. |
| 2 | GET /posts/9999 | 404, body is `{}` | A 404 still has a body but an empty JSON object, not "nothing". |
| 3 | POST /posts | 201, echoes my JSON plus `"id": 101` | 201 means created; the server assigns the id. |
| 4 | GET /posts/101 | 404, `{}` | The POST was faked — JSONPlaceholder never saves writes. |
| 5 | PUT /posts/1 (title only) | 200, `{"title": "only a title", "id": 1}` | PUT replaces the whole post; userId and body are gone, id comes from the URL. 200 because post 1 already existed. |
| 6 | DELETE /posts/1 | 200, `{}` | Some APIs return 200 + empty object instead of 204. |
| 7 | GET /posts/1 | 200, original post unchanged | The delete was faked too. |
| B | PATCH /posts/1 (title only) | 200, full post with only title changed | PATCH keeps userId and body; PUT drops them. |

## What I learned
        - JSONPlaceholder fakes every write: realistic responses to POST, PUT, PATCH and DELETE, but nothing on the server changes.
        - A 404 still has a body but empty: {}
