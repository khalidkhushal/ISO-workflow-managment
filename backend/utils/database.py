from pymongo import MongoClient
from flask import current_app

class Database:
    def __init__(self):
        self.client = None
        self.db = None

    def init_app(self, app):
        self.client = MongoClient(app.config['MONGO_URI'])
        self.db = self.client['iso_workflow']

    def get_collection(self, collection_name):
        return self.db[collection_name]

db = Database()