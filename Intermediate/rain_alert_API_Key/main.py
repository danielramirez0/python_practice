from config import FROM_NUMBER, OW_KEY, TO_NUMBER, TW_KEY, TW_ACCT
import requests
from twilio.rest import Client
# if hosting on pythonAnywhere need additional config for proxy client
from twilio.http.http_client import TwilioHttpClient
import os
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = { "https": os.environ["https_proxy"]}

# if using exvironment variables instead of config.py
example_key = os.environ.get("MY_ENVIRONMENT_VAR")
# if running on pythonAywhere, will need to add "export KEY=value; in front of python3 main.py in command of scheduled task"

V3_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 47.38
MY_LON = 83.06
EXCLUSIONS = "current,minutely,daily,alerts"
ID_THRESHOLD_RAIN = 700

params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": EXCLUSIONS,
    "appid": OW_KEY
}

res = requests.get(url=V3_ENDPOINT, params=params)
res.raise_for_status()
data = res.json()
# gets only first 12 items (pythonic way of .slice() which is also an option)
hourly_records = data["hourly"][:12]
will_rain = False
for record in hourly_records:
    condition_code = record["weather"][0]["id"]
    if condition_code < ID_THRESHOLD_RAIN:
        will_rain = True
        break
if will_rain:
    print("Bring an umbrella")
    client = Client(TW_ACCT, TW_KEY)
    # if hosting on pythonAnywhere on free account, use this line
    # client = Client(TW_ACCT, TW_KEY, http_client=proxy_client)

    message = client.messages.create(
        body="It is going to rain, bring an ☔️",
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )

    print(message.sid, message.status)
else:
    print("It's not going to rain")
