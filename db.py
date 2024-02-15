import json

import pymongo
import os

filename = 'db_config.json'

if not os.path.exists(filename):
    # Create the dictionary with the desired keys and values
    data = {
        'address': '10.20.9.3',
        'port': '27017',
        'QT_QPA_PLATFORM': True
    }
    
    # Write the dictionary to a JSON file
    with open(filename, 'w') as f:
        json.dump(data, f)

with open(filename, 'r') as f:
    db_config = json.load(f)
    address = db_config['address']+':'+db_config['port']


client = pymongo.MongoClient("mongodb://{}/".format(address))

cdUnitDB = client["cd_unit"]

def check_db_connection():
    try:
        client.admin.command("ping")
        return True
    except Exception as e:
        return False


def initializeDataBase():
    collegeCol = cdUnitDB["collegeList"]

    with open(r"data\route_list.json", "r") as read_file:
        route_list = json.load(read_file)
    collegeCol.insert_many(route_list)

    messengersCol = cdUnitDB["messengersDetails"]
    dataConfig = cdUnitDB["dataConfig"]

    with open(r"data\messengers.json", "r") as read_file:
        messengers = json.load(read_file)

    with open(r"data\config.json", "r") as read_file:
        configs = json.load(read_file)

    messengersCol.insert_many(messengers)
    dataConfig.insert_one(configs)



def getCollegeNameUsingID(colName, key, value):
    query = {key: value}
    projection = None
    return cdUnitDB[colName].find_one(query, projection)

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


if __name__ == "__main__":
    # change_stream = cdUnitDB['bundleDetails'].watch()
    # for change in change_stream:
    #     print(change)
        # callback(change)
    # pass
    # Process each change event

    # import datetime
    filter = {
        'messenger': 'Sivaprasd V'}
    #     'receivedDate': datetime.datetime(2023, 8, 9, 0, 0),
    # }

    # for doc in cdUnitDB['bundleDetails'].find(filter):
    #     print(doc,'\n')

    # from bson.objectid import ObjectId
    # from datetime import datetime

# Iterate over the recently added documents and print their details
# for document in recently_added_documents:
#     print(document)
    # import datetime
    # filter = {
    #     'messenger': 'Rajesh R S',
    #     'receivedDate': datetime.datetime(2023, 8, 9, 0, 0),
    # }

    # for doc in cdUnitDB['bundleDetails'].find(filter):
    #     print(doc,'\n')

    update = {'$set': {'messenger': 'Sivaprasad V'}}

    print(cdUnitDB["bundleDetails"].update_many(filter,update))

    # print(checkForBundles("bundleDetails", filter))

    # from datetime import datetime  
    # array = []
    # for cursor in cdUnitDB["bundleDetails"].find({'collegeName':"Mannam NSS College Edamulakkal, Anchal, Kollam"}):
    #     array.append(cursor)
    # print(len(array))
    # for doc in cdUnitDB["bundleDetails"].find(filter):
    #     print(doc)
        # cdUnitDB["bundleDetails"].find_one_and_update(doc,
        # { '$set': {"receivedDate" : datetime.strptime("Fri Dec 23 2022", '%a %b %d %Y')} })
    # cdUnitDB["bundleDetails"].find_one_and_update({'collegeName':"Milad-E-Sherief Memorial College Kayamkulam"},
    # { '$set': { "receivedDate" : datetime.strptime("Fri Oct 14 2022", '%a %b %d %Y')} })
    # for c in sortAndGetData("collegeList", "Route", "Local I"):
    #     print(c)
    # initializeDataBase()
    # for d in cdUnitDB["collegeList"].find():
    #     print(d.items())
