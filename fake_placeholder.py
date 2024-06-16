import asyncio
import aiosqlite
from faker import Faker

fake = Faker('ru')

async def made_to_db():
    async with aiosqlite.connect('db/users.db') as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
        userid INT,
        name TEXT,
        emal TEXT,
        date TEXT);
        """)
        await db.commit()


async def save_to_db():
    for i in range(1, 1000):
        user = [
        fake.random_int(),
        fake.name(),
        fake.email(),
        fake.date() + ' : ' + fake.time(),
    ]
    async with aiosqlite.connect('db/users.db') as db:
        await db.execute("""
        INSERT INTO users VALUES(?, ?, ?, ?);
        """, user)
        await db.commit()

async def load_to_db():
    async with aiosqlite.connect('db/users.db') as db:
        async with db.execute("SELECT * FROM users") as cursor:
            r = await cursor.fetchall()
            print(r)
            await cursor.close()
        
        
            




async def main():
    task1 = asyncio.create_task(made_to_db())
    task2 = asyncio.create_task(save_to_db())
    task3 = asyncio.create_task(load_to_db())

    await task1
    await task2
    await task3


if __name__ == '__main__':
    asyncio.run(main())
