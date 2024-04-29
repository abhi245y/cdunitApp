import json

import pymongo
import os

filename = "db_config.json"

if not os.path.exists(filename):
    data = {"address": "localhost", "port": "27017", "QT_QPA_PLATFORM": True}

    with open(filename, "w") as f:
        json.dump(data, f)

with open(filename, "r") as f:
    db_config = json.load(f)
    address = db_config["address"] + ":" + db_config["port"]


client = pymongo.MongoClient(
    "mongodb://{}/".format(address),
    connectTimeoutMS=1000,
    serverSelectionTimeoutMS=1000,
)

cdUnitDB = client["cd_unit"]


def check_db_connection():
    try:
        client.admin.command("ping")
        return True
    except:  # noqa: E722
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
