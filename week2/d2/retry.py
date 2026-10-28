import time
import requests

RETRY_STATUSES = {429, 502, 503, 504}

def fetch_with_retry(url, max_attempts=3, timeout=5):
    for attempt in range(1, max_attempts + 1):
        try:
                r = requests.get(url, timeout=timeout)
                if r.status_code in RETRY_STATUSES:
                        print(f"attempt {attempt}: got {r.status_code}")
                else:
                       r.raise_for_status()
                       return r
        except (requests.ConnectionError, requests.Timeout) as e:
                print(f"attempt {attempt}: {type(e).__name__}")
        if attempt == max_attempts:
                raise RuntimeError(f"failed after {max_attempts} attempts")
        else:
                wait = 2 ** (attempt - 1)
                print(f"waiting for {wait} seconds")
                time.sleep(wait)


if __name__ == "__main__":
    print(fetch_with_retry("https://postman-echo.com/get").status_code)

    try:
        print(fetch_with_retry("https://postman-echo.com/status/503"))
    except Exception as e:
        print(type(e).__name__, e)

    try:
        print(fetch_with_retry("https://postman-echo.com/status/404"))
    except Exception as e:
        print(type(e).__name__, e)


"""
1. gets the status code of 200
2. Status code is 503. Retries 2 times and then raises RuntimeError.
3. Status code is 404. raises the error, which is caught on except Exception as e. Does not return anything.
"""
