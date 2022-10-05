

#%%
import requests, sys

APP_ID = "03ca1ed4"
APP_KEY = "faf95b3d7c76b08f74e7f11823033b0f"
PARAMRS = {"fromDateTime": "2022-09-27T17:30:30.432z", "toDateTime":"2022-09-27T17:46:00.432z"}
ACCEPT = "application/json"
INITUAL_URL = "https://api.schiphol.nl/smart-energy/measurements"

INITIAL_HEADERS = {"app_id": APP_ID, "app_key": APP_KEY, "resourceversion": "v1", "accept":ACCEPT }
#%%

response = requests.get(INITUAL_URL, headers=INITIAL_HEADERS, params=PARAMRS, )
print(response.status_code)

#current_elements = response.json()

#%%
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text
    print(text)

my_json = jprint(response.json())

print(my_json)

#print(response.headers["Link"])
#%% 

with open(r'C:\Users\QuintenBohte\OneDrive - Valcon Business Development A S\Documents\Transdev\CO2_Energy_Monitor\Schiphol_aapie\personal.json', 'w') as json_file:
    json.dump(my_json, json_file)

print('succes')


#%%
import requests
def get_api_data(app_id, app_key, params, accept, end_point):

    APP_ID = app_id
    APP_KEY = app_key
    PARAMRS = params
    ACCEPT = accept
    INITUAL_URL = end_point

    HEADERS = {"app_id": APP_ID, "app_key": APP_KEY, "resourceversion": "v1", "accept":ACCEPT }
    response = requests.get(INITUAL_URL, headers=HEADERS, params=PARAMRS )
    response = response.json()

    return response

response = get_api_data(app_id = "03ca1ed4", 
                app_key = "faf95b3d7c76b08f74e7f11823033b0f", 
                params = {"fromDateTime": "2022-09-27T17:30:30.432z", "toDateTime":"2022-09-27T17:46:00.432z"}, 
                accept = "application/json", 
                end_point = "https://api.schiphol.nl/smart-energy/measurements")


print(response)
#%%
def response_to_json(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    return text

#%%
current_elements = response.json()

df = pd.DataFrame(current_elements)

#print(current_elements[1:5])
#%%

json_object = json.dumps(current_elements, indent = 4) 
print(json_object)

#%% Function for list interval between two dates 

from datetime import datetime, timedelta, date
def thirty_min_interval(start_date, end_date, interval_minutes):

    diff = end_date - start_date
    number_half_hours = int(diff.days * (48))
    half_hour = timedelta(minutes = interval_minutes)  
    dates_list = []

    for half_hours in range(number_half_hours):
        start_date = start_date + half_hour
        start_date_string = str(start_date)
        start_date_string = start_date_string[:10] + 'T' + start_date_string[11:] + '.432z'
        dates_list.append(start_date_string)

    return dates_list

start_date = datetime(2008, 8, 1, 0)
end_date = datetime(2008, 8, 10)
interval_minutes = 45

dates_test = thirty_min_interval(start_date, end_date, interval_minutes)
print(dates_test)


#%% Function To Call API

import requests
def get_api_data(app_id, app_key, params, accept, end_point):

    APP_ID = app_id
    APP_KEY = app_key
    PARAMRS = params
    ACCEPT = accept
    INITUAL_URL = end_point

    HEADERS = {"app_id": APP_ID, "app_key": APP_KEY, "resourceversion": "v1", "accept":ACCEPT }
    response = requests.get(INITUAL_URL, headers=HEADERS, params=PARAMRS )

    try:
        response = response.json()[]
        print('there is data')
    except:
        response = []
        print('no data ')

    return response
#%%
response = get_api_data(app_id = "03ca1ed4", 
                app_key = "faf95b3d7c76b08f74e7f11823033b0f", 
                params = {"fromDateTime": "2022-09-27T17:30:30.432z", "toDateTime":"2022-09-27T17:46:00.432z"}, 
                accept = "application/json", 
                end_point = "https://api.schiphol.nl/smart-energy/measurements")


print(response)
#%%
start_date = datetime(2022, 9, 1)
end_date = datetime(2022, 9, 5)

interval_minutes = 30

date_list_api = thirty_min_interval(start_date, end_date, interval_minutes)
start_date1 = date_list_api[1]
end_date1 = date_list_api[2]
print(start_date1, end_date1)
#%%
response = get_api_data(app_id = "03ca1ed4", 
                app_key = "faf95b3d7c76b08f74e7f11823033b0f", 
                params = {"fromDateTime": start_date1, "toDateTime":end_date1}, 
                accept = "application/json", 
                end_point = "https://api.schiphol.nl/smart-energy/measurements")
print(response)
#%%

start_date = datetime(2022, 9, 1)
end_date = datetime(2022, 9, 30)
interval_minutes = 30

date_list_api = thirty_min_interval(start_date, end_date, interval_minutes)

repsonse_list = []
loop = 0
for days in range(len(date_list_api)-1):

    loop =+ loop + 1
    print(len(date_list_api)- loop, 'to go')

    start_date = date_list_api[days]
    end_date = date_list_api[days+1]
    response = get_api_data(app_id = "03ca1ed4", 
                app_key = "faf95b3d7c76b08f74e7f11823033b0f", 
                params = {"fromDateTime": start_date, "toDateTime":end_date}, 
                accept = "application/json", 
                end_point = "https://api.schiphol.nl/smart-energy/measurements")
    if len(response) > 0:
        print('filling list')
        repsonse_list.append(response)
    

    


# %%
for i in repsonse_list:
    print(len(i))
# %%
