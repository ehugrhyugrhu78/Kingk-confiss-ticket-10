from telegram import Update
from telegram.ext import ContextTypes

from database.db import connect_db



async def toggle_bot(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    async with await connect_db() as db:

        await db.execute(
            """
            INSERT INTO settings(key,value)
            VALUES('status','off')
            ON CONFLICT(key)
            DO UPDATE SET value='off'
            """
        )

        await db.commit()


    await query.edit_message_text(
        "❌ ربات خاموش شد"
    )
