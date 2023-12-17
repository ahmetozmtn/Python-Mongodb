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


productList = [
    {"name": "Iphone 15", "price": "60000", "description": "Color Black"},
    {"name": "Iphone 14", "price": "50000", "description": "Color Black",
        "categories": ["telefon", "elektronik"]},
    {"name": "Iphone 13", "price": "40000", "description": "Color Black"},
    {"name": "Iphone 12", "price": "30000", "description": "Color Black"},
    {"name": "Iphone 11", "price": "20000", "description": "Color Black"}
]

result = mycollection.insert_many(productList)
print(result.inserted_ids)
