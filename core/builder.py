from database.db import connect_db


async def get_buttons():

    async with await connect_db() as db:

        cursor = await db.execute(
            """
            SELECT text, action
            FROM buttons
            WHERE enabled=1
            ORDER BY position ASC
            """
        )

        return await cursor.fetchall()



async def add_button(text, action, position=0):

    async with await connect_db() as db:

        await db.execute(
            """
            INSERT INTO buttons
            (text,action,position)
            VALUES(?,?,?)
            """,
            (
                text,
                action,
                position
            )
        )

        await db.commit()



async def delete_button(button_id):

    async with await connect_db() as db:

        await db.execute(
            "DELETE FROM buttons WHERE id=?",
            (button_id,)
        )

        await db.commit()
