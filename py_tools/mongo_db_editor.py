from pymongo import MongoClient
try:
    from .env_translator import env_to_var
except:
    from env_translator import env_to_var
import random

class MongoDBEditor:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient(f'mongodb+srv://FRIDGY-USER:{env_to_var("MONGO_DB_PASS")}@fridgy.bbwly.mongodb.net/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert(self, data):
        return self.collection.insert_one(data).inserted_id

    def find(self, query):
        return self.collection.find(query)

    def update(self, query, data):
        self.collection.update_one(query, {'$set': data})

    def delete(self, query):
        self.collection.delete_one(query)

    def delete_many(self, query):
        self.collection.delete_many(query)
    
    def close(self):
        self.client.close()
    
    def random(self):
        entries = list(self.collection.find())

        if entries:
            random_entry = random.choice(entries)
            random_entry_id = random_entry['_id']
            
            result = self.collection.delete_one({'_id': random_entry_id})
            print(f'Deleted entry with ID: {random_entry_id}. Deleted count: {result.deleted_count}.')
        else:
            print("No entries to delete.")
    
def main() -> None:
    mongo = MongoDBEditor("fridgy", "json-data")
    mongo.random()

if __name__ == '__main__':
    main()