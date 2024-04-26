# filename: get_dublin_coordinates.py
from skills import get_location_coordinates

# Fetch the coordinates of Dublin
coordinates = get_location_coordinates("Dublin")

# Check if coordinates were successfully retrieved and print them
if coordinates:
    print(f"Coordinates for Dublin: {coordinates}")
else:
    print("Location not found or an error occurred.")