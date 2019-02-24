import requests
import json
#PlaceRadiusAPI 

lat = 37.4215647
lng = -122.0839988

destination = input('Enter in the store ')
destination = destination.replace(' ','%20')


def PlaceRadius(destination, lat, lng):                      
    url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=' + destination + '&inputtype=textquery&fields=formatted_address,name,opening_hours&locationbias=circle:2000@'+ str(lat) + ',' + str(lng) + '&key=AIzaSyAYt13KNaGXHpQGaXoKEQURCx5fEaZ3Xlo'
    r = requests.get(url = url)
    json_string = r.text
    
    parsed_json = json.loads(json_string)

    candidates = parsed_json['candidates']

    json_address = candidates[0]

    address = json_address['formatted_address']
    print(address)
    
    
    

PlaceRadius(destination, lat, lng)
