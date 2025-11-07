#!/usr/bin/envs python3
'''
This script, implements a generator stream_user_ages() that yields user ages one by one.
'''
connect_to_prodev = __import__('seed').connect_to_prodev
stream_users = __import__('0-stream_users').stream_users

def stream_user_ages():
    """
    Generator that yields user ages one by one.
    """
    connection = connect_to_prodev()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT age FROM user_data")
            for row in cursor.fetchall():
                yield row.get('age')
    finally:
        connection.close()

if __name__ == "__main__":
    count = total = 0
    for a in stream_user_ages():
        total += a
        count += 1
    avg = total / count if count else None
    print(f"Average age of users: {avg}")
