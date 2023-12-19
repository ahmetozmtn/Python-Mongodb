import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["demo"]
mycollection = mydb["products"]


for i in mycollection.find():
    print(i)


mycollection.update_one(
    {"name": "Iphone 17"},
    {"$set": {
        "name": "Samsung S23",
        "price": "50000"
    }}
)

for i in mycollection.find():
    print(i)
