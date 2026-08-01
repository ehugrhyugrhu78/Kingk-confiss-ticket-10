from database.db import connect_db


async def get_sticker(name):

    async with await connect_db() as db:

        cursor = await db.execute(
            "SELECT file_id FROM stickers WHERE name=?",
            (name,)
        )

        result = await cursor.fetchone()

        if result:
            return result[0]

    return None



async def set_sticker(name, file_id):

    async with await connect_db() as db:

        await db.execute(
            """
            INSERT INTO stickers(name,file_id)
            VALUES(?,?)
            ON CONFLICT(name)
            DO UPDATE SET file_id=excluded.file_id
            """,
            (
                name,
                file_id
            )
        )

        await db.commit()



async def delete_sticker(name):

    async with await connect_db() as db:

        await db.execute(
            "DELETE FROM stickers WHERE name=?",
            (name,)
        )

        await db.commit()
