
Method | Usage | Safe | Idempotent | Body
GET | gets requested content with body | Y | Y | N
POST | posts reqested content onto server | N | N | Y
PATCH | patches/updates the content onto server | N | N | Y
QUERY | queers the data from server end without actually changing the server and returns the contents | Y | Y | Y
OPTIONS | Gives options of requests for the client | Y | Y | N
PUT | puts the requested content onto server | N | Y | Y
DELETE | deletes request content from server | Y | Y | Y
HEAD | Same with GET method but without body. Used to meta data | Y | Y | N




1. GET /coaches/42
Nothing changes with 2 requests
2. PUT /coaches/42 with {"name": "Smith", "rating": 4}
        - first call: puts the data by replacing the original one
        - second call: replaces the same data so server stays the same
3. PATCH /coaches/42 with {"rating": 4}
        - first: changes the rating from 3 to 4
        - second: nothing changes 
4. PATCH /coaches/42 with {"op": increment_rating"}
        - does not understnd operation increment_rating
        - second: same thing
5. POST /coaches with {"name": "Jones"}
        - Makes a new coach with the name Jones with a unique id
        - Makes another new caoch with the name Jones with a unique id
6. DELETE /coaches/42
        - deletes coach with id=42
        - data stays same since DELETE is idempotent
        - status code: 204(No content) then 404(Not found)
