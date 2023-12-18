import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["demo"]
mycollection = mydb["products"]

filter = {"name": "Iphone 11"}

result = mycollection.find_one(filter)  # name göre sorgulama

print(result)
