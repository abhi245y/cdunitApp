import json

import pymongo
import os
from random import randint
from datetime import datetime, timedelta
import random

from tqdm import tqdm
import time

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

def getAllBundles(query={}):
    return cdUnitDB["bundleDetails"].find(query, {"_id": 0}).limit(100)

def generateDummyData(total_iterations):
    dataConfig, messengersDetails = getConfig()
    messengers = [messenger['name'] for messenger in messengersDetails]
    routes = dataConfig['routes']
    qp_series_list = dataConfig['qp_series']
    
    progress_bar = tqdm(
        total=total_iterations,
        desc='Generating dummy data',
        bar_format="{l_bar}{bar} | {n_fmt}/{total_fmt} [Elapsed: {elapsed}, ETA: {remaining}]"
    )

    start_time = time.time()
    for i in range(total_iterations):
        messenger = messengers[randint(0, len(messengers)-1)]
        route = routes[randint(0, len(routes)-1)]

        pipeline = [
            {'$sample': {'size': 1}},
            {'$project': {'_id': 0, 'College Name': 1, 'Place': 1}}
        ]
        cursor = cdUnitDB['collegeList'].aggregate(pipeline, allowDiskUse=True)
        document = next(cursor) 

        college_name = f"{document['College Name']} {document['Place']}"
        same_date_entry_limit = randint(2, 10)
        random_date = datetime.today() - timedelta(days=random.randint(0, 90))

        data_to_insert = []
        for _ in range(same_date_entry_limit):
            qp_code = randint(1000, 9000)
            qp_series = qp_series_list[randint(0, len(qp_series_list)-1)]
            for _ in range(randint(1,5)): 
                data = {
                    "qpSeries": qp_series,
                    "qpCode": str(qp_code),
                    "isNil": False,
                    "receivedDate": datetime.strptime(random_date.strftime('%a %b %d %Y'), '%a %b %d %Y'),
                    "messenger": messenger,
                    "collegeName": college_name,
                "remarks": ""
                }
                data_to_insert.append(data)
        addDataToDB("bundleDetails", data_to_insert)

        progress_bar.update()

        elapsed_time = time.time() - start_time
        iterations_remaining = total_iterations - i - 1
        if iterations_remaining > 0:
            eta = elapsed_time / (i + 1) * iterations_remaining
        else:
            eta = 0
        progress_bar.set_postfix(elapsed=f"{elapsed_time:.2f}s", remaining=f"{eta:.2f}s")
    progress_bar.close()

# generateDummyData(100)