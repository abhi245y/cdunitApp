import json

import pymongo

client = pymongo.MongoClient("mongodb://192.168.29.190:27017/")

cdUnitDB = client["cd_unit"]


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


def addDataToDB(colName, data):
    try:
        cdUnitDB[colName].insert_many(data)
        return True, "Done"
    except Exception as e:
        return False, "Error: " + str(e)


def sortAndGetData(colName, key, value):
    query = {key: value}
    return cdUnitDB[colName].find(query)


def getConfig():
    return cdUnitDB["dataConfig"].find_one(), cdUnitDB["messengersDetails"].find()


if __name__ == "__main__":
    pass
    # from datetime import datetime  

    # for doc in cdUnitDB["bundleDetails"].find():
    #     cdUnitDB["bundleDetails"].find_one_and_update(doc,
    # { '$set': { "isNil" : False} })
    # cdUnitDB["bundleDetails"].find_one_and_update({'collegeName':"UIT Yeroor, Govt. Higher Secondary School Campus,  Yeroor, Near Anchal, Kollam"},
    # { '$set': { "receivedDate" : datetime.strptime("Fri Oct 14 2022", '%a %b %d %Y')} })
    # for c in sortAndGetData("collegeList", "Route", "Local I"):
    #     print(c)
    # initializeDataBase()
    # for d in cdUnitDB["collegeList"].find():
    #     print(d.items())
