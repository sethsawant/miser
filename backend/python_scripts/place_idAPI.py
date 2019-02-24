#place_idAPI
import requests
import json
place = 'ChIJ7_NwAjXPw4kRnSsd-af8Qpo'

def place_id(place_id):

    
    url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + place_id + '&key=AIzaSyAYt13KNaGXHpQGaXoKEQURCx5fEaZ3Xlo'

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

place_id(place)
