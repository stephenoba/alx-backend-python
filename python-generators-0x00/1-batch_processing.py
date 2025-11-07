#!/usr/bin/envs python3
'''
This script contains a function that fetches rows in batches and
processes each batch to filter users over the age of 25

Prototype:
- stream_users_in_batches(batch_size)
- batch_processing(batch_size)
'''
connect_to_prodev = __import__('seed').connect_to_prodev
stream_users = __import__('0-stream_users').stream_users

def stream_users_in_batches(batch_size):
    """
    Generator that fetches users in batches using LIMIT/OFFSET.
    """
    connection = connect_to_prodev()
    try:
        offset = 0
        batch_size = int(batch_size)
        while True:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT user_id, name, email, age FROM user_data LIMIT %s OFFSET %s",
                    (batch_size, offset)
                )
                rows = cursor.fetchall()
            if not rows:
                break
            sent = (yield rows)
            # handle .send() input to adjust offset
            if isinstance(sent, int):
                offset += sent
            else:
                offset += batch_size
    finally:
        connection.close()

def batch_processing(batch_size):
    """
    Processes each batch to yield users over age 25.
    """
    gen = stream_users_in_batches(batch_size)
    for batch in gen:
        for user in batch:
            if user.get('age', 0) > 25:
                print(user)