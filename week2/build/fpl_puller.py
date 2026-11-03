import csv
import time

import requests

URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
OUTPUT = "goalkeepers.csv"
RETRY_STATUSES = {429, 500, 502, 503, 504}
FIELDS = ["id", "first_name", "second_name", "price", "form", "points_per_game",
          "total_points", "clean_sheets_per_90", "goals_conceded_per_90"]


def fetch_json(url, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        try:
            r = requests.get(url, timeout=10)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            print(f"Attempt {attempt}: {type(e).__name__}")
        else:
                if r.status_code in RETRY_STATUSES:
                        print(f"attempt {attempt}: {r.status_code}")
                else:
                        r.raise_for_status()
                        return r.json()
        if attempt < max_attempts:
            time.sleep(2 ** attempt)

    raise RuntimeError(f"Gave up after {max_attempts} attempts")


def get_goalkeepers(body):
        elements = body["elements"]
        players = list()
        for p in elements:
                if p["element_type"] == 1:
                        players.append(p)
        return players


def write_csv(players, path):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for p in players:
                row = p.copy()
                row["price"] = row["now_cost"] / 10
                writer.writerow(row)


def main():
    try:
        body = fetch_json(URL)
    except (requests.exceptions.RequestException, RuntimeError) as e:
        print(f"Failed: {e}")
        return

    goalkeepers = get_goalkeepers(body)
    write_csv(goalkeepers, OUTPUT)
    print(f"Saved {len(goalkeepers)} goalkeepers to {OUTPUT}")


if __name__ == "__main__":
    main()
