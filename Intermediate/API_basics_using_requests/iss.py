import requests
import time
from datetime import datetime

MY_LAT = 51.507351
MY_LNG = -0.127758

# url kw is not required, just showing as example
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# for raising an exception if status_code is not in 200 family
response.raise_for_status()
data = response.json()

long = float(data["iss_position"]["longitude"])
lat = float(data["iss_position"]["latitude"])

iss_position = (long, lat)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

# using parameters in get request
res = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
res.raise_for_status()
data = res.json()
# print("-----USING PARAMS------\n", data, "\n")

# using parameters in URL and disabled fortmatting (gets unix time)
# res = requests.get(
# f"http://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}&formatted=0")
# res.raise_for_status()

# print("-----USING URL-----\n", res.json(), "\n")

# Get sunset/sunrise times

data = res.json()
# Get only the hour for each
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

while True:
    if MY_LNG - 5 <= iss_position[0] <= MY_LNG + 5 and MY_LAT - 5 <= iss_position[1] <= MY_LAT + 5:
        print("ISS is over head")


    if datetime.now().hour >= sunset or datetime.now().hour <= sunrise:
        print("Go look outside!")
    else:
        print("ISS is not there")
    time.sleep(60)