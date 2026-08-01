from telegram import Update
from telegram.ext import ContextTypes

from states.states import TicketState
from database.db import connect_db


async def create_ticket_start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    await query.message.reply_text(
        "🎟 لطفاً عنوان تیکت خود را ارسال کنید:"
    )


    return TicketState.TITLE



async def receive_title(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["title"] = update.message.text


    await update.message.reply_text(
        "💬 حالا مشکل یا درخواست خود را ارسال کنید:"
    )


    return TicketState.MESSAGE



async def receive_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    context.user_data["message"] = update.message.text


    await update.message.reply_text(
        "✅ تیکت آماده ارسال است.\n\nارسال شود؟"
    )


    return TicketState.CONFIRM
