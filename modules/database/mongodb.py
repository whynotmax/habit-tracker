from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="habit_tracker"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def save_current_data(self, data):
        self.db.current_data.insert_one(data)
    
    def load_current_data(self):
        return self.db.current_data.find_one()
    
    def __del__(self):
        self.client.close()
