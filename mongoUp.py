import pymongo
from pymongo import MongoClient
import json


cluster = pymongo.MongoClient("mongodb+srv://user:1234@productsdata.oimyn.mongodb.net/eCommerce?retryWrites=true&w=majority")
db = cluster["eCommere"]
collection = db["ProductsData"]

with open('C:/Users/Rohit/Desktop/task1.json') as f:
  data = json.load(f)
# post = {"_id": 1, "name": "rohit", "status": "online"}

collection.insert_many(data)