#place_idAPI
import requests
import json
place = 'ChIJ7_NwAjXPw4kRnSsd-af8Qpo'
API_key = 'meme' # Google Maps API Key

""" takes in a google maps place_id and returns the name, state and 
zip code of the store in a dictionary """

def id_to_name_state_zip(place_id):

    url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + place_id + API_key

    print(url)
    r = requests.get(url = url)
    json_string = r.text
    parsed_json = json.loads(json_string)

    result = parsed_json['result']
    json_body = result['adr_address']
    name = result['name']

    
    result = json_body.find('region')
    i = result + 8
    j = i + 2
    state = json_body[i:j]
    
    json_zip = json_body.find('postal-code')
    a = json_zip + 13
    b = a + 5
    zipcode = json_body[a:b]
    
    return {'name' : name, 'state' : state, 'zip' : zipcode}

""" takes two place_ids and calculates distances between them """
def distance_between(origin, destination):

    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' + origin + '&destinations=place_id:' + destination + API_key
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

def get_coords(origin):
    global lat
    global lng
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + origin + API_key
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
    return (lat, lng)


#Takes in GEOCODE coordinates and Grocery Store and returns the nearest ones
def find_nearby(lat, lng, radius):                      
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(lat) + ',' + str(lng) + '&radius=' + str(radius) + '&type=shopping&keyword=groceries' + API_key
    r = requests.get(url = url)
    json_string = r.text
    parsed_json = json.loads(json_string)
    result = parsed_json['results']
    
    output_list = []

    for i in range(len(result)):
        json_vars = result[i]
        name = json_vars['name']
        place_id = json_vars['place_id']
        vicinity = json_vars['vicinity'].replace("#", "")
        output_list.append({'name' : name, 'place_id' : place_id, 'vicinity' : vicinity})

    return output_list