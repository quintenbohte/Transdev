#%%
######################### PACKAGES #######################################
#%%
from datetime import datetime, timedelta, date
#%%
import requests
import numpy as np

#%%
############################## REQUEST DATA FOR API #######################

app_id = "03ca1ed4"
app_key = "faf95b3d7c76b08f74e7f11823033b0f"
accept = "application/json"

end_point = "https://api.schiphol.nl/smart-energy/measurements"
headers = {"app_id": app_id, "app_key": app_key, "resourceversion": "v1", "accept":accept}
params = {"fromDateTime": "2022-09-19T08:00:00.432z", "toDateTime":"2022-09-19T08:30:00.432z"}

#%%
############################## FUNCTION TO GET API DATA ######################

def get_api_data(url, headers, data_list, params = {}):
    url = url
    headers = headers
    data_list = data_list
    params = params

    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code == 200:
        current_elements = response.json()
        data_list.extend(current_elements)

        return_links = [link_pagination.split("; ") for link_pagination in\
                response.headers["Link"].replace("<", "").replace(">", "")\
                .split(", ")]
        for return_link in return_links:
                # The the link relation.
            rel = return_link[1].replace("rel=", "").replace("\"", "")
            print(rel,return_link[0])
        
            if rel == "next":
                get_api_data(return_link[0], headers, data_list = data_list)

            if rel == "last":
                

    return data_list

data_list = []
data_list = get_api_data(end_point, headers, data_list, params)
# %%
def get_api_data(url, headers, data_list, params = {}):
    url = url
    headers = headers
    data_list = data_list
    params = params

    response = requests.get(url=url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code == 200:
        current_elements = response.json()
        data_list.extend(current_elements)

        return_links = [link_pagination.split("; ") for link_pagination in\
                response.headers["Link"].replace("<", "").replace(">", "")\
                .split(", ")]

        for return_link in return_links:
                # The the link relation.
            rel = return_link[1].replace("rel=", "").replace("\"", "")



        return data_list, return_links
#%%
app_id = "03ca1ed4"
app_key = "faf95b3d7c76b08f74e7f11823033b0f"
accept = "application/json"

end_point = "https://api.schiphol.nl/smart-energy/measurements"
headers = {"app_id": app_id, "app_key": app_key, "resourceversion": "v1", "accept":accept}
params = {"fromDateTime": "2022-09-19T08:00:00.432z", "toDateTime":"2022-09-19T08:30:00.432z"}
data_list = []
data_1, return_link1 = get_api_data(end_point, headers, data_list, params)
# %%
data_list2  = []
url = "https://api.schiphol.nl:443/smart-energy/measurements?fromDateTime=2022-09-19T08:00:00.432z&toDateTime=2022-09-19T08:30:00.432z&page=1"
data_2, return_link2 = get_api_data(url, headers, data_list = data_list2)

# %%
data_list3  = []
url = "https://api.schiphol.nl:443/smart-energy/measurements?fromDateTime=2022-09-19T08:00:00.432z&toDateTime=2022-09-19T08:30:00.432z&page=2"
data_3, return_link3 = get_api_data(url, headers, data_list = data_list3)
# %%

app_id = "03ca1ed4"
app_key = "faf95b3d7c76b08f74e7f11823033b0f"
accept = "application/json"

headers = {"app_id": app_id, "app_key": app_key, "resourceversion": "v1", "accept":accept}
params = {"fromDateTime": "2022-09-19T08:00:00.432z", "toDateTime":"2022-09-19T08:30:00.432z"}
data_list = []


url = "https://api.schiphol.nl/smart-energy/measurements"
headers = headers
params = {"fromDateTime": "2022-09-27T17:30:30.432z", "toDateTime":"2022-09-27T17:46:00.432z"}
data_list = data_list

response = requests.get(url=url, headers=headers, params = params)
if response.status_code == 200:
    current_elements = response.json()
    data_list.extend(current_elements)

    return_links = [link_pagination.split("; ") for link_pagination in\
            response.headers["Link"].replace("<", "").replace(">", "")\
            .split(", ")]

    return_link = return_links[-1][0][0:-1]
    last_page = int(return_links[-1][0][-1])
    order = return_links[-1][1]

    print(return_link)
    print(last_page)
    print(order)

    if last_page > 1:

        page_list = np.arange(1,last_page+1)    
        print(page_list)
        for page in page_list:
            next_url = return_link + str(page)
            print(next_url)
            get_api_data_next_page(next_url, headers, data_list, params = {})
    



        







# %%
def get_api_data_next_page(next_url, headers, data_list, params = {}):

    next_url = next_url
    headers = headers
    data_list = data_list
    params = params

    response = requests.get(url=next_url, headers=headers, params=params)

    if response.status_code == 200:
        current_elements = response.json()
        data_list.extend(current_elements)
    
# %%


