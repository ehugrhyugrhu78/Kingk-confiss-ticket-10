from database.db import connect_db


async def save_log(action):

    async with await connect_db() as db:

        await db.execute(
            """
            INSERT INTO logs(action)
            VALUES(?)
            """,
            (action,)
        )

        await db.commit()
