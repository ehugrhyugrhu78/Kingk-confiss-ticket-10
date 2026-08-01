from database.db import connect_db



async def get_users():

    async with await connect_db() as db:

        cursor = await db.execute(
            "SELECT * FROM users"
        )

        return await cursor.fetchall()
