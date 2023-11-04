################################################
# locate.py
# Andrew Woska
# agwoska@bu.edu
################################################
# Locates the hospital closest to me using 
# Google Maps API
################################################

import requests
import os

def get_closest_hospital(latitude, longitude):
    # Set up the Google Places API URL
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')

    # Define parameters
    params = {
        "location": f"{latitude},{longitude}",
        "radius": "5000",  # Search within a 5km radius
        "type": "hospital",
        "key": api_key,
    }

    # Make the request
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        if data["results"]:
            closest_hospital = data["results"][0]
            return closest_hospital["name"], closest_hospital["vicinity"]
        else:
            return "No hospitals found nearby."
    else:
        return f"Error: {data['error_message']}" if 'error_message' in data else "Unknown error"
# end get_closest_hospital

def get_current_location():
    url = "https://www.googleapis.com/geolocation/v1/geolocate"
    params = {
        "key": os.getenv('GOOGLE_MAPS_API_KEY')
    }

    response = requests.post(url, json={}, params=params)
    data = response.json()

    if response.status_code == 200:
        return data["location"]["lat"], data["location"]["lng"]
    else:
        return None, None

latitude, longitude = get_current_location()
print(latitude, longitude)

result = get_closest_hospital(latitude, longitude)
print(result)