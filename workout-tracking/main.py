import requests
from datetime import datetime
import os

# APP_ID and API_KEY are stored in environment variables. See Pycharm Run Configuration
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}
json = {
    "query": input("What exercises do you want to log? "),
    "gender": "male",
    "weight_kg": 90.0,
    "height_cm": 180.0,
    "age": 27,
}
response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=json)

for exercise in response.json()["exercises"]:
    json = {
        "exercise": {
            "date": datetime.now().date().strftime("%d/%m/%Y"),
            "time": datetime.now().time().strftime("%H:%M:%S"),
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post("https://api.sheety.co/78ea250cebb814128750091852f45ff4/myWorkouts/exercises",
                             headers={"Authorization": SHEETY_AUTH}, json=json)
    print(response.text)
