import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["demo"]
mycollection = mydb["products"]

result = mycollection.find().sort("name")  # name göre artan sıralama yapar.

# name göre azalan sıralama yapar.
result = mycollection.find().sort("name", -1)


result = mycollection.find().sort("price")  # artan fiyata göre sıralar
result = mycollection.find().sort("price", -1)  # azalan fiyata göre sıralar

for i in result:
    print(i)
