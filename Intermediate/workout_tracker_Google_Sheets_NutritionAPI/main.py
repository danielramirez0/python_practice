from datetime import datetime
import requests
from env.config import GENDER, HEADERS, AGE, HEIGHT, SHEETS_AUTH_HEADER, WEIGHT, EXERCISE_ENDPOINT, SHEETS_ENDPOINT



workout = input("What did you do at the gym? ")
dt = datetime.now()
date_str = dt.strftime("%m/%d/%Y")
# time_str = dt.strftime("%H:%M:%S")
time_str = dt.strftime("%X")

body = {
    "query": workout,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

r = requests.post(url=EXERCISE_ENDPOINT, headers=HEADERS, json=body)
r.raise_for_status()
exercises = r.json()["exercises"]

for exercise in exercises:
    body = { 
        "workout":{
            "date": date_str,
            "time": time_str,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    r = requests.post(url=SHEETS_ENDPOINT, json=body, headers=SHEETS_AUTH_HEADER)
    r.raise_for_status()
    print(r.text)


