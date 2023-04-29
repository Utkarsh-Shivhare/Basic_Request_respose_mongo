import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["Government"] # Database Name
collec=db["Data"]
data=collec.find_one()
print(type(data))
print(data)
