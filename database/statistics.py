from database.db import connect_db



async def count_users():

    async with await connect_db() as db:

        cursor = await db.execute(
            "SELECT COUNT(*) FROM users"
        )

        return (
            await cursor.fetchone()
        )[0]
