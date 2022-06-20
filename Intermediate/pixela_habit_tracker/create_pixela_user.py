import requests
from env.config import PIXELA_USER_NAME, PIXELA_USER_TOKEN, USER_ENDPOINT



USER_DATA = {
    "token": PIXELA_USER_TOKEN,
    "username": PIXELA_USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

res = requests.post(url=USER_ENDPOINT, json=USER_DATA)

print(res.text)