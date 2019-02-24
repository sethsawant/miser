import requests
import json


# Places API: returns name and address

place = input("Enter in a place ")
url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=' + place + '&inputtype=textquery&fields=formatted_address,name,opening_hours&key=AIzaSyAYt13KNaGXHpQGaXoKEQURCx5fEaZ3Xlo'

r = requests.get(url = url)
json_string = r.text


parsed_json = json.loads(json_string)
json_candidates = parsed_json['candidates']
print(json_candidates)

list_value = json_candidates[0]
name = list_value['name']
formatted_address = list_value['formatted_address']

print(name)
print(formatted_address)




