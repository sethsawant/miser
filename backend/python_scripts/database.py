from pymongo import MongoClient
import urllib.parse

# URI for miser 
URI='@ds349455.mlab.com:49455/miser'

"""" This function connects to a MongoDB given a username,
password, and the @ part of Mongo URI. Returns a client object.
Prints a connection confirmation if successful."""
def authenticate(user, passwd):
    username = urllib.parse.quote_plus(user)
    password = urllib.parse.quote_plus(passwd)
    try:
        client = MongoClient('mongodb://%s:%s%s' % (username, password, URI))
    except pymongo.errors.OperationFailure as auth_fail:
        print("Authentication to remote database failed.")
        return
    print("Successfully connected to database, version %s." % (client.server_info()['version']))
    return client