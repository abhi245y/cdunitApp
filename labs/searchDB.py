import json
import datetime
import db
from tabulate import tabulate
import textwrap

if __name__ == '__main__':
    query = {
        'qpSeries': 'R',
        'isNil': False, 
        'receivedDate': datetime.datetime(2023, 4, 17, 0, 0), 
        'messenger': 'Rajesh R.S', 
        'collegeName': "KNM Govt. Arts & Science College Kanjiramkulam, Thiruvananthapuram"
    }

    query2 = {
        # 'messenger': 'Arun Bose R',
        # 'qpSeries': 'P',
        # 'qpCode': "1067",
        # 'collegeName':'KVVS College of Science & Technology Enathu, Adoor, Pathanamthitta',
        'receivedDate': datetime.datetime(2023, 4, 20, 0, 0),
    }

    query3 = {
        'messenger': 'Arun Bose R',
        'receivedDate': datetime.datetime(2023, 4, 28, 0, 0)
        # 'receivedDate': datetime.datetime(2023, 4, 25, 0, 0), 
    }


    query4 = {'qpSeries': 'R', 'qpCode': {'$gte': 1600, '$lte': 1691}}
    sort_order = [('qpCode', 1)]

    query5 = {
        'messenger': 'Rajesh R.S',
        'receivedDate': datetime.datetime(2023, 7, 27, 0, 0),
        'collegeName':'UIT Regional Centre Kanjiramkulam (Kovalam), Panchayath High School, Kanjiramkulam, Kazhivoor'
    }


    # execute the search query and print the results
    results = db.cdUnitDB["bundleDetails"].find(query5).sort(sort_order)

    # new_remarks_value = ""  # Replace this with the new value you want to set for the 'remarks' field

    # for result in results:
    # # Update the 'remarks' field for each result
    #     db.cdUnitDB["bundleDetails"].update_one({'_id': result['_id']}, {'$set': {'remarks': new_remarks_value}})


    # data = db.searchAndGetResult("bundleDetails", query4)
    data = results
    # Define the headers for the table
    headers = ['College Name', 'Is Nil', 'Messenger', 'QP Code', 'QP Series', 'Received Date']
    # Create a list of lists containing the data for each row of the table
    rows = [[textwrap.fill(d['collegeName']), d['isNil'], d['messenger'], d['qpCode'], d['qpSeries'], d['receivedDate']] for d in data]

    # Use the tabulate library to create the table with lines between the rows
    table = tabulate(rows, headers=headers, tablefmt='presto')

    print(table)

    # for res in db.searchAndGetResult("bundleDetails", query2):
    #     print(beautify_dict(res))
