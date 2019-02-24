
""" some simple example code for writing to data base, requires pymongo."""

import flipp
import database

# URI=mongodb://miser:miaomiaomiser69@ds349455.mlab.com:49455/miser

# connect to remote db
client = database.authenticate('miser','miaomiaomiser69')
# points to parse_flyer_json collection in database
db_collection = client.miser.parse_flyer_json


# gets current flyer data for urbana walmart
store_name = 'Walmart'
zip = '61801'
state = 'il'

flipp_url = 'https://backflipp.wishabi.com/flipp/items/search'
r = flipp.get_flyer_pricing_json(flipp_url,store_name, zip, state)
r = flipp.parse_flyer_json(r)

# inserts into collection in database
print("Writing data to database.")
db_collection.insert_many(r, ordered=False)
print("Sent.")
