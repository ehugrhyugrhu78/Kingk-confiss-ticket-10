from database.db import connect_db



async def get_tickets(
    status=None,
    limit=5,
    offset=0
):

    async with await connect_db() as db:

        if status:

            cursor = await db.execute(
                """
                SELECT *
                FROM tickets
                WHERE status=?
                ORDER BY id DESC
                LIMIT ? OFFSET ?
                """,
                (
                    status,
                    limit,
                    offset
                )
            )

        else:

            cursor = await db.execute(
                """
                SELECT *
                FROM tickets
                ORDER BY id DESC
                LIMIT ? OFFSET ?
                """,
                (
                    limit,
                    offset
                )
            )


        return await cursor.fetchall()



async def change_status(ticket_id,status):

    async with await connect_db() as db:

        await db.execute(
            """
            UPDATE tickets
            SET status=?
            WHERE id=?
            """,
            (
                status,
                ticket_id
            )
        )

        await db.commit()
