import pymongo
import requests

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
client=pymongo.MongoClient("mongodb://localhost:27017")
print(client)
db=client["Government"] # Database Name
collec=db["Data"]  #Collection Name
collec.insert_one(data) # insertion in collection
