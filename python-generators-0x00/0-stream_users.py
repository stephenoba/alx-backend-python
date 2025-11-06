#!/usr/bin/envs python3
'''
This script contains a function that uses a generator to
fetch rows one by one from the user_data table.
Prototype:
- def stream_users() :- generator function that yields one row at a time from the user_data table
'''
import sys
try:
    import pymysql
except ImportError:
    print("PyMySQL is not installed. Please run:")
    print("   pip install PyMySQL")
    sys.exit(1)

def stream_users():
    """
    Generator function that yields one row at a time from the user_data table.
    """
    try:
        connection = pymysql.connect(
            host="localhost",
            user="user",
            password="password",
            database="ALX_prodev",
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user_data;")
            for row in cursor:
                yield row
    except pymysql.MySQLError as e:
        print(f"Error fetching data from user_data: {e}")
    finally:
        if connection:
            connection.close()