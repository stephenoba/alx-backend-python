#!/usr/bin/envs python3
'''
This script:
- Set up the MySQL database, ALX_prodev with the table user_data with the following fields:
-- user_id(Primary Key, UUID, Indexed)
-- name (VARCHAR, NOT NULL)
-- email (VARCHAR, NOT NULL)
-- age (DECIMAL,NOT NULL)
- Populate the database with the sample data from this user_data.csv

Prototypes:
- def connect_db() :- connects to the mysql database server
- def create_database(connection):- creates the database ALX_prodev if it does not exist
- def connect_to_prodev() connects the the ALX_prodev database in MYSQL
- def create_table(connection):- creates a table user_data if it does not exists with the required fields
- def insert_data(connection, data):- inserts data in the database if it does not exist
'''
import sys

try:
    import pymysql
except ImportError:
    print("PyMySQL is not installed. Please run:")
    print("   pip install PyMySQL")
    sys.exit(1)

def connect_db():
    """
    Connects to the MySQL server using PyMySQL (without specifying a database)
    and returns the connection object.
    """
    try:
        connection = pymysql.connect(
            host="localhost",
            user="user",
            password="password",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Successfully connected to MySQL server using PyMySQL")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def create_database(connection):
    """
    Creates the database 'ALX_prodev' if it does not already exist.

    :param connection: Active MySQL connection from PyMYSQL
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
            print("Database ALX_prodev is ready.")
    except pymysql.MySQLError as e:
        print(f"Failed to create database, ALX_prodev: {e}")


def connect_to_prodev():
    """
    Connects directly to the 'ALX_prodev' database in MySQL.
    Returns the connection object if successfule, otherwise None.
    """
    try:
        connection = pymysql.connect(
            host="localhost",
            user="developer",
            password="2x+2y=26XY",
            database="ALX_prodev",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Successfully connected to the 'ALX_prodev' database")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to 'ALX_prodev': {e}")
        return None


def create_table(connection):
    """
    Create the user_data table if it does not exist with the required fields.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS user_data (
                    user_id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    age DECIMAL(3, 0) NOT NULL
                );
                """
            )
            print("Table 'user_data' is ready.")
    except pymysql.MySQLError as e:
        print(f"Failed to create table user_data: {e}")


def insert_data(connection, data):
    """
    Inserts data into the user_data table if it does not already exist.

    :param connection: Active MySQL connection from PyMYSQL
    :param data: CSV file containing user data (name, email, age)
    """
    # read data from CSV file
    import csv
    try:
        with open(data, mode='r') as file:
            csv_reader = csv.DictReader(file)
            with connection.cursor() as cursor:
                for row in csv_reader:
                    cursor.execute(
                        """
                        INSERT INTO user_data (name, email, age)
                        VALUES (%s, %s, %s)
                        ON DUPLICATE KEY UPDATE name=name;
                        """,
                        (row['name'], row['email'], row['age'])
                    )
            connection.commit()
            print("Data inserted successfully into user_data table.")
    except FileNotFoundError:
        print(f"CSV file {data} not found.")
    except pymysql.MySQLError as e:
        print(f"Failed to insert data into user_data: {e}")
