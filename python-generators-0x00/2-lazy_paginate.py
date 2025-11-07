#!/usr/bin/envs python3
'''
This script:
'''
seed = __import__('seed')


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """
    Generator that yields pages of users lazily.
    Each page contains 'page_size' number of users.
    """
    try:
        offset = 0
        while True:
            rows = paginate_users(page_size, offset)
            if not rows:
                break
            yield rows
            offset += page_size
    except Exception as e:
        print(f"An error occurred during pagination: {e}")