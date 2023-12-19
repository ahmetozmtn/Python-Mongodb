import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["demo"]
mycollection = mydb["products"]


for i in mycollection.find():
    print(i)


# tekil kayıt güncelleme
mycollection.update_one(
    {"name": "Iphone 17"},
    {"$set": {
        "name": "Samsung S23",
        "price": "50000"
    }}
)

query = {"name": "Iphone 11"}
new_value = {"$set": {
    "name": "Samsung S22",
    "price": "40000"
}}


# çoklu kayıt güncelleme
result = mycollection.update_many(query, new_value)
print(f"{result.modified_count} adet kayıt güncellendi!")
