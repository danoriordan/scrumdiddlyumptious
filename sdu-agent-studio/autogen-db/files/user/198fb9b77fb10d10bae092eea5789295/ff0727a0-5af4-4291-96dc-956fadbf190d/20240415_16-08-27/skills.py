

##### Begin of get_all_countries #####

import requests

def fetch_countries_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    data = response.json()
    return data

countries_data = fetch_countries_data()

#### End of get_all_countries ####

        