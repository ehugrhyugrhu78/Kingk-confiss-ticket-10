from telegram import Update
from telegram.ext import ContextTypes

from core.stickers import set_sticker


async def save_sticker(
    update:Update,
    context:ContextTypes.DEFAULT_TYPE
):

    name = context.user_data.get(
        "sticker_name"
    )

    if update.message.sticker:

        await set_sticker(
            name,
            update.message.sticker.file_id
        )


        await update.message.reply_text(
            "🎭 استیکر ذخیره شد"
        )
