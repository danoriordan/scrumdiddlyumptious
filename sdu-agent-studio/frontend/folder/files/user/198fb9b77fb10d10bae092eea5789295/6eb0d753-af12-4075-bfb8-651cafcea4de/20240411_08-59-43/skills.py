

##### Begin of get_coordinates #####

import os  
import requests  
from dotenv import load_dotenv  

# Step 1: Load environment variables  
load_dotenv()  

# Step 2: Retrieve the Google Maps API key from the .env file  
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")  

if GOOGLE_MAPS_API_KEY is None:  
    raise ValueError("Missing GOOGLE_MAPS_API_KEY in .env file")  

# Step 3: Define the function to get coordinates  
def get_location_coordinates():  
    # Request user input for the location  
    location_query = input("Enter the location: ")  

    # Prepare the request URL  
    api_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location_query}&key={GOOGLE_MAPS_API_KEY}"  

    # Make the API request  
    response = requests.get(api_url)  

    # Check if the request was successful  
    if response.status_code == 200:  
        location_data = response.json()  

        # Extract the coordinates if available  
        if location_data["status"] == "OK":  
            location = location_data["results"][0]["geometry"]["location"]  
            print(f"Coordinates for {location_query}: {location['lat']}, {location['lng']}")  
        else:  
            print(f"Failed to find coordinates for '{location_query}'. Reason: {location_data['status']}")  
    else:  
        print(f"Failed to connect to the Geocoding API. Status code: {response.status_code}")  

# Step 4: Call the function  
if __name__ == "__main__":  
    get_location_coordinates()  

#### End of get_coordinates ####

        