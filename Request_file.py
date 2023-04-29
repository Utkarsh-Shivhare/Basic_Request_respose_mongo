import pymongo
import requests
from mongo_extraction import extract_data

headers = {
    'accept': 'application/xml',
}

params = {
    'api-key': '579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b',
    'format': 'json',
}

response = requests.get('https://api.data.gov.in/resource/c5386e38-ae3c-4a17-abdb-6c4df94288cb', params=params, headers=headers)
data=response.json()
print(type(data))
url="mongodb+srv://utkarshshivhare26:Utkarsh%402005@cluster0.gjyria7.mongodb.net/test"
database="Government"
collection="Data"

def push_to_mongodb(url,database,collection,data):
    print("Connecting to database>>>>>>")
    client=pymongo.MongoClient(url)
    db=client[database] # Database Name
    collec=db[collection]  #Collection Name
    print("Pushing the data>>>>")
    collec.insert_one(data) # insertion in collection



# push_to_mongodb(url,database,collection,data)
# extract_data(url,database,collection)
