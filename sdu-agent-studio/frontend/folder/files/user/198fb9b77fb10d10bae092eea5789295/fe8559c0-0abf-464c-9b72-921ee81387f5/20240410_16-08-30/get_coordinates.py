# filename: get_coordinates.py

from geopy.geocoders import Nominatim

def get_coordinates(location):
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        location = geolocator.geocode(location)
        if location:
            return (location.latitude, location.longitude)
        else:
            return "Location not found."
    except Exception as e:
        return "An error occurred: " + str(e)

# Replace 'Roquefort-les-Pins' with any other location if needed.
location_name = "Roquefort-les-Pins"
coordinates = get_coordinates(location_name)

print(f"The coordinates of {location_name} are: {coordinates}")