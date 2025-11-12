#!/usr/bin/env python3
"""
Contains a class based context manager to handle opening and closing database connections automatically.
"""
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, type, value, traceback):
        if self.conn:
            self.conn.close()


# Example usage:
if __name__ == "__main__":
    with DatabaseConnection('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(users)