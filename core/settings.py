from database.db import connect_db



async def get_setting(key):

    async with await connect_db() as db:

        cursor = await db.execute(
            "SELECT value FROM settings WHERE key=?",
            (key,)
        )

        row = await cursor.fetchone()


        return row[0] if row else None



async def set_setting(key,value):

    async with await connect_db() as db:

        await db.execute(
            """
            INSERT INTO settings
            VALUES(?,?)
            ON CONFLICT(key)
            DO UPDATE SET value=excluded.value
            """,
            (
                key,
                value
            )
        )

        await db.commit()
