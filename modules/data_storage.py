import os
import json

class DataStorage:
    def __init__(self):
        if not os.path.exists("database_configuration.json"):
            self.setup()
        else:
            self.load_configuration()

    def setup(self):
        print("Setting up the database configuration. Please provide the following details:")
        database_type = input("Database Type (SQLite/MySQL/MongoDB): ")
        if database_type == "SQLite":
            self.setup_sqlite()
        elif database_type == "MySQL":
            self.setup_mysql()
        elif database_type == "MongoDB":
            self.setup_mongodb()
        else:
            print("Invalid database type. Please try again.")
            self.setup()
        
    def setup_sqlite(self):
        self.configuration = {
            "type": "SQLite",
            "database_name": input("Database Name: ")
        }
        with open("database_configuration.json", "w") as file:
            json.dump(self.configuration, file)
        print("Configuration saved successfully.")

    def setup_mysql(self):
        self.configuration = {
            "type": "MySQL",
            "host": input("Host: "),
            "username": input("Username: "),
            "password": input("Password: "),
            "database_name": input("Database Name: ")
        }
        with open("database_configuration.json", "w") as file:
            json.dump(self.configuration, file)
        print("Configuration saved successfully.")

    def setup_mongodb(self):
        self.configuration = {
            "type": "MongoDB",
            "uri": input("Connection String: "),
            "database_name": input("Database Name: ")
        }
        with open("database_configuration.json", "w") as file:
            json.dump(self.configuration, file)
        print("Configuration saved successfully.")

    def load_configuration(self):
        with open("database_configuration.json", "r") as file:
            self.configuration = json.load(file)
        print("Configuration loaded successfully.")

    def save_data(self, data):
        if self.configuration["type"] == "SQLite":
            self.save_data_sqlite(data)
        elif self.configuration["type"] == "MySQL":
            self.save_data_mysql(data)
        elif self.configuration["type"] == "MongoDB":
            self.save_data_mongodb(data)

    def save_data_sqlite(self, data):
        print("Saving data to SQLite database.")

    def save_data_mysql(self, data):
        print("Saving data to MySQL database.")

    def save_data_mongodb(self, data):
        print("Saving data to MongoDB database.")

    def load_data(self):
        if self.configuration["type"] == "SQLite":
            return self.load_data_sqlite()
        elif self.configuration["type"] == "MySQL":
            return self.load_data_mysql()
        elif self.configuration["type"] == "MongoDB":
            return self.load_data_mongodb()
        
    def load_data_sqlite(self):
        print("Loading data from SQLite database.")
        return []
    
    def load_data_mysql(self):
        print("Loading data from MySQL database.")
        return []
    
    def load_data_mongodb(self):
        print("Loading data from MongoDB database.")
        return []
    