import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["demo"]
mycollection = mydb["products"]


result = mycollection.find_one({"name": "Iphone 11"})  # name göre sorgulama
result = mycollection.find_one(
    {"_id": ObjectId("657f1a16b697374df9620456")})  # id'ye göre sorgulama

result = mycollection.find({
    "name": {
        # dizi de belirtilenden biri varsa return eder
        "$in": ["Iphone 15", "Iphone 16"]
    }
})

result = mycollection.find({
    "price": {
        "$gt": "30000"  # fiyatı 30000 den büyük olan kayıtları getirir.
    }
})

result = mycollection.find({
    "price": {
        "$gte": "30000"  # fiyatı 30000'e eşit ve büyük olan kayıtları getirir.
    }
})

result = mycollection.find({
    "price": {
        "$eq": "30000"  # fiyatı 30000'e eşit olan kayıtları getirir.
    }
})

for i in result:
    print(i)
