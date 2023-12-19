import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["demo"]
mycollection = mydb["products"]


for i in mycollection.find():
    print(i)

print("*"*75)

# mycollection.delete_one({"name": "Samsung S23"})
# mycollection.delete_many({"name": {"$regex": "^S"}})
result = mycollection.delete_many({})  # tüm kayıtları siler

print(f"{result.deleted_count} adet kayıt silindi")

for i in mycollection.find():
    print(i)
