import pymongo

myclient = pymongo.MongoClient("mongodb://172.17.0.2:27017/")

mydb = myclient["demo"]
mycollection = mydb["products"]


# product = {
#     "name": "Iphone 15",
#     "price": "60000",
#     "description": "Color Black"
# }

# result = mycollection.insert_one(product)

# print(result)
# print(type(result))
# print(result.inserted_id) # collection id gösterir.


# db'deki collectionları  listeler
# print(mydb.list_collection_names())
