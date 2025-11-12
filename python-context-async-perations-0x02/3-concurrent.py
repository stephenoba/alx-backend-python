#!/usr/bin/env python3
"""
contains two asynchronous functions: async_fetch_users() and
async_fetch_older_users() that fetches all users and users older than 40 respectively.
"""
import asyncio
import aiosqlite

async def async_fetch_users():
    async with aiosqlite.connect('users.db') as conn:
        cursor = await conn.execute("SELECT * FROM users")
        results = await cursor.fetchall()
        await cursor.close()
        return results
    
async def async_fetch_older_users(age_threshold):
    async with aiosqlite.connect('users.db') as conn:
        cursor = await conn.execute("SELECT * FROM users WHERE age > ?", (age_threshold,))
        results = await cursor.fetchall()
        await cursor.close()
        return results
    
async def fetch_concurrently():
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users(40)
    )
    all_users, older_users = results
    print("All Users:")
    for user in all_users:
        print(user)
    print("\nUsers older than 40:")
    for user in older_users:
        print(user)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())

