import requests

CODES = [200, 201, 204, 301, 304, 400, 401, 403, 404, 409, 422, 429 500, 503]
FAMILY = {2: "success", 3: "redirection", 4: "client error", 5: "server error"}

for code in CODES:
        r = requests.get(f"https://postman-echo.com/status/{code}",
                         allow_redirects=False, timeout=10)
        print(f"{r.status_code}  {r.reason:<22} {FAMILY[r.status_code // 100]:<13} "
          f"ok={r.ok!s:<5} body={len(r.content)}B")
