# database.py

import pymongo
import certifi
class Database:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://TestCluster0:TestCluster0@testcluster0.vaeijqh.mongodb.net/?retryWrites=true&w=majority&appName=TestCluster0",tlsCAFile=certifi.where())
        self.db = self.client["todo"]
        self.collection1 = self.db["task"]

    def get_collection1(self):
        return self.collection1

  
