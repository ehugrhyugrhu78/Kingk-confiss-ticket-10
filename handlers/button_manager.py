from database.db import connect_db



async def save_custom_button(
    text,
    action
):

    async with await connect_db() as db:

        await db.execute(
            """
            INSERT INTO buttons
            (text,action)
            VALUES(?,?)
            """,
            (
                text,
                action
            )
        )

        await db.commit()
