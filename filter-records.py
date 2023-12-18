import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["demo"]
mycollection = mydb["products"]

filter = {"name": "Iphone 11"}

result = mycollection.find_one(filter)  # name göre sorgulama
result = mycollection.find_one(
    {"_id": ObjectId("657f1a16b697374df9620456")})  # id'ye göre sorgulama

print(result)
