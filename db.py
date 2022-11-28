import json

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

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
        return False, "Error: "+str(e)


if __name__ == "__main__":
    initializeDataBase()
    # for d in cdUnitDB["collegeList"].find():
    #     print(d.items())
