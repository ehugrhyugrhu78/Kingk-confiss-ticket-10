from database.db import connect_db


async def get_message(key, default=""):

    async with await connect_db() as db:

        cursor = await db.execute(
            "SELECT text FROM messages WHERE key=?",
            (key,)
        )

        result = await cursor.fetchone()

        if result:
            return result[0]

    return default



async def set_message(key, text):

    async with await connect_db() as db:

        await db.execute(
            """
            INSERT INTO messages(key,text)
            VALUES(?,?)
            ON CONFLICT(key)
            DO UPDATE SET text=excluded.text
            """,
            (
                key,
                text
            )
        )

        await db.commit()
