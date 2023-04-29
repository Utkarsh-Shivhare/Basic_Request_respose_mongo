import pymongo

def extract_data(url,database,collection):
    print("Connecting to database>>>>>>")
    client=pymongo.MongoClient(url)
    db=client[database] # Database Name
    collec=db[collection]
    print("Extracting Data>>>>>")
    data=collec.find_one()
    print(type(data))
    print(data)
