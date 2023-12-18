import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["demo"]
mycollection = mydb["products"]

result = mycollection.find().sort("name")  # name göre sıralama yapar.

for i in result:
    print(i)
