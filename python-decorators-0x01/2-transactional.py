import sqlite3 
import functools

def with_db_connection(func):
    @functools.wraps(func) 
    def wrapper(*args, **kwargs): 
        conn = sqlite3.connect('users.db') 
        try: 
            result = func(conn, *args, **kwargs) 
            return result 
        finally: 
            conn.close() 
    return wrapper 

def transactional(func):
    """
    ensures a function running a database operation is wrapped inside a transaction.
    If the function raises an error, rollback; otherwise commit the transaction.
    """
    @functools.wraps(func) 
    def wrapper(conn, *args, **kwargs): 
        try: 
            result = func(conn, *args, **kwargs) 
            conn.commit() 
            return result 
        except Exception as e: 
            conn.rollback() 
            raise e 
    return wrapper

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute(f"UPDATE users SET email = {new_email} WHERE id = {user_id}") 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')