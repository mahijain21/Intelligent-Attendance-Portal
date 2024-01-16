# import gpsd
#
# # connect to the local GPS daemon
# #gpsd.connect()
# gpsd.connect(host="127.0.0.1", port=1803)
#
# # get the current GPS position
# packet = gpsd.get_current()
#
# # check if we have a valid GPS fix
# if packet.mode < 2:
#     print("No GPS fix available.")
# else:
#     # get the latitude and longitude
#     latitude = packet.position()[0]
#     longitude = packet.position()[1]
#     print("Latitude: ", latitude)
#     print("Longitude: ", longitude)


# import gpsd_client
#
# # create a GPSD client object
# client = gpsd_client.GpsdClient()
#
# # connect to the GPSD daemon
# client.connect()
#
# # get the current GPS position
# packet = client.get_current()
#
# # check if we have a valid GPS fix
# if packet.mode < 2:
#     print("No GPS fix available.")
# else:
#     # get the latitude and longitude
#     latitude = packet.lat
#     longitude = packet.lon
#     print("Latitude: ", latitude)
#     print("Longitude: ", longitude)
#
# # disconnect from the GPSD daemon
# client.close()


#
# import webbrowser
#
# # open a web page that requests the user's location
# webbrowser.open('https://www.google.com/maps')
#
# # the user will be prompted to share their location
# # once the location is retrieved, it will be displayed on the map in the web page
#
# # after the location is retrieved, you can use the browser's console to access the latitude and longitude
# # open the browser's console by pressing Ctrl+Shift+J (Windows/Linux) or Cmd+Opt+J (Mac)
# # in the console, type the following command to retrieve the latitude and longitude:
# # > console.log(`Latitude: ${window.navigator.geolocation.getCurrentPosition(position => position.coords.latitude)}\nLongitude: ${window.navigator.geolocation.getCurrentPosition(position => position.coords.longitude)}`)
#
# # the latitude and longitude will be displayed in the console


import requests

# replace YOUR_API_KEY with your actual Google Maps API key
api_key = 'YOUR_API_KEY'
# make a request to the Google Maps Geocoding API with the current IP address
response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params={'latlng': '0,0', 'key': api_key})

# check if the request was successful
if response.status_code == 200:
    # parse the response JSON to extract the latitude and longitude
    result = response.json()
    if result['results']:
        location = result['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
    else:
        print('No results found.')
else:
    print('Failed to retrieve location')
