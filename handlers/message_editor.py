from telegram import Update
from telegram.ext import ContextTypes

from core.messages import set_message


async def save_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    key = context.user_data.get(
        "edit_key"
    )

    if not key:
        return


    await set_message(
        key,
        update.message.text
    )


    await update.message.reply_text(
        "✅ پیام با موفقیت تغییر کرد"
    )


    context.user_data.clear()
