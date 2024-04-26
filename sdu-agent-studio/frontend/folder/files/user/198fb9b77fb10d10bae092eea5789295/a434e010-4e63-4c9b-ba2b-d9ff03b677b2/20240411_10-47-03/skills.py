

##### Begin of get_coordinates #####

# filename: get_coordinates.py
import requests  
from decouple import config  
  
# Function to fetch location coordinates  
def get_location_coordinates(location_name):  
    api_key = config('GOOGLE_MAPS_API_KEY')  # Access API key securely  
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"  # Google Maps Places API endpoint  
    params = {  
        'input': location_name,  
        'inputtype': 'textquery',  
        'fields': 'geometry',  
        'key': api_key  
    }  
    response = requests.get(base_url, params=params)  # Send the request  
    data = response.json()  # Parse JSON response  
  
    if response.status_code == 200 and data['candidates']:  # Check for successful response and non-empty result  
        location = data['candidates'][0]['geometry']['location']  
        return location['lat'], location['lng']  # Return the coordinates  
    else:  
        return None  # Handle errors or no results found  
  
# Example usage  
if __name__ == "__main__":  
    location_name = input("Enter a location name: ")  # Get user input for location  
    coordinates = get_location_coordinates(location_name)  # Fetch coordinates  
    if coordinates:  
        print(f"Coordinates for {location_name}: {coordinates}")  
    else:  
        print("Location not found or an error occurred.")  

#### End of get_coordinates ####

        