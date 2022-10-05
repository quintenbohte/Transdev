


import requests, sys

APP_ID = "03ca1ed4"
APP_KEY = "faf95b3d7c76b08f74e7f11823033b0f"
PARAMRS = {"fromDateTime": "2022-09-27T17:30:30.432z", "toDateTime":"2022-09-27T17:46:00.432z"}
ACCEPT = "application/json"
INITUAL_URL = "https://api.schiphol.nl/smart-energy/measurements"

INITIAL_HEADERS = {"app_id": APP_ID, "app_key": APP_KEY, "resourceversion": "v1", "accept":ACCEPT }


response = requests.get(INITUAL_URL, headers=INITIAL_HEADERS, params=PARAMRS, )
print(response.status_code)

#current_elements = response.json()


import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text
#    print(text)

my_json = jprint(response.json())

print(my_json)

#print(response.headers["Link"])


with open('personal.json', 'w') as json_file:
    json.dump(my_json, json_file)





