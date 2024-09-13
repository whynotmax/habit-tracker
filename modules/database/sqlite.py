import sqlite3

class SQLiteDB:
    def __init__(self, db_path="habit_tracker.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS current_data (
                id INTEGER PRIMARY KEY,
                data TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def save_current_data(self, data):
        self.cursor.execute('''
            INSERT INTO current_data (data) VALUES (?)
        ''', (data,))
        self.conn.commit()

    def load_current_data(self):
        self.cursor.execute('SELECT data FROM current_data ORDER BY id DESC LIMIT 1')
        return self.cursor.fetchone()

    def __del__(self):
        self.conn.close()