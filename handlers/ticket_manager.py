from telegram import Update
from telegram.ext import ContextTypes

from database.db import connect_db


async def save_ticket(user_id, title, message):

    async with await connect_db() as db:

        cursor = await db.execute(
            """
            INSERT INTO tickets
            (user_id,title,status,created_at)
            VALUES(?,?,?,datetime('now'))
            """,
            (
                user_id,
                title,
                "open"
            )
        )

        ticket_id = cursor.lastrowid


        await db.execute(
            """
            INSERT INTO ticket_messages
            (ticket_id,sender_id,sender_type,message_type,content,created_at)
            VALUES(?,?,?,?,?,datetime('now'))
            """,
            (
                ticket_id,
                user_id,
                "user",
                "text",
                message
            )
        )


        await db.commit()


    return ticket_id
