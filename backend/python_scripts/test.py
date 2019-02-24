
""" some simple example code for writing to data base, requires pymongo."""

import flipp
import database
import location_services

user = ''
passwd = ''
URI = ''

# connect to remote db
client = database.authenticate(user, passwd, URI)
# points to parse_flyer_json collection in database
db_collection = client.miser.price_data

lat = 40.111
lng = -88.22
store_list = location_services.find_nearby(lat, lng, 5000)


# for store in store_list:
#     print(store)

# gets current flyer data for urbana walmart
store_name = 'Walmart'
zip = '61801'
state = 'il'

flipp_url = 'https://backflipp.wishabi.com/flipp/items/search'
r = flipp.get_flyer_pricing_json(flipp_url,store_name, zip, state)
r = flipp.parse_flyer_json(r)

# inserts into collection in database
print("Writing price data to database...")
db_collection.insert_many(r, ordered=False)
print("Sent.")

test_store = [{'name' : 'Test Store','id' : 'wowth1s1sak00lid'}]
id = (test_store[0])['id']
print('writing store, id: %s' % (id))

database.write_store_data(test_store, client.miser.stores)
return_store = database.get_store_data(id, client.miser.stores)
for s in return_store:
    print(s)
