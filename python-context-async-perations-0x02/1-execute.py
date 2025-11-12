#!/usr/bin/env python3
"""
contains a reusable context manager that takes a query as input and executes it,
managing both connection and the query execution
"""
import sqlite3

class QueryExecutor(object):
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params if params is not None else ()
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor

    def __exit__(self, type, value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)
    with QueryExecutor('users.db', query, params) as cursor:
        results = cursor.fetchall()
        for row in results:
            print(row)