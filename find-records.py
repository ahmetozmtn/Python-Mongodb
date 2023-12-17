import pymongo

myclient = pymongo.MongoClient("mongodb://172.17.0.2:27017/")

mydb = myclient["demo"]
mycollection = mydb["products"]


# result = mycollection.find_one()  # tekil kayıt sorgulama


# collection daki tüm kayıtları getirir, query parametresi 0 olanı getirmez, 1 olanı getirir.
for i in mycollection.find({}, {"_id": 0, "name": 1, "price": 1}):
    print(i)


# print(result)
