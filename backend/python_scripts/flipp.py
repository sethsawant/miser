"""" this file contains files for fetching digital flyer data from Flipp."""

import requests
import json

# some useful URLs
# https://backflipp.wishabi.com/flipp/items/search
# https://backflipp.wishabi.com/flipp/items/search?locale=en-il&postal_code=61801&q=Walmart

"""
Function to fetch current weekly ad flyer prices for a store. 
Looks up based on store name, state, and zip code. Returns a 
complete JSON of Flipp's pricing data
"""
def get_flyer_pricing_json(url, store_name, zip_code, state):
    # set parameteres based on args
    PARAMS = {'locale':'en-' + state,
              'postal_code':str(zip_code),
              'q':str(store_name) } 
  
    # sending get request and saving the response as response object 
    r = requests.get(url = url, params = PARAMS) 
  
    # extracting data in json format 
    return r.json()


"""
Function to parse a Flipp flyer json. Returns a list of dictionaries
of product name, current price, and price qualifier, and
time period price is valid.
"""
def parse_flyer_json(json_file):
    #creates a list of dictionaries which contain individual price info
    extracted_data = []
    for item in json_file["items"]:
        extracted_data.append({'name' : item["name"],
        'price' : item["current_price"],
        'qualifier' : item["post_price_text"],
        'valid_from' : item["valid_from"],
        'valid_to' : item["valid_to"]})
    return extracted_data



    
