import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# get user location using IP address
response = requests.get('https://ipinfo.io/json')
data = response.json()
user_coords = (26.843347, 75.568515)
#user_coords = f"{data['loc']}"

#user_location = f"{data['city']}, {data['region']}, {data['country']}"

geolocator = Nominatim(user_agent="my_location_tracker")

# get user coordinates
#user_coords = geolocator.geocode(user_location)[1]

# get target location coordinates
park_location = geolocator.geocode("Manipal University, Jaipur")
park_coords = (park_location.latitude, park_location.longitude)

# calculate distance between user and target location
distance = geodesic(user_coords, park_coords).km

if distance < 1:
    print("You are currently within 1 kilometer of MUJ!")
    print(user_coords)
    print(park_coords)
else:
    print("Sorry, you are not within 1 kilometer of MUJ.")
    print(user_coords)
    print(park_coords)
