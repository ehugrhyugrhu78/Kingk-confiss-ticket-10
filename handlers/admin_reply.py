from telegram import Update
from telegram.ext import ContextTypes

from database.db import add_message



async def start_reply(
    update:Update,
    context:ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    ticket_id = int(
        query.data.split("_")[-1]
    )


    context.user_data["reply_ticket"] = ticket_id


    await query.message.reply_text(
        "💬 پیام پاسخ را ارسال کنید:"
    )



async def save_reply(
    update:Update,
    context:ContextTypes.DEFAULT_TYPE
):

    ticket_id = context.user_data.get(
        "reply_ticket"
    )


    if not ticket_id:
        return


    await add_message(
        ticket_id,
        update.effective_user.id,
        "admin",
        "text",
        update.message.text
    )


    await update.message.reply_text(
        "✅ پاسخ ارسال شد"
    )


    context.user_data.clear()
