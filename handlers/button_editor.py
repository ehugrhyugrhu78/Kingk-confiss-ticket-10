from telegram import Update
from telegram.ext import ContextTypes

from core.builder import add_button



async def create_button(
    update:Update,
    context:ContextTypes.DEFAULT_TYPE
):

    text = context.user_data.get(
        "button_text"
    )

    action = context.user_data.get(
        "button_action"
    )


    await add_button(
        text,
        action
    )


    await update.message.reply_text(
        "✅ دکمه ساخته شد"
    )
