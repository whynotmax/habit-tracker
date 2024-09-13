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
        if database_type not in ["SQLite", "MySQL", "MongoDB"]:
            print("Invalid database type. Please try again.")
            return
        if database_type == "SQLite":
            self.configuration = {
                "type": "SQLite",
                "path": input("Database name: ")
            }
        elif database_type == "MySQL":
            self.configuration = {
                "type": "MySQL",
                "host": input("Host: "),
                "username": input("Username: "),
                "password": input("Password: "),
                "database": input("Database: ")
            }
        elif database_type == "MongoDB":
            self.configuration = {
                "type": "MongoDB",
                "uri": input("Connection string: "),
            }
        with open("database_configuration.json", "w") as file:
            json.dump(self.configuration, file)
        print("Configuration saved successfully.")



    def load_configuration(self):
        with open("database_configuration.json", "r") as file:
            self.configuration = json.load(file)
        print("Configuration loaded successfully.")

    def save_data(self, data):
        dbtype = self.configuration["type"]
        if dbtype == "SQLite":
            # TODO: Implement SQLite saving
            return None
        elif dbtype == "MySQL":
            # TODO: Implement MySQL saving
            return None
        elif dbtype == "MongoDB":
            # TODO: Implement MongoDB saving
            return None

    def load_data(self):
        dbtype = self.configuration["type"]
        if dbtype == "SQLite":
            # TODO: Implement SQLite loading
            return None
        elif dbtype == "MySQL":
            # TODO: Implement MySQL loading
            return None
        elif dbtype == "MongoDB":
            # TODO: Implement MongoDB loading
            return None