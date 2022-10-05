############################### PACKAGES ##########################
#%%
from datetime import datetime, timedelta, date
import requests

#%%  
##################################### interval between two dates #############################################
from datetime import datetime, timedelta, date
import requests

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


#%%
############################################# GET API DATA #############################



def get_api_data(app_id, app_key, params, accept, end_point, elements):

    APP_ID = app_id
    APP_KEY = app_key
    PARAMRS = params
    ACCEPT = accept
    INITUAL_URL = end_point

    HEADERS = {"app_id": APP_ID, "app_key": APP_KEY, "resourceversion": "v1", "accept":ACCEPT }
    response = requests.get(INITUAL_URL, headers=HEADERS, params=PARAMRS )

    if response.status_code == 200:
        current_elements = response.json()
        elements.extend(current_elements)

 #       return_links = [link_pagination.split("; ") for link_pagination in\
  #                  response.headers["Link"].replace("<", "").replace(">", "")\
  #                  .split(", ")]

   #     for return_link in return_links:
    #            # The the link relation.
     #           rel = return_link[1].replace("rel=", "").replace("\"", "")
      #          print(rel)
       #         pagination_list.append(rel)

    return response

#%%

response = get_api_data(app_id = "03ca1ed4", 
                app_key = "faf95b3d7c76b08f74e7f11823033b0f", 
                params = {"fromDateTime": "2022-09-19T08:00:00.432z", "toDateTime":"2022-09-19T08:30:00.432z"}, 
                accept = "application/json", 
                end_point = "https://api.schiphol.nl/smart-energy/measurements",
                elements = [])


#%%
elements = []
if response.status_code == 200:
    current_elements = response.json()
    elements.extend(current_elements)


#%%
return_links = [link_pagination.split("; ") for link_pagination in\
                response.headers["Link"].replace("<", "").replace(">", "")\
                .split(", ")]


#%%


#%%
for return_link in return_links:
                # The the link relation.
                rel = return_link[1].replace("rel=", "").replace("\"", "")
                print(rel,return_link[0])
#%%


#%%
return_link = "https://api.schiphol.nl:443/smart-energy/measurements?fromDateTime=2022-09-19T08:00:00.432z&toDateTime=2022-09-19T08:30:00.432z&page=1"
APP_ID = "03ca1ed4"
APP_KEY = "faf95b3d7c76b08f74e7f11823033b0f" 
ACCEPT = "application/json"
HEADERS = {"app_id": APP_ID, "app_key": APP_KEY, "resourceversion": "v1", "accept":ACCEPT }
response_next = requests.get(return_link, headers = HEADERS, params = {})

elements_new = []
if response_next.status_code == 200:
        current_elements = response.json()
        elements_new.extend(current_elements)

#%%
start_date = datetime(2022, 9, 1)
end_date = datetime(2022, 10, 1)
interval_minutes = 30

date_list_api = thirty_min_interval(start_date, end_date, interval_minutes)

repsonse_list = []
loop = 0
pagination_list = []
elements = []

for days in range(len(date_list_api)-1):

    loop =+ loop + 1
    print(len(date_list_api)- loop, 'to go')

    start_date = date_list_api[days]
    end_date = date_list_api[days+1]

    response = get_api_data(app_id = "03ca1ed4", 
                app_key = "faf95b3d7c76b08f74e7f11823033b0f", 
                params = {"fromDateTime": start_date, "toDateTime":end_date}, 
                accept = "application/json", 
                end_point = "https://api.schiphol.nl/smart-energy/measurements",
                elements = elements, 
                pagination_list = pagination_list)
# %%

def get_api_data(url, headers, elements, params = {}):

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        current_elements = response.json()
        elements.extend(current_elements)
        print('succes')
        return_links = [link_pagination.split("; ") for link_pagination in\
                response.headers["Link"].replace("<", "").replace(">", "")\
                .split(", ")]

        for return_link in return_links:
                # The the link relation.
                rel = return_link[1].replace("rel=", "").replace("\"", "")
                print(rel,return_link[0])

                if rel == 'next':
                    get_api_data(return_link[0], headers, elements)
        


#%%

app_id = "03ca1ed4" 
app_key = "faf95b3d7c76b08f74e7f11823033b0f" 
params = {"fromDateTime": "2022-09-19T08:00:00.432z", "toDateTime":"2022-09-19T08:30:00.432z"},
accept = "application/json"
end_point = "https://api.schiphol.nl/smart-energy/measurements"

APP_ID = app_id
APP_KEY = app_key
PARAMS = params
ACCEPT = accept
INITUAL_URL = end_point

HEADERS = {"app_id": APP_ID, "app_key": APP_KEY, "resourceversion": "v1", "accept":ACCEPT }
elements = []

data_api = get_api_data(INITUAL_URL, HEADERS, elements, PARAMS)










#%%
def get_api_data(url, headers, elements, params = {}):

    response = requests.get(url, headers=headers, params=params)
    print('succes')
    if response.status_code == 200:
        current_elements = response.json()
        elements.extend(current_elements)

        return_links = [link_pagination.split("; ") for link_pagination in\
                response.headers["Link"].replace("<", "").replace(">", "")\
                .split(", ")]

        for return_link in return_links:
                # The the link relation.
                rel = return_link[1].replace("rel=", "").replace("\"", "")
                print(rel,return_link[0])

                if rel == 'next':
                    get_api_data(return_link[0], headers, elements)
        

#%%
