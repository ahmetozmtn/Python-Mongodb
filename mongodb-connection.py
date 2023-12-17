import pymongo

myclient = pymongo.MongoClient("mongodb://172.17.0.2:27017/")

mydb = myclient["demo"]["users"]


print(myclient.list_database_names())  # localhost'daki tüm db'leri listeler
