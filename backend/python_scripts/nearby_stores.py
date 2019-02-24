import requests
import json
#DistanceAPI

origin = input("Enter the start ")
origin = origin.replace(' ', '+')
radius = input("Enter the radius of search in meters ")
try:
   val = int(radius)
except ValueError:
   print("That's not an number!")
lat = 0
lng = 0


#calculates distance
def Distance(origin, destination):

    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' + origin + '&destinations=place_id:' + destination + '&key=AIzaSyAYt13KNaGXHpQGaXoKEQURCx5fEaZ3Xlo'
    r = requests.get(url = url)
    json_string = r.text
    parsed_json = json.loads(json_string)
    json_rows = parsed_json['rows']
    json_elements = json_rows[0] 
    elements = json_elements['elements']
    json_distance = elements[0]
    status = json_distance['status']
    if (status == "ZERO_RESULTS" or status == "NOT_FOUND"):
        print('not a valid address')
    else:
        distance = json_distance['distance']
        json_text = distance['text']
        print(json_text)
        json_duration = json_distance['duration']
        time = json_duration['text']
        print(time)

#Find coordinates for ORIGIN location to stores

def Geocode(origin):
    global lat
    global lng
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + origin + '&key=AIzaSyAYt13KNaGXHpQGaXoKEQURCx5fEaZ3Xlo'
    r = requests.get(url = url)
    json_string = r.text
    parsed_json = json.loads(json_string)
    result = parsed_json['results']
    if not result:
        print("Invalid Search ")
    else:
        json_geometry = result[0]
        geometry = json_geometry['geometry']
        location = geometry['location']
        lat = location['lat']
        lng = location['lng']


#Takes in GEOCODE coordinates and Grocery Store and returns the nearest ones
def NearbySearch(lat, lng, radius):                      
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(lat) + ',' + str(lng) + '&radius=' + radius + '&type=shopping&keyword=groceries&key=AIzaSyAYt13KNaGXHpQGaXoKEQURCx5fEaZ3Xlo'
    r = requests.get(url = url)
    json_string = r.text
    
    parsed_json = json.loads(json_string)
    result = parsed_json['results']
    
    i = 0
    while i < len(result):
        json_vars = result[i]
        name = json_vars['name']
        place_id = json_vars['place_id']
        vicinity = json_vars['vicinity'].replace("#", "")
        print ('Name: ' + name)
        print ('Address: ' + vicinity)
        Distance(origin, place_id)
        print('place_id: '+ place_id)
        print()
        i = i + 1

#Takes in GEOCODE coordinates and Grocery Store and returns the furthest store in the radius
#dont need anymore :(((((( 
def PlaceRadius(newdes, lat, lng):
    global destination
    url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=' + destination + '&inputtype=textquery&fields=formatted_address,name,opening_hours&locationbias=circle:20000@'+ str(lat) + ',' + str(lng) + '&key=AIzaSyAYt13KNaGXHpQGaXoKEQURCx5fEaZ3Xlo'
    r = requests.get(url = url)
    json_string = r.text
    
    parsed_json = json.loads(json_string)

    candidates = parsed_json['candidates']

    json_address = candidates[0]

    address = json_address['formatted_address']
    destination = address
    print(address)
    

Geocode(origin)
NearbySearch(lat, lng, radius)





