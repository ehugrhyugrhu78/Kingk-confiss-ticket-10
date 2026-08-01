from database.db import connect_db



async def get_admin_tickets(
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



async def ticket_count(status=None):

    async with await connect_db() as db:

        if status:

            cursor = await db.execute(
                "SELECT COUNT(*) FROM tickets WHERE status=?",
                (status,)
            )

        else:

            cursor = await db.execute(
                "SELECT COUNT(*) FROM tickets"
            )


        return (
            await cursor.fetchone()
        )[0]
