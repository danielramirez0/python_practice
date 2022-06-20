import requests
import datetime as dt
from env.config import GRAPH_ENDPOINT, HEADERS, PIXELA_USER_NAME, PIXELA_USER_TOKEN, GRAPH_ID

today = dt.datetime.now()
yesterday = dt.datetime(today.year, today.month, today.day -1).strftime("%Y%m%d")
print(yesterday)

# date_string = f"{today.year}{today.month:02d}{today.day:02d}"
date_string = today.strftime("%Y%m%d")

body = {
    "date": date_string,
    "quantity": "1.5",
}
res = requests.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}", headers=HEADERS, json=body)
res.raise_for_status()
print(res.text)

body["date"] = yesterday
body["quantity"] = "100"

res = requests.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}", headers=HEADERS, json=body)
print(res.text)

update_endpoint = f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{date_string}"

body = {
    "date": date_string,
    "quantity": "5.5"
}

update_req = requests.put(url=update_endpoint, headers=HEADERS, json=body)
res.raise_for_status()
print(update_req.text)

delete_req = requests.delete(url=update_endpoint, headers=HEADERS)
delete_req.raise_for_status()
print(delete_req.text)