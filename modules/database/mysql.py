import mysql.connector

class MySQLDB:
    def __init__(self, host="localhost", user="root", password="", database="habit_tracker"):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(dictionary=True)
    
    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS current_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                data TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def save_current_data(self, data):
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        sql = f"INSERT INTO current_data ({columns}) VALUES ({placeholders})"
        self.cursor.execute(sql, list(data.values()))
        self.connection.commit()
    
    def load_current_data(self):
        self.cursor.execute("SELECT * FROM current_data LIMIT 1")
        return self.cursor.fetchone()
    
    def __del__(self):
        self.cursor.close()
        self.connection.close()