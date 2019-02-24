import pymongo
from pymongo import MongoClient
from pymongo import UpdateOne
import json
import urllib.parse


"""" This function connects to a MongoDB given a username,
password, and the @ part of Mongo URI. Returns a client object.
Prints a connection confirmation if successful."""
def authenticate(user, passwd, URI):
    username = urllib.parse.quote_plus(user)
    password = urllib.parse.quote_plus(passwd)
    client = MongoClient('mongodb://%s:%s%s' % (username, password, URI))
    print("Successfully connected to database, version %s." % (client.server_info()['version']))
    return client

""" insert a list of store data structures"""
def write_store_data(store_data, store_collection):
    if not isinstance(store_data, list):
        raise TypeError("Input need to be a list of dicts") 
    upserts = []
    for store in store_data:
        id = store['id']
        upserts.append(UpdateOne({'id' : id}, {'id' : id}, upsert=True))
    try:
        store_collection.bulk_write(upserts)
    except pymongo.errors.BulkWriteError as bwe:
        print(json.dumps(dict(bwe.details), indent=2))

"""  find store entry corrosponding to id """
def get_store_data(id, store_collection):
    return store_collection.find({'id' : id})

def write_price_data(price_data):
    return

