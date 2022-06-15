import requests

ENDPOINT = "http://opentdb.com/api.php"
PARAMS = {
    "amount": 10,
    "type": "boolean"
}

res = requests.get(ENDPOINT, params=PARAMS)
res.raise_for_status()
question_data = res.json()["results"]