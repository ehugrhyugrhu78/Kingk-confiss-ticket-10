from telegram import Update
from telegram.ext import ContextTypes

from database.tickets import get_tickets



async def show_tickets(
    update:Update,
    context:ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    tickets = await get_tickets(
        limit=5
    )


    text = "🎟 لیست تیکت‌ها:\n\n"


    for ticket in tickets:

        text += (
            f"#{ticket[0]} | "
            f"کاربر {ticket[1]} | "
            f"{ticket[3]}\n"
        )


    await query.edit_message_text(
        text
    )
