import pymongo

myclient = pymongo.MongoClient("mongodb://172.17.0.2:27017/")

mydb = myclient["demo"]
mycollection = mydb["products"]


# result = mycollection.find_one()  # tekil kayıt sorgulama

for i in mycollection.find():
    print(i)


# print(result)
