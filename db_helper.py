import json

import pymongo
import os

filename = 'db_config.json'

if not os.path.exists(filename):
    # Create the dictionary with the desired keys and values
    data = {
        'address': 'localhost',
        'port': '27017'
    }
    
    # Write the dictionary to a JSON file
    with open(filename, 'w') as f:
        json.dump(data, f)

with open(filename, 'r') as f:
    db_config = json.load(f)
    address = db_config['address']+':'+db_config['port']


client = pymongo.MongoClient("mongodb://{}/".format(address))

cdUnitDB = client["cd_unit"]


def getCollegeNameUsingID(key, value):
    query = {key: value}
    projection = None
    return cdUnitDB['collegeList'].find_one(query, projection)

def addDataToDB(colName, data):
    try:
        cdUnitDB[colName].insert_many(data)
        return True, "Done"
    except Exception as e:
        return False, "Error: " + str(e)

def sortAndGetData(colName, key, value):
    query = {key: value}
    return cdUnitDB[colName].find(query).sort("College Name", pymongo.ASCENDING)

def getConfig():
    return cdUnitDB["dataConfig"].find_one(), cdUnitDB["messengersDetails"].find()

def searchAndGetResult(collectionName, query):
    result = cdUnitDB[collectionName].find(query)
     
    if result is None:
        return "Not Found"
    else:
        return result

def checkForBundles(collectionName, query):
    result = cdUnitDB[collectionName].find_one(query)

    if result is None:
        return False
    else:
        return True

def dbWatcher(collectionName, callback):
    change_stream = cdUnitDB[collectionName].watch()
    for change in change_stream:
        callback(change)

def check_db_connection():
    try:
        client.admin.command("ping")
        return True
    except Exception as e:
        return False