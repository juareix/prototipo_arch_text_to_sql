import sqlite3
import os

class DBConnection:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "olist.sqlite"))
        self.db_path = db_path
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute(self, query, params=None):
        if self.conn is None:
            self.connect()
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor
