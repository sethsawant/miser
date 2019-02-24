import requests
import json

#NearbySearchAPI


lat = 40.0500281
lng = -75.5970521
L = list()

def NearbySearch(lat, lng):                      
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(lat) + ',' + str(lng) + '&radius=5000&type=shopping&keyword=groceries&key=AIzaSyAYt13KNaGXHpQGaXoKEQURCx5fEaZ3Xlo'
    r = requests.get(url = url)
    json_string = r.text
    
    parsed_json = json.loads(json_string)
    result = parsed_json['results']
    
    i = 0
    while i < len(result):
        json_vars = result[i]
        name = json_vars['name']
        vicinity = json_vars['vicinity'].replace("#", "")
        print (name)
        print (vicinity)
        print()
        i = i + 1
 
    
    

NearbySearch(lat, lng)
